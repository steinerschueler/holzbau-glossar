---
id: mittelpfette
benennung: Mittelpfette
synonyme: [Zwischenpfette]
abgelehnte_benennungen: [Mittelträger, "middle purlin", Mittelbalken]
oberbegriff: pfette
begriffstyp: bauteilrolle
voraussetzungen: [pfette, bauteilachse, dachflaeche, dachkante, firstpfette, fusspfette, toleranzen]
abgrenzung_zu: [firstpfette, fusspfette, sparren, kehlbalken, knagge]
status: entwurf
theorie_pflichtig: required
quellen_primär:
  - "SIA 265:2021 'Holzbau', Abschnitt 5 (Konstruktive Durchbildung), Pfetten in Zwischenlage."
  - "SIA 232/1:2020 'Geneigte Dächer', Abschnitt 1 (Begriffe und geometrische Grundlagen)."
  - "DIN EN 1995-1-1:2010-12 (Eurocode 5), Abschnitt 5 (Tragwerksberechnung), Pfetten als Zwischenauflager der Sparren."
  - "DIN 1052:2008-12, Abschnitt 8 und 12, Mittelpfette als Zwischenauflager."
quellen_sekundär:
  - "Lignum (Hrsg.): Holzbautabellen HBT, Lignum, Zürich, aktuelle Auflage, Kap. 'Pfettendach'."
  - "Lignum (Hrsg.): Lignatec 'Geneigte Dächer in Holzbauweise'."
  - "Mönck, W.; Rug, W.: Holzbau – Bemessung und Konstruktion. 16. Aufl., Beuth, Berlin 2015, Kap. 11 'Dachtragwerke', § Pfettendach."
  - "Natterer, J.; Herzog, T.; Volz, M.: Holzbau-Atlas. 4. Aufl., Birkhäuser, Basel 2003."
  - "Gerner, M.: Fachwerk – Instandsetzung, Sanierung, Neubau. DVA, 7. Aufl. 2007, Glossar 'Mittelpfette'."
quellenkonflikt: |
  Keine konsultierte Norm enthält eine geschlossene Begriffsdefinition
  für „Mittelpfette"; alle Normen verwenden den Begriff vorausgesetzt.
  Sekundärquellen (Mönck/Rug, Natterer/Herzog, Lignum, Gerner)
  charakterisieren die Mittelpfette einhellig als Pfette zwischen
  Fuß- und Firstpfette, deren Hauptzweck die Reduktion der
  Sparrenspannweite und damit des erforderlichen Sparrenquerschnitts
  ist.

  Die Bezeichnung „Zwischenpfette" wird in Lignum-Schriften und in
  Schweizer Praxis synonym verwendet und hier als gleichrangiges
  Synonym geführt.

  Eigene Festlegung: Eine Mittelpfette ist eine Pfette, deren
  Bauteilachse parallel zum First (oder einer dazu parallelen
  Höhenlinie der Dachfläche) verläuft und deren Höhenlage strikt
  zwischen Fußpfetten- und Firstpfettenniveau liegt. Bei mehreren
  Mittelpfetten je Dachseite (großer Spannweiten-Bereich) qualifizieren
  alle Pfetten in Zwischenlage als Mittelpfetten; die feinere Abstufung
  („untere Mittelpfette", „obere Mittelpfette") bleibt eine
  konstruktive Anmerkung.

  Diese Festlegung ist konsistent mit allen konsultierten Quellen.
---

## Prosa-Definition

Eine **Mittelpfette** ist eine Pfette eines Dachtragwerks, deren
Bauteilachse parallel zum First (oder einer dazu parallelen
Höhenlinie der zugeordneten Dachfläche) verläuft und deren Höhenlage
strikt zwischen Fußpfetten- und Firstpfettenniveau liegt, und die im
Pfettendach die Sparren in einem Zwischenpunkt zwischen Sparrenfuß
und Sparrenfirstpunkt trägt, um deren Spannweite zu reduzieren.

## Mathematische Definition

Sei

- P eine Pfette im Sinne von `pfette` mit Bauteilachse
  a(P) = (p_a, p_e) und mittlerer Höhe
  z_P := (p_a.z + p_e.z) / 2,
- D eine zugeordnete Dachfläche im Sinne von `dachflaeche` mit
  Trägerebene E und äußerer Normaler n_a,
- d̂_F ∈ S² die Richtung des Firsts F (oder, falls kein First
  existiert wie beim Pultdach, die Richtung der Traufe der
  zugeordneten Dachfläche),
- z_Fuß die mittlere Höhe der zur Dachseite gehörigen Fußpfette
  (siehe `fusspfette`),
- z_First die mittlere Höhe der zur Dachseite gehörigen
  Firstpfette (siehe `firstpfette`); falls keine Firstpfette
  existiert (z. B. Sparrendach), ist die Mittelpfette nicht
  anwendbar,
- ε_K := Toleranzen.KOLLINEAR_EPS, ε_L := Toleranzen.LAENGE_EPS.

Dann heißt P eine **Mittelpfette** genau dann, wenn die folgenden
Bedingungen zusätzlich zu denen von `pfette` erfüllt sind:

1. **Parallelität zur Firstrichtung**: d̂_P ist kollinear mit d̂_F,
   ```
   ‖d̂_P × d̂_F‖ ≤ ε_K.
   ```
   Sinus-Test gegen Kollinearität; nach `_KONVENTIONEN.md`
   Sektion 4 ist `KOLLINEAR_EPS` die einschlägige Toleranz für
   Parallelitäts-Prädikate.

2. **Lage in der Trägerebene oder dachflächennah**: Die
   Bauteilachse liegt in der Trägerebene E der zugeordneten
   Dachfläche oder unmittelbar darunter (Höhenversatz ≤
   Pfettenhöhe). Formal:
   ```
   max( |⟨n_a, p_a − p₀⟩|, |⟨n_a, p_e − p₀⟩| ) ≤ h_Pfette + ε_L,
   ```
   wobei p₀ ∈ E ein Stützpunkt und h_Pfette die Pfettenhöhe ist.

3. **Zwischenlage**: Die mittlere Pfettenhöhe liegt strikt
   zwischen Fußpfetten- und Firstpfettenniveau,
   ```
   z_Fuß + ε_L < z_P < z_First − ε_L.
   ```

Wesentliche abgeleitete Größen:

- **Vertikalabstand zur Fußpfette**: Δz_Fuß := z_P − z_Fuß.
- **Vertikalabstand zur Firstpfette**: Δz_First := z_First − z_P.
- **Sparren-Teil-Spannweiten**: Im Pfettendach mit Mittelpfette
  teilt sich die Sparrenspannweite in zwei Abschnitte mit
  Längen, die proportional zu Δz_Fuß und Δz_First (gemessen
  entlang der Sparrenachse) sind. Die Mittelpfette wird oft so
  positioniert, dass diese beiden Abschnitte näherungsweise
  gleich lang sind (Spannweiten-Halbierung).

## Wohldefiniertheit

- **Existenz**: In jedem Pfettendach mit ausreichend großer
  Spannweite, in dem eine Mittelpfette konstruktiv eingesetzt
  wird, existiert die Pfette in der durch Bedingungen 1–3
  charakterisierten Lage. Die Existenz ist konstruktiv erfüllbar.
- **Mehrere Mittelpfetten**: Bei sehr großer Sparrenlänge
  (steile, hohe Dächer) sind zwei oder mehr Mittelpfetten je
  Dachseite üblich. Alle erfüllen Bedingungen 1–3; sie
  unterscheiden sich nur durch ihre Zwischenhöhe. Eine
  Eindeutigkeit der Mittelpfette ist **nicht** gefordert
  (anders als bei Firstpfette und Fußpfette).
- **Abgrenzung gegen Fußpfette und Firstpfette**: Die strikte
  Ungleichung in Bed. 3 verhindert, dass eine Pfette
  gleichzeitig als Mittelpfette und als Fußpfette/Firstpfette
  qualifiziert. Bei numerischer Gleichheit z_P = z_Fuß bzw.
  z_P = z_First (innerhalb ε_L) ist die jeweilige Endpfette
  vorrangig.
- **Konsistenz mit `hg_pfette.md`**: Alle Bedingungen aus `pfette`
  (Stabgeometrie, Horizontalität, Parallelität zu einer
  Dachkante) sind erfüllt.
- **Konsistenz mit `hg_dachflaeche.md`**: Bedingung 2 stellt sicher,
  dass die Mittelpfette **in der Dachfläche** sitzt und nicht
  außerhalb. Im Pfettendach liegt die Mittelpfette typisch
  unterhalb der Sparrenunterkante in der Trägerebene; das ist
  durch h_Pfette + ε_L tolerantgewählt.
- **Sparrendach-Ausschluss**: Im Sparrendach existiert weder
  Firstpfette noch Mittelpfette. Bedingung 3 ist nicht
  anwendbar; die Modellierung als Mittelpfette ist
  ausgeschlossen.
- **Nicht-Zirkularität**: Die Definition stützt sich nur auf
  bereits definierte Begriffe (`pfette`, `bauteilachse`,
  `dachflaeche`, `dachkante`, `firstpfette`, `fusspfette`,
  `toleranzen`).

## Erläuterung (nicht normativ)

Die Mittelpfette ist im Pfettendach das **konstruktive Mittel zur
Spannweiten-Reduktion**: ohne sie müsste der Sparren die volle
Distanz von der Fußpfette zur Firstpfette frei überspannen, was
hohe Querschnitte und damit Materialaufwand bedeutet. Eine
Mittelpfette halbiert (oder drittelt bei zwei Mittelpfetten) die
Sparrenspannweite und ermöglicht deutlich schlankere Sparren.

### Lage in der Dachfläche

Die Mittelpfette liegt typisch **innerhalb der Dachfläche**, mit
Oberkante in der Trägerebene oder leicht darunter (sodass die
Sparren auf der Pfette aufliegen, ohne die Eindeckungs-Ebene zu
beeinträchtigen). Die genaue Höhenlage hängt von der
Sparrenkonstruktion ab:

- bei aufliegenden Sparren: Pfettenoberkante = Sparrenunterkante;
- bei eingelassenen Sparren (Aufkämmung, Versatz): Sparren wird
  in die Pfette eingelassen, ein Teil der Pfettenhöhe befindet
  sich oberhalb der Sparrenunterkante.

### Mittelpfette im Stuhl

In zimmermannsmäßigen Pfettendächern werden die Mittelpfetten oft
durch **Stuhlsäulen** des „liegenden" oder „stehenden" Stuhls
unterstützt. Die Stuhlkonstruktion (mit Streben und
Stuhlschwellen) leitet die Mittelpfettenlast in die darunter
liegende Decke oder direkt in tragende Wände ab.

### Schweizer Sprachgebrauch

In der Schweiz wird **„Zwischenpfette"** als Synonym verwendet,
besonders in Lignum-Schriften. Im DE-Sprachgebrauch ist
„Mittelpfette" gebräuchlicher. Beide Begriffe bezeichnen exakt
dasselbe Bauteil; die Wahl ist regional.

### Verbindung zu Sparren

Typische Verbindung zwischen Sparren und Mittelpfette:

- **Aufkämmung** (Kammverbindung): der Sparren erhält an der
  Auflagerstelle eine rechteckige Aussparung, mit der er auf der
  Pfette „einrastet"; klassische zimmermannsmäßige Lösung.
- **Versatz**: vor allem an der Auflagerung mit Verbindungs-
  mitteln (Schrauben, Sparrenpfettenanker).
- **Reine Auflagerung mit Verbindungsmitteln**: bei modernen
  Konstruktionen mit vorgefertigten Anschlüssen.

## Beziehungen

- **Oberbegriff**: `pfette`. Die Mittelpfette ist eine Pfette mit
  zusätzlicher Lagebedingung (Zwischenlage zwischen Fuß- und
  Firstpfette).
- **Bestandteile (partitiv)**: geerbt von `pfette`
  (Bauteilachse, Querschnitt, Werkstoff, Faserrichtung).
- **Verwendung / Beziehung zu anderen Bauteilen**:
  - **Sparren** (`sparren`): liegt in einem Zwischenpunkt seiner
    Bauteilachse auf der Mittelpfette auf; wird so in zwei
    statisch entkoppelte Spannweiten-Abschnitte unterteilt.
  - **Firstpfette** (`firstpfette`) und **Fußpfette**
    (`fusspfette`): die zwei „Extrempfetten", zwischen denen die
    Mittelpfette liegt.
  - **Stuhlsäule** (`stuhlsaeule`, eigener Eintrag folgt):
    Stütze, die die Mittelpfette an Zwischenpunkten trägt
    (typisch im liegenden / stehenden Stuhl).
  - **Dachfläche** (`dachflaeche`): zugeordnete Fläche; die
    Mittelpfette liegt in oder unmittelbar unter der Trägerebene.
- **Abgrenzung**:
  - **Firstpfette** (`firstpfette`): am Firstniveau (oben).
  - **Fußpfette** (`fusspfette`): am Sparrenfuß (unten).
  - **Sparren** (`sparren`): geneigtes Bauteil, das **auf** der
    Mittelpfette aufliegt; nicht selbst Pfette.
  - **Kehlbalken** (`kehlbalken`): horizontaler Querbalken
    **zwischen** einem Sparrenpaar; verbindet zwei Sparren
    statt mehrere Sparren zu tragen. Optisch im Schnitt einer
    Dachseite ähnlich gelegen, aber konstruktiv und statisch
    völlig anders. Die Mittelpfette verläuft entlang der
    Firstrichtung (parallel zur Firstkante), der Kehlbalken
    rechtwinklig dazu (parallel zur Sparrenebene quer).

## Implementierungshinweis

Datentyp (Domänen-Schicht, Kotlin, Schicht `domain.bauteil`):

```kotlin
package domain.bauteil

import domain.Toleranzen
import domain.bauteil.Bauteil
import domain.bauteil.Pfette

/**
 * Mittelpfette: Pfette in Zwischenlage zwischen Fußpfette und
 * Firstpfette, parallel zum First.
 *
 * Glossar: hg_mittelpfette.md
 *
 * Synonym: Zwischenpfette.
 */
data class Mittelpfette(
    override val bauteil: Bauteil,
    val dachflaeche: Dachflaeche
) : Pfette.Mittelpfette() {

    init {
        // 1. Pfetten-Bedingungen aus Pfette geerbt.
        // 2. Parallelität zur Firstrichtung der Dachfläche
        //    (Bedingung 1 aus hg_mittelpfette.md).
        // 3. Lage in/unter der Trägerebene (Bedingung 2):
        //    max(|⟨n_a, p_a − p₀⟩|, |⟨n_a, p_e − p₀⟩|) ≤
        //    h_Pfette + LAENGE_EPS.
        // 4. Zwischenlage (Bedingung 3) wird im Tragwerks-Kontext
        //    gegen die konkrete Fuß- und Firstpfette geprüft.
    }
}

sealed class MittelpfetteEntartet {
    object NichtParallelZumFirst : MittelpfetteEntartet()
    object NichtInDachflaeche    : MittelpfetteEntartet()
    object NichtInZwischenlage   : MittelpfetteEntartet()
    object KeineFirstpfetteVorhanden : MittelpfetteEntartet()
    object KeineFusspfetteVorhanden  : MittelpfetteEntartet()
}
```

- **Einheit**: Längen in mm; Winkel intern in Radiant.
- **Identität**: `BauteilId` aus dem zugrunde liegenden Bauteil.
- **Invarianten** (zusätzlich zu denen von `Pfette`):
  1. Parallelität zur Firstrichtung — sonst
     `NichtParallelZumFirst`.
  2. Lage in/unter der Trägerebene — sonst `NichtInDachflaeche`.
  3. Zwischenlage zwischen Fuß- und Firstpfette (Cross-Cutting,
     im Tragwerks-Kontext geprüft) — sonst `NichtInZwischenlage`.
- **Edge Cases**:
  - **Mehrere Mittelpfetten je Dachseite**: zulässig; alle
    erfüllen Bedingung 1–3 individuell.
  - **Pultdach**: kein First vorhanden; d̂_F wird durch die
    Traufenrichtung ersetzt. Mittelpfette zwischen Fußpfette
    (an der Traufe) und Pultpfette (an der Pultkante).
  - **Sparrendach**: keine Mittelpfette zu modellieren.
  - **Mittelpfette gleichauf mit Fuß- oder Firstpfette**:
    technisch nicht sinnvoll; durch strikte Ungleichung
    ausgeschlossen.
- **Abgeleitete Eigenschaften**:
  - `getrageneSparrenIn(t: Tragwerk): List<Sparren>` — Sparren
    in `t`, deren Bauteilachse die Mittelpfettenachse innerhalb
    Toleranzen schneidet.
  - `sparrenSpannweitenAufteilung(s: Sparren): Pair<Double, Double>?`
    — die zwei Teil-Spannweiten des Sparrens beidseits der
    Mittelpfette, sofern die Mittelpfette diesen Sparren trägt.

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
