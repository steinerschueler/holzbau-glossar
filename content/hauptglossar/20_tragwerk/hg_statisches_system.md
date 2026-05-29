---
id: statisches_system
benennung: Statisches System
synonyme: [Tragwerksmodell, Stabwerksmodell, Strukturmodell]
abgelehnte_benennungen:
  - Bemessungsmodell
  - Idealisierung
  - "FE-Modell"
  - "Finite-Elemente-Modell"
  - Modell
  - "static system"
  - "structural system"
  - "structural model"
  - "analysis model"
oberbegriff: null
begriffstyp: aggregat
voraussetzungen:
  - tragwerk
  - bauteil
  - bauteilachse
  - auflager
  - punkt
  - vektor
  - gerade
  - strecke
  - uuid
  - weltkoordinatensystem
  - toleranzen
abgrenzung_zu:
  - tragwerk
  - bauteil
  - bauteilachse
  - auflager
  - verbindung
  - lastfall
  - fe_modell
  - knoten
  - stab
status: entwurf
subglossar_pendant: notwendig
quellen_primär:
  - "ISO 16739-1:2024 'Industry Foundation Classes (IFC) – Part 1: Data schema' (IFC 4.3), Structural-Analysis-Domain: `IfcStructuralAnalysisModel` (Wurzel-Entität der analytischen Schicht), `IfcStructuralItem` (abstrakt) mit `IfcStructuralMember` (Subtypen `IfcStructuralCurveMember`, `IfcStructuralSurfaceMember`) und `IfcStructuralConnection` (Subtypen Point/Curve/Surface); `IfcStructuralActivity` (Subtypen `IfcStructuralAction`, `IfcStructuralReaction`); `IfcStructuralLoadGroup` und `IfcStructuralResultGroup`; `IfcRelAssignsToProduct` als physisch-analytische Brücke zwischen `IfcStructuralMember` und `IfcBeam`/`IfcColumn`/`IfcWall`."
  - "DIN EN 1990:2010-12 'Eurocode: Grundlagen der Tragwerksplanung', Abschnitt 1.5.1.7 'Tragwerksanalyse' (Modellierungs-Schritt vom Tragwerk zur idealisierten Berechnungsschicht); Sekundärrezeption über `hg_tragwerk.md`, Volltext nicht frei zugänglich."
  - "DIN EN 1995-1-1:2010-12 (Eurocode 5), Abschnitt 5 'Tragwerksberechnung' (Stab- und Stabwerk-Idealisierung operativ vorausgesetzt)."
  - "SIA 260:2013 'Grundlagen der Projektierung von Tragwerken', Abschnitt 2 (Begriffe) und Abschnitt 4 (Tragwerksanalyse); Sekundärrezeption."
  - "DIN 1052:2008-12, Abschnitt 5 (Berechnungsverfahren)."
quellen_sekundär:
  - "Krätzig, W. B.; Wittek, U.; Harte, R.; Meskouris, K.: Tragwerke 1 / Tragwerke 2. Springer (VDI-Buch), Berlin/Heidelberg, mehrere Auflagen, Kapitel 'Das Tragwerksmodell der Statik der Tragwerke' — explizite Modellbildung vom realen Tragwerk zum idealisierten Stabwerk."
  - "Petersen, Chr.: Statik und Stabilität der Baukonstruktionen. Vieweg, Braunschweig — Lehrbuch-Standard zur Wertigkeits-Klassifikation und zur statischen Bestimmtheit."
  - "Schneider, K.-J.; Albert, A.: Bautabellen für Ingenieure. 26. Aufl., Bundesanzeiger Verlag, Köln 2024, Auflager-Klassifikation und Abzählformeln für Stabwerke."
  - "Mönck, W.; Rug, W.: Holzbau – Bemessung und Konstruktion. 16. Aufl., Beuth, Berlin 2015, Kap. 11 'Dachtragwerke' (Stab-Idealisierung der Sparrenpaare und Pfettendächer)."
  - "Blass, H. J.; Sandhaas, C.: Ingenieurholzbau – Grundlagen der Bemessung. KIT Scientific Publishing, Karlsruhe 2016, Kap. 5 'Stab-Bauteile'."
  - "Wikipedia, Lemma 'Baustatik' (abgerufen 2026-05-14): „In der Statik wird das reale Bauwerk durch ein Modell abgebildet, das als ‚Statisches System‘ bezeichnet wird.“"
  - "Wikipedia, Lemma 'Stabwerk (Technische Mechanik)' (abgerufen 2026-05-14): „ein ebenes oder räumliches Tragwerk, das aus mehreren, miteinander verbundenen schlanken Stäben besteht“."
  - "Wikipedia, Lemma 'Lager (Statik)' (abgerufen 2026-05-14): Lager als „abstrahierte Verbindungen zwischen einem Starrkörper (Tragwerk) und seiner Umgebung“."
  - "Wikipedia, Lemma 'Statische Bestimmtheit' (abgerufen 2026-05-14): Abzählformeln eben/räumlich, notwendiges versus hinreichendes Kriterium."
  - "buildingSMART, IFC-4.3.2-Dokumentation Structural-Analysis-Domain, Lexical-Einträge `IfcStructuralAnalysisModel` und `IfcRelAssignsToProduct` (Sekundärrezeption über WebSearch-Snippets, da WebFetch der buildingSMART-Seiten in der Recherche verweigert wurde)."
  - "Recherche-Bericht `docs/recherche/2026-05-14_hg_statisches_system.md`."
quellenkonflikt: |
  **Normlücke.** Keine der konsultierten deutschsprachigen Tragwerks-
  Normen — SIA 260:2013, SIA 265:2021, DIN EN 1990:2010-12,
  DIN EN 1995-1-1:2010-12, DIN 1052:2008-12 — enthält eine
  geschlossene Begriffs-Definition von „statisches System“. Der
  Begriff wird durchgängig vorausgesetzt; SIA 260 und DIN EN 1990
  führen lediglich „Tragwerksanalyse“ als Modellierungs-Schritt
  vom Tragwerk zur Berechnungsschicht. Die Quellenlage ist damit
  parallel zur Lage bei `hg_auflager.md` und `hg_tragwerk.md`.

  Eine geschlossene Definition findet sich ausschließlich (i) in
  der Statik-Lehrbuchliteratur (Krätzig/Wittek mit dem Kapitel
  „Das Tragwerksmodell der Statik der Tragwerke“; Petersen;
  Schneider/Albert; Wikipedia „Baustatik“: „In der Statik wird das
  reale Bauwerk durch ein Modell abgebildet, das als ‚Statisches
  System‘ bezeichnet wird“) und (ii) im **IFC-4.3-Schema** als
  geschlossene Entitäten-Familie (`IfcStructuralAnalysisModel`
  als Wurzel; `IfcStructuralCurveMember` / `…SurfaceMember` /
  `IfcStructuralConnection` als Bestandteile; `IfcStructuralAction`
  / `…Reaction` als Einwirkungen und Ergebnisse;
  `IfcRelAssignsToProduct` als explizite Brücke zwischen
  analytischer und physischer Schicht).

  **App-Festlegung — Eigenleistung.** Das statische System wird
  in diesem Glossar als App-eigene formale Festlegung eingeführt,
  konsistent mit allen konsultierten Quellen:

  - Das **Tragwerk** (siehe `hg_tragwerk.md`) ist die
    **bauteilbezogene Realität** im Weltkoordinatensystem
    (Bauteil-Polyeder, Verbindungen, Auflager-Manifestationen,
    Lastfälle).
  - Das **Statische System** (dieser Eintrag) ist die
    **bemessungstechnische Idealisierung** desselben physischen
    Substrats: Knoten als Punkte in W, Stäbe als gerichtete
    Trägerstrecken der Bauteilachsen mit Endknoten-Inzidenz,
    Auflager mit Wertigkeit pro Freiheitsgrad, Einwirkungen als
    Lastfall-Menge, plus Berechnungs-Theorie-Annahme (I./II./
    III. Ordnung).

  Beide stehen in einer Abstraktions-Relation; das statische
  System verweist über sein Feld `basistragwerk` auf die UUID des
  zugehörigen Tragwerks (analog zur IFC-Brücke
  `IfcRelAssignsToProduct`). Diese App-Festlegung greift die
  Drei-Schichtung Bearbeitung / Auflagefläche / Auflager aus
  `hg_auflager.md` strukturell auf: dort die Trennung am einzelnen
  Stützungs-Ort, hier die Trennung am gesamten Tragwerk.

  **Begriffstyp.** `aggregat` ist eindeutig (analog `verbindung`,
  `auflager`, `tragwerk`): das statische System trägt eine eigene
  UUID, hat eigene partitive Bestandteile (Knoten-Menge,
  Stab-Menge, übernommene Auflager- und Lastfall-Mengen,
  Berechnungs-Theorie) und eigene Konsistenzbedingungen über der
  Komposition (Knoten-Stab-Inzidenz, Stab-Bauteilachsen-
  Konsistenz, Auflager-Knoten-Inzidenz, Konsistenz mit dem
  Basistragwerk).

  **Oberbegriff — bewusste Entscheidung für `null`.** Die
  Recherche (`docs/recherche/2026-05-14_hg_statisches_system.md`
  Abschnitt G.2) hat die Wahl zwischen `null` und `tragwerk` als
  Diskussions-Punkt für die Hauptinstanz herausgearbeitet. Hier
  wird `null` gesetzt mit drei zusammenwirkenden Gründen:

  1. **Strukturparallelität** zu `auflager` und `verbindung`,
     die beide `begriffstyp: aggregat` und `oberbegriff: null`
     tragen. Diese drei Aggregate bilden die App-eigene Linie
     ontologisch eigenständiger Abstraktions-Sichten neben den
     Element-Linien (Bauteil-Hierarchie) und neben der
     funktional-aggregativen Linie (`tragwerk` als Subtyp von
     `bausystem`).
  2. **IFC-4.3-Schema-Lesart**: das statische System ist dort
     **nicht** Subtyp eines physischen Pendants, sondern eigene
     Wurzel-Entität `IfcStructuralAnalysisModel` mit
     `IfcRelAssignsToProduct` als **expliziter Brücke** zur
     physischen Schicht — die schema-feste Bestätigung der
     parallelen Lesart.
  3. **Sicht-Charakter**: das statische System ist eine
     **Abstraktions-Sicht** auf das Tragwerk, nicht eine
     Spezialisierung im fachlichen Sinne. Eine Spezialisierung
     `oberbegriff: tragwerk` würde implizieren, dass das
     statische System „ein besonderes Tragwerk“ sei; sachlich
     ist es jedoch eine **andere Lesart** desselben physischen
     Substrats — Krätzig/Wittek schreiben „Tragwerksmodell **der**
     Statik der Tragwerke“, der Genitiv markiert die
     Modell-Relation, nicht die Subsumtion.

  Die Abhängigkeit zum Tragwerk bleibt durch das Tupel-Feld
  `basistragwerk` ∈ 𝒰 (UUID des zugehörigen Tragwerks) explizit
  und prüfbar; sie wird nicht zur Hierarchie erhoben.

  **Erweiterung um 2D-Flächenelemente.** Die Recherche hat als
  Erweiterung gegenüber dem Auftragstext die `IfcStructural-
  SurfaceMember`-Pendants (Platten, Scheiben, Schalen) als
  zweiten Member-Zweig benannt. Diese werden im Tupel als
  optionale Menge `F` (Flächenelemente) geführt; im aktuellen
  App-Stand ist `F = ∅` Default, weil die App heute keine 2D-
  Idealisierung modelliert (`hg_bauteilachse.md` deckt nur den
  Stab-Fall ab). Die Aufnahme der Surface-Member-Familie ist
  Folgearbeit, sobald ein Flächenbauteil-Pendant zur Bauteilachse
  („Bezugsfläche“) angelegt wird.

  **Hauptbenennung „Statisches System“ vs. „Tragwerksmodell“.**
  Krätzig/Wittek favorisieren „Tragwerksmodell“; Wikipedia und
  die App-Tradition favorisieren „Statisches System“. Die
  App-Hauptbenennung ist „Statisches System“ (quellen-konsistent
  zur Wikipedia-Definition und zur App-Tradition); „Tragwerks-
  modell“, „Stabwerksmodell“ und „Strukturmodell“ sind als
  Synonyme geführt. „Stabwerksmodell“ ist als Hauptbenennung zu
  eng (schließt Flächenelemente aus), wird aber als Synonym
  akzeptiert, weil es im App-aktuellen Stand mit `F = ∅`
  bedeutungsgleich ist.

  **Abgrenzung zu FE-Modell.** Das **FE-Modell** (Finite-
  Elemente-Modell) ist die **numerische Diskretisierung** des
  statischen Systems für eine Computer-Berechnung (Knotenanzahl,
  Elementtyp, Netzweite, Lösungsverfahren). Es ist eine weitere
  Stufe der Verfeinerung über dem statischen System, kein
  Synonym. Im aktuellen App-Plan ist `fe_modell` nicht als
  eigener Hauptglossar-Eintrag vorgesehen (HG §6 (D)-Kategorie:
  Korpus-Begriff dauerhaft ohne eigenen Eintrag); der
  Forward-Verweis bleibt in `abgrenzung_zu:` stehen.

  **BTLx.** Das design2machine-Schema BTLx kennt **keine eigene
  Entität** für das statische System; Bemessungs-Information
  erscheint dort nicht. Analog `hg_verbindung.md` und
  `hg_auflager.md`: IFC 4.3 ist der einzige Industriestandard mit
  expliziter Pendant-Familie.
---

## Prosa-Definition

Ein **Statisches System** ist ein Aggregat aus einer endlichen
Menge von Knoten im Weltkoordinatensystem, einer endlichen Menge
gerichteter Stäbe, deren Trägerstrecken aus den Bauteilachsen
eines zugehörigen Tragwerks gewonnen sind und deren Endpunkte in
der Knotenmenge liegen, einer aus dem zugehörigen Tragwerk
übernommenen Menge von Auflagern mit Wertigkeit pro Freiheitsgrad,
einer aus dem zugehörigen Tragwerk übernommenen Menge von
Lastfällen, einer Berechnungs-Theorie-Annahme und einer
Referenz auf das Basistragwerk, das die bemessungstechnische
Idealisierung des Tragwerks als Punkt-Stab-Modell für die
Tragwerksanalyse darstellt, eine eigene technische Identität
trägt und sich vom Tragwerk als bauteilbezogener Realität
durch seinen Charakter als Abstraktions-Sicht unterscheidet.

## Mathematische Definition

Sei

- W das Weltkoordinatensystem (siehe `hg_weltkoordinatensystem.md`),
- 𝒰 der UUID-Raum nach `hg_uuid.md`,
- 𝒯 die Menge der Tragwerke nach `hg_tragwerk.md`,
- 𝓑 die Menge der Bauteile nach `hg_bauteil.md`,
- 𝓐 die Menge der Auflager nach `hg_auflager.md`,
- 𝓛 die (sammelbegrifflich geführte) Menge der Lastfälle nach
  EN 1990 / EN 1991 bzw. SIA 260 / SIA 261 (eigener Eintrag
  `lastfall` folgt; im aktuellen Glossarstand Forward-Verweis),
- 𝓟_W ⊂ ℝ³ die Menge der Punkte in W,
- 𝓢_W die Menge der Strecken in W nach `hg_strecke.md`.

### Knoten und Stäbe

Ein **Knoten** des statischen Systems ist ein Punkt k ∈ 𝓟_W mit
eigener Identität innerhalb des Systems. Die Knotenmenge K ist
eine endliche Teilmenge von 𝓟_W; identische geometrische Punkte
(im Sinne von `LAENGE_EPS`) werden zu **einem** Knoten
kontrahiert (siehe Wohldefiniertheit, Knoten-Kontraktion).

Ein **Stab** des statischen Systems ist das Tripel

```
m := (uuid_m, traegerstrecke, basisbauteil)
```

mit

- **uuid_m** ∈ 𝒰: Identität des Stabes innerhalb des Systems,
- **traegerstrecke** ∈ 𝓢_W: die gerichtete Strecke des Stabes
  in W (Anfang und Ende ∈ K),
- **basisbauteil** ∈ 𝒰: UUID des Bauteils b ∈ 𝓑, dessen
  Bauteilachse die Trägerstrecke geometrisch definiert.

Die Menge aller Stäbe ist M; die Endpunkte jedes Stabes liegen
in K (Inzidenz-Bedingung S1, siehe unten).

Optional kann das System eine Menge **F** von Flächenelementen
führen (Pendant zu `IfcStructuralSurfaceMember`, Folgearbeit;
im aktuellen App-Stand `F = ∅`). F wird im Tupel als optionale
Komponente mit Default-Wert ∅ geführt.

### Berechnungs-Theorie

Sei 𝓣ʜ die Menge der **Berechnungs-Theorie-Annahmen** des
statischen Systems:

```
𝓣ʜ := { linear_erster_ordnung,
        geometrisch_nichtlinear_zweiter_ordnung,
        materiell_nichtlinear,
        voll_nichtlinear_dritter_ordnung }.
```

Die App-Default-Wahl ist `linear_erster_ordnung`.

### Tupel-Definition

Dann ist ein **Statisches System** das Tupel

```
S := (uuid, basistragwerk, K, M, F, A, L, theorie, bezeichnung)
```

mit den Komponenten

- **uuid** ∈ 𝒰: technische Identität des Systems als Aggregat,
- **basistragwerk** ∈ 𝒰: UUID des zugehörigen Tragwerks
  T ∈ 𝒯 (Pflicht; entspricht der physisch-analytischen Brücke
  `IfcRelAssignsToProduct`),
- **K** ⊂ 𝓟_W, K endlich, K ≠ ∅: die Knotenmenge,
- **M** endliche Menge von Stäben (m = (uuid_m, traeger, basisbauteil)),
- **F** endliche Menge von Flächenelementen (Default: ∅;
  Folgearbeit),
- **A** ⊂ 𝓐, A ⊆ T.A: die aus dem Basistragwerk übernommene
  Auflager-Menge,
- **L** ⊂ 𝓛, L ⊆ T.L: die aus dem Basistragwerk übernommene
  Lastfall-Menge,
- **theorie** ∈ 𝓣ʜ: die Berechnungs-Theorie-Annahme,
- **bezeichnung** ∈ String ∪ {⊥}: freier Anzeigename.

### Konsistenzbedingungen

(S1) **Knoten-Stab-Inzidenz**: für jeden Stab m ∈ M gilt
m.traegerstrecke.anfang ∈ K ∧ m.traegerstrecke.ende ∈ K
(im Sinne von `LAENGE_EPS`-Punkt-Identität).

(S2) **Stab-Bauteilachsen-Konsistenz**: für jeden Stab m ∈ M
existiert ein b ∈ T.B mit b.uuid = m.basisbauteil, und die
Trägerstrecke von m fällt im prismatischen Stab-Fall mit der
Bauteilachse von b (siehe `hg_bauteilachse.md`) zusammen — oder
ist im allgemeinen Fall eine zulässige Diskretisierung der
Bauteilachse (Polygonzug-Approximation gekrümmter
Bauteilachsen). Formal:

```
∀ m ∈ M : ∃ b ∈ T.B : b.uuid = m.basisbauteil
                    ∧ traegerstrecke(m) ≈ bauteilachse(b),
```

wobei „≈“ die `LAENGE_EPS`-Identität der Endpunkte im
prismatischen Fall ist und im gekrümmten Fall die zulässige
Approximation gemäss Diskretisierungs-Konvention.

(S3) **Auflager-Knoten-Inzidenz**: für jedes Punkt-Auflager
a ∈ A mit `a.manifestation.dimension = 0` gilt
a.manifestation.ort ∈ K. Für Linien- und Flächen-Auflager
(`dimension ∈ {1, 2}`) liegen die Trägerpunkte der Manifestation
auf Stäben in M (Inzidenz im `LAENGE_EPS`-Sinn auf der jeweiligen
Trägerstrecke); falls F ≠ ∅, alternativ auf Flächenelementen
in F.

(S4) **Konsistenz Auflager mit Basistragwerk**: A ⊆ T.A. Die
Auflager-Menge des statischen Systems ist eine Teilmenge der
Auflager-Menge des Basistragwerks. Identische UUIDs bedeuten
identisches Auflager; das statische System fügt keine neuen
Auflager hinzu, sondern wählt aus den Tragwerks-Auflagern aus
(typisch: A = T.A).

(S5) **Konsistenz Lastfälle mit Basistragwerk**: L ⊆ T.L
(analog zu S4).

(S6) **Knoten-Vollständigkeit**: jeder Knoten k ∈ K ist
mindestens **einmal inzident** — entweder Endpunkt eines Stabes
in M, Ort eines Punkt-Auflagers in A oder Endpunkt eines
Stützungs-Knotens eines Linien-/Flächen-Auflagers. Isolierte
Knoten (ohne Inzidenz) sind unzulässig.

(S7) **Stabilität als ableitbares Prädikat**
(Abzählformel-Notwendigkeitskriterium): das statische System
trägt eine ableitbare Eigenschaft `istStabil(): Boolean`. Die
Abzählformel im räumlichen Fall ist

```
n := a + s + z − 6 · k,
```

mit
- `a` = Σ der Auflagerwertigkeiten (Anzahl gesperrter
  Freiheitsgrade über alle Auflager in A),
- `s` = |M| (Anzahl der Stäbe),
- `z` = Anzahl der Zwischenreaktionen / Nebenbedingungen
  (Gelenke, Gleitsteine etc.; im aktuellen Stand 0, weil
  Stabgelenke nicht modelliert sind),
- `k` = |K| (Anzahl der Knoten).

Im ebenen Fall (Sonderfall der Projektion auf eine Ebene)
gilt entsprechend `n := a + s + z − 3 · k`. Die Interpretation
ist `n > 0` ⇒ n-fach statisch unbestimmt; `n = 0` ⇒ statisch
bestimmt (**notwendiges**, nicht hinreichendes Kriterium —
selbst bei n = 0 kann das System kinematisch verschieblich
sein, wenn die Auflager-Reaktionsachsen linear abhängig sind);
`n < 0` ⇒ kinematisch verschieblich. Das hinreichende
Kriterium ist die Nicht-Singularität der Koeffizientenmatrix
der Gleichgewichtsbedingungen, formuliert in der Bemessungs-
Schicht.

(S8) **Theorie-Konsistenz**: die gewählte Berechnungs-Theorie
muss mit den Werkstoff- und Schlankheits-Verhältnissen der
Bauteile in T.B konsistent sein (zugesichert, nicht hart
geprüft im Glossar; formaler Nachweis in der Bemessungs-
Schicht).

### Geometrische Punktmenge

Die geometrische Punktmenge des statischen Systems in W ist

```
G_W(S) := K ∪ ⋃_{m ∈ M} traegerstrecke(m) ∪ ⋃_{f ∈ F} flaeche(f)
                ⊂ ℝ³.
```

## Wohldefiniertheit

- **Existenz**: für jedes konkrete Tragwerk T ∈ 𝒯 lässt sich
  ein statisches System konstruieren. Die kanonische
  Konstruktion ist:
  1. Knotenmenge K := { p_a, p_e | für jede Bauteilachse von
     T.B } modulo `LAENGE_EPS`-Identität (Knoten-Kontraktion).
  2. Stab-Menge M := { (uuid_m, bauteilachse(b).strecke, b.uuid) |
     b ∈ T.B } für stabförmige Bauteile (geometrie ∈ 𝒢_stab in
     `hg_bauteil.md`-Lesart).
  3. F := ∅ (Default; Folgearbeit für Flächenbauteile).
  4. A := T.A; L := T.L.
  5. theorie := linear_erster_ordnung (Default).
  Diese kanonische Konstruktion ist Inhalt der Funktion
  `Tragwerk.statischesSystem()`, die in `hg_tragwerk.md`
  Implementierungshinweis als Folgearbeit angekündigt ist.

- **Eindeutigkeit der Identität**: die UUID des statischen
  Systems ist unabhängig von der UUID seines Basistragwerks
  und unabhängig von den UUIDs anderer Aggregate. Mehrere
  statische Systeme können auf demselben Basistragwerk
  aufsetzen — z. B. mit unterschiedlicher Berechnungs-Theorie
  (lineares System für Gebrauchstauglichkeit, geometrisch
  nichtlineares System für Stabilitätsnachweis); jedes ist
  eine eigene Aggregat-Instanz mit eigener UUID.

- **Knoten-Kontraktion** (Repräsentanten-Wohldefiniertheit):
  zwei geometrische Punkte p_1, p_2 ∈ 𝓟_W mit
  ‖p_1 − p_2‖ ≤ `LAENGE_EPS` werden bei der Konstruktion auf
  **denselben** Knoten in K abgebildet. Die Inzidenz-Bedingungen
  (S1, S3) verwenden die Knoten-Identität, nicht den
  geometrischen Punkt-Vergleich. Diese Konvention ist
  notwendig, weil zwei sich treffende Sparren-Bauteilachsen
  am Firstpunkt einen einzigen Knoten teilen müssen, auch
  wenn die nominalen End-Koordinaten der Bauteilachsen sich
  um Rundungsfehler unterscheiden.

- **Wohldefiniertheit unter Permutation**: K, M, F, A, L
  sind Mengen (unsortiert); alle Aussagen über das statische
  System sind invariant unter Permutation der Elemente.

- **Konsistenz mit `hg_tragwerk.md`**: die Stabilitäts-
  zusicherung (Bedingung 4 in `hg_tragwerk.md`) bleibt im
  Tragwerk **qualitativ**; der formale Nachweis wird hier im
  statischen System geführt (S7-Abzählformel als notwendiges
  Kriterium; hinreichend in der Bemessungs-Schicht). Diese
  Aufgabenteilung ist die intendierte Funktion des statischen
  Systems gegenüber dem Tragwerk.

- **Konsistenz mit `hg_auflager.md`**: die Auflager-Wertigkeit
  ist bereits im `auflager`-Aggregat als 6-Tupel
  (Tx, Ty, Tz, Rx, Ry, Rz) ∈ 𝓦 modelliert; das statische
  System übernimmt die Wertigkeit unverändert in die
  Abzählformel S7. Eine zusätzliche Idealisierung ist nicht
  nötig.

- **Konsistenz mit `hg_bauteilachse.md`**: die Stab-Träger-
  strecken sind die Bauteilachsen-Strecken; die App-Konvention
  zur Vorzeichenausrichtung der Bauteilachse (siehe
  `hg_bauteilachse.md`) wird vom statischen System geerbt.

- **Nicht-Zirkularität**: die Definition stützt sich auf
  bereits definierte Begriffe (`tragwerk`, `bauteil`,
  `bauteilachse`, `auflager`, `punkt`, `gerade`, `strecke`,
  `uuid`, `weltkoordinatensystem`, `toleranzen`). Sie verweist
  auf `lastfall` und `fe_modell` ausschließlich abgrenzend
  (Frontmatter `abgrenzung_zu`); auf die Sub-Begriffe `knoten`
  und `stab` als innere Bestandteile, deren eigene Glossar-
  Einträge als Folgearbeit angelegt werden.

- **Stabilität als notwendiges Kriterium**: S7 prüft die
  Abzählung n = a + s + z − 6k. Bei n = 0 ist das System
  **nicht zwingend** stabil; ein hinreichender Nachweis
  erfordert die Determinante der Koeffizientenmatrix der
  Gleichgewichtsbedingungen und gehört in die Bemessungs-
  Schicht. Diese Asymmetrie ist im Glossar explizit benannt
  und folgt der Wikipedia- und Petersen-Lesart.

## Erläuterung (nicht normativ)

### Tragwerk und Statisches System — zwei Lesarten desselben Substrats

Das App-Modell trennt am selben physischen Holzbauwerk **zwei
Aggregate** mit eigener UUID und unterschiedlicher Lesart:

| Aspekt | Tragwerk (`hg_tragwerk.md`) | Statisches System (dieser Eintrag) |
|---|---|---|
| Lesart | bauteilbezogene Realität | bemessungstechnische Idealisierung |
| Geometrische Träger | Bauteil-Polyeder in W | Knoten als Punkte + Stäbe als Strecken in W |
| Bauteil-Bezug | direkt (B ⊂ 𝓑) | indirekt über `basisbauteil`-UUID je Stab |
| Auflager | Aggregat mit geometrischer Manifestation + Wertigkeit | übernommen aus Tragwerk |
| Lastfälle | Konzeptionelle Erfassung | übernommen aus Tragwerk |
| Stabilität | qualitativ zugesichert | formal über Abzählformel n = a + s + z − 6k |
| IFC-Pendant | `IfcBeam` / `IfcColumn` / `IfcWall` + `IfcRelConnectsElements` | `IfcStructuralAnalysisModel` mit `IfcStructuralCurveMember` / `…Connection` / `…Activity` |
| Brücke zur jeweils anderen Lesart | Funktion `Tragwerk.statischesSystem()` | Feld `basistragwerk` ∈ 𝒰 |

Die Parallelität zu `hg_auflager.md` Drei-Schichten-Trennung
(Bearbeitung / Auflagefläche / Auflager) ist beabsichtigt: dort
die Trennung am einzelnen Stützungs-Ort, hier die Trennung am
gesamten Tragwerk. Beide stehen in einer Abstraktions-Relation,
sind aber **nicht identisch** — die App führt sie als zwei
getrennte UUIDs mit expliziter Brücke.

### Bestandteile

| Bestandteil | App-Symbol | Lehrbuch-Sprache | IFC-4.3-Pendant |
|---|---|---|---|
| Knoten | K | Stab-Verbindungs-Punkte, Lasteinleitungs- und Lager-Orte | implizit über Stab-Endpunkte und `IfcStructuralPointConnection` |
| Stab | M | 1D-Idealisierung; Achse = Schwerlinie der Querschnitte | `IfcStructuralCurveMember` |
| Flächenelement (Folgearbeit) | F | 2D-Idealisierung mit Bezugsfläche | `IfcStructuralSurfaceMember` |
| Auflager | A | Loslager / Festlager / Einspannung; Federlager | `IfcStructuralConnection` + `IfcBoundaryCondition` |
| Lastfall (Folgearbeit `lastfall`) | L | Eigengewicht, Nutzlast, Schnee, Wind, Erdbeben | `IfcStructuralAction` in `IfcStructuralLoadGroup` |
| Lagerreaktion (Berechnungs-Ergebnis) | (abgeleitet) | Resultat aus Σ F = 0, Σ M = 0 | `IfcStructuralReaction` in `IfcStructuralResultGroup` |
| Bestimmtheits-Klassifikation | abgeleitet aus S7 | bestimmt / n-fach unbestimmt / kinematisch verschieblich | keine eigene Entität; aus dem Modell ableitbar |

### Abzählformel — anwendungs-nahe Lesart

Für das paradigmatische Sparrenpaar (ebenes Sparrendach,
symmetrisch, ohne Mittelpfette):

- k = 3 (Traufknoten links, Firstknoten, Traufknoten rechts),
- s = 2 (zwei Sparren),
- z = 0 (keine Zwischengelenke),
- a = 4 (zwei Festlager an den Traufen, je 2 gesperrte
  Translationen im ebenen Fall),
- ebene Abzählformel: n = 4 + 2 + 0 − 3·3 = −3.

Der Sparrenpaar **ohne** Zugglied ist also dreifach kinematisch
verschieblich — das bekannte Lehrbuch-Resultat, weshalb das
Sparrendach ein Zugglied (Deckenbalken oder Kehlbalken)
braucht. Mit einem Zugglied: s = 3, n = 4 + 3 + 0 − 3·3 = −2.
Mit zwei Zuggliedern (Decken- und Kehlbalken): s = 4,
n = 4 + 4 + 0 − 3·3 = −1. Eine kinematisch stabile Konfiguration
erfordert weitere Sperrungen (z. B. Übergang zu einem
Pfettendach mit Mittelpfette als zusätzlichem Auflager).

Die App führt diese Abzählung als `statischesSystem.bestimmtheit():
Bestimmtheit` (Folgearbeit, siehe Implementierungshinweis).

### Berechnungs-Theorie

Die Berechnungs-Theorie ist ein eigenes Tupel-Feld, weil sie
nicht aus der Geometrie ableitbar ist, sondern eine
**Modellierungs-Entscheidung** trägt:

- **I. Ordnung** (linear, kleine Verformungen am unverformten
  System): Standard für Gebrauchstauglichkeits-Nachweise
  schlanker, stabiler Holz-Tragwerke.
- **II. Ordnung** (geometrisch nichtlinear, Gleichgewicht am
  verformten System): erforderlich bei Stabilitätsnachweis
  druckbeanspruchter schlanker Stäbe (Knicken), bei
  weicheren Tragwerken (Pendelstützen, schmale Hochbauten).
- **III. Ordnung** (vollständig nichtlinear, geometrisch und
  materiell): in der Holzbau-Praxis selten; bei
  Brand-Bemessung, Erdbeben, plastischen Reserven.

Die App-Default-Wahl ist `linear_erster_ordnung`.

### Statisches System vs. FE-Modell

Das **statische System** ist die analytische Modellierung mit
Knoten, Stäben, Auflagern und Wertigkeiten — kontinuierlich.
Das **FE-Modell** ist die **numerische Diskretisierung** des
statischen Systems für eine Computer-Berechnung mit Element-
Vernetzung, Ansatzfunktionen und Lösungsverfahren. Beide stehen
in einer weiteren Abstraktions-Relation: FE-Modell ist
Verfeinerung des statischen Systems, nicht Synonym. Das
FE-Modell wird im aktuellen App-Plan **nicht** als eigener
Glossar-Eintrag geführt (siehe Frontmatter `quellenkonflikt`,
HG §6 (D)).

### IFC-Mapping

| Aspekt | IFC-4.3-Pendant |
|---|---|
| Statisches System als Aggregat | `IfcStructuralAnalysisModel` mit GlobalId |
| Knoten (Punkt-Auflager-Inzidenz) | `IfcStructuralPointConnection` mit `AppliedCondition` |
| Stab | `IfcStructuralCurveMember` |
| Flächenelement (Folgearbeit) | `IfcStructuralSurfaceMember` |
| Berechnungs-Theorie | `IfcStructuralAnalysisModel.PredefinedType` (LOADING_3D, LOADING_PLANE_FRAME …) |
| Übernahme der Auflager aus Tragwerk | `IfcStructuralConnection`-Instanzen, gemeinsam zwischen Tragwerk und statischem System |
| Lastfall-Gruppen | `IfcStructuralLoadGroup` (Subtypen: LoadCase, LoadCombination) |
| Berechnungs-Ergebnis | `IfcStructuralResultGroup` mit `IfcStructuralReaction` und Schnittgrössen |
| Physisch-analytische Brücke | `IfcRelAssignsToProduct` zwischen `IfcStructuralMember` und `IfcBeam`/`IfcColumn`/`IfcWall` |

Die App-Aggregat-Struktur folgt damit eng dem IFC-4.3-Schema
der Structural-Analysis-Domain. Das Tupel-Feld `basistragwerk`
ist das App-Pendant zur `IfcRelAssignsToProduct`-Beziehung.
Das BTLx-Schema (design2machine) kennt keine Pendant-Entität;
die Bemessungs-Information ist dort nicht abbildbar.

## Beziehungen

- **Oberbegriff**: `null` (analog `verbindung`, `auflager`).
  Statisches System ist eine eigenständige Abstraktions-Sicht
  auf das Tragwerk, kein Subtyp eines fachlichen Trägerbegriffs.
  Siehe Frontmatter `quellenkonflikt` für die Begründung der
  Wahl gegen `oberbegriff: tragwerk`.
- **Bestandteile (partitiv)**:
  - **Knoten** (`knoten`, Folgearbeit, sealed-Klasse `Element`-
    intern im statischen System): Punkte in W mit eigener
    Identität innerhalb des Systems.
  - **Stab** (`stab`, Folgearbeit): 1D-Element mit gerichteter
    Trägerstrecke, Endknoten-Inzidenz und Bauteil-UUID-Referenz.
  - **Flächenelement** (`flaechenelement`, Folgearbeit; Default
    ∅): 2D-Element mit Bezugsfläche.
  - **Auflager-Auswahl** (Teilmenge von T.A).
  - **Lastfall-Auswahl** (Teilmenge von T.L; `lastfall` als
    eigener Eintrag folgt).
  - **Berechnungs-Theorie-Annahme**.
- **Spezialisierungen nach Theorie** (Folgearbeit, falls
  benötigt; im aktuellen Stand im `theorie`-Feld aufgelöst):
  lineares statisches System, geometrisch nichtlineares
  statisches System (Theorie II. Ordnung) etc.
- **Verwendung**:
  - Abgeleitet aus einem **Tragwerk** (`tragwerk`) via
    `Tragwerk.statischesSystem()`. Das Feld `basistragwerk`
    trägt die UUID des Tragwerks.
  - Eingangsgrösse für die **Bemessungs-Schicht** (Folgearbeit):
    Tragsicherheits- und Gebrauchstauglichkeits-Nachweise nach
    EN 1995-1-1 / SIA 265 setzen das statische System voraus.
- **Abgrenzung**:
  - **Tragwerk** (`tragwerk`): bauteilbezogene Realität.
    Statisches System ist die idealisierte Modellierung
    desselben physischen Substrats; beide sind getrennte
    Aggregate mit eigener UUID. Die Brücke ist das Feld
    `basistragwerk`.
  - **Bauteil** (`bauteil`): Tragwerks-Substanz im W;
    Stäbe im statischen System sind **Idealisierungen** der
    Bauteile, nicht die Bauteile selbst. Der Bezug ist über
    die UUID-Referenz `stab.basisbauteil` explizit.
  - **Bauteilachse** (`bauteilachse`): geometrische Hauptachse
    eines Stabbauteils; die Trägerstrecke eines Stabes im
    statischen System ist die Bauteilachsen-Strecke des
    zugehörigen Bauteils. Die Bauteilachse lebt am Bauteil,
    der Stab im statischen System.
  - **Auflager** (`auflager`): Aggregat mit Manifestation und
    Wertigkeit. Statisches System übernimmt Auflager
    unverändert aus dem Basistragwerk (A ⊆ T.A); keine
    zusätzliche Idealisierung.
  - **Verbindung** (`verbindung`): Aggregat auf der Anschluss-
    Bemessungs-Seite. Verbindungen sind **nicht** Bestandteil
    des statischen Systems; ihre Federsteifigkeiten gehen
    gegebenenfalls als Gelenkfreiheiten oder Federgelenke in
    die Stab-Modellierung ein (Folgearbeit).
  - **Lastfall** (`lastfall`, Folgearbeit): konzeptuelle
    Einwirkung. Statisches System trägt eine ausgewählte
    Lastfall-Menge L ⊆ T.L.
  - **FE-Modell** (`fe_modell`, Korpus-Begriff dauerhaft ohne
    eigenen Eintrag, HG §6 (D)): numerische Diskretisierung
    des statischen Systems. Statisches System ist analytisch
    und kontinuierlich; FE-Modell ist diskret und numerisch.
  - **Knoten** (`knoten`, Folgearbeit) und **Stab** (`stab`,
    Folgearbeit): partitive Bestandteile des statischen
    Systems mit eigenen Folge-Glossareinträgen, sobald die
    sealed-Klasse `Element` (statisches-System-intern, nicht
    zu verwechseln mit der ontologischen `element`-
    Basisklasse aus `hg_bauteil.md`) im Code implementiert
    wird.

## Implementierungshinweis

Datentyp (Domänen-Schicht, Kotlin, Schicht
`domain.aggregat.statischessystem`):

```kotlin
package domain.aggregat.statischessystem

import domain.aggregat.auflager.Auflager
import domain.bauteil.Bauteil
import domain.bauteil.Tragwerk
import domain.geometrie.Punkt
import domain.geometrie.Strecke
import java.util.UUID

/** Berechnungs-Theorie-Annahme des statischen Systems. */
sealed interface BerechnungsTheorie {
    data object LinearErsterOrdnung                    : BerechnungsTheorie
    data object GeometrischNichtlinearZweiterOrdnung   : BerechnungsTheorie
    data object MateriellNichtlinear                   : BerechnungsTheorie
    data object VollNichtlinearDritterOrdnung          : BerechnungsTheorie
}

/** Klassifikation der Bestimmtheit aus S7-Abzählformel. */
sealed interface Bestimmtheit {
    data class StatischUnbestimmt(val grad: Int)       : Bestimmtheit
    data object StatischBestimmt                       : Bestimmtheit
    data class KinematischVerschieblich(val grad: Int) : Bestimmtheit
}

/** Knoten im statischen System: Punkt in W mit eigener Identität. */
data class Knoten(
    val uuid: UUID,
    val ort: Punkt
)

/** Stab im statischen System: gerichtete Strecke mit Bauteil-UUID-Referenz. */
data class Stab(
    val uuid: UUID,
    val traegerstrecke: Strecke,             // Anfang/Ende in der Knotenmenge
    val basisbauteil: UUID                   // FK auf Bauteil im Basistragwerk
)

/**
 * Statisches System: Aggregat aus Knoten, Stäben (1D), optional
 * Flächenelementen (2D, Folgearbeit), übernommenen Auflagern und
 * Lastfällen, Berechnungs-Theorie-Annahme und Referenz auf das
 * Basistragwerk.
 *
 * Glossar: hg_statisches_system.md
 *
 * NICHT Subtyp eines fachlichen Trägerbegriffs. Eigenes Aggregat,
 * analog Verbindung und Auflager. Brücke zum Tragwerk über das
 * Feld basistragwerk (Pendant zu IfcRelAssignsToProduct).
 *
 * IFC: IfcStructuralAnalysisModel mit IfcStructuralCurveMember,
 *      IfcStructuralConnection, IfcStructuralActivity.
 * BTLx: keine Pendant-Entität.
 */
data class StatischesSystem(
    val uuid: UUID,                          // eigene Identität als Aggregat
    val basistragwerk: UUID,                 // FK auf Tragwerk; physisch-analytische Brücke
    val knoten: Set<Knoten>,                 // K, |K| >= 1
    val staebe: Set<Stab>,                   // M
    val flaechenelemente: Set<Flaechenelement> = emptySet(),  // F, Default ∅, Folgearbeit
    val auflager: Set<Auflager>,             // A ⊆ T.A
    val lastfaelle: Set<Lastfall> = emptySet(),               // L ⊆ T.L, Folgearbeit
    val theorie: BerechnungsTheorie = BerechnungsTheorie.LinearErsterOrdnung,
    val bezeichnung: String? = null
) {
    init {
        // S1. Knoten-Stab-Inzidenz       (Modell-Validierung)
        // S2. Stab-Bauteilachsen-Konsistenz (Modell-Validierung mit Tragwerks-Lookup)
        // S3. Auflager-Knoten-Inzidenz   (Modell-Validierung)
        // S4. A ⊆ T.A                    (Modell-Validierung mit Tragwerks-Lookup)
        // S5. L ⊆ T.L                    (Modell-Validierung)
        // S6. Knoten-Vollständigkeit     (keine isolierten Knoten)
        // S7. Stabilität abgeleitet      (siehe bestimmtheit())
    }

    /** Abzählformel im räumlichen Fall (S7, notwendiges Kriterium). */
    fun bestimmtheit(): Bestimmtheit {
        val a = auflager.sumOf { it.gesperrteFhg() }
        val s = staebe.size
        val z = 0                                // Stabgelenke noch nicht modelliert
        val k = knoten.size
        val n = a + s + z - 6 * k
        return when {
            n > 0  -> Bestimmtheit.StatischUnbestimmt(n)
            n == 0 -> Bestimmtheit.StatischBestimmt
            else   -> Bestimmtheit.KinematischVerschieblich(-n)
        }
    }

    /** Notwendiges Stabilitäts-Kriterium aus S7. */
    fun istStabilNotwendig(): Boolean = bestimmtheit() !is Bestimmtheit.KinematischVerschieblich

    /** Hinreichendes Stabilitäts-Kriterium: Folgearbeit (Bemessungs-Schicht). */
    fun istStabil(): Boolean = TODO("Hinreichendes Kriterium: Determinante der Gleichgewichts-Matrix")
}

/** Platzhalter-Typ; eigener Eintrag folgt. */
data class Flaechenelement(val uuid: UUID /* ... */)
// Lastfall ist in domain.aggregat.lastfall.Lastfall ausformuliert
// (siehe hg_lastfall.md).
```

- **Einheit**: Längen in mm (Double); Winkel intern in Radiant;
  Lasten in der späteren Lastfall-Schicht in N, N/m, N/m² (SI).
- **Identität**: `uuid` ist Pflicht und eigenständig (eigene UUID
  des Aggregats, RFC 9562 v7, persistent).
- **Foreign-Key-Regel**: `basistragwerk`, `stab.basisbauteil`
  und alle Auflager-Referenzen gehen ausschließlich auf UUIDs
  (Memory `project_bauteil_identifikation`).
- **Pflicht- und Optionalfelder**:
  - `basistragwerk`, `knoten`, `staebe`, `auflager`, `theorie`
    sind Pflicht.
  - `flaechenelemente` (Default ∅, Folgearbeit für 2D-Pendant),
    `lastfaelle` (Default ∅ im Entwurfsstadium vor Bemessung),
    `bezeichnung` (frei) sind optional.
- **Invarianten** (in der Aggregat-Fabrikfunktion
  `StatischesSystem.bilde(modell: Modell, tragwerk: Tragwerk, …)`
  geprüft; bei Verletzung `Resultat.Fehler`, niemals Exception):
  1. `knoten.isNotEmpty()` ⇒ sonst `Entartet.LeeresSystem`.
  2. S1 (Knoten-Stab-Inzidenz): jeder Stab-Endpunkt ist im
     `LAENGE_EPS`-Sinn ein Knoten in `knoten` ⇒ sonst
     `Entartet.StabEndpunktAusserhalbKnoten`.
  3. S2 (Stab-Bauteilachsen-Konsistenz): jeder
     `stab.basisbauteil` existiert in `tragwerk.bauteile`, und
     die Trägerstrecke entspricht der Bauteilachsen-Strecke
     (Toleranz `LAENGE_EPS`) ⇒ sonst
     `Entartet.StabOhneBasisbauteil` bzw.
     `Entartet.TraegerstreckeAbweichend`.
  4. S3 (Auflager-Knoten-Inzidenz): Punkt-Auflager liegen auf
     Knoten; Linien-/Flächenauflager auf Stäben (bzw.
     Flächenelementen) ⇒ sonst `Entartet.AuflagerOhneInzidenz`.
  5. S4, S5 (Teilmengen-Konsistenz): `auflager ⊆ tragwerk.auflager`
     und `lastfaelle ⊆ tragwerk.lastfaelle` ⇒ sonst
     `Entartet.AuflagerNichtImTragwerk` bzw.
     `Entartet.LastfallNichtImTragwerk`.
  6. S6 (Knoten-Vollständigkeit): jeder Knoten ist mindestens
     einmal inzident ⇒ sonst `Entartet.IsolierterKnoten`.
  7. S7 (Stabilität als abgeleitete Eigenschaft): **nicht** in
     `init` geprüft; nur über `bestimmtheit()` abrufbar.
     Konstruktion eines kinematisch verschieblichen statischen
     Systems ist zulässig (Entwurfsstadium); die Stabilität
     wird in der Bemessungs-Schicht erzwungen.
- **Knoten-Kontraktion** (Wohldefiniertheits-Konvention): bei
  der kanonischen Konstruktion aus einem Tragwerk werden
  Bauteil-Achsen-Endpunkte mit Abstand ≤ `LAENGE_EPS` zu
  **einem** Knoten kontrahiert. Implementiert in der
  Fabrikfunktion `Tragwerk.statischesSystem()`.
- **Edge Cases**:
  - **Leeres statisches System** (|K| = 0 ∨ |M| = 0): nicht
    erlaubt; mindestens ein Knoten und ein Stab (oder
    Flächenelement) müssen vorhanden sein.
  - **Statisches System ohne Auflager**: nicht erlaubt im
    räumlichen Fall (Bestimmtheit wäre n < 0); im Code als
    `Entartet.OhneAuflager` abgelehnt (geerbt aus Tragwerk-
    Konsistenz S4 mit |T.A| ≥ 1).
  - **Mehrere statische Systeme an einem Tragwerk**: zulässig;
    z. B. ein lineares System für GZG und ein nichtlineares
    für Stabilität. Beide referenzieren dasselbe
    `basistragwerk` mit unterschiedlicher `uuid` und
    `theorie`.
  - **Knoten an identischem geometrischem Ort**: nicht
    erlaubt im `LAENGE_EPS`-Sinn (Knoten-Kontraktion in der
    Fabrikfunktion); manuelle Konstruktion mit Duplikaten
    liefert `Entartet.KnotenDuplikat`.
  - **Statisches System ohne 2D-Anteil**: Default; `F = ∅`.
    Aktueller App-Stand.
  - **Statisches System mit Stabgelenken**: noch nicht
    modelliert; `z = 0` in der Abzählformel S7. Folgearbeit,
    sobald Anschluss-Federsteifigkeiten aus Verbindungen
    einfliessen.
- **Toleranz-Anwendung** (siehe `hg_toleranzen.md` §4):
  - Knoten-Identität und Stab-Endpunkt-Inzidenz: `LAENGE_EPS`.
  - Trägerstrecken-Abweichung von der Bauteilachse:
    `LAENGE_EPS` an den Endpunkten.
  - Punkt-Auflager-Inzidenz auf Knoten: `LAENGE_EPS`.
- **IFC-Export-Mapping**:
  - `StatischesSystem` → `IfcStructuralAnalysisModel` mit
    `GlobalId`, `Name`, `PredefinedType` (abgeleitet aus
    `theorie`).
  - `staebe` → `IfcStructuralCurveMember`-Instanzen, je
    UUID-tragend.
  - `knoten` → bei Punkt-Auflager-Inzidenz als
    `IfcStructuralPointConnection`; sonst implizit über
    Stab-Endpunkte.
  - `auflager` mit `AppliedCondition` (siehe `hg_auflager.md`-
    IFC-Mapping).
  - `lastfaelle` → `IfcStructuralLoadGroup`-Instanzen
    (Folgearbeit).
  - `basistragwerk` und `stab.basisbauteil` →
    `IfcRelAssignsToProduct`-Beziehungen zwischen
    `IfcStructuralMember` und `IfcBeam`/`IfcColumn`/`IfcWall`.
- **BTLx-Export**: keine Pendant-Entität. Bemessungs-
  Information wird im BTLx-Export nicht ausgegeben.
- **Abgeleitete Eigenschaften** (als Funktionen, keine
  Felder):
  - `geometrieInWelt(): GeometrieInW` — Vereinigung der
    Knoten-Orte, Stab-Trägerstrecken und (falls vorhanden)
    Flächenelement-Träger.
  - `boundingBox(): AABB` — achsenparalleler Hüllquader in W.
  - `inzidenzgraph(): Graph<Knoten, Stab>` — ungerichteter
    Graph mit Knoten als Graphknoten und Stäben als Kanten.
  - `bestimmtheit(): Bestimmtheit` — Klassifikation aus S7
    (notwendiges Kriterium).
  - `istStabilNotwendig(): Boolean` — notwendiges
    Stabilitäts-Kriterium (Abzählung n ≥ 0).
  - `istStabil(): Boolean` — hinreichendes Kriterium
    (Folgearbeit Bemessungs-Schicht; Determinante der
    Gleichgewichts-Matrix).
- **Bezeichner-Konvention** (siehe `docs/_CODE_KONVENTIONEN.md`):
  Domänen-Klasse heisst `StatischesSystem` (deutsch,
  Glossarbegriff). Synonyme `Tragwerksmodell`,
  `Stabwerksmodell`, `Strukturmodell` erscheinen ausschliesslich
  als KDoc-Stichworte. Die innere sealed-Klasse `Element` des
  statischen Systems (für die Vereinigung von `Stab` und
  `Flaechenelement`) ist **nicht** zu verwechseln mit der
  ontologischen `element`-Basisklasse aus `hg_bauteil.md`; sie
  ist Implementierungs-intern.

## Quellen

**Primär (normativ):**

- ISO 16739-1:2024, „Industry Foundation Classes (IFC) for data
  sharing in the construction and facility management industries
  – Part 1: Data schema" (IFC 4.3), Structural-Analysis-Domain-
  Entitäten `IfcStructuralAnalysisModel`,
  `IfcStructuralCurveMember`, `IfcStructuralSurfaceMember`,
  `IfcStructuralConnection`, `IfcStructuralAction`,
  `IfcStructuralReaction`, `IfcStructuralLoadGroup`,
  `IfcStructuralResultGroup`, `IfcRelAssignsToProduct`.
- DIN EN 1990:2010-12, „Eurocode: Grundlagen der
  Tragwerksplanung", Abschnitt 1.5.1.7.
- DIN EN 1995-1-1:2010-12, „Eurocode 5: Bemessung und
  Konstruktion von Holzbauten – Teil 1-1", Abschnitt 5.
- SIA 260:2013, „Grundlagen der Projektierung von Tragwerken",
  Schweizerischer Ingenieur- und Architektenverein, Zürich.
- SIA 265:2021, „Holzbau", Schweizerischer Ingenieur- und
  Architektenverein, Zürich.
- DIN 1052:2008-12, „Entwurf, Berechnung und Bemessung von
  Holzbauwerken", Abschnitt 5.

**Sekundär:**

- Krätzig, W. B.; Wittek, U.; Harte, R.; Meskouris, K.:
  *Tragwerke 1 / Tragwerke 2.* Springer (VDI-Buch),
  Berlin/Heidelberg, Kapitel „Das Tragwerksmodell der Statik
  der Tragwerke".
- Petersen, Chr.: *Statik und Stabilität der Baukonstruktionen.*
  Vieweg, Braunschweig.
- Schneider, K.-J.; Albert, A.: *Bautabellen für Ingenieure.*
  26. Aufl., Bundesanzeiger Verlag, Köln 2024.
- Mönck, W.; Rug, W.: *Holzbau – Bemessung und Konstruktion.*
  16. Aufl., Beuth, Berlin 2015, Kap. 11.
- Blass, H. J.; Sandhaas, C.: *Ingenieurholzbau – Grundlagen
  der Bemessung.* KIT Scientific Publishing, Karlsruhe 2016,
  Kap. 5.
- Natterer, J.; Herzog, T.; Volz, M.: *Holzbau-Atlas.*
  4. Aufl., Birkhäuser, Basel 2003.
- buildingSMART, IFC-4.3.2-Dokumentation Structural-Analysis-
  Domain (Sekundärrezeption über WebSearch-Snippets;
  `IfcStructuralAnalysisModel`, `IfcRelAssignsToProduct`).

**Korpus (nicht autoritativ):**

- Wikipedia, Lemma „Baustatik" (abgerufen 2026-05-14).
- Wikipedia, Lemma „Stabwerk (Technische Mechanik)" (abgerufen
  2026-05-14).
- Wikipedia, Lemma „Stab (Statik)" (abgerufen 2026-05-14).
- Wikipedia, Lemma „Lager (Statik)" (abgerufen 2026-05-14).
- Wikipedia, Lemma „Statische Bestimmtheit" (abgerufen
  2026-05-14).
- D.I.E.-Statik, „Statisches System / Modell-Allgemeines"
  (abgerufen 2026-05-14).
- ingenieurkurse.de, „Tragwerksmodell", „Statische
  Bestimmtheit (Abzählformel)" (Sekundärrezeption).
- Recherche-Bericht: `docs/recherche/2026-05-14_hg_statisches_system.md`.
