---
id: fusspfette
benennung: Fußpfette
synonyme: [Mauerlatte, Schwellpfette, Traufpfette]
abgelehnte_benennungen: [Fußbalken, "wall plate", "eaves purlin", Mauerbank, Mauerschwelle]
oberbegriff: pfette
begriffstyp: bauteilrolle
voraussetzungen: [pfette, bauteilachse, traufe, dachkante, firstpfette, kerve, bezugsebene, toleranzen]
abgrenzung_zu: [firstpfette, mittelpfette, sparren, schwelle, raehm, traufe, bezugsebene, knagge]
status: entwurf
theorie_pflichtig: required
quellen_primär:
  - "SIA 265:2021 'Holzbau', Abschnitt 5 (Konstruktive Durchbildung), Pfetten am Sparrenfuß / an der Traufe."
  - "SIA 232/1:2020 'Geneigte Dächer', Abschnitt 1 (Begriffe und geometrische Grundlagen), Traufseitige Pfette."
  - "DIN EN 1995-1-1:2010-12 (Eurocode 5), Abschnitt 5 und 6, Fußpfette als unterste Pfette des Dachtragwerks."
  - "DIN 1052:2008-12, Abschnitt 8 und 12, Fußpfette / Mauerlatte."
quellen_sekundär:
  - "Lignum (Hrsg.): Holzbautabellen HBT, Lignum, Zürich, aktuelle Auflage, Kap. 'Pfettendach' und 'Mauerlatte'."
  - "Lignum (Hrsg.): Lignatec 'Geneigte Dächer in Holzbauweise'."
  - "Mönck, W.; Rug, W.: Holzbau – Bemessung und Konstruktion. 16. Aufl., Beuth, Berlin 2015, Kap. 11 'Dachtragwerke', § Pfettendach."
  - "Natterer, J.; Herzog, T.; Volz, M.: Holzbau-Atlas. 4. Aufl., Birkhäuser, Basel 2003."
  - "Gerner, M.: Fachwerk – Instandsetzung, Sanierung, Neubau. DVA, 7. Aufl. 2007, Glossar 'Fußpfette' und 'Mauerlatte'."
quellenkonflikt: |
  Keine konsultierte Norm enthält eine geschlossene Begriffsdefinition
  für „Fußpfette" oder ihre verbreiteten Synonyme „Mauerlatte" und
  „Schwellpfette". Die Sekundärquellen (Mönck/Rug, Lignum, Natterer/
  Herzog, Gerner) charakterisieren die Fußpfette einhellig als die
  unterste Pfette des Dachtragwerks, die die Sparrenfüße trägt und
  traufseitig liegt.

  Die Synonym-Frage ist nicht-trivial und in den Quellen nicht
  einheitlich gehandhabt:

  - **Mauerlatte**: in DE-Quellen (Mönck/Rug, Gerner) und in der
    Schweizer Bauaufnahme-Praxis bezeichnet „Mauerlatte" eine
    Fußpfette, die **unmittelbar auf der Mauerkrone** (Mauerwerk
    oder Stahlbeton-Ringbalken) aufliegt. Die Bezeichnung ist
    dann **eingeschränkt**: nicht jede Fußpfette ist eine
    Mauerlatte (etwa wenn sie auf einer Holzkonstruktion
    aufliegt). Im Sprachgebrauch wird der Begriff jedoch
    häufig auch für jede traufseitige Fußpfette verwendet.
  - **Schwellpfette**: regional (besonders in der süddeutschen
    und österreichischen Tradition, vereinzelt in der CH)
    verwendet, oft enger im Sinne einer „Schwelle, die die
    Funktion einer Pfette übernimmt"; teilweise auch als
    allgemeines Synonym für Fußpfette.
  - **Traufpfette**: gelegentlich verwendet, aber weniger
    etabliert als „Fußpfette" oder „Mauerlatte".

  Eigene Festlegung in diesem Glossar:

  - **Fußpfette** ist der **normfeste Hauptbegriff** in diesem
    Glossar, weil er die geometrische Lage am Sparrenfuß
    eindeutig benennt und unabhängig von der Auflagerart
    (Mauerwerk, Holzunterkonstruktion, Stahlbeton) ist.
  - **Mauerlatte** wird als **eingeschränktes Synonym** geführt
    und gilt streng nur, wenn die Fußpfette unmittelbar auf
    Mauerwerk oder Stahlbeton aufliegt. Im weiteren Sinne wird
    der Begriff jedoch in der Praxis synonym verwendet; die
    Domänen-Schicht erlaubt deshalb beide Begriffe als
    Bezeichner desselben Bauteils und annotiert die
    Auflagerart separat.
  - **Schwellpfette** wird als **regionales Synonym**
    (CH/AT/Süd-DE) geführt; semantisch identisch mit Fußpfette,
    aber im Sprachgebrauch heterogen. Die App-Anzeige bevorzugt
    „Fußpfette" gegenüber „Schwellpfette".
  - **Traufpfette** wird als nachrangiges Synonym geführt.

  Diese Festlegung ist konsistent mit allen konsultierten
  Quellen und löst die Mehrdeutigkeit pragmatisch: ein
  geometrischer Hauptbegriff, drei kontextabhängige
  Bezeichnungs-Synonyme.
---

## Prosa-Definition

Eine **Fußpfette** ist eine Pfette eines Dachtragwerks, deren
Bauteilachse parallel zur Traufe der zugeordneten Dachfläche
verläuft und deren Höhenlage näherungsweise am Niveau der
Sparrenfüße liegt, und die im Pfettendach (sowie in Mischsystemen)
die Sparren an ihrem Sparrenfuß trägt und deren Lasten in die
darunter liegende Wand-, Mauer- oder Stahlbeton-Konstruktion abgibt.

## Mathematische Definition

Sei

- P eine Pfette im Sinne von `pfette` mit Bauteilachse
  a(P) = (p_a, p_e) und mittlerer Höhe
  z_P := (p_a.z + p_e.z) / 2,
- T eine Traufe im Sinne von `traufe` mit Streckenzug-
  Repräsentation und Richtungs-Einheitsvektor d_hat_T sowie mittlerer
  Höhe z_T := mittlere Höhe der Traufenstützpunkte,
- ε_K := Toleranzen.KOLLINEAR_EPS, ε_L := Toleranzen.LAENGE_EPS,
- δ_z eine konstruktive Höhentoleranz für die Trauflagen-Nähe,
  Default δ_z := h_Pfette + ε_L (h_Pfette = Pfettenhöhe).

Dann heißt P eine **Fußpfette** genau dann, wenn die folgenden
Bedingungen zusätzlich zu denen von `pfette` erfüllt sind:

1. **Parallelität zur Traufe**: d_hat_P ist kollinear mit d_hat_T,
   ```
   ‖d_hat_P × d_hat_T‖ ≤ ε_K.
   ```
   Sinus-Test gegen Kollinearität; nach `_KONVENTIONEN.md`
   Sektion 4 ist `KOLLINEAR_EPS` die einschlägige Toleranz für
   Parallelitäts-Prädikate.

2. **Traufnähe**: Die mittlere Höhe der Pfettenachse liegt
   innerhalb δ_z der Traufhöhe,
   ```
   |z_P − z_T| ≤ δ_z.
   ```

3. **Eindeutigkeit als unterste Pfette**: Es existiert keine
   andere Pfette P′ ≠ P mit derselben Trauf-Parallelität, deren
   mittlere Höhe z_{P′} < z_P − ε_L erfüllt; in Worten: die
   Fußpfette ist die zur Traufenrichtung parallele Pfette mit
   der niedrigsten Lage im Dach.

Wesentliche abgeleitete Größen:

- **Vertikalabstand zur Traufe**: Δz := z_P − z_T (vorzeichen-
  behaftet); Δz ≈ 0, wenn die Fußpfettenoberkante mit der
  Trauf-Höhe zusammenfällt; Δz < 0 möglich, wenn die Fußpfette
  unter der Traufkante liegt (z. B. eingelassene Mauerlatte).
- **Auflagerart**: Annotation, ob die Fußpfette auf Mauerwerk /
  Stahlbeton (dann „Mauerlatte"), auf Holzkonstruktion (Rähm,
  Stuhlschwelle) oder freitragend (zwischen Stützen) aufgelagert
  ist; siehe Implementierungshinweis.

## Wohldefiniertheit

- **Existenz**: In jedem Pfettendach mit definierter Traufe
  existiert eine Fußpfette als unterste Längspfette; die
  Bedingungen 1–3 sind konstruktiv erfüllbar.
- **Eindeutigkeit**: Bedingung 3 stellt sicher, dass nur die
  unterste Trauf-parallele Pfette als Fußpfette qualifiziert.
  Bei symmetrischen Doppeldächern (zwei getrennte Trauflinien)
  treten zwei Fußpfetten auf, die durch ihre Zuordnung zur
  jeweiligen Traufe T unterschieden werden.
- **Konsistenz mit `hg_pfette.md`**: Alle Bedingungen aus `pfette`
  (Stabgeometrie, Horizontalität, Parallelität zu einer
  Dachkante) sind erfüllt; Bedingung 1 hier ist die
  Konkretisierung von Bedingung 3 aus `pfette` mit der Dachkante
  k = Traufe.
- **Sparrendach-Sonderfall**: Im Sparrendach existiert in der
  zimmermannssprachlichen Tradition keine eigentliche
  „Fußpfette" — die Sparrenfüße sind unmittelbar auf einem
  **Deckenbalken** (Zugglied) befestigt, der quer zur Traufrichtung
  verläuft. Eine traufseitig parallel verlaufende Mauerlatte als
  Auflagefläche ist jedoch häufig vorhanden und qualifiziert dann
  als Fußpfette nach den hier formulierten Bedingungen, auch wenn
  ihre statische Funktion eingeschränkt ist (sie trägt im
  Sparrendach nicht die Hauptlast, sondern dient als
  Lagerschicht zwischen Sparrenfuß-Konstruktion und
  Mauerwerk).
- **Mauerlatte als Spezialfall**: Eine Fußpfette qualifiziert
  als „Mauerlatte" im strengen Sinne genau dann, wenn ihre
  gesamte Bauteilachse auf einer durchgehenden mineralischen
  Auflagerschicht (Mauerwerk, Stahlbeton-Ringbalken) liegt. Im
  weiteren, sprachgebräuchlichen Sinne gilt der Begriff für
  jede traufseitige Fußpfette.
- **Nicht-Zirkularität**: Die Definition stützt sich nur auf
  bereits definierte Begriffe (`pfette`, `bauteilachse`, `traufe`,
  `dachkante`, `firstpfette`, `toleranzen`).

## Erläuterung (nicht normativ)

Die Fußpfette ist die **unterste Pfette** des Dachtragwerks und
zugleich die **Schnittstelle zwischen Dach und Wand** im
Pfettendach. Sie erfüllt drei Funktionen gleichzeitig:

- **statisch**: trägt die Sparrenfüße und überträgt deren Lasten
  auf die darunter liegende Konstruktion;
- **konstruktiv**: dient als kontinuierliche, gerade Auflage-Linie
  für die Sparrenfüße, sodass die Sparren-Anschlüsse einheitlich
  ausgeführt werden können;
- **bauphysikalisch / handwerklich**: bildet die feste Linie, an
  der das Dach an die Wand anschließt (Anschluss von Dachhaut,
  Dampfsperre, Wärmedämmung).

### Auflagerarten (entscheidend für die Bezeichnung)

Drei Auflagerarten kommen vor; die Bezeichnung der Fußpfette
variiert mit ihnen:

- **Auflagerung auf Mauerwerk oder Stahlbeton-Ringbalken**: die
  Fußpfette wird **unmittelbar** auf die Mauerkrone gelegt,
  meist auf Folie oder Bitumenbahn als Trennschicht und mit
  Verankerung (Mauerlatten-Anker, Schwerlastdübel) gegen Wind-
  Sog. Diese Konfiguration heißt traditionell **Mauerlatte**.
  Sehr häufig im **Massivbau-Dachstuhl** (gemauerte Außenwand,
  Holz-Dachstuhl).
- **Auflagerung auf Holzkonstruktion**: Fußpfette auf einer
  hölzernen Wand (Ständerwand, Riegelwand mit Rähm-
  Obergurt) oder auf einer Stuhlkonstruktion. In manchen
  Bauweisen übernimmt das **Rähm** der Wand direkt die
  Funktion der Fußpfette.
- **Freitragende Auflagerung zwischen Stützen**: die Fußpfette
  überspannt zwischen Stützen (z. B. bei aufgeständerten
  Pfettendächern, Carports). Das Pfetten-Tragverhalten in
  Längsrichtung wird dann maßgebend.

### Verbindung zu Sparren

Typische Sparrenfuß-Verbindungen auf der Fußpfette:

- **Versatz** (Stirn-, Fersen-, doppelter Versatz): klassische
  zimmermannsmäßige Lösung, erzeugt eine Druckfläche, die den
  Sparrenfuß formschlüssig auf der Fußpfette stützt.
- **Sparrenanschlag** (auch „Sparrenfußklotz"): ein zusätzliches
  Klotzholz, gegen das der Sparren stößt, ohne in die Fußpfette
  eingearbeitet zu werden. Schont den Pfetten-Querschnitt.
- **Aufkämmung (Kammverbindung)**: weniger üblich am Sparrenfuß
  als an der Mittelpfette, gelegentlich bei sichtbaren
  Konstruktionen.
- **Verbindungsmittel-Sicherung**: Schrauben, Sparrenpfettenanker
  (z. B. Simpson-Stahlanker), Sparrennägel zur Sicherung gegen
  Wind-Sog und Schub.

### Fußpfettenhöhe als lokale Bezugskote im Sparren-Tool

Im **Sparren-Tool** der App (Etappe 3.3, Einzel-Sparren mit
parametrischer Variation) definiert der **Bleischnitt-Punkt p_K
der Fußpfettenkerve** (siehe `hg_kerve.md`, Abschnitt
„Bleischnitt-Punkt der vorderen Kervflanke an der Bauteilachse",
Gleichungen (7a)/(7b)) die **lokale Bezugskote** der
Sparrenkonstruktion (z = 0 lokal). p_K ist der Schnittpunkt der
vorderen (sparrenfußseitigen) Kervflanke mit der Bauteilachse des
Sparrens; im Standardfall α₁ = π/2 ist er ein eindeutiger, auf
jedem Werkplan exakt rekonstruierbarer geometrischer Punkt am
Sparrenfuß.

Alle vertikalen Höhenangaben weiterer Konstruktionspunkte des
Sparrens (Höhenlage der Firstpfettenkerve, Höhenlage des Sparrenfußes
am Überstand) werden im Tool relativ zu p_K angegeben. Die Wahl ist
konsistent mit der Werkplan-Konvention „OK Fußpfette / OK Mauerlatte"
(vertikale Höhenkette ab dem ersten vom Holzbauer gesetzten Punkt)
und mit der Cadwork-Praxis (Bezugspunkt-Konvention für Dachebenen).

Diese Bezugskote-Rolle ist die tool-spezifische Realisierung des
allgemeinen Begriffs **Bezugsebene** (siehe `hg_bezugsebene.md`,
Abschnitt „Anker im Sparren-Tool: Bleischnitt-Punkt p_K der
Fußpfettenkerve"); die Sparren-Tool-Bezugsebene ist die horizontale
Ebene durch p_K, ihre skalare z-Höhe ist z₀(T_Sparren) = z(p_K).
Hintergrund und Recherche-Stand siehe
`docs/recherche/2026-05-10_sparrenmessung_neubau.md`.

### Schweizer Sprachgebrauch

In der Schweizer Praxis wird der Begriff **„Mauerlatte"** für
jede auf Mauerwerk aufliegende Fußpfette verwendet; **„Fußpfette"**
ist als allgemeiner Begriff weniger gebräuchlich, aber präziser
für den nicht-mauerwerksgebundenen Fall. **„Schwellpfette"** ist
in der CH selten; **„Traufpfette"** kommt in technischer
Fachliteratur vor.

## Beziehungen

- **Oberbegriff**: `pfette`. Die Fußpfette ist eine Pfette mit
  zusätzlicher Lagebedingung an der Traufe.
- **Bestandteile (partitiv)**: geerbt von `pfette`
  (Bauteilachse, Querschnitt, Werkstoff, Faserrichtung).
- **Verwendung / Beziehung zu anderen Bauteilen**:
  - **Traufe** (`traufe`): die Dachkante, parallel zu der die
    Fußpfette liegt.
  - **Sparren** (`sparren`): liegt mit dem Sparrenfuß auf der
    Fußpfette auf (Pfettendach) bzw. ist mit ihr durch Versatz
    oder Anschlag verbunden.
  - **Mauerwerk / Stahlbeton-Ringbalken**: traditionelles
    Auflager der Fußpfette als „Mauerlatte". Mauer und
    Fußpfette sind durch Mauerlatten-Anker oder Schwerlast-
    dübel kraftschlüssig verbunden.
  - **Wand / Rähm**: bei Holzwänden übernimmt das Rähm
    teilweise die Auflagerfunktion; die Fußpfette liegt auf
    dem Rähm.
  - **Stuhlsäule** / **Stuhlschwelle**: bei aufgeständerten
    Pfettendächern Auflagerung der Fußpfette auf einer
    Stuhlkonstruktion.
- **Abgrenzung**:
  - **Firstpfette** (`firstpfette`): am Firstniveau (oben).
    Fußpfette liegt am gegenüberliegenden Ende des Dachs (unten).
  - **Mittelpfette** (`mittelpfette`): zwischen Fuß- und
    Firstpfette.
  - **Sparren** (`sparren`): geneigtes Bauteil, das **auf** der
    Fußpfette aufliegt; nicht selbst Pfette.
  - **Schwelle** (`schwelle`): horizontales unteres Auflagerholz
    im **Wandbau**
    (zwischen Fundament und Wand-Ständern); trotz formaler
    Ähnlichkeit (horizontaler Stab am Boden) keine Pfette,
    da nicht im Dachtragwerk und keine Sparren tragend.
    Die Bezeichnung „Schwellpfette" steht trotz des
    Bestandteils „Schwelle" für eine Pfette, nicht für eine
    Schwelle.
  - **Rähm** (`raehm`): oberster horizontaler Längsträger einer Wand. In manchen
    Konstruktionen übernimmt das Rähm die Funktion einer
    Fußpfette; saubere Trennung zimmermannssprachlich:
    Rähm gehört zur Wand, Fußpfette gehört zum Dachtragwerk.
    Ein Bauteil kann nicht gleichzeitig Rähm und Fußpfette
    sein, sondern wird je nach konstruktiver Funktion
    der einen oder anderen Rolle zugeordnet.
  - **Traufe** (`traufe`): die geometrische Dachkante am
    Sparrenfuß; die Fußpfette liegt parallel zur Traufe und in
    deren Höhe, ist aber nicht identisch mit der Traufe (die
    Traufe ist Geometrie, die Fußpfette ist Bauteil).

## Implementierungshinweis

Datentyp (Domänen-Schicht, Kotlin, Schicht `domain.bauteil`):

```kotlin
package domain.bauteil

import domain.Toleranzen
import domain.bauteil.Bauteil
import domain.bauteil.Pfette

/** Auflagerart der Fußpfette; relevant für die Bezeichnung. */
enum class FusspfetteAuflager {
    MAUERWERK,                // qualifiziert als „Mauerlatte" (streng)
    STAHLBETON_RINGBALKEN,    // ebenfalls „Mauerlatte"
    HOLZKONSTRUKTION,         // auf Rähm, Stuhlschwelle etc.
    FREITRAGEND_ZWISCHEN_STUETZEN,
    UNBEKANNT
}

/**
 * Fußpfette: unterste Pfette eines Dachtragwerks, parallel zur
 * Traufe.
 *
 * Glossar: hg_fusspfette.md
 *
 * Synonyme: Mauerlatte (eingeschränkt: nur bei Auflagerung auf
 * Mauerwerk/Stahlbeton im strengen Sinne), Schwellpfette (regional
 * CH/AT/Süd-DE), Traufpfette.
 *
 * Vorzeichenkonvention für die Bauteilachse: gemäß lokaler
 * Bezeichnungskonvention (geerbt von Pfette).
 */
data class Fusspfette(
    override val bauteil: Bauteil,
    val traufe: Traufe,
    val auflager: FusspfetteAuflager = FusspfetteAuflager.UNBEKANNT,
    val deltaZMax: Double = Toleranzen.LAENGE_EPS    // δ_z
) : Pfette.Fusspfette() {

    init {
        // 1. Pfetten-Bedingungen aus Pfette geerbt.
        // 2. Parallelität zur Traufe (Bedingung 1 aus hg_fusspfette.md):
        //    ‖d_hat_P × d_hat_T‖ ≤ Toleranzen.KOLLINEAR_EPS — sonst
        //    Resultat.Fehler(FusspfetteEntartet.NichtParallelZurTraufe).
        //    Sinus-Test, bevorzugt für Parallelitäts-Prädikate;
        //    siehe hauptglossar/_KONVENTIONEN.md Sektion 4.
        // 3. Traufnähe (Bedingung 2):
        //    |z_P − z_T| ≤ deltaZMax — sonst
        //    FusspfetteEntartet.NichtTraufnah.
        // 4. Eindeutigkeit als unterste (Bedingung 3) wird im
        //    Tragwerks-Kontext geprüft.
    }

    /**
     * Mauerlatten-Prädikat im strengen Sinne: nur bei direkter
     * Auflagerung auf Mauerwerk oder Stahlbeton-Ringbalken.
     */
    val istMauerlatteImEngerenSinne: Boolean
        get() = auflager == FusspfetteAuflager.MAUERWERK ||
                auflager == FusspfetteAuflager.STAHLBETON_RINGBALKEN

    /**
     * Anzeigename: bevorzugt „Fußpfette"; bei Auflagerung auf
     * Mauerwerk darf zusätzlich „(Mauerlatte)" annotiert werden.
     */
    fun anzeigeName(): String = when (auflager) {
        FusspfetteAuflager.MAUERWERK,
        FusspfetteAuflager.STAHLBETON_RINGBALKEN ->
            "Fußpfette (Mauerlatte)"
        else -> "Fußpfette"
    }
}

sealed class FusspfetteEntartet {
    object NichtParallelZurTraufe : FusspfetteEntartet()
    object NichtTraufnah          : FusspfetteEntartet()
    object MehrdeutigImTragwerk   : FusspfetteEntartet()
}
```

- **Einheit**: Längen in mm; Winkel intern in Radiant.
- **Identität**: `BauteilId` aus dem zugrunde liegenden Bauteil.
- **Invarianten** (zusätzlich zu denen von `Pfette`):
  1. Parallelität zur Traufe — sonst `NichtParallelZurTraufe`.
  2. Traufnähe — sonst `NichtTraufnah`.
  3. Eindeutigkeit als unterste Trauf-parallele Pfette im
     Tragwerk — sonst `MehrdeutigImTragwerk` (Cross-Cutting).
- **Edge Cases**:
  - **Sparrendach mit Mauerlatte**: zulässig, aber statisch
    nachrangig (siehe Wohldefiniertheit).
  - **Pultdach**: nur eine Traufe, die untere Dachkante; die
    Fußpfette liegt dort. Es gibt keine Firstpfette, sondern
    eine Pultpfette an der Pultkante.
  - **Walmdach**: vier Trauflinien; je Trauflinie maximal eine
    Fußpfette. Die vier Fußpfetten verschiedener Dachseiten
    treffen an den Eckpunkten zusammen (Eckverbindung).
  - **Mehrere Fußpfetten am selben Trauflinienabschnitt**:
    durch die Eindeutigkeitsbedingung ausgeschlossen.
  - **Eingelassene Mauerlatte**: z_P liegt unterhalb von z_T;
    in diesem Fall δ_z muss die Einlasstiefe abdecken.
- **Abgeleitete Eigenschaften**:
  - `getrageneSparrenfuesseIn(t: Tragwerk): List<Sparren>` —
    Sparren in `t`, deren Sparrenfuß p_a auf der Fußpfetten-
    achse innerhalb Toleranzen liegt.
  - `verankerungsAbstand(): Double?` — typischer Achsabstand
    der Mauerlatten-Anker (Bemessungs-Hilfsfunktion, falls
    `istMauerlatteImEngerenSinne`).

## Quellen

**Primär (normativ):**

- SIA 265:2021, „Holzbau".
- SIA 232/1:2020, „Geneigte Dächer".
- DIN EN 1995-1-1:2010-12, „Eurocode 5".
- DIN 1052:2008-12.

**Sekundär:**

- Lignum (Hrsg.): *Holzbautabellen HBT.* Aktuelle Auflage.
- Lignum (Hrsg.): *Lignatec — Geneigte Dächer in Holzbauweise.*
- Mönck, W.; Rug, W.: *Holzbau – Bemessung und Konstruktion.*
  16. Auflage, Beuth, Berlin 2015.
- Natterer, J.; Herzog, T.; Volz, M.: *Holzbau-Atlas.* 4. Auflage,
  Birkhäuser, Basel 2003.
- Gerner, M.: *Fachwerk – Instandsetzung, Sanierung, Neubau.*
  DVA, 7. Auflage 2007.

**Korpus (nicht autoritativ):**

- Holzbau Deutschland, Merkblatt „Begriffe und Klassifizierungen
  für den Holzbau" (abgerufen 2026-05-08).
- Wikipedia, Lemmata „Pfette", „Mauerlatte" (abgerufen 2026-05-08).
