---
id: lagenstruktur
benennung: Lagenstruktur
synonyme: ["Lagenaufbau", "Lagenfolge", "Schichtaufbau (im Mehrlagenholz)", "lay-up"]
abgelehnte_benennungen: [Schichtung, Plattenaufbau, "layer set", "stack", "ply schedule"]
oberbegriff: null
begriffstyp: partitiv
voraussetzungen: [lage, einheitsvektor, toleranzen]
abgrenzung_zu: [lage, mehrlagenholz, haupttragrichtung, plattendicken_achse]
status: entwurf
subglossar_pendant: notwendig
quellen_primär:
  - "DIN EN 16351:2021-08, 'Holzbauwerke – Brettsperrholz – Anforderungen', Abschnitt 5 (Lagenaufbau): Mindestanzahl 3 Lagen, kreuzweise (typ. 0°/90°) verleimt, in der Regel ungerade Anzahl mit symmetrischem Aufbau (Decklage 0 = Decklage n−1)."
  - "DIN EN 636:2015-06, 'Sperrholz – Anforderungen': mindestens 3 Furnierlagen, in der Regel ungerade Anzahl, symmetrischer Aufbau (zur Vermeidung von Schüsselung)."
  - "DIN EN 1995-1-1:2010-12 (Eurocode 5), Abschnitt 9 und Anhang B (γ-Verfahren mit Lagenstruktur als Eingabe der Bemessung)."
quellen_sekundär:
  - "Schickhofer, G.; Bogensperger, T.; Moosbrugger, T. (Hrsg.): BSPhandbuch — Holz-Massivbauweise in Brettsperrholz. 2. Aufl., TU Graz 2010, Kap. 3 (Lagenaufbau, Symmetrie-Regel, Standardlayouts)."
  - "Blaß, H. J.; Flaig, M.: Stabförmige Bauteile aus Brettsperrholz. Karlsruher Berichte zum Ingenieurholzbau, Bd. 24, KIT Scientific Publishing, Karlsruhe 2012, DOI 10.5445/KSP/1000030362, Kap. 2 und 3."
  - "ProHolz Austria: Brettsperrholz Bemessung Band I. Wien 2014, Kap. 3 und 4 (Standard-CLT-Layouts 3-/5-/7-lagig, Symmetrie, Decklagen-Regel)."
  - "Niemz, P.; Sonderegger, W.: Physik des Holzes und der Holzwerkstoffe. Hanser, München 2017, Kap. 7 (Sperrholz, Brettsperrholz, Lagenaufbauten und Symmetrie)."
quellenkonflikt: |
  Die normative Symmetrie-Regel für CLT-Lagenaufbauten ist klar
  formuliert: ungerade Lagenanzahl, kreuzweise Faserrichtung
  (typ. 0°/90°), Decklage 0 und Decklage n−1 in derselben
  Faserrichtung. Sperrholz folgt analog (DIN EN 636). EC5 und SIA 265
  setzen diese Standardstruktur voraus, lassen aber abweichende
  Lagenaufbauten durch ETA / Bauteilzulassung zu (z. B. asymmetrische
  Layouts, 45°-Lagen).

  Eigene Festlegung in diesem Glossar:

  - Eine **Lagenstruktur** ist im Glossar das **Aggregat einer
    geordneten Lagenliste** mit n ≥ 3 plus einem Marker
    `abweichenderLagenaufbau: Boolean`. Pflichtfeld bei
    `mehrlagenholz` (Modus STRUKTURIERT).
  - **Standardlayout** (klassisches CLT/Sperrholz, Schickhofer 2010,
    DIN EN 16351): n ungerade, Decklage 0 und Decklage n−1
    in derselben Faserrichtung, alle Lagen-Faserrichtungen parallel
    oder rechtwinklig zur Haupttragrichtung. In diesem Fall ist
    `abweichenderLagenaufbau = false`.
  - **Abweichende Lagenaufbauten** (asymmetrisch, gerade Lagenanzahl,
    45°-Lagen): zulässig durch explizite Markierung
    `abweichenderLagenaufbau = true`. In diesem Fall werden die
    Symmetrie- und Orthogonalitäts-Invarianten ausgesetzt; der
    Bauteil-Träger trägt die Zulässigkeit über die ETA.
  - **Mindest-Lagenanzahl 3** ist Klassen-Invariante: zwei kreuzweise
    Lagen sind ein Sonderfall, der nicht zur Klasse Mehrlagenholz
    zählt; eine Lage ist BSH (`axiales_holz`).
  - **Symmetrie-Regel** als formale Invariante:
    `abweichenderLagenaufbau == false ⇒
       n ungerade UND lagen[0].faserrichtung = lagen[n−1].faserrichtung
       (bis auf Vorzeichen)`.
  - **Lagenausrichtungs-Regel** als formale Invariante:
    `abweichenderLagenaufbau == false ⇒
       ∀ i : ∠(lagen[i].faserrichtung, h_hat) ∈ {0, π/2}` (innerhalb
    Toleranzen.WINKEL_EPS).
  - **Position-Bijektivität**: die `position`-Felder der Lagen sind
    eine Bijektion auf {0, …, n−1} und stimmen mit der Listenreihung
    überein.
  - **Gesamtdicke** ist eine **abgeleitete Größe** (Σ Lagendicken),
    nicht Pflichtfeld.
---

## Prosa-Definition

Eine **Lagenstruktur** ist das Aggregat aus einer geordneten,
endlichen Liste von mindestens drei Lagen (n ≥ 3) plus einem
Markierungsfeld „abweichender Lagenaufbau", das den vollständigen
Schichtaufbau eines Mehrlagenholzes (CLT/BSP, Sperrholz, Multiplex)
in Stapelrichtung der Plattendicken-Achse beschreibt und das im
Standardfall die Symmetrie-Regel der DIN EN 16351 bzw. DIN EN 636
(ungerade Lagenanzahl, identische Decklagen-Faserrichtung,
kreuzweise wechselnde Lagenfaserrichtungen parallel oder rechtwinklig
zur Haupttragrichtung) erfüllt.

## Mathematische Definition

Sei

- 𝓛 die Menge der Lagen (siehe `lage`),
- h_hat ∈ S² die Haupttragrichtung des umgebenden Mehrlagenholzes
  (siehe `haupttragrichtung`),
- ε_W := Toleranzen.WINKEL_EPS.

Dann ist eine **Lagenstruktur** L das Tupel

```
L := (lagen, abweichenderLagenaufbau)
```

mit

- **lagen** = (ℓ₀, ℓ₁, …, ℓ_{n−1}) ∈ 𝓛^n, n ≥ 3,
- **abweichenderLagenaufbau** ∈ {true, false}.

**Klassen-Invarianten** (alle prüfbar):

```
(I1) Mindestanzahl:
       |lagen| = n ≥ 3.

(I2) Position-Bijektivität:
       ∀ i ∈ {0, …, n−1} : lagen[i].position = i.

(I3) Symmetrie-Regel (im Standardlayout):
       abweichenderLagenaufbau = false  ⇒
         (n ungerade)  ∧
         (lagen[0].faserrichtung ≡ lagen[n−1].faserrichtung
          bis auf Vorzeichen, d. h.
          | ⟨lagen[0].faserrichtung, lagen[n−1].faserrichtung⟩ |
          ≥ 1 − ε_W).

(I4) Lagenausrichtungs-Regel (im Standardlayout):
       abweichenderLagenaufbau = false  ⇒
         ∀ i : ∠(lagen[i].faserrichtung, h_hat) ∈ {0, π/2}
              (innerhalb ε_W),
       d. h. jede Lagen-Faserrichtung ist parallel oder rechtwinklig
       zur Haupttragrichtung.

(I5) Decklage steuert Haupttragrichtung:
       lagen[0].faserrichtung ≡ h_hat
       (bis auf Vorzeichen; immer, unabhängig von
        abweichenderLagenaufbau).
```

**Abgeleitete Größe — Gesamtdicke**:

```
gesamtdicke(L) := Σ_{i=0}^{n−1} lagen[i].dicke ∈ ℝ⁺
```

Die Gesamtdicke entspricht der Plattendicke nach DIN EN 13986 und
ist redundant zum Bauteil-Volumen (Folge-Eintrag).

**Lagen-Mittenebenen** (abgeleitet, für Visualisierung):

```
z_i := −gesamtdicke(L)/2 + Σ_{j=0}^{i−1} lagen[j].dicke
                          + lagen[i].dicke / 2
```

(Position der Lage ℓ_i entlang der Plattendicken-Achse, gemessen
von der Plattenmittelebene).

## Wohldefiniertheit

- **Existenz**: Für jedes nach DIN EN 16351 oder EN 636
  zertifizierte Mehrlagenprodukt ist die Lagenstruktur in der ETA
  bzw. im Datenblatt explizit dokumentiert.
- **Eindeutigkeit der Reihenfolge**: Die Lagenliste ist eine
  geordnete Folge; Reihenfolge entspricht der physikalischen
  Stapelung entlang der Plattendicken-Achse (von position 0 außen
  bis position n−1 außen).
- **Mindestanzahl 3 (I1)**: Klassen-Invariante. Zwei kreuzweise
  Lagen sind kein Mehrlagenholz im Sinne dieses Glossars; eine
  Lage ist BSH (`axiales_holz`).
- **Position-Bijektivität (I2)**: Die `position`-Felder sind
  eindeutig 0…n−1; doppelte oder fehlende Positionen sind
  Validierungsfehler.
- **Symmetrie-Regel (I3)**: Klassische CLT-Symmetrie ist im
  Standardlayout Pflicht. Bei `abweichenderLagenaufbau = true`
  ausgesetzt; die Verantwortung liegt dann bei der ETA des
  Bauteilherstellers.
- **Lagenausrichtungs-Regel (I4)**: Im Standardlayout ist jede
  Lagen-Faserrichtung parallel oder rechtwinklig zur
  Haupttragrichtung (also 0° oder 90°). Bei
  `abweichenderLagenaufbau = true` (z. B. 45°-Lagen)
  ausgesetzt.
- **Decklage steuert Haupttragrichtung (I5)**: Diese Invariante
  gilt **immer** (auch bei abweichendem Lagenaufbau), weil die
  Haupttragrichtung per Definition (ProHolz, DIN EN 16351) durch
  die Decklage 0 festgelegt ist.
- **Gesamtdicke wohldefiniert**: Σ Lagendicken ist eine endliche
  Summe positiver Reeller, also ∈ ℝ⁺.
- **Konsistenz mit Plattendicken-Achse**: Die Stapelrichtung der
  Lagen ist parallel zur Plattendicken-Achse des umgebenden
  Mehrlagenholzes; diese Konsistenz wird in `mehrlagenholz`
  geprüft, nicht in `lagenstruktur` selbst.
- **Nicht-Zirkularität**: Die Definition stützt sich auf `lage`,
  `einheitsvektor` und `toleranzen`. Sie verweist auf
  `haupttragrichtung` nur als externes Bezugsfeld in den
  Konsistenzbedingungen, nicht in der Definition selbst.

## Erläuterung (nicht normativ)

### Standardlayouts (DIN EN 16351, ProHolz, Schickhofer)

Klassische CLT-Standardlayouts:

```
3-lagig:   0° / 90° / 0°
5-lagig:   0° / 90° / 0° / 90° / 0°
7-lagig:   0° / 90° / 0° / 90° / 0° / 90° / 0°
```

Alle erfüllen Symmetrie (I3) und Lagenausrichtung (I4):

- ungerade Lagenanzahl;
- Decklage 0 und Decklage n−1 in 0°-Richtung (= h_hat);
- alle Lagen-Faserrichtungen ∈ {0°, 90°}.

Die Symmetrie verhindert Schüsselung beim Trocknen und macht das
Bauteil zweiseitig gleichwertig.

### Abweichende Lagenaufbauten

Beispiele für `abweichenderLagenaufbau = true`:

- **45°-Lagen** für Erdbeben-Aussteifung: ein 5-lagiges Layout
  0°/45°/90°/−45°/0° verteilt die Schubaufnahme über alle
  Plattenrichtungen; nicht in I4 (parallel/rechtwinklig zu h_hat).
- **Asymmetrisch**: 0°/90°/0°/90° (4 Lagen, gerade Anzahl) verletzt
  Symmetrie (I3); zulässig nur durch ETA-Zulassung.
- **Mischfestigkeiten**: jede Lage trägt eine eigene
  Festigkeitsklasse; Lagenstruktur erlaubt das standardmäßig
  (Pflichtfeld pro Lage).

### Gesamtdicke und Plattenmaße

Die Gesamtdicke der Lagenstruktur entspricht der Plattendicke
nach DIN EN 13986 (z. B. CLT 3000 × 1250 × 100 mm: gesamtdicke =
100 mm). Sie ist abgeleitet, nicht eigenes Pflichtfeld; bei
Konstruktion ist Gesamtdicke = Σ Lagendicken zu prüfen
(Konsistenz mit dem Bauteil-Plattenmaß; geprüft in `bauteil` /
`mehrlagenholz`).

### Visualisierung der Lagen — Schnittwinkel-App

Die Schnittwinkel-Visualisierung (Kernfunktion dieser App) muss
für ein Mehrlagenholz-Bauteil bei einem Schnitt:

1. die Lagenstruktur durchlaufen,
2. für jede Lage den Faserwinkel α_i zwischen Schnittebene und
   Lagen-Faserrichtung berechnen (siehe `hankinson_winkel`),
3. die Lagen-Mittenebenen z_i als Tiefeninformation visualisieren
   (Blass/Flaig 2012).

Eine einzelne „Bauteil-Faserrichtung" gibt es bei
`mehrlagenholz` nicht; die App muss alle Lagen mit
ihren individuellen Faserrichtungen darstellen.

## Beziehungen

- **Oberbegriff**: keiner. Lagenstruktur ist ein eigenständiges
  Aggregat.
- **Bestandteile**:
  - **Lagen** (`lage`): geordnete Liste mit n ≥ 3.
  - **Marker** `abweichenderLagenaufbau`: Boolean.
  - **Abgeleitet**: Gesamtdicke = Σ Lagendicken.
- **Verwendung**:
  - **Mehrlagenholz** (`mehrlagenholz`): Pflichtfeld; einziges
    Werkstoff-internes Aggregat des Modus STRUKTURIERT.
  - **Hankinson-Winkel pro Lage** (`hankinson_winkel`): Eingabe
    für die lagenweise Auswertung von α.
- **Abgrenzung**:
  - **`lage`**: einzelne Lage; Bestandteil der Lagenstruktur.
  - **`mehrlagenholz`**: der Werkstoff, der die Lagenstruktur als
    Pflichtfeld trägt.
  - **`haupttragrichtung`**: Einheitsvektor; durch Decklage 0
    festgelegt (Invariante I5). Lagenstruktur und
    Haupttragrichtung sind verbunden, aber begrifflich getrennt.
  - **`plattendicken_achse`**: Stapelrichtung der Lagen;
    konsistent mit Lagenstruktur, geprüft in `mehrlagenholz`.
  - **„Schichtaufbau"** (umgangssprachlich): synonym verwendet,
    aber unscharf. Lagenstruktur ist die formale Repräsentation.

## Implementierungshinweis

Datentyp (Domänen-Schicht, Kotlin, Schicht
`domain.holzbau.werkstoff`):

```kotlin
package domain.holzbau.werkstoff

/**
 * Lagenstruktur eines Mehrlagenholzes (CLT/BSP, Sperrholz,
 * Multiplex): geordnete Liste von Lagen mit n >= 3 plus Marker
 * für abweichende Lagenaufbauten.
 * Glossar: hg_lagenstruktur.md
 *
 * Standardlayout: ungerade Lagenanzahl, Decklage 0 = Decklage n-1
 * (Symmetrie), alle Faserrichtungen parallel/rechtwinklig zur
 * Haupttragrichtung. Bei abweichenderLagenaufbau = true werden
 * Symmetrie und Orthogonalitaet ausgesetzt (z. B. 45°-Lagen,
 * asymmetrische Layouts).
 *
 * Gesamtdicke ist abgeleitet (Sum Lagendicken).
 */
data class Lagenstruktur(
    val lagen: List<Lage>,
    val abweichenderLagenaufbau: Boolean = false
) {
    /** Abgeleitete Gesamtdicke in mm. */
    val gesamtdicke: Double get() = lagen.sumOf { it.dicke }

    init {
        // I1: Mindestanzahl
        require(lagen.size >= 3) {
            "Lagenstruktur braucht mindestens 3 Lagen, hat ${lagen.size}"
        }
        // I2: Position-Bijektivitaet
        require(lagen.withIndex().all { (i, l) -> l.position == i }) {
            "Lagen-Positionen muessen 0..n-1 sein und mit Listenindex uebereinstimmen"
        }
        // I3 + I4: Symmetrie + Orthogonalitaet werden in der
        // konstruktion des Mehrlagenholzes geprueft, weil dort die
        // Haupttragrichtung verfuegbar ist.
    }

    companion object {
        /**
         * Prueft Symmetrie-Regel I3 gegen die uebergebene
         * Haupttragrichtung. Wird in Mehrlagenholz.init aufgerufen.
         */
        fun pruefeSymmetrie(
            ls: Lagenstruktur,
            haupttragrichtung: Einheitsvektor,
            winkelEps: Double
        ): Resultat<Unit, EntartetGeometrie> { /* ... */ TODO() }
    }
}
```

- **Einheit**: `gesamtdicke` in mm (Double). Übrige Felder
  dimensionslos.
- **Identität**: keine; Werteklasse / data class.
- **Invarianten**:
  1. (I1) `lagen.size >= 3`.
  2. (I2) Position-Bijektivität: `lagen[i].position == i`.
  3. (I3, I4, I5) werden in `Mehrlagenholz.init` geprüft, weil
     die Haupttragrichtung dort verfügbar ist.
- **IFC-Mapping** (Persistenzschicht):
  - `IfcMaterialLayerSet` mit `IfcMaterialLayer`-Liste in
    derselben Reihenfolge wie `lagen`.
  - `IfcMaterialLayerSet.LayerSetDirection = AXIS3` (parallel zur
    Plattendicken-Achse).
  - `IfcMaterialLayer.Priority = lagen[i].position`.
- **Edge Cases**:
  - **Lagenstruktur mit < 3 Lagen**:
    `IllegalArgumentException` bzw.
    `Entartet.LagenstrukturZuWenigeLagen`.
  - **Doppelte Lagenpositionen**: `IllegalArgumentException`
    bzw. `Entartet.LagenpositionenNichtBijektiv`.
  - **Symmetrie-Verletzung im Standardlayout**: in
    `Mehrlagenholz.init` zurückgewiesen, sofern
    `abweichenderLagenaufbau = false`.
  - **Gerade Lagenanzahl im Standardlayout**: Symmetrie-Regel I3
    fordert ungerade Anzahl; gerade Anzahl nur bei
    `abweichenderLagenaufbau = true`.
  - **45°-Lagen**: zulässig nur bei
    `abweichenderLagenaufbau = true`.
- **Bezeichner-Konvention** (CLAUDE.md): Domänen-Klasse heißt
  `Lagenstruktur` (deutsch, Glossarbegriff).

## Quellen

**Primär (normativ):**

- DIN EN 16351:2021-08, „Holzbauwerke – Brettsperrholz".
- DIN EN 636:2015-06, „Sperrholz – Anforderungen".
- DIN EN 1995-1-1:2010-12, „Eurocode 5", Abschnitt 9 und
  Anhang B.

**Sekundär:**

- Schickhofer, G.; Bogensperger, T.; Moosbrugger, T. (Hrsg.):
  *BSPhandbuch.* 2. Aufl., TU Graz 2010.
- Blaß, H. J.; Flaig, M.: *Stabförmige Bauteile aus
  Brettsperrholz.* KIT Scientific Publishing, Karlsruhe 2012.
- ProHolz Austria: *Brettsperrholz Bemessung Band I.* Wien 2014.
- Niemz, P.; Sonderegger, W.: *Physik des Holzes und der
  Holzwerkstoffe.* Hanser, München 2017.

**Korpus (nicht autoritativ):**

- ETAs der CLT-Hersteller (KLH ETA-06/0138, Stora Enso ETA-14/0349,
  Hasslacher ETA-12/0281, Binderholz ETA-11/0210), abgerufen
  2026-05-08.
- Wikipedia, Lemmata „Brettsperrholz", „Sperrholz" (abgerufen
  2026-05-08).
