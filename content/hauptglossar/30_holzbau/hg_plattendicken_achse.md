---
id: plattendicken_achse
benennung: Plattendicken-Achse
synonyme: ["Plattennormale", "Dickenrichtung", "Plattendickenrichtung", "out-of-plane axis"]
abgelehnte_benennungen: [Plattennormalvektor, Plattenachse, Z-Achse, "thickness direction", "panel normal"]
oberbegriff: einheitsvektor
begriffstyp: merkmal
voraussetzungen: [vektor, einheitsvektor, toleranzen]
abgrenzung_zu: [einheitsvektor, faserrichtung, plattenlaengsrichtung, haupttragrichtung, nebentragrichtung, bauteilachse]
status: entwurf
theorie_pflichtig: required
quellen_primär:
  - "DIN EN 13986:2015-06, 'Holzwerkstoffe zur Verwendung im Bauwesen – Eigenschaften, Bewertung der Konformität und Kennzeichnung', Abschnitt 5 (Plattenmaße: Länge × Breite × Dicke)."
  - "DIN EN 1995-1-1:2010-12 (Eurocode 5), Abschnitt 9 (Plattenwerkstoffe und Bauteile aus Plattenwerkstoffen): Plattenebene und Plattendickenrichtung als Bezugsachsen für Festigkeits- und Steifigkeitswerte."
  - "DIN EN 16351:2021-08 (Brettsperrholz), DIN EN 636:2015-06 (Sperrholz), DIN EN 300:2006-09 (OSB), DIN EN 312:2010-12 (Spanplatten), DIN EN 622-5:2010-01 (MDF) — alle führen die Plattendicke als dritten Plattenmaß-Wert (Länge × Breite × Dicke)."
  - "ISO 16739-1:2024, 'Industry Foundation Classes (IFC) — Part 1: Data schema', Entitäten `IfcMaterialLayerSet.LayerSetDirection`, Wert `AXIS3` (Plattendicken-Richtung). [direkt]"
quellen_sekundär:
  - "Schickhofer, G.; Bogensperger, T.; Moosbrugger, T. (Hrsg.): BSPhandbuch — Holz-Massivbauweise in Brettsperrholz. 2. Aufl., TU Graz 2010, Kap. 2 (Plattenkoordinatensystem)."
  - "ProHolz Austria: Brettsperrholz Bemessung Band I. Wien 2014, Kap. 2 (Lokales Plattenkoordinatensystem)."
  - "Niemz, P.; Sonderegger, W.: Physik des Holzes und der Holzwerkstoffe. Hanser, München 2017, Kap. 7 (Plattenwerkstoffe, Plattenkoordinaten)."
quellenkonflikt: |
  Die normativen Quellen DIN EN 13986, EN 1995-1-1 Abschnitt 9 und
  die werkstoffspezifischen Plattennormen (EN 16351, EN 636, EN 300,
  EN 312, EN 622) verwenden „Plattendicke" und „Plattenebene"
  konsistent: die Plattendicke ist der dritte (kleinste)
  Plattenmaß-Wert, die Plattenebene wird durch die beiden anderen
  Maße (Länge, Breite) aufgespannt. Eine formale Definition der
  „Plattendicken-Achse" als Einheitsvektor im Bauteil-
  Koordinatensystem führt keine dieser Normen explizit; sie wird
  jedoch durch IFC `IfcMaterialLayerSet.LayerSetDirection = AXIS3`
  und durch die Plattenkoordinatensystem-Konvention bei ProHolz und
  Schickhofer eindeutig vorausgesetzt.

  Eigene Festlegung in diesem Glossar:

  - Die **Plattendicken-Achse** ist der Einheitsvektor in W,
    rechtwinklig zur Plattenebene, der die Richtung der kleinsten
    Plattendimension (Plattendicke) angibt.
  - **Default-Konvention** (analog zur Bauteilachsen-Konvention bei
    stabförmigen Bauteilen `axiales_holz`):
    `plattendicken_achse := bauteil.lokale_z_achse`,
    wobei die lokale z-Achse des Bauteils per Konstruktionsregel
    rechtwinklig zu den beiden Plattenformat-Richtungen liegt.
    Diese Default-Regel ist prüfbar; nach Auflösung muss
    `plattendicken_achse ∈ S²` gelten.
  - Die Vorzeichenkonvention („Plattendicken-Achse zeigt von der
    Unterseite zur Oberseite des Bauteils") ist auf der Bauteil-
    Ebene zu setzen, weil viele Plattenwerkstoffe weder eine
    ausgezeichnete Ober- noch Unterseite haben (Memory
    `project_plattenwerkstoffe`). Im allgemeinen Fall ist
    `plattendicken_achse` bis auf Vorzeichen eindeutig.
---

## Prosa-Definition

Die **Plattendicken-Achse** eines Plattenwerkstoffs oder Platten-
bauteils ist ein Einheitsvektor im Welt-Koordinatensystem, der
rechtwinklig zur Plattenebene steht und damit die Richtung der
kleinsten Plattendimension (Plattendicke nach DIN EN 13986) als
geometrische Bezugsachse für Lagenaufbau, Plattenebenen-
Festigkeitswerte und Anschluss-Geometrie definiert.

## Mathematische Definition

Sei

- e_hat ∈ S² ⊂ ℝ³ ein Einheitsvektor (siehe `einheitsvektor`),
- B ein Plattenbauteil oder Plattenwerkstoff (siehe `bauteil`,
  `werkstoff`; hier nur als Träger der Annotation vorausgesetzt).

Dann ist die **Plattendicken-Achse** des Plattenbauteils B eine
Annotation

```
plattendicken_achse(B) := e_hat ∈ S²,
```

mit der Eigenschaft, dass die **Plattenebene** als affine Ebene
durch den Bauteilbezugspunkt definiert ist als

```
Π(B) := { p ∈ ℝ³ | ⟨p − p_0, e_hat⟩ = 0 }
```

(p_0 ein Bezugspunkt auf der Mittelebene des Bauteils;
siehe `ebene`, `halbraum`).

**Default-Konvention** (prüfbare Konstruktionsregel, analog IFC und
zur Bauteilachsen-Konvention für stabförmige Bauteile):

```
Wenn plattendicken_achse am Werkstoff nicht explizit gesetzt,
gilt für ein Plattenbauteil B mit Werkstoff-Modus ∈
{STRUKTURIERT, SCHWACH, KEINE}:
  plattendicken_achse(B) := bauteil_lokale_z_achse(B).
```

Die lokale z-Achse des Plattenbauteils ist per Konstruktionsregel
rechtwinklig zu den beiden Plattenformat-Hauptrichtungen (Länge,
Breite). Eine fehlende Plattendicken-Achse **nach** Auflösung ist
Validierungsfehler, keine Warnung.

**Konsistenzbedingungen mit anderen Plattenrichtungen** (eigener
Eintrag siehe `plattenlaengsrichtung`, `haupttragrichtung`,
`nebentragrichtung`):

```
⟨plattendicken_achse, plattenlaengsrichtung⟩ ≤ Toleranzen.WINKEL_EPS
⟨plattendicken_achse, haupttragrichtung⟩    ≤ Toleranzen.WINKEL_EPS
⟨plattendicken_achse, nebentragrichtung⟩    ≤ Toleranzen.WINKEL_EPS
```

(jeweils Skalarprodukt ≈ 0 bedeutet orthogonal).

## Wohldefiniertheit

- **Existenz**: Für jeden in DIN EN 13986 zugelassenen
  Plattenwerkstoff ist die Plattendicke als dritter (kleinster)
  Plattenmaß-Wert produktnormativ definiert (z. B. CLT
  3000 × 1250 × 100 mm, OSB 2500 × 1250 × 22 mm). Die rechtwinklige
  Achse zur Plattenebene ist daher eindeutig festgelegt.
- **Eindeutigkeit bis auf Vorzeichen**: e_hat ist als Annotation eines
  Plattenbauteils eindeutig, sobald eine Vorzeichenkonvention
  festgelegt ist. Bei Plattenwerkstoffen mit ausgezeichneter Ober-/
  Unterseite (z. B. beschichtete Platten, Akustikplatten mit
  Strukturschicht) ist die Vorzeichenkonvention „e_hat zeigt von der
  Unterseite zur Oberseite". Bei seitenisotropen Platten (Memory
  `project_plattenwerkstoffe`) ist die Vorzeichenwahl konventionell
  und beim Bauteil zu dokumentieren; alle Bemessungs-Eigenschaften
  sind vorzeicheninvariant.
- **Pflichtcharakter**: Bei Werkstoff-Modus ∈ {STRUKTURIERT,
  SCHWACH, KEINE} ist `plattendicken_achse` Pflichtfeld am
  Werkstoff (siehe `werkstoff`, `mehrlagenholz`,
  `gerichteter_plattenwerkstoff`, `isotroper_plattenwerkstoff`).
  Bei Modus HART (`axiales_holz`) ist sie undefiniert
  (`plattendicken_achse = ⊥`).
- **Norm-Invariante**: e_hat erbt | ‖e_hat‖² − 1 | ≤ Toleranzen.NORM_EPS
  aus `einheitsvektor`.
- **Konsistenz mit den Plattenrichtungen**: Die Orthogonalität zu
  `plattenlaengsrichtung`, `haupttragrichtung`, `nebentragrichtung`
  ist Konstruktions-Invariante; eine Verletzung ist
  Validierungsfehler.
- **Default-Auflösung**: Die Konvention `plattendicken_achse :=
  bauteil.lokale_z_achse` ist eine Konstruktionsregel, kein
  Erlaubnis-Mechanismus zum Weglassen. Nach Auflösung muss ein
  konkreter Vektor in S² vorliegen.
- **Nicht-Zirkularität**: Die Definition stützt sich auf
  `vektor`, `einheitsvektor`, `toleranzen`. Sie verweist nicht auf
  ihre Geschwister-Plattenrichtungen in der eigenen Definition,
  sondern setzt sie nur in den Konsistenzbedingungen voraus.

## Erläuterung (nicht normativ)

### Plattenkoordinatensystem (ProHolz, Schickhofer)

Plattenwerkstoffe haben in der Bemessungspraxis ein lokales
Koordinatensystem mit drei Achsen:

- **Achse 1 (x)**: Plattenlängsrichtung bzw. Haupttragrichtung
  (siehe `plattenlaengsrichtung`, `haupttragrichtung`).
- **Achse 2 (y)**: Plattenquerrichtung bzw. Nebentragrichtung
  (siehe `nebentragrichtung`).
- **Achse 3 (z)**: Plattendicken-Achse — dieser Eintrag.

Die Plattendicken-Achse ist die **dritte Achse** (z) dieses
Systems. IFC bildet das mit
`IfcMaterialLayerSet.LayerSetDirection = AXIS3` direkt ab.

### Default-Konvention

Im Rohzustand des Datenmodells ist die Plattendicken-Achse oft
nicht explizit gesetzt; sie wird aus der Bauteilgeometrie abgeleitet:

- **Stabförmige Bauteile** (`axiales_holz`): keine Plattendicken-
  Achse, weil keine Plattengeometrie.
- **Plattenförmige Bauteile** (`mehrlagenholz`,
  `gerichteter_plattenwerkstoff`, `isotroper_plattenwerkstoff`):
  die App definiert eine lokale z-Achse rechtwinklig zu den
  Plattenformat-Hauptrichtungen, die als Default-Plattendicken-
  Achse dient.

Diese Default-Regel ist Industriepraxis (cadwork, Cadwork Lexikon
2026; BTLx Part-Element mit `Reference Side`-System; IFC
`IfcMaterialLayerSet`).

### Vorzeichen — Ober- vs. Unterseite

Bei vielen Plattenwerkstoffen (Spanplatte, MDF, OSB ohne
Sichtseite) sind Ober- und Unterseite gleichwertig (Memory
`project_plattenwerkstoffe`). In diesem Fall ist das Vorzeichen
der Plattendicken-Achse konventionell. Bei beschichteten Platten,
Akustikplatten mit Strukturschicht oder bei BSP mit
ausgezeichneter Sichtseite (Sichtqualität AB / Industriequalität
NSI) wird das Vorzeichen physikalisch festgelegt.

## Beziehungen

- **Oberbegriff**: `einheitsvektor`. Strukturell ist die
  Plattendicken-Achse ein Einheitsvektor; das Plattenwerkstoff-
  Spezifikum ist die semantische Rolle „rechtwinklig zur Plattenebene".
- **Verwendung**:
  - **Werkstoff** (`werkstoff`): bei Modus STRUKTURIERT, SCHWACH,
    KEINE Pflichtfeld; bei Modus HART nicht definiert.
  - **Mehrlagenholz** (`mehrlagenholz`): Pflichtfeld; rechtwinklig zu
    Haupttragrichtung und Nebentragrichtung.
  - **Gerichteter Plattenwerkstoff**
    (`gerichteter_plattenwerkstoff`): Pflichtfeld; rechtwinklig zur
    Plattenlängsrichtung.
  - **Isotroper Plattenwerkstoff** (`isotroper_plattenwerkstoff`):
    Pflichtfeld; einziges geometrisches Werkstoff-Merkmal.
  - **Bauteil** (`bauteil`): Plattendicken-Achse wird per Default
    aus der lokalen z-Achse abgeleitet.
- **Abgrenzung**:
  - **`einheitsvektor`** (allgemein): trägt keine semantische
    Rolle. Eine Plattendicken-Achse ist ein Einheitsvektor in der
    Rolle „rechtwinklig zur Plattenebene".
  - **`faserrichtung`**: Einheitsvektor in der Rolle „Material-
    hauptachse parallel zum Faserverlauf"; bei Plattenwerkstoffen
    nicht direkt anwendbar (siehe `werkstoff`,
    `faserrichtungs_modus`). Plattendicken-Achse und Faserrichtung
    sind orthogonale Begriffe — bei Lagen eines Mehrlagenholzes
    liegt die Faserrichtung jeder Lage in der Plattenebene
    (rechtwinklig zur Plattendicken-Achse).
  - **`plattenlaengsrichtung`** (für OSB),
    **`haupttragrichtung`** (für Mehrlagenholz),
    **`nebentragrichtung`**: alle in der Plattenebene, rechtwinklig
    zur Plattendicken-Achse.
  - **`bauteilachse`**: geometrische Längsachse eines Stabbauteils.
    Bei Plattenbauteilen nicht direkt anwendbar; die Plattendicken-
    Achse ist hier die geometrisch ausgezeichnete dritte
    Bauteilachse.
  - **„Z-Achse"** des Welt-Koordinatensystems: vertikal nach oben
    (CLAUDE.md). Die Plattendicken-Achse ist eine **lokale**
    Bauteil-Achse; sie kann beliebig im Raum orientiert sein
    (z. B. waagrechte CLT-Decke: Plattendicken-Achse vertikal;
    senkrechte BSP-Wand: Plattendicken-Achse horizontal).

## Implementierungshinweis

Datentyp (Domänen-Schicht, Kotlin, Schicht
`domain.holzbau.werkstoff`):

```kotlin
package domain.holzbau.werkstoff

import domain.geometrie.Einheitsvektor

/**
 * Plattendicken-Achse eines Plattenwerkstoffs/Plattenbauteils:
 * Einheitsvektor in der Rolle 'rechtwinklig zur Plattenebene'.
 * Glossar: hg_plattendicken_achse.md
 *
 * Strukturell ein Wrapper um Einheitsvektor, der die semantische
 * Rolle typsicher kommuniziert. Pflichtfeld bei Werkstoff-Modus
 * STRUKTURIERT/SCHWACH/KEINE; nicht definiert bei Modus HART.
 *
 * Default-Konvention: Wenn am Werkstoff nicht explizit gesetzt,
 * gilt plattendicken_achse := bauteil.lokale_z_achse.
 */
@JvmInline
value class PlattendickenAchse(val richtung: Einheitsvektor) {
    val x: Double get() = richtung.x
    val y: Double get() = richtung.y
    val z: Double get() = richtung.z

    operator fun unaryMinus(): PlattendickenAchse =
        PlattendickenAchse(-richtung)
}
```

- **Einheit**: dimensionslos (geerbt von `einheitsvektor`).
- **Invariante**: alle Invarianten von `Einheitsvektor`,
  insbesondere | ‖e_hat‖² − 1 | ≤ Toleranzen.NORM_EPS.
- **Vorzeichenkonvention**: Bei seitenisotropen Plattenwerkstoffen
  (Memory `project_plattenwerkstoffe`) konventionell; bei Platten
  mit ausgezeichneter Sichtseite physikalisch festgelegt
  („Plattendicken-Achse zeigt von der Unterseite zur Oberseite").
  Vorzeichen ist beim verwendenden Bauteil zu dokumentieren.
- **Konsistenzprüfungen** (am verwendenden Werkstoff in Fabrik-
  funktionen / `init` prüfen, bei Verletzung `Resultat.Fehler`,
  niemals Exception):
  1. Norm-Invariante (geerbt).
  2. Orthogonalität zu allen anderen Plattenrichtungen
     (Plattenlängsrichtung, Haupttragrichtung, Nebentragrichtung)
     innerhalb WINKEL_EPS.
- **Edge Cases**:
  - **Plattendicken-Achse bei Stabbauteil** (`axiales_holz`):
    nicht definiert; `Werkstoff.plattendickenAchse == null`
    (Klassen-Invariante).
  - **Fehlende Plattendicken-Achse nach Default-Auflösung**:
    `Entartet.PlattendickenAchseNichtAufloesbar` (z. B. bei
    Bauteilen ohne wohldefinierte lokale z-Achse).
  - **Plattendicken-Achse parallel zur Plattenlängsrichtung**:
    geometrisch entartet; Validierungsfehler.
- **Verwendungsregel**: Funktionen, die werkstoff- oder platten-
  ebene-relative Größen berechnen (Lagenstruktur-Stapelung,
  Plattenfestigkeiten f_m,0/f_m,90), nehmen `PlattendickenAchse`
  als Parametertyp und nicht den nackten `Einheitsvektor`. Dadurch
  wird die semantische Rolle am API-Rand sichtbar.

## Quellen

**Primär (normativ):**

- DIN EN 13986:2015-06, „Holzwerkstoffe zur Verwendung im
  Bauwesen".
- DIN EN 1995-1-1:2010-12, „Eurocode 5: Bemessung und Konstruktion
  von Holzbauten – Teil 1-1", Abschnitt 9.
- DIN EN 16351:2021-08, DIN EN 636:2015-06, DIN EN 300:2006-09,
  DIN EN 312:2010-12, DIN EN 622-5:2010-01.
- ISO 16739-1:2024, „Industry Foundation Classes (IFC) — Part 1:
  Data schema".

**Sekundär:**

- Schickhofer, G.; Bogensperger, T.; Moosbrugger, T. (Hrsg.):
  *BSPhandbuch.* 2. Aufl., TU Graz 2010.
- ProHolz Austria: *Brettsperrholz Bemessung Band I.* Wien 2014.
- Niemz, P.; Sonderegger, W.: *Physik des Holzes und der
  Holzwerkstoffe.* Hanser, München 2017.

**Korpus (nicht autoritativ):**

- Memory `project_plattenwerkstoffe` (interner Projektkontext,
  abgerufen 2026-05-08).
- BTLx 2.x Specification (design2machine, Stand 2024).
- cadwork Lexikon (abgerufen 2026-05-08).
