#!/usr/bin/env python3
"""Öffentlicher Hauptglossar-Filter für holzbau-glossar.

Säubert die aus ``zimmermann_app`` gespiegelten Hauptglossar-Einträge
(``content/hauptglossar/**/hg_*.md``) für die öffentliche Publikation
(Website, JSON-API, Zenodo-DOI-Tarball). App-Implementierungs- und
Autoren-Prozess-Bezüge sind für DOI-/API-Nutzer irrelevant.

``content/`` ist dadurch der öffentliche Spiegel; ``zimmermann_app``
bleibt Single Source of Truth. Wird von ``sync.sh`` nach dem rsync
aufgerufen. Idempotent — mehrfaches Anwenden ändert nichts mehr.

Umfang: ausschliesslich ``hg_*.md`` (nicht HG_KONVENTIONEN.md, nicht
Subglossar, nicht das Frontmatter-Schema).

Transformationen:
  1. Streiche die App-/Autoren-Sektionen ``## Implementierungshinweis``
     und ``## Folgearbeit (trigger-basiert)`` samt Inhalt (bis zur
     nächsten ``## ``-Sektion bzw. Dateiende). Dort sitzt praktisch der
     gesamte Kotlin-Code und die internen Projekt-TODOs.
  2. Anonymisiere die Autoren-Person: ``Eric`` → ``Anweiser`` (als
     Rollen-Pseudonym; ``Erics`` → ``Anweisers``; Komposita ``Eric-…``
     → ``Anweiser-…`` werden vom Wortgrenzen-Match miterfasst).
  3. Entferne interne ``(Memory `…`)``-Referenzen (Autoren-Profil-Bezüge).

Aufruf:  python3 hg_public_filter.py [content-verzeichnis]
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

DROP_SECTIONS = {"Implementierungshinweis", "Folgearbeit (trigger-basiert)"}

# Manueller Marker (FILTER_KONVENTION.md Teil B): in der ZMA-Quelle gesetzte
# HTML-Kommentar-Klammer um chirurgisch zu entfernende interne Stellen.
_INTERN_MARKER = re.compile(
    r"<!--\s*hbg:intern\s*-->.*?<!--\s*/hbg:intern\s*-->", re.DOTALL
)


def _strip_intern_marker(text: str) -> str:
    """Entferne `<!--hbg:intern-->…<!--/hbg:intern-->`-Spannen samt Inhalt."""
    return _INTERN_MARKER.sub("", text)


# Satzzeichen-Artefakte nach Entfernungen glätten (Leerraum vor Punktuation,
# Mehrfach-Leerzeilen, Leerzeichen am Zeilenende). Bewusst minimal — keine
# globale Mehrfach-Space-Kollabierung (würde Tabellen/Einrückung treffen).
_TIDY_SPACE_PUNCT = re.compile(r" +([.,;:)])")
_TIDY_OPEN_PAREN = re.compile(r"\( +")
_TIDY_TRAILING = re.compile(r"[ \t]+\n")
_TIDY_BLANKLINES = re.compile(r"\n{3,}")


def _tidy(text: str) -> str:
    text = _TIDY_SPACE_PUNCT.sub(r"\1", text)
    text = _TIDY_OPEN_PAREN.sub("(", text)
    text = _TIDY_TRAILING.sub("\n", text)
    text = _TIDY_BLANKLINES.sub("\n\n", text)
    return text


def _split_frontmatter(text: str) -> tuple[str, str]:
    """Trenne den YAML-Frontmatter-Block (``--- … ---``) vom Body. Der
    Frontmatter bleibt unangetastet (Rename greift später separat)."""
    if not text.startswith("---"):
        return "", text
    lines = text.splitlines(keepends=True)
    if lines and lines[0].rstrip("\n") == "---":
        for i in range(1, len(lines)):
            # Block-Skalar-Inhalt ist eingerückt; eine nackte '---'-Zeile
            # auf Spalte 0 schliesst den Frontmatter. Tabellen-Trenner
            # ('|---|') matchen nicht.
            if lines[i].rstrip("\n") == "---":
                return "".join(lines[: i + 1]), "".join(lines[i + 1 :])
    return "", text


def _drop_sections(body: str) -> str:
    """Entferne die in DROP_SECTIONS genannten ``## ``-Sektionen samt
    Inhalt. Splittet vor jeder Level-2-Überschrift; h3+ und Code-Zeilen
    lösen keinen Split aus."""
    parts = re.split(r"(?m)^(?=## )", body)
    kept: list[str] = []
    for part in parts:
        m = re.match(r"## (.+)", part)
        if m and m.group(1).strip() in DROP_SECTIONS:
            continue
        kept.append(part)
    new_body = "".join(kept)
    # Aufräumen: verwaiste '---'-Trenner am Ende + Mehrfach-Leerzeilen.
    new_body = re.sub(r"\n{3,}", "\n\n", new_body)
    new_body = re.sub(r"(?:\s*\n---\s*)+\n*$", "\n", new_body)
    return new_body.rstrip() + "\n"


_MEMORY_PAREN = re.compile(r"\s*\(Memory[^)]*\)")
_MEMORY_CLAUSE = re.compile(r"[;,]?\s*Memory\s+`[^`]*`")
_ERICS = re.compile(r"\bErics\b")
_ERIC = re.compile(r"\bEric\b")

# Tote Verweise auf die gestrichene '## Implementierungshinweis'-Sektion.
# Nur die eindeutigen Klammer-/Zusatz-Zeiger werden hier generisch
# entfernt; satz-eingebettete Verweise ('… ist im Implementierungshinweis
# zu behandeln') bleiben der Konvention/quellseitigen Markierung
# vorbehalten (zu satz-spezifisch für eine sichere Regel).
_IMPL_UND = re.compile(r"\s+und\s+Implementierungshinweise?(?=\))")
_IMPL_SEMI = re.compile(r"\s*;\s*siehe\s+Implementierungshinweise?(?=[.)])")
_IMPL_DASH = re.compile(r"\s*—\s*siehe\s+Implementierungshinweise?(?=[.):])")
_IMPL_PAREN = re.compile(r"\s*\((?:siehe\s+)?Implementierungshinweise?\)")


def _strip_impl_pointers(text: str) -> str:
    """Eindeutige Klammer-/Zusatz-Zeiger auf die gestrichene
    Implementierungshinweis-Sektion entfernen (sie zeigen ins Leere)."""
    text = _IMPL_UND.sub("", text)      # "(siehe X und Implementierungshinweis)" → "(siehe X)"
    text = _IMPL_SEMI.sub("", text)     # "…; siehe Implementierungshinweis." → "…."
    text = _IMPL_DASH.sub("", text)     # "… — siehe Implementierungshinweis):" → "…):"
    text = _IMPL_PAREN.sub("", text)    # "(siehe Implementierungshinweis)" → ""
    return text


# Interne Recherche-Bericht-Selbstzitate (`docs/recherche/<…>.md`, mit oder
# ohne Backticks) sind für die Öffentlichkeit tote Links. Neutralisieren statt
# entfernen: der Pfad wird durch ein Zitat-Token `[intern]` ersetzt, die
# Satz-Grammatik bleibt unangetastet (FILTER_KONVENTION.md Teil A).
_RECHERCHE = re.compile(r"`?docs/recherche/[\w./_-]+\.md`?")


def _neutralisiere_recherche(text: str) -> str:
    return _RECHERCHE.sub("[intern]", text)


def _scrub_author_meta(text: str) -> str:
    """Anonymisiere die Autoren-Person und entferne Memory-Referenzen."""
    # Memory-Referenzen zuerst (sonst bliebe '; Memory `user_role`' als
    # Rest in einem Klammer-Ausdruck stehen).
    text = _MEMORY_PAREN.sub("", text)
    text = _MEMORY_CLAUSE.sub("", text)
    # Person → Rollen-Pseudonym. 'Erics' vor 'Eric' (Wortgrenze trennt
    # beide ohnehin, aber explizit ist klarer).
    text = _ERICS.sub("Anweisers", text)
    text = _ERIC.sub("Anweiser", text)
    return text


def filter_text(text: str) -> str:
    # Marker zuerst auf dem GANZEN Dokument strippen — interne Stellen
    # sitzen auch in Frontmatter-Block-Skalaren (z. B. `quellenkonflikt: |`),
    # die über die API publiziert werden, nicht nur im Body.
    text = _strip_intern_marker(text)
    fm, body = _split_frontmatter(text)
    body = _drop_sections(body)
    doc = fm + body
    doc = _strip_impl_pointers(doc)
    doc = _scrub_author_meta(doc)
    doc = _neutralisiere_recherche(doc)
    doc = _tidy(doc)
    if not doc.endswith("\n"):
        doc += "\n"
    return doc


def main(argv: list[str]) -> int:
    content = Path(argv[1]) if len(argv) > 1 else Path("content")
    hg_dir = content / "hauptglossar"
    if not hg_dir.is_dir():
        print(f"hg_public_filter: {hg_dir} nicht gefunden — übersprungen.")
        return 0
    geaendert = 0
    for hg_file in sorted(hg_dir.rglob("hg_*.md")):
        original = hg_file.read_text(encoding="utf-8")
        gefiltert = filter_text(original)
        if gefiltert != original:
            hg_file.write_text(gefiltert, encoding="utf-8")
            geaendert += 1
    print(f"hg_public_filter: {geaendert} Hauptglossar-Einträge gefiltert.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
