---
id: lineares_groessenmass
benennung: Lineares Größenmaß
synonyme: ["lineares Maß einer Größe", "lineares Größenmerkmal"]
abgelehnte_benennungen: [Größenmaß, "linear size", "linear size dimension", "size dimension"]
oberbegriff: laengenmass
begriffstyp: merkmal
voraussetzungen: [laengenmass, strecke, ebene, gerade]
abgrenzung_zu: [laengenmass, gps, toleranzfeld, masstoleranz_din18202]
status: entwurf
subglossar_pendant: optional  # Begründung (Abweichung vom Normalfall notwendig): GPS-Tolerierungs-Begriff, in unterer Stufen-Didaktik nicht zentral; Code-Pendant Folgearbeit (HG_KONVENTIONEN §7).
quellen_primär:
  - "DIN EN ISO 14405-1:2017-07, 'Geometrische Produktspezifikation (GPS) — Dimensionelle Tolerierung — Teil 1: Lineare Größenmaße', Abschnitt 3 (Begriffe) und Abschnitt 4 (lineare Größenmaße)."
quellen_sekundär:
  - "Quality-Office-Schulungsskript 'GPS – Lineare Größenmaße nach DIN EN ISO 14405-1' (Stand 09-2024) — Aufzählung der vier toleranzfähigen Form-Element-Paare (Zylinder, Kugel, Kreis, Torus / parallele Geraden / parallele Ebenen)."
  - "Henzold, G.: Form und Lage. 4. Aufl., Beuth Verlag, Berlin — Kap. zur GPS-Systematik und zum Größenmaß-Begriff."
quellenkonflikt: |
  Die GPS-Systematik (Geometric Product Specification) ist im
  englischen Original „linear size", in der deutschen Übernahme von
  ISO 14405-1 als „lineares Größenmaß" geführt. Die nackte Form
  „Größenmaß" ist im DACH-Korpus mehrdeutig: sie wird teils für
  alle Größen-tolerierbaren Maße (auch Winkel, Lagen) verwendet,
  teils strikt für lineare Maße. DIN EN ISO 14405-1:2017-07
  spezifiziert die lineare Variante; dieser Eintrag übernimmt die
  Norm-Benennung „lineares Größenmaß" und führt „Größenmaß" in
  `abgelehnte_benennungen:`, weil die Spezifikation explizit auf
  „linear" eingeschränkt ist (winkliges Größenmaß ist Teil 2 der
  ISO 14405-Reihe und nicht Gegenstand dieses Eintrags).

  „GPS" und „Toleranzfeld" sind etablierte Korpus-Begriffe (HG-
  Konventions-Datei §6.D), erhalten in diesem Glossar **keinen
  eigenen Eintrag**, weil die App holzbau-zentriert ist und die
  GPS-Tolerierung im Holzbau nur in Sonderfällen (z. B. Stahl-
  Verbinder, CNC-gefräste Verbindungsmittel) auftritt. Der
  Forward-Verweis in `abgrenzung_zu:` ist daher dauerhaft.
---

## Prosa-Definition

Ein **lineares Größenmaß** ist ein Längenmaß zwischen zwei
gegenüberliegenden Features eines Form-Elements im Sinne der
GPS-Systematik, das mit einem Toleranzfeld versehen werden kann und
nach DIN EN ISO 14405-1 in einer der vier Form-Element-Konstellationen
auftritt: Durchmesser an Zylinder, Kugel, Kreis oder Torus; Abstand
zweier einander gegenüberliegender paralleler Geraden; Abstand zweier
einander gegenüberliegender paralleler Ebenen.

## Mathematische Definition

Sei

- F = (F₁, F₂) ein **Form-Element-Paar** bestehend aus zwei
  gegenüberliegenden Bezugs-Features im Sinne der vier folgenden
  Fälle (DIN EN ISO 14405-1, Abschnitt 4):

  - **Fall A (Durchmesser):** F₁ = F₂ = Z mit Z ∈ {Zylinder, Kugel,
    Kreis, Torus}; das Maß ist der Durchmesser d des Form-Elements.
  - **Fall B (parallele Geraden):** F₁, F₂ ⊂ E zwei parallele
    Geraden in einer gemeinsamen Ebene E (siehe `hg_gerade.md`,
    `hg_ebene.md`); das Maß ist der euklidische Abstand
    d(F₁, F₂) := inf { ‖p − q‖ | p ∈ F₁, q ∈ F₂ }.
  - **Fall C (parallele Ebenen):** F₁, F₂ ⊂ ℝ³ zwei parallele
    Ebenen (siehe `hg_ebene.md`); das Maß ist
    d(F₁, F₂) := inf { ‖p − q‖ | p ∈ F₁, q ∈ F₂ }.

- ℓ ∈ ℝ_{>0} der zugeordnete Maßwert (in mm) mit
  ℓ = d(F₁, F₂) im jeweiligen Fall (Fall A: ℓ = d),
- T = [ℓ_min, ℓ_max] ⊂ ℝ mit ℓ_min ≤ ℓ ≤ ℓ_max ein **Toleranzfeld**.

Dann ist das **lineare Größenmaß** das Tupel

```
G(F, ℓ, T) := (F, ℓ, T).
```

Insbesondere ist G(F, ℓ, T) durch Vergessen des Toleranzfeldes T
und durch Wahl einer Repräsentanten-Strecke s zwischen F₁ und F₂
(im Fall B/C die kürzeste Verbindungsstrecke) ein **Längenmaß** im
Sinne von `hg_laengenmass.md`.

## Wohldefiniertheit

- **Existenz und Eindeutigkeit:** Für jedes Form-Element-Paar in
  einem der drei Fälle ist d(F₁, F₂) bzw. d eindeutig bestimmt:
  - Fall A: der Durchmesser eines Zylinders/Kugel/Kreis/Torus ist
    durch das Form-Element selbst eindeutig festgelegt.
  - Fall B/C: der Infimumsabstand zweier paralleler Geraden bzw.
    Ebenen ist eindeutig und entspricht der Länge des gemeinsamen
    Lot-Streckenstücks (Strecke rechtwinklig zu beiden Features).
- **Repräsentanten-Unabhängigkeit:** In Fall B/C ist die
  Repräsentanten-Strecke s nicht eindeutig (jedes Lot zwischen F₁
  und F₂ liefert dieselbe Länge), aber der **Wert** ℓ ist es. Die
  Reduktion auf ein Längenmaß ist daher von der Wahl des Lotes
  unabhängig.
- **Beziehung zum Oberbegriff:** Jedes lineare Größenmaß ist durch
  Wahl einer Repräsentanten-Strecke und Vergessen des
  Toleranzfeldes ein Längenmaß; die umgekehrte Richtung gilt nicht
  (ein beliebiges Längenmaß zwischen zwei Punkten muss kein
  Form-Element-Paar im GPS-Sinne sein, z. B. der Abstand zweier
  Bohrungsachsen ist ein Längenmaß, aber kein Größenmaß).
- **Nicht-Zirkularität:** Die Definition stützt sich auf
  `laengenmass`, `strecke`, `gerade`, `ebene` und die Form-Element-
  Begriffe Zylinder/Kugel/Kreis/Torus, die im aktuellen Glossar nicht
  als eigene Einträge geführt sind und hier als externe
  GPS-Form-Element-Begriffe referenziert werden (keine
  Holzbau-Verankerung erforderlich).

## Erläuterung (nicht normativ)

DIN EN ISO 14405-1 ist Teil 1 der GPS-Reihe für dimensionelle
Tolerierung. Sie regelt, was im technischen Maschinenbau-Sinn ein
„toleranzfähiges Maß" ist und welche Form-Element-Paare in Frage
kommen. Der Unterschied zum allgemeinen Längenmaß ist substantiell:

- Ein **Längenmaß** nach DIN EN ISO 129-1 ist jeder lineare Abstand
  zwischen zwei Bezugs-Features in einer Zeichnung — auch der
  Abstand zwischen einer Kante und einer Bohrungsmitte.
- Ein **lineares Größenmaß** nach DIN EN ISO 14405-1 ist enger
  gefasst: es muss zwischen zwei gegenüberliegenden Features eines
  Form-Elements (Zylinder, Kugel, Kreis, Torus, parallele Geraden,
  parallele Ebenen) liegen, weil nur in diesen Konstellationen das
  Toleranzfeld eindeutig auf eine Form-Eigenschaft des
  Werkstücks bezogen werden kann.

Im Holzbau tritt das lineare Größenmaß nur in Sonderfällen auf:

- Breite einer Nut (parallele Ebenen),
- Durchmesser eines Bohrungs-Lochs (Zylinder),
- Dicke einer Platte zwischen Ober- und Unterseite (parallele
  Ebenen).

Die meisten Holzbau-Maße (Sparrenlänge, Pfettenabstand, Kervenfuß
zum Trauf-Anschnitt) sind **Längenmaße**, aber **keine linearen
Größenmaße** — sie sind nicht zwischen gegenüberliegenden Features
eines Form-Elements gemessen. Für den Holzbau-Werkplan ist daher
das `laengenmass` der relevantere Begriff; das
`lineares_groessenmass` ist primär für CNC-Verbinder-Schnittstellen
und Platten-Querschnitts-Maße einschlägig.

## Beziehungen

- **Oberbegriff:** `laengenmass` — durch Wahl einer
  Repräsentanten-Strecke und Vergessen des Toleranzfeldes wird ein
  lineares Größenmaß zu einem Längenmaß.
- **Teilbegriffe:** keine im aktuellen Glossar (die ISO-14405-1-
  Form-Element-Fälle sind durch die Fallunterscheidung in der
  Mathematischen Definition abgedeckt, nicht durch eigene Einträge).
- **Abgrenzung:**
  - **`laengenmass`:** Oberbegriff; allgemeine Bemaßung ohne
    Form-Element-Einschränkung und ohne Toleranzfeld.
  - **„Größenmaß" (nackt):** im DACH-Korpus mehrdeutig (umfasst
    teils auch winklige Größen); DIN EN ISO 14405-1 ist auf
    **lineare** Größenmaße eingeschränkt, daher die qualifizierende
    Norm-Benennung „lineares Größenmaß".
  - **GPS (Geometrische Produktspezifikation):** das normative
    Rahmenwerk, in dem das lineare Größenmaß steht; Korpus-Begriff
    ohne eigenen Hauptglossar-Eintrag (Konvention §6.D —
    holzbau-irrelevant in der breiten Form).
  - **Toleranzfeld:** der Wertebereich [ℓ_min, ℓ_max] für den
    Maßwert; Bestandteil des linearen Größenmaßes, im Glossar nicht
    eigenständig geführt (Konvention §6.D).
  - **`masstoleranz_din18202`:** Bauwerks-Maßtoleranz nach
    Ausführungsnorm; nicht identisch mit dem GPS-Toleranzfeld
    (DIN 18202 ist handwerkliche Bautoleranz, ISO 14405-1 ist
    Maschinenbau-GPS).

## Implementierungshinweis

Datentyp (Domänen-Schicht, Kotlin, Schicht `domain.bemassung` —
künftiges Paket, **nicht** Teil der Sparren-mit-zwei-Kerven-Etappe):

```
sealed class LinearesGroessenmass {
    abstract val wert: Double          // in mm, > 0
    abstract val toleranzfeld: ToleranzFeld  // ClosedFloatingPointRange<Double>

    data class Durchmesser(
        val formElement: GpsFormElement,  // Zylinder | Kugel | Kreis | Torus
        override val wert: Double,
        override val toleranzfeld: ToleranzFeld
    ) : LinearesGroessenmass()

    data class AbstandParalleleGeraden(
        val gerade1: Gerade,
        val gerade2: Gerade,            // parallel zu gerade1
        override val wert: Double,
        override val toleranzfeld: ToleranzFeld
    ) : LinearesGroessenmass()

    data class AbstandParalleleEbenen(
        val ebene1: Ebene,
        val ebene2: Ebene,              // parallel zu ebene1
        override val wert: Double,
        override val toleranzfeld: ToleranzFeld
    ) : LinearesGroessenmass()
}
```

- **Einheit:** Wert in mm (Double); Toleranzfeld-Grenzen in mm.
- **Invarianten** (Factory):
  1. `wert > Toleranzen.LAENGE_EPS` (positiv, nicht entartet).
  2. `toleranzfeld.start ≤ wert ≤ toleranzfeld.endInclusive`.
  3. Form-Element-Konsistenz: Bei `AbstandParalleleGeraden` muss
     `gerade1` parallel zu `gerade2` sein (Test via
     `KOLLINEAR_EPS`); analog für `AbstandParalleleEbenen` mit
     parallelen Normalen.
  4. Wert-Geometrie-Konsistenz: `|wert − d(F₁, F₂)| ≤ LAENGE_EPS`
     (Maßwert stimmt mit dem geometrischen Abstand überein).
- **Code-Pendant-Pflicht:** keine (`begriffstyp: merkmal`); die
  Klasse wird erst eingeführt, wenn ein Tolerierungs-/CNC-Modul
  gebaut wird.
- **Edge Cases:**
  - Nicht-parallele Geraden/Ebenen: kein lineares Größenmaß im
    Sinne von ISO 14405-1; Konstruktion über Factory mit
    `Resultat.Fehler`.
  - Toleranzfeld kollabiert (`start == endInclusive`): zulässig
    (Nullspiel-Maß), aber im Werkplan ungewöhnlich.

## Quellen

**Primär (normativ):**

- DIN EN ISO 14405-1:2017-07, „Geometrische Produktspezifikation
  (GPS) — Dimensionelle Tolerierung — Teil 1: Lineare Größenmaße",
  Abschnitte 3 (Begriffe) und 4 (lineare Größenmaße).

**Sekundär:**

- Henzold, G.: *Form und Lage.* 4. Aufl., Beuth Verlag, Berlin —
  Kap. zur GPS-Systematik und zum Größenmaß-Begriff.

**Korpus (nicht autoritativ):**

- Quality-Office-Schulungsskript „GPS – Lineare Größenmaße nach
  DIN EN ISO 14405-1" (Stand 09-2024).
