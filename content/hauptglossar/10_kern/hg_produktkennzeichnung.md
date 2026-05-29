---
id: produktkennzeichnung
benennung: Produktkennzeichnung
synonyme: ["Sortier-/CE-Kennzeichnung", "Material- und Chargenkennzeichnung", "Werks-Kennzeichnung"]
abgelehnte_benennungen: [Materialkennung, Holzstempel, Sortierstempel, Chargennummer, "marking", "product label", "batch id"]
oberbegriff: null
begriffstyp: aggregat
voraussetzungen: []
abgrenzung_zu: [uuid, positionsnummer, bezeichnung, werkstoff, festigkeitsklasse, abbundzeichen]
status: entwurf
subglossar_pendant: notwendig
quellen_primär:
  - "DIN 4074-1:2012-06, 'Sortierung von Holz nach der Tragfähigkeit — Teil 1: Nadelschnittholz'. Anforderungen an Sortier- und Werks-Kennzeichnung (Sortierklasse S 7 / S 10 / S 13, Holzart-Kurzzeichen, Hersteller-Code)."
  - "DIN EN 14080:2013-09, 'Holzbauwerke — Brettschichtholz und Balkenschichtholz — Anforderungen', insbesondere Anhang ZA (CE-Kennzeichnung): Hersteller-Identifikation, Festigkeitsklasse, Klebstofftyp, Produktionswoche, Notifikations-Stelle, WPK-Zertifikatnummer."
  - "DIN EN 14081-1:2019-10, 'Holzbauwerke — Nach Festigkeit sortiertes Bauholz mit rechteckigem Querschnitt — Teil 1: Allgemeine Anforderungen'. CE-Kennzeichnung sortierten Vollholzes."
  - "DIN EN 14374:2005-02, 'Holzbauwerke — Furnierschichtholz für tragende Zwecke — Anforderungen' (LVL, CE-Kennzeichnung)."
  - "Verordnung (EU) Nr. 305/2011 (Bauproduktenverordnung, CPR), Artikel 8–11 (CE-Kennzeichnung), Artikel 4 (Leistungserklärung DoP)."
  - "ISO 16739-1:2024, 'Industry Foundation Classes (IFC) — Part 1: Data schema', Material-Resource und Property Sets `Pset_MaterialWoodBasedBeam`, `Pset_MaterialWoodBasedPanel`."
quellen_sekundär:
  - "Mönck, W.; Rug, W.: Holzbau — Bemessung und Konstruktion. 16. Auflage, Beuth, Berlin 2015, Kap. 3 (Werkstoff Holz, Sortierung, Klassifikation)."
  - "Blass, H. J.; Sandhaas, C.: Ingenieurholzbau — Grundlagen der Bemessung. KIT Scientific Publishing, Karlsruhe 2016, Kap. 2 (Holz als Werkstoff)."
  - "Holzbau Deutschland — Informationsdienst Holz: Holzbau-Handbuch, Reihe 1 (Werkstoff Holz), Teil 1."
  - "Lignum (Hrsg.): Lignatec — diverse Hinweise zur CE-Kennzeichnung von Holzbauprodukten."
  - "Gerner, M.: Fachwerk — Instandsetzung, Sanierung, Neubau. DVA, 7. Auflage 2007 (historisch zu Abbundzeichen)."
  - "Krämer, V.: Grundwissen des Zimmerers. 7. Auflage, Bruderverlag, Köln 2018 (historisch zu Abbundzeichen, Sortierstempel)."
  - "design2machine: BTLx 2.x Specification (Stand 2024), Material-Element."
quellenkonflikt: |
  Anders als bei der Positionsnummer existiert für die
  Produktkennzeichnung eine **harte normative Grundlage**: Die
  DIN 4074-Reihe (Vollholz-Sortierung), DIN EN 14080 (BSH/BalkSH),
  DIN EN 14081 (CE-Vollholz), DIN EN 14374 (LVL) und die EU-CPR
  305/2011 schreiben Inhalte und Form der Kennzeichnung vor —
  abhängig vom Werkstoff. Der Begriff „Produktkennzeichnung" ist
  also normativ scharf, aber **werkstoffspezifisch
  ausdifferenziert**: Vollholz-Sortierstempel und CE-Etikett auf
  BSH unterscheiden sich in Inhalt und Form.

  Eigene Festlegung in diesem Glossar:

  - **Produktkennzeichnung** ist im Glossar ein **Aggregat-
    Begriff**: ein Sammelfeld, das je nach Werkstoff
    unterschiedliche Pflicht- und Optionalfelder trägt
    (Sortierklasse, Hersteller, Festigkeitsklasse, Klebstoff,
    Produktionswoche, WPK-Zertifikat, Notifikations-Stelle …).
  - Die konkreten Felder werden je Werkstoff-Klasse als
    Subtypen-Schema geführt (Vollholz nach DIN 4074-1, BSH nach
    DIN EN 14080, FSH nach DIN EN 14374). Die App speichert die
    relevante Variante.
  - Identifiziert wird die **Charge / Lieferung / das Produkt**,
    **niemals die Einbauposition** (vgl. Memory
    `project_bauteil_identifikation`).
  - **Verortung am Werkstoff, nicht am Element**: Die
    Produktkennzeichnung ist Pflichtfeld eines Werkstoffs
    (`werkstoff.produktkennzeichnung`), nicht direktes Feld eines
    Elements. Ein Element greift indirekt zu, über
    `element.werkstoff.produktkennzeichnung`. Die Memory-Festlegung
    `project_bauteil_identifikation` benennt drei orthogonale
    Identifikator-Spuren am Element (UUID, Positionsnummer,
    Produktkennzeichnung); die dritte Spur ist eine
    **Modellierungs-Sicht**, die in der App auf der Werkstoff-Ebene
    realisiert ist. Eine Pflichtsetzung gilt nur bei zertifizierten
    Werkstoffen (CE-pflichtige Produkte); bei nicht-zertifizierten
    Werkstoffen (Bestand, Sanierung) ist die Produktkennzeichnung
    optional.
  - **Mehrfachzuordnung**: Eine Charge wird typischerweise auf
    mehrere Elemente verteilt (1 → n); ein Element kann in
    seltenen Fällen aus mehreren Chargen zusammengesetzt sein
    (z. B. Fügeholz mit zwei Bezugsquellen). Beide Richtungen
    sind in der Datenstruktur zulässig.
  - **Historisches Abbundzeichen** (römische Ziffern mit
    Beizeichen für Wand und Geschoss; Gerner 1992, Krämer 2018)
    ist NICHT genormt und im modernen CNC-Abbund praktisch
    durch CAD-IDs ersetzt. Es wird hier **nicht** als
    Produktkennzeichnung geführt; in `abgrenzung_zu` erwähnt,
    eigener historischer Eintrag `abbundzeichen` (Folgearbeit)
    möglich.

  Begriffstyp `aggregat` ist eindeutig: mehrere normativ
  vorgeschriebene Felder werden zu einem Konzept zusammengefasst.
  Eine Lesart als `merkmal` (mit dem Hauptfeld „Festigkeitsklasse"
  als Surrogat) wäre eine unzulässige Vereinfachung, weil die
  CE-Kennzeichnung nach DIN EN 14080 mehrere Pflichtfelder hat,
  von denen die Festigkeitsklasse nur eines ist.
---

## Prosa-Definition

Eine **Produktkennzeichnung** ist die normativ verbindliche
Identifikation eines Holzwerkstoff-**Produkts** (Charge,
Lieferung, Einzelstück) im Sinne der einschlägigen Sortier- und
Produktnormen (DIN 4074-1 für Vollholz-Sortierung,
DIN EN 14080 / Anhang ZA für Brettschichtholz und
Balkenschichtholz, DIN EN 14081-1 für CE-zertifiziertes Vollholz,
DIN EN 14374 für Furnierschichtholz, EU-CPR 305/2011 als
CE-Rahmenwerk), die je nach Werkstoffart in unterschiedlicher
Form (Sortierstempel, CE-Etikett, Lieferschein-Eintrag)
ausgeführt ist und die in der App als Aggregat aus normativ
vorgegebenen Feldern (Sortierklasse, Holzart-Kurzzeichen,
Hersteller-Identifikation, Festigkeitsklasse, Klebstofftyp,
Produktionswoche, WPK-Zertifikatnummer, Notifikations-Stelle)
geführt wird, wobei die Produktkennzeichnung die **Charge** und
nicht die Einbauposition identifiziert.

## Mathematische Definition

Die Produktkennzeichnung ist nach Werkstoffart variabel; der
gemeinsame Rahmen ist:

Sei

- ℋ die Menge der Holzwerkstoff-Klassen (Vollholz, BSH, BalkSH,
  FSH/LVL, BSP, Plattenwerkstoff …),
- 𝒯ₕ die Menge der für die Werkstoff-Klasse h ∈ ℋ normativ
  vorgeschriebenen Pflichtfelder,
- 𝒪ₕ die Menge der für h optionalen Felder (z. B. Sortierer-
  Identifikation bei DIN 4074-1).

Eine **Produktkennzeichnung** ist ein Tupel

```
R := (h, t, o)
```

mit

- **h** ∈ ℋ                  (Werkstoff-Klasse),
- **t** ∈ 𝒯ₕ              (vollständig belegtes Tupel der
                              Pflichtfelder gemäß einschlägiger
                              Norm),
- **o** ⊆ 𝒪ₕ              (optional belegte Felder).

Beispiele konkreter 𝒯ₕ:

**Vollholz nach DIN 4074-1:2012** (Sortierstempel):

```
𝒯_Vollholz_DIN4074  :=  {
   sortierklasse  ∈ { S 7, S 10, S 13, MS 7, MS 10, MS 13 },
   holzart        ∈ Kurzzeichen-Liste (z. B. C24, C30 sind
                                        Festigkeitsklassen,
                                        Holzart kodiert getrennt),
   hersteller_id  ∈ String,
}
```

**Vollholz CE nach DIN EN 14081-1:2019**:

```
𝒯_Vollholz_EN14081  :=  𝒯_Vollholz_DIN4074  ∪  {
   festigkeitsklasse  ∈ { C14, C16, C18, C20, C22, C24, C27,
                          C30, C35, C40, C45, C50, … },
   notifikations_stelle ∈ String,
   ce_etikett_jahr      ∈ ℕ (4 Ziffern),
}
```

**BSH nach DIN EN 14080:2013, Anhang ZA** (CE-Kennzeichnung):

```
𝒯_BSH_EN14080  :=  {
   hersteller_id          ∈ String,
   festigkeitsklasse      ∈ { GL20h, GL22h, GL24h, GL26h, GL28h,
                              GL30h, GL32h,
                              GL20c, GL22c, GL24c, GL26c, GL28c,
                              GL30c, GL32c },
   klebstofftyp           ∈ { I, II } (DIN EN 301),
   produktionswoche       ∈ {1, …, 53} × ℕ_Jahr,
   notifikations_stelle   ∈ String,
   wpk_zertifikat_nummer  ∈ String,
   ce_etikett_jahr        ∈ ℕ,
}
```

**FSH/LVL nach DIN EN 14374:2005**: analog 𝒯_LVL mit eigenen
Pflichtfeldern (Querschnitt, Dichteklasse, …).

Die App speichert die Produktkennzeichnung als
**Summen-/Sealed-Type** über die Werkstoffklassen mit jeweils
eigenem Feldsatz (siehe Implementierungshinweis).

**Beziehung Charge ↔ Element**: Sei 𝓡 die Menge aller
Produktkennzeichnungen, 𝓔 die Menge aller Elemente. Dann ist die
Charge-Element-Relation

```
charge_in : 𝓔 → 𝓡 ∪ {⊥}     (Element → Charge oder „nicht gesetzt"),
elemente_aus_charge : 𝓡 → 𝒫(𝓔)  (Charge → Element-Menge).
```

Im Regelfall ist `elemente_aus_charge(R)` mehrelementig (eine
Charge wird auf mehrere Elemente verteilt). Im Fügeholz-
Sonderfall (Stoßung aus zwei Bezugsquellen) wird `charge_in(E)`
über eine zusätzliche Komposita-Relation
`element_aus_chargen : 𝓔 → 𝒫(𝓡)` ergänzt.

## Wohldefiniertheit

- **Existenz**: Für jeden im Holzbau zugelassenen Werkstoff
  existiert eine normativ vorgegebene Kennzeichnung. Eine
  Produktkennzeichnung kann jederzeit aus dem auf dem Bauteil
  vorgefundenen Sortierstempel oder CE-Etikett rekonstruiert
  werden, sofern dieses lesbar ist.
- **Eindeutigkeit (innerhalb der Charge)**: Die Pflichtfelder
  einer Charge identifizieren das Produkt eindeutig im Sinne
  der CPR und der einschlägigen Produktnorm. Zwei Chargen mit
  identischen Pflichtfeldern werden als dasselbe Produkt
  gehandelt.
- **Trennung Position ≠ Charge**: Die Produktkennzeichnung
  enthält **keine** Information über die Einbauposition. Diese
  Trennung ist konstruktionsseitig: das Tupel R hat kein
  Positions-Feld, und es gibt keine Funktion, die R und Position
  gemeinsam ableitet.
- **Mehrfachzuordnung**:
  - Im Regelfall: |elemente_aus_charge(R)| ≥ 1, eine Charge auf
    mehrere Elemente.
  - Im Fügefall: |element_aus_chargen(E)| ≥ 1, ein Element aus
    mehreren Chargen. Wird durch eigene Relation modelliert; in
    diesem Glossar nur erwähnt, eigener Eintrag `fuegestoss`
    (Folgearbeit) regelt das Detail.
- **Konsistenz mit Werkstoff** (`werkstoff`, eigener Eintrag
  folgt): Die Werkstoff-Klasse h der Produktkennzeichnung muss
  mit dem Werkstoff des Elements übereinstimmen. Diskrepanz
  (z. B. Element-Werkstoff = BSH, Produktkennzeichnung-
  Werkstoff = Vollholz) ist eine Datenfehler-Bedingung und führt
  zu `Entartet.WerkstoffMismatch`.
- **Mutabilität**: Eine Produktkennzeichnung ist von der Charge
  ererbt; sie ändert sich nur, wenn das Element einer anderen
  Charge zugeordnet wird (Materialwechsel im Entwurf,
  Fehlbestellung). Im laufenden Betrieb ist sie stabil.
- **Nicht-Zirkularität**: Die Definition stützt sich auf
  Werkstoff-Kategorien und Norm-Tupel. Sie verweist nicht auf
  andere Glossarbegriffe in ihrer eigenen Definition; `werkstoff`
  und `element` werden nur als Trägerbegriffe genannt, nicht
  in die Definition aufgenommen.

## Erläuterung (nicht normativ)

Die Produktkennzeichnung ist im Holzbau die **einzige normativ
scharf kodifizierte Identifikationsspur**. Im Gegensatz zur
Positionsnummer (Branchenusus, nicht normiert) und zur UUID
(technischer Hilfskonstrukt der App) ist die
Produktkennzeichnung in der Bauproduktenverordnung und den
Produktnormen exakt festgelegt — Form, Inhalt, Lesbarkeit und
Aufbringungspflicht sind dort geregelt.

**Praktische Bedeutung:**

- Auf der Baustelle ist der Sortierstempel (Vollholz) bzw. das
  CE-Etikett (BSH) das einzige verlässliche Mittel zur
  nachträglichen Verifikation der Festigkeitsklasse. Eine
  Pos-Nr. allein erlaubt keine Materialprüfung.
- Bei Mängelfällen (Schadensgutachten, Tragfähigkeitsverlust,
  Reklamation) ist die Produktkennzeichnung der Schlüssel zur
  Hersteller-Rückverfolgung.
- In der WPK-Praxis (werkseigene Produktionskontrolle nach
  Anhang ZA) werden Charge und CE-Kennzeichnung verbunden.

**App-relevant**: Bei IFC-Export reichert die App die
Element-Material-Definition mit der Produktkennzeichnung an
(`Pset_MaterialWoodBasedBeam`, `Pset_MaterialWoodBasedPanel`).
Das ermöglicht BIM-basierte Materialnachverfolgung im Sinne
der zukünftigen EU-Digital Product Passport-Initiativen.

**Historische Abgrenzung**: Vor dem CNC-Abbund waren
**Abbundzeichen** (römische Ziffern mit Beizeichen wie
Hechelzahn, Pfeilspitze, Mondkrückung; vgl. Gerner 1992,
Krämer 2018) das primäre Identifikations-Werkzeug für
zimmermannsmäßig abgebundene Bauteile. Sie kombinierten
Position, Geschoss, Wand und Reihenfolge in einem einzigen,
auf das Holz aufgerissenen Symbol. **Sie sind nicht genormt**
und im modernen Werkplan-/CNC-Workflow durch Pos-Nr. und
CAD-ID ersetzt. Im Glossar werden sie nicht als
Produktkennzeichnung geführt.

## Beziehungen

- **Oberbegriff**: keiner.
- **Verwendung**: Pflichtfeld eines **Werkstoffs**
  (`werkstoff.produktkennzeichnung`). Die Produktkennzeichnung
  ist Eigenschaft des Werkstoffs, nicht des Elements direkt; ein
  Element trägt einen Werkstoff (Pflichtfeld), und der Werkstoff
  trägt die Produktkennzeichnung. Mehrere Elemente können
  denselben Werkstoff (und damit dieselbe Produktkennzeichnung)
  teilen, wenn sie aus derselben Charge stammen; Aggregation auf
  Charge-Ebene erfolgt über die Werkstoff-Identität in der
  Persistenzschicht.
- **Bestandteile (partitiv)**: werkstoffspezifische Pflichtfelder
  (Sortierklasse, Hersteller-ID, Festigkeitsklasse, Klebstoff,
  Produktionswoche, WPK-Zertifikat …).
- **Abgrenzung**:
  - **UUID** (`uuid`): technischer Surrogatschlüssel, vergibt die
    App. Andere Spur, anderer Zweck.
  - **Positionsnummer** (`positionsnummer`): humanlesbarer
    Geschäftsschlüssel der Einbauposition. Konvention, nicht
    Norm. Identifiziert die **Position**, nicht die Charge.
  - **Werkstoff** (`werkstoff`): die abstrakte Materialklasse
    („BSH GL24h"). Werkstoff ist Eigenschaft des Elements;
    Produktkennzeichnung ist **Pflichtfeld des Werkstoffs**
    (`werkstoff.produktkennzeichnung`). Die Produktkennzeichnung
    konkretisiert den Werkstoff um Charge, Hersteller und
    Produktionsdatum. Die Feldzuordnung läuft strikt
    `element.werkstoff.produktkennzeichnung` — niemals direkt
    `element.produktkennzeichnung`.
  - **Festigkeitsklasse** (eigener Eintrag folgt): ein **Feld**
    der Produktkennzeichnung (z. B. `GL24h`, `C24`), nicht ein
    eigenständiger Identifikator.
  - **Bezeichnung** (freier Anzeigename): kein Identitätsanspruch.
  - **Abbundzeichen** (historisch, römische Ziffern mit
    Beizeichen): nicht genormt, im modernen Holzbau praktisch
    durch CAD-IDs ersetzt. Eigener historischer Eintrag
    (Folgearbeit) möglich; **nicht** als Produktkennzeichnung
    geführt.

## Implementierungshinweis

Datentyp (Domänen-Schicht, Kotlin, Schicht
`zimmermann.domain.identifikation`):

```kotlin
package zimmermann.domain.identifikation

import zimmermann.domain.Resultat
import java.time.Year

/**
 * Normativ kodifizierte Identifikation einer Holzwerkstoff-Charge
 * (oder eines Einzelprodukts).
 *
 * Glossar: hg_produktkennzeichnung.md
 *
 * Aggregat: je Werkstoffklasse unterschiedliche Pflichtfelder
 * (Sealed-Type-Hierarchie). Identifiziert die Charge, NIEMALS die
 * Einbauposition.
 *
 * Verortung: Pflichtfeld eines Werkstoffs
 * (`Werkstoff.produktkennzeichnung`), NICHT direktes Feld eines
 * Elements. Ein Element greift auf die Produktkennzeichnung über
 * `element.werkstoff.produktkennzeichnung` zu.
 *
 * Validierung: Konstruktoren der Subtypen sind `internal`;
 * Erzeugung erfolgt über Factory-Funktionen mit Rückgabetyp
 * `Resultat<…, ProduktkennzeichnungUngueltig>`. Die Domänen-Schicht
 * wirft niemals Exceptions. Vorbild:
 * `zimmermann.domain.koordinaten.LokalePlatzierung.aus(...)`.
 */
sealed interface Produktkennzeichnung {

    /** Vollholz nach DIN 4074-1, optional CE nach DIN EN 14081-1. */
    data class Vollholz(
        val sortierklasse: VollholzSortierklasse,    // S 7, S 10, S 13, MS 7, …
        val holzart: HolzartKurzzeichen,             // FI, TA, KI, …
        val hersteller: HerstellerId,
        val sortierer: SortiererId? = null,          // DIN 4074-1 optional; darf == hersteller sein
        val ce: CeKennzeichnungVollholz? = null      // gesetzt bei DIN EN 14081
    ) : Produktkennzeichnung

    /** BSH/BalkSH nach DIN EN 14080:2013, Anhang ZA (CE Pflicht). */
    data class Brettschichtholz(
        val hersteller: HerstellerId,
        val festigkeitsklasse: FestigkeitsklasseGL,  // GL20h, GL24c, …
        val klebstofftyp: Klebstofftyp,              // I oder II nach EN 301
        val produktionswoche: Produktionswoche,
        val notifikationsStelle: NotifikationsStelle,
        val wpkZertifikat: WpkZertifikatNummer,
        val ceEtikettJahr: Year
    ) : Produktkennzeichnung

    /** Furnierschichtholz nach DIN EN 14374. */
    data class Furnierschichtholz(
        val hersteller: HerstellerId,
        val produktbezeichnung: String,              // z. B. Kerto-S
        val produktionswoche: Produktionswoche,
        val notifikationsStelle: NotifikationsStelle,
        val wpkZertifikat: WpkZertifikatNummer,
        val ceEtikettJahr: Year
    ) : Produktkennzeichnung

    // Weitere Subtypen (BSP, Plattenwerkstoffe, …) als Folgearbeit.
}

@JvmInline value class HerstellerId(val wert: String)
@JvmInline value class SortiererId(val wert: String)
@JvmInline value class NotifikationsStelle(val wert: String)
@JvmInline value class WpkZertifikatNummer(val wert: String)
@JvmInline value class HolzartKurzzeichen(val wert: String)

enum class VollholzSortierklasse { S7, S10, S13, MS7, MS10, MS13 }
enum class FestigkeitsklasseGL {
    GL20H, GL22H, GL24H, GL26H, GL28H, GL30H, GL32H,
    GL20C, GL22C, GL24C, GL26C, GL28C, GL30C, GL32C
}
enum class Klebstofftyp { I, II }

/**
 * Produktionswoche nach ISO-8601-Wochenkalender (1..53).
 *
 * Konstruktor `internal`; Erzeugung über
 * [Produktionswoche.aus] mit Rückgabetyp
 * `Resultat<Produktionswoche, ProduktkennzeichnungUngueltig>`.
 * Vorbild: `LokalePlatzierung.aus(...)`.
 */
data class Produktionswoche internal constructor(val woche: Int, val jahr: Year) {
    companion object {
        fun aus(woche: Int, jahr: Year): Resultat<Produktionswoche, ProduktkennzeichnungUngueltig> =
            if (woche in 1..53) Resultat.Erfolg(Produktionswoche(woche, jahr))
            else Resultat.Fehler(ProduktkennzeichnungUngueltig.WocheAusserhalb)
    }
}

/** Domänen-Fehlerfälle der Produktkennzeichnungs-Validierung (keine Exceptions). */
sealed interface ProduktkennzeichnungUngueltig {
    object WocheAusserhalb : ProduktkennzeichnungUngueltig
    // weitere Varianten je Subtyp-Validierung in Folgearbeit
}

data class CeKennzeichnungVollholz(
    val festigkeitsklasse: FestigkeitsklasseC,    // C14, …, C50
    val notifikationsStelle: NotifikationsStelle,
    val ceEtikettJahr: Year
)

enum class FestigkeitsklasseC {
    C14, C16, C18, C20, C22, C24, C27, C30, C35, C40, C45, C50
}
```

- **Einheit**: keine (Aggregat aus normativ vorgegebenen Feldern).
- **Mutabilität**: stabil; ändert sich nur bei Charge-Wechsel
  des Elements (Materialdisposition, Fehlbestellung).
- **Trennung Position ≠ Charge**: Produktkennzeichnung enthält
  **kein** Positionsfeld. Wer Position und Charge gemeinsam
  speichern will, hält die Positionsnummer am Element
  (`element.positionsnummer`) und die Produktkennzeichnung am
  Werkstoff (`element.werkstoff.produktkennzeichnung`); ein
  Mischfeld ist konstruktiv ausgeschlossen.
- **1 → n Relation Charge → Elemente**: Eine
  `Produktkennzeichnung`-Instanz darf von mehreren Elementen
  geteilt werden (eine Charge auf zehn Sparren). Der Pfad führt
  über den gemeinsamen Werkstoff: mehrere Elemente referenzieren
  denselben Werkstoff, der die geteilte Produktkennzeichnung
  trägt. In der Persistenzschicht entsprechend als eigene
  Tabelle `werkstoff` mit FK `element.werkstoff_id →
  werkstoff.id (UUID)` und Spalten/Joins für die
  Produktkennzeichnungs-Felder modelliert.
- **n → m Relation Element → Chargen** (Sonderfall Fügeholz):
  ein Element ist dann mit mehreren Werkstoff-Instanzen verknüpft
  (jede mit eigener Produktkennzeichnung) über eine
  Hilfstabelle `element_werkstoff_anteil` mit Mengen- oder
  Längen-Anteil pro Charge. Eigener Eintrag `fuegestoss`
  (Folgearbeit) regelt Geometrie und Bemessung.
- **IFC-Mapping** (Persistenzschicht):
  - Material-Resource (`IfcMaterial`) erhält Property Set
    `Pset_MaterialWoodBasedBeam` bzw. `Pset_MaterialWoodBasedPanel`
    mit den Pflichtfeldern.
  - CE-relevante Felder (Notifikations-Stelle, WPK-Zertifikat,
    Produktionswoche) werden in einem eigenen `Pset_Manufacturing`
    geführt.
- **BTLx-Mapping**: Material-Element des Parts; CE-Felder als
  zusätzliche Attribute. Folgearbeit präzisiert Field-Mapping.
- **Edge Cases**:
  - **Werkstoff ohne aufgelöste Produktkennzeichnung**: im
    frühen Entwurfsstadium darf der Werkstoff eine Platzhalter-
    Produktkennzeichnung tragen (vgl. `hg_werkstoff.md`,
    `Produktkennzeichnung.UNBEKANNT`); muss vor Fertigung /
    Bemessung aufgelöst sein. Auf Element-Ebene gibt es kein
    eigenes Produktkennzeichnungs-Feld, das `null` sein könnte.
  - **Werkstoff-Mismatch** (Subklasse h der Produktkennzeichnung
    inkonsistent zur Werkstoff-Subklasse, der sie zugeordnet ist):
    → `Entartet.WerkstoffMismatch` als Resultat-Fehlerfall der
    Werkstoff-Factory.
  - **Lesbarkeit auf Baustelle**: bei verlorener oder unleserlicher
    Kennzeichnung gilt das Bauteil als nicht-CE-konform; in der
    App kann ein Element den Status `Produktkennzeichnung.UNLESBAR`
    erhalten (zukünftiger Subtyp), das Tragfähigkeitsnachweise
    sperrt.
  - **Historische Bauteile** (Bestandsbau, Sanierung): keine
    moderne Produktkennzeichnung; eine ergänzende
    in-situ-Sortierung nach DIN 4074 erzeugt eine nachträgliche
    Kennzeichnung. Im Glossar als `produktkennzeichnung_in_situ`
    ein Folgeeintrag möglich.
  - **Mehrfachstempel** (Holz mit alter und neuer Sortierung):
    der zeitlich jüngere, gültige Stempel zählt; die ältere
    Markierung wird als historische Information geführt.
  - **Sortierer = Hersteller** (Vollholz, DIN 4074-1): die
    Identitäten von `sortierer` und `hersteller` dürfen
    zusammenfallen. DIN 4074-1 verlangt keine organisatorische
    Trennung; im typischen Anwendungsfall der **visuellen
    Sortierung im Hersteller-Werk** durch einen werkseigenen,
    nach DIN 4074-1 ausgebildeten Sortierer ist
    `sortierer == hersteller` der Regelfall und ausdrücklich
    zulässig. Eine getrennte Belegung beider Felder ist nur dann
    erforderlich, wenn die Sortierung extern (z. B. durch eine
    unabhängige Sortierstelle nach Anlieferung) erfolgt.

## Quellen

**Primär (normativ):**

- DIN 4074-1:2012-06, „Sortierung von Holz nach der
  Tragfähigkeit — Teil 1: Nadelschnittholz".
- DIN EN 14080:2013-09, „Holzbauwerke — Brettschichtholz und
  Balkenschichtholz — Anforderungen", Anhang ZA.
- DIN EN 14081-1:2019-10, „Holzbauwerke — Nach Festigkeit
  sortiertes Bauholz mit rechteckigem Querschnitt — Teil 1:
  Allgemeine Anforderungen".
- DIN EN 14374:2005-02, „Holzbauwerke — Furnierschichtholz für
  tragende Zwecke — Anforderungen".
- DIN EN 301:2018-04, „Klebstoffe für tragende Holzbauteile —
  Phenolische und aminoplastische Klebstoffe — Klassifizierung
  und Leistungsanforderungen".
- Verordnung (EU) Nr. 305/2011 (Bauproduktenverordnung, CPR).
- ISO 16739-1:2024, „Industry Foundation Classes (IFC) —
  Part 1: Data schema".

**Sekundär:**

- Mönck, W.; Rug, W.: *Holzbau — Bemessung und Konstruktion.*
  16. Auflage, Beuth, Berlin 2015.
- Blass, H. J.; Sandhaas, C.: *Ingenieurholzbau — Grundlagen
  der Bemessung.* KIT Scientific Publishing, Karlsruhe 2016.
- Holzbau Deutschland — Informationsdienst Holz: *Holzbau-
  Handbuch*, Reihe 1, Teil 1.
- Lignum (Hrsg.): *Lignatec*, Hinweise zur CE-Kennzeichnung.
- design2machine: *BTLx 2.x Specification* (Stand 2024).

**Nur in der Abgrenzung referenziert (historisch, nicht
Definitionsquelle):**

- Gerner, M.: *Fachwerk — Instandsetzung, Sanierung, Neubau.*
  DVA, 7. Auflage 2007 (Abbundzeichen).
- Krämer, V.: *Grundwissen des Zimmerers.* 7. Auflage,
  Bruderverlag, Köln 2018 (Abbundzeichen, Sortierstempel).

**Korpus (nicht autoritativ):**

- Holzbau Deutschland, Merkblatt „Begriffe und Klassifizierungen
  für den Holzbau" (abgerufen 2026-05-08).
- buildingSMART International: *IFC4.3 Documentation*,
  Version 4.3.2.0, 2024.
- Wikipedia, Lemmata „Sortierstempel", „CE-Kennzeichnung",
  „Brettschichtholz" (abgerufen 2026-05-08).
