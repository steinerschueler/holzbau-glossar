---
id: element
benennung: Element
synonyme: [Modellelement, identifizierbares Objekt]
abgelehnte_benennungen: [Bauelement, Objekt, Ding, Stück, "element", "object", "product", "item"]
oberbegriff: null
begriffstyp: generisch
voraussetzungen: [uuid, weltkoordinatensystem, werkstoff, toleranzen]
abgrenzung_zu: [bauteil, verbindungsmittel, verbinder, verstaerkungselement, verbindung, tragwerk, dach, dachaufbau, bauteil_aggregat, werkstoff, geometrie, lokales_koordinatensystem]
status: entwurf
subglossar_pendant: notwendig
quellen_primär:
  - "ISO 16739-1:2024, 'Industry Foundation Classes (IFC) for data sharing in the construction and facility management industries — Part 1: Data schema', insbesondere die Vererbungshierarchie IfcRoot → IfcObjectDefinition → IfcObject → IfcProduct → IfcElement (Abschnitt 5 ff.)."
  - "buildingSMART International: 'IFC4.3 Documentation' (Version 4.3.2.0, 2024), Definitionen IfcRoot (mit GlobalId, Name, Description, OwnerHistory) und IfcElement (Vorfahre aller verbauten Bauteile, Verbindungsmittel, Zubehörteile)."
  - "RFC 9562:2024, 'Universally Unique IDentifiers (UUIDs)', IETF, Mai 2024."
quellen_sekundär:
  - "Evans, E.: Domain-Driven Design — Tackling Complexity in the Heart of Software. Addison-Wesley 2003, Kap. 5 'A Model Expressed in Software', insbesondere Entity / Identity."
  - "Vernon, V.: Implementing Domain-Driven Design. Addison-Wesley 2013, Kap. 5 'Entities' (Identitätsbegriff, Surrogate-Identität)."
  - "Fowler, M.: Patterns of Enterprise Application Architecture. Addison-Wesley 2003, Kap. 'Identity Field'."
  - "design2machine: BTLx 2.x Specification (Stand 2024), Element Part mit Attribut GUID."
quellenkonflikt: |
  Der Begriff „Element" wird in Holzbau-Normen uneinheitlich gebraucht:

  - DIN EN 1995-1-1 verwendet „element" und „member" weitgehend
    synonym für Bauteil im engeren Sinn (Stab, Träger).
  - SIA 265 spricht von „Bauteil"; „Element" tritt v. a. in
    Plattenwerkstoff-Kontexten auf (BSP-Element, Schichtholzelement).
  - ISO 16739-1 (IFC) und buildingSMART verwenden „IfcElement"
    abstrakt-generisch als Vorfahre aller verbauten Objekte —
    Bauteile, Verbindungsmittel (IfcMechanicalFastener), Zubehör-
    teile (IfcDiscreteAccessory) und Komponenten (IfcElementComponent)
    teilen IfcElement als gemeinsame Basisklasse.
  - DDD-Literatur (Evans, Vernon) führt den orthogonalen Begriff
    „Entity" für identitätstragende Objekte.

  Eigene Festlegung in diesem Glossar (konsistent mit IFC und mit
  der App-Ontologie):

  - **Element** ist hier der **abstrakte Oberbegriff** der App-
    Ontologie für identifizierbare, geometrisch verortete, in einem
    Bauwerk verbaute Objekte mit eigener UUID. Eine Element-Instanz
    ist nicht direkt instanziierbar; konkrete Instanzen sind
    Bauteile, Verbindungsmittel, Verbinder oder Verstärkungselemente
    (eigene Einträge folgen).
  - Die in EN 1995-1-1 / SIA 265 verwendete enge Lesart („Element
    als Stab/Träger") ist hier ausdrücklich **nicht** gemeint;
    diese Lesart fällt unter `bauteil`.
  - **Aggregate** (Verbindung, Tragwerk, Dach, Dachaufbau,
    Bauteilaggregat) sind **keine** Element-Subtypen, sondern
    Container für Element-Mengen. Ein Aggregat hat zwar selbst
    eine UUID, ist aber kein verbautes Einzelobjekt; deshalb wird
    es nicht unter Element subsumiert.
  - Die Wahl der Vererbungshierarchie folgt IFC bewusst, weil die
    App ihre Persistenz und Interoperabilität auf IFC und BTLx
    stützt.
---

## Prosa-Definition

Ein **Element** ist ein abstrakter Oberbegriff für ein
identifizierbares, geometrisch verortetes, in einem Bauwerk
verbautes Einzelobjekt, das durch eine eigene technische Identität
(UUID), eine Geometrie und eine Lage im Weltkoordinatensystem
charakterisiert ist und das in einer der vier konkreten Subklassen
**Bauteil**, **Verbindungsmittel**, **Verbinder** oder
**Verstärkungselement** instanziiert wird.

## Mathematische Definition

Sei

- W das Weltkoordinatensystem (siehe `weltkoordinatensystem`),
- 𝓤 der UUID-Raum nach RFC 9562 (siehe `uuid`),
- 𝓖 die Menge aller geometrischen Repräsentationen, die in der
  Domänen-Schicht zugelassen sind (Stab-Achse + Querschnitt,
  Trägerfläche + Dicke, Polyeder, Achsenpunkt, Linsen-/Stab-
  Geometrie eines Verbindungsmittels; eigene Einträge
  `geometrie`, `bauteilachse`, `polyeder`, … in Folgearbeit),
- SE(3) = SO(3) ⋉ ℝ³ die Menge der Starrkörpertransformationen
  (Rotation R ∈ SO(3) und Translation t ∈ ℝ³),
- 𝓦 die Menge der zulässigen Werkstoffe (siehe `werkstoff`,
  abstrakter Oberbegriff der Werkstoff-Hierarchie mit den vier
  konkreten Subklassen `axiales_holz`, `mehrlagenholz`,
  `gerichteter_plattenwerkstoff`, `isotroper_plattenwerkstoff`),
- ℙ = String ⊎ {⊥} die Menge der zulässigen Positionsnummern
  (siehe `positionsnummer`),
- ℛ die Menge der zulässigen Produktkennzeichnungen (siehe
  `produktkennzeichnung`),
- 𝒩 = String ⊎ {⊥} die Menge der zulässigen freien Bezeichnungen.

Dann ist ein **Element** das Tupel

```
E := (uuid, geometrie, lokale_platzierung, werkstoff,
      positionsnummer?, produktkennzeichnung?, bezeichnung?)
```

mit den Pflichtkomponenten

- **uuid** ∈ 𝓤  (eindeutiger, persistenter, technischer Identifikator),
- **geometrie** ∈ 𝓖  (geometrische Repräsentation im lokalen
  Element-Koordinatensystem; konkrete Subklasse bestimmt die
  zulässige Teilmenge von 𝓖),
- **lokale_platzierung** ∈ SE(3)  (Starrkörpertransformation, die
  das lokale Element-Koordinatensystem nach W überführt),
- **werkstoff** ∈ 𝓦  (Materialklasse, aus der das Element besteht;
  abstrakte Wurzel `werkstoff` mit vier konkreten Subklassen
  nach Faserrichtungs-Modus),

und den Optionalkomponenten

- **positionsnummer?** ∈ ℙ  (humanlesbarer Geschäftsschlüssel,
  mutable, scoped pro Projekt + Kategorie),
- **produktkennzeichnung?** ∈ ℛ  (normativ kodifizierte Charge-/
  Produkt-Identifikation, nur bei Werkstoff-Charge relevant),
- **bezeichnung?** ∈ 𝒩  (freier Anzeigename ohne Strukturanspruch).

Das Element ist **abstrakt**: Element selbst ist nicht
instanziierbar, sondern bezeichnet die Vereinigung der vier
konkreten Subklassen-Mengen

```
𝓔 := 𝓑 ⊎ 𝓥𝓜 ⊎ 𝓥𝓑 ⊎ 𝓥𝓢
```

mit

- 𝓑   = Menge der Bauteile (siehe `bauteil`),
- 𝓥𝓜  = Menge der Verbindungsmittel (siehe `verbindungsmittel`),
- 𝓥𝓑  = Menge der Verbinder (siehe `verbinder`),
- 𝓥𝓢  = Menge der Verstärkungselemente
  (siehe `verstaerkungselement`).

Die geometrische Punktmenge eines Elements im
Weltkoordinatensystem ist

```
G_W(E) := { lokale_platzierung(p) | p ∈ G_lokal(geometrie) } ⊂ ℝ³.
```

## Wohldefiniertheit

- **Existenz**: Für jedes konkrete in einem Bauwerk verbaute
  Objekt mit eigener Identität lässt sich die obige Tupelstruktur
  erfassen. Die UUID wird bei Objekterzeugung systemseitig vergeben
  (siehe `uuid`); Geometrie und lokale Platzierung sind
  Pflichtfelder mit nicht-leerer Wertemenge.
- **Eindeutigkeit der Identität**: Innerhalb eines Modells gilt
  ∀ E₁, E₂ : (E₁ ≠ E₂) ⇒ (E₁.uuid ≠ E₂.uuid). Die UUID ist
  technisch und persistent; siehe `uuid` für die Eindeutigkeits-
  garantie nach RFC 9562.
- **Abstrakt, nicht instanziierbar**: Element selbst hat keine
  Konstruktoren in der Domänen-Schicht (Kotlin: `sealed
  interface` oder `abstract class`). Jede Instanz ist
  notwendigerweise einer der vier Subklassen zugeordnet.
- **Disjunktheit der Subklassen**: 𝓑, 𝓥𝓜, 𝓥𝓑, 𝓥𝓢 sind paarweise
  disjunkt. Die Klassifikation eines konkreten Objekts in eine der
  vier Mengen ist eine Konstruktionsentscheidung, nicht eine
  Eigenschaft des Materials (Memory `project_element_ontologie`,
  Designregel 2: dieselbe Vollgewindeschraube ist
  Verbindungsmittel im Abscher-Anschluss, Verstärkungselement
  als Querzugverstärkung — getrennt instanziiert mit eigener
  UUID; siehe `hg_verstaerkungselement.md`).
- **Unabhängigkeit von der Wahl des lokalen Koordinatensystems**:
  Für jede zulässige Wahl des lokalen Element-Koordinatensystems
  liefert die zugehörige `lokale_platzierung` SE(3)-Transformation
  dieselbe Punktmenge G_W(E). Die Wahl ist Modellierungs-
  konvention, semantisch invariant.
- **Optionale Identifikatoren**:
  `positionsnummer?` und `produktkennzeichnung?` sind algebraisch
  optional (Wert oder ⊥); ⊥ ist ein zulässiger Wert und nicht
  das Fehlen einer Definition. Die Identitätspflicht wird
  ausschließlich durch `uuid` erfüllt; positionsnummer und
  produktkennzeichnung sind orthogonale Identifikator-Spuren mit
  je eigenem Zweck (siehe Memory `project_bauteil_identifikation`).
- **Nicht-Zirkularität**: Die Definition verwendet ausschließlich
  die Primitive `uuid`, `weltkoordinatensystem`, `toleranzen`,
  den (angelegten) Werkstoff-Oberbegriff `werkstoff` sowie die als
  Folge-Begriffe markierten Bausteine `geometrie`,
  `positionsnummer`, `produktkennzeichnung`. Sie
  verweist nicht auf die Subklassen Bauteil/Verbindungsmittel/
  Verbinder/Verstärkungselement in ihrer eigenen Definition,
  sondern grenzt sich nur extensional zu deren Vereinigung 𝓔 ab.

## Erläuterung (nicht normativ)

Der Element-Begriff dieses Glossars ist die **Wurzel der
App-Ontologie für verbaute Einzelobjekte**. Er trägt diejenigen
Eigenschaften, die jede konkrete Subklasse generisch erbt:
Identität, Geometrie, Lage in W, Werkstoff, optionale Beschriftung.

Die vier Subklassen unterscheiden sich in **Funktion und
Bemessungsverfahren**:

- **Bauteil** — tragend oder raumbildend; Querschnittsbemessung
  nach EC5 Kap. 6, SIA 265 Kap. 4 ff. Stab-, Flächen- oder
  Volumenbauteil.
- **Verbindungsmittel** — Nagel, Schraube, Bolzen, Stabdübel,
  Klammer, Klebung, Holzdübel; Anschlussbemessung nach EC5
  Kap. 8 (Johansen). IFC: `IfcMechanicalFastener`.
- **Verbinder** (Synonym: Verbindungselement) — Balkenschuh,
  Winkel, Knotenblech, Schlitzblech; meist mit eigener
  Zulassung (ETA, ABZ). IFC: `IfcDiscreteAccessory`.
- **Verstärkungselement** — Vollgewindeschraube als Querzug-,
  Querdruck- oder Schubverstärkung; axial bemessen nach
  EC5:2022-Entwurf bzw. ETA. IFC: `IfcMechanicalFastener` mit
  Funktions-Property-Set.

**Aggregate sind keine Elemente.** Eine Verbindung, ein Tragwerk,
ein Dach oder ein Dachaufbau bündeln mehrere Elemente, sind aber
selbst keine verbauten Einzelobjekte. Sie führen eine eigene
UUID-Klasse für ihre Identität, gehören aber strukturell auf eine
andere Hierarchie-Ebene.

**Drei orthogonale Identifikator-Spuren** (Memory
`project_bauteil_identifikation`): Jedes Element trägt potenziell
drei verschiedene Identifikatoren mit unterschiedlichen Zwecken
und Semantiken:

| Spur                  | Zweck                              | Mutabilität | Eindeutigkeit            | Foreign-Key-Ziel |
|-----------------------|------------------------------------|-------------|--------------------------|------------------|
| `uuid`                | technische Identität               | unveränderlich | global (RFC 9562)     | **immer**        |
| `positionsnummer`     | Werkplan-/Baustellenkommunikation  | mutable     | (projekt, kategorie)     | **nie**          |
| `produktkennzeichnung`| Charge/Lieferung (CE, DIN 4074)    | von Charge ererbt | je Norm festgelegt | **nie**          |

Foreign Keys aus Verbindungen, Aggregaten, BCF-Issues u. ä.
referenzieren ausschließlich die UUID. Renumbering der
Positionsnummer oder Materialwechsel bricht keine Beziehung.

## Beziehungen

- **Oberbegriff**: keiner. Element ist die Wurzel der App-Ontologie
  für verbaute Einzelobjekte.
- **Subklassen** (vier Geschwister unter dieser Basisklasse):
  - **Bauteil** (`bauteil`): tragend/raumbildend, Querschnitts-
    bemessung. Bestehender Eintrag; Umstellung auf
    `oberbegriff: element` erfolgt im Update-Task #16.
  - **Verbindungsmittel** (`verbindungsmittel`): Nagel, Schraube,
    Bolzen, Stabdübel, Klammer, Klebung. **Eintrag angelegt.**
  - **Verbinder** (`verbinder`, Synonym `verbindungselement`):
    Balkenschuh, Winkel, Knotenblech, Schlitzblech, Sherpa-
    Verbinder, Holzlasche. **Eintrag angelegt.**
  - **Verstärkungselement** (`verstaerkungselement`):
    Vollgewindeschraube als Querzug-/Querdruck-/Schubverstärkung
    nach EC5:2022 / ETA. **Eintrag angelegt.**
- **Bestandteile (partitiv) eines Elements**:
  - **UUID** (`uuid`): technische Identität, Pflicht.
  - **Geometrie** (`geometrie`, eigener Eintrag folgt):
    geometrische Repräsentation, Pflicht.
  - **Lokale Platzierung** (SE(3)-Transformation gegenüber W):
    Pflicht. Eigener Eintrag `lokales_koordinatensystem` /
    `lage` folgt.
  - **Werkstoff** (`werkstoff`): Materialklasse, Pflicht.
    Abstrakte Wurzel mit vier konkreten Subklassen
    (`axiales_holz`, `mehrlagenholz`,
    `gerichteter_plattenwerkstoff`, `isotroper_plattenwerkstoff`)
    nach Faserrichtungs-Modus.
  - **Positionsnummer** (`positionsnummer`): humanlesbarer
    Geschäftsschlüssel, optional.
  - **Produktkennzeichnung** (`produktkennzeichnung`):
    normativ kodifizierte Charge-Identifikation, optional.
  - **Bezeichnung**: freier Anzeigename, optional.
- **Abgrenzung**:
  - **Verbindung** (`verbindung`, eigener Eintrag folgt):
    Aggregat aus Bauteilen + Verbindungsmitteln (+ Verbindern
    + Verstärkungen) an einem Knotenpunkt. **Kein Element**,
    sondern Container.
  - **Tragwerk** (`tragwerk`): Aggregat lastabtragender
    Bauteile mit Verbindungen, Auflagern, Lastfällen.
    **Kein Element**.
  - **Dach** (`dach`), **Dachaufbau** (`dachaufbau`): Aggregate
    auf Bauwerksebene. **Keine Elemente**.
  - **Bauteilaggregat** (`bauteil_aggregat`, eigener Eintrag
    folgt): allgemeiner Aggregat-Oberbegriff.
  - **Werkstoff** (`werkstoff`): Stoffeigenschaft, **kein Element**.
    Abstrakte Werkstoff-Hierarchie mit vier konkreten Subklassen
    nach Faserrichtungs-Modus.
  - **Geometrie** (`geometrie`, eigener Eintrag folgt):
    Repräsentationsbaustein, **kein Element**.
  - **Lokales Koordinatensystem**
    (`lokales_koordinatensystem`, eigener Eintrag folgt):
    Bezugssystem, **kein Element**.

## Implementierungshinweis

Datentyp (Domänen-Schicht, Kotlin, Schicht `domain.element`):

```kotlin
package domain.element

import domain.geometrie.Geometrie         // eigener Eintrag folgt
import domain.geometrie.LokalePlatzierung // SE(3); eigener Eintrag folgt
import domain.holzbau.werkstoff.Werkstoff // sealed; vier Subklassen
                                          // (axiales_holz, mehrlagenholz,
                                          //  gerichteter_plattenwerkstoff,
                                          //  isotroper_plattenwerkstoff)
import domain.identifikation.Positionsnummer
import domain.identifikation.Produktkennzeichnung
import java.util.UUID

/**
 * Wurzel der App-Ontologie für verbaute Einzelobjekte.
 * Glossar: hg_element.md
 *
 * Abstrakt, nicht direkt instanziierbar. Konkrete Subklassen sind
 * Bauteil, Verbindungsmittel, Verbinder, Verstärkungselement.
 *
 * Pflichtfelder: uuid, geometrie, lokalePlatzierung, werkstoff.
 * Optionalfelder: positionsnummer, produktkennzeichnung, bezeichnung.
 *
 * Foreign-Key-Regel (siehe Memory project_bauteil_identifikation):
 * Verweise aus Verbindungen, Aggregaten, BCF-Issues etc.
 * referenzieren ausschließlich `uuid`, niemals `positionsnummer`
 * oder `produktkennzeichnung`.
 */
sealed interface Element {
    /** Technischer Surrogatschlüssel (UUID v7). Pflicht, persistent. */
    val uuid: UUID

    /** Geometrische Repräsentation im lokalen Element-Koordinatensystem. */
    val geometrie: Geometrie

    /** SE(3)-Transformation lokal → W. */
    val lokalePlatzierung: LokalePlatzierung

    /** Werkstoff-Klasse. Glossar: hg_werkstoff.md (sealed, 4 Subklassen). */
    val werkstoff: Werkstoff

    /** Humanlesbarer Geschäftsschlüssel (mutable, scoped). */
    val positionsnummer: Positionsnummer?

    /** Normativ kodifizierte Charge-Identifikation. */
    val produktkennzeichnung: Produktkennzeichnung?

    /** Freier Anzeigename. */
    val bezeichnung: String?
}
```

- **Einheit**: Längen in mm (Double); Winkel intern in Radiant;
  lokale Platzierung als SE(3)-Element (Rotation + Translation).
- **Identität**:
  - `uuid` ist Pflicht und wird **bei Objekterzeugung
    systemseitig** vergeben (UUID v7 nach RFC 9562, siehe `uuid`).
    Niemals händisch setzen.
  - `uuid` wird nach der Erzeugung **niemals geändert**, auch
    nicht bei IFC-/BTLx-Re-Import (externe GUIDs landen in
    eigenen Mapping-Feldern, nicht in `uuid`).
  - **Foreign Keys aller anderen Domänen-Klassen** referenzieren
    ausschließlich `uuid` — niemals `positionsnummer` oder
    `produktkennzeichnung`. Diese Regel ist die Schutzlinie der
    referentiellen Integrität.
- **Subklassenpflicht**: `Element` ist `sealed`; jede Instanz ist
  notwendigerweise einer der vier konkreten Subklassen
  Bauteil/Verbindungsmittel/Verbinder/Verstärkungselement
  zugeordnet (Glossareinträge angelegt; Bauteil-Umstellung auf
  `oberbegriff: element` im Update-Task #16).
- **Optionalität (normativ)**:
  - `positionsnummer: Positionsnummer?` — `null` zulässig im
    frühen Entwurfsstadium; wird typischerweise erst bei
    Werkplan-Erstellung vergeben. Niemals als Default-String
    setzen.
  - `produktkennzeichnung: Produktkennzeichnung?` — `null`
    zulässig solange noch keine Charge zugewiesen ist; wird bei
    Materialdisposition gesetzt.
  - `bezeichnung: String?` — `null` zulässig; Anzeige fällt dann
    auf `positionsnummer` oder UUID zurück.
- **Invarianten** (in Fabrikfunktionen / `init` der Subklassen
  prüfen, bei Verletzung `Resultat.Fehler` bzw. `Entartet`-Variante;
  niemals Exception werfen):
  1. `uuid` ist gesetzt und kein Null-UUID.
  2. `geometrie` ist nicht-degeneriert (Subklassen-spezifisch,
     siehe je Subklasse-Eintrag).
  3. `lokalePlatzierung` ist eine gültige SE(3)-Transformation
     (Rotation orthogonal, Determinante +1).
  4. `werkstoff` ist gesetzt.
- **IFC-Mapping** (Persistenzschicht, je Subklasse explizit
  dokumentieren):
  | Subklasse           | IFC-Klasse                                 | BTLx                                |
  |---------------------|--------------------------------------------|-------------------------------------|
  | Bauteil             | IfcBeam / IfcColumn / IfcMember / IfcPlate | Part mit @GUID                      |
  | Verbindungsmittel   | IfcMechanicalFastener                      | Processing oder eigenes Part        |
  | Verbinder           | IfcDiscreteAccessory                       | eigenes Part oder Reference         |
  | Verstärkungselement | IfcMechanicalFastener + Pset_Function      | wie VM + Funktionsattribut          |
  - `uuid` → `IfcRoot.GlobalId` (22-stellig Base64 nach
    ISO/IEC 9834-8) bzw. BTLx `Part/@GUID`.
  - `positionsnummer` → `IfcElement.Tag` bzw. BTLx
    `SingleMemberNumber`.
  - `produktkennzeichnung` → IFC Material-Resource Property Sets
    (`Pset_MaterialWoodBasedBeam`, `Pset_MaterialWoodBasedPanel`)
    bzw. BTLx Material-Element.
- **Edge Cases**:
  - **Element ohne lokale Platzierung**: nicht erlaubt;
    mindestens Identität in SE(3) (lokales System ≡ W) ist
    Pflicht.
  - **Element ohne Werkstoff**: nicht erlaubt; jeder verbaute
    Gegenstand hat eine Materialklasse (Holz, Stahl,
    Verbindungsmittelstahl, …). In sehr frühen Entwurfsphasen
    kann ein Platzhalter-Werkstoff `Werkstoff.UNBEKANNT`
    geführt werden, der vor Bemessung aufgelöst sein muss.
  - **Aggregate**: NICHT als Element instanziieren; eigene
    Klassen `Verbindung`, `Tragwerk`, `Dach`, `BauteilAggregat`
    (Folgearbeit).
  - **Versionierung / Revisionen**: Eine Modelländerung ohne
    Identitätsänderung lässt `uuid` unverändert (mutiertes
    Element). Eine konstruktive Neuanlage als Ersatz erzeugt
    eine neue UUID. Die Wahl zwischen event-sourced und
    temporal-versioniert ist Folgearbeit (Memory
    `project_bauteil_identifikation`).
- **Bezeichner-Konvention** (CLAUDE.md): Domänen-Klasse heißt
  `Element` (deutsch, Glossarbegriff); Subklassen heißen
  `Bauteil`, `Verbindungsmittel`, `Verbinder`,
  `Verstaerkungselement`.

## Quellen

**Primär (normativ):**

- ISO 16739-1:2024, „Industry Foundation Classes (IFC) for data
  sharing in the construction and facility management industries
  — Part 1: Data schema".
- buildingSMART International: „IFC4.3 Documentation",
  Version 4.3.2.0, 2024.
- RFC 9562:2024, „Universally Unique IDentifiers (UUIDs)", IETF,
  Mai 2024.

**Sekundär:**

- Evans, E.: *Domain-Driven Design — Tackling Complexity in the
  Heart of Software.* Addison-Wesley 2003.
- Vernon, V.: *Implementing Domain-Driven Design.* Addison-Wesley
  2013.
- Fowler, M.: *Patterns of Enterprise Application Architecture.*
  Addison-Wesley 2003.
- design2machine: *BTLx 2.x Specification* (Stand 2024).

**Korpus (nicht autoritativ):**

- DIN EN 1995-1-1:2010-12, „Eurocode 5 — Bemessung und
  Konstruktion von Holzbauten" (Verwendung von „element" /
  „member" im engeren Sinn; nicht maßgeblich für die abstrakte
  Lesart dieses Eintrags).
- SIA 265:2021, „Holzbau", Schweizerischer Ingenieur- und
  Architektenverein, Zürich.
