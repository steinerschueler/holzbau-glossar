"""MkDocs-Hook: bindet die per ``sync.sh`` gespiegelten Hauptglossar- und
Subglossar-Dateien als virtuelle Site-Seiten ein.

Liest ``content/hauptglossar/<cluster>/hg_*.md`` und
``content/subglossar/sg_*.md`` und erzeugt pro Hauptglossar-Eintrag
eine zusammengeführte Seite (HG oben, SG-Pendant darunter — falls
``glossar_ref:`` matcht). Cluster-Ordner werden zu Top-Navigations-
Bereichen.

Falls ``content/`` fehlt (Build ohne vorherigen Sync), passiert nichts —
der Hook degradiert still und das Skelett-Setup bleibt funktional."""

from __future__ import annotations

import json
import re
import unicodedata
from pathlib import Path

import yaml
from mkdocs.structure.files import File
from mkdocs.structure.nav import Section, Link

# API-Version. Major-Bump nur bei Schema-Brüchen; neue Felder sind kein
# Bruch. Apps und Konsumenten pinnen über den Pfad-Prefix /api/v1/.
API_VERSION = "1"
# Lizenz-URL für die Inhalts-Antworten der API.
API_LICENSE = "https://creativecommons.org/licenses/by/4.0/"
# Concept-DOI als stabile Quell-Referenz im _meta-Block.
API_CONCEPT_DOI = "10.5281/zenodo.20435319"

# Cluster-Ordner-Name → Anzeige-Label.
CLUSTERS: dict[str, str] = {
    "00_ressourcen": "Ressourcen",
    "10_kern": "Kern",
    "20_tragwerk": "Tragwerk",
    "30_holzbau": "Holzbau",
}

# Cluster-Ordner-Name → URL-Segment (lesbar, ohne Zahlen-Präfix).
CLUSTER_URL: dict[str, str] = {
    "00_ressourcen": "ressourcen",
    "10_kern": "kern",
    "20_tragwerk": "tragwerk",
    "30_holzbau": "holzbau",
}

# Cluster-Ordner-Name → 1-Buchstabe-Kürzel für den A-Z-Index.
CLUSTER_KURZ: dict[str, str] = {
    "00_ressourcen": "R",
    "10_kern": "K",
    "20_tragwerk": "T",
    "30_holzbau": "H",
}


def on_config(config):
    """Inject build_date into config.extra so the head template can use
    it as citation_publication_date / DC.date."""
    from datetime import date

    if "extra" not in config or config["extra"] is None:
        config["extra"] = {}
    config["extra"]["build_date"] = date.today().isoformat()
    return config


def on_files(files, config):
    """Append virtual files for every Hauptglossar entry, with optional
    Subglossar appendix. Records the per-cluster id list on ``config``
    for ``on_nav`` to consume."""

    content = Path(config["docs_dir"]).parent / "content"
    if not content.is_dir():
        # Sync wurde noch nicht ausgeführt — Build läuft mit reinem Skelett.
        return files

    sg_by_id = _load_subglossar_index(content / "subglossar")
    cluster_entries: dict[str, list[tuple[str, str]]] = {}
    # Flache Sammlung für den A-Z-Index: (benennung, virtual_uri, cluster_kurz).
    az_entries: list[tuple[str, str, str]] = []

    for cluster_dir, label in CLUSTERS.items():
        cluster_path = content / "hauptglossar" / cluster_dir
        if not cluster_path.is_dir():
            continue
        kurz = CLUSTER_KURZ[cluster_dir]
        entries: list[tuple[str, str]] = []
        for hg_file in sorted(cluster_path.glob("hg_*.md")):
            hg_id = hg_file.stem.removeprefix("hg_")
            hg_text = hg_file.read_text(encoding="utf-8")
            benennung = _extract_benennung(hg_text) or hg_id
            # Prosa-Auszug ins Frontmatter heben, damit das Jinja2-Head-
            # Template ihn als page.meta.prosa_excerpt für JSON-LD nutzen
            # kann. Modifikation greift nur in die virtuelle Site-Datei,
            # nicht ins Quell-Markdown unter content/.
            excerpt = _extract_prosa_excerpt(hg_text)
            if excerpt:
                hg_text = _inject_prosa_excerpt(hg_text, excerpt)
            merged = _merge_entry(hg_text, sg_by_id.get(hg_id), hg_id)
            virtual_uri = f"{CLUSTER_URL[cluster_dir]}/{hg_id}.md"
            files.append(File.generated(config, virtual_uri, content=merged))
            entries.append((benennung, virtual_uri))
            az_entries.append((benennung, virtual_uri, kurz))
        cluster_entries[label] = entries

    # A-Z-Index als eigene virtuelle Seite anlegen.
    if az_entries:
        az_md = _build_az_index(az_entries)
        files.append(File.generated(config, "index-az.md", content=az_md))
        config["_holzbau_az_uri"] = "index-az.md"

    # Stash for on_nav.
    config["_holzbau_cluster_entries"] = cluster_entries
    return files


def on_post_build(config):
    """Write ``.md``, ``.txt`` and ``.bib`` variants of each entry next
    to its rendered HTML page, plus the static JSON-API v1 under
    ``api/v1/``."""

    from datetime import date
    from pathlib import Path

    site_dir = Path(config["site_dir"])
    content = Path(config["docs_dir"]).parent / "content"
    if not content.is_dir():
        return

    sg_by_id = _load_subglossar_index(content / "subglossar")
    today = date.today().isoformat()
    site_url = (config.get("site_url") or "https://holzbau-glossar.ch").rstrip("/")
    site_author = config.get("site_author", "Eric Naville")

    for cluster_dir, _label in CLUSTERS.items():
        cluster_path = content / "hauptglossar" / cluster_dir
        if not cluster_path.is_dir():
            continue
        cluster_url = CLUSTER_URL[cluster_dir]
        out_dir = site_dir / cluster_url
        out_dir.mkdir(parents=True, exist_ok=True)

        for hg_file in sorted(cluster_path.glob("hg_*.md")):
            hg_id = hg_file.stem.removeprefix("hg_")
            hg_text = hg_file.read_text(encoding="utf-8")
            benennung = _extract_benennung(hg_text) or hg_id
            merged_md = _merge_for_download(hg_text, sg_by_id.get(hg_id))

            (out_dir / f"{hg_id}.md").write_text(merged_md, encoding="utf-8")
            (out_dir / f"{hg_id}.txt").write_text(
                _markdown_to_plain(merged_md), encoding="utf-8"
            )
            (out_dir / f"{hg_id}.bib").write_text(
                _build_bibtex(
                    hg_id=hg_id,
                    title=benennung,
                    author=site_author,
                    url=f"{site_url}/{cluster_url}/{hg_id}/",
                    date_iso=today,
                ),
                encoding="utf-8",
            )

    # JSON-API v1 — index, eintraege/<id>, graph, schema.
    _write_api_v1(content, site_dir, site_url)


def _build_bibtex(hg_id: str, title: str, author: str, url: str, date_iso: str) -> str:
    """Render a minimal but well-formed BibTeX @misc entry. The concept
    DOI (10.5281/zenodo.20435319) points to the latest version; the
    note carries the project context. Per-version DOIs aren't tracked
    per entry — the whole Glossar is the citable unit on Zenodo.

    Persönliche Autoren (Klassische Form ``Vorname Nachname``) werden
    zu BibTeX-konformer ``Nachname, Vorname``-Form umgeschrieben.
    Organisations-/Site-Autoren (z. B. ``holzbau-glossar.ch``) werden
    in doppelte geschweifte Klammern eingewickelt, damit BibTeX sie
    nicht als Person zerlegt."""
    year = date_iso[:4]
    is_organization = "," not in author and " " not in author
    if is_organization:
        # ``{{...}}`` schützt den Token vor BibTeX-Name-Parsing.
        author_bib = "{" + author + "}"
    elif "," not in author and " " in author:
        first, last = author.rsplit(" ", 1)
        author_bib = f"{last}, {first}"
    else:
        author_bib = author
    return (
        f"@misc{{holzbau-glossar:{hg_id},\n"
        f"  title     = {{{title}}},\n"
        f"  author    = {{{author_bib}}},\n"
        f"  year      = {{{year}}},\n"
        f"  publisher = {{holzbau-glossar.ch}},\n"
        f"  doi       = {{10.5281/zenodo.20435319}},\n"
        f"  url       = {{{url}}},\n"
        f"  urldate   = {{{date_iso}}},\n"
        f"  note      = {{Hauptglossar-Eintrag, CC BY 4.0}}\n"
        f"}}\n"
    )


def on_nav(nav, config, files):
    """Insert the A-Z-Index plus the four cluster sections directly after
    the „Zitieren"-Item, so that Impressum/Datenschutz (in der
    ``mkdocs.yml`` darunter eingetragen) als Pflicht-Anhang am Ende
    der Nav stehen bleiben. Fallback: ans Ende anhängen, falls
    „Zitieren" umbenannt oder entfernt wird."""
    cluster_entries = config.pop("_holzbau_cluster_entries", {})
    az_uri = config.pop("_holzbau_az_uri", None)
    if not cluster_entries:
        return nav

    new_items: list = []

    if az_uri:
        az_file = files.get_file_from_path(az_uri)
        if az_file is not None and az_file.page is not None:
            az_file.page.title = "A–Z-Index"
            new_items.append(az_file.page)

    for label, entries in cluster_entries.items():
        section_children = []
        for benennung, uri in entries:
            file = files.get_file_from_path(uri)
            if file is None:
                continue
            page = file.page
            if page is None:
                continue
            page.title = benennung
            section_children.append(page)
        section = Section(label, section_children)
        for child in section_children:
            child.parent = section
        new_items.append(section)

    # Einfügepunkt: vor dem ersten „Trailing-Static"-Item — die
    # statischen Seiten DOI (Zitieren), API, Impressum, Datenschutz
    # sollen sichtbar UNTER den Clustern hängen. Ohne Treffer (z.B.
    # wenn die Seiten umbenannt wurden) am Ende anhängen — defensives
    # Default-Verhalten.
    TRAILING_TITLES = {"DOI (Zitieren)", "API (Einbinden)", "Impressum", "Datenschutz"}
    insert_at = len(nav.items)
    for idx, item in enumerate(nav.items):
        if getattr(item, "title", None) in TRAILING_TITLES:
            insert_at = idx
            break

    nav.items[insert_at:insert_at] = new_items

    return nav


# ---------------------------------------------------------------------------
# Subglossar-Index
# ---------------------------------------------------------------------------

_GLOSSAR_REF_RE = re.compile(r"^glossar_ref:\s*(\S+)\s*$", re.MULTILINE)
_BENENNUNG_RE = re.compile(r"^benennung:\s*(.+?)\s*$", re.MULTILINE)


def _extract_benennung(text: str) -> str | None:
    """Pull ``benennung:`` out of the leading YAML frontmatter."""
    if not text.startswith("---"):
        return None
    end = text.find("---", 3)
    if end == -1:
        return None
    match = _BENENNUNG_RE.search(text[3:end])
    if not match:
        return None
    # Strip surrounding quotes if present.
    raw = match.group(1)
    return raw.strip("\"'")


def _load_subglossar_index(sg_dir: Path) -> dict[str, str]:
    """Map every Subglossar entry to its referenced Hauptglossar id."""
    if not sg_dir.is_dir():
        return {}
    index: dict[str, str] = {}
    for sg_file in sg_dir.glob("sg_*.md"):
        text = sg_file.read_text(encoding="utf-8")
        ref = _extract_glossar_ref(text)
        if ref:
            index[ref] = text
    return index


def _extract_glossar_ref(text: str) -> str | None:
    """Pull ``glossar_ref:`` out of the leading YAML frontmatter."""
    if not text.startswith("---"):
        return None
    end = text.find("---", 3)
    if end == -1:
        return None
    match = _GLOSSAR_REF_RE.search(text[3:end])
    return match.group(1) if match else None


# ---------------------------------------------------------------------------
# Prosa-Auszug für JSON-LD schema.org/DefinedTerm
# ---------------------------------------------------------------------------

_PROSA_SECTION_RE = re.compile(
    r"^##\s+Prosa-Definition\s*$(?P<body>.*?)(?=^##\s|\Z)",
    re.MULTILINE | re.DOTALL,
)
# Markdown-Inline-Markup, das im Plain-Text-Auszug stört.
_MD_INLINE_CODE = re.compile(r"`([^`\n]+?)`")
_MD_INLINE_LINK = re.compile(r"\[([^\]]+)\]\([^)]+\)")
_MD_INLINE_BOLD = re.compile(r"\*\*([^*\n]+?)\*\*")
_MD_INLINE_ITALIC = re.compile(r"(?<!\*)\*([^*\n]+?)\*(?!\*)")
_PROSA_EXCERPT_MAX = 320


def _extract_prosa_excerpt(text: str) -> str | None:
    """Extrahiere den ersten Absatz der ``## Prosa-Definition``-Sektion
    als Plain-Text-Auszug für JSON-LD ``description``. Markdown-Inline-
    Markup wird entfernt; Länge auf ``_PROSA_EXCERPT_MAX`` begrenzt
    (an Wortgrenze gekürzt). Liefert ``None``, wenn die Sektion fehlt
    oder leer ist."""
    body_match = _PROSA_SECTION_RE.search(text)
    if not body_match:
        return None
    body = body_match.group("body").strip()
    if not body:
        return None
    # Erster Absatz = bis zur ersten Leerzeile.
    first_para = re.split(r"\n\s*\n", body, maxsplit=1)[0].strip()
    if not first_para:
        return None
    # Erst Whitespace (inkl. Zeilenumbrüche) zusammenfalten, dann
    # Markdown-Inline-Markup neutralisieren. Quell-Markdowns haben Bold-
    # Markup gelegentlich über Zeilenumbrüche hinweg (`**foo\nbar**`),
    # die Regexe matchen aber nur innerhalb einer Zeile.
    plain = re.sub(r"\s+", " ", first_para).strip()
    plain = _MD_INLINE_LINK.sub(r"\1", plain)
    plain = _MD_INLINE_BOLD.sub(r"\1", plain)
    plain = _MD_INLINE_ITALIC.sub(r"\1", plain)
    plain = _MD_INLINE_CODE.sub(r"\1", plain)
    if len(plain) <= _PROSA_EXCERPT_MAX:
        return plain
    # An Wortgrenze kürzen.
    truncated = plain[:_PROSA_EXCERPT_MAX].rsplit(" ", 1)[0]
    return truncated + "…"


def _inject_prosa_excerpt(text: str, excerpt: str) -> str:
    """Füge ein ``prosa_excerpt:``-Feld in den YAML-Frontmatter-Block
    ein, damit die Jinja2-Template-Schicht es als ``page.meta.prosa_excerpt``
    lesen kann. Wenn das Feld bereits existiert, bleibt der Text
    unverändert."""
    if not text.startswith("---"):
        return text
    end = text.find("---", 3)
    if end == -1:
        return text
    front = text[3:end]
    if re.search(r"^prosa_excerpt:", front, re.MULTILINE):
        return text
    # YAML-Block-Skalar mit doppelten Anführungszeichen; Backslash und
    # eingebettete Quotes escapen.
    escaped = excerpt.replace("\\", "\\\\").replace('"', '\\"')
    new_front = front.rstrip() + f'\nprosa_excerpt: "{escaped}"\n'
    return "---" + new_front + text[end:]


# ---------------------------------------------------------------------------
# Verschränkung HG + SG
# ---------------------------------------------------------------------------


def _merge_entry(hg_text: str, sg_text: str | None, hg_id: str) -> str:
    """Concatenate Hauptglossar content with (optional) Subglossar body,
    rewriting cross-links so MkDocs resolves them against the rendered
    site structure. Appends download buttons for the .md / .txt / .bib
    variants generated in ``on_post_build``."""
    merged_hg = _rewrite_cross_links(hg_text)
    if sg_text:
        sg_body = _rewrite_cross_links(_strip_frontmatter(sg_text).lstrip())
        merged = (
            merged_hg.rstrip()
            + "\n\n"
            + "## Didaktische Hülle (Subglossar)\n\n"
            + sg_body
        )
    else:
        merged = merged_hg

    # Inline-HTML (statt Markdown-Link-Syntax), damit MkDocs keine
    # toten Cross-Link-Warnings für die per ``on_post_build`` erzeugten
    # .md/.txt/.bib-Assets wirft.
    downloads = (
        "\n\n---\n\n"
        "## Quelle herunterladen\n\n"
        '<p class="download-row">'
        f'<a class="download-btn" href="{hg_id}.md" download>Markdown</a>'
        f'<a class="download-btn" href="{hg_id}.txt" download>Plain Text</a>'
        f'<a class="download-btn" href="{hg_id}.bib" download>BibTeX</a>'
        "</p>\n"
    )
    return merged.rstrip() + downloads


# ---------------------------------------------------------------------------
# Cross-Link-Umschreibung
# ---------------------------------------------------------------------------
#
# Die Quell-Markdowns verlinken Geschwister-Einträge so:
#   1. Selbe Cluster (HG):       [..](hg_punkt.md)
#   2. Andere Cluster (HG):      [..](../00_ressourcen/hg_punkt.md)
#   3. Aus SG-Kontext zu HG:     [..](hauptglossar/00_ressourcen/hg_punkt.md)
#                                oder (../../hauptglossar/...)
#
# Im gerenderten Site liegt jeder Eintrag unter
# ``/{cluster_url}/{id}/``. Wir schreiben deshalb auf Markdown-Pfade
# um, die MkDocs gegen das jeweilige Ausgabe-Verzeichnis auflöst —
# das vermeidet Hartcodierung der ``site_url`` und respektiert
# ``use_directory_urls``.

def _merge_for_download(hg_text: str, sg_text: str | None) -> str:
    """Merged Markdown for direct download — HG with intact frontmatter,
    SG body appended. Cross-links remain as in the source so the result
    is a faithful citation snapshot."""
    if not sg_text:
        return hg_text
    sg_body = _strip_frontmatter(sg_text).lstrip()
    return (
        hg_text.rstrip()
        + "\n\n"
        + "## Didaktische Hülle (Subglossar)\n\n"
        + sg_body
    )


# Markdown → readable plain text. Conservative: keeps frontmatter,
# strips headers/emphasis/inline code, collapses links to "text (url)".
_MD_HEADER = re.compile(r"^#+\s*", re.MULTILINE)
_MD_EMPH_DOUBLE = re.compile(r"\*\*([^*\n]+?)\*\*")
_MD_EMPH_SINGLE = re.compile(r"\*([^*\n]+?)\*")
_MD_UNDER_DOUBLE = re.compile(r"__([^_\n]+?)__")
_MD_UNDER_SINGLE = re.compile(r"_([^_\n]+?)_")
_MD_LINK = re.compile(r"\[([^\]]+)\]\(([^)]+)\)")
_MD_CODE_INLINE = re.compile(r"`([^`\n]+?)`")


def _markdown_to_plain(text: str) -> str:
    text = _MD_LINK.sub(r"\1 (\2)", text)
    text = _MD_HEADER.sub("", text)
    text = _MD_EMPH_DOUBLE.sub(r"\1", text)
    text = _MD_EMPH_SINGLE.sub(r"\1", text)
    text = _MD_UNDER_DOUBLE.sub(r"\1", text)
    text = _MD_UNDER_SINGLE.sub(r"\1", text)
    text = _MD_CODE_INLINE.sub(r"\1", text)
    return text


# ---------------------------------------------------------------------------
# A-Z-Index
# ---------------------------------------------------------------------------


def _az_sort_key(benennung: str) -> tuple[str, str]:
    """Umlaut-bewusste Sortier-Schlüssel: 'Ä' → 'a', 'ß' → 'ss', Akzente
    fallen weg. Standard-NFKD-Zerlegung deckt alle DACH-Umlaute zuverlässig
    ab, ohne Locale-Setup auf dem Build-Runner."""
    base = unicodedata.normalize("NFKD", benennung).encode("ascii", "ignore").decode()
    folded = benennung.replace("ß", "ss").replace("ẞ", "Ss")
    folded_base = (
        unicodedata.normalize("NFKD", folded)
        .encode("ascii", "ignore")
        .decode()
    )
    return (folded_base.casefold(), benennung.casefold())


def _az_initial(benennung: str) -> str:
    """Anfangsbuchstabe für die Gruppierung — Umlaute auf den lateinischen
    Basisbuchstaben zurückgeführt, Ziffern und Sonderzeichen in „#"."""
    if not benennung:
        return "#"
    first = unicodedata.normalize("NFKD", benennung[0])
    for ch in first:
        if ch.isalpha():
            return ch.upper()
    return "#"


def _build_az_index(entries: list[tuple[str, str, str]]) -> str:
    """Erzeuge das Markdown für /index-az/. Eintragsformat:
    ``- [Benennung](uri) · K`` — Kürzel zeigt den Cluster (R/K/T/H)."""
    sorted_entries = sorted(entries, key=lambda e: _az_sort_key(e[0]))

    lines: list[str] = [
        "---",
        "title: A–Z-Index",
        "---",
        "",
        "# A–Z-Index",
        "",
        "Alle Hauptglossar-Einträge alphabetisch, clusterübergreifend. Das",
        "Kürzel rechts kennzeichnet den Cluster: **R** Ressourcen · **K**",
        "Kern · **T** Tragwerk · **H** Holzbau.",
        "",
    ]

    current_initial = ""
    for benennung, uri, kurz in sorted_entries:
        initial = _az_initial(benennung)
        if initial != current_initial:
            current_initial = initial
            lines.append("")
            lines.append(f"## {initial}")
            lines.append("")
        # MkDocs löst .md-Pfade relativ zum index-az.md auf — also direkt
        # gegen die virtuelle URI, ohne führenden Slash.
        lines.append(f"- [{benennung}]({uri}) · {kurz}")

    lines.append("")
    return "\n".join(lines)


_LINK_SAME_CLUSTER = re.compile(r"\]\(hg_(\w+)\.md\)")
_LINK_OTHER_CLUSTER = re.compile(r"\]\(\.\./(\d\d_\w+)/hg_(\w+)\.md\)")
_LINK_SG_TO_HG = re.compile(
    r"\]\((?:\.\./)*hauptglossar/(\d\d_\w+)/hg_(\w+)\.md\)"
)


def _rewrite_cross_links(text: str) -> str:
    """Map all ``hg_*.md`` link targets to the rendered site paths."""

    def _other(match: re.Match[str]) -> str:
        cluster_dir, hg_id = match.group(1), match.group(2)
        target = CLUSTER_URL.get(cluster_dir)
        return f"](../{target}/{hg_id}.md)" if target else match.group(0)

    def _sg(match: re.Match[str]) -> str:
        cluster_dir, hg_id = match.group(1), match.group(2)
        target = CLUSTER_URL.get(cluster_dir)
        return f"](../{target}/{hg_id}.md)" if target else match.group(0)

    text = _LINK_OTHER_CLUSTER.sub(_other, text)
    text = _LINK_SG_TO_HG.sub(_sg, text)
    text = _LINK_SAME_CLUSTER.sub(r"](\1.md)", text)
    return text


def _strip_frontmatter(text: str) -> str:
    """Remove the leading ``--- ... ---`` YAML block, return the body."""
    if not text.startswith("---"):
        return text
    end = text.find("---", 3)
    if end == -1:
        return text
    return text[end + 3 :]


# ---------------------------------------------------------------------------
# JSON-API v1
# ---------------------------------------------------------------------------
#
# Vier Endpoints unter ``/api/v1/``:
#   - ``index.json``            — Liste aller HG-Einträge (minimal).
#   - ``eintraege/<id>.json``   — Voll-Frontmatter + Markdown-Body
#                                  + Prosa-Auszug eines Eintrags.
#   - ``graph.json``            — Beziehungs-Graph aus voraussetzungen,
#                                  abgrenzung_zu und oberbegriff.
#   - ``schema.json``           — Beschreibung der Frontmatter-Felder.
#
# Jede Antwort trägt einen ``_meta``-Block: API-Version, Concept-DOI,
# Build-Datum, Lizenz, Generator. Apps und Konsumenten lesen ``_meta``
# vor der Payload, um Versions-Kompatibilität zu prüfen.


def _api_meta(build_date: str) -> dict:
    """Standard ``_meta``-Block, der jeder API-Antwort beiliegt."""
    return {
        "api_version": API_VERSION,
        "concept_doi": API_CONCEPT_DOI,
        "build_date": build_date,
        "license": API_LICENSE,
        "generator": "holzbau-glossar build_pages.py",
    }


def _parse_frontmatter(text: str) -> dict:
    """YAML-Frontmatter aus einer Markdown-Datei als Dict. Liefert leeres
    Dict, wenn kein ``---``-Block am Anfang steht oder das YAML kaputt
    ist (defensives Verhalten — die API soll auch bei einzelnen
    defekten Einträgen den Build nicht brechen)."""
    if not text.startswith("---"):
        return {}
    end = text.find("---", 3)
    if end == -1:
        return {}
    try:
        data = yaml.safe_load(text[3:end])
    except yaml.YAMLError:
        return {}
    return data if isinstance(data, dict) else {}


def _body_after_frontmatter(text: str) -> str:
    """Nur der Markdown-Body ohne YAML-Block, von führendem Whitespace
    befreit. Identisch zur internen ``_strip_frontmatter``, aber mit
    klarerem Namen für den API-Kontext."""
    return _strip_frontmatter(text).lstrip()


def _write_api_v1(
    content_dir: "Path",
    site_dir: "Path",
    site_url: str,
) -> None:
    """Erzeuge alle vier API-Endpoints unter ``site/api/v1/``. Wird
    aus ``on_post_build`` aufgerufen, nach der HTML-Generation, damit
    die JSON-Files neben der Site liegen und mit ausgeliefert werden."""
    from datetime import date

    api_dir = site_dir / "api" / "v1"
    eintraege_dir = api_dir / "eintraege"
    eintraege_dir.mkdir(parents=True, exist_ok=True)

    build_date = date.today().isoformat()
    meta = _api_meta(build_date)

    # Pro Eintrag: Frontmatter, Body, Prosa-Auszug einsammeln.
    entries: list[dict] = []
    for cluster_dir, _label in CLUSTERS.items():
        cluster_path = content_dir / "hauptglossar" / cluster_dir
        if not cluster_path.is_dir():
            continue
        cluster_url = CLUSTER_URL[cluster_dir]
        for hg_file in sorted(cluster_path.glob("hg_*.md")):
            hg_id = hg_file.stem.removeprefix("hg_")
            text = hg_file.read_text(encoding="utf-8")
            frontmatter = _parse_frontmatter(text)
            body = _body_after_frontmatter(text)
            excerpt = _extract_prosa_excerpt(text)
            entries.append({
                "id": hg_id,
                "cluster": cluster_url,
                "site_url": f"{site_url}/{cluster_url}/{hg_id}/",
                "frontmatter": frontmatter,
                "body_markdown": body,
                "prosa_excerpt": excerpt,
            })

    _write_api_index(api_dir, entries, meta)
    _write_api_entries(eintraege_dir, entries, meta)
    _write_api_graph(api_dir, entries, meta)
    _write_api_schema(api_dir, meta)


def _write_api_index(api_dir: "Path", entries: list[dict], meta: dict) -> None:
    """``index.json`` — Liste aller Einträge, minimal-Set Felder. Für
    App-Such- und Auswahl-Listen optimiert; keine Voll-Definition."""
    payload = {
        "_meta": meta,
        "count": len(entries),
        "entries": [
            {
                "id": e["id"],
                "benennung": e["frontmatter"].get("benennung", e["id"]),
                "cluster": e["cluster"],
                "url": e["site_url"],
                "api_url": f"/api/v1/eintraege/{e['id']}.json",
                "synonyme": e["frontmatter"].get("synonyme", []) or [],
                "status": e["frontmatter"].get("status"),
                "theorie_pflichtig": e["frontmatter"].get("theorie_pflichtig"),
                "oberbegriff": e["frontmatter"].get("oberbegriff"),
                "begriffstyp": e["frontmatter"].get("begriffstyp"),
            }
            for e in entries
        ],
    }
    (api_dir / "index.json").write_text(
        json.dumps(payload, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )


def _write_api_entries(eintraege_dir: "Path", entries: list[dict], meta: dict) -> None:
    """``eintraege/<id>.json`` — Voll-Daten pro Eintrag: gesamtes
    Frontmatter, gesamter Markdown-Body, Prosa-Auszug, URL-Verweise."""
    for e in entries:
        payload = {
            "_meta": meta,
            "id": e["id"],
            "cluster": e["cluster"],
            "site_url": e["site_url"],
            "frontmatter": e["frontmatter"],
            "prosa_excerpt": e["prosa_excerpt"],
            "body_markdown": e["body_markdown"],
        }
        (eintraege_dir / f"{e['id']}.json").write_text(
            json.dumps(payload, ensure_ascii=False, indent=2),
            encoding="utf-8",
        )


def _write_api_graph(api_dir: "Path", entries: list[dict], meta: dict) -> None:
    """``graph.json`` — Beziehungs-Graph als Nodes + Edges.

    Kanten-Relationen:
      - ``oberbegriff``   → einfache Vererbungs-Kante (Spezialisierung).
      - ``voraussetzung`` → Begriff braucht Ziel-Begriff zum Verstehen.
      - ``abgrenzung``    → Begriff ist von Ziel-Begriff aktiv abgegrenzt.
    """
    known_ids = {e["id"] for e in entries}
    nodes = [
        {
            "id": e["id"],
            "benennung": e["frontmatter"].get("benennung", e["id"]),
            "cluster": e["cluster"],
        }
        for e in entries
    ]
    edges: list[dict] = []
    for e in entries:
        src = e["id"]
        fm = e["frontmatter"]
        oberbegriff = fm.get("oberbegriff")
        if oberbegriff and oberbegriff in known_ids and oberbegriff != src:
            edges.append({"from": src, "to": oberbegriff, "relation": "oberbegriff"})
        for target in fm.get("voraussetzungen", []) or []:
            if target in known_ids and target != src:
                edges.append({"from": src, "to": target, "relation": "voraussetzung"})
        for target in fm.get("abgrenzung_zu", []) or []:
            if target in known_ids and target != src:
                edges.append({"from": src, "to": target, "relation": "abgrenzung"})

    payload = {
        "_meta": meta,
        "node_count": len(nodes),
        "edge_count": len(edges),
        "nodes": nodes,
        "edges": edges,
    }
    (api_dir / "graph.json").write_text(
        json.dumps(payload, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )


def _write_api_schema(api_dir: "Path", meta: dict) -> None:
    """``schema.json`` — Beschreibung der Frontmatter-Felder, die in
    ``eintraege/<id>.json`` auftauchen können. Kein striktes JSON-
    Schema (das wäre eine eigene Welle), sondern eine
    konsumenten-lesbare Tabelle."""
    payload = {
        "_meta": meta,
        "endpoints": {
            "/api/v1/index.json": "Liste aller HG-Einträge, minimaler Feldsatz pro Eintrag.",
            "/api/v1/eintraege/<id>.json": "Voll-Daten eines Eintrags (Frontmatter + Markdown-Body).",
            "/api/v1/graph.json": "Beziehungs-Graph (Nodes + Edges).",
            "/api/v1/schema.json": "Diese Schema-Beschreibung.",
        },
        "frontmatter_fields": {
            "id": {"type": "string", "required": True, "description": "Eindeutige Eintrags-ID (aus Dateinamen ohne hg_-Präfix)."},
            "benennung": {"type": "string", "required": True, "description": "Menschenlesbare Benennung (deutsche Form)."},
            "synonyme": {"type": "array<string>", "required": False, "description": "Synonyme der Benennung; gleichwertige Suchbegriffe."},
            "abgelehnte_benennungen": {"type": "array<string>", "required": False, "description": "Falsche/missverständliche Benennungen, die das Glossar bewusst nicht verwendet."},
            "oberbegriff": {"type": "string (id)", "required": False, "description": "ID eines anderen HG-Eintrags, der den Oberbegriff stellt."},
            "begriffstyp": {"type": "string", "required": False, "description": "Klassifikation: generisch | partitiv | aggregat | bauteilrolle | …"},
            "voraussetzungen": {"type": "array<string (id)>", "required": False, "description": "Liste von HG-IDs, die zum Verständnis dieses Eintrags vorausgesetzt sind."},
            "abgrenzung_zu": {"type": "array<string (id)>", "required": False, "description": "Liste von HG-IDs, von denen dieser Eintrag aktiv abgegrenzt ist."},
            "status": {"type": "string", "required": False, "description": "Pflegezustand: entwurf | … (Default: entwurf)."},
            "theorie_pflichtig": {"type": "string", "required": False, "description": "required | optional | none — bestimmt SG-Pendant-Pflicht."},
            "quellen_primär": {"type": "array<string>", "required": False, "description": "Primärquellen (Normen, Lehrbücher, Standard-Referenzen)."},
            "quellen_sekundär": {"type": "array<string>", "required": False, "description": "Sekundärquellen (Wikipedia, Fachforen, Branchen-Publikationen)."},
            "quellenkonflikt": {"type": "string", "required": False, "description": "Prosa-Diskussion bei widersprüchlicher Quellenlage."},
        },
        "graph_relations": {
            "oberbegriff": "Spezialisierungs-/Vererbungs-Kante (this is-a oberbegriff).",
            "voraussetzung": "Verständnis-Voraussetzung (this requires target).",
            "abgrenzung": "Aktive Abgrenzung (this is-not target).",
        },
        "versioning_policy": (
            "v1 bleibt rückwärtskompatibel: neue Felder kommen optional dazu, "
            "alte Felder werden nie entfernt oder umtypisiert. Breaking Changes "
            "kommen unter neuer Major-Version (/api/v2/) parallel zur laufenden v1."
        ),
        "license_note": (
            "Inhalte stehen unter CC BY 4.0. Bei Weiterverwendung "
            "holzbau-glossar.ch als Quelle angeben; der Concept-DOI "
            "10.5281/zenodo.20435319 ist die empfohlene Zitations-Referenz."
        ),
    }
    (api_dir / "schema.json").write_text(
        json.dumps(payload, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )
