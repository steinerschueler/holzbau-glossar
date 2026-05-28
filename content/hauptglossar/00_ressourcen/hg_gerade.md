---
id: gerade
benennung: Gerade
synonyme: ["affine Gerade", "Linie (Geometrie)", "eindimensionaler affiner Unterraum"]
abgelehnte_benennungen: [Linie, Strecke, Strahl, Achse, "line", "straight line"]
oberbegriff: null
begriffstyp: primitiv
voraussetzungen: [punkt, vektor, toleranzen]
abgrenzung_zu: [strecke, halbgerade, ebene, vektor]
status: entwurf
theorie_pflichtig: required
quellen_primär:
  - "DIN ISO 80000-2:2022-08, 'Größen und Einheiten – Teil 2: Mathematik', Abschnitt 2 (Geometrie und Vektoren), Symbole für Geraden im Raum."
  - "ISO 80000-2:2019, Abschnitt 2 'Mathematics – Geometry'."
quellen_sekundär:
  - "Bronstein, I. N. et al.: Taschenbuch der Mathematik. Kap. 3.5.1 'Geraden im Raum'."
  - "Fischer, G.: Lineare Algebra. 19. Aufl., Springer Spektrum 2020, Kap. 0/1 'Affine Geometrie'."
  - "Bär, C.: Elementargeometrie. Springer Spektrum, Kap. 4 'Geraden in Ebene und Raum'."
quellenkonflikt: |
  Holzbau-Normen (DIN 1052, DIN EN 1995-1-1, SIA 265) verwenden den
  Begriff Gerade als gegeben (z. B. „Sparrenachse", „Wirkungslinie"),
  ohne ihn axiomatisch zu definieren. DIN ISO 80000-2 nennt Symbole
  für Geraden, definiert sie jedoch nicht formal. Eigene Festlegung:
  eine Gerade ist die Punktmenge { p₀ + t·v | t ∈ ℝ } für einen
  Stützpunkt p₀ und einen Nicht-Nullvektor v (Richtungsvektor). Diese
  Festlegung ist konsistent mit Bronstein, Fischer, Bär und allen
  konsultierten Holzbau-Quellen.
---

## Prosa-Definition

Eine **Gerade** ist ein eindimensionaler affiner Unterraum von ℝ³,
gegeben als die Menge aller Punkte, die von einem festen Stützpunkt
p₀ aus durch ganzzahlige reelle Vielfache eines Nicht-Nullvektors v
(Richtungsvektor) erreicht werden; sie ist beidseitig unbegrenzt
und richtungslos in dem Sinne, dass eine Gerade durch (p₀, v) und
durch (p₀, −v) dieselbe Punktmenge bezeichnet.

## Mathematische Definition

Sei

- p₀ ∈ ℝ³ ein **Stützpunkt**,
- v ∈ ℝ³ \ {0} ein **Richtungsvektor**.

Dann ist die durch (p₀, v) definierte **Gerade** g ⊂ ℝ³ die Menge

```
g(p₀, v) := { p₀ + t · v ∈ ℝ³ | t ∈ ℝ }.
```

Die Abbildung

```
γ : ℝ → ℝ³,   γ(t) := p₀ + t · v
```

heißt **Parametrisierung** der Geraden. Sie ist injektiv (wegen
v ≠ 0) und surjektiv auf g.

Wesentliche abgeleitete Größen für x ∈ ℝ³:

- **Einheits-Richtung**: v̂ := v / ‖v‖ ∈ S² (bis auf Vorzeichen).
- **Vorzeichenbehafteter Parameter** von x ∈ g bezüglich (p₀, v̂):
  t(x) := ⟨x − p₀, v̂⟩, in mm.
- **Orthogonale Projektion** auf g: π_g(x) := p₀ + ⟨x − p₀, v̂⟩ · v̂.
- **Abstand** Punkt–Gerade: d_g(x) := ‖x − π_g(x)‖, in mm.

## Wohldefiniertheit

Die Definition g(p₀, v) ist als Punktmenge invariant unter den
folgenden Repräsentantenwechseln, die also dieselbe Gerade
bezeichnen:

1. **Skalierung des Richtungsvektors**: Für jedes λ ∈ ℝ \ {0} gilt
   g(p₀, λ·v) = g(p₀, v), denn { p₀ + t·(λv) | t ∈ ℝ } =
   { p₀ + (λt)·v | t ∈ ℝ } = { p₀ + s·v | s ∈ ℝ }. Insbesondere gilt
   g(p₀, v) = g(p₀, −v): die Gerade ist **ungerichtet**.
2. **Verschiebung des Stützpunkts entlang v**: Für jedes s ∈ ℝ und
   p₀' := p₀ + s·v gilt g(p₀', v) = g(p₀, v), denn { p₀' + t·v | t ∈ ℝ }
   = { p₀ + (s + t)·v | t ∈ ℝ } = g(p₀, v).
3. **Allgemeine Stützpunktwahl**: Für jedes p₀' ∈ g(p₀, v) gilt
   g(p₀', v) = g(p₀, v), denn p₀' − p₀ ∈ ℝ·v (Folge von 2).

Identitätsrelation der Geraden als Punktmengen: Zwei Datentyp-
Repräsentanten (p₀, v) und (p₀', v') beschreiben **dieselbe Gerade**
genau dann, wenn

```
v × v' = 0   (Kollinearität)   und   (p₀' − p₀) × v = 0   (Inzidenz),
```

beide Tests numerisch mit `Toleranzen.KOLLINEAR_EPS` auf normierten
Vektoren auszuführen.

Existenz: Für jedes (p₀, v) mit v ≠ 0 ist g nicht-leer (p₀ ∈ g) und
enthält tatsächlich überabzählbar viele Punkte.

Nicht-Zirkularität: Die Definition stützt sich nur auf Punkt, Vektor,
Skalar- und Kreuzprodukt sowie auf das Toleranzkonzept aus
`hg_toleranzen.md`.

## Erläuterung (nicht normativ)

Eine Gerade ist die einfachste eindimensionale geometrische Figur
mit unendlicher Ausdehnung in beide Richtungen. Im Holzbau treten
Geraden konzeptionell auf als

- Trägergeraden von Bauteilachsen (eine Sparrenachse als endlicher
  Bauteilbestandteil ist eine **Strecke**, ihre unbegrenzte
  Verlängerung eine Gerade),
- Schnittlinien zweier Ebenen (z. B. Gratlinie als Schnitt zweier
  Dachebenen, geometrisch eine Gerade; das tatsächliche Bauteil
  „Grat" ist davon ein endliches Stück),
- Wirkungslinien von Kräften (in der Statik),
- Anrisslinien als gedachte unbegrenzte Träger einer Markierung.

Der konzeptionelle Unterschied zur Strecke und zur Halbgeraden ist
die zweiseitige Unbegrenztheit. Der Unterschied zum Vektor ist die
Ortsbindung: ein Richtungsvektor v allein ist keine Gerade; erst
zusammen mit einem Stützpunkt p₀ definiert er eine.

## Beziehungen

- **Oberbegriff**: eindimensionaler affiner Unterraum von ℝ³ (formal).
  Im Glossar Primitiv.
- **Teilbegriffe / Rollen**:
  - **Achse** eines Stabbauteils: eine Gerade in spezialisierter Rolle
    (wenn unbegrenzt gemeint) bzw. eine Strecke (wenn auf das
    Bauteil eingeschränkt). Eigener Eintrag in Folgearbeit.
  - **Schnittgerade** zweier Ebenen: rollenbezogene Verwendung;
    eigener Eintrag.
- **Bestandteile (partitiv)**: jede Gerade enthält überabzählbar viele
  Punkte; eine Gerade hat keine eigenen ausgezeichneten Bestandteile
  (Anfangs- oder Endpunkt existieren nicht).
- **Abgrenzung**:
  - **Strecke** (`strecke`): endlicher Ausschnitt einer Geraden mit
    zwei Endpunkten. Formal: zu jeder Strecke [a, b] mit a ≠ b
    existiert eine eindeutige Trägergerade g(a, b − a), aber nicht
    umgekehrt — auf einer Geraden liegen unendlich viele Strecken.
  - **Halbgerade** (`halbgerade`): einseitig begrenzter Ausschnitt
    einer Geraden { p₀ + t·v | t ∈ [0, ∞) }. Eine Gerade lässt sich
    durch jeden ihrer Punkte in genau zwei Halbgeraden zerlegen,
    deren Schnitt der Trennpunkt ist.
  - **Ebene** (`ebene`): zweidimensionaler affiner Unterraum; höhere
    Dimension. Eine Gerade liegt entweder vollständig in einer Ebene
    oder schneidet sie in höchstens einem Punkt.
  - **Vektor** (`vektor`): ortsfreie gerichtete Verschiebung. Der
    Richtungsvektor v einer Geraden ist ein Vektor, die Gerade selbst
    ist es nicht.

## Implementierungshinweis

Datentyp (Domänen-Schicht, Kotlin, Schicht `domain.geometrie`):

```
data class Gerade(
    val stuetzpunkt: Punkt,   // p₀
    val richtung: Vektor      // v, ‖richtung‖² > Toleranzen.NORM_EPS
) {
    init {
        // ‖richtung‖² > Toleranzen.NORM_EPS, sonst Entartet.Nullrichtung
    }
}
```

- **Einheit**: Stützpunkt-Koordinaten und Komponenten der Richtung in
  mm (Double). Die Richtung ist in der Standard-Repräsentation nicht
  zwingend normiert; abgeleitete Operationen normieren intern.
- **Invarianten** (in `init` bzw. Factory prüfen, bei Verletzung
  `Entartet`-Variante zurückgeben, niemals Exception):
  1. ‖richtung‖² > Toleranzen.NORM_EPS (sonst keine Gerade definierbar).
  2. Alle Komponenten von `stuetzpunkt` und `richtung` finit (kein NaN,
     kein ±∞).
- **Konstruktoren**:
  - `Gerade.ausStuetzpunktUndRichtung(p0, v): Resultat<Gerade, EntartetGeometrie>`
  - `Gerade.ausZweiPunkten(a, b): Resultat<Gerade, EntartetGeometrie>` mit Failure-Variante
    `Entartet.Nullrichtung`, falls ‖b − a‖² ≤ Toleranzen.NORM_EPS.
  - `Gerade.ausStrecke(s: Strecke): Gerade` (Trägergerade einer
    Strecke; durch die Invariante der Strecke garantiert nicht
    entartet).
- **Edge Cases / Entartet-Varianten**:
  - **Nullrichtung** (‖v‖² ≤ Toleranzen.NORM_EPS): `Entartet.Nullrichtung`.
    Keine Gerade definierbar (entartete „Punktgerade").
  - **Nicht-finite Koordinaten** in `stuetzpunkt` oder `richtung`:
    `Entartet.NichtFinit`.
  - **Zwei-Punkt-Konstruktion mit fast gleichen Punkten**
    (‖b − a‖ knapp über Toleranz): zulässig, aber numerisch sensibel;
    Hinweis im Domain-Test.
- **Identität / Gleichheit**:
  - `fun istGleich(other: Gerade, eps: Double = Toleranzen.KOLLINEAR_EPS): Boolean`
    (Synonym `istIdentischZu(other, eps)`) prüft (i) Kollinearität
    von `richtung` und `other.richtung`
    über das Kreuzprodukt der normierten Vektoren und (ii) Inzidenz
    von `other.stuetzpunkt` mit `this` (siehe `enthaelt`).
  - Direkter `==`-Vergleich auf der Datenklasse vergleicht nur
    Repräsentanten, **nicht** Geraden als Punktmengen, und ist daher
    für geometrische Identität ungeeignet.
- **Abgeleitete Operationen** (`GeradeOps.kt`):
  - `fun einheitsRichtung(): Vektor` = richtung.normiert().werteOder { error("Invariante 1 verletzt") }
    (durch Invariante 1 zur Laufzeit nie betroffen).
  - `fun punktAuf(t: Double): Punkt` = stuetzpunkt + t · richtung.
  - `fun parameterVon(p: Punkt): Double` =
    ⟨p − stuetzpunkt, einheitsRichtung()⟩ (in mm; nur sinnvoll, wenn
    `enthaelt(p)` gilt, sonst Projektion).
  - `fun projizieren(p: Punkt): Punkt` = stuetzpunkt +
    ⟨p − stuetzpunkt, einheitsRichtung()⟩ · einheitsRichtung().
  - `fun abstand(p: Punkt): Double` = ‖p − projizieren(p)‖, in mm.
  - `fun enthaelt(p: Punkt, eps: Double = Toleranzen.LAENGE_EPS): Boolean`
    = abstand(p) ≤ eps.
  - `fun umkehrenRichtung(): Gerade` = Gerade(stuetzpunkt, −richtung)
    (gleiche Punktmenge, entgegengesetzter Richtungsrepräsentant).

## Quellen

**Primär (normativ):**

- DIN ISO 80000-2:2022-08, „Größen und Einheiten – Teil 2: Mathematik".
- ISO 80000-2:2019, „Quantities and units – Part 2: Mathematics".

**Sekundär:**

- Bronstein, I. N.; Semendjajew, K. A.; Musiol, G.; Mühlig, H.:
  *Taschenbuch der Mathematik.* Edition Harri Deutsch, aktuelle
  Auflage, Kap. 3.5.1.
- Fischer, G.: *Lineare Algebra.* 19. Aufl., Springer Spektrum 2020.
- Bär, C.: *Elementargeometrie.* Springer Spektrum.

**Korpus (nicht autoritativ):**

- Wikipedia, Lemma „Gerade" (abgerufen 2026-05-07).
