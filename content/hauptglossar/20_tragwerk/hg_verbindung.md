---
id: verbindung
benennung: Verbindung
synonyme: [Anschluss, Knoten, Stoss]
abgelehnte_benennungen: [Verbindungsmittel, Verbinder, "joint", "connection", "node", "Holzverbindung"]
oberbegriff: null
begriffstyp: aggregat
voraussetzungen: [bauteil, verbindungsmittel, verbinder, verstaerkungselement, uuid, toleranzen]
abgrenzung_zu: [bauteil, verbindungsmittel, verbinder, verstaerkungselement, element, tragwerk, konstruktionsdetail]
status: entwurf
theorie_pflichtig: required
quellen_primär:
  - "DIN EN 1995-1-1:2010-12 (Eurocode 5), Kapitel 8 'Anschlüsse mit metallischen Verbindungsmitteln', insbesondere 8.1 (Allgemeines), 8.2 (Tragfähigkeit von stiftförmigen Verbindungsmitteln auf Abscheren) — Konzept der Verbindung als Aggregat."
  - "DIN EN 1995-1-1:2010-12, Kapitel 10 'Klebungen' — Klebung als Sonderform der Verbindung."
  - "DIN EN 1995-1-1:2010-12, Abschnitt 8.2.3 'Indirekte Verbindungen' — Verbindungen mit vermittelndem Verbinder."
  - "SIA 265:2021 'Holzbau', Anhang A 'Verbindungen und Verbindungsmittel', insbesondere Mischungsverbot von verschiedenartigen Verbindungsmitteln in einer Verbindung."
  - "ÖNORM B 1995-1-1:2019, nationale Anwendungsbestimmungen zum Eurocode 5, Kap. 8."
  - "DIN 1052:2008-12, Abschnitt 12 'Verbindungen'."
  - "ISO 16739-1:2024 'Industry Foundation Classes (IFC) – Part 1: Data schema', Beziehungs-Entität `IfcRelConnectsElements` (Subtyp von `IfcRelConnects`); ergänzend `IfcGroup` mit `IfcRelAggregates`."
quellen_sekundär:
  - "Blass, H. J.; Sandhaas, C.: Ingenieurholzbau – Grundlagen der Bemessung. KIT Scientific Publishing, Karlsruhe 2016, Kap. 8 'Verbindungen' — Verbindung als bemessungstechnische Einheit."
  - "Holzbau-Handbuch, Reihe 2 'Tragwerksplanung', Teil 1 'Verbindungen', mehrere Folgen, Informationsdienst Holz."
  - "Mönck, W.; Rug, W.: Holzbau – Bemessung und Konstruktion. 16. Aufl., Beuth, Berlin 2015, Kap. 7 'Verbindungen'."
  - "Natterer, J.; Herzog, T.; Volz, M.: Holzbau-Atlas. 4. Aufl., Birkhäuser, Basel 2003, Kap. 'Verbindungen und Anschlüsse'."
  - "Gerner, M.: Fachwerk – Instandsetzung, Sanierung, Neubau. DVA, 7. Aufl. 2007, Kap. zimmermannsmäßige Verbindungen."
quellenkonflikt: |
  Begriffsfeld:
  - **DIN EN 1995-1-1** Kap. 8 spricht von „Anschluss" und
    „Verbindung" weitgehend synonym für das Aggregat aus
    beteiligten Bauteilen und Verbindungsmitteln an einem
    Knotenpunkt.
  - **SIA 265** verwendet „Verbindung" für das Aggregat,
    „Anschluss" oft enger für die einseitige Lasteinleitung.
  - In der zimmermannssprachlichen Tradition werden „Stoss"
    (längstoßende Verbindung gleichartiger Stäbe), „Anschluss"
    (Aufeinanderstoß verschiedener Stäbe) und „Knoten" (Mehrfach-
    Treffpunkt) unterschiedliche Konnotationen tragen, ohne dass
    eine Norm dies kodifiziert.

  Eigene Festlegung:
  - **Verbindung** ist die **Hauptbenennung** für das Aggregat im
    Sinne von EC5 Kap. 8: alle Bauteile, Verbindungsmittel,
    Verbinder und Verstärkungselemente, die an einem konstruktiven
    Knotenpunkt kraftschlüssig zusammenwirken, plus das
    angewandte Bemessungsverfahren.
  - **Anschluss**, **Knoten**, **Stoss** sind als Synonyme
    geführt; eine feinere Differenzierung erfolgt über das
    `typ`-Feld (`VerbindungsTyp`: Stoss, Anschluss, Knoten,
    Eckverbindung).

  Wichtige Setzung (Memory `project_element_ontologie`):
  Verbindung ist **NICHT** Subtyp von `element`, sondern eigene
  **Aggregat-Klasse** — analog `tragwerk`, `dach`, `dachaufbau`,
  `bauteil_aggregat`. Die Verbindung ist ein Container über mehrere
  Element-Instanzen mit eigener UUID und eigenem Bemessungsverfahren,
  aber kein verbautes Einzelobjekt.

  IFC kodifiziert Verbindungen als Beziehungsobjekte
  (`IfcRelConnectsElements`), nicht als eigene Element-Klasse —
  das bestätigt die Aggregat-/Beziehungs-Natur des Begriffs.
  Alternativ kann eine Verbindung als `IfcGroup` mit
  `IfcRelAggregates` modelliert werden, wenn sie als eigenes
  benamtes Konstruktionsdetail geführt werden soll.

  BTLx hat keine eigene Entität für Verbindungen; sie sind
  implizit über mehrere Parts und Processings gegeben.

  Konstruktionsregel (SIA 265, Anhang A, mit Entsprechungen in
  EC5): **Mischungsverbot** — an einer Verbindung dürfen keine
  verschiedenartigen Verbindungsmittel kombiniert werden, weil
  ihre Kraft-Verformungs-Charakteristiken unterschiedlich sind und
  sich nicht ohne Weiteres addieren lassen. Diese Regel ist im
  Glossar als Konsistenzbedingung formuliert; sie wird in der
  Bemessungs-Schicht hart geprüft.

  Der Oberbegriff `bauteil_aggregat` existiert im Glossar noch
  nicht; bis zu dessen Einführung wird `oberbegriff: null`
  gesetzt (analog zu `tragwerk`, `dach`, `dachaufbau`).
---

## Prosa-Definition

Eine **Verbindung** ist ein Aggregat aus zwei oder mehr Bauteilen,
einem oder mehreren Verbindungsmitteln, optional einem oder
mehreren Verbindern und optional einem oder mehreren
Verstärkungselementen, die an einem konstruktiven Knotenpunkt
kraftschlüssig zusammenwirken, das eine eigene technische
Identität (UUID), eine Klassifikation nach Verbindungsart (Stoss,
Anschluss, Knoten, Eckverbindung) und ein zugewiesenes
Nachweisverfahren nach DIN EN 1995-1-1 bzw. SIA 265 trägt und das
selbst kein verbautes Einzelobjekt ist, sondern eine
Aggregations-Beziehung zwischen Element-Instanzen.

## Mathematische Definition

Sei

- 𝓤 der UUID-Raum nach `uuid`,
- 𝓑 die Menge der Bauteile nach `bauteil`,
- 𝓥𝓜 die Menge der Verbindungsmittel nach `verbindungsmittel`,
- 𝓥𝓑 die Menge der Verbinder nach `verbinder`,
- 𝓥𝓢 die Menge der Verstärkungselemente nach
  `verstaerkungselement`,
- 𝓥_τ die Menge der Verbindungsarten
  ```
  𝓥_τ := { Stoss, Anschluss, Knoten, Eckverbindung,
          ZimmermannsmaessigerStoss, ZimmermannsmaessigerAnschluss,
          KlebeVerbindung }
  ```
  (sealed enum; eigene Folge-Einträge bei Bedarf),
- 𝓝 die Menge der Nachweisverfahren-Referenzen (eigener Folge-
  Eintrag `nachweisverfahren`; mindestens enthaltend: Johansen
  nach EC5 Kap. 8.2, Axialnachweis nach EC5:2022, Klebung nach
  EC5 Kap. 10, zimmermannsmäßiger Versatz nach SIA 265 Anhang A).

Dann ist eine **Verbindung** das Tupel

```
V := (uuid, typ, beteiligte_bauteile, verbindungsmittel,
      verbinder, verstaerkungen, nachweisverfahren,
      position?, bezeichnung?)
```

mit den Komponenten

- **uuid** ∈ 𝓤: technische Identität der Verbindung als Aggregat,
- **typ** ∈ 𝓥_τ: Verbindungsart,
- **beteiligte_bauteile** ⊂ 𝓤 mit |beteiligte_bauteile| ≥ 2:
  UUIDs der durch die Verbindung verknüpften Bauteile,
- **verbindungsmittel** ⊂ 𝓤 mit |verbindungsmittel| ≥ 1: UUIDs der
  Verbindungsmittel, die in der Verbindung wirken (ausnahmsweise
  |verbindungsmittel| = 0 für rein zimmermannsmäßige Verbindungen,
  in denen kein metallisches Verbindungsmittel beteiligt ist —
  z. B. Versatz, Blattung; siehe Wohldefiniertheit),
- **verbinder** ⊂ 𝓤: UUIDs der Verbinder, die in der Verbindung
  wirken; optional, |verbinder| ≥ 0,
- **verstaerkungen** ⊂ 𝓤: UUIDs der Verstärkungselemente, die in
  oder an der Verbindung wirken; optional, |verstaerkungen| ≥ 0,
- **nachweisverfahren** ∈ 𝓝: Referenz auf das angewandte
  Bemessungsverfahren (Johansen, Axialnachweis, Klebung,
  zimmermannsmäßiger Versatz, …),
- **position** ∈ ℝ³ ∪ {⊥}: optionaler geometrischer Knotenpunkt
  in W (typisch Schwerpunkt der Verbindung) zur Visualisierung
  und Inzidenz-Prüfung,
- **bezeichnung** ∈ String ∪ {⊥}: freier Anzeigename.

Es ist 𝓥 disjunkt zu 𝓔 (𝓥 ∩ 𝓔 = ∅): Verbindungen sind keine
Elemente, sondern Aggregate **über** Elementen.

### Konsistenzbedingungen

(C1) **Bauteil-Multiplizität**: |beteiligte_bauteile| ≥ 2.

(C2) **Verbindungsmittel-Inzidenz**: für jedes vm ∈
verbindungsmittel gilt
verbindet(vm) ⊆ beteiligte_bauteile.
Jedes Verbindungsmittel der Verbindung wirkt zwischen Bauteilen,
die zur Verbindung gehören.

(C3) **Verbinder-Inzidenz**: für jedes vb ∈ verbinder gilt
verbundene_bauteile(vb) ⊆ beteiligte_bauteile.
Jeder Verbinder vermittelt zwischen Bauteilen, die zur Verbindung
gehören.

(C4) **Verstärkungs-Inzidenz**: für jedes vs ∈ verstaerkungen
gilt verstaerkt(vs) ∈ beteiligte_bauteile. Jedes
Verstärkungselement wirkt auf ein Bauteil, das zur Verbindung
gehört.

(C5) **Mischungsverbot** (SIA 265, Anhang A; entsprechende
Anwendungsregel in EC5 Kap. 8):
für jede Verbindung gilt: alle Verbindungsmittel in
verbindungsmittel sind vom **gleichen Typ** (alle Nägel **oder**
alle Schrauben **oder** alle Stabdübel etc.). Verschiedenartige
Verbindungsmittel mit unterschiedlicher Kraft-Verformungs-
Charakteristik dürfen ihre Tragfähigkeiten an einer Verbindung
**nicht** addiert werden, weil die Verformungen, die zur
Aktivierung jeder Tragfähigkeit notwendig sind, sich
unterscheiden. Ausnahmen sind in EC5 punktuell geregelt
(z. B. Schraube + Beilage); diese werden im Glossar nicht
ausgeschlossen, müssen aber explizit als Sonder-Nachweis-
verfahren markiert sein.

(C6) **Nachweisverfahren-Konsistenz**:
das Nachweisverfahren in `nachweisverfahren` ist mit dem Typ und
der Verbindungsmittel-Klasse der Verbindung kompatibel:
- typ ∈ {Stoss, Anschluss, Knoten, Eckverbindung} mit
  metallischen Verbindungsmitteln auf Abscheren →
  Johansen-Verfahren (EC5 Kap. 8.2).
- Verstärkungs-Verbindung mit axialer Beanspruchung →
  Axialnachweis (EC5:2022).
- typ = KlebeVerbindung → Klebung (EC5 Kap. 10).
- typ = ZimmermannsmaessigerStoss/Anschluss →
  zimmermannsmäßiger Versatz/Zapfen (SIA 265 Anhang A,
  Lehrbuch-Verfahren).

(C7) **Geometrische Verträglichkeit**:
falls `position` ∈ ℝ³ gesetzt ist, soll die Position
näherungsweise der Schwerpunkt der Bauteil-/Verbindungsmittel-
Geometrien der Verbindung sein (Toleranz Toleranzen.LAENGE_EPS
× typische Bauteilabmessung). Geometrisch-formal nicht
zwingend, aber für UI-Lokalisierung und BCF-Verortung wichtig.

## Wohldefiniertheit

- **Existenz**: Für jede konkrete in einem Tragwerk realisierte
  konstruktive Verbindung lässt sich das obige Tupel erfassen.
  Mindestkonfiguration: typ = Anschluss, |beteiligte_bauteile| =
  2 (z. B. Sparren und Pfette), |verbindungsmittel| = 1
  (z. B. eine Schraubengruppe als eine
  `Verbindungsmittel`-Instanz mit `multiplizitaet > 1`),
  nachweisverfahren = Johansen.
- **Eindeutigkeit der Identität**: Die Verbindung trägt eine
  eigene UUID, unabhängig von den UUIDs ihrer Bestandteile.
  Verschiedene Verbindungen können dieselben Bauteile
  involvieren (ein Bauteil ist typisch in mehreren Verbindungen
  Teilnehmer), aber jede Verbindung hat eine eindeutige UUID.
- **Aggregat, kein Element**: 𝓥 ∩ 𝓔 = ∅. Verbindungen werden
  nicht als verbaute Einzelobjekte behandelt; sie sind
  Container/Beziehungen über mehreren Elementen.
- **Foreign-Key-Regel**: alle Verweise (`beteiligte_bauteile`,
  `verbindungsmittel`, `verbinder`, `verstaerkungen`)
  referenzieren ausschließlich UUIDs (siehe `uuid`).
- **Rein zimmermannsmäßige Verbindungen**: ein Versatz oder
  Schwalbenschwanz ohne metallisches Verbindungsmittel ist
  modellierbar mit |verbindungsmittel| = 0; in diesem Fall ist
  `nachweisverfahren` der zimmermannsmäßige Versatznachweis nach
  SIA 265 Anhang A bzw. nach Lehrbuch (Mönck/Rug, Blass/Sandhaas).
  Die Konsistenzbedingung C2 ist dann trivial erfüllt
  (leere Quantifikation).
- **Mehrfach-Bauteil-Verbindung**: Knotenverbindungen mit
  |beteiligte_bauteile| ≥ 3 sind häufig (z. B. Stiel- und
  Strebenanschluss am Rähm); die Definition deckt sie über die
  Mengenkardinalität ab.
- **Selbst-Verbindung ausgeschlossen**: ein Bauteil verbindet
  sich nicht mit sich selbst. Falls in der Bauteil-UUID-Menge
  Duplikate auftreten würden, sind sie zu eliminieren.
- **Mischungsverbot — Wohldefiniertheit**: C5 ist als
  hartabbruch-relevante Konsistenzbedingung formuliert
  (Bemessung würde sonst sinnlos werden). Implementierungs-
  seitig wird C5 in der Aggregat-Konstruktion geprüft; bei
  Verletzung liefert die Fabrikfunktion `Resultat.Fehler(
  Entartet.Mischungsverbot)`.
- **Position-Wohldefiniertheit**: Die Berechnung des
  Verbindungs-Schwerpunkts (falls automatisch berechnet) ist
  invariant unter Permutation der beteiligten Elemente; die
  Wahl ist Modellierungs-Konvention, semantisch invariant.
- **Nicht-Zirkularität**: Die Definition stützt sich auf
  `bauteil`, `verbindungsmittel`, `verbinder`,
  `verstaerkungselement`, `uuid`, `toleranzen`. Sie verweist
  auf `nachweisverfahren` als noch zu definierenden Folge-
  Begriff (Frontmatter `voraussetzungen` listet
  `nachweisverfahren` nicht, weil dieser Begriff später kommt;
  im aktuellen Glossarstand ist `nachweisverfahren` als
  Platzhalter-Typ in der Implementierung geführt).

## Erläuterung (nicht normativ)

### Verbindung als Aggregat — abgrenzend zu den vier Element-Subklassen

Die App-Ontologie kennt **eine abstrakte Element-Basisklasse mit
vier konkreten Subklassen** als Geschwister
(`bauteil`, `verbindungsmittel`, `verbinder`,
`verstaerkungselement`). Plus die separate Aggregat-Klasse
**Verbindung**.

Während ein **Verbindungsmittel** das einzelne kraftübertragende
Stück ist (Schraube, Nagel, Bolzen) und ein **Verbinder** das
vermittelnde Bauteil dazwischen (Knotenblech, Balkenschuh), ist
die **Verbindung** das **Gefüge selbst**: das Aggregat aus
mehreren beteiligten Bauteilen, einem oder mehreren
Verbindungsmitteln, ggf. einem Verbinder, ggf. Verstärkungs-
elementen — plus das angewandte Nachweisverfahren.

Eine Verbindung ist damit kein verbautes Einzelobjekt, sondern
**eine Bemessungs- und Modellierungs-Einheit**: sie trägt das
Bemessungsverfahren, sie ist Bezugsobjekt für statische
Nachweise, sie ist Gegenstand von Werkplan-Details, sie kann in
BCF-Issues referenziert werden — aber sie ist nicht etwas, was
beim Aufrichten einzeln auf den Bock gelegt wird.

### IFC- und BTLx-Mapping

| Element/Aggregat       | IFC                                                   | BTLx                                  |
|------------------------|-------------------------------------------------------|---------------------------------------|
| Bauteil                | IfcBeam / IfcColumn / IfcMember / IfcPlate            | Part mit @GUID                        |
| Verbindungsmittel      | IfcMechanicalFastener                                 | Processing oder eigenes Part          |
| Verbinder              | IfcDiscreteAccessory                                  | eigenes Part oder Reference           |
| Verstärkungselement    | IfcMechanicalFastener + Pset für Funktion             | wie VM + Funktionsattribut            |
| **Verbindung**         | **IfcRelConnectsElements** (Beziehung) bzw. `IfcGroup` mit `IfcRelAggregates` | **implizit über mehrere Parts/Processings** |

Die IFC-Repräsentation einer Verbindung ist **kein Element**,
sondern eine **Beziehung** (`IfcRelConnectsElements` — Subtyp von
`IfcRelConnects`) oder eine **Gruppe** (`IfcGroup`). Diese
IFC-Setzung bestätigt die App-Ontologie: Verbindungen sind nicht
verbaut, sondern relationieren Verbautes.

BTLx kennt keine eigene Verbindungs-Entität; eine Verbindung
manifestiert sich dort durch das gemeinsame Auftreten mehrerer
Parts (Bauteile) und Processings (Bohrungen, Lag-Screws,
Versätze) am selben Knotenpunkt — implizit, ohne explizites
Verbindungs-Objekt.

### Mischungsverbot

SIA 265, Anhang A, formuliert (mit Entsprechungen in EC5):

> An einer Verbindung dürfen keine verschiedenartigen
> Verbindungsmittel zur gemeinsamen Lastaufnahme kombiniert
> werden.

Begründung: Nägel, Schrauben, Bolzen und Stabdübel haben
unterschiedliche **Kraft-Verformungs-Charakteristiken**
(unterschiedliche Anfangssteifigkeiten, unterschiedliche
Schlupfwege bis zur Aktivierung). Würde man ihre Tragfähigkeiten
einfach addieren, würde man Tragfähigkeiten zählen, die in der
Realität bei verschiedenen Verformungs-Niveaus aktiv werden —
das versagt unterschätzt erst und versagt im Bauteil dann
typischerweise schubweise.

Die App prüft C5 in der Aggregat-Konstruktion; eine Verbindung
mit gemischten Verbindungsmitteln wird abgelehnt, sofern nicht
explizit ein Sonder-Nachweisverfahren markiert ist (z. B. die
EC5-Regel zur Schraube + Beilagscheibe).

### Verbindung vs. Konstruktionsdetail

Eine **Verbindung** ist die Bemessungs- und Modellierungs-
Einheit (Tupel mit UUIDs auf Bauteile/Verbindungsmittel/…). Ein
**Konstruktionsdetail** ist eine **plan- und werkstattorientierte
Repräsentation** desselben Knotenpunkts: Maßangaben, Schnittriss,
Abstände, Werkzeichnung, Detailnummer im Werkplan. Beide stehen
auf demselben Knotenpunkt, sind aber unterschiedliche
Repräsentationen.

Eine Verbindung kann von einem oder mehreren Konstruktions-
details begleitet sein; ein Konstruktionsdetail kann eine oder
mehrere Verbindungen umfassen (`hg_konstruktionsdetail.md`).

### Verbindung als Bestandteil eines Tragwerks

Im Tragwerks-Tupel (B, V, A, L) nach `hg_tragwerk.md` ist V die
Menge der Verbindungen. Eine Verbindung ist Bestandteil eines
Tragwerks im partitiv-aggregativen Sinn: das Tragwerk umfasst
seine Verbindungen, eine Verbindung gehört zu einem (oder
mehreren) Tragwerken.

## Beziehungen

- **Oberbegriff**: derzeit `null`. Künftig `bauteil_aggregat`
  bzw. allgemeiner `aggregat` (oberste Aggregatklasse für
  Container über Elementen, analog `tragwerk`, `dach`,
  `dachaufbau`).
- **Bestandteile (partitiv)**:
  - **Bauteile** (`bauteil`): die durch die Verbindung
    verknüpften Stäbe/Flächen, ≥ 2.
  - **Verbindungsmittel** (`verbindungsmittel`): die
    kraftübertragenden Stücke; ≥ 1 (Sonderfall 0 für
    rein zimmermannsmäßige Verbindungen).
  - **Verbinder** (`verbinder`, optional): das vermittelnde
    Stück (Knotenblech, Balkenschuh, Sherpa).
  - **Verstärkungselemente** (`verstaerkungselement`,
    optional): Vollgewindeschrauben in Verstärkungsfunktion.
  - **Nachweisverfahren** (`nachweisverfahren`, eigener
    Eintrag folgt): das angewandte Bemessungsverfahren.
- **Spezialisierungen nach Verbindungsart** (eigene Einträge
  folgen, im Body erläutert):
  - **Stoss** (`stoss`): längstoßende Verbindung gleichartiger
    Stäbe (Pfettenstoss, Sparrenstoss).
  - **Anschluss** (`anschluss`): Aufeinanderstoß verschiedener
    Stäbe (Sparren-Pfetten-Anschluss).
  - **Knoten** (`knoten`): Mehrfach-Treffpunkt (Strebe-
    Stiel-Rähm).
  - **Eckverbindung** (`eckverbindung`): rechtwinklige
    Verbindung zweier Stäbe (Pfette-Pfettenkopf,
    Schwellenecke).
  - **Zimmermannsmäßiger Stoss/Anschluss** (`versatz`, `zapfen`,
    `blatt`, `schwalbenschwanz` — Folgearbeit).
  - **Klebe-Verbindung** (`klebe_verbindung`): Sonderform
    nach EC5 Kap. 10.
- **Verwendung**:
  - Bestandteil eines **Tragwerks** (`tragwerk`): in der
    Tupel-Repräsentation (B, V, A, L) ist V die Menge der
    Verbindungen.
- **Abgrenzung**:
  - **Verbindungsmittel** (`verbindungsmittel`): einzelnes
    kraftübertragendes Element. Verbindung ist das Aggregat
    darüber; ein Verbindungsmittel ist Bestandteil **einer**
    Verbindung (typisch).
  - **Verbinder** (`verbinder`): vermittelndes Bauteil zwischen
    Stäben. Verbindung ist das Aggregat, das einen Verbinder
    enthalten **kann** (indirekte Verbindung nach EC5 8.2.3).
  - **Verstärkungselement** (`verstaerkungselement`):
    Schraube in Verstärkungsfunktion. Verbindung ist das
    Aggregat, das Verstärkungselemente enthalten kann
    (typisch bei verstärkten Anschlüssen).
  - **Bauteil** (`bauteil`): tragend/raumbildend.
    Verbindung ist kein Bauteil, sondern Aggregat über
    Bauteilen.
  - **Element** (`element`): Verbindung ist **nicht** Subtyp
    von Element. Verbindung ist Aggregat-Klasse, Element ist
    Wurzel der Einzelobjekt-Hierarchie. Disjunkte Hierarchien.
  - **Tragwerk** (`tragwerk`): übergeordnetes Aggregat aus
    Bauteilen + Verbindungen + Auflagern + Lastfällen. Eine
    Verbindung ist Bestandteil eines Tragwerks; sie ist nicht
    selbst Tragwerk.
  - **Konstruktionsdetail** (`konstruktionsdetail`, bereits
    angelegt): plan- und werkstattorientierte Repräsentation
    eines Knotenpunkts; eine Verbindung kann von einem oder
    mehreren Konstruktionsdetails begleitet sein. Verschiedene
    Repräsentations-Ebenen desselben Knotenpunkts.

## Implementierungshinweis

Datentyp (Domänen-Schicht, Kotlin, Schicht
`domain.aggregat.verbindung`):

```kotlin
package domain.aggregat.verbindung

import domain.geometrie.Punkt
import domain.bemessung.Nachweisverfahren    // Folgearbeit
import java.util.UUID

/** Verbindungsart. */
sealed interface VerbindungsTyp {
    data object Stoss                       : VerbindungsTyp
    data object Anschluss                   : VerbindungsTyp
    data object Knoten                      : VerbindungsTyp
    data object Eckverbindung               : VerbindungsTyp
    data object ZimmermannsmaessigerStoss   : VerbindungsTyp
    data object ZimmermannsmaessigerAnschluss : VerbindungsTyp
    data object KlebeVerbindung             : VerbindungsTyp
}

/**
 * Verbindung: Aggregat aus beteiligten Bauteilen,
 * Verbindungsmitteln, optional Verbindern und
 * Verstärkungselementen, plus Nachweisverfahren.
 *
 * Glossar: hg_verbindung.md
 *
 * NICHT Subtyp von Element. Eigene Aggregat-Klasse, analog
 * Tragwerk/Dach/Dachaufbau.
 *
 * IFC: IfcRelConnectsElements (Beziehung) bzw. IfcGroup mit
 *       IfcRelAggregates.
 * BTLx: implizit über mehrere Parts/Processings; keine eigene
 *       BTLx-Entität.
 */
data class Verbindung(
    val uuid: UUID,                                      // eigene Identität als Aggregat
    val typ: VerbindungsTyp,
    val beteiligteBauteile: Set<UUID>,                   // FK auf Bauteile, |...| >= 2
    val verbindungsmittel: Set<UUID> = emptySet(),       // FK auf Verbindungsmittel
    val verbinder: Set<UUID> = emptySet(),               // FK auf Verbinder, optional
    val verstaerkungen: Set<UUID> = emptySet(),          // FK auf Verstärkungselemente, optional
    val nachweisverfahren: Nachweisverfahren,            // Folgearbeit
    val position: Punkt? = null,                        // Schwerpunkt der Verbindung
    val bezeichnung: String? = null
) {
    init {
        // C1. beteiligteBauteile.size >= 2
        // C2. verbindungsmittel-Inzidenz   (in Validierung gegen Modell)
        // C3. verbinder-Inzidenz           (in Validierung gegen Modell)
        // C4. verstaerkungen-Inzidenz      (in Validierung gegen Modell)
        // C5. Mischungsverbot              (alle Verbindungsmittel gleichen Typs)
        // C6. Nachweisverfahren-Konsistenz (typ ↔ Verbindungsmittelart ↔ Nachweis)
        // C7. Position-Verträglichkeit     (weich; nur Warnung)
    }
}
```

- **Einheit**: Längen in mm (Double); `position` als `Punkt` in W.
- **Identität**: `uuid` ist Pflicht, eigenständig (eigene UUID
  des Aggregats, nicht eine UUID eines Bestandteils).
- **Foreign-Key-Regel**: alle vier Element-Mengen
  (`beteiligteBauteile`, `verbindungsmittel`, `verbinder`,
  `verstaerkungen`) referenzieren ausschließlich UUIDs.
- **Inzidenz-Validierung** (C2–C4): erfolgt nicht im
  `init`-Block, weil dort der Modell-Kontext fehlt. Die
  Validierung wird in der Aggregat-Konstruktion durch eine
  Modell-bezogene Fabrikfunktion `Verbindung.bilde(modell:
  Modell, …)` durchgeführt; bei Verletzung liefert sie
  `Resultat.Fehler(Entartet.InzidenzVerletzt)`.
- **Mischungsverbot-Validierung** (C5): erfolgt ebenfalls in der
  Fabrikfunktion mit Modell-Zugriff (Lookup der Verbindungs-
  mittel-Typen). Bei Verletzung: `Resultat.Fehler(Entartet.
  Mischungsverbot)`. Sonderausnahmen (Schraube + Beilage etc.)
  werden über ein optionales Flag `sonderNachweisverfahrenZulassen`
  geführt.
- **IFC-Mapping**:
  - **Variante A** (bevorzugt): `IfcRelConnectsElements`
    (Subtyp von `IfcRelConnects`) — eine Beziehungs-Entität, die
    zwei oder mehr Elemente verbindet. Eigenschaften:
    `RelatingElement`, `RelatedElement` (in IFC nur paarweise;
    Mehrfach-Verbindungen werden durch mehrere
    `IfcRelConnectsElements`-Instanzen oder durch `IfcGroup`
    abgebildet).
  - **Variante B**: `IfcGroup` (Subtyp von `IfcObjectDefinition`)
    mit `IfcRelAggregates` als Aggregations-Beziehung. Geeignet,
    wenn die Verbindung als benamtes Konstruktionsdetail mit
    eigener Identität geführt werden soll.
  - Die App entscheidet pro Verbindung; Default ist `IfcGroup`,
    weil die App-Verbindung eine eigene UUID, einen Typ und
    Eigenschaften (Nachweisverfahren) trägt — das ist mit
    `IfcGroup` natürlicher abbildbar als mit
    `IfcRelConnectsElements`.
- **BTLx-Mapping**: keine eigene Entität. Die Verbindung wird
  beim BTLx-Export aufgelöst in:
  - die beteiligten Bauteil-Parts (mit ihren UUIDs als
    `Part/@GUID`),
  - die Verbindungsmittel als Processings (`Drilling`,
    `Lag-Screw`) oder eigenständige Parts,
  - die Verbinder als eigene Parts,
  - die Verstärkungselemente als eigene Parts mit Funktions-
    attribut.
  - Die Verbindungs-UUID erscheint nicht im BTLx; sie wird
    optional als `UserAttribute` an den beteiligten Parts
    gespeichert (`ConnectionGuid`).
- **Edge Cases**:
  - **Verbindung ohne Verbindungsmittel** (rein
    zimmermannsmäßig): zulässig, sofern `typ` ∈
    {ZimmermannsmaessigerStoss, ZimmermannsmaessigerAnschluss}
    und `nachweisverfahren` der zimmermannsmäßige
    Versatznachweis ist.
  - **Verbindung mit nur einem Bauteil**: nicht erlaubt;
    `Entartet.VerbindungOhneZweitesBauteil`.
  - **Selbst-Verbindung** (Bauteil mit sich selbst): nicht
    erlaubt; bei doppelten UUIDs in `beteiligteBauteile` greift
    die Set-Semantik bereits konstruktiv.
  - **Verbindung mit Mischung von Verbindungsmittel-Typen**:
    nicht erlaubt (C5); `Entartet.Mischungsverbot`. Ausnahme
    nur bei explizitem Sonder-Nachweisverfahren.
  - **Verbindung über mehrere Tragwerke hinweg**: typisch
    nicht; aber zulässig, wenn das Modell so konstruiert ist
    (z. B. Trag-Verbindung zwischen Hauptbau und Vordach).
- **Abgeleitete Eigenschaften**:
  - `geometrieInWelt(modell: Modell): GeometrieInW` —
    Vereinigung der geometrischen Punktmengen aller
    beteiligten Element-Instanzen.
  - `boundingBox(modell: Modell): AABB` — achsenparalleler
    Hüllquader in W.
  - `schwerpunkt(modell: Modell): Punkt` — geometrischer
    Schwerpunkt der beteiligten Elemente; falls `position`
    leer ist, wird sie hieraus gefüllt.
  - `nachweisFuehren(modell: Modell): Nachweisergebnis` —
    Bemessungs-Schicht-Aufruf (Folgearbeit).
- **Bezeichner-Konvention** (CLAUDE.md): Domänen-Klasse heißt
  `Verbindung` (deutsch, Glossarbegriff). Synonyme `Anschluss`,
  `Knoten`, `Stoss` werden durch das `typ`-Feld differenziert,
  nicht durch eigene Klassen.

## Quellen

**Primär (normativ):**

- DIN EN 1995-1-1:2010-12, „Eurocode 5: Bemessung und
  Konstruktion von Holzbauten – Teil 1-1", Kapitel 8 und
  Kapitel 10.
- SIA 265:2021, „Holzbau", Anhang A.
- ÖNORM B 1995-1-1:2019.
- DIN 1052:2008-12, Abschnitt 12.
- ISO 16739-1:2024, IFC-Entitäten `IfcRelConnectsElements`,
  `IfcGroup`, `IfcRelAggregates`.

**Sekundär:**

- Blass, H. J.; Sandhaas, C.: *Ingenieurholzbau – Grundlagen
  der Bemessung.* KIT Scientific Publishing, Karlsruhe 2016,
  Kap. 8.
- Holzbau-Handbuch, Reihe 2, Teil 1, Informationsdienst Holz.
- Mönck, W.; Rug, W.: *Holzbau – Bemessung und Konstruktion.*
  16. Auflage, Beuth, Berlin 2015, Kap. 7.
- Natterer, J.; Herzog, T.; Volz, M.: *Holzbau-Atlas.*
  4. Auflage, Birkhäuser, Basel 2003.
- Gerner, M.: *Fachwerk – Instandsetzung, Sanierung, Neubau.*
  DVA, 7. Auflage 2007.

**Korpus (nicht autoritativ):**

- Holzbau Deutschland, Merkblatt „Begriffe und Klassifizierungen
  für den Holzbau" (abgerufen 2026-05-08).
- Wikipedia, Lemmata „Holzverbindung", „Anschluss (Holzbau)"
  (abgerufen 2026-05-08).
