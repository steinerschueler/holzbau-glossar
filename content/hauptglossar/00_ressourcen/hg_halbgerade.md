---
id: halbgerade
benennung: Halbgerade
synonyme: [Strahl, "geschlossene Halbgerade", "abgeschlossene Halbgerade"]
abgelehnte_benennungen: [Halbstrecke, Strahllinie, "ray", "half-line"]
oberbegriff: null
begriffstyp: primitiv
voraussetzungen: [punkt, vektor, gerade, toleranzen]
abgrenzung_zu: [gerade, strecke, vektor]
status: entwurf
theorie_pflichtig: required
quellen_primär:
  - "DIN ISO 80000-2:2022-08, 'Größen und Einheiten – Teil 2: Mathematik', Abschnitt 2 (Geometrie)."
quellen_sekundär:
  - "Bronstein, I. N. et al.: Taschenbuch der Mathematik. Kap. 3.5.1 'Geraden, Strahlen und Strecken im Raum'."
  - "Bär, C.: Elementargeometrie. Springer Spektrum, Kap. 4."
  - "Fischer, G.: Lineare Algebra. 19. Aufl., Springer Spektrum 2020."
quellenkonflikt: |
  Keine Holzbau-Norm definiert den Begriff Halbgerade. DIN ISO 80000-2
  listet das Symbol für die Halbgerade, ohne sie axiomatisch zu
  definieren. Eigene Festlegung: eine Halbgerade ist
  { p₀ + t·v | t ∈ [0, ∞) } für Ursprung p₀ und Richtung v ≠ 0;
  sie ist abgeschlossen (enthält den Ursprungspunkt). Diese Festlegung
  ist konsistent mit Bronstein, Bär und Fischer.
---

## Prosa-Definition

Eine **Halbgerade** (auch **Strahl**) ist ein einseitig begrenzter,
zur anderen Seite unbegrenzter Ausschnitt einer Geraden, der durch
einen ausgezeichneten **Ursprungspunkt** p₀ und einen
Nicht-Nullvektor v als Richtung gegeben ist und genau jene Punkte
enthält, die von p₀ aus durch nicht-negative reelle Vielfache von v
erreicht werden.

## Mathematische Definition

Sei

- p₀ ∈ ℝ³ der **Ursprungspunkt** (Anfangspunkt der Halbgeraden),
- v ∈ ℝ³ \ {0} der **Richtungsvektor**.

Dann ist die durch (p₀, v) definierte **Halbgerade** h ⊂ ℝ³ die
Menge

```
h(p₀, v) := { p₀ + t · v ∈ ℝ³ | t ∈ [0, ∞) }.
```

Die Halbgerade ist **gerichtet**: anders als bei der Geraden gilt
h(p₀, v) ≠ h(p₀, −v); die beiden Mengen sind die zwei
komplementären Halbgeraden derselben Trägergeraden mit gemeinsamem
Ursprungspunkt p₀ (h(p₀, v) ∩ h(p₀, −v) = {p₀}).

Wesentliche abgeleitete Größen:

- **Trägergerade**: g(p₀, v) ⊃ h(p₀, v).
- **Einheits-Richtung**: v̂ := v / ‖v‖.
- **Komplementäre Halbgerade**: h(p₀, −v).

## Wohldefiniertheit

- **Skalierung des Richtungsvektors mit positivem Faktor**: Für
  jedes λ > 0 gilt h(p₀, λ·v) = h(p₀, v), denn
  { p₀ + t·(λv) | t ≥ 0 } = { p₀ + (λt)·v | t ≥ 0 } = h(p₀, v).
- **Skalierung mit negativem Faktor kehrt die Halbgerade um**:
  h(p₀, −v) ist die komplementäre Halbgerade, **nicht** dieselbe.
  Die Halbgerade ist also durch die Richtungs-**Halbgerade** in S²
  (also v̂ bis auf positive Skalierung), nicht nur durch die
  Richtungslinie bestimmt.
- **Ursprungspunkt ist eindeutig**: p₀ ist der einzige Punkt von
  h(p₀, v), der nicht im offenen Inneren liegt; er ist durch die
  Halbgerade als Punktmenge eindeutig festgelegt.
- **Existenz**: Für jedes (p₀, v) mit v ≠ 0 ist h nicht-leer und
  enthält überabzählbar viele Punkte.
- **Nicht-Zirkularität**: Die Definition verwendet Punkt, Vektor und
  reelles Intervall.

## Erläuterung (nicht normativ)

Im Holzbau tritt die Halbgerade konzeptionell auf als

- gedachte Verlängerung einer Bauteilachse über eines ihrer Enden
  hinaus (z. B. Sparrenachse über den Firstpunkt hinaus zur
  Bestimmung von Verschneidungen),
- Sichtstrahl in der Visualisierung (Raycasting).

Beide Anwendungen sind im DACH-Holzbau-Korpus nur schwach belegt
und konzeptioneller Natur. Eine Anwendung als „gerichtete
Wirkungslinie einer Last" wäre fachlich irreführend: die Wirkungs-
linie einer Kraft ist in der Technischen Mechanik konsensual eine
**Gerade** (mit separat geführtem Richtungssinn), nicht eine
Halbgerade. Das Verschiebungsaxiom der Statik / Linienflüchtigkeit
verlangt bilaterale Verschiebung entlang der Wirkungslinie, die
auf einer Halbgerade nicht definiert wäre.

Sie ist von der Strecke (zwei Endpunkte) und der Geraden
(unbegrenzt in beide Richtungen) klar zu unterscheiden.

## Beziehungen

- **Oberbegriff**: einseitig begrenzte Teilmenge einer Geraden;
  formal das Bild des Halbintervalls [0, ∞) unter einer affinen
  Abbildung.
- **Bestandteile (partitiv)**: Ursprungspunkt p₀; offenes Inneres
  { p₀ + t·v | t > 0 }; offenes Ende (kein Endpunkt) bei t → ∞.
- **Abgrenzung**:
  - **Gerade** (`gerade`): unbegrenzt in beide Richtungen,
    ungerichtet. Eine Halbgerade ist eine echte Teilmenge ihrer
    Trägergerade.
  - **Strecke** (`strecke`): beidseitig begrenzt, endliche Länge.
    Eine Strecke [a, b] ist die Schnittmenge h(a, b−a) ∩ h(b, a−b)
    der beiden komplementären Halbgeraden mit Ursprung a bzw. b.
  - **Vektor** (`vektor`): ortsfreie Verschiebung; eine Halbgerade
    ist die ortsgebundene Realisierung einer „Richtung ab einem
    Punkt".

## Implementierungshinweis

Datentyp (Domänen-Schicht, Kotlin, Schicht `domain.geometrie`):

```
data class Halbgerade(
    val ursprung: Punkt,      // p₀
    val richtung: Vektor      // v, ‖richtung‖² > Toleranzen.NORM_EPS
) {
    init {
        // ‖richtung‖² > Toleranzen.NORM_EPS, sonst Entartet.Nullrichtung
    }
}
```

- **Einheit**: Ursprungs-Koordinaten und Richtungskomponenten in mm
  (Double). Die Richtung ist intern nicht zwingend normiert.
- **Invarianten**:
  1. ‖richtung‖² > Toleranzen.NORM_EPS.
  2. Alle Komponenten finit.
- **Edge Cases / Entartet-Varianten**:
  - **Nullrichtung**: `Entartet.Nullrichtung`.
  - **Nicht-finite Koordinaten**: `Entartet.NichtFinit`.
- **Abgeleitete Operationen** (`HalbgeradeOps.kt`):
  - `fun einheitsRichtung(): Vektor`.
  - `fun punktAuf(t: Double): Punkt` für alle reellen t. Für t < 0
    liegt das Ergebnis nicht auf der Halbgeraden, sondern auf der
    komplementären Halbgeraden; der Aufrufer kann das mit
    `enthaelt(p)` prüfen, falls nötig.
  - `fun traegergerade(): Gerade` = Gerade(ursprung, richtung).
  - `fun komplement(): Halbgerade` = Halbgerade(ursprung, −richtung).
  - `fun enthaelt(p: Punkt, eps: Double = Toleranzen.LAENGE_EPS): Boolean`
    = (a) `traegergerade().enthaelt(p, eps)` und (b)
    `⟨p − ursprung, einheitsRichtung()⟩ ≥ −eps`.

## Quellen

**Primär (normativ):**

- DIN ISO 80000-2:2022-08, „Größen und Einheiten – Teil 2: Mathematik".

**Sekundär:**

- Bronstein, I. N.; Semendjajew, K. A.; Musiol, G.; Mühlig, H.:
  *Taschenbuch der Mathematik.* Kap. 3.5.1.
- Bär, C.: *Elementargeometrie.* Springer Spektrum.
- Fischer, G.: *Lineare Algebra.* 19. Aufl., Springer Spektrum 2020.

**Korpus (nicht autoritativ):**

- Wikipedia, Lemma „Strahl (Geometrie)" (abgerufen 2026-05-07).
