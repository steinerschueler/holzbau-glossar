---
title: Methode — Übersicht
description: Wie das Glossar arbeitet — Aufbau, Schichten, Cluster, Status.
---

# Methode

Diese Seite beschreibt, wie das Glossar arbeitet. Sie ist gedacht für
Leser, die einen Eintrag zitieren, weiterverwenden oder die Methodik
rückwirkend prüfen wollen — Forschende, Normungs-Gremien, Entwickler
an CAD-Werkzeugen.

Die Methode-Seite ist in mehrere Unterkapitel gegliedert. Diese
Übersicht trägt die strukturellen Grundzüge (Schichten, Cluster,
Status); die Detail-Kapitel weiter unten erklären Begriffs-Schema,
Erstellungs-Workflow, Recherche-Standard und Sprachregeln.

| Unterkapitel | Inhalt |
|---|---|
| [Begriffe und Schema](begriffe.md) | Begriffstypen, Pflichtfelder pro Eintrag, Abgrenzung gegen Geschwister-Begriffe |
| [Eintrag-Erstellung](eintrag-erstellung.md) | Der Welle-Workflow von Recherche-Auftrag bis Subglossar-Pendant |
| [Recherche-Standard](recherche.md) | Quellen-Tier-System, Methodik-Sektion, Quellen-Hierarchie + Einsehungs-Status |
| [Sprachregeln](sprachregeln.md) | Senkrecht / rechtwinklig / orthogonal — und warum es darauf ankommt |
| [HG-Konventionen (Volltext)](hg-konventionen.md) | Vollständiger Originaltext der Hauptglossar-Konventionsdatei |

## Zwei Schichten

Das Glossar ist in **zwei Schichten** organisiert, die sich an
unterschiedliche Leser-Stufen richten:

- Das **Hauptglossar** trägt die normative Definition: mathematische
  Form, Wohldefiniertheit, Wertebereiche, Abgrenzung gegen
  Geschwister-Begriffe, Quellen-Belege, dokumentierte Konflikte
  zwischen Quellen.
- Das **Subglossar** trägt eine didaktische Hülle für die unteren
  Ausbildungs-Stufen (Schnuppi, Lehrling, Polier, Meister). Es
  paraphrasiert den Hauptglossar-Eintrag in zugänglicher Sprache,
  ergänzt SVG-Skizzen und benannte Praxis-Beispiele. Innerhalb eines
  Subglossar-Eintrags steigt die Tiefe stufenweise: der Schnuppi-
  Block setzt nichts voraus, der Meister-Block schliesst an
  Tragwerks-Sprache an. Die Ingenieur-Stufe wird nicht im Subglossar
  gespiegelt, sondern direkt aus dem Hauptglossar bedient.

Beide Schichten verweisen aufeinander. Auf der Webseite werden sie
verschränkt dargestellt: pro Begriff erscheint oben der Hauptglossar-
Inhalt, darunter — falls vorhanden — der Subglossar-Inhalt.

## Vier Cluster (IFC-naher Aufbau)

Die Einträge sind in vier Cluster gegliedert, deren Schnitt sich an
der IFC-Schichtung (`IfcResource`/`IfcCore`/`IfcInteroperability`/
`IfcDomain`) orientiert:

| Cluster | Inhalt |
|---|---|
| **Ressourcen** | Primitive Geometrie, Mathematik, Bauteil-Geometrie, Toleranz-Konstanten — alles ohne globale Identität, im Code als Werte-Typen geführt. |
| **Kern** | Abstrakte identitätstragende Wurzeln (Element, Bauteil, Bauwerk) und Identifikations-Begriffe (UUID, Positionsnummer, Produktkennzeichnung). |
| **Tragwerk** | Tragwerks-Aggregate, Statik-Begriffe, Verbindungs-Konzepte — werkstoffneutral. |
| **Holzbau** | Holz-spezifische Bauteilrollen, Werkstoffe, Bearbeitungen, Dach-Anatomie. |

Ein Eintrag lebt in dem Cluster, in dem sein engster Oberbegriff
lebt; bei polyhierarchischen Spannungen entscheidet die fachlich
engere Heimat, der breitere Bezug wird per Abgrenzung dokumentiert.

## Status der Schärfung

Das Glossar wird wellenweise gepflegt: jede Welle nimmt ein Bündel
inhaltlich zusammenhängender Begriffe auf, schliesst danach eine
Kohärenzprüfung über den Bestand ab und behebt erkannte Drifts.
Einträge tragen einen Status (`entwurf`, `in_revision`, `final`) und
einen Reife-Marker zur Quellen-Disziplin. Die Webseite bildet den
jeweils aktuellen Stand des Quell-Repos ab.

## Verbindliche Konventions-Quellen

Diese Methode-Seite ist die menschenlesbare Zusammenfassung. Die
verbindlichen Konventions-Dateien werden im internen Hauptprojekt
geführt:

| Konvention | Im Hauptprojekt | Auf dieser Site einsehbar? |
|---|---|---|
| **Hauptglossar-Konventionen** | `hauptglossar/HG_KONVENTIONEN.md` | ✓ [HG-Konventionen (Volltext)](hg-konventionen.md) |
| **Subglossar-Konventionen** — didaktische Hülle, SVG-Skizzen-Pattern, Stufen-Pattern, App-Verantwortungs-Trennung | `theorie/subglossar/SG_KONVENTIONEN.md` | nicht publiziert |
| **Recherche-Standard** — Tier-System, Methodik-Sektion, Falsifizier-Bereitschaft, Berichts-Persistenz | `docs/recherche/README.md` | als [Recherche-Standard](recherche.md) zusammengefasst |
| **Welle-Logs Hauptglossar** | `hauptglossar/STAND_HAUPTGLOSSAR.md` | nicht publiziert |
| **Welle-Logs Subglossar** | `theorie/subglossar/SUBGLOSSAR_STAND.md` | nicht publiziert |

Bei Konflikt zwischen dieser Seite und einer Konventions-Datei gilt
die Konventions-Datei. Die Seite wird angepasst, nicht der Konvention
widersprochen.

Das **Site-Repo** unter
[github.com/steinerschueler/holzbau-glossar](https://github.com/steinerschueler/holzbau-glossar)
liefert den Inhalt aus, der hier publiziert wird (`hg_*.md`, `sg_*.md`
unter `content/`, plus die freigegebene Konventionsdatei). Es ist
nicht das Hauptprojekt — das Hauptprojekt trägt zusätzlich Domain-
Code, Tests, Tooling, interne Recherche-Aufträge und ist derzeit
nicht öffentlich publiziert. Wer für eine wissenschaftliche oder
normungstechnische Auswertung Einsicht in eine zusätzliche
Konventions-Datei oder einen bestimmten Recherche-Bericht braucht,
kann das gerne über die Kontaktangabe im [Impressum](../impressum.md)
anfragen.
