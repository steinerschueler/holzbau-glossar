---
id: plattenlaengsrichtung
benennung: Plattenlängsrichtung
synonyme: ["Strand-Längsrichtung", "Plattenlängsachse", "Decklagen-Strandrichtung", "OSB-Längsrichtung"]
abgelehnte_benennungen: [Plattenlangseite, Plattenlangskante, Plattenrichtung, "panel longitudinal direction", "strand direction"]
oberbegriff: einheitsvektor
begriffstyp: merkmal
voraussetzungen: [vektor, einheitsvektor, plattendicken_achse, toleranzen]
abgrenzung_zu: [einheitsvektor, faserrichtung, haupttragrichtung, nebentragrichtung, plattendicken_achse, bauteilachse]
status: entwurf
theorie_pflichtig: required
quellen_primär:
  - "DIN EN 300:2006-09, 'Platten aus langen, schlanken, gerichteten Spänen (OSB) – Definitionen, Klassifizierung und Anforderungen', Abschnitt 3 (Begriffe): Plattenlängsrichtung als Strand-Längsrichtung der Decklagen, parallel zur längeren Plattenformat-Kante."
  - "DIN EN 1995-1-1:2010-12 (Eurocode 5), Abschnitt 9 (Plattenwerkstoffe und Bauteile aus Plattenwerkstoffen), Festigkeiten f_m,0 und f_m,90 für OSB als Funktion der Plattenlängsrichtung."
  - "DIN EN 12369-1:2001-04, 'Holzwerkstoffe – Charakteristische Werte für die Berechnung und Bemessung von Holzbauwerken – Teil 1: OSB, Spanplatten und Faserplatten', Tabelle 1 (OSB/2, OSB/3, OSB/4: f_m,0, f_m,90, E_m,0, E_m,90 mit Index 0 = Plattenlängsrichtung, Index 90 = Plattenquerrichtung)."
  - "DIN EN 13986:2015-06, 'Holzwerkstoffe zur Verwendung im Bauwesen', Abschnitt 5 (Plattenmaße: Länge × Breite × Dicke); standardisierte Plattenformate z. B. 2500 × 1250 mm, mit Plattenlängsrichtung parallel zur 2500-mm-Kante."
quellen_sekundär:
  - "Niemz, P.; Sonderegger, W.: Physik des Holzes und der Holzwerkstoffe. Hanser, München 2017, Kap. 7 (OSB, Strand-Orientierung)."
  - "Blass, H. J.; Sandhaas, C.: Ingenieurholzbau – Grundlagen der Bemessung. KIT Scientific Publishing, Karlsruhe 2016, Kap. 3 (OSB)."
  - "EGGER Holzwerkstoffe: Datenblatt EGGER OSB 4 TOP, EGGER OSB 3 (Plattenformate, Plattenlängsrichtung)."
  - "Kronospan: Datenblatt Kronoply OSB 3, Kronoply OSB 4."
quellenkonflikt: |
  Die normativen Quellen DIN EN 300, EN 1995-1-1 Abschnitt 9 und
  EN 12369-1 verwenden „Plattenlängsrichtung" als Strand-Längsrichtung
  der OSB-Decklagen, parallel zur längeren Plattenformat-Kante;
  die Plattenfestigkeiten sind über Index 0 (parallel) und Index 90
  (rechtwinklig) zu dieser Richtung tabelliert. Die Hersteller-Datenblätter
  (EGGER, Kronospan) bestätigen diese Konvention.

  Eigene Festlegung in diesem Glossar:

  - Die **Plattenlängsrichtung** ist der Einheitsvektor in W, in der
    Plattenebene, in Richtung der Strand-Längsrichtung der Decklagen
    (parallel zur längeren Plattenformat-Kante).
  - Sie ist Pflichtfeld bei Werkstoffen mit Faserrichtungs-Modus
    SCHWACH (`gerichteter_plattenwerkstoff`, zum Stand 2026 nur OSB).
  - **Default-Konvention**: Wenn am Werkstoff nicht explizit gesetzt,
    gilt `plattenlaengsrichtung := bauteil.lokale_x_achse`,
    wobei die lokale x-Achse per Konstruktionsregel parallel zur
    längeren Plattenformat-Kante liegt (Plattenformat z. B.
    2500 × 1250 → 2500-mm-Richtung).
  - **Orthogonalität zur Plattendicken-Achse** ist
    Konstruktions-Invariante:
    `⟨plattenlaengsrichtung, plattendicken_achse⟩ ≤ WINKEL_EPS`.
  - Die Vorzeichenkonvention ist konventionell und beim Bauteil zu
    dokumentieren; alle EC5-Festigkeitswerte (f_m,0, f_m,90) sind
    vorzeicheninvariant.

  Die Plattenlängsrichtung ist nicht zu verwechseln mit der
  **Haupttragrichtung** (`haupttragrichtung`): die Haupttragrichtung
  ist dem Modus STRUKTURIERT (Mehrlagenholz) vorbehalten und
  bezeichnet die Decklamellen-Richtung mit höherer Steifigkeit
  (ProHolz). Bei Mehrlagenholz wird die Plattenlängsrichtung **nicht**
  als eigenständiges Pflichtfeld geführt, weil die Steifigkeit dort
  über die Lagenstruktur und die Haupttragrichtung bestimmt ist.
---

## Prosa-Definition

Die **Plattenlängsrichtung** eines gerichteten Plattenwerkstoffs ist
ein Einheitsvektor im Welt-Koordinatensystem, der in der Plattenebene
liegt, rechtwinklig zur Plattendicken-Achse steht und in Richtung der
Strand-Längsrichtung der Decklagen (typisch parallel zur längeren
Plattenformat-Kante) zeigt, an dem die anisotropen Plattenfestigkeiten
f_m,0 (parallel) und f_m,90 (rechtwinklig) nach DIN EN 1995-1-1 / DIN EN
12369-1 ausgerichtet sind.

## Mathematische Definition

Sei

- ê_d ∈ S² die Plattendicken-Achse (siehe `plattendicken_achse`),
- ê_l ∈ S² ein Einheitsvektor (siehe `einheitsvektor`),
- B ein gerichtetes Plattenbauteil (siehe
  `gerichteter_plattenwerkstoff`; hier nur als Träger der Annotation
  vorausgesetzt).

Dann ist die **Plattenlängsrichtung** des Plattenbauteils B eine
Annotation

```
plattenlaengsrichtung(B) := ê_l ∈ S²,
```

mit der Orthogonalitäts-Invariante zur Plattendicken-Achse

```
⟨ê_l, ê_d⟩ = 0     (mathematische Idealform)
```

bzw. in der Domänen-Schicht prüfbar

```
| ⟨ê_l, ê_d⟩ | ≤ Toleranzen.WINKEL_EPS     (numerische Form).
```

**Default-Konvention** (prüfbare Konstruktionsregel):

```
Wenn plattenlaengsrichtung am Werkstoff nicht explizit gesetzt,
gilt für ein Plattenbauteil B mit Werkstoff-Modus SCHWACH:
  plattenlaengsrichtung(B) := bauteil_lokale_x_achse(B),
```

wobei die lokale x-Achse per Konstruktionsregel parallel zur
längeren Plattenformat-Kante (z. B. 2500-mm-Richtung bei Format
2500 × 1250 mm) liegt.

**Plattenquerrichtung** (abgeleitet, redundant):

```
ê_q := ê_d × ê_l ∈ S²,
```

mit ‖ê_q‖ = 1 wegen ⟨ê_l, ê_d⟩ = 0 und ‖ê_l‖ = ‖ê_d‖ = 1. Die
Plattenquerrichtung ist die zur Plattenlängsrichtung in der
Plattenebene rechtwinklige Richtung.

**Faserwinkel zur Kraft** (für Hankinson-Auswertung bei OSB):

```
α(F̂, ê_l) := arccos( | ⟨F̂, ê_l⟩ | ) ∈ [0, π/2]
```

(siehe `hankinson_winkel`); EC5-Tabellen führen für OSB die
diskreten Werte f_m,0 (α = 0) und f_m,90 (α = π/2), die Hankinson-
Interpolation ist abgeschwächt zulässig.

## Wohldefiniertheit

- **Existenz**: Für jedes nach DIN EN 300 zertifizierte OSB-Produkt
  ist die Strand-Längsrichtung der Decklagen produktnormativ
  definiert; sie ist parallel zur längeren Plattenformat-Kante. Die
  Plattenformate sind in DIN EN 13986 standardisiert (typ. 2500 ×
  1250 mm, 2440 × 1220 mm).
- **Eindeutigkeit bis auf Vorzeichen**: ê_l ist als Annotation eines
  Plattenbauteils eindeutig, sobald eine Vorzeichenkonvention
  festgelegt ist. Im Regelfall wird ê_l in dieselbe Halbachse wie die
  längere Plattenformat-Kante (von Anfangs- zu Endpunkt) gesetzt;
  alle EC5-Festigkeiten f_m,0 / f_m,90 sind vorzeicheninvariant.
- **Pflichtcharakter**: Bei Werkstoff-Modus SCHWACH ist
  `plattenlaengsrichtung` Pflichtfeld am Werkstoff (siehe
  `gerichteter_plattenwerkstoff`). Bei den anderen Modi nicht
  definiert.
- **Orthogonalitäts-Invariante**: ⟨ê_l, ê_d⟩ ≈ 0 ist Konstruktions-
  Invariante; eine Verletzung ist Validierungsfehler.
- **Norm-Invariante**: ê_l erbt | ‖ê_l‖² − 1 | ≤
  Toleranzen.NORM_EPS aus `einheitsvektor`.
- **Default-Auflösung**: Die Konvention `plattenlaengsrichtung :=
  bauteil.lokale_x_achse` ist Konstruktionsregel, nicht
  Erlaubnis-Mechanismus zum Weglassen. Nach Auflösung muss ein
  konkreter Vektor in S² mit erfüllter Orthogonalitäts-Invariante
  vorliegen.
- **Nicht-Zirkularität**: Die Definition stützt sich auf
  `vektor`, `einheitsvektor`, `plattendicken_achse`, `toleranzen`.
  Sie verweist nicht auf ihre Geschwister-Plattenrichtungen
  (Haupttragrichtung, Nebentragrichtung) in der eigenen Definition,
  sondern grenzt sich nur über den Modus ab.

## Erläuterung (nicht normativ)

### OSB-Strand-Schichtung

OSB (Oriented Strand Board, DIN EN 300) wird aus drei oder mehr
Schichten von langen, schlanken Holzspänen (Strands) gepresst. Die
Strands der **Decklagen** sind in einer Vorzugsrichtung gerichtet
(Plattenlängsrichtung), die der **Mittellage** typisch um 90°
gekreuzt. Diese kreuzweise Schichtung ähnelt strukturell dem
Sperrholz, aber:

- Die Strands sind keine durchgehenden Furniere, sondern Späne von
  ca. 50 × 25 × 0,6 mm.
- Die Streuung der Strand-Orientierung ist hoch (typ. ±15° um die
  Vorzugsrichtung).
- DIN EN 12369-1 führt für OSB **gemittelte Plattenfestigkeiten**
  f_m,0 und f_m,90 mit nur einem Index 0 / 90 — keine
  Einzellagen-Bemessung wie bei BSP.

Aus diesem Grund wird OSB im Glossar als
`gerichteter_plattenwerkstoff` (Modus SCHWACH) geführt, **nicht**
als `mehrlagenholz` (Modus STRUKTURIERT).

### Plattenformat-Konvention

OSB-Standardformate (DIN EN 13986):

| Format         | Längere Kante | Plattenlängsrichtung |
|----------------|----------------|----------------------|
| 2500 × 1250 mm | 2500 mm        | parallel zu 2500 mm  |
| 2440 × 1220 mm | 2440 mm        | parallel zu 2440 mm  |
| 2500 × 675 mm  | 2500 mm        | parallel zu 2500 mm  |
| 5000 × 2500 mm | 5000 mm        | parallel zu 5000 mm  |

Hersteller-Datenblätter (EGGER, Kronospan) bestätigen diese
Konvention. Die App nimmt diese Konvention als Default
(`plattenlaengsrichtung := bauteil.lokale_x_achse`); abweichende
Verlegungen (z. B. OSB-Brett quer eingebaut) müssen durch
explizites Setzen modelliert werden.

### Bemessungs-Konsequenz

Bei einem Wandbeplankung aus OSB ist der Schubfluss in
Plattenlängsrichtung mit höherer Steifigkeit aufgenommen als
quer. Bei Aussteifungsscheiben ist die Plattenlängsrichtung
typisch in Wand-Höhenrichtung verlegt, um die Steifigkeit
parallel zur Schubbeanspruchung zu maximieren.

## Beziehungen

- **Oberbegriff**: `einheitsvektor`. Strukturell ist die
  Plattenlängsrichtung ein Einheitsvektor; das OSB-Spezifikum ist
  die semantische Rolle „Strand-Längsrichtung der Decklagen".
- **Verwendung**:
  - **Gerichteter Plattenwerkstoff**
    (`gerichteter_plattenwerkstoff`): Pflichtfeld; einziges
    Plattenebene-Richtungsfeld.
  - **Bauteil** (`bauteil`): Plattenlängsrichtung wird per Default
    aus der lokalen x-Achse abgeleitet.
  - **Hankinson-Winkel** (`hankinson_winkel`): bei OSB als
    Faser-Bezugsachse für α (abgeschwächt anwendbar; EC5 nutzt
    primär die diskreten f_m,0 / f_m,90).
- **Abgrenzung**:
  - **`einheitsvektor`** (allgemein): trägt keine semantische
    Rolle.
  - **`faserrichtung`**: Faserrichtung im engeren Sinn ist die
    L-Richtung der Holzfaser; bei OSB ist die makroskopische
    „Faserrichtung" eine **gemittelte Strand-Richtung**, daher der
    eigenständige Begriff Plattenlängsrichtung. Strukturell ist
    sie ein Einheitsvektor in der Plattenebene wie `faserrichtung`,
    aber die Bemessungsformeln (f_m,0, f_m,90) sind diskret und
    nicht Hankinson-interpolationsfähig im strengen Sinn.
  - **`haupttragrichtung`**: bei Mehrlagenholz Pflichtfeld; bei
    OSB nicht verwendet, weil OSB keine Lagen-Mechanik hat. Die
    beiden Begriffe sind disjunkt und werden durch den Werkstoff-
    Modus auseinandergehalten.
  - **`plattendicken_achse`**: rechtwinklig zur Plattenebene;
    Plattenlängsrichtung liegt **in** der Plattenebene
    (rechtwinklig zur Plattendicken-Achse).
  - **`bauteilachse`**: geometrische Längsachse eines Stabbauteils;
    bei Plattenbauteilen nicht direkt anwendbar. Die lokale x-Achse
    eines Plattenbauteils ist die Default-Plattenlängsrichtung.

## Implementierungshinweis

Datentyp (Domänen-Schicht, Kotlin, Schicht
`domain.holzbau.werkstoff`):

```kotlin
package domain.holzbau.werkstoff

import domain.geometrie.Einheitsvektor

/**
 * Plattenlängsrichtung eines gerichteten Plattenwerkstoffs (OSB):
 * Einheitsvektor in der Plattenebene, parallel zur Strand-
 * Längsrichtung der Decklagen.
 * Glossar: hg_plattenlaengsrichtung.md
 *
 * Strukturell ein Wrapper um Einheitsvektor; semantische Rolle
 * 'Plattenlängsrichtung des Modus SCHWACH'. Pflichtfeld bei
 * GerichteterPlattenwerkstoff.
 *
 * Default-Konvention: Wenn am Werkstoff nicht explizit gesetzt,
 * gilt plattenlaengsrichtung := bauteil.lokale_x_achse.
 *
 * Konstruktions-Invariante: orthogonal zur Plattendicken-Achse
 * (innerhalb WINKEL_EPS).
 */
@JvmInline
value class Plattenlaengsrichtung(val richtung: Einheitsvektor) {
    val x: Double get() = richtung.x
    val y: Double get() = richtung.y
    val z: Double get() = richtung.z

    operator fun unaryMinus(): Plattenlaengsrichtung =
        Plattenlaengsrichtung(-richtung)
}
```

- **Einheit**: dimensionslos (geerbt).
- **Invariante**: alle Invarianten von `Einheitsvektor` plus
  Orthogonalität zur Plattendicken-Achse:
  `| richtung dot plattendickenAchse | ≤ Toleranzen.WINKEL_EPS`.
- **Vorzeichenkonvention**: typisch in dieselbe Halbachse wie die
  längere Plattenformat-Kante; alle EC5-Festigkeiten sind
  vorzeicheninvariant.
- **Konsistenzprüfungen** (am verwendenden Werkstoff prüfen, bei
  Verletzung `Resultat.Fehler`):
  1. Norm-Invariante (geerbt).
  2. Orthogonalität zur Plattendicken-Achse innerhalb WINKEL_EPS.
- **Edge Cases**:
  - **Verletzte Orthogonalität**:
    `Entartet.PlattenlaengsrichtungNichtOrthogonalZurPlattendickenAchse`.
  - **Plattenlängsrichtung bei nicht-OSB-Werkstoff**:
    Validierungsfehler; nicht erlaubt bei Modus HART, STRUKTURIERT,
    KEINE.
  - **Quer eingebautes OSB-Brett** (Plattenlängsrichtung
    ≠ längere Plattenformat-Kante): zulässig durch explizites Setzen,
    aber Plausibilitätswarnung in der Bemessungs-Schicht (verlustige
    Steifigkeit in Hauptbeanspruchungsrichtung).

## Quellen

**Primär (normativ):**

- DIN EN 300:2006-09, „Platten aus langen, schlanken, gerichteten
  Spänen (OSB)".
- DIN EN 1995-1-1:2010-12, „Eurocode 5", Abschnitt 9.
- DIN EN 12369-1:2001-04, „Holzwerkstoffe – Charakteristische
  Werte – Teil 1: OSB, Spanplatten und Faserplatten".
- DIN EN 13986:2015-06, „Holzwerkstoffe zur Verwendung im
  Bauwesen".

**Sekundär:**

- Niemz, P.; Sonderegger, W.: *Physik des Holzes und der
  Holzwerkstoffe.* Hanser, München 2017.
- Blass, H. J.; Sandhaas, C.: *Ingenieurholzbau – Grundlagen der
  Bemessung.* KIT Scientific Publishing, Karlsruhe 2016.
- EGGER Holzwerkstoffe, Datenblatt OSB 4 TOP / OSB 3 (abgerufen
  2026-05-08).
- Kronospan, Datenblatt Kronoply OSB 3 / OSB 4 (abgerufen
  2026-05-08).

**Korpus (nicht autoritativ):**

- Wikipedia, Lemma „Oriented Strand Board" (abgerufen 2026-05-08).
