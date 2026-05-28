---
id: senkel
benennung: Senkel
synonyme: [Senkelschnitt, Senkelfläche, "lotrechte Schnittfläche"]
abgelehnte_benennungen: ["vertikaler Schnitt", "vertical cut", "plumb cut"]
oberbegriff: ebene
begriffstyp: merkmal
voraussetzungen: [ebene, weltkoordinatensystem, einheitsvektor, toleranzen]
abgrenzung_zu: [ebene, bleischnitt, bezugsebene, dachflaeche, weltkoordinatensystem]
status: entwurf
theorie_pflichtig: required
quellen_primär:
  - "Holzbau Schweiz (Hrsg.): Magazin-Sammelserie 'Austragen', Teil 4 'Senkel- und Bleischnitt am geneigten Dach', Berufsverband Holzbau Schweiz, Zürich (zimmermannssprachliche Primärquelle der Schweizer Berufspraxis): Senkel als zur Lotrichtung parallel verlaufende Schnittfläche; Bleischnitt als zur Lotrichtung rechtwinklig verlaufende Schnittfläche. Stellenangabe nicht abschließend verifiziert (siehe quellenkonflikt-Block)."
quellen_sekundär:
  - "Lignum (Hrsg.): Holzbautabellen HBT, Lignum, Zürich, aktuelle Auflage, Kap. 'Sparrenanschlüsse' und 'Austragen': Schnittflächen am Sparrenfuß und Sparrenfirstpunkt mit Bezeichnung 'Senkel' / 'Senkelschnitt'."
  - "Mönck, W.; Rug, W.: Holzbau – Bemessung und Konstruktion. 16. Aufl., Beuth, Berlin 2015, Kap. 11 'Dachtragwerke', § Sparrenfuß und Stirnausbildung am Sparrenkopf."
  - "Gerner, M.: Fachwerk – Instandsetzung, Sanierung, Neubau. DVA, 7. Aufl. 2007, Glossar 'Senkelschnitt'."
  - "baubeaver.de: 'Senkelschnitt am Sparren — der Zimmerer erklärt' (abgerufen 2026-05-09)."
quellenkonflikt: |
  Es existiert **keine geschlossene normative Begriffsdefinition**
  für „Senkel" in den deutschsprachigen Holzbau-Normen (SIA 265,
  SIA 232/1, DIN EN 1995-1-1, DIN 1052, DIN 68800). Die Normen
  setzen den Begriff voraus, wo er überhaupt vorkommt, und
  beschreiben nur die Bemessungsfolgen einer Stirnausbildung am
  Sparrenfuß. Auch die BTLx-2.1-Spezifikation
  (design2machine) führt keinen eigenen Begriff „Senkel"; die
  geometrische Festlegung erfolgt dort über `Inclination`-Winkel.

  Die einschlägige sprachliche Primärquelle ist die
  Schweizer Zimmermannspraxis, dokumentiert in der
  Magazin-Sammelserie „Austragen" des Berufsverbands Holzbau
  Schweiz. Die genaue Heft-/Seitenangabe für Teil 4 ist in der
  Recherche **nicht abschließend verifiziert**; der Eintrag wird
  als `entwurf` geführt, bis Eric die Stellenangabe bestätigt
  oder korrigiert. Methodisches Vorgehen analog zu
  `hg_bauteilachse.md` und `hg_bezugsebene.md` (Begriff in Normen
  vorausgesetzt, Festlegung über Berufspraxis-Primärquelle).

  Eigene Festlegung in diesem Glossar (konsistent mit allen
  konsultierten Quellen):

  - Ein **Senkel** ist eine **Ebene** im Sinne von `ebene` mit
    der zusätzlichen Rolle, parallel zur Welt-Lotachse zu
    verlaufen — gleichbedeutend damit, dass die Ebenen-Normale
    rechtwinklig zur Welt-Lotachse steht.
  - Senkel ist ein **Prädikat über Ebenen** (Lage-Merkmal),
    kein eigener geometrischer Konstruktor und kein eigener
    Code-Datentyp. Die Klassifikation einer gegebenen Ebene
    als Senkel erfolgt über das Skalarprodukt der Normalen mit
    der Welt-Lotachsen-Richtung.
  - Senkel ist die geometrisch komplementäre Lage zum
    `bleischnitt` (Ebene rechtwinklig zur Welt-Lotachse). Die
    beiden Begriffe spannen die ausgezeichnete Lot-Lage-
    Klassifikation der Schweizer Zimmermannspraxis auf.

  Diese Festlegung ist konsistent mit Lignum HBT, Mönck/Rug,
  Gerner und der einschlägigen Schweizer Berufspraxis.
---

## Prosa-Definition

Ein **Senkel** ist eine im Welt-Koordinatensystem festgelegte
Ebene, deren Normalenrichtung rechtwinklig zur Welt-Lotachse
verläuft, sodass die Ebene selbst parallel zur Lotrichtung steht.

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

Dann gilt **`E ist Senkel`** genau dann, wenn

```
| ⟨ n̂, ê_z ⟩ | ≤ ε_K.                                            (1)
```

Äquivalente Formulierungen:

- **Geometrisch**: die Ebenen-Normale n̂ steht rechtwinklig zur
  Welt-Lotachse ê_z; folglich enthält die Ebene E die Richtung
  ê_z (sie verläuft parallel zur Lotrichtung).
- **Über Lot-Vektor**: für jeden Punkt p ∈ E und jedes λ ∈ ℝ
  gilt p + λ · ê_z ∈ E; jede zur Lotrichtung verschobene Kopie
  eines Punktes der Ebene liegt wieder in der Ebene.

Die zugehörige **Senkelmenge** ist die Klasse aller Ebenen, die
(1) erfüllen:

```
𝒮 := { E ⊂ ℝ³ | E Ebene, |⟨n̂_E, ê_z⟩| ≤ ε_K }.                  (2)
```

Senkel ist damit ein **Prädikat** (`istSenkel: Ebene → Bool`),
nicht ein eigener geometrischer Konstruktor.

## Wohldefiniertheit

- **Vorzeichen-Invarianz**: Die Hesse-Normalform repräsentiert E
  nur bis auf die Vorzeichenmehrdeutigkeit (n̂, d) ↔ (−n̂, −d)
  (siehe `ebene` Wohldefiniertheit). Bedingung (1) ist davon
  unabhängig, weil sie den Betrag |⟨n̂, ê_z⟩| verwendet:
  |⟨−n̂, ê_z⟩| = |−⟨n̂, ê_z⟩| = |⟨n̂, ê_z⟩|. Das Prädikat ist
  damit auf der Ebene wohldefiniert, nicht nur auf einer
  bestimmten Hesse-Repräsentation.
- **Existenz**: Für jede Ebene E ist ⟨n̂_E, ê_z⟩ wohldefiniert
  (Skalarprodukt zweier Einheitsvektoren in ℝ³); der Betrag und
  der Vergleich mit ε_K liefern einen Wahrheitswert.
- **Eindeutigkeit der Klassifikation**: Bei gegebener
  Toleranz ε_K liefert (1) eine eindeutige Ja-Nein-Antwort.
  Innerhalb des Toleranzbandes |⟨n̂, ê_z⟩| ∈ (ε_K, 1 − ε_K)
  ist E weder Senkel noch Bleischnitt; die beiden Klassen sind
  disjunkt, decken aber nicht alle Ebenen ab (geneigte Ebenen
  fallen in keine).
- **Konsistenz mit Bleischnitt**: Aus (1) und der
  Bleischnitt-Bedingung |⟨n̂, ê_z⟩| ≥ 1 − ε_K folgt, dass eine
  Ebene mit ε_K < 1 − ε_K (also für jede praktische Wahl von
  ε_K) **nicht gleichzeitig** Senkel und Bleischnitt sein
  kann. Die beiden Prädikate sind zueinander disjunkt
  (Beweis: Annahme (1) ∧ Bleischnitt-Bedingung erzwingt
  ε_K ≥ 1 − ε_K, also ε_K ≥ 1/2, was die Toleranzwahl
  ausschliesst).
- **Toleranzwahl `KOLLINEAR_EPS` (dimensionslos)**: Die
  Bedingung (1) testet ein Skalarprodukt zweier Einheitsvektoren,
  also einen Cosinus. Die einschlägige App-Toleranzkonstante
  für Cosinus-/Sinus-basierte Lage-Tests ist `KOLLINEAR_EPS`
  (siehe `toleranzen`, Abschnitt „Kollinearitäts-Toleranz");
  `WINKEL_EPS` (in Radiant) wäre dimensionsfremd. Die beiden
  Konstanten sind im App-Default beide auf 10⁻⁹ gesetzt, sodass
  die numerische Schwelle praktisch gleich ist.
- **Nicht-Zirkularität**: Die Definition stützt sich nur auf
  bereits definierte Begriffe (`ebene`, `weltkoordinatensystem`,
  `einheitsvektor`, `toleranzen`). Sie kommt nicht in ihrer
  eigenen Definition vor und verweist nicht auf
  `bleischnitt` als Voraussetzung, sondern nur in der
  Abgrenzung.

## Erläuterung (nicht normativ)

### Etymologie

Der Begriff **Senkel** stammt vom Lot, dem klassischen
Zimmermanns-Werkzeug aus einem Bleigewicht an einer Schnur. Die
Schnur, an der das Gewicht hängt, wird im Schweizer Holzbau-
Sprachgebrauch der **Senkel** genannt; sie verläuft per Schwerkraft
strikt parallel zur Lotrichtung. Eine Schnittfläche, die in die
gleiche Richtung wie der Senkel verläuft (also parallel zur
Lotachse), heisst entsprechend **Senkelschnitt** oder kurz
**Senkel**. Der Begriff ist komplementär zum **Blei** (siehe
`bleischnitt`): das Blei bezeichnet das Bleigewicht selbst und
gibt dem Bleischnitt seinen Namen — die zur Schwerkraft
rechtwinklig stehende, also waagerechte Fläche, auf der das Lot
zur Ruhe kommt. (Quelle: Holzbau-Schweiz-Magazin, Sammelserie
„Austragen", Teil 4.)

### Verwendung im Holzbau

Senkelschnitte treten an mehreren Stellen am geneigten Dach auf:

- **Sparrenfuß-Stirnseite** im Standardfall „senkrechter
  Sparrenfußabschnitt": die Stirnfläche des Sparrens am
  unteren Ende ist ein Senkel, sodass die Sparrenstirnseite
  vertikal nach unten zeigt (und z. B. ein Stirnbrett vertikal
  daran befestigt werden kann).
- **Sparrenfirstpunkt-Stirnseite** beim Sparren-an-Sparren-
  Anschluss am First: die beiden Sparrenfirstpunkt-Stirnflächen
  sind Senkel und treffen sich in der Firstlinie.
- **Kervflanken** der Standardklauenkerve (siehe `kerve`,
  α₁ = α₂ = π/2): die beiden Flanken sind Senkel; die Sohle
  ist ein Bleischnitt.
- **Senkelriss** im Werkplan: die zeichnerische Darstellung der
  Senkellage im Auf- und Seitenriss.

### Senkel und Sparrenrichtung

Ein Senkel ist **nicht** automatisch rechtwinklig zur
Sparrenachse. Bei einem geneigten Sparren steht die
Sparrenachse selbst geneigt; ein Senkel-Stirnschnitt am
Sparrenfuß ist deshalb **schräg** zur Sparrenachse (nicht
rechtwinklig). Die zur Sparrenachse rechtwinklige Stirnfläche
heisst dagegen **rechtwinkliger Anschnitt** und ist im
allgemeinen weder Senkel noch Bleischnitt.

### Toleranz in der Praxis

Die Toleranzbedingung (1) berücksichtigt, dass eine in der App
modellierte Senkel-Fläche durch numerische Konstruktion (z. B.
über Boole'sche Operationen oder Kantenberechnungen) leicht von
der exakten Lage abweichen kann. Mit `KOLLINEAR_EPS = 10⁻⁹`
entspricht die Toleranz einer Winkelabweichung von etwa
5,73·10⁻⁸ Grad und ist damit weit unterhalb jeder praktischen
Zimmermannstoleranz; sie filtert nur numerische Restfehler.

## Beziehungen

- **Oberbegriff**: `ebene`. Ein Senkel ist eine Ebene mit
  zusätzlicher Rolle (Parallelität zur Lotachse).
- **Spezialisierungen**: keine eigenständigen Glossar-
  Spezialisierungen vorgesehen; konkrete Senkel-Verwendungen
  (Sparrenfuß-Stirnseite, Kervflanke, Senkelriss) sind keine
  eigenen Begriffe, sondern Anwendungen.
- **Bestandteile (partitiv)**:
  - **Trägerebene** (geerbt von `ebene`): die Punktmenge im
    Welt-Koordinatensystem.
  - **Senkel-Eigenschaft**: das Lage-Merkmal nach (1). Es ist
    keine zusätzliche Information, sondern eine ableitbare
    Eigenschaft der Ebene.
- **Verwendung**:
  - Klassifikation von **Sparren-Stirnseiten** am Werkplan
    (Senkel vs. Bleischnitt vs. rechtwinkliger Anschnitt).
  - Klassifikation von **Kervflanken** in `hg_kerve.md` für den
    Standardfall α₁ = α₂ = π/2.
  - **Werkplan-Beschriftung** als Hinweis auf die Schnittart
    (Senkelschnitt-Notation in der traditionellen Schweizer
    Werkplan-Konvention).
- **Abgrenzung**:
  - **Ebene** (`ebene`): allgemeines geometrisches Primitiv
    ohne Lage-Merkmal. Senkel ist eine Ebene mit
    Lage-Klassifikation.
  - **Bleischnitt** (`bleischnitt`): Schwester-Begriff. Während
    der Senkel parallel zur Welt-Lotachse verläuft (Normale
    rechtwinklig zur Lotachse), verläuft der Bleischnitt
    rechtwinklig zur Welt-Lotachse (Normale parallel zur
    Lotachse). Senkel und Bleischnitt sind die beiden
    ausgezeichneten Lot-Lage-Klassen einer Ebene; sie sind
    geometrisch komplementär und zueinander disjunkt.
  - **Bezugsebene** (`bezugsebene`): tool-eigene Höhenreferenz.
    Eine Bezugsebene ist im Standardfall ein Bleischnitt
    (horizontal); ein Senkel als Bezugsebene wäre ein
    Sonderfall (z. B. eine vertikale Achsen-Bezugsebene).
  - **Dachfläche** (`dachflaeche`): geneigte Berandungsfläche
    eines Daches. Eine Dachfläche ist im Regelfall **weder**
    Senkel noch Bleischnitt (sie ist um die Dachneigung
    geneigt); im Grenzfall Dachneigung = 90° wäre sie ein
    Senkel, im Grenzfall Dachneigung = 0° ein Bleischnitt
    (Flachdach).
  - **Welt-Koordinatensystem** (`weltkoordinatensystem`): legt
    die Lotachsen-Richtung ê_z fest, gegen die Senkel und
    Bleischnitt gemessen werden. Ohne Welt-Koordinatensystem
    sind Senkel und Bleischnitt nicht definiert.

## Implementierungshinweis

**Kein eigener Code-Typ.** Senkel wird in der Domänen-Schicht
als **Prädikat** über `Ebene` realisiert, nicht als
data class oder Subtyp. Die Implementierung lebt als
Erweiterungsfunktion auf `Ebene`:

```kotlin
package domain.geometrie

import domain.Toleranzen
import kotlin.math.abs

/**
 * Prädikat: ist diese Ebene ein Senkel?
 *
 * Eine Ebene ist genau dann Senkel, wenn ihre Normale
 * rechtwinklig zur Welt-Lotachse ê_z = (0, 0, 1) steht, d. h.
 *
 *   |⟨n̂, ê_z⟩| ≤ Toleranzen.KOLLINEAR_EPS.
 *
 * Glossar: hg_senkel.md (Prädikat über `hg_ebene.md`).
 *
 * Wohldefiniertheit: das Prädikat ist invariant unter
 * Vorzeichenwechsel der Hesse-Normalform (Betrags-Bedingung),
 * siehe Glossar Wohldefiniertheit.
 */
fun Ebene.istSenkel(eps: Double = Toleranzen.KOLLINEAR_EPS): Boolean {
    val nz = this.normaleEinheit().z       // ⟨n̂, ê_z⟩
    return abs(nz) <= eps
}
```

- **Einheit**: dimensionsloser Skalarprodukt-Vergleich.
- **Identität**: keine; Senkel ist eine Eigenschaft, kein Objekt.
- **Toleranz**: `KOLLINEAR_EPS` (nicht `WINKEL_EPS`), siehe
  Wohldefiniertheits-Block.
- **Edge Cases**:
  - **Geneigte Ebene mit kleinem Lotabstand-Cosinus** (z. B.
    Dachneigung 89,99°): klassifiziert per (1) **nicht** als
    Senkel, sondern als geneigte Ebene; das ist beabsichtigt
    (Senkel ist ein scharfer Lage-Begriff, nicht „nahe
    senkrecht").
  - **Bezugsebene als Senkel**: theoretisch möglich, in der
    App nicht im Standard-Modellierungspfad vorgesehen
    (siehe `bezugsebene`); kein Sonderverhalten.
  - **Welt-Koordinatensystem mit anderer ê_z-Wahl**: das
    Prädikat ist gegen die im `weltkoordinatensystem`
    festgelegte Lotachsen-Richtung formuliert; eine
    Abweichung wäre eine Verletzung der Welt-Konvention und
    keine Senkel-Klassifikation.

**Folgearbeit (trigger-basiert):**

- **`senkelstoss`** (Senkelstoss zwischen zwei Sparren): zwei
  Sparren stossen mit ihren Senkel-Stirnflächen aneinander
  (typisch am First). Trigger: erstes Tool mit Sparren-an-
  Sparren-Stoss am First.
- **`senkelriss`** (Senkelriss als Werkplan-Begriff):
  zeichnerische Darstellung der Senkellage in Auf- und
  Seitenriss. Trigger: erstes Werkplan-Beschriftungs-Tool.
- **Klassifikations-Hilfsfunktion `Ebene.lotLage()`**: liefert
  einen Enum `LotLage = SENKEL | BLEISCHNITT | GENEIGT` für
  die einheitliche Klassifikation. Trigger: erstes Tool, das
  diese Klassifikation in einer Schleife über mehrere Ebenen
  benötigt.
- **Cross-Verweis in `hg_sparren.md`**: Sparren-Stirnseiten-Anschnitte
  (z. B. Sparrenfuß-Senkelstoß) sind ein natürlicher Anwendungsfall
  von Senkel/Bleischnitt. Trigger: bei Anlage des `anschnitt.md`-
  Eintrags (Folgearbeit aus `hg_bearbeitung.md`), gemeinsam mit den
  anderen Sparren-Schnitt-Begriffen einbauen.
- **Cross-Verweis in `hg_dachflaeche.md`**: eine Dachfläche ist weder
  Senkel noch Bleischnitt (geneigte Ebene); Abgrenzungs-Hinweis ist
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

- baubeaver.de: „Senkelschnitt am Sparren — der Zimmerer
  erklärt" (abgerufen 2026-05-09).
