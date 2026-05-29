---
title: Zitieren
description: Empfohlene Zitierform, Lizenz, Versions-Anker.
---

# Zitieren

Dieses Glossar ist als zitierbare Quelle für Forschung, Normungs-Arbeit
und Werkzeug-Entwicklung gedacht.

## Lizenz

Alle Glossar-Inhalte stehen unter
[Creative Commons BY 4.0](https://creativecommons.org/licenses/by/4.0/deed.de).

Das heisst konkret:

- **Erlaubt:** Nutzung in jeder Form, einschliesslich kommerzieller
  Werkzeuge (cadWork, ArchiCAD u.a.), abgeleiteter Werke und Übersetzungen.
- **Bedingung:** Namensnennung mit Verweis auf diese Quelle.

## Drei Formate pro Eintrag

Jeder Glossar-Eintrag wird in drei Formaten ausgeliefert, damit zitieren
ohne Umwege funktioniert:

- **HTML** für entspanntes Lesen im Browser (mit Hell- und Darkmode).
- **Markdown** (`.md`) als 1:1-Quelle mit Frontmatter — geeignet für
  Einbettung in eigene Doku-Pipelines, Pandoc-Konversion oder direkte
  Übernahme.
- **Plain-Text** (`.txt`) als reiner Text ohne Markdown-Syntax —
  geeignet für E-Mail, Notiz-Apps oder schnelles Copy-Paste.

Direkt unter jedem Eintrag stehen „Quelle herunterladen"-Buttons.

## DOI

Das Glossar ist auf [Zenodo](https://zenodo.org/) archiviert und unter
einer persistenten DOI zitierbar:

- **Concept-DOI** (verweist immer auf die jeweils neueste Version):
  [10.5281/zenodo.20435319](https://doi.org/10.5281/zenodo.20435319)
- **Version-DOI** v0.1.0 (Stand 2026-05-28):
  [10.5281/zenodo.20435320](https://doi.org/10.5281/zenodo.20435320)
- Weitere Version-DOIs für künftige Releases sind über die
  [Zenodo-Eintragsseite](https://doi.org/10.5281/zenodo.20435319)
  erreichbar.

### Was ist ein DOI — und wozu?

Ein **DOI** (Digital Object Identifier) ist ein persistenter
Identifikator, der einer Publikation dauerhaft zugeordnet bleibt — auch
wenn die ursprüngliche URL verschwindet, umzieht oder die Domain
ausläuft. Hinter dem DOI dieses Glossars steht **Zenodo**, betrieben
vom CERN: die Inhalte sind dort archiviert und mit einer Aufbewahrungs-
Zusage von mindestens 20 Jahren versehen.

Konkret gewinnst du mit einem DOI:

1. **Langzeit-Verlässlichkeit** — die DOI funktioniert auch dann noch,
   wenn `holzbau-glossar.ch` einmal nicht mehr erreichbar wäre. Sie
   ist die einzige Adresse, die du in einer wissenschaftlichen Arbeit
   guten Gewissens jahrzehntelang stehen lassen kannst.
2. **Maschinenlesbare Zitation** — Literaturverwaltungs-Programme wie
   Zotero, Mendeley, EndNote oder Citavi importieren über die DOI alle
   Meta-Daten (Titel, Autor, Datum, Verlag, Lizenz) automatisch.
   Kein Abtippen.
3. **Versionierte Eindeutigkeit** — die **Concept-DOI** sagt „dieses
   Glossar in seiner jeweils aktuellen Form", die **Version-DOI** sagt
   „dieser Stand, eingefroren". Für reproduzierbare Forschungs- oder
   Normungsarbeit zählt nur die Version-DOI: ändere ich morgen einen
   Eintrag, bleibt der gestern referenzierte Stand unverändert
   abrufbar.
4. **Sichtbarkeit und Tracking** — wissenschaftliche Such-Dienste
   (Google Scholar, OpenAIRE, BASE) indizieren über DOI; jede Zitation
   im Web wird mit der Quelle verknüpft.

### Concept-DOI oder Version-DOI — welche wann?

| Situation                                 | Empfohlen          |
|-------------------------------------------|--------------------|
| Lehr-Material, Werkzeug-Doku, Webseiten   | Concept-DOI        |
| Code-Bibliothek, die das Glossar einbettet| Concept-DOI        |
| Wissenschaftliche Arbeit, Norm-Verweis    | **Version-DOI**    |
| Behördliche oder gutachterliche Referenz  | **Version-DOI**    |
| Schul-Skript, didaktisches Material       | Concept-DOI        |

Faustregel: Wenn du willst, dass deine Leser**innen** immer den
aktuellen Stand sehen → Concept-DOI. Wenn du willst, dass dein Verweis
in zehn Jahren noch dasselbe zeigt wie heute → Version-DOI.

### Eine DOI praktisch nutzen

#### Im Browser

Hänge die DOI an `https://doi.org/`:
[https://doi.org/10.5281/zenodo.20435319](https://doi.org/10.5281/zenodo.20435319).
Der Link löst sich automatisch zur kanonischen Zenodo-Eintragsseite
auf, von wo du die Inhalte und alle Meta-Daten siehst.

#### In Zotero (Empfehlung für die meisten)

1. Zotero öffnen.
2. In der Werkzeugleiste auf den **Zauberstab** klicken
   („Eintrag durch Identifikator hinzufügen").
3. DOI eintippen: `10.5281/zenodo.20435319`
4. Eintrag erscheint mit allen Meta-Daten in deiner Bibliothek.

#### In Mendeley / EndNote / Citavi

Praktisch identisch: alle drei Programme bieten unter
„Datei → Importieren" oder „Eintrag hinzufügen" ein DOI-Feld an.
Einfach `10.5281/zenodo.20435319` einfügen → Meta-Daten werden
automatisch geladen.

#### Direkt als BibTeX

Jeder einzelne Glossar-Eintrag bietet einen `.bib`-Download (kleiner
Knopf unter dem Eintrag). Die Datei ist sofort einsetzbar — kopiere
sie in dein LaTeX- oder R Markdown-Projekt und referenziere via
`\cite{holzbau-glossar:<eintrag-id>}`.

Für das gesamte Glossar (statt eines einzelnen Eintrags) kannst du
auf der [Zenodo-Eintragsseite](https://doi.org/10.5281/zenodo.20435319)
rechts in der Spalte „Export" auf „BibTeX" klicken — das ergibt einen
sauberen `@misc`-Eintrag.

## Empfohlene Zitierform

### Gesamtes Glossar (Concept-DOI)

**APA 7:**

> Holzbau-Glossar. (2026). *Holzbau-Glossar*. holzbau-glossar.ch.
> https://doi.org/10.5281/zenodo.20435319

**ISO 690 (DACH-Normungs-Kontext):**

> Holzbau-Glossar. *Holzbau-Glossar* [online]. holzbau-glossar.ch, 2026.
> Abrufbar unter: doi:10.5281/zenodo.20435319.

**BibTeX:**

```bibtex
@misc{holzbau-glossar,
  title     = {Holzbau-Glossar},
  author    = {{holzbau-glossar.ch}},
  year      = {2026},
  publisher = {holzbau-glossar.ch},
  doi       = {10.5281/zenodo.20435319},
  url       = {https://holzbau-glossar.ch/},
  note      = {CC BY 4.0}
}
```

Die doppelten geschweiften Klammern `{{...}}` um den Autor halten
BibTeX davon ab, den Domain-Namen als Personen-Namen zu zerlegen.

### Bestimmter Eintrag (mit Version-DOI für reproduzierbare Belege)

Für einen einzelnen Glossar-Eintrag mit eingefrorenem Stand:

**APA 7:**

> Holzbau-Glossar. (2026). Kerve. In *Holzbau-Glossar* (v0.1.0).
> holzbau-glossar.ch.
> https://doi.org/10.5281/zenodo.20435320

**BibTeX** (per Eintrag — fertig zum Download unter jedem Glossar-
Eintrag):

```bibtex
@misc{holzbau-glossar:kerve,
  title     = {Kerve},
  author    = {{holzbau-glossar.ch}},
  year      = {2026},
  publisher = {holzbau-glossar.ch},
  doi       = {10.5281/zenodo.20435319},
  url       = {https://holzbau-glossar.ch/holzbau/kerve/},
  note      = {Hauptglossar-Eintrag, CC BY 4.0}
}
```

Die unter jedem Eintrag bereitgestellte `.bib`-Datei verwendet die
Concept-DOI; für eine Version-DOI ersetze den `doi`-Eintrag
entsprechend dem zitierten Release-Stand (siehe DOI-Liste oben).
