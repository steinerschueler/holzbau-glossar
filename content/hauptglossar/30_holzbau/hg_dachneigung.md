---
id: dachneigung
benennung: Dachneigung
synonyme: [Dachneigungswinkel, Neigung, "Neigungswinkel der Dachfläche"]
abgelehnte_benennungen: [Dachschräge, Dachschrägung, Dachpitch, Dachgefälle, "roof pitch", "roof slope", "roof angle"]
oberbegriff: einheitsvektor
begriffstyp: merkmal
voraussetzungen: [vektor, einheitsvektor, dachflaeche, toleranzen]
abgrenzung_zu: [dachflaeche, dachschraege, dachseite, faserrichtung, neigungswinkel]
status: entwurf
theorie_pflichtig: required
quellen_primär:
  - "SIA 232/1:2020 'Geneigte Dächer', Schweizerischer Ingenieur- und Architektenverein, Abschnitt 1 (Begriffe und geometrische Grundlagen): Neigung als Winkel der Dachfläche zur Horizontalen."
  - "DIN EN 1991-1-3:2010-12 'Eurocode 1 – Einwirkungen auf Tragwerke – Teil 1-3: Schneelasten', Abschnitt 5.3 und Anhang A: Formbeiwerte μ_i als Funktion der Dachneigung α."
  - "DIN EN 1991-1-4:2010-12 'Eurocode 1 – Einwirkungen auf Tragwerke – Teil 1-4: Windlasten', Abschnitt 7.2: Druck- und Sogbeiwerte als Funktion der Dachneigung."
  - "DIN 1055-5:1975-06 (zurückgezogen, übergeleitet in DIN EN 1991-1-3) 'Lastannahmen für Bauten – Schneelasten', Abschnitt 4: Schneelast als Funktion der Dachneigung."
quellen_sekundär:
  - "Lignum (Hrsg.): Lignatec 'Geneigte Dächer in Holzbauweise', Lignum, Zürich, aktuelle Auflage, Kap. 'Dachformen und Neigungen'."
  - "Lignum (Hrsg.): Holzbautabellen HBT, Lignum, Zürich, aktuelle Auflage, Tab. 'Übliche Dachneigungen'."
  - "Mönck, W.; Rug, W.: Holzbau – Bemessung und Konstruktion. 16. Aufl., Beuth Verlag 2015, Kap. 'Dachformen'."
  - "Gerner, M.: Fachwerk – Instandsetzung, Sanierung, Neubau. DVA, 7. Aufl. 2007, Glossar 'Dachneigung'."
  - "Holzbau Deutschland, Merkblatt 'Begriffe und Klassifizierungen für den Holzbau', Eintrag 'Dachneigung'."
quellenkonflikt: |
  Die kategoriale Einteilung der Dachneigung in „flach", „flach
  geneigt", „geneigt" und „steil" wird in keiner der konsultierten
  Normen einheitlich festgelegt. SIA 232/1 spricht ab etwa 10° von
  „geneigten Dächern" als Geltungsbereich; DIN 18531 trennt zwischen
  „nicht genutzten Dächern" und „genutzten Dächern" ohne Neigungs-
  Schwelle. EN 1991-1-3 (Schneelasten) verwendet feste Neigungs-
  Schwellen (15°, 30°, 60°) als Knickpunkte der Formbeiwerte μ_1,
  μ_2, ohne sie als „steil" oder „flach" zu benennen.

  Eigene Festlegung: Die hier angegebenen Faustbereiche
  (< 10° Flachdach, 10–20° schwach geneigt, 20–60° geneigt,
  > 60° steil) sind branchenübliche Orientierungswerte aus Lignum
  und Mönck/Rug; sie sind im Glossar **nicht normativ**, sondern
  rein deskriptiv. Die formale Definition der Dachneigung ist
  konsistent mit allen konsultierten Normen.

  „Dachschräge" ist im Sprachgebrauch häufig synonym für
  Dachneigung verwendet, im Glossar jedoch ein anderer Begriff
  (geometrische Untersicht; siehe `dachschraege`).
---

## Prosa-Definition

Die **Dachneigung** einer Dachfläche ist der Winkel α zwischen der
Trägerebene der Dachfläche und der Horizontalebene, gemessen über das
Skalarprodukt der nach außen gerichteten Einheits-Normalen der
Dachfläche mit der vertikalen Achse e_z, mit Wertebereich
α ∈ [0, π/2].

## Mathematische Definition

Sei

- D = (E, P, n_a) eine Dachfläche im Sinne von `dachflaeche` mit
  Trägerebene E, Umrisspolygon P und nach außen gerichteter
  Einheits-Normale n_a ∈ S² mit ⟨n_a, e_z⟩ ≥ 0,
- e_z = (0, 0, 1)ᵀ die vertikale Achse des Welt-Koordinatensystems
  (Rechtssystem, z nach oben).

Dann ist die **Dachneigung** der Dachfläche D der Winkel

```
α(D) := arccos(⟨n_a, e_z⟩) ∈ [0, π/2].
```

Äquivalente Charakterisierung über die Falllinie: Sei
ê_fall ∈ E ∩ S² die Einheitsrichtung der Falllinie von D im
Sinne von `hg_falllinie.md`, also der in E liegende Einheitsvektor
mit minimaler z-Komponente. Nach der dort fixierten
**Vorzeichenkonvention** zeigt ê_fall **nach unten**:
⟨ê_fall, e_z⟩ ≤ 0, also (ê_fall)_z ≤ 0. Diese Vorzeichenwahl
ist für die folgenden Identitäten bindend; Leser, die ältere
Fassungen dieses Eintrags mit einem bergauf-orientierten
Symbol `m̂` in Erinnerung haben, beachten, dass die hier
verwendete Größe ê_fall genau die antipodale (bergab-)
Lesart trägt. Eine bergauf-Richtung in der Trägerebene ist
−ê_fall; sie kommt in dieser App nur über die Bauteilachse
eines Sparrens vor (`hg_bauteilachse.md`, `hg_falllinie.md` Symbol-
Konvention) und nicht in der Dachneigungs-Definition selbst.

Mit dieser Konvention gilt

```
α(D) = arccos(⟨−ê_fall, e_xy⟩) = arcsin(|(ê_fall)_z|),
```

wobei e_xy = ê_fall − ⟨ê_fall, e_z⟩ · e_z, normiert, die
horizontale Projektion der Falllinie ist (definiert für
α < π/2). Der Steigungs-Tangens

```
tan(α(D)) = |(ê_fall)_z| / ‖ê_fall − ⟨ê_fall, e_z⟩ · e_z‖
```

ist der „Höhenunterschied pro horizontalem Abstand" entlang der
Falllinie und entspricht der in Prozent angegebenen Holzbau-Praxis:

```
Neigung in Prozent := 100 · tan(α(D)).
```

**Anzeigeformen** (intern Radiant, ausschließlich am API-Rand
konvertiert):

```
α_grad    := α · 180 / π                 (Grad, Hauptanzeige)
α_prozent := 100 · tan(α)                (Prozent, Holzbau-Praxis)
```

## Wohldefiniertheit

- **Existenz und Eindeutigkeit**: Für jede Dachfläche D ist n_a per
  Definition eindeutig (siehe `dachflaeche`, Bedingung 2:
  ⟨n_a, e_z⟩ ≥ 0). Damit ist arccos(⟨n_a, e_z⟩) ∈ [0, π/2]
  eindeutig bestimmt. arccos ist auf [−1, 1] eindeutig und stetig;
  ⟨n_a, e_z⟩ ∈ [0, 1] für jede zulässige Dachflächen-Normale.
- **Äquivalenz Falllinie ↔ Normale**: Die Falllinie ê_fall liegt
  in E und hat ⟨ê_fall, e_z⟩ = (ê_fall)_z minimal unter allen
  Einheitsvektoren in E. Aus ⟨n_a, e_z⟩ = cos(α) und
  ⟨ê_fall, e_z⟩ = −sin(α) (mit Vorzeichenkonvention
  (ê_fall)_z ≤ 0 nach `hg_falllinie.md`) folgt
  arccos(⟨n_a, e_z⟩) = arcsin(|(ê_fall)_z|). Beide
  Charakterisierungen liefern denselben Winkel. Im Grenzfall
  α = 0 ist ê_fall nicht eindeutig (jede Richtung in der
  horizontalen Trägerebene ist „flachste" Falllinie); die
  Definition über die Normale bleibt jedoch wohldefiniert mit
  α = 0.
- **Vorzeichenkonvention der Falllinie**: (ê_fall)_z ≤ 0 fixiert
  das Vorzeichen, sodass ê_fall stets „nach unten" zeigt;
  antipodale Mehrdeutigkeit wird damit aufgelöst. Diese
  Konvention ist normativ in `hg_falllinie.md` festgehalten und im
  gesamten Glossar verbindlich.
- **Wertebereich**: α ∈ [0, π/2]. Die Untergrenze α = 0 entspricht
  einer horizontalen Dachfläche (Flachdach); die Obergrenze
  α = π/2 ist nach `dachflaeche`-Bedingung 3 (α < π/2)
  ausgeschlossen — eine senkrechte Fläche ist eine Wand, keine
  Dachfläche.
- **Numerische Wohldefiniertheit**: Für n_a mit
  | ‖n_a‖² − 1 | ≤ NORM_EPS gilt
  ⟨n_a, e_z⟩ ∈ [−1 − ε, 1 + ε] mit ε ≪ 1; im Bereich
  ⟨n_a, e_z⟩ ∈ [0, 1] ist arccos numerisch gut konditioniert.
  Werte knapp über 1 (z. B. 1 + 10⁻¹⁵) werden vor dem arccos auf
  [0, 1] geclamped.
- **Konsistenz Anzeigeformen**: α_grad = α · 180/π ist eine
  Bijektion auf [0, 90]; α_prozent = 100 · tan(α) ist auf
  [0, π/2) streng monoton wachsend, mit α_prozent → ∞ für
  α → π/2. Die Holzbau-Praxis verwendet beide Formen abwechselnd,
  darum sind beide am API-Rand bereitgestellt.
- **Nicht-Zirkularität**: Die Definition stützt sich nur auf
  `vektor`, `einheitsvektor`, `dachflaeche` (mit ihrer äußeren
  Normalen) und `toleranzen`. Sie kommt nicht in ihrer eigenen
  Definition vor.

## Erläuterung (nicht normativ)

Die Dachneigung ist die zentrale formgebende Kenngröße einer
Dachfläche: sie bestimmt das Abflussverhalten von Niederschlag, die
Anwendbarkeit verschiedener Eindeckungsmaterialien (Ziegel benötigen
typisch ≥ 22°, Schindeln ≥ 14°, Blech ab 3°), die Schneelastansätze
(EN 1991-1-3) und die Windlastfallunterscheidung (EN 1991-1-4).

**Faustbereiche (Orientierungshinweis, nicht normativ)** — übliche
Branchenklassifikation aus Lignum und Mönck/Rug:

| Klasse                  | Bereich        | typische Eindeckungen        |
|-------------------------|----------------|------------------------------|
| Flachdach               | < 10°          | Bitumen, Folie, Begrünung    |
| schwach geneigtes Dach  | 10° – 20°      | Blech, Schindel mit Unterdach|
| geneigtes Dach          | 20° – 60°      | Ziegel, Naturschiefer        |
| steiles Dach            | > 60°          | Schiefer, Ortgang-orientiert |

Diese Bereiche sind **kein Normwerk**, sondern gängige
Branchenwerte. Die exakten Schwellen für Schnee- und Windlast-
Formbeiwerte sind in EN 1991-1-3 (15°, 30°, 60°) bzw. EN 1991-1-4
(5°, 15°, 30°, 45°, 60°, 75°) angegeben und unabhängig von der
Branchenklassifikation zu verwenden.

**Anzeigeformen in der Praxis**: Im Holzbau ist sowohl die Angabe
in **Grad** (Dachdecker, Architektur, Bemessungsnormen) als auch in
**Prozent** (Tiefbau, Strassenbau-nahe Konventionen, Schweizer
Bauplanung) verbreitet; Prozent ist dabei der Tangens · 100, nicht
der Winkel selbst. 100 % Neigung entspricht 45°, nicht 90°. Die
Domänen-Schicht hält den Winkel stets in **Radiant** vor und
konvertiert nur am API-Rand zur Anzeige.

Die **Falllinie** einer Dachfläche ist diejenige Gerade in der
Trägerebene, entlang derer das Wasser am steilsten abfließt; sie
steht im rechten Winkel zu allen Höhenlinien (näherungsweise
horizontalen Schnittlinien) der Dachfläche und insbesondere im
rechten Winkel zur Trauflinie. Der Steigungswinkel der Falllinie
gegenüber der Horizontalen ist exakt die Dachneigung α.

## Beziehungen

- **Oberbegriff**: `einheitsvektor` als formaler Träger (über die
  Normalencharakterisierung); fachlich ist α ein Winkelmerkmal
  einer Dachfläche, also ein **Merkmal** im Sinne der
  Begriffstypisierung.
- **Verwendungskontext**: jeder Dachflächen-Begriff
  (`dachflaeche`), alle dachlast-relevanten Begriffe
  (Schneelast, Windlast, Niederschlagsabfluss).
- **Abgrenzung**:
  - **`dachflaeche`**: zweidimensionales geometrisches Flächenstück;
    die Dachneigung ist eine ihrer skalaren Eigenschaften, kein
    eigenständiges Bauteil.
  - **`dachschraege`** (eigener Eintrag): die innen sichtbare
    Untersicht der Dachkonstruktion. Geometrisch eine **Fläche**,
    nicht ein Winkel. Die häufige sprachliche Verwendung von
    „Dachschräge" für „Dachneigung" wird hier als
    `abgelehnte_benennung` geführt, weil im Glossar trennscharf.
  - **`dachseite`** (eigener Eintrag): eine Dachfläche unter
    zusätzlicher Orientierungs-/Lage-Annotation (z. B.
    Wetterseite). Dachseite ist eine Fläche, kein Winkel.
  - **„Neigungswinkel"** (allgemein): in der allgemeinen Geometrie
    der Winkel zwischen einer Geraden oder Ebene und einer
    Bezugsebene. Dachneigung ist die Anwendung dieses Begriffs auf
    die spezifische Bezugsebene = Horizontalebene und das
    spezifische Objekt = Dachfläche. Im Glossar wird der
    allgemeine Neigungswinkel nicht eigenständig geführt.
  - **„Dachgefälle"**: in einigen Quellen synonym verwendet, in
    der Schweiz aber stärker mit Flachdach-/Abdichtungspraxis
    konnotiert. Hier abgelehnt zugunsten von „Dachneigung".

## Implementierungshinweis

Datentyp (Domänen-Schicht, Kotlin, Schicht `domain.bauteil` bzw.
`domain.geometrie`):

```
package domain.bauteil

import domain.geometrie.Einheitsvektor
import domain.geometrie.Vektor
import domain.Toleranzen
import kotlin.math.acos
import kotlin.math.tan
import kotlin.math.PI

/**
 * Dachneigung als Funktion einer Dachfläche.
 * Glossar: hg_dachneigung.md
 *
 * Wird als reine Funktion auf Dachflaeche bereitgestellt, nicht als
 * eigenständiger Datentyp: die Neigung ist ein abgeleitetes Merkmal,
 * keine selbständige Entität.
 */
fun Dachflaeche.dachneigung(): Double {
    val cos = aeussereNormale.z.coerceIn(0.0, 1.0)
    return acos(cos)        // Radiant, ∈ [0, π/2]
}

fun Dachflaeche.dachneigungGrad(): Double =
    dachneigung() * 180.0 / PI

fun Dachflaeche.dachneigungProzent(): Double {
    val a = dachneigung()
    require(a < PI / 2.0 - Toleranzen.WINKEL_EPS) {
        "Dachneigung 90° (vertikale Wand) hat keine Prozentanzeige"
    }
    return 100.0 * tan(a)
}

/** Klassifikation nach Branchen-Faustbereichen (nicht normativ). */
enum class DachneigungsKlasse { FLACH, SCHWACH_GENEIGT, GENEIGT, STEIL }

fun Dachflaeche.dachneigungsKlasse(): DachneigungsKlasse {
    val grad = dachneigungGrad()
    return when {
        grad < 10.0  -> DachneigungsKlasse.FLACH
        grad < 20.0  -> DachneigungsKlasse.SCHWACH_GENEIGT
        grad < 60.0  -> DachneigungsKlasse.GENEIGT
        else         -> DachneigungsKlasse.STEIL
    }
}
```

- **Einheit**: intern **Radiant** (Double). Anzeige in Grad oder
  Prozent ausschließlich am API-Rand. Niemals Mischung in einer
  Funktion.
- **Wertebereich**: α ∈ [0, π/2). α = π/2 ist nach `dachflaeche`-
  Definition ausgeschlossen (Wand, nicht Dach); die `require`-
  Bedingung in `dachneigungProzent` schützt vor Division-by-Zero
  bzw. tan(π/2) → ∞.
- **Invariante (vererbt von `dachflaeche`)**:
  ‖aeussereNormale‖ ∈ 1 ± Toleranzen.NORM_EPS, n_a · e_z ≥ 0.
  Damit ist `n_a.z ∈ [0 − ε, 1 + ε]`; `coerceIn(0.0, 1.0)` macht
  arccos numerisch sicher.
- **Edge Cases**:
  - **Flachdach (α = 0)**: zulässig. n_a = e_z, arccos(1) = 0.
    Prozentanzeige liefert 0 %. Die Falllinie ist nicht eindeutig,
    spielt für die Neigung selbst aber keine Rolle.
  - **Senkrechte Wand (α → π/2)**: durch `dachflaeche`-Bedingung 3
    ausgeschlossen; die Wand wird nicht als Dachfläche modelliert.
    Falls eine pathologisch konstruierte Dachfläche ⟨n_a, e_z⟩ ≈ 0
    aufweist, liefert `dachneigung` einen Wert nahe π/2 und die
    Prozentanzeige wirft eine Exception über `require`.
  - **Numerische Überschreitung von 1**: ⟨n_a, e_z⟩ kann durch
    Rundung minimal über 1 liegen; `coerceIn` fängt das ab und
    verhindert NaN aus arccos.
  - **Anisotrope Skalierung des Modells**: nicht zulässig; das
    Welt-Koordinatensystem ist isotrop in mm. Bei einer
    fehlerhaften Skalierung der Modelldaten gibt die Funktion ein
    konsistentes, aber möglicherweise fachlich falsches Ergebnis
    zurück.
- **Abgeleitete Operationen**:
  - `dachneigung(): Double` (Radiant) als kanonische Form.
  - `dachneigungGrad(): Double` für Anzeige.
  - `dachneigungProzent(): Double` für Holzbau-Praxis.
  - `falllinie(): Strecke?` (siehe `hg_falllinie.md`) entlang der
    Richtung ê_fall = −(e_z − (e_z · n̂) · n̂), normiert und mit
    der Vorzeichenkonvention ⟨ê_fall, e_z⟩ ≤ 0 (nach unten)
    gewählt.
- **Verwendungsregel**: Funktionen der Bemessungs- und
  Lastrechnung (Schneelast, Windlast) erhalten den Winkel **immer
  in Radiant**; nur UI-/Reportgeneratoren rufen die Grad-/Prozent-
  Varianten auf.

## Quellen

**Primär (normativ):**

- SIA 232/1:2020, „Geneigte Dächer", Schweizerischer Ingenieur- und
  Architektenverein, Zürich.
- DIN EN 1991-1-3:2010-12, „Eurocode 1: Einwirkungen auf Tragwerke –
  Teil 1-3: Schneelasten".
- DIN EN 1991-1-4:2010-12, „Eurocode 1: Einwirkungen auf Tragwerke –
  Teil 1-4: Windlasten".
- DIN 1055-5:1975-06 (zurückgezogen), übergeleitet in DIN EN 1991-1-3.

**Sekundär:**

- Lignum (Hrsg.): *Lignatec — Geneigte Dächer in Holzbauweise.*
  Lignum, Zürich, aktuelle Auflage.
- Lignum (Hrsg.): *Holzbautabellen HBT.* Lignum, Zürich,
  aktuelle Auflage.
- Mönck, W.; Rug, W.: *Holzbau – Bemessung und Konstruktion.*
  16. Auflage, Beuth Verlag 2015.
- Gerner, M.: *Fachwerk – Instandsetzung, Sanierung, Neubau.*
  DVA, 7. Auflage 2007.
- Holzbau Deutschland, Merkblatt „Begriffe und Klassifizierungen
  für den Holzbau".

**Korpus (nicht autoritativ):**

- Wikipedia, Lemma „Dachneigung" (abgerufen 2026-05-08).
