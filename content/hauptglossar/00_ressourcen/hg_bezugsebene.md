---
id: bezugsebene
benennung: Bezugsebene
synonyme: ["Bezugshöhenebene", "Höhenbezugsebene", "Tool-Bezugsebene"]
abgelehnte_benennungen: ["Nullebene", "Grundebene", "datum plane", "reference plane", "z=0-Ebene"]
oberbegriff: ebene
begriffstyp: generisch
voraussetzungen: [ebene, weltkoordinatensystem, einheitsvektor, bleischnitt, kerve, toleranzen]
abgrenzung_zu: [ebene, bleischnitt, dachflaeche, weltkoordinatensystem, lokales_koordinatensystem, traufe, fusspfette, kerve]
status: entwurf
subglossar_pendant: notwendig
quellen_primär:
  - "DIN 18202:2019-07, 'Toleranzen im Hochbau – Bauwerke', Abschnitt 4 (Begriffe) und Abschnitt 6 (Verfahren zur Prüfung): vor der Bauausführung sind geeignete Bezugspunkte festzulegen, gegen die der Ist-Zustand des Bauwerks geprüft wird; eine Bezugsfläche dient als Vergleichsfläche für Ebenheits- und Höhenmessungen."
  - "SIA 414/1:2010, 'Massgenauigkeit im Bauwesen – Grenzwerte', Abschnitt 'Bezugssystem' und Abschnitt 'Höhenmasse': Höhenmasse werden gegen vereinbarte Bezugsebenen (Höhenbezug) gemessen."
  - "ISO 16739-1:2024 'Industry Foundation Classes (IFC) for data sharing in the construction and facility management industries — Part 1: Data schema', Entitäten 'IfcGeometricRepresentationContext' und 'IfcLocalPlacement': Bezugskontext einer geometrischen Repräsentation, der unter anderem die Höhenreferenz (z = 0) der enthaltenen Geometrie festlegt."
  - "DIN ISO 80000-2:2022-08, Abschnitt 2 (Geometrie): Ebene als affiner Unterraum (siehe `hg_ebene.md`); eine Bezugsebene ist eine Ebene mit zugewiesener Bezugsrolle."
quellen_sekundär:
  - "Lignum (Hrsg.): Lignatec 'Geneigte Dächer in Holzbauweise', Lignum, Zürich, aktuelle Auflage, Bezugskoten und Höhenmasse."
  - "SIA 232/1:2020, 'Geneigte Dächer', Schweizerischer Ingenieur- und Architektenverein, Abschnitt 1 (Begriffe und geometrische Grundlagen): Höhenbezug für Dachgeometrie."
  - "Mönck, W.; Rug, W.: Holzbau – Bemessung und Konstruktion. 16. Aufl., Beuth, Berlin 2015, Kap. 11 'Dachtragwerke', Werkplan-Höhenbezüge."
quellenkonflikt: |
  Es existiert keine geschlossene normative Begriffsdefinition für
  „Bezugsebene" als Modellierungs- oder Werkzeug-Konzept im Sinne
  dieser App. DIN 18202 und SIA 414/1 verwenden „Bezugspunkt" und
  „Bezugsfläche" als Grundlage für Toleranzprüfungen, ohne sie
  axiomatisch zu definieren; sie setzen den Begriff voraus und
  beschreiben seine Funktion. ISO 16739-1 (IFC) führt mit
  `IfcGeometricRepresentationContext` einen Bezugskontext ein, in
  dem unter anderem die Höhenreferenz und die Achsenkonventionen
  festgelegt werden, ohne den Begriff „Bezugsebene" als solchen zu
  definieren.

  Eigene Festlegung in diesem Glossar (konsistent mit allen
  konsultierten Quellen):

  - Eine **Bezugsebene** ist eine **Ebene** im Sinne von `ebene` mit
    der zusätzlichen Rolle, in einem konkreten Modellierungs- oder
    Visualisierungs-Kontext (in dieser App: einem konkreten Tool)
    als Höhenreferenz z = 0 für die im Tool modellierten Bauteile
    und deren Höhenmasse zu dienen.
  - Die Bezugsebene ist **tool-spezifisch**, nicht global. Jedes
    Tool der App (Sparren-Tool, Wandschichtaufbau, Walmdach-Tool,
    …) wählt seine eigene Bezugsebene; konkrete Werte (welche
    Bauteilfläche, welche Dachkante) sind tool-spezifisch und
    werden **nicht** im Glossar fixiert. Der Glossareintrag
    spezifiziert nur den Begriff, nicht die einzelnen Tool-
    Festlegungen.
  - Die Bezugsebene ist **horizontal** (z-konstant in W) im
    Standardfall. Geneigte Bezugsebenen sind nicht ausgeschlossen,
    aber Sonderfall; sie kommen in der App nicht im Standard-
    Modellierungspfad vor und werden, falls notwendig, im jeweiligen
    Tool-Eintrag separat dokumentiert.
  - Die Bezugsebene ist **kein Koordinatensystem** (siehe
    Abgrenzung zu `weltkoordinatensystem` und
    `lokales_koordinatensystem`); sie legt nur die Höhe z = 0 fest,
    nicht die x- und y-Achsen. Sie ist damit eine schwächere
    Struktur als ein vollständiges Koordinatensystem.

  Diese Festlegung ist konsistent mit DIN 18202, SIA 414/1, IFC und
  der Lignum-Werkplan-Praxis.
---

## Prosa-Definition

Eine **Bezugsebene** ist eine im Welt-Koordinatensystem festgelegte
Ebene, die in einem konkreten Modellierungs- oder Visualisierungs-
Kontext (Tool) als Höhenreferenz z = 0 für die enthaltenen Bauteile
und deren Höhenmasse dient.

## Mathematische Definition

Sei

- W das Welt-Koordinatensystem (siehe `weltkoordinatensystem`) mit
  Ursprung O_W und Einheitsvektoren e_hat_x, e_hat_y, e_hat_z, wobei e_hat_z
  vertikal nach oben zeigt,
- T ein konkretes Modellierungs- oder Visualisierungs-Tool der App
  (Sparren-Tool, Wandschichtaufbau, Walmdach-Tool, …),
- z₀(T) ∈ ℝ ein vom Tool T festgelegter **Bezugshöhenwert** (in mm),
  gemessen entlang e_hat_z.

Dann ist die **Bezugsebene** des Tools T die Ebene

```
E_bez(T) := { x ∈ ℝ³ | ⟨e_hat_z, x⟩ = z₀(T) },                       (1)
```

in Hesse-Normalform (siehe `ebene`) repräsentiert durch das Paar
(n_hat, d) = (e_hat_z, z₀(T)). Die Bezugsebene ist horizontal in W
(Normalenvektor e_hat_z) und liegt auf der Höhe z₀(T).

Wesentliche abgeleitete Grössen für ein Bauteil B mit
Welt-Geometrie G_W(B) ⊂ ℝ³:

- **Höhe gegen Bezugsebene** eines Punktes p ∈ G_W(B):
  ```
  h_E(p; T) := ⟨e_hat_z, p⟩ − z₀(T) = signierterAbstand(p, E_bez(T)).  (2)
  ```
  Positive Werte liegen oberhalb, negative unterhalb der
  Bezugsebene.
- **Bauteil-Höhenbereich**:
  ```
  [h_min(B; T), h_max(B; T)]  mit
  h_min := min { h_E(p; T) | p ∈ G_W(B) },
  h_max := max { h_E(p; T) | p ∈ G_W(B) }.
  ```

**Tool-spezifische Festlegung von z₀(T)**: Die App fixiert z₀(T)
nicht im Glossar, sondern in der Tool-Konfiguration. z₀(T) ist
typisch durch einen ausgezeichneten **Punkt** an einer Bauteil-
Bauteilachse festgelegt; die Bezugsebene ist dann die horizontale
Ebene durch diesen Punkt, und z₀(T) ist seine Welt-z-Höhe. Konkrete
Festlegungen pro Tool stehen in der Tool-Dokumentation; siehe
Erläuterung für Beispiele.

### Anker im Sparren-Tool: Bleischnitt-Punkt p_K der Fußpfettenkerve

Im **Sparren-Tool** der App ist der Ursprung der Bezugsebene
normativ festgelegt als der **Bleischnitt-Punkt p_K der
Fußpfettenkerve an der Bauteilachse des Sparrens** (siehe
`hg_kerve.md`, Abschnitt „Bleischnitt-Punkt der vorderen Kervflanke
an der Bauteilachse", Gleichungen (7a)/(7b)). Im Standardfall
α₁ = π/2 reduziert sich p_K im Bauteil-Lokal-System auf
(x₀, 0, h_B / 2); in W ist p_K = T_{L_B → W}(p_K^lokal). Damit ist

```
z₀(T_Sparren)  :=  ⟨e_hat_z, p_K⟩,                                    (3)
```

und die Bezugsebene des Sparren-Tools ist die horizontale Ebene
durch p_K. Die in der Werkplan-Praxis übliche skalare Lesart
„z-Höhe der Bezugsebene" ist damit die abgeleitete Skalar-
Komponente z(p_K); die Bezugsebene selbst bleibt eine Ebene.

## Wohldefiniertheit

- **Existenz**: Für jedes Tool T mit festgelegtem z₀(T) ∈ ℝ ist
  E_bez(T) nach (1) eine wohldefinierte Ebene im Sinne von `ebene`
  (Stützpunkt p₀ = (0, 0, z₀(T)), Normale n = e_hat_z; ‖n‖ = 1 > 0).
- **Eindeutigkeit der Hesse-Repräsentation**: Mit der festgelegten
  Normalen-Orientierung „nach oben" (n_hat = e_hat_z, nicht −e_hat_z) ist die
  Bezugsebene durch z₀(T) eindeutig (und nicht modulo Vorzeichen,
  vgl. `ebene` Wohldefiniertheit). Die Halbraum-Aussagen
  „oberhalb/unterhalb" sind damit ohne weitere Konvention
  interpretierbar.
- **Tool-Lokalität**: E_bez(T) gehört zum Tool T und nur zu ihm.
  Verschiedene Tools T₁ ≠ T₂ haben im allgemeinen verschiedene
  Bezugsebenen; eine globale „Bezugsebene des Modells" ist nicht
  vorgesehen. Diese Lokalität ist analog zur IFC-Strukturierung
  über `IfcGeometricRepresentationContext`, der pro
  Repräsentations-Kontext ein eigenes Bezugssystem hält.
- **Horizontalität (Default)**: Die Festlegung n_hat = e_hat_z ist
  Standard und garantiert, dass „Höhe gegen Bezugsebene" mit der
  Welt-z-Höhe (bis auf Konstante z₀(T)) übereinstimmt; das ist die
  einschlägige Lesart von „Höhenbezug" in DIN 18202 / SIA 414/1
  und in der Werkplan-Praxis.
- **Wohldefiniertheit von h_E(p; T)**: Für jeden Punkt p ∈ ℝ³ ist
  ⟨e_hat_z, p⟩ wohldefiniert (drittes Koordinaten-Skalarprodukt); die
  Subtraktion z₀(T) ist eine Translation. Folglich ist h_E(p; T)
  eine wohldefinierte stetige Funktion auf ℝ³.
- **Nicht-Zirkularität**: Die Definition stützt sich nur auf
  bereits definierte Begriffe (`ebene`, `weltkoordinatensystem`,
  `einheitsvektor`, `toleranzen`). Sie kommt nicht in ihrer
  eigenen Definition vor und verweist nicht auf konkrete Tool-
  Bezugsebenen.

## Erläuterung (nicht normativ)

### Zweck

Die Bezugsebene löst ein praktisches Problem der Modellierung: für
jedes Tool muss klar sein, von welchem Niveau aus Höhenmasse
gemessen werden. Im **Sparren-Tool** etwa ist die Sparrenlage
durch die Höhe des Bleischnitts (Schnittpunkt der Pfettenoberkante
mit der Sparrenunterkante an der Auflagerung) bestimmt; in einem
**Wandschichtaufbau** ist die Höhe gegen den Rohboden wesentlich;
in einem **Walmdach-Tool** ist die Wandkronenhöhe der natürliche
Bezug. Die Bezugsebene macht diese Wahl explizit und in der
Tool-Konfiguration nachvollziehbar.

### Beispiele tool-spezifischer Bezugsebenen

Die folgende Tabelle zeigt typische Festlegungen pro Tool. Die
konkreten Werte sind tool-spezifisch und werden in der jeweiligen
Tool-Dokumentation, **nicht** in diesem Glossareintrag fixiert:

| Tool                    | Bezugsebene (Beispiel-Festlegung)                              |
|-------------------------|----------------------------------------------------------------|
| Sparren-Tool            | Horizontale Ebene durch den Bleischnitt-Punkt p_K der Fußpfettenkerve an der Sparren-Bauteilachse (siehe `hg_kerve.md` Gl. (7a)/(7b); `hg_fusspfette.md`; `docs/recherche/2026-05-10_sparrenmessung_neubau.md`) |
| Wandschichtaufbau       | OK Rohboden                                                    |
| Walmdach-Tool           | OK Wandkrone (= OK Mauerwerk / Wandkrone, traufseitig)         |
| Stützen-Tool            | OK Fundament / OK Schwelle                                     |
| Geschossdecke           | OK Rohdecke (Oberkante tragender Querschnitt)                  |

Diese Beispiele sind illustrativ. Jedes Tool dokumentiert seine
Bezugsebene in seinem eigenen Tool-Eintrag (Folgearbeit); der
Glossareintrag „Bezugsebene" liefert nur den Rahmen.

### Bezugsebene und Bleischnitt

Im Standardfall (horizontaler Höhenbezug) ist die Bezugsebene
geometrisch ein **Bleischnitt** (siehe `bleischnitt`): ihre
Normale n_hat = e_hat_z liegt parallel zur Welt-Lotachse, die
Trägerebene steht rechtwinklig zur Lotrichtung und ist damit
waagerecht. Eine Bezugsebene ist also typisch ein Bleischnitt
mit zusätzlicher Bezugsrolle (Höhenreferenz für ein Tool); die
Bezugsrolle ist die unterscheidende Information gegenüber
einem beliebigen Bleischnitt. Geneigte Bezugsebenen sind
Sonderfall (siehe Wohldefiniertheit „Horizontalität (Default)")
und sind dann **kein** Bleischnitt mehr.

### Bezugsebene und negativer Höhenbereich

Bauteile dürfen den Bereich z < z₀(T) (also unterhalb der
Bezugsebene) belegen. Im Sparren-Tool ragt der **Sparrenüberstand**
unterhalb des Bleischnitts in den Bereich h_E < 0 (siehe
`sparrenueberstand`, `bleischnitt`); im Walmdach-Tool ragen
Sparrenfüsse je nach Modellierung unterhalb der Wandkrone hinaus.
Die Bezugsebene trennt nicht „Bauteil-Innenraum" von „Aussenraum",
sondern dient nur als Höhennullpunkt.

### Bezugsebene vs. Trägerebene einer Dachfläche

Eine **Dachfläche** (siehe `dachflaeche`) trägt eine eigene
Trägerebene; diese ist im allgemeinen geneigt und nicht horizontal.
Die Bezugsebene ist eine Modellierungs-Hilfsebene des Tools und
typisch horizontal. Die beiden Begriffe sind disjunkt: die
Trägerebene einer Dachfläche ist nie automatisch die Bezugsebene
eines Tools.

### Bezugsebene vs. Welt-Koordinatensystem

Die Bezugsebene legt nur die **z-Höhe** z₀(T) fest, **nicht** die
x- und y-Achsen. Das Welt-Koordinatensystem trägt diese vollständig.
In dieser App sind beide unabhängig wählbar: das Welt-
Koordinatensystem ist global und konstant
(siehe `weltkoordinatensystem`); die Bezugsebene ist tool-lokal
und kann zwischen Tools variieren. Die Bezugsebene ist damit
**schwächer** als ein Koordinatensystem (legt nur eine Skalar-
Konstante fest), aber **stärker** als ein einzelner Punkt (legt
eine ganze Ebene fest).

## Beziehungen

- **Oberbegriff**: `ebene`. Die Bezugsebene ist eine Ebene mit
  zusätzlicher Rolle (Höhenreferenz eines Tools).
- **Spezialisierungen**: keine eigenständigen Glossar-Spezialisierungen
  vorgesehen; konkrete Bezugsebenen sind tool-spezifische
  Festlegungen, nicht eigene Begriffe.
- **Bestandteile (partitiv)**:
  - **Trägerebene** (geerbt von `ebene`): die Punktmenge im
    Welt-Koordinatensystem.
  - **Bezugshöhenwert** z₀(T): die einzige zusätzliche Information
    gegenüber der nackten Ebene; typisch positiv (gegen die
    Welt-Achsen-Wahl) und tool-abhängig.
  - **Tool-Zugehörigkeit**: jede Bezugsebene gehört zu genau einem
    Tool.
- **Verwendung**:
  - In jedem **Tool** der App (Sparren-Tool, Wandschichtaufbau,
    Walmdach-Tool, Stützen-Tool, …) als Höhenreferenz für Bauteil-
    Höhenmasse und Visualisierung.
  - Beim **Werkplan-Export** als Höhenbezug für Bemassungstexte
    („+2.50 ab OK Fußpfette", „−0.05 ab OK Rohboden").
  - Beim **IFC-Export** als Höhenkomponente des
    `IfcGeometricRepresentationContext` der Tool-Repräsentation.
- **Abgrenzung**:
  - **Ebene** (`ebene`): allgemeines geometrisches Primitiv ohne
    Bezugsrolle. Die Bezugsebene ist eine Ebene mit zugewiesener
    Bezugsrolle in einem Tool.
  - **Welt-Koordinatensystem** (`weltkoordinatensystem`): legt
    Ursprung und alle drei Achsen fest. Die Bezugsebene legt nur
    die z-Höhe fest und ist daher schwächer.
  - **Lokales Koordinatensystem**
    (`lokales_koordinatensystem`): ein bauteil-eigenes
    Koordinatensystem (Ursprung + drei Achsen). Die Bezugsebene
    ist tool-eigen, nicht bauteil-eigen, und legt nur eine z-Höhe
    fest.
  - **Dachfläche** (`dachflaeche`): trägt eine geneigte
    Trägerebene mit Polygonberandung. Die Bezugsebene ist
    horizontal und unbeschränkt; sie ist keine Dachfläche.
  - **Traufe** (`traufe`): horizontale Dachkante an der unteren
    Berandung der Dachfläche; geometrisch eine Strecke, nicht
    eine Ebene. Eine Bezugsebene des Sparren-Tools liegt
    typischerweise auf der Höhe der Traufe (oder darüber, am
    Bleischnitt der Fußpfette), ist aber nicht selbst die
    Traufe.
  - **Fußpfette** (`fusspfette`): Bauteil. Eine Bezugsebene kann
    auf einer ausgezeichneten Fläche der Fußpfette (OK, UK,
    Bleischnitt) verankert sein; sie ist aber nicht selbst die
    Fußpfette.

## Implementierungshinweis

Datentyp (Domänen-Schicht, Kotlin, Schicht
`domain.geometrie.kontext`):

```kotlin
package domain.geometrie.kontext

import domain.geometrie.Ebene

/**
 * Bezugsebene eines Tools: horizontale Ebene in W mit festgelegter
 * z-Höhe, die als Höhenreferenz z = 0 für die im Tool modellierten
 * Bauteile dient.
 *
 * Glossar: hg_bezugsebene.md
 *
 * Pflichtfeld: bezugshoehe (z₀ in mm). Die Trägerebene ergibt sich
 * konstruktiv aus (n_hat = e_hat_z, d = bezugshoehe).
 */
@ConsistentCopyVisibility
data class Bezugsebene internal constructor(
    val bezugshoehe: Double,        // z₀(T), mm in W
) {
    /** Trägerebene als Ebene-Wert (Hesse-Normalform mit n_hat = e_hat_z). */
    fun ebene(): Ebene = /* Ebene mit Normale (0, 0, 1), d = bezugshoehe */ TODO()

    companion object {
        /**
         * Konstruktion aus einer Bezugshöhe. Validiert nur, dass
         * die Höhe finit ist; alle finiten Werte sind zulässig.
         */
        fun aus(bezugshoehe: Double): Resultat<Bezugsebene, BezugsebeneUngueltig> = TODO()
    }
}

sealed class BezugsebeneUngueltig {
    object NichtFinit : BezugsebeneUngueltig()  // NaN/±∞
}
```

- **Einheit**: Bezugshöhe in mm (Double). Welt-Achsenkonvention
  e_hat_z vertikal nach oben.
- **Identität**: keine UUID. Die Bezugsebene ist eine Werteklasse
  (data class), kein identifiziertes Objekt; sie gehört zur Tool-
  Konfiguration und teilt deren Lebenszyklus.
- **Pflicht- und Optionalfelder**:
  - `bezugshoehe` — Pflicht, mm.
  - Die Normale ist konstant e_hat_z (Standardfall horizontale
    Bezugsebene); für geneigte Bezugsebenen wird ein eigener Subtyp
    `GeneigteBezugsebene` als Folgearbeit vorgesehen (Trigger:
    erstes Tool mit nicht-horizontalem Höhenbezug).
- **Invarianten** (in Companion-Factory `Bezugsebene.aus(...)`,
  `Resultat.Fehler` bei Verletzung; keine Exception):
  - `bezugshoehe.isFinite()` — sonst `BezugsebeneUngueltig.NichtFinit`.
- **Tool-Bindung**: Die Bezugsebene wird **nicht** als globaler
  Singleton geführt; sie ist Bestandteil der Tool-Konfiguration
  und wird beim Tool-Start instanziiert. Eine zentrale Registry
  „Bezugsebene des Modells" gibt es nicht; jedes Tool hält seine
  eigene.
- **IFC-Mapping** (Persistenzschicht, Phase 4):
  - Die Bezugsebene wird als Höhenkomponente des
    `IfcGeometricRepresentationContext` der Tool-Repräsentation
    geführt; konkret als `WorldCoordinateSystem` mit angepasstem
    Ursprung (z = bezugshoehe) gegen den globalen IFC-Projektnullpunkt.
- **Edge Cases**:
  - **bezugshoehe = 0**: zulässig; die Bezugsebene fällt mit der
    Welt-z-Nullebene zusammen.
  - **bezugshoehe < 0**: zulässig (z. B. Tool, dessen Höhenbezug
    unterhalb des globalen Modellnullpunkts liegt).
  - **Geneigte Bezugsebene**: nicht durch diesen Datentyp abgedeckt
    (Folgearbeit, Trigger: erstes Tool mit nicht-horizontalem
    Höhenbezug).

**Folgearbeit (trigger-basiert):**

- **Geneigte Bezugsebene** (`GeneigteBezugsebene` als eigener Subtyp
  oder Erweiterung): Trigger: erstes Tool mit Bezugsebene parallel
  zu einer Dachfläche oder einer geneigten Wand.
- **Tool-spezifische Bezugsebenen-Einträge** (z. B. `bezugsebene_sparren_tool.md`,
  `bezugsebene_wandschichtaufbau.md`): Trigger: Aufnahme des
  jeweiligen Tools in die App.
- **Werkplan-Bemassungs-Anbindung** (Höhenbezug-Texte „+2.50 ab
  OK Fußpfette"): Trigger: erstes Werkplan-Beschriftungs-Tool.

## Quellen

**Primär (normativ):**

- DIN 18202:2019-07, „Toleranzen im Hochbau – Bauwerke", DIN
  Deutsches Institut für Normung, Berlin.
- SIA 414/1:2010, „Massgenauigkeit im Bauwesen – Grenzwerte",
  Schweizerischer Ingenieur- und Architektenverein, Zürich.
- ISO 16739-1:2024, „Industry Foundation Classes (IFC) for data
  sharing in the construction and facility management industries
  — Part 1: Data schema" (Entitäten
  `IfcGeometricRepresentationContext`, `IfcLocalPlacement`).
- DIN ISO 80000-2:2022-08, „Größen und Einheiten – Teil 2:
  Mathematik", Abschnitt 2.

**Sekundär:**

- Lignum (Hrsg.): *Lignatec — Geneigte Dächer in Holzbauweise.*
  Lignum, Zürich, aktuelle Auflage.
- SIA 232/1:2020, „Geneigte Dächer", Schweizerischer Ingenieur-
  und Architektenverein, Zürich.
- Mönck, W.; Rug, W.: *Holzbau – Bemessung und Konstruktion.*
  16. Auflage, Beuth, Berlin 2015.

**Korpus (nicht autoritativ):**

- WEKA Verlag: „Masskontrolle nach DIN 18202" (abgerufen
  2026-05-09).
- Wikipedia, Lemma „Höhenbezug" (abgerufen 2026-05-09).
