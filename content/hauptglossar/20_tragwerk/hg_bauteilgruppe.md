---
id: bauteilgruppe
benennung: Bauteilgruppe
synonyme: ["zusammengesetztes Element", "Element-Assembly", Bauaggregat]
abgelehnte_benennungen: [Bauteilkomplex, Konstruktion, System, Bausystem, Baugruppe, "assembly", "composite element", "sub-assembly"]
oberbegriff: null
begriffstyp: aggregat
voraussetzungen: [bauteil, uuid, lokales_koordinatensystem, weltkoordinatensystem, polyeder, toleranzen]
abgrenzung_zu: [bauteil, bausystem, verbindung, tragwerk, bearbeitung, element, dach, dachaufbau, konstruktionsdetail]
status: entwurf
theorie_pflichtig: required
quellen_primär:
  - "ISO 16739-1:2024 'Industry Foundation Classes (IFC) for data sharing in the construction and facility management industries — Part 1: Data schema' (IFC 4.3.2), Entität `IfcElementAssembly` (Spezialisierung von `IfcElement`) und Beziehung `IfcRelAggregates`: ein zusammengesetztes Element ist eine eigene, identifizierte Entität mit GlobalId, deren Bestandteile über die exklusive `IfcRelAggregates`-Beziehung partitiv zugeordnet sind; Bestandteile gehören in dieser Beziehung zu genau einem übergeordneten Aggregat. IFC erlaubt die rekursive Verschachtelung von ElementAssemblies."
  - "buildingSMART International: 'IFC4.3 Documentation' (Version 4.3.2.0, 2024), `IfcElementAssembly` mit `PredefinedType` (z. B. ARCH_SEGMENT, BEAM_GRID, BRACED_FRAME, GIRDER, REINFORCEMENT_UNIT, RIGID_FRAME, SLAB_FIELD, TRUSS) und Aggregations-Semantik via `IfcRelAggregates` (Whole/Part-Beziehung mit kaskadischem Lebenszyklus)."
  - "DIN EN 1995-1-1:2010-12 (Eurocode 5), Abschnitt 1.5 (Begriffe) und Abschnitt 9 (Aussteifende Scheiben, zusammengesetzte Bauteile): zusammengesetzte Bauteile (z. B. nachgiebig verbundene Träger) als bemessungstechnische Einheit aus mehreren Holzbauteilen mit definiertem inneren Verbund."
  - "SIA 265:2021 'Holzbau', Abschnitt 5 (Konstruktive Durchbildung): Gauben, Auswechslungen und ähnliche Konstruktionen werden als zusammengehörende Bauteilgruppen behandelt, ohne formale Begriffsdefinition."
quellen_sekundär:
  - "Evans, E.: Domain-Driven Design — Tackling Complexity in the Heart of Software. Addison-Wesley 2003, Kap. 6 'The Life Cycle of a Domain Object', Aggregat (Aggregate) und Aggregat-Wurzel (Aggregate Root): Konsistenz-Grenze, exklusive Mitgliedschaft der Bestandteile, kaskadischer Lebenszyklus, externe Referenzen ausschließlich auf die Wurzel."
  - "Vernon, V.: Implementing Domain-Driven Design. Addison-Wesley 2013, Kap. 10 'Aggregates', insbesondere Abschnitte zur Wahl der Aggregat-Grenze und zur exklusiven Bestandteils-Mitgliedschaft."
  - "Mönck, W.; Rug, W.: Holzbau – Bemessung und Konstruktion. 16. Aufl., Beuth, Berlin 2015, Kap. 11 'Dachtragwerke', Auswechslungen und Gauben als zusammengehörige Konstruktionseinheiten."
  - "Gerner, M.: Fachwerk – Instandsetzung, Sanierung, Neubau. DVA, 7. Aufl. 2007, Glossar (Auswechslung, Gaube, Erker als zusammengesetzte Einheiten)."
  - "Natterer, J.; Herzog, T.; Volz, M.: Holzbau-Atlas. 4. Aufl., Birkhäuser, Basel 2003, Kap. 'Dachformen und Dachaufbauten'."
quellenkonflikt: |
  Keine Holzbau-Norm (SIA 265, DIN 1052, DIN EN 1995-1-1) führt
  einen geschlossenen Oberbegriff für „aus mehreren Bauteilen
  zusammengesetzte konstruktive Einheit mit eigener Identität" als
  Datenmodell-Wurzel ein. Die Normen verwenden konkrete Begriffe
  (Auswechslung, Gaube, Erker, Walm) jeweils funktional und ohne
  formale Aggregat-Spezifikation.

  Die einzige geschlossene, normativ gepflegte Spezifikation für
  Aggregate aus Bauteilen ist ISO 16739-1 (IFC). IFC modelliert
  zwei strukturell verschiedene Aggregations-Mechanismen:

  - `IfcElementAssembly` mit `IfcRelAggregates`: partitive,
    exklusive Komposition mit eigener Identität (Whole/Part).
  - `IfcBuildingSystem` mit `IfcRelAssignsToGroup`: funktionale,
    nicht-exklusive Gruppierung (Sicht).

  Diese Trennung wird hier ausdrücklich übernommen: `bauteilgruppe`
  entspricht dem ersten Mechanismus, `bausystem` dem zweiten (siehe
  `hg_bausystem.md`). Die DDD-Literatur (Evans, Vernon) stützt die
  Trennung mit dem Aggregat-Begriff.

  Eigene Festlegung in diesem Glossar:

  - **Bauteilgruppe** ist die Hauptbenennung für das partitive
    Aggregat aus mehreren Bauteilen mit eigener Identität,
    eigener Hüllgeometrie und kaskadischem Lebenszyklus.
  - „Baugruppe" wird als abgelehnte Benennung geführt, weil sie
    im Maschinenbau und in der Vorfertigungs-Logistik eine
    abweichende Bedeutung hat (vorgefertigte Liefereinheit ohne
    notwendige konstruktive Funktionseinheit).
  - „Bausystem" ist explizit **kein** Synonym (siehe
    `hg_bausystem.md`); die Verwechslung ist die Hauptmotivation für
    die strikte Trennung beider Begriffe.

  Konkrete Subtypen (Lukarne, Walm, Auswechslung, Erker, Drempel,
  Gaube, vorgefertigtes Wandelement) sind ausdrücklich **nicht**
  Gegenstand dieses Eintrags und werden in eigenen Folgeeinträgen
  definiert, sobald sie im Tool benötigt werden.
---

## Prosa-Definition

Eine **Bauteilgruppe** ist ein partitives Aggregat aus mindestens
zwei Bauteilen mit eigener, von außen referenzierbarer Identität,
einer eigenen Hüllgeometrie, einer konstruktiven Funktionseinheit
und exklusiver Bestandteils-Mitgliedschaft, dessen Bestandteile
lebenszyklisch an die Gruppe gebunden sind.

## Mathematische Definition

Sei

- W das Weltkoordinatensystem (siehe `weltkoordinatensystem`),
- 𝓑 die Menge aller Bauteile im Sinne von `bauteil`,
- 𝒰 der UUID-Raum nach `uuid`,
- 𝒢_huelle die Menge der zulässigen Hüllgeometrie-Repräsentationen
  (Polyeder, achsenparalleler Hüllquader oder allgemeiner
  Bounding-Volume; konkrete Repräsentation siehe `polyeder` und
  Folgearbeit `boundingvolume`).

Dann ist eine **Bauteilgruppe** ein Tupel

```
G := (uuid, bestandteile, lage, huelle, funktion?, bezeichnung?)
```

mit

- **uuid** ∈ 𝒰: technischer Surrogatschlüssel der Gruppe (Pflicht,
  persistent, RFC 9562 v7); externe Referenzen auf die Gruppe gehen
  ausschließlich auf diese UUID (Aggregat-Wurzel im Sinne von
  Evans 2003 Kap. 6).
- **bestandteile** ⊂ 𝓑, |bestandteile| ≥ 2: die endliche, nicht-leere
  Menge der Bauteile, die die Gruppe konstituieren.
- **lage** ∈ SE(3): die Starrkörpertransformation, die das lokale
  Gruppen-Koordinatensystem nach W überführt (Rotation R ∈ SO(3) und
  Translation t ∈ ℝ³); siehe `lokales_koordinatensystem`.
- **huelle** ∈ 𝒢_huelle: die geometrische Hülle der Gruppe im lokalen
  Gruppen-Koordinatensystem (Polyeder oder Bounding-Volume); diese
  Hülle ist eine Eigenschaft der Gruppe als Ganzes, nicht eines
  einzelnen Bestandteils.
- **funktion?**: optionale Klassifikation der konstruktiven Funktion
  (z. B. „Tageslicht-Aufbau", „Lasteinleitung um Öffnung",
  „Eckabschluss"); die genaue Wertemenge wird in den konkreten
  Subtypen festgelegt.
- **bezeichnung?**: optionaler humanlesbarer Name (z. B. „Lukarne
  über Wohnzimmer").

und den Konsistenzbedingungen

1. **Exklusive Mitgliedschaft** (zentrale Aggregat-Eigenschaft):
   In einem Modell mit Bauteilgruppen-Menge 𝒢ᴹ gilt
   ```
   ∀ G₁, G₂ ∈ 𝒢ᴹ : G₁ ≠ G₂ ⇒ G₁.bestandteile ∩ G₂.bestandteile = ∅
   ```
   Ein Bauteil gehört zu **höchstens einer** Bauteilgruppe pro
   Aggregations-Hierarchie.
2. **Kaskadische Lebenszyklus-Bindung**: Wird die Gruppe G aus dem
   Modell entfernt, so werden ihre Bestandteile entweder ebenfalls
   entfernt oder ausdrücklich an ein Eltern-Aggregat zurückgegeben.
   Es entstehen keine „freistehenden ehemaligen Gruppen-Bestandteile".
3. **Hüllen-Inklusion** (geometrische Konsistenz): Die geometrische
   Punktmenge der Bestandteile ist in der Hülle enthalten,
   ```
   ⋃_{b ∈ bestandteile} G_W(b) ⊆ G_W(G)
   ```
   wobei G_W(b) die Bauteil-Punktmenge in W (siehe `bauteil`) und
   G_W(G) := lage(G_lokal(huelle)) die transformierte Hülle ist. Die
   Hülle muss nicht die konvexe Hülle sein; sie muss nur
   einschließen.
4. **Verschachtelung erlaubt, Zyklen verboten**: Eine Bauteilgruppe
   kann Bestandteil einer übergeordneten Bauteilgruppe sein
   (rekursiv); der Aggregations-Graph ist azyklisch (DAG-Struktur,
   praktisch ein Baum bei strikter exklusiver Mitgliedschaft).
   Diese Erweiterung wird hier nur konzeptuell genannt und in
   konkreten Subtypen formalisiert; im Grundmodell genügt
   `bestandteile ⊂ 𝓑`.

Die **geometrische Punktmenge** der Bauteilgruppe in W ist

```
G_W(G) := lage(G_lokal(huelle)) ⊂ ℝ³
```

(transformierte Hülle); die alternative Repräsentation als
Vereinigung der Bestandteils-Punktmengen ⋃_{b ∈ bestandteile} G_W(b)
ist eine **abgeleitete** Größe und im Allgemeinen eine echte
Teilmenge von G_W(G).

## Wohldefiniertheit

- **Existenz**: Für jede konstruktive Einheit aus zwei oder mehr
  zusammengehörigen Bauteilen lässt sich eine Bauteilgruppe als
  Tupel (uuid, bestandteile, lage, huelle, funktion?, bezeichnung?)
  erfassen. Mindestkonfiguration: |bestandteile| = 2,
  lage = id_SE(3), huelle = achsenparalleler Hüllquader der beiden
  Bauteil-Bounding-Boxen, funktion = ⊥, bezeichnung = ⊥.
- **Eindeutigkeit der Identität**: Innerhalb eines Modells gilt
  ∀ G₁, G₂ : (G₁ ≠ G₂) ⇒ (G₁.uuid ≠ G₂.uuid). Die Gruppen-UUID ist
  konstruktionsseitig zu vergeben (UUID v7 nach RFC 9562) und
  persistent.
- **Eindeutigkeit der Mitgliedschaft**: Bedingung 1 (exklusive
  Mitgliedschaft) garantiert, dass die Zuordnung Bauteil → Gruppe
  funktional ist: für jedes b ∈ ⋃_{G ∈ 𝒢ᴹ} G.bestandteile existiert
  genau eine Gruppe G mit b ∈ G.bestandteile. Diese Funktion ist
  die Aggregat-Wurzel-Auflösung.
- **Unabhängigkeit von der Wahl des lokalen Gruppen-
  Koordinatensystems**: Für jede zulässige Wahl des lokalen Systems
  liefert die zugehörige Lage SE(3)-Transformation dieselbe
  Punktmenge G_W(G); semantisch invariant.
- **Konsistenz mit `bauteil`**: Jedes b ∈ bestandteile ist ein
  Bauteil im Sinne von `bauteil` (mit eigener Identität, Lage,
  Geometrie, Werkstoff). Die Bauteile bleiben eigenständige
  Element-Instanzen mit eigener UUID; die Mitgliedschaft in der
  Gruppe ist eine zusätzliche Beziehung, keine Überschreibung der
  Bauteil-Eigenschaften.
- **Nicht-Zirkularität**: Die Definition verwendet die Primitive
  `punkt`, `vektor`, `weltkoordinatensystem`, `toleranzen`,
  `lokales_koordinatensystem`, `polyeder`, `uuid` sowie den bereits
  definierten Begriff `bauteil`. Sie verweist nicht auf konkrete
  Subtypen (Lukarne, Walm, Auswechslung) und nicht auf `bausystem`
  (das ist ein orthogonaler Aggregations-Mechanismus, keine
  Voraussetzung).
- **Trivial wohldefinierte Bestandteile-Menge**: bestandteile ist
  als Menge unsortiert; alle Aussagen über die Gruppe sind invariant
  unter Permutation der Bestandteile.

## Erläuterung (nicht normativ)

Die Bauteilgruppe ist die ontologische Antwort auf eine Klasse von
konstruktiven Einheiten, die im Holzbau immer wieder auftauchen und
gemeinsame strukturelle Eigenschaften haben:

- Eine **Lukarne** über dem Wohnzimmer ist als „diese Lukarne"
  referenzierbar; sie hat eine Stehhöhe, eine Grundfläche und ein
  Bounding-Volume als Eigenschaften der Lukarne, nicht der einzelnen
  Sparren oder Wechsel. Wird die Lukarne entfernt, verschwinden auch
  ihre Bestandteile (oder sie werden ausdrücklich an die umgebende
  Dachfläche zurückgegeben).
- Eine **Auswechslung** um eine Kaminöffnung ist eine konstruktive
  Funktionseinheit aus Wechselbalken und auszuwechselnden Sparren,
  die zusammen die Last um die Öffnung herumführen. Ein einzelner
  Wechsel gehört zu genau einer Auswechslung, nicht zu mehreren
  gleichzeitig.
- Ein **Walm** (`hg_walm.md`, bereits angelegt) ist die geometrische
  und konstruktive Einheit aus Gratsparren, Schiftern und einem
  optionalen Mittelsparren in der Walmfläche an einem walmförmig
  abgeschrägten Dachende; auch hier hat das Aggregat eigene
  Eigenschaften (Walmlinie via `hg_grat.md`, Walmneigung),
  die einzelne Sparren nicht
  haben.

In allen drei Beispielen sind die strukturellen Merkmale identisch:
**eigene Identität**, **eigene Geometrie als Hülle**, **exklusive
Mitgliedschaft**, **kaskadische Lebenszyklus-Bindung**,
**konstruktive Funktionseinheit**. Diese Merkmalsgemeinsamkeit
rechtfertigt den abstrakten Oberbegriff Bauteilgruppe.

### DDD-Perspektive

Im Sinne von Domain-Driven Design (Evans 2003 Kap. 6, Vernon 2013
Kap. 10) ist eine Bauteilgruppe ein **Aggregat im engeren Sinn**:
eine Konsistenz-Grenze um zusammengehörige Entitäten, mit einer
Aggregat-Wurzel, die als einziger Einstiegspunkt für externe
Referenzen dient. Externe Aufrufer referenzieren „die Lukarne"
über die Gruppen-UUID; sie greifen nicht direkt auf einzelne
Sparren der Lukarne zu, ohne über die Wurzel zu gehen. Diese
Eigenschaft ist die Grundlage für eine konsistente
Modifikations-Semantik: alle Veränderungen an Bestandteilen der
Lukarne werden über die Lukarne-Aggregat-Wurzel koordiniert.

### Abgrenzung zu Bausystem in einem Satz

Bauteilgruppe ist **partitive Komposition mit exklusiver
Mitgliedschaft**, Bausystem ist **funktionale Gruppierung mit
nicht-exklusiver Mitgliedschaft**. Ein Bauteil kann zu höchstens
einer Bauteilgruppe gehören, aber zu beliebig vielen Bausystemen
gleichzeitig. Siehe `hg_bausystem.md`.

### Abgrenzung zu Verbindung in einem Satz

Eine **Verbindung** (`verbindung`) ist ein lokales Knoten-Aggregat
aus Bauteilen, Verbindungsmitteln, Verbindern und Verstärkungen
mit Fokus auf Kraftübertragung an einem Punkt; eine
**Bauteilgruppe** ist eine konstruktive Funktionseinheit aus
mehreren Bauteilen über einen räumlich ausgedehnten Bereich. Eine
Bauteilgruppe enthält in der Regel mehrere Verbindungen zwischen
ihren Bestandteilen.

## Beziehungen

- **Oberbegriff**: derzeit `null`. Bauteilgruppe und Bausystem
  liegen auf einer eigenen Aggregats-Hierarchie neben Element
  (Bauteil/Verbindungsmittel/Verbinder/Verstärkungselement); ein
  gemeinsamer abstrakter Oberbegriff für „Aggregat über Bauteilen"
  wird derzeit nicht eingeführt, weil die strukturellen Unterschiede
  (exklusiv vs. nicht-exklusiv, eigene Geometrie vs. optional, eigene
  Identität als Whole vs. als Sicht) zu groß sind.
- **Bestandteile (partitiv)**:
  - **Bauteile** (`bauteil`): die exklusiven Bestandteile der Gruppe.
  - **Lokales Koordinatensystem** (`lokales_koordinatensystem`): die
    Bezugssystem-Festlegung der Gruppe.
  - **Hülle** (`polyeder` oder Bounding-Volume): die geometrische
    Aggregat-Eigenschaft der Gruppe.
- **Spezialisierungen** (eigene Einträge folgen, trigger-basiert):
  - **Binder** (`binder`, bereits angelegt): werks-vorgefertigtes
    Trag-Aggregat (Sparrenbinder, Pfettenbinder, Nagelplattenbinder,
    BSH-Binder, Fachwerk-/Vollwandbinder).
  - **Lukarne** / **Gaube** (`lukarne`, `gaube`): Dachaufbau für
    Tageslicht und Stehhöhe.
  - **Walm** (`walm`, bereits angelegt): walmförmiger Abschluss
    eines Daches als Aggregat aus Gratsparren, Schiftern und
    optionalem Mittelsparren in der Walmfläche.
  - **Auswechslung** (`auswechslung`): Aggregat aus Wechselbalken
    und auszuwechselnden Bauteilen um eine Öffnung
    (Kamin, Treppenloch, Dachfenster).
  - **Erker** (`erker`): vorspringende Bauteilgruppe mit eigener
    Geometrie.
  - **Drempel-Aufbau** (`drempel_aufbau`): Aggregat aus Drempelwand-
    Bauteilen über einer Geschossdecke.
  - **Vorgefertigtes Wandelement / Deckenelement**: Aggregat aus
    Rahmen, Beplankung und Dämmlagen, das als Liefereinheit
    verbaut wird.
- **Verwendung**:
  - Bestandteil eines **Bauwerks**.
  - Möglicher Bestandteil eines übergeordneten Aggregats
    (Verschachtelung erlaubt, siehe Bedingung 4).
- **Abgrenzung**:
  - **Bauteil** (`bauteil`): einzelner Bestandteil; eine
    Bauteilgruppe ist eine Komposition aus mehreren Bauteilen, kein
    einzelnes Bauteil. Eine Bauteilgruppe ist insbesondere **nicht**
    selbst ein Element-Subtyp (siehe `element`); sie hat eine eigene
    Aggregat-Hierarchie.
  - **Bausystem** (`bausystem`): funktionale, nicht-exklusive
    Gruppierung; siehe oben und `hg_bausystem.md`.
  - **Verbindung** (`verbindung`): lokales Knoten-Aggregat mit
    Fokus auf Kraftübertragung; siehe oben.
  - **Tragwerk** (`tragwerk`): nicht-exklusives Bausystem über
    lastabtragenden Bauteilen, kein partitives Aggregat. Ein Bauteil
    kann gleichzeitig Bestandteil einer Auswechslung
    (Bauteilgruppe) und Mitglied des Tragwerks (Bausystem) sein.
  - **Bearbeitung** (`bearbeitung`): subtraktiv am Bauteil selbst,
    keine Komposition mehrerer Bauteile.
  - **Dach** (`dach`), **Dachaufbau** (`dachaufbau`): bestehende
    Aggregat-Begriffe mit eigener spezifischer Semantik
    (Tripel- bzw. Schichtaufbau-Struktur). Bauteilgruppe ist der
    generischere Oberbegriff für aus mehreren Bauteilen bestehende
    Einheiten mit exklusiver Mitgliedschaft; ob `dach` und
    `dachaufbau` künftig formal als Bauteilgruppen-Spezialisierungen
    eingeordnet werden, ist eine offene Designfrage und nicht
    Gegenstand dieses Eintrags.
  - **Konstruktionsdetail** (`konstruktionsdetail`, bereits angelegt):
    lokale Modellierungseinheit eines Anschlusses; nicht-exklusive
    Mitgliedschaft (vs. partitive Bauteilgruppe-Mitgliedschaft).
  - **Element** (`element`): Bauteilgruppen sind keine
    Element-Subtypen; Element-Subtypen sind ausschließlich
    Bauteil, Verbindungsmittel, Verbinder und Verstärkungselement
    (Memory `project_element_ontologie`).

## Implementierungshinweis

**Im aktuellen Glossarstand wird ausdrücklich keine Code-Klasse
`Bauteilgruppe` angelegt** (Memory `project_glossar_konventionen`,
Briefing `briefing_aggregations_begriffe.md`). Die ontologische
Vorbereitung lebt zunächst nur im Glossar; die Code-Klasse entsteht
zusammen mit dem ersten konkreten Subtyp (z. B. `Auswechslung`,
`Lukarne`), der in einem Tool tatsächlich benötigt wird. Der
folgende Skizzen-Code ist ausschließlich orientierender
Implementierungs-Hinweis für den Zeitpunkt, an dem dieser Subtyp
implementiert wird.

```kotlin
// SKIZZE — nicht jetzt anlegen.
// Glossar: hg_bauteilgruppe.md

package domain.bauteil

import domain.bauteil.Bauteil
import java.util.UUID

/**
 * Bauteilgruppe: partitives Aggregat aus mehreren Bauteilen mit
 * eigener Identität, eigener Hülle und exklusiver Mitgliedschaft.
 *
 * Sealed, weil konkrete Subtypen (Auswechslung, Lukarne, Walm,
 * Erker, Drempel-Aufbau) eigene Constraints und eigene
 * Aggregat-Geometrie tragen. Direktes Instanziieren des
 * Oberbegriffs ist konzeptuell möglich, in der Praxis aber selten
 * sinnvoll.
 */
sealed class Bauteilgruppe {
    abstract val uuid: UUID
    abstract val bestandteile: Set<Bauteil>
    abstract val lokalePlatzierung: LokalePlatzierung
    abstract val huelle: Huellgeometrie
    abstract val bezeichnung: String?

    init {
        // 1. bestandteile.size >= 2          → sonst Entartet.ZuKleineGruppe
        // 2. Hüllen-Inklusion (Bedingung 3)  → sonst Entartet.HuelleZuKlein
        // 3. Exklusive Mitgliedschaft wird auf Modell-Ebene geprüft,
        //    nicht im Konstruktor (Cross-Aggregat-Invariante).
    }
}
```

- **Einheit**: Längen in mm (Double); Winkel intern in Radiant; Lage
  als SE(3)-Element (Rotation + Translation, siehe Folgearbeit).
- **Identität**: `uuid` ist Pflicht und persistent (RFC 9562 v7);
  externe Referenzen auf eine Bauteilgruppe gehen ausschließlich auf
  diese UUID (Aggregat-Wurzel). Bestandteile werden über ihre
  jeweiligen Bauteil-UUIDs referenziert (Foreign-Key-Regel, Memory
  `project_bauteil_identifikation`).
- **Invarianten** (im `init`-Block bzw. in Fabrikfunktionen prüfen,
  bei Verletzung `Resultat.Fehler` bzw. `Entartet`-Variante;
  niemals Exception werfen):
  1. `bestandteile.size >= 2` ⇒ sonst
     `Entartet.ZuKleineGruppe` (eine einelementige Gruppe ist kein
     Aggregat).
  2. **Hüllen-Inklusion**: für jedes b ∈ bestandteile gilt
     G_W(b) ⊆ G_W(G); bei Verletzung
     `Entartet.HuelleZuKlein`. Toleranz `Toleranzen.LAENGE_EPS`.
  3. **Exklusive Mitgliedschaft** (modellweite Cross-Aggregat-
     Invariante): für jedes b ∈ bestandteile existiert keine
     andere Bauteilgruppe G' ≠ G mit b ∈ G'.bestandteile. Diese
     Invariante kann nicht im Gruppen-Konstruktor allein geprüft
     werden; sie ist Aufgabe des Modell-Containers (Repository,
     `Bauwerk`-Aggregat-Manager). Bei Verletzung
     `Entartet.MehrfachMitgliedschaft`.
  4. **Azyklischer Aggregations-Graph** (bei Verschachtelung):
     keine Bauteilgruppe darf direkt oder transitiv ihre eigene
     Vorfahrin sein. Bei Verletzung `Entartet.ZyklischeGruppe`.
- **Edge Cases**:
  - **Zwei-Bauteile-Gruppe** (|bestandteile| = 2): zulässig
    (z. B. einfache Auswechslung aus einem Wechsel und einem
    auszuwechselnden Sparren).
  - **Verschachtelte Gruppen** (Lukarne enthält eine
    Auswechslung um ihr Dachfenster): erlaubt, solange der
    Aggregations-Graph azyklisch bleibt.
  - **Bauteil-Wechsel der Gruppen-Zugehörigkeit** (z. B. ein
    Sparren wird von der Lukarne in die umgebende Dachfläche
    übergeben): erfordert eine koordinierte Modifikation beider
    Gruppen über den Modell-Container; nicht durch direkten
    Bauteil-Zugriff.
  - **Bauteilgruppe ohne Hülle**: nicht zulässig. Die Hülle ist
    Pflichtfeld und konstituierende Eigenschaft der Gruppe.
- **Abgeleitete Eigenschaften** (als Funktionen, keine Felder):
  - `geometrieInWelt(): GeometrieInW` = `lage(huelle)` als
    transformierte Hülle in W.
  - `bestandteilsVereinigung(): GeometrieInW` =
    ⋃_{b ∈ bestandteile} G_W(b); im Allgemeinen echte Teilmenge
    der Hülle.
  - `boundingBox(): AABB` = achsenparalleler Hüllquader in W,
    abgeleitet aus der Hülle.
  - `volumen(): Double` (mm³) = Volumen der Hülle.
  - `enthaelt(b: Bauteil): Boolean` = `b in bestandteile`.

## Quellen

**Primär (normativ):**

- ISO 16739-1:2024, „Industry Foundation Classes (IFC) for data
  sharing in the construction and facility management industries —
  Part 1: Data schema", insbesondere `IfcElementAssembly` und
  `IfcRelAggregates`.
- buildingSMART International: *IFC4.3 Documentation* (Version
  4.3.2.0, 2024).
- DIN EN 1995-1-1:2010-12, „Eurocode 5: Bemessung und Konstruktion
  von Holzbauten – Teil 1-1: Allgemeines", Abschnitte 1.5 und 9.
- SIA 265:2021, „Holzbau", Schweizerischer Ingenieur- und
  Architektenverein, Zürich, Abschnitt 5.

**Sekundär:**

- Evans, E.: *Domain-Driven Design — Tackling Complexity in the
  Heart of Software.* Addison-Wesley 2003, insbes. Kap. 6.
- Vernon, V.: *Implementing Domain-Driven Design.* Addison-Wesley
  2013, insbes. Kap. 10.
- Mönck, W.; Rug, W.: *Holzbau – Bemessung und Konstruktion.*
  16. Auflage, Beuth, Berlin 2015.
- Gerner, M.: *Fachwerk – Instandsetzung, Sanierung, Neubau.*
  DVA, 7. Auflage 2007.
- Natterer, J.; Herzog, T.; Volz, M.: *Holzbau-Atlas.* 4. Auflage,
  Birkhäuser, Basel 2003.

**Korpus (nicht autoritativ):**

- Holzbau Deutschland, Merkblatt „Begriffe und Klassifizierungen
  für den Holzbau" (abgerufen 2026-05-09).
- Wikipedia, Lemmata „Lukarne", „Gaube", „Auswechslung", „Walm"
  (abgerufen 2026-05-09).

## Folgearbeit (trigger-basiert)

Konkrete Spezialisierungen werden definiert, sobald das jeweilige
Tool sie benötigt:

- `lukarne` / `gaube` — Dachaufbau für Tageslicht und Stehhöhe.
- `walm` — walmförmiger Abschluss eines Daches.
- `auswechslung` — Aggregat um eine Öffnung im Dach oder in der
  Decke (Kamin, Treppenloch, Dachfenster).
- `erker` — vorspringende Bauteilgruppe.
- `drempel_aufbau` — Aggregat aus Drempelwand-Bauteilen.
- `vorgefertigtes_wandelement` / `vorgefertigtes_deckenelement` —
  Liefereinheit aus Rahmen, Beplankung, Dämmlagen.

Außerdem als Folgearbeit auf Glossar-Ebene:

- `boundingvolume` als Hüllgeometrie-Repräsentation für Aggregate
  (achsenparalleler Hüllquader, orientierter Hüllquader, konvexer
  Hüllpolyeder, beliebiger Hüllpolyeder).
- Ggf. ein abstrakter Oberbegriff `aggregat` über
  `bauteilgruppe`, `bausystem`, `verbindung` und `tragwerk`, falls
  sich strukturelle Gemeinsamkeiten (eigene UUID, Lebenszyklus)
  als hinreichend tragfähig erweisen — derzeit als offen geführt.
