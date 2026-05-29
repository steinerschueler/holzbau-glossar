---
id: firstpfette
benennung: Firstpfette
synonyme: [Firstbalken, Firstträger]
abgelehnte_benennungen: [First, "ridge purlin", "ridge beam", Firstbohle, Firstlatte]
oberbegriff: pfette
begriffstyp: bauteilrolle
voraussetzungen: [pfette, bauteilachse, first, dachkante, toleranzen]
abgrenzung_zu: [first, mittelpfette, fusspfette, sparren, kehlbalken, knagge]
status: entwurf
theorie_pflichtig: required
quellen_primär:
  - "SIA 265:2021 'Holzbau', Abschnitt 5 (Konstruktive Durchbildung), Pfetten am First."
  - "SIA 232/1:2020 'Geneigte Dächer', Abschnitt 1 (Begriffe und geometrische Grundlagen)."
  - "DIN EN 1995-1-1:2010-12 (Eurocode 5), Abschnitt 5 und 6, Firstpfette als Pfette mit Lage am First."
  - "DIN 1052:2008-12, Abschnitt 8 und 12, Firstpfette als Tragglied am First."
quellen_sekundär:
  - "Lignum (Hrsg.): Holzbautabellen HBT, Lignum, Zürich, aktuelle Auflage, Kap. 'Pfettendach'."
  - "Lignum (Hrsg.): Lignatec 'Geneigte Dächer in Holzbauweise'."
  - "Mönck, W.; Rug, W.: Holzbau – Bemessung und Konstruktion. 16. Aufl., Beuth, Berlin 2015, Kap. 11 'Dachtragwerke'."
  - "Natterer, J.; Herzog, T.; Volz, M.: Holzbau-Atlas. 4. Aufl., Birkhäuser, Basel 2003."
  - "Gerner, M.: Fachwerk – Instandsetzung, Sanierung, Neubau. DVA, 7. Aufl. 2007, Glossar 'Firstpfette'."
quellenkonflikt: |
  Keine konsultierte Norm enthält eine geschlossene Begriffsdefinition
  für „Firstpfette"; alle Normen verwenden den Begriff vorausgesetzt,
  als „Pfette unter dem First" oder „Pfette am First". Sekundärquellen
  (Mönck/Rug, Natterer/Herzog, Lignum, Gerner) charakterisieren die
  Firstpfette einhellig als Pfette, deren Bauteilachse parallel zum
  First und auf oder nahe dem Firstniveau verläuft, und die die
  Sparrenfirstpunkte trägt.

  Eigene Festlegung: Eine Firstpfette ist eine Pfette, deren
  Bauteilachse parallel zum First eines Daches verläuft und deren
  Höhenlage näherungsweise am Firstniveau liegt (entweder unmittelbar
  unter dem First oder im Sonderfall „aufgesattelt" auf zwei
  gegenüberstehenden Sparrenpaaren mit dem First darüber). Die
  konkrete Lage „unter dem First" vs. „am First" ist eine
  konstruktive Wahl, kein Definitionsmerkmal.

  Im **Sparrendach** entfällt eine Firstpfette, da das System ohne
  mittige Pfettenauflagerung auskommt; die Firstpfette ist somit ein
  charakteristisches Element des **Pfetten-** und teils auch des
  **Kehlbalkendachs** sowie von Misch- und Bindersystemen.

  Diese Festlegung ist konsistent mit allen konsultierten Quellen.
---

## Prosa-Definition

Eine **Firstpfette** ist eine Pfette eines Dachtragwerks, deren
Bauteilachse parallel zum First des zugeordneten Daches verläuft und
deren Höhenlage näherungsweise am Firstniveau liegt, und die im
Pfettendach (sowie in Mischsystemen mit Pfettenanteil) die Sparren an
ihrem Sparrenfirstpunkt trägt.

## Mathematische Definition

Sei

- P eine Pfette im Sinne von `pfette` mit Bauteilachse
  a(P) = (p_a, p_e), Richtungs-Einheitsvektor d_hat_P und mittlerer
  Höhe z_P := (p_a.z + p_e.z) / 2,
- F ein First im Sinne von `first` mit Streckenzug-Repräsentation
  und Richtungs-Einheitsvektor d_hat_F sowie Firstniveau
  z_F := mittlere Höhe der Firststützpunkte,
- ε_K := Toleranzen.KOLLINEAR_EPS,
- δ_z eine konstruktive Höhentoleranz, die die zulässige Differenz
  zwischen Pfetten- und Firstniveau begrenzt; Default
  δ_z := h_Pfette + ε_L, wobei h_Pfette die (rechteckige) Pfetten-
  höhe ist und ε_L = Toleranzen.LAENGE_EPS.

Dann heißt P eine **Firstpfette** genau dann, wenn die folgenden
Bedingungen zusätzlich zu denen von `pfette` erfüllt sind:

1. **Parallelität zum First**: d_hat_P ist kollinear mit d_hat_F,
   ```
   ‖d_hat_P × d_hat_F‖ ≤ ε_K.
   ```
   Sinus-Test gegen Kollinearität; nach `_KONVENTIONEN.md`
   Sektion 4 ist `KOLLINEAR_EPS` die einschlägige Toleranz für
   Parallelitäts-Prädikate.

2. **Firstnah**: Die mittlere Höhe der Pfettenachse liegt
   innerhalb δ_z des Firstniveaus,
   ```
   |z_P − z_F| ≤ δ_z.
   ```

3. **Eindeutigkeit am Dach**: Es existiert keine andere Pfette
   P′ ≠ P mit derselben First-Parallelität, deren mittlere Höhe
   z_{P′} > z_P + ε_L erfüllt; in Worten: die Firstpfette ist
   die zur Firstrichtung parallele Pfette mit der höchsten Lage
   im Dach.

Wesentliche abgeleitete Größen:

- **Firstpfettenlänge**: ‖p_e − p_a‖ (in mm); im Regelfall
  geringfügig kleiner als die Firstlänge des Daches (Überstände
  und Anschnitte abhängig von der Konstruktion).
- **Vertikalabstand zum First**: Δz := z_F − z_P (vorzeichen-
  behaftet); Δz = 0, wenn die Firstpfettenachse auf Firstniveau
  liegt; Δz > 0, wenn die Firstpfette unmittelbar unter dem
  First sitzt.

## Wohldefiniertheit

- **Existenz**: In jedem Pfettendach mit First gibt es eine
  Firstpfette als oberste Längspfette; die Bedingungen 1–3 sind
  konstruktiv erfüllbar.
- **Eindeutigkeit**: Bedingung 3 stellt sicher, dass nur die
  oberste First-parallele Pfette als Firstpfette qualifiziert.
  Bei symmetrischen Doppelfirstkonstruktionen (z. B. zwei
  Doppelhausanteile) treten zwei Firstpfetten an zwei
  verschiedenen Firsten auf — diese werden durch die Zuordnung
  zur jeweiligen First-Instanz F unterschieden.
- **Konsistenz mit `hg_pfette.md`**: Alle Bedingungen aus
  `pfette` (Stabgeometrie, Horizontalität, Parallelität zu einer
  Dachkante) sind erfüllt; Bedingung 1 hier ist die Konkretisierung
  von Bedingung 3 aus `pfette`, mit der Dachkante k = First.
- **Wohldefiniertheit von δ_z**: Die Höhentoleranz δ_z ist
  konstruktiv und nicht numerisch; sie hängt vom konkreten
  Pfettenquerschnitt und der Anschlusskonstruktion (aufliegend,
  unterhängend, eingelassen) ab. Die Default-Wahl
  δ_z = h_Pfette + ε_L ist eine pragmatische Obergrenze, die alle
  üblichen Anschlüsse abdeckt; in der Domänen-Schicht ist δ_z
  als optionaler Parameter zu führen.
- **Sparrendach-Ausschluss**: Im Sparrendach existiert kein First
  als separates Bauteil-Auflager; die zwei gegenüberliegenden
  Sparren stützen sich gegenseitig am Firstanschnitt. Eine
  Firstpfette ist in diesem System nicht vorgesehen und sollte
  nicht modelliert werden.
- **Nicht-Zirkularität**: Die Definition stützt sich nur auf
  bereits definierte Begriffe (`pfette`, `bauteilachse`, `first`,
  `dachkante`, `toleranzen`).

## Erläuterung (nicht normativ)

Die Firstpfette nimmt die Sparrenfirstpunkt-Lasten beider Dachseiten auf
und leitet sie über ihre Auflager (Stuhlsäulen, Giebelwände,
Stirnwände) ab. Sie ist im Pfettendach ein charakteristisches
Tragelement und wird oft sichtbar belassen.

### Lage relativ zum First

Drei konstruktive Anordnungen sind verbreitet:

- **Unterfirstpfette** (häufigste Variante): Pfettenoberkante
  liegt unter dem Firstniveau; der Sparrenfirstpunkt wird über die
  Pfette geführt und am First (durch Anschnitt mit dem
  gegenüberliegenden Sparren oder durch Firstbrett) verschlossen.
- **Firstpfette in Firstniveau** (Aufsatzpfette): Pfettenoberkante
  liegt exakt auf Firstniveau; die Sparrenfirstpunkte sitzen seitlich
  auf der Firstpfette auf, der First wird durch Firstziegel oder
  Firstbohle gebildet.
- **Aufgesattelte Firstpfette** (selten, bei stark
  unterschiedlichen Dachneigungen oder Sparren-Aufdoppelung): die
  Firstpfette liegt **über** dem First, gestützt durch
  zusätzliche Konstruktion.

### Verbindung zu Sparren

Typische Verbindung zwischen Sparren und Firstpfette:

- **Versatz** (Stirnversatz oder Klauenversatz),
- **Aufkämmung** des Sparrens auf die Firstpfette,
- **Anschlag** des Sparrens an der Firstpfette mit
  Verbindungsmittel-Sicherung (Schrauben, Sparrenpfettenanker),
- in modernen Systemen: vorgefertigte Stahl-Sparrenpfettenanker.

### Firstpfettenhöhe als primärer Eingabeparameter im Sparren-Tool

Im **Sparren-Tool** der App (Etappe 3.3) ist die **Firstpfettenhöhe**
der primäre Eingabeparameter für die Höhenausdehnung des Sparrens.
Sie bezeichnet die **vertikale Höhendifferenz** zwischen dem
Bleischnitt-Punkt der Firstpfettenkerve und dem Bleischnitt-Punkt
der Fußpfettenkerve (= lokale Bezugskote, siehe `fusspfette` und
`bezugsebene`). Einheit: mm, gemessen entlang der Welt-z-Achse.

Diese Wahl entspricht der Werkplan-Praxis: im Vertikalschnitt eines
Daches sind Firstpfetten- und Fußpfettenhöhe als vertikale
Höhenkoten eingetragen, nicht als Distanz entlang der Sparrenachse.
Die SEMA-Profil-Eingabe (Firsthöhe + Traufhöhe als Profilparameter)
und die Cadwork-Konvention (Bezugspunkt OK Fußpfette für
Dachebenen-Höhen) bestätigen diese Logik.

#### Axialer Kervenabstand `s` (p_K-basiert, kanonisch)

Die Position der Firstpfettenkerve **entlang der Sparren-Bauteilachse**
(„axiale Kervposition", relevant für BTLx-Export und Maschinenübergabe)
ist als Abstand der beiden Bleischnitt-Punkte p_K der Fußpfetten-
und der Firstpfettenkerve auf der Sparren-Bauteilachse A(B) definiert.
Sei p_K^Fuß ∈ A(B) der Bleischnitt-Punkt der Fußpfettenkerve und
p_K^First ∈ A(B) der Bleischnitt-Punkt der Firstpfettenkerve, je
gemäß `hg_kerve.md` Gleichungen (7a)/(7b) (Schnittpunkt der vorderen
Kervflanke g₁ mit der Bauteilachse). Da p_K^Fuß und p_K^First
beide auf der Bauteilachse A(B) liegen, ist ihre Verbindung
kollinear mit dem Bauteilachsen-Richtungsvektor d_hat; mit der
Vorzeichenkonvention aus `hg_sparren.md` (d_hat zeigt bergauf, also
entgegen e_hat_fall) gilt

```
s  :=  ⟨ p_K^First − p_K^Fuß ,  d_hat ⟩                            (s.1)
    =  ‖ p_K^First − p_K^Fuß ‖,                                 (s.2)
```

wobei (s.1) die vorzeichen-behaftete skalare Projektion auf die
Bauteilachse ist und (s.2) ihre Norm-Form für den Regelfall
p_K^First „bergauf von" p_K^Fuß (positives Vorzeichen). `s` ist
damit der **axiale Kervenabstand** entlang der Bauteilachse und
identisch mit dem gleichnamigen Eintrag in der Sparrenlängen-
Symbol-Tabelle in `hg_sparren.md` (Sparren-Pipeline-Begriffe).

Lesart: `s` misst direkt entlang der Bauteilachse, also entlang
derjenigen Richtung, in der das Werkzeug am Sparren verfährt;
dies ist die in BTLx und in der Werkplan-Bemassung erwartete
Lesart der „Kervenposition" am Sparren.

#### Spezialfall: z-Differenz / sin(α)

Im idealisierten Fall — Pfetten waagerecht, Standardklauenkerven
mit α₁ = π/2 (vordere Kervflanke senkel, p_K auf gleicher Höhe
wie die Pfettenoberkante in z), Sparrenachse exakt in der
Trägerebene der Dachfläche und entgegen e_hat_fall gerichtet — sind
die z-Koordinaten von p_K^Fuß und p_K^First genau die jeweiligen
Pfettenhöhen, und die Bauteilachse ist um die Dachneigung α
gegen die Horizontale geneigt. Dann folgt aus (s.2) die
geschlossene Form

```
s  =  ( z(p_K^First) − z(p_K^Fuß) ) / sin(α)                    (s.3)
   =  ( firstpfetteHoehe − fusspfetteHoehe ) / sin(α).          (s.4)
```

Lesart: (s.4) ist eine **Konsequenz** von (s.1)/(s.2) im
idealisierten Fall, kein eigenständiger Definitionsterm. Bei
geneigten Pfetten, abweichenden Flankenwinkeln (α₁ ≠ π/2,
cot α₁ ≠ 0) oder einer Bauteilachse ausserhalb der Trägerebene
weicht die z-Differenz der p_K-Punkte von der Differenz der
Pfettenhöhen ab; in diesen Fällen liefern (s.1)/(s.2) das
geometrisch korrekte Ergebnis, (s.3)/(s.4) hingegen nur eine
Näherung. Die **kanonische Form ist (s.1)/(s.2)**;
(s.3)/(s.4) wird als idealisierter Spezialfall geführt.

Hintergrund und Recherche-Stand siehe
`docs/recherche/2026-05-10_sparrenmessung_neubau.md`.

### Verbindung zu Stützen / Stuhlsäulen

Die Firstpfette wird in regelmäßigen Achsabständen durch
Stuhlsäulen, Giebelwände oder Stirnwände unterstützt. Typische
Verbindungen:

- **Zapfen** zwischen Pfettenende und Säulenkopf,
- **Versatz** auf einem Säulenkopf-Sattel,
- **Knaggenanschluss** (`knagge` als Konsole zur Auflagerung).

## Beziehungen

- **Oberbegriff**: `pfette`. Die Firstpfette ist eine Pfette mit
  zusätzlicher Lagebedingung am First.
- **Bestandteile (partitiv)**: geerbt von `pfette`
  (Bauteilachse, Querschnitt, Werkstoff, Faserrichtung).
- **Verwendung / Beziehung zu anderen Bauteilen**:
  - **First** (`first`): die Dachkante, parallel zu der die
    Firstpfette liegt.
  - **Sparren** (`sparren`): liegt mit dem Sparrenfirstpunkt auf der
    Firstpfette auf (Pfettendach) bzw. wird durch sie unterstützt
    (Mischsystem).
  - **Stuhlsäule** (`stuhlsaeule`, eigener Eintrag folgt):
    Stütze, die die Firstpfette an Zwischenpunkten trägt.
  - **Giebelwand** / **Stirnwand**: traditionelle Auflager der
    Firstpfette an den Dach-Stirnseiten.
- **Abgrenzung**:
  - **First** (`first`): die geometrische Schnittkante zweier
    Dachflächen am höchsten Punkt; die Firstpfette ist ein
    materialbehaftetes Stabbauteil, das **unter oder am** First
    liegt. First und Firstpfette sind nicht identisch (Geometrie
    vs. Bauteil), liegen aber parallel zueinander.
  - **Mittelpfette** (`mittelpfette`): liegt zwischen Fuß- und
    Firstpfette, also weiter unten am Dach.
  - **Fußpfette** (`fusspfette`): liegt am Sparrenfuß, also weit
    unten am Dach.
  - **Sparren** (`sparren`): geneigtes Bauteil, das **auf** der
    Firstpfette aufliegt; nicht selbst Pfette.
  - **Kehlbalken** (`kehlbalken`): horizontaler Querbalken
    zwischen einem Sparrenpaar; trägt keine Sparren in
    Längsrichtung. Keine Firstpfette.

## Implementierungshinweis

Datentyp (Domänen-Schicht, Kotlin, Schicht `domain.bauteil`):

```kotlin
package domain.bauteil

import domain.Toleranzen
import domain.bauteil.Bauteil
import domain.bauteil.Pfette
import kotlin.math.abs

/**
 * Firstpfette: Pfette parallel zum First, am Firstniveau.
 * Glossar: hg_firstpfette.md
 *
 * Vorzeichenkonvention für die Bauteilachse: gemäß lokaler
 * Bezeichnungskonvention (geerbt von Pfette); typisch in
 * Welt-x-Richtung steigend.
 */
data class Firstpfette(
    override val bauteil: Bauteil,
    val first: First,
    val deltaZMax: Double = Toleranzen.LAENGE_EPS    // δ_z
) : Pfette.Firstpfette() {

    init {
        // 1. Pfetten-Bedingungen aus Pfette geerbt (Stabgeometrie,
        //    Horizontalität, Parallelität zu einer Dachkante).
        // 2. Parallelität zum First (Bedingung 1 aus hg_firstpfette.md):
        //    ‖d_hat_P × d_hat_F‖ ≤ Toleranzen.KOLLINEAR_EPS — sonst
        //    Resultat.Fehler(FirstpfetteEntartet.NichtParallel).
        //    Sinus-Test, bevorzugt für Parallelitäts-Prädikate;
        //    siehe hauptglossar/_KONVENTIONEN.md Sektion 4.
        // 3. Firstnah (Bedingung 2):
        //    |z_P − z_F| ≤ deltaZMax — sonst
        //    FirstpfetteEntartet.NichtFirstnah.
        // 4. Eindeutigkeit (Bedingung 3) wird im Tragwerks-Kontext
        //    geprüft, nicht in init (Cross-Cutting).
    }
}

sealed class FirstpfetteEntartet {
    object NichtParallel : FirstpfetteEntartet()
    object NichtFirstnah : FirstpfetteEntartet()
    object MehrdeutigImTragwerk : FirstpfetteEntartet()
}
```

- **Einheit**: Längen in mm; Winkel intern in Radiant.
- **Identität**: `BauteilId` aus dem zugrunde liegenden Bauteil.
- **Invarianten** (zusätzlich zu denen von `Pfette`):
  1. Parallelität zum First — sonst `NichtParallel`.
  2. Firstnähe — sonst `NichtFirstnah`.
  3. Eindeutigkeit als oberste First-parallele Pfette im
     Tragwerk — sonst `MehrdeutigImTragwerk` (Cross-Cutting).
- **Edge Cases**:
  - **Sparrendach**: keine Firstpfette zu modellieren.
  - **Mehrere Firste am selben Dach** (Walmdach hat keinen
    durchgehenden First; Krüppelwalm hat einen verkürzten First):
    je First mindestens eine Firstpfette zulässig; die
    Eindeutigkeit (Bed. 3) bezieht sich auf den jeweiligen First.
  - **Aufgesattelte Firstpfette**: z_P > z_F. δ_z muss in diesem
    Fall entsprechend angepasst werden, sonst greift `NichtFirstnah`.
- **Abgeleitete Eigenschaften**:
  - `getrageneSparrenfirstpunkteIn(t: Tragwerk): List<Sparren>` —
    Sparren in `t`, deren Sparrenfirstpunkt p_e auf der
    Firstpfettenachse innerhalb Toleranzen liegt. (Frühere
    Fassung hiess `getrageneSparrenkoepfeIn(...)`; die
    Umbenennung zieht die Konvention „Sparrenfirstpunkt"
    aus `hg_sparren.md` nach.)

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
- Wikipedia, Lemma „Pfette" (abgerufen 2026-05-08).
