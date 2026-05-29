---
id: bausystem
benennung: Bausystem
synonyme: [Bauteilsystem, "funktionales System", "Building System"]
abgelehnte_benennungen: [Bauteilgruppe, System, Anlage, Baugruppe, Tragsystem, "system", "group", "assembly"]
oberbegriff: null
begriffstyp: relation
voraussetzungen: [bauteil, uuid, weltkoordinatensystem, toleranzen]
abgrenzung_zu: [bauteilgruppe, bauteil, tragwerk, verbindung, dachflaeche, dachaufbau, element, bauwerk]
status: entwurf
subglossar_pendant: nein
quellen_primär:
  - "ISO 16739-1:2024 'Industry Foundation Classes (IFC) for data sharing in the construction and facility management industries — Part 1: Data schema' (IFC 4.3.2), Entität `IfcBuildingSystem` (Spezialisierung von `IfcSystem`, ihrerseits Spezialisierung von `IfcGroup`) und Beziehung `IfcRelAssignsToGroup`: ein Bausystem ist eine funktionale Gruppierung von verbauten Elementen mit eigener GlobalId, die nicht-exklusive Mitgliedschaft erlaubt; ein Element kann gleichzeitig in mehreren `IfcBuildingSystem`-Instanzen enthalten sein. `IfcBuildingSystem.PredefinedType` führt unter anderem FENESTRATION, FOUNDATION, LOADBEARING, OUTERSHELL, SHADING, TRANSPORT, REINFORCING."
  - "buildingSMART International: 'IFC4.3 Documentation' (Version 4.3.2.0, 2024), Vererbungshierarchie `IfcGroup` → `IfcSystem` → `IfcBuildingSystem` und Abgrenzung zur partitiven Aggregation via `IfcRelAggregates` (`IfcElementAssembly`)."
  - "DIN EN 1995-1-1:2010-12 (Eurocode 5), Abschnitt 1.5 (Begriffe) und Abschnitt 5 (Tragwerksberechnung): das Tragwerk wird funktional als „Gesamtheit der lastabtragenden Bauteile“ verstanden, ohne formale Aggregat-Spezifikation; identische Bauteile können bemessungstechnisch gleichzeitig Teil von Tragwerk und Aussteifung sein."
  - "DIN EN 1990:2010-12 'Eurocode: Grundlagen der Tragwerksplanung', Abschnitt 1.5.1.1 'Tragwerk' als funktionales System."
  - "SIA 260:2013 'Grundlagen der Projektierung von Tragwerken', Abschnitt 2.1: Tragwerk als funktionale Gesamtheit."
quellen_sekundär:
  - "Evans, E.: Domain-Driven Design — Tackling Complexity in the Heart of Software. Addison-Wesley 2003, Kap. 6 'The Life Cycle of a Domain Object', Abgrenzung Aggregat (Aggregate) vs. Sicht/Tag-Beziehungen ohne Aggregat-Wurzel."
  - "Vernon, V.: Implementing Domain-Driven Design. Addison-Wesley 2013, Kap. 5 'Entities' und Kap. 10 'Aggregates', Diskussion der Wahl zwischen partitivem Aggregat und nicht-exklusiver Gruppierung."
  - "Lignum (Hrsg.): Holzbautabellen HBT, Lignum, Zürich, aktuelle Auflage, Kap. 'Tragwerke und Aussteifung' — Tragwerk und Aussteifung als überlappende funktionale Sichten auf dieselben Bauteile."
  - "Blass, H. J.; Sandhaas, C.: Ingenieurholzbau – Grundlagen der Bemessung. KIT Scientific Publishing, Karlsruhe 2016, Kap. 1 und 5."
quellenkonflikt: |
  Keine Holzbau-Norm (SIA 265, DIN 1052, DIN EN 1995-1-1) führt
  einen geschlossenen Oberbegriff für „funktionale, nicht-exklusive
  Gruppierung mehrerer Bauteile" als Datenmodell-Wurzel ein. Die
  Normen verwenden konkrete Begriffe (Tragwerk, Aussteifung,
  Hüllkonstruktion, Eindeckung, Schichtaufbau) jeweils funktional,
  ohne formale Mitgliedschafts-Semantik.

  Die einzige geschlossene, normativ gepflegte Spezifikation für
  funktionale Bauteil-Gruppierungen mit nicht-exklusiver
  Mitgliedschaft ist ISO 16739-1 (IFC) mit `IfcBuildingSystem` und
  der Beziehung `IfcRelAssignsToGroup`. Die strukturelle Trennung
  zwischen `IfcBuildingSystem` (funktional, nicht-exklusiv) und
  `IfcElementAssembly` (partitiv, exklusiv) ist im IFC-Datenmodell
  explizit und wird hier ausdrücklich übernommen.

  Eigene Festlegung in diesem Glossar:

  - **Bausystem** ist die Hauptbenennung für die funktionale,
    nicht-exklusive Gruppierung im Sinne von `IfcBuildingSystem`.
  - „Bauteilgruppe" wird als abgelehnte Benennung geführt, weil sie
    in diesem Glossar bereits als partitives Aggregat mit
    exklusiver Mitgliedschaft belegt ist (siehe `hg_bauteilgruppe.md`).
    Die strikte Trennung beider Begriffe ist die Hauptmotivation
    für diesen Eintrag.
  - „Tragsystem" wird als abgelehnte Benennung geführt, weil es im
    Sprachgebrauch häufig als Synonym von „Tragwerk" verwendet
    wird; das verengt den Bausystem-Begriff unzulässig auf den
    lastabtragenden Subtyp.
  - „System" ohne Qualifikator ist als abgelehnte Benennung
    geführt, weil zu generisch.

  Konkrete Subtypen (Tragwerk, Dachfläche als funktionale Sicht,
  Aussteifungssystem, Schichtaufbau, Eindeckung, Hüllkonstruktion,
  Befestigungssystem) sind ausdrücklich **nicht** Gegenstand dieses
  Eintrags und werden in eigenen Folgeeinträgen definiert, sobald
  sie im Tool benötigt werden — bzw. existieren bereits als eigene
  Glossarbegriffe (insbesondere `tragwerk`, das ontologisch eine
  Spezialisierung von Bausystem ist; siehe Folgearbeit).
---

## Prosa-Definition

Ein **Bausystem** ist eine funktionale Gruppierung von Bauteilen
nach gemeinsamer konstruktiver oder bemessungstechnischer Aufgabe
mit eigener Identität, in der die Mitgliedschaft eines Bauteils
nicht-exklusiv ist und die Bauteile selbst lebenszyklisch
unabhängig vom Bausystem existieren.

## Mathematische Definition

Sei

- W das Weltkoordinatensystem (siehe `weltkoordinatensystem`),
- 𝓑 die Menge aller Bauteile im Sinne von `bauteil`,
- 𝒰 der UUID-Raum nach `uuid`,
- ℱ ein endlicher Funktions-Klassifikationsraum (z. B.
  {Tragwerk, Aussteifung, Hüllkonstruktion, Eindeckung,
  Schichtaufbau-Lage_n, Befestigungssystem, …}); die genaue
  Wertemenge wird in den konkreten Subtypen festgelegt.

Dann ist ein **Bausystem** ein Tupel

```
S := (uuid, mitglieder, funktion, bezeichnung?)
```

mit

- **uuid** ∈ 𝒰: technischer Surrogatschlüssel des Bausystems
  (Pflicht, persistent, RFC 9562 v7); externe Referenzen auf das
  Bausystem gehen ausschließlich auf diese UUID.
- **mitglieder** ⊂ 𝓑, mitglieder endlich: die Menge der Bauteile,
  die dem Bausystem funktional zugeordnet sind. Die leere Menge ist
  zulässig (ein Bausystem in Definition vor Bauteil-Zuordnung).
- **funktion** ∈ ℱ: die konstruktive oder bemessungstechnische
  Aufgabe, die die Mitglieder gemeinsam erfüllen.
- **bezeichnung?**: optionaler humanlesbarer Name (z. B.
  „Hauptdach-Tragwerk", „südliche Dachfläche").

und den Konsistenzbedingungen

1. **Nicht-Exklusive Mitgliedschaft** (zentrale Bausystem-
   Eigenschaft): In einem Modell mit Bausystem-Menge 𝒮ᴹ ist
   ```
   ∀ S₁, S₂ ∈ 𝒮ᴹ : S₁ ≠ S₂ ⇏ S₁.mitglieder ∩ S₂.mitglieder = ∅
   ```
   Mitgliedschaften können sich beliebig überlappen; ein Bauteil
   kann gleichzeitig Mitglied beliebig vieler Bausysteme sein. Auch
   die gleichzeitige Mitgliedschaft in einem Bausystem und einer
   Bauteilgruppe (`bauteilgruppe`) ist zulässig.
2. **Keine kaskadische Lebenszyklus-Bindung**: Wird das Bausystem
   S aus dem Modell entfernt, bleiben seine Mitglieder bestehen.
   Das Entfernen eines Bausystems löscht ausschließlich die
   Gruppierungs-Beziehung, nicht die Bauteile selbst.
3. **Mitglieder-Existenz**: Jedes Mitglied b ∈ mitglieder existiert
   unabhängig vom Bausystem; b ist auch ohne S ein vollständiges
   Bauteil. Die Mitgliedschaft b ∈ S.mitglieder ist eine
   **Beziehung**, kein konstituierender Bestandteil von b.
4. **Optionale Auswahl-Regel** (deklarativ vs. extensional): Ein
   Bausystem kann durch eine **explizite Mitgliederliste**
   (extensional) oder durch eine **Auswahl-Regel über Bauteilen**
   (intensional, z. B. „alle b ∈ 𝓑 mit b.istLastabtragend()")
   definiert sein. Beide Varianten sind zulässig; die intensionale
   Variante muss bei jeder Modell-Änderung neu ausgewertet werden,
   die extensionale ist eine eingefrorene Momentaufnahme. Die
   Wahl ist Modellierungs-Entscheidung pro Subtyp; in der
   formalen Definition genügt mitglieder ⊂ 𝓑 als Endergebnis.

Eine **eigene geometrische Punktmenge** des Bausystems ist
**optional** und nicht konstituierend: manche Bausysteme haben eine
Bezugsebene oder eine Hülle (z. B. eine Dachfläche als funktionales
Bausystem hat eine Trägerfläche), andere nicht (ein Tragwerk hat
keine eigene Hülle, sondern besteht aus den Geometrien seiner
Mitglieder). Wird eine geometrische Repräsentation modelliert, ist
sie eine zusätzliche Eigenschaft des Subtyps, nicht des
Bausystem-Oberbegriffs.

Die **abgeleitete geometrische Punktmenge** als Vereinigung der
Mitglieder-Punktmengen ist immer verfügbar:

```
G_W(S) := ⋃_{b ∈ mitglieder} G_W(b) ⊂ ℝ³.
```

## Wohldefiniertheit

- **Existenz**: Für jede funktionale Aufgabe, die mehrere Bauteile
  gemeinsam erfüllen, lässt sich ein Bausystem als Tupel
  (uuid, mitglieder, funktion, bezeichnung?) erfassen.
  Mindestkonfiguration: |mitglieder| = 0, funktion ∈ ℱ,
  bezeichnung = ⊥ (zulässig als noch nicht befülltes System in
  Definition).
- **Eindeutigkeit der Identität**: Innerhalb eines Modells gilt
  ∀ S₁, S₂ : (S₁ ≠ S₂) ⇒ (S₁.uuid ≠ S₂.uuid). Die Bausystem-UUID
  ist konstruktionsseitig zu vergeben (UUID v7 nach RFC 9562) und
  persistent.
- **Mitgliedschafts-Funktion ist nicht funktional**: Anders als bei
  `bauteilgruppe` kann ein Bauteil b mehreren Bausystemen
  angehören. Die Beziehung Bauteil → Bausystem ist eine **Relation**
  (Many-to-Many), keine Funktion. Diese Eigenschaft ist die
  zentrale strukturelle Differenz zu `bauteilgruppe`.
- **Konsistenz mit `bauteil`**: Jedes b ∈ mitglieder ist ein
  Bauteil im Sinne von `bauteil`. Die Mitgliedschaft fügt b keine
  zusätzlichen Pflichtfelder hinzu und ändert keine
  Bauteil-Eigenschaften.
- **Wohldefiniertheit bei intensionaler Auswahl-Regel**: Wenn S
  durch eine Auswahl-Regel φ : 𝓑 → {true, false} definiert ist,
  gilt mitglieder = { b ∈ 𝓑 | φ(b) = true } zum
  Auswertungszeitpunkt. Die Regel φ muss deterministisch und seitens
  des Modells reproduzierbar sein; bei nicht-deterministischer Regel
  ist das Bausystem nicht wohldefiniert.
- **Trivial wohldefinierte Mitglieder-Menge**: mitglieder ist als
  Menge unsortiert; alle Aussagen über das Bausystem sind invariant
  unter Permutation der Mitglieder.
- **Nicht-Zirkularität**: Die Definition verwendet die Primitive
  `punkt`, `vektor`, `weltkoordinatensystem`, `toleranzen`, `uuid`
  sowie den bereits definierten Begriff `bauteil`. Sie verweist
  nicht auf konkrete Subtypen (Tragwerk, Dachfläche-als-Sicht,
  Aussteifungssystem) und nicht auf `bauteilgruppe` (das ist ein
  orthogonaler Aggregations-Mechanismus, keine Voraussetzung).

## Erläuterung (nicht normativ)

Das Bausystem ist die ontologische Antwort auf eine Klasse von
funktionalen Sichten, die im Holzbau immer wieder auftauchen und
gemeinsame strukturelle Eigenschaften haben:

- Das **Tragwerk** eines Bauwerks ist die funktionale Sicht „alle
  lastabtragenden Bauteile". Ein Sparren ist Mitglied des Tragwerks,
  weil er Lasten trägt — er bleibt aber konstruktiv ein Sparren mit
  eigener Identität und kann gleichzeitig Mitglied der Dachfläche
  als funktionalem Bausystem sein.
- Eine **Dachfläche** als funktionale Sicht („alle Bauteile, die
  geometrisch zur südlichen Dachfläche gehören") sammelt Sparren,
  Schalung und Eindeckung dieser Dachseite. Derselbe Sparren ist
  gleichzeitig Mitglied des Tragwerks (lastabtragend) und Mitglied
  der Dachfläche (geometrisch zugehörig); diese Doppelmitgliedschaft
  ist genau der Punkt.
- Ein **Aussteifungssystem** sammelt alle Bauteile, die zur
  horizontalen Aussteifung beitragen (**Streben** (`strebe`),
  **Kopfbänder** (`kopfband`), Windrispen, aussteifende Schalungen).
  Auch hier sind die einzelnen Streben gleichzeitig Mitglieder des
  Tragwerks und des Aussteifungssystems.

In allen drei Beispielen sind die strukturellen Merkmale identisch:
**eigene Identität als Sicht/Klassifikation**, **nicht-exklusive
Mitgliedschaft**, **keine kaskadische Löschung**, **Bauteile
existieren unabhängig vom System**, **geometrische Eigenschaften
optional**. Diese Merkmalsgemeinsamkeit rechtfertigt den abstrakten
Oberbegriff Bausystem.

### DDD-Perspektive

Im Sinne von Domain-Driven Design ist ein Bausystem **kein
Aggregat im engeren Sinn** (Evans 2003 Kap. 6), sondern eine
Sicht, ein Tag oder eine Many-to-Many-Klassifikation. Die
Aggregate des Modells sind die Bauteile selbst (sowie die
Bauteilgruppen, siehe `bauteilgruppe`); das Bausystem ist eine
Klammer um eine Auswahl dieser Aggregate. Die Modifikations-Semantik
folgt daraus direkt: das Hinzufügen oder Entfernen einer
Bausystem-Mitgliedschaft ist eine Beziehungs-Operation, keine
Aggregat-Operation, und greift insbesondere nicht in die
Bauteil-Aggregate ein.

### Strukturelle Rolle: `begriffstyp: relation` und Asymmetrie zu Spezialisierungen

Das Bausystem trägt `begriffstyp: relation`, weil es eine **funktionale
Sicht** auf Bauteile ist: es führt **nicht-exklusive Mitgliedschaft**,
hat **keine eigenen partitiven Bestandteile** über die
Mitglieder-Beziehung hinaus und bindet die Mitglieder nicht an seinen
Lebenszyklus. Eine Spezialisierung des Bausystems darf strukturell
**mehr** leisten als die Wurzel und in diesem Fall einen anderen
`begriffstyp:` führen. Paradigmatisch ist `tragwerk`: fachlich ist es
ein Bausystem (die funktionale Sicht „lastabtragend"), strukturell aber
ein **Aggregat** (`begriffstyp: aggregat`), weil es zusätzlich zur
Bauteil-Mitgliedschaft eigene partitive Bestandteile (Verbindungen,
Auflager, Lastfälle) sowie eigene **Konsistenzbedingungen über der
Komposition** (Inzidenz, Zusammenhang, Lastpfad-Vollständigkeit) trägt.
Die daraus folgende Asymmetrie zwischen `oberbegriff:` (fachliche
Spezialisierungs-Linie) und `begriffstyp:` (strukturelle Rolle) ist
zulässig und beabsichtigt; sie ist in `_KONVENTIONEN.md` Sektion 3,
Erläuterung zu `relation`, normativ verankert.

### Abgrenzung zu Bauteilgruppe in einem Satz

Bausystem ist **funktionale Gruppierung mit nicht-exklusiver
Mitgliedschaft und ohne kaskadische Löschung**, Bauteilgruppe ist
**partitive Komposition mit exklusiver Mitgliedschaft und
kaskadischer Löschung**. Ein Bauteil kann zu beliebig vielen
Bausystemen, aber zu höchstens einer Bauteilgruppe gehören. Siehe
`hg_bauteilgruppe.md`.

### Mehrfachmitgliedschaft als Stärke, nicht als Schwäche

Die Tatsache, dass ein Sparren gleichzeitig im Tragwerk, in der
Dachfläche, im Aussteifungssystem und (falls vorhanden) in einer
Auswechslungs-Bauteilgruppe geführt wird, ist kein Modellierungs-
Konflikt, sondern die korrekte Repräsentation der konstruktiven
Realität: derselbe physische Sparren erfüllt mehrere Funktionen
gleichzeitig. Die ontologische Trennung zwischen Bauteilgruppe
(exklusiv) und Bausystem (nicht-exklusiv) erlaubt diese
Mehrfachzuordnung, ohne die exklusive Whole/Part-Beziehung der
Bauteilgruppen zu verletzen.

## Beziehungen

- **Oberbegriff**: derzeit `null`. Bauteilgruppe und Bausystem
  liegen auf einer eigenen Aggregats-Hierarchie neben Element
  (siehe Erläuterung in `hg_bauteilgruppe.md`).
- **Bestandteile (relational, nicht partitiv)**:
  - **Bauteile** (`bauteil`) als **Mitglieder** der Gruppierung;
    die Beziehung ist Many-to-Many, nicht Whole/Part.
  - **Funktion** (Klassifikation aus ℱ): die konstituierende
    funktionale Aufgabe.
- **Spezialisierungen** (eigene Einträge folgen oder existieren
  bereits, trigger-basiert):
  - **Tragwerk** (`tragwerk`) — **existiert bereits als
    Glossareintrag**: funktionale Sicht „alle lastabtragenden
    Bauteile". Ontologisch eine Spezialisierung von Bausystem;
    siehe Folgearbeit unten zur Frage einer formalen Anbindung.
  - **Aussteifungssystem** (`aussteifungssystem`): funktionale
    Sicht „alle Bauteile, die zur horizontalen Aussteifung
    beitragen".
  - **Dachfläche als funktionale Sicht** (`dachflaeche` führt
    derzeit den geometrischen Begriff; eine zusätzliche Lesart
    als funktionales Bausystem „alle Bauteile dieser Dachseite"
    ist denkbar, aber nicht Gegenstand dieses Eintrags).
  - **Schichtaufbau-Lage** (`dachaufbau` führt den Schichtaufbau
    als Aggregat; einzelne Lagen können als Bausysteme
    aufgefasst werden).
  - **Eindeckung** (`eindeckung`, Folgearbeit): funktionale Sicht
    „alle Eindeckungsbauteile (Ziegel, Schindeln, Bahnenware)".
  - **Hüllkonstruktion** (`huellkonstruktion`, Folgearbeit):
    Außenhülle des Bauwerks als funktionales System.
  - **Befestigungssystem** (`befestigungssystem`, Folgearbeit):
    funktionale Gruppierung von Verbindungsmitteln und Verbindern
    nach gemeinsamem Befestigungs-Zweck.
- **Verwendung**:
  - Bestandteil eines **Bauwerks** als funktionale Klassifikation.
  - Mehrere Bausysteme können auf denselben Bauteilen koexistieren
    (siehe Bedingung 1).
- **Abgrenzung**:
  - **Bauteilgruppe** (`bauteilgruppe`): partitive, exklusive
    Komposition; siehe oben und `hg_bauteilgruppe.md`.
  - **Bauteil** (`bauteil`): einzelner Bestandteil; ein Bausystem
    ist eine Beziehung über mehreren Bauteilen, kein Bauteil. Ein
    Bausystem ist insbesondere **nicht** selbst ein Element-Subtyp
    (siehe `element`).
  - **Tragwerk** (`tragwerk`): konkrete Spezialisierung von
    Bausystem für die Funktion „lastabtragend". Tragwerk hat
    derzeit `oberbegriff: null`, was vor der Einführung des
    Bausystem-Begriffs konsistent war; nach Einführung wäre
    `oberbegriff: bausystem` die strukturell saubere Anbindung
    (siehe Tragwerk-Beobachtung in der Folgearbeit unten).
  - **Verbindung** (`verbindung`): lokales Knoten-Aggregat aus
    Bauteilen, Verbindungsmitteln, Verbindern und Verstärkungen
    mit Fokus auf Kraftübertragung an einem Punkt; ist
    ontologisch ein partitives Aggregat (eigener
    `begriffstyp: aggregat`), kein Bausystem.
  - **Dachfläche** (`dachflaeche`): derzeit als geometrischer
    Begriff geführt (begrenzte ebene Fläche mit Neigung). Die
    Lesart als funktionales Bausystem über den Bauteilen einer
    Dachseite ist eine andere Begriffsschicht und nicht
    Gegenstand dieses Eintrags.
  - **Dachaufbau** (`dachaufbau`): aggregierter Schichtaufbau
    eines Daches; eigene Aggregat-Semantik, nicht primär ein
    funktionales Bausystem.
  - **Element** (`element`): Bausysteme sind keine
    Element-Subtypen (Memory `project_element_ontologie`).

## Implementierungshinweis

**Im aktuellen Glossarstand wird ausdrücklich keine Code-Klasse
`Bausystem` angelegt** (Memory `project_glossar_konventionen`,
Briefing `briefing_aggregations_begriffe.md`). Die ontologische
Vorbereitung lebt zunächst nur im Glossar; die Code-Klasse entsteht
zusammen mit dem ersten konkreten Subtyp, der in einem Tool
tatsächlich benötigt wird (vermutlich entweder eine konkrete
Tragwerk-Implementierung oder eine Dachflächen-Sicht). Der folgende
Skizzen-Code ist ausschließlich orientierender Implementierungs-
Hinweis.

```kotlin
// SKIZZE — nicht jetzt anlegen.
// Glossar: hg_bausystem.md

package domain.bauteil

import domain.bauteil.Bauteil
import java.util.UUID

/**
 * Bausystem: funktionale, nicht-exklusive Gruppierung von
 * Bauteilen nach gemeinsamer Aufgabe. Keine eigene Aggregat-
 * Identität im DDD-Sinn — die Mitglieder sind die Aggregate, das
 * Bausystem ist die Klammer.
 *
 * Sealed, weil konkrete Subtypen (Tragwerk, Aussteifungssystem,
 * Dachflächen-Sicht, Schichtaufbau-Lage, Eindeckung,
 * Hüllkonstruktion) eigene Funktion-Klassifikationen und eigene
 * Auswahl-Regeln tragen.
 */
sealed class Bausystem {
    abstract val uuid: UUID
    abstract val mitglieder: Set<Bauteil>      // extensional
    abstract val funktion: BausystemFunktion
    abstract val bezeichnung: String?

    // Keine Invariante "mitglieder.isNotEmpty()" — leere Bausysteme
    // sind in der Definitions-Phase zulässig.

    // Keine Invariante "Mitglieder gehören zu keinem anderen
    // Bausystem" — Mehrfachmitgliedschaft ist die zentrale
    // Eigenschaft.
}

enum class BausystemFunktion {
    TRAGWERK, AUSSTEIFUNG, HUELLKONSTRUKTION,
    EINDECKUNG, SCHICHTAUFBAU_LAGE, BEFESTIGUNGSSYSTEM,
    /* Folgearbeit: erweitern, sobald konkrete Subtypen entstehen */
}
```

- **Einheit**: Längen (sofern eine optionale Bausystem-Geometrie
  existiert) in mm (Double); Winkel intern in Radiant.
- **Identität**: `uuid` ist Pflicht und persistent (RFC 9562 v7);
  externe Referenzen auf ein Bausystem gehen ausschließlich auf
  diese UUID. Mitglieder werden über ihre Bauteil-UUIDs
  referenziert.
- **Invarianten** (im `init`-Block prüfen, bei Verletzung
  `Resultat.Fehler` bzw. `Entartet`-Variante; niemals Exception
  werfen):
  1. Keine Mindestgröße: `mitglieder.size >= 0` (leere Bausysteme
     in Definition zulässig).
  2. **Keine** Exklusivitäts-Prüfung gegen andere Bausysteme.
     Mehrfachmitgliedschaft ist die zentrale Eigenschaft und
     ausdrücklich zugelassen.
  3. Bei intensionaler Definition durch Auswahl-Regel φ: φ muss
     deterministisch sein; bei nicht-deterministischer Regel
     `Entartet.NichtDeterministischeAuswahlregel`.
- **Edge Cases**:
  - **Leeres Bausystem**: zulässig (Definition ohne Mitglieder).
  - **Bausystem mit einem Mitglied**: zulässig (z. B. ein
    einzelner Kragträger als alleiniges Tragwerk).
  - **Vollständige Überlappung mit anderem Bausystem**
    (S₁.mitglieder = S₂.mitglieder bei verschiedenen funktionen):
    zulässig (z. B. „Tragwerk" und „Holzkonstruktion" decken
    sich, wenn alle Bauteile aus Holz und tragend sind).
  - **Mitgliedschaft eines Bauteils in einer Bauteilgruppe und
    in einem Bausystem gleichzeitig**: zulässig (z. B. ein
    Wechselbalken einer Auswechslungs-Bauteilgruppe ist
    gleichzeitig Mitglied des Tragwerks-Bausystems).
  - **Entfernen eines Bauteils aus dem Modell**: das Bauteil wird
    automatisch aus allen Bausystem-Mitgliederlisten entfernt;
    die Bausysteme bleiben als Gruppierungen bestehen
    (gegebenenfalls leer).
- **Abgeleitete Eigenschaften** (als Funktionen, keine Felder):
  - `geometrieInWelt(): GeometrieInW` = ⋃_{b ∈ mitglieder} G_W(b).
  - `boundingBox(): AABB` = achsenparalleler Hüllquader in W über
    den Mitgliedern.
  - `enthaelt(b: Bauteil): Boolean` = `b in mitglieder`.
  - `auswahlregel(): (Bauteil) -> Boolean` (optional, bei
    intensional definierten Bausystemen): die deterministische
    Mitgliedschafts-Funktion.

## Quellen

**Primär (normativ):**

- ISO 16739-1:2024, „Industry Foundation Classes (IFC) for data
  sharing in the construction and facility management industries —
  Part 1: Data schema", insbesondere `IfcBuildingSystem` und
  `IfcRelAssignsToGroup`.
- buildingSMART International: *IFC4.3 Documentation* (Version
  4.3.2.0, 2024).
- DIN EN 1990:2010-12, „Eurocode: Grundlagen der Tragwerksplanung",
  Abschnitt 1.5.1.1.
- DIN EN 1995-1-1:2010-12, „Eurocode 5: Bemessung und Konstruktion
  von Holzbauten – Teil 1-1: Allgemeines", Abschnitte 1.5 und 5.
- SIA 260:2013, „Grundlagen der Projektierung von Tragwerken",
  Abschnitt 2.1.

**Sekundär:**

- Evans, E.: *Domain-Driven Design — Tackling Complexity in the
  Heart of Software.* Addison-Wesley 2003, insbes. Kap. 6.
- Vernon, V.: *Implementing Domain-Driven Design.* Addison-Wesley
  2013, insbes. Kap. 5 und 10.
- Lignum (Hrsg.): *Holzbautabellen HBT.* Lignum, Zürich,
  aktuelle Auflage.
- Blass, H. J.; Sandhaas, C.: *Ingenieurholzbau – Grundlagen der
  Bemessung.* KIT Scientific Publishing, Karlsruhe 2016.

**Korpus (nicht autoritativ):**

- Holzbau Deutschland, Merkblatt „Begriffe und Klassifizierungen
  für den Holzbau" (abgerufen 2026-05-09).
- Wikipedia, Lemmata „Tragwerk" und „Aussteifung" (abgerufen
  2026-05-09).

## Folgearbeit (trigger-basiert)

Konkrete Spezialisierungen werden definiert oder ontologisch
angebunden, sobald das jeweilige Tool sie benötigt:

- **`tragwerk` (existiert bereits)** — funktionale Sicht „alle
  lastabtragenden Bauteile". Strukturell eine Spezialisierung von
  Bausystem; eine formale Anbindung (`oberbegriff: bausystem` in
  `hg_tragwerk.md`) ist eine sinnvolle Folge-Korrektur, ist aber
  nicht Gegenstand dieses Eintrags und wird Eric zur Entscheidung
  vorgelegt (siehe Übergabe-Notiz dieses Auftrags).
- `aussteifungssystem` — Sicht über aussteifende Bauteile.
- `eindeckung` — Sicht über Eindeckungsbauteile (Ziegel,
  Schindeln, Bahnenware).
- `huellkonstruktion` — Sicht über die Außenhülle des Bauwerks.
- `befestigungssystem` — Sicht über Verbindungsmittel und
  Verbinder eines gemeinsamen Befestigungs-Zwecks.
- Erweiterte Lesart von `dachflaeche` als funktionales Bausystem
  „alle Bauteile dieser Dachseite" — wenn ein Tool diese Sicht
  braucht, als zusätzliche Begriffsschicht modellieren.

Außerdem als Folgearbeit auf Glossar-Ebene:

- Ggf. ein abstrakter Oberbegriff `aggregat` über
  `bauteilgruppe`, `bausystem`, `verbindung` und `tragwerk`, falls
  sich strukturelle Gemeinsamkeiten (eigene UUID, Gruppierungs-
  Beziehung) als hinreichend tragfähig erweisen — derzeit als
  offen geführt.
