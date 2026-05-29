---
id: verbindungsmittel
benennung: Verbindungsmittel
synonyme: [mechanisches Verbindungsmittel]
abgelehnte_benennungen: [Befestigungsmittel, Verbindung, Verbindungselement, "fastener", "connector", "Beschlag"]
oberbegriff: element
begriffstyp: generisch
voraussetzungen: [element, uuid, gerade, strecke, bauteil, werkstoff, werkstoff_stahl, axiales_holz, toleranzen]
abgrenzung_zu: [bauteil, verbinder, verstaerkungselement, verbindung, element]
status: entwurf
subglossar_pendant: notwendig
quellen_primär:
  - "DIN EN 1995-1-1:2010-12 (Eurocode 5), Kapitel 8 'Anschlüsse mit metallischen Verbindungsmitteln' (insb. 8.1 Allgemeines, 8.2 stiftförmige Verbindungsmittel auf Abscheren — Johansen-Theorie, 8.3 Nägel, 8.5 Bolzen, 8.6 Stabdübel, 8.7 Schrauben, 8.10 Nagelplatten); Gl. 8.17 für n_ef bei Schraubenreihen."
  - "DIN EN 14592:2022-09 'Holzbauwerke – Stiftförmige Verbindungsmittel – Anforderungen'."
  - "DIN EN 14545:2009-02 'Holzbauwerke – Verbinder – Anforderungen' (für nicht-stiftförmige Dübel besonderer Bauart)."
  - "SIA 265:2021 'Holzbau', Anhang A 'Verbindungen und Verbindungsmittel'."
  - "ÖNORM B 1995-1-1:2019, nationale Anwendungsbestimmungen zum Eurocode 5, Kap. 8."
  - "ISO 16739-1:2024 'Industry Foundation Classes (IFC) – Part 1: Data schema', Entität `IfcMechanicalFastener` (Subtyp von `IfcElementComponent`); Property Sets `Pset_FastenerCommon`, `Pset_MechanicalFastener`."
  - "design2machine: BTLx 2.x Specification (Stand 2024), Processing-Typen `Drilling`, `Lag-Screw` u. a. sowie Part-Element für selbständig geführte Verbindungsmittel."
  - "ETA-11/0190, 'Würth ASSY plus VG, ASSY 3.0, ASSY 4.0' (Vollgewindeschrauben mit europäischer technischer Bewertung)."
  - "Z-9.1-519, 'Schrauben mit Vollgewinde als Verbindungsmittel und als Verstärkung von Holzbauteilen' (SPAX, allgemeine bauaufsichtliche Zulassung, DIBt)."
  - "ETA-12/0373, 'Reisser-Schrauben — Schrauben für die Verwendung in Holzbauteilen'."
quellen_sekundär:
  - "Blass, H. J.; Sandhaas, C.: Ingenieurholzbau – Grundlagen der Bemessung. KIT Scientific Publishing, Karlsruhe 2016, Kap. 8 'Verbindungen'."
  - "Holzbau-Handbuch, Reihe 2 'Tragwerksplanung', Teil 1 'Verbindungen', Folge 1 'Verbindungen mit stiftförmigen Verbindungsmitteln', Informationsdienst Holz, aktuelle Auflage."
  - "Mönck, W.; Rug, W.: Holzbau – Bemessung und Konstruktion. 16. Aufl., Beuth, Berlin 2015, Kap. 7 'Verbindungen'."
  - "cadwork informatik: Dokumentation 'Verbindungsmittelachse (VBA)' — 1D-Geometrie mit Anfangs- und Endpunkt; Verbindungsmitteltyp als Attribut."
  - "Hersteller-BIM-Bibliotheken Rothoblaas, Würth, SFS, Simpson Strong-Tie (jeweils als IfcMechanicalFastener ausgeliefert)."
quellenkonflikt: |
  Die Begriffsabgrenzung „Verbindungsmittel" vs. „Verbinder" vs.
  „Verbindung" ist normativ einheitlich (EC5 Kap. 8, SIA 265
  Anhang A): das Verbindungsmittel ist das einzelne kraftübertragende
  Stück (Schraube, Nagel, Bolzen), die Verbindung ist das Aggregat
  am Knotenpunkt, der Verbinder (im EC5: „Verbindungselement") ist
  das vermittelnde Bauteil dazwischen (Knotenblech, Balkenschuh).

  Der Sonderfall **Vollgewindeschraube als Tragglied** ist die einzige
  echte Begriffs-Spannung: dieselbe physische Schraube ist
  Verbindungsmittel (Abscher-Anschluss, Bemessung nach Johansen,
  EC5 Kap. 8) **oder** Verstärkungselement (Querzug-/Querdruck-/
  Schubverstärkung, axiale Bemessung nach EC5:2022 / ETA). Diese App
  löst den Konflikt durch eine eigene Element-Subklasse
  `verstaerkungselement`; siehe dort und Memory
  `project_element_ontologie`. **Funktion bestimmt die Klasse, nicht
  das Material.**

  IFC-Mapping ist ebenfalls konsistent: alle stiftförmigen und
  nicht-stiftförmigen Verbindungsmittel sind `IfcMechanicalFastener`
  (Subtyp von `IfcElementComponent`); niemals `IfcBeam`. Hersteller-
  BIM-Bibliotheken (Rothoblaas, Würth, SFS, Simpson) bestätigen
  diese Konvention.

  BTLx ist hybrid: meist erscheint das Verbindungsmittel als
  **Processing am Bauteil** (`Drilling`, `Lag-Screw`), bei sichtbaren
  Tragelementen mit eigener Stückliste (lange Vollgewindeschrauben,
  Gewindestangen, ETA-Verstärkungsschrauben) als **eigenes Part mit
  GUID**. Die Spec lässt beides zu; die App entscheidet
  fallbezogen.

  Klebungen sind in EC5 Kap. 8 nicht als „Verbindungsmittel im engeren
  Sinn" geführt; sie werden in EC5 Kap. 10 / SIA 265 Anhang A separat
  behandelt. Im vorliegenden Glossar werden Klebungen als
  Verbindungsmittel-Subtyp (`klebung`, Folgearbeit) geführt, weil sie
  im App-Datenmodell dieselben Element-Eigenschaften (UUID,
  Geometrie, verbindet) tragen wie mechanische Verbindungsmittel.
---

## Prosa-Definition

Ein **Verbindungsmittel** ist ein Element der App-Ontologie, das als
einzelnes mechanisches oder geklebtes Tragstück Kräfte zwischen zwei
oder mehr Bauteilen überträgt, das dazu eine eindimensional dominante
Geometrie (Achse mit Anfangs- und Endpunkt sowie typabhängigem
Querschnitt) und eine Typspezifikation (Nagel, Schraube, Bolzen,
Stabdübel, Klammer, Klebung oder Dübel besonderer Bauart) besitzt
und dessen Bemessung nach DIN EN 1995-1-1 Kapitel 8 erfolgt.

## Mathematische Definition

Sei

- 𝓔 die Menge der Elemente nach `element`,
- 𝓤 der UUID-Raum nach `uuid`,
- 𝓑 die Menge der Bauteile nach `bauteil`,
- 𝓦_VM := werkstoff_stahl ∪ axiales_holz ∪ {⊥_klebstoff} die
  Werkstoffmenge der Verbindungsmittel, formal referenziert auf die
  Werkstoff-Hierarchie (Stahl für stiftförmige und nicht-stiftförmige
  metallische Verbindungsmittel; axiales Holz für Holzdübel aus
  Hartholz; ⊥_klebstoff als Platzhalter für die noch zu definierende
  Klebstoff-Klasse nach EC5 Kap. 10, Folgearbeit). Aluminium-
  Verbindungsmittel werden konventionell der Stahl-Klasse zugeordnet,
  bis eine eigene Werkstoffklasse `werkstoff_aluminium` eingeführt
  wird (Folgearbeit),
- 𝓥𝓜_τ die Menge der Verbindungsmittel-Typen
  ```
  𝓥𝓜_τ := { Nagel, Schraube, Bolzen, Stabduebel,
            Klammer, Holzduebel, NagelPlatte,
            DuebelBesondererBauart, Klebung }
  ```
  (sealed enum; eigene Folge-Einträge),
- 𝓛 := ℝ⁺ die Menge der zulässigen Längen in mm,
- 𝓔𝓣𝓐 die Menge der ETA-Referenzen (eigener Folge-Eintrag
  `eta_referenz`),
- 𝓢𝓰 die Menge der Stahlgüten (eigener Folge-Eintrag `stahlguete`).

Dann ist ein **Verbindungsmittel** das Tupel

```
VM := (uuid, geometrie, lokale_platzierung, werkstoff,
       typ, nenndurchmesser, nennlaenge, achse,
       verbindet, multiplizitaet,
       eta_zulassung?, stahlguete?,
       positionsnummer?, produktkennzeichnung?, bezeichnung?)
```

mit den von `element` ererbten Pflichtfeldern

- **uuid** ∈ 𝓤,
- **geometrie** ∈ 𝓖_VM ⊂ 𝓖 (1D-dominante Verbindungsmittelgeometrie:
  Stab mit kreisförmigem Querschnitt für stiftförmige; Plattengeometrie
  für Nagelplatten und Dübel besonderer Bauart; Klebfuge als
  Flächengeometrie für Klebungen),
- **lokale_platzierung** ∈ SE(3),
- **werkstoff** ∈ 𝓦,

und den verbindungsmittel-spezifischen Pflichtfeldern

- **typ** ∈ 𝓥𝓜_τ (Verbindungsmittel-Typ),
- **nenndurchmesser** d ∈ 𝓛 (Nenndurchmesser in mm; bei Klebungen
  und Nagelplatten typabhängig zu interpretieren oder ⊥),
- **nennlaenge** ℓ ∈ 𝓛 (Nennlänge in mm),
- **achse** ∈ Strecke ⊂ Gerade × ℝ²: die **Verbindungsmittelachse**
  als Strecke s = (P₀, P₁) mit P₀, P₁ ∈ ℝ³ in W (cadwork-Konzept VBA);
  ‖P₁ − P₀‖ ≈ ℓ bzw. ≤ ℓ + Toleranzen.LAENGE_EPS (das geometrische
  Versenken der Schraubenspitze ist eine Bemessungsfrage, nicht eine
  Geometriefrage),
- **verbindet** ⊂ 𝓤 mit |verbindet| ≥ 2: die UUIDs derjenigen Bauteile,
  die durch das Verbindungsmittel verbunden werden,
- **multiplizitaet** n ∈ ℕ, n ≥ 1 (Default 1; Anzahl gleichartiger
  Verbindungsmittel, die durch dieses Element repräsentiert werden;
  IFC `IfcMechanicalFastener` ist „one or many" zulässig),

und den Optionalfeldern

- **eta_zulassung** ∈ 𝓔𝓣𝓐 ∪ {⊥},
- **stahlguete** ∈ 𝓢𝓰 ∪ {⊥},
- **positionsnummer**, **produktkennzeichnung**, **bezeichnung**
  wie in `element`.

Die **Achse** s = (P₀, P₁) trägt Position und Richtung; der **Typ**
zusammen mit Nenndurchmesser, Nennlänge und ETA-Zulassung trägt die
Bemessungs- und Stücklisten-Spezifikation. Diese Trennung folgt dem
cadwork-Konzept der **Verbindungsmittelachse (VBA)**: aus der Achse
werden Werkplan-Symbol, Bohrlochbearbeitung am Bauteil, Stücklisten-
Eintrag und statische Position für externe Bemessung erzeugt; aus
dem Typ folgen alle Bemessungseingaben.

Es ist 𝓥𝓜 ⊂ 𝓔, d. h. die Menge der Verbindungsmittel ist eine
disjunkte Teilmenge der Element-Menge (siehe `element`).

## Wohldefiniertheit

- **Existenz**: Für jedes konkrete in einem Tragwerk eingebaute
  Verbindungsmittel lässt sich das obige Tupel erfassen.
  Mindestkonfiguration: typ = Nagel, d = 4.0 mm, ℓ = 100 mm, achse
  als Strecke der Länge ≈ 100 mm, |verbindet| = 2, multiplizitaet = 1.
- **Eindeutigkeit der Identität**: über `uuid` (geerbt von `element`).
- **Geometrie-Konsistenz**: Die Achse s = (P₀, P₁) ist im Welt-
  Koordinatensystem zu interpretieren; das lokale Element-
  Koordinatensystem hat per Konvention seinen Ursprung in P₀, mit
  z-Achse entlang (P₁ − P₀)/‖P₁ − P₀‖. Die `lokale_platzierung`
  überführt dieses lokale System nach W; G_W(VM) ist der durch typ,
  nenndurchmesser und nennlaenge erzeugte Stab- bzw. Flächenkörper
  unter dieser Transformation.
- **Achse-Länge-Konsistenz**: Es gilt ‖P₁ − P₀‖ ≤ ℓ +
  Toleranzen.LAENGE_EPS. Die Achse ist die geometrische Lage des
  eingebauten Stücks; ℓ ist die ungekürzte Nennlänge des
  Lieferprodukts. Bei Schrauben mit nicht eingedrehtem Kopfüberstand
  oder bei Bolzen mit Mutter und Beilagscheiben ist diese
  Toleranz typisch klein (≪ ℓ).
- **Verbindet-Konsistenz**: Jedes uuid ∈ verbindet referenziert ein
  existierendes Bauteil im Modell. |verbindet| ≥ 2 ist zwingend; ein
  Verbindungsmittel, das nur ein Bauteil „durchsticht", wird nicht
  modelliert (das wäre eine reine Bohrung als Bauteil-Bearbeitung).
  **Foreign-Key-Regel** (siehe `uuid`): die Liste enthält
  ausschließlich UUIDs, niemals Positionsnummern.
- **Multiplizität**: n ≥ 1. Eine Instanz mit n = k repräsentiert k
  gleichartige Verbindungsmittel an derselben funktionalen Position
  (Nagelfeld, Schraubenreihe, Stabdübel-Cluster). Bemessungs-
  konsequenz: die effektive Anzahl n_ef nach EC5 Gl. 8.17 bezieht
  sich auf diese Multiplizität.
- **Disjunktheit zu Bauteil/Verbinder/Verstärkung**: Ein
  Verbindungsmittel-Tupel ist genau dann ein Verstärkungselement im
  Sinne von `verstaerkungselement`, wenn es funktional in eine
  Verstärkungsrolle gestellt wird; dann wird es in einem **eigenen**
  Tupel der Klasse `Verstaerkungselement` instanziiert (mit eigener
  UUID), das auf das Verbindungsmittel-Spezifikations-Tripel
  (typ, d, ℓ) zurückgreift. Es entsteht keine Mehrfach-Klassifikation
  desselben Tupels; die Klassifikation ist Konstruktions-
  entscheidung.
- **Wohldefiniertheit der Bemessungsdaten**: typ und nenndurchmesser
  bestimmen zusammen mit dem ETA-Eintrag (falls vorhanden) den
  charakteristischen Wert für die Tragfähigkeit nach EC5; die App
  liefert die geometrische Eingabe, nicht den Bemessungswert.
- **Nicht-Zirkularität**: Die Definition stützt sich auf `element`,
  `uuid`, `gerade`, `strecke`, `bauteil`, `werkstoff` und
  `toleranzen`. Sie verweist auf `verbindung`, `verbinder`,
  `verstaerkungselement` ausschließlich in der Abgrenzung, nicht in
  der Definition.

## Erläuterung (nicht normativ)

### Werkstoff

Verbindungsmittel haben **typisch Werkstoff `werkstoff_stahl`**
(Stahlgüten 4.6 / 5.6 / 8.8 / 10.9 für Bolzen und Schrauben,
A2-70 / A4-70 für Edelstahl-Anwendungen, S235 / S355 für Klammern
und Nagelplatten). **Holzdübel** sind die Ausnahme: sie haben
Werkstoff `axiales_holz` aus Hartholz (typisch Eiche, Esche,
Robinie). **Klebungen** als Verbindungsmittel-Subtyp tragen einen
eigenen Werkstoff-Begriff (Klebstoff-Klasse nach EC5 Kap. 10),
der außerhalb der hier eingeführten Werkstoff-Hierarchie liegt
(Folgearbeit).

### Klassifikation nach EC5 Kap. 8

Die Verbindungsmittel-Familie zerfällt nach DIN EN 1995-1-1 in drei
Hauptklassen:

1. **Stiftförmige Verbindungsmittel** auf Abscheren (Kap. 8.2 ff.):
   Nägel (8.3), Klammern (8.4), Bolzen (8.5), Stabdübel (8.6),
   Schrauben (8.7), Holzschrauben mit Vollgewinde (auch Kap. 8.7).
   Die Bemessung folgt der **Johansen-Theorie**: aus den drei
   möglichen Versagensmoden (Lochleibung in Holz, Fließen des
   Verbindungsmittels mit ein bzw. zwei Fließgelenken) wird der
   maßgebende Mindestwert gewählt; der Seileffekt erhöht die
   Tragfähigkeit zusätzlich.
2. **Nicht-stiftförmige Verbindungsmittel**: Nagelplatten (Kap. 8.10),
   Dübel besonderer Bauart nach DIN EN 14545 (Ringdübel,
   Scheibendübel, Zahnscheiben), die die Lasten flächig in das Holz
   einleiten.
3. **Klebungen** (EC5 Kap. 10): Klebfuge zwischen zwei Bauteilen,
   nach Klebstoff- und Vorbereitungs-Klassen bemessen.

### Verbindungsmittelachse (cadwork-Konzept VBA)

Die App folgt dem in cadwork etablierten Konzept der
**Verbindungsmittelachse**: ein Verbindungsmittel ist intern
**eindimensional** als Strecke (P₀, P₁) repräsentiert. Aus dieser
Achse plus Typ-Spezifikation werden generiert:

- **3D-Visualisierung**: Stabkörper (Schaft + ggf. Kopf) durch
  Sweep des Querschnitts entlang der Achse.
- **Werkplan-Symbol**: 2D-Darstellung im Riss (Querschnitt durchs
  Achssegment).
- **Bohrlochbearbeitung**: Boolean-Subtraktion eines Zylinders mit
  Durchmesser d und Länge ‖P₁ − P₀‖ aus jedem Bauteil in
  `verbindet` (BTLx-Processing `Drilling` oder `Lag-Screw`).
- **Stücklisten-Eintrag**: Typ + d + ℓ + multiplizitaet ⇒
  Eintrag in der Verbindungsmittelliste.
- **Statische Position**: Achse als Eingabe für externe
  Bemessungstools (z. B. mb-Statik, RFEM).

### Stücklisten-Trennung

Verbindungsmittel haben **eigene Stücklisten**, getrennt von der
Bauteilstückliste. Das entspricht der Realität der Beschaffungs-
logistik (Schrauben in Eimern, Nägel im Sack, Stabdübel als
Meterware) und folgt dem cadwork-Konzept „Verbindungsmittelliste"
≠ „Bauteilstückliste". Die Trennung ist im Datenmodell durch die
unterschiedlichen Element-Subklassen `Bauteil` und
`Verbindungsmittel` bereits erzwungen.

### Multiplizität

Eine Instanz `Verbindungsmittel` mit `multiplizitaet = 24`
repräsentiert ein Schraubenfeld aus 24 gleichartigen Schrauben
mit gemeinsamer Bemessungs-Logik (Mindestabstände untereinander,
effektive Anzahl n_ef). Die einzelnen 24 Schrauben werden nicht
als 24 getrennte Verbindungsmittel-Instanzen geführt — das wäre
geometrisch korrekt, datenmodellseitig aber unnötig redundant und
würde die Bemessungs-Aggregation erschweren. IFC erlaubt
`IfcMechanicalFastener` ausdrücklich als „one or many of actual
mechanical fasteners".

Bei der Visualisierung wird n × der Stab gerendert, bei der
Stückliste n × der Eintrag erzeugt; die UUID ist genau eine.

### Bemessungs-Trennlinie zur Bauteil-Bemessung

| Schicht                | Norm                  | Bezugsobjekt          |
|------------------------|-----------------------|-----------------------|
| Querschnittsbemessung  | EC5 Kap. 6, SIA 265 §4 | Bauteil               |
| Anschlussbemessung     | EC5 Kap. 8, SIA 265 Anhang A | Verbindungsmittel + Verbindung |
| Verstärkungs-Bemessung | EC5:2022 (Entwurf), ETA | Verstärkungselement |
| Klebung                | EC5 Kap. 10           | Klebung als Verbindungsmittel-Subtyp |

## Beziehungen

- **Oberbegriff**: `element` (Element der App-Ontologie).
- **Spezialisierungen** (eigene Einträge folgen):
  - **Nagel** (`nagel`): EC5 Kap. 8.3.
  - **Klammer** (`klammer`): EC5 Kap. 8.4.
  - **Bolzen** (`bolzen`): EC5 Kap. 8.5.
  - **Stabdübel** (`stabduebel`): EC5 Kap. 8.6.
  - **Schraube** (`schraube`): EC5 Kap. 8.7; insbesondere
    Holzschraube mit Vollgewinde (`vollgewindeschraube`).
  - **Holzdübel** (`holzduebel`): zimmermannsmäßiges
    Verbindungsmittel aus Hartholz.
  - **Nagelplatte** (`nagelplatte`): EC5 Kap. 8.10.
  - **Dübel besonderer Bauart** (`duebel_besonderer_bauart`):
    DIN EN 14545.
  - **Klebung** (`klebung`): EC5 Kap. 10.
- **Bestandteile (partitiv)** (geerbt von `element`):
  uuid, geometrie, lokale_platzierung, werkstoff;
  zusätzlich typ, nenndurchmesser, nennlaenge, achse, verbindet,
  multiplizitaet.
- **Verwendung**:
  - Bestandteil einer **Verbindung** (`verbindung`, eigener Eintrag
    folgt): die Verbindung führt eine Liste von Verbindungsmittel-
    UUIDs.
  - Bestandteil eines **Tragwerks** (`tragwerk`): erweitert die
    Element-Menge des Tragwerks, gehört zur Verbindungs-Menge V
    in der Tupel-Repräsentation (B, V, A, L).
- **Abgrenzung**:
  - **Bauteil** (`bauteil`): tragend und/oder raumbildend;
    Querschnittsbemessung nach EC5 Kap. 6. Verbindungsmittel sind
    **kein** Bauteil und werden in **eigenen Stücklisten** geführt.
  - **Verbinder** (`verbinder`): vermittelndes Bauteil zwischen
    Stäben (Knotenblech, Balkenschuh), das **selbst** durch
    Verbindungsmittel befestigt wird. Verbinder ist EC5-Konzept
    der „indirekten Verbindung" (8.2.3); Verbindungsmittel ist
    das einzelne Stück.
  - **Verstärkungselement** (`verstaerkungselement`): selbe
    physische Objektklasse wie ein Verbindungsmittel (typisch
    Vollgewindeschraube), aber in **Verstärkungsfunktion** mit
    eigener axialer Bemessung nach EC5:2022 / ETA. **Funktion
    bestimmt die Klasse, nicht das Material** (Memory
    `project_element_ontologie`, Designregel 2). Wer denselben
    Schraubentyp einmal als Anschluss-Schraube und einmal als
    Querzugverstärkung einbaut, instanziiert zwei verschiedene
    Element-Subklassen.
  - **Verbindung** (`verbindung`): Aggregat-Klasse über
    Bauteilen + Verbindungsmitteln (+ Verbindern + Verstärkungen)
    an einem Knotenpunkt. Verbindungsmittel ist das einzelne
    Tragstück, Verbindung das Aggregat darüber.
  - **Element** (`element`): abstrakter Oberbegriff;
    Verbindungsmittel ist eine konkrete Subklasse.

## Implementierungshinweis

Datentyp (Domänen-Schicht, Kotlin, Schicht
`domain.element.verbindungsmittel`):

```kotlin
package domain.element.verbindungsmittel

import domain.element.Element
import domain.geometrie.Geometrie
import domain.geometrie.LokalePlatzierung
import domain.geometrie.Strecke
import domain.holzbau.Werkstoff
import domain.identifikation.Positionsnummer
import domain.identifikation.Produktkennzeichnung
import domain.identifikation.Stahlguete
import domain.identifikation.ETAReferenz
import java.util.UUID

/** Verbindungsmittel-Typ nach EC5 Kap. 8 plus Klebung (Kap. 10). */
sealed interface VerbindungsmittelTyp {
    data object Nagel              : VerbindungsmittelTyp
    data object Klammer            : VerbindungsmittelTyp
    data object Bolzen             : VerbindungsmittelTyp
    data object Stabduebel         : VerbindungsmittelTyp
    data object Schraube           : VerbindungsmittelTyp
    data object Holzduebel         : VerbindungsmittelTyp
    data object NagelPlatte        : VerbindungsmittelTyp
    data object DuebelBesondererBauart : VerbindungsmittelTyp
    data object Klebung            : VerbindungsmittelTyp
}

/**
 * Verbindungsmittel: einzelnes mechanisches oder geklebtes
 * Tragstück, das Kräfte zwischen Bauteilen überträgt.
 *
 * Glossar: hg_verbindungsmittel.md
 *
 * Repräsentation folgt dem cadwork-Konzept "Verbindungsmittelachse
 * (VBA)": die Achse trägt Position/Richtung, der Typ trägt die
 * Spezifikation. Daraus generiert: Werkplan-Symbol,
 * Bohrlochbearbeitung am Bauteil, Stücklisten-Eintrag, statische
 * Position.
 *
 * IFC: IfcMechanicalFastener (Subtyp von IfcElementComponent).
 * BTLx: hybrid — meist Processing am Bauteil (Drilling, Lag-Screw),
 *        bei sichtbaren Tragelementen eigenes Part mit GUID.
 */
data class Verbindungsmittel(
    override val uuid: UUID,
    override val geometrie: Geometrie,
    override val lokalePlatzierung: LokalePlatzierung,
    override val werkstoff: Werkstoff,
    val typ: VerbindungsmittelTyp,
    val nenndurchmesser: Double,        // mm
    val nennlaenge: Double,             // mm
    val achse: Strecke,                 // Verbindungsmittelachse in W
    val verbindet: List<UUID>,          // FK auf Bauteil-UUIDs, |verbindet| >= 2
    val multiplizitaet: Int = 1,        // n >= 1; eine Instanz kann eine Gruppe sein
    val etaZulassung: ETAReferenz? = null,
    val stahlguete: Stahlguete? = null,
    override val positionsnummer: Positionsnummer? = null,
    override val produktkennzeichnung: Produktkennzeichnung? = null,
    override val bezeichnung: String? = null
) : Element {
    init {
        // 1. nenndurchmesser > Toleranzen.LAENGE_EPS
        // 2. nennlaenge > Toleranzen.LAENGE_EPS
        // 3. achse.laenge() <= nennlaenge + Toleranzen.LAENGE_EPS
        // 4. verbindet.size >= 2
        // 5. verbindet.all { it != uuid }   (kein Selbstbezug)
        // 6. multiplizitaet >= 1
    }
}
```

- **Einheit**: Längen in mm (Double). Winkel intern in Radiant.
- **Identität**: `uuid` von `element` ererbt; eine Instanz mit
  `multiplizitaet > 1` führt **eine** UUID, nicht n UUIDs.
- **Geometrie-Repräsentation**:
  - **Stiftförmig** (Nagel, Schraube, Bolzen, Stabdübel, Klammer):
    Achse als `Strecke`, Querschnitt als Kreis mit Durchmesser
    `nenndurchmesser`. Die Geometrie wird durch Sweep erzeugt; sie
    ist nicht eigenständig im Tupel persistiert (abgeleitet aus
    `achse`, `typ`, `nenndurchmesser`, `nennlaenge`).
  - **Nagelplatte / Dübel besonderer Bauart**: 2D-Plattengeometrie
    mit Dicke; eigene Geometrie-Variante in Folgearbeit.
  - **Klebung**: Klebfugen-Fläche zwischen zwei Bauteilen; eigene
    Geometrie-Variante in Folgearbeit.
- **Foreign-Key-Regel** (siehe `uuid`): `verbindet: List<UUID>` und
  jede andere Beziehung referenzieren ausschließlich UUIDs.
- **Multiplizität und Bemessung**: `multiplizitaet = n` repräsentiert
  eine Gruppe; die effektive Anzahl n_ef nach EC5 Gl. 8.17 (für
  Schraubenreihen in Faserrichtung) ist
  ```
  n_ef = min(n, n^0.9 · (a₁ / (13 · d))^(1/4))
  ```
  und wird in der Bemessungs-Schicht berechnet, nicht im Glossar.
- **IFC-Mapping** (Persistenzschicht):
  - IFC-Klasse: `IfcMechanicalFastener` (Subtyp von
    `IfcElementComponent`, **NICHT** `IfcBuildingElement`).
  - Property Sets: `Pset_FastenerCommon` (Reference,
    NominalDiameter, NominalLength), `Pset_MechanicalFastener`
    (NominalLength, NailLength, NominalDiameter, Strength,
    PreLoad).
  - Multiplizität: ein `IfcMechanicalFastener` darf „one or many"
    repräsentieren; die App verwendet i. d. R. eine Instanz pro
    funktionaler Gruppe.
  - Hersteller-BIM-Bibliotheken (Rothoblaas, Würth, SFS, Simpson
    Strong-Tie) liefern alle Verbindungsmittel als
    `IfcMechanicalFastener` aus.
- **BTLx-Mapping** (Persistenzschicht):
  - **Standardfall**: `Processing` am betroffenen Bauteil
    (`Drilling` für Stabdübel/Bolzen, `Lag-Screw` für
    Holzschrauben). Das Verbindungsmittel ist dann **nicht** als
    eigenes Part im BTLx-File geführt.
  - **Sonderfall** (lange Vollgewindeschrauben, Gewindestangen,
    ETA-Verstärkungsschrauben mit eigener Stückliste, sichtbare
    Tragelemente): eigenes `Part` mit `@GUID` (entspricht
    `Verbindungsmittel.uuid`).
  - Die Wahl ist exportseitig pro Verbindungsmittel-Instanz
    konfigurierbar; Default folgt aus `typ` und `nennlaenge`.
- **Edge Cases**:
  - **Verbindungsmittel mit |verbindet| = 1**: nicht erlaubt
    (eine Bohrung in einem einzelnen Bauteil ist eine Bauteil-
    Bearbeitung, kein Verbindungsmittel). Konstruktor liefert
    `Resultat.Fehler` bzw. `Entartet.VerbindungsmittelOhneAnschluss`.
  - **Achse-Länge ≫ Nennlänge**: nicht erlaubt;
    `Entartet.AchseLaengerAlsNennlaenge`.
  - **Doppel-UUID in `verbindet`**: nicht erlaubt;
    `Entartet.DoppelterAnschluss`.
  - **Verstärkungs-Schraube**: niemals als `Verbindungsmittel`
    instanziieren, sondern als `Verstaerkungselement`.
- **Abgeleitete Eigenschaften**:
  - `geometrieInWelt(): GeometrieInW` — Sweep des Typ-Querschnitts
    entlang der Achse, transformiert nach W.
  - `bohrlochAn(b: Bauteil): Bohrloch` — die Bohrlochbearbeitung,
    die das Verbindungsmittel im Bauteil b erzeugt
    (Implementierung in der Geometrie-Schicht, Folgearbeit).
  - `effektiveAnzahl(achsabstand: Double): Double` — n_ef nach
    EC5 Gl. 8.17 (Bemessungs-Schicht).
- **Bezeichner-Konvention** (CLAUDE.md): Domänen-Klasse heißt
  `Verbindungsmittel` (deutsch, Glossarbegriff); Spezialisierungen
  heißen `Nagel`, `Schraube`, `Bolzen`, `Stabduebel`,
  `Klammer`, `Holzduebel`, `NagelPlatte`,
  `DuebelBesondererBauart`, `Klebung`.

## Quellen

**Primär (normativ):**

- DIN EN 1995-1-1:2010-12, „Eurocode 5: Bemessung und Konstruktion
  von Holzbauten – Teil 1-1", Kapitel 8 und Kapitel 10.
- DIN EN 14592:2022-09, „Holzbauwerke – Stiftförmige
  Verbindungsmittel – Anforderungen".
- DIN EN 14545:2009-02, „Holzbauwerke – Verbinder – Anforderungen".
- SIA 265:2021, „Holzbau", Anhang A.
- ÖNORM B 1995-1-1:2019.
- ISO 16739-1:2024, IFC-Entität `IfcMechanicalFastener`.
- design2machine: *BTLx 2.x Specification* (Stand 2024).
- ETA-11/0190 (Würth ASSY).
- Z-9.1-519 (SPAX Vollgewindeschrauben, DIBt).
- ETA-12/0373 (Reisser).

**Sekundär:**

- Blass, H. J.; Sandhaas, C.: *Ingenieurholzbau – Grundlagen der
  Bemessung.* KIT Scientific Publishing, Karlsruhe 2016, Kap. 8.
- Holzbau-Handbuch, Reihe 2, Teil 1, Folge 1, Informationsdienst
  Holz.
- Mönck, W.; Rug, W.: *Holzbau – Bemessung und Konstruktion.*
  16. Auflage, Beuth, Berlin 2015, Kap. 7.
- cadwork informatik: Dokumentation „Verbindungsmittelachse (VBA)".
- Hersteller-BIM-Bibliotheken: Rothoblaas, Würth, SFS, Simpson
  Strong-Tie.

**Korpus (nicht autoritativ):**

- Holzbau Deutschland, Merkblatt „Begriffe und Klassifizierungen
  für den Holzbau" (abgerufen 2026-05-08).
- Wikipedia, Lemma „Holzverbindung" (abgerufen 2026-05-08).
