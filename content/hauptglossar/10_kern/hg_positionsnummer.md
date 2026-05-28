---
id: positionsnummer
benennung: Positionsnummer
synonyme: ["Pos-Nr.", "Werkplan-Position", "Positionskennung"]
abgelehnte_benennungen: [Bauteilnummer, Stücknummer, Nummer, "part number", "tag", "position number", "item number"]
oberbegriff: null
begriffstyp: merkmal
voraussetzungen: []
abgrenzung_zu: [uuid, produktkennzeichnung, bezeichnung, abbundzeichen, ifc_tag, btlx_singlemembernumber]
status: entwurf
theorie_pflichtig: required
quellen_primär:
  - "DIN EN ISO 7519:2025-01 (zuvor DIN 1356-1), 'Technische Produktdokumentation — Bauzeichnungen — Allgemeine Grundsätze der Darstellung — Hochbauzeichnungen', Stücklisten- und Beschriftungsanforderungen."
  - "DIN 18334:2019-09, VOB Vergabe- und Vertragsordnung für Bauleistungen — Teil C: Allgemeine Technische Vertragsbedingungen für Bauleistungen (ATV) — Zimmer- und Holzbauarbeiten. Anforderung an eindeutige Beschreibung von Holzbauteilen ohne Vorgabe einer Form."
  - "ISO 16739-1:2024, 'Industry Foundation Classes (IFC) — Part 1: Data schema', Attribut `IfcElement.Tag`: 'The tag (or label) identifier at the particular instance of a product, e.g. the serial number, or the position number.' Alternativ `Pset_BeamCommon.Reference` etc."
  - "design2machine: BTLx 2.x Specification (Stand 2024), Element Part mit Attribut `@SingleMemberNumber` (geteilt von identischen Teilen zur Stücklistenbildung); ergänzend `OrderNumber`, `AssemblyNumber`."
quellen_sekundär:
  - "Holzbau Deutschland — Informationsdienst Holz: Holzbau-Handbuch, Reihe 2 (Tragwerksplanung), Teil 1 (Berechnung und Konstruktion), Folge 1 (Konstruktion und Bemessung von Holzbauteilen), Werkplan-Hinweise."
  - "Krämer, V.: Grundwissen des Zimmerers. 7. Auflage, Bruderverlag, Köln 2018, Kap. zu Werkplanung und Bauteilbezeichnung."
  - "cadwork informatik AG: cadwork lexocad / cadwork 3D Anwenderdokumentation, Konzept der gemeinsamen Pos-Nr. für identische Teile (Stücklistenbildung)."
  - "Date, C. J.: An Introduction to Database Systems. 8. Auflage, Addison-Wesley 2003, Kap. 9 (Surrogate vs. Natural Keys)."
  - "Ambler, S. W.; Sadalage, P. J.: Refactoring Databases. Addison-Wesley 2006, Kap. 6 (Identity)."
  - "OpenBOM Blog: 'Why intelligent part numbers are a bad idea' (2019, regelmässig aktualisiert)."
  - "Arena Solutions: 'Smart vs. Non-Smart Part Numbering — A PLM Best Practice'."
  - "BuyPLM / Javelin Tech: PLM-Whitepapers zu Part-Number-Strategien."
  - "dbt Labs: 'Surrogate keys vs. natural keys', dbt Documentation (2023)."
quellenkonflikt: |
  Es gibt **keine harte normative Vorgabe** für Werkplan-
  Positionsnummern im Holzbau. Die einschlägigen Bemessungs- und
  Holzbau-Normen schweigen:

  - DIN EN 1995-1-1 (Eurocode 5) und EC5/NA enthalten keine
    Klausel zu Bauteilnummerierung.
  - SIA 265:2021 (Holzbau) enthält keine Klausel zu
    Bauteilnummerierung.
  - ÖNORM B 1995 enthält keine Klausel zu Bauteilnummerierung.
  - DIN 1052:2008-12 enthält keine Klausel zu Bauteilnummerierung.
  - DIN 18334 (VOB/C ATV Zimmer- und Holzbauarbeiten) verlangt
    nur „eindeutige Beschreibung", lässt Form frei.
  - DIN EN ISO 7519:2025-01 (ehemals DIN 1356-1) verlangt
    Stücklisten in Bauzeichnungen, schreibt aber keine
    Bauteilkürzel oder Nummerierungsschemata vor.

  Die in der Praxis verwendeten Kürzel (S, P, St, R, D, KB, Schw,
  Rä, W, UZ) sind **Branchenusus, nicht normiert**, und die
  Quellen widersprechen sich teilweise:

  - Holzbau-Handbuch Reihe 2/Teil 1/Folge 1 verwendet `S` für
    Sparren.
  - Krämer „Grundwissen des Zimmerers" verwendet `S` mehrdeutig:
    teils Sparren, teils Stütze; `St` als Stütze-Kürzel ist
    verbreiteter, aber nicht durchgängig.
  - Schweizer Praxis (Lignum, cadwork-Vorlagen) verwendet teils
    eigene Kürzel.

  Eigene Festlegung in diesem Glossar:

  - Die Positionsnummer ist im Glossar als **Konvention dieses
    Tools** geführt, **nicht als Norm**.
  - Die Liste der Branchenkürzel im Body ist deskriptiv und nicht
    erschöpfend; die App lässt projektspezifische Konventionen zu.
  - Die Strukturregeln (Scope der Eindeutigkeit, Mutabilität,
    Foreign-Key-Verbot, Padding für Sortierung) sind eigene
    Festlegungen, abgeleitet aus PLM-Best-Practice (Date,
    Ambler, OpenBOM, Arena, BuyPLM, dbt) und cadwork-Praxis.
  - Identitätsschutz erfolgt ausschließlich über `uuid`; die
    Positionsnummer ist mutable, ohne dass referentielle
    Integrität betroffen ist.

  Diese Festlegung ist konfliktfrei mit allen konsultierten
  Quellen, sobald die Positionsnummer als Konvention und nicht
  als Norm verstanden wird.
---

## Prosa-Definition

Eine **Positionsnummer** ist ein projektspezifischer, humanlesbarer
Identifikator eines Elements (Bauteil, Verbindungsmittel, Verbinder
oder Verstärkungselement) mit semantischer Struktur (typisch:
Kategorienkürzel + laufende Nummer + optionale Geschoss-/
Bauteilgruppen-Markierung), der zur Werkplan-, Stücklisten- und
Baustellenkommunikation dient, der innerhalb des Geltungsbereichs
(Projekt × Kategorie) eindeutig sein muss, der mutable ist und der
ausdrücklich **kein** Foreign-Key-Ziel anderer Domänen-Beziehungen
ist.

## Mathematische Definition

Sei

- 𝓟 die Menge aller in dieser App verwalteten Projekte,
- 𝓚 die Menge der Element-Kategorien
  𝓚 = { Bauteil, Verbindungsmittel, Verbinder,
         Verstärkungselement },
  ggf. weiter unterteilt nach Subtypen (Sparren, Pfette, Stütze, …),
- 𝓢 = String die Menge der zulässigen humanlesbaren Strings
  (UTF-8, max. 64 Zeichen, ohne Steuerzeichen).

Eine **Positionsnummer** ist ein Tripel

```
P := (projekt, kategorie, kennung) ∈ 𝓟 × 𝓚 × 𝓢
```

mit der Eindeutigkeitsbedingung

```
∀ E₁, E₂ ∈ 𝓔 :
   E₁ ≠ E₂  ∧  P(E₁), P(E₂) ≠ ⊥
   ∧  projekt(E₁) = projekt(E₂)
   ∧  kategorie(E₁) = kategorie(E₂)
   ⇒  kennung(E₁) ≠ kennung(E₂),
```

wobei 𝓔 die Menge der Element-Instanzen (siehe `element`) ist und
P(E) die Positionsnummer von E (oder ⊥, falls nicht gesetzt).

Die Positionsnummer ist **mutable**: sie darf jederzeit über eine
Aktualisierungsoperation

```
neuvergabe : 𝓔 × 𝓢 → 𝓔,    neuvergabe(E, k') := E mit kennung := k'
```

geändert werden, sofern die Eindeutigkeitsbedingung im Scope
(projekt, kategorie) erhalten bleibt.

**Kein Foreign-Key**: Für jede Beziehung r ⊆ 𝓔 × X mit X einem
beliebigen Domänenobjekt-Raum gilt: r referenziert E
ausschließlich über uuid(E), nicht über P(E). Insbesondere
existiert keine Domänen-Beziehung der Form X → kennung(E).

## Wohldefiniertheit

- **Existenz**: Für jedes Element kann eine Positionsnummer
  vergeben werden; die Menge 𝓢 ist überabzählbar groß. Im frühen
  Entwurfsstadium ist `null` (⊥) zulässig.
- **Wohldefiniertheit der Eindeutigkeit**: Die Bedingung ist
  scoped (projekt, kategorie). Eine projektübergreifende
  Eindeutigkeit ist **nicht** gefordert und faktisch nicht
  herstellbar (verschiedene Bauvorhaben verwenden ähnliche
  Strukturen).
- **Mutabilität konsistent mit referentieller Integrität**: Da
  keine Foreign Keys auf die Positionsnummer zeigen, ist
  Renumbering ohne Bruch möglich. Eine reine Aktualisierung des
  Kennungs-Strings ändert keine Beziehung. Diese Eigenschaft ist
  konstruktiv: Sie wird durch das Verbot von FK-Verweisen auf P
  hergestellt, nicht durch eine Eigenschaft von P selbst.
- **Vergabelogik (cadwork-Modell)**: Identische Geometrie und
  identische bemessungsrelevante Attribute → gleiche
  Positionsnummer (zur Stücklistenbildung). Diese Aggregation
  erfolgt **nicht** über Foreign Keys, sondern als
  Berichts-/Stücklisten-Operation in der Persistenz- bzw.
  Berichtsschicht.
- **Padding zur lex-Sortierung**: Eine Positionsnummer wie
  `S-007` sortiert vor `S-010` lexikografisch korrekt; ohne
  Padding wäre `S-10` < `S-7` lex, aber die Montage-Reihenfolge
  fordert numerisch sortiert zu lesen. Das Padding ist
  Modellierungs-Empfehlung, nicht Pflicht.
- **Nicht-Zirkularität**: Die Definition stützt sich auf Mengen
  von Projekten und Kategorien sowie auf Strings. Sie verweist
  nicht auf andere Glossarbegriffe in ihrer eigenen Definition;
  insbesondere wird `element` nur als Träger der Positionsnummer
  erwähnt, nicht in deren Definition mitkonstruiert.

## Branchenusus der Kürzel (deskriptiv, nicht normativ)

In der DACH-Holzbaupraxis sind folgende Kürzel verbreitet (aus
Holzbau-Handbuch, Krämer, cadwork-Vorlagen). Die Liste ist
**deskriptiv**, nicht normativ; die Quellen widersprechen sich
teilweise:

| Kürzel | Bauteilrolle                            | Anmerkung                                |
|--------|------------------------------------------|------------------------------------------|
| `S`    | Sparren (häufig) ODER Stütze (teilweise) | **Mehrdeutig** — Konflikt der Quellen    |
| `St`   | Stütze                                   | weniger mehrdeutig als `S` für Stütze    |
| `P`    | Pfette                                   | First-, Mittel-, Fußpfette ggf. `Pf`, `MP`, `FP` |
| `R`    | Riegel                                   |                                          |
| `D`    | Strebe / Diagonale                       |                                          |
| `KB`   | Kopfband                                 |                                          |
| `Schw` | Schwelle                                 |                                          |
| `Rä`   | Rähm                                     |                                          |
| `W`    | Wechsel                                  |                                          |
| `UZ`   | Unterzug                                 |                                          |
| `KH`   | Kehlbalken                               |                                          |
| `BB`   | Bundbalken                               |                                          |

Empfehlung der App: `St` für Stütze, `S` für Sparren — die
weniger mehrdeutige Variante. Projektspezifische Abweichungen
sind zulässig und werden im Projekt-Header (Pos-Nr.-Schema)
dokumentiert.

**Zusammengesetztes Schema**: Verbreitet ist
`<Kürzel>-<lfd. Nummer>[-<Geschoss>]`, z. B. `S-12-OG1`,
`P-001-DG`, `St-04-EG`. Komplexere Schemata (Bauabschnitt,
Wandnummer, Achsbezug) sind möglich, sollten aber **kein
Klassifikations-Encoding** außer der Element-Kategorie tragen
(siehe Anti-Pattern unten).

## Anti-Pattern: „intelligent part numbers"

Positionsnummern, die über die Element-Kategorie hinaus
zusätzliche Klassifikationsmerkmale (Material, Festigkeitsklasse,
Querschnitt, Lieferant, Bauphase) **in den Identifikator
encodieren**, gelten in der PLM-Literatur einhellig als
Anti-Pattern (OpenBOM, Arena, BuyPLM, Javelin):

- Bei Reklassifikation (z. B. Wechsel der Festigkeitsklasse von
  C24 auf C30) müsste die Pos-Nr. neu vergeben werden, was
  Werkpläne und Bauteilbeschriftungen ungültig macht.
- Die Pos-Nr. wird zum „Schatten-Datenmodell" mit eigener
  Konsistenz-Pflege.
- Zwei eigentlich gleiche Konstruktionen mit unterschiedlichem
  Lieferanten erscheinen als verschiedene Positionsnummern,
  obwohl sie identisch sind.

Composing über Aggregat-Beziehungstabellen (z. B. „dieses Bauteil
gehört zu Wand W-12 in Geschoss EG") gehört in eine relationale
Beziehung, **nicht** in den Identifikator.

## Beziehungen

- **Oberbegriff**: keiner.
- **Verwendung**: optionales Feld jedes **Elements** (`element`,
  `bauteil`, `verbindungsmittel`, `verbinder`,
  `verstaerkungselement`).
- **Abgrenzung**:
  - **UUID** (`uuid`): technisch, persistent, semantik-frei.
    Trägt Foreign Keys. Andere Spur, anderer Zweck.
  - **Produktkennzeichnung** (`produktkennzeichnung`):
    normativ kodifizierte Charge-/Produkt-Identifikation. Die
    Positionsnummer identifiziert die **Einbauposition**, die
    Produktkennzeichnung die **Charge** — strikt getrennt zu
    führen. **Verortung am Werkstoff, nicht am Element direkt**:
    Der Zugriff vom Element aus läuft strikt
    `element.werkstoff.produktkennzeichnung`. Die drei
    Identifikator-Spuren (UUID, Positionsnummer,
    Produktkennzeichnung) sind eine Modellierungs-Sicht aus Memory
    `project_bauteil_identifikation`; die Produktkennzeichnungs-
    Spur ist indirekt über den Werkstoff erreichbar.
  - **Bezeichnung**: freier Anzeigename ohne Strukturanspruch
    (kein Eindeutigkeits-Constraint).
  - **Abbundzeichen** (historisch, römische Ziffern mit
    Beizeichen für Wand/Geschoss; vgl. Gerner 1992,
    Krämer 2018): nicht genormt, im modernen CNC-Abbund
    praktisch durch CAD-IDs ersetzt. Wird nicht als
    Positionsnummer geführt; eigener historischer Eintrag
    `abbundzeichen` (Folgearbeit) möglich.
  - **IFC `IfcElement.Tag`**: IFC-Persistenz-Slot der
    Positionsnummer (IFC-Norm benennt „position number"
    wörtlich). Kein eigener Glossar-Begriff.
  - **BTLx `Part/@SingleMemberNumber`**: BTLx-Persistenz-Slot
    der Positionsnummer für identische Teile. Kein eigener
    Glossar-Begriff.

## Implementierungshinweis

Datentyp (Domänen-Schicht, Kotlin, Schicht
`zimmermann.domain.identifikation`):

```kotlin
package zimmermann.domain.identifikation

import zimmermann.domain.Resultat

/**
 * Humanlesbarer Geschäftsschlüssel eines Elements.
 * Glossar: hg_positionsnummer.md
 *
 * Konvention dieses Tools, KEINE Norm. Eindeutigkeit ist
 * scoped pro (Projekt, Kategorie). Mutable. Niemals als
 * Foreign-Key-Ziel verwenden — alle FK referenzieren
 * ausschließlich Element.uuid.
 *
 * Validierung erfolgt ausschließlich über die Factory
 * `Positionsnummer.aus(...)` mit Rückgabetyp
 * `Resultat<Positionsnummer, PositionsnummerUngueltig>`.
 * Der Konstruktor ist `internal`; `init { require(...) }` wird
 * NICHT verwendet, weil die Domänen-Schicht keine Exceptions
 * werfen darf. Vorbild:
 * `zimmermann.domain.koordinaten.LokalePlatzierung.aus(...)`.
 */
@JvmInline
value class Positionsnummer internal constructor(val kennung: String) {

    companion object {
        private const val MAX_LAENGE = 64

        /**
         * Erzeugt eine Positionsnummer aus einer Roh-Kennung.
         *
         * Liefert
         *  - [Resultat.Erfolg] mit der Positionsnummer, wenn die Kennung
         *    nicht leer ist, höchstens [MAX_LAENGE] Zeichen umfasst und
         *    keine Steuerzeichen enthält,
         *  - [Resultat.Fehler] mit der jeweiligen
         *    [PositionsnummerUngueltig]-Variante sonst.
         */
        fun aus(kennung: String): Resultat<Positionsnummer, PositionsnummerUngueltig> = when {
            kennung.isBlank() ->
                Resultat.Fehler(PositionsnummerUngueltig.Leer)
            kennung.length > MAX_LAENGE ->
                Resultat.Fehler(PositionsnummerUngueltig.ZuLang)
            kennung.any { it.isISOControl() } ->
                Resultat.Fehler(PositionsnummerUngueltig.Steuerzeichen)
            else ->
                Resultat.Erfolg(Positionsnummer(kennung))
        }
    }
}

/** Domänen-Fehlerfälle der Positionsnummer-Validierung (keine Exceptions). */
sealed interface PositionsnummerUngueltig {
    object Leer : PositionsnummerUngueltig
    object ZuLang : PositionsnummerUngueltig
    object Steuerzeichen : PositionsnummerUngueltig
}

/**
 * Projekt- und Kategorien-Scope der Eindeutigkeit.
 * Wird in der Persistenzschicht als UNIQUE-Constraint
 * über (projektId, kategorie, positionsnummer) abgebildet.
 */
data class PositionsnummerScope(
    val projektId: ProjektId,
    val kategorie: ElementKategorie
)

enum class ElementKategorie {
    BAUTEIL, VERBINDUNGSMITTEL, VERBINDER, VERSTAERKUNGSELEMENT
}
```

- **Einheit**: keine (humanlesbarer String).
- **Mutabilität**: mutable. Eine Aktualisierung über
  `Element.copy(positionsnummer = …)` (Kotlin-Datenklasse)
  ändert keine Foreign Keys, weil keine Foreign Keys auf die
  Positionsnummer existieren.
- **Vergabe**:
  - In der Praxis manuell über Werkplan oder automatisch über
    cadwork-Pos-Nr.-Generator (gleicher Pos-Nr.-Wert für
    geometrisch + attributiv identische Teile).
  - In der App: optionale Vergabe-Operation
    `Element.vergabePositionsnummer(scope, kennung)`.
- **Eindeutigkeits-Erzwingung** (Persistenzschicht):
  ```sql
  UNIQUE (projekt_id, element_kategorie, positionsnummer)
       WHERE positionsnummer IS NOT NULL;
  ```
  In Kotlin/in-memory: vor Insert prüfen; bei Verletzung
  `Resultat.Fehler(KollisionInScope)`.
- **Padding-Empfehlung**:
  - Format `<Kürzel>-<3-stellig laufend>` (z. B. `S-007`,
    `P-012`) für Projekte bis 1 000 Teile pro Kategorie.
  - Format `<Kürzel>-<4-stellig laufend>` für größere Projekte.
  - Padding ist **Empfehlung**, kein Pflicht-Constraint.
- **IFC-/BTLx-Mapping** (Persistenzschicht):
  - IFC-Export: `IfcElement.Tag := positionsnummer.kennung`.
    Alternativ `Pset_BeamCommon.Reference`.
  - BTLx-Export: `Part/@SingleMemberNumber :=
    positionsnummer.kennung`. Identische Teile (gleiche
    Geometrie + Attribute) teilen die SingleMemberNumber.
- **Edge Cases**:
  - **Element ohne Positionsnummer**: zulässig im frühen
    Entwurfsstadium (`null`).
  - **Renumbering**: zulässig; FK bleiben unverändert (es gibt
    keine FK auf die Pos-Nr.).
  - **Kollision im Scope**: vor Insert prüfen, bei Verletzung
    `Resultat.Fehler(KollisionInScope)`. Niemals Exception.
  - **Mehrere Elemente mit gleicher Pos-Nr. in verschiedenen
    Kategorien**: zulässig (Scope schließt Kategorie ein), z. B.
    ein Bauteil `S-12` und eine Verbindungsmittelreihe `S-12`
    koexistieren.
  - **Sonderzeichen / Unicode**: zulässig, aber empfohlen
    UTF-8-Standard ohne Sonderzeichen außer `-`, `_`, `.` und
    Zahlen/Buchstaben. Steuerzeichen sind verboten.
- **Anti-Pattern-Schutz**: Die App vermeidet Klassifikations-
  Encoding in der Pos-Nr. Empfehlung im UI: Nur Element-
  Kategorie + laufende Nummer + optional Geschoss erlauben;
  weitere Attribute (Material, Festigkeitsklasse, Lieferant)
  in eigenen Feldern.

## Quellen

**Primär (normativ):**

- DIN EN ISO 7519:2025-01, „Technische Produktdokumentation —
  Bauzeichnungen — Allgemeine Grundsätze der Darstellung —
  Hochbauzeichnungen" (zuvor DIN 1356-1).
- DIN 18334:2019-09, „VOB Vergabe- und Vertragsordnung für
  Bauleistungen — Teil C: Allgemeine Technische
  Vertragsbedingungen für Bauleistungen (ATV) — Zimmer- und
  Holzbauarbeiten".
- ISO 16739-1:2024, „Industry Foundation Classes (IFC) —
  Part 1: Data schema" (Attribut `IfcElement.Tag`).
- design2machine: *BTLx 2.x Specification* (Stand 2024).

**Sekundär:**

- Holzbau Deutschland — Informationsdienst Holz: *Holzbau-
  Handbuch*, Reihe 2/Teil 1/Folge 1.
- Krämer, V.: *Grundwissen des Zimmerers.* 7. Auflage,
  Bruderverlag, Köln 2018.
- cadwork informatik AG: cadwork lexocad / cadwork 3D
  Anwenderdokumentation.
- Date, C. J.: *An Introduction to Database Systems.* 8. Auflage,
  Addison-Wesley 2003.
- Ambler, S. W.; Sadalage, P. J.: *Refactoring Databases —
  Evolutionary Database Design.* Addison-Wesley 2006.
- OpenBOM Blog: „Why intelligent part numbers are a bad idea".
- Arena Solutions: „Smart vs. Non-Smart Part Numbering — A PLM
  Best Practice".
- BuyPLM / Javelin Tech: PLM-Whitepapers zu Part-Number-
  Strategien.
- dbt Labs: „Surrogate keys vs. natural keys", dbt Documentation.

**Korpus (nicht autoritativ):**

- Holzbau Deutschland, Merkblatt „Begriffe und Klassifizierungen
  für den Holzbau" (abgerufen 2026-05-08).
- Wikipedia, Lemma „Positionsnummer" (abgerufen 2026-05-08;
  schwacher Bezug zum Holzbau).

**Negativ-Befund (geprüft, kein Treffer):**

- DIN EN 1995-1-1:2010-12 — keine Klausel zu Bauteilnummerierung.
- SIA 265:2021 — keine Klausel zu Bauteilnummerierung.
- ÖNORM B 1995 — keine Klausel zu Bauteilnummerierung.
- DIN 1052:2008-12 — keine Klausel zu Bauteilnummerierung.
