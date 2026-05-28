---
title: Methode
description: Wie das Glossar arbeitet — Aufbau, Begriffstypen, Quellen-Hierarchie, Cluster-Logik.
---

# Methode

Diese Seite beschreibt, wie das Glossar arbeitet. Sie ist gedacht für
Leser, die einen Eintrag zitieren, weiterverwenden oder die Methodik
rückwirkend prüfen wollen — Forschende, Normungs-Gremien, Entwickler an
CAD-Werkzeugen.

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
  Block setzt nichts voraus, der Meister-Block schliesst an Tragwerks-
  Sprache an. Die Ingenieur-Stufe wird nicht im Subglossar gespiegelt,
  sondern direkt aus dem Hauptglossar bedient.

Beide Schichten verweisen aufeinander. Auf der Webseite werden sie
verschränkt dargestellt: pro Begriff erscheint oben der Hauptglossar-
Inhalt, darunter — falls vorhanden — der Subglossar-Inhalt.

## Vier Cluster (IFC-naher Aufbau)

Die Einträge sind in vier Cluster gegliedert, deren Schnitt sich an der
IFC-Schichtung (`IfcResource`/`IfcCore`/`IfcInteroperability`/`IfcDomain`)
orientiert:

| Cluster | Inhalt |
|---|---|
| **Ressourcen** | Primitive Geometrie, Mathematik, Bauteil-Geometrie, Toleranz-Konstanten — alles ohne globale Identität, im Code als Werte-Typen geführt. |
| **Kern** | Abstrakte identitätstragende Wurzeln (Element, Bauteil, Bauwerk) und Identifikations-Begriffe (UUID, Positionsnummer, Produktkennzeichnung). |
| **Tragwerk** | Tragwerks-Aggregate, Statik-Begriffe, Verbindungs-Konzepte — werkstoffneutral. |
| **Holzbau** | Holz-spezifische Bauteilrollen, Werkstoffe, Bearbeitungen, Dach-Anatomie. |

Ein Eintrag lebt in dem Cluster, in dem sein engster Oberbegriff lebt;
bei polyhierarchischen Spannungen entscheidet die fachlich engere
Heimat, der breitere Bezug wird per Abgrenzung dokumentiert.

## Begriffstypen

Jeder Eintrag trägt genau einen von acht Begriffstyp-Werten. Die Wahl
ordnet den Eintrag einer strukturellen Rolle im Begriffssystem zu, die
orthogonal zur fachlichen Spezialisierungs-Linie (Oberbegriff) ist.

| Wert | Bedeutung |
|---|---|
| `primitiv` | Unzerlegbares Konzept ohne weitere innere Struktur (Tupel von Skalaren, keine eigenen Subtypen). Beispiele: Punkt, Vektor, Gerade. |
| `generisch` | Eigenständiges Konzept mit interner Struktur, ggf. mit Subtypen, aber ohne Komposition aus mehreren Trägerbegriffen. Beispiele: Ebene, Polygon, Werkstoff. |
| `aggregat` | Komposition mehrerer eigenständiger Begriffe mit eigener Identität (UUID); trägt Konsistenzbedingungen über der Komposition. Beispiele: Verbindung, Tragwerk, Dach. |
| `partitiv` | Strenger Bestandteil eines Trägerbegriffs ohne eigenständige Existenz; Lebenszyklus an den Träger gekoppelt. Beispiele: Bearbeitung, Lage, Lagenstruktur. |
| `relation` | Beziehung zwischen Trägerbegriffen ohne eigene partitive Komposition. Beispiel: Bausystem als Mitgliedschafts-Sicht. |
| `bauteilrolle` | Konstruktiv definierter Bauteil-Subtyp mit rollenspezifischen geometrischen Constraints. Beispiele: Sparren, Pfette, Fusspfette. |
| `merkmal` | Eigenschaft oder Annotation an einem Trägerbegriff — ein **Wert**, kein **Objekt**. Beispiele: Faserrichtung, Dachneigung. |
| `hilfsbegriff` | Infrastrukturelle Festlegung der Geometrie-Schicht selbst, von vielen Begriffen vorausgesetzt. Beispiele: Toleranzen, Weltkoordinatensystem. |

Die Trennlinien sind im Hauptglossar präzisiert; bei Konflikt zwischen
einem Eintrag und der Begriffstyp-Tabelle wird der Eintrag korrigiert,
nicht die Tabelle.

## Quellen-Hierarchie und Einsehungs-Status

Norm- und Lehrbuch-Verweise tragen einen **Einsehungs-Status**, der
sichtbar macht, ob die Quelle direkt im Volltext eingesehen wurde,
nur in Vorschau-Form vorlag oder über eine Sekundärquelle
rekonstruiert ist.

| Marker | Bedeutung |
|---|---|
| (kein Marker) | via Sekundärquelle rekonstruiert (Default) |
| `[direkt]` | Volltext direkt eingesehen |
| `[einsicht: vorschau-pdf]` | nur kostenlose Vorschau eingesehen (Inhaltsverzeichnis, Auszug) |
| `[einsicht: snippet]` | nur Snippet direkt eingesehen (Google-Books, Suchergebnis-Snippet mit zitiertem Wortlaut) |
| `[via: <Quelle>]` | konkrete Sekundärquelle benannt |

Hintergrund: Norm-Volltexte sind häufig paywalled. Recherche
rekonstruiert ihre Aussagen oft aus Sekundärquellen — das ist
fachlich tragfähig, muss aber transparent sein. Der Default
„via Sekundärquelle" reflektiert die ehrliche Voreinstellung:
solange Direkteinsicht nicht ausgewiesen ist, gilt die Quelle als
nicht direkt verifiziert.

Wikipedia und vergleichbare Korpus-Quellen sind grundsätzlich
Sekundärlit, nicht Primärquelle.

## Abgrenzung gegen Geschwister-Begriffe

Jeder Eintrag dokumentiert seine Abgrenzung zu fachlich benachbarten
Begriffen explizit. Die Felder `abgrenzung_zu:`,
`abgelehnte_benennungen:` und der Quellenkonflikt-Block bilden zusammen
ein engmaschiges Trenn-Geflecht, das Begriffsdrift in der Praxis
sichtbar macht und gegen den korrekten Eintrag leitet.

Forward-Verweise — Abgrenzungen gegen Begriffe, die noch keinen
eigenen Eintrag haben — sind im `abgrenzung_zu:`-Feld zulässig, in
`voraussetzungen:` nicht. Begründung: Abgrenzungen benötigen den
abzugrenzenden Begriff nicht definitorisch, sondern nur als Ankerwort;
Voraussetzungen dagegen tragen die zirkelfreie Aufbaureihenfolge des
Glossars und müssen auf existierende Einträge zeigen.

## Eine Sprachregel: senkrecht, rechtwinklig, orthogonal

Im Glossar wird **„rechtwinklig"** oder **„im rechten Winkel zu"**
verwendet, wenn ein 90°-Winkel zwischen zwei geometrischen Objekten
gemeint ist (relationale Bedeutung). **„Senkrecht"** ist ausschliesslich
für **„lotrecht"** reserviert — in Fallrichtung eines losgelassenen
Gegenstands. **„Orthogonal"** ist Synonym zu „rechtwinklig", wenn der
mathematische Kontext es nahelegt.

Begründung: „Senkrecht" hat im Deutschen zwei nicht zur Deckung zu
bringende Bedeutungen — relational und absolut. Im Holzbau-Kontext, in
dem zugleich vom Welt-Koordinatensystem und von Bauteil-Lokalsystemen
die Rede ist, führt diese Mehrdeutigkeit zu vermeidbarer Unklarheit.

Die zimmermannssprachlichen Realisierungen der absoluten Lot-Bezogenheit
— **Senkel** (parallel zur Lotachse) und **Bleischnitt** (rechtwinklig
zur Lotachse) — sind als eigene Glossarbegriffe geführt und ersetzen
die mehrdeutigen Wortlauten „vertikaler Schnitt" / „horizontaler
Schnitt".

## Status der Schärfung

Das Glossar wird wellenweise gepflegt: jede Welle nimmt ein Bündel
inhaltlich zusammenhängender Begriffe auf, schliesst danach eine
Kohärenzprüfung über den Bestand ab und behebt erkannte Drifts.
Einträge tragen einen Status (`entwurf`, `in_revision`, `final`) und
einen Reife-Marker zur Quellen-Disziplin. Die Webseite bildet den
jeweils aktuellen Stand des Quell-Repos ab.
