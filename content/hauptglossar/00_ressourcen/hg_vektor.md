---
id: vektor
benennung: Vektor
synonyme: [Verschiebungsvektor, "freier Vektor"]
abgelehnte_benennungen: [Pfeil, Richtung, "vector"]
oberbegriff: null
begriffstyp: primitiv
voraussetzungen: []
abgrenzung_zu: [punkt, einheitsvektor, faserrichtung]
status: entwurf
subglossar_pendant: notwendig
quellen_primär:
  - "DIN ISO 80000-2:2022-08, Abschnitt 2 (Geometrie und Vektoren), Symbole 2-7 ff."
  - "ISO 80000-2:2019, Abschnitt 2 'Vektoren und Tensoren'."
quellen_sekundär:
  - "Bronstein, I. N. et al.: Taschenbuch der Mathematik. Kap. 3.5 'Vektoralgebra' und Kap. 4.1 'Lineare Algebra'."
  - "Fischer, G.: Lineare Algebra. 19. Aufl., Springer Spektrum 2020, Kap. 0 'Lineare Geometrie im n-dimensionalen reellen Raum'."
  - "Bär, C.: Elementare Differentialgeometrie. de Gruyter 2010, Kap. 1.1."
quellenkonflikt: |
  Wie bei Punkt definiert keine Holzbau-Norm den Begriff Vektor; er
  wird vorausgesetzt. Eigene Festlegung: ein Vektor ist ein Element
  des Tangentialraumes ℝ³ und beschreibt eine gerichtete Verschiebung
  ohne Ortsbindung. Konsistent mit ISO 80000-2 und der Standard-
  Lehrbuchliteratur.
---

## Prosa-Definition

Ein **Vektor** ist ein Element des dreidimensionalen reellen
Vektorraumes ℝ³, das eine gerichtete Verschiebung im Raum
repräsentiert und durch ein geordnetes Tripel reeller Komponenten
(v_x, v_y, v_z) bezüglich der kanonischen Basis des
Weltkoordinatensystems dargestellt wird; im Längenkontext sind die
Komponenten in Millimeter zu interpretieren.

## Mathematische Definition

Sei

- ℝ³ der dreidimensionale reelle Vektorraum,
- (e_x, e_y, e_z) die kanonische rechtshändige Orthonormalbasis aus
  CLAUDE.md (e_z vertikal nach oben).

Dann ist ein **Vektor** v ∈ ℝ³ eindeutig charakterisiert durch sein
Komponententripel

```
v = v_x · e_x + v_y · e_y + v_z · e_z   mit   (v_x, v_y, v_z) ∈ ℝ³.
```

Die euklidische **Norm** (Länge) ist

```
‖v‖ := √(v_x² + v_y² + v_z²).
```

Ein Vektor heißt **Einheitsvektor**, wenn ‖v‖ = 1, und **Nullvektor**,
wenn v = (0, 0, 0)ᵀ. Die Sphäre der Einheitsvektoren wird mit
S² := { v ∈ ℝ³ | ‖v‖ = 1 } bezeichnet.

## Wohldefiniertheit

- Eindeutigkeit der Komponenten: Bei festgelegter Basis ist die
  Darstellung v ↔ (v_x, v_y, v_z) eine Bijektion zwischen ℝ³ und
  Komponententripeln.
- Wohldefiniertheit der Norm: ‖·‖ ist die durch das kanonische
  Skalarprodukt induzierte Norm; positiv-definit, homogen, dreiecks-
  ungleich.
- Nicht-Zirkularität: Die Definition verwendet ausschließlich
  reelle Zahlen, die Basis (e_x, e_y, e_z) und die Wurzelfunktion.

## Erläuterung (nicht normativ)

Ein Vektor ist die Abstraktion einer Verschiebung: er hat Richtung
und Länge, aber keinen festen Anfangspunkt. In der Holzkonstruktion
treten Vektoren auf als

- Faserrichtung eines Bauteils (Einheitsvektor),
- Normalenvektor einer Ebene (z. B. Dachfläche),
- Differenz zweier Punkte (z. B. Sparrenachse als Endpunkt − Anfangspunkt),
- Translationsvektoren bei Verschiebungen.

Der zentrale konzeptionelle Unterschied zum Punkt ist die fehlende
Ortsbindung. „Punkt + Vektor → Punkt" und „Punkt − Punkt → Vektor"
sind die zulässigen Mischoperationen.

## Beziehungen

- **Oberbegriff**: keiner; Vektor ist mathematisches Primitiv.
- **Teilbegriffe (Spezialisierungen)**:
  - **Einheitsvektor**: Vektor mit Norm 1.
  - **Nullvektor**: eindeutiger Vektor mit Norm 0.
  - **Faserrichtung**: holzbauspezifische Rolle eines Einheitsvektors,
    der die Richtung des Holzwuchses am Bauteil angibt (eigener
    Eintrag in Folgearbeit).
- **Abgrenzung**:
  - **Punkt** (eigener Eintrag): hat eine Stelle, aber keine
    Richtung; ein Vektor hat eine Richtung, aber keine Stelle.
  - **Strecke** (eigener Eintrag): konkrete, ortsgebundene
    Verbindung zweier Punkte; ein Vektor ist die ortsfreie
    Differenz dieser Punkte.
  - **Gerade**: ein eindimensionaler affiner Unterraum, definiert
    durch Punkt + Richtungsvektor; nicht identisch mit dem
    Richtungsvektor selbst.

## Implementierungshinweis

Datentyp (Domänen-Schicht, Kotlin, Schicht `domain.geometrie`):

```
data class Vektor(
    val x: Double,   // mm (oder dimensionslos für Einheitsvektoren)
    val y: Double,
    val z: Double
)
```

- **Einheit**: Im Längen-Kontext (Differenzvektor zweier Punkte) in
  mm. Im Richtungs-Kontext (Normalenvektor, Faserrichtung)
  dimensionslos und auf Norm 1 normiert. Die Domänen-Schicht
  unterscheidet beides typkonsistent über Wrapper bzw. Konvention,
  niemals durch implizite Reinterpretation.
- **Invarianten**: keine auf `Vektor` selbst. Für Einheitsvektoren
  wird die Bedingung ‖v‖ ∈ 1 ± Toleranzen.NORM_EPS in den Klassen
  geprüft, die einen Einheitsvektor erwarten (z. B. `Ebene.normale`).
- **Edge Cases**:
  - Nullvektor (‖v‖ = 0): zulässig als Wert, aber nicht als
    Richtung. Versuche, einen Nullvektor zu normieren, liefern
    `Resultat.Fehler` bzw. `EntartetGeometrie.Nullrichtung`.
  - NaN/±∞ in einer Komponente: `EntartetGeometrie.NichtFinit`.
  - Sehr kleine, aber nicht-null Vektoren (‖v‖ < Toleranzen.NORM_EPS):
    werden als entartet behandelt; Normierung würde numerisch
    instabil.
- **Abgeleitete Operationen**:
  - `operator fun plus(w: Vektor): Vektor`
  - `operator fun minus(w: Vektor): Vektor`
  - `operator fun times(s: Double): Vektor` (Skalarmultiplikation)
  - `infix fun dot(w: Vektor): Double` (Skalarprodukt)
  - `infix fun cross(w: Vektor): Vektor` (Kreuzprodukt)
  - `val norm: Double` = √(x² + y² + z²)
  - `fun normiert(): Resultat<Vektor, EntartetGeometrie>` (liefert `Resultat.Fehler` bei Nullvektor)

## Quellen

**Primär (normativ):**

- DIN ISO 80000-2:2022-08, „Größen und Einheiten – Teil 2: Mathematik".
- ISO 80000-2:2019.

**Sekundär:**

- Bronstein, I. N.; Semendjajew, K. A.; Musiol, G.; Mühlig, H.:
  *Taschenbuch der Mathematik.*
- Fischer, G.: *Lineare Algebra.* 19. Aufl., Springer Spektrum 2020.
- Bär, C.: *Elementare Differentialgeometrie.* 2. Aufl., de Gruyter 2010.

**Korpus (nicht autoritativ):**

- Wikipedia, Lemma „Vektor" (abgerufen 2026-05-07).
