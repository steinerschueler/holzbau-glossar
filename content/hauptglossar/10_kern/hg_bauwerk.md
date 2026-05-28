---
id: bauwerk
benennung: Bauwerk
synonyme: []
abgelehnte_benennungen: [Gebäude, Bauobjekt, Bauanlage, "bauliche Anlage", Konstruktion, Ingenieurbauwerk, Hochbau, Tiefbau, "building", "construction works", "structure", "facility"]
oberbegriff: null
begriffstyp: aggregat
voraussetzungen: [uuid, weltkoordinatensystem, bauteil, tragwerk, bausystem, element, toleranzen]
abgrenzung_zu: [tragwerk, bausystem, bauteil, element, verbindung, bauteilgruppe, dach, gebaeude, ingenieurbauwerk, bauliche_anlage, standort, grundstueck, liegenschaft, hochbau, tiefbau, dachstuhl, konstruktion]
status: entwurf
theorie_pflichtig: required
quellen_primär:
  - "SIA 260:2013 'Grundlagen der Projektierung von Tragwerken', Schweizerischer Ingenieur- und Architektenverein, Abschnitt 2.1 (Begriffe), Definition 'Bauwerk': „Von Bauarbeiten herrührendes Werk, im Allgemeinen bestehend aus Tragwerk und nicht tragenden Bauteilen.“ [einsicht: snippet]"
  - "ISO 6707-1:2020 'Buildings and civil engineering works — Vocabulary — Part 1: General terms', Abschnitt 3.1 'construction works': „everything that is constructed or results from construction operations“; ferner 'building' und 'civil engineering works' als disjunkte Spezialisierungen."
  - "DIN EN 1990:2010-12 'Eurocode: Grundlagen der Tragwerksplanung', Abschnitt 1.5.1.1 'Bauwerk' (construction works); Begriffsapparat unter Verweis auf ISO 6707-1."
  - "ISO 16739-1:2024 'Industry Foundation Classes (IFC) for data sharing in the construction and facility management industries — Part 1: Data schema' (IFC 4.3.2): Entität `IfcFacility` (abstrakt) als Oberbegriff über `IfcBuilding`, `IfcBridge`, `IfcRoad`, `IfcRailway`, `IfcMarineFacility`; Aggregationsbeziehung `IfcRelAggregates` zu `IfcSite` und zu `IfcFacilityPart`. [einsicht: snippet]"
  - "buildingSMART International: 'IFC4.3 Documentation' (Version 4.3.2.0, 2024), Lexical-Einträge `IfcFacility`, `IfcBuilding`, `IfcSite`. [einsicht: snippet]"
  - "Musterbauordnung (MBO 2002) §2, Bauministerkonferenz: Legaldefinitionen 'bauliche Anlage' und 'Gebäude' — zur Abgrenzung gegen den fachsprachlichen Bauwerksbegriff (das deutsche Bauordnungsrecht führt 'Bauwerk' nicht als Legaldefinition). [einsicht: snippet]"
quellen_sekundär:
  - "Lignum (Hrsg.): Holzbautabellen HBT, Lignum, Zürich, aktuelle Auflage, Kap. 'Tragwerke und Aussteifung'."
  - "Mönck, W.; Rug, W.: Holzbau – Bemessung und Konstruktion. 16. Aufl., Beuth, Berlin 2015, Kap. 1 und 4."
  - "Blass, H. J.; Sandhaas, C.: Ingenieurholzbau – Grundlagen der Bemessung. KIT Scientific Publishing, Karlsruhe 2016, Kap. 1 und 5."
  - "Natterer, J.; Herzog, T.; Volz, M.: Holzbau-Atlas. 4. Aufl., Birkhäuser, Basel 2003."
quellenkonflikt: |
  **(1) Hoch-Tier-Konvergenz SIA 260 / ISO 6707-1 / DIN EN 1990.** Die
  drei Hoch-Tier-Normquellen definieren „Bauwerk" inhaltsidentisch:
  alles, was baulich erstellt wird oder von Bauarbeiten herrührt, im
  Allgemeinen bestehend aus einem Tragwerk und nicht tragenden
  Bauteilen. ISO 6707-1 ist die Wurzel; DIN EN 1990 verweist
  ausdrücklich auf ISO 6707-1; SIA 260 §2.1 ist mit der ISO-Lesart
  vollumfänglich kompatibel. Diese Konvergenz wird im Eintrag als
  primäre Norm-Stütze genutzt; die Schweizer SIA-260-Formulierung
  führt sprachlich, da das App-Projekt im Schweizer Holzbau verortet
  ist.

  **(2) DACH-Bauordnungs-Asymmetrie.** Das **deutsche Bauordnungs-
  recht** (MBO §2 und ihm folgende Landesbauordnungen) **kennt keinen
  Legalbegriff „Bauwerk"**. Es operiert mit „baulicher Anlage" (weiter
  Oberbegriff, umfasst auch Zäune, Werbeanlagen, Pflasterungen) und
  „Gebäude" (Subtyp baulicher Anlagen). „Bauwerk" ist im deutschen
  Bauordnungsrecht eine rein **technische**, keine rechtliche
  Kategorie. Die **Schweiz** kennt keinen bundesweiten Baulegalbegriff;
  kantonale Bauordnungen verwenden „Baute" oder „Bauten und Anlagen",
  die IVHB definiert nur geometrische Begriffe (Höhen, Abstände),
  nicht „Bauwerk". In Schweizer Norm-Sprache ist SIA 260 die einzige
  normfeste Quelle für „Bauwerk".

  Konsequenz für diesen Eintrag: die fachsprachliche Definition
  (SIA 260 / ISO 6707-1 / EN 1990) gilt sachlich für CH und DE; die
  rechtssprachliche Asymmetrie wird im Erläuterungsblock erwähnt,
  ist aber nicht definitorisch konstituierend. „Bauliche Anlage" wird
  in `abgrenzung_zu` geführt, nicht synonymisiert.

  **(3) IFC-Anbindung über `IfcFacility`.** Mit IFC 4.3 wurde die
  räumliche Hierarchie 2024 grundlegend umstrukturiert: `IfcFacility`
  (abstrakt) ist Oberbegriff über `IfcBuilding`, `IfcBridge`,
  `IfcRoad`, `IfcRailway`, `IfcMarineFacility`. Damit existiert ein
  präzises IFC-Pendant zum normativen Bauwerks-Oberbegriff; für den
  engeren Subtyp „Gebäude" ist `IfcBuilding` das Pendant. Die
  App-Ontologie spiegelt diese Hierarchie: `bauwerk` ist
  Top-Level-Aggregat, konkrete Subtypen (`gebaeude`,
  `ingenieurbauwerk`) folgen in eigenen Folgeeinträgen, sobald die
  App sie modelliert.

  **(4) Tragwerk ist Teil-Aspekt, nicht Subtyp.** SIA 260 trennt
  explizit „Bauwerk = Tragwerk + nicht tragende Bauteile". Tragwerk
  und Bauwerk stehen in einer **Aggregations-Beziehung** (ein Bauwerk
  hat ein bis mehrere Tragwerke), nicht in einer Vererbungs-Beziehung.
  Die App-Ontologie folgt dem: `tragwerk` trägt `oberbegriff:
  bausystem` (funktional „lastabtragend"), wird vom Bauwerk
  aggregativ enthalten und ist **kein** Subtyp von `bauwerk`. Ein
  Bauwerk kann mehrere Tragwerke umfassen (Haupttragwerk plus
  unabhängiges Vordach-Tragwerk).

  **(5) DIN 1052 als Quelle entbehrlich.** DIN 1052:2008-12 führt
  keinen eigenen Bauwerksbegriff, sondern verweist auf DIN 1055-100
  (inzwischen DIN EN 1990) für bautyp-unabhängige Begriffe. DIN 1052
  ist in `quellen_primär:` dieses Eintrags daher nicht aufgenommen.

  **(6) Eigene Festlegungen.**

  - Top-Level-Stellung: `oberbegriff: null`. Bauwerk ist die Wurzel
    der App-Ontologie über Tragwerken, Bausystemen, Bauteilen,
    Bauteilgruppen und Verbindungen. Ein darüber liegender
    Holzbau-/Bauwesen-Fachbegriff existiert nicht; die in Wikipedia
    angeführte „künstliche Anlage" trägt definitorisch nichts.
  - Begriffstyp `aggregat`: Bauwerk komponiert eigenständige
    Trägerbegriffe (Tragwerke, weitere — nicht tragende — Bauteile,
    Standortbezug) mit eigener UUID-Identität und Konsistenz-
    bedingungen über der Komposition (mindestens ein Tragwerk,
    Standortbezug nicht leer, geometrische Konsistenz aller Bauteile
    in W).
  - Standortbezug (Site-Pendant zu `IfcSite`): im aktuellen
    Glossarstand als Sammelbegriff im mathematischen Tupel geführt
    (analog zum Vorgehen bei `auflager` / `lastfall` in
    `hg_tragwerk.md`). Ein eigener Eintrag `standort` bzw.
    `grundstueck` folgt, sobald die App Georeferenzierung
    (LV95 / WGS84 / EPSG) einführt; siehe Folgearbeiten.
  - Subtypen: `gebaeude` (Hochbau, IFC `IfcBuilding`) und
    `ingenieurbauwerk` (Tiefbau, IFC `IfcBridge`/`IfcRoad`/…) sind
    keine Synonyme, sondern disjunkte Spezialisierungen nach ISO
    6707-1. Eigene Einträge folgen trigger-basiert.

  **(7) Vermerk zu nicht volltext-verifizierten Quellen.** Der
  Wortlaut von SIA 260 §2.1 und DIN EN 1990 §1.5.1.1 wurde aus
  Sekundärquellen erschlossen (Norm-Auszug bei studocu.com, Wikipedia
  „Ingenieurbauwerk", baunormenlexikon.de, bauprofessor.de), die
  konvergent dieselbe Definition belegen. Direkter Zugriff auf die
  paywall-geschützten Norm-Volltexte steht aus. Korrekturrisiko
  gering, weil die ISO-6707-Wurzel inhaltsidentisch ist.
---

## Prosa-Definition

Ein **Bauwerk** ist ein von Bauarbeiten herrührendes, eigenständig
identifizierbares Aggregat mit eigener Identität und festgelegtem
Standortbezug, das ein oder mehrere Tragwerke und die weiteren, nicht
tragenden Bauteile zu einer übergeordneten konstruktiven Einheit
zusammenfasst und in seiner Gesamtheit eine konstruktive oder
infrastrukturelle Funktion erfüllt.

## Mathematische Definition

Sei

- W das Weltkoordinatensystem (siehe `weltkoordinatensystem`),
- 𝒰 der UUID-Raum nach `uuid`,
- 𝒯 die Menge aller Tragwerke im Sinne von `tragwerk`,
- 𝓑 die Menge aller Bauteile im Sinne von `bauteil`,
- 𝒮 die (im aktuellen Glossarstand sammelbegrifflich geführte) Menge
  der **Standortbezüge** — geometrisch verortete Bezugsobjekte des
  Bauwerks-Aufstellungsorts (Geländeschnitt, Liegenschaft,
  Grundstück, Georeferenzierung gegen einen Welt-Bezugsrahmen);
  ein eigener Eintrag `standort` folgt trigger-basiert, sobald die
  App Georeferenzierung modelliert (Folgearbeit; analog zum
  IFC-Pflichtknoten `IfcSite` über `IfcFacility`),
- 𝒩 = String ⊎ {⊥} die Menge der zulässigen freien Bezeichnungen.

Dann ist ein **Bauwerk** das Tupel

```
W_b := (uuid, tragwerke, weitere_bauteile, standort, bezeichnung?)
```

mit

- **uuid** ∈ 𝒰: technischer Surrogatschlüssel des Bauwerks
  (Pflicht, persistent, RFC 9562 v7); externe Referenzen auf das
  Bauwerk gehen ausschließlich auf diese UUID. IFC-Mapping: auf
  `IfcRoot.GlobalId` an der zugehörigen `IfcFacility`-/`IfcBuilding`-
  Instanz.
- **tragwerke** ⊂ 𝒯, tragwerke endlich, tragwerke ≠ ∅: die Menge
  der Tragwerke des Bauwerks. Mindestens ein Tragwerk ist Pflicht
  (ein Bauwerk ohne Tragwerk ist sachlich sinnlos; SIA 260 §2.1:
  „im Allgemeinen bestehend aus Tragwerk und nicht tragenden
  Bauteilen").
- **weitere_bauteile** ⊂ 𝓑, weitere_bauteile endlich: die Menge der
  Bauteile des Bauwerks, die **nicht** Mitglied eines der
  Tragwerke aus *tragwerke* sind (Eindeckungs-, Hüllkonstruktions-,
  Schichtaufbau-Bauteile, nicht tragende Innenwände,
  Bekleidungen). Die leere Menge ist zulässig.
- **standort** ∈ 𝒮: der Standortbezug des Bauwerks (Pflicht; im
  aktuellen Glossarstand mindestens als Lage des Bauwerks-Ursprungs
  in W realisiert; Subtyp/Inhalt durch den zukünftigen Eintrag
  `standort` präzisiert).
- **bezeichnung?** ∈ 𝒩: optionaler humanlesbarer Name des Bauwerks
  (z. B. „Wohnhaus Beispielstrasse 12", „Brücke X").

und den Konsistenzbedingungen

1. **Bauteil-Disjunktheit zwischen Tragwerken und weiteren
   Bauteilen**: Die Tragwerks-Mitgliedschaft und die Mitgliedschaft
   in *weitere_bauteile* sind disjunkt; für jedes Bauteil
   b ∈ B(W_b) gilt entweder b ist Mitglied mindestens eines
   T ∈ tragwerke (lastabtragend, gemäß `tragwerk`-Tupel-Komponente
   B), oder b ∈ weitere_bauteile (nicht tragend), nicht beides. Die
   funktionale Mehrfach-Mitgliedschaft eines Bauteils in mehreren
   **Bausystemen** (`bausystem`, nicht-exklusiv) bleibt davon
   unberührt; sie ist Eigenschaft des Bausystem-Begriffs, nicht der
   Bauwerk-Komposition.
2. **Gesamt-Bauteilmenge**: Die Bauteilmenge des Bauwerks ist
   ```
   B(W_b) := ( ⋃_{T ∈ tragwerke} T.B ) ∪ weitere_bauteile
   ```
   und ist endlich.
3. **Geometrische Konsistenz**: Alle Bauteile b ∈ B(W_b) sind in W
   verortet (ererbt aus `bauteil`); ihre lokalen Bauteil-
   Koordinatensysteme werden über b.lage nach W überführt. Das
   Bauwerk selbst trägt **kein** eigenes lokales Koordinatensystem
   im Sinne einer SE(3)-Transformation; sein geometrischer Bezug ist
   die kollektive Lage der enthaltenen Bauteile in W. Der
   Standortbezug *standort* setzt den Aufstellungsort des Bauwerks
   in einem externen Welt-Bezugsrahmen fest (Georeferenzierung;
   Folgearbeit).
4. **Tragwerks-Disjunktheit der Auflager**: Die Auflager-Mengen
   verschiedener Tragwerke an demselben Bauwerk sind disjunkt
   (ein Auflager gehört genau einem Tragwerk an).
5. **Lifecycle-Eigentümerschaft**: Tragwerke und weitere Bauteile
   sind als Element- bzw. Aggregat-Begriffe lifecycle-unabhängig
   vom Bauwerk im Sinne der `bausystem`-Semantik; der Bauwerk-
   Wegfall (modellseitig) löscht weder die Bauteile noch die
   Tragwerke. Die Bauwerk-Beziehung ist eine **aggregative
   Zuordnung mit eigener Identität**, keine partitive
   Lebenszyklus-Kopplung der enthaltenen Aggregate.

Die **geometrische Punktmenge** des Bauwerks im
Weltkoordinatensystem ist die Vereinigung der bauteilbezogenen
Punktmengen

```
G_W(W_b) := ⋃_{b ∈ B(W_b)} G_W(b) ⊂ ℝ³.
```

## Wohldefiniertheit

- **Existenz**: Für jedes konkrete realisierte oder geplante Bauwerk
  lässt sich das Tupel (uuid, tragwerke, weitere_bauteile, standort,
  bezeichnung?) erfassen. Mindestkonfiguration: |tragwerke| = 1,
  |weitere_bauteile| = 0, standort ≠ ∅, bezeichnung = ⊥ (zulässig
  für ein einfachstes Bauwerk wie eine Brücke aus einem einzigen
  Tragwerk auf einem definierten Standort).
- **Eindeutigkeit der Identität**: Innerhalb eines Modells gilt
  ∀ W₁, W₂ : (W₁ ≠ W₂) ⇒ (W₁.uuid ≠ W₂.uuid). Die Bauwerks-UUID ist
  konstruktionsseitig zu vergeben (UUID v7 nach RFC 9562) und
  persistent über den gesamten Lebenszyklus.
- **Eindeutigkeit der Komponentenzuordnung**: tragwerke und
  weitere_bauteile sind als Mengen unsortiert; alle Aussagen über
  das Bauwerk sind invariant unter Permutation der Mitglieder. Die
  Disjunktheits-Bedingung 1 stellt sicher, dass die Klassifikation
  jedes Bauteils als „tragend" (Mitglied eines Tragwerks) oder
  „nicht tragend" (in weitere_bauteile) eindeutig ist.
- **Unabhängigkeit vom Standort-Subtyp**: Wenn der zukünftige
  `standort`-Eintrag mehrere konkrete Realisierungen erhält
  (georeferenziert nach LV95, nach WGS84, nur als bauwerksrelativer
  Bezug), bleibt die Bauwerk-Definition formal unverändert; die
  Standort-Komponente wird durch den jeweiligen Subtyp konkretisiert,
  ohne die Bauwerk-Tupel-Struktur zu ändern.
- **Konsistenz mit `tragwerk`**: Jedes T ∈ tragwerke ist ein Tragwerk
  im Sinne von `tragwerk` (mit eigenem (B, V, A, L)-Tupel, eigener
  UUID, eigenen Konsistenzbedingungen). Die Bauteilmenge T.B ⊂
  B(W_b) eines jeden Tragwerks ist Teilmenge der Bauwerks-
  Bauteilmenge.
- **Konsistenz mit `bauteil`**: Jedes b ∈ B(W_b) ist ein Bauteil im
  Sinne von `bauteil`; G_W(W_b) ist die Vereinigung der Bauteil-
  Punktmengen.
- **Konsistenz mit `bausystem`**: Bauwerk und Bausystem sind
  unterschiedliche Aggregations-Kategorien: das Bauwerk komponiert
  Tragwerke und weitere Bauteile **mit Disjunktheit** zwischen
  Tragwerks-Mitgliedern und weiteren Bauteilen; das Bausystem ist
  eine **funktionale, nicht-exklusive** Sicht über Bauteilen. Beide
  können koexistieren: ein Bauteil ist genau einmal in einem
  Bauwerk verankert (über sein Tragwerk oder als weiteres Bauteil),
  aber gleichzeitig Mitglied beliebig vieler Bausysteme.
- **Top-Level-Stellung (kein Oberbegriff)**: Das Bauwerk hat im
  Glossar `oberbegriff: null` und steht außerhalb der
  Element-Subklassen-Hierarchie (`element` → Bauteil /
  Verbindungsmittel / Verbinder / Verstärkungselement). Ein Bauwerk
  ist **kein Element** im Sinne von `hg_element.md`, weil es kein
  verbautes Einzelobjekt ist, sondern ein Aggregat über
  Tragwerken, Bauteilen und Standortbezug.
- **Stabilität, Lastpfad und Bemessung**: Die statisch-mechanischen
  Eigenschaften (Stabilität, Lastpfad-Vollständigkeit) sind
  Eigenschaft der enthaltenen Tragwerke (siehe `tragwerk`,
  Bedingungen 4 und 5) und werden im Glossar nicht zusätzlich am
  Bauwerk geprüft. Die Bauwerks-Definition koordiniert die
  Aggregation; die statische Substanz lebt in den Tragwerken.
- **Nicht-Zirkularität**: Die Definition verwendet die Primitive
  `uuid`, `weltkoordinatensystem`, `toleranzen` sowie die bereits
  definierten Begriffe `bauteil`, `tragwerk`, `bausystem` und
  `element`. Sie verweist auf `standort` als noch zu definierenden
  Folge-Begriff — diese Abhängigkeit ist im Frontmatter als
  `abgrenzung_zu` markiert und im Tupel-Definitionsblock
  ausdrücklich als Sammelbegriff vermerkt.

## Erläuterung (nicht normativ)

Das Bauwerk ist der **ontologische Top-Level-Begriff** der App.
Drei Aspekte machen es zu einem eigenständigen Begriff statt einer
bloßen Bauteil-Sammlung:

- **Identität**: ein Bauwerk wird als Ganzes adressiert — für
  Persistenz, Eigentumsbezug, Werkplan-Versionierung, externe
  Mapping-Felder gegen `IfcRoot.GlobalId` der zugehörigen
  `IfcFacility`-/`IfcBuilding`-Instanz.
- **Funktion und Zweck**: ein Bauwerk wird durch seine
  übergeordnete Funktion charakterisiert (Wohngebäude, Brücke,
  Hallenbau, Schleuse). Die Funktion ist im Glossar nicht als
  Pflichtfeld eingeführt, weil sie auf der Subtyp-Ebene
  (`gebaeude`, `ingenieurbauwerk`, jeweils mit eigenem konkreten
  Funktionswert) sauberer aufgehoben ist; das Bauwerk-Tupel selbst
  enthält nur die strukturelle Komposition.
- **Standortbezug**: anders als ein abstraktes Tragwerk hat ein
  Bauwerk einen konkreten Aufstellungsort. Im IFC-Modell entspricht
  dem die Pflicht-Aggregation einer `IfcFacility` unter eine
  `IfcSite`; in der App ist `standort` als Sammelbegriff in der
  Bauwerk-Definition aufgenommen und wird mit der ersten
  Georeferenzierung als eigener Eintrag konkretisiert.

### Vier-Ebenen-Ontologie

In der App-Ontologie steht das Bauwerk an der Spitze einer
Vier-Ebenen-Trennung:

| Ebene       | Glossarbegriff                | IFC-Pendant                                            |
|-------------|-------------------------------|--------------------------------------------------------|
| **Bauwerk** | `bauwerk` (dieser Eintrag)    | `IfcFacility` (abstrakt) / `IfcBuilding` (konkret)     |
| **Tragwerk**| `tragwerk` (lastabtragend)    | lastabtragende `IfcBuiltElement`-Menge / `IfcStructuralAnalysisModel` |
| **Bausystem**| `bausystem` (funktionale Sicht)| `IfcBuildingSystem`                                  |
| **Bauteil** | `bauteil`                     | `IfcElement` (mit Subtypen Beam, Column, Member, Plate)|

Diese Hierarchie folgt SIA 260 §2.1 und ISO 6707-1 §3.1 in der Sache
und IFC 4.3 in der Datenmodell-Repräsentation. Sie ist im
Quellenkonflikt-Block (Punkte 1, 3, 4) ausführlich begründet.

### Bauwerk vs. Tragwerk

SIA 260 trennt sauber: **Bauwerk = Tragwerk + nicht tragende
Bauteile**. Tragwerk ist also ein **Teil-Aspekt** des Bauwerks, kein
Subtyp. Ein Bauwerk kann mehrere Tragwerke umfassen (z. B. ein
Wohngebäude mit Haupttragwerk und unabhängigem Vordach-Tragwerk; eine
Brücke mit Überbau-Tragwerk und Pfeiler-Tragwerken); jedes Tragwerk
ist eine eigene zusammenhängende Tragwerks-Instanz mit eigenen
Auflagern, Verbindungen und Lastfällen.

### Bauwerk vs. Gebäude / Ingenieurbauwerk

„Bauwerk" ist der **Oberbegriff**; „Gebäude" und „Ingenieurbauwerk"
sind disjunkte **Subtypen** nach ISO 6707-1:

- **Gebäude** (`gebaeude`, Folgearbeit): „construction works that has
  the provision of shelter for its occupants or contents as one of
  its main purposes" (ISO 6707-1). IFC-Pendant: `IfcBuilding`.
- **Ingenieurbauwerk** (`ingenieurbauwerk`, Folgearbeit): „civil
  engineering works comprising a structure, such as a dam, bridge,
  road, railway, runway, utilities, pipeline, or sewerage system"
  (ISO 6707-1). IFC-Pendant: `IfcBridge`, `IfcRoad`, `IfcRailway`,
  `IfcMarineFacility`.

Beide Subtypen werden in eigenen Folgeeinträgen geführt, sobald die
App über das erste Tool (Sparrenbearbeitung) hinaus ganze Bauwerke
modelliert. Bis dahin ist „Gebäude" als abgelehnte Benennung des
Bauwerks-Oberbegriffs geführt — ein Wohnhaus ist ein Gebäude, kein
Bauwerk-Synonym, sondern ein Bauwerk-Subtyp.

### Bauwerk vs. „bauliche Anlage" und Rechtssprache

Das **deutsche Bauordnungsrecht** (MBO §2) verwendet „bauliche
Anlage" und „Gebäude" als Legaldefinitionen, „Bauwerk" hingegen
**nicht**. „Bauliche Anlage" ist breiter als „Bauwerk": sie umfasst
auch Zäune, Werbeanlagen, Pflasterungen. Im Glossar wird
„bauliche Anlage" daher als **abgegrenzter** Begriff (`abgrenzung_zu`)
geführt, nicht als Synonym. Eine eigene Anlage `bauliche_anlage` ist
nur dann sinnvoll, wenn die App Bauantragsdaten oder
Baurechts-Compliance modelliert; Folgearbeit niedriger Priorität.

In der **Schweiz** existiert kein bundesweiter Baulegalbegriff;
kantonale Bauordnungen verwenden „Baute" oder „Bauten und Anlagen",
die IVHB definiert geometrische Begriffe (Höhen, Abstände), nicht
„Bauwerk". SIA 260 ist die normfeste Quelle für „Bauwerk" als
technischen Oberbegriff in der Schweiz.

### Bauwerk vs. Dach / Dachstuhl

Ein **Dach** (`dach`) ist ein Bestandteil eines Bauwerks (typisch
eines Gebäudes); es ist nicht selbst ein Bauwerk. In der App-Ontologie
trägt `dach` ein eigenes Aggregat-Tupel (Tragwerk + Dachflächen +
Dachaufbau). Ein **Dachstuhl** (`dachstuhl`, Folgearbeit) ist die
zimmermannssprachliche enge Lesart des Dachtragwerks — also
Bestandteil eines Daches, nicht Synonym für Bauwerk.

### Anwendungsfall des Schwerpunkt-Tools (Sparren mit zwei Kerven)

Im ersten Tool der App (Sparrenbearbeitung) ist das Bauwerk nicht
unmittelbar als Modellobjekt instanziiert; das Tool arbeitet auf der
Bauteil- bzw. Bearbeitungs-Ebene. Das Bauwerk steht als
**ontologischer Anker** für künftige Tools, die ganze Dachgeometrien
oder ganze Gebäudekonfigurationen verwalten (Phase 4 ff.). Die
didaktische Stufung („Haus → Tragwerk → Sparren") wird im
Subglossar-Pendant entfaltet.

## Beziehungen

- **Oberbegriff**: keiner (`oberbegriff: null`). Bauwerk ist die
  Wurzel der App-Ontologie für aggregative Bauwerksstrukturen. Es
  steht außerhalb der `element`-Hierarchie (Bauwerk ist kein
  Element-Subtyp).
- **Bestandteile (partitiv-aggregativ)**:
  - **Tragwerke** (`tragwerk`, Pflicht, mindestens eines): die
    lastabtragenden Aggregat-Bestandteile des Bauwerks.
  - **Weitere Bauteile** (`bauteil`, optional): nicht tragende
    Bauteile (Eindeckung, Hüllkonstruktion, Schichtaufbau,
    Bekleidungen, nicht tragende Innenwände).
  - **Standortbezug** (`standort`, Pflicht; Folgearbeit): der
    Aufstellungsort des Bauwerks; im aktuellen Glossarstand
    sammelbegrifflich geführt, Konkretisierung sobald
    Georeferenzierung modelliert wird.
- **Spezialisierungen** (eigene Einträge folgen, trigger-basiert):
  - **Gebäude** (`gebaeude`, Folgearbeit): Bauwerk mit
    Schutzfunktion (ISO 6707-1 „building"); IFC-Pendant
    `IfcBuilding`.
  - **Ingenieurbauwerk** (`ingenieurbauwerk`, Folgearbeit):
    Bauwerk des Tief-/Verkehrs-/Wasserbaus (ISO 6707-1 „civil
    engineering works"); IFC-Pendant `IfcBridge`, `IfcRoad`,
    `IfcRailway`, `IfcMarineFacility`.
- **Verwendung**:
  - Top-Level-Container für alle Modellinhalte eines konkreten
    Bauvorhabens.
  - Foreign-Key-Ziel von Bemessungs-Nachweisen, Bauantrag-
    Mappings, IFC-Export-Wurzeln.
- **Abgrenzung**:
  - **Tragwerk** (`tragwerk`): Teil-Aspekt des Bauwerks
    (lastabtragend), nicht Synonym, nicht Subtyp. Ein Bauwerk
    enthält **ein bis mehrere** Tragwerke; SIA 260 §2.1.
  - **Bausystem** (`bausystem`): funktionale Sicht über Bauteilen
    mit nicht-exklusiver Mitgliedschaft; Bauwerk ist hingegen
    eine **aggregative Komposition** mit disjunkter Trennung von
    Tragwerks-Mitgliedern und weiteren Bauteilen.
  - **Bauteil** (`bauteil`): einzelner Bestandteil; das Bauwerk
    aggregiert Bauteile entweder mittelbar über Tragwerke oder
    unmittelbar als weitere Bauteile.
  - **Element** (`element`): Wurzel der App-Ontologie für
    **verbaute Einzelobjekte** (Bauteil/Verbindungsmittel/
    Verbinder/Verstärkungselement). Bauwerk ist **kein
    Element-Subtyp**, sondern eine Aggregat-Hierarchie eine
    Stufe darüber.
  - **Verbindung** (`verbindung`): lokales Knoten-Aggregat
    (Bauteile + Verbindungsmittel + Verbinder + Verstärkungen);
    Bestandteil eines Tragwerks, nicht des Bauwerks unmittelbar.
  - **Bauteilgruppe** (`bauteilgruppe`): partitive Aggregat-
    Klasse mit exklusiver Mitgliedschaft und kaskadischer
    Lebenszyklus-Bindung — strukturell anders als das Bauwerk
    (das Bauwerk ist exklusiv für Bauteile, aber ohne
    kaskadische Lifecycle-Kopplung der enthaltenen Aggregate
    `tragwerk`).
  - **Dach** (`dach`): Bestandteil eines Bauwerks (Aggregat aus
    Dachtragwerk, Dachflächen, Dachaufbau), nicht selbst
    Bauwerk.
  - **Dachstuhl** (`dachstuhl`, Folgearbeit): zimmermanns-
    sprachliche enge Lesart des Dachtragwerks; eine Stufe unter
    dem Bauwerk.
  - **Gebäude** (`gebaeude`, Folgearbeit): **Subtyp**, nicht
    Synonym. Ein Wohnhaus ist ein Gebäude, also ein Bauwerk-
    Subtyp.
  - **Ingenieurbauwerk** (`ingenieurbauwerk`, Folgearbeit):
    **Subtyp**, nicht Synonym; Brücken, Tunnel, Dämme,
    Schleusen.
  - **Bauliche Anlage** (`bauliche_anlage`, Folgearbeit niedriger
    Priorität): baurechtlicher Oberbegriff der MBO §2; **breiter**
    als Bauwerk (umfasst auch Zäune, Werbeanlagen, Pflasterungen)
    und auf andere Begriffsebene (rechtlich, nicht technisch).
  - **Standort** (`standort`, Folgearbeit): geometrischer
    Aufstellungsort des Bauwerks; Bestandteil des Bauwerk-Tupels,
    aber eigener Begriff. Konkretisierung sobald Georeferenzierung
    eingeführt wird.
  - **Grundstück** (`grundstueck`, Folgearbeit): liegenschafts-
    rechtliche Einheit; in Schweiz/Deutschland unterschiedlich
    realisiert; nicht Synonym zu Standort, sondern eine
    rechtliche Lesart des Aufstellungsorts.
  - **Liegenschaft** (`liegenschaft`, Folgearbeit): liegenschafts-
    rechtliche Sammelbenennung in CH-Praxis; eigener Eintrag bei
    Bedarf.
  - **Hochbau** / **Tiefbau** (`hochbau`, `tiefbau`,
    Folgearbeit): Klassifikations-Achsen über Bauwerken, keine
    Begriffe für das Bauwerk selbst. Werden als abgelehnte
    Benennungen geführt.
  - **Konstruktion** (`konstruktion`): mehrdeutiger Begriff
    (Konstruktionsweise, Konstruktions-Stand, Tragwerks-
    Konstruktion); im Holzbau eher als Synonym von Tragwerk-
    Konstruktion verwendet. Als abgelehnte Benennung geführt.

## Implementierungshinweis

**Im aktuellen Glossarstand wird ausdrücklich keine Code-Klasse
`Bauwerk` angelegt.** Das erste Tool (Sparren mit zwei Kerven,
Etappe D7/D8) arbeitet auf der Bauteil-/Bearbeitungs-Ebene; eine
Bauwerk-Klasse ist erst sinnvoll, wenn ein Tool ganze
Bauwerkskonfigurationen verwaltet (Phase 4 ff.). Der folgende
Skizzen-Code ist ausschließlich orientierender Implementierungs-
Hinweis.

```kotlin
// SKIZZE — nicht jetzt anlegen.
// Glossar: hg_bauwerk.md

package domain.bauwerk

import domain.bauteil.Bauteil
import domain.bauteil.Tragwerk
import domain.standort.Standort   // eigener Eintrag folgt
import java.util.UUID

/**
 * Bauwerk: Top-Level-Aggregat über Tragwerken, weiteren Bauteilen
 * und Standortbezug. Eigene UUID-Identität; nicht Element-Subtyp.
 *
 * Glossar: hg_bauwerk.md
 * IFC-Pendant: IfcFacility (abstrakt) / IfcBuilding (konkret).
 *
 * Pflichtfelder: uuid, tragwerke (≥ 1), standort.
 * Optionalfelder: weitereBauteile, bezeichnung.
 *
 * Foreign-Key-Regel (siehe Memory project_bauteil_identifikation):
 * externe Referenzen auf das Bauwerk gehen ausschließlich auf
 * `uuid` — nicht auf `bezeichnung`.
 */
data class Bauwerk(
    val uuid: UUID,
    val tragwerke: Set<Tragwerk>,
    val weitereBauteile: Set<Bauteil> = emptySet(),
    val standort: Standort,
    val bezeichnung: String? = null,
) {
    init {
        // 1. tragwerke.isNotEmpty()
        //    → sonst Entartet.BauwerkOhneTragwerk
        // 2. Disjunktheit: weitereBauteile ∩ ( ⋃ tragwerke.B ) = ∅
        //    → sonst Entartet.BauteilDoppeltKlassifiziert
        // 3. Auflager-Disjunktheit zwischen Tragwerken
        //    → sonst Entartet.AuflagerDoppeltZugeordnet
        // 4. standort ist gesetzt (Standort-eigene Invarianten ererbt)
    }

    /** Gesamt-Bauteilmenge B(W_b) = ⋃ tragwerke.B ∪ weitereBauteile. */
    fun bauteile(): Set<Bauteil> =
        tragwerke.flatMap { it.bauteile }.toSet() + weitereBauteile

    fun bauteilNach(uuid: UUID): Bauteil? =
        bauteile().firstOrNull { it.uuid == uuid }
}
```

- **Einheit**: Längen in mm (Double); Winkel intern in Radiant;
  Standort-Georeferenzierung in den späteren `standort`-Typen
  abhängig vom Bezugsrahmen (LV95 in m, WGS84 in Grad).
- **Identität**: `uuid` ist Pflicht und persistent (RFC 9562 v7);
  externe Referenzen auf ein Bauwerk gehen ausschließlich auf diese
  UUID. IFC-Mapping: auf `IfcRoot.GlobalId` der zugehörigen
  `IfcFacility`-Instanz (22-stellig Base64 nach ISO/IEC 9834-8).
- **Invarianten** (im `init`-Block prüfen, bei Verletzung
  `Resultat.Fehler` bzw. `Entartet`-Variante; niemals Exception
  werfen):
  1. `tragwerke.isNotEmpty()` ⇒ sonst
     `Entartet.BauwerkOhneTragwerk` (SIA 260 §2.1).
  2. **Bauteil-Disjunktheit**: für jedes b ∈ weitereBauteile gilt
     b ∉ T.bauteile für jedes T ∈ tragwerke ⇒ sonst
     `Entartet.BauteilDoppeltKlassifiziert`.
  3. **Auflager-Disjunktheit**: die Auflager-Mengen verschiedener
     Tragwerke an demselben Bauwerk sind disjunkt ⇒ sonst
     `Entartet.AuflagerDoppeltZugeordnet`.
  4. `standort` ist gesetzt (Pflichtfeld; sobald `standort` als
     eigener Eintrag mit eigenen Invarianten existiert, ererben
     diese transitiv).
- **Edge Cases**:
  - **Bauwerk mit einem einzigen Tragwerk und keinen weiteren
    Bauteilen**: zulässig (z. B. eine einfache Brücke). Mindestens
    ein Tragwerk; weitere Bauteile dürfen leer sein.
  - **Bauwerk mit mehreren Tragwerken**: zulässig (Hauptgebäude-
    Tragwerk + unabhängiges Vordach-Tragwerk; Brücke mit Überbau-
    Tragwerk und Pfeiler-Tragwerken). Modellseitig getrennte
    `Tragwerk`-Instanzen, am Bauwerk gemeinsam aggregiert.
  - **Bauwerk ohne expliziten Standort**: nicht erlaubt im finalen
    Modell; in frühen Entwurfsstadien kann ein Platzhalter-
    Standort (Bauwerks-Ursprung in W ohne Georeferenzierung)
    geführt werden, der vor IFC-Export aufgelöst sein muss.
  - **Verschachtelung**: Bauwerke werden in der App **nicht**
    verschachtelt (kein Bauwerk-im-Bauwerk). Ein Großbauvorhaben
    mit mehreren Gebäuden auf einem Grundstück wird als
    **mehrere Bauwerks-Instanzen** modelliert, die denselben
    Standort-/Grundstücks-Bezug teilen. (IFC kennt
    `IfcFacilityPart` für längsschnittweise Brückenabschnitte;
    diese Verfeinerung ist Folgearbeit.)
  - **Subtyp-Klassifikation Gebäude vs. Ingenieurbauwerk**: in
    der konkreten Subklasse-Hierarchie (Folgearbeit) zu treffen;
    nicht in der hier definierten Wurzel.
- **Abgeleitete Eigenschaften** (als Funktionen, keine Felder):
  - `bauteile(): Set<Bauteil>` = Gesamt-Bauteilmenge.
  - `geometrieInWelt(): GeometrieInW` = ⋃_{b ∈ bauteile()} G_W(b).
  - `boundingBox(): AABB` = achsenparalleler Hüllquader in W über
    allen Bauteilen.
  - `tragwerkFuer(b: Bauteil): Tragwerk?` = das Tragwerk, dessen
    Mitglied b ist (Null, falls b ∈ weitereBauteile).
- **IFC-Mapping** (Persistenzschicht, je Subklasse explizit zu
  dokumentieren):
  | Bauwerk-Lesart      | IFC-Klasse              |
  |---------------------|-------------------------|
  | Wurzel (abstrakt)   | `IfcFacility`           |
  | Gebäude             | `IfcBuilding`           |
  | Brücke              | `IfcBridge`             |
  | Straße              | `IfcRoad`               |
  | Bahnstrecke         | `IfcRailway`            |
  | Hafen/Schleuse      | `IfcMarineFacility`     |
  - `uuid` → `IfcRoot.GlobalId` der `IfcFacility`-Instanz.
  - `bezeichnung` → `IfcRoot.Name`.
  - `standort` → Aggregations-Beziehung `IfcRelAggregates` zu
    `IfcSite` (IFC-Pflichtknoten ein Bauwerk eindeutig
    georeferenzieren).
  - `tragwerke` → Mengen lastabtragender `IfcBuiltElement`-
    Instanzen innerhalb der `IfcFacility`; gegebenenfalls
    `IfcStructuralAnalysisModel` als analytische Sicht.
- **Bezeichner-Konvention** (CLAUDE.md): Domänen-Klasse heißt
  `Bauwerk` (deutsch, Glossarbegriff); Subklassen heißen `Gebaeude`,
  `Ingenieurbauwerk`.

## Quellen

**Primär (normativ):**

- SIA 260:2013, „Grundlagen der Projektierung von Tragwerken",
  Schweizerischer Ingenieur- und Architektenverein, Zürich,
  Abschnitt 2.1.
- ISO 6707-1:2020, „Buildings and civil engineering works —
  Vocabulary — Part 1: General terms", Abschnitt 3.1.
- DIN EN 1990:2010-12, „Eurocode: Grundlagen der
  Tragwerksplanung", Abschnitt 1.5.1.1.
- ISO 16739-1:2024, „Industry Foundation Classes (IFC) for data
  sharing in the construction and facility management industries
  — Part 1: Data schema" (IFC 4.3.2).
- buildingSMART International: *IFC4.3 Documentation*
  (Version 4.3.2.0, 2024).
- Musterbauordnung (MBO 2002) §2, Bauministerkonferenz.

**Sekundär:**

- Lignum (Hrsg.): *Holzbautabellen HBT.* Lignum, Zürich,
  aktuelle Auflage.
- Mönck, W.; Rug, W.: *Holzbau – Bemessung und Konstruktion.*
  16. Auflage, Beuth, Berlin 2015.
- Blass, H. J.; Sandhaas, C.: *Ingenieurholzbau – Grundlagen der
  Bemessung.* KIT Scientific Publishing, Karlsruhe 2016.
- Natterer, J.; Herzog, T.; Volz, M.: *Holzbau-Atlas.*
  4. Auflage, Birkhäuser, Basel 2003.

**Korpus (nicht autoritativ):**

- Holzbau Deutschland, Merkblatt „Begriffe und Klassifizierungen
  für den Holzbau" (abgerufen 2026-05-14).
- Wikipedia, Lemmata „Bauwerk", „Gebäude", „Ingenieurbauwerk",
  „Hochbau", „Tiefbau" (abgerufen 2026-05-14).
- baunormenlexikon.de, bauprofessor.de — DIN-EN-1990-Begriffs-
  Erläuterungen (abgerufen 2026-05-14).

## Folgearbeit (trigger-basiert)

Konkrete Spezialisierungen und Bestandteile werden definiert, sobald
das jeweilige Tool oder Modellierungs-Schritt sie benötigt:

- **`gebaeude`** — Subtyp „Bauwerk mit Schutzfunktion" (ISO 6707-1
  „building", IFC `IfcBuilding`). Trigger: erste App-Phase, in der
  Wohn-/Geschäftsgebäude über die reine Dach-Modellierung hinaus
  modelliert werden (Geschosse, Raumzellen).
- **`ingenieurbauwerk`** — Subtyp „Bauwerk des Tief-/Verkehrs-/
  Wasserbaus" (ISO 6707-1 „civil engineering works", IFC
  `IfcBridge`/`IfcRoad`/`IfcRailway`/`IfcMarineFacility`). Trigger:
  spätere App-Phase mit Brücken-/Wasserbau-Werkzeugen.
- **`standort`** — geometrischer Aufstellungsort des Bauwerks,
  Site-Pendant zu IFC `IfcSite`. Trigger: erste Georeferenzierung
  der App-Daten (LV95 / WGS84 / EPSG). Löst gleichzeitig die
  Forward-Verweise `lv95` und `wgs84` in
  `hg_weltkoordinatensystem.md` auf.
- **`grundstueck`** / **`liegenschaft`** — liegenschaftsrechtliche
  Begriffe; eigener Eintrag bei Bedarf (z. B. wenn die App
  Liegenschaftsdaten persistiert oder gegen Schweizer Grundbuch-
  oder deutsche Liegenschaftskataster mappt).
- **`bauliche_anlage`** — baurechtlicher Oberbegriff der MBO §2;
  niedrige Priorität. Nur dann, wenn die App Bauantragsdaten oder
  Baurechts-Compliance modelliert.
- **`dachstuhl`** — zimmermannssprachliche enge Lesart des
  Dachtragwerks. Folgearbeit bereits in `hg_tragwerk.md` notiert.
- **`hochbau`** / **`tiefbau`** — Klassifikations-Achsen; eigener
  Eintrag nur, falls in der App eine entsprechende Sichtenklassifikation
  modelliert wird. In der Regel als abgelehnte Benennungen am
  Bauwerks-Eintrag belassen.
- **`konstruktion`** — mehrdeutig; bei Bedarf als eigener Eintrag mit
  Disambiguator (z. B. `konstruktion_geometrisch` /
  `konstruktion_konstruktionsweise`).

Auf Glossar-Konventions-Ebene:

- **Sichtungs-Tabellen-Pflege in `HG_KONVENTIONEN.md` §6.A**:
  Forward-Verweise aus diesem Eintrag (`gebaeude`,
  `ingenieurbauwerk`, `bauliche_anlage`, `standort`, `grundstueck`,
  `liegenschaft`, `hochbau`, `tiefbau`, `dachstuhl`, `konstruktion`)
  in die (A)-Trigger-Liste aufnehmen.
- **`hg_bausystem.md`** und **`hg_dach.md`** tragen `bauwerk`
  in `abgrenzung_zu:` (im selben R-Schritt nachgezogen, in dem
  dieser Eintrag entstand).
