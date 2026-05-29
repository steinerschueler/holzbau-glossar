---
id: strecke
benennung: Strecke
synonyme: [Linienstück, "geschlossene Strecke", "abgeschlossene Strecke"]
abgelehnte_benennungen: [Linie, Gerade, Segment, "line segment"]
oberbegriff: null
begriffstyp: primitiv
voraussetzungen: [punkt, vektor]
abgrenzung_zu: [gerade, halbgerade, kante, polygon]
status: entwurf
subglossar_pendant: notwendig
quellen_primär:
  - "DIN ISO 80000-2:2022-08, Abschnitt 2 (Geometrie), Bezeichnungen für Strecken."
  - "DIN EN ISO 129-1:2022-02, 'Technische Produktdokumentation (TPD) — Angabe von Maßen und Toleranzen — Teil 1: Grundlagen', §3.2.4 (Begriff 'Längenmaß' / linear dimension; Bemaßungs-Sicht als ISO-129-1-Pendant zur didaktischen 'Maßstrecke'). [einsicht: vorschau-pdf, Inhaltsverz.]"
  - "DIN EN ISO 14405-1:2017-07, 'Geometrische Produktspezifikation (GPS) — Dimensionelle Tolerierung — Teil 1: Lineare Größenmaße' (Begriff 'Lineares Größenmaß'; Tolerierungs-Sicht: Abstand gegenüberliegender paralleler Geraden/Ebenen)."
quellen_sekundär:
  - "Bronstein, I. N. et al.: Taschenbuch der Mathematik. Kap. 3.5.1 'Geraden und Strecken im Raum'."
  - "Bär, C.: Elementargeometrie. Springer Spektrum, Kap. 1 'Punkte und Strecken'."
  - "Hodgson, F. T.: The Steel Square. Industrial Publication Co., New York 1903 (Bd. 1, Kap. 1) – Verwendung des Streckenbegriffs im Zimmererhandwerk."
  - "Springer, Trägerlehre (Lehrbuch-Kapitel) — Stabachse als Idealisierung eines Stabbauteils mit dominanter Längsdimension auf seine Schwerlinie."
  - "ingenieurkurse.de, Baustatik 1+2, Lemma 'Stabtragwerke' — gleichlautende Idealisierungs-Aussage in der Hochschul-Lehre."
quellenkonflikt: |
  Holzbau-Normen verwenden den Begriff Strecke, ohne ihn zu definieren
  (z. B. „Stablänge", „Sparrenlänge"). DIN ISO 80000-2 listet das
  Symbol für die Strecke AB, ohne die Strecke axiomatisch zu
  definieren. Eigene Festlegung: eine Strecke ist die abgeschlossene,
  konvexe Hülle zweier Punkte, äquivalent das Bild des Einheits-
  intervalls unter der affinen Abbildung t ↦ (1−t)·a + t·b. Diese
  Festlegung ist konsistent mit Bronstein und Bär und mit allen
  Holzbau-Quellen.

  Zur Bemaßungs-/Tolerierungs-Terminologie: Die früher zitierte
  DIN 406-10:1992-12 ist zurückgezogen; sie führt „Maßstrecke" nicht
  als definierten Begriff. Die normativen deutschen Termini für die
  Strecke in technischer Zeichnung und Tolerierung sind heute
  „Längenmaß" (DIN EN ISO 129-1:2022-02 §3.2.4, Bemaßungs-Sicht)
  und „Lineares Größenmaß" (DIN EN ISO 14405-1:2017-07,
  Tolerierungs-Sicht). „Maßstrecke" ist im DACH-Holzbau-Korpus ein
  didaktischer Sprachgebrauch ohne Norm-Definition; dieser HG-Eintrag
  übernimmt ihn deskriptiv im Body, aber nicht als Norm-Beleg. Eigene
  HG-Einträge für `laengenmass` und `lineares_groessenmass` sind als
  Folgearbeit vorgesehen.
---

## Prosa-Definition

Eine **Strecke** ist die abgeschlossene, geradlinige Verbindung
zweier verschiedener Punkte a, b ∈ ℝ³, bestehend aus a, b und allen
Punkten, die echt zwischen a und b auf der Verbindungsgeraden liegen;
sie hat eine endliche, positive euklidische Länge.

## Mathematische Definition

Sei

- a ∈ ℝ³ der **Anfangspunkt**,
- b ∈ ℝ³ der **Endpunkt**,
- a ≠ b (Nicht-Entartungsbedingung).

Dann ist die **Strecke** [a, b] definiert als die abgeschlossene
konvexe Hülle von {a, b}:

```
[a, b] := { (1 − t)·a + t·b ∈ ℝ³ | t ∈ [0, 1] }
       = { a + t·(b − a) | t ∈ [0, 1] }.
```

Wesentliche abgeleitete Größen:

- **Richtungsvektor**: r := b − a ∈ ℝ³ \ {0}.
- **Länge**: ℓ([a, b]) := ‖b − a‖ ∈ ℝ_{>0} (in mm).
- **Mittelpunkt**: m := ½·(a + b).
- **Einheits-Richtung**: e_hat := r / ‖r‖ ∈ S².

Die Strecke ist **ungeordnet**, wenn nur ihre Punktmenge zählt
(dann gilt [a, b] = [b, a]); sie ist **geordnet** (orientiert),
wenn die Reihenfolge (a, b) als Teil der Strecke betrachtet wird
(dann gilt [a, b] ≠ [b, a]). Die Domänen-Schicht modelliert die
geordnete Variante als Standard.

## Wohldefiniertheit

- Existenz und Eindeutigkeit: Für jedes Paar (a, b) ∈ ℝ³ × ℝ³ mit
  a ≠ b ist die Menge { (1 − t)·a + t·b | t ∈ [0, 1] } eindeutig
  bestimmt.
- Unabhängigkeit von der Parametrisierung: Die definierte Punkt-
  menge ist invariant unter Reparametrisierungen t ↦ φ(t) mit
  φ: [0, 1] → [0, 1] streng monoton bijektiv. Insbesondere liefert
  die Vertauschung (a, b) ↔ (b, a) dieselbe Punktmenge bei
  ungeordneter Lesart, die orientierte Variante hingegen die
  entgegengesetzt orientierte Strecke.
- Wohldefiniertheit der Länge: ‖b − a‖ hängt nicht von der Wahl
  des Repräsentanten ab und erfüllt ‖b − a‖ = ‖a − b‖, ist also
  insbesondere unabhängig von der Orientierung.
- Nicht-Zirkularität: Die Definition stützt sich nur auf Punkt,
  Vektor und reelles Intervall.

## Erläuterung (nicht normativ)

Eine Strecke ist die einfachste eindimensionale geometrische Figur
mit endlicher Ausdehnung. Im Zimmererhandwerk treten Strecken auf
als

- Bauteilachsen (Sparrenachse, Pfettenachse),
- Bauteilkanten (Sparrenoberkante, Trauflinie),
- Hilfslinien beim Anriss,
- bemaßte Strecken in der technischen Zeichnung — im didaktischen
  DACH-Lehr-Korpus auch „Maßstrecke" genannt; in der Norm-
  Terminologie heißen die einschlägigen Begriffe „Längenmaß"
  (DIN EN ISO 129-1, Bemaßungs-Sicht) bzw. „Lineares Größenmaß"
  (DIN EN ISO 14405-1, Tolerierungs-Sicht).

Sie ist von der **Geraden** (unbegrenzt) und der **Halbgeraden**
(einseitig begrenzt) durch ihre beidseitige Begrenzung unterschieden.
Eine **Kante** eines Bauteils ist eine Strecke in einer
spezialisierten Rolle; sie ist als Begriff abgeleitet, nicht
fundamental.

**Stab- und Bauteilachse als Idealisierung.** In der Tragwerks-
Theorie wird ein Stabbauteil mit einer wesentlich größeren
Dimension (Länge) gegenüber den beiden anderen (Querschnitts-
abmessungen) auf seine Schwerlinie reduziert — eine Strecke vom
Stab-Anfang zum Stab-Ende, genannt **Stab-** oder **Bauteilachse**.
Dieser Reduktionsschritt ist der Übergang vom 3D-Volumen-Bauteil
zum 1D-Stabmodell und damit eine der grundlegenden Idealisierungen,
mit denen das Strecken-Primitiv im Holzbau seine konstruktive
Wirkung entfaltet.

## Beziehungen

- **Oberbegriff**: kompakte konvexe Hülle zweier Punkte (formal),
  bzw. eindimensionales Linienstück mit endlichen Endpunkten.
- **Teilbegriffe (Spezialisierungen)**:
  - **Kante** (eines Polygons oder Bauteils): rollenbezogene
    Spezialisierung; eigene Einträge.
  - **Achse** (eines Stabbauteils): rollenbezogene Spezialisierung;
    eigener Eintrag.
- **Bestandteile (partitiv)**:
  - Anfangspunkt a, Endpunkt b, innere Punkte (a, b) (offenes Inneres).
- **Abgrenzung**:
  - **Gerade**: { a + t·r | t ∈ ℝ }, unbegrenzt in beide Richtungen.
  - **Halbgerade (Strahl)**: { a + t·r | t ∈ [0, ∞) }, einseitig
    begrenzt.
  - **Polygon**: aus mehreren Strecken (Kanten) zusammengesetzt;
    ein Polygon mit zwei Eckpunkten ist degeneriert und wird in
    diesem Glossar nicht als Polygon, sondern als Strecke geführt.
  - **Vektor**: ortsfrei, beschreibt nur Richtung und Länge; eine
    Strecke ist die ortsgebundene Realisierung eines Vektors
    zwischen zwei festen Punkten.

## Implementierungshinweis

Datentyp (Domänen-Schicht, Kotlin, Schicht `domain.geometrie`):

```
data class Strecke(
    val anfang: Punkt,
    val ende: Punkt
) {
    init {
        // ‖ende − anfang‖ > Toleranzen.LAENGE_EPS, sonst Entartet
    }
}
```

- **Einheit**: Endpunkt-Koordinaten in mm (Double); Länge in mm.
- **Invarianten** (in `init` oder `Strecke.of(...)` -Factory prüfen,
  bei Verletzung `Entartet`-Variante zurückgeben, niemals
  Exception):
  1. ‖ende − anfang‖ > Toleranzen.LAENGE_EPS.
  2. Alle Komponenten von `anfang` und `ende` finit (kein NaN, kein ±∞).
- **Orientierung**: Die Datenklasse ist geordnet (anfang ≠ ende
  unterscheidet sich von ende ≠ anfang). Für ungeordnete
  Vergleiche steht `gleichUngeordnet(other, eps)` bereit.
- **Edge Cases**:
  - `anfang ≈ ende` (innerhalb Toleranz): `Entartet.NullStrecke`.
  - Nicht-finite Koordinaten: `Entartet.NichtFinit`.
  - Sehr kurze Strecken (knapp über Toleranz): zulässig, aber
    Richtungsableitungen wie e_hat = (b − a)/‖b − a‖ sind numerisch
    sensibel; die Domänen-Schicht warnt im Test, nicht zur Laufzeit.
- **Abgeleitete Operationen** (in `StreckeOps.kt`):
  - `fun laenge(): Double` = ‖ende − anfang‖
  - `fun richtung(): Vektor` = ende − anfang
  - `fun einheitsRichtung(): Resultat<Vektor, EntartetGeometrie>` (Fehler bei
    NullStrecke)
  - `fun mittelpunkt(): Punkt` = (anfang + ende − O) / 2 ... O.h.
    `Punkt((a.x+b.x)/2, …)`
  - `fun punktAuf(t: Double): Punkt` für t ∈ [0, 1] mit
    Klemmung/Validierung außerhalb.
  - `fun umkehren(): Strecke` = Strecke(ende, anfang).

## Quellen

**Primär (normativ):**

- DIN ISO 80000-2:2022-08, „Größen und Einheiten – Teil 2:
  Mathematik".
- DIN EN ISO 129-1:2022-02, „Technische Produktdokumentation (TPD)
  — Angabe von Maßen und Toleranzen — Teil 1: Grundlagen", §3.2.4
  („Längenmaß" / linear dimension).
- DIN EN ISO 14405-1:2017-07, „Geometrische Produktspezifikation
  (GPS) — Dimensionelle Tolerierung — Teil 1: Lineare Größenmaße"
  („Lineares Größenmaß").

**Sekundär:**

- Bronstein, I. N.; Semendjajew, K. A.; Musiol, G.; Mühlig, H.:
  *Taschenbuch der Mathematik.*
- Bär, C.: *Elementargeometrie.* Springer Spektrum.
- Hodgson, F. T.: *The Steel Square.* Industrial Publication Co.,
  New York 1903.
- Springer, *Trägerlehre* (Lehrbuch-Kapitel) — Stabachse als
  Idealisierung eines Stabbauteils auf seine Schwerlinie
  (Tier Mittel-Hoch).
- ingenieurkurse.de, *Baustatik 1+2*, Lemma „Stabtragwerke" —
  Idealisierungs-Aussage in Hochschul-Lehre (Tier Mittel).

**Korpus (nicht autoritativ):**

- Wikipedia, Lemma „Strecke (Geometrie)" (abgerufen 2026-05-07).
- Quality-Office-Schulungsskript zu DIN EN ISO 14405 (Tier Mittel)
  — deskriptive Verwendung von „Lineares Größenmaß" im DACH-
  Lehr-Korpus.
- DACH-Holzbau-Lehr-Korpus, deskriptive Verwendung des Wortes
  „Maßstrecke" als didaktischer Begriff ohne Norm-Definition
  (siehe Drift-Befund D10 in `hauptglossar/ABWEICHUNGEN.md`).
