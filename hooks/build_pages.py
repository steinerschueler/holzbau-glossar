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

import re
from pathlib import Path

from mkdocs.structure.files import File
from mkdocs.structure.nav import Section, Link

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

    for cluster_dir, label in CLUSTERS.items():
        cluster_path = content / "hauptglossar" / cluster_dir
        if not cluster_path.is_dir():
            continue
        entries: list[tuple[str, str]] = []
        for hg_file in sorted(cluster_path.glob("hg_*.md")):
            hg_id = hg_file.stem.removeprefix("hg_")
            hg_text = hg_file.read_text(encoding="utf-8")
            benennung = _extract_benennung(hg_text) or hg_id
            merged = _merge_entry(hg_text, sg_by_id.get(hg_id))
            virtual_uri = f"{CLUSTER_URL[cluster_dir]}/{hg_id}.md"
            files.append(File.generated(config, virtual_uri, content=merged))
            entries.append((benennung, virtual_uri))
        cluster_entries[label] = entries

    # Stash for on_nav.
    config["_holzbau_cluster_entries"] = cluster_entries
    return files


def on_post_build(config):
    """Write a ``.md`` and a ``.txt`` variant of each entry next to its
    rendered HTML page. The ``.md`` is the merged Markdown source (HG +
    optional SG appendix, with original cross-links untouched); the
    ``.txt`` is a conservatively stripped plain-text version of the same
    content. Both are intended for direct citation / archival download."""

    from pathlib import Path

    site_dir = Path(config["site_dir"])
    content = Path(config["docs_dir"]).parent / "content"
    if not content.is_dir():
        return

    sg_by_id = _load_subglossar_index(content / "subglossar")

    for cluster_dir, _label in CLUSTERS.items():
        cluster_path = content / "hauptglossar" / cluster_dir
        if not cluster_path.is_dir():
            continue
        out_dir = site_dir / CLUSTER_URL[cluster_dir]
        out_dir.mkdir(parents=True, exist_ok=True)

        for hg_file in sorted(cluster_path.glob("hg_*.md")):
            hg_id = hg_file.stem.removeprefix("hg_")
            hg_text = hg_file.read_text(encoding="utf-8")
            merged_md = _merge_for_download(hg_text, sg_by_id.get(hg_id))
            (out_dir / f"{hg_id}.md").write_text(merged_md, encoding="utf-8")
            (out_dir / f"{hg_id}.txt").write_text(
                _markdown_to_plain(merged_md), encoding="utf-8"
            )


def on_nav(nav, config, files):
    """Append four cluster sections after the static pages."""
    cluster_entries = config.pop("_holzbau_cluster_entries", {})
    if not cluster_entries:
        return nav

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
        nav.items.append(section)

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
# Verschränkung HG + SG
# ---------------------------------------------------------------------------


def _merge_entry(hg_text: str, sg_text: str | None) -> str:
    """Concatenate Hauptglossar content with (optional) Subglossar body,
    rewriting cross-links so MkDocs resolves them against the rendered
    site structure."""
    merged_hg = _rewrite_cross_links(hg_text)
    if not sg_text:
        return merged_hg

    sg_body = _rewrite_cross_links(_strip_frontmatter(sg_text).lstrip())
    return (
        merged_hg.rstrip()
        + "\n\n"
        + "## Didaktische Hülle (Subglossar)\n\n"
        + sg_body
    )


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
