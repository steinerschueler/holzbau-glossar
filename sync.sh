#!/usr/bin/env bash
# Synchronisiert Hauptglossar- und Subglossar-Quellen aus dem lokalen
# zimmermann_app-Projekt in content/ — manuell vor jedem Site-Push.
# Single-Source-of-Truth bleibt zimmermann_app; content/ ist Snapshot.

set -euo pipefail

SOURCE="${1:-${ZIMMERMANN_APP:-../zimmermann_app}}"
TARGET="content"

if [[ ! -d "$SOURCE/hauptglossar" || ! -d "$SOURCE/lerninhalt/subglossar" ]]; then
    echo "Fehler: $SOURCE enthält weder hauptglossar/ noch lerninhalt/subglossar/." >&2
    echo "Aufruf:  ./sync.sh [pfad-zu-zimmermann_app]" >&2
    echo "Default: ../zimmermann_app (oder Umgebungsvariable ZIMMERMANN_APP)" >&2
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
    "$SOURCE/hauptglossar/" "$TARGET/hauptglossar/"

# Subglossar: flach, nur sg_*.md.
rsync -a --delete \
    --include='sg_*.md' \
    --exclude='*' \
    "$SOURCE/lerninhalt/subglossar/" "$TARGET/subglossar/"

HG_COUNT=$(find "$TARGET/hauptglossar" -name 'hg_*.md' | wc -l)
SG_COUNT=$(find "$TARGET/subglossar" -name 'sg_*.md' | wc -l)
echo "Sync abgeschlossen: $HG_COUNT Hauptglossar-Einträge, $SG_COUNT Subglossar-Einträge."
echo "Bereit für: git add content/ && git commit -m 'sync: ...' && git push"
