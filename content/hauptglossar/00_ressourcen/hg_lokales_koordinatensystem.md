---
id: lokales_koordinatensystem
benennung: Lokales Koordinatensystem
synonyme: ["Bauteilkoordinatensystem", "Bauteil-Lokal", "lokales Bezugssystem", "Lokal-CRS", "Bauteilframe"]
abgelehnte_benennungen: [Lokalsystem, Bauteilachsensystem, "local coordinate system", "local frame", "object frame", "body frame", LCS]
oberbegriff: koordinatensystem
begriffstyp: hilfsbegriff
voraussetzungen: [koordinatensystem, punkt, vektor, einheitsvektor, weltkoordinatensystem, toleranzen]
abgrenzung_zu: [weltkoordinatensystem, bauteilachse, achse, bauteil, element]
status: entwurf
theorie_pflichtig: required
quellen_primär:
  - "ISO 19111:2019, 'Geographic information — Referencing by coordinates', Abschnitt 7 (Coordinate systems): Begriff des kartesischen Koordinatensystems unabhängig vom Bezugsdatum; trägt die Trennung 'Koordinatensystem' vs. 'Bezugsdatum', die hier als Welt/Lokal-Trennung wieder auftaucht."
  - "DIN ISO 80000-2:2022-08, 'Größen und Einheiten – Teil 2: Mathematik', Abschnitt 2 (Geometrie und Vektoren): kartesisches Koordinatensystem, Rechtshändigkeit, orthonormale Basis."
  - "EN ISO 5459:2011, 'Geometrische Produktspezifikation (GPS) – Bezüge und Bezugssysteme', Abschnitt 5: bauteilbezogene Bezugssysteme als rechtshändige kartesische Systeme, deren Achsen aus Bauteilmerkmalen (Achsen, Flächen, Punkten) abgeleitet werden."
  - "ISO 10303-42:2022, 'Industrial automation systems and integration — Product data representation and exchange — Part 42: Integrated generic resource: Geometric and topological representation', Entitäten 'axis2_placement_3d' und 'cartesian_transformation_operator_3d': normative Festlegung lokaler Platzierungen (Ursprung + zwei Richtungen → Rechtssystem) und ihrer Transformation in das übergeordnete System."
  - "ISO 16739-1:2024 (IFC 4.3), 'Industry Foundation Classes for data sharing in the construction and facility management industries', insbesondere 'IfcLocalPlacement', 'IfcAxis2Placement3D' und die Verschachtelungs-Semantik 'PlacementRelTo' (lokale Platzierung relativ zu einer übergeordneten Platzierung)."
quellen_sekundär:
  - "Murray, R. M.; Li, Z.; Sastry, S. S.: A Mathematical Introduction to Robotic Manipulation. CRC Press 1994, Kap. 2 'Rigid Body Motion': starre Bewegungen als Elemente von SE(3), Komposition `(R₁,t₁) ∘ (R₂,t₂) = (R₁·R₂, R₁·t₂ + t₁)`, Wirkung `p ↦ R·p + t`."
  - "Shoemake, K.: Animating Rotation with Quaternion Curves. SIGGRAPH '85: Quaternionen als kompakte, numerisch stabile Repräsentation von Drehungen in SO(3); Doppel-Überdeckung."
  - "Hartenberg, R. S.; Denavit, J.: Kinematic Synthesis of Linkages. McGraw-Hill 1964: Verkettung lokaler Koordinatensysteme entlang einer kinematischen Kette (DH-Konvention) — mathematisches Vorbild für Verschachtelung."
  - "Foley, J. D.; van Dam, A.; Feiner, S. K.; Hughes, J. F.: Computer Graphics — Principles and Practice. 2nd ed., Addison-Wesley 1996, Kap. 5 'Geometrical Transformations' und Kap. 7 'Object Hierarchy and Simple PHIGS': hierarchisch verschachtelte lokale Koordinatensysteme (Szenengraph)."
  - "Bronstein, I. N. et al.: Taschenbuch der Mathematik, Kap. 3.5 'Analytische Geometrie des Raumes', Koordinatentransformationen."
quellenkonflikt: |
  Es gibt keine Holzbau-Norm (DIN 1052, DIN EN 1995-1-1, SIA 265,
  SIA 232/1, Holzbau-Deutschland-Merkblätter), die ein lokales
  Bauteilkoordinatensystem für die digitale Modellierung von
  Holzkonstruktionen festlegt. Die einschlägigen Quellen sind
  produktdaten- (ISO 10303, ISO 16739/IFC) und allgemein-
  mathematisch (DIN ISO 80000-2, EN ISO 5459).

  Konflikt 1 — Konvention der starren Transformation:
  Es koexistieren zwei Schreibweisen für die Welt-zu-Lokal-Beziehung:

    (a) `p_welt = R · p_lokal + t`        (aktive Wirkung, "(R,t)")
    (b) `p_welt = R · (p_lokal − t')`     (passive Wirkung, t' im Welt-System)

  Murray/Li/Sastry, Foley/van Dam und IFC verwenden (a); ältere
  geodätische und photogrammetrische Quellen verwenden (b). Beide sind
  äquivalent über `t = −R · t'`, aber nicht in derselben Funktion
  mischbar. Eigene Festlegung dieses Glossars: ausnahmslos (a),
  konsistent mit der Code-Realität in
  `zimmermann.domain.koordinaten.LokalePlatzierung.transformiere`.

  Konflikt 2 — Komposition-Reihenfolge:
  In der Robotik (Murray/Li/Sastry) und in Computergrafik-Lehrbüchern
  (Foley/van Dam) wird die Komposition zweier starrer Transformationen
  als "rechts wirkt zuerst" geschrieben:
  `(T₁ ∘ T₂)(p) = T₁(T₂(p))`. Manche Lehrbücher der elementaren
  Linearen Algebra schreiben die umgekehrte Konvention. Eigene
  Festlegung dieses Glossars: "rechts wirkt zuerst", konsistent mit
  `LokalePlatzierung.komponiere` und `Rotation.komponiere` (siehe
  Implementierungshinweis).

  Konflikt 3 — Achsen-Festlegung am Bauteil:
  EN ISO 5459 lässt die Zuordnung x/y/z-Achse zu Bauteilmerkmalen
  offen; im Holzbau koexistieren mehrere Konventionen
  (z. B. x = Faserrichtung, y = Querrichtung in Plattenebene,
  z = Plattendicken-Achse für Plattenwerkstoffe vs. x = Bauteillängs-
  achse, z = vertikale Bauteilrichtung für Stabbauteile). Der
  vorliegende Eintrag definiert das Lokalsystem **strukturell** als
  rechtshändiges kartesisches System ohne Festlegung einer Achsen-
  Bauteil-Zuordnung; die Zuordnung wird pro Bauteilkategorie in
  separaten Glossareinträgen (z. B. `hg_bauteil.md` für Stabbauteile,
  `hg_mehrlagenholz.md` für Plattenwerkstoffe) normativ festgelegt.

  Diese Festlegungen sind konfliktfrei mit allen konsultierten Quellen,
  sobald sie als App-interne Konventionen (nicht als Aussagen über die
  Quellen selbst) verstanden werden.
---

## Prosa-Definition

Ein **lokales Koordinatensystem** ist ein rechtshändiges kartesisches
Bezugssystem (O_L, e_x^L, e_y^L, e_z^L) im dreidimensionalen affinen
Raum, dessen Ursprung und Achsen einem konkreten Bauteil oder
Konstruktionsteil zugeordnet sind und das durch eine eindeutige starre
Transformation (Translation und Rotation) auf das
[Weltkoordinatensystem](hg_weltkoordinatensystem.md) abgebildet wird.

## Mathematische Definition

Sei

- 𝔸³ der dreidimensionale reelle affine Raum,
- W = (O_W, e_x, e_y, e_z, η, ω) das **Weltkoordinatensystem** gemäß
  `hg_weltkoordinatensystem.md`,
- O_L ∈ 𝔸³ ein in W festgelegter Ursprung des Lokalsystems,
- (e_x^L, e_y^L, e_z^L) eine Basis von ℝ³ mit den Eigenschaften
  ```
  ‖e_x^L‖ = ‖e_y^L‖ = ‖e_z^L‖ = 1,                      (Einheitsvektoren)
  ⟨e_x^L, e_y^L⟩ = ⟨e_y^L, e_z^L⟩ = ⟨e_z^L, e_x^L⟩ = 0, (paarweise orthogonal)
  e_x^L × e_y^L = e_z^L.                                 (Rechtssystem)
  ```

Dann ist ein **lokales Koordinatensystem** das Tupel

```
L := (O_L, e_x^L, e_y^L, e_z^L, η_L),
```

wobei

- η_L : 𝔸³ → ℝ³ die Koordinatenabbildung
  ```
  η_L(p) = (x_L, y_L, z_L)  ⇔  p = O_L + x_L·e_x^L + y_L·e_y^L + z_L·e_z^L
  ```
  ist; die Komponenten sind in Millimeter zu interpretieren.

### Starre Transformation L → W

Die Beziehung zwischen L und W wird durch eine **starre Transformation**
T_{L→W} ∈ SE(3) hergestellt, eindeutig bestimmt durch

- den **Translations-Vektor** t ∈ ℝ³ — die Welt-Koordinaten von O_L:
  ```
  t := η(O_L) ∈ ℝ³,    Längeneinheit mm.
  ```
- die **Rotation** R ∈ SO(3) — die orthogonale Matrix mit Determinante
  +1, deren Spalten die Welt-Koordinaten der lokalen Basisvektoren sind:
  ```
  R := ( η(e_x^L) | η(e_y^L) | η(e_z^L) ) ∈ ℝ^{3×3},    R^T R = I, det R = +1.
  ```

Die Rechtssystem-Bedingung `e_x^L × e_y^L = e_z^L` ist äquivalent zu
`det R = +1`.

**Aktive Wirkung auf einen Punkt** mit lokalen Koordinaten p_L ∈ ℝ³:

```
T_{L→W}(p_L) := R · p_L + t                                       (1)
```

— ergibt die Welt-Koordinaten desselben affinen Punktes. Die Inverse ist

```
T_{W→L}(q) := R^T · (q − t) = R^T · q − R^T · t                   (2)
```

(weil R^{-1} = R^T für R ∈ SO(3)).

**Wirkung auf Verschiebungs-Vektoren:** Differenzen zweier Punkte sind
translationsinvariant. Folglich wirkt T_{L→W} auf einem Vektor v ∈ ℝ³
**rein durch die Rotation**:

```
T_{L→W}(v) := R · v.                                              (3)
```

Diese Unterscheidung ist mathematisch zwingend, nicht bloß
konventionell: `(R · p₂ + t) − (R · p₁ + t) = R · (p₂ − p₁)`.

### Verschachtelung

Lokale Koordinatensysteme dürfen **verschachtelt** werden: Ein
Lokalsystem L₂ kann statt direkt auf W auf ein übergeordnetes
Lokalsystem L₁ bezogen sein. Sei dazu

- T_{L₁→W} = (R₁, t₁) die starre Transformation von L₁ nach W,
- T_{L₂→L₁} = (R₂, t₂) die starre Transformation von L₂ nach L₁,
  d. h. der Ursprung O_{L₂} und die Basis (e_x^{L₂}, e_y^{L₂}, e_z^{L₂})
  sind in **L₁-Koordinaten** angegeben.

Dann ist die zusammengesetzte Transformation T_{L₂→W} eindeutig durch

```
T_{L₂→W}(p_{L₂}) = T_{L₁→W}(T_{L₂→L₁}(p_{L₂}))
                 = R₁ · (R₂ · p_{L₂} + t₂) + t₁
                 = (R₁ · R₂) · p_{L₂} + (R₁ · t₂ + t₁)
```

gegeben, also

```
T_{L₂→W} = (R₁ · R₂,  R₁ · t₂ + t₁).                              (4)
```

Schreibt man die Komposition als binäre Operation `∘` mit Lese-
Reihenfolge "rechts wirkt zuerst", so ist

```
T_{L₂→W} = T_{L₁→W} ∘ T_{L₂→L₁}.                                  (5)
```

Per Induktion lässt sich eine **Kette** L_n → L_{n−1} → … → L_1 → W
beliebiger endlicher Tiefe wieder auf eine einzige starre
Transformation in SE(3) reduzieren:

```
T_{L_n→W} = T_{L₁→W} ∘ T_{L₂→L₁} ∘ … ∘ T_{L_n→L_{n−1}}.            (6)
```

(SE(3) ist eine Gruppe — Abgeschlossenheit unter Komposition,
Existenz der Inversen, Identität — daher ist (6) wohldefiniert
unabhängig von der Klammerung.)

## Wohldefiniertheit

- **Existenz**: Zu jedem Welt-Punkt O_L und jeder
  Rechtssystem-Orthonormalbasis ist L durch (1) wohldefiniert; ein
  triviales Beispiel ist L = W mit t = 0, R = I.
- **Eindeutigkeit der Transformation bei gegebenem L**: Bei festgelegter
  Wahl von O_L und (e_x^L, e_y^L, e_z^L) ist (R, t) durch
  ```
  t = η(O_L),    R = (η(e_x^L) | η(e_y^L) | η(e_z^L))
  ```
  eindeutig bestimmt — die Spalten einer orthogonalen Matrix sind durch
  die abgebildeten Basisvektoren festgelegt.
- **Eindeutigkeit von L bei gegebener Transformation**: Umgekehrt legt
  ein Element (R, t) ∈ SE(3) das Lokalsystem L vollständig fest:
  O_L = O_W + t als affiner Punkt, und e_i^L ist das i-te Spaltenvektor
  von R, in W gelesen.
- **Unabhängigkeit von der Komponenten-Wahl**: η_L ist bei festgelegter
  Basis eine Bijektion 𝔸³ ↔ ℝ³; alle abgeleiteten Operationen
  (Differenz, Norm, Skalarprodukt, Kreuzprodukt) sind unter dieser
  Bijektion wohldefiniert und kommutieren mit T_{L→W}, weil R
  orthogonal mit Determinante +1 ist (Norm- und Orientierungs-
  Erhaltung).
- **Wohldefiniertheit der Verschachtelung**: SE(3) ist eine Gruppe
  unter Komposition; (4) und (5) liefern wieder ein Element von
  SE(3). Insbesondere ist `R₁ · R₂ ∈ SO(3)` (Produkt orthogonaler
  Matrizen mit Determinante +1) und `R₁ · t₂ + t₁ ∈ ℝ³` (Summe
  endlicher Vektoren). Die Klammerungs-Unabhängigkeit folgt aus der
  Assoziativität der Gruppen-Operation.
- **Inverse**: Aus (1) folgt T_{W→L} = (R^T, −R^T · t) ∈ SE(3); diese
  existiert für jedes Lokalsystem und ist selbst wieder eine starre
  Transformation.
- **Konsistenz mit `hg_weltkoordinatensystem.md`**: W ist Spezialfall von
  L mit t = 0, R = I; in dieser Sicht ist W = T_{W→W} = (I, 0)
  Identitäts-Element von SE(3).
- **Numerische Stabilität bei verschachtelten Systemen**: Bei
  Verschachtelungstiefe n ≤ 10 und Bauteilabmessungen ≤ 10⁴ mm bleibt
  der akkumulierte Translations-Fehler aus n-facher Komposition unter
  IEEE 754 binary64 deutlich unter `Toleranzen.LAENGE_EPS`. Bei sehr
  tiefen Hierarchien (n ≫ 10) ist eine **periodische Re-Verankerung
  gegen W** sinnvoll, ist aber nicht Bestandteil dieses Eintrags.
- **Nicht-Zirkularität**: Die Definition stützt sich nur auf den
  affinen Raum, das bereits definierte Weltkoordinatensystem, die
  Primitive Punkt, Vektor, Einheitsvektor und auf `Toleranzen`. L
  kommt nicht in seiner eigenen Definition vor.

## Erläuterung (nicht normativ)

Der praktische Nutzen lokaler Koordinatensysteme im Holzbau ist die
**bauteileigene Geometrie-Beschreibung**. Beispielsweise ist eine
Sparrenkerve als geometrisches Muster im Sparren-Lokalsystem
(x = Bauteillängsachse, y = Bauteilbreite, z = Bauteilhöhe) eine
einfache Folge von Schnittebenen mit konstanten Koordinaten. Erst beim
Einbau in eine Dachfläche wird dieselbe Kerve über die Sparren-
Platzierung T_{Sparren→W} = (R, t) auf die im Dach gemeinsame
Welt-Geometrie abgebildet — ein Sparren mit Neigung 35° hat im
Welt-System eine schräg liegende Kerve, im Sparren-Lokalsystem aber
weiterhin dieselbe horizontal-vertikale Form.

Die **Verschachtelung** bringt zwei weitere Strukturmerkmale:

- **Hierarchie**: Eine Versatz-Kerve eines Sparrens kann als
  Sub-Lokalsystem im Sparren-Lokal beschrieben werden; eine
  Bauteilgruppe (z. B. ein vorgefertigtes Dachmodul) kann als
  übergeordnetes Lokalsystem angelegt werden, in dem die einzelnen
  Sparren ihrerseits Lokalsysteme haben. Die Welt-Koordinaten ergeben
  sich automatisch aus der Komposition (6).
- **Wiederverwendung**: Identische Bauteile erhalten identische
  Lokal-Geometrie und unterscheiden sich nur in der Platzierung
  (R, t). Das ist dieselbe Idee wie in IFC (`IfcLocalPlacement` mit
  `PlacementRelTo`) und in BTLx (Bauteil-CNC-Daten relativ zur
  Bauteil-Referenz-Seite).

## Brücke zur Bauteil-/Element-Schicht (begrifflich vorbereitet, nicht
implementiert)

Dieser Eintrag bereitet die spätere Bauteil- und Element-Schicht
**begrifflich** vor, ohne sie festzulegen:

1. **Bauteil-Lokal**: Jedes Bauteil im Sinne von `hg_bauteil.md` erhält
   genau **ein** primäres lokales Koordinatensystem L_B mit einer
   starren Transformation T_{L_B→W} ∈ SE(3) zur Welt. Welche Achse des
   L_B welcher Bauteilrichtung entspricht (z. B. x = Bauteilachse für
   Stabbauteile vs. z = Plattendicken-Achse für Plattenwerkstoffe),
   wird **pro Bauteilkategorie** in den entsprechenden
   Glossareinträgen festgelegt.
2. **Subteil-Lokal / Verbindungs-Lokal**: Geometrische Merkmale eines
   Bauteils (Kerven, Bohrungen, Versätze, Anschnitte) und
   Verbindungselemente (`hg_element.md`) dürfen ihrerseits Lokalsysteme
   L_S besitzen, die **relativ zu L_B** definiert sind (Eltern-Kind-
   Relation): T_{L_S→W} = T_{L_B→W} ∘ T_{L_S→L_B}.
3. **Konstruktionsgruppen-Lokal**: Verschachtelung in der anderen
   Richtung — eine Bauteilgruppe (Dachstuhl-Modul, Wand-Element)
   erhält ein übergeordnetes Lokalsystem L_G, in dem die einzelnen
   Bauteil-Lokalsysteme L_B als Kinder hängen:
   T_{L_B→W} = T_{L_G→W} ∘ T_{L_B→L_G}.

Diese drei Verschachtelungs-Ebenen sind durch (6) mathematisch
vollständig abgedeckt; die zugehörigen **Glossareinträge** und ihre
**Implementierungs-Klassen** (Bauteil-Hierarchie, Szenengraph) sind
Folgearbeit der Phasen D7/D8 und nicht Gegenstand des vorliegenden
Eintrags. Die Code-Klasse `LokalePlatzierung` deckt die starre
Transformation als Einzelglied bereits ab (siehe
Implementierungshinweis), die **Verkettung** über mehrere Hierarchie-
Stufen ist begrifflich vorbereitet, aber noch nicht als
Datenstruktur implementiert.

## Beziehungen

- **Oberbegriff**: keiner. Wie das Weltkoordinatensystem ist L eine
  Modellierungs-Konvention, kein geometrisches Objekt im Modell. Ein
  abstrakter Oberbegriff `koordinatensystem` würde erst sinnvoll,
  wenn er mit `weltkoordinatensystem` und `lokales_koordinatensystem`
  als Geschwistern eingeführt wird; bis dahin wird die Abgrenzung
  inline geführt.
- **Verwandte Begriffe**:
  - **Weltkoordinatensystem** (`hg_weltkoordinatensystem.md`): das
    eindeutige globale Bezugssystem; jedes lokale System ist über
    eine starre Transformation auf W bezogen.
  - **Bauteilachse** (`hg_bauteilachse.md`): eine ausgezeichnete Achse
    eines Bauteils; sie liefert typischerweise einen der drei
    lokalen Basisvektoren (häufig e_x^L), bestimmt aber das
    Lokalsystem nicht vollständig (zwei weitere Achsen fehlen).
- **Abgrenzung**:
  - **Weltkoordinatensystem**: global gültig, eindeutig; lokale
    Systeme sind bauteileigen und vielfach.
  - **Bauteilachse**: einzelne Achse, kein vollständiges
    Koordinatensystem. Eine Bauteilachse kann eine Achse eines
    Lokalsystems sein, ist aber kein Synonym dafür.
  - **Achse** (`hg_achse.md`): allgemeine ausgezeichnete Linie; ohne
    Ursprungspunkt und ohne zwei weitere orthogonale Richtungen
    kein Koordinatensystem.
  - **Bauteil** (Folge-Eintrag, in `hg_bauteil.md` bereits angelegt):
    physikalisches Objekt; das Lokalsystem ist eine an das Bauteil
    geheftete **Konvention**, nicht das Bauteil selbst.
  - **Element** (Folge-Eintrag, in `hg_element.md` bereits angelegt):
    abstrakte Basisklasse für Bauteile, Verbindungsmittel,
    Verbinder, Verstärkungselemente; auch jedes Element trägt im
    Modell ein Lokalsystem, die Festlegung erfolgt in den jeweiligen
    Spezial-Einträgen.
  - **LV95 / WGS84**: externe Geo-Bezugssysteme; lokale
    Bauteilkoordinatensysteme werden **nicht** in LV95/WGS84
    geführt, sondern intern in mm bezüglich W.

## Implementierungshinweis

**Bestehende Code-Realität (Stand D5-2):**

Die starre Transformation T_{L→W} eines Lokalsystems ist in der
Domänen-Schicht durch die Klasse
`zimmermann.domain.koordinaten.LokalePlatzierung` repräsentiert; die
Drehkomponente R ∈ SO(3) ist in
`zimmermann.domain.koordinaten.Rotation` als Einheits-Quaternion
realisiert. Die im Code dokumentierten Operationen sind die
Referenz für diesen Glossareintrag — keine zusätzlichen Operationen
werden hier eingeführt.

```kotlin
package zimmermann.domain.koordinaten

/**
 * Starre Transformation (Translation + Rotation) eines lokalen
 * Koordinatensystems relativ zum Weltkoordinatensystem.
 *
 * Glossar: hg_lokales_koordinatensystem.md
 *
 * Felder-Semantik (normativ):
 *   - translation : Welt-Koordinaten des Lokal-Ursprungs O_L,
 *     entspricht t in der Glossar-Definition (Gleichung 1).
 *   - rotation    : Orientierung der Lokal-Basis relativ zur Welt;
 *     entspricht R ∈ SO(3) als Einheits-Quaternion.
 *
 * Wirkung (Glossar Gleichung 1):
 *   p_welt = rotation.rotiere(p_lokal) + translation.
 */
public data class LokalePlatzierung internal constructor(
    public val translation: Vektor,
    public val rotation: Rotation,
) { /* … */ }
```

**Im Code implementiert** (`LokalePlatzierung`, vollständig durch
diesen Glossareintrag normativ gedeckt):

- `transformiere(p: Punkt) : Punkt` — Wirkung (1) auf Punkte
  (Lokal → Welt).
- `transformiere(v: Vektor) : Vektor` und
  `transformiere(e: Einheitsvektor) : Einheitsvektor` — Wirkung (3)
  auf Verschiebungs-Vektoren bzw. Richtungen, rein rotativ.
- `inverseTransformiere(p: Punkt) : Punkt` etc. — Wirkung (2),
  T_{W→L}.
- `inverse() : LokalePlatzierung` — liefert (R^T, −R^T · t) als neues
  `LokalePlatzierung`-Objekt; wohldefiniert für jede gültige Instanz.
- `komponiere(other: LokalePlatzierung) : LokalePlatzierung` —
  binäre Komposition gemäß (4) mit Lese-Reihenfolge "rechts wirkt
  zuerst": `(this komponiere other).transformiere(p) =
  this.transformiere(other.transformiere(p))`. Damit ist die
  Verschachtelung (5)/(6) auf der Code-Ebene als wiederholte
  `komponiere`-Verkettung darstellbar.
- `istGleichePlatzierung(other, eps)` — Toleranz-basierter Vergleich
  unter Berücksichtigung der Quaternionen-Doppel-Überdeckung.
- `IDENTITAET = LokalePlatzierung(Vektor.NULL, Rotation.IDENTITAET)` —
  Identitäts-Element von SE(3), entspricht L = W.
- `aus(translation, rotation) : Resultat<LokalePlatzierung,
  EntartetGeometrie>` — Konstruktor mit Endlichkeits-Prüfung der
  Translation; Rotation trägt ihre Norm-Invariante per Typ.

**Im Code implementiert** (`Rotation`, R ∈ SO(3)):

- `rotiere(v: Vektor) : Vektor`, `rotiere(e: Einheitsvektor) :
  Einheitsvektor`, `rotiere(p: Punkt) : Punkt` — Drehung um den
  Welt-Ursprung.
- `inverse() : Rotation` — konjugiertes Quaternion `(w, −x, −y, −z)`.
- `komponiere(other) : Rotation` — Hamilton-Produkt
  `this · other`, Lese-Reihenfolge "rechts wirkt zuerst".
- `istGleicheRotation(other, eps)` — Vergleich unter Doppel-
  Überdeckung.
- `IDENTITAET = (1, 0, 0, 0)`.
- `ausAchseUndWinkel(achse: Einheitsvektor, winkel: Double) :
  Resultat<Rotation, EntartetGeometrie>` — Rodrigues-/Quaternion-
  Konstruktion `q = (cos(α/2), sin(α/2)·achse)`.
- `ausQuaternion(w, x, y, z) : Resultat<Rotation, EntartetGeometrie>`
  — Konstruktor mit Normierung und Endlichkeits-/Null-Prüfung.

**Konventionen:**

- **Einheit**: Translation in mm (Double); Rotation dimensionslos
  (Einheits-Quaternion). Niemals Mischung in einer Funktion.
- **Konvention der starren Transformation**: ausnahmslos
  `p_welt = R · p_lokal + t` (Gleichung 1 dieses Eintrags); die
  passive Konvention `R · (p_lokal − t')` ist verboten.
- **Konvention der Komposition**: ausnahmslos "rechts wirkt zuerst"
  (Gleichungen 4–6). Wer eine andere Reihenfolge benötigt, vertauscht
  die Operanden vor dem Aufruf.
- **Wirkung auf Vektoren**: rein rotativ (Gleichung 3). Eine
  Translation auf einer Verschiebung anzuwenden ist mathematisch
  falsch und in der Schnittstelle nicht möglich (`transformiere(v:
  Vektor)` ruft nur `rotation.rotiere(v)` auf).
- **Verkettungs-Reihenfolge der Inverse**: `T.inverse() ∘ T = id` und
  `T ∘ T.inverse() = id` (jeweils im Sinne von
  `istGleichePlatzierung`). Daraus folgt für eine Kette
  `T_n ∘ … ∘ T_1`: Inverse = `T_1.inverse() ∘ … ∘ T_n.inverse()`.

**Invarianten:**

1. `R^T · R = I ∧ det R = +1` — strukturell garantiert durch die
   Einheits-Quaternion-Repräsentation in `Rotation` und die
   Norm-Invariante der Companion-Factories.
2. Translation endlich (kein NaN, kein ±∞) — strukturell garantiert
   durch `LokalePlatzierung.aus` mit `Resultat`-Wrapping und
   `@ConsistentCopyVisibility`.
3. Komposition zweier gültiger Platzierungen ist wieder eine gültige
   Platzierung — folgt aus 1 und 2 sowie der Norm-Erhaltung von
   `Rotation.rotiere`.

**Edge Cases:**

- **L = W**: Spezialfall `LokalePlatzierung.IDENTITAET`, transformiert
  jeden Punkt strukturell-exakt auf sich selbst.
- **Reine Translation** (R = I): `LokalePlatzierung(t, Rotation.
  IDENTITAET)` mit `t ≠ 0`. Erlaubt; transformiere wirkt rein
  additiv.
- **Reine Rotation um O_W** (t = 0): erlaubt; transformiere wirkt
  rein als Drehung um den Welt-Ursprung.
- **Nicht-finite Translation**: durch `LokalePlatzierung.aus`
  ausgeschlossen (`Resultat.Fehler(EntartetGeometrie.NichtFinit)`).
- **Null-Quaternion oder nicht-finite Quaternion-Komponenten**:
  durch `Rotation.ausQuaternion` ausgeschlossen
  (`EntartetGeometrie.Nullrichtung` bzw.
  `EntartetGeometrie.NichtFinit`).
- **Numerische Akkumulation bei tiefer Verschachtelung**: bei
  Verschachtelungstiefe n ≤ 10 strukturell vernachlässigbar; tiefere
  Ketten siehe Wohldefiniertheit.

**Verwendungsregel:**

- Funktionen, die Punkte oder Vektoren entgegennehmen, gehen ohne
  weitere Annotation davon aus, dass diese in **W** gegeben sind
  (siehe `hg_weltkoordinatensystem.md`, Verwendungsregel).
- Lokale Koordinaten erhalten in der späteren Bauteil-Schicht einen
  eigenen Wrapper-Typ (z. B. `BauteilLokal<T>`) mit expliziter
  `nachWelt(platzierung: LokalePlatzierung) → T`-Operation; eine
  implizite Reinterpretation lokaler Komponenten als
  Welt-Komponenten ist verboten. Der Wrapper-Typ ist Folgearbeit von
  D7/D8.

## Quellen

**Primär (normativ):**

- ISO 19111:2019, „Geographic information — Referencing by
  coordinates".
- DIN ISO 80000-2:2022-08, „Größen und Einheiten – Teil 2:
  Mathematik".
- EN ISO 5459:2011, „Geometrische Produktspezifikation (GPS) –
  Bezüge und Bezugssysteme".
- ISO 10303-42:2022, „Industrial automation systems and integration
  — Product data representation and exchange — Part 42: Integrated
  generic resource: Geometric and topological representation"
  (`axis2_placement_3d`, `cartesian_transformation_operator_3d`).
- ISO 16739-1:2024 (IFC 4.3), „Industry Foundation Classes for data
  sharing in the construction and facility management industries"
  (`IfcLocalPlacement`, `IfcAxis2Placement3D`, `PlacementRelTo`).

**Sekundär:**

- Murray, R. M.; Li, Z.; Sastry, S. S.: *A Mathematical Introduction
  to Robotic Manipulation.* CRC Press 1994.
- Shoemake, K.: „Animating Rotation with Quaternion Curves."
  *SIGGRAPH '85.*
- Hartenberg, R. S.; Denavit, J.: *Kinematic Synthesis of Linkages.*
  McGraw-Hill 1964.
- Foley, J. D.; van Dam, A.; Feiner, S. K.; Hughes, J. F.:
  *Computer Graphics — Principles and Practice.* 2nd ed.,
  Addison-Wesley 1996.
- Bronstein, I. N. et al.: *Taschenbuch der Mathematik*, Kap. 3.5.

**Korpus (nicht autoritativ):**

- Wikipedia, Lemmata „Koordinatensystem", „Rigid transformation",
  „SE(3)", „Scene graph" (abgerufen 2026-05-08).
