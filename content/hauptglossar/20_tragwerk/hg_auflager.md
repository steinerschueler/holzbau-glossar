---
id: auflager
benennung: Auflager
synonyme: [Lager, Stützung]
abgelehnte_benennungen: [Anschluss, Knoten, Sparrenfuß, Mauerbank, Mauerlatte, "support", "bearing", "seat", "saddle"]
oberbegriff: null
begriffstyp: aggregat
voraussetzungen: [bauteil, polyeder, polygon, punkt, vektor, einheitsvektor, uuid, weltkoordinatensystem, toleranzen]
abgrenzung_zu: [bauteil, kerve, bearbeitung, verbindung, verbindungsmittel, tragwerk, auflageflaeche, lastfall, statisches_system, konstruktionsdetail]
status: entwurf
subglossar_pendant: notwendig
quellen_primär:
  - "ISO 16739-1:2024 'Industry Foundation Classes (IFC) – Part 1: Data schema', IFC 4.3, Structural Analysis Domain: `IfcStructuralConnection` (abstrakt) mit den konkreten Subtypen `IfcStructuralPointConnection`, `IfcStructuralCurveConnection`, `IfcStructuralSurfaceConnection`; Attribut `AppliedCondition` vom Typ `IfcBoundaryCondition` mit den Subtypen `IfcBoundaryNodeCondition`, `IfcBoundaryEdgeCondition`, `IfcBoundaryFaceCondition` (pro Freiheitsgrad fest/frei/federnd); zugehörige Reaktion `IfcStructuralReaction` mit `IfcStructuralLoadSingleForce` als Last-Tupel (ForceX/Y/Z, MomentX/Y/Z)."
  - "DIN EN 1990:2010-12 'Eurocode: Grundlagen der Tragwerksplanung', Abschnitt 1.5 (Begriffe): „Auflager“ als Stelle der Lagerreaktion vorausgesetzt; keine geschlossene Begriffs-Definition."
  - "DIN EN 1995-1-1:2010-12 (Eurocode 5), Abschnitt 6.1.5 (Druck rechtwinklig zur Faser, Auflagerpressung) und Abschnitt 6.5 (Schubnachweis am ausgeklinkten Auflager); Auflagerlänge ℓ als operationale Bemessungsgröße."
  - "SIA 260:2013 'Grundlagen der Projektierung von Tragwerken', Abschnitt 1 (Geltungsbereich) und Abschnitt 2 (Begriffe): „Auflager“ als Ort der Lagerreaktion vorausgesetzt."
  - "SIA 265:2021 'Holzbau', Abschnitt 5 (Konstruktive Durchbildung) und Anhang B (Schub am ausgeklinkten Bereich): Auflagerausbildung im Holzbau."
  - "DIN 1052:2008-12, Abschnitt 12 (Konstruktive Anforderungen): Auflagerpressung, Auflagerlänge."
quellen_sekundär:
  - "Petersen, Chr.: Statik und Stabilität der Baukonstruktionen. Vieweg, Braunschweig (mehrfache Auflagen); Lehrbuch-Standard zur Klassifikation Loslager/Festlager/Einspannung im ebenen und räumlichen Fall."
  - "Schneider, K.-J.; Albert, A.: Bautabellen für Ingenieure. 26. Aufl., Bundesanzeiger Verlag, Köln 2024; Auflager-Klassifikation Punkt-/Linien-/Flächenauflager."
  - "Mönck, W.; Rug, W.: Holzbau – Bemessung und Konstruktion. 16. Aufl., Beuth, Berlin 2015, Kap. 11 'Dachtragwerke', § Sparrenauflager auf Pfetten."
  - "Blass, H. J.; Sandhaas, C.: Ingenieurholzbau – Grundlagen der Bemessung. KIT Scientific Publishing, Karlsruhe 2016, Kap. 5 (Stab-Bauteile) und Kap. 8 (Verbindungen / Anschlüsse)."
  - "Natterer, J.; Herzog, T.; Volz, M.: Holzbau-Atlas. 4. Aufl., Birkhäuser, Basel 2003, Kap. 'Tragwerke' / 'Anschlüsse'."
  - "Baustatik-Wiki Wismar (Hochschule Wismar): 'Direkte und indirekte Lagerung' — direkte Lagerung über Druckspannungen vom lastbringenden ins lasttragende Bauteil; indirekte Lagerung mit Aufhängung in die Druckzone."
  - "Wikipedia, Lemma 'Lager (Statik)' (abgerufen 2026-05-14): Lager als „in der Mechanik abstrahierte Verbindungen zwischen einem Starrkörper (Tragwerk) und seiner Umgebung“, mit Wertigkeit und Lagerreaktion."
  - "Recherche-Bericht [intern]."
quellenkonflikt: |
  **Normlücke.** Keine der konsultierten deutschsprachigen Holzbau-
  und Tragwerks-Normen — SIA 260:2013, SIA 261:2020, SIA 265:2021,
  DIN EN 1990:2010-12, DIN EN 1995-1-1:2010-12, DIN 1052:2008-12 —
  enthält eine geschlossene Begriffs-Definition von „Auflager“. Der
  Begriff wird in allen Normen vorausgesetzt und ausschließlich über
  seine Bemessungs- und Klassifikationseigenschaften behandelt
  (Auflagerpressung als Querdruck-Nachweis EC5 6.1.5; Schub am
  ausgeklinkten Auflager EC5 6.5; Lagerreaktion in den Lastkombinations-
  Regeln EN 1990/SIA 260).

  Eine geschlossene Begriffs-Definition findet sich ausschließlich
  (i) in der Statik-Lehrbuchliteratur als **rein mechanische**
  Festlegung (Petersen, Schneider/Albert, Mönck/Rug, Blass/Sandhaas,
  Wikipedia „Lager (Statik)“: „abstrahierte Verbindung zwischen
  Starrkörper und Umgebung mit Wertigkeit und Lagerreaktion“) und
  (ii) im **IFC-4.3-Schema** als geschlossene Entitäten-Familie
  (`IfcStructuralConnection` mit den Subtypen Point/Curve/Surface plus
  `IfcBoundaryCondition.AppliedCondition` pro Freiheitsgrad). Beide
  geschlossenen Definitions-Linien sind primär mechanisch; sie tragen
  die geometrische Lesart „Auflagefläche zwischen zwei Bauteilen“ nur
  implizit über die Dimensionsklassen Punkt/Linie/Fläche.

  **Geometrische vs. mechanische Lesart.** Im DACH-Holzbau-Korpus
  (Wikipedia „Sparren“, Mönck/Rug Kap. 11, baubeaver.de,
  holzbau-system.de, zimmerer-treff.com) wird „Auflager“ durchgängig
  parallel **geometrisch** als die konkrete Auflagefläche des
  aufgelegten auf dem auflagernden Bauteil verwendet (z. B. „Pfetten
  sind die waagerechten Auflager, auf denen die Sparren ruhen“). In
  dieser Korpus-Lesart fallen Kerve (als Bearbeitung am Sparren),
  Auflagefläche (als ausgezeichnete Polygon-Fläche des Sparren-
  Polyeders) und Auflager (als idealisierte Lagerreaktions-Stelle)
  ohne saubere Abgrenzung zusammen.

  **App-Festlegung — Eigenleistung.** Da keine normative oder
  wissenschaftliche Quelle die Trennung explizit macht, wird sie in
  diesem Glossar als App-eigene Festlegung eingeführt:

  - Die **Kerve** (siehe `hg_kerve.md`) ist die **Bearbeitung** am
    Sparren-Polyeder — eine partitive subtraktive Modifikation. Sie
    ist **nicht** das Auflager.
  - Die **Auflagefläche** ist eine ausgezeichnete **Polygon-Fläche**
    des Bauteil-Polyeders (zum Beispiel die Kerv-Sohle = Bleischnitt-
    Fläche, oder die ebene Stirnfläche eines Stützenfußes), die nach
    Einbau bündig mit der Trägerfläche des auflagernden Bauteils
    liegt. Sie ist die **geometrische Manifestation** des Auflagers
    im gestützten Bauteil. Die Auflagefläche ist im aktuellen Glossar
    nicht als eigener Eintrag geführt; sie wird im
    Auflager-Tupel über ihre Trägerfläche referenziert.
  - Das **Auflager** (dieser Eintrag) ist die **Idealisierung des
    Stützungsorts**: ein Aggregat aus geometrischer Manifestation
    (Punkt-, Linien- oder Flächenort in W), Inzidenz zu genau einem
    gestützten Bauteil, gestützt-durch-Relation (Baugrund oder ein
    weiteres tragendes Bauteil) und Wertigkeit pro Freiheitsgrad
    (sechs Komponenten im 3D). Das Auflager ist Bestandteil der
    Auflager-Menge A des Tragwerks-Tupels (B, V, A, L) nach
    `hg_tragwerk.md` und entspricht der IFC-Familie
    `IfcStructuralConnection` plus `IfcBoundaryCondition`.

  Diese App-Festlegung ist **konsistent** mit allen konsultierten
  Quellen — die Korpus-Sprache fasst die drei Schichten lediglich
  nicht auseinander, widerspricht aber der getrennten Modellierung
  nicht.

  **Begriffstyp.** `aggregat` ist eindeutig (analog `verbindung`,
  `tragwerk`, `dach`): das Auflager trägt eine eigene UUID, hat
  eigene partitive Bestandteile (geometrische Manifestation,
  Wertigkeit pro Freiheitsgrad) und eigene Konsistenzbedingungen
  über der Komposition (Bauteil-Inzidenz, Dimensionsverträglichkeit
  zwischen geometrischer Form und Boundary-Condition-Typ). Ein
  zuvor erwogener Oberbegriff `bauteil_aggregat` ist ausdrücklich
  nicht mehr geplant (siehe `hg_tragwerk.md`-Quellenkonflikt);
  `oberbegriff: null` bleibt analog zu `verbindung`.

  **Synonyme und abgelehnte Benennungen.** „Lager“ und „Stützung“
  sind im DACH-Korpus belegt und werden als Synonyme geführt;
  „Anschluss“ und „Knoten“ werden abgelehnt, weil sie in
  `hg_verbindung.md` bereits als Verbindungs-Synonyme reserviert
  sind und auf die Anschluss-/Bemessungs-Seite (EC5 Kap. 8) zielen,
  nicht auf die Tragwerks-Seite (EC5 Kap. 5, Lagerreaktion).
  „Sparrenfuß“ ist nur eine geometrische Spezialisierung
  („Sparrenfuß ist die Stelle, an der ein Sparrenauflager sitzt“)
  und keine Auflager-Hauptbenennung. Englische Pendants („support“,
  „bearing“, „seat“, „saddle“) sind in der Hauptdefinition nicht
  zulässig. „Mauerbank“/„Mauerlatte“ kollidieren mit der
  `fusspfette`-Synonymie und bezeichnen Bauteile, nicht Auflager.

  **Indirekte Lagerung.** Im Holzbau wird zusätzlich zwischen
  direkter Lagerung (Auflagerkraft über Druckspannungen vom
  lastbringenden ins lasttragende Bauteil, typischer Sparrenfuß auf
  Pfette) und indirekter Lagerung (lastbringendes Bauteil bindet
  seitlich ein, Aufhängung in die Druckzone, Querzugverstärkung)
  unterschieden. Diese Unterscheidung wird im Auflager-Tupel als
  optionales Klassifikations-Merkmal `lagerungsart`
  ({direkt, indirekt}) geführt und im Erläuterungsblock erklärt.

  **BTLx.** Das design2machine-Schema BTLx kennt **keine eigene
  Auflager-Entität**; Auflagerbezüge erscheinen dort implizit über
  Processings und Part-Inzidenzen — analog zur Verbindung
  (siehe `hg_verbindung.md`-Quellenkonflikt). IFC 4.3 ist der
  einzige Industriestandard mit expliziter Auflager-Entitäten-Familie.
---

## Prosa-Definition

Ein **Auflager** ist ein Aggregat aus einer geometrischen
Manifestation (Punkt-, Linien- oder Flächenort im
Weltkoordinatensystem) und einer mechanischen Wertigkeit pro
Freiheitsgrad, das genau ein gestütztes Bauteil mit dem Baugrund
oder mit genau einem auflagernden weiteren tragenden Bauteil
inzident verknüpft, eine eigene technische Identität trägt und die
geometrische sowie kinematische Idealisierung der Stützungsstelle
für die Tragwerksberechnung darstellt.

## Mathematische Definition

Sei

- W das Weltkoordinatensystem (siehe `hg_weltkoordinatensystem.md`),
- 𝒰 der UUID-Raum nach `hg_uuid.md`,
- 𝓑 die Menge der Bauteile nach `hg_bauteil.md`,
- 𝓟 die Menge der Polygone nach `hg_polygon.md` (Repräsentation
  einer Polygon-Fläche in ℝ³ mit Ebene und Eckpunktfolge),
- 𝓓:= {0, 1, 2} die Menge der geometrischen Dimensionen
  (0 = Punkt, 1 = Linie, 2 = Fläche),
- 𝓜 die Menge der **geometrischen Manifestationen**

  ```
  𝓜:= { (d, g) ∈ 𝓓 × (ℝ³ ∪ 𝓢 ∪ 𝓟)
       | d = 0 ⇒ g ∈ ℝ³
         d = 1 ⇒ g ∈ 𝓢          (Strecke nach `hg_strecke.md`)
         d = 2 ⇒ g ∈ 𝓟 }
  ```

  also ein Paar aus Dimension und dimensions-passendem
  geometrischem Träger,
- 𝓕:= {fest, frei, federnd(k)} die Menge der **Komponenten-
  Wertigkeiten** je Freiheitsgrad, wobei `federnd(k)` eine
  lineare Federsteifigkeit `k ∈ ℝ₊` trägt
  (translatorisch in N/mm, rotatorisch in N·mm/rad),
- 𝓦:= 𝓕⁶ die Menge der **Auflager-Wertigkeiten** als
  geordnetes 6-Tupel über den Freiheitsgraden
  (Tx, Ty, Tz, Rx, Ry, Rz) im W-System,
- 𝓛𝓐:= {direkt, indirekt, ⊥} die Klassifikation der
  **Lagerungsart** im Sinne der Baustatik-Konvention
  direkt/indirekt; `⊥` für „nicht klassifiziert“,
- 𝓢𝓣:= {baugrund} ∪ 𝒰 die Menge der **Stützungs-Gegenüber**:
  entweder der Baugrund (Welt-Rand) oder die UUID eines
  weiteren tragenden Bauteils.

Dann ist ein **Auflager** das Tupel

```
A:= (uuid, manifestation, gestuetztes_bauteil, gestuetzt_durch,
      wertigkeit, lagerungsart, bezeichnung)
```

mit den Komponenten

- **uuid** ∈ 𝒰: technische Identität des Auflagers als Aggregat,
- **manifestation** = (d, g) ∈ 𝓜: geometrische Form und Träger
  in W (0D Punkt, 1D Linie, 2D Polygon),
- **gestuetztes_bauteil** ∈ 𝒰: UUID des durch das Auflager
  gestützten Bauteils b ∈ 𝓑,
- **gestuetzt_durch** ∈ 𝓢𝓣: Stützungs-Gegenüber (Baugrund oder
  UUID eines weiteren tragenden Bauteils),
- **wertigkeit** = (w_Tx, w_Ty, w_Tz, w_Rx, w_Ry, w_Rz) ∈ 𝓦:
  Komponenten-Wertigkeit pro Freiheitsgrad in W,
- **lagerungsart** ∈ 𝓛𝓐: Klassifikation direkt/indirekt
  (optional, ⊥ zulässig),
- **bezeichnung** ∈ String ∪ {⊥}: freier Anzeigename
  (optional).

### Konsistenzbedingungen

(A1) **Bauteil-Inzidenz**: `gestuetztes_bauteil` ist die UUID
eines existierenden Bauteils im Modell; das Auflager ist
**genau einem** Bauteil zugeordnet (vgl. Tragwerks-Inzidenz-
Bedingung 2 in `hg_tragwerk.md`).

(A2) **Geometrische Inzidenz**: der geometrische Träger g der
Manifestation liegt auf dem Polyeder ∂P(b) des gestützten
Bauteils b oder auf einer ausgezeichneten Polygon-Fläche
desselben, im Toleranzbereich `LAENGE_EPS`. Für d = 0 heißt
das `dist(g, ∂P(b)) ≤ LAENGE_EPS`; für d = 1 muss die
Strecke vollständig auf ∂P(b) liegen; für d = 2 muss das
Polygon eine Teilfläche einer Polyeder-Face von b sein
(oder mit ihr im `LAENGE_EPS`-Sinn übereinstimmen).

(A3) **Stützungs-Disjunktheit**: falls
`gestuetzt_durch` ∈ 𝒰, gilt
`gestuetzt_durch ≠ gestuetztes_bauteil` (ein Bauteil stützt
sich nicht selbst).

(A4) **Dimensionsverträglichkeit Wertigkeit ↔ Manifestation**:
die Wertigkeit muss mit der geometrischen Dimension d der
Manifestation kompatibel sein in dem Sinne, dass mindestens ein
translatorischer Freiheitsgrad gesperrt ist (sonst wäre das
Auflager keine Stützung). Formal:

```
∃ i ∈ {Tx, Ty, Tz}: w_i ≠ frei.
```

Die rotatorischen Komponenten dürfen für d = 0 (Punkt-
Auflager) konstruktiv nicht gleichzeitig alle gesperrt sein
**außer** im Spezialfall einer expliziten 6-fachen Einspannung
(z. B. eingespannter Stützenfuß im Beton-Köcher); für d ∈ {1, 2}
sind weitere Sperrungen kinematisch zulässig.

(A5) **Konsistenz mit Lagerungsart**: falls
`lagerungsart = direkt`, muss die Manifestation auf einer
**Druck-belasteten Bauteil-Fläche** liegen (Polyeder-Face mit
ausgerichteter Innen-Normale gegen die Lasteinleitungsrichtung);
falls `lagerungsart = indirekt`, ist die Manifestation typisch
eine seitliche Anbindung mit Aufhängungs-Pfad. Diese Bedingung
ist **zugesichert**, nicht formal geprüft.

(A6) **Toleranz-gestützte Identität**: zwei Auflager
a₁ ≠ a₂ am selben Bauteil dürfen identische geometrische
Manifestationen tragen nur, wenn sich ihre Wertigkeiten
unterscheiden; eine triviale Duplizierung (gleiche
Manifestation **und** gleiche Wertigkeit) ist unzulässig.

## Wohldefiniertheit

- **Existenz**: für jeden konkreten Stützungs-Ort eines
  Bauteils lässt sich das obige Tupel erfassen. Mindest-
  konfiguration: ein Sparrenfuß auf einer Fußpfette als
  Punktauflager (d = 0, g = Schwerpunkt der Kerv-Sohle in W,
  Wertigkeit = (fest, fest, fest, frei, frei, frei),
  lagerungsart = direkt, gestuetzt_durch = UUID der Fußpfette).
- **Eindeutigkeit der Identität**: die UUID des Auflagers ist
  unabhängig von der UUID seines gestützten Bauteils und von
  den UUIDs anderer beteiligter Bauteile. Mehrere Auflager
  können am selben Bauteil und am selben Stützungs-Gegenüber
  sitzen (Mehrfeld-Träger mit zwei Pfettenauflagern auf
  derselben Pfette).
- **Mehrfach-Auflagerung eines Bauteils**: zulässig — ein
  Sparren hat typisch zwei Auflager (Fuß- und Firstauflager
  bzw. Fuß- und Mittelpfettenauflager). Jedes Auflager ist eine
  eigene Aggregat-Instanz mit eigener UUID.
- **Geometrische Repräsentanten**: für d = 2 ist die Manifestation
  durch ihr Polygon repräsentiert; verschiedene parametrisierte
  Repräsentationen desselben geometrischen Polygons
  (Eckpunktrotation, kombinatorisch äquivalent) führen auf
  dasselbe Auflager. Die Wohldefiniertheit unter Eckpunkt-
  Permutation folgt direkt aus der Polygon-Definition in
  `hg_polygon.md`.
- **Wertigkeit als 6-Tupel im W-System**: die Komponenten beziehen
  sich auf die Welt-Achsen (Tx ∥ e_x_W, …). Die Übersetzung in
  ein lokales Auflager-Koordinatensystem (z. B. mit
  Normalenrichtung der Manifestations-Fläche als ausgezeichneter
  Achse) ist eine abgeleitete Größe und nicht Teil der
  primären Definition.
- **Federsteifigkeiten**: `federnd(k)` mit `k ∈ ℝ₊`; `k = 0`
  ist `frei`, `k = ∞` ist `fest`. Die kontinuierliche
  Parametrisierung ist eine Verallgemeinerung der diskreten
  Klassifikation fest/frei und entspricht der IFC-Logik
  (`IfcBoundaryCondition` mit `IfcLinearStiffness`).
- **Geometrische und mechanische Lesart**: die geometrische
  Manifestation und die mechanische Wertigkeit sind **getrennte
  Felder** des Aggregats; die App führt sie als zwei unabhängige
  Achsen, konsistent mit der IFC-Trennung von
  `IfcStructuralConnection` (Dimension) und
  `IfcBoundaryCondition` (Wertigkeit). Damit ist die in der
  Korpus-Sprache verwischte Drei-Schichtung Bearbeitung /
  Auflagefläche / Auflager im App-Modell durchsetzbar.
- **Nicht-Zirkularität**: die Definition stützt sich auf die
  bereits definierten Begriffe `bauteil`, `polyeder`, `polygon`,
  `punkt`, `vektor`, `einheitsvektor`, `uuid`,
  `weltkoordinatensystem`, `toleranzen`. Sie verweist auf
  `kerve`, `bearbeitung`, `verbindung`, `tragwerk` ausschließlich
  abgrenzend (Frontmatter-Feld `abgrenzung_zu`).

## Erläuterung (nicht normativ)

### Drei-Schichten-Trennung: Bearbeitung — Auflagefläche — Auflager

In der App werden drei begriffliche Schichten am selben
physischen Sparrenfuß-Punkt sauber getrennt:

| Schicht | Glossarbegriff | Lebenszyklus | Beispiel am Sparrenfuß |
|---|---|---|---|
| **Bearbeitung** (geometrische Modifikation am Bauteil) | `kerve` (Spezialfall einer `bearbeitung`) | Bauteil-gekoppelt (partitiv) | zweiflächiger Einschnitt am Sparren mit Sohle und Senkel |
| **Auflagefläche** (Polygon-Face am Bauteil-Polyeder, der nach Einbau auf der Trägerfläche liegt) | derzeit kein eigener Eintrag; im Auflager-Tupel als Polygon-Manifestation referenziert | Bauteil-gekoppelt (folgt aus Polyeder + Bearbeitung) | die Kerv-Sohle (Bleischnitt-Fläche) als Polygon-Face |
| **Auflager** (Idealisierung der Stützung) | dieser Eintrag | eigene UUID; Tragwerks-Bestandteil | Punkt- oder Flächenauflager mit Wertigkeit (fest, fest, fest, frei, frei, frei) am Schwerpunkt der Kerv-Sohle |

Die Korpus-Sprache („die Kerve ist das Auflager des Sparrens“)
fasst diese drei Schichten zusammen; das App-Modell trennt sie,
weil sie in unterschiedlichen Lebenszyklus-Klassen leben (die
Kerve gehört zum Bauteil; das Auflager gehört zum Tragwerk) und
unterschiedliche Information tragen (die Kerve trägt geometrische
Form und Bemessungs-Bezug zur Querschnittsschwächung; das
Auflager trägt Wertigkeit und Lastpfad-Ende).

### Auflagerwertigkeits-Klassifikation

Die Klassifikation der Wertigkeit folgt der Statik-Lehrbuch-
Tradition. Im **ebenen** Fall (zwei Translationen Tx, Ty plus
eine Rotation Rz) ergeben sich drei Standard-Klassen:

| Bezeichnung | Wertigkeit (eben) | Gesperrte FHG | Reaktionen |
|---|---|---|---|
| Loslager / Gleitlager | 1 | 1 Translation | 1 Kraft |
| Festlager / Gelenklager | 2 | 2 Translationen | 2 Kräfte |
| Feste Einspannung | 3 | 2 Translationen + 1 Rotation | 2 Kräfte + 1 Moment |

Im **räumlichen** Fall (drei Translationen, drei Rotationen)
entsteht analog eine 6-stufige Skala bis zur 6-fachen
Einspannung. Die App-Wertigkeit ist als 6-Tupel
(Tx, Ty, Tz, Rx, Ry, Rz) modelliert; eine Komponente kann
`fest`, `frei` oder `federnd(k)` sein. Die Reduktion auf den
ebenen Fall ist eine abgeleitete Sicht und gehört in die
Bemessungs-Schicht (`statisches_system`).

### Geometrische Dimension der Manifestation

Analog zur IFC-Familie `IfcStructuralPointConnection /
CurveConnection / SurfaceConnection` trägt das App-Auflager die
geometrische Dimension d ∈ {0, 1, 2} der Manifestation:

| Dimension | Beispiele im Holzbau |
|---|---|
| 0 — Punkt | Stützenfuß-Knoten, einzelner Sparrenfuß-Schwerpunkt, Pendelstützen-Auflager |
| 1 — Linie | Linienlager eines Trägers auf einer Mauerkrone, Auflager-Linie eines Plattenrandes |
| 2 — Fläche | Bodenplatte auf Erdreich, Brettsperrholz-Wand auf Streifenfundament, Sparrenauflage als Bleischnitt-Fläche |

Die Wahl der Dimension ist Modellierungs-Entscheidung; die App
erlaubt für denselben Sparrenfuß sowohl die Punkt-Idealisierung
(Schwerpunkt der Kerv-Sohle) als auch die Flächen-Idealisierung
(die Kerv-Sohle selbst als 2D-Polygon). Beide sind valide
geometrische Manifestationen desselben physischen Stützungs-
Orts; sie unterscheiden sich in der Aussage zur Auflagerpressung
(EC5 6.1.5: die Flächen-Idealisierung trägt die Auflagerlänge
explizit, die Punkt-Idealisierung nicht).

### Direkte vs. indirekte Lagerung

Die Baustatik-Konvention unterscheidet:

- **Direkte Lagerung**: die Auflagerkraft wird über
  Druckspannungen vom lastbringenden ins lasttragende Bauteil
  übertragen (Sparrenfuß auf Pfette als Druck rechtwinklig zur
  Faser). Im Holzbau die übliche und mechanisch vorteilhafte
  Variante.
- **Indirekte Lagerung**: das lastbringende Bauteil bindet
  seitlich in das lasttragende ein, ohne dass die vorteilhaften
  Druckspannungen entstehen; die Auflagerkraft muss in die
  Druckzone des tragenden Bauteils eingehängt werden
  (Aufhängungs-Pfad). Im Holzbau über Querzugverstärkung mit
  Vollgewindeschrauben realisiert; vermessungs- und bemessungs-
  technisch aufwendiger.

Die App führt diese Unterscheidung als optionales Klassifikations-
Merkmal `lagerungsart`. Bei `lagerungsart = direkt` muss die
geometrische Manifestation auf einer Polyeder-Face des gestützten
Bauteils liegen, deren Innen-Normale gegen die Lasteinleitungs-
Richtung zeigt (zugesicherte Konsistenzbedingung A5). Bei
`lagerungsart = indirekt` ist die Manifestation typisch eine
seitliche Linien- oder Flächen-Anbindung mit zusätzlich
verlangtem Aufhängungs-Nachweis in der Bemessungs-Schicht.

### IFC-Mapping

| Aspekt | IFC 4.3 Pendant |
|---|---|
| Auflager als Aggregat | `IfcStructuralConnection` (abstrakt) mit GlobalId |
| Manifestation 0D | `IfcStructuralPointConnection` |
| Manifestation 1D | `IfcStructuralCurveConnection` |
| Manifestation 2D | `IfcStructuralSurfaceConnection` |
| Wertigkeit (6 Komponenten) | `IfcBoundaryNodeCondition` / `IfcBoundaryEdgeCondition` / `IfcBoundaryFaceCondition` (pro FHG fest/frei/federnd via `IfcLinearStiffness`) |
| Lagerreaktion | `IfcStructuralReaction` mit `IfcStructuralLoadSingleForce` (Fx, Fy, Fz, Mx, My, Mz) |

Die App-Aggregat-Struktur folgt damit eng dem IFC-4.3-Schema
der Structural-Analysis-Domain. Die geometrische und die
mechanische Achse sind in beiden Modellen orthogonal: das
geometrische Subtyp-Trio Point/Curve/Surface trägt die Dimension;
die Wertigkeit pro Freiheitsgrad trägt die Steifigkeits-
Klassifikation. Das BTLx-Schema (design2machine) kennt keine
eigene Auflager-Entität; Auflagerbezüge sind dort implizit über
Processings und Part-Inzidenzen gegeben.

### Auflager vs. Verbindung — verwandte, nicht-konkurrierende Sichten

Am Sparrenfuß-auf-Pfette-Punkt koexistieren **zwei** App-
Aggregate, die denselben physischen Bauteil-Treffen aus
verschiedenen Sichten erfassen:

- **Verbindung** (`hg_verbindung.md`): das Aggregat aus
  beteiligten Bauteilen + Verbindungsmitteln (Sparrennägel,
  Sparren-Pfetten-Anker) + Nachweisverfahren auf der
  **Anschluss-Bemessungs-Seite** (EC5 Kap. 8, SIA 265
  Anhang A).
- **Auflager** (dieser Eintrag): das Aggregat aus geometrischer
  Manifestation + Wertigkeit auf der **Tragwerks-Seite** (EC5
  Kap. 5, SIA 260 Lastpfad-Ende, IFC Structural Analysis
  Domain).

Beide Aggregate stehen an derselben Stelle in W und können sich
in ihrer Manifestation überlappen (die Kerv-Sohle als
Auflagefläche **ist** zugleich Teil der konstruktiv
verschraubten Verbindung). Sie sind aber **nicht** Synonyme;
die App führt sie als zwei getrennte UUIDs mit gegenseitiger
Referenz (`Auflager.gestuetzt_durch` kann auf ein Bauteil
zeigen, das zugleich Mitglied einer `Verbindung` ist).

## Beziehungen

- **Oberbegriff**: derzeit `null` (analog `verbindung`,
  `tragwerk`). Ein Oberbegriff `bauteil_aggregat` ist
  ausdrücklich nicht mehr geplant; siehe
  `hg_tragwerk.md`-Quellenkonflikt.
- **Bestandteile (partitiv)**:
  - **Geometrische Manifestation** (Dimension d ∈ {0, 1, 2}
    plus geometrischer Träger: `punkt`, `strecke` oder
    `polygon`).
  - **Wertigkeit** (6-Tupel über Freiheitsgraden, je
    {fest, frei, federnd(k)}).
  - **Lagerungsart** (`{direkt, indirekt}`, optional).
  - **Stützungs-Gegenüber** (Baugrund oder UUID eines
    weiteren tragenden Bauteils).
- **Spezialisierungen nach Dimension** (Folgearbeit, falls
  benötigt; im aktuellen Glossar im `manifestation`-Tupel
  aufgelöst): Punktauflager, Linienauflager, Flächenauflager.
- **Spezialisierungen nach Wertigkeit** (Folgearbeit als
  Bemessungs-Schicht-Konzepte): Loslager, Festlager, feste
  Einspannung; sechs-Komponenten-Subklassen.
- **Verwendung**:
  - Bestandteil eines **Tragwerks** (`tragwerk`): in der
    Tupel-Repräsentation (B, V, A, L) ist A die Menge der
    Auflager. Die Tragwerks-Inzidenz-Bedingung 2 verlangt,
    dass jedes Auflager genau einem Bauteil zugeordnet ist.
- **Abgrenzung**:
  - **Kerve** (`kerve`): Bearbeitung am Sparren-Polyeder
    (partitiv, Bauteil-gekoppelt). Die Kerv-Sohle kann
    geometrische Manifestation eines Auflagers **sein**, ist
    aber selbst kein Auflager. Bearbeitung und Auflager sind
    unterschiedliche Lebenszyklus-Schichten.
  - **Bearbeitung** (`bearbeitung`): allgemeiner Oberbegriff
    der Kerve. Bearbeitungen sind subtraktive Modifikationen
    des Bauteil-Polyeders; sie sind nie selbst Auflager.
  - **Verbindung** (`verbindung`): Aggregat auf der
    Anschluss-Bemessungs-Seite. Auflager und Verbindung
    koexistieren am selben physischen Bauteil-Treffen, sind
    aber unterschiedliche Sichten und unterschiedliche
    Aggregate mit eigener UUID.
  - **Verbindungsmittel** (`verbindungsmittel`): einzelnes
    kraftübertragendes Element (Schraube, Nagel, Anker).
    Verbindungsmittel sind nicht Auflager; sie sind
    Bestandteil einer Verbindung.
  - **Tragwerk** (`tragwerk`): das übergeordnete Aggregat,
    dessen A-Komponente die Menge der Auflager ist. Ein
    Auflager ist Bestandteil eines Tragwerks; es ist nicht
    selbst Tragwerk.
  - **Bauteil** (`bauteil`): ein Auflager ist kein Bauteil,
    sondern ein Aggregat, das ein Bauteil mit dem Baugrund
    oder mit einem weiteren tragenden Bauteil verknüpft.
  - **Auflagefläche** (Korpus-Begriff, kein eigener Eintrag
    geplant): die geometrische Manifestation eines
    Flächenauflagers; nicht eigenständiges App-Begriff,
    sondern Manifestations-Komponente innerhalb des Auflager-
    Tupels (siehe Quellenkonflikt-Block, „Auflagefläche“).
  - **Lastfall** (`lastfall`, bereits angelegt): Aggregat aus
    Bemessungssituation, Leiteinwirkung und Begleiteinwirkungen.
    Auflager ist Lastpfad-Ende, Lastfall ist Lastpfad-Anfang;
    beide sind Bestandteile der Tragwerks-Tupel-Komponenten A
    und L.
  - **Statisches System** (`statisches_system`, bereits angelegt):
    die bemessungstechnische Idealisierung des Tragwerks mit
    Punkt-Stab-Modell, Knoten und Auflagerklassen. Auflager
    ist die bauteilbezogene Idealisierung in W; das statische
    System ist eine darüber gelegte Bemessungs-Abstraktion.
  - **Konstruktionsdetail** (`konstruktionsdetail`, bereits
    angelegt): plan-orientiertes Aggregat über Verbindung,
    Auflager und Bearbeitungen am selben Knotenpunkt. Auflager
    ist die statisch-mechanische Sicht, Konstruktionsdetail die
    werkplan-orientierte Sicht am selben Knoten.

## Quellen

**Primär (normativ):**

- ISO 16739-1:2024, „Industry Foundation Classes (IFC) for data
  sharing in the construction and facility management industries
  – Part 1: Data schema“ (IFC 4.3), Structural-Analysis-Domain-
  Entitäten `IfcStructuralConnection`,
  `IfcStructuralPointConnection`, `IfcStructuralCurveConnection`,
  `IfcStructuralSurfaceConnection`, `IfcBoundaryCondition`
  (Subtypen `IfcBoundaryNodeCondition`,
  `IfcBoundaryEdgeCondition`, `IfcBoundaryFaceCondition`),
  `IfcStructuralReaction`, `IfcStructuralLoadSingleForce`.
- DIN EN 1990:2010-12, „Eurocode: Grundlagen der
  Tragwerksplanung“, Abschnitt 1.5.
- DIN EN 1995-1-1:2010-12, „Eurocode 5: Bemessung und
  Konstruktion von Holzbauten – Teil 1-1“, Abschnitte 6.1.5 und
  6.5.
- SIA 260:2013, „Grundlagen der Projektierung von Tragwerken“,
  Schweizerischer Ingenieur- und Architektenverein, Zürich.
- SIA 265:2021, „Holzbau“, Abschnitt 5 und Anhang B.
- DIN 1052:2008-12, „Entwurf, Berechnung und Bemessung von
  Holzbauwerken“, Abschnitt 12.

**Sekundär:**

- Petersen, Chr.: *Statik und Stabilität der Baukonstruktionen.*
  Vieweg, Braunschweig (Lehrbuch-Klassifikation Loslager /
  Festlager / Einspannung).
- Schneider, K.-J.; Albert, A.: *Bautabellen für Ingenieure.*
  26. Aufl., Bundesanzeiger Verlag, Köln 2024.
- Mönck, W.; Rug, W.: *Holzbau – Bemessung und Konstruktion.*
  16. Aufl., Beuth, Berlin 2015, Kap. 11.
- Blass, H. J.; Sandhaas, C.: *Ingenieurholzbau – Grundlagen
  der Bemessung.* KIT Scientific Publishing, Karlsruhe 2016,
  Kap. 5 und 8.
- Natterer, J.; Herzog, T.; Volz, M.: *Holzbau-Atlas.* 4. Aufl.,
  Birkhäuser, Basel 2003.
- Baustatik-Wiki Wismar: „Direkte und indirekte Lagerung“
  (Hochschule Wismar, online).
- Wikipedia, Lemma „Lager (Statik)“ (abgerufen 2026-05-14).

**Korpus (nicht autoritativ):**

- Wikipedia, Lemma „Sparren“ (abgerufen 2026-05-14):
  geometrische Korpus-Lesart „Pfette als waagerechtes Auflager
  der Sparren“.
- holzbau-system.de, Lemma „Sparren“ (abgerufen 2026-05-14).
- baubeaver.de, Lemma „Pfetten“ und Lemma
  „Auflagerpressung“ (abgerufen 2026-05-14).
- zimmerer-treff.com, „Sparrenverbindungen“ (abgerufen
  2026-05-14).
- D.I.E.-Statik, „Sparrenauflager Pfette genagelt“ (abgerufen
  2026-05-14).
- Recherche-Bericht: [intern].
