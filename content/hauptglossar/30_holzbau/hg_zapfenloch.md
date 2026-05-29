---
id: zapfenloch
benennung: Zapfenloch
synonyme: [Zapfenaussparung, Zapfenausnehmung, "mortise", "mortice"]
abgelehnte_benennungen: [Loch, Bohrung, Schlitz, Tasche, Aussparung, "hole", "pocket", "mortise hole", Zapfenverbindung, Verzapfung]
oberbegriff: bearbeitung
begriffstyp: partitiv
voraussetzungen: [bearbeitung, bauteil, polyeder, lokales_koordinatensystem, bauteilachse, punkt, vektor, einheitsvektor, toleranzen, uuid]
abgrenzung_zu: [zapfen, kerve, bohrung, versatz, schlitz, blatt, kamm, anschnitt, aussparung, bearbeitung, bauteil, verbindung, verbindungsmittel]
status: entwurf
theorie_pflichtig: required
quellen_primär:
  - "DIN EN 1995-1-1:2010-12 (Eurocode 5), Abschnitt 6.1.5 'Druck rechtwinklig zur Faser' (Querdruck): die Lochwand des Zapfenlochs steht im Wirkungspfad des Zapfen-Druckschafts und wird gegen die charakteristische Druckfestigkeit f_{c,90,k} senkrecht zur Faser bemessen. Abschnitt 8 'Anschlüsse mit metallischen Verbindungsmitteln' regelt die zimmermannsmässige Zapfenverbindung **nicht direkt**; sie ist Gegenstand des Nationalen Anhangs (DIN EN 1995-1-1/NA) und der nationalen Holzbau-Norm DIN 1052."
  - "DIN EN 1995-1-1/NA:2013-08, Nationaler Anhang Deutschland zu Eurocode 5: regelt zimmermannsmässige Verbindungen (Versatz, Zapfen, Holznagel) als Ergänzung zum Hauptteil."
  - "DIN 1052:2008-12 'Entwurf, Berechnung und Bemessung von Holzbauwerken', Abschnitt 15 'Zimmermannsmässige Verbindungen': Bemessungsregeln für die Zapfenverbindung einschliesslich des Querdruck-Nachweises an der Lochwand und des Schub-Nachweises am verbleibenden Holz unterhalb des Zapfenlochs."
  - "SIA 265:2021 'Holzbau', Schweizerischer Ingenieur- und Architektenverein, Zürich, Anhang A 'Zimmermannsmässige Verbindungen': Bemessung von Versatz, Zapfen und Blatt; Querdruck-Nachweis am Zapfenloch."
  - "design2machine: 'BTLx interface description', Version 2.1, 16.11.2023, Abschnitt 'List of Processings', Processings 'Mortise', 'DovetailMortise', 'HouseMortise', 'JapaneseMortise' (S. 8 ff.): rechteckiges bzw. schwalbenschwanzförmiges Zapfenloch im Bauteilfeld oder am Bauteilende, parametrisch über ReferencePlane, Position (StartX, StartY, StartDepth), Orientation (Angle, Inclination), Geometrie (Width, Height, Depth) und ggf. ConeAngle (DovetailMortise) spezifiziert."
  - "ISO 16739-1:2024 'Industry Foundation Classes (IFC) for data sharing in the construction and facility management industries — Part 1: Data schema' (IFC 4.3.2): Entität 'IfcOpeningElement' mit Beziehung 'IfcRelVoidsElement' als generisches Pendant zum Zapfenloch im IFC-Modell. [direkt]"
quellen_sekundär:
  - "Mönck, W.; Rug, W.: Holzbau – Bemessung und Konstruktion. 16. Aufl., Beuth, Berlin 2015, Kap. 7 'Verbindungen', § Zapfenverbindung (Geometrie, Faustregeln, Querdruck-Nachweis an der Lochwand)."
  - "Blass, H. J.; Sandhaas, C.: Ingenieurholzbau – Grundlagen der Bemessung. KIT Scientific Publishing, Karlsruhe 2016, Kap. 8 'Verbindungen'."
  - "Natterer, J.; Herzog, T.; Volz, M.: Holzbau-Atlas. 4. Aufl., Birkhäuser, Basel 2003, Kap. 'Verbindungen und Anschlüsse', § Zapfenverbindung."
  - "Gerner, M.: Fachwerk – Instandsetzung, Sanierung, Neubau. DVA, 7. Aufl. 2007, Glossar 'Zapfen' / 'Zapfenloch'."
  - "Krämer, F.: Grundwissen des Zimmerers. Bruderverlag, Karlsruhe (referenziert in der Recherche)."
  - "Lignum (Hrsg.): Holzbautabellen HBT1:2021 / HBT2, Lignum, Zürich, Kap. 'Zimmermannsmässige Verbindungen'."
  - "Claus, T.: Zapfenverbindungen im Holzbau – bruchmechanische Analyse und Vorschlag eines Berechnungsmodells. Bautechnik 97 (2020), Wiley."
  - "Informationsdienst Holz: Tragverhalten zimmermannsmässiger Holzverbindungen (Reihen-Publikation)."
  - "Wikipedia, Lemma 'Zapfenverbindung' (de.wikipedia.org, abgerufen 2026-05-14): 'Bei einer Zapfenverbindung wird ein hervorstehender Holzteil, der Zapfen, in eine Aussparung, das Zapfenloch, eines zweiten Bauteils eingeführt. Das Zapfenloch ist üblicherweise 5 bis 10 mm tiefer als der Zapfen lang ist (Zapfenluft).'"
quellenkonflikt: |
  Es existiert **keine geschlossene, im Sandbox-Korpus
  zugängliche, normative Geometrie-Spezifikation des
  Zapfenlochs** in einer einzelnen deutschsprachigen Holzbau-
  Norm. Die einschlägigen Normen-Stellen verteilen sich auf
  vier Quellen, die im Hauptglossar synthetisiert werden müssen:

  - **EC5 (DIN EN 1995-1-1) §6.1.5** regelt den **Querdruck**
    an der Lochwand (Druck rechtwinklig zur Faser des
    Trägerbauteils), aber **nicht** die Geometrie der Aussparung
    selbst. §8 betrifft Anschlüsse mit metallischen
    Verbindungsmitteln und ist **nicht** die einschlägige
    Bemessungs-Stelle für die Zapfenverbindung (Recherche-
    Befund 2026-05-14, der die Auftrags-Hypothese §8 explizit
    falsifiziert).
  - **DIN EN 1995-1-1/NA** (Nationaler Anhang Deutschland) und
    **DIN 1052:2008-12 §15** tragen die zimmermannsmässige
    Verbindung (Versatz, Zapfen, Holznagel). Die DIN 1052-Stelle
    war im Sandbox-Recherche-Korpus nicht im Volltext
    einsehbar; die Aussagen dieses Eintrags folgen dem Konsens
    der Sekundärliteratur (Mönck/Rug, Blass/Sandhaas,
    Natterer/Herzog).
  - **SIA 265:2021 Anhang A** behandelt zimmermannsmässige
    Verbindungen im Schweizer Normkorpus; ebenfalls nicht im
    Volltext eingesehen.
  - **BTLx 2.1** (design2machine) spezifiziert das Zapfenloch
    parametrisch als CNC-Processing `Mortise` (sowie
    `DovetailMortise`, `HouseMortise`, `JapaneseMortise`) und
    ist die geschlossene Industriestandard-Schnittstelle.

  Die Glossar-Festlegung wählt — analog zu `kerve` —
  den **Mittelweg**:

  (1) Das Zapfenloch ist **ontologisch eine prismatische,
      subtraktive Bearbeitung** am aufnehmenden Bauteil. Die
      geometrische Definition wird als rechteckiger Werkzeug-
      körper im Bauteil-Lokal-System geführt; die
      Schwalbenschwanz-Variante ist eine Erweiterung mit
      Konuswinkel, die Haus-Variante eine Erweiterung mit
      flacher Anlagestufe.

  (2) Die **Bezugsfläche** der Aussparung ist eine Bauteil-
      Aussenfläche (typisch eine Längsseite oder Stirnseite
      des aufnehmenden Bauteils); die Lochtiefe wird in deren
      Flächennormale gemessen. Damit ist das Zapfenloch im
      Gegensatz zur Kerve **nicht zwingend welt-aligned**,
      sondern **bauteil-aligned**. Diese Festlegung ist
      konsistent mit BTLx (`ReferencePlane`-Bezug) und mit
      IFC (`IfcOpeningElement` mit lokaler Platzierung am
      Master-Element).

  (3) Die **Zapfenluft** (Lochtiefe = Zapfenlänge + 5…10 mm)
      ist eine berufssprachlich konsistent überlieferte,
      aber im verfügbaren normativen Korpus nicht im
      Wortlaut zitierte Faustregel. Sie wird **nicht** als
      geometrische Definitionsbedingung am Zapfenloch
      geführt, weil das geometrische Konzept eine
      prismatische Aussparung mit selbständiger Tiefe ist
      (geometrisch wohldefiniert auch ohne zugeordneten
      Zapfen). Die Zapfenluft tritt erst im Tragwerks-Kontext
      auf, in dem ein Zapfen geometrisch in das Zapfenloch
      eingeführt wird (siehe `verbindung`,
      `VerbindungsTyp.ZimmermannsmaessigerAnschluss`). Die
      App führt eine **weiche Plausibilitätsprüfung**
      (Warnung, kein Validierungsfehler): bei einem
      Verbindungs-Aggregat mit gepaartem Zapfen und Zapfenloch
      prüft die Tragwerks-Schicht
      Lochtiefe − Zapfenlänge gegen
      `Toleranzen.ZAPFENLUFT_MIN` (Standard 5 mm) und
      `Toleranzen.ZAPFENLUFT_MAX` (Standard 10 mm). Diese
      Konstanten sind projekt- und normspezifisch
      überschreibbar.

  (4) Der **Mindest-Restquerschnitt** am Trägerbauteil ist im
      verfügbaren normativen Korpus nicht als geschlossene
      Faustregel beigebracht; die Bemessung erfolgt
      norm-implizit über den Querdruck-Nachweis (EC5 §6.1.5)
      und den Schub-Nachweis am verbleibenden Holz
      unterhalb der Aussparung (EC5 §6.5, analog zum
      ausgeklinkten Träger). Berufssprachlich gilt die
      Plausibilitätsregel **Restholz ≥ Lochbreite + 2 · 30 mm**
      auf jeder Seite des Lochs (also genügend Holz zu beiden
      Längsseiten) sowie **Restholz unter dem Loch ≥
      Lochtiefe**, beides als Warnung in der App, nicht als
      harte Invariante. Die App-Konstanten heissen
      `Toleranzen.ZAPFENLOCH_RESTHOLZ_SEITLICH_MIN` und
      `Toleranzen.ZAPFENLOCH_RESTHOLZ_UNTEN_MIN`.

  (5) **BTLx/IFC sind Übersetzungsschichten in Phase 4**
      (analog zu `bearbeitung` und `kerve`). Die App-interne
      Subtypen-Liste des Zapfenlochs (Standard, Schwalbenschwanz,
      Haus) ist nach zimmermannssprachlichen Kriterien
      gegliedert; die BTLx-Processings `Mortise`,
      `DovetailMortise`, `HouseMortise`, `JapaneseMortise`
      werden bidirektional auf diese Subtypen abgebildet.
      `JapaneseMortise` wird als eigener Glossartyp
      `japanisches_zapfenloch` (Folgearbeit) geführt, weil es
      eine Mehrflächen-Geometrie hat, die das hier definierte
      Standard-Zapfenloch nicht abdeckt.

  **Symmetrie zum Zapfen-Eintrag:** Dieser Eintrag und der
  parallele Eintrag `hg_zapfen.md` definieren ein
  **komplementäres Begriffs-Paar**: das Zapfenloch ist die
  Aussparung am Trägerbauteil, der Zapfen das hervorstehende
  Element am Anschlussbauteil. Beide Einträge sind
  eigenständige Hauptglossar-Einträge mit eigener UUID und
  eigener Bearbeitungs-Liste; die Bündelung zur **Zapfen-
  verbindung** erfolgt auf der Aggregats-Ebene
  (`hg_verbindung.md`, `VerbindungsTyp.ZimmermannsmaessigerAnschluss`),
  nicht durch einen eigenen Aggregat-Eintrag
  `zapfen_verbindung` (siehe Recherche-Bericht
  `docs/recherche/2026-05-14_hg_zapfen.md` §H). Der
  Erläuterungs-Block beider Einträge trägt dasselbe Material
  zur Zapfenverbindung als Gesamtkonzept.
---

## Prosa-Definition

Ein **Zapfenloch** ist eine subtraktive Bearbeitung an einem
Bauteil, die einen prismatischen, rechteckigen (oder
schwalbenschwanzförmigen) Hohlraum aus dem Bauteilkörper
entfernt; der Hohlraum ist durch eine ebene Bezugsfläche an der
Bauteilaussenfläche (typisch eine Längsseite oder Stirnseite),
durch eine rechteckige Öffnungskontur in der Bezugsfläche und
durch eine in Richtung der Flächennormalen gemessene Lochtiefe
bestimmt und dient der formschlüssigen Aufnahme eines an einem
anderen Bauteil hervorstehenden Zapfens (siehe `zapfen`).

## Mathematische Definition

Sei

- B ein Bauteil im Sinne von `bauteil` mit ungeschwächtem
  Bauteilkörper G_B^lokal ⊂ ℝ³ im Bauteil-Lokal-System
  L_B = (O_B, e_hat_x^B, e_hat_y^B, e_hat_z^B),
- 𝓕(B) die endliche Menge der **Bezugsflächen** von B (die
  rechteckigen Aussenflächen des Bauteilkörpers — beim
  Quaderbauteil sechs Stück: vier Längsseiten und zwei
  Stirnseiten; siehe `laengsseite`, `stirnseite`),
- für eine gewählte Bezugsfläche F ∈ 𝓕(B) der **Flächen-Ursprung**
  O_F ∈ F (typisch eine ausgezeichnete Ecke), die in F
  liegenden Tangentialrichtungen e_hat_u^F, e_hat_v^F (orthonormal,
  rechtshändig) sowie die **nach innen** zeigende
  Flächen-Normale e_hat_n^F ∈ S² mit ⟨e_hat_n^F, e_hat_z^B-Komponente⟩
  oder einer anderen kanonischen Wahl, sodass der
  Werkzeugkörper bei positiver Lochtiefe in den Bauteilkörper
  hinein zeigt,
- ε_L := Toleranzen.LAENGE_EPS, ε_W := Toleranzen.WINKEL_EPS.

Die **Parameter** eines Zapfenlochs sind das Tupel

```
p_ZL := (F, u_0, v_0, b, h, t, ψ, variante, κ)                    (1)
```

mit

- **F** ∈ 𝓕(B): **Bezugsfläche** am Bauteil, an der das
  Zapfenloch geöffnet ist. Bei einem als Quader idealisierten
  Bauteil eine der sechs Aussenflächen; bei einem Stab-Bauteil
  typisch eine Längsseite (Loch im Bauteilfeld, z. B. an einer
  Pfette) oder eine Stirnseite (Loch am Bauteilende).
- **(u_0, v_0)** ∈ ℝ²: **Lochmittelpunkt** in den
  Flächenkoordinaten (u, v) von F, gemessen in mm vom Flächen-
  Ursprung O_F.
- **b** ∈ ℝ⁺: **Lochbreite** in u-Richtung (mm), b > ε_L. Bei
  einem Zapfenloch am Bauteilfeld typisch das längere
  Rechteckmass; entspricht der Zapfenbreite des
  einzuführenden Zapfens.
- **h** ∈ ℝ⁺: **Lochhöhe** in v-Richtung (mm), h > ε_L.
  Entspricht der Zapfenhöhe.
- **t** ∈ ℝ⁺: **Lochtiefe** in Richtung der inneren Flächen-
  Normalen e_hat_n^F (mm), t > ε_L.
- **ψ** ∈ [−π/2, π/2]: **Loch-Drehwinkel** in der Bezugsfläche
  (Rotation des Lochrechtecks gegen e_hat_u^F); Standard ψ = 0
  (Loch achs-aligned).
- **variante** ∈ {Standard, Schwalbenschwanz, Haus}:
  Geometrievariante. **Standard** ist das gerade Zapfenloch
  (rechteckiger Quaderkörper). **Schwalbenschwanz** trägt
  zusätzlich einen Konuswinkel κ. **Haus** trägt eine zusätzliche
  flache Anlagestufe an der Bezugsfläche.
- **κ** ∈ [0, π/4]: **Konuswinkel** der Schwalbenschwanz-Variante
  (Neigung der schmäleren Seitenwände nach innen). Bei
  variante ≠ Schwalbenschwanz ist κ = 0. Berufssprachliche
  Faustregeln: κ = atan(1/7) für Nadelholz, κ = atan(1/8) für
  Laubholz.

Sei T_F→B ∈ SE(3) die Starrkörpertransformation, die das
Flächen-Koordinatensystem (O_F, e_hat_u^F, e_hat_v^F, e_hat_n^F) in das
Bauteil-Lokal-System L_B überführt; T_F→B ist durch die Wahl
von F und O_F eindeutig bestimmt.

### Werkzeugkörper

Der **Werkzeugkörper** des Zapfenlochs ist im Flächen-Koordinaten-
system zunächst durch die in der Bezugsfläche liegende
Loch-Öffnung und die Tiefen-Extrusion gegeben.

Sei R(ψ) ∈ SO(2) die ebene Rotation um ψ; das Loch-Rechteck in
der Bezugsfläche ist

```
□_F  :=  { (u, v) ∈ ℝ² |
           |u − u_0|_R(ψ) ≤ b/2  und  |v − v_0|_R(ψ) ≤ h/2 }       (2)
```

(achs-paralleler Rechteckbereich nach Rotation um ψ).

Für die **Standard-Variante** ist der Werkzeugkörper das
gerade Prisma

```
K_ZL^Standard  :=  □_F × [0, t]   ⊂   ℝ² × ℝ⁺                     (3)
```

im Flächen-Koordinatensystem, wobei die dritte Komponente die
Tiefe in Richtung e_hat_n^F ist. In Bauteil-Lokal-Koordinaten:

```
K_ZL^Standard(B, p_ZL)  :=  T_F→B( □_F × [0, t] ).                (4)
```

Für die **Schwalbenschwanz-Variante** (DovetailMortise) ist
der Werkzeugkörper ein Pyramidenstumpf mit zur Eintrittsfläche
hin schmäler werdendem Querschnitt:

```
K_ZL^Schwalbenschwanz  :=  { (u, v, z) ∈ ℝ³ |  0 ≤ z ≤ t,
   (u, v) ∈ □_F^{ψ, b(z), h} }                                    (5)
```

mit

```
b(z)  :=  b  −  2 · z · tan(κ),   (Loch verengt sich nach innen
                                   in u-Richtung um den Konus κ),
```

bzw. — je nach Schwalbenschwanz-Orientierung — verengt sich
v(z) statt b(z). Geometrisch ist K_ZL^Schwalbenschwanz ein
gerader Pyramidenstumpf mit rechteckigen Grund- und Deckflächen
unterschiedlicher Breite, dessen kleinere Fläche an der
Bezugsfläche F liegt.

Für die **Haus-Variante** (HouseMortise) ist der Werkzeug-
körper die Vereinigung des Standard-Werkzeugkörpers mit einer
zusätzlichen flachen Anlagestufe an der Bezugsfläche:

```
K_ZL^Haus  :=  K_ZL^Standard  ∪  □_F^{Haus} × [0, t_Haus],         (6)
```

mit einem grösseren Rechteck □_F^{Haus} ⊃ □_F (Schultern der
Anlagestufe) und einer kleinen Stufentiefe t_Haus ≪ t (typisch
5–20 mm). Die Haus-Variante wird in den meisten App-Kontexten
durch ein eigenes Parameter-Subtupel mit (b_Haus, h_Haus,
t_Haus) ergänzt; die genaue Parameter-Form ist Folgearbeit beim
Tool, das Haus-Zapfenlöcher erstmals braucht.

In allen Varianten ist die **Wirkung** des Zapfenlochs auf das
Bauteil B die Boole'sche Differenz nach `bearbeitung`:

```
G_B'(F)  :=  G_B^lokal  \  K_ZL^{variante}(B, p_ZL).               (7)
```

Damit ist ein **Zapfenloch** (als Subtyp von `bearbeitung`)
das Tupel

```
F_ZL  :=  (uuid, typ = Zapfenloch, parameter = p_ZL,
          lokale_platzierung = id_SE(3), bezeichnung?)             (8)
```

mit den Pflicht- und Optionalfeldern aus `bearbeitung`. Das
zugehörige Bauteil B ist **nicht Bestandteil des Tupels**,
sondern ergibt sich aus der partitiven Komposition: das
Zapfenloch ist Element der Bearbeitungs-Liste genau eines
Bauteils. Die lokale Platzierung F_ZL.lokale_platzierung ist im
Standardfall die Identität in SE(3), weil die Positionierung
bereits vollständig durch (F, u_0, v_0, ψ) im Parametertupel
getragen ist; eine nicht-identische Platzierung kommt nur in
Sonderfällen vor (etwa wenn ein gemeinsamer
Werkzeug-Bezugspunkt mehrerer gleichartiger Zapfenlöcher
gewählt wird).

## Wohldefiniertheit

- **Existenz**: Für jede zimmermannsmässig gestemmte oder
  gestochene Aussparung zur Aufnahme eines Zapfens lässt sich
  das Tupel (uuid, typ = Zapfenloch, p_ZL, id_SE(3), ⊥)
  angeben; mit Default-Werten variante = Standard,
  b = Zapfenbreite, h = Zapfenhöhe, t = Zapfenlänge + 8 mm
  (mittlere Zapfenluft), ψ = 0, κ = 0 entsteht das Standard-
  Zapfenloch nach DIN 1052 §15.
- **Eindeutigkeit der Werkzeugkörper-Konstruktion**: Bei
  festgelegter Bezugsfläche F, Parametertupel p_ZL und Bauteil B
  mit bekannter `lokalePlatzierung` ist das Loch-Rechteck □_F
  nach (2) durch (u_0, v_0, b, h, ψ) eindeutig festgelegt, und
  der Werkzeugkörper nach (4)/(5)/(6) ist eindeutig bestimmt.
- **Unabhängigkeit von der Wahl des Flächen-Ursprungs**: Eine
  andere Wahl von O_F (etwa eine andere Ecke der Bezugsfläche
  als Ursprung) führt zu transformierten Parametern (u_0', v_0',
  ψ'), die denselben Werkzeugkörper beschreiben. Die Wahl ist
  Modellierungskonvention; semantisch invariant.
- **Geometrische Nicht-Degeneriertheit (harte Invarianten,
  Validierungsfehler bei Verletzung)**:
  1. **Lochbreite-Positivität**: b > ε_L.
  2. **Lochhöhen-Positivität**: h > ε_L.
  3. **Lochtiefe-Positivität**: t > ε_L. Ein Zapfenloch mit
     Tiefe 0 ist keine Aussparung, sondern eine Anriss-
     Markierung.
  4. **Lochtiefe-Beschränkung am Bauteil**: t ≤ d_F(B) − ε_L,
     wobei d_F(B) die Bauteildicke in Richtung e_hat_n^F ist
     (also der lotrechte Abstand von F zur gegenüberliegenden
     Bauteilfläche). Ein Zapfenloch mit Tiefe ≥ d_F(B) ist
     ein **durchgehendes Zapfenloch** (Schlitz / through
     mortise), das in der App entweder als Sonderfall mit
     t = d_F(B) − ε_L (gerade noch geschlossen) oder als
     eigene Bearbeitung `schlitz` (Folgearbeit) geführt wird;
     siehe Erläuterung.
  5. **Loch innerhalb der Bezugsfläche**: das Loch-Rechteck
     □_F muss vollständig in der Bezugsfläche F liegen, also
     bei einer rechteckigen F mit Abmessungen (u_max, v_max)
     gilt
     ```
     |u − u_0|_R(ψ) ≤ b/2  und  |v − v_0|_R(ψ) ≤ h/2
     ⇒  0 ≤ u ≤ u_max  und  0 ≤ v ≤ v_max  für alle
        Eckpunkte des rotierten Rechtecks.
     ```
     Ein Zapfenloch, dessen Öffnung über den Rand der
     Bezugsfläche hinausragt, ist im Bauteil wirkungslos und
     wird als `ZapfenlochAusserhalbBezugsflaeche` abgelehnt
     (Validierungsfehler, analog zu
     `KervePositionAusserhalbBauteil` in `hg_kerve.md`).
  6. **Konuswinkel-Beschränkung**: bei variante =
     Schwalbenschwanz gilt 0 < κ ≤ π/4 und b − 2 · t · tan(κ)
     > ε_L (die schmälere Seite des Schwalbenschwanzes muss
     positive Breite haben); bei variante = Standard und
     variante = Haus ist κ = 0 strukturell erzwungen.
  7. **Drehwinkel-Wertebereich**: ψ ∈ [−π/2, π/2]; im
     Datentyp als gewickelter Wert geführt.
- **Wohldefiniertheit der Wirkung**: G_B'(F) nach (7) ist die
  Boole'sche Differenz beschränkter, abgeschlossener
  Polyeder; nach `bearbeitung` strukturell wohldefiniert.
- **Plausibilität (weiche Invarianten, Warnung; kein
  Validierungsfehler — siehe `quellenkonflikt`-Block):**
  1. **Mindest-Restholz zu den Bauteil-Längsseiten**:
     auf jeder Seite des Loch-Rechtecks (in u- und v-Richtung)
     muss das verbleibende Restholz die Konstante
     `Toleranzen.ZAPFENLOCH_RESTHOLZ_SEITLICH_MIN` (Standard
     30 mm) einhalten. Verletzung → `Warnung.
     ZapfenlochZuNahAmRand`.
  2. **Mindest-Restholz unter dem Loch**: d_F(B) − t ≥
     `Toleranzen.ZAPFENLOCH_RESTHOLZ_UNTEN_MIN` (Standard
     gleich der Lochtiefe t, also d_F(B) ≥ 2 · t). Verletzung
     → `Warnung.ZapfenlochZuTief` mit Hinweis auf
     EC5 §6.1.5 Querdruck-Nachweis und ggf. EC5 §6.5
     Schubnachweis am verbleibenden Holz unterhalb der
     Aussparung.
  3. **Zapfenluft** (greift nur im Tragwerks-Kontext, wenn
     ein zugeordneter Zapfen identifiziert ist): t − ℓ_Zapfen
     ∈ [`Toleranzen.ZAPFENLUFT_MIN`,
     `Toleranzen.ZAPFENLUFT_MAX`] (Standardwerte 5 mm bzw.
     10 mm). Verletzung → `Warnung.ZapfenluftAusserhalb`.
- **Subtraktivität (geerbt von `bearbeitung`)**: G_B'(F) ⊆
  G_B^lokal nach (7); siehe `bearbeitung`.
- **Zuordnungs-Eindeutigkeit**: Das Zapfenloch ist über die
  partitive Komposition genau einem Bauteil zugeordnet. Dass
  ein Zapfenloch mit einem Zapfen am Anschlussbauteil eine
  Zapfenverbindung herstellt, ist **keine** geometrische
  Voraussetzung der Zapfenloch-Geometrie selbst, sondern
  ergibt sich erst im Tragwerks-Kontext (siehe `verbindung`,
  `VerbindungsTyp.ZimmermannsmaessigerAnschluss`, Folgearbeit).
- **Nicht-Zirkularität**: Die Definition stützt sich nur auf
  bereits definierte Begriffe (`bearbeitung`, `bauteil`,
  `polyeder`, `lokales_koordinatensystem`, `bauteilachse`,
  `punkt`, `vektor`, `einheitsvektor`, `toleranzen`, `uuid`).
  Der parallele Begriff `zapfen` erscheint nur in der
  Erläuterung und in `abgrenzung_zu:`, nicht in der
  geometrischen Definition selbst.

## Erläuterung (nicht normativ)

### Zapfenverbindung als Gesamt-Konzept

Das Zapfenloch ist die **Aussparungs-Hälfte** des klassischen
zimmermannsmässigen Paares **Zapfen + Zapfenloch**. Die
Zapfenverbindung (engl. *mortise and tenon joint*) ist eine
der ältesten und im DACH-Holzbau am weitesten verbreiteten
Holzverbindungen: ein hervorstehender Zapfen am einen Bauteil
(typisch Stuhlsäule, Stiel, Strebe, Riegel-Endholz) wird in
ein passgenau gestemmtes Zapfenloch am anderen Bauteil
(typisch Pfette, Schwelle, Rähm, Hauptträger) eingeführt; die
Kraftübertragung erfolgt **primär durch Vollholz-Kontakt
zwischen den anliegenden Brust- und Schulterflächen**, nicht
durch den Zapfen selbst.

### Wirkungsmechanismus

Die Zapfenverbindung übernimmt:

- **Druck längs zur Faser des hervorstehenden Bauteils**:
  durch Vollholz-Kontakt zwischen der Brust am Anschlussbauteil
  und der angrenzenden Aussenfläche des Trägerbauteils.
  **Nicht** durch die Zapfenstirn — dort ist die **Zapfenluft**
  von 5–10 mm konstruktiv eingerechnet, damit Schwund und
  Quellung des Holzes nicht die Bauteile auseinanderdrücken.
- **Querkraft**: durch den Zapfen-Schaft, der in der Lochwand
  des Zapfenlochs **rechtwinklig zur Faser** des Trägerbauteils
  drückt. Bemessungs-Anker: **EC5 §6.1.5 (Querdruck,
  Druck rechtwinklig zur Faser)** an der Lochwand.
- **Zug**: nur eingeschränkt. Die Standard-Zapfenverbindung
  ist **nicht zugfest**. Zug wird klassisch über einen
  **Holznagel** quer durch Zapfen und Zapfenloch oder über einen
  **Keil** an der Zapfenstirn übertragen. Die
  **Schwalbenschwanz-Variante** ist durch ihre Geometrie in
  einer Richtung zugfest.
- **Biegung**: sehr eingeschränkt; die Zapfenverbindung wird im
  Holzbau klassisch als **gelenkartiger Anschluss** modelliert.

Die Bemessungs-Stelle ist — abweichend von einer in der
Auftrags-Vorbereitung naheliegenden Annahme — **nicht** EC5
§8 (das regelt **metallische Verbindungsmittel**), sondern:

- **EC5 §6.1.5** für den Wirkungsmechanismus (Querdruck an
  der Lochwand),
- **DIN EN 1995-1-1/NA** und **DIN 1052 §15** in Deutschland
  bzw. **SIA 265 Anhang A** in der Schweiz für die
  zimmermannsmässige Bemessung als Gesamtnachweis.

### Typologie

Das Zapfenloch tritt in mehreren konstruktiv unterschiedenen
Varianten auf:

- **Einfaches Zapfenloch** (Standard, BTLx `Mortise`): ein
  rechteckiger Hohlraum mit Lochtiefe < Bauteildicke
  (Blindloch). Standardfall an Pfetten, Schwellen und Rähmen.
- **Doppel-Zapfenloch**: zwei parallele Zapfenlöcher
  nebeneinander, zur Aufnahme zweier Zapfen am selben
  Anschlussbauteil; modelliert als zwei `Zapfenloch`-Instanzen
  mit eigenen UUIDs in derselben Bearbeitungs-Liste, nicht
  als eigener Subtyp.
- **Durchgehendes Zapfenloch (through mortise)**:
  Lochtiefe = Bauteildicke, der Zapfen tritt auf der
  Rückseite wieder aus. Geometrisch geht das Standard-
  Zapfenloch hier in den Sonderfall t = d_F(B) − ε_L über;
  in der DACH-Berufssprache wird die durchgehende Variante
  uneinheitlich auch `schlitz` genannt — **diese Wurzel-
  Benennung ist im Glossar abgelehnt** (siehe
  `abgelehnte_benennungen:`): „Schlitz" ist im Glossar für
  Schlitzblech-Aufnahmen reserviert (längliche schmale
  Subtraktionen mit geringer Breite und grosser Tiefe zur
  Aufnahme eines Stahlblechs, eigener Folgeeintrag
  `hg_schlitz.md`). Die berufssprachliche Doppelnutzung wird
  anerkannt, im Glossar aber zugunsten der scharfen Trennung
  Zapfenloch ↔ Schlitz nicht übernommen.
- **Schwalbenschwanz-Zapfenloch** (BTLx `DovetailMortise`):
  Querschnitt verengt sich von der Bezugsfläche aus nach
  innen (typischer Konus κ = atan(1/7) für Nadelholz,
  atan(1/8) für Laubholz); zugfest in einer Richtung.
  Klassischer Anschluss Nebenträger ↔ Hauptträger.
- **Brustzapfen-Loch / Haus-Zapfenloch** (BTLx
  `HouseMortise`): rechteckiges Zapfenloch mit zusätzlicher
  flacher Anlagestufe (Haus, Schulter) an der Bezugsfläche;
  schafft eine grössere Flächen-Anlage gegen die Brust des
  Zapfens und ist druckfest auch quer zur Zapfenachse.
  Klassisch bei Balken-Wechseln und bei der Anschlusskette
  Stuhlsäule ↔ Schwelle.
- **Japanisches Zapfenloch** (BTLx `JapaneseMortise`):
  Mehrflächen-Geometrie mit asymmetrischen Aufweitungen
  oder schrägen Wänden; in der DACH-Tradition unüblich,
  als Folgearbeit `japanisches_zapfenloch` zu führen.

Eine **normativ kodifizierte Typologie** existiert in den
zugänglichen Normen nicht; die obige Liste folgt dem
DACH-Berufssprache-Konsens und der BTLx-Spec.

### Geometrie-Konsens: Zapfenluft

Die in der Wikipedia-Definition und im
DACH-Berufssprache-Konsens überlieferte Geometrieregel
**Lochtiefe = Zapfenlänge + 5…10 mm** trägt einen
konstruktiven Grund: das Vollholz arbeitet (Schwund und
Quellung, vor allem in tangentialer Richtung); die Zapfenluft
sorgt dafür, dass die Bauteile sich nicht über den Zapfen
abstützen und auseinanderdrücken, sondern den Kraftpfad über
die anliegenden Brust- und Schulterflächen führen. Diese
Geometrieregel ist im Glossar **kein Bestandteil der
Zapfenloch-Definition selbst** (das Zapfenloch ist
geometrisch wohldefiniert auch ohne zugeordneten Zapfen),
sondern tritt erst im Tragwerks-Kontext der Zapfenverbindung
auf.

### BTLx- und IFC-Übersetzung (Export-Schicht, Phase 4)

**BTLx 2.1** modelliert das Zapfenloch über mehrere
Processings, je nach Variante:

| App-Variante         | Primäre BTLx-Entsprechung   | Anmerkung                       |
|----------------------|------------------------------|----------------------------------|
| Standard             | `Mortise`                    | rechteckiges Blindloch           |
| Schwalbenschwanz     | `DovetailMortise`            | mit ConeAngle κ                  |
| Haus                 | `HouseMortise`               | mit zusätzlicher Anlagestufe     |
| Japanisch (Folgearbeit) | `JapaneseMortise`         | Mehrflächen-Geometrie            |

**IFC 4.3** modelliert das Zapfenloch generisch als
`IfcOpeningElement` mit `IfcRelVoidsElement`-Beziehung zum
Trägerbauteil (analog zu allen anderen subtraktiven
Bearbeitungen); die Variante wird über die explizite
Geometrie (Solid / SweptSolid) ausgedrückt, nicht über einen
eigenen IFC-Typ.

### Tätigkeit vs. Resultat

Im Sprachgebrauch bezeichnet **„zapfenlochen"** oder
**„stemmen"** die Tätigkeit (Herstellen des Zapfenlochs mit
Stemmeisen, Hohleisen, Kettenfräse oder CNC). Dieser
Glossareintrag definiert ausschliesslich die **Resultatslesart**:
die geometrische Aussparung am fertigen Bauteil. Die Tätigkeit
und ihre Werkzeug-/Reihenfolge-Wahl sind Gegenstand der
Fertigungs-Schicht.

## Beziehungen

- **Oberbegriff**: `bearbeitung`. Strukturell ist das
  Zapfenloch eine konkrete subtraktive Bearbeitung mit dem
  typspezifischen Parametertupel p_ZL.
- **Bestandteile (partitiv)** (geerbt von `bearbeitung`):
  - **UUID** (`uuid`): technische Identität, Pflicht.
  - **Typ**: konstant `Zapfenloch`.
  - **Parameter** (typspezifisch): F, u_0, v_0, b, h, t, ψ,
    variante, κ.
  - **Lokale Platzierung**: SE(3); im Standardfall die Identität.
  - **Bezeichnung**: optional.
  - **Keine Backref auf das Bauteil**: das zugehörige Bauteil
    (typisch eine Pfette, Schwelle, ein Rähm oder ein
    Hauptträger) ist über die partitive Komposition bestimmt,
    nicht über ein Feld am Zapfenloch-Objekt.
- **Verwendung**:
  - Bestandteil eines **Bauteils** (`bauteil`): das Zapfenloch
    erscheint als Bearbeitung in der Liste der Bauteil-
    Bearbeitungen; geometrisch sitzt es an einer Bezugsfläche
    F ∈ 𝓕(B) des Bauteilkörpers.
  - **Aufnahme eines Zapfens** (`zapfen`): das Zapfenloch
    bildet die formschlüssige Aufnahme; die Paarung
    Zapfenloch ↔ Zapfen wird **nicht** im Zapfenloch selbst
    geführt, sondern erst auf der Aggregats-Ebene über
    `verbindung` mit
    `VerbindungsTyp.ZimmermannsmaessigerAnschluss`.
- **Spezialisierungen** (Folgearbeit, eigene Glossareinträge
  bei Bedarf):
  - **Schwalbenschwanz-Zapfenloch**: hier als Variante des
    Standard-Zapfenlochs mit Konuswinkel κ geführt; bei
    eigenständigem Glossareintrag-Bedarf wäre der Eintrag
    `schwalbenschwanz_zapfenloch` (Folgearbeit).
  - **Haus-Zapfenloch / Brustzapfen-Loch**: hier als Variante
    mit zusätzlicher flacher Anlagestufe geführt.
  - **Japanisches Zapfenloch** (`japanisches_zapfenloch`,
    Folgearbeit): Mehrflächen-Geometrie, deckt das
    Standard-Modell dieses Eintrags nicht ab.
- **Abgrenzung**:
  - **Zapfen** (`zapfen`): das **hervorstehende** Element am
    **Anschlussbauteil**, das in das Zapfenloch eingeführt
    wird. Zapfen und Zapfenloch sind Welle-4-Geschwister
    derselben Verbindungsart; das Paar wird auf der
    Aggregats-Ebene über `verbindung` zusammengeführt. Der
    Zapfen ist eine Bearbeitung am anderen Bauteil.
  - **Kerve** (`kerve`): zweiflächiger dreieckiger Einschnitt
    an einem Stab-Bauteil; **kein** prismatischer Hohlraum
    mit rechteckiger Öffnung. Die Kerve trägt
    Auflagerkräfte über zwei zueinander rechtwinklige
    Flächen, das Zapfenloch über die vier Lochwände eines
    Quaders. Geometrisch klar getrennt.
  - **Bohrung** (`bohrung`, Forward-Verweis A): zylindrische
    Subtraktion. Geometrisch klar getrennt vom rechteckigen
    Zapfenloch.
  - **Versatz** (`versatz`, Forward-Verweis A): flache,
    schräge Druckfläche quer zur Faser ohne hervorstehenden
    Stift und ohne rechteckigen Hohlraum. Geometrisch klar
    getrennt.
  - **Schlitz** (`schlitz`, Forward-Verweis A): längliche
    Subtraktion mit geringer Breite und grosser Tiefe zur
    Aufnahme eines Schlitzblechs. Im DACH-Korpus
    überwiegend für Schlitzblech-Aufnahmen reserviert; die
    durchgehende Variante des Zapfenlochs ist
    berufssprachlich teilweise ebenfalls als „Schlitz"
    geführt — siehe Erläuterung.
  - **Blatt** (`blatt`, Forward-Verweis A): flächige
    Längs-Überlappung mit halber Holzdicke; weder
    rechteckige Aussparung noch hervorstehender Stift.
  - **Kamm** (`kamm`, Forward-Verweis A): einseitige
    Materialwegnahme am übergreifenden Holz; keine
    geschlossene Aussparung im Bauteilinneren.
  - **Anschnitt** (`anschnitt`, Forward-Verweis A): planare
    Schräge am Bauteilende; keine Aussparung.
  - **Aussparung** (Forward-Verweis A, Folgearbeit nach
    `hg_bohrung.md`-Konvention): allgemeiner Bearbeitungs-Subtyp
    für **große nicht-kreisförmige Sackausnehmungen** (BTLx
    `Pocket` mit nicht-kreisförmigem Profil). Das Zapfenloch ist
    eine **spezialisierte Aussparung mit rechteckiger Öffnung und
    definierter Aufnahmefunktion**. Trigger: erste Bemessung
    einer Trägeröffnung nach EC5:2025 „Design of holes in beams"
    oder erstes Tool mit großer Sackausnehmung außerhalb des
    Zapfenloch-Spektrums.
  - **Bearbeitung** (`bearbeitung`): der Oberbegriff. Das
    Zapfenloch ist eine konkrete Bearbeitung, kein
    Bearbeitungs-Aggregat.
  - **Bauteil** (`bauteil`): das Trägerobjekt, in dem das
    Zapfenloch sitzt. Das Zapfenloch ist kein Bauteil,
    sondern ein Merkmal eines Bauteils.
  - **Verbindung** (`verbindung`): das Tragwerks-Aggregat,
    das ein Zapfenloch an einem Bauteil mit einem Zapfen
    an einem anderen Bauteil paart. Das Zapfenloch ist
    keine Verbindung, sondern eine geometrische
    Voraussetzung dafür.
  - **Verbindungsmittel** (`verbindungsmittel`): metallische
    oder hölzerne kraftübertragende Elemente (Schraube,
    Nagel, Holznagel). Das Zapfenloch ist **kein**
    Verbindungsmittel, sondern eine Bauteilbearbeitung. Ein
    Holznagel, der den Zapfen im Zapfenloch sichert, ist
    ein eigenes Element (Verbindungsmittel), nicht Teil des
    Zapfenlochs.

## Implementierungshinweis

Datentyp (Domänen-Schicht, Kotlin, Schicht
`domain.bauteil.bearbeitung`):

```kotlin
package domain.bauteil.bearbeitung

import domain.geometrie.LokalePlatzierung
import java.util.UUID

/**
 * Zapfenloch: rechteckige (oder schwalbenschwanzförmige)
 * prismatische Aussparung am Trägerbauteil zur Aufnahme eines
 * Zapfens (siehe `Zapfen`).
 *
 * Glossar: hg_zapfenloch.md.
 *
 * Phase 4.x (Folgearbeit, Trigger: Stuhlsäulen-Pfetten-
 * Anschluss).
 */
data class Zapfenloch(
    override val uuid: UUID,
    /** Bezugsfläche am Bauteil (BezugsflaechenId; eine der
     *  sechs Aussenflächen des Quader-Bauteilkörpers). */
    val bezugsflaeche: BezugsflaechenId,
    /** Lochmittelpunkt in u-Richtung der Bezugsfläche, in mm. */
    val u0: Double,
    /** Lochmittelpunkt in v-Richtung der Bezugsfläche, in mm. */
    val v0: Double,
    /** Lochbreite in u-Richtung, in mm. */
    val breite: Double,
    /** Lochhöhe in v-Richtung, in mm. */
    val hoehe: Double,
    /** Lochtiefe in Richtung der inneren Flächen-Normalen, in mm. */
    val tiefe: Double,
    /** Drehwinkel des Loch-Rechtecks gegen die u-Achse der
     *  Bezugsfläche, in Radiant. Standard 0.0. */
    val drehwinkel: Double = 0.0,
    /** Geometrievariante: Standard, Schwalbenschwanz, Haus. */
    val variante: ZapfenlochVariante = ZapfenlochVariante.STANDARD,
    /** Konuswinkel der Schwalbenschwanz-Variante, in Radiant.
     *  Bei variante = Standard / Haus erzwungen 0.0. */
    val konuswinkel: Double = 0.0,
    override val lokalePlatzierung: LokalePlatzierung = LokalePlatzierung.IDENTITAET,
    override val bezeichnung: String? = null,
) : Bearbeitung
```

- **Einheit**: Längen (u_0, v_0, b, h, t) in mm (Double);
  Winkel (ψ, κ) intern in Radiant (Anzeige in Grad).
- **Identität**: `uuid` ist Pflicht und persistent (RFC 9562 v7),
  unabhängig vom zugeordneten Bauteil.
- **Keine Backref auf das Bauteil**: analog zu `kerve` und
  `bearbeitung`. Die Beziehung Zapfenloch → Bauteil ist
  partitive Komposition; das Bauteil hält seine Zapfenlöcher
  als Element seiner Bearbeitungs-Liste. Die Auflösung
  „zu welchem Bauteil gehört diese Zapfenloch-UUID?" ist
  Repository-Aufgabe.
- **Bezugsflächen-Adressierung**: `BezugsflaechenId` ist ein
  enum-artiges Wertobjekt, das eine der Aussenflächen des
  Bauteilkörpers benennt (typisch sechs Werte beim Quader-
  Bauteil: `LAENGSSEITE_OBEN`, `LAENGSSEITE_UNTEN`,
  `LAENGSSEITE_LINKS`, `LAENGSSEITE_RECHTS`,
  `STIRNSEITE_ANFANG`, `STIRNSEITE_ENDE`). Die konkrete
  Geometrie der Bezugsfläche (Ursprung, e_hat_u^F, e_hat_v^F, e_hat_n^F)
  wird aus dem Bauteil-Lokal-System und dem
  Bauteil-Querschnitt abgeleitet.
- **Lebenszyklus / Komposition**: identisch zu `kerve` und
  `bearbeitung`.
- **Pflicht- und Optionalfelder (normativ)**:
  - `uuid` — Pflicht, niemals null.
  - `bezugsflaeche`, `u0`, `v0`, `breite`, `hoehe`, `tiefe` —
    Pflicht.
  - `drehwinkel` — Default 0.0.
  - `variante` — Default `STANDARD`.
  - `konuswinkel` — Default 0.0; bei variante ≠ Schwalbenschwanz
    in der Fabrik-Validierung auf 0.0 zwangsgesetzt.
  - `lokalePlatzierung` — Default `LokalePlatzierung.IDENTITAET`.
  - `bezeichnung` — `null` zulässig.
- **Invarianten** (in der Fabrikfunktion
  `Zapfenloch.aus(...)` und beim Anhängen
  `Bauteil.mitBearbeitung(zl)` prüfen; bei Verletzung
  `Resultat.Fehler` mit subtypspezifischer Variante; niemals
  Exception werfen):
  1. `breite > Toleranzen.LAENGE_EPS` →
     `ZapfenlochBreiteUngueltig`.
  2. `hoehe > Toleranzen.LAENGE_EPS` →
     `ZapfenlochHoeheUngueltig`.
  3. `tiefe > Toleranzen.LAENGE_EPS` →
     `ZapfenlochTiefeUngueltig`.
  4. `tiefe < d_F(B) - Toleranzen.LAENGE_EPS` (bauteil-relativ,
     beim Anhängen geprüft) → andernfalls
     `ZapfenlochTiefeAusserhalbBauteil`.
  5. Loch-Rechteck vollständig innerhalb der Bezugsfläche
     (bauteil-relativ, beim Anhängen geprüft) → andernfalls
     `ZapfenlochAusserhalbBezugsflaeche`.
  6. `variante == SCHWALBENSCHWANZ ⇒ 0 < konuswinkel ≤ π/4`
     und `breite - 2 * tiefe * tan(konuswinkel) >
     Toleranzen.LAENGE_EPS` →
     `SchwalbenschwanzKonusUngueltig`.
  7. `variante in {STANDARD, HAUS} ⇒ konuswinkel == 0.0`
     (strukturell durch Datentyp-Wahl erzwungen oder in
     Fabrik-Validierung auf 0.0 zwangsgesetzt).
- **Berechnung der bearbeiteten Bauteilgeometrie**: lazy on
  demand in der Geometrie-Schicht (analog zu `kerve`); die
  Domänen-Schicht hält ausschliesslich die Parameter.
- **BTLx-Export** (Phase 4): Mapping nach der Tabelle in der
  Erläuterung; Mortise / DovetailMortise / HouseMortise /
  JapaneseMortise.
- **IFC-Export** (Phase 4): `IfcOpeningElement` mit eigener
  `GlobalId` (= Zapfenloch-UUID, Base64-kodiert nach
  ISO/IEC 9834-8); Wirkung via `IfcRelVoidsElement` auf das
  Trägerbauteil.
- **Edge Cases**:
  - **Durchgehendes Zapfenloch** (t = d_F(B) − ε_L): zulässig,
    aber die Bemessungs-Schicht warnt, dass damit kein
    Restholz unter dem Loch verbleibt und EC5 §6.5 Schub
    nicht direkt anwendbar ist. Eine echte Durchstemmung
    (t = d_F(B)) ist in der App als `schlitz` (Folgearbeit)
    zu modellieren, sobald der Schlitz-Eintrag vorliegt.
  - **Schwalbenschwanz-Zapfenloch mit Konuswinkel 0**:
    strukturell unzulässig (würde die Variante semantisch
    auf Standard reduzieren); in der Fabrik-Validierung
    abgelehnt.
  - **Mehrere überlappende Zapfenlöcher**: zulässig (analog
    zu mehreren überlappenden Bearbeitungen in
    `bearbeitung`); semantisch egal in der Aggregation, aber
    in der Praxis ungewöhnlich.
  - **Zapfenloch an einem Bauteil ohne ebene Bezugsfläche**
    (krumme Bauteilkörper, NURBS-Bauteile): in der ersten
    Tool-Phase ausgeschlossen; das Zapfenloch ist nur an
    quaderförmig idealisierten Bauteilen definiert. Die
    Erweiterung auf krumme Bezugsflächen ist Folgearbeit.
- **Abgeleitete Eigenschaften** (als Funktionen, keine Felder):
  - `werkzeugkoerper(): Polyeder` —
    K_ZL^{variante}(B, p_ZL) im Bauteil-Lokal-System;
    variantenspezifische Implementierung (Quader,
    Pyramidenstumpf, Quader + Anlagestufe).
  - `oeffnungsrechteck(): Polygon` — □_F nach (2) in der
    Bezugsfläche; nützlich für die Visualisierung.
  - `lochwand_normal(): Einheitsvektor` — e_hat_n^F; Hauptachse
    des Querdruck-Nachweises an der Lochwand.
  - `querdruck_lochflaeche(): Double` — Fläche der
    drucktragenden Lochwand (b · h für Standard); Bemessungs-
    Schicht (EC5 §6.1.5).
- **Bezeichner-Konvention** (CLAUDE.md): Domänen-Klasse heisst
  `Zapfenloch` (deutsch, Glossarbegriff); Variantenenum heisst
  `ZapfenlochVariante` mit Werten `STANDARD`,
  `SCHWALBENSCHWANZ`, `HAUS`. Die Bezugsflächen-Adresse
  `BezugsflaechenId` ist ein eigener Wertbegriff (Folgearbeit,
  ggf. eigener Glossar-Hilfsbegriff).

## Quellen

**Primär (normativ):**

- DIN EN 1995-1-1:2010-12, „Eurocode 5: Bemessung und
  Konstruktion von Holzbauten – Teil 1-1", Abschnitt 6.1.5
  „Druck rechtwinklig zur Faser" (Querdruck an der Lochwand).
- DIN EN 1995-1-1/NA:2013-08, Nationaler Anhang Deutschland
  zu Eurocode 5.
- DIN 1052:2008-12, „Entwurf, Berechnung und Bemessung von
  Holzbauwerken", Abschnitt 15 „Zimmermannsmässige Verbindungen".
- SIA 265:2021, „Holzbau", Schweizerischer Ingenieur- und
  Architektenverein, Zürich, Anhang A „Zimmermannsmässige
  Verbindungen".
- design2machine: *BTLx interface description*, Version 2.1,
  16.11.2023, Processings `Mortise`, `DovetailMortise`,
  `HouseMortise`, `JapaneseMortise`.
- ISO 16739-1:2024, „Industry Foundation Classes (IFC) for
  data sharing in the construction and facility management
  industries — Part 1: Data schema" (`IfcOpeningElement`,
  `IfcRelVoidsElement`).

**Sekundär:**

- Mönck, W.; Rug, W.: *Holzbau – Bemessung und Konstruktion.*
  16. Auflage, Beuth, Berlin 2015, Kap. 7 „Verbindungen".
- Blass, H. J.; Sandhaas, C.: *Ingenieurholzbau – Grundlagen
  der Bemessung.* KIT Scientific Publishing, Karlsruhe 2016,
  Kap. 8.
- Natterer, J.; Herzog, T.; Volz, M.: *Holzbau-Atlas.*
  4. Auflage, Birkhäuser, Basel 2003.
- Gerner, M.: *Fachwerk – Instandsetzung, Sanierung, Neubau.*
  DVA, 7. Auflage 2007.
- Krämer, F.: *Grundwissen des Zimmerers.* Bruderverlag,
  Karlsruhe.
- Lignum (Hrsg.): *Holzbautabellen HBT1:2021 / HBT2.* Lignum,
  Zürich.
- Claus, T.: *Zapfenverbindungen im Holzbau – bruchmechanische
  Analyse und Vorschlag eines Berechnungsmodells.* Bautechnik
  97 (2020), Wiley.
- Informationsdienst Holz: *Tragverhalten zimmermannsmässiger
  Holzverbindungen.*

**Korpus (nicht autoritativ):**

- Wikipedia, Lemma „Zapfenverbindung" (de.wikipedia.org,
  abgerufen 2026-05-14).
- Wikipedia, Lemma „Mortise and tenon" (en.wikipedia.org,
  abgerufen 2026-05-14).
- baunetzwissen.de, „Zimmermannsmässige Verbindungen".
- baubeaver.de, „Zimmermannsmässige Holzverbindungen".
- bauredakteur.de, „Holzverbindungen — Zimmerer und Schreiner".
- zimmerer-treff.com, „Zapfenverbindungen".
- schreiner-seiten.de, „Schlitz und Zapfen".
- Recherche-Bericht
  `docs/recherche/2026-05-14_hg_zapfen.md` (interner Anker
  für die Quellen-Synthese, einschliesslich Sandbox-blockierter
  Norm-Volltexte).
