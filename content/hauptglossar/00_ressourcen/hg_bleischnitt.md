---
id: bleischnitt
benennung: Bleischnitt
synonyme: [Blei, "Bleischnitt-Fläche", "waagerechter Schnitt"]
abgelehnte_benennungen: ["horizontaler Schnitt", "horizontal cut", "level cut", "seat cut"]
oberbegriff: ebene
begriffstyp: merkmal
voraussetzungen: [ebene, weltkoordinatensystem, einheitsvektor, toleranzen]
abgrenzung_zu: [ebene, senkel, bezugsebene, dachflaeche, weltkoordinatensystem]
status: entwurf
theorie_pflichtig: required
quellen_primär:
  - "Holzbau Schweiz (Hrsg.): Magazin-Sammelserie 'Austragen', Teil 4 'Senkel- und Bleischnitt am geneigten Dach', Berufsverband Holzbau Schweiz, Zürich (zimmermannssprachliche Primärquelle der Schweizer Berufspraxis): Bleischnitt als zur Lotrichtung rechtwinklig verlaufende Schnittfläche; Senkel als zur Lotrichtung parallel verlaufende Schnittfläche. Stellenangabe nicht abschließend verifiziert (siehe quellenkonflikt-Block)."
quellen_sekundär:
  - "Lignum (Hrsg.): Holzbautabellen HBT, Lignum, Zürich, aktuelle Auflage, Kap. 'Sparrenanschlüsse' und 'Austragen': Schnittflächen am Sparrenfuß und Sparrenfirstpunkt mit Bezeichnung 'Bleischnitt' / 'Blei'."
  - "Mönck, W.; Rug, W.: Holzbau – Bemessung und Konstruktion. 16. Aufl., Beuth, Berlin 2015, Kap. 11 'Dachtragwerke', § Sparrenfuß und Auflagerausbildung."
  - "Gerner, M.: Fachwerk – Instandsetzung, Sanierung, Neubau. DVA, 7. Aufl. 2007, Glossar 'Bleischnitt'."
  - "baubeaver.de: 'Bleischnitt am Sparren — der Zimmerer erklärt' (abgerufen 2026-05-09)."
quellenkonflikt: |
  Es existiert **keine geschlossene normative Begriffsdefinition**
  für „Bleischnitt" in den deutschsprachigen Holzbau-Normen
  (SIA 265, SIA 232/1, DIN EN 1995-1-1, DIN 1052, DIN 68800).
  Die Normen setzen den Begriff voraus, wo er überhaupt vorkommt,
  und beschreiben nur die Bemessungsfolgen einer Auflagerfläche.
  Auch die BTLx-2.1-Spezifikation (design2machine) führt keinen
  eigenen Begriff „Bleischnitt"; die geometrische Festlegung
  erfolgt dort über `Inclination`-Winkel.

  Die einschlägige sprachliche Primärquelle ist die
  Schweizer Zimmermannspraxis, dokumentiert in der
  Magazin-Sammelserie „Austragen" des Berufsverbands Holzbau
  Schweiz. Die genaue Heft-/Seitenangabe für Teil 4 ist in der
  Recherche **nicht abschließend verifiziert**; der Eintrag
  wird als `entwurf` geführt, bis Eric die Stellenangabe
  bestätigt oder korrigiert. Methodisches Vorgehen analog zu
  `hg_bauteilachse.md`, `hg_bezugsebene.md` und der Schwester-Datei
  `hg_senkel.md`.

  In bestehenden Glossareinträgen (`hg_sparrenueberstand.md`,
  `hg_bezugsebene.md`, `hg_kerve.md`) wurde „Bleischnitt" bereits
  vor diesem Eintrag verwendet; der vorliegende Eintrag
  verankert den Begriff jetzt **normativ** und wird aus den
  drei Stellen rückverwiesen (siehe Cross-Verweise in den
  betreffenden Einträgen).

  Eigene Festlegung in diesem Glossar (konsistent mit allen
  konsultierten Quellen):

  - Ein **Bleischnitt** ist eine **Ebene** im Sinne von `ebene`
    mit der zusätzlichen Rolle, rechtwinklig zur Welt-Lotachse
    zu verlaufen — gleichbedeutend damit, dass die Ebenen-
    Normale parallel zur Welt-Lotachse steht. Eine Bleischnitt-
    Fläche ist somit horizontal („im Lot, also waagerecht").
  - Bleischnitt ist ein **Prädikat über Ebenen** (Lage-
    Merkmal), kein eigener geometrischer Konstruktor und kein
    eigener Code-Datentyp. Die Klassifikation einer gegebenen
    Ebene als Bleischnitt erfolgt über das Skalarprodukt der
    Normalen mit der Welt-Lotachsen-Richtung.
  - Bleischnitt ist die geometrisch komplementäre Lage zum
    `senkel` (Ebene parallel zur Welt-Lotachse). Die beiden
    Begriffe spannen die ausgezeichnete Lot-Lage-
    Klassifikation der Schweizer Zimmermannspraxis auf.

  Diese Festlegung ist konsistent mit Lignum HBT, Mönck/Rug,
  Gerner und der einschlägigen Schweizer Berufspraxis.
---

## Prosa-Definition

Ein **Bleischnitt** ist eine im Welt-Koordinatensystem
festgelegte Ebene, deren Normalenrichtung parallel zur
Welt-Lotachse verläuft, sodass die Ebene selbst rechtwinklig
zur Lotrichtung steht und damit waagerecht liegt.

## Mathematische Definition

Sei

- W das Welt-Koordinatensystem (siehe `weltkoordinatensystem`)
  mit Einheitsvektoren ê_x, ê_y, ê_z, wobei ê_z vertikal nach
  oben zeigt und damit die **Lotachsen-Richtung** trägt,
- E ⊂ ℝ³ eine Ebene im Sinne von `ebene`, repräsentiert in
  Hesse-Normalform durch das Paar (n̂, d) ∈ S² × ℝ,
- ε_K := `Toleranzen.KOLLINEAR_EPS` die einschlägige
  dimensionslose Toleranzkonstante für Skalarprodukt-basierte
  Lage-Tests (siehe `toleranzen`).

Dann gilt **`E ist Bleischnitt`** genau dann, wenn

```
| ⟨ n̂, ê_z ⟩ | ≥ 1 − ε_K.                                        (1)
```

Äquivalente Formulierungen:

- **Geometrisch**: die Ebenen-Normale n̂ ist parallel oder
  antiparallel zur Welt-Lotachse ê_z; folglich steht die Ebene
  E rechtwinklig zur Lotrichtung und ist waagerecht.
- **Über Höhenkonstanz**: für jeden Punkt p ∈ E hat ⟨ê_z, p⟩
  denselben Wert; E ist eine Höhenlinie der z-Koordinaten-
  funktion.

Die zugehörige **Bleischnitt-Menge** ist die Klasse aller
Ebenen, die (1) erfüllen:

```
ℬ := { E ⊂ ℝ³ | E Ebene, |⟨n̂_E, ê_z⟩| ≥ 1 − ε_K }.              (2)
```

Bleischnitt ist damit ein **Prädikat** (`istBleischnitt: Ebene
→ Bool`), nicht ein eigener geometrischer Konstruktor.

## Wohldefiniertheit

- **Vorzeichen-Invarianz**: Die Hesse-Normalform repräsentiert
  E nur bis auf die Vorzeichenmehrdeutigkeit (n̂, d) ↔ (−n̂,
  −d) (siehe `ebene` Wohldefiniertheit). Bedingung (1) ist
  davon unabhängig, weil sie den Betrag |⟨n̂, ê_z⟩| verwendet:
  |⟨−n̂, ê_z⟩| = |−⟨n̂, ê_z⟩| = |⟨n̂, ê_z⟩|. Das Prädikat ist
  damit auf der Ebene wohldefiniert, nicht nur auf einer
  bestimmten Hesse-Repräsentation.
- **Existenz**: Für jede Ebene E ist ⟨n̂_E, ê_z⟩ wohldefiniert
  (Skalarprodukt zweier Einheitsvektoren in ℝ³); der Betrag
  und der Vergleich mit 1 − ε_K liefern einen Wahrheitswert.
- **Eindeutigkeit der Klassifikation**: Bei gegebener Toleranz
  ε_K liefert (1) eine eindeutige Ja-Nein-Antwort. Innerhalb
  des Toleranzbandes |⟨n̂, ê_z⟩| ∈ (ε_K, 1 − ε_K) ist E weder
  Senkel noch Bleischnitt; die beiden Klassen sind disjunkt,
  decken aber nicht alle Ebenen ab (geneigte Ebenen fallen in
  keine).
- **Konsistenz mit Senkel**: Aus (1) und der
  Senkel-Bedingung |⟨n̂, ê_z⟩| ≤ ε_K folgt, dass eine Ebene
  mit ε_K < 1 − ε_K (also für jede praktische Wahl von ε_K)
  **nicht gleichzeitig** Bleischnitt und Senkel sein kann. Die
  beiden Prädikate sind zueinander disjunkt (Beweis: Annahme
  Bleischnitt-Bedingung ∧ Senkel-Bedingung erzwingt
  ε_K ≥ 1 − ε_K, also ε_K ≥ 1/2, was die Toleranzwahl
  ausschliesst).
- **Toleranzwahl `KOLLINEAR_EPS` (dimensionslos)**: Die
  Bedingung (1) testet ein Skalarprodukt zweier
  Einheitsvektoren, also einen Cosinus. Die einschlägige
  App-Toleranzkonstante für Cosinus-/Sinus-basierte Lage-Tests
  ist `KOLLINEAR_EPS` (siehe `toleranzen`, Abschnitt
  „Kollinearitäts-Toleranz"); `WINKEL_EPS` (in Radiant) wäre
  dimensionsfremd. Die beiden Konstanten sind im App-Default
  beide auf 10⁻⁹ gesetzt, sodass die numerische Schwelle
  praktisch gleich ist.
- **Nicht-Zirkularität**: Die Definition stützt sich nur auf
  bereits definierte Begriffe (`ebene`,
  `weltkoordinatensystem`, `einheitsvektor`, `toleranzen`).
  Sie kommt nicht in ihrer eigenen Definition vor und
  verweist nicht auf `senkel` als Voraussetzung, sondern nur
  in der Abgrenzung.

## Erläuterung (nicht normativ)

### Etymologie

Der Begriff **Blei** stammt vom Bleigewicht des Lots, dem
klassischen Zimmermanns-Werkzeug aus einem Stück Blei an einer
Schnur. Das Bleigewicht hängt per Schwerkraft strikt entlang
der Lotrichtung; eine Fläche, **auf der das Blei zur Ruhe
kommt**, steht entsprechend rechtwinklig zur Lotrichtung — sie
ist „im Lot, also waagerecht". Eine Schnittfläche mit dieser
Lage heisst deshalb **Bleischnitt** oder kurz **Blei**. Der
Begriff ist komplementär zum **Senkel** (siehe `senkel`): der
Senkel bezeichnet die Schnur, an der das Bleigewicht hängt, und
gibt dem Senkelschnitt seinen Namen — die zur Schwerkraft
parallel verlaufende, also lotrechte Fläche. (Quelle:
Holzbau-Schweiz-Magazin, Sammelserie „Austragen", Teil 4.)

### Verwendung im Holzbau

Bleischnitte treten an mehreren Stellen am geneigten Dach auf:

- **Kervsohle** der Standardklauenkerve (siehe `kerve`,
  α₁ = α₂ = π/2): die Sohle ist ein Bleischnitt; sie liegt
  formschlüssig auf der waagerecht orientierten Pfetten-
  Oberkante. Die beiden Flanken sind dagegen Senkel.
- **Bezugsebene des Sparren-Tools**: die Bezugsebene auf der
  Höhe des Bleischnitts der Fußpfetten-Kerve ist selbst ein
  Bleischnitt mit zusätzlicher Bezugsrolle (siehe
  `bezugsebene`).
- **Sparrenüberstand-Begrenzung**: der obere Endpunkt des
  Sparrenüberstands liegt am Bleischnitt-Punkt p_K der
  Fußpfettenkerve (siehe `hg_kerve.md` Gl. (7a)/(7b),
  `hg_sparrenueberstand.md`).
- **Sparrenfuß-Stirnseite** im Standardfall „waagerechter
  Sparrenfußabschnitt" bei Sparren mit horizontaler
  Stirnfläche: die Stirnfläche ist ein Bleischnitt (für
  Stirnbretter, die waagerecht ausgerichtet werden).
- **Pfettenoberkante** und **Pfettenunterkante** als
  geometrische Bezugsflächen: beide sind Bleischnitte (sofern
  die Pfette in Standardlage horizontal eingebaut ist).
- **Bleiriss** im Werkplan: die zeichnerische Darstellung der
  Bleilage in Höhenrissen.

### Bleischnitt und Bezugsebene

Im Standardfall (horizontaler Höhenbezug) **ist** eine
Bezugsebene typisch ein Bleischnitt mit zusätzlicher
Bezugsrolle (siehe `bezugsebene`). Die beiden Begriffe sind
dabei nicht gleich: ein Bleischnitt ist eine geometrische
Lage-Klassifikation jeder horizontalen Ebene; eine Bezugsebene
ist eine ausgezeichnete Bleischnitt-Ebene **mit zugewiesener
Höhenreferenz-Rolle** in einem konkreten Tool. Jede
Bezugsebene im Standardfall ist ein Bleischnitt, aber nicht
jeder Bleischnitt ist eine Bezugsebene.

### „Höhe des Bleischnitts" als skalare Lesart

In Werkplan- und Tool-Sprache wird gelegentlich von der „Höhe
des Bleischnitts" (z. B. der Fußpfettenkerve) gesprochen. Diese
Lesart bezeichnet die **abgeleitete Skalar-Größe** z = ⟨ê_z, p⟩
für einen ausgezeichneten Punkt p der Bleischnittebene (etwa den
Bleischnitt-Punkt p_K der Fußpfettenkerve nach `hg_kerve.md` Gl.
(7a)/(7b)); sie ist nicht eine alternative Definition des
Bleischnitts. Der Bleischnitt selbst bleibt eine Ebene mit
Lage-Klassifikation gemäß (1), kein Punkt und keine Skalar-
Größe.

### Toleranz in der Praxis

Die Toleranzbedingung (1) berücksichtigt, dass eine in der App
modellierte Bleischnitt-Fläche durch numerische Konstruktion
leicht von der exakten Lage abweichen kann. Mit
`KOLLINEAR_EPS = 10⁻⁹` entspricht die Toleranz einer
Winkelabweichung von etwa 5,73·10⁻⁸ Grad und ist damit weit
unterhalb jeder praktischen Zimmermannstoleranz; sie filtert
nur numerische Restfehler.

## Beziehungen

- **Oberbegriff**: `ebene`. Ein Bleischnitt ist eine Ebene mit
  zusätzlicher Rolle (Rechtwinkligkeit zur Lotachse).
- **Spezialisierungen**: keine eigenständigen Glossar-
  Spezialisierungen vorgesehen; konkrete Bleischnitt-
  Verwendungen (Kervsohle, Bezugsebene, Pfettenoberkante)
  sind keine eigenen Begriffe, sondern Anwendungen oder
  rollenbezogene Spezialisierungen mit eigenem Eintrag (z. B.
  `bezugsebene`).
- **Bestandteile (partitiv)**:
  - **Trägerebene** (geerbt von `ebene`): die Punktmenge im
    Welt-Koordinatensystem.
  - **Bleischnitt-Eigenschaft**: das Lage-Merkmal nach (1).
    Es ist keine zusätzliche Information, sondern eine
    ableitbare Eigenschaft der Ebene.
- **Verwendung**:
  - Klassifikation der **Kervsohle** in `hg_kerve.md` für den
    Standardfall α₁ = α₂ = π/2.
  - Klassifikation der **Bezugsebene** im Standardfall (siehe
    `bezugsebene`).
  - Geometrischer Anker des **Sparrenüberstands** (siehe
    `sparrenueberstand`).
  - Klassifikation von **Sparren-Stirnseiten** am Werkplan
    (Bleischnitt vs. Senkel vs. rechtwinkliger Anschnitt).
  - **Werkplan-Beschriftung** als Hinweis auf die Schnittart
    (Bleischnitt-Notation in der traditionellen Schweizer
    Werkplan-Konvention).
- **Abgrenzung**:
  - **Ebene** (`ebene`): allgemeines geometrisches Primitiv
    ohne Lage-Merkmal. Bleischnitt ist eine Ebene mit
    Lage-Klassifikation.
  - **Senkel** (`senkel`): Schwester-Begriff. Während der
    Bleischnitt rechtwinklig zur Welt-Lotachse verläuft
    (Normale parallel zur Lotachse), verläuft der Senkel
    parallel zur Welt-Lotachse (Normale rechtwinklig zur
    Lotachse). Senkel und Bleischnitt sind die beiden
    ausgezeichneten Lot-Lage-Klassen einer Ebene; sie sind
    geometrisch komplementär und zueinander disjunkt.
  - **Bezugsebene** (`bezugsebene`): tool-eigene
    Höhenreferenz mit zusätzlicher Bezugsrolle. Eine
    Bezugsebene **ist** im Standardfall ein Bleischnitt; aber
    nicht jeder Bleischnitt ist eine Bezugsebene (die
    Bezugsrolle ist die zusätzliche Information).
  - **Dachfläche** (`dachflaeche`): geneigte Berandungsfläche
    eines Daches. Eine Dachfläche ist im Regelfall **weder**
    Bleischnitt noch Senkel (sie ist um die Dachneigung
    geneigt); im Grenzfall Dachneigung = 0° (Flachdach) wäre
    sie ein Bleischnitt, im Grenzfall Dachneigung = 90° ein
    Senkel.
  - **Welt-Koordinatensystem** (`weltkoordinatensystem`):
    legt die Lotachsen-Richtung ê_z fest, gegen die
    Bleischnitt und Senkel gemessen werden. Ohne
    Welt-Koordinatensystem sind Bleischnitt und Senkel nicht
    definiert.

## Implementierungshinweis

**Kein eigener Code-Typ.** Bleischnitt wird in der
Domänen-Schicht als **Prädikat** über `Ebene` realisiert,
nicht als data class oder Subtyp. Die Implementierung lebt als
Erweiterungsfunktion auf `Ebene`:

```kotlin
package domain.geometrie

import domain.Toleranzen
import kotlin.math.abs

/**
 * Prädikat: ist diese Ebene ein Bleischnitt?
 *
 * Eine Ebene ist genau dann Bleischnitt, wenn ihre Normale
 * parallel oder antiparallel zur Welt-Lotachse ê_z = (0, 0, 1)
 * steht, d. h.
 *
 *   |⟨n̂, ê_z⟩| ≥ 1 − Toleranzen.KOLLINEAR_EPS.
 *
 * Glossar: hg_bleischnitt.md (Prädikat über `hg_ebene.md`).
 *
 * Wohldefiniertheit: das Prädikat ist invariant unter
 * Vorzeichenwechsel der Hesse-Normalform (Betrags-Bedingung),
 * siehe Glossar Wohldefiniertheit.
 */
fun Ebene.istBleischnitt(eps: Double = Toleranzen.KOLLINEAR_EPS): Boolean {
    val nz = this.normaleEinheit().z       // ⟨n̂, ê_z⟩
    return abs(nz) >= 1.0 - eps
}
```

- **Einheit**: dimensionsloser Skalarprodukt-Vergleich.
- **Identität**: keine; Bleischnitt ist eine Eigenschaft, kein
  Objekt.
- **Toleranz**: `KOLLINEAR_EPS` (nicht `WINKEL_EPS`), siehe
  Wohldefiniertheits-Block.
- **Edge Cases**:
  - **Geneigte Ebene mit kleinem Lot-Abstand-Sinus** (z. B.
    Dachneigung 0,01°): klassifiziert per (1) **nicht** als
    Bleischnitt, sondern als geneigte Ebene; das ist
    beabsichtigt (Bleischnitt ist ein scharfer Lage-Begriff,
    nicht „nahe waagerecht").
  - **Bezugsebene als Bleischnitt**: Standardfall; das
    Prädikat liefert `true` für jede horizontale Bezugsebene
    (siehe `bezugsebene`). Kein Sonderverhalten.
  - **Welt-Koordinatensystem mit anderer ê_z-Wahl**: das
    Prädikat ist gegen die im `weltkoordinatensystem`
    festgelegte Lotachsen-Richtung formuliert; eine
    Abweichung wäre eine Verletzung der Welt-Konvention und
    keine Bleischnitt-Klassifikation.

**Folgearbeit (trigger-basiert):**

- **`hoehenlinie`** (Höhenlinie als ausgezeichneter
  Bleischnitt-Schnitt durch eine Bauteilfläche): Trigger:
  erstes Tool, das Höhenlinien-Konstruktion an Bauteilen
  benötigt (z. B. Walmdach-Tool zur Konstruktion des
  Walmgrats über Höhenlinien-Schnitte).
- **`bleiriss`** (Bleiriss als Werkplan-Begriff): Trigger:
  erstes Werkplan-Beschriftungs-Tool.
- **Klassifikations-Hilfsfunktion `Ebene.lotLage()`**: liefert
  einen Enum `LotLage = SENKEL | BLEISCHNITT | GENEIGT` für
  die einheitliche Klassifikation. Trigger: erstes Tool, das
  diese Klassifikation in einer Schleife über mehrere Ebenen
  benötigt.
- **Cross-Verweis in `hg_sparren.md`**: Sparren-Stirnseiten-Anschnitte
  (z. B. Bleischnitt am Sparrenfuß bei waagerecht abgeschnittenem
  Sparrenende) sind ein natürlicher Anwendungsfall von
  Senkel/Bleischnitt. Trigger: bei Anlage des `anschnitt.md`-Eintrags
  (Folgearbeit aus `hg_bearbeitung.md`), gemeinsam mit den anderen
  Sparren-Schnitt-Begriffen einbauen.
- **Cross-Verweis in `hg_dachflaeche.md`**: eine Dachfläche ist weder
  Bleischnitt noch Senkel (geneigte Ebene); Abgrenzungs-Hinweis ist
  sinnvoll. Trigger: bei erstem Tool, das Dachflächen-Geometrie mit
  nicht-trivialen Schnittwinkeln behandelt, oder bei nächster
  substanzieller `hg_dachflaeche.md`-Überarbeitung.

## Quellen

**Primär (normativ):**

- Holzbau Schweiz (Hrsg.): *Magazin-Sammelserie „Austragen",
  Teil 4 — Senkel- und Bleischnitt am geneigten Dach.*
  Berufsverband Holzbau Schweiz, Zürich. (Stellenangabe nicht
  abschließend verifiziert; siehe quellenkonflikt-Block.)

**Sekundär:**

- Lignum (Hrsg.): *Holzbautabellen HBT.* Lignum, Zürich,
  aktuelle Auflage, Kap. „Sparrenanschlüsse" und „Austragen".
- Mönck, W.; Rug, W.: *Holzbau – Bemessung und Konstruktion.*
  16. Auflage, Beuth, Berlin 2015, Kap. 11.
- Gerner, M.: *Fachwerk – Instandsetzung, Sanierung, Neubau.*
  DVA, 7. Auflage 2007.

**Korpus (nicht autoritativ):**

- baubeaver.de: „Bleischnitt am Sparren — der Zimmerer
  erklärt" (abgerufen 2026-05-09).
