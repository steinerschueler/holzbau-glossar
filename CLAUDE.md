# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

# holzbau-glossar — Webseite holzbau-glossar.ch

## Zweck

Öffentliche Webseite (`holzbau-glossar.ch`) für das Holzbau-Glossar:
122 Hauptglossar- und 9 Subglossar-Einträge, plus Methode-Doku und eine
statische JSON-API. **MkDocs Material**-Site (`mkdocs.yml`, `src/`,
`overrides/`, `hooks/build_pages.py`), gebaut und deployt über eine
GitHub Action bei jedem Push auf `main`.

## Verhältnis zum Quell-Repo

**Die Glossar-Inhalte gehören NICHT diesem Repo** — sie sind eine
Spiegelung aus dem privaten Quell-Repo `steinerschueler/zimmermann_app`
(lokal `/home/eric/zimmermann_app`, dort `hauptglossar/` + `lerninhalt/`).
`zimmermann_app` ist die **Single Source of Truth**.

- `content/hauptglossar/**`, `content/subglossar/**`,
  `content/hauptglossar/HG_KONVENTIONEN.md` sind **gespiegelt** — niemals
  hier von Hand editieren. Änderungen am Glossar passieren im App-Repo,
  dann Re-Sync (siehe unten).
- Site-eigen (hier editierbar): `mkdocs.yml`, `src/**` (Methode-,
  Lizenz-, Zitieren-, Datenschutz-Seiten), `overrides/**` (Templates),
  `hooks/build_pages.py` (Seiten- + JSON-API-Generator), `sync.sh`.

## Konto / Repo

Owner ist Erics **Zweit**-Account `steinerschueler` (nicht `Bawdyness`).
Vor `gh`-Aktionen: `gh auth switch --user steinerschueler`. `gh`-Calls
explizit mit `--repo steinerschueler/holzbau-glossar` setzen.

## Inhalts-Sync aus zimmermann_app

```bash
./sync.sh /home/eric/zimmermann_app
```

`sync.sh` rsync-spiegelt (`--delete`) die `hg_*.md`, `HG_KONVENTIONEN.md`
und `sg_*.md` aus dem App-Repo nach `content/`. Bei jeder neuen
Glossar-Welle im App-Repo: syncen, committen, pushen → GitHub Action baut
und deployt die Site.

## Release-Workflow (Zenodo-DOI)

**Jeder GitHub-Release-Tag löst über die Zenodo-GitHub-Integration einen
neuen, permanenten Version-DOI aus.** Die Inhalte sind unter CC BY 4.0
archiviert (Zenodo / CERN).

> ⚠️ **Zenodo-DOIs sind permanent und nicht löschbar.** Einen Release
> nur auf ausdrückliche Freigabe von Eric anlegen — nie autonom.

Zwei DOI-Arten (beide in `mkdocs.yml` unter `extra:`):
- **`concept_doi`** = `10.5281/zenodo.20435319` — **konstant**, zeigt
  immer auf die neueste Version. **Niemals ändern.**
- **`version_doi`** — pro Release neu, von Zenodo vergeben (nicht
  vorhersehbar/fortlaufend). Wird zusammen mit `version_label` nach jedem
  Release eingebettet.

Versionsschema: `vMAJOR.MINOR.0`, pro Welle Minor-Bump (zuletzt v0.6.0).

### Schritte

1. **Inhalt aktuell?** Falls eine neue Glossar-Welle vorliegt: erst
   `./sync.sh /home/eric/zimmermann_app`, committen, pushen, Build-Action
   grün abwarten (`gh run list --repo steinerschueler/holzbau-glossar`).
2. **Nächste Version bestimmen:** `gh release list --repo steinerschueler/holzbau-glossar`
   → letzten Tag ablesen, Minor um 1 erhöhen.
3. **Release-Notes** schreiben (Changelog gegenüber der Vorversion;
   Korpus-Stand, was neu/geändert, Concept-DOI-Zeile). Stil: siehe
   `gh release view <letzter-tag> --repo steinerschueler/holzbau-glossar`.
4. **Release anlegen** (löst Zenodo aus):
   ```bash
   gh release create vX.Y.0 --repo steinerschueler/holzbau-glossar \
     --title "vX.Y.0 — <kurz>" --notes-file <notes.md>
   ```
   Was im Zenodo-Tarball landet, steuert die `.gitattributes`-
   `export-ignore`-Whitelist (nur Inhalt, keine Meta-/Build-Dateien).
5. **Auf den Version-DOI warten** (~1–5 Min Zenodo-Latenz). Abrufen über
   die Zenodo-API des Concept-Records:
   ```bash
   curl -s "https://zenodo.org/api/records/20435319" \
     | python3 -c "import sys,json; d=json.load(sys.stdin); print(d['doi'], d['metadata']['version'])"
   ```
   `20435319` ist die Concept-Record-ID (= Zahl des `concept_doi`). Das
   Feld `doi` des aufgelösten neuesten Records ist der neue Version-DOI.
   Solange noch die Vorversion erscheint: Zenodo ist nicht fertig — erneut
   abfragen. (Alternativ manuell: `https://doi.org/10.5281/zenodo.20435319`
   leitet auf die neueste Version, dort den Version-DOI ablesen.)
6. **Version-DOI einbetten** (das ist der „embed"-Commit):
   - `mkdocs.yml` → `extra:`: `version_label: vX.Y.0`,
     `version_doi: "10.5281/zenodo.<neue-id>"`. `concept_doi` **nicht**
     anfassen.
   - `src/zitieren.md`: DOI-Liste und Zitier-Beispiel auf den neuen
     Version-DOI / das neue Label aktualisieren.
   - Der Footer rendert beide DOIs über `overrides/partials/copyright.html`;
     Citation-Meta-Tags stehen in `overrides/main.html` (nutzen den
     Concept-DOI, bleiben unverändert).
7. **Commit + push:**
   ```bash
   git commit -am "embed vX.Y.0 Zenodo version DOI"
   git push origin main
   ```
   Die GitHub Action deployt die Site mit dem eingebetteten DOI.

### Verifikation nach dem Release

- `gh run list` → Deploy-Build grün.
- Footer auf `holzbau-glossar.ch` zeigt das neue `version_label` mit Link
  auf den neuen Version-DOI; Concept-DOI unverändert.
- `https://doi.org/<version_doi>` löst auf den neuen Zenodo-Record auf.

## Build lokal

```bash
mkdocs build        # statische Site nach site/
mkdocs serve        # lokale Vorschau
```

`hooks/build_pages.py` generiert zur Build-Zeit die Glossar-Seiten und die
JSON-API (`/api/v1/`) aus `content/`. Das JSON-Schema (`schema.json`)
spiegelt die Frontmatter-Felder der Einträge — bei Feld-Umbenennungen im
App-Repo (z. B. `theorie_pflichtig:` → `subglossar_pendant:`, 2026-05-29)
auch hier in `hooks/build_pages.py` und den Methode-/API-Doku-Seiten unter
`src/` nachziehen.
