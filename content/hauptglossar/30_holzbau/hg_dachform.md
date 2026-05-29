---
id: dachform
benennung: Dachform
synonyme: [Dachtyp, Dachgestalt]
abgelehnte_benennungen: [Dachart, "roof shape", "roof type", "roof form"]
oberbegriff: null
begriffstyp: merkmal
voraussetzungen: [dach, dachflaeche, dachneigung, first, traufe, grat, kehle, toleranzen]
abgrenzung_zu: [dach, dachstuhl, dachflaeche, dachneigung, dachtragwerk, dachseite, dachaufbau, gaube, dachoeffnung, bauwerk]
status: entwurf
subglossar_pendant: notwendig
quellen_primär:
  - "SIA 232/1:2020 'Geneigte Dächer', Schweizerischer Ingenieur- und Architektenverein, Abschnitt 1 (Begriffe und geometrische Grundlagen): die einzelnen Dachformen (Sattel-, Pult-, Walm-, Krüppelwalm-, Mansard-, Zelt-) werden im Korpus als bekannt vorausgesetzt; ein geschlossener Begriffseintrag „Dachform“ ist nicht geführt."
  - "DIN EN 1991-1-3:2010-12 'Eurocode 1 – Einwirkungen auf Tragwerke – Teil 1-3: Schneelasten', Tab. 5.2 und Bilder 5.1/5.2 (Pult- und Satteldach), Abschnitt 5.3.4 (Mehrfeld-Dächer), Abschnitt 5.3.5 (Tonnendach), Anhang B (Schneeverwehungen, u. a. Sheddach): Dachform-Namen werden operativ als Eingang in Formbeiwerte μ_i verwendet, ohne sie definitorisch festzulegen."
  - "DIN EN 1991-1-4:2010-12 'Eurocode 1 – Einwirkungen auf Tragwerke – Teil 1-4: Windlasten', Abschnitt 7.2: Druck- und Sogbeiwerte werden für Flach-, Pult-, Sattel-, Walm-, Trog- und gebogene Dächer differenziert; die Formen werden vorausgesetzt, nicht definiert."
  - "DIN 1356-1:1995-02 / :2024-04 'Bauzeichnungen – Teil 1: Arten, Inhalte und Grundregeln der Darstellung': zeichnungstechnische Symbolik für die Darstellung der Dachform in Bauaufrissen (Volltext nicht verifiziert)."
  - "buildingSMART, IFC 4.3, IfcRoofTypeEnum: 14 PredefinedType-Werte (FLAT_ROOF, SHED_ROOF, GABLE_ROOF, HIP_ROOF, HIPPED_GABLE_ROOF, GAMBREL_ROOF, MANSARD_ROOF, BARREL_ROOF, RAINBOW_ROOF, BUTTERFLY_ROOF, PAVILION_ROOF, DOME_ROOF, FREEFORM, USERDEFINED, NOTDEFINED) als externes Pendant; https://ifc43-docs.standards.buildingsmart.org/IFC/RELEASE/IFC4x3/HTML/lexical/IfcRoofTypeEnum.htm. [direkt]"
quellen_sekundär:
  - "Mönck, W.; Rug, W.: Holzbau – Bemessung und Konstruktion. 16. Aufl., Beuth Verlag 2015, Kap. 'Dachformen'."
  - "Natterer, J.; Herzog, T.; Volz, M.: Holzbau-Atlas. 4. Aufl., Birkhäuser, Basel 2003, Kap. 'Tragwerke und Dachformen'."
  - "Lignum (Hrsg.): Lignatec 'Geneigte Dächer in Holzbauweise', Lignum, Zürich, aktuelle Auflage, Kap. 'Dachformen und Neigungen'."
  - "Lignum (Hrsg.): Holzbautabellen HBT, Lignum, Zürich, aktuelle Auflage."
  - "Koepf, H.; Binding, G.: Bildwörterbuch der Architektur. Kröner, Stuttgart, jeweilige Auflage, Lemmata zu den einzelnen Dachformen."
  - "Holzbau Deutschland, Merkblatt 'Begriffe und Klassifizierungen für den Holzbau'."
  - "BauNetz Wissen, 'Dachformen' (https://www.baunetzwissen.de/geneigtes-dach/fachwissen/dachformen) — Korpusbeleg."
quellenkonflikt: |
  **Norm-Lücke.** Keine der konsultierten Normen (SIA 232/1:2020,
  SIA 265:2021, DIN 18531-1, DIN 18338, DIN 1356-1, DIN EN 1991-1-3,
  DIN EN 1991-1-4, DIN EN 1995-1-1) führt einen **geschlossenen
  Begriffseintrag „Dachform“** mit normativer Klassifikations-Liste.
  Die Klassifikation ist berufssprachlich stabil und wird in den
  Lastansatz-Normen (EN 1991-1-3, EN 1991-1-4) **operativ** als
  bekannt vorausgesetzt: einzelne Dachform-Namen (Pultdach,
  Satteldach, Tonnendach, Sheddach) treten als Eingang in
  Formbeiwerte auf, ohne dass die Formen selbst definiert wären.
  Eigene Festlegung dieses Glossars: Dachform ist ein
  klassifikatorisches **Merkmal des Daches**, abgeleitet aus der
  Topologie der Dachflächen-Familie 𝒟; ein endlicher Werte-Katalog
  bildet die im DACH-Holzbau-Korpus etablierten Formen ab und ist
  weitgehend deckungsgleich mit `IfcRoofTypeEnum`.

  **Drei orthogonale Klassifikations-Achsen am Dach.** Die in der
  Fachliteratur teils vermischte Verwendung wird hier sauber getrennt:

  - **Dachform** (diese Datei): rein **geometrische** Klassifikation
    der äußeren Dachhülle nach Anzahl, Anordnung und Krümmung der
    Dachflächen. Wert am `dach` (Merkmal).
  - **Dachstuhl-Typ** (eigener Eintrag `hg_dachstuhl.md` folgt):
    Klassifikation der **zimmermannsmäßigen Tragwerks-Konstruktion**
    (Sparrendach, Pfettendach, Kehlbalkendach, Binderdach). Wert am
    `dachtragwerk` / `tragwerk`. Im Korpus auch „Dachtyp" genannt —
    diese Mehrdeutigkeit ist der Grund, warum „Dachtyp" hier nur als
    Synonym von Dachform mit Eindeutigkeits-Vorbehalt geführt wird.
  - **Dach** (`hg_dach.md`): das übergeordnete **Aggregat** aus
    Tragwerk, Dachflächen-Familie und Dachaufbau. Trägt die Dachform
    als abgeleitete Eigenschaft.

  Die Beziehung Dachform ↔ Dachstuhl-Typ ist eine **lose
  Implikation**: ein Walmdach erfordert typischerweise ein
  Pfettendach (Gratsparren liegen quer zur Sparrenebene), aber die
  Dachform legt den Dachstuhl-Typ nicht eindeutig fest, und mehrere
  Dachstuhl-Typen lassen sich für dieselbe Dachform realisieren
  (Mönck/Rug, Natterer, BauNetz Wissen).

  **Mansard/Gambrel-Asymmetrie.** Der IFC-Standard 4.3 trennt
  GAMBREL_ROOF (Mansard mit zwei Seiten, Sattel-Variante) von
  MANSARD_ROOF (Mansard mit vier Seiten, Walm-Variante). Im DACH-
  Holzbau-Korpus ist **Mansarddach** der Oberbegriff für „Knick pro
  Dachseite" und deckt **beide** IFC-Werte ab; die Differenzierung
  erfolgt im Deutschen über die Zahl der geknickten Seiten, nicht
  über zwei eigenständige Namen (BauNetz, Wikipedia „Mansarddach",
  Carpentry Way Blog). Der App-Code-Pendant `Mansarddach`
  parametrisiert daher die Seitenanzahl (2 oder 4), und der IFC-
  Export bildet auf GAMBREL_ROOF bzw. MANSARD_ROOF ab.

  **Sheddach-Lücke in IFC.** `IfcRoofTypeEnum` enthält keinen
  eigenen Wert für das **Sheddach (Sägezahn)**; das im Industriebau
  etablierte Reihen-Pultdach wird beim IFC-Export typischerweise als
  Komposition mehrerer `SHED_ROOF`-Elemente oder als `FREEFORM`
  exportiert (Vermutung aus IFC-Mapping-Praxis, keine normative
  Quelle). Die App-Seite führt Sheddach als eigenen, parametrischen
  Wert (Anzahl der Sheds); der IFC-Mapping-Konflikt ist Thema einer
  Folgearbeit im IFC-Export-Modul.

  **Synonym „Dachtyp".** Im Korpus (Online-Glossare, Hersteller-
  Sites) wird „Dachtyp" weitgehend synonym mit Dachform verwendet,
  bezieht sich aber teilweise auch auf die Konstruktions-Achse
  (Sparrendach/Pfettendach/Binderdach). Wegen dieser Mehrdeutigkeit
  ist „Dachtyp" hier nur als sekundäres Synonym geführt; die
  Hauptbenennung bleibt „Dachform“.

  **Bogen-/Tonnendach-Unschärfe.** BauNetz Wissen weist explizit
  darauf hin, dass „Bogendach" im DACH-Korpus „nicht klar definiert"
  ist und der Übergang zum Tonnendach fließend ist (Krümmungsmaß,
  Halbkreis vs. Kreissegment). Die App-Seite folgt der schärferen
  Lesart: Tonnendach = Halbkreis-Querschnitt, Bogendach =
  Kreissegment kleiner als Halbkreis; bei Grenzfällen wird der
  Code-Pendant-Wert `Bogendach` mit explizitem Krümmungs-Parameter
  geführt.
---

## Prosa-Definition

Die **Dachform** eines Daches ist sein klassifikatorisches geometrisches
Merkmal nach Anzahl, Anordnung, Neigungsverteilung, Schnittkanten-
Topologie und Krümmung der Dachflächen seiner Dachflächen-Familie,
ohne Bezug auf den materiellen Dachaufbau und ohne Bezug auf den
konstruktiven Typ seines Tragwerks.

## Mathematische Definition

Sei

- d = (T, 𝒟, A) ein Dach im Sinne von `dach` mit Dachflächen-Familie
  𝒟 = { D₁, …, D_m }, m ≥ 1, D_i = (E_i, P_i, n_{a,i}),
- α_i := α(D_i) ∈ [0, π/2) die Dachneigung jeder Dachfläche D_i
  nach `dachneigung`,
- K(D_i, D_j) ⊂ ℝ³ der Schnitt der berandeten Dachflächen
  F(P_i) ∩ F(P_j) für i ≠ j; dieser Schnitt ist entweder leer, ein
  einzelner Punkt oder eine Strecke (gemeinsame Randstrecke) gemäß
  der Selbstüberlapps-Bedingung in `dach`,
- 𝓚(d) := { K(D_i, D_j) | i ≠ j, K(D_i, D_j) ist eine Strecke } die
  Menge der gemeinsamen Randstrecken,
- klass: 𝓚(d) → {first, grat, kehle} die Klassifikation jeder
  gemeinsamen Randstrecke gemäß den Einträgen `first`, `grat`,
  `kehle` (First ≈ horizontal, beide n_a treffen sich bergauf;
  Grat geneigt und konvex ausspringend; Kehle geneigt und konkav
  einspringend),
- κ_i ∈ {eben, gekrümmt} die Krümmungs-Klasse von E_i (eben für
  alle Dachflächen im Sinne von `dachflaeche`; gekrümmte
  Dachflächen sind ein App-spezifischer Erweiterungsfall, dessen
  Definition im Subglossar/Folgeeintrag `gekruemmte_dachflaeche`
  ausgearbeitet wird).

Dann ist die **Dachform** von d die Klassifikations-Funktion

```
form: Dach → 𝓕
form(d) := Φ( m, (α_i)_{i=1..m}, 𝓚(d), klass, (κ_i)_{i=1..m} )
```

wobei

- 𝓕 := { Flachdach, Pultdach, Satteldach, Walmdach,
  Krüppelwalmdach, Zeltdach, Mansarddach(s, β), Schmetterlingsdach,
  Sheddach(n), Tonnendach, Bogendach(r) } ∪ {Freiform}
  der endliche Werte-Katalog ist (zwölf etablierte Formen plus
  Freiform-Ausweichwert; einzelne Werte tragen Parameter:
  s ∈ {2, 4} und β ∈ (0, π/2) für das Mansarddach, n ≥ 2 für das
  Sheddach, r > 0 für das Bogendach), und

- Φ die folgende stückweise Klassifikation ist (Hauptfälle; nicht
  exhaustiv für alle Mischformen; bei Mehrdeutigkeit gilt die
  spezifischere Form vor der allgemeineren):

```
Φ = Flachdach          falls  m = 1  und  α_1 ≤ ε_α
Φ = Pultdach           falls  m = 1  und  α_1 >  ε_α
Φ = Satteldach         falls  m = 2  und  |𝓚(d)| = 1
                              und klass(K_{12}) = first
Φ = Schmetterlingsdach falls  m = 2  und  |𝓚(d)| = 1
                              und klass(K_{12}) = kehle
Φ = Walmdach           falls  m = 4  und alle vier Dachflächen
                              treffen sich in einem First mit zwei
                              Walmen (vier Traufkanten, vier Grat-
                              kanten, ein First; klass-Multi-
                              menge: {first × 1, grat × 4})
Φ = Krüppelwalmdach    falls  m = 4  und Walm-Topologie,
                              aber die Walme erreichen nicht die
                              Traufe (zwei Krüppelwalm-Trapeze
                              statt zwei vollständiger Walme)
Φ = Zeltdach           falls  m ≥ 3  und alle Dachflächen treffen
                              sich in einem einzigen Punkt
                              (Spitze, kein First; alle Schnitt-
                              kanten sind Grate, |first| = 0)
Φ = Mansarddach(s, β)  falls  jede der s ∈ {2, 4} Dachseiten
                              durch zwei Dachflächen unterschied-
                              licher Neigung mit horizontalem
                              Knick zusammengesetzt ist; β ist der
                              Knickwinkel
Φ = Sheddach(n)        falls  m = 2n und die Dachflächen sich zu
                              n hintereinander gereihten Pult-
                              elementen mit lotrechten Zwischen-
                              flächen ordnen
Φ = Tonnendach         falls  𝒟 eine einzige gekrümmte Dachfläche
                              mit Halbkreis-Querschnitt enthält
Φ = Bogendach(r)       falls  𝒟 eine einzige gekrümmte Dachfläche
                              mit Kreissegment-Querschnitt mit
                              Radius r enthält und der Bogen
                              kleiner als ein Halbkreis ist
Φ = Freiform           sonst (keine der obigen Klassen trifft zu)

Hinweis: „Trogdach" ist im DACH-Korpus eine berufssprachliche
Variante des Schmetterlingsdachs bei größeren Spannweiten oder
Industriebauten; geometrisch deckungsgleich (m = 2, eine Kehle,
beide Dachflächen nach innen geneigt) — Φ liefert in beiden
Fällen `Schmetterlingsdach`. „Trogdach" wird als Synonym von
Schmetterlingsdach geführt, nicht als eigener Φ-Wert.
```

ε_α := Toleranzen.WINKEL_EPS ist der Grenzwert, ab dem eine
einzelne Dachfläche als „nicht horizontal" gilt; faktisch wird in
der Praxis ein größerer Schwellenwert (etwa 7°/10° nach Lignum)
verwendet, dieser ist aber **nicht normativ** und gehört in die
Bemessungs-/Aufbau-Schicht (Eindeckungs-Mindestneigung), nicht in
die geometrische Klassifikation.

## Wohldefiniertheit

- **Existenz**: Für jedes Dach d mit nicht-leerer Dachflächen-
  Familie 𝒟 ist Φ(d) wohldefiniert: die Argumente m, (α_i),
  𝓚(d), klass und (κ_i) sind aus 𝒟 und den bereits definierten
  Begriffen `dachflaeche`, `dachneigung`, `first`, `grat`, `kehle`
  konstruktiv ableitbar. Der Ausweichwert `Freiform` garantiert,
  dass die Klassifikation für jedes d ein Resultat liefert.
- **Eindeutigkeit der Klassifikation**: Φ ist als Funktion
  definiert, d. h. liefert für jedes d einen eindeutigen Wert in
  𝓕. Die Bedingungen der Hauptfälle schließen sich paarweise aus
  bis auf wohldefinierte Spezialisierungs-Hierarchien (Krüppelwalm
  vor Walm, Zeltdach vor Walm im Grenzfall verschwindender
  Firstlänge); die App-Implementierung führt die Prüfreihenfolge
  vom spezifischeren zum allgemeineren Fall.
- **Invarianz unter Permutation**: 𝒟 ist als Menge unsortiert
  (siehe `dach`); 𝓚(d) und klass hängen nur von der Inzidenz der
  Dachflächen ab, nicht von einer gewählten Indizierung. Φ(d) ist
  damit invariant unter jeder Permutation der Dachflächen.
- **Invarianz unter Modell-Skalierung und Translation**: Die
  Klassifikation hängt nur von Winkeln (α_i, Knickwinkel β) und
  topologischen Inzidenzen ab, nicht von absoluten Längen. Sie ist
  damit invariant unter isotroper Skalierung und Translation des
  Modells, **aber nicht** invariant unter anisotroper Skalierung
  (die das Welt-Koordinatensystem ohnehin verbietet, siehe
  `weltkoordinatensystem`).
- **Eindeutigkeit der Parameter**: Für `Mansarddach(s, β)` ist β
  der Mittelwert der zwei vorkommenden Dachneigungen pro Seite —
  und durch die geometrische Konfiguration eindeutig bestimmt;
  Mansarddächer mit unterschiedlichen Knickwinkeln auf
  unterschiedlichen Seiten sind als `Freiform` klassifiziert. Für
  `Sheddach(n)` ist n die Anzahl der Pult-Elemente; für
  `Bogendach(r)` der Krümmungs-Radius der einzigen gekrümmten
  Dachfläche.
- **Grenzfälle**:
  - **Walmdach mit Firstlänge → 0**: kollabiert zum Zeltdach.
    Die Klassifikation folgt der Längen-Klassifikation der
    First-Strecke gegen `Toleranzen.LAENGE_EPS`; bei
    First-Strecken-Länge ≤ `Toleranzen.LAENGE_EPS` wird Zeltdach
    zurückgegeben.
  - **Krüppelwalm mit verschwindender Krüppelhöhe**: kollabiert
    zum Walmdach. Auch hier entscheidet ein Längen-Vergleich
    gegen `Toleranzen.LAENGE_EPS`.
  - **Mehrfach-Dach am selben Bauwerk** (z. B. zwei Satteldach-
    Flügel über separat verbundenen Trakten): wird laut `dach`
    als zwei getrennte Dach-Instanzen modelliert und entsprechend
    pro Instanz klassifiziert.
- **Konservativität**: Die Definition ist Abkürzung der konstruktiven
  Klassifikation aus den bereits definierten Begriffen
  `dachflaeche`, `dachneigung`, `first`, `grat`, `kehle`; sie führt
  kein zusätzliches Axiom ein.
- **Nicht-Zirkularität**: Die Definition verwendet nur `dach`,
  `dachflaeche`, `dachneigung`, `first`, `grat`, `kehle` und
  `toleranzen`. Sie kommt nicht in ihrer eigenen Definition vor.
  Die Werte des Katalogs 𝓕 sind durch ihre topologischen
  Bedingungen definiert, nicht durch Selbstreferenz.

## Erläuterung (nicht normativ)

Die Dachform abstrahiert von der Konstruktion und vom Material und
beschreibt das Dach **nur durch seine geometrische Erscheinung von
außen**: ein Satteldach mit Pfettendach und ein Satteldach mit
Sparrendach haben dieselbe Dachform, aber unterschiedliche Tragwerks-
Konstruktionen; ein Walmdach mit Tonziegeln und ein Walmdach mit
Blecheindeckung haben dieselbe Dachform, aber unterschiedliche
Dachaufbauten.

### Zwölf-Form-Katalog des DACH-Holzbau-Korpus

Im DACH-Holzbau sind die folgenden zwölf Dachformen
berufssprachlich etabliert (Mönck/Rug, Natterer, Lignum, BauNetz
Wissen). Die Tafel ist deskriptiv, nicht normativ; sie zeigt
Geometrie-Kern und IFC-Mapping pro Form.

| Dachform              | Geometrie-Kern                                                              | IFC 4.3 (`IfcRoofTypeEnum`) |
|-----------------------|-----------------------------------------------------------------------------|-----------------------------|
| **Flachdach**         | m = 1, α ≤ ε_α (faktisch < 7°–10°)                                          | `FLAT_ROOF`                 |
| **Pultdach**          | m = 1, α > ε_α                                                              | `SHED_ROOF`                 |
| **Satteldach**        | m = 2, zwei gegeneinander geneigte Dachflächen mit horizontalem First       | `GABLE_ROOF`                |
| **Walmdach**          | m = 4, vier geneigte Dachflächen, ein First, zwei Walmflächen statt Giebel  | `HIP_ROOF`                  |
| **Krüppelwalmdach**   | wie Walmdach, Walme reichen nicht bis zur Traufe (Giebel-Trapez bleibt)     | `HIPPED_GABLE_ROOF`         |
| **Zeltdach**          | m ≥ 3, alle Dachflächen treffen in einer Spitze (kein First)                | `PAVILION_ROOF`             |
| **Mansarddach**       | pro Dachseite zwei Neigungs-Segmente mit horizontalem Knick; s ∈ {2, 4}     | `GAMBREL_ROOF` / `MANSARD_ROOF` (siehe Quellenkonflikt) |
| **Schmetterlingsdach**| umgekehrtes Satteldach: zwei V-förmig nach innen geneigte Dachflächen       | `BUTTERFLY_ROOF`            |
| **Sheddach (Sägezahn)**| n ≥ 2 hintereinander gereihte Pultflächen mit lotrechten Zwischenflächen   | **kein eigener IFC-Wert** (siehe Quellenkonflikt) |
| **Tonnendach**        | gekrümmte Dachfläche, Querschnitt Halbkreis                                 | `BARREL_ROOF`               |
| **Bogendach**         | gekrümmte Dachfläche, Querschnitt Kreissegment (kleiner als Halbkreis)      | `RAINBOW_ROOF`              |

`PAVILION_ROOF` schließt den Spezialfall **Pyramidendach** ein
(vier gleiche Flächen über quadratischem Grundriss); im DACH-
Korpus wird Pyramidendach teils synonym mit Zeltdach, teils enger
verwendet (Wikipedia „Zeltdach"). Die App führt nur Zeltdach als
eigenen Wert; die Pyramiden-Eigenschaft ist eine
abgeleitete Eigenschaft der Symmetrie der Dachflächen.

### Dachform ↔ Dachstuhl-Typ als orthogonale Achsen

Die App-Modellierung trennt drei orthogonale Klassifikations-
Achsen am Dach:

- **Dachform** (diese Datei): rein geometrisch, abgeleitet aus 𝒟.
- **Dachstuhl-Typ** (`hg_dachstuhl.md` folgt): konstruktiv,
  abgeleitet aus dem Tragwerk T (Sparren-/Pfetten-/Kehlbalken-/
  Binderdach). Im Korpus auch „Dachtyp" — diese Mehrdeutigkeit ist
  der Grund, warum „Dachtyp" hier kein eigenständiges Synonym ist.
- **Dachaufbau-Typ** (`hg_dachaufbau.md`): materialschichtig,
  Kaltdach/Warmdach/Umkehrdach.

Eine Dachform schränkt mögliche Dachstuhl-Typen ein, legt sie aber
nicht eindeutig fest. Walmdächer erfordern typischerweise ein
Pfettendach (Gratsparren liegen quer zur Sparrenebene), aber dasselbe
Satteldach kann als Sparrendach, Pfettendach oder Kehlbalkendach
ausgeführt werden.

### Verhältnis zu `IfcRoofTypeEnum`

Das App-Pendant zu `dach` ist `IfcRoof`; die Dachform-Klassifikation
hängt als `PredefinedType: IfcRoofTypeEnum` an dieser Entität. Das
ist strukturell identisch zur App-Empfehlung: Dachform als **Wert
am Dach**, nicht als Subtyp des Dachs. Die zwei dokumentierten
Reibungsstellen — Mansard/Gambrel-Asymmetrie und Sheddach-Lücke —
sind im Quellenkonflikt-Block beschrieben.

## Beziehungen

- **Oberbegriff**: `null`. Dachform ist ein klassifikatorisches
  Merkmal des Daches; ein generischer Oberbegriff (etwa
  „bauwerks_klassifikationsmerkmal") existiert im Glossar nicht und
  ist auch nicht geplant.
- **Träger**: `dach`. Die Dachform ist eine abgeleitete Eigenschaft
  einer `dach`-Instanz und wird nicht freistehend modelliert.
- **Voraussetzungen**:
  - **`dach`**: das Aggregat, dessen Dachflächen-Familie 𝒟 die
    Klassifikation trägt.
  - **`dachflaeche`**: die elementare ebene Komponente von 𝒟.
  - **`dachneigung`**: das Winkel-Merkmal, das in die
    Klassifikation eingeht (Flach- vs. Pultdach, Mansard-Knick).
  - **`first`, `traufe`, `grat`, `kehle`**: die Kantentypen, die
    in der Klassifikation der gemeinsamen Randstrecken
    aufgerufen werden.
  - **`toleranzen`**: für die Längen- und Winkel-Schwellen der
    Grenzfälle (First → 0, α → 0, Krüppel-Höhe → 0).
- **Werte des Katalogs 𝓕** (eigene Einträge folgen, nicht alle
  notwendig — Mansarddach und Sheddach werden über parametrische
  sealed-Subtypen des Code-Pendants abgedeckt; eigenständige
  Glossareinträge für jede Dachform sind **nicht** automatisch
  vorgesehen, sondern werden trigger-basiert je nach erstem
  Tool-Bedarf angelegt):
  - `flachdach`, `pultdach`, `satteldach`, `walmdach`,
    `krueppelwalmdach`, `zeltdach`, `mansarddach`,
    `schmetterlingsdach`, `sheddach`, `tonnendach`, `bogendach`,
    `trogdach`.
- **Abgrenzung**:
  - **`dach`**: das Aggregat als Ganzes; Dachform ist eines seiner
    Merkmale, nicht das Dach selbst.
  - **`dachstuhl`** (eigener Eintrag folgt): die konstruktive
    Tragwerks-Klassifikation (Sparrendach/Pfettendach/
    Kehlbalkendach/Binderdach). Orthogonale Achse zur Dachform;
    eine Dachform legt den Dachstuhl-Typ nicht eindeutig fest.
  - **`dachflaeche`**: die elementare Komponente, deren Familie
    klassifiziert wird; Dachform ist eine Eigenschaft der
    **Familie**, nicht der einzelnen Dachfläche.
  - **`dachneigung`**: ein Winkel-Merkmal **einer einzelnen**
    Dachfläche; Dachform ist ein Topologie-Merkmal **der ganzen
    Familie**.
  - **`dachtragwerk`** (eigener Eintrag folgt unter `tragwerk`):
    das lastabtragende Aggregat unter dem Dach; trägt den Dachstuhl-
    Typ, nicht die Dachform.
  - **`dachseite`**: eine Dachfläche mit Orientierungs-Annotation
    (Wetterseite, Sonnenseite); nicht synonym mit Dachform.
  - **`dachaufbau`**: die materielle Schichtfolge; orthogonal zur
    Dachform (jede Dachform kann mit unterschiedlichen Aufbauten
    realisiert werden).
  - **`gaube`** (Forward-Verweis): ein Dachaufbau-Element auf
    einer Dachfläche; verändert die Dachform der Hauptdachfläche
    nicht, sondern wird als eigene Subgeometrie geführt.
  - **`dachoeffnung`** (Forward-Verweis): lokale Aussparung in
    Dachfläche und Dachaufbau (Schornstein, Dachflächenfenster);
    kein Form-Merkmal.
  - **`bauwerk`** (Forward-Verweis): die übergeordnete Einheit;
    ein Bauwerk kann mehrere Dächer unterschiedlicher Dachform
    tragen.

## Implementierungshinweis

Die Dachform wird im Code als **`sealed class Dachform`** modelliert,
weil einige Form-Werte parametrisch sind (Mansarddach: Seitenzahl
und Knickwinkel; Sheddach: Anzahl Pult-Elemente; Krüppelwalmdach:
Krüppel-Höhe oder -Anteil; Bogendach: Krümmungsradius). Ein reines
`enum class` reicht für diese Werte nicht aus.

Datentyp (Domänen-Schicht, Kotlin, Schicht `domain.bauteil`):

```kotlin
package domain.bauteil

/**
 * Dachform: klassifikatorisches geometrisches Merkmal eines Daches.
 * Glossar: hg_dachform.md
 *
 * Strukturell ein Wert am `Dach`, keine eigene Identität. Wird über
 * `Dach.dachform()` aus der Topologie der Dachflächen-Familie 𝒟
 * abgeleitet.
 *
 * Sealed-Hierarchie (nicht Enum), weil einige Werte parametrisch
 * sind (Mansarddach, Sheddach, Krüppelwalmdach, Bogendach).
 */
sealed class Dachform {

    /** m = 1, α ≤ Toleranzen.WINKEL_EPS. */
    data object Flachdach : Dachform()

    /** m = 1, α > Toleranzen.WINKEL_EPS. */
    data object Pultdach : Dachform()

    /** m = 2, ein horizontaler First. */
    data object Satteldach : Dachform()

    /** m = 4, ein First plus zwei Walme bis zur Traufe. */
    data object Walmdach : Dachform()

    /**
     * Wie Walmdach, Walme erreichen nicht die Traufe.
     * @param kruppelHoeheAnteil h_k / h_g ∈ (0, 1) — Verhältnis
     *        der Krüppelwalm-Höhe zur Giebelhöhe.
     */
    data class Krueppelwalmdach(val kruppelHoeheAnteil: Double) : Dachform()

    /** m ≥ 3, alle Dachflächen treffen in einer Spitze. */
    data object Zeltdach : Dachform()

    /**
     * Pro Dachseite zwei Neigungs-Segmente mit horizontalem Knick.
     * @param seiten 2 (entspricht IFC GAMBREL_ROOF, Sattel-Variante)
     *               oder 4 (entspricht IFC MANSARD_ROOF, Walm-Variante).
     * @param knickwinkel β ∈ (0, π/2) — Knickwinkel zwischen oberem
     *                   und unterem Segment, in Radiant.
     */
    data class Mansarddach(val seiten: Int, val knickwinkel: Double) : Dachform()

    /** m = 2, ein zentrale Kehle (V-förmig). */
    data object Schmetterlingsdach : Dachform()

    /**
     * n hintereinander gereihte Pult-Elemente mit lotrechten
     * Zwischenflächen.
     * @param anzahlSheds n ≥ 2.
     */
    data class Sheddach(val anzahlSheds: Int) : Dachform()

    /** Halbkreis-Querschnitt. */
    data object Tonnendach : Dachform()

    /**
     * Kreissegment-Querschnitt kleiner als Halbkreis.
     * @param kruemmungsradius r > 0 in mm.
     */
    data class Bogendach(val kruemmungsradius: Double) : Dachform()

    /** Ausweichwert für nicht klassifizierbare Geometrien. */
    data object Freiform : Dachform()
}

/**
 * Klassifikations-Funktion form: Dach → 𝓕.
 * Glossar: hg_dachform.md, Mathematische Definition.
 */
fun Dach.dachform(): Dachform = TODO("Implementierung folgt in Etappe Walmdach-Tool")
```

- **Einheit**: Knickwinkel β intern in **Radiant** (Double);
  Krümmungsradius in **mm** (Double); Krüppelwalm-Anteil
  **dimensionslos** (Double in (0, 1)). Anzeige in Grad
  ausschließlich am API-Rand.
- **Identität**: keine. Dachform ist ein Wert am Dach, kein Objekt
  mit eigener UUID.
- **Invarianten**:
  - `Krueppelwalmdach.kruppelHoeheAnteil` ∈ (0, 1); 0 entspricht
    Walmdach, 1 entspricht Satteldach mit beidseitigem Giebel.
  - `Mansarddach.seiten` ∈ {2, 4}; andere Werte sind unzulässig.
  - `Mansarddach.knickwinkel` ∈ (Toleranzen.WINKEL_EPS,
    π/2 − Toleranzen.WINKEL_EPS).
  - `Sheddach.anzahlSheds` ≥ 2; n = 1 ist Pultdach.
  - `Bogendach.kruemmungsradius` > 0 mm.
- **Edge Cases**:
  - **Mehrfach-Klassifikation**: bei Mischformen (z. B.
    Mansard-Sattel mit unterschiedlichen Knickwinkeln auf den
    zwei Seiten) liefert `Dach.dachform()` `Dachform.Freiform`.
  - **Grenzfälle Walm ↔ Zelt**: First-Länge ≤
    `Toleranzen.LAENGE_EPS` ⇒ Zeltdach.
  - **Grenzfälle Walm ↔ Krüppelwalm**: Krüppel-Höhen-Anteil ≤
    `Toleranzen.LAENGE_EPS`-relativ ⇒ Walmdach.
  - **Pyramidendach**: spezifischer Subfall des Zeltdachs mit
    vier gleichen Dachflächen über quadratischem Grundriss; im
    Code als Eigenschaft `Zeltdach.istPyramide()` (Folgearbeit),
    nicht als eigener Wert.
- **IFC-Mapping** (Folgearbeit im IFC-Export-Modul):
  - `Flachdach` → `FLAT_ROOF`
  - `Pultdach` → `SHED_ROOF`
  - `Satteldach` → `GABLE_ROOF`
  - `Walmdach` → `HIP_ROOF`
  - `Krueppelwalmdach` → `HIPPED_GABLE_ROOF`
  - `Zeltdach` → `PAVILION_ROOF`
  - `Mansarddach(2, β)` → `GAMBREL_ROOF`
  - `Mansarddach(4, β)` → `MANSARD_ROOF`
  - `Schmetterlingsdach` → `BUTTERFLY_ROOF`
  - `Sheddach(n)` → Komposition von n × `SHED_ROOF` **oder**
    `FREEFORM` mit `ObjectType = "Sheddach"`; Behandlung im
    IFC-Export entscheiden (siehe Quellenkonflikt).
  - `Tonnendach` → `BARREL_ROOF`
  - `Bogendach(r)` → `RAINBOW_ROOF`
  - `Freiform` → `FREEFORM` mit `ObjectType`-String.
- **Verwendungsregel**: Funktionen der Last-Eingabe (Schneelast,
  Windlast) nehmen die Dachform als Klassifikations-Eingang, um die
  passenden Formbeiwerte aus EN 1991-1-3 bzw. EN 1991-1-4
  auszuwählen. Die Geometrie selbst (α_i, Stützweiten) bleibt
  unabhängig führend.

## Quellen

**Primär (normativ):**

- SIA 232/1:2020, „Geneigte Dächer", Schweizerischer Ingenieur-
  und Architektenverein, Zürich, Abschnitt 1.
- DIN EN 1991-1-3:2010-12, „Eurocode 1: Einwirkungen auf
  Tragwerke – Teil 1-3: Schneelasten", Abschnitt 5.3, Tab. 5.2,
  Bilder 5.1/5.2, Anhang B.
- DIN EN 1991-1-4:2010-12, „Eurocode 1: Einwirkungen auf
  Tragwerke – Teil 1-4: Windlasten", Abschnitt 7.2.
- DIN 1356-1:1995-02 / :2024-04, „Bauzeichnungen – Teil 1:
  Arten, Inhalte und Grundregeln der Darstellung", Abschnitt 5
  (Volltext nicht verifiziert).

**Primär (externes Pendant):**

- buildingSMART, IFC 4.3, `IfcRoofTypeEnum`,
  https://ifc43-docs.standards.buildingsmart.org/IFC/RELEASE/IFC4x3/HTML/lexical/IfcRoofTypeEnum.htm.
- buildingSMART, IFC4 ADD2, `IfcRoofTypeEnum`,
  https://standards.buildingsmart.org/IFC/RELEASE/IFC4/ADD2/HTML/schema/ifcsharedbldgelements/lexical/ifcrooftypeenum.htm.

**Sekundär:**

- Mönck, W.; Rug, W.: *Holzbau – Bemessung und Konstruktion.*
  16. Auflage, Beuth Verlag 2015, Kap. „Dachformen".
- Natterer, J.; Herzog, T.; Volz, M.: *Holzbau-Atlas.*
  4. Auflage, Birkhäuser, Basel 2003.
- Lignum (Hrsg.): *Lignatec — Geneigte Dächer in Holzbauweise.*
  Lignum, Zürich, aktuelle Auflage.
- Lignum (Hrsg.): *Holzbautabellen HBT.* Lignum, Zürich, aktuelle
  Auflage.
- Koepf, H.; Binding, G.: *Bildwörterbuch der Architektur.*
  Kröner, Stuttgart, jeweilige Auflage.
- Holzbau Deutschland, Merkblatt „Begriffe und Klassifizierungen
  für den Holzbau".
- BauNetz Wissen, „Dachformen",
  https://www.baunetzwissen.de/geneigtes-dach/fachwissen/dachformen
  (abgerufen 2026-05-14).

**Korpus (nicht autoritativ):**

- Wikipedia, Lemmata „Dachform“, „Walmdach", „Krüppelwalmdach",
  „Mansarddach", „Zeltdach", „Pyramidendach", „Sparrendach",
  „Pfettendach", „Dachstuhl" (deutsch); „List of roof shapes",
  „Hip roof", „Mansard roof", „Gambrel" (englisch);
  abgerufen 2026-05-14.
- Sanier.de, „Fachbegriffe rund ums Dach"; baucheck.io;
  energie-experten.org; holzbau-system.de; woodipedia.de
  — Korpusbelege zum Sprachgebrauch von „Dachform“ und „Dachtyp".

**Negativer Befund:** kein konsultiertes Normwerk (SIA 232/1,
SIA 265, DIN 1356-1, DIN 18531, DIN 18338, DIN EN 1991-1-3,
DIN EN 1991-1-4, DIN EN 1995-1-1) führt einen geschlossenen
Begriffseintrag „Dachform“; die Klassifikation existiert
operativ als bekannt vorausgesetzte Aufzählung. Die hier gewählte
formale Definition über die Topologie der Dachflächen-Familie ist
**eigene Festlegung**, konsistent mit allen konsultierten Quellen.
