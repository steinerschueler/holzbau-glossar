---
id: rechteck_querschnitt
benennung: Rechteck-Querschnitt
synonyme: ["rechteckiger Querschnitt", "Rechteckprofil", "Vollholzquerschnitt (rechteckig)", "Kantholzquerschnitt"]
abgelehnte_benennungen: [Rechteckform, Vierkantquerschnitt, Vierkant, "rectangular cross section", "rectangular profile"]
oberbegriff: querschnitt
begriffstyp: generisch
voraussetzungen: [querschnitt, punkt, vektor, ebene, toleranzen]
abgrenzung_zu: [querschnitt, polygon, ebene, bauteilachse, bauteil]
status: entwurf
subglossar_pendant: notwendig
quellen_primär:
  - "DIN EN 14081-1:2019-10, 'Holzbauwerke – Nach Festigkeit sortiertes Bauholz mit rechteckigem Querschnitt – Teil 1: Allgemeine Anforderungen': normative Festlegung des rechteckigen Querschnitts als Klassifikationsmerkmal von Bauholz."
  - "DIN EN 14080:2013-09, 'Holzbauwerke – Brettschichtholz und Balkenschichtholz – Anforderungen', Abschnitt 5 (Anforderungen): rechteckiger Querschnitt als Standardform."
  - "DIN EN 15497:2014-07, 'Keilgezinktes Vollholz für tragende Zwecke', Abschnitt 5: rechteckiger Querschnitt für KVH."
  - "DIN EN 1995-1-1:2010-12 (Eurocode 5), Abschnitt 6.1 (Bemessung von Querschnitten unter einachsiger Beanspruchung): Querschnittswerte für rechteckige Querschnitte (A = b·h, I_y = b·h³/12, I_z = h·b³/12, W_y = b·h²/6, W_z = h·b²/6)."
  - "SIA 265:2021, 'Holzbau', Anhang A (Querschnittswerte) und Anhang B (Standardquerschnitte für Bauholz und BSH)."
  - "ISO 16739-1:2024 (IFC 4.3), Entität 'IfcRectangleProfileDef' (XDim = Breite, YDim = Höhe, Position als IfcAxis2Placement2D im Schwerpunkt)."
quellen_sekundär:
  - "Lignum (Hrsg.): Holzbautabellen HBT, Lignum, Zürich, aktuelle Auflage, Kap. 'Standardquerschnitte Vollholz', 'Standardquerschnitte KVH', 'Standardquerschnitte BSH'."
  - "Mönck, W.; Rug, W.: Holzbau – Bemessung und Konstruktion. 16. Aufl., Beuth, Berlin 2015, Kap. 5 'Querschnittswerte', Tabellen rechteckiger Vollholzquerschnitte."
  - "Blass, H. J.; Sandhaas, C.: Ingenieurholzbau – Grundlagen der Bemessung. KIT Scientific Publishing, Karlsruhe 2016, Kap. 5."
  - "Natterer, J.; Herzog, T.; Volz, M.: Holzbau-Atlas. 4. Aufl., Birkhäuser, Basel 2003, Tabellenanhang 'Standardquerschnitte'."
  - "Bronstein, I. N. et al.: Taschenbuch der Mathematik. Kap. 3.1.2 'Rechteck' (Schwerpunkt im Schnittpunkt der Diagonalen, Flächenträgheitsmomente)."
quellenkonflikt: |
  Es besteht kein Konflikt in den Quellen. Sowohl DIN EN 14081-1
  (Bauholz) als auch DIN EN 14080 (BSH/BSc) und DIN EN 15497 (KVH)
  setzen den rechteckigen Querschnitt als Standardform voraus. SIA 265
  und EC5 führen die Querschnittswerte (A, I, W) für rechteckige
  Querschnitte mit den klassischen geschlossenen Formeln. Die App
  übernimmt diese Festlegungen direkt.

  Konvention zur Definition der lokalen 2D-Achsen (u_hat, v_hat) in der
  Querschnittsebene:

  - **u_hat** = lokale **y-Achse** des Bauteils (Breitenrichtung,
    parallel zur Breitenkante b).
  - **v_hat** = lokale **z-Achse** des Bauteils (Höhenrichtung,
    parallel zur Höhenkante h).
  - Das lokale 3D-System des Bauteils ist (x_hat_lokal, y_hat_lokal, ẑ_lokal)
    mit x_hat_lokal entlang der Bauteilachse, y_hat_lokal = u_hat in der
    Querschnittsebene und ẑ_lokal = v_hat in der Querschnittsebene
    (rechtshändig, x_hat × y_hat = ẑ).

  Diese Konvention ist konsistent mit:

  - **EC5-Tradition**: y-Achse als „starke" Biegeachse (I_y > I_z),
    wenn h > b; W_y = b·h²/6 (Biegung um y-Achse, Spannungen in
    z-Richtung).
  - **IFC**: `IfcRectangleProfileDef.XDim` (Breite, x-lokal-Profil)
    und `YDim` (Höhe, y-lokal-Profil); Position als
    `IfcAxis2Placement2D` mit Ursprung im Schwerpunkt.
  - **BTLx**: Part-Element mit Width und Height, Reference Side 1
    auf der Breitenseite.
  - **cadwork**: Bauteil-y entlang Breite, Bauteil-z entlang Höhe.

  Die Konvention „b = Breite" und „h = Höhe" mit b ≤ h für
  hochkant verlegte Bauteile (Sparren, Pfetten, Stützen-Biegung um
  starke Achse) ist Industrie-Standard, aber **nicht erzwungen**: ein
  flach verlegter Sparrenfussklotz darf b > h tragen. Die Klasse
  fordert nur b > 0 und h > 0; die Zuordnung zur „starken" oder
  „schwachen" Biegeachse erfolgt über die Querschnittseigenschaften
  (Folgearbeit), nicht über eine b-vs-h-Ordnungsrelation.
---

## Prosa-Definition

Ein **Rechteck-Querschnitt** ist ein Querschnitt der Form RECHTECK,
der in einem lokalen 2D-Koordinatensystem (u, v) seiner Quer-
schnittsebene mit Ursprung im Flächenschwerpunkt durch die
abgeschlossene rechteckige Punktmenge [−b/2, b/2] × [−h/2, h/2]
gegeben ist, mit den Pflichtparametern Breite b > 0 und Höhe h > 0
(in mm).

## Mathematische Definition

Sei

- 𝓠𝓢 die Menge der Querschnitte (siehe `querschnitt`),
- E ⊂ ℝ³ die Querschnittsebene (siehe `ebene`) mit lokalem
  rechtshändigem Orthonormalsystem (u_hat, v_hat) ⊂ E im Flächenschwerpunkt
  z ∈ E als Ursprung,
- b > 0 die **Breite** in mm,
- h > 0 die **Höhe** in mm.

Dann ist ein **Rechteck-Querschnitt** das Tupel

```
RQ := (form, ebene, flaechenschwerpunkt, breite, hoehe)
     = (RECHTECK, E, z, b, h)
```

mit der Punktmenge in lokalen (u, v)-Koordinaten

```
Q_lokal(b, h) := { (u, v) ∈ ℝ² | −b/2 ≤ u ≤ b/2  ∧  −h/2 ≤ v ≤ h/2 }
              = [−b/2, b/2] × [−h/2, h/2]
```

und der zugehörigen Punktmenge in W

```
Q(RQ) := { z + u·u_hat + v·v_hat ∈ ℝ³ | (u, v) ∈ Q_lokal(b, h) }.
```

Es ist 𝓡𝓠 ⊂ 𝓠𝓢, d. h. die Menge der Rechteck-Querschnitte ist eine
disjunkte Teilmenge der Querschnitts-Menge mit `form = RECHTECK`.

**Eckpunkte** in lokalen (u, v)-Koordinaten (zyklisch gegen den
Uhrzeigersinn, beginnend mit dem Eckpunkt im Quadranten (+u, +v)):

```
v₁ = ( +b/2, +h/2 )
v₂ = ( −b/2, +h/2 )
v₃ = ( −b/2, −h/2 )
v₄ = ( +b/2, −h/2 )
```

In W-Koordinaten:

```
v_i^W = z + u_i · u_hat + v_i · v_hat   für i = 1, …, 4.
```

**Flächenschwerpunkt**: per Konstruktion im Ursprung des lokalen
(u, v)-Systems, da

```
z_lokal = (1 / (b·h)) · ∫∫_{Q_lokal} (u, v) du dv
        = ( (1/b) · ∫_{-b/2}^{+b/2} u du,  (1/h) · ∫_{-h/2}^{+h/2} v dv )
        = ( 0, 0 ).
```

Damit gilt z = z + 0·u_hat + 0·v_hat, d. h. der Flächenschwerpunkt in W
stimmt mit dem Ursprung des lokalen Querschnittssystems überein.

**Querschnittsfläche**:

```
A := 𝓛²(Q(RQ)) = b · h   (in mm²).
```

## Wohldefiniertheit

- **Existenz**: Für b > 0 und h > 0 ist Q_lokal(b, h) eine
  nicht-leere, abgeschlossene, beschränkte, zusammenhängende, konvexe
  Punktmenge in ℝ² mit positivem Lebesgue-Mass b·h > 0. Die Einbettung
  in ℝ³ über die affine Abbildung (u, v) ↦ z + u·u_hat + v·v_hat ist eine
  Isometrie und überträgt diese Eigenschaften.
- **Eindeutigkeit der Punktmenge**: Q_lokal(b, h) ist durch (b, h)
  eindeutig festgelegt; Q(RQ) ist durch (E, z, u_hat, v_hat, b, h) eindeutig
  festgelegt.
- **Wohldefiniertheit des Flächenschwerpunkts**: Der Flächenschwerpunkt
  liegt per Symmetrie im Schnittpunkt der Diagonalen, d. h. im
  Ursprung des lokalen (u, v)-Systems. Die Definition ist daher
  konsistent mit der Forderung aus `hg_querschnitt.md`, dass der
  Flächenschwerpunkt z ∈ E ein Pflichtfeld des Querschnitts ist.
- **Wohldefiniertheit des lokalen Systems (u_hat, v_hat)**: Die Wahl von
  (u_hat, v_hat) als rechtshändiges Orthonormalsystem in E bestimmt die
  Orientierung der Breiten- und Höhenkanten in W. Diese Wahl ist
  **Festlegung des Bauteils**, nicht des Querschnitts (siehe
  Implementierungshinweis unten und `hg_bauteil.md`); auf der Ebene des
  Querschnitts wird (u_hat, v_hat) als gegeben vorausgesetzt. Die Punktmenge
  Q(RQ) hängt von dieser Wahl ab; alternative rechtshändige
  Orthonormalsysteme (z. B. Drehung um 90°) ergeben andere
  Punktmengen, aber dieselbe Querschnittsfläche und dieselben
  intrinsischen Querschnittseigenschaften (modulo Vertauschung
  von I_y und I_z).
- **Eckpunkte**: Die vier Eckpunkte v₁ … v₄ sind paarweise
  verschieden (b > 0 ∧ h > 0), liegen in E und bilden ein
  einfaches, konvexes Polygon (Polygon im Sinne von `polygon`).
- **Klassen-Invariante**: `form = RECHTECK` ist konstant für diese
  Subklasse.
- **Disjunktheit zu anderen Subklassen**: Ein Rechteck-Querschnitt
  ist ausgeschlossen von der Menge der Rund-, I-, T-, polygonal-
  Querschnitte durch das Diskriminator-Feld `form`.
- **Nicht-Zirkularität**: Die Definition stützt sich auf
  `querschnitt`, `punkt`, `vektor`, `ebene` und `toleranzen`. Sie
  verweist nicht auf andere Querschnitt-Subklassen in ihrer eigenen
  Definition.

## Erläuterung (nicht normativ)

### Standardquerschnitte im Holzbau

Der rechteckige Querschnitt ist im Holzbau der dominierende
Querschnittstyp:

- **Vollholz / KVH** (DIN EN 14081-1, DIN EN 15497): Standardgrössen
  nach Lignum HBT bzw. DIN 4070, z. B. 60×120, 80×160, 100×200,
  120×240, 140×240, 160×240 mm.
- **Brettschichtholz / BSH** (DIN EN 14080): Standardbreiten 80, 100,
  120, 140, 160, 200, 240 mm; Höhen frei wählbar in 40-mm-Stufen.
- **Balkenschichtholz / BSc** (DIN EN 14080): rechteckig, kleinere
  Standardquerschnitte.
- **Furnierschichtholz / LVL** (DIN EN 14374): rechteckig, breite
  Stege bis 1800 mm.

Im Sparrendach-Standardfall (Memory `project_grobplan_erstes_tool`)
ist der Sparren ein Vollholz- oder KVH-Bauteil mit Rechteck-
Querschnitt, typisch 80×160 oder 100×200 mm. Daher ist der
Rechteck-Querschnitt der **Default-Subtyp** für die D8a-Bauteilklasse.

### Geometrische Eigenschaften

Für einen Rechteck-Querschnitt mit Breite b und Höhe h gelten die
klassischen geschlossenen Formeln:

```
A    = b · h                        (Querschnittsflaeche)
I_y  = b · h³ / 12                  (Flächentraegheitsmoment um y)
I_z  = h · b³ / 12                  (Flächentraegheitsmoment um z)
W_y  = b · h² / 6                   (Widerstandsmoment um y)
W_z  = h · b² / 6                   (Widerstandsmoment um z)
i_y  = h / sqrt(12)                 (Tragheitsradius um y)
i_z  = b / sqrt(12)                 (Tragheitsradius um z)
I_T  ≈ k(b/h) · b³ · h              (Torsions-Flaechenmoment, naeherungsweise)
```

mit y-Achse parallel zur Breitenkante b und z-Achse parallel zur
Höhenkante h (siehe oben). Diese Formeln werden im Folge-Eintrag
`querschnittseigenschaften` aus der Querschnittsdefinition
hergeleitet und nicht hier als Definitionen geführt
(Konservativität, vgl. CLAUDE.md / Glossar-Methodik).

### „Starke" und „schwache" Biegeachse

Bei einem Rechteck-Querschnitt mit h > b (hochkant verlegt) ist die
y-Achse die „starke" Biegeachse (I_y > I_z) und die z-Achse die
„schwache". Sparren werden konventionell hochkant verlegt
(h = Sparrenhöhe entlang der Falllinie projizierter Komponente, b =
Sparrenbreite); die starke Biegeachse liegt damit horizontal in der
Dachebene, was bei Schneelast die maximale Tragfähigkeit ergibt.

Die Klasse `RechteckQuerschnitt` erzwingt **keine** Ordnung b ≤ h.
Ein flach verlegter Riegel (h < b, „flachkant") ist erlaubt; die
Bemessungsschicht erkennt die starke/schwache Achse über die
Querschnittseigenschaften.

### Lokales 2D-System und Bauteil-Einbettung

Die Trennung „lokal in der Querschnittsebene" vs. „Einbettung in W"
ist konsistent mit IFC und BTLx:

- **IFC**: `IfcRectangleProfileDef(XDim = b, YDim = h, Position =
  IfcAxis2Placement2D(Location = Schwerpunkt, RefDirection = u_hat))`;
  die Einbettung in W erfolgt über `IfcExtrudedAreaSolid` und
  `IfcAxis2Placement3D`.
- **BTLx**: Part-Element trägt `Width = b`, `Height = h`; Lage und
  Orientierung über `RefSide` und `RefEdge`.

Die Klasse `RechteckQuerschnitt` enthält daher nur b und h, nicht
die Einbettungs-Information; letztere lebt im Bauteil.

## Beziehungen

- **Oberbegriff**: `querschnitt` (Form-Diskriminator RECHTECK).
- **Subklassen**: keine. Rechteck-Querschnitt ist Blatt der
  Hierarchie. (Eine eventuelle weitere Spezialisierung „Quadrat-
  Querschnitt" als b = h ist als Werte-Spezialfall zu behandeln,
  nicht als eigene Klasse.)
- **Pflichtfelder über `querschnitt` hinaus**:
  - **Breite** b > 0 (in mm; Pflicht): Ausdehnung entlang der lokalen
    u_hat-Achse (Bauteil-y).
  - **Höhe** h > 0 (in mm; Pflicht): Ausdehnung entlang der lokalen
    v_hat-Achse (Bauteil-z).
- **Verwendung**:
  - **Bauteil** (`bauteil`): jedes **Stabbauteil** trägt typisch einen
    Rechteck-Querschnitt als Pflichtfeld (D8a; siehe Memory
    `project_grobplan_erstes_tool`); im Standardfall Vollholz/KVH/BSH.
  - **Sparren** (`sparren`): Standardfall, 80×160 oder 100×200 mm.
  - **Pfette** (`pfette`): Standardfall, 120×160 oder 140×200 mm.
  - **Stütze** (Folgearbeit): Standardfall, 120×120 oder 140×140 mm.
  - **Strebe** (Folgearbeit): Standardfall, 80×120 mm.
- **Abgrenzung**:
  - **Querschnitt** (`querschnitt`): abstrakter Oberbegriff;
    Rechteck-Querschnitt ist eine konkrete Subklasse, charakterisiert
    durch `form = RECHTECK` und die rechteckige Punktmenge.
  - **Polygon** (`polygon`): die Berandung eines Rechteck-Querschnitts
    ist ein einfaches, konvexes Polygon mit 4 Eckpunkten; der
    Rechteck-Querschnitt ist aber **keine** Polygon-Instanz, weil er
    zusätzlich die Klassen-Invariante `form = RECHTECK` und die
    Pflichtparameter (b, h) trägt. Polygonale Querschnitte mit
    beliebiger Eckenzahl gehören in die Folgearbeit-Klasse
    `polygonaler_querschnitt`.
  - **Ebene** (`ebene`): die Querschnittsebene ist eine Ebene; der
    Rechteck-Querschnitt ist eine beschränkte Teilmenge dieser Ebene
    mit fester rechteckiger Form.
  - **Bauteilachse** (`bauteilachse`): die Querschnittsebene steht
    per Konstruktion rechtwinklig zur Bauteilachsen-Tangente, und der
    Schwerpunkt des Rechteck-Querschnitts liegt auf der Bauteilachse.
  - **Bauteil** (`bauteil`): Rechteck-Querschnitt ist Eigenschaft
    eines Stabbauteils, nicht das Bauteil selbst.

## Implementierungshinweis

Datentyp (Domänen-Schicht, Kotlin, Schicht
`zimmermann.domain.bauteil.querschnitt`):

```kotlin
package zimmermann.domain.bauteil.querschnitt

import zimmermann.domain.geometrie.Toleranzen
import zimmermann.domain.fehler.EntartetGeometrie
import zimmermann.domain.fehler.Resultat

/**
 * Rechteck-Querschnitt: Querschnitt-Subklasse mit rechteckiger
 * Schnittfigur in der Querschnittsebene.
 * Glossar: hg_rechteck_querschnitt.md
 *
 * Pflichtfelder: breite b > 0, hoehe h > 0 (in mm).
 * Form: konstant RECHTECK.
 *
 * Lokales 2D-System: Ursprung im Flaechenschwerpunkt, lokale
 * u-Achse parallel zur Breitenkante (Bauteil-y), lokale v-Achse
 * parallel zur Hoehenkante (Bauteil-z). Punktmenge:
 * [-b/2, b/2] x [-h/2, h/2].
 *
 * Die Einbettung der Querschnittsebene in W (Lage des Schwerpunkts,
 * Orientierung der lokalen Achsen) ist Sache des Bauteils, nicht
 * des Querschnitts. RechteckQuerschnitt ist daher eine Werteklasse,
 * die fuer mehrere Bauteile geteilt werden kann.
 *
 * Validierung: Konstruktion ausschliesslich ueber Factory
 * `RechteckQuerschnitt.aus(breite, hoehe): Resultat<RechteckQuerschnitt,
 * EntartetGeometrie>`. Konstruktor ist `internal`. Vorbild:
 * `LokalePlatzierung.aus(...)`.
 */
@ConsistentCopyVisibility
public data class RechteckQuerschnitt internal constructor(
    public val breite: Double,
    public val hoehe: Double,
) : Querschnitt {
    public override val form: QuerschnittsForm = QuerschnittsForm.RECHTECK

    public override val flaeche: Double get() = breite * hoehe

    public companion object {
        public fun aus(
            breite: Double,
            hoehe: Double,
        ): Resultat<RechteckQuerschnitt, EntartetGeometrie> {
            // 1. Endlich.
            // 2. breite > Toleranzen.NORM_EPS, hoehe > Toleranzen.NORM_EPS.
            // 3. konkrete Pruefung in Factory; bei Verletzung
            //    Resultat.Fehler(EntartetGeometrie.NullQuerschnitt).
            TODO("D8a-Implementierung")
        }
    }
}
```

- **Einheit**: Breite und Höhe in mm (Double); Fläche in mm²;
  Form-Diskriminator dimensionslos (Aufzählung).
- **Identität**: Rechteck-Querschnitt trägt **keine** UUID. Werteklasse
  (data class); zwei Rechteck-Querschnitte mit identischen (b, h)
  sind structurally equal und dürfen geteilt werden (z. B. ein
  Standardquerschnitt 80×160 für alle Sparren eines Daches).
- **Lokales 2D-System (Konvention)**: u_hat = Bauteil-y (Breitenrichtung,
  parallel zu b), v_hat = Bauteil-z (Höhenrichtung, parallel zu h). Diese
  Konvention wird im Bauteil bei der Einbettung der Querschnittsebene
  in W realisiert; der Querschnitt selbst trägt nur (b, h).
- **Invarianten** (in Factory `RechteckQuerschnitt.aus(...)` prüfen,
  bei Verletzung `Resultat.Fehler(EntartetGeometrie.NullQuerschnitt)`
  zurückgeben; kein `init+require`, keine Exception):
  1. `form == QuerschnittsForm.RECHTECK` (Klassen-Invariante).
  2. `breite.isFinite() && hoehe.isFinite()`.
  3. `breite > Toleranzen.NORM_EPS && hoehe > Toleranzen.NORM_EPS`
     (positives Flächenmass A = b·h > 0).
  4. **Keine** Forderung b ≤ h (flachkant ist erlaubt).
- **Standardgrössen** (Lignum HBT, Memory `reference_richtpreise_holzbau`,
  als Konstanten in `RechteckQuerschnitt.Standardgroessen` zu führen,
  Folgearbeit):
  - Vollholz / KVH: 60×120, 80×160, 100×200, 120×240, 140×240, 160×240.
  - BSH: Breite ∈ {80, 100, 120, 140, 160, 200, 240}, Höhe in
    40-mm-Stufen.
- **IFC-Mapping**:
  - `IfcRectangleProfileDef.XDim` ← `breite`.
  - `IfcRectangleProfileDef.YDim` ← `hoehe`.
  - `IfcRectangleProfileDef.Position` ← `IfcAxis2Placement2D` mit
    Location im Schwerpunkt (lokal Origin) und RefDirection als u_hat.
- **BTLx-Mapping**: Part-Element mit `Width = breite`, `Height = hoehe`.
- **Edge Cases**:
  - **Quadrat-Querschnitt** (b == h): erlaubt; keine eigene Klasse,
    sondern Wertspezialisierung. Stützenquerschnitt 120×120 ist
    typischer Anwendungsfall.
  - **Sehr schmaler Querschnitt** (b ≪ h, z. B. 24×240): erlaubt;
    Plattenstreifen oder Lattung. Bemessungsschicht prüft Kipp-
    stabilität.
  - **Negative oder Null-Werte**: nicht erlaubt; Factory liefert
    `Resultat.Fehler`.
  - **Nicht-finite Werte (NaN, ±∞)**: nicht erlaubt; Factory liefert
    `Resultat.Fehler`.
  - **Sehr grosse Werte** (b · h > 10⁹ mm² ≈ 1 m² Querschnitt):
    erlaubt, aber in der Praxis unüblich; keine harte Obergrenze.
- **Bezeichner-Konvention** (CLAUDE.md): Domänen-Klasse heisst
  `RechteckQuerschnitt` (deutsch, Glossarbegriff zusammengesetzt aus
  Subtyp + Oberbegriff).

## Quellen

**Primär (normativ):**

- DIN EN 1995-1-1:2010-12, „Eurocode 5: Bemessung und Konstruktion
  von Holzbauten – Teil 1-1".
- SIA 265:2021, „Holzbau", Schweizerischer Ingenieur- und
  Architektenverein, Zürich.
- DIN EN 14081-1:2019-10, „Holzbauwerke – Nach Festigkeit
  sortiertes Bauholz mit rechteckigem Querschnitt – Teil 1:
  Allgemeine Anforderungen".
- DIN EN 14080:2013-09, „Holzbauwerke – Brettschichtholz und
  Balkenschichtholz – Anforderungen".
- DIN EN 15497:2014-07, „Keilgezinktes Vollholz für tragende
  Zwecke".
- ISO 16739-1:2024, „Industry Foundation Classes (IFC)",
  `IfcRectangleProfileDef`.

**Sekundär:**

- Lignum (Hrsg.): *Holzbautabellen HBT.* Lignum, Zürich, aktuelle
  Auflage.
- Mönck, W.; Rug, W.: *Holzbau – Bemessung und Konstruktion.*
  16. Auflage, Beuth, Berlin 2015.
- Blass, H. J.; Sandhaas, C.: *Ingenieurholzbau – Grundlagen der
  Bemessung.* KIT Scientific Publishing, Karlsruhe 2016.
- Natterer, J.; Herzog, T.; Volz, M.: *Holzbau-Atlas.* 4. Auflage,
  Birkhäuser, Basel 2003.
- Bronstein, I. N. et al.: *Taschenbuch der Mathematik.* Verlag
  Harri Deutsch, Frankfurt am Main, aktuelle Auflage.

**Korpus (nicht autoritativ):**

- Holzbau Deutschland, Merkblatt „Begriffe und Klassifizierungen
  für den Holzbau" (abgerufen 2026-05-09).
- Wikipedia, Lemma „Rechteckquerschnitt" (abgerufen 2026-05-09).
