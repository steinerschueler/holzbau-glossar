---
id: achse
benennung: Achse
synonyme: ["Bezugslinie", "Bezugsachse (allgemein)", "axis"]
abgelehnte_benennungen: [Mittellinie, Linie, Strahl, "axis line", "centerline"]
oberbegriff: gerade
begriffstyp: generisch
voraussetzungen: [gerade, vektor, einheitsvektor, toleranzen]
abgrenzung_zu: [gerade, strecke, halbgerade, vektor, faserrichtung]
status: entwurf
theorie_pflichtig: required
quellen_primär:
  - "DIN ISO 80000-2:2022-08, 'Größen und Einheiten – Teil 2: Mathematik', Abschnitt 2 (Geometrie und Vektoren), Bezeichnungen für Achsen, Symmetrieachsen und Koordinatenachsen."
  - "ISO 80000-2:2019, Abschnitt 2 'Mathematics – Geometry', Eintrag 'axis'."
quellen_sekundär:
  - "Bronstein, I. N. et al.: Taschenbuch der Mathematik. Kap. 3.5.1 'Geraden im Raum' und Kap. 3.6 'Symmetrien' (Symmetrie- und Drehachsen)."
  - "Bär, C.: Elementargeometrie. Springer Spektrum, Kap. 4 (Geraden und Achsen)."
  - "Fischer, G.: Lineare Algebra. 19. Aufl., Springer Spektrum 2020, Kap. 4 (Eigenwerte, Drehachsen)."
quellenkonflikt: |
  Weder DIN ISO 80000-2 noch die Holzbau-Normen (SIA 265, EN 1995-1-1,
  DIN 1052) liefern eine geschlossene Definition des Begriffs „Achse".
  In allen konsultierten Quellen wird „Achse" vorausgesetzt und durch
  ihre Rolle qualifiziert: Symmetrieachse, Drehachse, Bezugsachse,
  Koordinatenachse, Bauteilachse, Sparrenachse, Wirkungslinie. Die
  mathematische Sekundärliteratur (Bronstein, Bär, Fischer) verwendet
  „Achse" durchgängig im Sinne einer Geraden, die in einem konkreten
  Bezugsrahmen eine ausgezeichnete Rolle erfüllt.

  Eigene Festlegung: eine Achse ist strukturell eine Gerade in ℝ³,
  versehen mit einer semantischen Rolle, die ihre Bedeutung im
  jeweiligen Kontext festlegt (Symmetrie, Drehung, Bezug, Koordinate,
  Bauteilhauptachse). Die Achse ist damit kein eigenes geometrisches
  Primitiv neben der Geraden, sondern eine **Annotation** an einer
  Geraden — vergleichbar zur Beziehung zwischen `einheitsvektor` und
  `faserrichtung`. Diese Festlegung ist konsistent mit allen
  konsultierten Quellen.
---

## Prosa-Definition

Eine **Achse** ist eine Gerade in ℝ³, versehen mit einer
ausgezeichneten semantischen Rolle (Symmetrie-, Dreh-, Bezugs-,
Koordinaten- oder Bauteilhauptachse), die ihre Bedeutung im
jeweiligen Bezugsrahmen festlegt; geometrisch ist sie nicht mehr
und nicht weniger als ihre Trägergerade.

## Mathematische Definition

Sei

- g ⊂ ℝ³ eine Gerade im Sinne von `gerade`,
- 𝓡 eine endliche Menge zulässiger **Achsenrollen**, mindestens
  ```
  𝓡 ⊇ { Symmetrie, Drehung, Bezug, Koordinate, Bauteilhauptachse }.
  ```

Dann ist eine **Achse** A ein Tupel

```
A := (g, ρ)   mit ρ ∈ 𝓡,
```

bestehend aus der **Trägergeraden** g und der **Rolle** ρ. Die durch
A bezeichnete Punktmenge in ℝ³ ist die der Trägergeraden:

```
|A| := g.
```

Eine Achse kann zusätzlich **gerichtet** sein: dann gehört zur Rolle
ρ die Wahl eines Einheits-Richtungsvektors d_hat ∈ S² mit d_hat ∈ ℝ·v
(v ein Richtungsvektor von g). Im ungerichteten Fall ist die Achse
nur durch g und ρ bestimmt; die zwei möglichen Vorzeichen von d_hat
sind dann äquivalent.

Wesentliche Spezialisierungen ergeben sich aus der Wahl von ρ:

- **Symmetrieachse** (ρ = Symmetrie): g ist Fixpunktmenge einer
  Spiegelung S_g : ℝ³ → ℝ³ einer betrachteten Punktmenge X ⊂ ℝ³,
  d. h. S_g(X) = X.
- **Drehachse** (ρ = Drehung): g ist die Fixpunktmenge einer
  Drehung R_{g, φ} ∈ SO(3) um den Winkel φ ≠ 0; gerichtete
  Variante mit d_hat legt den Drehsinn (rechtshändig zu d_hat) fest.
- **Bezugsachse** (ρ = Bezug): g dient als Referenz für Abstände
  und Winkel anderer geometrischer Objekte (z. B. „Höhe über
  Trauflinie", „Abstand zur Firstachse").
- **Koordinatenachse** (ρ = Koordinate): g geht durch den Ursprung
  eines Koordinatensystems und trägt einen Richtungs-Einheits-
  vektor; eine der drei kanonischen Achsen x, y, z eines
  Rechtssystems.
- **Bauteilhauptachse** (ρ = Bauteilhauptachse): g ist die
  geometrische Hauptachse eines Bauteils; Spezialisierung
  `bauteilachse`.

## Wohldefiniertheit

- **Existenz**: Für jede Gerade g ∈ ℝ³ und jede Rolle ρ ∈ 𝓡 ist
  A = (g, ρ) wohldefiniert; die Menge der Achsen ist nicht-leer,
  da bereits jede Koordinatenachse eines beliebigen Rechtssystems
  ein Beispiel ist.
- **Repräsentantenwahl der Trägergeraden**: Die Achse erbt die
  Repräsentanten-Invarianz der Geraden (siehe `gerade`,
  Wohldefiniertheit): Skalierung und Translation des
  Richtungsvektor-/Stützpunkt-Repräsentanten ändern die Achse als
  Tupel (g, ρ) nicht, da g als Punktmenge unverändert bleibt.
- **Vorzeichenkonvention**: Im ungerichteten Fall sind (g, ρ) und
  (g, ρ) mit „umgekehrter" Richtungsrepräsentation dieselbe Achse.
  Im gerichteten Fall (mit d_hat) sind (g, ρ, d_hat) und (g, ρ, −d_hat) als
  Punktmengen identisch, aber als orientierte Achsen verschieden.
  Die Festlegung, ob eine Achse gerichtet ist, ist Eigenschaft der
  Rolle ρ und beim verwendenden Begriff zu dokumentieren.
- **Konsistenz Rolle ↔ Geometrie**: Wenn ρ = Drehung, muss die
  Drehung um g eine wohldefinierte Isometrie ℝ³ → ℝ³ sein; das ist
  für jede Gerade g und jeden Winkel φ erfüllt. Wenn ρ = Symmetrie
  bezogen auf eine Punktmenge X, muss S_g(X) = X gelten; diese
  Konsistenz ist Eigenschaft des verwendenden Kontexts und nicht
  der Achse selbst.
- **Nicht-Zirkularität**: Die Definition stützt sich nur auf
  `gerade`, `vektor`, `einheitsvektor` und `toleranzen`. Die Rolle
  ρ ist ein Element einer aufzählbaren Menge 𝓡, deren Mitglieder
  außerhalb der Geometrie definiert sind (Symmetrie, Drehung als
  Gruppentheorie-Begriffe; Bezug, Koordinate als Modellierungs-
  konventionen).
- **Eliminierbarkeit**: Jede Verwendung des Begriffs „Achse" lässt
  sich durch „Gerade in der Rolle ρ" ersetzen. Die Achse trägt
  geometrisch nichts hinzu, was nicht schon in der Geraden steht;
  der Mehrwert liegt in der typsicheren Kommunikation der Rolle.

## Erläuterung (nicht normativ)

Der Begriff „Achse" ist in der Geometrie und insbesondere im
Holzbau allgegenwärtig, ohne präzise definiert zu sein. Er
bezeichnet stets dasselbe Strukturobjekt — eine Gerade — qualifiziert
durch eine **Rolle**, die im Kontext klar sein muss: Sparrenachse,
Pfettenachse, Stützenachse, Trauflinie, Firstachse, Symmetrieachse
eines Daches, Drehachse eines Schwenkdaches.

Die Entscheidung, „Achse" als **Annotation** an einer Geraden zu
modellieren und nicht als eigenes Primitiv, vermeidet eine
Begriffshypertrophie: eine Symmetrieachse und eine Drehachse sind
geometrisch identisch (beide sind Geraden); sie unterscheiden sich
nur in dem, wofür sie gerade gebraucht werden. Diese Modellierung
ist parallel zu `faserrichtung`, das ein `einheitsvektor` mit einer
semantischen Rolle ist.

In der Praxis bedeutet das: die App-Domäne kennt die Klasse
`Gerade` als Geometrie-Primitiv und führt für jede konkrete
Achsenrolle einen eigenen Typ (z. B. `Bauteilachse`,
`Koordinatenachse`), der eine Gerade kapselt und zusätzliche
Constraints und Operationen bereitstellt. Der Glossar-Begriff
„Achse" ist der gemeinsame Oberbegriff dieser Spezialisierungen.

Polysemie-Hinweis: das Wort „Achse" hat im Schweizer
Zimmermannssprachgebrauch außerdem die Lesart „Reihe von Stützen
oder Stielen entlang einer gemeinsamen geometrischen Achse" (z. B.
„Achse A", „Achse 1"). Diese Lesart ist hier **nicht** definiert;
sie wäre eine Spezialisierung „Bauwerksachse" oder
„Konstruktionsachse" und wird in einem eigenen Eintrag behandelt.

## Beziehungen

- **Oberbegriff**: `gerade`. Strukturell ist eine Achse eine
  Gerade; die Rolle ρ ist eine Annotation an dieser Geraden.
- **Spezialisierungen (eigene Einträge folgen)**:
  - **Symmetrieachse** (`symmetrieachse`): Achse einer Spiegelung.
  - **Drehachse** (`drehachse`): Achse einer Drehung; gerichtet.
  - **Bezugsachse** (`bezugsachse`): Referenzachse für Abstände
    und Winkel.
  - **Koordinatenachse** (`koordinatenachse`): kanonische Achse
    eines Koordinatensystems; durch den Ursprung mit
    Richtungs-Einheitsvektor.
  - **Bauteilachse** (`bauteilachse`): geometrische Hauptachse
    eines Bauteils; Spezialisierung mit Bezug auf einen
    Bauteilkörper.
- **Bestandteile (partitiv)**: keine eigenen; die partitiven
  Bestandteile der Trägergeraden gelten (siehe `gerade`).
- **Abgrenzung**:
  - **Gerade** (`gerade`): die geometrische Substanz ohne Rolle.
    Jede Achse ist eine Gerade plus Rolle; jede Gerade kann durch
    Annotation einer Rolle zur Achse gemacht werden. Die zwei
    Begriffe sind nicht synonym, aber die Punktmenge ist dieselbe.
  - **Strecke** (`strecke`): begrenzt; eine Achse ist
    konzeptionell unbegrenzt. Die Trägergerade einer
    Bauteilachsen-Strecke ist eine Achse im Sinne dieses Eintrags;
    die Strecke selbst nicht.
  - **Halbgerade** (`halbgerade`): einseitig begrenzt; nicht
    Achse. Eine gerichtete Achse hat zwar eine Richtung, ist aber
    beidseitig unbegrenzt.
  - **Vektor** (`vektor`): ortsfreie Verschiebung; eine Achse hat
    Ortsbindung (geht durch konkrete Punkte des Raums). Der
    Richtungsvektor einer Achse ist ein Vektor, die Achse selbst
    nicht.
  - **Faserrichtung** (`faserrichtung`): Einheitsvektor in einer
    Materialrolle; ortsfrei. Eine Faserrichtung ist keine Achse
    in diesem Sinne. Eine Bauteilachse ist eine Achse; die
    Faserrichtung beschreibt die Materialhauptrichtung relativ
    zum Bauteilkörper, nicht eine Gerade in ℝ³.

## Implementierungshinweis

Der Glossarbegriff „Achse" wird in der Domänen-Schicht
(`zimmermann.domain.geometrie`, D4-Stand) als schlanker
**Wrapper-Datentyp** über einer `Gerade` realisiert, der die
Achsenrolle ρ als Aufzählung trägt. Strukturell ist `Achse` damit
keine `sealed interface` mit Subtyp pro Rolle, sondern eine
`data class`. Die im Glossar als Spezialisierungen genannten
Achsenrollen (Symmetrieachse, Drehachse, Bezugsachse,
Koordinatenachse, Bauteilhauptachse) werden als Enum-Konstanten
geführt; rollenspezifische Operationen sind in D4 noch nicht
erforderlich und werden als Folgearbeit hinzugefügt, wenn sie
gebraucht werden (siehe „Folgearbeit" unten).

Datentyp (Domänen-Schicht, Kotlin, Schicht
`zimmermann.domain.geometrie`):

```kotlin
package zimmermann.domain.geometrie

/**
 * Achse als Annotation einer Geraden mit semantischer Rolle.
 * Glossar: hg_achse.md
 */
public data class Achse(
    public val gerade: Gerade,
    public val rolle: AchsenRolle = AchsenRolle.UNSPEZIFIZIERT,
)

public enum class AchsenRolle {
    SYMMETRIEACHSE,
    DREHACHSE,
    BEZUGSACHSE,
    KOORDINATENACHSE,
    BAUTEILHAUPTACHSE,
    UNSPEZIFIZIERT,
}
```

- **Einheit**: erbt von `gerade` (Stützpunkt-Koordinaten in mm,
  Richtungsvektor-Komponenten dimensionslos bis auf Skalierung).
- **Rolle als Datenfeld vs. Typinformation**: D4-pragmatisch wird
  die Rolle ρ als `enum`-Feld gespeichert, **nicht** über
  Subtypen. Begründung: in der aktuellen Phase gibt es keine
  rollenspezifischen Operationen, die ein Subtyp typsicher tragen
  müsste; ein Enum-Feld vermeidet Klassen-Hypertrophie. Wenn
  später rollenspezifische Operationen anfallen (z. B.
  `fun drehung(achse: Drehachse, winkel: Double): Lage`), werden
  die betreffenden Rollen als eigene Wrapper-Klassen herausgezogen
  (Folgearbeit).
- **Gerichtetheit**: Eine `Achse` über einer `Gerade` ist
  strukturell ungerichtet (`Gerade.umkehren()` liefert dieselbe
  Punktmenge). Gerichtete Achsen werden bei Bedarf durch eigene
  Klassen modelliert (analog zu `Bauteilachse`, die strukturell
  über `Strecke` läuft und damit gerichtet ist).
- **Strukturelle Beziehung zu `Bauteilachse`**: Die im Glossar
  ausgewiesene Hierarchie `bauteilachse oberbegriff achse` ist
  **semantisch** zu lesen, nicht als Kotlin-Vererbung. `Achse`
  (Wrapper über `Gerade`, unbegrenzt, ungerichtet) und
  `Bauteilachse` (Wrapper über `Strecke`, begrenzt, gerichtet)
  sind strukturell verschieden; eine Vererbung wäre semantisch
  falsch. Beide Klassen stehen unabhängig nebeneinander; die
  KDoc verweist explizit auf die Glossar-Hierarchie als
  semantische Beziehung.
- **Edge Cases / Entartet-Varianten**: Die `Gerade`-Factory fängt
  alle entarteten Eingaben ab (`Nullrichtung`, `NichtFinit`); die
  `Achse`-Konstruktion fügt keine zusätzlichen Invarianten hinzu
  und kann daher als nackte `data class` ohne Factory geführt
  werden. Inkonsistenz-Prüfungen Rolle ↔ Geometrie (z. B.
  Symmetrieachse einer konkreten Punktmenge) sind Sache der
  jeweiligen Anwendungsstelle, nicht der `Achse`-Klasse.
- **Identität / Gleichheit**: `equals` (data-class-Standard) ist
  strukturell-exakt; für geometrische Identität stellen die
  Methoden `istGleicheAchse(other, eps)` (Geraden-Identität UND
  gleiche Rolle) und `istGleicheAchsenLinie(other, eps)`
  (Geraden-Identität, Rolle ignoriert) zur Verfügung.
- **Verwendungsregel**: Funktionen, die eine Achse mit einer
  konkreten Rolle benötigen, prüfen `rolle` explizit oder nehmen
  einen rollenspezifischen Wrapper-Typ entgegen, sobald dieser
  eingeführt ist.

**Folgearbeit (trigger-basiert):**

- **Rollen als eigene Wrapper-Klassen** (`Drehachse`,
  `Koordinatenachse`, `Symmetrieachse`, `Bezugsachse`) — wenn
  rollenspezifische Operationen erforderlich werden (z. B.
  Drehung um eine Drehachse, Koordinatentransformation entlang
  einer Koordinatenachse). Bis dahin reicht die Enum-Rolle.
- **`sealed interface Achse` mit Subtypen statt Enum** — wenn
  mindestens zwei Rollen rollenspezifische API tragen und der
  Refactoring-Aufwand sich gegen den Vorteil typsicherer
  Operationen lohnt.

## Quellen

**Primär (normativ):**

- DIN ISO 80000-2:2022-08, „Größen und Einheiten – Teil 2:
  Mathematik".
- ISO 80000-2:2019, „Quantities and units – Part 2: Mathematics".

**Sekundär:**

- Bronstein, I. N.; Semendjajew, K. A.; Musiol, G.; Mühlig, H.:
  *Taschenbuch der Mathematik.* Edition Harri Deutsch, aktuelle
  Auflage, Kap. 3.5 und 3.6.
- Bär, C.: *Elementargeometrie.* Springer Spektrum, Kap. 4.
- Fischer, G.: *Lineare Algebra.* 19. Aufl., Springer Spektrum 2020,
  Kap. 4.

**Korpus (nicht autoritativ):**

- Wikipedia, Lemma „Achse (Geometrie)" (abgerufen 2026-05-08).
