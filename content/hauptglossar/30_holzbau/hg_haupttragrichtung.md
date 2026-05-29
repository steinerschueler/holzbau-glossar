---
id: haupttragrichtung
benennung: Haupttragrichtung
synonyme: ["Decklamellen-Richtung", "0°-Richtung (CLT)", "main load-bearing direction", "stronger axis of CLT"]
abgelehnte_benennungen: [Tragrichtung, Hauptachse, Plattenlängsachse, "main bearing axis", "strong direction"]
oberbegriff: einheitsvektor
begriffstyp: merkmal
voraussetzungen: [einheitsvektor, plattendicken_achse, lagenstruktur, toleranzen]
abgrenzung_zu: [einheitsvektor, plattendicken_achse, plattenlaengsrichtung, nebentragrichtung, faserrichtung]
status: entwurf
theorie_pflichtig: required
quellen_primär:
  - "DIN EN 16351:2021-08, 'Holzbauwerke – Brettsperrholz – Anforderungen', Abschnitt 3 (Begriffe) und Abschnitt 5 (Lagenaufbau): Decklage = äußere Lage; Decklamellen-Richtung als bemessungsrelevante Hauptachse."
  - "DIN EN 1995-1-1:2010-12 (Eurocode 5), Abschnitt 9 (Plattenwerkstoffe und Bauteile aus Plattenwerkstoffen) und Anhang B (γ-Verfahren): Bemessungsachsen 0° / 90° der Platte, mit 0° als Decklamellen-Richtung."
  - "ProHolz Austria: Brettsperrholz Bemessung Band I — Grundlagen für Statik und Konstruktion. Wien 2014, Kap. 2.3: 'Haupttragrichtung (0°): Richtung der Decklamellen mit höherer Steifigkeit der Platte.'"
quellen_sekundär:
  - "Schickhofer, G.; Bogensperger, T.; Moosbrugger, T. (Hrsg.): BSPhandbuch — Holz-Massivbauweise in Brettsperrholz. 2. Aufl., TU Graz 2010, Kap. 2 und 3 (Plattenkoordinatensystem, Haupttragrichtung als Decklagen-Faserrichtung)."
  - "Blaß, H. J.; Flaig, M.: Stabförmige Bauteile aus Brettsperrholz. Karlsruher Berichte zum Ingenieurholzbau, Bd. 24, KIT Scientific Publishing, Karlsruhe 2012."
  - "Niemz, P.; Sonderegger, W.: Physik des Holzes und der Holzwerkstoffe. Hanser, München 2017, Kap. 7 (Brettsperrholz, Lagenaufbauten)."
quellenkonflikt: |
  Die ProHolz-Definition „Haupttragrichtung (0°) = Richtung der
  Decklamellen mit höherer Steifigkeit der Platte" ist konfliktfrei in
  der CLT-Bemessungsliteratur (Schickhofer 2010, Blaß/Flaig 2012,
  ProHolz 2014). DIN EN 16351 und DIN EN 1995-1-1 setzen den Begriff
  voraus, ohne ihn explizit als Vektor zu definieren.

  Eigene Festlegung in diesem Glossar:

  - Die **Haupttragrichtung** ist der Einheitsvektor in W, in der
    Plattenebene, in Richtung der Faserrichtung der äußeren Decklage
    (Lage 0 der Lagenstruktur).
  - Sie ist Pflichtfeld bei Werkstoffen mit Faserrichtungs-Modus
    STRUKTURIERT (`mehrlagenholz`).
  - **Eindeutigkeitsregel** (formal aus der ProHolz-Definition):
    `haupttragrichtung := lagenstruktur.lagen[0].faserrichtung`
    (bis auf Vorzeichen).
  - **Orthogonalität zur Plattendicken-Achse**:
    `⟨haupttragrichtung, plattendicken_achse⟩ ≤ WINKEL_EPS`.
  - **Vorzeichenkonvention**: typisch in dieselbe Halbachse wie die
    längere Plattenformat-Kante (analog `plattenlaengsrichtung`).
  - Die Verallgemeinerung von CLT auf Sperrholz und Multiplex
    (DIN EN 636) ist zulässig: bei Sperrholz ist die
    Haupttragrichtung ebenfalls die Decklage-Faserrichtung.

  Die Haupttragrichtung ist disjunkt zur **Plattenlängsrichtung**
  (`plattenlaengsrichtung`): Plattenlängsrichtung ist OSB-spezifisch
  (Modus SCHWACH, Strand-Richtung), Haupttragrichtung ist Mehrlagen-
  holz-spezifisch (Modus STRUKTURIERT, Decklagen-Richtung).
---

## Prosa-Definition

Die **Haupttragrichtung** eines Mehrlagenholzes ist ein
Einheitsvektor im Welt-Koordinatensystem, der in der Plattenebene
liegt, rechtwinklig zur Plattendicken-Achse steht und in Richtung der
Faserrichtung der äußeren Decklage zeigt, an der die höhere
Plattensteifigkeit (E_0,mean nach DIN EN 1995-1-1 / ProHolz) und
damit die bemessungsrelevante 0°-Richtung der Plattenfestigkeitswerte
ausgerichtet ist.

## Mathematische Definition

Sei

- e_hat_d ∈ S² die Plattendicken-Achse (siehe `plattendicken_achse`),
- L = (ℓ₀, …, ℓ_{n−1}) die Lagenstruktur des Mehrlagenholzes
  (siehe `lagenstruktur`), n ≥ 3,
- h_hat ∈ S² ein Einheitsvektor (siehe `einheitsvektor`).

Dann ist die **Haupttragrichtung** des Mehrlagenholzes definiert als

```
haupttragrichtung := h_hat
                   := ℓ₀.faserrichtung
                       (bis auf Vorzeichen),
```

mit den Konstruktions-Invarianten

```
(H1) Orthogonalität zur Plattendicken-Achse:
       ⟨h_hat, e_hat_d⟩ = 0     (mathematisch),
       | ⟨h_hat, e_hat_d⟩ | ≤ Toleranzen.WINKEL_EPS     (numerisch).

(H2) Decklage-Konsistenz:
       h_hat ≡ ℓ₀.faserrichtung     (bis auf Vorzeichen),
       d. h. | ⟨h_hat, ℓ₀.faserrichtung⟩ | ≥ 1 − Toleranzen.WINKEL_EPS.

(H3) Norm-Invariante:
       | ‖h_hat‖² − 1 | ≤ Toleranzen.NORM_EPS     (geerbt von einheitsvektor).
```

**Nebentragrichtung** (siehe eigener Eintrag `nebentragrichtung`):

```
n_hat := e_hat_d × h_hat ∈ S²,
```

mit ‖n_hat‖ = 1 wegen ⟨h_hat, e_hat_d⟩ = 0 und ‖h_hat‖ = ‖e_hat_d‖ = 1.

**Faserwinkel zur Kraft** (für Hankinson-Auswertung *gemittelt* über
das Bauteil; in der Praxis erfolgt die Bemessung pro Lage, siehe
`hankinson_winkel` und `mehrlagenholz`):

```
α(F_hat, h_hat) := arccos( | ⟨F_hat, h_hat⟩ | ) ∈ [0, π/2]
```

Die Hankinson-Formel ist auf der Bauteil-Ebene **nicht** direkt
anwendbar; sie muss pro Lage ausgewertet werden (vgl. Blaß/Flaig
2012 KIT).

## Wohldefiniertheit

- **Existenz**: Jede CLT-/Sperrholz-Platte hat per
  Lagenstruktur-Pflicht (n ≥ 3) eine Decklage 0 mit definierter
  Faserrichtung; daraus folgt die Haupttragrichtung eindeutig.
- **Eindeutigkeit bis auf Vorzeichen**: h_hat ist durch
  ℓ₀.faserrichtung bis auf Vorzeichen festgelegt.
  Vorzeichenkonvention ist beim Mehrlagenholz/Bauteil zu
  dokumentieren (typisch in Halbachse der längeren Plattenformat-
  Kante).
- **Pflichtcharakter**: Bei Werkstoff-Modus STRUKTURIERT ist
  `haupttragrichtung` Pflichtfeld am Werkstoff. Bei den anderen
  Modi nicht definiert.
- **Orthogonalitäts-Invariante (H1)**: h_hat ⊥ e_hat_d ist
  Konstruktions-Invariante; Verletzung ist Validierungsfehler.
- **Decklage-Konsistenz (H2)**: h_hat entspricht ℓ₀.faserrichtung bis
  auf Vorzeichen; diese Invariante ist Pflicht (auch bei
  abweichendem Lagenaufbau, vgl. `lagenstruktur` Invariante I5).
- **Eindeutigkeit der Nebentragrichtung**: n_hat = e_hat_d × h_hat ist
  algebraisch bestimmt (Rechte-Hand-Regel mit Welt-
  Rechtssystem konsistent).
- **Konsistenz mit Lagenstruktur**: alle Lagen-Faserrichtungen
  sind im Standardlayout parallel oder rechtwinklig zu h_hat
  (Lagenstruktur-Invariante I4); bei abweichendem Lagenaufbau
  ausgesetzt.
- **Nicht-Zirkularität**: Die Definition stützt sich auf
  `einheitsvektor`, `plattendicken_achse`, `lagenstruktur`,
  `toleranzen`. Sie verweist auf `nebentragrichtung` nur als
  abgeleitete Größe, nicht in der eigenen Definition.

## Erläuterung (nicht normativ)

### ProHolz-Definition

ProHolz Austria definiert in „Brettsperrholz Bemessung Band I"
wörtlich:

> **Haupttragrichtung (0°)**: Richtung der Decklamellen mit
> höherer Steifigkeit der Platte.

Diese Definition wird im Glossar wörtlich übernommen und durch
folgende Präzisierung formalisiert:

- „Decklamellen" = Lage 0 der Lagenstruktur (äußere Decklage).
- „Höhere Steifigkeit" = E_0,mean > E_90,mean (DIN EN 1995-1-1).
  Bei einer 5-lagigen 30/30/30/30/30-mm-Platte mit
  Faserrichtungen 0°/90°/0°/90°/0° und allen Lagen aus C24-Holz
  ist die Steifigkeit in 0°-Richtung höher, weil drei Lagen die
  Last aufnehmen, in 90°-Richtung nur zwei.
- Bei symmetrischen Standardlayouts (3, 5, 7 Lagen, ungerade)
  ist die 0°-Richtung gleich der Decklage-0-Faserrichtung.

### Verallgemeinerung auf Sperrholz und Multiplex

DIN EN 636 (Sperrholz) führt analog eine Decklage-Faserrichtung;
die Haupttragrichtung im Glossar ist auch hier die Faserrichtung
der äußersten Furnierlage. Multiplex (≥ 5 Lagen) folgt derselben
Konvention.

### Bemessung bei Mehrlagenholz

Die Bemessung von BSP/CLT-Bauteilen erfolgt nach EN 1995-1-1
Anhang B (γ-Verfahren) oder nach Schickhofer-Methodik. Beide
unterscheiden:

- **Plattenfestigkeit f_m,0,k**: parallel zur Haupttragrichtung
  (= Decklage-Richtung).
- **Plattenfestigkeit f_m,90,k**: parallel zur Nebentragrichtung
  (= 90° zur Decklage).

Bei Schubbeanspruchung sind zusätzlich die Lagen-Schubfestigkeiten
(Rollschub) maßgebend.

### Schnittwinkel-App: lagenweise

Die App muss bei einem Schnitt durch ein Mehrlagenholz die
Faserwinkel α_i = ∠(Schnittebene, ℓ_i.faserrichtung) **pro Lage**
berechnen, nicht einen einzelnen Bauteil-Winkel
α(Schnitt, h_hat). Die Haupttragrichtung dient dabei als Bezugsachse
für die UI-Darstellung („Schnitt schräg zur Haupttragrichtung")
und für die Plattenfestigkeits-Annotation, nicht für die
lagenweise Hankinson-Auswertung.

## Beziehungen

- **Oberbegriff**: `einheitsvektor`. Strukturell ist die
  Haupttragrichtung ein Einheitsvektor; das Mehrlagenholz-
  Spezifikum ist die semantische Rolle „Decklage-Richtung mit
  höherer Steifigkeit".
- **Verwendung**:
  - **Mehrlagenholz** (`mehrlagenholz`): Pflichtfeld; primäres
    Plattenebene-Richtungsfeld.
  - **Nebentragrichtung** (`nebentragrichtung`): abgeleitet als
    e_hat_d × h_hat.
  - **Lagenstruktur** (`lagenstruktur`): Invariante I5 verknüpft
    h_hat mit ℓ₀.faserrichtung.
  - **Hankinson-Winkel** (`hankinson_winkel`): bei Mehrlagenholz
    pro Lage; Haupttragrichtung dient als Bezugsachse für die
    Plattenfestigkeit, nicht für lagenweise Bemessung.
- **Abgrenzung**:
  - **`einheitsvektor`** (allgemein): trägt keine semantische
    Rolle.
  - **`plattendicken_achse`**: rechtwinklig zur Plattenebene;
    Haupttragrichtung liegt in der Plattenebene (rechtwinklig zur
    Plattendicken-Achse).
  - **`plattenlaengsrichtung`**: OSB-spezifisch (Modus SCHWACH);
    Haupttragrichtung ist Mehrlagenholz-spezifisch (Modus
    STRUKTURIERT). Disjunkt nach Werkstoff-Modus.
  - **`nebentragrichtung`**: 90° zur Haupttragrichtung in der
    Plattenebene; abgeleitet, redundant.
  - **`faserrichtung`**: Faserrichtung im engeren Sinn ist die
    L-Richtung der Holzfaser einer einzelnen Holzlamelle. Die
    Haupttragrichtung ist die makroskopische Decklage-
    Faserrichtung; sie stimmt mit ℓ₀.faserrichtung überein, hat
    aber eine andere semantische Rolle (Bauteil-Bemessungsachse vs.
    Lagen-Materialachse).

## Implementierungshinweis

Datentyp (Domänen-Schicht, Kotlin, Schicht
`domain.holzbau.werkstoff`):

```kotlin
package domain.holzbau.werkstoff

import domain.geometrie.Einheitsvektor

/**
 * Haupttragrichtung eines Mehrlagenholzes (CLT/BSP, Sperrholz,
 * Multiplex): Einheitsvektor in der Plattenebene, parallel zur
 * Decklage-Faserrichtung (Lage 0 der Lagenstruktur).
 * Glossar: hg_haupttragrichtung.md — ProHolz Austria 2014.
 *
 * Strukturell ein Wrapper um Einheitsvektor; semantische Rolle
 * 'Bauteil-0°-Bemessungsachse'. Pflichtfeld bei Mehrlagenholz.
 *
 * Konstruktions-Invarianten:
 *   H1: orthogonal zur Plattendicken-Achse (innerhalb WINKEL_EPS).
 *   H2: parallel zu lagenstruktur.lagen[0].faserrichtung
 *       (bis auf Vorzeichen).
 *   H3: Norm-Invariante (geerbt).
 */
@JvmInline
value class Haupttragrichtung(val richtung: Einheitsvektor) {
    val x: Double get() = richtung.x
    val y: Double get() = richtung.y
    val z: Double get() = richtung.z

    operator fun unaryMinus(): Haupttragrichtung =
        Haupttragrichtung(-richtung)
}
```

- **Einheit**: dimensionslos (geerbt).
- **Invarianten**: alle Invarianten von `Einheitsvektor` plus H1
  und H2; geprüft in `Mehrlagenholz.init`, weil dort
  Plattendicken-Achse und Lagenstruktur verfügbar sind.
- **Vorzeichenkonvention**: typisch in dieselbe Halbachse wie die
  längere Plattenformat-Kante; alle Plattenfestigkeiten f_0/f_90
  sind vorzeicheninvariant.
- **Edge Cases**:
  - **Verletzung H1** (Haupttragrichtung nicht rechtwinklig zur
    Plattendicken-Achse):
    `Entartet.HaupttragrichtungNichtOrthogonalZurPlattendickenAchse`.
  - **Verletzung H2** (Haupttragrichtung nicht parallel zur
    Decklage-Faserrichtung):
    `Entartet.HaupttragrichtungInkonsistentZurDecklage`.
  - **Mehrlagenholz mit ungewöhnlicher Decklage** (z. B. 45°-Lage):
    Haupttragrichtung folgt trotzdem ℓ₀.faserrichtung, weil I5
    auch bei abweichendem Lagenaufbau gilt. Der UI sollte die
    Sondersituation explizit anzeigen.
- **IFC-Mapping** (Persistenzschicht): nicht direkt abgebildet;
  die Haupttragrichtung ergibt sich aus
  `IfcMaterialLayerSet.LayerSetDirection` plus Decklage-Faserrichtung.
- **Verwendungsregel**: Funktionen, die plattenebenebezogene
  Festigkeiten (f_m,0, f_m,90) berechnen, nehmen
  `Haupttragrichtung` als Parametertyp und nicht den nackten
  `Einheitsvektor`. Dadurch wird die semantische Rolle am API-Rand
  sichtbar.

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

- ETAs der CLT-Hersteller (KLH ETA-06/0138, Stora Enso ETA-14/0349,
  Hasslacher ETA-12/0281, Binderholz ETA-11/0210), abgerufen
  2026-05-08.
- Wikipedia, Lemma „Brettsperrholz" (abgerufen 2026-05-08).
