---
id: uuid
benennung: UUID (Universally Unique Identifier)
synonyme: ["GUID", "Universally Unique Identifier"]
abgelehnte_benennungen: [ID, Identifikator, Schlüssel, Surrogatschlüssel, "globally unique identifier", "object id"]
oberbegriff: null
begriffstyp: hilfsbegriff
voraussetzungen: []
abgrenzung_zu: [positionsnummer, produktkennzeichnung, bezeichnung, ifc_global_id, btlx_guid, primary_key]
status: entwurf
subglossar_pendant: optional
quellen_primär:
  - "RFC 9562:2024, 'Universally Unique IDentifiers (UUIDs)', IETF, Mai 2024 (obsoletet RFC 4122). Definitionen Versionen 1, 3, 4, 5, 6, 7, 8 und Variante DCE 1.1; insbesondere § 5.7 (UUID Version 7, time-ordered Unix epoch milliseconds + random)."
  - "ISO/IEC 9834-8:2014 / ITU-T X.667, 'Information technology — Procedures for the operation of object identifier registration authorities — Part 8: Generation of universally unique identifiers (UUIDs) and their use in object identifiers'."
  - "ISO 16739-1:2024, 'Industry Foundation Classes (IFC) — Part 1: Data schema', Datentyp `IfcGloballyUniqueId` (22-stelliger Base64-Code eines 128-Bit-UUID nach ISO/IEC 9834-8); Vererbungsregel UR1: jedes IfcRoot-Objekt führt einen GlobalId-Wert."
  - "PostgreSQL Global Development Group: 'PostgreSQL 18 Documentation', Funktion `uuidv7()` (native time-ordered UUID-Erzeugung, Stand 2025)."
quellen_sekundär:
  - "Date, C. J.: An Introduction to Database Systems. 8. Auflage, Addison-Wesley 2003, Kap. 9 'Integrity', Surrogate Keys."
  - "Khorikov, V.: 'Entity Identity vs Database Primary Key'. enterprisecraftsmanship.com, 2019 (Diskussion Surrogate vs. Natural Key, Identity-Persistenz)."
  - "Vernon, V.: Implementing Domain-Driven Design. Addison-Wesley 2013, Kap. 5 (Entity Identity, Surrogate Identity)."
  - "Evans, E.: Domain-Driven Design. Addison-Wesley 2003, Kap. 5."
  - "Ambler, S. W.; Sadalage, P. J.: Refactoring Databases — Evolutionary Database Design. Addison-Wesley 2006, Kap. 6 (Identity)."
  - "design2machine: BTLx 2.x Specification (Stand 2024), Element Part mit Attribut `@GUID` (in Spec wörtlich: 'GUID must be unique')."
quellenkonflikt: |
  Mai 2024 hat IETF RFC 9562 publiziert und RFC 4122 obsoletet.
  Bestehende Werkzeuge, Bibliotheken und Normen verweisen jedoch
  überwiegend noch auf RFC 4122. Die in diesem Glossar maßgebliche
  Quelle ist RFC 9562; RFC 4122 wird nicht mehr als Primärquelle
  geführt. Die Inkompatibilität ist gering: Versionen 1, 3, 4, 5
  bleiben definitorisch identisch; neu sind die Versionen 6, 7, 8
  und die schärfere Formulierung der Variante.

  ISO 16739-1:2024 (IFC) verlangt in Vererbungsregel UR1, dass jede
  IfcRoot-Instanz einen `GlobalId`-Wert führt. IFC kodiert die UUID
  als **22-stelligen Base64-String** nach ISO/IEC 9834-8, nicht als
  kanonischen 8-4-4-4-12-Hex-String aus RFC 9562. Beide Formen sind
  bijektiv ineinander überführbar; in der App wird intern die
  binäre Form (16 Byte) verwendet, am IFC-Rand der 22-stellige
  Base64-Code, am übrigen API-Rand der kanonische 8-4-4-4-12-String.

  CAD-Re-Import-Persistenz: Revit, ARCHICAD und weitere CAD-/BIM-
  Werkzeuge regenerieren bei bestimmten Operationen (Datei-Re-Save,
  Worksharing-Synchronisation, Element-Kopien) ihre internen GUIDs.
  Die App-UUID wird deshalb bei Re-Import **nicht überschrieben**;
  externe GUIDs werden in zusätzlichen Mapping-Feldern
  (`ifc_global_id`, `btlx_guid`, …) geführt. Dies ist eine eigene
  Festlegung dieser App auf Basis dokumentierter Praxiserfahrungen,
  nicht eine Norm-Vorschrift.

  Begriffstyp `hilfsbegriff` analog zu `hg_toleranzen.md`: Die UUID
  ist kein fachlich-bauliches Holzbau-Konzept, sondern ein
  technischer Identitäts-Mechanismus, der quer zu allen
  Element-Subklassen verwendet wird. Sie ist nicht „Merkmal eines
  Elements" im Sinne einer fachlichen Eigenschaft (Querschnitt,
  Werkstoff), sondern Werkzeug der Identitätsverwaltung.
---

## Prosa-Definition

Eine **UUID (Universally Unique Identifier)** ist ein nach RFC 9562
spezifizierter 128-Bit-Bezeichner, der einem identifizierbaren
Objekt bei seiner Erzeugung einmalig, dauerhaft und ohne
Koordination mit anderen Erzeugern zugewiesen wird, der weder eine
fachliche Bedeutung noch eine Beziehung zum bezeichneten Objekt
encodiert und der in der App als technische Identität jedes
Elements und jedes identitätstragenden Aggregats geführt wird.

## Mathematische Definition

Sei

- 𝔹 := {0, 1} die Menge der Bits,
- 𝓤 := 𝔹¹²⁸ die Menge der 128-Bit-Wörter.

Eine **UUID** ist ein Element u ∈ 𝓤. Die zwei in der App
relevanten Versionen sind durch Bit-Layout-Constraints
charakterisiert (RFC 9562 § 4.1, § 5.4, § 5.7):

**UUID v4** (random):

```
u  =  random_122      (122 Bit zufällig),
mit Versions-Bits  u[48..51]  =  0100   (Hex 4),
und Varianten-Bits u[64..65]  =  10     (RFC-Variante).
```

**UUID v7** (time-ordered, in der App empfohlen):

```
u[0..47]   =  unix_ts_ms   (48-Bit-Unix-Zeitstempel in ms, big-endian),
u[48..51]  =  0111         (Versions-Bits, Hex 7),
u[52..63]  =  rand_a       (12 Bit zufällig oder monoton),
u[64..65]  =  10           (Varianten-Bits),
u[66..127] =  rand_b       (62 Bit zufällig).
```

Die kanonische **String-Repräsentation** ist (RFC 9562 § 4):

```
xxxxxxxx-xxxx-Mxxx-Nxxx-xxxxxxxxxxxx     (32 Hex-Ziffern + 4 Bindestriche),
M ∈ {1, 4, 6, 7, 8},                      (Versions-Hex)
N ∈ {8, 9, a, b}.                         (Varianten-Nibble RFC)
```

Die **URN-Form** ist `urn:uuid:<kanonisch>` (RFC 9562 § 4.10,
referenziert RFC 8141).

Die **Base64-Kompaktform nach ISO/IEC 9834-8** komprimiert die 16
Byte ohne Padding in 22 Zeichen `[A-Za-z0-9_$]` (IFC-Form
`IfcGloballyUniqueId`):

```
b22 : 𝓤 → Σ²²,    bijektiv,
mit  Σ = { A..Z, a..z, 0..9, _, $ }.
```

Die **Eindeutigkeitsgarantie** von v4/v7 ist probabilistisch
(RFC 9562 § 6.1, Geburtstagsproblem):

```
P(Kollision bei N Erzeugungen aus 122 Bit Zufall)  ≈  N² / 2¹²³.
```

Für N = 10⁹ folgt P ≈ 10⁻¹⁹, deutlich unterhalb jeder
domänenrelevanten Schwelle.

## Wohldefiniertheit

- **Existenz**: 𝓤 ist nicht-leer; jede deterministische oder
  zufallsgesteuerte Auswahl gemäß § 5.4 (v4) oder § 5.7 (v7)
  liefert eine zulässige UUID.
- **Eindeutigkeit (probabilistisch)**: Die Wahrscheinlichkeit
  einer Kollision in 𝓤 ist bei korrekter Erzeugung
  vernachlässigbar (siehe oben). Die Eindeutigkeit ist nicht
  konstruktiv erzwingbar (es gibt kein zentrales Verzeichnis),
  sondern als Garantie der Erzeugungsverfahren formuliert.
- **Persistenz**: Eine UUID ist nach Vergabe **unveränderlich**.
  Implementierungen, die UUIDs „rotieren" oder „rekonstruieren",
  sind nicht regelkonform. In der App folgt daraus, dass UUIDs in
  unveränderlichen Werttypen (Kotlin `value class` über `UUID`)
  gehalten werden.
- **Versions-Bestimmtheit**: Die Versions-Bits eindeutig
  identifizieren das Erzeugungsverfahren; eine UUID kann ohne
  Kontextwissen daraufhin geprüft werden.
- **Bijektivität der Repräsentationen**: Kanonisch-String,
  ISO/IEC 9834-8-Base64 (22 Zeichen) und Binärform (16 Byte)
  sind paarweise bijektiv ineinander überführbar; jede dieser
  Formen identifiziert dieselbe UUID.
- **Nicht-Zirkularität**: Die Definition stützt sich auf Bits,
  Bytes, deterministische Bit-Layouts und Wahrscheinlichkeit. Sie
  enthält keinen Verweis auf Glossarbegriffe und ist daher
  zirkelfrei.

## Empfehlung: UUID v7

Für die App ist **UUID v7** der Default für neu erzeugte Elemente.
Begründung:

- **Zeit-Sortierbarkeit**: Die ersten 48 Bit kodieren den
  Erzeugungszeitstempel in Unix-Millisekunden (big-endian). Eine
  lexikografische Sortierung der Binär- oder String-Form ergibt
  damit eine zeitliche Sortierung — günstig für B-Tree-Indizes,
  Log-Strukturen und Replikations-Reihenfolge.
- **Native DB-Unterstützung**: PostgreSQL 18 (2025) führt die
  Funktion `uuidv7()` direkt; weitere Datenbanken folgen.
- **Tausch-kompatibel mit v4**: An Stellen, an denen kein
  Zeitbezug gewünscht ist (Privacy-Anforderungen, kryptografische
  Tokens), kann v4 verwendet werden, ohne das Identitätsmodell zu
  ändern.

UUID v1 (MAC-Adresse + Zeit) wird nicht verwendet (Privacy-
Probleme, MAC-Spoofing-Risiko, in RFC 9562 als „legacy"
gekennzeichnet). UUID v3/v5 (Namens-Hashing) sind für deterministische
Identifikation von Konfigurations-Konstanten nützlich, nicht
für identitätstragende Element-Instanzen.

## Foreign-Key-Regel (kritisch)

Foreign Keys aller Domänenobjekte (Verbindungen, Aggregate,
BCF-Issues, Bemessungs-Datensätze) referenzieren **ausschließlich**
die UUID — niemals `positionsnummer` oder `produktkennzeichnung`.

Diese Regel ist die Schutzlinie der referentiellen Integrität:

- Eine Positionsnummer ist mutable; Renumbering bei Reklassifikation
  oder Plan-Revision würde Fremdschlüssel brechen.
- Eine Produktkennzeichnung ist von der Charge ererbt; ein
  Materialwechsel würde die Beziehung trennen, obwohl die
  Element-Identität gleich bleibt.
- Die UUID ist als Surrogatschlüssel fachlich-semantik-frei und
  wird über die gesamte Lebensdauer des Elements **nie**
  überschrieben — auch nicht bei IFC-/BTLx-Re-Import (siehe
  Quellenkonflikt).

## CAD-/BIM-Interoperabilität

| Container        | UUID-Slot                        | Form                              |
|------------------|----------------------------------|-----------------------------------|
| App intern       | 16-Byte-Binär in `value class`  | UUID v7 nach RFC 9562             |
| API / JSON       | kanonisch 8-4-4-4-12 Hex         | RFC 9562 § 4                      |
| URN / Linked Data| `urn:uuid:<kanonisch>`           | RFC 9562 § 4.10                   |
| IFC              | `IfcGloballyUniqueId`            | 22-stellig Base64 (ISO/IEC 9834-8)|
| BTLx             | `Part/@GUID`                     | kanonisch 8-4-4-4-12 oder 22-stellig (Spec lässt beides zu) |
| BCF              | `Topic/@Guid`, `Comment/@Guid`   | kanonisch                         |

**Externe GUIDs (CAD-Re-Import)** werden **nicht** in die App-UUID
übernommen. Stattdessen führt jedes Element optionale
Mapping-Felder

```
ifc_global_id : String?   (22-stellig Base64; aus letztem IFC-Import)
btlx_guid     : String?   (aus letztem BTLx-Import)
revit_unique_id : String? (CAD-spezifisch; bei Bedarf)
```

zur Rückverfolgung. Die Mapping-Felder sind ohne Identitätsanspruch
geführt und dürfen sich bei jedem Re-Import ändern.

## Beziehungen

- **Oberbegriff**: keiner. UUID ist ein technisches Hilfskonzept.
- **Verwendung**:
  - Pflichtfeld jedes **Elements** (`element`).
  - Pflichtfeld jedes identitätstragenden Aggregats
    (`verbindung`, `tragwerk`, `dach`, `dachaufbau`,
    `bauteil_aggregat` — Folgearbeit).
  - Schlüssel aller **Foreign-Key-Beziehungen** in der
    Persistenzschicht.
- **Abgrenzung**:
  - **Positionsnummer** (`positionsnummer`): humanlesbarer
    Geschäftsschlüssel, mutable, scoped pro Projekt + Kategorie.
    Trägt **keine** Foreign Keys. Andere Spur, anderer Zweck.
  - **Produktkennzeichnung** (`produktkennzeichnung`):
    normativ kodifizierte Charge-/Produkt-Identifikation
    (DIN 4074, DIN EN 14080 etc.). Identifiziert die Charge,
    nicht das Element. Andere Spur, anderer Zweck. **Verortung
    am Werkstoff, nicht am Element direkt**: Der Zugriff vom
    Element aus läuft strikt
    `element.werkstoff.produktkennzeichnung` (Memory
    `project_bauteil_identifikation` — die drei
    Identifikator-Spuren am Element sind eine Modellierungs-Sicht;
    die Produktkennzeichnung ist indirekt über den Werkstoff
    erreichbar).
  - **Bezeichnung** (freier Anzeigename): hat keinen
    Identitätsanspruch.
  - **IFC GlobalId**: `IfcGloballyUniqueId` ist die
    IFC-Persistenz-Repräsentation einer UUID, kein eigener
    Identifikator. Die App führt eine **eigene** UUID;
    `ifc_global_id` wird als Mapping-Feld gehalten.
  - **BTLx GUID**: `Part/@GUID`, analog Mapping-Feld.
  - **Datenbank-Primärschlüssel**: in der Persistenzschicht
    fällt der Primärschlüssel mit der UUID zusammen, ist aber
    konzeptuell ein anderer Begriff (Datenbankebene vs.
    Domänenebene; Khorikov 2019).

## Implementierungshinweis

Datentyp (Domänen-Schicht, Kotlin, Schicht
`zimmermann.domain.identifikation`):

```kotlin
package zimmermann.domain.identifikation

import zimmermann.domain.Resultat
import java.util.UUID as JavaUUID

/**
 * Universally Unique Identifier nach RFC 9562.
 * Glossar: hg_uuid.md
 *
 * Default-Version: v7 (zeit-sortierbar, B-Tree-freundlich).
 * v4 nur bei expliziter Privacy-Anforderung.
 *
 * Foreign-Key-Regel: alle Verweise auf Elemente/Aggregate
 * referenzieren ausschließlich diesen Typ — niemals
 * Positionsnummer oder Produktkennzeichnung.
 *
 * Validierung erfolgt ausnahmslos über die Factory-Funktionen im
 * Companion mit Rückgabetyp `Resultat<Uuid, UuidParseFehler>`. Die
 * Domänen-Schicht wirft niemals Exceptions; Java-Boundary-Aufrufe
 * (`JavaUUID.fromString`) werden in expliziten try/catch-Blöcken
 * gefangen und in `Resultat.Fehler` gewrappt. Vorbild:
 * `zimmermann.domain.koordinaten.LokalePlatzierung.aus(...)`.
 */
@JvmInline
value class Uuid internal constructor(val wert: JavaUUID) {

    /** Kanonische Form 8-4-4-4-12. */
    fun kanonisch(): String = wert.toString()

    /** URN-Form `urn:uuid:...`. */
    fun urn(): String = "urn:uuid:${wert}"

    /** IFC-Form: 22-stellig Base64 nach ISO/IEC 9834-8. */
    fun ifcGlobalId(): String = IfcGuidCodec.encode(wert)

    companion object {
        /** Neue UUID v7 (Default für Element-Erzeugung). */
        fun neuV7(): Uuid = Uuid(UuidV7Generator.next())

        /** Neue UUID v4 (kein Zeitbezug; Privacy-Modus). */
        fun neuV4(): Uuid = Uuid(JavaUUID.randomUUID())

        /**
         * Parst eine UUID aus der kanonischen 8-4-4-4-12-Form.
         *
         * Java-Boundary: `JavaUUID.fromString` kann eine
         * `IllegalArgumentException` werfen; sie wird hier
         * abgefangen und in `Resultat.Fehler` gewrappt.
         * Die Domänen-Schicht propagiert keine Exceptions.
         */
        fun ausKanonisch(s: String): Resultat<Uuid, UuidParseFehler> =
            try {
                Resultat.Erfolg(Uuid(JavaUUID.fromString(s)))
            } catch (_: IllegalArgumentException) {
                Resultat.Fehler(UuidParseFehler.UngueltigesFormat)
            }

        /** Aus IFC-22-stellig Base64 parsen. */
        fun ausIfcGlobalId(s: String): Resultat<Uuid, UuidParseFehler> = IfcGuidCodec.decode(s)
    }
}

/** ISO/IEC 9834-8 / IFC Base64 22-Codec (kein RFC-Base64; eigenes Alphabet). */
internal object IfcGuidCodec {
    fun encode(u: JavaUUID): String = TODO("Implementierung in Folge-Auftrag")
    fun decode(s: String): Resultat<Uuid, UuidParseFehler> = TODO("Implementierung in Folge-Auftrag")
}

/** UUID-v7-Generator (Unix-ms + Zufall). */
internal object UuidV7Generator {
    fun next(): JavaUUID = TODO("Implementierung in Folge-Auftrag; "
        + "PostgreSQL 18 uuidv7() bzw. java.util.UUID-Selbstbau")
}
```

- **Einheit**: keine (Bit-Wort).
- **Identität (im Identitätsbegriff)**: Eine UUID **ist** die
  Identität; sie hat keine eigene Identität jenseits ihres
  Bit-Werts.
- **Vergabe**: ausschließlich systemseitig bei Element-Erzeugung.
  Niemals händisch in Konstruktor-Aufrufen setzen.
- **Persistenz-Garantie**:
  - Niemals überschreiben.
  - Bei IFC-/BTLx-Re-Import nicht ersetzen; externe GUIDs landen
    in eigenen Mapping-Feldern.
  - Bei Modell-Migrationen (Schema-Änderungen) wandert die UUID
    unverändert mit.
- **Invarianten** (in Codec-Funktionen prüfen, bei Verletzung
  `Resultat.Fehler`; niemals Exception):
  1. 128-Bit-Wert ist nicht der Null-UUID
     (`00000000-0000-0000-0000-000000000000`).
  2. Versions-Nibble ∈ {1, 4, 6, 7, 8}.
  3. Varianten-Nibble ∈ {8, 9, a, b}.
- **Edge Cases**:
  - **Null-UUID** (`00000000-…`): in der App **verboten** als
    Element-UUID (verwechslungsanfällig mit „nicht initialisiert").
    Codec lehnt Parsing ab.
  - **UUID v1 mit MAC-Adresse**: bei Import aus Altsystemen
    zulässig; bei Eigen-Erzeugung **verboten** (Privacy).
  - **Kollisionsverdacht**: bei Persistenz-Insert mit DB-UNIQUE-
    Constraint-Verletzung wird ein Programmierfehler vermutet
    (Kollisionswahrscheinlichkeit ≈ 10⁻¹⁹); Behandlung als
    `Entartet.UuidKollision` mit Logeintrag.
  - **String-Parsing**: case-insensitive für Hex-Ziffern,
    case-sensitive für ISO/IEC 9834-8-Base64.
- **Mapping-Felder für externe GUIDs** (auf Element-Ebene, nicht
  hier):
  - `ifc_global_id: String?` (22-stellig Base64; letzter
    IFC-Import).
  - `btlx_guid: String?` (BTLx-Import).
  - Weitere CAD-spezifische Felder nach Bedarf
    (`revit_unique_id`, `archicad_global_id` …).

## Quellen

**Primär (normativ):**

- RFC 9562:2024, „Universally Unique IDentifiers (UUIDs)", IETF,
  Mai 2024.
- ISO/IEC 9834-8:2014 / ITU-T X.667, „Information technology —
  Procedures for the operation of object identifier registration
  authorities — Part 8: Generation of universally unique
  identifiers (UUIDs) and their use in object identifiers".
- ISO 16739-1:2024, „Industry Foundation Classes (IFC) — Part 1:
  Data schema" (Datentyp `IfcGloballyUniqueId`,
  Vererbungsregel UR1).
- PostgreSQL Global Development Group: *PostgreSQL 18
  Documentation*, Funktion `uuidv7()`.

**Sekundär:**

- Date, C. J.: *An Introduction to Database Systems.* 8. Auflage,
  Addison-Wesley 2003.
- Khorikov, V.: „Entity Identity vs Database Primary Key".
  enterprisecraftsmanship.com, 2019.
- Vernon, V.: *Implementing Domain-Driven Design.* Addison-Wesley
  2013.
- Evans, E.: *Domain-Driven Design.* Addison-Wesley 2003.
- Ambler, S. W.; Sadalage, P. J.: *Refactoring Databases —
  Evolutionary Database Design.* Addison-Wesley 2006.
- design2machine: *BTLx 2.x Specification* (Stand 2024).

**Korpus (nicht autoritativ):**

- buildingSMART International: *IFC4.3 Documentation*,
  Version 4.3.2.0, 2024.
- Wikipedia, Lemmata „Universally unique identifier", „GUID"
  (abgerufen 2026-05-08).
