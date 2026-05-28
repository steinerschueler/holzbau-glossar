---
id: punkt
benennung: Punkt
synonyme: [Ortspunkt, "Punkt im Raum"]
abgelehnte_benennungen: [Stelle, Position, "point"]
oberbegriff: null
begriffstyp: primitiv
voraussetzungen: [toleranzen]
abgrenzung_zu: [vektor, koordinatensystem]
status: entwurf
theorie_pflichtig: required
quellen_primär:
  - "DIN ISO 80000-2:2022-08, 'Größen und Einheiten – Teil 2: Mathematik', Abschnitt 2 (Geometrie und Vektoren)."
  - "ISO 80000-2:2019, Symbole und Bezeichnungen für Punkte und Vektoren im affinen Raum."
quellen_sekundär:
  - "Bronstein, I. N.; Semendjajew, K. A.; Musiol, G.; Mühlig, H.: Taschenbuch der Mathematik. 12. Aufl., Europa-Lehrmittel/Harri Deutsch, Edition Harri Deutsch 2024, Kap. 3.5 'Analytische Geometrie des Raumes'."
  - "Bär, C.: Elementare Differentialgeometrie. 2. Aufl., de Gruyter 2010, Kap. 1 'Affiner Raum'."
  - "Berger, M.: Geometry I. Springer 1987, §2 'Affine spaces'."
quellenkonflikt: |
  Im DIN-Korpus des Holzbaus (DIN 1052, DIN EN 1995-1-1, SIA 265,
  Holzbau-Deutschland-Merkblätter) wird der Begriff Punkt vorausgesetzt
  und nicht definiert. Eigene Festlegung: ein Punkt ist ein Element
  des affinen Raumes ℝ³, repräsentiert durch ein Tripel reeller
  Koordinaten in mm bezüglich des in CLAUDE.md festgelegten
  Weltkoordinatensystems (Rechtssystem, z-Achse vertikal nach oben).
  Diese Festlegung ist mathematisch Standard (Bronstein, Bär) und
  konfliktfrei mit allen konsultierten Holzbau-Quellen.
---

## Prosa-Definition

Ein **Punkt** ist ein Element des dreidimensionalen affinen Raumes
ℝ³, das eine eindeutige Stelle im Weltkoordinatensystem bezeichnet
und durch ein geordnetes Tripel reeller Koordinaten (x, y, z) ∈ ℝ³
in der Längeneinheit Millimeter dargestellt wird.

## Mathematische Definition

Sei

- 𝔸³ der dreidimensionale reelle affine Raum,
- (O, e_x, e_y, e_z) das in CLAUDE.md festgelegte Welt-Koordinatensystem
  mit Ursprung O ∈ 𝔸³ und kanonischer rechtshändiger
  Orthonormalbasis (e_x, e_y, e_z), wobei e_z vertikal nach oben weist.

Dann ist ein **Punkt** p ∈ 𝔸³ eindeutig charakterisiert durch sein
Koordinatentripel

```
p ↔ (x, y, z) ∈ ℝ³  mit  p = O + x·e_x + y·e_y + z·e_z.
```

Die Koordinaten sind in Millimeter zu interpretieren: x, y, z ∈ ℝ
mit Einheit mm.

## Wohldefiniertheit

- Eindeutigkeit der Koordinaten: Bei festem Koordinatensystem
  (O, e_x, e_y, e_z) ist die Abbildung p ↔ (x, y, z) eine Bijektion.
- Unabhängigkeit von der Wahl des Repräsentanten: trivial, da
  Punkte im verwendeten Datenmodell genau durch ihr Koordinatentripel
  repräsentiert werden.
- Nicht-Zirkularität: Die Definition verwendet ausschließlich die
  Primitive reelle Zahl, affiner Raum und das festgelegte
  Koordinatensystem.

## Erläuterung (nicht normativ)

Ein Punkt ist die Abstraktion einer „Stelle im Raum" ohne Ausdehnung.
In der Holzkonstruktion sind Punkte typischerweise Eckpunkte von
Bauteilen (Sparrenfußpunkt, Firstpunkt, Anschlusspunkte), Schnitt-
punkte von Geraden (Verschneidungspunkte) oder ausgewiesene
Markierungspunkte (Anriss, Bezugspunkt).

Der Unterschied zwischen Punkt und Vektor ist konzeptionell
fundamental: ein Punkt benennt eine Stelle, ein Vektor eine gerichtete
Verschiebung. Punkte können nicht addiert werden, wohl aber Punkt +
Vektor → Punkt und Punkt − Punkt → Vektor.

## Beziehungen

- **Oberbegriff**: keiner; Punkt ist mathematisches Primitiv des
  Glossars.
- **Teilbegriffe (Spezialisierungen)**: keine im engeren Sinne;
  rollenbezogene Bezeichnungen wie Eckpunkt, Stützpunkt,
  Schnittpunkt, Fußpunkt sind Verwendungen, keine Subtypen.
- **Abgrenzung**:
  - **Vektor** (eigener Eintrag): Element des Tangentialraums ℝ³ am
    affinen Raum, repräsentiert eine gerichtete Verschiebung. Ein
    Vektor hat keine Stelle; ein Punkt hat keine Richtung.
  - **Koordinatentripel**: ein Punkt ist nicht das Tripel (x, y, z),
    sondern wird durch dieses Tripel bezüglich eines festgelegten
    Koordinatensystems repräsentiert.

## Implementierungshinweis

Datentyp (Domänen-Schicht, Kotlin, Schicht `domain.geometrie`):

```
data class Punkt(
    val x: Double,   // mm
    val y: Double,   // mm
    val z: Double    // mm
)
```

- **Einheit**: Millimeter (Double) in allen drei Komponenten.
- **Koordinatensystem**: Weltkoordinatensystem aus CLAUDE.md
  (rechtshändig, z-Achse vertikal nach oben). Lokale Koordinaten
  werden durch eigene Datentypen (z. B. `BauteilLokal`) und
  explizite Transformationen abgebildet, niemals durch implizite
  Reinterpretation der Komponenten.
- **Invarianten**: keine (jedes Tripel reeller Zahlen ist ein
  zulässiger Punkt). NaN- und Unendlichkeits-Werte sind im
  Konstruktor zugelassen; Aufrufer prüft Finitheit über
  `istFinit()`. Eine entartete Variante
  `EntartetGeometrie.NichtFinit` greift erst in nachgelagerten
  Operationen wie z. B. `Strecke.ausPunkten`.
- **Edge Cases**:
  - Sehr große Beträge (> 10⁹ mm = 1000 km): zulässig, aber numerisch
    gefährdet; Hinweis im Domain-Test.
  - Gleichheitstest: ausschließlich mit Toleranz, niemals mit
    `==`. Konvention: `p.gleich(q, eps = Toleranzen.LAENGE_EPS)`
    bedeutet ‖p − q‖ ≤ eps. Der kanonische Default-Wert für
    `LAENGE_EPS` (1e-3 mm = 1 µm) ist in `hg_toleranzen.md` festgelegt.
  - NaN/±∞ in einer Komponente: nicht im Konstruktor abgelehnt,
    sondern über `istFinit()` prüfbar; nachgelagerte Operationen
    liefern `EntartetGeometrie.NichtFinit`.
- **Abgeleitete Operationen** (in eigener Datei `PunktOps.kt`):
  - `operator fun Punkt.minus(q: Punkt): Vektor` (Punkt − Punkt)
  - `operator fun Punkt.plus(v: Vektor): Punkt` (Punkt + Vektor)
  - `infix fun Punkt.abstand(q: Punkt): Double` (‖p − q‖, mm)

## Quellen

**Primär (normativ):**

- DIN ISO 80000-2:2022-08, „Größen und Einheiten – Teil 2: Mathematik".
- ISO 80000-2:2019, „Quantities and units – Part 2: Mathematics".

**Sekundär:**

- Bronstein, I. N.; Semendjajew, K. A.; Musiol, G.; Mühlig, H.:
  *Taschenbuch der Mathematik.* Edition Harri Deutsch, aktuelle
  Auflage, Kap. 3.5 „Analytische Geometrie des Raumes".
- Bär, C.: *Elementare Differentialgeometrie.* 2. Aufl., de Gruyter,
  Berlin 2010.
- Berger, M.: *Geometry I.* Springer, Berlin 1987.

**Korpus (nicht autoritativ):**

- Wikipedia, Lemma „Punkt (Geometrie)" (abgerufen 2026-05-07).
