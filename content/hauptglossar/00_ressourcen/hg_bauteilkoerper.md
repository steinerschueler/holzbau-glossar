---
id: bauteilkoerper
benennung: Bauteilkörper
kurz: "Der Bauteilkörper ist die vollständige räumliche Form eines Bauteils, so wie es nach allen Sägeschnitten und Ausklinkungen tatsächlich an seinem Platz im Bauwerk dasteht — mit all seinen Ecken, Kanten und Flächen."
synonyme: ["Bauteil-Volumen", "Bauteilgeometrie (Volumenanteil)", "Volumenkörper eines Bauteils", "Body", "Solid"]
abgelehnte_benennungen: [Körper, Rohkörper, Rohling, Bauteilform, Stabkörper, Holzkörper, "Bauteil-Solid", Volumenkörper, "body representation", "solid model"]
oberbegriff: polyeder
begriffstyp: merkmal
voraussetzungen: [polyeder, bauteil, uuid, weltkoordinatensystem, lage, toleranzen]
abgrenzung_zu: [bauteil, polyeder, bauteilachse, querschnitt, lage, bauteilgeometrie, volumenkoerper, ifc_shape_representation]
status: entwurf
subglossar_pendant: optional
quellen_primär:
  - "ISO 16739-1:2024, 'Industry Foundation Classes (IFC) for data sharing in the construction and facility management industries — Part 1: Data schema' (IFC 4.3.2), Entität `IfcSolidModel` (abstrakter Supertyp aller 3D-Volumen-Repräsentationen, Subtyp von `IfcGeometricRepresentationItem`) mit Subtypen `IfcManifoldSolidBrep`, `IfcCsgSolid`, `IfcSweptAreaSolid` (`IfcExtrudedAreaSolid`, `IfcRevolvedAreaSolid`, `IfcFixedReferenceSweptAreaSolid`), `IfcSweptDiskSolid`, `IfcSectionedSolid`; Entität `IfcShapeRepresentation` mit Attribut `RepresentationIdentifier = 'Body'` als normative Klassifikation der 3D-Körper-Sicht eines Produkts; Trennung von `IfcElement` (ontologisch, mit `GlobalId`) und der über `IfcProductDefinitionShape` getragenen Body-Repräsentation. [einsicht: snippet]"
  - "ISO 19107:2019 'Geographic information – Spatial schema', Abschnitt 6.4 'GM_Solid' (volumetrisches Geometrieobjekt mit polygonal berandeter Hülle, B-Rep-Modell) als allgemeine Spezifikation eines orientierten, mannigfaltigen 3D-Körpers."
  - "DIN EN ISO 10303-42, 'Industrieautomation – Produktmodelldaten – Teil 42: Geometrische und topologische Repräsentation' (B-Rep-Modell für volumetrische Festkörper)."
quellen_sekundär:
  - "baulexikon.brz.eu, Lemma 'Volumenkörper': räumlich geschlossener 3D-Körper zur Darstellung von Bauteilen in CAD- und BIM-Modellen, Basis für Mengen und Kollisionserkennung."
  - "Hoffmann, C. M.: Geometric and Solid Modeling – An Introduction. Morgan Kaufmann, San Mateo 1989, Kap. 3 (B-Rep) und Kap. 4 (CSG)."
  - "Mäntylä, M.: An Introduction to Solid Modeling. Computer Science Press, Rockville 1988, Kap. 6 (Boundary Representation)."
  - "Recherche zum Begriff im DACH-Holzbau-Korpus: [intern] (Stand 2026-05-14)."
quellenkonflikt: |
  **Wichtige Markierung — der Begriff ist im DACH-Holzbau-Korpus nicht
  etabliert.** Weder die einschlägigen Holzbau-Normen (SIA 265:2021,
  DIN EN 1995-1-1:2010-12, DIN 1052:2008-12, DIN EN 14080:2013-09,
  DIN EN 14081-1:2019-10) noch die Standard-Lehrbuchliteratur
  (Mönck/Rug, Blass/Sandhaas, Natterer/Herzog/Volz) noch die
  öffentlich zugängliche CAD-Hersteller-Dokumentation (Cadwork,
  Dietrich's, SEMA) führen „Bauteilkörper" als technischen Terminus.
  Die Holzbau-Sprache modelliert Bauteile geometrisch implizit über
  Achse + Querschnitt bzw. Trägerfläche + Dicke und macht keine
  begriffliche Achse „Bauteil ontologisch ↔ Bauteilkörper
  geometrisch" auf. Vollständige Quellenlage und Negativ-Befunde:
  [intern].

  Der Eintrag ist damit **App-getragen und IFC-verankert**, nicht
  Holzbau-Standard. Das einzige normativ tragende Schema, das die
  Trennung explizit führt, ist ISO 16739-1 (IFC 4.3.2):
  `IfcElement` (semantisch, mit `GlobalId`, Material, Klassifikation)
  ↔ `IfcShapeRepresentation` mit `RepresentationIdentifier = 'Body'`
  und `IfcSolidModel`-Items (geometrisch). Im DACH-Sprachraum bleibt
  „Volumenkörper" der gängige Allgemein-Term und „Solid" der
  Anglizismus aus dem CAD-Umfeld; beide sind hier als Synonyme
  geführt, aber zu allgemein, um die spezifische
  Bauteil-Volumenrolle zu benennen.

  Dieselbe Verfahrensweise ist bereits bei `hg_bausystem.md`
  angewandt, das ebenfalls primär IFC-getragen ist (dort
  `IfcBuildingSystem`).

  **Lesart-Entscheidung dieses Eintrags: α (Volumen-Rolle).** Der
  Bauteilkörper ist hier die geometrische **Volumen-Repräsentation**
  eines Bauteils, also die Rolle eines Polyeders als 𝒢_volumen-Anteil
  einer konkreten Bauteilinstanz. Diese Lesart wurde der alternativ
  möglichen Sammel-Lesart β (über 𝒢_stab ∪ 𝒢_flaeche ∪ 𝒢_volumen)
  vorgezogen, aus drei Gründen:

  1. Konsistenz mit dem bereits bestehenden Glossar: `hg_polyeder.md`
     kündigt „bauteilkoerper" ausdrücklich als „Polyeder in der Rolle
     ‚Volumen eines konkreten Bauteils im Welt-Koordinatensystem'" an.
  2. Konsistenz mit der Domänen-Schicht: die Sammel-Lesart β über
     alle drei Geometrievarianten ist im Code bereits als
     `Bauteilgeometrie` (sealed-Hierarchie `Stab | Flaeche | Volumen`)
     realisiert; ein zweiter Sammelbegriff im Hauptglossar wäre
     Redundanz.
  3. IFC-Anker: das engste IFC-Pendant der gemeinten Idee ist
     `IfcSolidModel`, das per Schema-Definition nur die 3D-Volumen-
     Sicht abdeckt; eine Achse (`IfcCurve` in der `Axis`-Repräsentation)
     ist kein `IfcSolidModel`. Die normative IFC-Verankerung trägt
     also genau α, nicht β.

  Stabbauteile (𝒢_stab) und Flächenbauteile (𝒢_flaeche) haben in
  dieser Lesart **keinen Bauteilkörper im engen Sinn**; ihre
  Geometrie wird über `bauteilachse` + `querschnitt` bzw.
  Trägerfläche + Dicke geführt. Erst die volumetrische Auffüllung
  zu einer Punktmenge in ℝ³ — beim Stabbauteil das Sweep-Volumen
  des Querschnitts entlang der Achse, beim Flächenbauteil die
  Aufdickung der Trägerfläche — ergibt einen Bauteilkörper im
  Sinne dieses Eintrags. Volumenbauteile (𝒢_volumen) tragen ihren
  Bauteilkörper unmittelbar.

  „Rohkörper" (Dietrich's) wird als abgelehnte Benennung geführt,
  weil der Begriff in der CAD-Hersteller-Sprache eine **andere**
  Bedeutung trägt (Roh-Block vor Bearbeitungen, vergleichbar mit
  Cadwork „Rohling"). Der Bauteilkörper im Sinne dieses Eintrags
  ist der **bearbeitete** Endzustand, nicht das Ausgangs-
  Halbzeug. Diese Verwechslungsgefahr ist im DACH-Holzbau real und
  rechtfertigt die ausdrückliche Ablehnung.
---

## Prosa-Definition

Ein **Bauteilkörper** ist die geometrische 3D-Volumen-Repräsentation
eines Bauteils, gegeben als das im Weltkoordinatensystem platzierte
Polyeder, das die räumliche Punktmenge des Bauteils nach Anwendung
aller seiner Bearbeitungen umfasst.

## Mathematische Definition

Sei

- W das Weltkoordinatensystem (siehe `weltkoordinatensystem`),
- B ein Bauteil im Sinne von `bauteil` mit Lage `B.lage` ∈ SE(3) und
  Geometrie `B.geometrie` ∈ 𝒢 = 𝒢_stab ∪ 𝒢_flaeche ∪ 𝒢_volumen,
- 𝒰 der UUID-Raum nach `uuid`,
- 𝒫 die Menge aller Polyeder im Sinne von `polyeder`.

Die **Volumen-Auffüllung** ord: 𝒢 → 𝒫 ordnet jeder Geometrie-
Repräsentation ihr Polyeder im lokalen Bauteil-Koordinatensystem zu:

- für (achse, querschnitt) ∈ 𝒢_stab: das prismatische bzw. allgemein
  gesweepte Polyeder, das durch Translation des Querschnittspolygons
  entlang der Bauteilachse entsteht;
- für (traegerflaeche, dicke) ∈ 𝒢_flaeche: das prismatische Polyeder,
  das durch Translation des Trägerflächenpolygons entlang der
  Trägerflächen-Normalen über die Dicke entsteht;
- für p ∈ 𝒢_volumen: das Polyeder p selbst.

Dann ist der **Bauteilkörper** des Bauteils B das Tupel

```
K(B):= (uuid_B, P_W),
```

mit

- **uuid_B**:= B.uuid ∈ 𝒰: die UUID des Trägerbauteils (keine eigene
  Identität; der Bauteilkörper trägt die Identität seines Bauteils),
- **P_W** ∈ 𝒫: das Polyeder, dessen Eckpunkte aus den lokalen
  Eckpunkten von ord(B.geometrie) durch die SE(3)-Transformation
  B.lage in W überführt sind:

  ```
  P_W:= lage_anwenden(B.lage, ord(B.geometrie)),
  ```

  wobei `lage_anwenden` jeden Eckpunkt v_lokal ∈ ℝ³ des lokalen
  Polyeders auf den Eckpunkt v_W:= B.lage(v_lokal) im
  Weltkoordinatensystem abbildet und die Inzidenzstruktur (Kanten,
  Flächen, Außennormalen) topologisch erhält.

Die Punktmenge des Bauteilkörpers in W ist

```
|K(B)|:= |P_W| ⊂ ℝ³.
```

Sie ist nach Konstruktion identisch zur Bauteil-Punktmenge G_W(B)
aus `hg_bauteil.md` und nach Voraussetzung von `polyeder`
beschränkt, abgeschlossen, regulär und durch eine endliche
Vereinigung ebener Polygone berandet.

## Wohldefiniertheit

- **Existenz**: Für jedes Bauteil B mit gültiger Geometrie
  (Stabachse mit Länge > LAENGE_EPS und Querschnittsfläche
  > FLAECHE_EPS; bzw. Trägerflächeninhalt > FLAECHE_EPS und Dicke
  > LAENGE_EPS; bzw. Volumen-Polyeder nach `polyeder`-Invarianten)
  liefert die Volumen-Auffüllung ord(B.geometrie) ein regulär
  begrenztes Polyeder; die Anwendung der SE(3)-Lage erhält
  Regularität und Beschränktheit, daher ist K(B) wohldefiniert.

- **Eindeutigkeit der Identität**: Der Bauteilkörper trägt keine
  eigene UUID; seine Identität ist B.uuid des Trägerbauteils.
  Damit gilt: ∀ B₁, B₂: (B₁ ≠ B₂) ⇒ (K(B₁) ≠ K(B₂)), und es gibt
  keine zwei Bauteilkörper an demselben Bauteil. Diese Festlegung
  spiegelt die IFC-Architektur: `IfcSolidModel` als
  Repräsentations-Item trägt keine `GlobalId`; sie sitzt am
  `IfcElement`.

- **Unabhängigkeit von der Wahl des lokalen Bauteil-Koordinaten-
  systems**: Für jede zulässige Wahl des lokalen Systems liefert
  die zugehörige Lage SE(3)-Transformation dieselbe Punktmenge
  |K(B)| ⊂ ℝ³. Die kombinatorische Struktur des Polyeders
  (V, E, F mit Inzidenz) ist invariant unter Starrkörper-
  Transformation; nur die Koordinatentupel der Eckpunkte ändern
  sich.

- **Konsistenz mit `hg_bauteil.md`**: |K(B)| = G_W(B) für jedes
  Bauteil B. Beide Punktmengen sind durch dieselbe Konstruktion
  (Anwendung der Lage auf die lokale Geometrie) definiert; der
  Bauteilkörper ist die Polyeder-Repräsentation dieser Punktmenge.

- **Triviale Sweep-Wohlgeformtheit**: Bei Stab- und Flächen-
  Geometrien ist die Volumen-Auffüllung ord ein Sweep eines
  Polygons entlang einer Strecke (bzw. eines konstanten Vektors)
  und liefert per Konstruktion ein regulär berandetes, einfach
  zusammenhängendes Polyeder; bei Volumen-Geometrien ist
  ord die Identität, und die Wohlgeformtheit folgt direkt aus
  `polyeder`. Die Wohldefiniertheit ist damit für alle drei
  Geometrie-Varianten erfüllt.

- **Nicht-Zirkularität**: Die Definition stützt sich auf
  `polyeder`, `bauteil`, `uuid`, `weltkoordinatensystem`, `lage`
  und `toleranzen`. Sie kommt nicht in ihrer eigenen Definition
  vor; insbesondere referenziert sie `bauteil` als Trägerbegriff
  und `polyeder` als geometrischen Oberbegriff, beide ohne
  Rückbezug auf `bauteilkoerper`. Die Spezifikation des
  Bauteilbegriffs setzt zwar eine Geometrie voraus, aber nicht
  diesen Eintrag — der Bauteilkörper ist eine **abgeleitete
  Sicht** auf den bereits definierten Bauteil-Geometrie-Anteil,
  keine konstitutive Komponente des Bauteils.

- **Begriffstyp `merkmal` (gewählt)**: Der Bauteilkörper ist eine
  **Sicht** an einem Bauteil mit eigenem Wert (Polyeder in W),
  aber ohne eigene Identität und ohne eigene Subtyp-Hierarchie.
  Strukturell ist er ein abgeleiteter Wert eines Bauteils, nicht
  ein eigenständiges Domänenobjekt. Das entspricht der
  IFC-Schema-Lage: `IfcSolidModel`-Items sind keine `IfcRoot`-
  Subtypen und tragen keine eigene `GlobalId`.

## Erläuterung (nicht normativ)

### Hinweis zur Theorie-Pflicht

`subglossar_pendant: optional` (Abweichung vom Normalfall `notwendig`,
`HG_KONVENTIONEN.md` §7) ist hier **bewusst** gewählt: der Bauteilkörper
ist eine abgeleitete Sicht eines Bauteils ohne eigenständige didaktische
Substanz — der zugehörige Stufen-Inhalt wird über `bauteil` und
`polyeder` bereits abgedeckt; eine eigene Subglossar-Reihe fügt
keinen Lehrwert hinzu.

### Begriffstyp-Asymmetrie zum Oberbegriff

`begriffstyp: merkmal` mit `oberbegriff: polyeder` (selbst `generisch`)
ist eine **bewusst gewählte** Asymmetrie nach `HG_KONVENTIONEN.md` §3:
eine Spezialisierung darf als `merkmal` klassifiziert sein, wenn sie
keine eigene Identität und keine eigene Subtyp-Hierarchie trägt —
hier eine Sicht/Wert am Bauteil ohne `GlobalId`-Pendant in IFC.

Der Bauteilkörper-Begriff ist der **App-interne Name für die
3D-Körper-Sicht eines Bauteils**. Er ist nicht in der DACH-Holzbau-
Berufssprache verankert (siehe `quellenkonflikt:`), sondern wird
hier als geometrischer Hilfsbegriff geführt, der drei Funktionen
trägt:

- **Render-Adresse**: Die Visualisierungs-Schicht benötigt ein
  adressierbares 3D-Geometrieobjekt, das sie an Filament als Mesh
  übergeben kann. Dieses Objekt ist genau der Bauteilkörper:
  Polyeder im Welt-Koordinatensystem, mit Eckpunkten in mm, Außen-
  normalen je Fläche, und Rückverweis auf die Bauteil-UUID für
  Picking und Selektion.
- **IFC-Export-Adresse**: Beim Export nach IFC 4.3 ist der
  Bauteilkörper das Pendant der `IfcShapeRepresentation` mit
  `RepresentationIdentifier = 'Body'` und einem `IfcSolidModel`-
  Item (typisch `IfcExtrudedAreaSolid` bei prismatischen
  Stabbauteilen, `IfcManifoldSolidBrep` oder `IfcCsgSolid` nach
  Bearbeitungen).
- **Mengen- und Kollisions-Adresse**: Volumen-, Oberflächen- und
  Hüllquader-Berechnungen (für Materiallisten, Eigengewicht,
  Kollisionserkennung) operieren auf dem Bauteilkörper, nicht auf
  dem abstrakten Bauteil-Tupel.

**Abgrenzung „Bauteilkörper" vs. „Rohkörper" / „Rohling".** In der
CAD-Hersteller-Sprache bezeichnet „Rohkörper" (Dietrich's) bzw.
„Rohling" (Cadwork) den **kleinsten umschreibenden rechteckigen
Block des Bauteils vor Bearbeitungen** — das Ausgangs-Halbzeug,
aus dem durch Verschneiden mit Bearbeitungs-Polyedern die fertige
Geometrie entsteht. Der Bauteilkörper im Sinne dieses Eintrags
ist demgegenüber der **bearbeitete Endzustand**: das Polyeder,
das nach Anwendung aller Kerven, Versätze, Zapfen, Blattungen
übrig bleibt. Wer „Rohling" oder „Rohkörper" meint, soll diese
Hersteller-Begriffe verwenden; sie sind hier nicht synonym geführt.

**Abgrenzung „Bauteilkörper" vs. „Bauteilgeometrie".** Die
Bauteilgeometrie umfasst nach `hg_bauteil.md` alle drei
Geometrie-Varianten 𝒢_stab, 𝒢_flaeche, 𝒢_volumen und ist die
Sealed-Wurzel der App-Code-Klasse `Bauteilgeometrie`. Der
Bauteilkörper ist demgegenüber die spezifische **3D-Volumen-
Repräsentation** eines Bauteils — der Polyeder, der bei Stab-
und Flächenbauteilen erst durch Sweep der Achs- bzw. Flächen-
Geometrie entsteht. „Bauteilgeometrie" steht eine Ebene
abstrakter; „Bauteilkörper" ist die abgeleitete Volumen-Sicht
auf ein konkretes Bauteil.

**Abgrenzung zum allgemeinen „Volumenkörper".** „Volumenkörper"
ist nach baulexikon.brz.eu ein räumlich geschlossener 3D-Körper
ohne Bauteil-Bezug. Der Bauteilkörper ist ein Volumenkörper
**in der Rolle eines bestimmten Bauteils**, mit Rückverweis auf
dessen UUID. Ein freistehender Volumenkörper ohne Bauteil ist
geometrisch wohlgeformt, aber kein Bauteilkörper.

**Stab- und Flächenbauteile haben einen Bauteilkörper.** Trotz
der α-Lesart (Volumen-Rolle) bleibt jedes Bauteil bauteilkörper-
fähig: die Volumen-Auffüllung ord liefert auch für 𝒢_stab und
𝒢_flaeche ein Polyeder. Was diese Lesart **ausschließt**, ist die
Identifikation des Bauteilkörpers mit der abstrakten Achs- bzw.
Trägerflächen-Sicht; jene sind eine Geometrie-Repräsentation,
aber kein Bauteilkörper. Die Achse als solche (`bauteilachse`)
ist 1D und füllt kein Volumen; sie wird erst über den
Querschnitt-Sweep zu einem Bauteilkörper.

## Beziehungen

- **Oberbegriff**: `polyeder` — der Bauteilkörper ist ein Polyeder
  in einer bestimmten Rolle (Volumen eines konkreten Bauteils im
  Welt-Koordinatensystem, mit Rückverweis auf die Bauteil-UUID).
  Alle geometrischen Operationen, die auf Polyedern definiert
  sind (Volumen, Oberfläche, Schwerpunkt, AABB, Boolesche
  Operationen), sind direkt auf den Bauteilkörper anwendbar.

- **Träger**: `bauteil` — jeder Bauteilkörper gehört zu genau
  einem Bauteil und trägt dessen UUID. Bauteilkörper ohne
  Trägerbauteil existieren nicht.

- **Bestandteile** (geerbt von `polyeder`):
  - **Eckpunkte** (in W, in mm),
  - **Kanten** (Strecken zwischen Eckpunkten),
  - **Begrenzungsflächen** (planare Polygone mit Außennormalen),
  - **Inneres** (Volumenmenge).

- **Spezialisierungen / Rollen** (Folgearbeit, nicht in diesem
  Eintrag):
  - Bauteilkörper eines Stabbauteils (Sweep-Prisma vor
    Bearbeitungen, allgemeines Polyeder nach Bearbeitungen),
  - Bauteilkörper eines Flächenbauteils (Aufdickungs-Prisma der
    Trägerfläche),
  - Bauteilkörper eines Volumenbauteils (Polyeder direkt).
  Eigene Glossar-Einträge sind nicht vorgesehen, solange die
  drei Fälle nur Konstruktions-Vorschriften unterscheiden, aber
  keine eigene Begriffs-Substanz tragen.

- **Abgrenzung**:
  - **Bauteil** (`bauteil`): das Trägerobjekt mit eigener
    Identität, Werkstoff, Faserrichtungs-Modi und Bemessungs-
    Eigenschaften; der Bauteilkörper ist eine **Sicht** an ihm,
    nicht das Bauteil selbst. Ein Bauteil hat genau einen
    Bauteilkörper; ein Bauteilkörper hat genau ein Bauteil.
  - **Polyeder** (`polyeder`): allgemeiner geometrischer
    Oberbegriff ohne Bauteil-Bindung. Jeder Bauteilkörper ist ein
    Polyeder, aber nicht jedes Polyeder ist ein Bauteilkörper
    (es kann Hilfsgeometrien, Schnitt-Polyeder, Verbindungs-
    Polyeder geben, die zu keinem Bauteil gehören).
  - **Bauteilachse** (`bauteilachse`): die 1D-Hauptachse
    stabförmiger Bauteile. Sie ist eine Achse, kein Volumen, und
    damit kein Bauteilkörper. Erst durch Sweep des Querschnitts
    entlang der Bauteilachse entsteht ein Bauteilkörper.
  - **Querschnitt** (`querschnitt`): die 2D-Schnittfigur eines
    Stabbauteils in einer Ebene rechtwinklig zur Bauteilachse.
    Ein Querschnitt ist 2D-beschränkt, der Bauteilkörper
    3D-beschränkt; der Querschnitt ist eine Bestandteil-Sicht,
    aus der zusammen mit der Bauteilachse der Bauteilkörper
    konstruiert wird.
  - **Lage** (`lage`): die SE(3)-Starrkörpertransformation, die
    das lokale Bauteil-Koordinatensystem nach W überführt. Die
    Lage ist Teil der Konstruktion des Bauteilkörpers (sie wird
    auf das lokale Polyeder angewandt), aber nicht selbst der
    Bauteilkörper.
  - **Bauteilgeometrie** (Sealed-Wurzel `Bauteilgeometrie` im
    Code; kein eigener Glossareintrag): die App-interne
    Sammelklasse über alle drei Geometrievarianten
    (`Stab | Flaeche | Volumen`). Sie ist eine Ebene abstrakter
    als der Bauteilkörper und enthält auch die nicht-volumetrischen
    Repräsentationen; der Bauteilkörper ist die abgeleitete
    Volumen-Sicht.
  - **Volumenkörper** (allgemein-bautechnischer Term, kein eigener
    Glossareintrag): räumlich geschlossener 3D-Körper im Sinne
    von baulexikon.brz.eu, ohne Bauteil-Bindung. Der Bauteilkörper
    ist ein Volumenkörper in der Rolle eines Bauteils.
  - **`IfcShapeRepresentation`** (IFC-Schema, kein eigener
    Glossareintrag): die IFC-Klammer um mehrere geometrische
    Repräsentations-Items einer Sicht (`Axis`, `Body`, `Box`,
    `Profile`). Der Bauteilkörper korrespondiert zur
    `IfcShapeRepresentation` mit `RepresentationIdentifier
    = 'Body'`, nicht zur `IfcShapeRepresentation` insgesamt.

## Quellen

**Primär (normativ):**

- ISO 16739-1:2024, „Industry Foundation Classes (IFC) for data
  sharing in the construction and facility management industries
  – Part 1: Data schema" (IFC 4.3.2), Entitäten `IfcSolidModel`,
  `IfcShapeRepresentation` (mit `RepresentationIdentifier`),
  `IfcGeometricRepresentationItem`, sowie die Subtyp-Hierarchie
  unter `IfcSolidModel` (`IfcManifoldSolidBrep`, `IfcCsgSolid`,
  `IfcSweptAreaSolid`, `IfcSweptDiskSolid`, `IfcSectionedSolid`).
- ISO 19107:2019, „Geographic information – Spatial schema",
  Abschnitt 6.4 (`GM_Solid`).
- DIN EN ISO 10303-42, „Industrieautomation – Produktmodelldaten
  – Teil 42: Geometrische und topologische Repräsentation".

**Sekundär:**

- Hoffmann, C. M.: *Geometric and Solid Modeling – An Introduction.*
  Morgan Kaufmann, San Mateo 1989.
- Mäntylä, M.: *An Introduction to Solid Modeling.* Computer
  Science Press, Rockville 1988.
- baulexikon.brz.eu, Lemma „Volumenkörper" (abgerufen 2026-05-14).

**Korpus (nicht autoritativ):**

- Cadwork-Knowledge-Base (Bauteil als Volumen, Rohling-Mechanik):
  `kb.cadwork.ch`, `de.cadwork.swiss/knowledgebase`.
- Dietrich's-Dokumentation („Volumeninfo", „Rohkörper" als
  Roh-Block vor Bearbeitungen): `docs.dietrichs.com` —
  **andere Bedeutung als der Bauteilkörper dieses Eintrags**;
  siehe Erläuterung.
- design2machine, BTLx 2.x Spezifikation (`design2machine.com/
  btlx/`): Part-Element mit Width/Height/Length/Reference-Sides;
  kein direktes Pendant zum Bauteilkörper-Begriff.
- Wikipedia, Lemmata „Volumenmodell", „CAD",
  „Industry Foundation Classes" (abgerufen 2026-05-14).
- Recherche-Bericht zur Begriffslage:
  [intern].
