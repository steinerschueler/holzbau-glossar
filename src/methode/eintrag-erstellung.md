---
title: Eintrag-Erstellung
description: Welle-Workflow von Recherche-Auftrag bis Subglossar-Pendant.
---

# Eintrag-Erstellung

Begriffserstellung verläuft in einer festen Welle-Logik. Jede Welle
bündelt fachlich verwandte Begriffe und durchläuft denselben Pfad:

1. **Recherche-Auftrag** — kurzer Brief unter `docs/auftraege/`:
   Fragestellung, Kontext, Abgrenzung, gewünschtes Output-Format.
2. **Recherche-Bericht** — strukturierte Antwort unter
   `docs/recherche/<datum>_<kurztitel>.md`, gemäß dem
   [Recherche-Standard](recherche.md). Der Bericht ist
   nachvollziehbarer Beleg und bleibt erhalten, auch wenn er später
   überholt wird.
3. **Glossar-Eintrag** — die Begriffsfassung wird aus dem Bericht
   destilliert, in den HG-Cluster geschrieben, mit allen
   [Pflichtfeldern](begriffe.md#pflichtfelder-pro-eintrag) gefüllt.
4. **Kohärenz-Review** — nach jeder Welle wird der gesamte Bestand
   gegen die neue(n) Eintrag(/Einträge) geprüft: Geschwister-
   Abgrenzung, Cluster-Heimat, Voraussetzungs-Zykel, Benennungs-
   Drift. Erkannte Drifts werden in derselben Welle behoben, nicht
   aufgeschoben.
5. **Subglossar-Pendant** — wenn `theorie_pflichtig: required`, wird
   die didaktische Hülle in `theorie/subglossar/sg_<id>.md` parallel
   geschrieben.

Welle-Logs und Kohärenz-Befunde werden im Quellrepo unter
`hauptglossar/STAND_HAUPTGLOSSAR.md` und
`theorie/subglossar/SUBGLOSSAR_STAND.md` archiviert.

## Welle als Einheit

Eine Welle ist die kleinste publizierbare Einheit. Ein einzelner
Eintrag in Isolation wird in der Regel nicht veröffentlicht — er
existiert nur als Bestandteil einer thematisch koherenten Welle,
die ihn fachlich einrahmt. Begründung: ein Begriff existiert in
Beziehung zu Nachbarbegriffen; Erstpublikation ohne diese
Nachbarschaft ist methodisch unscharf.

Ausnahmen sind isolierte Korrekturen an einem bereits publizierten
Eintrag (Tippfehler, Norm-Aktualisierung, Quelle nachgereicht). Sie
laufen als „Pflege-Mini-Welle" und werden in derselben Stand-Datei
geloggt, aber ohne neue Versions-DOI.

## Kohärenz-Review im Detail

Nach jeder Welle prüft der Kohärenz-Review fünf Punkte am gesamten
Bestand:

1. **Geschwister-Abgrenzung** — sind neue Einträge in
   `abgrenzung_zu:`-Listen der Nachbarn aufgenommen, wo fachlich
   relevant?
2. **Cluster-Heimat** — passen die neuen Einträge in den gewählten
   Cluster, oder sind sie polyhierarchisch zwischen mehreren
   Clustern verteilt?
3. **Voraussetzungs-Zykel** — entstehen durch neue
   `voraussetzungen:`-Verweise zirkuläre Abhängigkeiten?
4. **Benennungs-Drift** — verwendet ein neuer Eintrag eine
   Benennung, die in einem alten Eintrag als
   `abgelehnte_benennungen:` markiert ist?
5. **Math-Notations-Konformität** — folgen neue Einträge der
   Math-Konvention (§11 in HG-Konventionen), oder schleichen sich
   Combining-Diakritika ein?

Bei jeder gefundenen Drift wird **in derselben Welle** korrigiert.
Aufschieben einer erkannten Drift in eine spätere Welle ist
ausdrücklich nicht zulässig.
