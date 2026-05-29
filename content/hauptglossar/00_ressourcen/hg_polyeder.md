---
id: polyeder
benennung: Polyeder
synonyme: ["Vielflach", "Vielflächner", "Polytop (3D)", "festes Polyeder"]
abgelehnte_benennungen: [Körper, Volumenkörper, Mehrflächner, "polyhedron", "solid"]
oberbegriff: null
begriffstyp: generisch
voraussetzungen: [punkt, vektor, ebene, polygon, halbraum, toleranzen]
abgrenzung_zu: [polygon, halbraum, ebene, bauteil]
status: entwurf
theorie_pflichtig: required
quellen_primär:
  - "DIN ISO 80000-2:2022-08, 'Größen und Einheiten – Teil 2: Mathematik', Abschnitt 2 (Geometrie), Bezeichnungen für Vielflache (Polyeder)."
  - "ISO 19107:2019 'Geographic information – Spatial schema', Abschnitt 6.4 'GM_Solid' (volumetrisches Geometrieobjekt mit polygonal berandeter Hülle, B-Rep-Modell)."
  - "DIN EN ISO 10303-42 'Industrieautomation – Produktmodelldaten – Teil 42: Geometrische und topologische Repräsentation' (B-Rep-Modell für volumetrische Festkörper)."
quellen_sekundär:
  - "Ziegler, G. M.: Lectures on Polytopes. Springer 1995, Kap. 0–2 (V- und H-Repräsentation konvexer Polytope, Hauptsatz von Weyl-Minkowski)."
  - "de Berg, M.; Cheong, O.; van Kreveld, M.; Overmars, M.: Computational Geometry – Algorithms and Applications. 3. Aufl., Springer 2008, Kap. 11 (Convex Hulls in 3D) und Kap. 12 (Binary Space Partitions)."
  - "Hoffmann, C. M.: Geometric and Solid Modeling – An Introduction. Morgan Kaufmann 1989, Kap. 3 (B-Rep) und Kap. 4 (CSG)."
  - "Mäntylä, M.: An Introduction to Solid Modeling. Computer Science Press 1988, Kap. 6 (Boundary Representation)."
  - "Bronstein, I. N. et al.: Taschenbuch der Mathematik. Kap. 3.5.4 'Polyeder im Raum'."
quellenkonflikt: |
  Holzbau-Normen (SIA 265, EN 1995-1-1, DIN 1052) verwenden den Begriff
  „Polyeder" nicht; sie modellieren Bauteile geometrisch implizit über
  Querschnitt + Achse (Stab) bzw. Trägerfläche + Dicke (Fläche). Bei
  Bauteilen mit Verbindungs-Ausschnitten (Zapfen, Versätze, Blattungen)
  gibt es jedoch in keiner Norm eine geschlossene geometrische
  Repräsentation; die Geometrie wird in den Werkplänen rissweise
  dargestellt.

  In der mathematischen und CAD-Literatur stehen zwei klassische,
  beweisbar äquivalente Repräsentationen für (konvexe) Polyeder zur
  Verfügung:
    - **V-Repräsentation** (Eckpunkt-Repräsentation): Polyeder als
      konvexe Hülle endlich vieler Punkte (Ziegler, Kap. 1).
    - **H-Repräsentation** (Halbraum-Repräsentation): Polyeder als
      Schnitt endlich vieler Halbräume (Ziegler, Kap. 1; Hauptsatz
      von Weyl-Minkowski).
  Für allgemeine, nicht zwingend konvexe Polyeder verwendet das
  Solid Modeling überwiegend die **B-Rep** (Boundary Representation,
  Hoffmann; Mäntylä) oder die **CSG** (Constructive Solid Geometry,
  Hoffmann).

  Eigene Festlegung in diesem Glossar: ein Polyeder ist ein
  beschränkter, abgeschlossener, regulärer Teilkörper von ℝ³, dessen
  Rand eine endliche Vereinigung ebener Polygone ist; die App-Domäne
  modelliert ihn primär als **B-Rep** (Listen von Eckpunkten, Kanten,
  Flächen mit Inzidenzrelationen) und im konvexen Spezialfall
  äquivalent als **H-Rep** (Schnitt endlich vieler geschlossener
  Halbräume). Diese Festlegung ist konsistent mit ISO 19107
  (GM_Solid), DIN EN ISO 10303-42 (B-Rep), Ziegler (Polytope) und
  Hoffmann/Mäntylä (Solid Modeling).
---

## Prosa-Definition

Ein **Polyeder** ist ein beschränkter, abgeschlossener,
dreidimensionaler Teilkörper von ℝ³, dessen Rand eine endliche,
geschlossene, kantenweise einfach inzidente Vereinigung ebener
Polygone ist und der mit seinem Inneren übereinstimmt mit dem
Abschluss seines topologischen Inneren (Regularität).

## Mathematische Definition

Sei

- V = (v_1, …, v_n) ∈ (ℝ³)^n eine endliche Folge von **Eckpunkten**
  mit n ≥ 4, paarweise verschieden, nicht alle koplanar,
- E = (e_1, …, e_m) ⊂ V × V eine Menge von **Kanten** als
  ungeordnete Punktepaare {v_i, v_j}, i ≠ j, mit m ≥ 6,
- F = (F_1, …, F_k) eine Menge von **Begrenzungsflächen** mit
  k ≥ 4, wobei jede Fläche F_l ein Polygon im Sinne von `polygon`
  ist (mit Eckpunkten aus V und Kanten aus E),
- ι_F : F → 𝒫(E), ι_E : E → 𝒫(V) **Inzidenzfunktionen**, die
  jeder Fläche ihre Randkanten und jeder Kante ihre Endpunkte
  zuordnen.

Das Tupel P = (V, E, F, ι_F, ι_E) heißt **Polyeder** in B-Rep
(Boundary Representation), wenn die folgenden Bedingungen gelten:

1. **Inzidenz-Konsistenz**: Für jede Kante e ∈ E ist
   |ι_E(e)| = 2 (zwei verschiedene Eckpunkte). Für jede Fläche
   F_l ∈ F bilden die Kanten ι_F(F_l) den Rand des Polygons F_l
   in zyklischer Reihenfolge.

2. **Mannigfaltigkeits-Bedingung am Rand**: Jede Kante e ∈ E
   gehört zu **genau zwei** Flächen aus F (zweiseitige
   Mannigfaltigkeitsstruktur ohne Rand). Jeder Eckpunkt v ∈ V
   liegt in einem topologischen Stern, dessen Linkkurve zyklisch
   einfach geschlossen ist.

3. **Planare Flächen**: Jede Fläche F_l ist ein Polygon im Sinne
   von `polygon`, insbesondere koplanar und einfach (nicht
   selbstüberschneidend).

4. **Geschlossenheit der Hülle**: ∂P := ⋃_{l=1}^{k} F_l ist eine
   geschlossene, orientierbare, stückweise lineare 2-Mannigfaltigkeit
   in ℝ³.

5. **Beschränktheit und Regularität**: Die durch ∂P berandete
   Punktmenge

   ```
   |P| := ∂P ∪ Inneres(∂P) ⊂ ℝ³
   ```

   (mit „Inneres" im Sinne der von ∂P berandeten beschränkten
   Komponente von ℝ³ ∖ ∂P) ist beschränkt, abgeschlossen und
   **regulär**, d. h. |P| = cl(int(|P|)).

Die Punktmenge |P| ist die geometrische Substanz des Polyeders;
das Tupel (V, E, F, ι_F, ι_E) ist seine kombinatorisch-
topologische Struktur.

**Euler-Formel**: Für ein einfach zusammenhängendes Polyeder
(Geschlecht g = 0, z. B. Quader, Sparren-Polyeder, Tetraeder) gilt

```
|V| − |E| + |F| = 2.
```

Allgemein gilt für ein zusammenhängendes Polyeder vom Geschlecht
g (Anzahl der „Henkel"):

```
|V| − |E| + |F| = 2 − 2g.
```

**Konvexer Spezialfall (H-Rep, äquivalent)**: Ein Polyeder P ⊂ ℝ³
heißt **konvex**, wenn für alle x, y ∈ |P| die Verbindungsstrecke
[x, y] ⊂ |P|. Konvexe Polyeder lassen sich nach dem **Hauptsatz
von Weyl-Minkowski** äquivalent als endlicher Schnitt
geschlossener Halbräume schreiben:

```
|P| = ⋂_{i=1}^{k} H_bar_i,    H_bar_i = H_bar(p_i, n_i),
```

mit Stützpunkten p_i ∈ ℝ³ und nach innen gerichteten Normalen
n_i ∈ ℝ³ \ {0} (Halbraum-Konvention nach `halbraum`). Diese
**H-Repräsentation** ist für konvexe Polyeder gleichwertig zur
**V-Repräsentation** als konvexe Hülle der Eckpunkte:

```
|P| = conv(V) = { Σ_{i=1}^{n} λ_i v_i | λ_i ≥ 0, Σ λ_i = 1 }.
```

**Allgemeiner Fall (CSG)**: Nicht-konvexe Polyeder werden in der
**Constructive Solid Geometry** als Boolesche Kombination
einfacherer Polyeder (insbesondere Halbraum-Schnitte) gebildet:

```
|P| = (P_1 ∪ P_2 ∪ … ∪ P_r) \ (Q_1 ∪ … ∪ Q_s),
```

mit konvexen Bausteinen P_j und Q_j. Im Holzbau ist genau diese
Konstruktion natürlich: ein Sparren-Polyeder mit Versatz-Ausschnitt
ist der reguläre Volumen-Differenzkörper aus dem ungeschnittenen
Sparrenquader und dem Versatz-Polyeder.

Wesentliche abgeleitete Größen:

- **Eckenzahl**: |V|. **Kantenzahl**: |E|. **Flächenzahl**: |F|.
- **Geschlecht**: g = (2 − (|V| − |E| + |F|)) / 2.
- **Volumen**: V(P) := ∫_{|P|} dV (mm³); berechenbar per
  Divergenztheorem als V(P) = (1/6) · Σ_{F ∈ F} ⟨v_{F,1}, n_F⟩ · A(F)
  oder per signierten Tetraeder-Volumen über die triangulierten
  Flächen.
- **Oberfläche**: A(∂P) := Σ_{F ∈ F} A(F) (mm²).
- **Schwerpunkt**: c(P) ∈ |P| (Volumenschwerpunkt).
- **Achsenparalleler Hüllquader (AABB)**: kleinster Quader mit zu
  den Welt-Koordinatenachsen parallelen Kanten, der |P| umschließt.

## Wohldefiniertheit

- **Existenz**: Für jede zulässige Tupel-Eingabe (V, E, F, ι_F, ι_E),
  die Bedingungen 1–5 erfüllt, ist das Polyeder als Punktmenge
  |P| ⊂ ℝ³ wohldefiniert; die Existenz nicht-trivialer Beispiele
  (Tetraeder, Quader) ist klassisch.
- **Eindeutigkeit der Innenseiten**: Die Mannigfaltigkeits-
  Bedingung 2 zusammen mit der Geschlossenheit 4 garantiert nach
  dem **Jordan-Brouwer-Trennungssatz** für stückweise lineare
  Hyperflächen, dass ℝ³ ∖ ∂P aus genau zwei zusammenhängenden
  Komponenten besteht, von denen genau eine beschränkt ist.
  Diese beschränkte Komponente ist das Innere; sein Abschluss ist
  |P|.
- **Wohldefiniertheit des Volumens**: V(P) ist als Lebesgue-
  Volumen einer beschränkten, regulären, abgeschlossenen Menge
  definiert; die Divergenztheorem-Formel ist invariant unter Wahl
  der Triangulierung der Flächen (klassisch).
- **Repräsentantenwahl der Eckenfolge**: Zyklische Verschiebung
  innerhalb einer Fläche und globale Permutation der Flächen-,
  Kanten- und Eckenfolgen ändern das Polyeder nicht. Identität
  zweier Polyeder als kombinatorische Strukturen ist die
  Isomorphie ihrer Inzidenzgraphen; als Punktmengen die
  Mengengleichheit der |P|.
- **Äquivalenz B-Rep ↔ H-Rep im konvexen Fall**: Hauptsatz von
  Weyl-Minkowski (Ziegler, Kap. 1.1): Eine Teilmenge von ℝ³ ist
  genau dann ein beschränkter Schnitt endlich vieler Halbräume,
  wenn sie die konvexe Hülle endlich vieler Punkte ist. Für
  konvexe Polyeder im Sinne dieses Eintrags sind beide
  Repräsentationen daher gleichwertig; eine kann aus der anderen
  algorithmisch konstruiert werden (Doppelbeschreibungs-Methode,
  konvexe-Hülle-Algorithmen).
- **Nicht-Zirkularität**: Die Definition stützt sich auf `punkt`,
  `vektor`, `ebene`, `polygon`, `halbraum`, `toleranzen` sowie
  klassische Resultate (Jordan-Brouwer für PL-Hyperflächen,
  Weyl-Minkowski für konvexe Polytope). Sie kommt nicht in ihrer
  eigenen Definition vor; insbesondere wird `polygon` für die
  Begrenzungsflächen und `halbraum` für die H-Repräsentation
  verwendet, beide bereits ohne Bezug auf `polyeder` definiert.
- **Begriffstyp `primitiv` (gewählt)**: Ein Polyeder ist im
  Glossar als zusammengesetztes Geometrieprimitiv geführt — analog
  zu `polygon` (das ebenfalls aus Punkten und Strecken aufgebaut
  ist, aber als Primitiv geführt wird). Eine Klassifizierung als
  `generisch` wäre vertretbar, weil das Polyeder seine
  Bestandteile (Polygone, Halbräume) referenziert und nicht
  konzeptionell unter sie subsumierbar ist; die Wahl `primitiv`
  spiegelt jedoch wider, dass es in der Domänen-Schicht als
  atomarer Geometrietyp behandelt wird. Begründung: keine andere
  Glossar-Klasse subsumiert ein Polyeder als Spezialisierung.

## Erläuterung (nicht normativ)

Das Polyeder ist die natürliche geometrische Repräsentation für
**Bauteilkörper im Holzbau**, sobald die Geometrie über die
einfache Repräsentation „Achse + Querschnitt" oder „Trägerfläche +
Dicke" hinausgeht. Konkret tritt der Polyederbegriff auf bei:

- **ungeschnittene Stab-Bauteile** (Sparren, Pfette, Stütze) als
  prismatische Polyeder (Quader oder allgemeiner: konvexes
  Prisma über das Querschnittspolygon);
- **geschnittene Stab-Bauteile mit Verbindungs-Ausschnitten**
  (Sparren mit Versatz und Klauenanschnitt, Pfette mit
  Schwalbenschwanzaufnahme, Stütze mit Zapfen): Polyeder
  entstanden durch Volumen-Subtraktion eines konvexen Versatz- bzw.
  Verbindungs-Polyeders aus einem ungeschnittenen Stab-Polyeder;
- **Volumen-Bauteile** (Massivholz-Treppen, gefräste BSH-Knoten,
  zusammengesetzte BSP-Wandelemente): allgemeine, oft
  nicht-konvexe Polyeder;
- **Schnitt- und Verschneidungsgeometrien** (Walmverschneidungen,
  Kehlausarbeitungen, Anschnitt-Polygone): Schnitt zweier oder
  mehrerer Polyeder, der selbst wieder ein Polyeder ist.

**Walmdach-Hüllvolumen als zusammengesetztes Polyeder** (Stamm-
Anwendungsfall einer CSG-Vereinigung konvexer Bausteine): Im
Berufsschul-Korpus der Zimmerei wird das Hüllvolumen eines
Walmdachs als **Vereinigung dreier konvexer Bausteine** zerlegt
— ein **dreieckiges Prisma** zwischen den beiden Firstendpunkten
und **zwei rechteckige Pyramiden** an den Walmenden. Mit
Firstlänge f, Traufbreite b, Traufflucht l und Dachhöhe h ergibt
sich die kompakte Volumenformel

```
V = (1/6) · b · h · (2·l + f).
```

Diese Zerlegung ist das prominenteste Beispiel im Holzbau-Korpus
für eine **CSG-Vereinigung konvexer Polyeder zu einem
nicht-zwingend-konvexen Hüllpolyeder** und illustriert die
`csgVereinigung`-Operation der Folgearbeit `BRepPolyeder` auf
Stamm-Anwendungsfall-Niveau. Der zugehörige Volumen-Begriff
(Polyeder in der Rolle „Hüllvolumen eines Daches") ist als
Folgearbeit `dachkoerper` vorgesehen (siehe §Beziehungen und
`HG_KONVENTIONEN.md` §6.A).

**Konvex vs. allgemein**: Konvexe Polyeder erlauben effiziente
Operationen (insbesondere die H-Repräsentation als Halbraum-
Schnitt, die für Inzidenztests in O(k) statt O(|F|) ist) und
entstehen direkt bei jedem prismatischen Bauteil mit konvexem
Querschnitt. Allgemeine (nicht-konvexe) Polyeder treten auf,
sobald Verbindungs-Ausschnitte gemacht werden — ein Sparren mit
Versatzausnehmung ist nicht mehr konvex. In der App-Domäne wird
ein gemeinsamer Polyeder-Datentyp als B-Rep mit optionaler
Konvexitäts-Annotation geführt; konvexe Polyeder erlauben
zusätzlich die effiziente H-Rep-Repräsentation.

**Repräsentationsentscheidung**: Die App-Domäne führt **B-Rep als
Primärdarstellung** (Listen von Eckpunkten, Kanten, Flächen mit
Inzidenzfunktionen). Der Grund: B-Rep ist universell (auch für
nicht-konvexe Polyeder), interagiert direkt mit der Render-Schicht
(Filament rendert B-Rep-Meshes), und Verbindungs-Ausschnitte sind
als CSG-Operationen über B-Rep ausdrückbar. Die H-Rep wird als
**abgeleitete Sekundärdarstellung** für konvexe Polyeder bei Bedarf
erzeugt (z. B. für effiziente Inzidenz- und Schnitt-Tests).

## Beziehungen

- **Oberbegriff**: keiner als formales Glossarprimitiv;
  mathematisch ein beschränkter, regulärer 3-dimensionaler
  Teilkörper von ℝ³ mit polygonal stückweise linearem Rand. Im
  Glossar als Primitiv geführt.
- **Spezialisierungen / Rollen**:
  - **Konvexes Polyeder** (`polyeder_konvex`, in Folgearbeit):
    Polyeder mit der Konvexitätseigenschaft; H-Rep verfügbar.
  - **Quader** (`quader`, in Folgearbeit): konvexes Polyeder mit
    sechs rechteckigen, paarweise parallelen Seitenflächen.
  - **Prisma** (`prisma`, in Folgearbeit): konvexes Polyeder, das
    durch Translation eines Polygons entlang einer Achse entsteht.
  - **Bauteilkörper** (`bauteilkoerper`, in Folgearbeit): Polyeder
    in der Rolle „Volumen eines konkreten Bauteils im
    Welt-Koordinatensystem".
  - **Dachkörper** (`dachkoerper`, in Folgearbeit): Polyeder in
    der Rolle „Hüllvolumen eines Daches" (Walmdach-Volumen,
    Satteldach-Volumen, allgemeines Dach-Hüllvolumen), typischerweise
    als CSG-Vereinigung konvexer Bausteine (Prismen, Pyramiden)
    konstruiert.
- **Bestandteile (partitiv)**:
  - **Eckpunkte** (V): die nulldimensionalen Bestandteile des Randes.
  - **Kanten** (E): die eindimensionalen Bestandteile des Randes,
    jede eine Strecke zwischen zwei Eckpunkten.
  - **Begrenzungsflächen** (F): die zweidimensionalen Bestandteile
    des Randes, jede ein Polygon (siehe `polygon`).
  - **Inneres**: int(|P|), die offene Volumenmenge.
  - **Rand**: ∂P = ⋃ F_l, eine geschlossene PL-2-Mannigfaltigkeit.
- **Abgrenzung**:
  - **Polygon** (`polygon`): zweidimensional; ein Polygon ist die
    Begrenzungsfläche eines Polyeders, nicht das Polyeder selbst.
    Ein Polyeder hat |F| ≥ 4 Polygonflächen.
  - **Halbraum** (`halbraum`): unbeschränkt; ein Polyeder ist
    beschränkt. Ein konvexes Polyeder ist ein **endlicher Schnitt**
    geschlossener Halbräume; ein einzelner Halbraum ist kein
    Polyeder. Diese Beziehung löst die in `hg_halbraum.md`
    angedeutete Vorwärtsreferenz auf: Halbräume sind die
    atomaren Bausteine konvexer Polyeder.
  - **Ebene** (`ebene`): zweidimensional, unbeschränkt; jede
    Begrenzungsfläche eines Polyeders liegt in einer Ebene
    (Trägerebene des Flächenpolygons).
  - **Bauteil** (`bauteil`): allgemeiner Begriff aus der Holzbau-
    Domäne; ein Bauteil ist mehr als nur seine Geometrie (Identität,
    Lage, Werkstoff, Annotationen). Ein Polyeder kann **als
    Geometrie eines Bauteils** dienen (Variante `Bauteilgeometrie.Volumen`
    in `hg_bauteil.md`), ist aber selbst kein Bauteil.
  - **Selbstüberschneidende Polyeder** (z. B. nicht-mannigfaltige
    Hüllen, Sterne): werden in diesem Glossar **nicht** als
    Polyeder zugelassen. In der `KonvexerPolyeder`-Implementierung
    sind solche Eingaben strukturell ausgeschlossen (Halbraum-Schnitt
    ist konstruktiv wohlgeformt). Mit der Folgearbeit `BRepPolyeder`
    werden sie als `Entartet.Selbstschnitt` bzw.
    `Entartet.NichtMannigfaltig` zurückgewiesen — beide Varianten sind
    heute noch nicht im `EntartetGeometrie`-Sealed-Interface vorhanden
    (siehe Implementierungshinweis).

## Implementierungshinweis

**Code-Eingrenzung:** Codeseitig wird vorerst nur **konvexer Polyeder
als endlicher Schnitt von Halbräumen** implementiert
(`KonvexerPolyeder`). Das deckt alle absehbaren Anwendungsfälle der
App ab (Quader, Prismen, Pyramiden, parametrische Werkstücke; Sparren
mit Kerven, geschichtete Bauteile). Eine spätere Erweiterung auf
allgemeine B-Rep-Polyeder (`BRepPolyeder` mit Eckpunkten/Kanten/Flächen,
Inzidenz-Strukturen, Selbstschnitt-Tests) bleibt vorgesehen, wird aber
erst eingeführt, wenn ein konkreter Anwendungsfall (z. B. nicht-konvexe
Bool'sche Operationen) sie verlangt. Der oben definierte allgemeine
Polyeder-Begriff bleibt als Glossar-Spezifikation gültig —
`KonvexerPolyeder` ist der erste implementierte Spezialfall (analog zur
Modi-Differenzierung in `hg_faserrichtung.md`: Glossar deckt alle Modi ab,
Code grenzt zunächst auf den am häufigsten benötigten ein).

**Entartet-Varianten je Implementierungs-Variante:**

Die `EntartetGeometrie`-Sealed-Class enthält für `KonvexerPolyeder`
strukturell nur:

- `LeeresHalbraumSystem` — der Schnitt der angegebenen Halbräume ist leer.
- `UnbeschraenktesPolyeder` — der Schnitt ist nicht-leer, aber unbeschränkt.
- `NichtFinit` — eine Halbraum-Definition enthält NaN/±∞ (geerbt aus den
  Halbräumen).

`KonvexerPolyeder` kennt strukturell **keinen** Selbstschnitt, **keine**
Nicht-Mannigfaltigkeit und **keine** entarteten Flächen — der
Halbraum-Schnitt ist konstruktiv wohlgeformt.

Folgearbeit `BRepPolyeder` (Boundary-Representation, allgemeine
Polyeder) wird zusätzlich folgende Varianten erfordern, die heute noch
nicht im `EntartetGeometrie`-Sealed-Interface existieren:

- `Selbstschnitt` — zwei Flächen schneiden sich entlang einer
  nicht-Kanten-Linie.
- `NichtMannigfaltig` — eine Kante gehört zu mehr als zwei Flächen, oder
  eine Fläche ist nicht-orientierbar.
- `EntarteteFlaeche` — eine Fläche hat Fläche 0 oder kollineare Eckpunkte.
- `NichtPlanareFlaeche` — Eckpunkte einer Fläche nicht koplanar innerhalb
  `LAENGE_EPS`.
- `NichtGeschlossen` — Flächen bilden keine geschlossene Hülle (offene
  Kanten vorhanden).
- `LeerePolyederFlaeche` — |V| < 4 oder |F| < 4 in einer B-Rep-Eingabe.
- (Weitere bei konkreter Bedarfsklärung.)

Die folgenden Datentyp-, Invarianten- und Edge-Case-Skizzen beschreiben
ausschließlich die **Folgearbeit `BRepPolyeder`** und sind für die
aktuelle `KonvexerPolyeder`-Implementierung nicht maßgeblich; sie
stehen hier dokumentiert, damit der Begriffsraum vollständig vorbereitet
ist.

---

**Folgearbeit-Skizze `BRepPolyeder` (nicht aktuelle Implementierung):**

Datentyp (Domänen-Schicht, Kotlin, Schicht `domain.geometrie`):

```kotlin
package domain.geometrie

import domain.Toleranzen

/**
 * Polyeder als B-Rep (Boundary Representation).
 * Glossar: hg_polyeder.md
 *
 * Primärrepräsentation: Eckpunkte + Kanten + Flächen mit
 * Inzidenzrelationen. Konvexe Polyeder können zusätzlich eine
 * H-Repräsentation tragen (endlicher Schnitt geschlossener
 * Halbräume); diese wird bei Bedarf abgeleitet.
 */
data class Polyeder(
    val ecken: List<Punkt>,                   // V
    val flaechen: List<Polyederflaeche>,       // F mit Eckindex-Zyklen
    val konvex: Boolean = false                // Konvexitäts-Annotation
) {
    init {
        // alle Invarianten 1..5 prüfen, sonst Entartet
    }

    /**
     * Eine Fläche als zyklische Folge von Eckindices in `ecken`.
     * Die Trägerebene wird intern aus den ersten drei nicht-
     * kollinearen Indices abgeleitet; die Eckenfolge muss bezüglich
     * der nach außen weisenden Außennormale rechtshändig orientiert
     * sein (siehe Erläuterung).
     */
    data class Polyederflaeche(
        val eckIndices: List<Int>,             // i_1, …, i_p (zyklisch)
        val aussenNormale: Einheitsvektor      // ‖.‖ = 1, nach außen
    )
}

/** H-Repräsentation für konvexe Polyeder. */
data class PolyederH(
    val halbraeume: List<Halbraum>             // alle Geschlossen, Innen-Normale
)

/** Entartet-Varianten. */
sealed class PolyederErgebnis {
    data class Regulaer(val p: Polyeder) : PolyederErgebnis()
    sealed class Entartet : PolyederErgebnis() {
        object LeerePolyederFlaeche : Entartet()        // V < 4 oder F < 4
        data class EntarteteFlaeche(val index: Int) : Entartet()
        object NichtGeschlossen : Entartet()            // Hülle nicht geschlossen
        object NichtMannigfaltig : Entartet()           // Kanten ≠ 2 Flächen
        object Selbstschnitt : Entartet()               // Flächen schneiden sich
        data class NichtPlanareFlaeche(val index: Int) : Entartet()
        object NichtFinit : Entartet()
    }
}
```

- **Einheit**: Eckpunkt-Koordinaten in mm; Volumen in mm³;
  Oberfläche in mm². Die Außennormalen jeder Fläche sind
  dimensionslos (Einheitsvektoren).
- **Repräsentationsentscheidung**: B-Rep als Primärdarstellung;
  H-Rep nur für konvexe Polyeder als optionale Sekundärdarstellung
  (Konvertierung über Doppelbeschreibungs-Methode oder
  konvexe-Hülle-Algorithmen). Begründung: B-Rep ist universell,
  rendering-kompatibel, und Verbindungs-Ausschnitte (zentral im
  Holzbau) sind als CSG-Operationen über B-Rep auszudrücken.
- **Außennormalen-Konvention**: Die Außennormale jeder Fläche zeigt
  **vom Inneren des Polyeders nach außen**. Diese Konvention ist
  verbindlich und im KDoc jeder Konstruktor- und Operations-
  methode zu nennen. Die Eckenfolge einer Fläche ist relativ zu
  ihrer Außennormale rechtshändig zu orientieren (Daumen entlang
  Außennormale, Finger entlang Eckenfolge).
- **Achtung**: Diese Außennormalen-Konvention auf der Polyeder-Ebene
  ist die **Umkehrung** der Halbraum-Konvention nach `hg_halbraum.md`,
  bei der die Normale **in den Halbraum hinein** zeigt. Bei
  Konversion B-Rep → H-Rep ist daher die Außennormale jeder
  Begrenzungsfläche zu negieren, um die Innen-Normale der
  zugehörigen Halbräume zu erhalten.
- **Invarianten** (in Factory `Polyeder.of(...)` prüfen, bei
  Verletzung Entartet-Variante zurückgeben, niemals Exception):
  1. **Mindestgröße**: |V| ≥ 4 und |F| ≥ 4 — sonst
     `Entartet.LeerePolyederFlaeche`.
  2. **Planare Flächen**: jede Fläche muss als Polygon im Sinne
     von `polygon` konstruierbar sein (Koplanarität der Eckpunkte
     innerhalb Toleranzen.LAENGE_EPS, k ≥ 3, einfach) — sonst
     `Entartet.NichtPlanareFlaeche` bzw. `Entartet.EntarteteFlaeche`.
  3. **Mannigfaltigkeit**: jede Kante (definiert durch ein Paar
     aufeinanderfolgender Eckindices in einer Fläche) gehört zu
     genau zwei Flächen — sonst `Entartet.NichtMannigfaltig`.
  4. **Geschlossenheit**: die Vereinigung aller Flächen bildet
     eine geschlossene 2-Mannigfaltigkeit — sonst
     `Entartet.NichtGeschlossen` (geprüft über die Kanten-zu-Flächen-
     Inzidenz).
  5. **Selbstschnittfreiheit**: keine zwei nicht-benachbarten Flächen
     schneiden sich im Inneren — sonst `Entartet.Selbstschnitt`. Test
     in O(|F|²) hinreichend; für Zwischenergebnisse einer CSG-Pipeline
     kann die Invariante temporär ausgesetzt werden (Konfiguration
     über Factory-Parameter).
  6. **Finite Koordinaten**: keine NaN, keine ±∞ — sonst
     `Entartet.NichtFinit`.
- **Edge Cases / Entartet-Varianten** (Folgearbeit `BRepPolyeder`; alle
  als Varianten der gemeinsamen `EntartetGeometrie`-Hierarchie nach
  D3-Konvention, kein Exception-Werfen; aktuell **nicht** im
  Sealed-Interface vorhanden, werden mit `BRepPolyeder` ergänzt):
  - `Entartet.LeerePolyederFlaeche` (|V| < 4 oder |F| < 4): kein
    3D-Körper bildbar.
  - `Entartet.EntarteteFlaeche(index)`: eine Flächen-Polygon-
    Komponente degeneriert zu Strecke oder Punkt.
  - `Entartet.NichtPlanareFlaeche(index)`: Eckpunkte einer Fläche
    nicht koplanar innerhalb LAENGE_EPS — korrekturwürdig
    (Triangulierung der Fläche oder Anpassung der Eckpunkte).
  - `Entartet.NichtGeschlossen`: Flächen bilden keine geschlossene
    Hülle (offene Kanten vorhanden).
  - `Entartet.NichtMannigfaltig`: eine Kante gehört zu ≠ 2 Flächen
    (z. B. drei Flächen treffen sich an einer Kante: T-Knoten).
  - `Entartet.Selbstschnitt`: zwei nicht-benachbarte Flächen
    schneiden sich. Je nach Anwendung Defekt (finales Bauteil)
    oder zulässig (CSG-Zwischenergebnisse).
  - `Entartet.NichtFinit`: ein Eckpunkt enthält NaN/±∞.
- **Bewusst nicht als Entartung modelliert**:
  - **Konkavität / Geschlecht > 0**: nicht-konvexe Polyeder und
    Polyeder mit Henkeln (Geschlecht g ≥ 1) sind **gültige**
    Polyeder; lediglich die Konvexitäts-Annotation ist dann false.
  - **Sehr kleine oder dünne Flächen**: zulässig, aber numerisch
    sensibel; Warnung im Domain-Test.
- **Konstruktoren**:
  - `Polyeder.of(ecken, flaechen, konvex = false): PolyederErgebnis`
    — vollständige B-Rep-Konstruktion mit Validierung.
  - `Polyeder.ausHRepKonvex(halbraeume: List<Halbraum>): PolyederErgebnis`
    — H-Rep → B-Rep für konvexe Polyeder via Doppelbeschreibungs-
    Methode; setzt `konvex = true`.
  - `Polyeder.quader(p_min: Punkt, p_max: Punkt): Polyeder` —
    achsenparalleler Quader als häufigster Spezialfall (Stab-
    Bauteilkörper vor Verbindungs-Ausschnitten).
  - `Polyeder.prisma(grundpolygon: Polygon, hoehe: Vektor): Polyeder`
    — Translationsprisma als allgemeiner prismatischer
    Bauteilkörper.
- **Identität / Gleichheit**:
  - Standard-`equals`: strikt gleiche Repräsentanten-Tupel.
  - `gleichKombinatorisch(other)`: Isomorphie der Inzidenz-
    Strukturen (gleiche topologische Struktur, ggf. unterschiedliche
    Geometrie).
  - `gleichGeometrisch(other, eps)`: gleiche Punktmenge |P| modulo
    Toleranz.
- **Abgeleitete Operationen** (`PolyederOps.kt`):
  - `fun volumen(): Double` (mm³, via Divergenztheorem über
    triangulierte Flächen).
  - `fun oberflaeche(): Double` (mm², Σ Flächeninhalte).
  - `fun schwerpunkt(): Punkt` (Volumenschwerpunkt).
  - `fun hueckquader(): AABB` — achsenparalleler Hüllquader.
  - `fun enthaeltPunkt(p: Punkt, eps: Double): Boolean` —
    Inzidenztest; im konvexen Fall via H-Rep in O(|F|), im
    allgemeinen Fall via Ray-Casting.
  - `fun istKonvex(eps: Double): Boolean` — Test über die
    H-Rep-Konsistenz aller Flächen.
  - `fun zuHRep(): Resultat<PolyederH, EntartetGeometrie>` — nur für konvexe Polyeder.
  - `fun csgVereinigung(other: Polyeder): PolyederErgebnis`,
    `csgSchnitt`, `csgDifferenz` — Boolesche Operationen für
    Verbindungs-Ausschnitte (Implementierung Folgearbeit).

## Quellen

**Primär (normativ):**

- DIN ISO 80000-2:2022-08, „Größen und Einheiten – Teil 2:
  Mathematik", Abschnitt 2.
- ISO 19107:2019, „Geographic information – Spatial schema",
  Abschnitt 6.4 (GM_Solid).
- DIN EN ISO 10303-42, „Industrieautomation – Produktmodelldaten –
  Teil 42: Geometrische und topologische Repräsentation".

**Sekundär:**

- Ziegler, G. M.: *Lectures on Polytopes.* Springer, New York 1995.
- de Berg, M.; Cheong, O.; van Kreveld, M.; Overmars, M.:
  *Computational Geometry – Algorithms and Applications.*
  3. Aufl., Springer 2008.
- Hoffmann, C. M.: *Geometric and Solid Modeling – An Introduction.*
  Morgan Kaufmann, San Mateo 1989.
- Mäntylä, M.: *An Introduction to Solid Modeling.* Computer
  Science Press, Rockville 1988.
- Bronstein, I. N.; Semendjajew, K. A.; Musiol, G.; Mühlig, H.:
  *Taschenbuch der Mathematik.* Edition Harri Deutsch, aktuelle
  Auflage, Kap. 3.5.4.

**Korpus (nicht autoritativ):**

- Wikipedia, Lemmata „Polyeder", „Konvexes Polytop",
  „Boundary Representation", „Constructive Solid Geometry"
  (abgerufen 2026-05-08).
