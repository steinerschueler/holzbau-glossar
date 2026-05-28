---
id: lastfall
benennung: Lastfall
synonyme: []
abgelehnte_benennungen: [Belastungsfall, Lastannahme, Einwirkung, Einwirkungskombination, Lastkombination, Lastfallkombination, "load case", "action", "action combination", "combination of actions"]
oberbegriff: null
begriffstyp: aggregat
voraussetzungen: [bauteil, uuid, weltkoordinatensystem, toleranzen]
abgrenzung_zu: [einwirkung, bemessungssituation, lastkombination, einwirkungskombination, gefaehrdungsbild, lastannahme, tragwerk, auflager, bauteil, statisches_system]
status: entwurf
theorie_pflichtig: required
quellen_primär:
  - "SIA 260:2013 'Grundlagen der Projektierung von Tragwerken', Schweizerischer Ingenieur- und Architektenverein, Zürich, Abschnitt 4.4 (Bemessungssituationen und Lastfälle): „Die physikalisch verträgliche Anordnung von simultan auftretenden Einwirkungen formen den Lastfall für einen bestimmten rechnerischen Nachweis. Jeder Lastfall ist Teil einer Bemessungssituation.“ (Sekundärquellen-Konsens, Originaltext nicht im Volltext eingesehen — siehe Recherche §A/§L)."
  - "DIN EN 1990:2010-12 'Eurocode: Grundlagen der Tragwerksplanung', Abschnitt 1.5 (Begriffe) und Abschnitt 3.2 (Bemessungssituationen, design situations: persistent / transient / accidental / seismic); Abschnitt 6 (Bemessungswerte): Lastfall als operationale Größe in den Kombinations-Regeln, keine geschlossene Begriffs-Definition."
  - "DIN 1055-100:2001-03 (zurückgezogen) 'Einwirkungen auf Tragwerke — Teil 100: Grundlagen der Tragwerksplanung, Sicherheitskonzept und Bemessungsregeln': „Ein Lastfall ist eine Festlegung von Lastanordnungen, Verformungen und Imperfektionen, die gleichzeitig auf ein Tragwerk einwirken können.“ (historische Schwester-Definition; durch Eurocode-Apparat abgelöst.)"
  - "DIN EN 1991-1-1:2010-12 bis DIN EN 1991-1-7 'Eurocode 1: Einwirkungen auf Tragwerke' (Wichten/Eigengewicht/Nutzlasten; Brandeinwirkungen; Schneelasten; Windlasten; Temperatur; außergewöhnliche Einwirkungen): zahlenmäßige Festlegung der Einwirkungen, aus denen Lastfälle gebildet werden."
  - "SIA 261:2020 + SIA 261/1:2020 'Einwirkungen auf Tragwerke' und 'Ergänzende Festlegungen': Schweizer Pendant zu EN 1991 mit eigenständigen Schnee- (§5), Wind- (§6), Temperatur- (§7) und Erdbeben-Festlegungen (§16); Schicht-1-Norm zur Festlegung der Einwirkungswerte."
  - "ISO 16739-1:2024 'Industry Foundation Classes (IFC) — Part 1: Data schema' (IFC 4.3.2), Structural-Analysis-Domain: Entitäten-Familie `IfcStructuralLoad` (abstrakter Lastwert) mit Subtypen `IfcStructuralLoadSingleForce`, `IfcStructuralLoadLinearForce`, `IfcStructuralLoadPlanarForce`, `IfcStructuralLoadTemperature` etc.; `IfcStructuralAction` (Wirkung am Modell, abstrakt) mit `IfcStructuralPointAction`/`IfcStructuralCurveAction`/`IfcStructuralSurfaceAction`; `IfcStructuralLoadGroup` (Gruppierungs-Container) mit konkretem Subtyp `IfcStructuralLoadCase` und `IfcLoadGroupTypeEnum`-Werten `LOAD_GROUP` / `LOAD_CASE` / `LOAD_COMBINATION` / `USERDEFINED`."
quellen_sekundär:
  - "Petersen, Chr.: Statik und Stabilität der Baukonstruktionen. Vieweg, Braunschweig (mehrfache Auflagen); Lehrbuch-Standard zur Begriffshierarchie Einwirkung → Lastfall → Lastkombination."
  - "Schneider, K.-J.; Albert, A.: Bautabellen für Ingenieure. 26. Aufl., Bundesanzeiger Verlag, Köln 2024; Tabellen-Klassifikation Einwirkungen G/Q/A/A_E und Kombinationsregeln."
  - "Mönck, W.; Rug, W.: Holzbau – Bemessung und Konstruktion. 16. Aufl., Beuth, Berlin 2015, Kap. 4 (Bemessungsgrundlagen)."
  - "Blass, H. J.; Sandhaas, C.: Ingenieurholzbau – Grundlagen der Bemessung. KIT Scientific Publishing, Karlsruhe 2016, Kap. 4."
  - "Marti, P.: Tragwerksentwurf. ETH Zürich, IBK; SIA-260-Einführung (PDF, archiv.ibk.ethz.ch)."
  - "SIA-D 0211 'Erläuterungen zur Tragwerksnorm SIA 260', sgeb.ch."
  - "Lüchinger, P.: 'Konzept der Tragwerksnormen SIA', Forum Holzbau."
  - "Recherche-Bericht: `docs/recherche/2026-05-14_hg_lastfall.md`."
quellenkonflikt: |
  **Norm-Asymmetrie zwischen SIA 260, EN 1990 und DIN 1055-100.** Keine
  der drei Hoch-Tier-Quellen trägt eine einheitlich geschlossene
  Begriffs-Definition über alle Quellen hinweg. Die Lage ist
  asymmetrisch (vgl. Recherche §M.1):

  - **SIA 260:2013 §4.4** liefert die qualitativ schärfste Definition
    („physikalisch verträgliche Anordnung von simultan auftretenden
    Einwirkungen für einen bestimmten rechnerischen Nachweis“).
    Diese App führt die SIA-260-Lesart als **Definitionskern**.
  - **DIN EN 1990:2010-12** trägt den Begriff operational im
    Kombinations-Apparat (§6) und in der Bemessungssituations-
    Klassifikation (§3.2), aber keine geschlossene Begriffs-
    Definition mit Definitionssatzbau.
  - **DIN 1055-100:2001-03** ist die nominell geschlossenste, aber
    durch den Eurocode-Apparat **zurückgezogene** Quelle. Ihre
    Definition wird als historisches Pendant geführt, nicht als
    aktuell normativ.

  **Vier-Schicht-Begriffsfamilie — eigene Festlegung.** Die App
  führt die Begriffsfamilie des Sicherheitskonzepts EN 1990 / SIA 260
  als **vier strikt getrennte Schichten**:

  1. **Einwirkung** (action) — Ursache mechanischer Beanspruchung am
     Tragwerk (Kraft, aufgezwungene Verformung), klassifiziert nach
     zeitlicher Veränderlichkeit (G ständig, Q veränderlich,
     A außergewöhnlich, A_E Erdbeben).
  2. **Bemessungssituation** (design situation) — Zustand des
     Tragwerks im Zeitraum eines Nachweises: persistent, transient,
     accidental, seismic.
  3. **Lastfall** (dieser Eintrag) — physikalisch verträgliche
     Anordnung gleichzeitig wirkender Einwirkungen für einen
     bestimmten Nachweis.
  4. **Lastkombination** (combination of actions) — rechnerische
     Überlagerung mehrerer Lastfälle bzw. Einwirkungen mit
     Teilsicherheits- und Kombinationsbeiwerten (γ, ψ) zur
     Erzeugung des Bemessungswerts E_d.

  „Einwirkung“ und „Lastkombination“ sind in dieser App **keine
  Synonyme** des Lastfalls, sondern Nachbar-Begriffe der Schichten 1
  und 4. Im praktischen Sprachgebrauch (Eurocode-Praxis-Literatur,
  Software-Hersteller-Doku) werden die Schichten 3 und 4 regelmäßig
  vermischt („Lastfallkombination“, „load case combination“) — diese
  Vermischung ist nicht durch die Norm gedeckt; die App lehnt sie ab
  und führt die Schichten in getrennten Aggregaten.

  **Schweiz/DE-Asymmetrie.** Die schweizerische und die deutsche
  Begriffslinie sind inhaltlich konvergent, sprachlich aber
  verschieden:

  - **Gefährdungsbild** (SIA 260 §4) ist ein **Schweizer Spezifikum**
    ohne genaues Pendant in EN 1990. SIA 260 schaltet zwischen
    Nutzungsvereinbarung und Bemessungssituation eine eigene Stufe
    der Risiko-Szenarien-Beschreibung ein (z. B. „Wintersturm mit
    gleichzeitigem Vollschnee“); EN 1990 fasst diese Lesart in die
    Bemessungssituation hinein. Der Begriff `gefaehrdungsbild` ist
    in `abgrenzung_zu` aufgenommen und gehört in die Kategorie (D)
    nach `HG_KONVENTIONEN.md` §6 — die App modelliert ihn nicht
    als eigenständigen Glossarbegriff, sondern referenziert ihn als
    Schweizer Norm-Konzept im SIA-260-Kontext. Falls die App später
    SIA-260-spezifische Workflows abbildet (Nutzungsvereinbarung,
    Projektbasis), kann das Gefährdungsbild als Folge-Eintrag
    nachgezogen werden.
  - **Schneelast-Zonen**: in der Schweiz gilt SIA 261 §5 mit eigener
    Bodenwertekarte (alpenraum-spezifisch deutlich höher als DACH-
    Tiefland); die Karte in EN 1991-1-3 Annex C ist in der Schweiz
    nur informativ, in Deutschland gilt DIN EN 1991-1-3/NA mit
    Zonen 1/1a/2/2a/3.
  - **Windlast-Zonen**: SIA 261 §6 mit eigener, topographie-
    getriebener Bodenwertekarte (Föhn-Zonen); Deutschland DIN EN
    1991-1-4/NA mit Zonen 1–4. Die Karten sind nicht deckungsgleich.
  - **Erdbeben-Zonen**: SIA 261 §16 + SIA 261/1 mit Zonen
    Z1a/Z1b/Z2/Z3a/Z3b und eigenen Bauwerksklassen-Faktoren;
    Deutschland DIN EN 1998/NA mit anderer Zonierung.
  - **Bauwerksklassen** (SIA 260 §4: I/II/III) und **Consequences
    Classes** (EN 1990 Anhang B: CC1/CC2/CC3) sind funktional
    analog, aber nicht deckungsgleich.

  Die Lastzonen-Details gehören nicht in diesen Glossareintrag,
  sondern in eine spätere Lastannahmen-/Norm-Daten-Schicht der App.

  **Historische Lastfall-Klassen H und HZ.** Die alte DIN 1055
  operierte mit deterministischen Lastfall-Klassen **H**
  (Hauptlastfall = Eigenlast + eine veränderliche Hauptlast) und
  **HZ** (Hauptlastfall mit Zusatzlast = Eigenlast + Haupt- +
  Zusatzlasten, seltene Kombination, mit zulässigem Spannungs-
  Faktor). Diese Lastfall-Klassen aus dem alten globalen
  Sicherheitskonzept (ein einziger Globalfaktor ν) sind mit der
  Eurocode-Einführung durch den semiprobabilistischen Apparat mit
  γ_G/γ_Q/ψ-Faktoren **abgelöst**. Praktiker verwenden die
  H/HZ-Bezeichnungen noch im Bestand und im Brückenbau (DIN 1072);
  für die App-Modellierung sind sie historisch, nicht normativ
  (siehe Erläuterungsblock).

  **IFC-Mapping und Schicht-Kollaps.** IFC 4.3 trennt sauber den
  **Lastwert** (`IfcStructuralLoad`) von der **Wirkung am Modell**
  (`IfcStructuralAction`), kollabiert aber die App-Schichten 2/3/4
  in eine einzige Entität `IfcStructuralLoadGroup` mit
  `PredefinedType`-Diskriminator (`LOAD_GROUP` / `LOAD_CASE` /
  `LOAD_COMBINATION` / `USERDEFINED`). Der konkrete Subtyp
  `IfcStructuralLoadCase` (mit Attribut `SelfWeightCoefficients`)
  trägt die Schicht-3-Lesart der App. Diese App führt die
  vier Schichten als getrennte Aggregate; das IFC-Mapping
  ist im Implementierungs-Hinweis dokumentiert. Das design2machine-
  Schema BTLx trägt **keine eigene Lastfall-Entität** (analog
  Auflager und Verbindung).

  **Mindest-Lastfälle.** Weder EN 1990 noch SIA 260 schreiben eine
  abschließende Pflichtmenge an Lastfällen vor; beide verlangen,
  dass für **alle relevanten Bemessungssituationen** Lastfälle
  betrachtet werden. Die in der Erläuterung genannten typischen
  Hochbau-Einwirkungen (Eigenlast, Nutzlast, Schnee, Wind,
  Temperatur, ggf. Erdbeben) sind Praxis-Standard, nicht Norm-Pflicht.

  **Begriffstyp.** `aggregat` ist eindeutig (analog `verbindung`,
  `tragwerk`, `auflager`): der Lastfall trägt eine eigene UUID
  (für Referenzierbarkeit aus Bemessungs-Nachweisen, Lastkombinationen
  und externem IFC-Export als `IfcStructuralLoadCase` mit eigener
  GlobalId), hat eigene partitive Bestandteile (Leiteinwirkung,
  Begleiteinwirkungen, Einwirkungs-Anordnung, Inzidenz zu Bauteilen)
  und eigene Konsistenzbedingungen über der Komposition
  (physikalische Verträglichkeit, Bauteil-Inzidenz, Bemessungs-
  situations-Konsistenz). `oberbegriff: null` analog zu den
  Geschwister-Aggregaten.

  **Synonyme und abgelehnte Benennungen.** Es gibt keine echten
  Synonyme: „Belastungsfall“ ist im Korpus selten und veraltet;
  „Lastannahme“ ist Pendant zu Schicht 1 (Einwirkung), nicht
  Schicht 3; „Einwirkung“ und „Lastkombination“ /
  „Einwirkungskombination“ sind eigene Nachbar-Schichten und
  ausdrücklich nicht synonym; „Lastfallkombination“ ist ein
  Praxis-Hybrid für Lastkombination und wird abgelehnt. Englische
  Pendants (`load case`, `action`, `action combination`,
  `combination of actions`) sind in der Hauptdefinition nicht
  zulässig.

  **Quellen-Volltext-Lücke (ehrlich markiert).** Originaltexte von
  SIA 260:2013 §4.4, DIN EN 1990:2010-12 §1.5/§3.2, DIN 1055-100:
  2001-03, ISO 16739-1:2024 (IFC 4.3) konnten in der Recherche
  nicht im Volltext eingesehen werden (kostenpflichtig, kein
  Web-Volltext, WebFetch im Sandbox-Profil nicht freigegeben).
  Die hier zitierten Definitions-Wortlaute stützen sich auf
  Sekundärquellen-Konsens. Die Lücke ist in
  `docs/recherche/2026-05-14_hg_lastfall.md` §A und §L dokumentiert.
---

## Prosa-Definition

Ein **Lastfall** ist ein Aggregat aus einer physikalisch verträglichen
Anordnung gleichzeitig wirkender Einwirkungen (einer Leiteinwirkung
und endlich vielen Begleiteinwirkungen), das einer Bemessungssituation
zugeordnet ist, jeder Einwirkung eine geometrische Verteilung im
Weltkoordinatensystem sowie eine Inzidenz zu Bauteilen des Tragwerks
zuweist, eine eigene technische Identität trägt und damit den
nachweisbezogenen Eingabe-Zustand für einen rechnerischen
Tragwerksnachweis darstellt.

## Mathematische Definition

Sei

- W das Weltkoordinatensystem (siehe `hg_weltkoordinatensystem.md`),
- 𝒰 der UUID-Raum nach `hg_uuid.md`,
- 𝓑 die Menge der Bauteile nach `hg_bauteil.md`,
- 𝓔 die Menge der **Einwirkungen** im Sinne der EN 1990 / SIA 260
  (Schicht 1; eigener Glossareintrag `einwirkung` folgt). Jede
  Einwirkung e ∈ 𝓔 trägt mindestens eine Klassifikation
  `kategorie(e) ∈ {G, Q, A, A_E}` (ständig, veränderlich,
  außergewöhnlich, Erdbeben), einen charakteristischen Wert
  und eine semantische Identität (z. B. „Schnee“, „Wind Süd“,
  „Nutzlast Wohnen“),
- 𝓢 := {persistent, transient, accidental, seismic} die Menge der
  **Bemessungssituationen** nach EN 1990 §3.2 bzw. SIA 260 §4.4
  (Schicht 2; eigener Glossareintrag `bemessungssituation` folgt),
- 𝓥𝓔 die Menge der **Einwirkungs-Anordnungen**: jede Anordnung ist
  eine Funktion `α: 𝓔 → 𝓖_W`, die jeder Einwirkung ihre
  geometrische Verteilung im W-System zuordnet (Punkt-, Linien-,
  Flächen- oder Volumen-Verteilung mit Wert und Richtung an jeder
  Stelle); 𝓖_W ist die Menge der geometrischen Verteilungen über
  Trägern in ℝ³,
- 𝓘 die Menge der **Inzidenzen** zu Bauteilen: jede Inzidenz ist
  eine Relation `ι ⊆ 𝓔 × 𝒰`, die jeder Einwirkung diejenigen
  Bauteil-UUIDs zuordnet, auf die sie als Eingangsgröße wirkt
  (Bauteil, Bauteil-Fläche, Bauteil-Kante oder Bauteil-Punkt).

Dann ist ein **Lastfall** das Tupel

```
ℓ := (uuid, bemessungssituation, leiteinwirkung, begleiteinwirkungen,
      einwirkungs_anordnung, inzidenz, bezeichnung)
```

mit den Komponenten

- **uuid** ∈ 𝒰: technische Identität des Lastfalls als Aggregat,
- **bemessungssituation** ∈ 𝓢: die zugeordnete Bemessungssituation
  (persistent / transient / accidental / seismic),
- **leiteinwirkung** ∈ 𝓔: die im Lastfall dominierende Einwirkung
  (im Sinne der EN-1990-Kombinations-Regel das ψ₀-unabhängig
  voll angesetzte Glied),
- **begleiteinwirkungen** ⊂ 𝓔, endlich (möglicherweise leer): die
  weiteren simultan wirkenden Einwirkungen,
- **einwirkungs_anordnung** ∈ 𝓥𝓔: geometrische Verteilung jeder
  Einwirkung des Lastfalls im W-System,
- **inzidenz** ∈ 𝓘: Zuordnung jeder Einwirkung zu Bauteilen über
  deren UUIDs,
- **bezeichnung** ∈ String ∪ {⊥}: freier Anzeigename
  (optional, z. B. „LF1 — Eigenlast + Schnee als Leit“).

Die Gesamt-Einwirkungsmenge des Lastfalls ist

```
E(ℓ) := {leiteinwirkung} ∪ begleiteinwirkungen.
```

### Konsistenzbedingungen

(L1) **Leiteinwirkung disjunkt von Begleiteinwirkungen**:
`leiteinwirkung ∉ begleiteinwirkungen`. Die Leiteinwirkung tritt
genau einmal im Lastfall auf und ist nicht Bestandteil der
Begleitmenge.

(L2) **Anordnungs-Vollständigkeit**: für jede Einwirkung
e ∈ E(ℓ) ist `einwirkungs_anordnung(e)` definiert und
nicht-leer. Es gibt keine Einwirkung im Lastfall ohne
geometrische Verteilung.

(L3) **Inzidenz-Vollständigkeit**: für jede Einwirkung
e ∈ E(ℓ) ist die Inzidenzmenge
`{u ∈ 𝒰 | (e, u) ∈ inzidenz}` nicht-leer. Jede Einwirkung
wirkt auf mindestens ein Bauteil.

(L4) **Bauteil-Existenz**: jede in `inzidenz` referenzierte UUID
ist die UUID eines existierenden Bauteils im Modell
(b ∈ 𝓑). Inzidenzen auf nicht-existierende Bauteile sind
unzulässig.

(L5) **Physikalische Verträglichkeit** (zugesichert, nicht
formal geprüft): die Einwirkungen in E(ℓ) können nach
fachlicher Beurteilung **gleichzeitig** auftreten. Logisch
unverträgliche Kombinationen (z. B. Vollschnee und
Vollsonneneinstrahlung am selben Punkt zum selben Zeitpunkt)
sind ausgeschlossen. Diese Bedingung folgt der SIA-260-Lesart
„physikalisch verträgliche Anordnung von simultan auftretenden
Einwirkungen“ und wird in der App **zugesichert**, nicht
mechanisch validiert; eine formale Verträglichkeits-Prüfung
gehört in die Bemessungs-Schicht.

(L6) **Konsistenz mit Bemessungssituation** (zugesichert, nicht
formal geprüft): die Kategorie-Mischung in E(ℓ) ist mit der
gewählten Bemessungssituation kompatibel im Sinne der
EN-1990-/SIA-260-Klassifikation:

| Bemessungssituation | zulässige Kategorien (typisch) |
|---|---|
| persistent | G, Q |
| transient | G, Q (mit transient-spezifischen ψ-Werten) |
| accidental | G, Q, **mindestens ein** A |
| seismic | G, Q, **mindestens ein** A_E |

Auch diese Bedingung ist zugesichert; die formale Prüfung
gehört in die Bemessungs-Schicht (Lastkombinations-Generator).

## Wohldefiniertheit

- **Existenz**: für jeden konkreten Tragwerks-Nachweis lässt sich
  ein Lastfall als obiges Tupel erfassen. Mindestkonfiguration:
  Eigenlast als Leiteinwirkung, keine Begleiteinwirkungen,
  Bemessungssituation `persistent`, Anordnung als
  volumenverteilte Schwerkraft auf allen Bauteilen, Inzidenz auf
  alle Bauteile des Tragwerks.

- **Eindeutigkeit der Identität**: die UUID des Lastfalls ist
  unabhängig von den UUIDs der referenzierten Bauteile und
  unabhängig von den semantischen Identitäten der Einwirkungen.
  Mehrere Lastfälle können dieselbe Einwirkungsmenge bei
  unterschiedlicher Anordnung oder Inzidenz tragen
  (z. B. „Wind aus Süd“ und „Wind aus Nord“ als zwei Lastfälle
  mit gleicher Einwirkung „Wind“, aber unterschiedlicher
  α-Anordnung).

- **Mengen-Unsortiertheit**: `begleiteinwirkungen` ist als Menge
  unsortiert; alle Aussagen über den Lastfall sind invariant
  unter Permutation der Begleiteinwirkungen. Die Auszeichnung
  der Leiteinwirkung erfolgt durch den separaten Feldnamen, nicht
  durch Reihenfolge.

- **Repräsentanten der Anordnung**: verschiedene parametrische
  Repräsentationen derselben geometrischen Verteilung
  (z. B. Polygonaler Verlauf einer Linienlast mit
  kombinatorisch äquivalenten Eckpunktrotationen) führen auf
  denselben Lastfall. Die Wohldefiniertheit unter solchen
  Repräsentanten-Wechseln folgt aus der zugrundeliegenden
  Polygon- bzw. Verteilungs-Definition.

- **Mehrere Lastfälle pro Bemessungssituation**: zulässig und
  Norm-üblich — die Bemessungssituation ist ein Klassifikations-
  Wert; pro Situation existieren mehrere Lastfälle (verschiedene
  Leiteinwirkungen, verschiedene Anordnungen).

- **Lastkombination ist nicht Lastfall**: die Überlagerung
  mehrerer Lastfälle mit γ- und ψ-Faktoren zum Bemessungswert
  E_d ist eine **Operation** über der Menge der Lastfälle, nicht
  selbst ein Lastfall. Sie wird in einem getrennten Aggregat
  `lastkombination` (Folgeeintrag) geführt.

- **Nicht-Zirkularität**: die Definition stützt sich auf die
  bereits definierten Begriffe `bauteil`, `uuid`,
  `weltkoordinatensystem`, `toleranzen`. Sie verweist auf
  `einwirkung`, `bemessungssituation`, `lastkombination`,
  `tragwerk`, `auflager`, `statisches_system`, `gefaehrdungsbild`
  ausschließlich abgrenzend (Frontmatter-Feld `abgrenzung_zu`).
  Die Beziehung zum Tragwerk ist **invertiert**: der Lastfall
  wird im Tragwerks-Tupel (B, V, A, L) als Bestandteil der
  L-Komponente geführt; das Tragwerk setzt den Lastfall
  voraus, nicht umgekehrt. Damit ist der Aufbau zirkelfrei.

## Erläuterung (nicht normativ)

### Begriffsfamilie: Einwirkung — Bemessungssituation — Lastfall — Lastkombination

Das Sicherheitskonzept der EN 1990 / SIA 260 bildet eine
vier-schichtige Begriffsfamilie. Die App führt jede Schicht als
eigenständigen Begriff; im aktuellen Glossarstand ist nur die
Schicht 3 (Lastfall, dieser Eintrag) angelegt, die übrigen drei
folgen als Folgearbeit (siehe `HG_KONVENTIONEN.md` §6.A).

| Schicht | Begriff | Inhalt | Eigener App-Glossareintrag |
|---|---|---|---|
| 1 | **Einwirkung** (`einwirkung`, Folgeeintrag) | Ursache mechanischer Beanspruchung am Tragwerk: Kraft, aufgezwungene Verformung, indirekte Einwirkung. Klassifiziert nach zeitlicher Veränderlichkeit (G ständig, Q veränderlich, A außergewöhnlich, A_E Erdbeben). | folgt |
| 2 | **Bemessungssituation** (`bemessungssituation`, Folgeeintrag) | Zustand des Tragwerks im Zeitraum eines Nachweises: persistent, transient, accidental, seismic (EN 1990 §3.2). Trägt die Gesamtheit der zu berücksichtigenden Einwirkungen für einen Lebenszustand. | folgt |
| 3 | **Lastfall** (dieser Eintrag) | Physikalisch verträgliche Anordnung gleichzeitig wirkender Einwirkungen für einen bestimmten rechnerischen Nachweis. Pro Bemessungssituation existieren mehrere Lastfälle. | **angelegt** |
| 4 | **Lastkombination** (`lastkombination`, Folgeeintrag) | Mathematische Überlagerung mehrerer Lastfälle bzw. Einwirkungen mit Teilsicherheitsbeiwerten γ und Kombinationsbeiwerten ψ zur Erzeugung des Bemessungswerts der Einwirkungs-Auswirkung E_d (Grundkombination, häufige Kombination, quasi-ständige Kombination, außergewöhnliche Kombination, Erdbeben-Kombination). | folgt |

**Wichtig — keine Synonymie zwischen den Schichten.** „Einwirkung“
und „Lastkombination“ werden im praktischen Sprachgebrauch
regelmäßig mit „Lastfall“ vermischt („Lastfallkombination“,
„load case combination“); diese Vermischung ist nicht durch die
Norm gedeckt und wird in der App abgelehnt. Die App führt die
vier Schichten als getrennte Aggregate mit eigenen UUIDs und
eigenen Konsistenzbedingungen.

### Einwirkungs-Klassifikation (Schicht 1, zur Orientierung)

Die Einwirkungen — die Bestandteile eines Lastfalls — werden nach
EN 1990 §4.1.1 bzw. SIA 260 §4 in vier Kategorien klassifiziert:

| Kategorie | Symbol | Charakteristik | Beispiele im Holzbau-Hochbau |
|---|---|---|---|
| Ständig | **G** | über die gesamte Nutzungsdauer mit vernachlässigbarer Veränderung | Eigengewicht tragender Bauteile, Eigengewicht nichttragender Bauteile, Auflasten durch Bodenaufbau, Vorspannung P |
| Veränderlich | **Q** | zeitlich oder örtlich variabel, nicht ständig | Nutzlast Wohnen / Büro / Lager, Schneelast, Windlast (Druck/Sog), Verkehrslast, Temperatur-Einwirkungen |
| Außergewöhnlich | **A** | kurze Dauer, niedrige Eintretens-Wahrscheinlichkeit, große Schäden | Anprall, Explosion, außergewöhnliche Brandlasten |
| Erdbeben | **A_E** | seismische Einwirkung (EN 1998 / SIA 261 §16) | Bemessungs-Erdbeben in den Schweizer Zonen Z1a–Z3b |

Erweiterte Klassifikation (EN 1990 §4.1.2) nach Ort
(fest/frei), Variation (statisch/dynamisch) und Natur (direkt =
Kraft / indirekt = aufgezwungene Verformung) ist
bemessungs-strukturell, nicht lastfall-bildend.

### Typische Holzbau-Hochbau-Einwirkungen (Praxis-Standard, nicht Norm-Pflicht)

In der Praxis des Holzbau-Hochbaus treten typischerweise auf:

- Eigenlast G_k (tragende Bauteile),
- Eigenlast G_k,Aufbau (Dachaufbau, Estrich, Trockenbau),
- Nutzlast Q_k (Wohnen, Büro, Versammlung, Lager — nach
  EN 1991-1-1 / SIA 261 §3 mit Kategorie und charakteristischem
  Wert),
- Schneelast s_k (EN 1991-1-3 / SIA 261 §5; in den Schweizer
  Alpen deutlich höher als im DACH-Tiefland),
- Windlast w_k (EN 1991-1-4 / SIA 261 §6, Druck und Sog, Zonen-
  und Geländeabhängig),
- Temperatur-Einwirkung (EN 1991-1-5 / SIA 261 §7, im Holzbau
  oft nicht bemessungsrelevant),
- ggf. Erdbeben-Einwirkung A_E (EN 1998 / SIA 261 §16, im
  schweizerischen Mittelland und Alpenrand bemessungsrelevant).

Diese Liste ist **Praxis-Standard, nicht Norm-Pflicht**: weder
EN 1990 noch SIA 260 schreiben eine abschließende Mindestmenge an
Lastfällen vor; beide verlangen lediglich, dass für alle relevanten
Bemessungssituationen Lastfälle betrachtet werden.

### Historische Lastfall-Klassen H und HZ (nicht-normativ)

Die alte DIN 1055 (insbesondere DIN 1055-100:2001-03, durch den
Eurocode-Apparat zurückgezogen) operierte mit deterministischen
Lastfall-Klassen aus dem alten globalen Sicherheitskonzept
(ein einziger Globalfaktor ν):

- **Lastfall H** (Hauptlastfall): Eigenlast plus eine
  veränderliche Hauptlast (häufige Beanspruchungs-Situation).
- **Lastfall HZ** (Hauptlastfall mit Zusatzlast): Eigenlast plus
  Haupt- plus Zusatzlasten (selten zusammen auftretend; zulässige
  Spannungen durften ggf. um einen Faktor erhöht werden).

Diese H/HZ-Klassifikation ist mit der Einführung des
semiprobabilistischen Sicherheitskonzepts (γ_G, γ_Q, ψ-Faktoren)
**abgelöst**. Praktiker verwenden die H/HZ-Bezeichnungen noch im
Bestand und im Brückenbau (DIN 1072) — für die App-Modellierung
sind sie historisch, nicht normativ. Die App führt sie nicht als
Lastfall-Subtypen, sondern referenziert sie ausschließlich im
Erläuterungsblock zur historischen Einordnung.

### Lastfall vs. statisches System

Der **Lastfall** ist die nachweisbezogene Anordnung der Einwirkungen
am bauteilbezogenen Tragwerk in W. Das **statische System** ist die
darüber gelegte bemessungstechnische Idealisierung (Punkt-Stab-Modell
mit Knoten, Stabachsen, Gelenkfreiheiten, Auflagerklassen, Lastfall-
Reduktion auf Stab-Einwirkungen). Der Lastfall trägt die Eingabe-
Information vor der Idealisierung; das statische System trägt die
Modell-Lasten nach Idealisierung. Beide stehen in einer
Reduktions-Relation, sind aber **nicht identisch**.

### Gefährdungsbild (Schweizer Spezifikum, ohne eigenen App-Eintrag)

SIA 260 §4 schaltet zwischen Nutzungsvereinbarung und Bemessungs-
situation eine Stufe der Risiko-Szenarien-Beschreibung ein, das
**Gefährdungsbild** (z. B. „Wintersturm mit gleichzeitigem
Vollschnee“, „Vollnutzung bei gleichzeitigem Sommer-Maximum“).
Aus dem Gefährdungsbild wird die Bemessungssituation abgeleitet,
und aus der Bemessungssituation der Lastfall.

EN 1990 trägt keinen entsprechenden Begriff; die Risiko-Szenarien-
Beschreibung ist dort implizit in der Bemessungssituation
enthalten. Die App führt das Gefährdungsbild **nicht** als eigenen
Glossarbegriff (`abgrenzung_zu`, Kategorie (D) nach
`HG_KONVENTIONEN.md` §6 — Korpus-Begriff dauerhaft ohne eigenen
Eintrag), kann ihn aber bei Bedarf später als SIA-260-spezifischen
Workflow-Begriff nachziehen, falls die App Nutzungsvereinbarung
und Projektbasis als eigene Schichten abbildet.

### IFC-Mapping (Hauptlinien)

| App-Konzept | IFC 4.3 Pendant |
|---|---|
| Einwirkung (Schicht 1) als physikalische Ursache | `IfcStructuralAction` (abstrakt) mit Subtypen `IfcStructuralPointAction` / `IfcStructuralCurveAction` / `IfcStructuralSurfaceAction`; trägt einen `IfcStructuralLoad` über das Attribut `AppliedLoad` |
| Lastwert | `IfcStructuralLoad`-Subtyp (`IfcStructuralLoadSingleForce` / `IfcStructuralLoadLinearForce` / `IfcStructuralLoadPlanarForce` / `IfcStructuralLoadTemperature` etc.) |
| Bemessungssituation (Schicht 2) | im IFC-Schema implizit; ggf. über `IfcLoadGroupTypeEnum` + Properties auf der enthaltenden `IfcStructuralLoadGroup` |
| **Lastfall (Schicht 3, dieser Eintrag)** | `IfcStructuralLoadCase` (konkreter Subtyp von `IfcStructuralLoadGroup`); trägt eigene GlobalId und das Attribut `SelfWeightCoefficients` |
| Lastkombination (Schicht 4) | `IfcStructuralLoadGroup` mit `PredefinedType = LOAD_COMBINATION` |
| Inzidenz Einwirkung ↔ Bauteil | `IfcRelConnectsStructuralActivity` zwischen `IfcStructuralAction` und `IfcStructuralItem` (Member/Connection) |
| übergeordneter Bemessungs-Container | `IfcStructuralAnalysisModel` (umschließt Tragwerks-Pendant + alle Lasten/Aktionen/Gruppen) |

Die IFC-Trennung von **Lastwert** (`IfcStructuralLoad`) und
**Wirkung am Modell** (`IfcStructuralAction`) ist in der Norm-
Sprache implizit, in der App-Modellierung aber wichtig: ein
Lastwert allein ist keine Einwirkung — erst die Wirkung an einem
geometrischen Träger macht ihn zur Einwirkung im Sinne der
Schicht 1. Die App folgt dieser Trennung im Folgeeintrag
`einwirkung`.

IFC kollabiert die App-Schichten 2/3/4 in eine einzige Entität
`IfcStructuralLoadGroup` mit `PredefinedType`-Diskriminator. Beim
IFC-Export trägt die App den Lastfall als `IfcStructuralLoadCase`
(konkreter Subtyp), die Lastkombination als
`IfcStructuralLoadGroup` mit `PredefinedType = LOAD_COMBINATION`,
und die Bemessungssituation als Property auf der Gruppe.

Das BTLx-Schema (design2machine) trägt **keine eigene Lastfall-
Entität**; Lastbezüge erscheinen dort nicht — analog zur Auflager-
und Verbindungs-Seite (siehe `hg_auflager.md`, `hg_verbindung.md`).

### Lastfall vs. Tragwerk

Der Lastfall ist **Bestandteil eines Tragwerks** — in der
Tragwerks-Tupel-Repräsentation (B, V, A, L) nach
`hg_tragwerk.md` ist L die endliche Menge der zu
berücksichtigenden Lastfälle. Die Beziehung ist asymmetrisch:
das Tragwerk setzt den Lastfall in seiner L-Komponente voraus;
der Lastfall setzt das Tragwerk nicht voraus, sondern referenziert
lediglich Bauteile (über `inzidenz`). Ein Lastfall kann formal
auch ohne Tragwerks-Kontext existieren (Eingangs-Bibliothek für
spätere Tragwerks-Modellierung); im typischen Modellzustand
sitzt er aber als Element von L in einem Tragwerk.

## Beziehungen

- **Oberbegriff**: derzeit `null` (analog `verbindung`,
  `tragwerk`, `auflager`). Eine fachliche Spezialisierungs-Linie
  aus einem Oberbegriff heraus existiert nicht; die Einwirkung
  (Schicht 1) ist nicht Oberbegriff des Lastfalls (Schicht 3),
  sondern Nachbar-Begriff.

- **Bestandteile (partitiv)**:
  - **Leiteinwirkung** (Element von 𝓔; eigener Eintrag
    `einwirkung` folgt).
  - **Begleiteinwirkungen** (endliche Menge in 𝓔).
  - **Einwirkungs-Anordnung** (geometrische Verteilung pro
    Einwirkung im W-System).
  - **Inzidenz** (Zuordnung Einwirkung ↔ Bauteil-UUIDs).
  - **Bemessungssituations-Zuordnung** (Klassifikations-Wert
    aus 𝓢; eigener Eintrag `bemessungssituation` folgt).

- **Spezialisierungen nach Bemessungssituation** (Folgearbeit,
  falls didaktisch nützlich): persistente Lastfälle, transiente
  Lastfälle, außergewöhnliche Lastfälle, Erdbeben-Lastfälle. Im
  aktuellen App-Modell als Wert der `bemessungssituation`-
  Komponente aufgelöst, nicht als Subtyp-Hierarchie.

- **Verwendung**:
  - Bestandteil eines **Tragwerks** (`tragwerk`): in der
    Tupel-Repräsentation (B, V, A, L) ist L die Menge der
    Lastfälle.
  - Eingang einer **Lastkombination** (`lastkombination`,
    Folgeeintrag): die Lastkombination überlagert mehrere
    Lastfälle mit γ- und ψ-Faktoren zum Bemessungswert E_d.

- **Abgrenzung**:
  - **Einwirkung** (`einwirkung`, Folgeeintrag): Schicht-1-
    Begriff; eine Einwirkung ist Bestandteil eines Lastfalls,
    nicht selbst ein Lastfall. Die Einwirkung ist nicht
    Oberbegriff des Lastfalls und ausdrücklich nicht Synonym.
  - **Bemessungssituation** (`bemessungssituation`,
    Folgeeintrag): Schicht-2-Begriff; ein Klassifikationswert,
    der den Lastfall einem Tragwerks-Lebenszustand zuordnet.
    Mehrere Lastfälle pro Bemessungssituation; ein Lastfall
    gehört zu genau einer Bemessungssituation.
  - **Lastkombination** / **Einwirkungskombination**
    (`lastkombination`, Folgeeintrag): Schicht-4-Begriff;
    rechnerische Überlagerung mehrerer Lastfälle. Eine
    Lastkombination ist eine Operation über der Menge der
    Lastfälle, nicht selbst ein Lastfall.
  - **Gefährdungsbild** (Korpus-Begriff, kein eigener Eintrag
    geplant; Kategorie (D) nach `HG_KONVENTIONEN.md` §6):
    Schweizer Spezifikum aus SIA 260 §4; eine Risiko-Szenarien-
    Beschreibung, die der Bemessungssituation vorgelagert ist.
    Ohne Pendant in EN 1990.
  - **Lastannahme** (Korpus-Begriff): synonym mit
    Einwirkung (Schicht 1), nicht mit Lastfall (Schicht 3); in
    `abgelehnte_benennungen` geführt.
  - **Tragwerk** (`tragwerk`): das übergeordnete Aggregat, in
    dessen L-Komponente der Lastfall Element ist. Lastfall ist
    Bestandteil eines Tragwerks; er ist nicht selbst Tragwerk.
  - **Auflager** (`auflager`): Lastpfad-Ende. Auflager und
    Lastfall sind beide Bestandteile des Tragwerks-Tupels
    (Komponenten A und L), aber unterschiedliche Aggregate
    mit unterschiedlicher Substanz: Auflager trägt
    geometrische Manifestation + Wertigkeit pro Freiheitsgrad,
    Lastfall trägt Einwirkungs-Anordnung + Bauteil-Inzidenz.
  - **Bauteil** (`bauteil`): das Trägerobjekt der Einwirkungs-
    Inzidenz. Bauteile werden im Lastfall ausschließlich über
    UUID referenziert (Foreign-Key-Regel); ein Lastfall ist
    kein Bauteil und enthält kein Bauteil partitiv.
  - **Statisches System** (`statisches_system`, Folgeeintrag):
    die bemessungstechnische Idealisierung des Tragwerks mit
    reduzierten Stab-Einwirkungen. Der Lastfall ist die
    nachweisbezogene Eingangs-Anordnung am bauteilbezogenen
    Tragwerk; das statische System trägt die daraus
    abgeleiteten reduzierten Modell-Lasten.

## Implementierungshinweis

Datentyp (Domänen-Schicht, Kotlin, Schicht
`domain.aggregat.lastfall`):

```kotlin
package domain.aggregat.lastfall

import java.util.UUID

/** Einwirkungs-Kategorie nach EN 1990 §4.1.1 / SIA 260 §4. */
enum class Einwirkungskategorie { STAENDIG_G, VERAENDERLICH_Q, AUSSERGEWOEHNLICH_A, ERDBEBEN_AE }

/** Bemessungssituation nach EN 1990 §3.2. */
enum class Bemessungssituation { PERSISTENT, TRANSIENT, ACCIDENTAL, SEISMIC }

/**
 * Einwirkung (Schicht 1) — Folgeeintrag `einwirkung`.
 * Hier nur als Vorwärts-Referenz auf eigene Identität und Kategorie.
 */
data class Einwirkung(
    val uuid: UUID,
    val kategorie: Einwirkungskategorie,
    val bezeichnung: String
    /* + charakteristischer Wert, semantische Identität — Folgearbeit */
)

/** Geometrische Verteilung einer Einwirkung im W-System (Folgearbeit). */
sealed interface EinwirkungsVerteilung {
    /* Punkt-, Linien-, Flächen-, Volumen-Verteilung mit Wert+Richtung
     * pro Träger; im Folgeeintrag `einwirkung` ausformuliert. */
}

/** Inzidenz einer Einwirkung zu einer Bauteil-Stelle. */
data class EinwirkungsInzidenz(
    val einwirkungUuid: UUID,
    val bauteilUuid: UUID
    /* + optional: Bauteilflaeche/Kante/Punkt-Selektor — Folgearbeit */
)

/**
 * Lastfall (Schicht 3): Aggregat aus physikalisch verträglicher Anordnung
 * gleichzeitig wirkender Einwirkungen für einen bestimmten Nachweis.
 *
 * Glossar: hg_lastfall.md
 *
 * NICHT Subtyp von Element. Eigene Aggregat-Klasse, analog Verbindung,
 * Tragwerk, Auflager.
 *
 * IFC: IfcStructuralLoadCase (Subtyp von IfcStructuralLoadGroup).
 * BTLx: keine eigene Entität.
 */
data class Lastfall(
    val uuid: UUID,
    val bemessungssituation: Bemessungssituation,
    val leiteinwirkung: Einwirkung,
    val begleiteinwirkungen: Set<Einwirkung>,
    val einwirkungsAnordnung: Map<UUID, EinwirkungsVerteilung>,    // EinwirkungUuid -> Verteilung
    val inzidenz: Set<EinwirkungsInzidenz>,
    val bezeichnung: String? = null
) {
    init {
        // L1. leiteinwirkung ∉ begleiteinwirkungen
        // L2. ∀ e ∈ E(ℓ): einwirkungsAnordnung[e.uuid] != null
        // L3. ∀ e ∈ E(ℓ): { i ∈ inzidenz | i.einwirkungUuid == e.uuid }.isNotEmpty()
        // L4. Modell-Validierung: jede inzidenz.bauteilUuid existiert im Modell
        // L5. physikalische Verträglichkeit (zugesichert, nicht geprüft)
        // L6. Kategorie-Konsistenz mit Bemessungssituation (zugesichert)
    }

    /** Gesamt-Einwirkungsmenge E(ℓ). */
    fun einwirkungen(): Set<Einwirkung> = begleiteinwirkungen + leiteinwirkung
}
```

- **Einheit**: Längen in mm (Double); Lasten in N (Einzelkraft),
  N/m (Linienlast), N/m² (Flächenlast); Temperatur in K
  (Differenz) bzw. °C (absoluter Wert mit dokumentierter
  Referenz); Winkel intern in Radiant. Alle Last-Werte
  konsistent SI.

- **Identität**: `uuid` ist Pflicht und eigenständig (eigene UUID
  des Aggregats; nicht UUID eines Bauteils, einer Einwirkung
  oder einer Bemessungssituation).

- **Foreign-Key-Regel**: Bauteil-Bezüge in `inzidenz` und in
  späteren Lastpfad-Aussagen referenzieren ausschließlich Bauteil-
  UUIDs (Memory `project_bauteil_identifikation`). Einwirkungs-
  Bezüge in `inzidenz` und in `einwirkungsAnordnung`
  referenzieren ausschließlich Einwirkungs-UUIDs.

- **Invarianten** (in der Aggregat-Fabrikfunktion
  `Lastfall.bilde(modell: Modell, …)` geprüft; bei Verletzung
  `Resultat.Fehler`, niemals Exception):
  1. `leiteinwirkung !in begleiteinwirkungen` ⇒ sonst
     `Entartet.LeiteinwirkungDoppelt` (L1).
  2. Anordnung für jede Einwirkung definiert ⇒ sonst
     `Entartet.AnordnungUnvollstaendig` (L2).
  3. Inzidenz für jede Einwirkung nicht-leer ⇒ sonst
     `Entartet.InzidenzLeer` (L3).
  4. Jede in `inzidenz` referenzierte Bauteil-UUID existiert im
     Modell ⇒ sonst `Entartet.BauteilUnbekannt` (L4).
  5. **Physikalische Verträglichkeit (L5)** und **Kategorie-
     Konsistenz mit Bemessungssituation (L6)**: zugesichert,
     **nicht** im `init` geprüft. Formale Prüfung erfolgt in der
     Bemessungs-Schicht (Lastkombinations-Generator).

- **Edge Cases**:
  - **Lastfall mit leerer Begleitmenge**: zulässig (reine
    Eigenlast-Situation; Leiteinwirkung = Eigenlast,
    `begleiteinwirkungen = emptySet()`).
  - **Außergewöhnlicher Lastfall**: `bemessungssituation =
    ACCIDENTAL` mit mindestens einer A-Einwirkung in E(ℓ);
    typisch: Anprall als Leiteinwirkung, Eigenlast und
    quasi-ständige Nutzlast als Begleiteinwirkungen.
  - **Erdbeben-Lastfall**: `bemessungssituation = SEISMIC` mit
    mindestens einer A_E-Einwirkung; in der Schweiz nach
    SIA 261 §16 mit zonen- und bauwerksklassenabhängigen Werten.
  - **Mehrere Lastfälle mit derselben Einwirkungsmenge**:
    zulässig bei unterschiedlicher Anordnung oder Inzidenz
    (z. B. „Wind aus Süd“ und „Wind aus Nord“).
  - **Lastfall ohne Tragwerk**: formal zulässig (Eingangs-
    Bibliothek); im typischen Modellzustand sitzt der Lastfall
    in der L-Komponente eines Tragwerks.
  - **Vermischung Schicht 3 / Schicht 4 ablehnen**: ein
    Aufruf-Code, der einen Lastfall als „Lastkombination mit
    γ = 1“ konstruieren möchte, wird abgewiesen — der dafür
    vorgesehene Aggregat-Typ ist `Lastkombination` (Folgearbeit),
    nicht `Lastfall`.

- **Toleranz-Anwendung** (siehe `hg_toleranzen.md` §4):
  - Im Lastfall selbst keine geometrischen Toleranzen, da die
    geometrischen Träger in `EinwirkungsVerteilung` und
    `EinwirkungsInzidenz` ihre eigene Toleranz-Anwendung
    mitbringen (`LAENGE_EPS` für Bauteil-Inzidenz-Punkte).
  - Last-Werte (N, N/m, N/m²) tragen keine geometrischen
    Toleranzen; ihre numerische Toleranz ist Sache der
    Bemessungs-Schicht.

- **IFC-Export-Mapping**:
  - `Lastfall` → `IfcStructuralLoadCase` (Subtyp von
    `IfcStructuralLoadGroup`) mit eigener `GlobalId` aus
    `uuid`; `SelfWeightCoefficients` aus Eigenlast-Anordnung,
    falls dargestellt.
  - `bemessungssituation` → Property auf der enthaltenden
    `IfcStructuralLoadGroup` oder im umschließenden
    `IfcStructuralAnalysisModel`.
  - `leiteinwirkung` und jede `e ∈ begleiteinwirkungen` →
    `IfcStructuralAction` (Point/Curve/Surface je nach
    Verteilungs-Dimension) mit `AppliedLoad` als
    passender `IfcStructuralLoad`-Subtyp.
  - `inzidenz` → `IfcRelConnectsStructuralActivity` zwischen
    `IfcStructuralAction` und `IfcStructuralItem` des Bauteils.
  - Eine spätere `Lastkombination` (Folgearbeit) wird als
    `IfcStructuralLoadGroup` mit
    `PredefinedType = LOAD_COMBINATION` exportiert und
    referenziert die enthaltenen `IfcStructuralLoadCase`-
    Instanzen.

- **BTLx-Export**: keine eigene Entität; Lastfälle werden beim
  BTLx-Export nicht ausgegeben (BTLx ist Maschinen-Format für
  die zerspanende Vorfertigung, nicht für die Bemessungs-Schicht).

- **Abgeleitete Eigenschaften** (als Funktionen, keine Felder):
  - `einwirkungen(): Set<Einwirkung>` — Vereinigung
    `{leiteinwirkung} ∪ begleiteinwirkungen`.
  - `bauteilUuids(): Set<UUID>` — Menge aller Bauteil-UUIDs in
    `inzidenz`.
  - `enthaeltKategorie(k: Einwirkungskategorie): Boolean` —
    Existenz einer Einwirkung der Kategorie k in E(ℓ).
  - `istAussergewoehnlich(): Boolean` —
    `bemessungssituation == ACCIDENTAL`.
  - `istErdbebenLastfall(): Boolean` —
    `bemessungssituation == SEISMIC`.

- **Bezeichner-Konvention** (siehe `docs/_CODE_KONVENTIONEN.md`):
  Domänen-Klasse heißt `Lastfall` (deutsch, Glossarbegriff).
  „Belastungsfall“, „Lastannahme“ und englische Pendants
  (`load case`, `action`) werden weder als Klassen noch als
  KDoc-Stichworte geführt; sie sind ausdrücklich als
  abgelehnte Benennungen markiert.

## Quellen

**Primär (normativ):**

- SIA 260:2013, „Grundlagen der Projektierung von Tragwerken“,
  Schweizerischer Ingenieur- und Architektenverein, Zürich,
  Abschnitt 4.4 (Bemessungssituationen und Lastfälle).
- DIN EN 1990:2010-12, „Eurocode: Grundlagen der
  Tragwerksplanung“, Abschnitte 1.5 (Begriffe), 3.2
  (Bemessungssituationen) und 6 (Bemessungswerte).
- DIN 1055-100:2001-03 (zurückgezogen), „Einwirkungen auf
  Tragwerke — Teil 100: Grundlagen der Tragwerksplanung“ —
  historische Definition.
- DIN EN 1991-1-1:2010-12 bis DIN EN 1991-1-7, „Eurocode 1:
  Einwirkungen auf Tragwerke“ (Wichten/Eigengewicht/Nutzlasten,
  Brand, Schnee, Wind, Temperatur, außergewöhnliche
  Einwirkungen).
- SIA 261:2020 + SIA 261/1:2020, „Einwirkungen auf Tragwerke“
  und „Ergänzende Festlegungen“, Schweizerischer Ingenieur-
  und Architektenverein.
- ISO 16739-1:2024, „Industry Foundation Classes (IFC) — Part 1:
  Data schema“ (IFC 4.3.2), Structural-Analysis-Domain,
  insbesondere `IfcStructuralLoadCase`, `IfcStructuralLoadGroup`,
  `IfcStructuralAction`, `IfcStructuralLoad`.

**Sekundär:**

- Petersen, Chr.: *Statik und Stabilität der Baukonstruktionen.*
  Vieweg, Braunschweig (mehrfache Auflagen).
- Schneider, K.-J.; Albert, A.: *Bautabellen für Ingenieure.*
  26. Auflage, Bundesanzeiger Verlag, Köln 2024.
- Mönck, W.; Rug, W.: *Holzbau – Bemessung und Konstruktion.*
  16. Auflage, Beuth, Berlin 2015, Kap. 4.
- Blass, H. J.; Sandhaas, C.: *Ingenieurholzbau – Grundlagen
  der Bemessung.* KIT Scientific Publishing, Karlsruhe 2016,
  Kap. 4.
- Marti, P.: *Tragwerksentwurf.* ETH Zürich, Institut für
  Baustatik und Konstruktion (Lehrunterlagen, archiv.ibk.ethz.ch).
- SIA-D 0211, „Erläuterungen zur Tragwerksnorm SIA 260“, sgeb.ch.
- Lüchinger, P.: „Konzept der Tragwerksnormen SIA“, Forum
  Holzbau.

**Korpus (nicht autoritativ):**

- Wikipedia, Lemma „Lastfall“ (abgerufen 2026-05-14):
  historische Lastfall-Klassen H und HZ.
- mauerwerksbau-lehre.de, „Einwirkungskombinationen“ (abgerufen
  2026-05-14).
- drvollenweiderag.ch, „Gefährdungsbild und Bemessungssituation“
  (abgerufen 2026-05-14).
- structuralbasics.com, „Design situations EN 1990“
  (abgerufen 2026-05-14).
- standards.buildingsmart.org, IFC-4.3-Lexikon, Einträge
  `IfcStructuralLoadCase`, `IfcStructuralLoadGroup`,
  `IfcStructuralAction` (abgerufen 2026-05-14).
- Recherche-Bericht: `docs/recherche/2026-05-14_hg_lastfall.md`.
