---
id: bearbeitung
benennung: Bearbeitung
synonyme: [Holzbearbeitung, Abbund-Bearbeitung, "Bearbeitung am Bauteil", subtraktive Bearbeitung]
abgelehnte_benennungen: [Bearbeitungsschritt, Operation, Abbundoperation, Verarbeitung, Holzverbindung, Verbindung, "processing", "machining", "feature", "cutout", "subtractive feature"]
oberbegriff: null
begriffstyp: partitiv
voraussetzungen: [bauteil, uuid, lokales_koordinatensystem, polyeder, toleranzen]
abgrenzung_zu: [verbindungsmittel, verbinder, verstaerkungselement, element, verbindung, bauteil, querschnitt, polyeder, lokales_koordinatensystem]
status: entwurf
subglossar_pendant: notwendig
quellen_primär:
  - "design2machine: 'BTLx interface description', Version 2.1, 16.11.2023, Abschnitt 'List of Processings' (S. 8 ff., S. 9): Prozessierungen als parametrische, am Bauteil definierte materialabtragende Operationen (JackRafterCut, LongitudinalCut, DoubleCut, RidgeValleyCut, SawCut, Slot, BirdsMouth, HipValleyRafterNotch, Lap, LogHouseHalfLap, FrenchRidgeLap, Chamfer, LogHouseJoint, LogHouseFront, Pocket, Drilling, Tenon, Mortise, House, HouseMortise, DovetailTenon, DovetailMortise, JapaneseMortise, JapaneseTenon, SimpleScarf, ScarfJoint, StepJoint, StepJointNotch, Planing, ProfileFront, ProfileCambered, RoundArch, ProfileHead, Sphere, TriangleCut, TyroleanDovetail, Dovetail, SimpleContour, NURBS Curve, NURBS Patch, Composite). Annotationen (Marking, Text) sind in BTLx als Processings geführt, aber materialerhaltend."
  - "ISO 16739-1:2024 'Industry Foundation Classes (IFC) for data sharing in the construction and facility management industries — Part 1: Data schema' (IFC 4.3.2), Entitäten 'IfcOpeningElement', 'IfcFeatureElementSubtraction' und Beziehung 'IfcRelVoidsElement': subtraktive Geometriemerkmale werden als eigene Entitätsklasse außerhalb der IfcElement-Hierarchie geführt; ihre Wirkung auf das Master-Element ist eine implizite Boole'sche Differenz auf der Body-Repräsentation. [direkt]"
  - "DIN EN 1995-1-1:2010-12 (Eurocode 5), Abschnitt 5.2 (Berücksichtigung der Querschnittsschwächungen) und Abschnitt 6.5 (Querzug- und Schubnachweise an ausgeklinkten Bauteilen): Bearbeitungen reduzieren den tragenden Querschnitt; die geschwächte Stelle ist Bemessungsobjekt."
  - "DIN EN 14081-1:2019-10 'Holzbauwerke – Nach Festigkeit sortiertes Bauholz mit rechteckigem Querschnitt – Teil 1', Bezugsquerschnitt als ungeschwächter Vollquerschnitt; Bearbeitungen werden gegen diesen Bezug gemessen."
  - "SIA 265:2021 'Holzbau', Abschnitt 4.6 (Querschnittswerte) und Abschnitt 5 (Konstruktive Durchbildung): Querschnittsschwächungen durch Bearbeitungen sind in der Bemessung gesondert zu erfassen."
quellen_sekundär:
  - "Mönck, W.; Rug, W.: Holzbau – Bemessung und Konstruktion. 16. Aufl., Beuth, Berlin 2015, Kap. 7 'Verbindungen' und Kap. 11 'Dachtragwerke', Versätze, Kerven, Zapfen als Bauteilbearbeitungen."
  - "Gerner, M.: Fachwerk – Instandsetzung, Sanierung, Neubau. DVA, 7. Aufl. 2007, Glossar (Versatz, Blattung, Zapfen, Kerve, Schlitz, Kamm)."
  - "Natterer, J.; Herzog, T.; Volz, M.: Holzbau-Atlas. 4. Aufl., Birkhäuser, Basel 2003, Kap. 'Verbindungen und Anschlüsse'."
  - "cadwork informatik: Dokumentation 'Bearbeitung am Bauteil' (Standard-Bearbeitungstypen Klaue/Kerve, Versatz, Bohrung, Schlitz, Zapfenloch, Blatt, Schrägschnitt) — Korpus, nicht autoritativ."
  - "Kloepfer, H.: Holzschutz nach DIN 68800 — bauliche Maßnahmen, kloepfer 2014: Bearbeitungen an tragenden Hölzern als Schwachstellen für Bewitterung und Holzschutz."
quellenkonflikt: |
  Es gibt keine Holzbau-Norm (SIA 265, SIA 232/1, DIN 1052,
  DIN EN 1995-1-1, DIN 68800), die einen geschlossenen
  Oberbegriff für „Bearbeitung am Bauteil" als Datenmodell-Wurzel
  einführt. EC5 5.2 und SIA 265 4.6 setzen den Begriff voraus
  („Querschnittsschwächung", „ausgeklinkter Träger", „Versatz")
  und behandeln nur die Bemessungsfolgen.

  Die einzige geschlossene, normativ gepflegte Spezifikation
  konkreter Bearbeitungstypen für den digitalen Abbund ist die
  BTLx-Spec von design2machine (BTLx 2.1). Sie listet ca. 40
  Processing-Typen, davon sind etwa 35 echte materialabtragende
  Bearbeitungen, ca. 3 Annotationen (Marking, Text) und ca. 2
  Komposita (Composite, NURBSCurve/Patch als Hilfsgeometrien).

  IFC 4.3 modelliert subtraktive Features als eigene Klasse
  `IfcFeatureElementSubtraction` (Spezialisierung
  `IfcOpeningElement`) außerhalb der `IfcElement`-Hierarchie,
  verbunden mit dem Master-Element über `IfcRelVoidsElement`. IFC
  geht damit weiter als BTLx: das Subtraktions-Feature ist eine
  eigenständig identifizierte Entität mit GlobalId, deren Wirkung
  auf das Bauteil durch eine implizite Boole'sche Differenz
  realisiert wird.

  Der vorliegende Eintrag wählt den **konzeptuellen Mittelweg**:

  - **Bearbeitung ist ein eigener Glossarbegriff mit eigener
    UUID**, parametrischer Definition und Lokal-Platzierung
    relativ zum Bauteil. Die UUID ist nötig zur Referenzierbarkeit
    der einzelnen Bearbeitung aus externen Kontexten:
    Verbindungsmittel, die eine Bohrung als Folgegeometrie
    erzeugen; Bemessungs-Nachweise, die sich auf einen konkreten
    Kervquerschnitt beziehen (EC5 6.5); CNC-Schnittstellen wie
    BTLx, deren Processings über die UUID-Bezeichnung
    rückverfolgbar sein müssen.
  - **Bearbeitung ist KEIN eigenständiges Aggregat**, sondern ein
    referenzierbarer **Bestandteil eines Bauteils** (Bauteil-
    Bestandteil; im Glossar nicht als eigener Term geführt). Die
    Beziehung Bauteil ↔ Bearbeitung ist eine **partitive
    Komposition**: das Bauteil besitzt seine Bearbeitungen, eine
    freistehende Bearbeitung existiert nicht. Der Lebenszyklus
    der Bearbeitung ist an den des Bauteils gekoppelt; bei
    Löschung des Bauteils erlischt sie kaskadierend.
  - **Bearbeitung ist NICHT eine Subklasse von `element`**, weil
    sie kein verbautes Einzelobjekt im Sinne der App-Ontologie
    ist (Memory `project_element_ontologie`): keine eigene
    Materialklasse, kein eigener Bemessungsstatus, kein
    eigenständiger Lebenszyklus. Eine Bearbeitung ist immer an
    genau ein Bauteil gebunden.
  - **Bearbeitung ist ausschließlich subtraktiv** (klassisches
    Zimmermanns-Verständnis vom Abbund): Material wird **vom**
    Bauteil entfernt. Additive Operationen (Anbringen eines
    Verbindungsmittels, Aufschrauben eines Verbinders, Einbringen
    einer Verstärkungsschraube) sind keine Bearbeitungen,
    sondern eigene Element-Subklassen unter `element`. Das ist
    die Hauptabgrenzung dieses Eintrags und macht den Begriff
    operational scharf.
  - **BTLx/IFC sind Übersetzungsschichten in Phase 4 (Export),
    keine direkte Schemaübernahme.** Die App-interne Subtypen-
    liste ist nach zimmermannssprachlichen, nicht nach BTLx-
    technischen Kriterien gegliedert (z. B. fasst die App-Klasse
    `Kerve` mehrere BTLx-Processings — primär `BirdsMouth`,
    in Sonderfällen `HipValleyRafterNotch` und `StepJointNotch`
    — auf einen einzigen begrifflich homogenen Glossartyp
    zusammen). Insbesondere modelliert IFC subtraktive Features
    als `IfcOpeningElement` mit `IfcRelVoidsElement`-Relation zum
    Master-Element; das ist eine externe Datenaustausch-
    Konvention, die in der Übersetzungsschicht zwischen
    Domänenmodell und IFC-Export berücksichtigt wird, aber **nicht**
    die ontologische Begründung für die Modellierung im
    Domänenmodell darstellt. Im Domänenmodell selbst wird die
    ontologisch sauberere partitive Komposition gewählt.

  Diese Festlegung ist konsistent mit allen konsultierten Quellen,
  sobald sie als App-interne Konvention (nicht als Aussage über
  die Quellen selbst) verstanden wird.

  Subtypen mit Implementierungs-Status (Phase 2 ff.):
    - `kerve` — Phase 2 (gleichzeitig mit diesem Eintrag definiert).
    - `anschnitt` — bereits angelegt (`hg_anschnitt.md`); BTLx
      `JackRafterCut`/`LongitudinalCut`/`DoubleCut`/`TriangleCut`.
    - `bohrung` — bereits angelegt (`hg_bohrung.md`); BTLx
      `Drilling`/`Pocket`.
    - `versatz` — bereits angelegt (`hg_versatz.md`); BTLx
      `StepJoint`/`StepJointNotch`.
    - `zapfen` — bereits angelegt (`hg_zapfen.md`); BTLx `Tenon`,
      Schwalbenschwanz-Variante `DovetailTenon`.
    - `zapfenloch` — bereits angelegt (`hg_zapfenloch.md`); BTLx
      `Mortise`, `DovetailMortise`, `HouseMortise`.
    - `schlitz` — Folgearbeit (Trigger: Schlitzblech-Verbinder).
    - `blatt` (Blattung), `kamm` (Kammverbindung),
      `chamfer` (Fase) — Folgearbeit nach Bedarf.
  Diese Subtypen sind in `voraussetzungen` **nicht** verlinkt,
  weil sie noch nicht als eigene Glossareinträge existieren
  (siehe Memory `project_glossar_konventionen` zu Forward-
  Verweisen).
---

## Prosa-Definition

Eine **Bearbeitung** ist eine subtraktive, materialabtragende
geometrische Operation, die einem genau einem Bauteil zugeordnet
ist, durch eine endliche Menge typabhängiger Parameter und eine
lokale Platzierung relativ zum Bauteil-Lokal-Koordinatensystem
vollständig festgelegt ist und deren Wirkung auf das Bauteil in
der Entfernung des durch die Bearbeitung beschriebenen
Werkzeugkörpers aus dem ungeschwächten Bauteilkörper besteht.

## Mathematische Definition

Sei

- 𝓤 der UUID-Raum nach `uuid`,
- 𝓑 die Menge der Bauteile nach `bauteil`,
- SE(3) = SO(3) ⋉ ℝ³ die Menge der Starrkörpertransformationen
  (siehe `lokales_koordinatensystem`),
- 𝓟 die Menge der zulässigen Polyeder im ℝ³ nach `polyeder`,
- 𝓣 := { Kerve, Bohrung, Versatz, Zapfenloch, Schlitz, Blatt,
  Kamm, Anschnitt, Fase, … } die endliche Menge der zulässigen
  Bearbeitungstypen (`sealed`-Aufzählung; konkrete Subtypen
  werden in eigenen Glossareinträgen definiert),
- für jeden Typ τ ∈ 𝓣 eine endliche, typspezifische Parametermenge
  Π_τ ⊂ ℝⁿ_τ × ℬ^m_τ (Längen in mm, Winkel in Radiant, Boolesche
  Optionen) sowie eine **Werkzeugkörper-Funktion**
  ```
  K_τ : Π_τ → 𝓟,    p_τ ↦ K_τ(p_τ),
  ```
  die jedem zulässigen Parametertupel p_τ einen abgeschlossenen,
  beschränkten Polyeder K_τ(p_τ) ⊂ ℝ³ in einem typeigenen
  Bezugs-Koordinatensystem zuordnet.

Dann ist eine **Bearbeitung** das Tupel

```
F := (uuid, typ, parameter, lokale_platzierung, bezeichnung?)
```

mit

- **uuid** ∈ 𝓤: technischer Surrogatschlüssel der Bearbeitung,
- **typ** τ ∈ 𝓣: Bearbeitungstyp (sealed),
- **parameter** p_τ ∈ Π_τ: typspezifisches Parametertupel,
- **lokale_platzierung** T_F ∈ SE(3): Starrkörpertransformation,
  die das Bezugs-Koordinatensystem des Werkzeugkörpers K_τ(p_τ)
  in das Bauteil-Lokal-Koordinatensystem L_B des zugehörigen
  Bauteils B überführt,
- **bezeichnung** ∈ String ∪ {⊥}: optionaler Anzeigename.

Das zugehörige Bauteil B ∈ 𝓑 ist **nicht Bestandteil des Tupels**:
Die Beziehung Bearbeitung → Bauteil ist eine partitive Komposition,
in der das Bauteil seine Bearbeitungen als geordnete Liste hält.
Eine Backref `bauteil_uuid` am Bearbeitungs-Objekt wäre redundante
Information (sie doppelt die Container-Beziehung) und würde eine
zusätzliche Konsistenz-Invariante erzwingen (Backref muss zum
enthaltenden Bauteil passen). Die Auflösung „zu welchem Bauteil
gehört diese Bearbeitungs-UUID?" ist Aufgabe der Repository-/Index-
Schicht, nicht des Glossars. Die Glossar-Festlegung ist hier strikter
als IFC: IFC modelliert die Beziehung in einer eigenen Relations-
Entität `IfcRelVoidsElement`, nicht als Backref am
`IfcOpeningElement` — Variante 1 ist also IFC-konsistent.

Die **Wirkung** der Bearbeitung F auf das Bauteil B ist die
Boole'sche Differenz

```
G_B'(F) := G_B^lokal \ T_F( K_τ(p_τ) ) ⊂ ℝ³,                    (1)
```

wobei G_B^lokal die ungeschwächte Bauteilgeometrie im Bauteil-
Lokal-System ist und T_F( K_τ(p_τ) ) der ins Bauteil-Lokal-System
überführte Werkzeugkörper. Bei mehreren Bearbeitungen
F_1, …, F_n eines Bauteils B ist die endgültige Bauteilgeometrie

```
G_B^bearbeitet := G_B^lokal \ ⋃_{i=1}^{n} T_{F_i}( K_{τ_i}(p_{τ_i}) ).  (2)
```

Die **Welt-Geometrie** des bearbeiteten Bauteils ergibt sich durch
Anwendung der Bauteil-Lokal-Platzierung T_{L_B→W} ∈ SE(3) (siehe
`lokales_koordinatensystem`):

```
G_W^bearbeitet(B) := T_{L_B→W}( G_B^bearbeitet ).               (3)
```

Es gilt strukturell

```
G_B^bearbeitet ⊆ G_B^lokal,                                     (4)
```

d. h. die Bauteilgeometrie wird durch jede Bearbeitung ausschließlich
verkleinert (subtraktive Festlegung).

## Wohldefiniertheit

- **Existenz**: Für jedes konkrete Bauteil und jeden im Abbund
  vorkommenden zimmermannsmäßigen Materialabtrag (Kerve, Bohrung,
  Versatz, Zapfenloch, Schlitz, Blatt, Kamm, Anschnitt, Fase) lässt
  sich das obige Tupel angeben. Mindestkonfiguration: typ = Kerve
  (siehe `kerve`), parameter = Default-Parametertupel der Kerve,
  T_F = Identität in SE(3), bezeichnung = ⊥.
- **Eindeutigkeit der Identität**: Innerhalb eines Modells gilt
  ∀ F₁, F₂ : (F₁ ≠ F₂) ⇒ (F₁.uuid ≠ F₂.uuid). UUID v7 nach
  RFC 9562, vgl. `uuid`.
- **Eindeutigkeit der Zuordnung**: Jede Bearbeitung gehört zu
  **genau einem** Bauteil. Diese Zuordnung wird über die
  partitive Komposition realisiert: Bearbeitung F ist genau dem
  Bauteil B zugeordnet, in dessen Bearbeitungs-Liste F enthalten
  ist. Die Container-Eigenschaft ist bereits eine Bijektion
  Bearbeitung → Bauteil (Memory `project_bauteil_identifikation`,
  partitive Komposition). Mehrfachzuordnung ist strukturell
  ausgeschlossen; eine geometrisch ähnliche Bearbeitung an einem
  zweiten Bauteil ist eine **eigene Instanz** mit eigener UUID
  in der Bearbeitungs-Liste des zweiten Bauteils.
- **Wohldefiniertheit der Wirkung**: Die Boole'sche Differenz (1)
  ist für beschränkte, abgeschlossene Polyeder K_τ(p_τ) und einen
  beschränkten Bauteilkörper G_B^lokal stets wohldefiniert (Ergebnis
  ist eine messbare, beschränkte Punktmenge). Das Ergebnis ist im
  allgemeinen kein Polyeder mehr, sondern ein Polyeder oder eine
  Polyederzerlegung; eine konkrete Polyederrepräsentation des
  Ergebnisses zu konstruieren ist Aufgabe der Geometrie-Schicht
  (Folgearbeit Phase 3.2).
- **Reihenfolge-Unabhängigkeit der Aggregation (2)**: Die Vereinigung
  ⋃ ist kommutativ und assoziativ; damit ist G_B^bearbeitet
  unabhängig von der Reihenfolge, in der die einzelnen Bearbeitungen
  F_1, …, F_n abgezogen werden. Die zimmermannsmäßige Reihenfolge
  des **Abbunds** (z. B. erst Kerve fräsen, dann bohren) ist eine
  Prozessfrage, keine Geometriefrage; sie ist nicht im Glossar
  geführt, sondern in der Fertigungs-Schicht (BTLx-Export).
- **Subtraktivität (4)**: Strukturell garantiert durch die
  Definition als Boole'sche Differenz; eine „additive Bearbeitung"
  ist im Sinne dieses Glossars **nicht** möglich. Wer Material
  hinzufügen will, instanziiert ein eigenes Element (Bauteil,
  Verbindungsmittel, Verbinder, Verstärkungselement) und nicht eine
  Bearbeitung.
- **Unabhängigkeit von der Wahl des Bezugs-Koordinatensystems
  des Werkzeugkörpers**: Für jede zulässige Wahl des typeigenen
  Bezugs-Koordinatensystems liefert die zugehörige T_F dasselbe
  G_B'(F). Die Wahl ist Modellierungskonvention pro Subtyp (z. B.
  bei `kerve`: Ursprung im Auflagepunkt der Kervsohle, x-Achse
  entlang Bauteilachse, z-Achse in Kervtiefe-Richtung); semantisch
  invariant.
- **Konsistenz Werkzeugkörper ↔ Bauteilgeometrie**: Es ist nicht
  erforderlich, dass T_F( K_τ(p_τ) ) ⊂ G_B^lokal; ein über die
  Bauteilberandung hinausragender Werkzeugkörper ist zulässig
  (Standardfall einer Klauenkerve, deren Werkzeugkörper unten aus
  dem Sparren herausragt) und führt einfach zu einer Differenz, die
  außerhalb des Bauteils geometrisch unwirksam ist. Die Toleranz
  für „außerhalb" ist `Toleranzen.LAENGE_EPS`.
- **Plausibilität der Querschnittsschwächung** (weiche Invariante,
  nicht Bestandteil der Definition): Bearbeitungen reduzieren den
  tragenden Querschnitt nach EC5 5.2 / SIA 265 4.6. Die App
  warnt — typisiert pro Subtyp — wenn die verbleibende Holzhöhe
  bzw. -breite eine subtypspezifische Faustregel unterschreitet
  (z. B. bei `kerve`: Restholz ≥ ⅔ Sparrenhöhe). Diese
  Plausibilitätsprüfung ist **keine** Definitionsbedingung; eine
  über die Faustregel hinausgehende Kerve bleibt eine Kerve im
  Sinne dieses Glossars, sie ist bemessungstechnisch jedoch
  problematisch.
- **Nicht-Zirkularität**: Die Definition stützt sich nur auf
  bereits definierte Begriffe (`bauteil`, `uuid`,
  `lokales_koordinatensystem`, `polyeder`, `toleranzen`) sowie
  auf die abstrakte Subtypen-Menge 𝓣, deren konkrete Elemente in
  eigenen Folgeeinträgen definiert werden. Sie kommt nicht in
  ihrer eigenen Definition vor und verweist nicht auf konkrete
  Subtypen (Kerve, Bohrung, Versatz …) in der Definition selbst,
  sondern nur in der Erläuterung und im quellenkonflikt-Block.

## Erläuterung (nicht normativ)

Der Bearbeitungs-Begriff dieses Glossars ist die **Wurzel der
App-Ontologie für subtraktive Geometriemerkmale am Bauteil**. Er
trägt diejenigen Eigenschaften, die jeder konkrete Bearbeitungs-
Subtyp generisch erbt: eigene UUID, Foreign-Key auf das
zugehörige Bauteil, ein Bearbeitungs-Typ, ein typspezifisches
Parametertupel, eine lokale Platzierung relativ zum Bauteil und
optionaler Anzeigename.

### Vier Element-Subklassen vs. Bearbeitung — die ontologische Trennlinie

In der App-Ontologie (Memory `project_element_ontologie`) gibt es
vier Element-Subklassen, die alle **additiv** mit einem Bauteil
verbunden werden:

| Klasse                  | Wirkung am Bauteil                          | UUID-Hierarchie       |
|-------------------------|---------------------------------------------|-----------------------|
| `bauteil`               | ist selbst Tragglied                        | eigene Element-UUID   |
| `verbindungsmittel`     | überträgt Kräfte zwischen ≥ 2 Bauteilen     | eigene Element-UUID   |
| `verbinder`             | vermittelt zwischen Bauteilen               | eigene Element-UUID   |
| `verstaerkungselement`  | verstärkt Bauteil axial                     | eigene Element-UUID   |
| **`bearbeitung`**       | **entfernt Material aus genau einem Bauteil** | eigene UUID, FK auf 1 Bauteil |

Bearbeitung ist **kein eigenständiges Aggregat** parallel zu
Element, Verbindung, Tragwerk oder Bauteil-Aggregat, sondern ein
**referenzierbarer Bestandteil eines Bauteils**. Sie ist **kein
verbautes Einzelobjekt**, sondern ein **geometrisches Merkmal
eines verbauten Einzelobjekts**, das durch eine eigene UUID
adressierbar bleibt (für Verbindungsmittel-Folgegeometrie,
Bemessungs-Nachweise nach EC5 6.5 und CNC-Schnittstellen wie
BTLx), aber dessen Lebenszyklus an das tragende Bauteil gekoppelt
ist.

Der Unterschied wird besonders sichtbar an der Bohrung als
Grenzfall:

- **Bohrung als Bearbeitung**: ein Loch in einem einzelnen Bauteil
  ohne durchgehendes Verbindungsmittel (z. B. Lüftungsbohrung,
  vorgebohrter Schraubkanal, Sicherungsbohrung). Subtraktiv,
  wirkt nur auf dieses Bauteil.
- **Bohrung als Konsequenz eines Verbindungsmittels**: das
  Bohrloch wird durch ein Verbindungsmittel (Schraube, Bolzen,
  Stabdübel) verursacht. Modelliert wird das Verbindungsmittel,
  nicht das Bohrloch — die geometrische Bohrung ist eine
  abgeleitete Konsequenz, im BTLx-Export erscheint sie als
  Processing `Drilling` am Bauteil (siehe `hg_verbindungsmittel.md`,
  Edge Case „Verbindungsmittel mit |verbindet| = 1").

**Funktion bestimmt die Klasse, nicht die Geometrie.** Eine
Bohrung ohne Verbindungsmittel ist eine `Bearbeitung` mit
`typ = Bohrung`. Eine geometrisch identische Bohrung, durch die
eine Schraube läuft, wird als `Verbindungsmittel` instanziiert;
das Bohrloch ist Folgegeometrie und nicht eigenständig im Modell.

### Komposition statt Vererbung

Die Beziehung zwischen Bauteil und Bearbeitung ist **partitive
Komposition** (das Bauteil besitzt seine Bearbeitungen; eine
freistehende Bearbeitung existiert nicht; Löschung des Bauteils
kaskadiert auf alle seine Bearbeitungen):

```
Bauteil  1 ── 0..n ──► Bearbeitung   (FK: bauteil_uuid)
```

Auf Bauteil-Ebene bleibt die ungeschwächte Geometrie (das
„Rohbauteil") als kanonische Repräsentation; die bearbeitete
Geometrie ist eine **abgeleitete Funktion** über die ungeschwächte
Geometrie und die Liste aller Bearbeitungen (Gleichung 2). Diese
Trennung hat drei Vorteile:

1. **Kanonische Querschnittswerte**: Querschnittsfläche, Trägheits-
   moment, Schwerpunkt usw. werden weiterhin am ungeschwächten
   Querschnitt geführt; die Schwächungsfaktoren der Bemessung
   (EC5 5.2) greifen darauf zu, ohne die Bauteilrepräsentation zu
   verändern.
2. **Editierbarkeit**: Bearbeitungen können einzeln hinzugefügt,
   geändert oder entfernt werden, ohne dass die Bauteilgeometrie
   neu rekonstruiert werden muss.
3. **Export-Treue**: Sowohl BTLx (Processings am Part) als auch IFC
   (Voiding-Beziehung) modellieren genau diese Trennung; die App-
   interne Struktur ist 1:1 exportierbar (Trennung Roh-Geometrie /
   Bearbeitungs-Liste).

### BTLx- und IFC-Übersetzung (Export-Schicht, Phase 4)

**BTLx 2.1** (design2machine) listet unter „Processings"
ca. 35 echte materialabtragende Operationen. Die Übersetzung der
App-internen Bearbeitungs-Subtypen auf BTLx-Processings ist
**eine Übersetzungsschicht**, keine Schemaübernahme:

| App-Subtyp        | Primäre BTLx-Entsprechung               | Sonderfälle                          |
|-------------------|-----------------------------------------|--------------------------------------|
| `kerve`           | `BirdsMouth`                            | `HipValleyRafterNotch` (Grat/Kehle), `StepJointNotch` (Stuhl) |
| `bohrung`         | `Drilling`                              | `Pocket` nur für grosse Sacklöcher mit Fräser-Werkzeug → eigener Subtyp `aussparung` (Folgearbeit) |
| `versatz`         | `StepJoint`                             | `StepJointNotch` bei tiefen Versätzen |
| `zapfen`          | `Tenon`                                 | `DovetailTenon` (Schwalbenschwanz)   |
| `zapfenloch`      | `Mortise`                               | `DovetailMortise`, `HouseMortise`, `JapaneseMortise` |
| `schlitz`         | `Slot`                                  |                                      |
| `blatt`           | `Lap`                                   | `LogHouseHalfLap`                    |
| `kamm`            | `House`                                 |                                      |
| `anschnitt`       | `JackRafterCut`, `LongitudinalCut`, `DoubleCut`, `TriangleCut` | typabhängig (1:n)  |
| `fase`            | `Chamfer`                               |                                      |

**IFC 4.3** modelliert subtraktive Features einheitlich als
`IfcOpeningElement` (Spezialisierung von
`IfcFeatureElementSubtraction`), verbunden mit dem Master-Element
über `IfcRelVoidsElement`. Die App-Bearbeitung mappt direkt auf
ein `IfcOpeningElement` mit eigener `GlobalId` (entspricht der
Bearbeitungs-UUID); die Wirkung wird über `IfcRelVoidsElement`
mit dem zugehörigen Bauteil realisiert.

Beide Übersetzungen sind **bidirektional verlustfrei** für die
Standard-Subtypen; bei NURBS-Patches und freien Polyederformen
greift im IFC-Pfad die generische `BooleanResult`-Repräsentation,
die in dieser App nicht als App-internes Konzept geführt wird
(Folgearbeit, falls überhaupt erforderlich).

### Tätigkeit vs. Resultat

Im zimmermannssprachlichen Sprachgebrauch bezeichnet „Bearbeitung"
sowohl die **Tätigkeit** (das Bearbeiten, der Abbund-Vorgang) als
auch das **Resultat** (die geometrische Veränderung am fertigen
Bauteil). Dieser Glossareintrag definiert ausschließlich die
**Resultatslesart**: das geometrische Merkmal am bearbeiteten
Bauteil. Die Tätigkeit (Werkzeugwahl, Schnittreihenfolge,
Werkzeugführung, CNC-Programmierung) ist Gegenstand der
Fertigungs-Schicht und nicht im Glossar geführt.

### Welt-aligned vs. bauteil-aligned Bearbeitungen

Die Werkzeugkörper-Konstruktion der Bearbeitungs-Subtypen folgt
zwei verschiedenen Bezugs-Konventionen, die sich orthogonal aus
der zimmermannssprachlichen Praxis ergeben:

- **Welt-aligned** (Sohle/Senkel in Bezug auf Welt-Lotachse):
  Die Sohle ist parallel zur Welt-Horizontalen (Bleischnitt),
  der Senkel parallel zur Welt-Vertikalen. Anwendungsfall: die
  Kerve (`hg_kerve.md`), bei der die formschlüssige Auflagerung
  auf einer welt-horizontalen Pfettenoberseite normativ ist
  (Zimmermannsregel: „Bleischnitt unten, Senkel hinten").
- **Bauteil-aligned** (Geometrie-Parameter in Bezug auf
  Bauteilachse und Bauteilflächen): Die Bearbeitungs-Geometrie
  wird durch Winkel gegen die Bauteilachse und Lage auf einer
  Bezugsfläche parametrisiert, unabhängig von der Welt-
  Ausrichtung des Bauteils. Anwendungsfälle: `anschnitt`,
  `versatz`, `bohrung`, `zapfen`, `zapfenloch`.

Die Kerve ist im Subtypen-Spektrum **Solitär in welt-aligned**.
Diese Asymmetrie ist begründet: nur die Kerve verlangt eine
welt-horizontale Auflagefläche (Tragwerks-Funktion), die übrigen
Bearbeitungen sind welt-orientierungs-neutral. Die App-Konstanten
beider Klassen werden zentral in `hg_toleranzen.md` Sektion
„Bearbeitungs-Plausibilitäts-Konstanten" gepflegt.

## Beziehungen

- **Oberbegriff**: keiner als eigener Glossarterm. Bearbeitung
  ist konzeptuell ein **Bauteil-Bestandteil** (im Glossar nicht
  als eigener Term geführt; partitive Beziehung Bauteil ↔
  Bearbeitung). Sie ist **kein eigenständiges Aggregat** parallel
  zu `element`, `verbindung`, `tragwerk` oder `bauteil_aggregat`,
  sondern ein referenzierbares Bestandteil genau eines Bauteils
  mit eigener UUID (für Referenzierbarkeit aus
  Verbindungsmittel-Folgegeometrie, Bemessungs-Nachweisen und
  BTLx-Export), aber an dessen Lebenszyklus gekoppelt.
- **Subtypen** (`sealed`, eigene Glossareinträge — Status pro Eintrag):
  - **Kerve** (`kerve`): zweiflächige Auskerbung am Sparren für
    die Auflagerung auf einer Pfette. **Phase 2, parallel zu
    diesem Eintrag definiert.**
  - **Bohrung** (`bohrung`, Folgearbeit): zylindrische Subtraktion;
    Trigger: Sparren-Schraubenanschluss erforderlich.
  - **Versatz** (`versatz`, Folgearbeit): Stirn-, Fersen- oder
    doppelter Versatz am Sparrenfuß / Strebenfuß; Trigger:
    Sparrenfuß auf liegendem Stuhl.
  - **Zapfenloch** (`zapfenloch`, Folgearbeit): rechteckige
    Subtraktion zur Aufnahme eines Zapfens; Trigger: Stuhlsäulen-
    Pfetten-Anschluss.
  - **Schlitz** (`schlitz`, Folgearbeit): längliche Subtraktion zur
    Aufnahme eines Schlitzblechs oder einer Lasche; Trigger:
    Schlitzblech-Verbinder.
  - **Blatt** (`blatt`, Folgearbeit): halbe Holzdicke abtragend
    (Halbblatt, Schwalbenschwanz-Blatt, Hakenblatt); Trigger:
    Pfettenstoß.
  - **Kamm** (`kamm`, Folgearbeit): einseitige Materialwegnahme
    am übergreifenden Holz; Trigger: Sparren-Mittelpfette.
  - **Anschnitt** (`anschnitt`, Folgearbeit): planare Stirn- oder
    Schrägfläche am Bauteilende; Trigger: First-Anschluss zweier
    Sparren.
  - **Fase** (`fase`, Folgearbeit): kleinflächige
    Kantenabschrägung; Trigger: Sichtholz-Optik.
- **Bestandteile (partitiv) einer Bearbeitung**:
  - **UUID** (`uuid`): technische Identität, Pflicht.
  - **Typ**: Bearbeitungstyp aus 𝓣, Pflicht.
  - **Parameter**: typspezifisches Parametertupel, Pflicht.
  - **Lokale Platzierung** (`lokales_koordinatensystem`): SE(3),
    Pflicht.
  - **Bezeichnung**: freier Anzeigename, optional.
  - **Keine Backref auf das Bauteil**: das zugehörige Bauteil
    ist über die partitive Komposition (Container-Beziehung)
    bestimmt, nicht über ein Feld am Bearbeitungs-Objekt.
    Auflösung Bearbeitung-UUID → Bauteil ist Repository-/Index-
    Aufgabe (siehe Implementierungshinweis).
- **Verwendung**:
  - Bestandteil eines **Bauteils** (`bauteil`): das Bauteil führt
    eine geordnete oder ungeordnete Liste von Bearbeitungs-UUIDs
    (partitive Komposition; das Bauteil ist Eigentümer). Bei
    Löschung des Bauteils werden alle zugehörigen Bearbeitungen
    kaskadierend gelöscht.
  - Bezugnahme aus **Tragwerk** / **Verbindung** / **Bauteil-
    Aggregat**: Bearbeitungen erscheinen dort indirekt über das
    zugehörige Bauteil; eigene FK aus Aggregaten auf
    Bearbeitungen sind nicht vorgesehen (die Bearbeitung
    „gehört" dem Bauteil, nicht dem Aggregat).
- **Abgrenzung**:
  - **Verbindungsmittel** (`verbindungsmittel`): überträgt
    Kräfte zwischen ≥ 2 Bauteilen, **additiv** angefügt
    (Schraube, Nagel, Bolzen, Stabdübel, Klammer, Holzdübel,
    Klebung). Eine Bohrung als Konsequenz eines Verbindungs-
    mittels wird **nicht** als eigene Bearbeitung modelliert;
    die Bohrung ergibt sich abgeleitet im BTLx-Export aus dem
    Verbindungsmittel (siehe `hg_verbindungsmittel.md`, Edge Case).
  - **Verbinder** (`verbinder`): vermittelt zwischen Bauteilen
    (Balkenschuh, Winkel, Knotenblech, Schlitzblech), **additiv**
    angeschraubt/genagelt. Ein durch einen Verbinder verursachter
    Schlitz oder eine Bohrung ist eine **eigene Bearbeitung am
    Bauteil**, weil sie unabhängig vom Verbinder geometrisch
    realisiert wird und ohne Verbinder geometrisch fortbesteht.
  - **Verstärkungselement** (`verstaerkungselement`): axial
    eingedrehte Schraube (Querzug-/Querdruck-/Schubverstärkung),
    **additiv**. Die zugehörige Vorbohrung ist eine abgeleitete
    Konsequenz, keine eigenständige Bearbeitung.
  - **Element** (`element`): abstrakter Oberbegriff der vier
    additiven Element-Subklassen. Bearbeitung ist **keine**
    Element-Subklasse (siehe Erläuterung).
  - **Verbindung** (`verbindung`): Aggregat aus Bauteilen +
    Verbindungsmitteln (+ Verbindern + Verstärkungen) an einem
    Knotenpunkt. Eine Verbindung enthält **keine** Bearbeitungen
    direkt; Bearbeitungen sind Eigenschaften ihrer Bauteile.
  - **Bauteil** (`bauteil`): das Tragobjekt, auf das die
    Bearbeitung wirkt. Bearbeitung ist kein Bauteil, sondern
    ein Merkmal davon.
  - **Querschnitt** (`querschnitt`): die Querschnittsfläche eines
    Bauteils im ungeschwächten Zustand. Eine Bearbeitung
    schwächt den Querschnitt lokal; der Bezugs-Querschnitt
    bleibt unverändert.
  - **Polyeder** (`polyeder`): die geometrische Repräsentation
    des Werkzeugkörpers K_τ(p_τ). Polyeder ist Repräsentations-
    baustein, keine Bearbeitung.
  - **Lokales Koordinatensystem**
    (`lokales_koordinatensystem`): Bezugssystem für die
    Platzierung der Bearbeitung relativ zum Bauteil. Keine
    Bearbeitung an sich.

## Implementierungshinweis

Datentyp (Domänen-Schicht, Kotlin, Schicht
`domain.bauteil.bearbeitung`):

```kotlin
package domain.bauteil.bearbeitung

import domain.bauteil.Bauteil
import domain.geometrie.LokalePlatzierung
import java.util.UUID

/**
 * Bearbeitungstyp. Sealed; konkrete Subtypen tragen ihre
 * typspezifischen Parameter selbst.
 *
 * Glossar: hg_bearbeitung.md (sealed `typ`-Aufzählung 𝓣).
 *
 * Phase 2: nur `Kerve` implementiert. Weitere Subtypen folgen
 * trigger-basiert (siehe quellenkonflikt-Block der Glossardatei).
 */
sealed interface Bearbeitung {
    /** Technischer Surrogatschlüssel der Bearbeitung. RFC 9562 v7. */
    val uuid: UUID

    /** Starrkörpertransformation Werkzeug-Bezugssystem → Bauteil-Lokal.
     *  Siehe `hg_lokales_koordinatensystem.md`. */
    val lokalePlatzierung: LokalePlatzierung

    /** Optionaler Anzeigename. */
    val bezeichnung: String?

    // Bewusst ohne Backref auf das Bauteil: die Beziehung
    // Bearbeitung → Bauteil ist partitive Komposition; das
    // Bauteil hält seine Bearbeitungen als geordnete Liste.
    // Die Auflösung Bearbeitungs-UUID → Bauteil ist Aufgabe der
    // Repository-/Index-Schicht (siehe Implementierungshinweis
    // hg_bearbeitung.md), nicht der Domänen-Datenklasse.
}
```

- **Einheit**: Längen in mm (Double); Winkel intern in Radiant;
  Lokale Platzierung als SE(3)-Element (Rotation + Translation).
- **Identität**: `uuid` ist Pflicht und persistent (RFC 9562 v7),
  unabhängig vom zugeordneten Bauteil. Damit kann eine Bearbeitung
  über ihren Lebenszyklus identifiziert, ge-tracked und in der
  CNC-Werkzeugliste referenziert werden, auch wenn sie
  nachträglich verändert wird.
- **Keine Backref auf das Bauteil**: Die Domänen-Datenklasse
  führt **kein** Feld `bauteilUuid`. Die Beziehung Bearbeitung →
  Bauteil ist partitive Komposition; das Bauteil hält seine
  Bearbeitungen als geordnete Liste, und damit ist die
  Container-Beziehung selbst die Zuordnung. Eine Backref wäre
  redundante Information und würde eine zusätzliche
  Konsistenz-Invariante erzwingen (Backref muss zum enthaltenden
  Bauteil passen).
- **Repository-Auflösung Bearbeitung → Bauteil**: Wird die
  Auflösung „zu welchem Bauteil gehört diese Bearbeitungs-UUID?"
  benötigt (etwa für CNC-Werkzeuglisten oder Bemessungs-
  Nachweise), erfolgt sie über einen Repository-Lookup
  (`BauteilRepository.findeBauteilZuBearbeitung(bearbeitungsUuid)`),
  der den Modell-Container nach dem Bauteil durchsucht, dessen
  Bearbeitungs-Liste die UUID enthält. Diese Verantwortung liegt
  in der Persistenz-/Index-Schicht, **nicht** in der
  Domänen-Datenklasse `Bearbeitung`.
- **Lebenszyklus / Komposition**: Die Bearbeitung ist im Sinne
  der **partitiven Komposition** Eigentum des Bauteils und
  **kein eigenständiges Aggregat**. Wird das Bauteil aus dem
  Modell entfernt, werden alle zugehörigen Bearbeitungen
  strukturell mitentfernt (sie sind Bestandteile der
  Bauteil-Liste). Die Bearbeitung kann **nicht** ohne Bauteil
  existieren.
- **Pflicht- und Optionalfelder (normativ)**:
  - `uuid` — Pflicht, niemals null.
  - `lokalePlatzierung` — Pflicht; mindestens `LokalePlatzierung.
    IDENTITAET` zulässig (Werkzeug-Bezugssystem ≡ Bauteil-Lokal).
  - `bezeichnung` — `null` zulässig.
  - Typspezifische Parameter — Pflicht, im jeweiligen Subtyp
    deklariert (z. B. `Kerve.kervtiefe`, `Kerve.kervbreite`).
  - **Kein** `bauteilUuid`-Feld; die Bauteil-Zugehörigkeit ist
    die Container-Beziehung in der Bearbeitungs-Liste des
    Bauteils.
- **Invarianten** (in Fabrikfunktionen / `init` der Subtypen
  prüfen, bei Verletzung `Resultat.Fehler` bzw. `Entartet`-
  Variante; niemals Exception werfen):
  1. Typspezifische Parameter-Invarianten (siehe Subtyp-Eintrag).
  2. Plausibilitätsregeln zur Querschnittsschwächung (typabhängig,
     **weiche** Invariante; Verstoß → Warnung in der Bemessungs-
     Schicht, **kein** Validierungsfehler).
- **Berechnung der bearbeiteten Bauteilgeometrie**: G_B^bearbeitet
  nach Gleichung (2) wird **nicht eager** berechnet, sondern
  **lazy on demand** in der Geometrie-Schicht (Phase 3.2). Die
  Domänen-Schicht hält ausschließlich die ungeschwächte
  Bauteilgeometrie und die Liste der Bearbeitungen; die Boole'sche
  Differenz ist Aufgabe einer eigenen Komponente
  `domain.bauteil.geometrie.BearbeitungsAggregator`
  (Folgearbeit).
- **BTLx-Export** (Persistenzschicht, Phase 4):
  - Jede Bearbeitung wird in das passende BTLx-Processing
    am betroffenen Bauteil-Part übersetzt (siehe Tabelle in
    Erläuterung). Die Bearbeitungs-UUID erscheint nicht direkt
    im BTLx-Schema, kann aber als Bearbeitungs-Bezeichnung
    geführt werden, wenn der CNC-Workflow das benötigt.
- **IFC-Export** (Persistenzschicht, Phase 4):
  - Jede Bearbeitung wird als `IfcOpeningElement` mit eigener
    `GlobalId` (= Bearbeitungs-UUID, Base64-kodiert nach
    ISO/IEC 9834-8) angelegt; die Beziehung zum Bauteil läuft
    über `IfcRelVoidsElement`.
- **Edge Cases**:
  - **Bearbeitung ohne Bauteilbezug**: strukturell ausgeschlossen.
    Eine Bearbeitung existiert ausschließlich als Element der
    Bearbeitungs-Liste eines Bauteils; eine freistehende
    Bearbeitungs-Instanz hat keinen modellseitigen Zustand.
    Konstruktion erfolgt über `Bauteil.fuegeBearbeitungHinzu(…)`,
    nicht über einen freien Bearbeitungs-Konstruktor mit
    Bauteil-Referenz.
  - **Bearbeitungs-Werkzeugkörper vollständig oder teilweise
    außerhalb des Bauteils** (T_F( K_τ(p_τ) ) ⊄ G_B^lokal, also
    insbesondere die Fälle T_F( K_τ(p_τ) ) ∩ G_B^lokal = ∅
    *und* T_F( K_τ(p_τ) ) \ G_B^lokal ≠ ∅): geometrisch wäre die
    Boole'sche Differenz wohldefiniert, aber das Ergebnis hätte
    keinen sinnvollen Modellzustand (eine ins Leere zeigende
    Bearbeitung wäre für BTLx-/IFC-Export unsauber und kann
    keinen formschlüssigen Geometrie-Beitrag mehr leisten).
    Beide Fälle werden auf Glossar-Subtyp-Ebene gleich hart
    behandelt: das Anhängen einer solchen Bearbeitung an das
    Bauteil ist Validierungsfehler und schlägt mit einer subtyp-
    spezifischen Variante von `BearbeitungAmBauteilUngueltig`
    fehl (für die Kerve: `KervePositionAusserhalbBauteil`, siehe
    `hg_kerve.md`). Eine reine Warnung an dieser Stelle ist nicht
    vorgesehen, weil Modellkonsistenz vor nachträglicher
    Reparatur-Toleranz steht. Subtyp-Einträge dürfen diese
    Default-Härte nicht aufweichen.
  - **Mehrere überlappende Bearbeitungen**: zulässig (z. B. Kerve
    und Bohrung am selben Bereich); die Reihenfolge der
    Vereinigung in (2) ist semantisch egal.
  - **Bearbeitung an einem isotropen Plattenwerkstoff**: zulässig
    (z. B. Bohrung in Spanplatte); die Faserrichtungs-
    Plausibilitätswarnung greift dann nicht.
- **Abgeleitete Eigenschaften** (als Funktionen, keine Felder;
  Implementierung in der Geometrie-Schicht / Bemessungs-Schicht):
  - `werkzeugkoerper(): Polyeder` — K_τ(p_τ) im typeigenen
    Bezugssystem; subtypspezifische Implementierung.
  - `werkzeugkoerperInBauteilLokal(): Polyeder` —
    T_F( K_τ(p_τ) ); generisch über Polyeder-Transformation.
  - `wirkungAuf(b: Bauteil): Polyeder` — G_B^lokal \
    werkzeugkoerperInBauteilLokal(); Geometrie-Schicht.
  - `querschnittsschwaechung(b: Bauteil, s: Double): Double` —
    Anteil der bei Längsparameter s entfernten
    Querschnittsfläche; Bemessungs-Schicht (EC5 5.2 / SIA 265
    4.6).
- **Bezeichner-Konvention** (CLAUDE.md): Domänen-Klasse heißt
  `Bearbeitung` (deutsch, Glossarbegriff); Subtypen heißen
  `Kerve`, `Bohrung`, `Versatz`, `Zapfenloch`, `Schlitz`,
  `Blatt`, `Kamm`, `Anschnitt`, `Fase`. Der Aggregator heißt
  technisch englisch (`BearbeitungsAggregator`), weil er kein
  Glossarbegriff ist.

## Quellen

**Primär (normativ):**

- design2machine: *BTLx interface description*, Version 2.1,
  16.11.2023 (Stand BTLx_2_1_0.xsd).
- ISO 16739-1:2024, „Industry Foundation Classes (IFC) for data
  sharing in the construction and facility management industries
  — Part 1: Data schema" (`IfcOpeningElement`,
  `IfcFeatureElementSubtraction`, `IfcRelVoidsElement`).
- DIN EN 1995-1-1:2010-12, „Eurocode 5: Bemessung und Konstruktion
  von Holzbauten – Teil 1-1", Abschnitt 5.2 und Abschnitt 6.5.
- DIN EN 14081-1:2019-10, „Holzbauwerke – Nach Festigkeit
  sortiertes Bauholz mit rechteckigem Querschnitt – Teil 1".
- SIA 265:2021, „Holzbau", Schweizerischer Ingenieur- und
  Architektenverein, Zürich, Abschnitt 4.6 und Abschnitt 5.

**Sekundär:**

- Mönck, W.; Rug, W.: *Holzbau – Bemessung und Konstruktion.*
  16. Auflage, Beuth, Berlin 2015.
- Gerner, M.: *Fachwerk – Instandsetzung, Sanierung, Neubau.*
  DVA, 7. Auflage 2007.
- Natterer, J.; Herzog, T.; Volz, M.: *Holzbau-Atlas.* 4. Auflage,
  Birkhäuser, Basel 2003.
- Kloepfer, H.: *Holzschutz nach DIN 68800 — bauliche Maßnahmen.*
  Kloepfer 2014.

**Korpus (nicht autoritativ):**

- cadwork informatik: Dokumentation „Bearbeitung am Bauteil"
  (Standard-Bearbeitungstypen) — Korpus.
- Holzbau Deutschland, Merkblatt „Begriffe und Klassifizierungen
  für den Holzbau" (abgerufen 2026-05-09).
- Wikipedia, Lemma „Holzverbindung" (abgerufen 2026-05-09).
