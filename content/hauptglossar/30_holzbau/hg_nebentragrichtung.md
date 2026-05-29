---
id: nebentragrichtung
benennung: Nebentragrichtung
synonyme: ["90°-Richtung (CLT)", "Querrichtung (Mehrlagenholz)", "secondary load-bearing direction", "weaker axis of CLT"]
abgelehnte_benennungen: [Querrichtung, Nebenachse, Plattenquerachse, "minor axis", "weak direction"]
oberbegriff: einheitsvektor
begriffstyp: merkmal
voraussetzungen: [einheitsvektor, haupttragrichtung, plattendicken_achse, toleranzen]
abgrenzung_zu: [einheitsvektor, haupttragrichtung, plattendicken_achse, plattenlaengsrichtung, faserrichtung]
status: entwurf
theorie_pflichtig: required
quellen_primär:
  - "DIN EN 16351:2021-08, 'Holzbauwerke – Brettsperrholz – Anforderungen', Abschnitt 5: 90°-Richtung als zur 0°-Richtung (Decklage) rechtwinklige Plattenebenen-Achse."
  - "DIN EN 1995-1-1:2010-12 (Eurocode 5), Abschnitt 9 und Anhang B: Plattenfestigkeiten f_m,90,k, E_90,mean als Werte in der zur Haupttragrichtung rechtwinkligen Plattenebenen-Richtung."
  - "ProHolz Austria: Brettsperrholz Bemessung Band I. Wien 2014, Kap. 2.3: 'Nebentragrichtung (90°): Richtung rechtwinklig zur Haupttragrichtung in der Plattenebene'."
quellen_sekundär:
  - "Schickhofer, G.; Bogensperger, T.; Moosbrugger, T. (Hrsg.): BSPhandbuch — Holz-Massivbauweise in Brettsperrholz. 2. Aufl., TU Graz 2010, Kap. 2 (Plattenkoordinatensystem)."
  - "Blaß, H. J.; Flaig, M.: Stabförmige Bauteile aus Brettsperrholz. Karlsruher Berichte zum Ingenieurholzbau, Bd. 24, KIT Scientific Publishing, Karlsruhe 2012."
  - "Niemz, P.; Sonderegger, W.: Physik des Holzes und der Holzwerkstoffe. Hanser, München 2017, Kap. 7."
quellenkonflikt: |
  Die Definition der Nebentragrichtung als 90°-Komplement der
  Haupttragrichtung in der Plattenebene ist konfliktfrei in der
  CLT-Bemessungsliteratur (ProHolz 2014, Schickhofer 2010, Blaß/Flaig
  2012). Die Norm DIN EN 1995-1-1 setzt den Begriff über den Index
  „90" der Plattenfestigkeiten (f_m,90,k, E_90,mean) implizit voraus.

  Eigene Festlegung in diesem Glossar:

  - Die **Nebentragrichtung** ist der Einheitsvektor in W, in der
    Plattenebene, rechtwinklig zur Haupttragrichtung.
  - Sie ist eine **abgeleitete, redundante Größe**:
    `nebentragrichtung := plattendicken_achse × haupttragrichtung`.
    Sie wird im Datenmodell explizit geführt, weil:
    1. UI und Bemessungsformeln auf sie direkt zugreifen
       (f_m,90, E_90).
    2. Die Vorzeichenkonvention durch das Kreuzprodukt mit dem
       Welt-Rechtssystem konsistent festgelegt wird.
    3. Die explizite Speicherung erlaubt Konsistenzprüfung gegen
       Haupttragrichtung und Plattendicken-Achse zur
       Konstruktionszeit.
  - Sie ist Pflichtfeld bei Werkstoffen mit Faserrichtungs-Modus
    STRUKTURIERT (`mehrlagenholz`).
  - **Orthogonalität zur Plattendicken-Achse** und **zur
    Haupttragrichtung** sind Konstruktions-Invarianten:
    `⟨n_hat, e_hat_d⟩ ≤ WINKEL_EPS` und `⟨n_hat, h_hat⟩ ≤ WINKEL_EPS`.
---

## Prosa-Definition

Die **Nebentragrichtung** eines Mehrlagenholzes ist ein
Einheitsvektor im Welt-Koordinatensystem, der in der Plattenebene
liegt, sowohl zur Plattendicken-Achse als auch zur Haupttragrichtung
rechtwinklig steht und damit die zur Haupttragrichtung 90°
komplementäre Plattenebenen-Richtung kennzeichnet, an der die
geringere Plattensteifigkeit (E_90,mean nach DIN EN 1995-1-1 /
ProHolz) und damit die bemessungsrelevante 90°-Richtung der
Plattenfestigkeitswerte ausgerichtet ist.

## Mathematische Definition

Sei

- e_hat_d ∈ S² die Plattendicken-Achse (siehe `plattendicken_achse`),
- h_hat ∈ S² die Haupttragrichtung (siehe `haupttragrichtung`),
  mit ⟨h_hat, e_hat_d⟩ = 0.

Dann ist die **Nebentragrichtung** definiert als

```
nebentragrichtung := n_hat := e_hat_d × h_hat ∈ S².
```

Die Orthogonalitäts-Bedingung ⟨h_hat, e_hat_d⟩ = 0 sichert ‖n_hat‖ = 1 (siehe
Wohldefiniertheit), so dass n_hat ∈ S² gilt.

**Konstruktions-Invarianten**:

```
(N1) Orthogonalität zur Plattendicken-Achse:
       ⟨n_hat, e_hat_d⟩ = 0     (mathematisch),
       | ⟨n_hat, e_hat_d⟩ | ≤ Toleranzen.WINKEL_EPS     (numerisch).

(N2) Orthogonalität zur Haupttragrichtung:
       ⟨n_hat, h_hat⟩ = 0     (mathematisch),
       | ⟨n_hat, h_hat⟩ | ≤ Toleranzen.WINKEL_EPS     (numerisch).

(N3) Algebraische Konsistenz:
       n_hat = e_hat_d × h_hat     (innerhalb NORM_EPS).

(N4) Norm-Invariante:
       | ‖n_hat‖² − 1 | ≤ Toleranzen.NORM_EPS     (geerbt).
```

**Plattenkoordinatensystem**: (h_hat, n_hat, e_hat_d) ist ein
Rechtssystem-Tripel in W:

```
e_hat_d × h_hat = n_hat,        h_hat × n_hat = e_hat_d,        n_hat × e_hat_d = h_hat,
```

konsistent mit der Welt-Rechtssystem-Konvention (CLAUDE.md:
z-Achse vertikal nach oben, Rechtssystem).

## Wohldefiniertheit

- **Existenz**: Für jede Haupttragrichtung h_hat und Plattendicken-
  Achse e_hat_d mit ⟨h_hat, e_hat_d⟩ = 0 ist n_hat = e_hat_d × h_hat wohldefiniert; das
  Kreuzprodukt zweier orthogonaler Einheitsvektoren ist wieder ein
  Einheitsvektor.
- **Eindeutigkeit**: n_hat ist algebraisch durch das Kreuzprodukt
  bestimmt; das Vorzeichen folgt der Rechte-Hand-Regel und ist
  damit konsistent zum Welt-Rechtssystem.
- **‖n_hat‖ = 1 aus ⟨h_hat, e_hat_d⟩ = 0**: Es gilt
  ‖e_hat_d × h_hat‖² = ‖e_hat_d‖² · ‖h_hat‖² − ⟨e_hat_d, h_hat⟩² = 1 · 1 − 0 = 1
  (Lagrange-Identität), also ‖n_hat‖ = 1.
- **Pflichtcharakter**: Bei Werkstoff-Modus STRUKTURIERT ist
  `nebentragrichtung` Pflichtfeld am Werkstoff. Bei den anderen
  Modi nicht definiert.
- **Orthogonalitäts-Invarianten (N1, N2)**: n_hat ⊥ e_hat_d und n_hat ⊥ h_hat
  folgen direkt aus der Definition n_hat = e_hat_d × h_hat.
- **Algebraische Konsistenz (N3)**: Wenn n_hat explizit am Werkstoff
  gespeichert wird, ist die Konsistenz mit e_hat_d × h_hat zu prüfen
  (innerhalb NORM_EPS); andernfalls Validierungsfehler.
- **Plattenkoordinatensystem (Rechtssystem)**: (h_hat, n_hat, e_hat_d) bildet
  ein orthonormales Rechtssystem; Spatprodukt
  ⟨h_hat × n_hat, e_hat_d⟩ = 1.
- **Nicht-Zirkularität**: Die Definition stützt sich auf
  `einheitsvektor`, `plattendicken_achse`, `haupttragrichtung`,
  `toleranzen`. Sie kommt nicht in ihrer eigenen Definition vor.

## Erläuterung (nicht normativ)

### ProHolz-Definition

ProHolz Austria definiert in „Brettsperrholz Bemessung Band I":

> **Nebentragrichtung (90°)**: Richtung rechtwinklig zur
> Haupttragrichtung in der Plattenebene.

Diese Definition wird im Glossar wörtlich übernommen und durch
die mathematische Form n_hat = e_hat_d × h_hat präzisiert.

### Bemessungs-Konsequenz

Die Plattenfestigkeitswerte sind in DIN EN 1995-1-1 / EN 14080 /
EN 16351 für die beiden Hauptachsen tabelliert:

| Achse                    | Festigkeit         | Richtung                |
|--------------------------|--------------------|-------------------------|
| Haupttragrichtung (0°)   | f_m,0,k, E_0,mean  | parallel zu h_hat           |
| Nebentragrichtung (90°)  | f_m,90,k, E_90,mean| parallel zu n_hat          |

Bei symmetrischem CLT-Standardlayout (3, 5, 7 Lagen) ist die
Steifigkeit in 90°-Richtung geringer als in 0°-Richtung, weil
weniger Lagen die Last in 90°-Richtung tragen. Die Reduktion
liegt typisch bei E_90,mean / E_0,mean ≈ 0,30…0,55 je nach
Lagenanzahl (Schickhofer 2010, Tab. 3.4).

### Redundanz und Speicherung

Die Nebentragrichtung ist mathematisch redundant (algebraisch
durch Plattendicken-Achse und Haupttragrichtung bestimmt). Sie
wird im Datenmodell trotzdem explizit gespeichert:

1. **API-Klarheit**: Bemessungsfunktionen, die f_m,90 / E_90
   benötigen, nehmen `Nebentragrichtung` als typsicheren
   Parameter; das vermeidet wiederholte Kreuzproduktberechnungen.
2. **Konsistenzprüfung**: Speicherung als eigenes Feld erlaubt
   Plausibilitätsprüfung gegen Plattendicken-Achse und
   Haupttragrichtung zur Konstruktionszeit.
3. **UI-Visualisierung**: 3D-Renderer kann die drei Plattenachsen
   (h_hat, n_hat, e_hat_d) direkt aus Werkstoff-Feldern darstellen.

### Plattenkoordinatensystem

Die drei Achsen (h_hat, n_hat, e_hat_d) bilden ein lokales
Plattenkoordinatensystem mit Rechtssystem-Orientierung. Dies ist
konsistent mit:

- **IFC** `IfcMaterialLayerSet.LayerSetDirection = AXIS3` für e_hat_d
  und der durch das Layer-Set induzierten 0°/90°-Konvention.
- **BTLx** `Reference Side`-System mit den drei lokalen Achsen.
- **cadwork** Plattenkoordinatensystem.

## Beziehungen

- **Oberbegriff**: `einheitsvektor`. Strukturell ist die
  Nebentragrichtung ein Einheitsvektor; das Mehrlagenholz-
  Spezifikum ist die semantische Rolle „90°-Komplement zur
  Haupttragrichtung".
- **Verwendung**:
  - **Mehrlagenholz** (`mehrlagenholz`): Pflichtfeld; sekundäres
    Plattenebene-Richtungsfeld.
  - **Plattenfestigkeiten f_m,90, E_90**: Bezugsachse der
    Bemessungswerte.
- **Abgrenzung**:
  - **`einheitsvektor`** (allgemein): trägt keine semantische
    Rolle.
  - **`haupttragrichtung`**: 0°-Richtung der Plattenfestigkeiten;
    Nebentragrichtung ist das 90°-Komplement.
  - **`plattendicken_achse`**: rechtwinklig zur Plattenebene;
    Nebentragrichtung liegt **in** der Plattenebene.
  - **`plattenlaengsrichtung`** (OSB): bei OSB die einzige
    Plattenebene-Vorzugsrichtung; Nebentragrichtung ist nur bei
    Mehrlagenholz definiert. Disjunkt nach Werkstoff-Modus.
  - **`faserrichtung`**: Faserrichtung im engeren Sinn ist die
    L-Richtung der Holzfaser einer einzelnen Holzlamelle. Die
    Nebentragrichtung ist eine makroskopische Plattenebenen-
    Bemessungsachse, kein Materialachsen-Vektor einer Lage.

## Implementierungshinweis

Datentyp (Domänen-Schicht, Kotlin, Schicht
`domain.holzbau.werkstoff`):

```kotlin
package domain.holzbau.werkstoff

import domain.geometrie.Einheitsvektor

/**
 * Nebentragrichtung eines Mehrlagenholzes (CLT/BSP, Sperrholz,
 * Multiplex): Einheitsvektor in der Plattenebene, rechtwinklig
 * zur Haupttragrichtung.
 * Glossar: hg_nebentragrichtung.md — ProHolz Austria 2014.
 *
 * Strukturell ein Wrapper um Einheitsvektor; semantische Rolle
 * 'Bauteil-90°-Bemessungsachse'. Pflichtfeld bei Mehrlagenholz.
 *
 * Mathematisch redundant: nebentragrichtung := plattendicken_achse
 * x haupttragrichtung. Wird trotzdem explizit gespeichert
 * (API-Klarheit, Konsistenzpruefung).
 *
 * Konstruktions-Invarianten:
 *   N1: orthogonal zur Plattendicken-Achse (innerhalb WINKEL_EPS).
 *   N2: orthogonal zur Haupttragrichtung (innerhalb WINKEL_EPS).
 *   N3: nebentragrichtung = plattendicken_achse x haupttragrichtung
 *       (innerhalb NORM_EPS).
 *   N4: Norm-Invariante (geerbt).
 */
@JvmInline
value class Nebentragrichtung(val richtung: Einheitsvektor) {
    val x: Double get() = richtung.x
    val y: Double get() = richtung.y
    val z: Double get() = richtung.z

    operator fun unaryMinus(): Nebentragrichtung =
        Nebentragrichtung(-richtung)

    companion object {
        /**
         * Konstruiert die Nebentragrichtung aus Plattendicken-Achse
         * und Haupttragrichtung (Default-Konstruktion).
         */
        fun ausPlattenachsen(
            plattendickenAchse: Einheitsvektor,
            haupttragrichtung: Einheitsvektor
        ): Resultat<Nebentragrichtung, EntartetGeometrie> { /* Kreuzprodukt + Normierung */ TODO() }
    }
}
```

- **Einheit**: dimensionslos (geerbt).
- **Invarianten**: alle Invarianten von `Einheitsvektor` plus N1,
  N2, N3; geprüft in `Mehrlagenholz.init`, weil dort
  Plattendicken-Achse und Haupttragrichtung verfügbar sind.
- **Vorzeichenkonvention**: durch Kreuzprodukt-Definition fest;
  konsistent mit Welt-Rechtssystem.
- **Edge Cases**:
  - **Inkonsistenz mit e_hat_d × h_hat** (N3 verletzt):
    `Entartet.NebentragrichtungInkonsistent`.
  - **Verletzte Orthogonalität (N1 oder N2)**:
    `Entartet.NebentragrichtungNichtOrthogonal`.
  - **Mehrlagenholz mit nicht-orthogonalen h_hat und e_hat_d**: das ist
    bereits in `mehrlagenholz` Konstruktions-Invariante; bei
    Verletzung scheitert die Werkstoff-Konstruktion vor der
    Nebentragrichtungs-Berechnung.
- **IFC-Mapping** (Persistenzschicht): nicht direkt abgebildet;
  die Nebentragrichtung ergibt sich implizit aus
  Layer-Set-Direction und 0°/90°-Konvention der Lagenstruktur.
- **Verwendungsregel**: Funktionen, die Plattenfestigkeiten f_m,90
  / E_90 verwenden, nehmen `Nebentragrichtung` als typsicheren
  Parameter, nicht den nackten `Einheitsvektor`.

## Quellen

**Primär (normativ):**

- DIN EN 16351:2021-08, „Holzbauwerke – Brettsperrholz".
- DIN EN 1995-1-1:2010-12, „Eurocode 5", Abschnitt 9 und
  Anhang B.
- ProHolz Austria: *Brettsperrholz Bemessung Band I.* Wien 2014.

**Sekundär:**

- Schickhofer, G.; Bogensperger, T.; Moosbrugger, T. (Hrsg.):
  *BSPhandbuch.* 2. Aufl., TU Graz 2010.
- Blaß, H. J.; Flaig, M.: *Stabförmige Bauteile aus
  Brettsperrholz.* KIT Scientific Publishing, Karlsruhe 2012.
- Niemz, P.; Sonderegger, W.: *Physik des Holzes und der
  Holzwerkstoffe.* Hanser, München 2017.

**Korpus (nicht autoritativ):**

- ETAs der CLT-Hersteller (KLH, Stora Enso, Hasslacher,
  Binderholz), abgerufen 2026-05-08.
- Wikipedia, Lemma „Brettsperrholz" (abgerufen 2026-05-08).
