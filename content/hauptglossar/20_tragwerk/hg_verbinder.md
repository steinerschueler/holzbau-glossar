---
id: verbinder
benennung: Verbinder
synonyme: [Verbindungselement]
abgelehnte_benennungen: [Anschlussmittel, Verbindung, Verbindungsmittel, Beschlag, "connector", "fitting", "Hardware"]
oberbegriff: element
begriffstyp: generisch
voraussetzungen: [element, uuid, verbindungsmittel, werkstoff, werkstoff_stahl, axiales_holz, toleranzen]
abgrenzung_zu: [bauteil, verbindungsmittel, verstaerkungselement, verbindung, element]
status: entwurf
theorie_pflichtig: required
quellen_primär:
  - "DIN EN 1995-1-1:2010-12 (Eurocode 5), Abschnitt 8.2.3 'Indirekte Verbindungen' (Verbindungselement zwischen zwei oder mehr Stäben, jeder Stab durch eigene Verbindungsmittel an das Verbindungselement angeschlossen)."
  - "DIN EN 1995-1-1:2010-12, Anhang A bzw. nationale Anhänge zu Verbindern (Balkenschuhe, Winkelverbinder)."
  - "EC5 Nationaler Anhang Deutschland (DIN EN 1995-1-1/NA), Verbindungselemente und Beschläge."
  - "SIA 265:2021 'Holzbau', Anhang A 'Verbindungen und Verbindungsmittel', Beschläge und Verbindungselemente."
  - "ISO 16739-1:2024 'Industry Foundation Classes (IFC) – Part 1: Data schema', Entität `IfcDiscreteAccessory` (Subtyp von `IfcElementComponent`); Predefined Types u. a. ANCHORPLATE, BRACKET, SHOE."
  - "design2machine: BTLx 2.x Specification (Stand 2024), Part-Element bzw. Reference für Beschläge."
  - "ETA-06/0106, 'Simpson Strong-Tie 3D-Verbinder' (BSD-, AKR-, AHL-Reihen)."
  - "ETA-11/0496, 'Rothoblaas Wing-Verbinder, Alumini-Balkenschuh, Plattenverbinder'."
  - "Z-9.1-447, 'Sherpa-Verbinder' (allgemeine bauaufsichtliche Zulassung, DIBt)."
  - "ETA-09/0322, 'BMF Balkenschuh, BMF-Verbinder'."
quellen_sekundär:
  - "Blass, H. J.; Sandhaas, C.: Ingenieurholzbau – Grundlagen der Bemessung. KIT Scientific Publishing, Karlsruhe 2016, Kap. 8.6 ff. 'Anschlüsse mit eingeschlitzten und außenliegenden Blechen'."
  - "Holzbau-Handbuch, Reihe 2 'Tragwerksplanung', Teil 1 'Verbindungen', Folge 4 'Anschlüsse mit Stahlblechformteilen', Informationsdienst Holz."
  - "Mönck, W.; Rug, W.: Holzbau – Bemessung und Konstruktion. 16. Aufl., Beuth, Berlin 2015, Kap. 7."
  - "Hersteller-Kataloge Simpson Strong-Tie, Rothoblaas, BMF, SFS, Würth — IFC-Modelle als IfcDiscreteAccessory."
quellenkonflikt: |
  Begriffsfeld:
  - **DIN EN 1995-1-1** spricht in 8.2.3 von „Verbindungselement"
    bzw. „indirekte Verbindung". Das deutsche „Verbinder" ist
    hier **synonym** mit dem Norm-Begriff „Verbindungselement".
  - **SIA 265** verwendet „Beschlag" und „Verbindungselement"
    weitgehend synonym.
  - In der Schweizer Praxis und in cadwork ist „Verbinder" der
    eingeführte Sammelbegriff (Balkenschuh-Verbinder, Sherpa-
    Verbinder, Schlitzblech-Verbinder).
  - **IFC** kennt für diese Klasse die Entität
    `IfcDiscreteAccessory` mit Predefined Types ANCHORPLATE,
    BRACKET, SHOE u. a. — explizit getrennt von
    `IfcMechanicalFastener` (Verbindungsmittel) und von
    `IfcBeam`/`IfcMember` (Bauteil).

  Eigene Festlegung:
  - **Verbinder** ist die **Hauptbenennung** dieses Glossars
    (kürzer, im Schweizer Holzbau-Sprachgebrauch fest verankert).
  - **Verbindungselement** ist als **Synonym** im Frontmatter
    geführt (entsprechend EC5 8.2.3). Der Begriff wird hier
    nicht als eigener Eintrag geführt, weil er denotational
    identisch ist.
  - **Beschlag** ist eine zimmermannssprachliche Variante mit
    leicht engerer Bedeutung (typisch flaches Blech-Element)
    und wird **nicht** als Synonym, sondern als
    abgelehnte Benennung geführt — nur wenn ein eigener Eintrag
    `beschlag` mit klar abgegrenzter Bedeutung definiert wird,
    rückt er ins Glossar.
  - **Anschlussmittel** wird ebenfalls als abgelehnte Benennung
    geführt: zu nahe an `Verbindungsmittel`, in der Praxis
    ungebräuchlich und damit verwechslungsanfällig.

  Sherpa-Verbinder, Knapp-Verbinder, Pitzl-Verbinder etc. sind
  hersteller-spezifische, ETA-zugelassene Verbinder-Bauarten;
  sie alle erben den Begriff „Verbinder" und werden im IFC
  ebenfalls als `IfcDiscreteAccessory` ausgeliefert.

  Sonderfall: Ein Knotenblech, das selbst als druck- oder
  zugbeanspruchtes Tragglied ausgelegt ist (z. B. als Diagonale
  in einem Stahlfachwerk), könnte begrifflich als Bauteil
  klassifiziert werden. In dieser App wird die Trennung **nach
  Funktion im Holzbau-Tragwerk** gezogen: das Knotenblech
  vermittelt zwischen Holzstäben und ist daher **Verbinder**.
  Tritt es als eigenständiges, durch andere Verbindungsmittel
  angeschlossenes Stahltragglied auf, wird es als
  Stahl-Bauteil (eigene Folge-Klasse) modelliert.

  Aluminiumlegierungen (z. B. bei Sherpa-Verbindern) sind in der
  aktuellen Werkstoff-Hierarchie nicht als eigene Klasse geführt;
  sie werden konventionell der `werkstoff_stahl`-Klasse zugeordnet
  (analoge ETA- und Bemessungsführung). Eine eigene Klasse
  `werkstoff_aluminium` ist als Folgearbeit vorgesehen; bis dahin
  führt das `voraussetzungen`-Feld nur `werkstoff_stahl` und
  `axiales_holz`.
---

## Prosa-Definition

Ein **Verbinder** ist ein Element der App-Ontologie, das als
vermittelndes Bauteil zwischen zwei oder mehr Holzbauteilen
eingesetzt wird, das selbst durch Verbindungsmittel an die
verbundenen Bauteile befestigt wird, das in der Regel aus Stahl
(seltener aus Holz oder Verbundwerkstoff) besteht und dessen
Verwendung zu einer indirekten Verbindung im Sinne von DIN EN
1995-1-1 Abschnitt 8.2.3 führt.

## Mathematische Definition

Sei

- 𝓔 die Menge der Elemente nach `element`,
- 𝓤 der UUID-Raum nach `uuid`,
- 𝓥𝓜 die Menge der Verbindungsmittel nach `verbindungsmittel`,
- 𝓦 die Menge der Werkstoffe (typisch Stahl S235 oder verzinkter
  Stahl, Edelstahl A2/A4; Hartholz für Holzlaschen),
- 𝓥𝓑_τ die Menge der Verbinder-Typen
  ```
  𝓥𝓑_τ := { Balkenschuh, Winkelverbinder, Knotenblech,
            Schlitzblech, SherpaVerbinder, KnappVerbinder,
            PitzlVerbinder, Holzlasche, Zugband, Druckband,
            Verbindungsplatte }
  ```
  (sealed enum; eigene Folge-Einträge),
- 𝓔𝓣𝓐 die Menge der ETA-Referenzen,
- 𝓢𝓰 die Menge der Stahlgüten.

Dann ist ein **Verbinder** das Tupel

```
VB := (uuid, geometrie, lokale_platzierung, werkstoff,
       typ, befestigt_durch,
       eta_zulassung?, stahlguete?,
       positionsnummer?, produktkennzeichnung?, bezeichnung?)
```

mit den von `element` ererbten Pflichtfeldern

- **uuid** ∈ 𝓤,
- **geometrie** ∈ 𝓖_VB ⊂ 𝓖 (typabhängig: 2D-Plattengeometrie mit
  Dicke und Bohrlochmuster für Bleche und Balkenschuhe;
  Profilgeometrie für Winkelverbinder; Polyeder für 3D-
  Verbinder wie Sherpa),
- **lokale_platzierung** ∈ SE(3),
- **werkstoff** ∈ 𝓦,

und den verbinder-spezifischen Pflichtfeldern

- **typ** ∈ 𝓥𝓑_τ,
- **befestigt_durch** ⊂ 𝓤 mit |befestigt_durch| ≥ 1: die UUIDs
  derjenigen Verbindungsmittel, die den Verbinder an den
  beteiligten Bauteilen befestigen,

und den Optionalfeldern

- **eta_zulassung** ∈ 𝓔𝓣𝓐 ∪ {⊥} (für ETA-zugelassene
  Hersteller-Verbinder: Simpson Strong-Tie ETA-06/0106,
  Rothoblaas ETA-11/0496, Sherpa Z-9.1-447, BMF ETA-09/0322 u. a.),
- **stahlguete** ∈ 𝓢𝓰 ∪ {⊥},
- **positionsnummer**, **produktkennzeichnung**, **bezeichnung**
  wie in `element`.

Es ist 𝓥𝓑 ⊂ 𝓔, d. h. die Menge der Verbinder ist eine disjunkte
Teilmenge der Element-Menge.

Die durch einen Verbinder vermittelte Menge der **mittelbar
verbundenen Bauteile** ergibt sich (transitiv) aus den
Verbindungsmitteln:

```
verbundene_bauteile(VB) := ⋃_{vm ∈ befestigt_durch} verbindet(vm).
```

## Wohldefiniertheit

- **Existenz**: Für jeden konkreten in einem Tragwerk eingebauten
  Verbinder lässt sich das obige Tupel erfassen. Mindest-
  konfiguration: typ = Balkenschuh, geometrie als 2D-Plattenkörper,
  |befestigt_durch| = 2 (eine Schraubengruppe in den Träger, eine
  in den Hauptträger).
- **Eindeutigkeit der Identität**: über `uuid` (geerbt von `element`).
- **Geometrie-Konsistenz**: Die Geometrie ist im lokalen
  Verbinder-Koordinatensystem zu interpretieren, dessen Lage durch
  `lokale_platzierung` ∈ SE(3) festgelegt wird. Bohrlochmuster im
  Verbinder müssen geometrisch mit den Achsen der Verbindungsmittel
  in `befestigt_durch` zusammenpassen (Konsistenzbedingung; im
  Glossar zugesichert, formaler Nachweis in der Geometrie-Schicht).
- **Befestigung**: |befestigt_durch| ≥ 1 ist zwingend
  (ein Verbinder ohne Verbindungsmittel ist kein Verbinder, sondern
  ein lose eingelegtes Stück Stahl). Typisch ist
  |befestigt_durch| ≥ 2: mindestens ein Verbindungsmittel pro
  angeschlossenem Bauteil. **Foreign-Key-Regel**
  (siehe `uuid`): die Liste enthält ausschließlich UUIDs.
- **Mindestens zwei mittelbar verbundene Bauteile**:
  |verbundene_bauteile(VB)| ≥ 2 — sonst handelt es sich nicht um
  eine vermittelnde Funktion. (Ausnahme: Wandanker an einer
  Betonwand, der nur ein Holzbauteil mit dem Untergrund verbindet;
  dies ist ein Sonderfall „Verankerung" und wird im Datenmodell
  durch eine virtuelle Bauteil-UUID `Untergrund` aufgelöst.)
- **Disjunktheit zu Bauteil und Verbindungsmittel**: Ein Verbinder
  ist **kein Bauteil** im Sinne von `bauteil` (er ist nicht primär
  tragend/raumbildend, sondern vermittelnd) und **kein
  Verbindungsmittel** (er ist nicht das einzelne kraftübertragende
  Stück, sondern das Stück, **durch** das Verbindungsmittel
  hindurchgehen).
- **Indirekte Verbindung**: Die Wirkung eines Verbinders entspricht
  dem EC5-Konzept der **indirekten Verbindung** (8.2.3): die
  beteiligten Stäbe haben je einen Anschluss an das vermittelnde
  Element, statt direkten Holz-Holz-Kontakt. Dies ist eine
  funktionale Eigenschaft, formal nicht in Zahl gefasst, aber als
  Klassifikations-Kriterium im Glossar fixiert.
- **Nicht-Zirkularität**: Die Definition stützt sich auf `element`,
  `uuid`, `verbindungsmittel`, `werkstoff` und `toleranzen`. Sie
  verweist auf `verbindung`, `bauteil`, `verstaerkungselement`
  ausschließlich in der Abgrenzung.

## Erläuterung (nicht normativ)

### Werkstoff

Verbinder haben **typisch Werkstoff `werkstoff_stahl`** (verzinkter
Stahl S235 / S355 für Balkenschuhe, Winkelverbinder, Schlitzbleche
und Knotenbleche; Edelstahl A2 / A4 für korrosionsbeanspruchte
Anwendungen; Aluminiumlegierungen bei Sherpa-Verbindern als
Sonderfall, der hier konventionell der Stahl-Klasse zugeordnet
wird, weil ETA und Bemessung analog laufen). **Holzlaschen**
sind die Ausnahme: sie haben Werkstoff `axiales_holz` (Hartholz
oder zur Hauptkonstruktion passendes Konstruktionsholz) und folgen
in der Bemessung einem eigenen Versagens-Regime (Holz-Lochleibung,
Spaltbruchgefahr).

### Typische Verbinder-Bauarten

| Typ                  | Funktion                                | Beispiele |
|----------------------|-----------------------------------------|-----------|
| **Balkenschuh**      | hängender Trägeranschluss an Hauptträger | Simpson BSI, Rothoblaas WHT, BMF, Knapp K |
| **Winkelverbinder**  | rechtwinkliger Anschluss zweier Stäbe   | Simpson AKR, BMF AB, Rothoblaas ALUMINI |
| **Knotenblech**      | mehrteiliger Knoten mit Stabdübeln/Bolzen | Schlitzblech-Knoten in BSH-Trägern |
| **Schlitzblech**     | eingeschlitztes Stahlblech mit Stabdübeln | EC5 8.6, BSH-Stützenfuß |
| **Sherpa-Verbinder** | aluminiumgegossener Schwalbenschwanz    | Z-9.1-447 |
| **Knapp-Verbinder**  | Holz-Holz-Verbinder mit gehärteten Klauen | RICON, MEGANT |
| **Holzlasche**       | beidseitig anliegendes Holzbrett        | klassischer zimmermannsmäßiger Stoß |
| **Zugband**          | Stahlband, das Zugkräfte zwischen Bauteilen weiterleitet | Sturmanker, Holz-Beton-Verbund |

### Verbinder vs. Verbindungsmittel — die EC5-Trennung

DIN EN 1995-1-1 trennt in Kap. 8 systematisch:

- **Verbindungsmittel** (Kap. 8.3 ff.): das einzelne Stück (Nagel,
  Schraube, Bolzen, Stabdübel) — ein Verbindungsmittel überträgt
  Lasten **direkt** zwischen Holzfasern oder zwischen Holz und Stahl.
- **Verbindungselement** = Verbinder (Kap. 8.2.3): ein
  vermittelndes, oft stählernes Bauteil, das **selbst** durch
  Verbindungsmittel angeschlossen ist — die Lastübertragung erfolgt
  dann **indirekt** über das Verbindungselement.

Die App folgt dieser Trennung strikt: ein einzelner Stabdübel ist
ein Verbindungsmittel, ein eingeschlitztes Knotenblech mit
mehreren Stabdübeln ist ein Verbinder, befestigt durch n
Verbindungsmittel.

### IFC- und BTLx-Mapping

| Element             | IFC                                                | BTLx                                |
|---------------------|----------------------------------------------------|-------------------------------------|
| Bauteil             | IfcBeam / IfcColumn / IfcMember / IfcPlate         | Part mit @GUID                      |
| Verbindungsmittel   | IfcMechanicalFastener (`IfcElementComponent`)      | Processing oder eigenes Part        |
| **Verbinder**       | **IfcDiscreteAccessory** (`IfcElementComponent`)   | **eigenes Part oder Reference**     |
| Verstärkungselement | IfcMechanicalFastener + Pset_Function              | wie VM + Funktionsattribut          |
| Verbindung          | IfcRelConnectsElements (Beziehung)                 | implizit über mehrere Parts         |

Der Verbinder hat **immer** eine eigene Stückliste-relevante
Identität (er wird als ETA-Bauteil bestellt, nummeriert,
geliefert, montiert) und wird in BTLx daher als eigenes `Part`
oder als `Reference` geführt — anders als ein Standardnagel, der
im BTLx-Processing aufgeht.

### Stücklisten-Trennung

Verbinder haben **eigene Stücklisten**, getrennt von Bauteil- und
Verbindungsmittel-Stücklisten. Hersteller liefern Verbinder mit
ETA-Nummer, Bestellnummer und WPK-Zertifikat; im cadwork-Workflow
ist die „Verbinderliste" eine eigene Sicht.

## Beziehungen

- **Oberbegriff**: `element`.
- **Spezialisierungen** (eigene Einträge folgen):
  - **Balkenschuh** (`balkenschuh`): hängender Trägeranschluss.
  - **Winkelverbinder** (`winkelverbinder`): rechtwinkliger
    Anschluss.
  - **Knotenblech** (`knotenblech`): mehrteiliger Knoten.
  - **Schlitzblech** (`schlitzblech`): eingeschlitztes Stahlblech.
  - **Sherpa-Verbinder** (`sherpa_verbinder`): Aluguss-Verbinder.
  - **Holzlasche** (`holzlasche`): zimmermannsmäßiger Holzverbinder.
  - **Zugband** (`zugband`): Stahlband zur Zugkraft-Übertragung.
- **Bestandteile (partitiv)**: alles geerbt von `element` plus
  typ, befestigt_durch.
- **Verwendung**:
  - Bestandteil einer **Verbindung** (`verbindung`): der Verbinder
    ist Aggregatbestandteil neben Bauteilen, Verbindungsmitteln
    und ggf. Verstärkungselementen.
  - Bestandteil eines **Tragwerks** (`tragwerk`): erweitert die
    Element-Menge.
- **Abgrenzung**:
  - **Verbindungsmittel** (`verbindungsmittel`): das einzelne
    kraftübertragende Stück (Nagel, Schraube, Bolzen, Stabdübel).
    Verbindungsmittel sind das, **womit** der Verbinder befestigt
    wird; der Verbinder ist das, **was** befestigt wird. Anders
    formuliert: Verbindungsmittel gehen **durch** den Verbinder
    in das Bauteil.
  - **Verstärkungselement** (`verstaerkungselement`): ein
    Verbindungsmittel in Verstärkungsfunktion mit eigener axialer
    Bemessung. Verbinder hingegen ist ein **eigenes Stück Stahl/
    Holz**, nicht eine Funktionsrolle eines Verbindungsmittels.
  - **Bauteil** (`bauteil`): tragend/raumbildend mit Querschnitts-
    bemessung nach EC5 Kap. 6. **Sonderfall**: wenn ein Knotenblech
    selbst als druck- oder zugbeanspruchtes Tragglied (z. B. als
    Diagonale) ausgelegt ist und nicht primär Holzstäbe vermittelt,
    wird es als Stahl-Bauteil (eigene Folge-Klasse) modelliert,
    nicht als Verbinder. Die Klassifikations-Frage ist
    funktional zu entscheiden: vermittelnd zwischen Holzstäben →
    Verbinder; primär tragend ohne vermittelnde Funktion → Bauteil.
  - **Verbindung** (`verbindung`): Aggregat-Klasse, die einen
    Verbinder enthalten kann. Der Verbinder ist Bestandteil der
    Verbindung, nicht selbst die Verbindung.
  - **Element** (`element`): abstrakter Oberbegriff;
    Verbinder ist eine konkrete Subklasse.

## Implementierungshinweis

Datentyp (Domänen-Schicht, Kotlin, Schicht
`domain.element.verbinder`):

```kotlin
package domain.element.verbinder

import domain.element.Element
import domain.geometrie.Geometrie
import domain.geometrie.LokalePlatzierung
import domain.holzbau.Werkstoff
import domain.identifikation.Positionsnummer
import domain.identifikation.Produktkennzeichnung
import domain.identifikation.Stahlguete
import domain.identifikation.ETAReferenz
import java.util.UUID

/** Verbinder-Typ. */
sealed interface VerbinderTyp {
    data object Balkenschuh        : VerbinderTyp
    data object Winkelverbinder    : VerbinderTyp
    data object Knotenblech        : VerbinderTyp
    data object Schlitzblech       : VerbinderTyp
    data object SherpaVerbinder    : VerbinderTyp
    data object KnappVerbinder     : VerbinderTyp
    data object PitzlVerbinder     : VerbinderTyp
    data object Holzlasche         : VerbinderTyp
    data object Zugband            : VerbinderTyp
    data object Druckband          : VerbinderTyp
    data object Verbindungsplatte  : VerbinderTyp
}

/**
 * Verbinder: vermittelndes Bauteil zwischen Holzstäben, das selbst
 * durch Verbindungsmittel befestigt wird (EC5 8.2.3 indirekte
 * Verbindung).
 *
 * Glossar: hg_verbinder.md
 *
 * IFC: IfcDiscreteAccessory (Subtyp von IfcElementComponent).
 * BTLx: eigenes Part mit @GUID oder Reference.
 *
 * Synonym laut EC5: Verbindungselement.
 */
data class Verbinder(
    override val uuid: UUID,
    override val geometrie: Geometrie,
    override val lokalePlatzierung: LokalePlatzierung,
    override val werkstoff: Werkstoff,
    val typ: VerbinderTyp,
    val befestigtDurch: List<UUID>,    // FK auf Verbindungsmittel-UUIDs, |...| >= 1
    val etaZulassung: ETAReferenz? = null,
    val stahlguete: Stahlguete? = null,
    override val positionsnummer: Positionsnummer? = null,
    override val produktkennzeichnung: Produktkennzeichnung? = null,
    override val bezeichnung: String? = null
) : Element {
    init {
        // 1. befestigtDurch.isNotEmpty()
        // 2. befestigtDurch.all { it != uuid }   (kein Selbstbezug)
        // 3. befestigtDurch.distinct().size == befestigtDurch.size
    }
}
```

- **Einheit**: Längen in mm (Double). Winkel intern in Radiant.
- **Identität**: `uuid` von `element` ererbt.
- **Foreign-Key-Regel**: `befestigtDurch` referenziert
  ausschließlich Verbindungsmittel-UUIDs. Die mittelbar verbundenen
  Bauteile werden nicht direkt persistiert, sondern über die
  Verbindungsmittel transitiv ermittelt.
- **IFC-Mapping**:
  - IFC-Klasse: `IfcDiscreteAccessory` (Subtyp von
    `IfcElementComponent`).
  - Predefined Types: ANCHORPLATE (Verankerungsplatte), BRACKET
    (Konsolen-/Winkelverbinder), SHOE (Balkenschuh), USERDEFINED
    (Sonstige; z. B. Sherpa).
  - Property Sets: `Pset_DiscreteAccessoryCommon`,
    `Pset_DiscreteAccessoryGeneral`.
  - Hersteller-BIM-Bibliotheken (Simpson Strong-Tie, Rothoblaas,
    BMF, Sherpa) liefern Verbinder als `IfcDiscreteAccessory` aus.
- **BTLx-Mapping**:
  - **Standardfall**: eigenes `Part` mit `@GUID`
    (entspricht `Verbinder.uuid`).
  - **Alternativfall**: `Reference` auf eine externe
    Hersteller-Bibliothek mit ETA-Bezug.
  - Die zugehörigen Bohrlöcher in den verbundenen Holz-Bauteilen
    werden als `Drilling`-Processings geführt — das sind nicht die
    Verbinder selbst, sondern die Bearbeitungen, die durch die
    Verbindungsmittel im Holz entstehen.
- **Edge Cases**:
  - **Verbinder ohne Verbindungsmittel** (|befestigtDurch| = 0):
    nicht erlaubt; `Entartet.UnbefestigterVerbinder`.
  - **Verbinder, der nur ein Bauteil mit dem Untergrund verbindet**
    (Wandanker an Beton): zulässig, sofern eine virtuelle Bauteil-
    UUID `Untergrund`/`Fundament` im Modell existiert. Das ist eine
    Modellierungs-Konvention, nicht eine Eigenschaft des Verbinders.
  - **Knotenblech als Tragglied** (Diagonale im Stahlfachwerk):
    nicht als Verbinder, sondern als Stahl-Bauteil modellieren.
  - **Holzlasche aus Hartholz**: Werkstoff = Holz, nicht Stahl;
    Konsistenz wird in der Bemessung beachtet (eigene
    Versagens-Mechanismen).
- **Abgeleitete Eigenschaften**:
  - `verbundeneBauteile(model: Modell): Set<UUID>` —
    transitiv ermittelt aus `befestigtDurch` und den
    `verbindet`-Listen der Verbindungsmittel.
  - `geometrieInWelt(): GeometrieInW` — Verbinder-Geometrie unter
    `lokalePlatzierung` transformiert nach W.
- **Bezeichner-Konvention** (CLAUDE.md): Domänen-Klasse heißt
  `Verbinder` (deutsch, Glossarbegriff). Synonym
  `Verbindungselement` (EC5) wird in KDoc erwähnt, aber nicht als
  zweite Klasse geführt.

## Quellen

**Primär (normativ):**

- DIN EN 1995-1-1:2010-12, „Eurocode 5 – Bemessung und
  Konstruktion von Holzbauten", Abschnitt 8.2.3 sowie
  Verbinder-spezifische Abschnitte.
- DIN EN 1995-1-1/NA, deutscher Nationaler Anhang.
- SIA 265:2021, „Holzbau", Anhang A.
- ISO 16739-1:2024, IFC-Entität `IfcDiscreteAccessory`.
- design2machine: *BTLx 2.x Specification* (Stand 2024).
- ETA-06/0106 (Simpson Strong-Tie 3D-Verbinder).
- ETA-11/0496 (Rothoblaas Verbinder-Familie).
- Z-9.1-447 (Sherpa-Verbinder, DIBt).
- ETA-09/0322 (BMF Balkenschuh).

**Sekundär:**

- Blass, H. J.; Sandhaas, C.: *Ingenieurholzbau – Grundlagen der
  Bemessung.* KIT Scientific Publishing, Karlsruhe 2016, Kap. 8.6 ff.
- Holzbau-Handbuch, Reihe 2, Teil 1, Folge 4 (Anschlüsse mit
  Stahlblechformteilen), Informationsdienst Holz.
- Mönck, W.; Rug, W.: *Holzbau – Bemessung und Konstruktion.*
  16. Auflage, Beuth, Berlin 2015, Kap. 7.
- Hersteller-Kataloge: Simpson Strong-Tie, Rothoblaas, BMF, SFS,
  Würth, Knapp, Pitzl, Sherpa.

**Korpus (nicht autoritativ):**

- Holzbau Deutschland, Merkblatt „Begriffe und Klassifizierungen
  für den Holzbau" (abgerufen 2026-05-08).
- Wikipedia, Lemma „Holzverbinder" (abgerufen 2026-05-08).
