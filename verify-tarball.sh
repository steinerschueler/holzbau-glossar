#!/usr/bin/env bash
# Pre-release Tarball-Sanity-Check.
#
# Erzeugt den Tarball, den GitHub/Zenodo beim nächsten Release-Tag
# verteilen würden, und prüft, dass alle enthaltenen Pfade einem der
# erwarteten Muster entsprechen. Bei Abweichung: Liste der unerwarteten
# Pfade + Exit-Code 1.
#
# Aufruf:  ./verify-tarball.sh
# Vor:     gh release create v0.x.0 …

set -euo pipefail

cd "$(git rev-parse --show-toplevel)"

# Pfad-Muster, die im Tarball erwartet werden. Erweitern, wenn eine
# neue inhaltliche Kategorie publiziert werden soll (z. B. eine neue
# Konventions-Datei, eine Forschungs-Snapshot-Sektion).
EXPECTED_PATTERNS='^(content/|src/methode/|LICENSE$|README.md$)'

tarball=$(git archive --worktree-attributes HEAD --format=tar 2>/dev/null \
    | tar -tf - 2>/dev/null \
    | grep -v '/$' \
    | sort)

unexpected=$(echo "$tarball" | grep -vE "$EXPECTED_PATTERNS" || true)

if [[ -n "$unexpected" ]]; then
    echo "⚠  Unerwartete Pfade im Tarball:"
    echo "$unexpected" | sed 's/^/    /'
    echo
    echo "Total: $(echo "$tarball" | wc -l) Files."
    echo
    echo "→ Entweder .gitattributes erweitern (Pfad als -export-ignore eintragen),"
    echo "  oder EXPECTED_PATTERNS in dieser Datei nachziehen."
    exit 1
fi

count=$(echo "$tarball" | wc -l)
content_count=$(echo "$tarball" | grep -c '^content/' || true)
methode_count=$(echo "$tarball" | grep -c '^src/methode/' || true)

echo "✓ Tarball-Inhalt entspricht der Whitelist."
echo
echo "  $count Files insgesamt, davon:"
echo "    $content_count  in content/ (Glossar-Korpus + HG-Konventionen)"
echo "    $methode_count   in src/methode/ (Methode-Doku)"
echo
echo "  Top-Level:"
echo "$tarball" | awk -F/ '{print $1}' | sort -u | sed 's/^/    /'
