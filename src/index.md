---
title: Holzbau-Glossar
description: Präzises, normativ belegtes Glossar zum Holzbau — frei zugänglich.
---

# Holzbau-Glossar

In einer Welt, in der **Information frei** und **Begriffe exakt** sind,
lässt sich leichter Schönes bauen. Dieses Glossar will Begriffe rund
um den Holzbau möglichst präzise definieren — und die Ergebnisse frei
für jeden verfügbar machen.

## Was dieses Glossar kann

- **Begriffe normativ belegen.** Jede Definition stützt sich auf
  überprüfbare Quellen (SIA, DIN, EN, ÖNORM, Lignum HBT, anerkannte
  Lehrbücher). Wo Direkteinsicht in die Norm möglich war, ist das
  ausdrücklich markiert; wo nicht, ist die Sekundärquelle benannt.
- **Begriffe gegeneinander abgrenzen.** Pro Eintrag werden
  Geschwister-Begriffe explizit aufgezählt, mit klarer Trennung. Was
  oft mit einem anderen Wort verwechselt wird, steht als „abgelehnte
  Benennung" sichtbar daneben.
- **Quellen-Konflikte explizit machen.** Wenn die Norm-Quelle und die
  Lehrbuch-Tradition auseinanderlaufen, wird der Konflikt nicht
  verschwiegen, sondern als Block dokumentiert und entschieden.
- **DACH-Sprache ernst nehmen.** Schweizer, deutsche und österreichische
  Benennungen kommen vor, regionale Varianten werden als Synonyme
  aufgenommen — nicht als „falsch" abgetan.
- **Frei nutzbar bleiben.** Inhalte unter [CC BY 4.0](lizenz.md):
  Übernahme in Lehrbücher, Schulungs-Skripte, kommerzielle Werkzeuge
  (cadwork, ArchiCAD, SketchUp), wissenschaftliche Arbeiten und
  Forschungs-Pipelines — ohne separate Lizenz.
- **Persistent zitierbar sein.** Jedes Release bekommt einen
  [DOI](zitieren.md) über Zenodo (CERN, ≥ 20 Jahre Aufbewahrung). Die
  Adresse gilt auch dann noch, wenn `holzbau-glossar.ch` einmal nicht
  mehr erreichbar wäre.
- **Maschinenlesbar sein.** Eine [statische JSON-API](api.md) liefert
  alle Einträge, Synonyme und Beziehungen für Apps, IDE-Plugins und
  Forschungs-Pipelines — ohne Token, ohne Anmeldung.
- **Zwei Lese-Schichten anbieten.** Das Hauptglossar trägt die
  präzise normative Definition (Forschung, Normungs-Arbeit). Das
  Subglossar paraphrasiert dieselbe Begriffsfassung in zugänglicher
  Sprache (Ausbildungs-Stufen Schnuppi, Lehrling, Polier, Meister) —
  mit SVG-Skizzen und benannten Praxis-Beispielen.
- **Transparent über die eigene Methode sein.** Welle-Workflow,
  Quellen-Disziplin, Recherche-Standard und die volle
  Hauptglossar-Konventionsdatei sind unter [Methode](methode/index.md)
  öffentlich einsehbar. Auch der [Privacy-Stand der Webseite](datenschutz.md)
  selbst ist bei jedem Build neu maschinell belegt.

## Was es nicht kann

- **Kein Holzbau-Lehrbuch.** Das Glossar definiert Begriffe; es lehrt
  den Holzbau nicht systematisch vom Sparren-Aufmaß bis zum
  Dachstuhl. Für Lehrgang und Schulbuch sind weiter Tibbs, Mönck/Rug,
  Holzbau-Atlas und die Lignum-Reihe die richtigen Adressen.
- **Keine Bemessung, keine Statik.** Werte werden nicht berechnet,
  Bauteile nicht dimensioniert. Eurocode 5, SIA 265 und die
  zugehörigen Software-Werkzeuge bleiben dafür zuständig.
- **Keine Material-Datenblätter.** Festigkeitsklassen, Quellmaße,
  k-mod-Werte und ähnliche Kennwerte stehen in den Normen und in
  Hersteller-Datenblättern, nicht hier.
- **Kein Norm-Ersatz.** Die zitierten Normen bleiben verbindlich. Das
  Glossar paraphrasiert ihre Begriffsfassung im definitorischen Kern,
  ersetzt aber weder Anwendungs-Regeln noch die Pflicht zur
  Originaleinsicht im rechtlich relevanten Fall.
- **Kein Marktplatz, keine Hersteller-Empfehlung.** Wo Marken-Namen
  fallen (cadwork, ArchiCAD), dann nur als Anwendungs-Beispiel, nicht
  als Kaufempfehlung. Es gibt keinen Vergleichs-Test, keine Tabelle
  „bester Anbieter".
- **Keine Rechtsberatung.** Konflikte zwischen Bauherr, Architekt und
  Zimmerei lassen sich nicht über Begriffsklärung lösen — das Glossar
  klärt die Worte, nicht die Verträge.
- **Keine Vollständigkeit.** Das Glossar wird wellenweise gepflegt
  und bleibt absehbar in Bewegung. Ein fehlender Begriff heisst nur,
  dass er noch nicht dran war — nicht, dass er nicht definiert
  werden könnte. Lücken zeigt der [A-Z-Index](index-az.md).

## Aufbau

Die Einträge sind in vier Cluster gegliedert, deren Schnitt sich an
der IFC-Schichtung orientiert:

- **Ressourcen** — geometrische Primitive, Mathematik, Toleranzen.
- **Kern** — Element, Bauteil und andere identitätstragende Wurzeln.
- **Tragwerk** — Tragwerk-Aggregate, Verbindungen, werkstoffneutrale
  Bauteil-Wurzeln.
- **Holzbau** — Bauteilrollen, Werkstoffe, Dach-Anatomie und alles
  holz-spezifische.

Jeder Eintrag liefert zusätzlich zur HTML-Ansicht eine Markdown-,
Plain-Text- und BibTeX-Quelle zum Direkt-Zitieren. Details:
[Methode](methode/index.md) · [DOI (Zitieren)](zitieren.md) ·
[API (Einbinden)](api.md) · [Lizenz](lizenz.md).

## Stand

Aktueller Bestand: **122 Hauptglossar-Einträge** und
**9 Subglossar-Einträge** in vier Clustern. Das Glossar wird
wellenweise erweitert; eine Welle umfasst typischerweise einen
fachlich zusammenhängenden Block von Begriffen plus eine
Kohärenz-Prüfung über den gesamten Bestand. Welle-Logs werden im
Quellrepo geführt; das jeweils publizierte Release hängt am
Versions-DOI im Footer.

Inhalte stehen unter CC BY 4.0. Concept-DOI:
[10.5281/zenodo.20435319](https://doi.org/10.5281/zenodo.20435319).
