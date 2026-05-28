---
id: hankinson_winkel
benennung: Hankinson-Winkel
synonyme: ["Faserwinkel α (im Sinne der Hankinson-Formel)", "Kraft-Faser-Winkel", "α-Winkel der Hankinson-Bemessung"]
abgelehnte_benennungen: [Faserwinkel, "fibre angle", Lochleibungswinkel, "load-grain angle", Hankinson-Wert]
oberbegriff: null
begriffstyp: merkmal
voraussetzungen: [vektor, einheitsvektor, faserrichtung, lage, lagenstruktur, toleranzen]
abgrenzung_zu: [faserrichtung, faserneigung, plattenlaengsrichtung, haupttragrichtung]
status: entwurf
theorie_pflichtig: required
quellen_primär:
  - "Hankinson, R. L.: 'Investigation of Crushing Strength of Spruce at Varying Angles of Grain'. Air Service Information Circular Vol. III, No. 259, U.S. Air Service, 1921."
  - "DIN EN 1995-1-1:2010-12 (Eurocode 5), 'Bemessung und Konstruktion von Holzbauten – Teil 1-1', Gleichung (6.16) (Druck unter Winkel zur Faser σ_c,α,d) und Gleichungen (8.31), (8.32) (Lochleibungsfestigkeit f_h,α,k unter Winkel α zur Faser bei stiftförmigen Verbindungsmitteln)."
  - "SIA 265:2021, 'Holzbau', Anhang A: Hankinson-Formel zur Bestimmung der charakteristischen Festigkeit unter Winkel zur Faser."
  - "Eurocode 5 — Anwendungsdokument: Erläuterungen zu Gleichung (6.16) und zur Definition des Faserwinkels α als Winkel zwischen Kraftrichtung und Faserrichtung."
quellen_sekundär:
  - "Blass, H. J.; Sandhaas, C.: Ingenieurholzbau – Grundlagen der Bemessung. KIT Scientific Publishing, Karlsruhe 2016, Kap. 5 (Lochleibung), Kap. 6 (Druck unter Winkel)."
  - "Blaß, H. J.; Flaig, M.: Stabförmige Bauteile aus Brettsperrholz. Karlsruher Berichte zum Ingenieurholzbau, Bd. 24, KIT Scientific Publishing, Karlsruhe 2012, DOI 10.5445/KSP/1000030362, Kap. 4 (lagenweise Bemessung mit α_i je Lage)."
  - "Forest Products Laboratory: Wood Handbook FPL-GTR-282, USDA 2021, Kap. 5 (Mechanical Properties of Clear Wood, Hankinson-Formel)."
  - "Niemz, P.; Sonderegger, W.: Physik des Holzes und der Holzwerkstoffe. Hanser, München 2017, Kap. 6 (Anisotropie und Hankinson-Formel)."
  - "Mönck, W.; Rug, W.: Holzbau – Bemessung und Konstruktion. 16. Aufl., Beuth, Berlin 2015."
quellenkonflikt: |
  Die Definition des Hankinson-Winkels α als Winkel zwischen
  Kraftrichtung und Faserrichtung ist in EN 1995-1-1, SIA 265,
  Blass/Sandhaas und FPL Wood Handbook konfliktfrei. Hankinsons
  Originalarbeit (1921) führt α implizit über den Krafteintragswinkel
  zur Faserrichtung beim Druck-Versuch ein.

  Die Wertebereich-Konvention α ∈ [0°, 90°] ist EC5-Praxis
  (EN 1995-1-1, Gl. 6.16 verwendet sin²α + cos²α im Nenner;
  Periodizität ist π/2 wegen des Quadrats). FPL Wood Handbook und
  Blass/Sandhaas folgen derselben Konvention. Für die App-
  Implementation ist die Beschränkung auf [0, π/2] über den Betrag
  des Skalarproduktes |F · n̂| natürlich.

  Eigene Festlegung in diesem Glossar:

  - Der **Hankinson-Winkel** α ist eine **Operation** auf einem
    Kraftvektor F ∈ ℝ³ \\ {0} und einer Faserrichtung f̂ ∈ S²
    (oder analog auf einer Plattenlängsrichtung / Haupttragrichtung
    für Werkstoffe ohne strenge L-Faserrichtung):
       α(F, f̂) := arccos( |F · f̂| / ‖F‖ )  ∈ [0, π/2].
    Die Reduktion auf [0, π/2] erfolgt durch den Betrag
    |F · f̂|; physikalisch ist die Faserachse ungerichtet, daher ist
    der Winkel zu f̂ und −f̂ gleich.
  - Die **Hankinson-Formel** selbst (f_α = f_0 · f_90 /
    (f_0 sin²α + f_90 cos²α)) ist Bemessungsrechnung und gehört in
    die Bemessungs-Schicht; im Glossar wird sie nur als Erläuterung
    geführt. Der Hankinson-**Winkel** ist die geometrische
    Eingangsgröße der Formel und ist im Glossar als
    Geometrie-Operation definiert.
  - **Lagenweise Auswertung bei Mehrlagenholz**: Bei einem
    Mehrlagenholz-Bauteil mit Lagenstruktur (ℓ₀, …, ℓ_{n−1}) wird
    α nicht skalar auf Bauteilebene berechnet, sondern als Vektor
    (α_0, …, α_{n−1}) je Lage:
       α_i(F) := α(F, ℓ_i.faserrichtung).
    Diese Konsequenz ist explizit in der App umzusetzen
    (Visualisierung pro Lage, vgl. Blaß/Flaig 2012, Kap. 4).
  - **Anwendung bei OSB**: Bei Modus SCHWACH ist α auf die
    Plattenlängsrichtung bezogen (α_pl = ∠(F, ê_l)); die
    Hankinson-Formel ist hier abgeschwächt zulässig, weil EC5 /
    EN 12369-1 nur diskrete f_m,0 / f_m,90 führt.
  - **Anwendung bei Modus KEINE**: nicht anwendbar; α ist in der
    Plattenebene undefiniert (Spanplatte, MDF, HDF).

  Die Begriffstyp-Wahl `operation` (statt `merkmal`) ist begründet:
  α ist nicht eine Eigenschaft eines Bauteils, sondern eine Funktion
  zweier Vektoren (Kraft und Faserrichtung). Das ist in der
  Glossar-Methodik (DIN 2330, ISO 704) als operationale Definition
  zu führen.
---

## Prosa-Definition

Der **Hankinson-Winkel** α ist die Operation, die einem Kraftvektor F
im Welt-Koordinatensystem (mit ‖F‖ > 0) und einer Faserrichtung f̂ ∈ S²
genau einen Winkel α ∈ [0°, 90°] als den Betrags-Winkel zwischen der
Kraftrichtung und der Faserachse zuordnet, der als geometrische
Eingangsgröße der Hankinson-Formel zur Bestimmung der charakteristischen
Festigkeit f_α unter beliebigem Faserwinkel nach DIN EN 1995-1-1
(Gl. 6.16, 8.31, 8.32) und SIA 265 (Anhang A) dient.

## Mathematische Definition

Sei

- F ∈ ℝ³ \\ {0} ein Kraftvektor (siehe `vektor`),
- f̂ ∈ S² ⊂ ℝ³ ein Einheitsvektor in der Rolle Faserachse
  (siehe `einheitsvektor`, `faserrichtung`).

Dann ist der **Hankinson-Winkel** α definiert als die Funktion

```
α : (ℝ³ \ {0}) × S² → [0, π/2],
α(F, f̂) := arccos( |⟨F, f̂⟩| / ‖F‖ ).
```

Der Betrag |⟨F, f̂⟩| sichert, dass α ∈ [0, π/2] und dass α
invariant unter Vorzeichenwechsel von f̂ ist (die Faserachse ist
physikalisch ungerichtet; siehe `faserrichtung` Wohldefiniertheit).

**Spezialisierung mit normiertem Kraftvektor**: Für F̂ := F / ‖F‖
∈ S² vereinfacht sich die Formel zu

```
α(F̂, f̂) = arccos( |⟨F̂, f̂⟩| ).
```

**Lagenweise Auswertung bei Mehrlagenholz**: Sei B ein Bauteil mit
Werkstoff w ∈ 𝓜𝓛 (Mehrlagenholz, siehe `mehrlagenholz`) und
Lagenstruktur L = (ℓ₀, …, ℓ_{n−1}) (siehe `lagenstruktur`). Dann
ist der Hankinson-Winkel **pro Lage**

```
α_i(F) := α(F, ℓ_i.faserrichtung)     für i ∈ {0, …, n−1},
```

ein Tupel von n Winkeln. Eine einzelne „Bauteil-α" gibt es bei
Mehrlagenholz **nicht**.

**Werkstoff-Modus-spezifische Bezugsachse**:

| Modus          | Bezugsachse für α                                             |
|----------------|----------------------------------------------------------------|
| HART           | f̂ = Werkstoff-Faserrichtung (siehe `axiales_holz`)            |
| STRUKTURIERT   | (f̂_0, …, f̂_{n−1}) = lagenweise Faserrichtungen (siehe `lage`) |
| SCHWACH        | f̂ = Plattenlängsrichtung (siehe `plattenlaengsrichtung`)      |
| KEINE          | nicht definiert (kein α-Begriff in der Plattenebene)           |

**Hankinson-Formel** (nicht definitorisch, nur Erläuterung; siehe
unten): Die charakteristische Festigkeit unter Faserwinkel α ist

```
f_α = (f_0 · f_90) / (f_0 · sin²α + f_90 · cos²α),
```

mit f_0 = Festigkeit parallel zur Faser (α = 0), f_90 = Festigkeit
rechtwinklig zur Faser (α = π/2). Die Formel ist abgeleiteter Satz der
Bemessungs-Schicht; die Definition gehört in EN 1995-1-1 / SIA 265,
nicht in dieses Glossar.

## Wohldefiniertheit

- **Existenz und Eindeutigkeit**: Für F ∈ ℝ³ \\ {0} und f̂ ∈ S² ist
  ⟨F, f̂⟩ wohldefiniert; |⟨F, f̂⟩| / ‖F‖ ∈ [0, 1] (Cauchy-Schwarz mit
  ‖f̂‖ = 1); arccos: [0, 1] → [0, π/2] ist stetig und bijektiv. Damit
  ist α(F, f̂) eindeutig in [0, π/2].
- **Wertebereich [0, π/2]**: Die Reduktion erfolgt durch den Betrag
  |⟨F, f̂⟩|, der den Winkel zur **ungerichteten** Faserachse misst.
  EN 1995-1-1 und SIA 265 verwenden α ∈ [0°, 90°].
- **Vorzeicheninvarianz von α gegen f̂**: α(F, f̂) = α(F, −f̂), weil
  |⟨F, −f̂⟩| = |⟨F, f̂⟩|. Dies ist Voraussetzung für die
  Wohldefiniertheit, weil die Faserrichtung physikalisch ungerichtet
  ist (siehe `faserrichtung`).
- **Vorzeicheninvarianz von α gegen F**: α(F, f̂) = α(−F, f̂), weil
  |⟨−F, f̂⟩| = |⟨F, f̂⟩|. Damit ist α unabhängig von der
  Kraftrichtungs-Vorzeichenwahl (relevant für reine
  Beanspruchungsklassen Druck/Zug).
- **Numerische Wohldefiniertheit**: arccos auf [0, 1] ist gut
  konditioniert. Für F̂ ∈ S² (normiert) wird |⟨F̂, f̂⟩| in [0, 1]
  durch `coerceIn(0.0, 1.0)` gegen Rundungsüberschreitung gesichert.
- **Edge Case ‖F‖ ≈ 0**: nicht zulässig (Operation auf
  ℝ³ \\ {0}); Aufrufer muss ‖F‖ > 0 sicherstellen
  (`Entartet.HankinsonWinkelKraftIstNullvektor`).
- **Norm-Invariante**: f̂ erbt | ‖f̂‖² − 1 | ≤ NORM_EPS aus
  `einheitsvektor`; die Wohldefiniertheit von α ist auf die
  Norm-Invariante angewiesen (sonst |⟨F, f̂⟩| / ‖F‖ ∉ [0, 1]).
- **Lagenweise Wohldefiniertheit**: α_i ist für jede Lage ℓ_i
  separat wohldefiniert, weil ℓ_i.faserrichtung ∈ S² (Lagen-
  Invariante, siehe `lage`).
- **Nicht-Zirkularität**: Die Definition stützt sich auf `vektor`,
  `einheitsvektor`, `faserrichtung`, `lage`, `lagenstruktur`,
  `toleranzen`. Sie kommt nicht in ihrer eigenen Definition vor.

## Erläuterung (nicht normativ)

### Hankinson-Formel

Die Hankinson-Formel (Hankinson 1921) interpoliert die
charakteristische Festigkeit von Holz unter beliebigem Faserwinkel
α zwischen den beiden Grenzwerten:

```
f_α = (f_0 · f_90) / (f_0 · sin²α + f_90 · cos²α)
```

mit f_0 = Festigkeit parallel zur Faser (α = 0°),
f_90 = Festigkeit rechtwinklig zur Faser (α = 90°).

| α     | sin²α | cos²α | f_α                      |
|-------|-------|-------|---------------------------|
| 0°    | 0     | 1     | f_0                       |
| 30°   | 0,25  | 0,75  | f_0·f_90 / (0,25 f_0 + 0,75 f_90) |
| 45°   | 0,5   | 0,5   | 2 · f_0 · f_90 / (f_0 + f_90)     |
| 60°   | 0,75  | 0,25  | f_0·f_90 / (0,75 f_0 + 0,25 f_90) |
| 90°   | 1     | 0     | f_90                      |

Für Fichte-Vollholz C24: f_c,0,k ≈ 21 N/mm², f_c,90,k ≈ 2,5 N/mm²;
f_c,45 ≈ 4,5 N/mm² (Faktor 5 zur Faser-parallelen Festigkeit).

### Anwendung in EC5

| EC5-Stelle           | Bemessungssituation                                                |
|----------------------|---------------------------------------------------------------------|
| Gl. 6.16             | Druck schräg zur Faser σ_c,α,d                                      |
| Gl. 8.31             | Lochleibungsfestigkeit f_h,α,k bei Bolzen, Stabdübel (D ≤ 30 mm)   |
| Gl. 8.32             | Lochleibungsfestigkeit Sonderfall (Nadelholz mit D > 8 mm)         |

Bei Schraubenverbindungen mit Vollgewindeschrauben (DIN EN 14592)
geht α ebenfalls in die Lochleibungs- und Ausziehfestigkeiten ein.

### Lagenweise Auswertung bei Mehrlagenholz (Blaß/Flaig 2012)

Bei Brettsperrholz ist die Hankinson-Formel auf Bauteilebene **nicht
direkt anwendbar**, weil die Faserrichtung pro Lage variiert.
Blass/Flaig 2012 (KIT, DOI 10.5445/KSP/1000030362) zeigen, dass
für stabförmige BSP-Bauteile die Bemessung pro Lage erfolgen muss:

1. Für jede Lage ℓ_i den Winkel α_i = α(F, ℓ_i.faserrichtung)
   berechnen.
2. Lagenweise Festigkeit f_α_i mit Hankinson auswerten.
3. Lagenbeitrag mit Lagenfläche und Lagensteifigkeit gewichten
   (γ-Verfahren EN 1995-1-1 Anhang B oder Schickhofer-Methodik).

Konsequenz für die App: Die Schnittwinkel-Visualisierung muss bei
Mehrlagenholz alle Lagen mit ihren α_i darstellen, nicht ein
einzelnes α auf Bauteilebene.

### Anwendung bei OSB (Modus SCHWACH)

Bei OSB ist die Faserrichtung im strengen Sinn nicht definiert; die
Bezugsachse für α ist die `plattenlaengsrichtung`. EC5 / EN 12369-1
führt für OSB diskrete f_m,0 (parallel) und f_m,90 (rechtwinklig);
die Hankinson-Interpolation ist abgeschwächt zulässig (großes
Streumaß durch Strand-Streuung).

### Modus KEINE: kein Hankinson-Winkel

Bei Spanplatte, MDF, HDF, harten Faserplatten ist die Festigkeit
in der Plattenebene **richtungsunabhängig** (DIN EN 12369-1: eine
einzige Festigkeit pro Beanspruchungsart). Der Hankinson-Winkel
ist hier nicht definiert; α-Anfragen liefern „nicht zutreffend".

## Beziehungen

- **Oberbegriff**: keiner. Hankinson-Winkel ist eine Operation
  (Funktion).
- **Eingaben**:
  - `Vektor` (Kraftvektor F ∈ ℝ³ \\ {0}).
  - `Einheitsvektor` (Faserachse f̂ ∈ S²) bzw. `Faserrichtung`.
  - Bei Mehrlagenholz: `Lagenstruktur` zur lagenweisen Auswertung.
- **Ausgabe**:
  - Bei `axiales_holz` und `gerichteter_plattenwerkstoff`: skalarer
    Winkel α ∈ [0, π/2] (Radiant; Anzeige in Grad).
  - Bei `mehrlagenholz`: Tupel (α_0, …, α_{n−1}) ∈ [0, π/2]^n.
  - Bei `isotroper_plattenwerkstoff`: nicht zutreffend.
- **Verwendung**:
  - **Hankinson-Formel f_α** (Bemessungs-Schicht): Eingangsgröße.
  - **Schnittwinkel-Visualisierung** (Kernfunktion der App):
    Anzeige des Faserwinkels bei einem Schnitt.
  - **Lochleibungsfestigkeit f_h,α,k** (EN 1995-1-1 Gl. 8.31, 8.32):
    bei stiftförmigen Verbindungsmitteln.
- **Abgrenzung**:
  - **`faserrichtung`**: Einheitsvektor in der Rolle „Material-
    hauptachse"; Eingabe der α-Operation, nicht synonym dazu.
  - **`faserneigung`** (DIN 4074-1): Tangens des Winkels zwischen
    Faser und Bauteillängsachse; Sortier-Merkmal für die
    Festigkeitsklassen-Zuordnung. Hankinson-Winkel ist Winkel
    zwischen Kraft und Faser, Faserneigung ist Winkel zwischen
    Faser und Bauteilachse — beides Winkel, aber an
    unterschiedlichen Geometrieobjekten.
  - **`plattenlaengsrichtung`**: bei OSB (Modus SCHWACH)
    Bezugsachse für α statt Faserrichtung.
  - **`haupttragrichtung`**: bei Mehrlagenholz **nicht** Bezugsachse
    für α (das wäre eine Mittelung); pro Lage wird
    ℓ_i.faserrichtung verwendet.

## Implementierungshinweis

Datentyp (Domänen-Schicht, Kotlin, Package
`zimmermann.domain.geometrie`):

```kotlin
package zimmermann.domain.geometrie

import zimmermann.domain.Resultat
import kotlin.math.abs
import kotlin.math.acos

/**
 * Hankinson-Winkel α zwischen Kraftrichtung und Faserachse.
 * Glossar: hg_hankinson_winkel.md
 *
 * Wertebereich: [0, π/2] Radiant. Vorzeicheninvariant gegen
 * F und n̂ (Faserachse ungerichtet, Kraftrichtungs-Vorzeichen
 * irrelevant für Faserwinkel).
 */
public object HankinsonWinkel {

    /** Vektor-Variante: F kann Nullvektor / nicht-finit sein. */
    public fun von(
        kraft: Vektor,
        faserrichtung: Einheitsvektor,
    ): Resultat<Double, EntartetGeometrie> {
        if (!kraft.istFinit()) return Resultat.Fehler(EntartetGeometrie.NichtFinit)
        if (kraft.istNullvektor()) return Resultat.Fehler(EntartetGeometrie.Nullrichtung)
        val cosAbs = (abs(faserrichtung dot kraft) / kraft.norm).coerceIn(0.0, 1.0)
        return Resultat.Erfolg(acos(cosAbs))
    }

    /** Einheitsvektor-Variante: strukturell nicht fehlschlagbar. */
    public fun von(
        kraftrichtung: Einheitsvektor,
        faserrichtung: Einheitsvektor,
    ): Double = acos(abs(kraftrichtung dot faserrichtung).coerceIn(0.0, 1.0))
}
```

- **Einheit**: α intern in Radiant (Double). Anzeige in Grad
  (CLAUDE.md-Konvention).
- **Wertebereich**: [0, π/2] = [0°, 90°].
- **Methodenname**: `von(...)` (deutsch, „Hankinson-Winkel **von** F
  und n̂") gemäß `project_kotlin_konventionen.md` (deutsche
  Bezeichner für Glossarbegriffe).
- **Toleranzen**: arccos-Argument auf [0, 1] geklemmt
  (`coerceIn`); Eingaben müssen `Einheitsvektor`-Norm-Invariante
  erfüllen (NORM_EPS-Toleranz geerbt).
- **Identität**: keine; reine Funktion / `object`.
- **Fehlerbehandlung**: kein `throw` für entartete Eingaben
  (CLAUDE.md, `project_kotlin_konventionen.md`). Stattdessen
  `Resultat<Double, EntartetGeometrie>` mit den vorhandenen
  Varianten:
  - **‖F‖² ≤ NORM_EPS**: `Resultat.Fehler(EntartetGeometrie.Nullrichtung)`.
  - **F enthält NaN / ±∞**: `Resultat.Fehler(EntartetGeometrie.NichtFinit)`.
  - Die Einheitsvektor-Variante kann strukturell nicht fehlschlagen
    (Norm-Invariante per Typ; `coerceIn` fängt Float-Rundung).
- **Edge Cases**:
  - **Faserrichtung antiparallel zur Kraft**: α = 0 (nicht π); der
    Betrag im Skalarprodukt sichert dies.
  - **Faserrichtung rechtwinklig zur Kraft**: α = π/2.
  - **Werkstoff Modus KEINE**: α nicht zutreffend; Aufrufer muss
    Modus prüfen, bevor er α anfragt. Eine eigene Klassifikations-
    schicht (Werkstoff-Modus → α-Verfügbarkeit) ist Folgearbeit.
- **Folgearbeit (YAGNI-ausgelagert)**:
  - **`alphaProLage(...)`** für Mehrlagenholz (Blass/Flaig 2012):
    sobald `Lagenstruktur` modelliert ist, einen Iterator über die
    Lagen anbieten, der `von(F, ℓ_i.faserrichtung)` je Lage aufruft.
    Trigger: erstmaliges Anlegen von `domain/holzbau/`.
  - **Hankinson-Formel** `f_α = f_0·f_90 / (f_0·sin²α + f_90·cos²α)`:
    Bemessungs-Schicht (DIN EN 1995-1-1, SIA 265). Trigger:
    erstmalige Bemessungs-Tools.
  - **OSB-Bezugsachse** auf `plattenlaengsrichtung` umstellen:
    sobald Plattenwerkstoff-Werkstoffklasse modelliert ist, Faktor
    aus `werkstoff.faserrichtungsModus` ableiten.
- **Verwendungsregel**: Bemessungsfunktionen (f_α, f_h,α,k) in der
  späteren Bemessungs-Schicht nehmen `HankinsonWinkel.von(...)` als
  Eingangsgröße. Die Geometrie-Schicht stellt α; die
  Bemessungs-Schicht setzt es in EC5-Formeln ein.

## Quellen

**Primär (normativ und originär):**

- Hankinson, R. L.: „Investigation of Crushing Strength of Spruce
  at Varying Angles of Grain". Air Service Information Circular
  Vol. III, No. 259, U.S. Air Service, 1921.
- DIN EN 1995-1-1:2010-12, „Eurocode 5: Bemessung und Konstruktion
  von Holzbauten – Teil 1-1", Gleichungen 6.16, 8.31, 8.32.
- SIA 265:2021, „Holzbau", Anhang A.

**Sekundär:**

- Blass, H. J.; Sandhaas, C.: *Ingenieurholzbau – Grundlagen der
  Bemessung.* KIT Scientific Publishing, Karlsruhe 2016.
- Blaß, H. J.; Flaig, M.: *Stabförmige Bauteile aus
  Brettsperrholz.* KIT Scientific Publishing, Karlsruhe 2012,
  DOI 10.5445/KSP/1000030362.
- Forest Products Laboratory: *Wood Handbook FPL-GTR-282.* USDA,
  Madison WI 2021.
- Niemz, P.; Sonderegger, W.: *Physik des Holzes und der
  Holzwerkstoffe.* Hanser, München 2017.
- Mönck, W.; Rug, W.: *Holzbau – Bemessung und Konstruktion.*
  16. Aufl., Beuth, Berlin 2015.

**Korpus (nicht autoritativ):**

- Wikipedia, Lemma „Hankinson's equation" (abgerufen 2026-05-08).
