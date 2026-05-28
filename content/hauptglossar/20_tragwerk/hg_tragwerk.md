---
id: tragwerk
benennung: Tragwerk
synonyme: [Tragsystem, Tragkonstruktion]
abgelehnte_benennungen: [Gerüst, Skelett, "structural frame", "load-bearing structure", "structure"]
oberbegriff: bausystem
begriffstyp: aggregat
voraussetzungen: [bausystem, bauteil, element, verbindung, auflager, lastfall, uuid, punkt, weltkoordinatensystem, toleranzen]
abgrenzung_zu: [bauteil, element, verbindung, bauteilgruppe, bausystem, bauwerk, dach, dachstuhl, konstruktionsdetail, statisches_system, verbindungsmittel, verbinder, verstaerkungselement, dachtragwerk]
status: entwurf
theorie_pflichtig: required
quellen_primär:
  - "SIA 260:2013 'Grundlagen der Projektierung von Tragwerken', Schweizerischer Ingenieur- und Architektenverein, Abschnitt 1 (Geltungsbereich) und Abschnitt 2.1 (Begriffe)."
  - "SIA 265:2021 'Holzbau', Schweizerischer Ingenieur- und Architektenverein, Abschnitt 1 und Abschnitt 4 (Grundlagen der Bemessung von Tragwerken aus Holz)."
  - "DIN EN 1990:2010-12 'Eurocode: Grundlagen der Tragwerksplanung', Abschnitt 1.5 (Begriffe), insbesondere 1.5.1.1 'Tragwerk' (engl. structure) und 1.5.1.7 'Tragwerksanalyse'."
  - "DIN EN 1991-1-1:2010-12 'Eurocode 1: Einwirkungen auf Tragwerke – Teil 1-1: Wichten, Eigengewicht und Nutzlasten im Hochbau'."
  - "DIN EN 1995-1-1:2010-12 'Eurocode 5: Bemessung und Konstruktion von Holzbauten – Teil 1-1', Abschnitt 1.5 und Abschnitt 5 (Tragwerksberechnung)."
  - "DIN 1052:2008-12, Abschnitt 3 (Begriffe), Tragwerk als Gesamtheit der lastabtragenden Bauteile."
quellen_sekundär:
  - "Lignum (Hrsg.): Holzbautabellen HBT, Lignum, Zürich, aktuelle Auflage, Kap. 'Tragwerke und Aussteifung'."
  - "Mönck, W.; Rug, W.: Holzbau – Bemessung und Konstruktion. 16. Aufl., Beuth, Berlin 2015, Kap. 1, 4 und 11 (Dachtragwerke)."
  - "Blass, H. J.; Sandhaas, C.: Ingenieurholzbau – Grundlagen der Bemessung. KIT Scientific Publishing, Karlsruhe 2016, Kap. 1 und 5."
  - "Natterer, J.; Herzog, T.; Volz, M.: Holzbau-Atlas. 4. Aufl., Birkhäuser, Basel 2003, Kap. 'Tragwerke'."
  - "Gerner, M.: Fachwerk – Instandsetzung, Sanierung, Neubau. DVA, 7. Aufl. 2007, Glossar 'Tragwerk' und 'Dachstuhl'."
  - "NIhK Glossary of Prehistoric and Historic Timber Buildings, Lemmata 'roof structure', 'frame'."
quellenkonflikt: |
  Weder SIA 260, SIA 265 noch DIN EN 1990 oder DIN 1052 enthalten eine
  geschlossene formal-mathematische Definition von „Tragwerk"; die
  Normen verwenden den Begriff funktional und beschränken sich auf
  seine Bemessungs- und Klassifikationseigenschaften (Tragsicherheit,
  Gebrauchstauglichkeit, Robustheit). DIN EN 1990 Abschn. 1.5.1.1
  beschreibt das Tragwerk als „planmäßige Anordnung miteinander
  verbundener Bauteile, die so entworfen ist, dass sie Lasten
  aufnimmt und ausreichende Steifigkeit aufweist".

  Im umgangssprachlichen Holzbau wird **Dachstuhl** häufig synonym
  mit **Dachtragwerk** verwendet; die Verwendung schwankt jedoch
  zwischen CH/DE/AT:

  - In der zimmermannssprachlichen Tradition (Gerner, NIhK) bezeichnet
    „Dachstuhl" (`hg_dachstuhl.md`) eng die zimmermannsmäßig gefertigte
    Konstruktion aus Sparren, Pfetten und Stuhlsäulen — ohne
    werks-vorgefertigte Binder (Nagelbinder, BSH-Binder, Fachwerk-
    binder); siehe `hg_dachstuhl.md` Bauart-Prädikat (Bedingung 2).
  - In Lignum HBT und SIA 265 wird „Dachtragwerk" als der allgemeine
    Begriff verwendet, der alle Tragwerks-Varianten umfasst
    (zimmermannsmäßig, Binder, Mischformen).
  - In der Schweizer Praxis ist „Dachstuhl" zwar gebräuchlich, aber
    weniger normfest als „Dachtragwerk" (Lignum, SIA).

  Eigene Festlegung in diesem Glossar (konsistent mit `hg_dach.md`):

  - **Tragwerk** ist der allgemeine, normfeste Sammelbegriff für die
    Gesamtheit der lastabtragenden Bauteile.
  - **Dachstuhl** wird **nicht** als Synonym geführt, sondern in
    `abgrenzung_zu` aufgenommen und in einem späteren eigenen
    Eintrag als enger gefasster Sonderbegriff (zimmermannsmäßiges
    Dachtragwerk) definiert.
  - **Dachtragwerk** ist die fachlich gebräuchliche Spezialisierung
    von Tragwerk im Anwendungsbereich „Dach"; eigener Eintrag folgt.

  Die formale Stabilitätsanalyse (kinematische Bestimmtheit, statische
  Bestimmtheit, Auflagerreaktionen) gehört nicht in dieses Glossar,
  sondern in die spätere Bemessungsschicht der App. Im Glossar wird
  Stabilität nur als zugesicherte Eigenschaft des Tupels (B, V, A, L)
  notiert, nicht als formal überprüfbares Prädikat.

  Tragwerk ist konkreter Subtyp von `bausystem` (siehe
  `hg_bausystem.md`): es erfüllt alle Bausystem-Merkmale —
  nicht-exklusive Mitgliedschaft eines Bauteils (ein Sparren ist
  zugleich Mitglied des Tragwerks und kann Mitglied einer
  Dachflächen-Sicht oder eines Aussteifungssystems sein), keine
  kaskadische Lebenszyklus-Bindung (das Entfernen eines Tragwerks
  löscht nicht die Bauteile) und eigene Identität als funktionale
  Klassifikation der Funktion „lastabtragend". `oberbegriff` wird
  daher auf `bausystem` gesetzt.

  Ein zuvor erwogener Oberbegriff `bauteil_aggregat` ist
  ausdrücklich **nicht mehr geplant**. Die ontologische Trennung
  in `bauteilgruppe` (partitive Komposition mit exklusiver
  Mitgliedschaft und kaskadischer Löschung) und `bausystem`
  (funktionale Gruppierung mit nicht-exklusiver Mitgliedschaft und
  ohne kaskadische Löschung) fasst den intendierten Rahmen
  sauberer als ein zusammenfassender Begriff es täte; siehe
  `briefing_aggregations_begriffe.md` für die Begründung. Frühere
  Verweise auf `bauteil_aggregat` in diesem Eintrag sind durch
  `bausystem` bzw. `bauteilgruppe` ersetzt oder gestrichen.

  Begriffstyp: `aggregat` ist eindeutig — das Tragwerk ist eine
  partitive Zusammenfassung mehrerer Bauteile mit Verbindungen und
  Auflagern. Bauteil-Mitgliedschaft am Tragwerk ist
  bauteilgruppen-fremd: nicht-exklusiv, ohne kaskadische Löschung
  (Bausystem-Semantik).
---

## Prosa-Definition

Ein **Tragwerk** ist ein Aggregat lastabtragender Bauteile, das alle
auf ein Bauwerk oder einen Bauwerksteil einwirkenden Lasten
(Eigengewicht, Nutzlasten, Schnee, Wind und gegebenenfalls
Erdbebeneinwirkungen) durch ein System verbundener Bauteile aufnimmt
und über definierte Auflager in den Baugrund oder in andere tragende
Bauteile leitet, wobei das Aggregat im Holzbau aus stab- und/oder
flächenförmigen Holzbauteilen sowie deren Verbindungen besteht.

## Mathematische Definition

Sei

- W das Weltkoordinatensystem (siehe `weltkoordinatensystem`),
- 𝓑 die Menge aller Bauteile im Sinne von `bauteil`,
- 𝓥 die Menge der **Verbindungen** im Sinne von `verbindung`
  (Aggregate aus Bauteilen + Verbindungsmitteln + ggf. Verbindern
  + ggf. Verstärkungselementen + Nachweisverfahren an einem
  Knotenpunkt); 𝓥 ist ausdrücklich **nicht** die Menge der einzelnen
  Verbindungsmittel — diese sind individuelle Element-Instanzen,
  die als Bestandteile in den Verbindungen geführt werden,
- 𝓐 die Menge der Auflager nach `auflager` — Aggregate aus
  Auflagefläche (Polygon am Bauteilpolyeder), Manifestations-Typ
  (Punkt/Linie/Fläche) und Wertigkeit (fest/beweglich/einspannend),
- 𝒰 der UUID-Raum nach `uuid`,
- 𝓛 die Menge der Lastfälle nach `lastfall` (Aggregat aus
  Bemessungssituation, Leiteinwirkung, Begleiteinwirkungen,
  Einwirkungs-Anordnung; gemäss EN 1990/EN 1991 bzw. SIA 260/261).

Dann ist ein **Tragwerk** das Tupel

```
T := (uuid, B, V, A, L)
```

mit

- **uuid** ∈ 𝒰: technischer Surrogatschlüssel des Tragwerks
  (Pflicht, persistent, RFC 9562 v7); externe Referenzen auf das
  Tragwerk gehen ausschließlich auf diese UUID. Übergeordnete
  Aggregate wie `bauwerk` führen Tragwerks-Instanzen als Menge mit
  identitätstragender Mitgliedschaft (`tragwerke ⊂ 𝒯`), die durch
  diese UUID definiert ist.
- **B** ⊂ 𝓑, B endlich, B ≠ ∅: die Menge der lastabtragenden Bauteile,
- **V** ⊂ 𝓥, V endlich: die Menge der Verbindungen zwischen Elementen
  von B,
- **A** ⊂ 𝓐, A endlich, A ≠ ∅: die Menge der Auflager des Tragwerks,
- **L** ⊂ 𝓛, L endlich: die Menge der zu berücksichtigenden
  Lastfälle (zumindest konzeptuell; die quantitative Bemessung
  erfolgt in einer späteren Schicht),

**Element-Menge und Tupel-Wahl.** Die Bauteilmenge B umfasst
ausschließlich Element-Instanzen der Subklasse `bauteil`
(tragend/raumbildend, Querschnittsbemessung nach EC5 Kap. 6).
Die einzelnen Verbindungsmittel-, Verbinder- und Verstärkungs-
element-Instanzen sind nicht in B enthalten, sondern werden
über die Verbindungen v ∈ V (siehe `verbindung`) als deren
Aggregatbestandteile transitiv erfasst. Wer die Gesamt-Element-
Menge des Tragwerks benötigt, bildet

```
E(T) := B ∪ ⋃_{v ∈ V} elemente(v)
```

(mit `elemente(v)` als der Menge aller Element-Bestandteile der
Verbindung v gemäß `verbindung`). E(T) ist eine **abgeleitete**
Größe; das primäre Tupel des Tragwerks bleibt (B, V, A, L), weil
diese vier Mengen die strukturell unterschiedlichen Rollen
(Tragwerksbauteil, Knotenaggregat, Stützung, Einwirkung) sauber
trennen.

und den Konsistenzbedingungen

1. **Verbindungs-Inzidenz**: Jede Verbindung v ∈ V verbindet eine
   nicht-leere Teilmenge B(v) ⊆ B von Bauteilen; isolierte
   Verbindungen ohne Bauteilbezug sind unzulässig.
2. **Auflager-Inzidenz**: Jedes Auflager a ∈ A ist genau einem
   Bauteil b(a) ∈ B zugeordnet (das durch das Auflager gestützte
   Bauteil); nicht zugeordnete Auflager sind unzulässig.
2a. **Auflager-Exklusivität zwischen Tragwerken** (cross-Tragwerk-
   Invariante): Ein Auflager a ∈ A gehört genau einem Tragwerk an.
   In einem Modell mit Tragwerks-Menge 𝒯ᴹ gilt
   ∀ T₁, T₂ ∈ 𝒯ᴹ : T₁.uuid ≠ T₂.uuid ⇒ T₁.A ∩ T₂.A = ∅.
   Diese Bedingung spiegelt `hg_bauwerk.md` Bed. 4 (Auflager-
   Disjunktheit zwischen Tragwerken am selben Bauwerk) auf
   Tragwerks-Seite.
3. **Zusammenhang**: Der ungerichtete Inzidenzgraph G(T) mit
   Knotenmenge B und Kantenmenge { (b₁, b₂) | ∃ v ∈ V :
   {b₁, b₂} ⊆ B(v) } ∪ { (b, a) | a ∈ A, b = b(a) } ist
   zusammenhängend; getrennte Tragwerke werden als getrennte
   Instanzen modelliert.
4. **Stabilitätszusicherung** (qualitativ): Die Konfiguration aus
   B, V und A ist so beschaffen, dass das Tragwerk unter den
   Lastfällen L kinematisch bestimmt oder unbestimmt ist (nicht
   kinematisch verschieblich); für 3D-Tragwerke entspricht dies
   mindestens sechs unabhängigen, nicht-kollinearen
   Auflagerreaktions-Komponenten oder einem gleichwertigen
   Stabilitätssystem. Diese Bedingung ist im Glossar **zugesichert**,
   nicht formal überprüft; der formale Nachweis ist Aufgabe der
   Bemessungs-Schicht (`statisches_system`).
5. **Lastpfad-Vollständigkeit** (qualitativ): Für jeden Lastfall
   ℓ ∈ L existiert ein Lastpfad von jeder Lasteinleitungsstelle
   über Elemente von B und V zu mindestens einem Auflager in A.
   `hg_lastfall.md` Bed. L3 (Inzidenz-Vollständigkeit) garantiert
   die Einwirkungs-Bauteil-Inzidenz; tragwerk-Bed. 5 ergänzt die
   Pfad-Existenz vom inzidierten Bauteil zum Auflager. Auch diese
   Bedingung ist zugesichert, nicht formal überprüft.
6. **Mischungsverbot pro Verbindung** (SIA 265 Anhang A,
   formuliert in `verbindung`): Innerhalb einer einzelnen Verbindung
   v ∈ V dürfen verschiedene Verbindungsmittel-Wirkungsmechanismen
   nicht ohne Nachweis kombiniert werden (z. B. Nagelung +
   Verleimung; Stabdübel + Versatz). Diese Konsistenzbedingung wirkt
   pro Verbindung und ist im Glossareintrag `verbindung`
   formalisiert; im Tragwerk gilt sie transitiv für alle v ∈ V.

Die **geometrische Punktmenge** des Tragwerks im
Weltkoordinatensystem ist

```
G_W(T) := ⋃_{b ∈ B} G_W(b) ⊂ ℝ³
```

(Vereinigung der bauteilbezogenen Punktmengen nach `bauteil`).

## Wohldefiniertheit

- **Existenz**: Für jedes konkrete Holzbauwerk lässt sich ein Tragwerk
  als Tupel (B, V, A, L) erfassen. Mindestkonfiguration: |B| = 1,
  |V| = 0, |A| = 1, |L| = 1 (z. B. ein einzelner Stabbauteil mit einem
  Festeinspannungs-Auflager und Eigengewicht als einzigem Lastfall).
- **Nicht-Eindeutigkeit der Komposition**: Ein Bauwerk kann mehrere
  getrennte Tragwerke enthalten (z. B. ein Hauptdach-Tragwerk und ein
  unabhängig getragenes Vordach-Tragwerk). Jede zusammenhängende
  Komponente des Inzidenzgraphen ist eine eigene Tragwerks-Instanz.
- **Eindeutigkeit der Komponentenzuordnung**: B, V, A, L sind als
  Mengen unsortiert; alle Aussagen über das Tragwerk sind invariant
  unter Permutation der Elemente.
- **Konsistenz mit `bauteil`**: Jedes b ∈ B ist ein Bauteil im Sinne
  von `bauteil` (mit Identität, Lage, Geometrie, Werkstoff). Die
  geometrische Punktmenge G_W(T) ist die Vereinigung der Bauteil-
  Punktmengen.
- **Konsistenz mit `dach`**: Wird ein Tragwerk als Bestandteil eines
  Dachs verwendet (Dachtragwerk), so ist es genau die Komponente T
  des Dach-Tripels (T, 𝒟, A_aufbau) aus `hg_dach.md`. Die in `hg_dach.md`
  zugesicherte Auflagerung der Dachflächen 𝒟 durch Elemente aus T
  wird damit formal nachgereicht: jede Dachfläche D_i ∈ 𝒟 wird durch
  mindestens ein Bauteil b ∈ B getragen.
- **Stabilität nicht formal**: Die Stabilitätszusicherung (Bedingung
  4) ist qualitativ. Eine formale kinematische und statische
  Bestimmtheits-Analyse erfordert das **statische System**
  (Punkt-Stab-Modell mit Auflagerklassen, Federsteifigkeiten,
  Gelenkfreiheiten) und ist Gegenstand der Bemessungs-Schicht. Die
  Trennung ist bewusst: das Glossar beschreibt die **bauteilbezogene
  Realität**, die Bemessungs-Schicht die **idealisierte Modellierung**.
- **Nicht-Zirkularität**: Die Definition verwendet die Primitive
  `punkt`, `vektor`, `weltkoordinatensystem`, `toleranzen` sowie die
  bereits definierten Begriffe `bauteil`, `verbindung`, `bausystem`,
  `auflager`, `lastfall` und `uuid`. Sie verweist auf
  `statisches_system` und `dachtragwerk` als bereits definierte
  bzw. partner-/spezialisierungs-Begriffe.

## Erläuterung (nicht normativ)

Das Tragwerk ist die **lastabtragende Substanz eines Bauwerks**. Es
ist gleichzeitig

- **Bestandteil eines Dachs** (siehe `dach`): das Dachtragwerk ist
  diejenige Tragwerks-Instanz, die die Dachflächen trägt;
- **eigenständiges Konzept**, das auch außerhalb von Dächern
  auftritt: Wandtragwerke (Wände tragen Lasten ab), Deckentragwerke
  (Decken tragen Nutzlasten ab), Bodentragwerke (Bodenplatten,
  Streifenfundamente), Brückentragwerke, Hallentragwerke.

In dieser App liegt der Anwendungsschwerpunkt auf dem
**Dachtragwerk** als der wichtigsten Tragwerks-Klasse im
zimmermannsmäßigen Holzbau.

### Konstruktive Systeme im Holzbau-Dachtragwerk

Im Holzbau haben sich vier statische Hauptsysteme für Dachtragwerke
etabliert (eigene Glossareinträge folgen):

1. **Sparrendach**: Sparrenpaare bilden mit einem horizontalen
   Zugglied (Deckenbalken oder Kehlbalken) ein statisches Dreieck.
   Lastabtrag erfolgt ohne mittige Pfette; die Sparren sind
   geneigte, druck- und biegebeanspruchte Stäbe, das Zugglied nimmt
   den Horizontalschub auf. Klassisches System für mittlere
   Spannweiten und einfache Dachformen.
2. **Pfettendach**: Sparren liegen auf horizontalen **Pfetten**
   (First-, Mittel-/Mittel-, Fuß- bzw. Schwellpfette) auf. Die
   Pfetten leiten die Sparrenlasten in Wände, Stützen oder
   Stuhlsäulen ab. Geeignet für große Spannweiten, unsymmetrische
   Dächer, Gauben und Aufbauten.
3. **Kehlbalkendach**: Erweiterung des Sparrendachs um einen
   horizontalen **Kehlbalken** auf etwa halber Sparrenhöhe, der die
   Sparren gegeneinander aussteift und die Knicklänge halbiert.
   Geeignet für größere Dachneigungen und Spannweiten.
4. **Binderdach**: Vorgefertigte **Binder** (Nagelbinder,
   BSH-Binder, Fachwerkbinder) übernehmen die Tragfunktion in
   regelmäßigen Achsabständen; quer dazu spannen Pfetten und
   Lattung. Klassisches System für große Spannweiten
   (Hallenbau, Industriebau, freitragende Wohngebäude-Dächer).

Mischformen sind verbreitet (z. B. Pfettendach mit Kehlbalken,
Sparrendach mit Aufdoppelung im Firstbereich) und werden in der
Praxis häufiger verwendet als die reinen Lehrbuchsysteme.

### Tragwerk vs. statisches System

Das **Tragwerk** ist die bauteilbezogene Realität: konkrete Sparren,
Pfetten, Binder mit ihren Querschnitten, Materialien und Verbindungen
in W. Das **statische System** ist die idealisierte Modellierung des
Tragwerks für die Bemessung: Punkt-Stab-Modell mit Knoten,
Stabachsen, Gelenkfreiheiten, Auflagerklassen und Steifigkeiten.
Die App stellt das Tragwerk dar; das statische System ist
abgeleitet und Gegenstand späterer Bemessungs-Funktionalität.

### Strukturelle Rolle: `begriffstyp: aggregat` trotz `oberbegriff: bausystem`

Das Tragwerk trägt `begriffstyp: aggregat`, obwohl sein Oberbegriff
`bausystem` als `begriffstyp: relation` geführt wird. Diese Asymmetrie
zwischen `oberbegriff:` und `begriffstyp:` ist zulässig und ausdrücklich
beabsichtigt (siehe `_KONVENTIONEN.md` Sektion 3, Erläuterung zu
`relation`, sowie `hg_bausystem.md`). Die beiden Felder tragen
unterschiedliche Lasten:

- `oberbegriff: bausystem` markiert die **fachliche Verortung**:
  Tragwerk ist eine spezialisierte funktionale Sicht (die Funktion
  „lastabtragend") und erbt von Bausystem die nicht-exklusive
  Mitgliedschaft eines Bauteils sowie die Abwesenheit einer
  kaskadischen Lebenszyklus-Bindung der Bauteile.
- `begriffstyp: aggregat` markiert die davon abweichende **strukturelle
  Rolle**: das Tragwerk hat eine eigene UUID, eigene partitive
  Bestandteile (Verbindungen, Auflager, Lastfälle) und eigene
  Konsistenzbedingungen über der Komposition (Verbindungs-Inzidenz,
  Auflager-Inzidenz, Zusammenhang des Inzidenzgraphen,
  Lastpfad-Vollständigkeit). Diese Substanz ist im reinen Bausystem
  nicht vorgesehen.

Daraus folgt: Tragwerk-Mitgliedschaft eines Bauteils bleibt
bausystem-konform (nicht-exklusiv, ohne kaskadische Bauteil-Löschung),
während die zusätzlichen Tragwerk-eigenen Mengen (Verbindungen,
Auflager, Lastfälle) die Aggregat-Substanz tragen.

## Beziehungen

- **Oberbegriff**: `bausystem`. Tragwerk erfüllt alle drei
  Bausystem-Merkmale: nicht-exklusive Mitgliedschaft eines
  Bauteils (ein Sparren ist zugleich Tragwerksmitglied und kann
  Mitglied einer Dachflächen-Sicht oder eines
  Aussteifungssystems sein), keine kaskadische
  Lebenszyklus-Bindung (das Entfernen des Tragwerks löscht nicht
  die Bauteile) und eigene Identität als funktionale
  Klassifikation („lastabtragend"). Ein zuvor erwogener
  Sammelbegriff `bauteil_aggregat` ist nicht mehr geplant; siehe
  Quellenkonflikt-Block.
- **Bestandteile (partitiv)**:
  - **Bauteile** (`bauteil`): die lastabtragenden Stab- und
    Flächenbauteile (Sparren, Pfetten, Binder, Kehlbalken,
    Stützen, Streben, Schwellen, Rähme, Schalungen, BSP-Elemente).
  - **Verbindungen** (`verbindungsmittel`, `anschluss`; eigene
    Einträge folgen): Nägel, Schrauben, Bolzen, Stabdübel,
    Klammern sowie zimmermannsmäßige Verbindungen (Zapfen,
    Versatz, Blatt, Schwalbenschwanz).
  - **Auflager** (`auflager`, bereits angelegt): Aggregate aus
    Auflagefläche (Polygon am Bauteilpolyeder), Manifestations-Typ
    (Punkt/Linie/Fläche) und Wertigkeit (fest/beweglich/einspannend).
  - **Lastfälle** (`lastfall`, bereits angelegt): Aggregat aus
    Bemessungssituation, Leiteinwirkung, Begleiteinwirkungen,
    Einwirkungs-Anordnung; gemäss EN 1990/EN 1991 bzw. SIA 260/261.
- **Spezialisierungen nach Anwendungsbereich** (eigene Einträge
  folgen):
  - **Dachtragwerk** (`dachtragwerk`): Tragwerk, das die
    Dachflächen eines Daches trägt. Im Anwendungsschwerpunkt der
    App.
  - **Wandtragwerk** (`wandtragwerk`, Folgearbeit): Tragwerk einer
    Wand (Pfostenwand, Ständerwand, Riegelwerk, BSP-Wand).
  - **Deckentragwerk** (`deckentragwerk`, Folgearbeit): Tragwerk
    einer Decke (Balkenlage, BSP-Decke, Holz-Beton-Verbunddecke).
  - **Bodentragwerk** (`bodentragwerk`, Folgearbeit): Tragwerk
    einer Bodenkonstruktion (Schwellen, Lagerhölzer auf Fundament).
- **Konstruktive Subtypen** (eigene Einträge folgen, im Body
  erläutert; verortet **unter `dachstuhl`** bzw. unter dem
  künftigen `binderdach`-Aggregat, nicht direkt unter `tragwerk`):
  - **Sparrendach** (`sparrendach`) — Dachstuhl-Bauart
  - **Pfettendach** (`pfettendach`) — Dachstuhl-Bauart
  - **Kehlbalkendach** (`kehlbalkendach`) — Dachstuhl-Bauart
  - **Binderdach** (`binderdach`) — Geschwister-Aggregat zum
    Dachstuhl unter dem künftigen `dachtragwerk`
- **Verwendung**:
  - Bestandteil eines **Dachs** (`dach`, partitive Beziehung): das
    Tragwerk ist die T-Komponente des Dach-Tripels (T, 𝒟, A).
  - Bestandteil eines **Bauwerks** (`bauwerk`): jedes Tragwerk
    gehört modellseitig genau einem Bauwerk an. Die Mitgliedschaft
    ist über `bauwerk.tragwerke ⊂ 𝒯` (identitätstragende Menge mit
    `tragwerk.uuid` als Primärschlüssel) ausgedrückt; analog zur
    `IfcRelAggregates`-Beziehung zwischen `IfcFacility` und
    Tragwerks-Pendants in IFC 4.3.
- **Abgrenzung**:
  - **Bauteil** (`bauteil`): einzelner Bestandteil; das Tragwerk
    ist eine Komposition mehrerer Bauteile, kein einzelnes Bauteil.
  - **Bauteilgruppe** (`bauteilgruppe`): orthogonale
    Aggregat-Ontologie, partitive (exklusive) Komposition mit
    kaskadischer Lebenszyklus-Bindung. Tragwerk ist *keine*
    Bauteilgruppe — Bauteile dürfen gleichzeitig
    Tragwerksmitglied und Mitglied weiterer Sichten (z. B.
    Dachfläche, Aussteifungssystem, Lieferlos) sein.
  - **Bausystem** (`bausystem`): jetzt der Oberbegriff von
    Tragwerk; alle Bausystem-Eigenschaften (nicht-exklusive
    Mitgliedschaft, keine kaskadische Löschung, funktionale
    Klassifikation) gelten auch für Tragwerk. Verweis statt
    Abgrenzung — siehe „Oberbegriff" oben.
  - **Bauwerk** (Gebäude, Brücke, Halle als Ganzes): die
    übergeordnete Einheit; ein Bauwerk kann **mehrere** Tragwerke
    umfassen (z. B. Hauptbau-Tragwerk und unabhängiges
    Vordach-Tragwerk).
  - **Dach** (`dach`): das Aggregat aus Tragwerk, Dachflächen und
    Dachaufbau. Das Tragwerk ist Bestandteil eines Daches, nicht
    selbst das Dach.
  - **Dachstuhl**: in der zimmermannssprachlichen Tradition meist
    nur das (zimmermannsmäßig gefertigte) Dachtragwerk, ohne
    Pfettenwände, Nagelbinder, BSH-Binder. Verwendung schwankt
    zwischen CH/DE/AT (siehe Quellenkonflikt). Wegen
    Mehrdeutigkeit **nicht** als Synonym geführt; eigener Eintrag
    `dachstuhl` (= enger gefasstes zimmermannsmäßiges Dachtragwerk)
    folgt.
  - **Konstruktionsdetail** (`konstruktionsdetail`, bereits angelegt):
    lokale, oft mehrere Bauteile mitsamt Verbindungsmitteln
    umfassende Modellierungseinheit (z. B. Sparrenfuß-Anschluss an
    Fußpfette). Ein Detail beschreibt einen lokalen Ausschnitt des
    Tragwerks, ist aber selbst kein Tragwerk.
  - **Verbindungsmittel** (`verbindungsmittel`, eigener Eintrag
    folgt): Nägel, Schrauben, Bolzen, Stabdübel — Bestandteil der
    Verbindungs-Menge V eines Tragwerks, aber nicht selbst
    Tragwerk.
  - **Auflager** (`auflager`, bereits angelegt): Aggregat aus
    Auflagefläche, Manifestation und Wertigkeit; Bestandteil der
    Auflager-Menge A eines Tragwerks, aber nicht selbst Tragwerk.
  - **Lastfall** (`lastfall`, bereits angelegt): Aggregat aus
    Bemessungssituation und Einwirkungen; Bestandteil der
    Lastfall-Menge L, aber nicht selbst Tragwerk.
  - **Statisches System** (`statisches_system`, bereits angelegt):
    die idealisierte Modellierung des Tragwerks für die
    Bemessung (Punkt-Stab-Modell mit Knoten, Stabachsen,
    Gelenkfreiheiten, Auflagerklassen). Tragwerk ist die
    bauteilbezogene Realität, statisches System die bemessungs-
    technische Idealisierung. Beide stehen in einer
    Abstraktions-Relation, sind aber **nicht identisch**.

## Implementierungshinweis

Datentyp (Domänen-Schicht, Kotlin, Schicht `domain.bauteil`):

```kotlin
package domain.bauteil

import domain.bauteil.Bauteil
import java.util.UUID

/**
 * Tragwerk: Aggregat lastabtragender Bauteile mit Verbindungen,
 * Auflagern und Lastfällen.
 *
 * Glossar: hg_tragwerk.md
 *
 * Sammelbegriffe Verbindung, Auflager, Lastfall werden in
 * Folgeeinträgen formal definiert; im aktuellen Glossarstand als
 * Platzhalter-Typen geführt.
 */
data class Tragwerk(
    val bauteile: Set<Bauteil>,                  // B, lastabtragend
    val verbindungen: Set<Verbindung>,           // V, eigener Typ folgt
    val auflager: Set<Auflager>,                 // A, eigener Typ folgt
    val lastfaelle: Set<Lastfall> = emptySet()   // L, optional in frühen Stadien
) {
    init {
        // 1. bauteile.isNotEmpty()             → sonst Entartet.LeeresTragwerk
        // 2. auflager.isNotEmpty()             → sonst Entartet.OhneAuflager
        // 3. ∀ v ∈ verbindungen: v.bauteile ⊆ bauteile
        //                                      → sonst Entartet.VerbindungOhneBauteil
        // 4. ∀ a ∈ auflager: a.bauteil ∈ bauteile
        //                                      → sonst Entartet.AuflagerOhneBauteil
        // 5. Inzidenzgraph zusammenhängend     → sonst Entartet.NichtZusammenhaengend
    }

    fun bauteileNach(uuid: UUID): Bauteil? =
        bauteile.firstOrNull { it.uuid == uuid }

    fun istDachtragwerk(): Boolean = /* Klassifikation aus Bauteilrollen */ TODO()
}
```

- **Einheit**: Längen in mm (Double); Winkel intern in Radiant; Lasten
  in den späteren Lastfall-/Bemessungstypen in N, N/m, N/m² (SI).
- **Identität**: Tragwerks-Instanzen führen eine eigene `TragwerkId`
  (UUID, RFC 9562 v7, persistent, Pflicht — mathematische Tupel-
  Komponente, siehe Definitions-Block). Bauteile werden ausschließlich
  über `uuid` referenziert (Foreign-Key-Regel, siehe Memory
  `project_bauteil_identifikation`).
- **Invarianten** (in `init` prüfen, bei Verletzung `Resultat.Fehler`
  bzw. `Entartet`-Variante zurückgeben, niemals Exception werfen):
  1. `bauteile.isNotEmpty()` ⇒ sonst `Entartet.LeeresTragwerk`.
  2. `auflager.isNotEmpty()` ⇒ sonst `Entartet.OhneAuflager`.
  3. Jede Verbindung referenziert ausschließlich Bauteile aus
     `bauteile` ⇒ sonst `Entartet.VerbindungOhneBauteil`.
  4. Jedes Auflager referenziert genau ein Bauteil aus
     `bauteile` ⇒ sonst `Entartet.AuflagerOhneBauteil`.
  5. Der Inzidenzgraph (Knoten = Bauteile + Auflager, Kanten =
     Verbindungen + Bauteil-Auflager-Inzidenzen) ist
     zusammenhängend ⇒ sonst `Entartet.NichtZusammenhaengend`
     (mehrere getrennte Tragwerke werden als getrennte Instanzen
     modelliert).
  6. **Stabilität** (qualitativ, **nicht** in `init` geprüft):
     für 3D-Tragwerke mindestens sechs unabhängige
     Auflagerreaktions-Komponenten oder gleichwertiges
     Stabilitätssystem. Formaler Nachweis durch
     `statisches_system.istStabil()` in der Bemessungs-Schicht.
- **Edge Cases**:
  - **Einzelbauteil-Tragwerk** (|B| = 1, |V| = 0, |A| = 1):
    zulässig (z. B. Kragträger).
  - **Mehrere getrennte Tragwerke an einem Bauwerk**: als
    getrennte `Tragwerk`-Instanzen modellieren, nicht als ein
    einziges Tragwerk mit nicht-zusammenhängendem Inzidenzgraph.
  - **Tragwerk ohne explizite Lastfälle** (Entwurfsstadium vor
    Bemessung): `lastfaelle = emptySet()` zulässig; in der
    Bemessungs-Schicht ist L ≠ ∅ Vorbedingung für die
    Tragsicherheits-Nachweise.
  - **Mischformen** (Pfettendach mit Kehlbalken, BSH-Binder
    kombiniert mit zimmermannsmäßigen Sparren): zulässig; die
    konstruktive Subtyp-Klassifikation (`sparrendach`,
    `pfettendach`, …) ist bei Mischformen **nicht** eindeutig
    und wird in der Domänen-Schicht als Mehrfach-Klassifikation
    oder als „Mischsystem" abgebildet.
  - **Verbindungsmittel-Geometrie**: Nägel, Schrauben usw. werden
    nicht als Bauteile in B geführt (siehe `bauteil`), sondern als
    Bestandteile der Verbindungs-Menge V mit eigener Geometrie
    und Identität.
- **Abgeleitete Eigenschaften** (als Funktionen, keine Felder):
  - `geometrieInWelt(): GeometrieInW` = Vereinigung der
    Bauteil-Punktmengen ⋃_{b ∈ B} G_W(b).
  - `boundingBox(): AABB` = achsenparalleler Hüllquader in W.
  - `inzidenzgraph(): Graph<Bauteil, Verbindung>` = der
    ungerichtete Graph mit Bauteilen als Knoten und Verbindungen
    als Kanten.
  - `auflagerVon(b: Bauteil): Set<Auflager>` = alle Auflager, die
    b stützen.
  - `statischesSystem(): StatischesSystem` = abgeleitete
    Idealisierung für die Bemessung (Folgearbeit).

## Quellen

**Primär (normativ):**

- SIA 260:2013, „Grundlagen der Projektierung von Tragwerken",
  Schweizerischer Ingenieur- und Architektenverein, Zürich.
- SIA 265:2021, „Holzbau", Schweizerischer Ingenieur- und
  Architektenverein, Zürich.
- DIN EN 1990:2010-12, „Eurocode: Grundlagen der
  Tragwerksplanung", Abschnitt 1.5.
- DIN EN 1991-1-1:2010-12, „Eurocode 1: Einwirkungen auf
  Tragwerke – Teil 1-1: Wichten, Eigengewicht und Nutzlasten im
  Hochbau".
- DIN EN 1995-1-1:2010-12, „Eurocode 5: Bemessung und
  Konstruktion von Holzbauten – Teil 1-1: Allgemeines",
  Abschnitt 1.5 und Abschnitt 5.
- DIN 1052:2008-12, „Entwurf, Berechnung und Bemessung von
  Holzbauwerken – Allgemeine Bemessungsregeln und
  Bemessungsregeln für den Hochbau", Abschnitt 3.

**Sekundär:**

- Lignum (Hrsg.): *Holzbautabellen HBT.* Lignum, Zürich,
  aktuelle Auflage.
- Mönck, W.; Rug, W.: *Holzbau – Bemessung und Konstruktion.*
  16. Auflage, Beuth, Berlin 2015.
- Blass, H. J.; Sandhaas, C.: *Ingenieurholzbau – Grundlagen der
  Bemessung.* KIT Scientific Publishing, Karlsruhe 2016.
- Natterer, J.; Herzog, T.; Volz, M.: *Holzbau-Atlas.*
  4. Auflage, Birkhäuser, Basel 2003.
- Gerner, M.: *Fachwerk – Instandsetzung, Sanierung, Neubau.*
  DVA, 7. Auflage 2007.

**Korpus (nicht autoritativ):**

- NIhK: *Glossary of Prehistoric and Historic Timber Buildings.*
- Holzbau Deutschland, Merkblatt „Begriffe und Klassifizierungen
  für den Holzbau" (abgerufen 2026-05-08).
- Wikipedia, Lemmata „Tragwerk" und „Dachstuhl" (abgerufen
  2026-05-08).
