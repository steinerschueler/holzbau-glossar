#!/usr/bin/env bash
# Synchronisiert Hauptglossar- und Subglossar-Quellen aus dem lokalen
# ens_holzbau-Projekt in content/ — manuell vor jedem Site-Push.
# Single-Source-of-Truth bleibt ens_holzbau; content/ ist Snapshot.

set -euo pipefail

SOURCE="${1:-${ENS_HOLZBAU:-../../intern/ens_holzbau}}"
TARGET="content"

if [[ ! -d "$SOURCE/glossary" || ! -d "$SOURCE/learning/subglossary" ]]; then
    echo "Fehler: $SOURCE enthält nicht glossary/ und learning/subglossary/." >&2
    echo "Aufruf:  ./sync.sh [pfad-zu-ens_holzbau]" >&2
    echo "Default: ../../intern/ens_holzbau (oder Umgebungsvariable ENS_HOLZBAU)" >&2
    exit 1
fi

mkdir -p "$TARGET/hauptglossar" "$TARGET/subglossar"

# Hauptglossar: Cluster-Struktur erhalten, hg_*.md plus die öffentlich
# publizierte HG_KONVENTIONEN.md (für die Methode-Seite).
# Andere Top-Level-Dateien (STAND_*.md, ABWEICHUNGEN.md, README.md) bleiben
# durch den case-sensitiven Glob aussen vor.
rsync -a --delete \
    --include='*/' \
    --include='hg_*.md' \
    --include='HG_KONVENTIONEN.md' \
    --exclude='*' \
    "$SOURCE/glossary/" "$TARGET/hauptglossar/"

# Subglossar: flach, nur sg_*.md.
rsync -a --delete \
    --include='sg_*.md' \
    --exclude='*' \
    "$SOURCE/learning/subglossary/" "$TARGET/subglossar/"

# Öffentlich-Filter: App-Implementierung (Kotlin/Implementierungshinweis),
# interne Projekt-TODOs (Folgearbeit) und Autoren-Prozess-Bezüge aus den
# HG-Einträgen entfernen bzw. anonymisieren ("Eric" → "Anweiser"). content/
# ist der öffentliche Spiegel (Website/API/DOI); Single Source of Truth
# bleibt ens_holzbau. Idempotent; läuft nach jedem rsync, weil --delete
# sonst die Vollfassung wiederherstellt. Nur hg_*.md (nicht Konventionen/SG).
python3 "$(dirname "$0")/hg_public_filter.py" "$TARGET"

HG_COUNT=$(find "$TARGET/hauptglossar" -name 'hg_*.md' | wc -l)
SG_COUNT=$(find "$TARGET/subglossar" -name 'sg_*.md' | wc -l)
echo "Sync abgeschlossen: $HG_COUNT Hauptglossar-Einträge, $SG_COUNT Subglossar-Einträge."
echo "Bereit für: git add content/ && git commit -m 'sync: ...' && git push"
