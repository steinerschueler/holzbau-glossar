---
id: verstaerkungselement
benennung: Verstärkungselement
synonyme: [Verstärkungsschraube, Verstärkungs-Vollgewindeschraube]
abgelehnte_benennungen: [Verbindungsmittel, Bauteil, Verstärkung, "reinforcement screw", "reinforcement", "Bewehrung"]
oberbegriff: element
begriffstyp: generisch
voraussetzungen: [element, uuid, verbindungsmittel, bauteil, faserrichtung, werkstoff, werkstoff_stahl, toleranzen]
abgrenzung_zu: [verbindungsmittel, bauteil, verbinder, verbindung, element]
status: entwurf
subglossar_pendant: notwendig
quellen_primär:
  - "DIN EN 1995-1-1:2010-12 (Eurocode 5), Anhang A bzw. nationale Anhänge — Verstärkung quer zur Faser durch Vollgewindeschrauben (in der derzeitigen Ausgabe lediglich punktuell, ausführlich erst im Entwurf der Neuausgabe)."
  - "Entwurf prEN 1995-1-1:2024 (Eurocode 5, Neuausgabe ~2027, Vernehmlassungsfassung), neuer Verstärkungsabschnitt: axiale Bemessung der Verstärkungsschraube auf Herausziehen, Hineindrücken, Stabknicken; Mindestabstände."
  - "ETA-11/0190, 'Würth ASSY plus VG, ASSY 3.0, ASSY 4.0' — Vollgewindeschrauben mit europäischer technischer Bewertung; explizit als Verstärkungsmittel zugelassen."
  - "Z-9.1-519, 'Schrauben mit Vollgewinde als Verbindungsmittel und als Verstärkung von Holzbauteilen' (SPAX, allgemeine bauaufsichtliche Zulassung, DIBt)."
  - "Z-9.1-235, 'Holzschrauben mit Vollgewinde der Firma SPAX' (frühere Zulassungsfassung, ergänzend)."
  - "ETA-12/0373, 'Reisser-Schrauben — Schrauben für die Verwendung in Holzbauteilen', Verwendungsbereich Verstärkung."
  - "ISO 16739-1:2024, IFC-Entität `IfcMechanicalFastener` mit Property Set für Verstärkungsfunktion (Pset_FastenerCommon Reference + custom Pset)."
quellen_sekundär:
  - "Dietsch, P. (TUM, Lehrstuhl für Holzbau): 'Eurocode 5:2022 — Einführung in den neuen Abschnitt Verstärkungen', Vortrag, Technische Universität München, 2023."
  - "Müller, A.; Heubuch, M.: 'Stabdübelverbindungen und eingeklebte Gewindestangen in Buchen-Brettschichtholz', 25. Internationales Holzbau-Forum (IHF), Innsbruck 2019."
  - "Sigrist, C.: 'Verbindungsmittelabstände bei eng gesetzten Verstärkungs- und Verbindungsschrauben', SIA-Holzbautag Biel, 2018."
  - "Blass, H. J.; Sandhaas, C.: Ingenieurholzbau – Grundlagen der Bemessung. KIT Scientific Publishing, Karlsruhe 2016, Abschnitt 'Verstärkung quer zur Faser'."
  - "Holzbau-Handbuch, Reihe 2 'Tragwerksplanung', Teil 1 'Verbindungen', Folge 1 'Verbindungen mit stiftförmigen Verbindungsmitteln' und einschlägige Folgen zu Verstärkung, Informationsdienst Holz."
  - "Bejtka, I.; Blass, H. J.: 'Verstärkungen mit selbstbohrenden Holzschrauben', Konstruktiver Ingenieurbau, 2005."
quellenkonflikt: |
  Begriffliche Lage:
  - **DIN EN 1995-1-1:2010 (Ausgabe 2010)** behandelt
    Verstärkungen nur punktuell (z. B. Querzugverstärkungen in
    ausgeklinkten Trägern), ohne den Begriff
    „Verstärkungselement" als eigene Klasse zu führen.
  - **Entwurf EC5:2022 / 2024** (Vernehmlassungsfassung der
    Neuausgabe, Erscheinen geplant ~2027) führt einen eigenen
    Verstärkungsabschnitt mit axialer Bemessung
    (Herausziehen / Hineindrücken / Stabknicken / Material-
    festigkeit), Mindestabständen und Anwendungsregeln.
  - **ETA-11/0190** (Würth ASSY), **Z-9.1-519** (SPAX) und
    **ETA-12/0373** (Reisser) regeln die Verwendung von
    Vollgewindeschrauben sowohl als Verbindungsmittel
    (Bemessung nach EC5 Kap. 8) als auch als
    Verstärkungselement (eigene axiale Bemessung).

  Ontologische Pointe:
  Dasselbe physische Objekt — z. B. Würth ASSY 8 × 200 — kann

  - **als Verbindungsmittel** auftreten, wenn es einen Sparren-
    Pfetten-Anschluss auf Abscheren bildet (Bemessung nach
    Johansen, EC5 Kap. 8); dann wird es als
    `Verbindungsmittel`-Instanz modelliert,
  - **als Verstärkungselement** auftreten, wenn es als
    ETA-konforme Querzugverstärkung in einem ausgeklinkten
    BSH-Träger eingesetzt wird (axiale Bemessung nach EC5:2022
    bzw. ETA); dann wird es als `Verstaerkungselement`-Instanz
    modelliert.

  Konsequenz: **Funktion bestimmt die Klasse, nicht das Material.**
  Die App führt zwei getrennte Element-Subklassen mit getrennten
  UUIDs für die zwei funktionalen Auftrittsformen (Memory
  `project_element_ontologie`, Designregel 2).

  Begriffstyp-Wahl:
  Geprüft wurden zwei Varianten:
  1. `merkmal` — Verstärkungselement als Funktion-Annotation an
     einem Verbindungsmittel-Objekt. Vorteil: betont die
     ontologische Identität von Material und Verbindungsmittel.
     Nachteil: vermischt zwei unterschiedliche Bemessungs-
     Regimes in einer Klasse, widerspricht der gewählten
     sealed-interface-Hierarchie unter `element`.
  2. `generisch` — Verstärkungselement als eigenständige
     Element-Subklasse. Vorteil: konsistent mit der
     Element-Ontologie (vier Geschwister unter abstrakter
     Basisklasse), getrennte Bemessungs-Logik, getrennte IFC-
     Property-Sets, getrennte Stückliste, getrennte UUID.
     Nachteil: zwei getrennte Klassen für „dasselbe Material"
     erfordern bei Wechselverwendung explizite Re-Instanziierung.

  Festlegung: **`generisch`**. Die ontologische Pointe wird durch
  das Pflichtfeld `basis_verbindungsmittel` aufgelöst: das
  Verstärkungselement **rollt** die Verbindungsmittel-
  Spezifikation (Typ, Durchmesser, Länge, ETA) und ergänzt die
  Verstärkungs-Funktion. Damit ist die Material-Identität durch
  Verweis abgebildet, ohne die Bemessungs-Regimes zu vermischen.
  Diese Festlegung folgt EC5:2022 (Vernehmlassung) und der
  ETA-Bemessungspraxis.
---

## Prosa-Definition

Ein **Verstärkungselement** ist ein Element der App-Ontologie,
das physisch ein Verbindungsmittel ist (typisch eine
Vollgewindeschraube, seltener eine eingeklebte Gewindestange),
das jedoch nicht primär einen Anschluss zwischen Bauteilen
herstellt, sondern in einer Verstärkungsfunktion (Querzug-,
Querdruck- oder Schubverstärkung) ein einzelnes Bauteil verstärkt,
und dessen Bemessung als axial beanspruchtes Tragglied auf
Herausziehen, Hineindrücken, Stabknicken sowie auf
Materialfestigkeit nach europäischer technischer Bewertung
(ETA) bzw. nach dem Verstärkungsabschnitt der Neuausgabe von
DIN EN 1995-1-1 (EC5:2022) erfolgt.

## Mathematische Definition

Sei

- 𝓔 die Menge der Elemente nach `element`,
- 𝓤 der UUID-Raum nach `uuid`,
- 𝓥𝓜 die Menge der Verbindungsmittel nach `verbindungsmittel`,
- 𝓑 die Menge der Bauteile nach `bauteil`,
- 𝓥𝓢_τ die Menge der Verstärkungstypen
  ```
  𝓥𝓢_τ := { Querzugverstaerkung,
            Querdruckverstaerkung,
            Schubverstaerkung,
            Auflagerverstaerkung,
            AusklinkungsVerstaerkung,
            DurchbruchVerstaerkung }
  ```
  (sealed enum; eigene Folge-Einträge),
- 𝓦 die Menge der Werkstoffe (typisch Stahl der Schraube),
- 𝓔𝓣𝓐 die Menge der ETA-Referenzen (siehe `eta_referenz`),
- A := [0, 2π) die Menge der Winkel (intern Radiant; Anzeige Grad).

Dann ist ein **Verstärkungselement** das Tupel

```
VS := (uuid, geometrie, lokale_platzierung, werkstoff,
       basis_verbindungsmittel, verstaerkt,
       verstaerkungstyp, winkel_zur_faser, eta_zulassung,
       positionsnummer?, produktkennzeichnung?, bezeichnung?)
```

mit den von `element` ererbten Pflichtfeldern

- **uuid** ∈ 𝓤,
- **geometrie** ∈ 𝓖_VS ⊂ 𝓖 (1D-dominante Schrauben- bzw.
  Stangen-Geometrie, identisch zur Verbindungsmittel-Geometrie
  ihres `basis_verbindungsmittel`),
- **lokale_platzierung** ∈ SE(3),
- **werkstoff** ∈ 𝓦,

und den verstärkungselement-spezifischen Pflichtfeldern

- **basis_verbindungsmittel** ∈ 𝓥𝓜_spec: Verweis auf die zugrunde
  liegende Verbindungsmittel-Spezifikation (Typ, Nenndurchmesser,
  Nennlänge). Realisierungsoption A: UUID eines explizit angelegten
  Verbindungsmittel-Objekts. Realisierungsoption B: eingebettetes
  Spezifikations-Tupel (typ, d, ℓ, eta) ohne eigene UUID.
  Im App-Datenmodell wird Option B bevorzugt, weil ein
  Verstärkungselement **kein** Verbindungsmittel ist, sondern es
  nur seine Spezifikation ausleiht; die UUID des physischen Stücks
  ist die UUID des Verstärkungselements.
- **verstaerkt** ∈ 𝓤: UUID des **einen** Bauteils, das verstärkt
  wird. Anders als ein Verbindungsmittel, das ≥ 2 Bauteile
  verbindet, wirkt ein Verstärkungselement auf genau ein Bauteil.
- **verstaerkungstyp** ∈ 𝓥𝓢_τ,
- **winkel_zur_faser** φ ∈ A: der Winkel zwischen der Schrauben-
  achse und der Faserrichtung des verstärkten Bauteils im Punkt
  des Eindrehens (typisch φ = π/2 für klassische Querzug-/
  Querdruckverstärkung, φ = π/4 für geneigt eingedrehte
  Schubverstärkung); zentral für die Bemessung,
- **eta_zulassung** ∈ 𝓔𝓣𝓐: Pflicht, weil Verstärkungselemente
  nahezu ausschließlich ETA-zugelassene Vollgewindeschrauben sind
  (ETA-11/0190, Z-9.1-519, Z-9.1-235, ETA-12/0373).

Es ist 𝓥𝓢 ⊂ 𝓔, d. h. die Menge der Verstärkungselemente ist eine
disjunkte Teilmenge der Element-Menge.

## Wohldefiniertheit

- **Existenz**: Für jedes konkrete in einem Bauteil eingedrehte
  Verstärkungselement lässt sich das obige Tupel erfassen.
  Mindestkonfiguration: basis = Würth ASSY 8 × 200 mit
  ETA-11/0190, verstaerkt = UUID eines BSH-Trägers,
  verstaerkungstyp = Querzugverstaerkung, winkel_zur_faser = π/2.
- **Eindeutigkeit der Identität**: über `uuid` (geerbt von
  `element`). Das Verstärkungselement hat eine **eigene**
  UUID, unabhängig von der UUID eines etwaigen homonymen
  Verbindungsmittels.
- **Disjunktheit zu Verbindungsmittel**:
  𝓥𝓢 ∩ 𝓥𝓜 = ∅ — auch wenn dieselbe physische Schraube in einem
  alternativen Einbau-Szenario als Verbindungsmittel klassifiziert
  würde, ist die konkrete Instanz im konkreten Modell entweder
  Verbindungsmittel oder Verstärkungselement, niemals beides
  gleichzeitig.
- **Verstärkt genau ein Bauteil**: |verstaerkt| = 1.
  Das Verstärkungselement wirkt auf **ein** Bauteil. Erstreckt
  sich die Schraube über mehrere Bauteile (durchgehend von
  Bauteil A in Bauteil B), wird sie typischerweise als
  Verbindungsmittel klassifiziert (verbindet zwei Bauteile auf
  Abscheren oder Herausziehen), nicht als Verstärkungselement
  eines einzelnen.
- **Winkel zur Faser**: φ ist der Winkel zwischen der Schraubenachse
  (entlang der `geometrie.achse` projiziert in W) und der
  Faserrichtung des verstärkten Bauteils. Für faserlose oder
  richtungsisotrope Werkstoffe (Spanplatte, MDF) ist
  Verstärkungseinsatz untypisch und nicht im Glossar formal
  definiert; das Pflichtfeld `winkel_zur_faser` ist im
  Wertebereich [0, π/2] ⊂ A; größere Winkel werden durch
  Symmetrie reduziert.
- **ETA-Pflicht**: Verstärkungselemente erfordern die ETA-
  Zulassung, weil sie ausschließlich auf Basis ETA-zertifizierter
  Hersteller-Spezifikationen bemessen werden. Eine Vollgewinde-
  schraube ohne ETA darf nicht als Verstärkungselement
  klassifiziert werden; sie wäre dann „Verbindungsmittel mit
  zweifelhafter Eignung".
- **Foreign-Key-Regel**: `verstaerkt` und (falls verwendet)
  `basis_verbindungsmittel` referenzieren ausschließlich UUIDs.
- **Nicht-Zirkularität**: Die Definition stützt sich auf
  `element`, `uuid`, `verbindungsmittel` (ausschließlich für die
  Spezifikations-Übernahme), `bauteil` (für das verstärkte
  Bauteil), `faserrichtung` (für den Bemessungs-Winkel) und
  `toleranzen`. Sie verweist nicht auf `verbindung` oder
  `verstaerkungselement` selbst.

## Erläuterung (nicht normativ)

### Werkstoff

Verstärkungselemente haben **praktisch immer Werkstoff
`werkstoff_stahl`** — sie sind nahezu ausschließlich
Vollgewindeschrauben mit ETA-Zulassung (Würth ASSY, SPAX, Reisser).
Die Stahlgüte ist typisch ein höherfester carbonierter Stahl mit
charakteristischem Zugwiderstand F_t,Rk nach ETA. Eingeklebte
Gewindestangen (Sonderfall) sind ebenfalls Stahl. Holz-/Hartholz-
Verstärkungen sind in dieser App nicht vorgesehen.

### Ontologische Pointe

Dasselbe physische Objekt — eine ETA-11/0190-konforme
Würth ASSY 8 × 200 — ist:

- **Verbindungsmittel**, wenn es eine Sparren-Pfetten-Verbindung
  auf Abscheren herstellt. Bemessung nach Johansen (EC5 Kap. 8).
  Datenmodell: `Verbindungsmittel`-Instanz mit `verbindet` =
  [Sparren-UUID, Pfetten-UUID].
- **Verstärkungselement**, wenn es als ETA-konforme Querzug-
  verstärkung in einem ausgeklinkten BSH-Träger eingesetzt wird.
  Bemessung axial (Herausziehen, EC5:2022). Datenmodell:
  `Verstaerkungselement`-Instanz mit `verstaerkt` =
  BSH-Träger-UUID.

**Funktion bestimmt die Klasse, nicht das Material.** Der gleiche
Schraubentyp, der gleiche Werkstoff, die gleichen Maße — aber
zwei verschiedene Element-Subklassen, weil die Bemessungs-Regimes
unterschiedlich sind (Abschertheorie vs. axiale Theorie).

### Bemessungs-Regime

Die Bemessung des Verstärkungselements gliedert sich in vier
Tragfähigkeits-Nachweise (EC5:2022-Entwurf, ETA-11/0190,
Z-9.1-519):

1. **Herausziehen / Hineindrücken** (axiale Tragfähigkeit
   F_ax,Rk): aus dem charakteristischen Ausziehparameter f_ax,k
   (ETA-Wert), Nenndurchmesser d, effektiver Eindrehlänge ℓ_ef
   und Faserwinkel-Korrektur. Formel typischerweise
   ```
   F_ax,Rk = π · d · ℓ_ef · f_ax,k · (90° / α + 1)^(-1)
   ```
   bzw. analog nach ETA. Wert wird aus ETA übernommen.
2. **Stabknicken** der Schraube (bei längeren Verstärkungs-
   schrauben in Querdruckanwendung): nach Euler bzw. nach
   Knickkriterium der ETA, mit der Schraube als druck-
   beanspruchtem Stab in elastischer Bettung des umgebenden
   Holzes.
3. **Materialfestigkeit der Schraube** (Zug- oder Druck-
   spannung im Schaft): nach Stahl-Festigkeitsklasse der
   Schraube; ETA gibt charakteristischen Zugwiderstand F_t,Rk.
4. **Mindestabstände** (untereinander, zum Rand, zur
   Hirnholzfläche): nach ETA bzw. EC5:2022. Die Mindestabstände
   bei eng gesetzten Verstärkungsschrauben sind ein eigenes
   Forschungsfeld (Sigrist 2018).

Die App liefert die geometrische Eingabe (Achse, Winkel zur
Faser, Eindrehlänge); die Bemessungs-Schicht (Folgearbeit)
führt die Tragfähigkeits-Nachweise.

### Anwendungsfälle

- **Querzugverstärkung** in ausgeklinkten BSH-Trägern,
  Durchbrüchen, gekrümmten Trägern, Satteldachträgern.
  Die Schraube wird **quer zur Faser** (φ ≈ π/2) eingedreht und
  überträgt die im Holz lokal entstehenden Zugspannungen quer
  zur Faserrichtung.
- **Querdruckverstärkung** unter konzentrierten Auflagern
  (Schwellendruck, Stützenfußauflager). Die Schraube nimmt einen
  Teil der Druckkraft als axiales Tragglied auf, das umgebende
  Holz wird entlastet.
- **Schubverstärkung** in Trägern mit erhöhter Schubbeanspruchung
  (Kerven, Anschlüsse). Die Schraube wird **geneigt** zur Faser
  (φ ≈ π/4) eingedreht und nimmt eine Komponente der schiefen
  Hauptzugspannung auf.
- **Auflagerverstärkung** an Pfetten- und Sparrenfüßen.
- **Ausklinkungs- und Durchbruchverstärkung** bei lokal
  geschwächten Trägerquerschnitten.

### IFC- und BTLx-Mapping

| Element                | IFC                                                   | BTLx                                  |
|------------------------|-------------------------------------------------------|---------------------------------------|
| Verbindungsmittel      | IfcMechanicalFastener                                 | Processing oder eigenes Part          |
| **Verstärkungselement**| **IfcMechanicalFastener** + Custom-Pset `IsReinforcement` | **wie VM, plus Funktionsattribut**    |

Die IFC-Klasse ist dieselbe wie für Verbindungsmittel
(`IfcMechanicalFastener`); die Verstärkungs-Funktion wird durch
ein eigenes Property Set bzw. eine Custom-Property unterschieden.
Hersteller-BIM-Bibliotheken (Würth ASSY, SPAX) liefern in der
Regel die ETA-Referenz mit; die App ergänzt die Funktions-
Annotation.

In BTLx erscheint das Verstärkungselement typisch als eigenes
`Part` mit GUID (analog zu langen Vollgewindeschrauben), weil es
in einer eigenen Stückliste mit ETA-Bezug geführt wird.

### Stücklisten-Trennung

Verstärkungselemente führt die App in einer **eigenen Stückliste**,
getrennt von Bauteilen, Verbindungsmitteln und Verbindern. Das ist
in der Praxis sinnvoll, weil Verstärkungsschrauben mit ETA-Bezug
nachweispflichtig sind und in der Statik separat aufgeführt
werden müssen.

## Beziehungen

- **Oberbegriff**: `element`.
- **Spezialisierungen** (eigene Einträge folgen):
  - **Querzugverstärkung** (`querzugverstaerkung`).
  - **Querdruckverstärkung** (`querdruckverstaerkung`).
  - **Schubverstärkung** (`schubverstaerkung`).
  - **Auflagerverstärkung** (`auflagerverstaerkung`).
  - **Ausklinkungsverstärkung** (`ausklinkungsverstaerkung`).
  - **Durchbruchverstärkung** (`durchbruchverstaerkung`).
- **Bestandteile (partitiv)**: alles geerbt von `element` plus
  basis_verbindungsmittel, verstaerkt, verstaerkungstyp,
  winkel_zur_faser, eta_zulassung.
- **Verwendung**:
  - Bestandteil einer **Verbindung** (`verbindung`):
    Verstärkungen werden in der Verbindungs-Aggregat-Klasse
    optional als eigene Liste geführt.
  - Bestandteil eines **Tragwerks** (`tragwerk`): erweitert die
    Element-Menge.
- **Abgrenzung**:
  - **Verbindungsmittel** (`verbindungsmittel`): selbe physische
    Objektklasse, andere **Funktion** und andere **Bemessung**.
    Die ontologische Trennung folgt EC5:2022 und der ETA-
    Bemessungspraxis. Funktion bestimmt die Klasse, nicht das
    Material.
  - **Bauteil** (`bauteil`): Verstärkungselemente sind keine
    Bauteile (auch nicht „kleine Bauteile"); sie sind Element-
    Subklassen mit eigener Bemessungslogik. Die Trennung folgt
    EC5:2022.
  - **Verbinder** (`verbinder`): vermittelndes Stück Stahl/Holz,
    nicht eine Funktionsrolle eines Verbindungsmittels.
    Verstärkungselement ist hingegen ein Verbindungsmittel-
    Objekt in funktionaler Verstärkungsrolle.
  - **Verbindung** (`verbindung`): Aggregat-Klasse;
    Verstärkungselemente können Bestandteil einer Verbindung
    sein, sind aber nicht selbst Verbindung.
  - **Element** (`element`): abstrakter Oberbegriff;
    Verstärkungselement ist eine konkrete Subklasse.

## Implementierungshinweis

Datentyp (Domänen-Schicht, Kotlin, Schicht
`domain.element.verstaerkung`):

```kotlin
package domain.element.verstaerkung

import domain.element.Element
import domain.element.verbindungsmittel.VerbindungsmittelTyp
import domain.geometrie.Geometrie
import domain.geometrie.LokalePlatzierung
import domain.holzbau.Werkstoff
import domain.identifikation.Positionsnummer
import domain.identifikation.Produktkennzeichnung
import domain.identifikation.ETAReferenz
import java.util.UUID

/** Verstärkungstyp nach EC5:2022-Entwurf und ETA. */
sealed interface VerstaerkungsTyp {
    data object Querzugverstaerkung      : VerstaerkungsTyp
    data object Querdruckverstaerkung    : VerstaerkungsTyp
    data object Schubverstaerkung        : VerstaerkungsTyp
    data object Auflagerverstaerkung     : VerstaerkungsTyp
    data object AusklinkungsVerstaerkung : VerstaerkungsTyp
    data object DurchbruchVerstaerkung   : VerstaerkungsTyp
}

/**
 * Eingebettete Verbindungsmittel-Spezifikation, die das
 * Verstärkungselement von einem Verbindungsmittel-Typ ausleiht.
 * Eigene UUID hat sie nicht — die UUID gehört dem
 * Verstärkungselement.
 */
data class VerbindungsmittelSpezifikation(
    val typ: VerbindungsmittelTyp,
    val nenndurchmesser: Double,        // mm
    val nennlaenge: Double              // mm
)

/**
 * Verstärkungselement: physisch ein Verbindungsmittel
 * (typisch Vollgewindeschraube), funktional in einer
 * Verstärkungsrolle nach EC5:2022 / ETA.
 *
 * Glossar: hg_verstaerkungselement.md
 *
 * Ontologische Pointe: dasselbe Material kann Verbindungsmittel
 * ODER Verstärkungselement sein — nie beides gleichzeitig.
 * Funktion bestimmt die Klasse.
 *
 * IFC: IfcMechanicalFastener + Custom-Pset für Verstärkungs-
 *       Funktion (z. B. IsReinforcement = TRUE).
 * BTLx: typisch eigenes Part mit @GUID + Funktionsattribut.
 */
data class Verstaerkungselement(
    override val uuid: UUID,
    override val geometrie: Geometrie,
    override val lokalePlatzierung: LokalePlatzierung,
    override val werkstoff: Werkstoff,
    val basisVerbindungsmittel: VerbindungsmittelSpezifikation,
    val verstaerkt: UUID,                        // FK auf das verstärkte Bauteil
    val verstaerkungstyp: VerstaerkungsTyp,
    val winkelZurFaser: Double,                  // Radiant, in [0, π/2]
    val etaZulassung: ETAReferenz,               // Pflicht (kein null)
    override val positionsnummer: Positionsnummer? = null,
    override val produktkennzeichnung: Produktkennzeichnung? = null,
    override val bezeichnung: String? = null
) : Element {
    init {
        // 1. winkelZurFaser in [0.0, PI/2 + Toleranzen.WINKEL_EPS]
        // 2. basisVerbindungsmittel.nenndurchmesser > Toleranzen.LAENGE_EPS
        // 3. basisVerbindungsmittel.nennlaenge      > Toleranzen.LAENGE_EPS
        // 4. verstaerkt != uuid                     (kein Selbstbezug)
        // 5. etaZulassung-Existenz konsistenter Wert (in ETAReferenz geprüft)
    }
}
```

- **Einheit**: Längen in mm (Double); Winkel intern in Radiant
  (Anzeige in Grad).
- **Identität**: `uuid` von `element` ererbt. Die UUID des
  Verstärkungselements ist **nicht** die UUID eines
  Verbindungsmittel-Objekts; die App führt die Verstärkungs-
  schraube als eigenes physisches Stück.
- **Spezifikations-Verweis**: das Pflichtfeld
  `basisVerbindungsmittel` ist als **eingebettetes Tupel**
  (kein UUID-Verweis) modelliert, weil ein Verstärkungselement
  in der App nicht über ein paralleles Verbindungsmittel-Objekt
  „gehängt" wird, sondern dessen Spezifikation rollt. Damit
  bleibt die Element-Hierarchie sauber disjunkt.
- **Foreign-Key-Regel**: `verstaerkt: UUID` referenziert das
  verstärkte Bauteil ausschließlich per UUID.
- **IFC-Mapping**:
  - IFC-Klasse: `IfcMechanicalFastener`.
  - Custom-Pset oder Property: `Pset_Reinforcement` (eigenes
    App-Pset) oder Custom-Property `IsReinforcement = TRUE`,
    plus `ReinforcementType` (Querzug / Querdruck / Schub).
  - Property Set zusätzlich: `Pset_FastenerCommon` (Reference,
    NominalDiameter, NominalLength) wie für reguläre
    Verbindungsmittel.
- **BTLx-Mapping**:
  - **Standardfall**: eigenes `Part` mit `@GUID` + Funktions-
    attribut (z. B. UserAttribute `Function = Reinforcement`).
  - **Alternativfall**: kombiniertes `Lag-Screw`-Processing am
    verstärkten Bauteil + Funktionsattribut.
- **Edge Cases**:
  - **Verstärkungselement ohne ETA**: nicht erlaubt;
    `Entartet.VerstaerkungOhneEta`. Eine Vollgewindeschraube ohne
    ETA muss als Verbindungsmittel mit zweifelhafter Eignung,
    nicht als Verstärkungselement klassifiziert werden.
  - **Verstärkungselement, das ein Plattenwerkstoff-Bauteil
    verstärkt**: faserlose Werkstoffe sind im typischen
    Anwendungsfall nicht relevant; Modellierung möglich, aber
    `winkelZurFaser` verliert Bemessungs-Bedeutung. Die App
    erlaubt diese Modellierung mit Warnung in der Bemessungs-
    Schicht.
  - **Verstärkungselement, das mehrere Bauteile durchquert**:
    nicht als Verstärkungselement modellieren, sondern als
    Verbindungsmittel mit |verbindet| ≥ 2.
  - **Doppel-Klassifikation**: dieselbe physische Schraube darf
    nicht gleichzeitig als Verbindungsmittel und als
    Verstärkungselement modelliert sein. Wird sie funktional in
    beiden Rollen wirksam (sehr selten), ist die Bemessung
    konservativ als Verstärkungselement zu führen (axial), oder
    der Konstruktionsfall wird vermieden.
- **Abgeleitete Eigenschaften**:
  - `effektiveEindrehlaenge(): Double` — die für die Auszieh-
    Bemessung wirksame Länge ℓ_ef im Holz (geometrische
    Berechnung aus Achse, Bauteilgeometrie und Eindrehrichtung).
  - `geometrieInWelt(): GeometrieInW` — Schrauben-Sweep unter
    `lokalePlatzierung` transformiert nach W.
  - `axialeTragfaehigkeit(): Double` — F_ax,Rk nach ETA bzw.
    EC5:2022 (Bemessungs-Schicht, Folgearbeit).
- **Bezeichner-Konvention** (CLAUDE.md): Domänen-Klasse heißt
  `Verstaerkungselement` (deutsch ohne Umlaut, Glossarbegriff).
  Spezialisierungen heißen `Querzugverstaerkung`,
  `Querdruckverstaerkung`, `Schubverstaerkung`.

## Quellen

**Primär (normativ):**

- DIN EN 1995-1-1:2010-12, „Eurocode 5 – Bemessung und
  Konstruktion von Holzbauten – Teil 1-1", Anhang/Verstärkungs-
  abschnitt.
- Entwurf prEN 1995-1-1:2024 (EC5-Neuausgabe, Vernehmlassung,
  Erscheinen ~2027), neuer Verstärkungsabschnitt.
- ETA-11/0190 (Würth ASSY).
- Z-9.1-519 (SPAX Vollgewindeschrauben, DIBt).
- Z-9.1-235 (SPAX, frühere Zulassung).
- ETA-12/0373 (Reisser).
- ISO 16739-1:2024, IFC-Entität `IfcMechanicalFastener`.

**Sekundär:**

- Dietsch, P. (TUM): „Eurocode 5:2022 — Einführung in den neuen
  Abschnitt Verstärkungen". TUM, 2023.
- Müller, A.; Heubuch, M.: „Stabdübelverbindungen und
  eingeklebte Gewindestangen in Buchen-BSH". 25. IHF Innsbruck
  2019.
- Sigrist, C.: „Verbindungsmittelabstände bei eng gesetzten
  Verstärkungs- und Verbindungsschrauben". SIA-Holzbautag Biel,
  2018.
- Blass, H. J.; Sandhaas, C.: *Ingenieurholzbau – Grundlagen
  der Bemessung.* KIT Scientific Publishing, Karlsruhe 2016.
- Bejtka, I.; Blass, H. J.: „Verstärkungen mit selbstbohrenden
  Holzschrauben". Konstruktiver Ingenieurbau, 2005.
- Holzbau-Handbuch, Reihe 2, Teil 1, Folgen zu Verstärkung,
  Informationsdienst Holz.

**Korpus (nicht autoritativ):**

- Würth, SPAX, Reisser: Hersteller-Bemessungssoftware
  (Eingabemasken decken die ETA-Bemessungspraxis ab).
- Holzbau Deutschland, Merkblatt „Begriffe und Klassifizierungen
  für den Holzbau" (abgerufen 2026-05-08).
