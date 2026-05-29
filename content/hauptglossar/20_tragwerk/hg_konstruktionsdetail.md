---
id: konstruktionsdetail
benennung: Konstruktionsdetail
synonyme: [Detail, Anschlussdetail, Knotendetail]
abgelehnte_benennungen:
  - Knoten
  - Konstruktionsknoten
  - Detailpunkt
  - Detailzeichnung
  - Werkplandetail
  - "connection detail"
  - "construction detail"
  - "joint detail"
  - "node detail"
oberbegriff: null
begriffstyp: aggregat
voraussetzungen:
  - bauteil
  - verbindung
  - auflager
  - bearbeitung
  - verbindungsmittel
  - verbinder
  - uuid
  - punkt
  - weltkoordinatensystem
  - toleranzen
abgrenzung_zu:
  - verbindung
  - auflager
  - bauteilgruppe
  - kerve
  - bearbeitung
  - tragwerk
  - bauteil
  - bauwerk
status: entwurf
subglossar_pendant: notwendig
quellen_primär:
  - "ISO 16739-1:2024 'Industry Foundation Classes (IFC) – Part 1: Data schema' (IFC 4.3.2.0): `IfcGroup` (Subtyp von `IfcObjectDefinition`) mit `IfcRelAggregates`/`IfcRelAssignsToGroup` als nicht-exklusiver Aggregations-Beziehung; `IfcElementAssembly` (Subtyp von `IfcElement`) als Element-Komposit-Pendant. Pendant für die App-Lesart II (Sach-Aggregat über Bauteilen, Verbindungen, Auflagern und Bearbeitungen mit eigener Identität)."
  - "DIN 1356-1:2024-04, 'Bauzeichnungen — Teil 1: Grundregeln der Darstellung' [einsicht: snippet, baunormenlexikon.de / DIN Media]. Trägt 'Detailzeichnung' als Zeichnungstyp/Maßstabsklasse (1:20, 1:10, 1:5, 1:1), nicht 'Konstruktionsdetail' als Sach-Begriff. Begrifflich nur Plan-Artefakt-Lesart (Lesart I)."
  - "DIN EN 1995-1-1:2010-12 (Eurocode 5), Abschnitt 1.5 (Begriffe). Der Begriff 'Konstruktionsdetail' ist nicht definiert; die EC5-Sicht auf einen Knoten ist die der Verbindung (Kap. 8 'Anschlüsse mit metallischen Verbindungsmitteln')."
  - "SIA 265:2021 'Holzbau', Abschnitt 5 'Konstruktive Durchbildung'. Der Begriff 'Konstruktive Durchbildung' deckt das Themenfeld inhaltlich ab, ohne eine geschlossene Begriffs-Definition von 'Konstruktionsdetail' zu geben."
  - "DIN 1052:2008-12, Abschnitt 3 'Begriffe'. Kein definitorischer Eintrag zu 'Konstruktionsdetail'."
quellen_sekundär:
  - "Holzbau-Handbuch, Reihe 1, Teil 7, Folge 2 'Anschlüsse im Hallenbau', Informationsdienst Holz. Verwendet 'Anschluss' und 'Detail' praktisch synonym als Sach-Gegenstand (Knoten mit beteiligten Bauteilen, Bearbeitungen, Verbindungsmitteln)."
  - "Mönck, W.; Rug, W.: Holzbau – Bemessung und Konstruktion. 16. Aufl., Beuth, Berlin 2015, Kap. 11 'Dachtragwerke'. Sparrenfußdetail, Firstdetail, Pfettenstoßdetail als praxis-übliche Werkplan-Bezeichnungen."
  - "Natterer, J.; Herzog, T.; Volz, M.: Holzbau-Atlas. 4. Aufl., Birkhäuser, Basel 2003, Kap. 'Anschlüsse'."
  - "Blass, H. J.; Sandhaas, C.: Ingenieurholzbau – Grundlagen der Bemessung. KIT Scientific Publishing, Karlsruhe 2016, Kap. 8 'Verbindungen'."
  - "Holzbau Deutschland-Institut: 'Regeldetailkatalog — Planungshilfen für Außenwandbekleidungen aus Holz'. Korpus-Lesart III (Detail als Katalog-Eintrag)."
  - "Lignum: 'Bauteilkatalog' (Brandschutz, Schallschutz). Korpus-Lesart III."
  - "KLH-Detailkatalog (Brettsperrholz, CAD-Detailkatalog 2020)."
  - "Recherche-Bericht `docs/recherche/2026-05-14_hg_konstruktionsdetail.md`."
quellenkonflikt: |
  **Normlücke.** Keine der konsultierten deutschsprachigen Bau- und
  Holzbau-Normen — DIN 1356-1:2024-04, DIN EN 1995-1-1:2010-12,
  SIA 265:2021, DIN 1052:2008-12, DIN EN 1990:2010-12 — enthält eine
  geschlossene Begriffs-Definition von „Konstruktionsdetail". DIN 1356-1
  führt „Detailzeichnung" ausschließlich als **Zeichnungstyp** /
  **Maßstabsklasse** (1:20 bis 1:1) und nicht als Sach-Begriff für die
  abgebildete Konstruktion. EC5 und SIA 265 verwenden „Anschluss",
  „Verbindung" und „Konstruktive Durchbildung", nicht
  „Konstruktionsdetail" als Lemma. Analog zur Lage bei `hg_auflager.md`
  und `hg_statisches_system.md` ist hier eine **App-Festlegung**
  erforderlich.

  **Drei Korpus-Lesarten.** Die Sichtung des DACH-Holzbau-Korpus zeigt,
  dass „Konstruktionsdetail" unmarkiert in drei nicht-disjunkten Lesarten
  verwendet wird:

  | Lesart | Trägt | Ist | Beispiel |
  |---|---|---|---|
  | I — Plan-Artefakt | Plan-Status | Zeichnungs-/Maßstabsklasse | Blatt 7 „Sparrenfußdetail M 1:5" als Werkzeichnung |
  | II — Sach-Aggregat | Sach-Status | mehrere Bauteile + Verbindungen + Auflager + Bearbeitungen in lokaler Nachbarschaft am gemeinsamen Knotenpunkt | das modellierte Konvolut Sparren+Pfette+Kerve+Schrägschrauben+Auflager am Sparrenfuß |
  | III — Katalog-Typ | Typ-Status | wiederverwendbare Detail-Vorlage mit fester Maßkette und Ausführungsregeln | Regeldetail-Eintrag „Sparrenfuß auf Mauerlatte, Variante a" |

  Lesart I deckt DIN 1356-1 ab (Plan-Schicht, Darstellungsregeln).
  Lesart II ist die ontologische Sicht der Werkplan-Erzeugung und der
  CAD-Praxis (Cadwork, Dietrich's, SEMA: „Detail" als Ausschnitts-Sicht
  mit beteiligten Bauteilen und Bearbeitungen). Lesart III liegt
  Detail-Katalogen (Holzbau Deutschland-Institut Regeldetailkatalog,
  Lignum Bauteilkatalog, KLH-Detailkatalog) zugrunde.

  **App-Wahl: Lesart II.** Dieser Glossareintrag definiert
  „Konstruktionsdetail" in der **Sach-Aggregat-Lesart** — als
  ontologische Sicht auf einen lokal abgegrenzten Bereich der
  Tragwerks-Realität, die Bauteile, Verbindungen, Auflager und
  Bearbeitungen am gemeinsamen Knotenpunkt zur plan- und
  werkstattorientierten Repräsentation bündelt. Lesart I
  (Detailzeichnung) wird als **abgelehnte Benennung** geführt
  (Plan-Artefakt, eigene Schicht der Visualisierungs-/Plan-Erzeugung).
  Lesart III (Detail-Katalog-Eintrag) ist als **Folgearbeit** auf
  Wieder-Verwendung von Konstruktionsdetail-Instanzen vorgesehen
  (Detail-Katalog-Funktion), aber kein Gegenstand dieses Eintrags.

  **App-Synthese transparent.** Keine der konsultierten Quellen
  formuliert die Bündelung „Auflager + Verbindung + Bearbeitungen +
  beteiligte Bauteile am gemeinsamen Knotenpunkt" als eigenständigen
  Sach-Begriff explizit. Das Holzbau-Handbuch Reihe 1 Teil 7 Folge 2
  verwendet „Anschluss" und „Detail" praktisch synonym, ohne die drei
  Sichten Bemessung/Tragwerk/Werkplan auseinanderzufassen. Die
  App-Festlegung ist **mit allen konsultierten Quellen konsistent**,
  aber **nicht durch sie erzwungen**: sie ist eine **Eigenleistung**.
  Eine andere App hätte die Drei-Sichten-Trennung anders bestimmen
  können (etwa Konstruktionsdetail = nur Plan-Artefakt; das
  Sach-Aggregat hätte dann einen anderen Namen). Die hier gewählte
  Auswahl ist **vertretbar**, nicht **alternativlos**.

  **Drei-Sichten-Bild am gemeinsamen Knotenpunkt.** Am physischen
  Sparrenfuß-auf-Pfette-Punkt koexistieren drei App-Aggregate als
  unterschiedliche Sichten desselben Knotens:

  - **Verbindung** (`hg_verbindung.md`): die **Bemessungs-Sicht**
    (EC5 Kap. 8, SIA 265 Anhang A) — Tupel aus beteiligten Bauteilen,
    Verbindungsmitteln, Verbindern, Verstärkungen und
    Nachweisverfahren.
  - **Auflager** (`hg_auflager.md`): die **Tragwerks-Sicht** (EC5
    Kap. 5, SIA 260) — Tupel aus geometrischer Manifestation und
    mechanischer Wertigkeit, das ein Bauteil mit Baugrund oder
    weiterem tragenden Bauteil verknüpft.
  - **Konstruktionsdetail** (dieser Eintrag): die
    **Werkplan-/Werkstatt-Sicht** — Aggregat über einer
    Ausschnittsregion am Knotenpunkt, das die dort beteiligten
    Bauteile, Verbindungen, Auflager und Bearbeitungen für die
    plan- und werkstatt-orientierte Repräsentation bündelt.

  Die drei Sichten überlappen geometrisch (dieselbe Bauteil-Schar am
  selben Punkt) und sind dennoch **nicht** synonym: sie tragen
  unterschiedliche Mengen, unterschiedliche Konsistenzbedingungen
  und werden in unterschiedlichen Bemessungs- und Plan-Schichten
  benutzt. Ein Konstruktionsdetail kann ohne Auflager-Bezug auftreten
  (z. B. Pfettenstoßdetail im freien Feld eines durchlaufenden
  Trägers — dort gibt es eine Verbindung, aber kein Auflager); die
  Bündelung „Auflager + Verbindung + Bearbeitungen" ist daher
  **konjunktiv möglich**, nicht **konstitutiv pflichtig**.

  **Ausschnittsfreiheit.** Die räumliche Begrenzung eines
  Konstruktionsdetails — welche Bauteile einbezogen sind, wie weit die
  Ausschnittsregion reicht — ist **Plan-/Modellierungs-Entscheidung**,
  nicht **Sach-Eigenschaft** der Konstruktion. Ein „Sparrenfußdetail"
  kann den Sparren + die Pfette + die Aufschiebung + das Traufgesims
  umfassen — oder nur Sparren + Pfette mit Verbindungsmittel. Die
  Definition trägt diese Freiheit explizit über die Ausschnittsregion
  R als eigene Komponente des Aggregat-Tupels (statt sie versteckt
  über die Mitgliedsmengen zu führen).

  **Begriffstyp `aggregat`.** Eindeutig, analog zu `verbindung`,
  `auflager`, `tragwerk`, `bauteilgruppe`:

  - Komposition mehrerer eigenständiger Begriffe (Bauteile,
    Verbindungen, Auflager, Bearbeitungen).
  - Eigene UUID für Werkplan-Adressierung und mögliche Wieder-
    Verwendung als Katalog-Eintrag (Lesart III als Folgearbeit).
  - Eigene Konsistenzbedingungen über der Komposition
    (Inzidenz mit der Ausschnittsregion, Nicht-Leere am
    Knotenpunkt, Konsistenz mit dem Träger-Tragwerk).

  `begriffstyp: relation` wäre falsch, weil ein Konstruktionsdetail
  mehr trägt als eine reine Mitgliedschafts-Sicht: es führt eine
  räumliche Ausschnittsregion mit eigener Geometrie. `begriffstyp:
  partitiv` wäre falsch, weil das Konstruktionsdetail nicht
  lebenszyklus-gekoppelt an genau einen Träger ist; es lebt als
  eigenständiger Knoten-Repräsentant mit eigener UUID. **Anders als
  `bauteilgruppe`** ist die Mitgliedschaft am Konstruktionsdetail
  **nicht-exklusiv**: derselbe Sparren ist typisch in mehreren
  Details sichtbar (Sparrenfußdetail + Mittelpfettendetail +
  Firstdetail).

  **IFC-Mapping.** Default ist `IfcGroup` mit `IfcRelAggregates`
  (analog `hg_verbindung.md`-Festlegung). `IfcElementAssembly` ist
  nur **teilweise** passend: es ist als `IfcElement` (verbautes
  Objekt) typisiert, ein Konstruktionsdetail ist aber keine
  eigenständig verbaute Sache, sondern eine Sicht auf bereits
  verbaute Bauteile; zusätzlich impliziert
  `IsDecomposedBy`/`IfcRelAggregates` an `IfcElementAssembly`
  exklusive Bestandteils-Eigentümerschaft, was der nicht-exklusiven
  Mitgliedschaft am Konstruktionsdetail widerspricht. Die App führt
  Konstruktionsdetails daher als `IfcGroup`-Pendant.

  **Werkplan-Bezeichnungs-Grammatik.** Im DACH-Holzbau-Korpus
  („Sparrenfußdetail", „Firstdetail", „Pfettenstoßdetail",
  „Traufdetail", „Ortgangdetail", „Eckdetail", „Sockeldetail")
  folgt die berufssprachliche Benennung der impliziten Grammatik

  ```
  [Bauteilrolle]<Anschluss-Topologie>-Detail
  ```

  mit `<Anschluss-Topologie>` ∈ {Fuß, Kopf, Stoß, Anschluss, First,
  Trauf, Ortgang, Ecke, Sockel, ⊥}. Diese Grammatik ist **nicht
  normativ** (kein Norm-Lemma kodifiziert sie), aber im Korpus
  konsistent. Sie wird im Erläuterungs-Block als Empfehlung geführt
  und für die spätere Detail-Adressierung im Werkplan-Modul
  vorgesehen.

  **BTLx.** Das design2machine-Schema BTLx kennt **keine eigene
  Detail-Entität**; ein Konstruktionsdetail manifestiert sich dort
  implizit über die beteiligten Parts und Processings am selben
  Knotenpunkt — analog zur Verbindung und zum Auflager (siehe
  `hg_verbindung.md`-Quellenkonflikt und `hg_auflager.md`-Quellen-
  konflikt). IFC 4.3 ist der einzige Industriestandard mit
  brauchbarem Aggregat-Pendant (`IfcGroup`).

  **Synonyme und abgelehnte Benennungen.** „Detail",
  „Anschlussdetail", „Knotendetail" sind im DACH-Holzbau-Korpus
  belegt und werden als Synonyme geführt. „Knoten" (allein) wird
  abgelehnt, weil es bereits in `hg_verbindung.md` als
  Verbindungs-Synonym reserviert ist (siehe dort `synonyme:` Z. 4)
  und zudem in der Statik-Lehrbuch-Sprache den Punkt-Stab-Knoten
  (`hg_statisches_system.md` K-Komponente) bezeichnet — die
  dreifache Belegung ist nicht zulässig. Der zusammengesetzte
  Begriff **„Knotenpunkt"** dagegen bleibt zulässig und benennt
  hier die geometrische Bezugsstelle (Punkt im W-Raum) innerhalb
  des Konstruktionsdetails; die Wort-Asymmetrie ist bewusst:
  „Knoten" allein ist mehrdeutig und wird vermieden, „Knotenpunkt"
  als zusammengesetzter Begriff trägt seine Bedeutung im Wortstamm.
  „Konstruktionsknoten" hat keine Korpus-Verankerung (Anglizismus-
  Verdacht). „Detailpunkt" bezeichnet im DIN 1356-1-Kontext den
  Plan-Marker (Detail-Kreis im Übersichtsplan), nicht den
  Sach-Gegenstand. „Detailzeichnung" ist Lesart I (Plan-Artefakt),
  nicht die hier gewählte Lesart II. „Werkplandetail" wird zu eng
  auf den Werkplan-Kontext geführt; das Konstruktionsdetail existiert
  auch in Bemessungs- und Ausführungs-Plänen. Englische Pendants
  („connection detail", „construction detail", „joint detail",
  „node detail") sind in der Hauptdefinition nicht zulässig
  (CLAUDE.md, Architektur-Verbote).
---

## Prosa-Definition

Ein **Konstruktionsdetail** ist ein Aggregat aus einer räumlich
abgegrenzten Ausschnittsregion an einem Knotenpunkt eines Tragwerks
und den in dieser Region inzidenten Bauteilen, Verbindungen,
Auflagern und Bearbeitungen, das eine eigene technische Identität
trägt und die plan- und werkstattorientierte Repräsentation des
Knotenpunkts bündelt, ohne selbst eine verbaute Sache, eine
Bemessungs-Einheit oder eine Stützungs-Idealisierung zu sein.

## Mathematische Definition

Sei

- W das Weltkoordinatensystem (siehe `hg_weltkoordinatensystem.md`),
- 𝒰 der UUID-Raum nach `hg_uuid.md`,
- 𝓑 die Menge der Bauteile nach `hg_bauteil.md`,
- 𝓥 die Menge der Verbindungen nach `hg_verbindung.md`,
- 𝓐 die Menge der Auflager nach `hg_auflager.md`,
- 𝓟 die Menge der Bearbeitungen nach `hg_bearbeitung.md`,
- 𝓡 die Menge der **Ausschnittsregionen** in W: nicht-leere,
  beschränkte, einfach zusammenhängende Teilmengen R ⊂ ℝ³ mit
  endlichem Volumen, repräsentiert durch einen achsenparallelen
  Hüllquader, einen orientierten Hüllquader oder ein allgemeines
  Polyeder (konkrete Repräsentation Folgearbeit; im aktuellen
  Glossarstand reicht „beschränkter Bereich um den Knotenpunkt"),
- p ∈ ℝ³ ein **Knoten-Bezugspunkt** in W (optional, Anker der
  Ausschnittsregion).

Dann ist ein **Konstruktionsdetail** das Tupel

```
K := (uuid, ausschnitt, knotenpunkt, beteiligte_bauteile,
      beteiligte_verbindungen, beteiligte_auflager,
      beteiligte_bearbeitungen, traegertragwerk, bezeichnung)
```

mit den Komponenten

- **uuid** ∈ 𝒰: technische Identität des Konstruktionsdetails als
  Aggregat,
- **ausschnitt** ∈ 𝓡: räumliche Ausschnittsregion in W,
- **knotenpunkt** ∈ ℝ³ ∪ {⊥}: optionaler Knoten-Bezugspunkt in W
  (typisch geometrischer Schwerpunkt der Bauteil-Treffen in der
  Region),
- **beteiligte_bauteile** ⊂ 𝒰: UUIDs der in `ausschnitt` inzidenten
  Bauteile, |beteiligte_bauteile| ≥ 1,
- **beteiligte_verbindungen** ⊂ 𝒰: UUIDs der in `ausschnitt`
  inzidenten Verbindungen, |beteiligte_verbindungen| ≥ 0,
- **beteiligte_auflager** ⊂ 𝒰: UUIDs der in `ausschnitt` inzidenten
  Auflager, |beteiligte_auflager| ≥ 0,
- **beteiligte_bearbeitungen** ⊂ 𝒰: UUIDs der an den beteiligten
  Bauteilen sitzenden Bearbeitungen, deren geometrische Manifestation
  in `ausschnitt` liegt, |beteiligte_bearbeitungen| ≥ 0,
- **traegertragwerk** ∈ 𝒰: UUID des Tragwerks, auf dem das
  Konstruktionsdetail eine Sicht bildet (siehe `hg_tragwerk.md`),
- **bezeichnung** ∈ String ∪ {⊥}: optionaler Anzeigename, idealerweise
  nach der Grammatik `[Bauteilrolle]<Anschluss-Topologie>-Detail`
  (Erläuterungs-Block).

### Konsistenzbedingungen

(K1) **Nicht-Leere am Knotenpunkt**:
|beteiligte_bauteile| ≥ 1, und falls
|beteiligte_bauteile| = 1 gilt zusätzlich
|beteiligte_verbindungen| + |beteiligte_auflager| +
|beteiligte_bearbeitungen| ≥ 1. Ein Konstruktionsdetail, das **nur**
ein Bauteil ohne Verbindung, Auflager oder Bearbeitung zeigt, hat
keinen plan- oder werkstattrelevanten Inhalt und ist unzulässig.

(K2) **Inzidenz mit der Ausschnittsregion**:

- Für jedes b ∈ beteiligte_bauteile schneidet die geometrische
  Punktmenge G_W(b) des Bauteils die Ausschnittsregion:
  G_W(b) ∩ ausschnitt ≠ ∅.
- Für jede v ∈ beteiligte_verbindungen gilt: mindestens ein Bauteil
  der Verbindung ist in beteiligte_bauteile enthalten und die
  Knotenposition der Verbindung (oder ein Repräsentationspunkt) liegt
  in `ausschnitt` (Toleranz LAENGE_EPS).
- Für jedes a ∈ beteiligte_auflager gilt: das gestützte Bauteil ist
  in beteiligte_bauteile enthalten und die geometrische Manifestation
  des Auflagers liegt in `ausschnitt` (Toleranz LAENGE_EPS).
- Für jede p ∈ beteiligte_bearbeitungen gilt: das Träger-Bauteil von
  p ist in beteiligte_bauteile enthalten und die geometrische
  Manifestation von p liegt in `ausschnitt`.

(K3) **Tragwerks-Konsistenz**: alle in beteiligte_bauteile,
beteiligte_verbindungen und beteiligte_auflager referenzierten
UUIDs sind Mitglieder bzw. Bestandteile des Tragwerks
`traegertragwerk` im Sinne von `hg_tragwerk.md` (B, V, A).

(K4) **Knotenpunkt-Verträglichkeit**: falls `knotenpunkt` ≠ ⊥, gilt
`knotenpunkt` ∈ ausschnitt (Toleranz LAENGE_EPS).

(K5) **Toleranz-gestützte Identität**: zwei Konstruktionsdetails
k₁ ≠ k₂ am selben Tragwerk dürfen identische Ausschnittsregionen
und identische Mitgliedsmengen tragen nur, wenn sie sich in der
Bezeichnung oder im optionalen Knotenpunkt unterscheiden; eine
triviale Duplizierung (gleiche Region **und** gleiche Mengen **und**
gleicher Knotenpunkt **und** gleiche Bezeichnung) ist unzulässig.

(K6) **Nicht-Exklusivität der Mitgliedschaft** (im Gegensatz zur
Bauteilgruppe): ein Bauteil b ∈ 𝓑 darf in mehreren
Konstruktionsdetails als beteiligtes Bauteil auftreten (typisch
Sparren im Sparrenfußdetail + Mittelpfettendetail + Firstdetail).
Die Mitgliedschaft ist **nicht** Lebenszyklus-bindend; das Entfernen
eines Konstruktionsdetails löscht weder seine Bauteile noch seine
Verbindungen, Auflager oder Bearbeitungen.

## Wohldefiniertheit

- **Existenz.** Für jeden konstruktiv relevanten Knotenpunkt eines
  Tragwerks lässt sich das obige Tupel erfassen. Mindestkonfiguration:
  ein Sparrenfußdetail am Auflager auf der Fußpfette mit
  beteiligte_bauteile = {sparren_uuid, fusspfette_uuid},
  beteiligte_verbindungen = {sparren_pfette_verbindung_uuid},
  beteiligte_auflager = {sparrenfuss_auflager_uuid},
  beteiligte_bearbeitungen = {sparrenfuss_kerve_uuid}, ausschnitt =
  achsenparalleler Hüllquader um den Knoten, knotenpunkt = Schwerpunkt
  der Kerv-Sohle, traegertragwerk = dachtragwerk_uuid.

- **Eindeutigkeit der Identität.** Die UUID des Konstruktionsdetails
  ist unabhängig von den UUIDs seiner Mitglieder und unabhängig vom
  Tragwerk; sie wird einmalig vergeben (RFC 9562 v7) und ist
  persistent. K5 schließt triviale Duplikate aus.

- **Nicht-Exklusivität der Mitgliedschaft (K6).** Im Unterschied zur
  Bauteilgruppe ist das Konstruktionsdetail **keine** partitive
  Komposition mit kaskadischem Lebenszyklus. Mehrere
  Konstruktionsdetails am selben Tragwerk dürfen identische Mitglieder
  haben (typisch: derselbe Sparren erscheint in Sparrenfußdetail,
  Mittelpfettendetail und Firstdetail desselben Sparrendachs). Daraus
  folgt: das Entfernen eines Konstruktionsdetails wirkt nicht auf
  seine Mitglieder; das Entfernen eines Bauteils, das Mitglied eines
  Konstruktionsdetails ist, erfordert vorherige Bereinigung der
  Mitgliedsbeziehung im Detail.

- **Ausschnittsfreiheit als bewusste Modellierungsentscheidung.** Die
  Ausschnittsregion `ausschnitt` ist nicht aus den Mitgliedern
  abgeleitet, sondern eine eigenständige Komponente des Tupels. Damit
  trägt das Konstruktionsdetail die Plan-/Modellierungs-Entscheidung
  „wie weit reicht der Ausschnitt" explizit, statt sie versteckt über
  die Auswahl der Mitglieder zu führen. Konsequenz: zwei
  Konstruktionsdetails am selben Knotenpunkt dürfen sich in
  `ausschnitt` (kleinerer/größerer Hüllquader) unterscheiden und
  unterschiedliche Mitgliedsmengen tragen, ohne dass eine der beiden
  Modellierungen falsch wäre.

- **Wohldefiniertheit der Inzidenz (K2).** Die Inzidenz „G_W(b) ∩
  ausschnitt ≠ ∅" hängt von der geometrischen Repräsentation des
  Bauteil-Polyeders ab; sie ist invariant unter zulässigen
  Repräsentanten-Wahlen (siehe `hg_bauteilkoerper.md`). Die Toleranz
  LAENGE_EPS in K2 fängt den numerischen Randfall ab, in dem ein
  Bauteil die Ausschnittsregions-Grenze tangential berührt.

- **Aggregat, kein Element.** Das Konstruktionsdetail ist **nicht**
  Subtyp von `element` (siehe `hg_element.md`); es ist ein
  Aggregat-Begriff mit eigener UUID, das Sichten auf
  Element-Instanzen bündelt. 𝒦 ∩ 𝓔 = ∅, analog zur Verbindung und
  zum Auflager.

- **Foreign-Key-Regel.** Alle Mitglieds-Felder
  (`beteiligte_bauteile`, `beteiligte_verbindungen`,
  `beteiligte_auflager`, `beteiligte_bearbeitungen`,
  `traegertragwerk`) referenzieren ausschließlich UUIDs (Memory
  `project_bauteil_identifikation`).

- **Ausschnittsregion-Repräsentanten.** Verschiedene Repräsentationen
  desselben geometrischen Bereichs (achsenparalleler Hüllquader vs.
  beliebiges Polyeder) führen auf semantisch dieselbe Inzidenz-
  Klassifikation, sofern der dargestellte Bereich gleich ist. Die
  Wahl der Repräsentation ist Implementierungs-Entscheidung; die
  Definition bleibt invariant.

- **Nicht-Zirkularität.** Die Definition stützt sich auf die bereits
  definierten Begriffe `bauteil`, `verbindung`, `auflager`,
  `bearbeitung`, `verbindungsmittel`, `verbinder`, `uuid`, `punkt`,
  `weltkoordinatensystem`, `toleranzen` sowie auf `tragwerk` als
  Träger-Aggregat. Sie verweist auf `bauteilgruppe`, `kerve`,
  `bauwerk` ausschließlich abgrenzend (`abgrenzung_zu`).

## Erläuterung (nicht normativ)

### Drei-Sichten-Bild am gemeinsamen Knotenpunkt

```
            am selben Knotenpunkt
                    |
        ┌───────────┼───────────┐
        v           v           v
   Verbindung   Auflager   Konstruktionsdetail
   (Bemessung) (Tragwerk)  (Werkplan / Werkstatt)
    EC5 K. 8     EC5 K. 5         (App-Lesart II)
   IfcRel...    IfcStruct...      IfcGroup
```

Die drei App-Aggregate koexistieren an derselben physischen Stelle
in W und beschreiben **denselben** Bauteil-Treffen aus **drei
unterschiedlichen** Sichten. Die Drei-Sichten-Trennung ist
**App-Synthese**, nicht Korpus-Ergebnis (siehe Quellenkonflikt-Block):
die Norm-Quellen sprechen meist nur von einer Schicht (EC5 vom
Anschluss, SIA 260 vom Auflager), die CAD-Praxis verwischt sie. Das
Sach-Modell der App trennt sie, weil sie in unterschiedlichen
Bemessungs- und Plan-Schichten benutzt werden und unterschiedliche
Informationen tragen.

| Sicht | Trägt | Wer nutzt sie |
|---|---|---|
| Verbindung | Bauteile, Verbindungsmittel, Verbinder, Verstärkungen, Nachweisverfahren | Bemessungs-Schicht, IFC-Export als `IfcRelConnectsElements` |
| Auflager | Manifestation, Wertigkeit, Lagerungsart, gestützt-durch | Tragwerks-Schicht, IFC-Export als `IfcStructuralConnection` |
| Konstruktionsdetail | Ausschnittsregion, beteiligte Bauteile/Verbindungen/Auflager/Bearbeitungen | Werkplan-Schicht, IFC-Export als `IfcGroup` |

### Werkplan-Bezeichnungs-Grammatik

Im DACH-Holzbau-Korpus folgen die Bezeichnungen von Konstruktions-
details einer impliziten Grammatik

```
[Bauteilrolle]<Anschluss-Topologie>-Detail
```

mit den im Korpus etablierten Werten:

| Bezeichnung | Topologie | Beteiligte Bauteilrollen (typisch) |
|---|---|---|
| Sparrenfußdetail | Fuß-Anschluss | Sparren + Fußpfette/Mauerlatte |
| Mittelpfettendetail | Mittel-Auflager | Sparren + Mittelpfette |
| Firstdetail | First-Anschluss | Sparren + Sparren bzw. Sparren + Firstpfette |
| Pfettenstoßdetail | Längs-Stoss | Pfette + Pfette (gleiche Rolle) |
| Traufdetail | Trauf-Anschluss | Sparren + Fußpfette + ggf. Aufschiebling + Traufgesims |
| Ortgangdetail | Ortgang-Anschluss | Sparren + Ortgangbohle + ggf. Windrispe |
| Sockeldetail | Sockel-Anschluss | Schwelle + Fundament |
| Eckdetail | Ecke (innen/außen) | Wand + Wand bzw. Bauteilrolle + Bauteilrolle |

Diese Grammatik ist **nicht normativ** (keine Norm kodifiziert sie),
aber im DACH-Korpus weitgehend konsistent. Die App verwendet sie als
Empfehlung für das optionale `bezeichnung`-Feld und für die
Detail-Adressierung im späteren Werkplan-Modul. Cross-Hersteller
(Cadwork, Dietrich's, SEMA) gibt es **kein** einheitliches Schema
für Detail-Nummern oder Detail-Adressen; die App führt eine eigene
Detail-Adressierung als Folgearbeit.

### Anwendungsbeispiel: Sparrenfußdetail

Am Sparrenfuß-auf-Fußpfette-Punkt eines Pfettendachs koexistieren
gleichzeitig:

- die **Verbindung** mit Schraubengruppe (`Verbindung` mit `typ =
  Anschluss`, Bauteile = {Sparren, Fußpfette}, Verbindungsmittel =
  {sparren_pfette_schrauben}, Nachweisverfahren = Johansen);
- das **Auflager** des Sparrens auf der Fußpfette
  (`Auflager` mit `manifestation` = Polygon der Kerv-Sohle,
  `gestuetztesBauteil` = Sparren, `gestuetztDurch` = Fußpfette,
  `wertigkeit` = (fest, fest, fest, frei, frei, frei),
  `lagerungsart = direkt`);
- das **Konstruktionsdetail** „Sparrenfußdetail" (dieser Eintrag)
  mit `beteiligte_bauteile` = {Sparren, Fußpfette},
  `beteiligte_verbindungen` = {sparren_pfette_verbindung},
  `beteiligte_auflager` = {sparrenfuss_auflager},
  `beteiligte_bearbeitungen` = {sparrenfuss_kerve} und einer
  Ausschnittsregion, die den Sparrenfuß-Bereich umschließt.

Wird der Sparrenfuß im Werkplan dokumentiert, ist das
Konstruktionsdetail das adressierbare Aggregat; Verbindung und
Auflager werden über die UUID-Verweise im Detail mit-erschlossen.

### Wann ist Konstruktionsdetail nicht das richtige Aggregat?

- Eine **lokale konstruktive Funktionseinheit** mit eigener
  Geometrie und exklusiver Mitgliedschaft (Lukarne, Auswechslung,
  vorgefertigtes Wandelement) ist eine **Bauteilgruppe**
  (`hg_bauteilgruppe.md`), kein Konstruktionsdetail. Die
  Bauteilgruppe ist partitiv mit kaskadischem Lebenszyklus; das
  Konstruktionsdetail ist nicht-exklusiv und nicht
  Lebenszyklus-bindend.
- Eine **Detailzeichnung** im Sinne von DIN 1356-1 (Plan-Artefakt,
  Maßstabsklasse 1:20 bis 1:1) ist ein **Plan-Objekt** in der
  Visualisierungs-/Plan-Schicht, kein Sach-Aggregat im
  Domänen-Modell. Das Konstruktionsdetail ist das, was die
  Detailzeichnung **darstellt** — nicht die Zeichnung selbst.
- Ein **Detail-Katalog-Eintrag** (Regeldetail, Standarddetail,
  Leitdetail) ist eine **Typ-Vorlage** mit fester Maßkette und
  Ausführungsregeln; sie wird im konkreten Bauwerk als
  Konstruktionsdetail-Instanz **realisiert**. Die Typ-Lesart
  (Lesart III) ist Folgearbeit als Detail-Katalog-Funktion auf
  Wieder-Verwendung von Konstruktionsdetail-Instanzen.

### IFC-Mapping

| Aspekt | IFC 4.3 Pendant |
|---|---|
| Konstruktionsdetail als Aggregat | `IfcGroup` mit eigener `GlobalId`, Subtyp von `IfcObjectDefinition` |
| Mitgliedschaft (Bauteile/Verbindungen/Auflager) | `IfcRelAggregates` oder `IfcRelAssignsToGroup` (nicht-exklusiv) |
| Optionale Element-Komposit-Variante | `IfcElementAssembly` (Subtyp von `IfcElement`); nur teilweise passend (Element-Charakter zu streng, exklusive Mitgliedschaft) |
| Plan-Artefakt-Pendant (Lesart I) | `IfcAnnotation`, `IfcDocumentReference`, 2D-Darstellungs-Schicht — **nicht** Gegenstand dieses Eintrags |
| Detail-Katalog (Lesart III) | kein IFC-Pendant; App-eigene Folgearbeit |

Die App-Default-Wahl `IfcGroup` ist konsistent mit der Default-Wahl
in `hg_verbindung.md`. `IfcElementAssembly` ist nur dann sinnvoll,
wenn das Konstruktionsdetail als **vorgefertigte** Bauteilgruppe
(Sparren-Pfetten-Paar als Aufbau-Einheit aus dem Werk) geführt wird —
in diesem Fall verschiebt sich der Charakter zur Bauteilgruppe
(`hg_bauteilgruppe.md`), und das Konstruktionsdetail als
Werkplan-Sicht bleibt orthogonal.

### Folgearbeit

- **Detail-Adressierungs-Schema** im Werkplan-Modul (Detail-Nummer,
  Detail-Kreis im Übersichtsplan, Pfeil-Verweise) — Trigger: erstes
  Tool, das Werkplaene erzeugt. Nicht Teil dieses Eintrags.
- **Detail-Katalog-Funktion** (Lesart III) als optionaler Aufsatz
  auf Konstruktionsdetail-Instanzen, mit Typ-Vorlage und
  Wiederverwendung — Trigger: erste Wiederverwendungs-Operation
  an Detail-Instanzen.
- **Sub-Spezialisierungen** wie `sparrenfuss_detail`,
  `firstdetail`, `pfettenstoss_detail`, `traufdetail`,
  `ortgangdetail` — Trigger: erstes Tool, das einen dieser Typen
  als eigenen Sub-Aggregat-Typ mit eigenen Constraints benötigt.

## Beziehungen

- **Oberbegriff**: derzeit `null` (analog `verbindung`, `auflager`,
  `bauteilgruppe`, `tragwerk`). Ein gemeinsamer abstrakter
  Oberbegriff für „Aggregat über Element-Instanzen" ist derzeit
  nicht geplant — die strukturellen Unterschiede zwischen
  Verbindung (Bemessung), Auflager (Tragwerk), Konstruktionsdetail
  (Werkplan) und Bauteilgruppe (Komposition) sind zu groß.
- **Bestandteile (referenziell, nicht partitiv)**:
  - **Ausschnittsregion** (Hüllquader / Polyeder in W).
  - **Beteiligte Bauteile** (UUID-Menge auf `bauteil`).
  - **Beteiligte Verbindungen** (UUID-Menge auf `verbindung`).
  - **Beteiligte Auflager** (UUID-Menge auf `auflager`).
  - **Beteiligte Bearbeitungen** (UUID-Menge auf `bearbeitung`).
  - **Träger-Tragwerk** (UUID auf `tragwerk`).
- **Spezialisierungen** (Folgearbeit, trigger-basiert):
  - `sparrenfuss_detail` — Sparren-Fußpfetten-Anschluss.
  - `mittelpfetten_detail` — Sparren-Mittelpfetten-Anschluss.
  - `firstdetail` — Sparren-Sparren- bzw. Sparren-Firstpfetten-
    Anschluss am First.
  - `pfettenstoss_detail` — Längs-Stoss zweier Pfettenabschnitte.
  - `traufdetail` — Trauf-Anschluss mit Sparrenfuß, Fußpfette,
    Aufschiebling, Traufgesims.
  - `ortgangdetail` — Dachrand quer zur Traufe.
- **Verwendung**:
  - Sicht auf ein **Tragwerk** (`tragwerk`): das Träger-Tragwerk
    wird über `traegertragwerk` referenziert; das Konstruktions-
    detail bildet keinen eigenen Tragwerks-Eintrag.
  - Adressier-Einheit im **Werkplan** (Folgearbeit): die UUID des
    Konstruktionsdetails ist die persistente Adresse für
    Detail-Verweise in Übersichtsplänen.
- **Abgrenzung**:
  - **Verbindung** (`verbindung`): Bemessungs-Sicht am
    Knotenpunkt. Verbindung und Konstruktionsdetail koexistieren
    am selben Knotenpunkt; das Detail referenziert die Verbindung
    in `beteiligte_verbindungen`. Beide sind unterschiedliche
    Aggregate mit eigener UUID.
  - **Auflager** (`auflager`): Tragwerks-Sicht am Knotenpunkt.
    Auflager und Konstruktionsdetail koexistieren am selben
    Knotenpunkt; das Detail referenziert das Auflager in
    `beteiligte_auflager`, falls am Knoten ein Auflager liegt.
    Ein Konstruktionsdetail **kann** ohne Auflager-Bezug
    auftreten (Pfettenstoßdetail im freien Feld).
  - **Bauteilgruppe** (`bauteilgruppe`): partitive Komposition mit
    **exklusiver** Mitgliedschaft und kaskadischem Lebenszyklus.
    Das Konstruktionsdetail ist **nicht-exklusiv** und nicht
    Lebenszyklus-bindend; ein Bauteil kann gleichzeitig Mitglied
    einer Bauteilgruppe (z. B. Auswechslung) und beteiligtes
    Bauteil in mehreren Konstruktionsdetails sein.
  - **Kerve** (`kerve`): partitive Bearbeitung am Sparren-Polyeder
    (Bauteil-gekoppelt). Die Kerve **ist** typisch beteiligte
    Bearbeitung eines Sparrenfußdetails, aber das Konstruktions-
    detail **ist nicht die Kerve**: das Detail trägt zusätzlich
    Bauteile, Verbindung, Auflager und Ausschnittsregion.
  - **Bearbeitung** (`bearbeitung`): allgemeiner Oberbegriff der
    Kerve. Bearbeitungen sind partitiv, Konstruktionsdetail ist
    Aggregat-Sicht; das Detail referenziert seine beteiligten
    Bearbeitungen, ist aber selbst keine Bearbeitung.
  - **Tragwerk** (`tragwerk`): übergeordnete bauteilbezogene
    Realität. Das Konstruktionsdetail bildet eine **lokale Sicht**
    auf das Tragwerk; es ist Bestandteil **keiner** der
    Tragwerks-Tupel-Komponenten (B, V, A, L). Das Tragwerk wird
    über `traegertragwerk` referenziert.
  - **Bauteil** (`bauteil`): ein Konstruktionsdetail ist kein
    Bauteil, sondern Aggregat-Sicht über Bauteilen, Verbindungen,
    Auflagern und Bearbeitungen.
  - **Bauwerk** (`bauwerk`): ein Konstruktionsdetail gehört
    transitiv zum Bauwerk, das das `traegertragwerk` enthält. Die
    Beziehung ist nicht direkt modelliert.

## Implementierungshinweis

**Im aktuellen Glossarstand wird ausdrücklich keine Code-Klasse
`Konstruktionsdetail` angelegt** (analog `hg_bauteilgruppe.md`:
die ontologische Vorbereitung lebt zunächst nur im Glossar). Die
Code-Klasse entsteht zusammen mit dem ersten Werkplan-Tool, das
Detail-Adressierung tatsächlich benötigt. Der folgende
Skizzen-Code ist orientierender Implementierungs-Hinweis für
diesen Zeitpunkt.

```kotlin
// SKIZZE — nicht jetzt anlegen.
// Glossar: hg_konstruktionsdetail.md

package domain.aggregat.konstruktionsdetail

import domain.geometrie.Punkt
import java.util.UUID

/** Ausschnittsregion in W: achsenparalleler Hüllquader oder Polyeder. */
sealed interface Ausschnittsregion {
    data class HuellquaderAchsenparallel(
        val min: Punkt,
        val max: Punkt
    ) : Ausschnittsregion
    // Spätere Varianten: HuellquaderOrientiert, Polyederbegrenzt.
}

/**
 * Konstruktionsdetail: Aggregat-Sicht über einer räumlich
 * abgegrenzten Ausschnittsregion an einem Knotenpunkt eines
 * Tragwerks, das die dort beteiligten Bauteile, Verbindungen,
 * Auflager und Bearbeitungen für die plan- und werkstatt-
 * orientierte Repräsentation bündelt.
 *
 * Glossar: hg_konstruktionsdetail.md
 *
 * NICHT Subtyp von Element. Eigene Aggregat-Klasse, analog
 * Verbindung, Auflager und Tragwerk. Mitgliedschaft nicht-exklusiv
 * (anders als Bauteilgruppe).
 *
 * IFC: IfcGroup mit IfcRelAggregates/IfcRelAssignsToGroup
 *      (Default); IfcElementAssembly nur bei vorgefertigter
 *      Aufbau-Einheit (siehe Erläuterungs-Block).
 * BTLx: keine eigene Entität; manifestiert sich implizit über
 *       beteiligte Parts und Processings.
 */
data class Konstruktionsdetail(
    val uuid: UUID,                                       // eigene Identität
    val ausschnitt: Ausschnittsregion,                    // räumliche Region in W
    val knotenpunkt: Punkt? = null,                       // optionaler Bezugspunkt
    val beteiligteBauteile: Set<UUID>,                    // FK auf Bauteile, |...| >= 1
    val beteiligteVerbindungen: Set<UUID> = emptySet(),   // FK auf Verbindungen
    val beteiligteAuflager: Set<UUID> = emptySet(),       // FK auf Auflager
    val beteiligteBearbeitungen: Set<UUID> = emptySet(),  // FK auf Bearbeitungen
    val traegertragwerk: UUID,                            // FK auf Tragwerk
    val bezeichnung: String? = null
) {
    init {
        // K1. Nicht-Leere am Knotenpunkt              → Entartet.LeeresDetail
        // K2. Inzidenz mit ausschnitt (Modell-Lookup) → Entartet.MitgliedNichtInAusschnitt
        // K3. Tragwerks-Konsistenz (Modell-Lookup)    → Entartet.MitgliedNichtImTragwerk
        // K4. knotenpunkt in ausschnitt              → Entartet.KnotenpunktAusserhalb
        // K5. Keine triviale Duplizierung            → Entartet.TrivialeDuplizierung
        // K6. Nicht-Exklusivität ist Default        — keine Prüfung nötig
    }
}
```

- **Einheit**: Längen in mm (Double); geometrische Träger im
  W-System.
- **Identität**: `uuid` ist Pflicht und eigenständig (eigene UUID
  des Aggregats, RFC 9562 v7, persistent). Externe Verweise auf das
  Konstruktionsdetail gehen ausschließlich auf diese UUID.
- **Foreign-Key-Regel**: alle Mitglieds-Felder (Bauteile,
  Verbindungen, Auflager, Bearbeitungen, Tragwerk) referenzieren
  ausschließlich UUIDs (Memory `project_bauteil_identifikation`).
- **Invarianten** (in einer Modell-bezogenen Fabrikfunktion
  `Konstruktionsdetail.bilde(modell: Modell, …)` geprüft; bei
  Verletzung `Resultat.Fehler`, niemals Exception):
  1. K1 — Nicht-Leere → `Entartet.LeeresDetail`.
  2. K2 — Inzidenz aller Mitglieder mit `ausschnitt` im
     Toleranzbereich `Toleranzen.LAENGE_EPS` → sonst
     `Entartet.MitgliedNichtInAusschnitt`.
  3. K3 — alle Mitglieder gehören zum Träger-Tragwerk → sonst
     `Entartet.MitgliedNichtImTragwerk`.
  4. K4 — `knotenpunkt ∈ ausschnitt` (Toleranz `LAENGE_EPS`) →
     sonst `Entartet.KnotenpunktAusserhalb`.
  5. K5 — keine triviale Duplizierung mit anderem Detail am
     selben Tragwerk → sonst `Entartet.TrivialeDuplizierung`.
- **Toleranz-Anwendung** (siehe `hg_toleranzen.md` §4):
  - Inzidenz-Tests (K2, K4): `LAENGE_EPS` auf
    Punkt-/Polygon-Abständen.
- **Edge Cases**:
  - **Konstruktionsdetail mit einem Bauteil und einer
    Bearbeitung** (z. B. „Zapfendetail" zur Dokumentation einer
    isolierten Bearbeitung): zulässig nach K1.
  - **Konstruktionsdetail ohne Auflager** (z. B. „Pfettenstoßdetail"
    im freien Feld eines durchlaufenden Trägers):
    `beteiligteAuflager = emptySet()` zulässig.
  - **Konstruktionsdetail mit nur einem Bauteil und ohne weitere
    Mitglieder**: nicht zulässig (K1) — kein plan- oder
    werkstattrelevanter Inhalt.
  - **Mehrfach-Mitgliedschaft eines Bauteils**: zulässig (K6) —
    derselbe Sparren in Sparrenfußdetail + Mittelpfettendetail +
    Firstdetail.
  - **Verschachtelte Konstruktionsdetails** (Detail im Detail):
    derzeit nicht modelliert; bei Bedarf als Folgearbeit über
    eine `untergeordnete_details`-Komponente.
  - **Konstruktionsdetail über Tragwerks-Grenzen hinweg**: nicht
    zulässig — ein Detail bezieht sich auf genau ein Tragwerk
    (K3, `traegertragwerk` als Pflichtfeld).
- **IFC-Export-Mapping**:
  - **Default**: `IfcGroup` mit eigener `GlobalId`, plus
    `IfcRelAggregates` (oder `IfcRelAssignsToGroup`) als
    Mitgliedschafts-Beziehung zu den Bauteilen, Verbindungen,
    Auflagern und Bearbeitungen.
  - **Optional** (bei vorgefertigter Aufbau-Einheit):
    `IfcElementAssembly` mit `PredefinedType = USERDEFINED` und
    benamtem `ElementType` — verschiebt aber den Charakter zur
    Bauteilgruppe (siehe `hg_bauteilgruppe.md`).
  - **Plan-Artefakt** (Lesart I): wird separat über
    `IfcAnnotation`/`IfcDocumentReference` der Plan-Schicht
    abgebildet; nicht Gegenstand dieses Mappings.
- **BTLx-Export**: keine eigene Entität. Das Konstruktionsdetail
  wird beim BTLx-Export nicht ausgegeben; optional kann es als
  `UserAttribute` (`DetailGuid`) an den beteiligten Parts vermerkt
  werden.
- **Abgeleitete Eigenschaften** (als Funktionen, keine Felder):
  - `geometrieInWelt(modell: Modell): GeometrieInW` —
    Vereinigung der Bauteil-Punktmengen, geschnitten mit
    `ausschnitt`.
  - `boundingBox(): AABB` — achsenparalleler Hüllquader der
    Ausschnittsregion in W.
  - `enthaeltBauteil(b: UUID): Boolean` — `b ∈ beteiligteBauteile`.
  - `werkplanBezeichnung(): String` — abgeleitete Bezeichnung
    nach der Grammatik `[Bauteilrolle]<Anschluss-Topologie>-Detail`
    (Folgearbeit).
- **Bezeichner-Konvention** (siehe `docs/_CODE_KONVENTIONEN.md`):
  Domänen-Klasse heißt `Konstruktionsdetail` (deutsch,
  Glossarbegriff). Synonyme `Detail`, `Anschlussdetail`,
  `Knotendetail` werden im Code nicht als eigene Klassen geführt,
  sondern erscheinen ausschließlich als KDoc-Stichworte zu
  `Konstruktionsdetail`.

## Quellen

**Primär (normativ):**

- ISO 16739-1:2024, „Industry Foundation Classes (IFC) for data
  sharing in the construction and facility management industries
  – Part 1: Data schema" (IFC 4.3.2.0), Entitäten `IfcGroup`,
  `IfcRelAggregates`, `IfcRelAssignsToGroup`, `IfcElementAssembly`.
- DIN 1356-1:2024-04, „Bauzeichnungen – Teil 1: Grundregeln der
  Darstellung" (Detailzeichnung als Maßstabsklasse).
- DIN EN 1995-1-1:2010-12, „Eurocode 5: Bemessung und Konstruktion
  von Holzbauten – Teil 1-1", Abschnitt 1.5 und Kapitel 8.
- SIA 265:2021, „Holzbau", Abschnitt 5 „Konstruktive Durchbildung".
- DIN 1052:2008-12, „Entwurf, Berechnung und Bemessung von
  Holzbauwerken", Abschnitt 3.

**Sekundär:**

- Holzbau-Handbuch, Reihe 1, Teil 7, Folge 2 „Anschlüsse im
  Hallenbau", Informationsdienst Holz.
- Mönck, W.; Rug, W.: *Holzbau – Bemessung und Konstruktion.*
  16. Aufl., Beuth, Berlin 2015, Kap. 11.
- Natterer, J.; Herzog, T.; Volz, M.: *Holzbau-Atlas.* 4. Aufl.,
  Birkhäuser, Basel 2003.
- Blass, H. J.; Sandhaas, C.: *Ingenieurholzbau – Grundlagen der
  Bemessung.* KIT Scientific Publishing, Karlsruhe 2016.
- Gerner, M.: *Fachwerk – Instandsetzung, Sanierung, Neubau.*
  DVA, 7. Aufl. 2007.
- Holzbau Deutschland-Institut: *Regeldetailkatalog – Planungs-
  hilfen für Außenwandbekleidungen aus Holz.*
- Lignum: *Bauteilkatalog* (Brandschutz, Schallschutz), Lignum,
  Zürich.
- KLH: *Detailkatalog* (Brettsperrholz, CAD-Detailkatalog 2020).

**Korpus (nicht autoritativ):**

- Cadwork-Hersteller-Dokumentation, cadwork.de — CAD-Praxis
  „Detail" als Plan-Modul.
- Dietrich's-Forum, forum.dietrichs.com.
- SEMA-Forum, sema-soft.net.
- baubeaver.de, Lemma „Pfetten", „Sparrenfuß".
- harzerstatik.de, „Variante - Dachdetails - First".
- Wikipedia, Lemmata „Detail (Bauwesen)" (abgerufen 2026-05-14).
- Recherche-Bericht: `docs/recherche/2026-05-14_hg_konstruktionsdetail.md`.
