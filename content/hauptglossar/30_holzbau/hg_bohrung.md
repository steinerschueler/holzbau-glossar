---
id: bohrung
benennung: Bohrung
synonyme: [Bohrloch]
abgelehnte_benennungen: [Loch, "Öffnung", "drill hole", "bore", "hole", "Drilling", "Sackloch", "Durchgangsloch"]
oberbegriff: bearbeitung
begriffstyp: partitiv
voraussetzungen: [bearbeitung, bauteil, uuid, lokales_koordinatensystem, punkt, vektor, polyeder, querschnitt, toleranzen]
abgrenzung_zu: [bearbeitung, verbindungsmittel, kerve, anschnitt, versatz, zapfen, zapfenloch, aussparung, ausklinkung, schlitz, senkbohrung, vorbohrung]
status: entwurf
theorie_pflichtig: required
quellen_primär:
  - "DIN EN 1995-1-1:2010-12 (Eurocode 5), Abschnitt 5.2 (Berücksichtigung der Querschnittsschwächungen): Bohrungen reduzieren den anrechenbaren Nettoquerschnitt; die geschwächte Stelle ist Bemessungsobjekt. Eine geometrische Definition des Begriffs 'Bohrung' enthält der Eurocode nicht; er wird als Tatbestand vorausgesetzt."
  - "DIN EN 1995-1-1:2010-12 (Eurocode 5), Abschnitt 8.3.1.2 (Nägel): Vorbohrpflicht für ρ_k > 500 kg/m³ und Nageldurchmesser d > 6 mm (in einigen Editionen d > 8 mm); Holzteildicke t < max{ 7d ; (13d − 30) · ρ_k / 400 }. Die Vorbohrung ist als Bohrloch geringeren Durchmessers vor dem Eintreiben des Nagels auszuführen."
  - "DIN EN 1995-1-1:2010-12 (Eurocode 5), Abschnitt 8.5 (Bolzen): Bohrloch im Holz darf den Bolzennenndurchmesser um bis zu 1 mm übersteigen (gewöhnliche Bolzen); beim Passbolzen ist das Bohrloch gleich dem Nenndurchmesser auszuführen. Im Stahlblech bis zu d + 2 mm."
  - "DIN EN 1995-1-1:2010-12 (Eurocode 5), Abschnitt 8.6 (Stabdübel): Bohrloch im Holz ist mit dem Nenndurchmesser des Stabdübels auszuführen (Passsitz); Bohrloch im Stahlblech ≤ d + 1 mm."
  - "DIN EN 1995-1-1:2010-12 (Eurocode 5), Abschnitt 8.7 (Schrauben): Vorbohrpflichten typabhängig; Holzschrauben in der Regel ab d ≥ 6 mm bei ρ_k ≤ 500 kg/m³, ab d ≥ 4 mm bei ρ_k > 500 kg/m³ vorzubohren. Vollgewindeschrauben mit ETA in den ETA-Grenzen vorbohrfrei."
  - "SIA 265:2021 'Holzbau', Abschnitt 4.6 (Querschnittswerte) und Anhang A (Verbindungsmittel): Bohrungen als Querschnittsschwächung im Nettoquerschnitt; Vorbohr- und Passsitz-Regeln analog Eurocode 5."
  - "ISO 16739-1:2024 'Industry Foundation Classes (IFC) – Part 1: Data schema' (IFC 4.3.2), Entität 'IfcOpeningElement' (Spezialisierung von 'IfcFeatureElementSubtraction'), PredefinedType-Enum 'IfcOpeningElementTypeEnum' (Werte 'OPENING', 'RECESS', 'USERDEFINED', 'NOTDEFINED'); zylindrische Bohrungen werden über einen 'SweptSolid'-Body mit 'IfcExtrudedAreaSolid' und 'IfcCircleProfileDef' repräsentiert; Voiding-Beziehung über 'IfcRelVoidsElement'. Der frühere Subtyp 'IfcOpeningStandardCase' (IFC 4.0/4.1) ist in IFC 4.3 entfernt. [direkt]"
  - "design2machine: 'BTLx interface description', Version 2.1, 16.11.2023, Abschnitt 'Drilling' (Parameter StartX, StartY, Angle, Inclination, DepthLimited, Depth, Diameter) und Abschnitt 'Pocket' (für grosse Sacklöcher und rechteckige Taschen)."
quellen_sekundär:
  - "Mönck, W.; Rug, W.: Holzbau – Bemessung und Konstruktion. 16. Aufl., Beuth, Berlin 2015, Kap. 7 'Verbindungen': Bohrlochtoleranzen für Bolzen, Stabdübel, Passbolzen."
  - "Blass, H. J.; Sandhaas, C.: Ingenieurholzbau – Grundlagen der Bemessung. KIT Scientific Publishing, Karlsruhe 2016, Kap. 8 'Verbindungen': Vorbohrung als Spaltvermeidungs-Massnahme bei stiftförmigen Verbindungsmitteln."
  - "Holzbau-Handbuch, Reihe 2 'Tragwerksplanung', Teil 1 'Verbindungen', Folge 1 'Verbindungen mit stiftförmigen Verbindungsmitteln', Informationsdienst Holz, aktuelle Auflage: Vorbohr-Praxis und Bohrlochtoleranzen."
  - "ETA-11/0190, 'Würth ASSY plus VG, ASSY 3.0, ASSY 4.0': Vorbohrgrenzen für Vollgewindeschrauben in ETA-Bewertung."
  - "Z-9.1-519, 'Schrauben mit Vollgewinde als Verbindungsmittel und als Verstärkung von Holzbauteilen' (SPAX, DIBt): Vorbohr-Vorgaben."
  - "Recherche-Bericht docs/recherche/2026-05-14_hg_bohrung.md (Bestand-Verortung, Typologie, IFC/BTLx-Mapping, Quellen-Tier-Bewertung)."
quellenkonflikt: |
  Keine Holzbau-Norm (DIN EN 1995-1-1, SIA 265, DIN 1052, DIN 68800)
  führt eine geschlossene geometrische Definition des Begriffs
  'Bohrung'. Eurocode 5 und SIA 265 setzen den Begriff durchgängig
  als Tatbestand voraus und regeln nur seine Bemessungsfolgen
  (Querschnittsschwächung nach EC5 5.2; Bohrlochdurchmesser-
  Vorgaben für stiftförmige Verbindungsmittel nach EC5 8.3.1.2,
  8.5, 8.6, 8.7). Eine geschlossene parametrische Spezifikation
  existiert nur in den Austauschformaten BTLx 2.1 ('Drilling' /
  'Pocket') und IFC 4.3 ('IfcOpeningElement' mit
  'IfcCircleProfileDef'); beide sind Schemata für Datenaustausch,
  keine Definitionsquellen für das Domänenmodell.

  Der vorliegende Eintrag rekonstruiert die geometrische Definition
  aus drei sich ergänzenden Bezugspunkten, konsistent mit allen
  konsultierten Quellen:

  (a) **Werkzeugzentrierte Korpussprache** (Maschinenbau, Holzbe-
      und -verarbeitung): Bohrung als materialabtragende Operation
      eines rotierenden zylindrischen Werkzeugs mit definiertem
      Schneiddurchmesser, charakterisiert durch Nenndurchmesser,
      Tiefe und Achse.

  (b) **Resultatszentrierte Glossarsicht** (gemäss `hg_bearbeitung`):
      Eine Bohrung ist nicht die Werkzeugtätigkeit, sondern das
      geometrische Resultat am bearbeiteten Bauteil — der
      kreiszylindrische Materialabtrag.

  (c) **Austauschformat-konsistente Parametrisierung**: Achse,
      Nenndurchmesser, Tiefen-Erstreckung (Durchgang/Sackloch),
      Startpunkt — die gemeinsame Schnittmenge der BTLx-`Drilling`-
      und IFC-`IfcOpeningElement`-Parametersätze.

  Daraus folgt die geometrische Wurzeldefinition: eine Bohrung ist
  ein **kreiszylindrischer subtraktiver Werkzeugkörper** an einem
  Bauteil. Diese Festlegung ist normativ tragfähig, weil sie keine
  Aussage trifft, die einer der konsultierten Normen widerspricht;
  sie ist gleichzeitig schärfer als jede Einzelquelle, weil sie die
  Zylindrizität als definierendes Merkmal explizit macht.

  **Zweiachsige Typologie der Bohrung:**

  Achse 1 — **Tiefen-Erstreckung** (im Frontmatter-Parametertupel
  `tiefenart`):

  - **Durchgangsbohrung**: Werkzeugkörper durchstösst das Bauteil
    vollständig; im Modell parametrisch durch die Marke
    `tiefenart = DURCHGANG`. IFC-Pendant: `IfcOpeningElementTypeEnum.OPENING`.
    BTLx-Pendant: `Drilling` mit `DepthLimited = false`.
  - **Sackbohrung** (Sackloch): Werkzeugkörper hat definierte
    Tiefe kleiner als die Bauteildurchstossweite entlang der
    Achse; im Modell `tiefenart = SACKLOCH`, zusätzlich ist die
    Tiefe `t` gebunden. IFC-Pendant: `IfcOpeningElementTypeEnum.RECESS`.
    BTLx-Pendant: `Drilling` mit `DepthLimited = true` (kleine bis
    mittlere Durchmesser) bzw. `Pocket` (grosse Durchmesser oder
    nicht-kreisförmige Sacklöcher; im Glossar dann **keine**
    Bohrung mehr, sondern eigener Subtyp `aussparung`).

  Diese Unterscheidung ist im **Parametertupel** der Bohrung
  geführt, nicht in eigenen Subtypen. Begründung: die geometrische
  Definition (kreiszylindrischer Werkzeugkörper) ist identisch; die
  Tiefen-Erstreckung ist eine Marke am selben Werkzeugkörper-
  Konstruktor.

  Achse 2 — **Funktion** (eigene Glossar-Subtypen, Folgearbeit):

  - **Technische Bohrung**: eigenständige Bohrung ohne
    Verbindungsmittel-Bezug (Lüftungsbohrung, Elektrokabel-
    Durchführung, Glued-in-Rod-Bohrung für eingeleimte
    Gewindestangen, Plattenheizungs-Rohrführung). Standardfall
    dieses Eintrags.
  - **Vorbohrung**: funktional spezialisierte Bohrung mit Bezug
    auf ein folgendes Verbindungsmittel (kleinerer Durchmesser zur
    Spaltvermeidung bei Nägeln nach EC5 8.3.1.2 und Schrauben
    nach EC5 8.7). Geometrisch identisch zu einer Bohrung; trägt
    keine eigene Werkzeugkörper-Geometrie, sondern eine
    funktionale Annotation. Im Modell **nicht** als eigenständige
    Bohrung modelliert, sondern als Folgegeometrie des
    Verbindungsmittels (siehe Erläuterung).
  - **Senkbohrung** (Senkung): Komposition aus Zylinderbohrung
    und kegelförmiger bzw. stufenförmiger Erweiterung am
    Bohrungseingang zur Aufnahme eines Schraubenkopfs oder einer
    Beilagscheibe. Geometrisch **keine reine Bohrung mehr**;
    eigener Bearbeitungs-Subtyp `senkbohrung` (Folgearbeit,
    Trigger: erste sichtbare Schraubverbindung mit Senkkopf).
  - **Passbohrung** (Passsitz-Bohrung): Bohrung, deren
    Durchmesser den Nenndurchmesser des einzusetzenden
    Verbindungsmittels exakt trifft (Stabdübel nach EC5 8.6,
    Passbolzen nach EC5 8.5). Geometrisch identisch zu einer
    Bohrung; die Passsitz-Bedingung ist eine
    Verbindungsmittel-Annotation, kein eigener Bohrungs-Subtyp.

  **Verbindungsmittel-Folgebohrungen sind nicht als eigenständige
  Bohrungen modelliert.** Eine Bohrung im Sinne dieses Glossars
  ist eine eigenständige Bearbeitung am Bauteil ohne
  Verbindungsmittel-Träger. Sobald eine Bohrung durch ein
  Verbindungsmittel verursacht wird (Schraube, Bolzen, Stabdübel,
  Nagel, Vollgewinde-Verstärkungsschraube), wird sie als
  Folgegeometrie des Verbindungsmittels geführt und erscheint
  erst beim BTLx-Export als `Drilling`-Processing am Bauteil
  (siehe `hg_bearbeitung.md` Erläuterung 'Vier Element-Subklassen
  vs. Bearbeitung' und `hg_verbindungsmittel.md` Edge Case
  'Verbindungsmittel mit |verbindet| = 1'). Diese
  Modell-Festlegung ist nicht definitorisch durch eine Norm
  erzwungen, sondern eine App-interne Disambiguation der
  Werkzeug-Resultats-Mehrdeutigkeit; sie ist konsistent mit IFC
  (das `IfcOpeningElement` einer Schraube läuft über die
  generische Voiding-Beziehung) und mit BTLx (die `Drilling`-
  Geometrie ist im Export aus dem Verbindungsmittel ableitbar).

  **Quantitative EC5-Werte (Bohrlochtoleranzen, Vorbohrschwellen):**

  Die Eurocode-Vorgaben (Bohrloch ≤ d + 1 mm bei gewöhnlichen
  Bolzen, Bohrloch = d bei Stabdübeln und Passbolzen, ρ_k > 500
  kg/m³ als Vorbohrschwelle für Nägel, Schwellendurchmesser d > 6
  mm bzw. d > 8 mm zwischen Eurocode-Editionen) sind in der
  Sekundärliteratur konsistent reproduziert. Die Volltext-
  Verifikation gegen die aktuelle Eurocode-Edition ist als
  Folgearbeit markiert (Trigger: erste Implementierung einer
  Vorbohrprüfung in der Bemessungsschicht); der vorliegende
  Eintrag führt die Werte als sekundär belegt.

  **Begriffsumfang 'Loch' vs. 'Bohrung':** das Wort 'Loch'
  bezeichnet im DACH-Korpus jede Materialaussparung beliebiger
  Form (Bohrloch, Zapfenloch, Schlitz, Mannloch); 'Bohrung' ist
  die kreiszylindrische Spezialisierung. Im Glossar ist 'Loch'
  als zu generische Wurzelbenennung abgelehnt; 'Bohrloch' als
  Synonym akzeptiert.
---

## Prosa-Definition

Eine **Bohrung** ist eine Bearbeitung im Sinne von `bearbeitung`,
deren Werkzeugkörper ein endlicher Kreiszylinder ist, der durch
einen Startpunkt auf einer Bauteiloberfläche, eine
Achsrichtung als Einheitsvektor im Bauteil-Lokal-System, einen
Nenndurchmesser und eine Tiefen-Erstreckung — entweder
**Durchgangsbohrung** (Werkzeugkörper durchstösst das Bauteil
vollständig) oder **Sackbohrung** (Werkzeugkörper hat
festgelegte Tiefe kleiner als die Bauteildurchstossweite entlang
der Achse) — vollständig festgelegt ist und deren Wirkung auf
das Bauteil die Boole'sche Differenz nach `bearbeitung` Gl. (1)
mit diesem Kreiszylinder als Werkzeugkörper ist.

## Mathematische Definition

Sei

- B ein Bauteil im Sinne von `bauteil`,
- L_B = (O_B, ê_x^B, ê_y^B, ê_z^B) das Bauteil-Lokal-Koordinaten-
  system (`lokales_koordinatensystem`),
- G_B^lokal ⊂ ℝ³ die ungeschwächte Bauteilgeometrie im
  Bauteil-Lokal-System (Polyeder, siehe `polyeder`),
- p_S ∈ ℝ³ ein **Startpunkt** in Bauteil-Lokal-Koordinaten,
  liegend auf der Berandung von G_B^lokal oder im Inneren des
  Bauteils,
- â ∈ ℝ³ ein **Achseneinheitsvektor** in Bauteil-Lokal-Koordinaten
  mit ‖â‖² = 1 (im Sinne von `vektor`),
- d ∈ ℝ⁺ ein **Nenndurchmesser** (in mm),
- α ∈ {DURCHGANG, SACKLOCH} eine **Tiefen-Erstreckungsmarke**,
- t ∈ ℝ⁺ ∪ {⊥} eine **Tiefe** (in mm), mit t ∈ ℝ⁺ falls α = SACKLOCH
  und t = ⊥ falls α = DURCHGANG,
- ε_L := Toleranzen.LAENGE_EPS, ε_N := Toleranzen.NORM_EPS.

Das **Parametertupel** einer Bohrung ist

```
p_Bohrung := (p_S, â, d, α, t)                                    (1)
```

mit den oben genannten Bedingungen an die Komponenten.

### Werkzeugkörper

Sei r := d/2 der Bohrungsradius. Der **infinite Achsenzylinder**
mit Achse durch p_S in Richtung â und Radius r ist die Punktmenge

```
Z_∞(p_S, â, r)
   := { q ∈ ℝ³ |  ‖ (q − p_S) − ⟨q − p_S, â⟩ · â ‖ ≤ r }.        (2)
```

Der **Halbraum-Anker** an p_S in Achsrichtung ist

```
H_+(p_S, â)  :=  { q ∈ ℝ³ |  ⟨q − p_S, â⟩ ≥ 0 }.                  (3)
```

Der **Werkzeugkörper** der Bohrung ist dann

```
K_Bohrung(p_Bohrung)
   :=  Z_∞(p_S, â, r)  ∩  H_+(p_S, â)  ∩  Σ(α, t, p_S, â, G_B^lokal)  (4)
```

mit dem **Tiefen-Schnittkörper** Σ:

- für α = SACKLOCH:
  ```
  Σ(SACKLOCH, t, p_S, â, ·)
     :=  { q ∈ ℝ³ |  ⟨q − p_S, â⟩ ≤ t },                          (5a)
  ```
  d. h. der Werkzeugkörper ist der endliche Kreiszylinder der
  Höhe t mit kreisförmigen Endflächen rechtwinklig zu â.
- für α = DURCHGANG:
  ```
  Σ(DURCHGANG, ⊥, p_S, â, G_B^lokal)
     :=  { q ∈ ℝ³ |  ⟨q − p_S, â⟩ ≤ t_max(p_S, â, G_B^lokal) },   (5b)
  ```
  wobei
  ```
  t_max(p_S, â, G_B^lokal)
     :=  sup{ λ ∈ ℝ⁺ |  p_S + λ · â ∈ G_B^lokal }                 (6)
  ```
  die maximale Eindringlänge der Achse in das Bauteil ist (das
  Supremum existiert, da G_B^lokal beschränkt ist).

In beiden Fällen ist K_Bohrung ein abgeschlossener, beschränkter
Kreiszylinder mit kreisförmigen Endflächen rechtwinklig zu â.

### Wirkung auf das Bauteil

Die **Wirkung** einer Bohrung F = (uuid, typ = Bohrung,
p_Bohrung, T_F, bezeichnung?) auf das Bauteil B ist die
Boole'sche Differenz nach `bearbeitung` Gl. (1):

```
G_B'(F)  :=  G_B^lokal  \  T_F( K_Bohrung(p_Bohrung) ).           (7)
```

Im Standardfall (T_F = id_{SE(3)}) ist der Werkzeugkörper bereits
im Bauteil-Lokal-System; T_F wird nur dann nicht-trivial, wenn
der Werkzeugkörper-Konstruktor in einem typeigenen Bezugssystem
(z. B. mit Achse parallel zu ê_z) geführt wird und durch T_F in
die Bauteil-Lokal-Lage überführt wird.

### Bohrungs-Tupel

Damit ist eine **Bohrung** als Subtyp von `bearbeitung` das
Tupel

```
F  :=  (uuid, typ = Bohrung, parameter = p_Bohrung,
       lokale_platzierung = T_F, bezeichnung?)                    (8)
```

mit den Pflicht- und Optionalfeldern aus `bearbeitung`. Das
zugehörige Bauteil B ist **nicht Bestandteil des Tupels**,
sondern ergibt sich aus der partitiven Komposition: die Bohrung
ist Element der Bearbeitungs-Liste genau eines Bauteils
(`bearbeitung`, Abschnitt 'Wohldefiniertheit',
Eindeutigkeit der Zuordnung).

## Wohldefiniertheit

- **Existenz**: Für jede zimmermannsmässig hergestellte Bohrung
  an einem Bauteil — Lüftungsbohrung an einem Sparren, Glued-in-
  Rod-Sackbohrung an einer Stütze, Durchgangsbohrung für eine
  Elektroinstallation an einem CLT-Element — lässt sich das
  Tupel (uuid, typ = Bohrung, p_Bohrung, T_F, ⊥) angeben.
  Mindestkonfiguration: p_S auf einer Bauteilberandung, â als
  einwärts-gerichteter Einheitsvektor, d > ε_L, α = DURCHGANG,
  t = ⊥, T_F = id_{SE(3)}.
- **Eindeutigkeit der Werkzeugkörper-Konstruktion**: Bei
  festgelegtem Parametertupel p_Bohrung und Bauteilkörper
  G_B^lokal ist der Werkzeugkörper K_Bohrung nach (4) eindeutig
  bestimmt:
  - Z_∞ nach (2) ist eindeutig als Niveaumenge der Funktion
    q ↦ ‖ (q − p_S) − ⟨q − p_S, â⟩ · â ‖.
  - H_+ nach (3) ist eindeutig als Halbraum durch p_S mit
    Normale â.
  - Σ nach (5a) bzw. (5b) ist eindeutig: bei α = SACKLOCH durch
    den Parameter t allein; bei α = DURCHGANG durch das
    Supremum (6), das für jedes beschränkte G_B^lokal und jeden
    festen Achsenstrahl wohlbestimmt ist.
- **Unabhängigkeit von der Wahl des typeigenen Bezugssystems**:
  Wird der Werkzeugkörper-Konstruktor in einem typeigenen
  Bezugssystem geführt (z. B. mit p_S = 0 und â = ê_z), und der
  Übergang in das Bauteil-Lokal-System über T_F ∈ SE(3)
  realisiert, ist das Ergebnis T_F( K_Bohrung^typ ) identisch
  zum direkt im Bauteil-Lokal-System konstruierten
  K_Bohrung(p_Bohrung), weil SE(3)-Transformationen Kreiszylinder
  auf Kreiszylinder gleicher Achsenrichtung und gleichen
  Durchmessers abbilden. Die Wahl ist Modellierungskonvention;
  semantisch invariant.
- **Wohldefiniertheit für α = DURCHGANG**: Das Supremum (6) ist
  nicht das blosse Supremum eines beliebigen Strahls, sondern
  beschränkt auf Eindringlängen, für die der Strahl noch innerhalb
  des Bauteilkörpers liegt. Für einen einfach zusammenhängenden,
  konvexen oder polyederförmigen G_B^lokal und einen p_S auf der
  Berandung mit â einwärts gerichtet ist (6) gleich der ersten
  positiven Lösung von p_S + λ · â ∈ ∂G_B^lokal. Für nicht-konvexe
  Bauteilkörper (etwa nach vorangegangenen Bearbeitungen) ist (6)
  trotzdem wohldefiniert: t_max ist die letzte Eindringlänge mit
  p_S + λ · â ∈ G_B^lokal, und die Boole'sche Differenz (7)
  arbeitet stabil auch über mehrfach durchstossene Bereiche
  hinweg.
- **Geometrische Nicht-Degeneriertheit (harte Invarianten,
  Validierungsfehler bei Verletzung)**:
  1. **Durchmesserpositivität**: d > ε_L. Eine Bohrung mit
     Durchmesser 0 ist keine Bohrung, sondern eine Anriss-Linie.
  2. **Einheitsvektor der Achse**: | ‖â‖² − 1 | ≤ ε_N. Eine Bohrung
     mit Null-Achse oder unnormierter Achse hat keinen
     wohldefinierten Werkzeugkörper.
  3. **Tiefenpositivität bei Sackloch**: α = SACKLOCH ⇒ t > ε_L.
     Eine Sackbohrung der Tiefe 0 ist keine Bohrung.
  4. **Tiefen-Marken-Konsistenz**: α = DURCHGANG ⇒ t = ⊥;
     α = SACKLOCH ⇒ t ∈ ℝ⁺. Die Marke α und der Tiefenwert t
     müssen miteinander konsistent sein.
  5. **Bauteilwirksamkeit**: K_Bohrung(p_Bohrung) ∩ G_B^lokal ≠ ∅
     mit messbarem Volumen > 0. Eine Bohrung, deren Werkzeugkörper
     das Bauteil nicht trifft, ist im Modell sinnleer; das
     Anhängen einer solchen Bohrung schlägt mit
     `BohrungAusserhalbBauteil` fehl (analog zu
     `KervePositionAusserhalbBauteil` in `hg_kerve.md`).
- **Reihenfolge-Unabhängigkeit bei Komposition**: Folgt aus
  `bearbeitung` Wohldefiniertheit (2) — die Vereinigung über
  Werkzeugkörper ist kommutativ und assoziativ; die Boole'sche
  Differenz einer Bohrung mit anderen Bearbeitungen am selben
  Bauteil ist von der Reihenfolge unabhängig.
- **Subtraktivität**: Strukturell garantiert durch (7); siehe
  `bearbeitung` Gl. (4).
- **Nicht-Zirkularität**: Die Definition stützt sich nur auf
  bereits definierte Begriffe (`bearbeitung`, `bauteil`,
  `lokales_koordinatensystem`, `punkt`, `vektor`, `polyeder`,
  `toleranzen`). Sie verweist auf `querschnitt` (Voraussetzung
  für die Querschnittsschwächungs-Plausibilität, weiche
  Invariante) nicht in der Definition selbst, sondern nur im
  Implementierungshinweis. Sie kommt nicht in ihrer eigenen
  Definition vor.
- **Plausibilität der Querschnittsschwächung** (weiche Invariante,
  nicht Bestandteil der Definition): Bohrungen reduzieren den
  Nettoquerschnitt nach EC5 5.2 / SIA 265 4.6. Die App warnt,
  wenn der Bohrungsdurchmesser d ein bauteilabhängiges
  Plausibilitäts-Verhältnis überschreitet (Faustregel-Default
  in der Bemessungsschicht; nicht im Glossar normativ
  festgelegt). Diese Prüfung ist **keine** Definitionsbedingung;
  eine grosse Bohrung bleibt eine Bohrung im Sinne dieses
  Glossars, sie ist bemessungstechnisch jedoch problematisch.

## Erläuterung (nicht normativ)

Die Bohrung ist der häufigste subtraktive Bauteil-Merkmaltyp im
Holzbau und gleichzeitig der mit der grössten konzeptuellen
Schärfungsbedürftigkeit: sie kann **eigenständige
Bauteilbearbeitung** sein (Lüftungsbohrung, Glued-in-Rod-
Sackbohrung, Elektroinstallations-Durchführung), oder sie kann
**Folgegeometrie eines Verbindungsmittels** sein
(Schraubenkanal, Bolzenloch, Stabdübel-Bohrung,
Nagel-Vorbohrung). Die App-Ontologie trennt die beiden Fälle
strukturell — siehe `hg_bearbeitung.md`, Erläuterungs-Abschnitt
'Vier Element-Subklassen vs. Bearbeitung':

- **Bohrung als Bearbeitung** (dieser Eintrag): eigenständige
  zylindrische Subtraktion an genau einem Bauteil; trägt eigene
  UUID; erscheint als Element in der Bearbeitungs-Liste des
  Bauteils.
- **Bohrung als Verbindungsmittel-Folgegeometrie** (nicht dieser
  Eintrag): das Bohrloch wird durch ein Verbindungsmittel
  (Schraube, Bolzen, Stabdübel, Nagel) verursacht; modelliert
  wird das Verbindungsmittel, nicht das Bohrloch. Die geometrische
  Bohrung ist eine abgeleitete Konsequenz und erscheint erst im
  BTLx-Export als `Drilling`-Processing an den durchbohrten
  Bauteilen.

**Funktion bestimmt die Klasse, nicht die Geometrie.** Eine
geometrisch identische zylindrische Subtraktion kann je nach
Funktion eine `Bearbeitung` mit `typ = Bohrung` sein oder eine
Folgegeometrie eines `Verbindungsmittels`.

### Tätigkeit vs. Resultat

Analog zu `hg_bearbeitung.md`: 'Bohrung' bezeichnet im
zimmermannssprachlichen Sprachgebrauch sowohl die **Tätigkeit**
(das Bohren, der Bohrvorgang) als auch das **Resultat** (das
zylindrische Loch im fertigen Bauteil). Dieser Glossareintrag
definiert ausschliesslich die **Resultatslesart**: das
geometrische Merkmal am bearbeiteten Bauteil. Die Tätigkeit
(Werkzeugwahl, Vorschub, Bohrgeschwindigkeit, CNC-Programmierung)
ist Gegenstand der Fertigungs-Schicht und nicht im Glossar
geführt.

### BTLx- und IFC-Übersetzung (Export-Schicht, Phase 4)

**BTLx 2.1** führt für zylindrische Materialabträge zwei
Processings; die Übersetzung erfolgt fallbezogen:

| App-Bohrung | BTLx-Processing | Trigger |
|---|---|---|
| Standardfall (kleiner bis mittlerer Durchmesser, beliebige Tiefe) | `Drilling` | immer, sofern Werkzeugklasse 'Holzbau-Spiralbohrer' |
| Grosse Sackbohrung (Werkzeugklasse Fräser) | `Pocket` mit kreisförmigem Profil | Durchmesser > Werkzeugschwelle; im Glossar dann eigener Subtyp `aussparung` (Folgearbeit) |

Die Parameter des `Drilling`-Processings (`StartX`, `StartY`,
`Angle`, `Inclination`, `DepthLimited`, `Depth`, `Diameter`)
ergeben sich aus dem Bohrungs-Tupel:

- `StartX`, `StartY`: Bauteil-Oberflächen-Koordinaten von p_S
  auf der `Drilling`-Referenz-Seite.
- `Angle`, `Inclination`: zwei Winkel, die â im
  Referenz-Seitensystem ausdrücken.
- `DepthLimited`: `true` für α = SACKLOCH, `false` für
  α = DURCHGANG.
- `Depth`: Tiefe t in mm, nur bei `DepthLimited = true` wirksam.
- `Diameter`: Nenndurchmesser d in mm.

**IFC 4.3** modelliert eine Bohrung als `IfcOpeningElement`
(Spezialisierung von `IfcFeatureElementSubtraction`) mit einem
`SweptSolid`-Body. Die Zylindrizität wird über die Representation
als `IfcExtrudedAreaSolid` mit `IfcCircleProfileDef` (Radius
r = d/2) als `SweptArea` ausgedrückt. Der frühere Subtyp
`IfcOpeningStandardCase` (IFC 4.0/4.1) ist in IFC 4.3 entfernt
— die buildingSMART-Empfehlung lautet, statt eines eigenen
Subtyps `IfcOpeningElement` direkt mit der entsprechenden
Body-Representation zu verwenden. Der `PredefinedType` aus dem
Enum `IfcOpeningElementTypeEnum` codiert die Tiefen-Erstreckung:

- α = DURCHGANG → `IfcOpeningElementTypeEnum.OPENING`.
- α = SACKLOCH → `IfcOpeningElementTypeEnum.RECESS`.

Die App-UUID der Bohrung wird zur `GlobalId` des
`IfcOpeningElement` (Base64-kodiert nach ISO/IEC 9834-8); die
Beziehung zum Bauteil läuft über `IfcRelVoidsElement` (siehe
`hg_bearbeitung.md`, Erläuterung 'BTLx- und IFC-Übersetzung').

### Verbindungsmittel-Pendant-Bohrungen (Vorbohrungs- und Passsitz-Regeln)

Die EC5-Regeln für Bohrlochdurchmesser an Verbindungsmitteln —
Stabdübel (Bohrloch = Nenndurchmesser, EC5 8.6), Passbolzen
(Bohrloch = Nenndurchmesser, EC5 8.5), gewöhnliche Bolzen
(Bohrloch ≤ d + 1 mm, EC5 8.5), Vorbohrung für Nägel (Bohrloch
≤ 0,8 · d nach Praxis, EC5 8.3.1.2), Vorbohrung für Schrauben
(typabhängig, EC5 8.7) — sind **nicht** im Bohrungs-Eintrag
verankert, weil die zugehörigen Bohrungen im Modell nicht als
eigenständige `Bohrung`-Instanzen geführt werden, sondern als
Folgegeometrie ihres Verbindungsmittels. Diese Regeln sind in
`hg_verbindungsmittel.md` und in der Bemessungsschicht zu
führen, nicht hier.

## Beziehungen

- **Oberbegriff**: `bearbeitung` (subtraktive Bauteilbearbeitung;
  generische Wirkung über Boole'sche Differenz, siehe
  `hg_bearbeitung.md` Gl. (1)).
- **Subtypen** (Folgearbeit, eigene Glossareinträge — keine
  Implementierung in Phase 2):
  - **Senkbohrung** (`senkbohrung`, Folgearbeit; Trigger: erste
    sichtbare Schraubverbindung mit Senkkopf): Komposition aus
    Zylinderbohrung und kegel- oder stufenförmiger Erweiterung
    am Eingang. Geometrisch keine reine Bohrung, daher eigener
    Subtyp unter `bearbeitung`.
- **Bestandteile (partitiv) einer Bohrung** (Parametertupel
  p_Bohrung):
  - **Startpunkt** p_S in Bauteil-Lokal-Koordinaten, Pflicht.
  - **Achseneinheitsvektor** â in Bauteil-Lokal-Koordinaten,
    Pflicht.
  - **Nenndurchmesser** d ∈ ℝ⁺, Pflicht (mm).
  - **Tiefenart** α ∈ {DURCHGANG, SACKLOCH}, Pflicht.
  - **Tiefe** t ∈ ℝ⁺ ∪ {⊥}, Pflicht-konsistent mit α (Wert bei
    SACKLOCH, ⊥ bei DURCHGANG).
  - **UUID, lokale Platzierung, Bezeichnung**: geerbt aus
    `bearbeitung`.
- **Verwendung**:
  - Element in der Bearbeitungs-Liste eines Bauteils (partitive
    Komposition, siehe `hg_bauteil.md` und `hg_bearbeitung.md`).
  - Mapping-Ziel im BTLx-Export (`Drilling`) und IFC-Export
    (`IfcOpeningElement` mit `SweptSolid`-Body).
- **Abgrenzung**:
  - **Bearbeitung** (`bearbeitung`): generischer Oberbegriff;
    eine Bohrung ist die kreiszylindrische Spezialisierung.
  - **Verbindungsmittel** (`verbindungsmittel`): überträgt Kräfte
    zwischen Bauteilen; die durch ein Verbindungsmittel
    verursachte zylindrische Subtraktion ist **keine eigene
    Bohrung im Modell**, sondern Folgegeometrie des
    Verbindungsmittels. Die App-Disambiguation 'Funktion bestimmt
    die Klasse, nicht die Geometrie' (siehe Erläuterung) zieht
    die Trennlinie.
  - **Kerve** (`kerve`): zweiflächiger dreieckiger Einschnitt mit
    welt-aligned Schnittflächen; Werkzeugkörper prismatisch, nicht
    zylindrisch. Eine Bohrung hat einen kreiszylindrischen
    Werkzeugkörper; eine Kerve einen prismatischen mit
    Dreiecksquerschnitt.
  - **Aussparung** (Forward-Verweis, Folgearbeit; Trigger: erste
    Bemessung einer Trägeröffnung nach EC5:2025 'Design of holes
    in beams'): grosse, im Bauteilmittelbereich gelegene Öffnung
    beliebiger Form (rechteckig, polygonal, kreisförmig). Eine
    Aussparung mit kreisförmigem Querschnitt unterscheidet sich
    von einer Bohrung durch die Werkzeugklasse (Fräser statt
    Spiralbohrer) und durch die Bemessungsregel (separate
    Reduktionsfaktoren nach EC5:2025); im BTLx-Export als
    `Pocket`, nicht als `Drilling`. Die Abgrenzungs-Schwelle
    Bohrung ↔ Aussparung ist nicht normativ festgelegt; sie ist
    werkzeugklassen- und werkzeugmaschinen-abhängig.
  - **Ausklinkung** (Forward-Verweis, Folgearbeit; Trigger:
    erste Träger-Endauflagerung nach EC5 6.5): quaderförmiger
    Ausschnitt am Bauteilende, dient als Auflagerausnehmung.
    Eine Ausklinkung ist nicht zylindrisch, hat keinen
    Achsen-Begriff und liegt definitorisch am Bauteilende, nicht
    im Mittelbereich; im BTLx mit eigenen Processings (`Lap`
    bzw. typabhängig).
  - **Schlitz** (`schlitz`, Folgearbeit; Trigger:
    Schlitzblech-Verbinder): längliche Subtraktion mit
    rechteckigem oder ovalem Querschnitt zur Aufnahme einer
    Lasche oder eines Schlitzblechs. Nicht kreiszylindrisch;
    BTLx-Pendant: `Slot`.
  - **Zapfenloch** (`zapfenloch`, Folgearbeit; Trigger:
    Stuhlsäulen-Pfetten-Anschluss): rechteckige Subtraktion zur
    Aufnahme eines Zapfens. Nicht kreiszylindrisch; BTLx-Pendant:
    `Mortise`.
  - **Senkbohrung** (`senkbohrung`, Folgearbeit): Komposition
    aus Zylinderbohrung und Senkung; im strengen Sinne keine
    reine Bohrung mehr (zwei Werkzeugkörper-Stufen).
  - **Vorbohrung** (`vorbohrung`, Folgearbeit, möglicherweise
    nur als Funktionsmerkmal am Verbindungsmittel und nicht als
    eigener Bearbeitungs-Subtyp): geometrisch eine Bohrung mit
    spezialisierter funktionaler Bedeutung (Spaltvermeidung,
    Führung) und Verbindungsmittel-bezogenem Durchmesser.
    Modellseitig nicht als eigenständige `Bohrung` geführt,
    sondern als Folgegeometrie des Verbindungsmittels.

## Implementierungshinweis

Datentyp (Domänen-Schicht, Kotlin, Schicht
`domain.bauteil.bearbeitung`):

```kotlin
package domain.bauteil.bearbeitung

import domain.geometrie.Einheitsvektor
import domain.geometrie.LokalePlatzierung
import domain.geometrie.Punkt
import java.util.UUID

/**
 * Bohrung — kreiszylindrische subtraktive Bearbeitung an einem
 * Bauteil. Sealed-Subtyp von [Bearbeitung].
 *
 * Glossar: hg_bohrung.md
 *
 * @property startpunkt Achsen-Startpunkt in Bauteil-Lokal-Koordinaten;
 *           Pflicht.
 * @property achse Achsen-Einheitsvektor in Bauteil-Lokal-Koordinaten;
 *           Pflicht (Invariante: |‖â‖² − 1| ≤ Toleranzen.NORM_EPS).
 * @property nenndurchmesser Bohrungsdurchmesser in mm; > Toleranzen.LAENGE_EPS.
 * @property tiefenart DURCHGANG oder SACKLOCH.
 * @property tiefe Tiefe in mm bei SACKLOCH; null bei DURCHGANG.
 *           Invariante: tiefenart == SACKLOCH ⇔ tiefe != null.
 */
data class Bohrung(
    override val uuid: UUID,
    override val lokalePlatzierung: LokalePlatzierung,
    override val bezeichnung: String?,
    val startpunkt: Punkt,
    val achse: Einheitsvektor,
    val nenndurchmesser: Double,
    val tiefenart: Tiefenart,
    val tiefe: Double?,
) : Bearbeitung {

    enum class Tiefenart { DURCHGANG, SACKLOCH }
}
```

- **Einheit**: Längen (Startpunkt-Koordinaten, Durchmesser,
  Tiefe) in mm (Double); Achsenvektor dimensionslos
  (Einheitsvektor).
- **Identität**: `uuid` ist Pflicht und persistent (RFC 9562 v7),
  unabhängig vom zugeordneten Bauteil (siehe `bearbeitung`).
- **Keine Backref auf das Bauteil**: konsistent mit
  `bearbeitung` — die Zuordnung läuft über die
  Container-Beziehung in der Bearbeitungs-Liste des Bauteils,
  nicht über ein Feld am Bohrungs-Objekt.
- **Pflicht- und Optionalfelder (normativ)**:
  - `uuid`, `lokalePlatzierung`, `startpunkt`, `achse`,
    `nenndurchmesser`, `tiefenart` — Pflicht.
  - `tiefe` — Pflicht-konsistent mit `tiefenart`: bei
    `DURCHGANG` muss `tiefe == null` sein; bei `SACKLOCH` muss
    `tiefe != null` und `tiefe > Toleranzen.LAENGE_EPS` sein.
  - `bezeichnung` — null zulässig.
- **Invarianten** (in Fabrikfunktion `Bohrung.erzeugen(...)` prüfen,
  bei Verletzung `Resultat.Fehler` mit subtypspezifischer
  Variante zurückgeben; niemals Exception werfen):
  1. `nenndurchmesser > Toleranzen.LAENGE_EPS`.
  2. `|‖achse.vektor‖² − 1| ≤ Toleranzen.NORM_EPS` (Einheitsvektor).
  3. `tiefenart == SACKLOCH ⇒ tiefe != null && tiefe > Toleranzen.LAENGE_EPS`.
  4. `tiefenart == DURCHGANG ⇒ tiefe == null`.
  5. Werkzeugkörper trifft Bauteilkörper mit messbarem Volumen
     (Validierungsfehler `BohrungAusserhalbBauteil` bei
     Verletzung; geprüft in `Bauteil.fuegeBearbeitungHinzu(...)`).
- **Berechnung des Werkzeugkörpers**:
  - `werkzeugkoerper(): Polyeder` — Approximation des
    Kreiszylinders durch reguläres N-Eck-Prisma; N je nach
    Visualisierungs-Genauigkeit (Default N = 32 für die
    Domänen-Schicht-Berechnung der Boole'schen Differenz; N kann
    in der Visualisierungs-Schicht höher gewählt werden für
    Rendering). Die Wahl von N ist Modellierungs-Konvention der
    Geometrie-Schicht, nicht Bestandteil der Definition.
  - Für α = DURCHGANG wird der Werkzeugkörper als endlicher
    Zylinder über die Eindringlänge t_max nach (6) berechnet,
    eventuell mit kleinem Überstand (≥ Toleranzen.LAENGE_EPS),
    um Tangenten-Artefakte an der Bauteilberandung zu vermeiden.
- **BTLx-Export** (Persistenzschicht, Phase 4):
  - Mapping auf `Drilling`-Processing am betroffenen Bauteil-Part.
  - Parameter-Übersetzung gemäss Erläuterung 'BTLx- und IFC-
    Übersetzung'.
- **IFC-Export** (Persistenzschicht, Phase 4):
  - Mapping auf `IfcOpeningElement` mit `SweptSolid`-Body
    (`IfcExtrudedAreaSolid` / `IfcCircleProfileDef` als
    Representation), `PredefinedType` aus
    `IfcOpeningElementTypeEnum` gemäss `tiefenart`.
- **Edge Cases**:
  - **Bohrung mit Achse parallel zur Bauteiloberfläche** (â
    tangential zur Berandung in p_S): geometrisch möglich, im
    Modell aber sinnleer, weil die Boole'sche Differenz den
    Werkzeugkörper sofort wieder verlässt; durch die
    Bauteilwirksamkeits-Invariante (5) ausgeschlossen.
  - **Bohrung mit Startpunkt vollständig innerhalb des
    Bauteils** (p_S ∈ int(G_B^lokal)): zulässig (etwa für
    eingeleimte Gewindestangen, deren Achse nicht an einer
    Oberfläche beginnt); der Werkzeugkörper schliesst dann auch
    den Anfangs-Halbzylinder ein, der innerhalb des Bauteils
    liegt.
  - **Durchgangsbohrung in ein nicht-konvexes Bauteil** (etwa
    nach vorangegangener Kerve): t_max nach (6) ist trotzdem
    wohldefiniert; die Boole'sche Differenz arbeitet stabil
    auch über durchquerte Hohlräume hinweg.
  - **Bohrung in einen isotropen Plattenwerkstoff** (Spanplatte,
    OSB): zulässig; die Faserrichtungs-Plausibilitäts-Warnung
    aus der Bemessungsschicht greift nicht.
  - **Bohrung an einem Plattenwerkstoff mit Plattendicken-
    Achse** (CLT, BSP): die Achse â kann in Plattendicken-
    Richtung (rechtwinklig zur Plattenebene) oder in
    Plattenebene liegen; beide Fälle sind geometrisch zulässig
    und für unterschiedliche Anwendungen typisch (Bohrung
    rechtwinklig zur Plattenebene für Verbindungsmittel-
    Vorbereitung; Bohrung in Plattenebene für Glued-in-Rod-
    Anschlüsse).
- **Abgeleitete Eigenschaften** (als Funktionen, keine Felder;
  Implementierung in Geometrie-Schicht und Bemessungs-Schicht):
  - `werkzeugkoerper(): Polyeder` — K_Bohrung nach (4) im
    Bauteil-Lokal-System.
  - `effektiveTiefe(b: Bauteil): Double` — t bei SACKLOCH;
    t_max(p_S, â, G_B^lokal) bei DURCHGANG (Geometrie-Schicht).
  - `querschnittsschwaechung(b: Bauteil, s: Double): Double` —
    Anteil der bei Längsparameter s entfernten Querschnittsfläche
    (Bemessungs-Schicht, EC5 5.2).
- **Bezeichner-Konvention**: Domänen-Klasse heisst `Bohrung`
  (deutsch, Glossarbegriff); das innere Enum heisst `Tiefenart`
  mit Werten `DURCHGANG` und `SACKLOCH` (deutsch).

## Quellen

**Primär (normativ):**

- DIN EN 1995-1-1:2010-12, „Eurocode 5: Bemessung und Konstruktion
  von Holzbauten – Teil 1-1", Abschnitt 5.2 (Querschnittsschwächung),
  Abschnitt 8.3.1.2 (Nägel, Vorbohrpflicht), Abschnitt 8.5
  (Bolzen, Bohrlochtoleranzen), Abschnitt 8.6 (Stabdübel,
  Passsitz), Abschnitt 8.7 (Schrauben, Vorbohrpflicht).
- SIA 265:2021, „Holzbau", Schweizerischer Ingenieur- und
  Architektenverein, Zürich, Abschnitt 4.6 (Querschnittswerte)
  und Anhang A (Verbindungsmittel).
- ISO 16739-1:2024, „Industry Foundation Classes (IFC) for data
  sharing in the construction and facility management industries
  — Part 1: Data schema" (IFC 4.3.2): `IfcOpeningElement`,
  `IfcOpeningElementTypeEnum`, `IfcExtrudedAreaSolid`,
  `IfcCircleProfileDef`, `IfcRelVoidsElement`. Der frühere
  Subtyp `IfcOpeningStandardCase` (IFC 4.0/4.1) ist in IFC 4.3
  entfernt.
- design2machine: *BTLx interface description*, Version 2.1,
  16.11.2023, Abschnitte `Drilling` und `Pocket`.

**Sekundär:**

- Mönck, W.; Rug, W.: *Holzbau – Bemessung und Konstruktion.*
  16. Auflage, Beuth, Berlin 2015, Kap. 7.
- Blass, H. J.; Sandhaas, C.: *Ingenieurholzbau – Grundlagen der
  Bemessung.* KIT Scientific Publishing, Karlsruhe 2016, Kap. 8.
- Holzbau-Handbuch, Reihe 2 *Tragwerksplanung*, Teil 1
  *Verbindungen*, Folge 1 *Verbindungen mit stiftförmigen
  Verbindungsmitteln*, Informationsdienst Holz, aktuelle Auflage.
- ETA-11/0190, „Würth ASSY plus VG, ASSY 3.0, ASSY 4.0".
- Z-9.1-519, „Schrauben mit Vollgewinde als Verbindungsmittel
  und als Verstärkung von Holzbauteilen" (SPAX, DIBt).

**Korpus (nicht autoritativ):**

- Recherche-Bericht `docs/recherche/2026-05-14_hg_bohrung.md`
  (Bestand-Verortung, Typologie, IFC/BTLx-Mapping, Quellen-Tier-
  Bewertung).
- Wikipedia, Lemmata „Bohrung", „Durchgangsbohrung", „Sackloch"
  (abgerufen 2026-05-14).
- cadwork informatik: Dokumentation „Bearbeitung am Bauteil"
  (Bohrungs-Typen Holz-Spiralbohrer, Forstner, Schlangenbohrer).
