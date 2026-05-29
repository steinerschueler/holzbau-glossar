---
id: weltkoordinatensystem
benennung: Weltkoordinatensystem
synonyme: ["Globales Koordinatensystem", "Welt-CRS", "Welt-Bezugssystem"]
abgelehnte_benennungen: [Weltsystem, Globalsystem, "world coordinate system", "world frame", WCS]
oberbegriff: koordinatensystem
begriffstyp: hilfsbegriff
voraussetzungen: [koordinatensystem, punkt, vektor, einheitsvektor, toleranzen]
abgrenzung_zu: [lokales_koordinatensystem, bauteilachse, lv95, wgs84]
status: entwurf
subglossar_pendant: notwendig  # Überschreibung hilfsbegriff-Default optional → required: das globale z-oben-Rechtssystem ist Grundmodell jeder räumlichen Darstellung, bis Meister praxisrelevant (HG_KONVENTIONEN §7).
quellen_primär:
  - "ISO 19111:2019, 'Geographic information — Referencing by coordinates', insbesondere Abschnitt 4 (Terms and definitions: coordinate reference system, coordinate system, datum) und Abschnitt 7 (Coordinate systems)."
  - "DIN ISO 80000-2:2022-08, 'Größen und Einheiten – Teil 2: Mathematik', Abschnitt 2 (Geometrie und Vektoren), insbesondere zum kartesischen Koordinatensystem und zur Rechtshändigkeit."
  - "DIN EN ISO 80000-3:2020-12, 'Größen und Einheiten – Teil 3: Raum und Zeit', Abschnitt 3 (Raum), Definitionen für Länge, Koordinaten, kartesische Bezugssysteme."
  - "swisstopo (Bundesamt für Landestopografie): 'Bezugsrahmen LV95 / Koordinaten in der amtlichen Vermessung', technische Spezifikation EPSG:2056 (CH1903+/LV95). Insbesondere die Festlegung E (Easting), N (Northing) und der Höhenbezug (LN02 bzw. LHN95)."
  - "EN ISO 5459:2011, 'Geometrische Produktspezifikation (GPS) – Bezüge und Bezugssysteme', Abschnitt 5 (Bezugssysteme): Konventionen für rechtshändige kartesische Bezugssysteme in technischen Zeichnungen."
quellen_sekundär:
  - "OGC 18-005r4 (2019), 'Geographic information — Well-known text representation of coordinate reference systems', Abschnitt zu projektierten kartesischen 2D/3D-Systemen."
  - "Hofmann-Wellenhof, B.; Lichtenegger, H.; Wasle, E.: GNSS — Global Navigation Satellite Systems. Springer 2008, Kap. 2 'Reference Systems' (kartesische und ellipsoidische Bezugssysteme, Konventionen)."
  - "Snyder, J. P.: Map Projections — A Working Manual. USGS Professional Paper 1395, Washington 1987, Kap. 4 (Projektionsgrundlagen, lokale planare Approximation)."
  - "Bronstein, I. N. et al.: Taschenbuch der Mathematik. Kap. 3.5 'Analytische Geometrie des Raumes'."
  - "Lignum (Hrsg.): Lignatec — diverse Bauplanungs-Hinweise zur Lagebezugnahme von Holzbauten auf das Schweizer Landeskoordinatensystem."
quellenkonflikt: |
  Es gibt keine Holzbau-Norm (DIN 1052, DIN EN 1995-1-1, SIA 265,
  SIA 232/1, Holzbau-Deutschland-Merkblätter), die ein
  Welt-Koordinatensystem für die digitale Modellierung von
  Holzkonstruktionen festlegt. Die einschlägigen Quellen sind
  geoinformatisch (ISO 19111, swisstopo) und allgemein-mathematisch
  (DIN ISO 80000-2, EN ISO 5459).

  Konflikt 1 — Achsenzuordnung:
  EN ISO 5459 (technische Zeichnung, Bauteilebene) lässt die
  Zuordnung der Achsen zu Himmelsrichtungen offen; sie ist eine
  Modellierungskonvention. Manche CAD-Systeme verwenden y = oben,
  z = nach hinten (insbesondere ältere 3D-Tools). Diese Festlegung
  ist mit der CLAUDE.md-Vorgabe (z = oben, Rechtssystem)
  unvereinbar und wird durch eine explizite Importtransformation
  aufgelöst, nicht durch interne Mischkonventionen.

  Konflikt 2 — Winkelkonvention:
  In der Mathematik (DIN ISO 80000-2) werden ebene Winkel um die
  z-Achse gegen den Uhrzeigersinn ab +x gemessen. In der Geodäsie
  und im Schweizer Vermessungswesen (swisstopo, ISO 19111) wird das
  Azimut von Nord aus im Uhrzeigersinn gemessen. Beide Konventionen
  sind in ihrem Kontext normativ. Eigene Festlegung dieses Glossars
  (siehe Abschnitt 'Mathematische Definition'): intern gilt der
  mathematische Standard (Winkel φ ∈ [0, 2π) ab +x gegen den
  Uhrzeigersinn um e_z), das Azimut ψ wird ausschließlich als
  Anzeige- und Eingabe-Transformation am API-Rand geführt. Die
  Konversion ist ψ = (π/2 − φ) mod 2π (siehe `hg_dachseite.md` für
  einen bereits vorhandenen Anwendungsfall).

  Konflikt 3 — Längeneinheit:
  swisstopo führt LV95-Koordinaten in Metern; die Domänen-Schicht
  dieser App führt ausnahmslos Millimeter (CLAUDE.md). Diese
  Differenz wird durch die Welt-zu-Lokal-Trennung dieses Eintrags
  und einen expliziten Faktor 10³ am Importrand aufgelöst, nicht
  durch eine globale Umstellung der internen Längeneinheit.

  Diese Festlegungen sind konfliktfrei mit allen konsultierten
  Quellen, sobald sie als App-interne Konventionen (nicht als
  Aussagen über die Quellen selbst) verstanden werden.
---

## Prosa-Definition

Das **Weltkoordinatensystem** der App ist das eindeutige, global
gültige rechtshändige kartesische Bezugssystem (O, e_x, e_y, e_z) im
dreidimensionalen affinen Raum, dessen Ursprung O eine projektweit
fest gewählte Stelle in der Nähe des Bauwerks bezeichnet, dessen
x-Achse nach geographisch Ost, dessen y-Achse nach geographisch Nord
und dessen z-Achse vertikal nach oben gerichtet ist, mit Längen in
Millimeter und ebenen Winkeln um e_z intern in Radiant ab +x gegen
den Uhrzeigersinn gemessen.

## Mathematische Definition

Sei

- 𝔸³ der dreidimensionale reelle affine Raum,
- O ∈ 𝔸³ ein projektweit fest gewählter Ursprung,
- (e_x, e_y, e_z) eine Basis von ℝ³ mit den Eigenschaften
  ```
  ‖e_x‖ = ‖e_y‖ = ‖e_z‖ = 1,                      (Einheitsvektoren)
  ⟨e_x, e_y⟩ = ⟨e_y, e_z⟩ = ⟨e_z, e_x⟩ = 0,      (paarweise orthogonal)
  e_x × e_y = e_z.                                 (Rechtssystem)
  ```

Dann ist das **Weltkoordinatensystem** das Tupel

```
W := (O, e_x, e_y, e_z, η, ω),
```

wobei

- η : 𝔸³ → ℝ³ die Koordinatenabbildung
  ```
  η(p) = (x, y, z)  ⇔  p = O + x·e_x + y·e_y + z·e_z,
  ```
  ist; die Komponenten x, y, z sind in Millimeter zu interpretieren,

- ω : ℝ³ × ℝ³ → ℝ die Winkelmessung um e_z im mathematischen Sinn,
  ```
  ω(u, v) := atan2( ⟨e_z, u_hat × v_hat⟩ , ⟨u_hat, v_hat⟩ )  ∈ (−π, π],
  ```
  mit u_hat = u/‖u‖, v_hat = v/‖v‖, definiert für u, v ∉ Null der
  Toleranz `Toleranzen.NORM_EPS`. ω misst den orientierten Winkel
  von u nach v gegen den Uhrzeigersinn um e_z, in **Radiant**.

Die geographische Einbettung wird durch die zusätzliche Festlegung

```
e_x ≙ Ost,    e_y ≙ Nord,    e_z ≙ Zenit (Vertikale nach oben)
```

am Modellierungsort hergestellt. „Lokales Ost", „Lokales Nord" und
„Lokale Vertikale" beziehen sich dabei auf eine ebene
(planare) Approximation der Erdoberfläche in der Umgebung von O,
deren Genauigkeit für Bauwerksabmessungen ≤ 10⁴ mm konservativ
besser als `Toleranzen.LAENGE_EPS` ist (Krümmungsfehler ≤ 10⁻⁵ mm
auf 10 m Bauwerksspanne).

## Anzeige-Konvention: Azimut

Aus W ist eine zweite Winkelkonvention ableitbar, die ausschließlich
für Eingabe und Anzeige verwendet wird:

```
ψ : (Vektor \ vertikal) → [0, 2π),
ψ(v) := atan2( ⟨v, e_x⟩ , ⟨v, e_y⟩ )  mod 2π          (Azimut)
```

mit ψ = 0 bei Nord, ψ = π/2 bei Ost, ψ = π bei Süd, ψ = 3π/2 bei
West (Kompass-Konvention, im Uhrzeigersinn). Der Zusammenhang zum
mathematischen Winkel φ um e_z ist

```
ψ = (π/2 − φ) mod 2π,    φ = (π/2 − ψ) mod 2π.
```

ψ ist **kein eigenständiges Koordinatensystem**, sondern eine
Anzeige-Transformation; im Code wird intern ausnahmslos mit ω und φ
gerechnet. Das Azimut ψ erscheint nur an Ein- und Ausgaberändern
(z. B. `dachseite.orientierung()`).

## Wohldefiniertheit

- **Existenz**: ℝ³ mit der kanonischen Orthonormalbasis und einem
  beliebigen, projektweit gewählten Ursprung O erfüllt alle drei
  Basisbedingungen; die Existenz von W ist trivial.
- **Eindeutigkeit**: W ist als App-Konvention fest. Insbesondere ist
  es nicht erlaubt, im laufenden Betrieb des Modells den Ursprung
  oder die Achsen umzudefinieren; jede Umdefinition ist eine neue
  Welt und erfordert einen vollständigen Modellexport/-import.
- **Unabhängigkeit der Operationen von Wahl der Komponenten**: η ist
  bei festgelegter Basis eine Bijektion 𝔸³ ↔ ℝ³; alle abgeleiteten
  Operationen (Differenz, Norm, Skalarprodukt, Kreuzprodukt) sind
  unter dieser Bijektion wohldefiniert.
- **Konsistenz mit `punkt` und `vektor`**: Beide Einträge nehmen
  bereits explizit Bezug auf das in CLAUDE.md festgelegte
  Welt-Koordinatensystem; der vorliegende Eintrag fixiert das dort
  vorausgesetzte System normativ und löst die bislang implizite
  Achsenzuordnung Ost/Nord auf.
- **Konsistenz mit `dachseite`**: Der Eintrag `hg_dachseite.md`
  verwendet die Konvention e_x = Ost, e_y = Nord, e_z = oben
  bereits operativ; mit dem vorliegenden Eintrag ist diese
  Voraussetzung normativ gedeckt.
- **Numerische Stabilität bei großen Koordinaten**: Bei
  Bauwerksabmessungen ≤ 10⁴ mm und einem in Bauwerksnähe gewählten
  Ursprung liegt der absolute Rundungsfehler einer Koordinate in
  IEEE 754 binary64 weit unterhalb `Toleranzen.LAENGE_EPS`. Bei
  Bezug auf entfernte Welt-Ursprünge (z. B. unmittelbare Verwendung
  von LV95-Koordinaten mit Werten der Größenordnung 10⁹ mm) wächst
  der absolute Rundungsfehler proportional und kann
  `Toleranzen.LAENGE_EPS` überschreiten. Daraus folgt die
  Welt-zu-Lokal-Trennung dieses Eintrags.
- **Nicht-Zirkularität**: Die Definition stützt sich nur auf
  reelle Zahlen, den affinen Raum, die Primitive Punkt, Vektor,
  Einheitsvektor und auf `Toleranzen`. W kommt nicht in seiner
  eigenen Definition vor.

## Anwendung in der Schweiz: Bezug zu LV95

Das **Schweizer Landeskoordinatensystem CH1903+/LV95**
(EPSG:2056, swisstopo) ist das amtliche projizierte 2D-Bezugssystem
der Schweiz mit zwei kartesischen Komponenten

- **E (Easting)**: Ostkoordinate in Metern, Projektionsursprung so
  gewählt, dass E ≈ 2 600 000 m bei Bern liegt;
- **N (Northing)**: Nordkoordinate in Metern, N ≈ 1 200 000 m bei
  Bern.

Die Höhe wird als getrennte 1D-Komponente in den Höhenrahmen LN02
(klassisch) oder LHN95 (modern, gravimetrisch) in Metern geführt.

**Zuordnung W ↔ LV95**:

```
e_x  ≙  E-Richtung    (Ost),
e_y  ≙  N-Richtung    (Nord),
e_z  ≙  Höhe          (Vertikal),
1 m  ≙  10³ mm.
```

**Welt-zu-Lokal-Trennung**: LV95-Koordinaten mit Werten der
Größenordnung 10⁹ mm überschreiten den numerisch günstigen Bereich
für Bauteilkoordinaten (CLAUDE.md, Konvention ≤ 10⁴ mm). Daraus
folgt die normative Trennung zwischen

1. **Welt-Koordinatensystem W** (dieser Eintrag): rechtshändiges
   kartesisches System in mm mit Ursprung in **Bauwerksnähe**.
   Alle Bauteilgeometrien werden in W modelliert.

2. **Geo-Bezugssystem** (Folge-Eintrag `lv95.md`, noch nicht
   angelegt): das Schweizer Landeskoordinatensystem in Metern.
   Wird **nicht** in der Domänen-Schicht verwendet, sondern nur
   am Importrand zur Lagebezugnahme des Welt-Ursprungs.

3. **Lokales Bauteilkoordinatensystem** (Folge-Eintrag
   `hg_lokales_koordinatensystem.md`, noch nicht angelegt):
   bauteileigenes kartesisches System (z. B. Sparrenachse als
   Längsachse), das durch eine starre Transformation
   (Translation + Rotation) auf W abgebildet wird.

Die Verbindung zwischen W und LV95 wird durch eine **starre
Transformation** T_{W→LV95} : 𝔸³_W → 𝔸³_LV95 hergestellt,
bestehend aus

- einer Translation um den Welt-Ursprung O, in LV95 angegeben durch
  ein Tripel (E_O, N_O, H_O) ∈ ℝ³ in **Metern**,
- einer optionalen Drehung um e_z um einen Winkel γ ∈ [0, 2π), die
  ausgleicht, falls die Bauwerks-Hauptachse nicht
  Nord-Süd/Ost-West orientiert wurde,
- der Skalierung 1 m = 10³ mm.

Diese Transformation gehört nicht in W selbst, sondern in einen
eigenen Geo-Anker; sie wird hier nur erwähnt, um die Schichten
sauber zu trennen.

## Erläuterung (nicht normativ)

Das Welt-Koordinatensystem ist die **stillschweigende Voraussetzung
aller bisherigen Glossareinträge**. CLAUDE.md hatte sie auf zwei
Sätze („Rechtssystem, z-Achse vertikal nach oben") reduziert; mit
dem vorliegenden Eintrag wird sie auf ein Niveau gehoben, das die
Achsen-Zuordnung zu Himmelsrichtungen, die Winkelkonvention und die
Beziehung zum Schweizer Vermessungswesen abdeckt.

Der zentrale praktische Nutzen ist die **Disambiguierung von
Winkeln**. In der Mathematik dreht ein positiver Winkel um e_z
gegen den Uhrzeigersinn (von +x nach +y); in der Geodäsie dreht
ein positives Azimut von Nord aus im Uhrzeigersinn (also im
mathematischen Sinn negativ). Beide Konventionen treten in der
App auf: die mathematische intern (alle Geometrierechnungen, alle
Trigonometrie auf Vektoren), die geodätische am API-Rand (Anzeige,
Bauplanaufschrift, Eingabe einer Dachausrichtung als „Süd", „Süd-
Süd-West"). Die Trennung „intern Mathematik, extern Azimut" hält
beide Welten kollisionsfrei.

Praktisch bedeutet das: Ein in der App eingegebenes Azimut von
180° (Süd) wird sofort zu einem mathematischen Winkel
φ = (π/2 − π) mod 2π = 3π/2 = 270° konvertiert, der dann in
sämtlichen Rechnungen verwendet wird. Eine Vermischung beider
Größen führt zu Fehlern, die meist erst bei der dritten oder
vierten Verschneidung sichtbar werden — daher die strenge
Schichtentrennung.

## Beziehungen

- **Oberbegriff**: keiner. Das Weltkoordinatensystem ist eine
  Modellierungs- und Darstellungs-Konvention, kein geometrisches
  Objekt im Modell. Ein abstrakter Oberbegriff `koordinatensystem`
  würde erst sinnvoll, wenn Geschwister-Begriffe
  `lokales_koordinatensystem` und `lv95` separat definiert werden
  und ein gemeinsames Vokabular benötigen; bis dahin wird die
  Abgrenzung inline geführt.
- **Verwandte Begriffe**:
  - **Lokales Koordinatensystem**: bauteileigenes oder
    konstruktionsteilbezogenes kartesisches System, das durch eine
    starre Transformation auf W abgebildet wird; eigener Eintrag
    `hg_lokales_koordinatensystem.md` in Folgearbeit.
  - **Bauteilachse**: Längsachse eines Bauteils (z. B.
    Sparrenachse), häufige Wahl der x- oder z-Achse eines lokalen
    Systems.
- **Abgrenzung**:
  - **Lokales Koordinatensystem** (Folge-Eintrag): nur lokal an
    einem Bauteil oder Konstruktionsteil gültig, durch starre
    Transformation auf W bezogen. W ist global, lokal Systeme sind
    es nicht.
  - **Bauteilachse** (Folge-Eintrag): eine ausgezeichnete Achse
    eines Bauteils, nicht ein vollständiges Koordinatensystem. Eine
    Bauteilachse kann eine Achse eines lokalen Systems sein, ist
    aber kein Synonym dafür.
  - **LV95 (CH1903+)** (Folge-Eintrag `lv95.md`): amtliches
    Schweizer Landeskoordinatensystem in Metern, projiziert.
    LV95 wird in der Domänen-Schicht **nicht** als Welt-System
    verwendet, sondern nur als externer Bezug am Importrand.
  - **WGS84** (Folge-Eintrag `wgs84.md`): geographisches
    ellipsoidisches Bezugssystem; nicht kartesisch und nicht
    projiziert. Wird in der App nur über GPS/GNSS-Importschnitt-
    stellen berührt und nicht intern verwendet.
  - **Maßtoleranz, Numerik-Toleranz**: andere Begriffsdomäne,
    keine Konkurrenz zu W.

## Implementierungshinweis

Datentyp und Konvention (Domänen-Schicht, Kotlin, Schicht
`zimmermann.domain.koordinaten`):

```
package zimmermann.domain.koordinaten

import zimmermann.domain.geometrie.Einheitsvektor
import zimmermann.domain.geometrie.Punkt
import kotlin.math.PI

/**
 * Welt-Koordinatensystem der App.
 * Glossar: hg_weltkoordinatensystem.md
 *
 * Konvention (normativ):
 *   - Rechtshändig, kartesisch, ortsfest.
 *   - e_x = Ost, e_y = Nord, e_z = vertikal nach oben.
 *   - Längeneinheit: mm (Double).
 *   - Winkel um e_z intern: Radiant, ab +x gegen den Uhrzeigersinn.
 *
 * Es gibt nur EIN Weltsystem zur Laufzeit. Dieser Typ ist deshalb
 * ein Marker-Objekt; konkrete Punkte/Vektoren in W werden durch
 * die Typen Punkt bzw. Vektor dargestellt, deren Komponenten
 * implizit auf W bezogen sind.
 */
object Weltkoordinatensystem {

    /** Ursprung O, projektweit fest gewählt. */
    val URSPRUNG: Punkt = Punkt.URSPRUNG

    /** e_x, Einheitsvektor in Ost-Richtung. */
    val EX: Einheitsvektor = Einheitsvektor.EX

    /** e_y, Einheitsvektor in Nord-Richtung. */
    val EY: Einheitsvektor = Einheitsvektor.EY

    /** e_z, Einheitsvektor in Vertikal-Richtung (nach oben). */
    val EZ: Einheitsvektor = Einheitsvektor.EZ

    /**
     * Konvertiert ein geodätisches Azimut ψ (Kompass-Konvention:
     * 0 = Nord, π/2 = Ost) in den mathematischen Winkel φ um e_z
     * (ab +x gegen den Uhrzeigersinn). Normative Konversion gemäß
     * Glossar: φ = (π/2 − ψ) mod 2π. Auf ganz ℝ definiert
     * (Modulo-Reduktion); Resultat in [0, 2π).
     * Glossar: weltkoordinatensystem#anzeige-konvention-azimut.
     */
    fun azimutZuMathematischemWinkel(azimut: Double): Double = ...

    /**
     * Konvertiert den mathematischen Winkel φ um e_z in ein
     * geodätisches Azimut ψ. Inverse zu
     * [azimutZuMathematischemWinkel] modulo 2π. Resultat in [0, 2π).
     * Glossar: weltkoordinatensystem#anzeige-konvention-azimut.
     */
    fun mathematischerWinkelZuAzimut(phi: Double): Double = ...
}
```

**Implementiert** (Stand D5-1, Code-Realität in
`zimmermann.domain.koordinaten.Weltkoordinatensystem`):

- `URSPRUNG`, `EX`, `EY`, `EZ` als delegierte Konstanten an
  `Punkt.URSPRUNG` bzw. `Einheitsvektor.EX/EY/EZ` — keine
  Wert-Duplikation, kein Drift-Risiko. Die Typsignatur
  `Einheitsvektor` (statt `Vektor`) trägt die Norm-Invariante
  `‖e_i‖ = 1` durch das Typsystem.
- `azimutZuMathematischemWinkel(azimut: Double): Double` und
  `mathematischerWinkelZuAzimut(phi: Double): Double` als die
  einzigen erlaubten Übergangs-Stellen zwischen Anzeige-Azimut ψ
  und interner mathematischer Winkel-Konvention φ. Beide Funktionen
  sind auf ganz ℝ total (Modulo-Reduktion auf [0, 2π)),
  propagieren NaN/±∞ gemäß IEEE-754, werfen niemals.
- Konstanten `LAENGENEINHEIT = "mm"` und `WINKELEINHEIT = "rad"`
  als API-lesbare Marker der Domänen-Schicht-Konventionen.

**Trigger-basierte Folgearbeit** (siehe
`feedback_trigger_basierte_tasks.md`):

- `winkelUmZ(u: Vektor, v: Vektor): Double?` — orientierter
  mathematischer Winkel von u nach v um e_z, mit `Entartet`-Fall
  bei zu kurzen Vektoren. **Trigger**: wenn eine Domänen-Operation
  einen orientierten Winkel zweier Vektoren um die Vertikale
  benötigt (z. B. Verschneidungsberechnung mit zwei
  Dachseiten-Normalen).
- `azimut(v: Vektor): Double?` — Azimut eines 3D-Vektors via
  Horizontalprojektion auf die x-y-Ebene, mit `Entartet`-Fall bei
  vertikalen Vektoren (Horizontalprojektion zu kurz). **Trigger**:
  wenn ein Tool die Berechnung des Azimuts aus einem 3D-Vektor mit
  Horizontalprojektion verlangt (z. B. Anzeige der
  Dachseiten-Orientierung als Kompass-Wert aus der Normalen).

- **Einheit**: Längen in mm (Double); Winkel intern in Radiant
  (Double); Anzeige in Grad. Niemals Mischung in einer Funktion.
- **Konvention der Achsen**: `EX = Ost`, `EY = Nord`, `EZ = oben`.
  Diese Zuordnung wird in der gesamten Domänen-Schicht
  vorausgesetzt und nicht parametrisiert. CAD-Importe mit
  abweichender Konvention (z. B. y = oben) werden im Importrand
  durch eine explizite Achsenrotation auf W abgebildet, nicht
  durch eine alternative Welt-Konfiguration.
- **Konvention der Winkelmessung**: intern ausnahmslos
  mathematisch (φ ∈ (−π, π] bzw. [0, 2π) ab +x gegen den
  Uhrzeigersinn um e_z). Das Azimut ψ ist eine reine
  Darstellungs- und Eingabe-Transformation am API-Rand. Gemischte
  Verwendung in einer Funktion ist verboten. Bestehende Glossar-
  einträge, die ψ produzieren (z. B. `dachseite.orientierung()`),
  müssen ψ explizit benennen und nicht als „Winkel" simpliciter.
- **Welt-zu-Lokal-Trennung**: Bauteilkoordinaten in mm bezüglich W
  mit Ursprung in **Bauwerksnähe**. LV95-Importe werden über einen
  Geo-Anker (Translation + ggf. Drehung um e_z, Skalierung
  1 m = 10³ mm) auf W abgebildet. LV95-Koordinaten dürfen
  **nicht** roh als Bauteilkoordinaten verwendet werden.
- **Invarianten**:
  1. `EX × EY = EZ` (Rechtssystem-Bedingung). **Strukturell
     garantiert** durch Delegation an `Einheitsvektor.EX/EY/EZ`
     im `geometrie`-Sub-Package — die Rechtssystem-Eigenschaft ist
     im Vektor-Test (`VektorTest`) bereits durchgängig geprüft.
     Im `WeltkoordinatensystemTest` zusätzlich als Konsistenz-Check
     auf der Welt-Konventions-Ebene wiederholt.
  2. Es existiert genau ein Welt-Objekt zur Laufzeit. Daraus folgt
     die Modellierung als Kotlin-`object`, nicht als `class`.
- **Edge Cases**:
  - **Entartete Basis** (eine Achse linear abhängig von den
    anderen, oder Linkssystem): in der aktuellen Implementierung
    **strukturell unmöglich**, weil `EX/EY/EZ` an die normierten
    `Einheitsvektor`-Konstanten delegieren — eine entartete Basis
    kann nicht erzeugt werden. Der `Entartet.UngueltigesSystem`-Fall
    ist deshalb keine reale Variante in `EntartetGeometrie` und
    bleibt nur als Folgearbeit erwähnt: falls die App später
    benutzerdefinierte Welt-Koordinatensysteme zulässt (z. B.
    nicht-rechtshändige Subsysteme für Spezial-Anwendungen),
    müsste eine entsprechende Variante in `EntartetGeometrie`
    eingeführt und der Konstruktor mit `Resultat`-Wrapping
    versehen werden.
  - **Sehr großer Welt-Ursprung-Versatz** (z. B. unmittelbarer
    Bezug zu LV95): wird durch die Welt-zu-Lokal-Trennung
    abgefangen. Wenn dennoch ein Modell mit Koordinaten ≫ 10⁶ mm
    erstellt wird, ist die Annahme `LAENGE_EPS = 10⁻³ mm` zu
    überprüfen (siehe `hg_toleranzen.md`).
  - **Dauerlauf-Drift / Zeitabhängigkeit**: W ist zeitlich
    konstant. Plattenbewegung, Gezeiten, Erdrotation und sonstige
    geophysikalische Effekte sind für Holzbau-Bauwerke (Spanne
    ≤ 10⁴ mm, Lebensdauer ≤ 10² Jahre) deutlich kleiner als
    `Toleranzen.LAENGE_EPS` und werden nicht modelliert.
- **Verwendungsregel**: Funktionen, die Punkte oder Vektoren
  entgegennehmen, gehen ohne weitere Annotation davon aus, dass
  diese in W gegeben sind. Bauteil- und Lokalkoordinaten erhalten
  einen eigenen Wrapper-Typ (z. B. `BauteilLokal<T>`) mit
  expliziter `nachWelt(transformation)`-Operation; eine implizite
  Reinterpretation von Komponenten ist verboten (siehe `hg_punkt.md`).

## Quellen

**Primär (normativ):**

- ISO 19111:2019, „Geographic information — Referencing by
  coordinates".
- DIN ISO 80000-2:2022-08, „Größen und Einheiten – Teil 2:
  Mathematik".
- DIN EN ISO 80000-3:2020-12, „Größen und Einheiten – Teil 3:
  Raum und Zeit".
- swisstopo (Bundesamt für Landestopografie): „Bezugsrahmen
  LV95 / Koordinaten in der amtlichen Vermessung", technische
  Spezifikation EPSG:2056 (CH1903+/LV95) inkl. Höhenrahmen LN02
  und LHN95.
- EN ISO 5459:2011, „Geometrische Produktspezifikation (GPS) –
  Bezüge und Bezugssysteme".

**Sekundär:**

- OGC 18-005r4 (2019), „Geographic information — Well-known text
  representation of coordinate reference systems".
- Hofmann-Wellenhof, B.; Lichtenegger, H.; Wasle, E.: *GNSS —
  Global Navigation Satellite Systems.* Springer 2008.
- Snyder, J. P.: *Map Projections — A Working Manual.* USGS
  Professional Paper 1395, Washington 1987.
- Bronstein, I. N. et al.: *Taschenbuch der Mathematik*,
  Kap. 3.5 „Analytische Geometrie des Raumes".
- Lignum (Hrsg.): *Lignatec* — Bauplanungs-Hinweise zur
  Lagebezugnahme von Holzbauten.

**Nur in der Abgrenzung referenziert (nicht als Definitionsquelle):**

- WGS84 (NGA Standardization Document NGA.STND.0036_1.0.0_WGS84,
  2014): geographisches ellipsoidisches Bezugssystem; in dieser
  App nur über GPS-Importrand berührt.

**Korpus (nicht autoritativ):**

- Wikipedia, Lemmata „Koordinatensystem", „Schweizer
  Landeskoordinaten", „LV95", „CH1903+" (abgerufen 2026-05-08).
