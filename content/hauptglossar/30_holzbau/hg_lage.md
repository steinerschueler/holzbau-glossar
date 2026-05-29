---
id: lage
benennung: Lage
synonyme: ["Einzellage", "Lamelle (im Mehrlagenholz)", "Furnierlage", "Brettlage", "ply"]
abgelehnte_benennungen: [Schicht, Brettschicht, Lamelle, Furnier, "layer", "lamination"]
oberbegriff: null
begriffstyp: partitiv
voraussetzungen: [einheitsvektor, festigkeitsklasse, toleranzen]
abgrenzung_zu: [lagenstruktur, mehrlagenholz, faserrichtung, festigkeitsklasse]
status: entwurf
theorie_pflichtig: required
quellen_primär:
  - "DIN EN 16351:2021-08, 'Holzbauwerke – Brettsperrholz – Anforderungen', Abschnitt 3 (Begriffe: Decklage, Mittellage, Querlage, Längslage) und Abschnitt 5 (Lagenaufbau): jede Lage hat Dicke (typ. 19–40 mm), Festigkeitsklasse (typ. C24) und Faserrichtung (typ. 0° oder 90° zur Haupttragrichtung)."
  - "DIN EN 636:2015-06, 'Sperrholz – Anforderungen': Furnierlage als Einzellage; Dicke 1–4 mm; Faserrichtung lagenweise um 90° gekreuzt."
  - "DIN EN 1995-1-1:2010-12 (Eurocode 5), Abschnitt 9 (Plattenwerkstoffe), Anhang B (γ-Verfahren mit Lagenwerten als Eingabe der mechanischen Bemessung)."
quellen_sekundär:
  - "Schickhofer, G.; Bogensperger, T.; Moosbrugger, T. (Hrsg.): BSPhandbuch — Holz-Massivbauweise in Brettsperrholz. 2. Aufl., TU Graz 2010, Kap. 3 (Lagenaufbau, Lagenwerte E_L, G_LR, Festigkeit je Lage)."
  - "Blaß, H. J.; Flaig, M.: Stabförmige Bauteile aus Brettsperrholz. Karlsruher Berichte zum Ingenieurholzbau, Bd. 24, KIT Scientific Publishing, Karlsruhe 2012, DOI 10.5445/KSP/1000030362, Kap. 2 (Lagen-Modellierung)."
  - "Niemz, P.; Sonderegger, W.: Physik des Holzes und der Holzwerkstoffe. Hanser, München 2017, Kap. 7 (Sperrholz, Brettsperrholz, Lagenaufbau)."
  - "ProHolz Austria: Brettsperrholz Bemessung Band I. Wien 2014, Kap. 3 (Lagenstruktur und Lagenausrichtung)."
quellenkonflikt: |
  Die normativen Quellen DIN EN 16351 (CLT) und EN 636 (Sperrholz)
  verwenden „Lage" als Begriff der Werkstoffstruktur, ohne eine
  formale Datenstruktur-Definition (Tupel von Dicke,
  Festigkeitsklasse, Faserrichtung, Position) zu führen. Schickhofer
  und Blaß/Flaig modellieren die Lage in der Bemessung als ebenes
  orthotropes Sublaminat mit Dicke, Faserwinkel relativ zur
  Bauteilachse und werkstoffspezifischen Festigkeits-/
  Steifigkeitswerten.

  Eigene Festlegung in diesem Glossar:

  - Eine **Lage** ist im Glossar ein **Aggregat** aus genau vier
    Pflichtfeldern:
    1. `dicke ∈ ℝ⁺` (in mm; typ. 19–40 mm bei CLT, 1–4 mm bei
       Sperrholz),
    2. `faserrichtung ∈ S²` (Einheitsvektor in W; lagen-spezifisch),
    3. `festigkeitsklasse ∈ 𝓕𝓚_axiales_holz` (typ. C24 bei CLT,
       furnierspezifisch bei Sperrholz),
    4. `position ∈ ℕ₀` (Lagennummer von außen, 0-basiert).
  - Die Lage ist ein **werkstoff-internes Aggregat**, das nur als
    Bestandteil einer `lagenstruktur` (siehe dort) und damit eines
    `mehrlagenholz` (Modus STRUKTURIERT) auftritt; sie ist kein
    selbständiger Werkstoff.
  - Die Lage trägt **keine UUID** (keine Element-Identität) und
    keine Geometrie über die Dicke hinaus; ihre räumliche Lage im
    Bauteil ist durch die Lagenstruktur und die Plattendicken-Achse
    bestimmt.
  - Die Faserrichtung jeder Lage ist im Standardlayout parallel
    oder rechtwinklig zur Haupttragrichtung des umgebenden
    Mehrlagenholzes (DIN EN 16351, Schickhofer 2010); abweichende
    Lagenaufbauten (z. B. 45°-Lagen für Erdbebenanwendungen) sind
    zulässig, müssen aber als „abweichender Lagenaufbau" in der
    `lagenstruktur` markiert werden.
  - Die Lagenposition `position` ist 0-basiert von außen gezählt:
    `position = 0` ist die erste Decklage (Außenseite, an der die
    Plattendicken-Achse positiv beginnt), `position = n−1` ist die
    zweite Decklage (gegenüberliegende Außenseite). Die
    Konvention orientiert sich an Schickhofer 2010 und IFC
    `IfcMaterialLayer.Priority`.
---

## Prosa-Definition

Eine **Lage** ist das Aggregat aus genau einer Lagendicke (Länge
in mm), genau einer Lagenfaserrichtung (Einheitsvektor in W),
genau einer Lagenfestigkeitsklasse (axiales-Holz-Festigkeitsklasse
nach DIN EN 338 / 14080 / 14374) und genau einer Lagenposition
(0-basierte Lagennummer von außen), das den Beitrag einer
einzelnen, planparallelen Holzschicht innerhalb der Lagenstruktur
eines Mehrlagenholzes vollständig charakterisiert.

## Mathematische Definition

Sei

- ℝ⁺ die positiven reellen Zahlen,
- S² ⊂ ℝ³ die Einheitssphäre (siehe `einheitsvektor`),
- 𝓕𝓚_AH die Menge der für axiales Holz zulässigen
  Festigkeitsklassen (siehe `festigkeitsklasse`),
- ℕ₀ die natürlichen Zahlen einschließlich 0.

Dann ist eine **Lage** das Tupel

```
ℓ := (dicke, faserrichtung, festigkeitsklasse, position) ∈
     ℝ⁺ × S² × 𝓕𝓚_AH × ℕ₀
```

mit

- **dicke** ∈ ℝ⁺ (mm; typ. 19–40 bei CLT, 1–4 bei Sperrholz),
- **faserrichtung** ∈ S² (Einheitsvektor in W; lagen-spezifische
  Faserorientierung),
- **festigkeitsklasse** ∈ 𝓕𝓚_AH (typ. C24 für CLT-Lagen),
- **position** ∈ ℕ₀ (0-basierte Lagennummer von außen).

**Konsistenzbedingungen** mit der umgebenden Lagenstruktur
(siehe `lagenstruktur`, formale Aussage dort):

```
0 ≤ position ≤ |L| − 1
∠(faserrichtung, h_hat) ∈ {0, π/2}     (im Standardlayout)
oder Lagenstruktur ist als „abweichender Lagenaufbau" markiert,
```

mit h_hat = Haupttragrichtung des umgebenden Mehrlagenholzes
(siehe `haupttragrichtung`).

**Lagen-Mittenebene** (abgeleitet, für Visualisierung):

Wenn die Lagen ℓ₀, …, ℓ_{n−1} der Lagenstruktur in dieser
Reihenfolge entlang der Plattendicken-Achse e_hat_d gestapelt sind und
das Bauteil seinen Bezugspunkt p₀ in der Bauteilmitte hat, ist die
Mittenebene der Lage ℓ_i auf Höhe

```
z_i := −d/2 + Σ_{j=0}^{i−1} ℓ_j.dicke + ℓ_i.dicke / 2
```

mit d = Σ_j ℓ_j.dicke der Gesamtdicke. Diese Größe ist abgeleitet
und nicht Bestandteil der Lage selbst.

## Wohldefiniertheit

- **Existenz**: Für jedes nach DIN EN 16351 oder EN 636
  zertifizierte Mehrlagenprodukt ist der Lagenaufbau in der ETA
  bzw. im Datenblatt explizit dokumentiert (z. B. KLH XL-CL3-h:
  3 Lagen 30/30/30 mm, Faserrichtungen 0°/90°/0°,
  Festigkeitsklasse C24).
- **Eindeutigkeit der Pflichtfelder**: dicke, faserrichtung,
  festigkeitsklasse, position sind alle eindeutig durch das
  Produkt-Datenblatt festgelegt.
- **Eindeutigkeit der Faserrichtung bis auf Vorzeichen**: f_hat_i ist
  als Annotation einer Lage eindeutig, sobald eine
  Vorzeichenkonvention im umgebenden Mehrlagenholz festgelegt ist
  (typisch: in dieselbe Halbachse wie die Haupttragrichtung).
- **Norm-Invariante**: faserrichtung erbt
  | ‖f_hat‖² − 1 | ≤ Toleranzen.NORM_EPS aus `einheitsvektor`.
- **Positiv-Invariante**: dicke > 0; Lagen mit Dicke 0 oder
  negativ sind unzulässig (`Entartet.LageDickeNichtPositiv`).
- **Position-Eindeutigkeit**: innerhalb einer Lagenstruktur
  L = (ℓ₀, …, ℓ_{n−1}) ist position eine **bijektive** Abbildung
  auf {0, …, n−1}; doppelte oder fehlende Positionen sind
  unzulässig (Konsistenz wird in `lagenstruktur` geprüft).
- **Konsistenz mit Haupttragrichtung**: Die Lagen-Faserrichtung
  ist im Standardlayout parallel oder rechtwinklig zur
  Haupttragrichtung; bei Abweichung ist der `lagenstruktur`-Marker
  „abweichender Lagenaufbau" Pflicht.
- **Nicht-Zirkularität**: Die Definition stützt sich auf
  `einheitsvektor`, `festigkeitsklasse`, `toleranzen`. Sie
  verweist auf `lagenstruktur` und `haupttragrichtung` nur in den
  Konsistenzbedingungen, nicht in der Definition selbst.

## Erläuterung (nicht normativ)

### Lagen-Konvention bei CLT (DIN EN 16351, Schickhofer)

Brettsperrholz hat 3, 5 oder 7 Lagen mit ungerader Anzahl
(klassisches Layout). Eine typische 5-lagige Platte CLT/BSP
hat den Lagenaufbau:

| position | dicke | faserrichtung | festigkeitsklasse |
|----------|-------|---------------|-------------------|
| 0        | 30 mm | 0° (= h_hat)      | C24               |
| 1        | 30 mm | 90°           | C24               |
| 2        | 30 mm | 0° (= h_hat)      | C24               |
| 3        | 30 mm | 90°           | C24               |
| 4        | 30 mm | 0° (= h_hat)      | C24               |

Die Decklagen (position 0 und 4) haben dieselbe Faserrichtung;
die Symmetrie ist in `lagenstruktur` als Klassen-Invariante
geprüft.

### Lagen-Konvention bei Sperrholz (DIN EN 636)

Furniersperrholz hat ungerade Lagenanzahl (3, 5, 7, 9, …) mit
dünnen Lagen (1–4 mm). Multiplex hat ≥ 5 Lagen. Die Konvention
ist analog zu CLT: jede Lage trägt Dicke, Faserrichtung,
Festigkeitsklasse, Position.

### Abweichende Lagenaufbauten

Sonderfälle:

- **45°-Lagen** für Erdbeben-Aussteifung: zulässig, aber
  Lagenstruktur muss als „abweichender Lagenaufbau" markiert sein.
- **Asymmetrische Aufbauten** (Decklage A ≠ Decklage B):
  produktnormativ zulässig (DIN EN 16351 Anhang); App-Marker
  erforderlich.
- **Mischfestigkeiten** (Lage 0 = C30, Lage 1 = C24): zulässig,
  jede Lage trägt eigene Festigkeitsklasse.

### Lagen-Position vs. Lagen-Index

Die `position` ist eine **physikalische** 0-basierte Nummer von
außen, nicht ein bloßer Listenindex. Sie ist redundant zum Index
in der Listendarstellung der Lagenstruktur, wird aber explizit
geführt, weil:

1. Spätere Modifikationen (Lagen einfügen/löschen) erfordern
   Stabilität der Lagenidentität.
2. IFC `IfcMaterialLayer.Priority` führt eine analoge
   physikalische Reihung.
3. Die Lagen-Mittenebene wird über `position` und Dicke berechnet,
   nicht über den Listenindex.

## Beziehungen

- **Oberbegriff**: keiner. Lage ist ein eigenständiges Aggregat.
- **Bestandteile**:
  - **Lagendicke** (`dicke`): Länge in mm, > 0.
  - **Lagenfaserrichtung** (`faserrichtung`): Einheitsvektor.
  - **Lagenfestigkeitsklasse** (`festigkeitsklasse`):
    `AxialesHolzFestigkeitsklasse` (typ. C24).
  - **Lagenposition** (`position`): 0-basierte Lagennummer von
    außen.
- **Verwendung**:
  - **Lagenstruktur** (`lagenstruktur`): geordnete Liste von
    Lagen mit n ≥ 3.
  - **Mehrlagenholz** (`mehrlagenholz`): trägt eine Lagenstruktur
    aus Lagen.
- **Abgrenzung**:
  - **`lagenstruktur`**: das **Aggregat aller Lagen** eines
    Mehrlagenholzes; eine einzelne Lage ist Bestandteil der
    Lagenstruktur, nicht synonym dazu.
  - **`mehrlagenholz`**: der Werkstoff selbst; eine Lage ist
    Werkstoff-internes Aggregat, kein eigenständiger Werkstoff.
  - **`faserrichtung`**: ist Einheitsvektor in der Rolle „Material-
    hauptachse parallel zum Faserverlauf"; eine Lage trägt eine
    Faserrichtung als Feld, ist aber nicht selbst eine
    Faserrichtung.
  - **`festigkeitsklasse`**: ist Aufzählungswert; eine Lage trägt
    eine Festigkeitsklasse als Feld.
  - **„Brettlamelle"** (in BSH): bei BSH (`axiales_holz`) sind
    alle Lamellen parallel; sie werden nicht als Lagen geführt,
    weil keine STRUKTURIERTE Anisotropie vorliegt. Lage im Sinne
    dieses Glossars ist nur bei Modus STRUKTURIERT
    (`mehrlagenholz`) relevant.

## Implementierungshinweis

Datentyp (Domänen-Schicht, Kotlin, Schicht
`domain.holzbau.werkstoff`):

```kotlin
package domain.holzbau.werkstoff

import domain.geometrie.Einheitsvektor
import domain.holzbau.Faserrichtung

/**
 * Lage: einzelne Holzschicht innerhalb einer Lagenstruktur eines
 * Mehrlagenholzes (DIN EN 16351, EN 636).
 * Glossar: hg_lage.md
 *
 * Aggregat aus vier Pflichtfeldern; trägt keine UUID, keine
 * Geometrie über die Dicke hinaus. Räumliche Position ergibt sich
 * aus position und Plattendicken-Achse des umgebenden
 * Mehrlagenholzes.
 */
data class Lage(
    /** Lagendicke in mm, > 0. */
    val dicke: Double,
    /** Lagenfaserrichtung in W (Einheitsvektor in der Plattenebene). */
    val faserrichtung: Faserrichtung,
    /** Lagenfestigkeitsklasse (axiales Holz, typ. C24 bei CLT). */
    val festigkeitsklasse: AxialesHolzFestigkeitsklasse,
    /** 0-basierte Lagennummer von außen. */
    val position: Int
) {
    init {
        require(dicke > 0.0) {
            "Lagendicke muss positiv sein, war $dicke"
        }
        require(position >= 0) {
            "Lagenposition muss >= 0 sein, war $position"
        }
        // faserrichtung erbt Norm-Invariante von Einheitsvektor.
    }
}
```

- **Einheit**: `dicke` in mm (Double, CLAUDE.md-Konvention);
  übrige Felder dimensionslos.
- **Identität**: keine; Werteklasse / data class. Eine Lage ist
  durch ihren Inhalt identisch, nicht durch eine UUID.
- **Invarianten** (in `init` prüfen, bei Verletzung
  `IllegalArgumentException` als require — alternativ Resultat-
  Wrapping in einer Fabrikfunktion `Lage.erzeuge(...): Resultat<Lage, EntartetGeometrie>`,
  je nach Aufruferschicht):
  1. `dicke > 0` (positiv).
  2. `position >= 0`.
  3. `faserrichtung` erfüllt Norm-Invariante (geerbt von
     `Einheitsvektor`).
  4. `festigkeitsklasse ∈ 𝓕𝓚_AH` (durch Typ erzwungen:
     `AxialesHolzFestigkeitsklasse`).
- **Konsistenz mit Lagenstruktur** (geprüft in `lagenstruktur`,
  nicht in `lage`):
  - Position ist innerhalb der Lagenstruktur eindeutig (Bijektion
    auf {0, …, n−1}).
  - Faserrichtung parallel oder rechtwinklig zur Haupttragrichtung
    des umgebenden Mehrlagenholzes (im Standardlayout).
- **IFC-Mapping** (Persistenzschicht):
  - `IfcMaterialLayer.LayerThickness` ← `dicke` (mm umrechnen auf
    IFC-Längeneinheit).
  - `IfcMaterialLayer.Material.Name` ← Festigkeitsklasse-Name.
  - `IfcMaterialLayer.Priority` ← `position`.
- **Edge Cases**:
  - **Dicke = 0**: nicht zulässig; `IllegalArgumentException` bzw.
    `Entartet.LageDickeNichtPositiv`.
  - **Position negativ oder zu groß**: nicht zulässig; Bereich
    {0, …, n−1} wird in `lagenstruktur` geprüft.
  - **Faserrichtung 45°**: zulässig nur bei
    `lagenstruktur.abweichenderLagenaufbau == true`; sonst
    Validierungsfehler beim Aufnehmen in die Lagenstruktur.
  - **Mehrere Lagen mit identischer Position**: nicht zulässig;
    Bijektivitätsprüfung in `lagenstruktur`.

## Quellen

**Primär (normativ):**

- DIN EN 16351:2021-08, „Holzbauwerke – Brettsperrholz".
- DIN EN 636:2015-06, „Sperrholz – Anforderungen".
- DIN EN 1995-1-1:2010-12, „Eurocode 5", Abschnitt 9 und Anhang B.

**Sekundär:**

- Schickhofer, G.; Bogensperger, T.; Moosbrugger, T. (Hrsg.):
  *BSPhandbuch.* 2. Aufl., TU Graz 2010.
- Blaß, H. J.; Flaig, M.: *Stabförmige Bauteile aus
  Brettsperrholz.* KIT Scientific Publishing, Karlsruhe 2012.
- Niemz, P.; Sonderegger, W.: *Physik des Holzes und der
  Holzwerkstoffe.* Hanser, München 2017.
- ProHolz Austria: *Brettsperrholz Bemessung Band I.* Wien 2014.

**Korpus (nicht autoritativ):**

- ETAs der CLT-Hersteller (KLH ETA-06/0138, Stora Enso ETA-14/0349,
  Hasslacher ETA-12/0281, Binderholz ETA-11/0210), abgerufen
  2026-05-08.
- Wikipedia, Lemma „Brettsperrholz" (abgerufen 2026-05-08).
