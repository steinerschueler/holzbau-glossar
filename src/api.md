---
title: API
description: Maschinenlesbare JSON-API für Anwendungen, Tools und Forschung.
---

# API

Das Holzbau-Glossar liefert seine Inhalte zusätzlich zur menschen-
lesbaren Webseite als **maschinenlesbare JSON-API**. Damit lassen
sich die Definitionen, Synonyme und Beziehungen direkt in Apps,
Werkzeuge und Forschungs-Pipelines übernehmen — ohne Scraping,
ohne Anmeldung, ohne Token.

Basis-URL: `https://holzbau-glossar.ch/api/v1/`.

## Was ist eine API — und wozu?

Eine **API** (Application Programming Interface) liefert Inhalte in
einem Format, das **Programme** unmittelbar einlesen können — anders
als die HTML-Seiten, die für menschliche Augen optimiert sind. Beim
Holzbau-Glossar ist das ein Satz statischer **JSON-Dateien** hinter
dem GitHub-Pages-CDN: keine Anmeldung, keine Anfrage-Begrenzung,
identisch zur Website-Auslieferung.

Konkret gewinnst du mit dieser API:

1. **Glossar-Anbindung in eigenen Apps** — eine Holzbau-App,
   ein Werkstatt-Tablet oder ein Lehr-Werkzeug kann die normativ
   gepflegten Definitionen direkt einbinden, statt sie zu duplizieren.
   Updates am Glossar landen automatisch in der App, sobald sie
   wieder online ist.
2. **Beziehungs-Visualisierungen für Didaktik** — der Graph-Endpoint
   macht die Voraussetzungs- und Abgrenzungs-Struktur zwischen
   Begriffen explizit; ideal für Lern-Pfade, Begriffs-Karten und
   Konsistenz-Linter.
3. **Tools-Integration** — IDE-Plugins, Eingabe-Validatoren,
   Auto-Vervollständigung im CAD-Workflow können auf Synonyme
   und abgelehnte Benennungen zugreifen, um Eingaben zu
   normalisieren.
4. **Forschungs- und ML-Pipelines** — Bibliometrie, Begriffs-Drift-
   Analyse, automatisierte Übersetzungen: der Volltext jedes
   Eintrags ist als sauberes Markdown verfügbar, das `_meta`-Feld
   verankert jede Antwort über die Concept-DOI auf eine zitierbare
   Version.

Die API liegt **physisch im selben Repository** wie das Glossar
selbst und wird bei jedem Build neu aus den Markdown-Quellen
erzeugt. Damit ist sie immer konsistent mit der Website.

## Welcher Endpoint wofür?

| Situation | Endpoint |
|---|---|
| App zeigt eine Such-/Auswahl-Liste mit allen Begriffen | `index.json` |
| App lädt die Voll-Definition eines einzelnen Begriffs | `eintraege/<id>.json` |
| Lehrmaterial visualisiert „was setzt was voraus" | `graph.json` |
| Konsument prüft, welche Felder ein Eintrag haben kann | `schema.json` |

Faustregel: **`index.json` für „welche Begriffe gibt es", `eintraege/`
für „was sagt dieser Begriff", `graph.json` für „wie hängen sie
zusammen".** Das `schema.json` brauchst du nur einmal beim Bauen
deines Konsumenten.

## Eine API praktisch nutzen

### Im Browser

Hänge den Endpoint an die Basis-URL — z. B.
`https://holzbau-glossar.ch/api/v1/index.json`. Moderne Browser
rendern JSON formatiert und durchsuchbar.

### Python — alle Einträge laden

```python
import urllib.request, json

with urllib.request.urlopen("https://holzbau-glossar.ch/api/v1/index.json") as r:
    index = json.load(r)

print(f"{index['count']} Einträge, API v{index['_meta']['api_version']}")
for entry in index["entries"][:5]:
    print(f"  {entry['benennung']}: {entry['url']}")
```

### Kotlin / Android — typisiert mit kotlinx-serialization

```kotlin
@Serializable
data class IndexResponse(
    @SerialName("_meta") val meta: Meta,
    val count: Int,
    val entries: List<EntrySummary>
)

@Serializable
data class EntrySummary(
    val id: String,
    val benennung: String,
    val cluster: String,
    val url: String,
    val synonyme: List<String> = emptyList(),
)

val response = httpClient.get("https://holzbau-glossar.ch/api/v1/index.json")
val index = Json.decodeFromString<IndexResponse>(response.bodyAsText())
```

Die App kann den `index.json`-Snapshot lokal cachen (Room/DataStore)
und beim nächsten Online-Sein gegen `_meta.build_date` prüfen,
ob ein Update verfügbar ist.

### curl + jq — schneller Einzelabruf

```bash
curl -s https://holzbau-glossar.ch/api/v1/eintraege/kerve.json \
  | jq '.frontmatter | {benennung, synonyme, voraussetzungen}'
```

### Beziehungs-Graph filtern

```bash
curl -s https://holzbau-glossar.ch/api/v1/graph.json \
  | jq '.edges | map(select(.relation == "voraussetzung")) | .[:10]'
```

## Endpoint-Referenz

### `/api/v1/index.json`

Liste **aller** Hauptglossar-Einträge mit minimalem Feldsatz pro
Eintrag.

```json
{
  "_meta": {
    "api_version": "1",
    "concept_doi": "10.5281/zenodo.20435319",
    "build_date": "2026-05-29",
    "license": "https://creativecommons.org/licenses/by/4.0/",
    "generator": "holzbau-glossar build_pages.py"
  },
  "count": 122,
  "entries": [
    {
      "id": "kerve",
      "benennung": "Kerve",
      "cluster": "holzbau",
      "url": "https://holzbau-glossar.ch/holzbau/kerve/",
      "api_url": "/api/v1/eintraege/kerve.json",
      "synonyme": ["Sparrenkerve", "Sparrenkerbe", "Klauenkerve", "..."],
      "status": "entwurf",
      "theorie_pflichtig": "required",
      "oberbegriff": "bearbeitung",
      "begriffstyp": "partitiv"
    }
  ]
}
```

### `/api/v1/eintraege/<id>.json`

Voll-Daten eines Eintrags — gesamtes Frontmatter, kompletter
Markdown-Body, Prosa-Auszug.

```json
{
  "_meta": { "...": "..." },
  "id": "kerve",
  "cluster": "holzbau",
  "site_url": "https://holzbau-glossar.ch/holzbau/kerve/",
  "frontmatter": {
    "id": "kerve",
    "benennung": "Kerve",
    "synonyme": [ "..." ],
    "voraussetzungen": [ "bearbeitung", "bauteil", "sparren", "..." ],
    "abgrenzung_zu": [ "versatz", "zapfen", "..." ],
    "quellen_primär": [ "..." ],
    "...": "..."
  },
  "prosa_excerpt": "Eine Kerve ist eine subtraktive Bearbeitung ...",
  "body_markdown": "## Prosa-Definition\n\n..."
}
```

### `/api/v1/graph.json`

Beziehungs-Graph aller Einträge — Nodes und Edges mit drei
Relations-Typen:

- **`oberbegriff`** — Spezialisierung (`this is-a target`).
- **`voraussetzung`** — Verständnis-Voraussetzung (`this requires target`).
- **`abgrenzung`** — aktive Abgrenzung (`this is-not target`).

```json
{
  "_meta": { "...": "..." },
  "node_count": 122,
  "edge_count": 1678,
  "nodes": [
    { "id": "kerve", "benennung": "Kerve", "cluster": "holzbau" }
  ],
  "edges": [
    { "from": "kerve", "to": "bearbeitung", "relation": "oberbegriff" },
    { "from": "kerve", "to": "sparren",     "relation": "voraussetzung" },
    { "from": "kerve", "to": "versatz",     "relation": "abgrenzung" }
  ]
}
```

### `/api/v1/schema.json`

Beschreibung der Frontmatter-Felder, die in `eintraege/<id>.json`
auftauchen können — konsumenten-lesbare Tabelle (kein striktes
JSON-Schema-Dokument).

## Versionsstrategie

| Pfad | Garantie |
|---|---|
| `/api/v1/` | rückwärtskompatibel: neue Felder kommen optional dazu; alte werden nie entfernt oder umtypisiert |
| `/api/v2/` | erscheint erst bei Schema-Bruch, läuft parallel zu v1 |

Apps und Konsumenten **pinnen über den Pfad-Prefix**. Der `_meta`-
Block in jeder Antwort trägt `api_version` als zusätzlichen Sanity-
Check.

## CORS und Caching

- **CORS**: GitHub-Pages liefert ohne expliziten
  `Access-Control-Allow-Origin`. Cross-Origin-JavaScript-Konsum
  wird unterstützt, sobald GitHub-Pages CORS-Header setzt; bis
  dahin sind Server-seitige Proxies oder gleicher Origin nötig.
- **Caching**: ETag und `Last-Modified` aus GitHub-Pages
  funktionieren out of the box. Apps sollten den `_meta.build_date`-
  Wert für client-seitiges Cache-Invalidating nutzen.

## Lizenz und Zitation

Inhalte stehen unter CC BY 4.0. Details zu Bedingungen, Praxis und
Begründung der Lizenz-Wahl: siehe [Lizenz](lizenz.md). Empfohlene
Zitations-Form mit DOI: siehe [DOI (Zitieren)](zitieren.md).
