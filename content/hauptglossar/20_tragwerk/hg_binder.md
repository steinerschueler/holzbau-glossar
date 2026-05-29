---
id: binder
benennung: Binder
synonyme: [Dachbinder, Holzbinder]
abgelehnte_benennungen: ["truss", "binder", "girder", "roof truss", "trussed rafter", "nail-plate truss", "glulam beam", Dachträger, Dachstuhlbinder, Bindebalken]
oberbegriff: bauteilgruppe
begriffstyp: aggregat
voraussetzungen: [bauteilgruppe, bauteil, verbindung, uuid, lokales_koordinatensystem, weltkoordinatensystem, ebene, polyeder, toleranzen]
abgrenzung_zu: [bauteilgruppe, tragwerk, bauteil, sparren, pfette, verbindung, dach, dachflaeche, bauteilachse, nagelplattenbinder, sparrenbinder, pfettenbinder, bsh_binder, fachwerkbinder, vollwandbinder, hauptbinder, kehlbalkenbinder, polygonalbinder, hetzer_binder, binderdach]
status: entwurf
subglossar_pendant: notwendig
quellen_primär:
  - "DIN EN 14250:2010-05 'Holzbauwerke – Produktanforderungen an vorgefertigte tragende Bauteile mit Nagelplattenverbindungen' [einsicht: snippet, ANSI-Webstore / dinmedia.de]: Anwendungsbereich umfasst vorgefertigte tragende Bauteile (Fachwerkträger für Dächer, Wände und Decken, sowie Rahmen, zusammengesetzte Träger) aus festigkeitssortiertem Bauholz nach DIN EN 14081-1 mit oder ohne Keilzinkenverbindungen unter Verwendung von Nagelplatten; Fachwerkträger bis 35 m Länge, sonstige vorgefertigte tragende Bauteile mit Spannweiten bis 12 m. Die Norm definiert Produktanforderungen am Sub-Typ Nagelplattenbinder, nicht den Oberbegriff Binder."
  - "DIN EN 1995-1-1:2010-12 (Eurocode 5), Abschnitt 9 (Aussteifende Scheiben, zusammengesetzte Bauteile) und Abschnitt 10 (Konstruktive Durchbildung) — Binder als vorausgesetzter Berufsbegriff für mehrteilig zusammengesetzte Tragglieder; keine geschlossene Begriffsdefinition."
  - "DIN EN 14080:2013-09 'Holzbauwerke – Brettschichtholz und Balkenschichtholz – Anforderungen' — Produktnorm für die werkstoffliche Grundlage des Brettschichtholz-Binders; keine Definition des Begriffs Binder selbst."
  - "DIN 1052:2008-12, Abschnitt 8 und 12 — Binder als vorausgesetzter Tragwerks-Begriff in Kontexten wie 'Binderabstand', 'Hauptbinder', 'Pfettenbinder'; keine geschlossene Begriffsdefinition."
  - "SIA 265:2021 'Holzbau', Schweizerischer Ingenieur- und Architektenverein, Abschnitt 5 (Konstruktive Durchbildung) — Binder als vorausgesetzter Berufsbegriff; keine geschlossene Begriffsdefinition."
  - "SIA 232/1:2020 'Geneigte Dächer', Abschnitt 1 (Begriffe und geometrische Grundlagen) — Binder als vorausgesetzter Tragwerks-Begriff im Kontext geneigter Dächer; keine geschlossene Begriffsdefinition."
quellen_sekundär:
  - "Lignum (Hrsg.): Holzbautabellen HBT, Lignum, Zürich, aktuelle Auflage, Kap. 'Dachtragwerke' und 'Bindersysteme'."
  - "Lignum (Hrsg.): Lignatec 'Geneigte Dächer in Holzbauweise', Abschnitt zu Binder-Tragsystemen."
  - "Mönck, W.; Rug, W.: Holzbau – Bemessung und Konstruktion. 16. Aufl., Beuth, Berlin 2015, Kap. 11 'Dachtragwerke', §§ Binderdach, Nagelplattenbinder, BSH-Binder."
  - "Blass, H. J.; Sandhaas, C.: Ingenieurholzbau – Grundlagen der Bemessung. KIT Scientific Publishing, Karlsruhe 2016, Kap. 12 (Fachwerkträger und BSH-Träger)."
  - "Natterer, J.; Herzog, T.; Volz, M.: Holzbau-Atlas. 4. Aufl., Birkhäuser, Basel 2003, Kap. 'Dachtragwerke / Bindersysteme'."
  - "Gerner, M.: Fachwerk – Instandsetzung, Sanierung, Neubau. DVA, 7. Aufl. 2007, Glossar (Sparrenbinder, Kehlbalkenbinder, Hängewerk, Sprengwerk)."
  - "de.wikipedia.org/wiki/Dachbinder_(Holzbau) — Typologie und Synonyme."
  - "de.wikipedia.org/wiki/Binder_(Tragwerk) — werkstoffübergreifende Verallgemeinerung."
quellenkonflikt: |
  Keine der konsultierten Normen (SIA 265:2021, SIA 232/1:2020,
  DIN EN 1995-1-1:2010, DIN 1052:2008, DIN EN 14250:2010, DIN EN
  14080:2013) führt eine geschlossene Begriffsdefinition für
  „Binder". Der Begriff wird in allen Normen vorausgesetzt und nur
  über seine konstruktive Rolle und seine Sub-Typen charakterisiert.
  Die einzige normfeste Sub-Verankerung ist DIN EN 14250, die den
  **Nagelplattenbinder** als Produktklasse („vorgefertigte tragende
  Bauteile mit Nagelplattenverbindungen") regelt, nicht den
  Oberbegriff Binder selbst. Detail-Befund siehe
  `docs/recherche/2026-05-14_hg_binder.md`.

  Die Schweizer und die deutsche Korpussprache unterscheiden sich:

  - In der Schweiz dominiert im Wohnbau das **Pfettendach** ohne
    Binder; **BSH-Binder** sind im Hallen-, Industrie- und
    Gewerbebau verbreitet, **Nagelplattenbinder** sind im Wohnbau
    eher selten (Lignum HBT, implizite Praxis-Verankerung).
  - In Deutschland ist der **Nagelplattenbinder** auch im
    Wohnungs- und Reihenhausbau verbreitet, und „Binderdach"
    wird häufig als eigene Tragwerks-Familie neben Sparren- und
    Pfettendach geführt (Mönck/Rug 2015 Kap. 11).

  Eigene Festlegung in diesem Glossar (konsistent mit allen
  konsultierten Quellen):

  - **Binder** ist eine **Bauteilgruppe** im Sinne von
    `hg_bauteilgruppe.md`: ein vorgefertigtes oder im Werk
    fertig gefügtes, partitives Aggregat aus mehreren
    stab- oder lamellenförmigen Holzbauteilen sowie deren
    Verbindungen und Verbindungsmitteln, das als geometrische
    und konstruktive Einheit eine Spannweite überspannt und in
    regelmäßigen Achsabständen als Primärtragglied eines
    Dachtragwerks (oder im Hallenbau eines Deckentragwerks)
    eingesetzt wird.
  - **Strukturtyp `aggregat`**: der Binder hat eigene Identität
    (UUID), eine eigene Tragebene als Hüllgeometrie, eine
    eigene Spannweite, eigene Auflager-Achspunkte und eigene
    Konsistenzbedingungen über der Komposition (Knoten-Inzidenz,
    statisches Dreieck oder parallelgurtiges Fachwerk). Damit ist
    der Binder gerade **nicht** ein einzelnes `bauteil`; die
    Bestandteile (Sparren, Bundbalken, Streben, Pfosten, Pfetten,
    Lamellen, Nagelplatten) bleiben eigenständige Element-
    Instanzen mit eigener UUID.
  - **Oberbegriff `bauteilgruppe`**: der Binder erfüllt die zwei
    Kern-Merkmale der Bauteilgruppe — **exklusive Mitgliedschaft**
    der Bestandteile (ein Sparren eines Sparrenbinders ist nicht
    zugleich Bestandteil eines anderen Binders) und **kaskadische
    Lebenszyklus-Bindung** (das Entfernen des Binders entfernt
    seine Bestandteile als Modell-Einheit oder gibt sie
    ausdrücklich an ein Eltern-Aggregat zurück). Damit ist
    `bauteilgruppe` der korrekte Oberbegriff; `bausystem`
    (nicht-exklusive Mitgliedschaft) und `tragwerk` (Aggregat
    mit zusätzlichen Mengen Auflager und Lastfälle) sind als
    Oberbegriffe ausdrücklich abgelehnt.
  - **Englischer falscher Freund**: das englische Wort „binder"
    bezeichnet in der historischen Timber-Framing-Terminologie
    ein horizontales Quer-Bauteil zur Versteifung der Joists und
    ist **nicht** das deutsche „Binder". Das deutsche „Binder"
    heißt im Englischen je nach Kontext „truss", „girder", „roof
    girder", „trussed rafter" oder „glulam beam"; alle diese
    Anglizismen sind hier als abgelehnte Benennungen geführt,
    weil keiner von ihnen den deutschen Oberbegriff trifft („truss"
    und „trussed rafter" deckt Vollwandbinder nicht ab, „girder"
    und „glulam beam" decken Fachwerk- und Nagelplattenbinder
    nicht ab, „binder" trifft den deutschen Begriff überhaupt
    nicht).
  - **„Träger" ist nicht Synonym, sondern Oberbegriff im weiteren
    Sinn**: jeder Binder ist ein Träger, nicht jeder Träger ist
    ein Binder. „Binder" ist in der DACH-Zimmerei tragwerks- und
    dachspezifisch sowie mehrteilig zusammengesetzt, „Träger" ist
    der allgemeinere statische Begriff für linear-spannende
    Bauteile. Die Aufnahme von „Dachträger" und „Dachstuhlbinder"
    in `abgelehnte_benennungen` schließt die unscharfen Korpus-
    Varianten aus.
  - **„Bindebalken"** ist ein historisches Synonym für
    Bundbalken — also einen **Bestandteil** des Sparrenbinders,
    nicht den Binder selbst; als Benennung für den Binder ist es
    daher abgelehnt.

  Konkrete Sub-Spezialisierungen (Nagelplattenbinder, Sparrenbinder,
  Pfettenbinder, BSH-Binder, Fachwerkbinder, Vollwandbinder,
  Hauptbinder) sind ausdrücklich **nicht** Gegenstand dieses
  Eintrags und werden in eigenen Folgeeinträgen definiert, sobald
  ein Tool sie geometrisch oder bemessungstechnisch braucht. Die
  drei orthogonalen Klassifikations-Achsen (statisches System,
  Bauart/Werkstoff, Tragwerks-Hierarchie) sind im
  Erläuterungsblock dokumentiert.
---

## Prosa-Definition

Ein **Binder** ist eine Bauteilgruppe aus mindestens zwei stab- oder
lamellenförmigen Holzbauteilen und deren Verbindungen, deren
Bestandteile zusammen ein statisches Dreieck oder ein parallelgurtiges
Trag-Aggregat in einer im Tragwerk vorgesehenen Tragebene bilden, das
zwischen zwei oder mehr Auflagern eine Spannweite überspannt und in
regelmässigen Achsabständen als Primärtragglied eines Dachtragwerks
oder eines weitspannenden Deckentragwerks eingesetzt wird.

## Mathematische Definition

Sei

- W das Weltkoordinatensystem (siehe `weltkoordinatensystem`),
- 𝓑 die Menge aller Bauteile im Sinne von `bauteil`,
- 𝓥 die Menge aller Verbindungen im Sinne von `verbindung`,
- 𝒰 der UUID-Raum nach `uuid`,
- 𝓟 die Menge der Ebenen im Sinne von `ebene`,
- 𝒢_huelle die Menge der zulässigen Hüllgeometrie-Repräsentationen
  einer Bauteilgruppe (siehe `bauteilgruppe`).

Dann ist ein **Binder** ein Tupel

```
Bᵢ := (uuid, bestandteile, verbindungen, tragebene, auflagerpunkte,
       lage, huelle, bezeichnung?)
```

mit

- **uuid** ∈ 𝒰: technischer Surrogatschlüssel des Binders (Pflicht,
  persistent, RFC 9562 v7); externe Referenzen auf den Binder gehen
  ausschliesslich auf diese UUID (Aggregat-Wurzel im Sinne von
  `bauteilgruppe`).
- **bestandteile** ⊂ 𝓑, |bestandteile| ≥ 2: die endliche Menge der
  Holzbauteile, die den Binder konstituieren (z. B. zwei Sparren und
  ein Bundbalken eines Sparrenbinders; Ober-/Untergurt, Streben und
  Pfosten eines Fachwerkbinders; ein Brettschichtholz-Stab eines
  BSH-Binders mit |bestandteile| = 1 ist **nicht** zulässig — ein
  einzelner BSH-Träger ist Träger, nicht Binder, siehe
  Erläuterung 4.2 und §6.3 der zugehörigen Recherche).
- **verbindungen** ⊂ 𝓥, |verbindungen| ≥ 1: die Menge der Verbindungen
  zwischen Elementen von bestandteile (mindestens ein Knoten, an dem
  zwei Bauteile gefügt sind).
- **tragebene** ∈ 𝓟: die Ebene in W, in der die Bauteilachsen der
  Bestandteile näherungsweise liegen (die ausgezeichnete Trag-Ebene
  des Binders); per Konvention die Ebene, deren Lot-Stellung das
  Aggregat als „flächiges Trag-Element" auszeichnet.
- **auflagerpunkte** ⊂ ℝ³, |auflagerpunkte| ≥ 2: die endliche Menge
  der Punkte in W, an denen der Binder im umgebenden Tragwerk
  aufgelagert wird; diese Punkte sind Achspunkte, nicht die
  geometrischen Auflager des umgebenden Tragwerks selbst (eigener
  Eintrag `auflager` folgt; im Glossar wird hier nur die punkthafte
  Anbindungs-Position notiert).
- **lage** ∈ SE(3): die Starrkörpertransformation, die das lokale
  Binder-Koordinatensystem nach W überführt (siehe
  `lokales_koordinatensystem`).
- **huelle** ∈ 𝒢_huelle: die geometrische Hülle des Binders im lokalen
  Koordinatensystem (Polyeder oder Bounding-Volume).
- **bezeichnung?**: optionaler humanlesbarer Name (z. B. „Binder B-04
  Halle West").

und den Konsistenzbedingungen

1. **Bauteilgruppen-Konformität**: das Tupel
   (uuid, bestandteile, lage, huelle, bezeichnung?) erfüllt alle
   Konsistenzbedingungen 1–4 von `bauteilgruppe` (exklusive
   Mitgliedschaft, kaskadische Lebenszyklus-Bindung,
   Hüllen-Inklusion, azyklische Verschachtelung).
2. **Verbindungs-Inzidenz**: jede Verbindung v ∈ verbindungen
   referenziert ausschliesslich Bauteile aus bestandteile,
   ```
   ∀ v ∈ verbindungen : bauteile(v) ⊆ bestandteile
   ```
   wobei bauteile(v) die Bauteilmenge der Verbindung v gemäss
   `verbindung` bezeichnet.
3. **Zusammenhang**: der ungerichtete Inzidenzgraph
   G(Bᵢ) := (bestandteile, E) mit
   E := { {b₁, b₂} | ∃ v ∈ verbindungen : {b₁, b₂} ⊆ bauteile(v) }
   ist zusammenhängend; getrennte Binder werden als getrennte
   Instanzen modelliert.
4. **Tragebenen-Lage**: für jedes b ∈ bestandteile liegt die
   Bauteilachse a(b) (siehe `bauteilachse`, soweit für b definiert)
   näherungsweise in tragebene, d. h. der Abstand jedes
   Bauteilachspunktes zu tragebene ist ≤ Toleranzen.LAENGE_EPS.
   Bauteile, die in der App keine eindimensionale Bauteilachse
   tragen (z. B. flächige Beplankungen am Vollwandbinder), sind
   von dieser Bedingung ausgenommen und nur über die
   Hüllen-Inklusion (Bedingung 1) gebunden.
5. **Auflagerpunkte in der Tragebene**: für jedes
   p ∈ auflagerpunkte ist der Abstand von p zu tragebene
   ≤ Toleranzen.LAENGE_EPS, und es existiert ein b ∈ bestandteile
   mit p ∈ G_W(b) (das Auflagerpunkt-Bauteil), wobei G_W(b) die
   Bauteil-Punktmenge in W nach `bauteil` ist.
6. **Mindest-Spannweite zwischen den Auflagerpunkten**: für
   mindestens ein Paar (p₁, p₂) ∈ auflagerpunkte² gilt
   ‖p₁ − p₂‖ > Toleranzen.LAENGE_EPS; entartete Konfigurationen mit
   zusammenfallenden Auflagerpunkten sind unzulässig.

Die **geometrische Punktmenge** des Binders in W ist

```
G_W(Bᵢ) := lage(G_lokal(huelle)) ⊂ ℝ³
```

(transformierte Hülle); die alternative Repräsentation als Vereinigung
der Bestandteils-Punktmengen ⋃_{b ∈ bestandteile} G_W(b) ist eine
abgeleitete Grösse und im Allgemeinen eine echte Teilmenge von
G_W(Bᵢ) (siehe `bauteilgruppe` Bedingung 3).

## Wohldefiniertheit

- **Existenz**: Für jede konstruktive Einheit aus mindestens zwei
  Holzbauteilen und einer Verbindung, die zwischen zwei
  Auflagerpunkten in einer ausgezeichneten Tragebene aufgelagert
  ist und eine Spannweite überspannt, lässt sich ein Binder als
  Tupel der angegebenen Form erfassen. Mindestkonfiguration:
  |bestandteile| = 2, |verbindungen| = 1, |auflagerpunkte| = 2,
  lage = id_SE(3), huelle = achsenparalleler Hüllquader der beiden
  Bauteil-Bounding-Boxen, bezeichnung = ⊥.
- **Eindeutigkeit der Identität**: Bedingung 1 (Bauteilgruppen-
  Konformität) erbt die Aggregat-Wurzel-Auflösung von
  `bauteilgruppe`; die Binder-UUID ist konstruktionsseitig zu
  vergeben und persistent.
- **Eindeutigkeit der Tragebene**: tragebene ist als Teil des Tupels
  explizit gewählt. Aus den Bauteilachsen der Bestandteile lässt
  sich tragebene über Hauptkomponenten-Analyse rekonstruieren,
  sofern mindestens drei nicht-kollineare Bauteilachspunkte
  existieren; bei genau zwei kollinearen Bauteilachsen ist die
  Tragebene nicht eindeutig bestimmt und muss durch die explizite
  Wahl in tragebene festgelegt werden. Diese Konstruktive
  Wahl-Notwendigkeit ist im Datenmodell als Pflichtfeld abgebildet.
- **Unabhängigkeit von der Wahl des lokalen Koordinatensystems**:
  Für jede zulässige Wahl des lokalen Binder-Koordinatensystems
  liefert die zugehörige Lage-Transformation dieselbe Punktmenge
  G_W(Bᵢ); semantisch invariant.
- **Konsistenz mit `bauteilgruppe`**: Jede Konsistenzbedingung von
  `bauteilgruppe` (exklusive Mitgliedschaft, kaskadische Löschung,
  Hüllen-Inklusion, Azyklizität) gilt für den Binder, weil er Subtyp
  von `bauteilgruppe` ist. Die Binder-spezifischen Bedingungen 2–6
  treten **additiv** hinzu und schwächen keine
  Bauteilgruppen-Bedingung ab.
- **Konsistenz mit `verbindung`**: Jede Verbindung v ∈ verbindungen
  ist eine Verbindung im Sinne von `verbindung`; ihre eigenen
  Konsistenzbedingungen (insbesondere das Mischungsverbot
  verschiedener Wirkungsmechanismen pro Verbindung gemäss SIA 265
  Anhang A) gelten unverändert.
- **Konsistenz mit `bauteil`**: Jedes b ∈ bestandteile ist ein
  Bauteil im Sinne von `bauteil` mit eigener Identität, Lage,
  Geometrie und Werkstoff. Die Bestandteile bleiben eigenständige
  Element-Instanzen; die Binder-Mitgliedschaft ist eine zusätzliche
  Beziehung, keine Überschreibung der Bauteil-Eigenschaften.
- **Nicht-Zirkularität**: Die Definition verwendet
  `bauteilgruppe`, `bauteil`, `verbindung`, `uuid`,
  `lokales_koordinatensystem`, `weltkoordinatensystem`, `ebene`,
  `polyeder`, `toleranzen` — alle bereits definiert. Sie verweist
  nicht auf konkrete Sub-Typen (Sparrenbinder, Pfettenbinder,
  Nagelplattenbinder, BSH-Binder) und nicht auf `tragwerk` (der
  Binder ist Bestandteil eines Tragwerks, nicht definitorisch
  davon abhängig).
- **Trivial wohldefinierte Bestandteils-Menge**: bestandteile und
  verbindungen sind als Mengen unsortiert; alle Aussagen über den
  Binder sind invariant unter Permutation der Bestandteile.

## Erläuterung (nicht normativ)

Der Binder ist das paradigmatische **werks-vorgefertigte
Trag-Aggregat** im Holzbau. Sein Wesen liegt in drei Merkmalen, die
ihn von einem einzelnen `bauteil` (z. B. Sparren, Pfette, BSH-Träger)
und von einem nicht-exklusiv klassifizierten `bausystem` (z. B.
Tragwerk, Aussteifungssystem) gleichermassen unterscheiden:

1. **Mehrteiligkeit mit eigener Identität**: ein Binder besteht aus
   mehreren Holzbauteilen, die zusammen ein Aggregat mit eigener
   UUID, eigener Tragebene und eigener Spannweite bilden. Ein
   einzelner BSH-Träger ist trotz Brettschichtholz-Bauart **kein**
   Binder im Sinne dieses Eintrags, weil ihm die Mehrteiligkeit
   fehlt; er ist ein Bauteil und gegebenenfalls ein Träger im
   weiteren Sinn.
2. **Exklusive Mitgliedschaft seiner Bestandteile**: die Sparren,
   Streben, Pfosten und Lamellen eines Binders sind diesem Binder
   exklusiv zugeordnet. Sie können nicht zugleich Bestandteil eines
   zweiten Binders sein. Das unterscheidet den Binder strukturell
   vom Tragwerk, in dem ein Bauteil parallel mehreren funktionalen
   Sichten angehören kann.
3. **Werksvorfertigung als Aggregat**: der Binder wird typischerweise
   im Werk fertig gefügt (Nagelplattenbinder mit hydraulischer
   Presse, BSH-Binder durch Lamellenverleimung, zimmermannsmäßiger
   Sparrenbinder durch Abbund) und als Liefereinheit zur Baustelle
   gebracht. Die Werksvorfertigung ist konzeptuell prägend; das
   Aggregat wird als Ganzes gerechnet, geliefert und montiert.

### Drei orthogonale Klassifikations-Achsen

Im DACH-Korpus werden Binder nach drei strukturell unterschiedlichen
und voneinander unabhängigen Achsen klassifiziert. Eine konkrete
Binder-Instanz trägt typischerweise eine Klassifikation pro Achse;
die Achsen sind orthogonal und sollen im App-Modell auch so geführt
werden.

**Achse 1 — Statisches System.** Beschreibt, welche Last das Aggregat
in welcher Anordnung abträgt:

- **Sparrenbinder** / **Satteldachbinder**: statisches Dreieck aus
  zwei Sparren und einem Bundbalken.
- **Kehlbalkenbinder**: Sparrenbinder mit zusätzlichem Kehlbalken.
- **Pfettenbinder**: Hauptträger eines Hauptträger-Nebenträger-
  Systems; trägt Pfetten, die wiederum Sparren tragen.
- **Sparrenpfetten-Binder**, **Polygonalbinder**, **Trapez-**,
  **Mansard-**, **Bogen-**, **Pultdach-**, **Walmdach-**,
  **Schifterbinder**: Geometrie-Spezialisierungen nach Dachform.

**Achse 2 — Bauart und Werkstoff.** Beschreibt, wie das Aggregat
gefügt ist und woraus:

- **Vollwandbinder**: flächige Tragebene; höherer Holzverbrauch.
- **Fachwerkbinder**: Stab-Fachwerk; materialsparend.
- **Nagelplattenbinder (NPB)**: Stab-Fachwerk mit Stahl-
  Nagelplatten an den Knoten; einzige normfest verankerte
  Bauart (DIN EN 14250).
- **Brettschichtholz-Binder** (BSH-Binder, Leimbinder):
  verleimte Lamellen.
- **Bohlenbinder**, **Nagelbinder**, **Hetzer-Binder**: historische
  Bauarten.

**Achse 3 — Tragwerks-Hierarchie.** Beschreibt die Rolle im
umgebenden Tragwerk:

- **Hauptbinder** / **Vollbinder**: primäres Lastabtragungs-Niveau.
- **Nebenbinder** / **Leerbinder**: sekundär, zwischen Hauptbindern.
- **Endbinder** / **Giebelbinder**: randständig am Giebel.

Ein konkreter Binder lässt sich an allen drei Achsen klassifizieren:
ein „Hauptbinder als Pfettenbinder in NPB-Bauart" ist eine
zulässige, im Korpus geläufige Kombination. Im App-Modell sollten
die drei Achsen als separate Annotationen (oder Sub-Typen) geführt
werden, nicht in eine einzige Liste gemischt.

### Abgrenzung zu Tragwerk in einem Satz

Ein **Tragwerk** ist ein Aggregat mit zusätzlichen Mengen (Auflager,
Lastfälle) und einer **nicht-exklusiven** Bauteil-Mitgliedschaft; ein
**Binder** ist eine Bauteilgruppe mit **exklusiver** Bestandteils-
Mitgliedschaft, die als werks-vorgefertigtes Element typischerweise
ein **Bestandteil** des Tragwerks ist (so wie ein Sparren ein Bauteil
des Tragwerks ist). Ein Binderdach ist ein Tragwerk, dessen
Primärtragglieder Binder sind.

### Abgrenzung zu Sparren / Pfette in einem Satz

Ein **Sparrenbinder** enthält zwei Sparren als Bestandteile, ist aber
selbst kein Sparren; ein **Pfettenbinder** trägt Pfetten, ist aber
selbst keine Pfette. Sparren und Pfette tragen den `begriffstyp:
bauteilrolle` (sealed-Subtyp unter `bauteil`); Binder trägt den
`begriffstyp: aggregat` (Komposition mehrerer Bauteile).

### Englischer falscher Freund

Das englische Wort **„binder"** bezeichnet in der historischen
Timber-Framing-Terminologie ein **horizontales Quer-Bauteil zur
Versteifung der Joists** („a timber joist at the bases of the beams
to strengthen them") und ist somit ein einzelnes Bauteil — also nicht
das mehrteilige deutsche „Binder"-Aggregat. Das deutsche „Binder"
heisst im Englischen je nach Kontext „truss" (statisches Dreieck,
NPB), „girder" oder „roof girder" (Hauptträger im Hauptträger-
Nebenträger-System) oder „glulam beam" (für den BSH-Binder, sofern
nicht fachwerkartig). Im Glossar werden alle vier Anglizismen als
abgelehnte Benennungen geführt, weil keiner von ihnen den deutschen
Oberbegriff trifft.

## Beziehungen

- **Oberbegriff**: `bauteilgruppe`. Der Binder erfüllt alle Bauteil-
  gruppen-Merkmale (exklusive Mitgliedschaft, kaskadische
  Lebenszyklus-Bindung, eigene Hülle, eigene Identität,
  konstruktive Funktionseinheit) und fügt drei eigene Merkmale
  hinzu: explizite Tragebene, mindestens zwei Auflagerpunkte und
  mindestens eine Verbindung zwischen den Bestandteilen.
- **Bestandteile (partitiv)**:
  - **Bauteile** (`bauteil`): Sparren, Bundbalken, Streben, Pfosten,
    Lamellen, Pfetten — die exklusiven Holzbauteile des Binders.
  - **Verbindungen** (`verbindung`): die Knotenaggregate zwischen
    den Bestandteilen (Nagelplatten-Knoten, Versatz, Zapfen,
    Stabdübel-Verbindung, Verleimung).
  - **Tragebene** (`ebene`): die ausgezeichnete Trag-Ebene des
    Aggregats.
  - **Lokales Koordinatensystem** (`lokales_koordinatensystem`).
  - **Hülle** (`polyeder` oder Bounding-Volume).
- **Spezialisierungen** (eigene Einträge folgen, trigger-basiert
  gemäss Folgearbeit-Block):
  - `nagelplattenbinder` — Bauart-Achse, DIN-EN-14250-Anker.
  - `sparrenbinder` — statisches System.
  - `pfettenbinder` — statisches System.
  - `bsh_binder` (Brettschichtholz-Binder, Leimbinder) — Bauart.
  - `fachwerkbinder` / `vollwandbinder` — Bauart-Achse.
  - `hauptbinder` — Tragwerks-Hierarchie (offene Designfrage, ob
    eigener Eintrag).
- **Verwendung**:
  - Bestandteil eines **Tragwerks** (`tragwerk`): ein Binder ist
    typischerweise ein Primärtragglied eines Dachtragwerks. Die
    Tragwerks-Bauteilmenge B enthält die einzelnen Holzbauteile,
    der Binder fasst eine Teilmenge davon zur Bauteilgruppe
    zusammen.
  - Bestandteil eines **Daches** (`dach`) — als Teil des
    Dachtragwerks.
- **Abgrenzung**:
  - **Bauteilgruppe** (`bauteilgruppe`): Oberbegriff — siehe oben.
  - **Tragwerk** (`tragwerk`): das umgebende Aggregat aus
    lastabtragenden Bauteilen mit Auflagern und Lastfällen; ein
    Binder ist Bestandteil eines Tragwerks, nicht selbst eines.
    Tragwerk hat zudem nicht-exklusive Bauteil-Mitgliedschaft,
    der Binder exklusive Bestandteils-Mitgliedschaft.
  - **Bauteil** (`bauteil`): einzelner Bestandteil; ein Binder ist
    eine Komposition mehrerer Bauteile, kein einzelnes Bauteil.
    Insbesondere ist ein einzelner BSH-Träger ohne weitere Stäbe
    **kein** Binder.
  - **Sparren** (`sparren`): ein einzelnes geneigtes Stab-Bauteil
    entlang der Falllinie einer Dachfläche. Ein Sparrenbinder
    enthält zwei Sparren als Bestandteile, ist aber kein Sparren.
  - **Pfette** (`pfette`): ein einzelnes horizontales Längs-Stab-
    Bauteil parallel zur Dachkante. Ein Pfettenbinder trägt
    Pfetten, ist aber keine Pfette. „Pfettenbinder" und
    „Sparrenbinder" benennen Binder-Sub-Typen über das **getragene**
    bzw. **enthaltene** Bauteil, nicht über die Identität des
    Binders mit jenem Bauteil.
  - **Verbindung** (`verbindung`): lokales Knoten-Aggregat aus
    Bauteilen, Verbindungsmitteln, Verbindern und Verstärkungen an
    einem Punkt. Ein Binder enthält **mehrere** Verbindungen
    zwischen seinen Bestandteilen und ist selbst keine Verbindung.
  - **Dach** (`dach`), **Dachfläche** (`dachflaeche`): ein Binder
    ist Bestandteil des Dachtragwerks, das wiederum Bestandteil
    eines Daches ist; er ist selbst kein Dach und keine Dachfläche.
  - **Bauteilachse** (`bauteilachse`): ein Bestandteil eines
    Binders trägt eine Bauteilachse; der Binder selbst trägt keine
    Bauteilachse, sondern eine Tragebene.
  - **Binderdach** (`binderdach`, eigener Eintrag folgt): das
    Dachtragwerks-System, in dem Binder die Primärtragglieder
    sind. Binder ist das einzelne Aggregat, Binderdach das
    Tragwerks-System.
  - **Nagelplattenbinder**, **Sparrenbinder**, **Pfettenbinder**,
    **BSH-Binder**, **Fachwerkbinder**, **Vollwandbinder**,
    **Hauptbinder**, **Kehlbalkenbinder**, **Polygonalbinder**,
    **Hetzer-Binder**: alles Sub-Typen entlang der drei oben
    genannten Klassifikations-Achsen; eigene Einträge folgen
    trigger-basiert.

## Implementierungshinweis

**Im aktuellen Glossarstand wird keine eigene Code-Klasse `Binder`
angelegt.** Die ontologische Vorbereitung lebt zunächst nur im
Glossar; eine Code-Klasse entsteht zusammen mit dem ersten
konkreten Sub-Typ (typischerweise `Sparrenbinder` oder
`Nagelplattenbinder`), der in einem Tool tatsächlich benötigt wird.
Der folgende Skizzen-Code ist ausschliesslich orientierender
Implementierungs-Hinweis für den Zeitpunkt, an dem dieser Sub-Typ
implementiert wird, und folgt der Sealed-Hierarchie unter
`Bauteilgruppe` aus `hg_bauteilgruppe.md`.

```kotlin
// SKIZZE — nicht jetzt anlegen.
// Glossar: hg_binder.md

package domain.bauteil

import domain.bauteil.Bauteilgruppe
import domain.bauteil.Bauteil
import domain.geometrie.Ebene
import domain.geometrie.Punkt
import domain.verbindung.Verbindung
import java.util.UUID

/**
 * Binder: Bauteilgruppe, deren Bestandteile zusammen ein
 * statisches Dreieck oder ein parallelgurtiges Trag-Aggregat in
 * einer expliziten Tragebene bilden und zwischen mindestens zwei
 * Auflagerpunkten eine Spannweite überspannen.
 *
 * Sealed unter Bauteilgruppe; konkrete Sub-Typen entlang der drei
 * Klassifikations-Achsen (statisches System, Bauart/Werkstoff,
 * Tragwerks-Hierarchie) entstehen trigger-basiert.
 */
sealed class Binder : Bauteilgruppe() {
    abstract val verbindungen: Set<Verbindung>
    abstract val tragebene: Ebene
    abstract val auflagerpunkte: Set<Punkt>

    init {
        // 1. bestandteile.size >= 2          → sonst Entartet.ZuKleinerBinder
        // 2. verbindungen.isNotEmpty()       → sonst Entartet.OhneVerbindung
        // 3. auflagerpunkte.size >= 2        → sonst Entartet.ZuWenigAuflagerpunkte
        // 4. Verbindungs-Inzidenz            → sonst Entartet.VerbindungOhneBestandteil
        // 5. Zusammenhang Inzidenzgraph      → sonst Entartet.NichtZusammenhaengenderBinder
        // 6. Bauteilachsen in Tragebene      → sonst Entartet.AchseAusserhalbTragebene
        // 7. Auflagerpunkte in Tragebene     → sonst Entartet.AuflagerpunktAusserhalbTragebene
        // 8. Mindest-Spannweite              → sonst Entartet.ZusammenfallendeAuflagerpunkte
    }
}
```

- **Einheit**: Längen in mm (Double); Winkel intern in Radiant; Lage
  als SE(3)-Element.
- **Identität**: `uuid` ist Pflicht und persistent (RFC 9562 v7);
  externe Referenzen auf einen Binder gehen ausschliesslich auf diese
  UUID. Bestandteile und Verbindungen werden über ihre jeweiligen
  UUIDs referenziert (Foreign-Key-Regel).
- **Invarianten** (in `init` bzw. Fabrikfunktionen prüfen, bei
  Verletzung `Resultat.Fehler` bzw. `Entartet`-Variante; niemals
  Exception werfen):
  1. `bestandteile.size >= 2` ⇒ sonst `Entartet.ZuKleinerBinder`.
  2. `verbindungen.isNotEmpty()` ⇒ sonst `Entartet.OhneVerbindung`.
  3. `auflagerpunkte.size >= 2` ⇒ sonst
     `Entartet.ZuWenigAuflagerpunkte`.
  4. Jede Verbindung referenziert ausschliesslich Bauteile aus
     `bestandteile` ⇒ sonst `Entartet.VerbindungOhneBestandteil`.
     Toleranz nicht erforderlich (Mengenzugehörigkeit).
  5. Der Bestandteils-Inzidenzgraph ist zusammenhängend ⇒ sonst
     `Entartet.NichtZusammenhaengenderBinder`.
  6. Für jede Bauteilachse a(b), b ∈ bestandteile, ist der
     Maximalabstand der Achspunkte zu `tragebene`
     ≤ `Toleranzen.LAENGE_EPS` ⇒ sonst
     `Entartet.AchseAusserhalbTragebene`. Bauteile ohne
     eindimensionale Bauteilachse sind ausgenommen.
  7. Für jeden Auflagerpunkt p ist der Abstand zu `tragebene`
     ≤ `Toleranzen.LAENGE_EPS` ⇒ sonst
     `Entartet.AuflagerpunktAusserhalbTragebene`.
  8. Für mindestens ein Paar (p₁, p₂) gilt
     ‖p₁ − p₂‖ > `Toleranzen.LAENGE_EPS` ⇒ sonst
     `Entartet.ZusammenfallendeAuflagerpunkte`.
  9. **Exklusive Mitgliedschaft** (modellweite Cross-Aggregat-
     Invariante, geerbt von `Bauteilgruppe`): kein Bauteil
     b ∈ bestandteile ist zugleich Bestandteil eines anderen Binders
     oder einer anderen Bauteilgruppe in der Aggregations-Hierarchie.
     Prüfung im Modell-Container; bei Verletzung
     `Entartet.MehrfachMitgliedschaft`. Die Exklusivität gilt
     analog für die **`verbindungen`-Komponente**: jede Verbindung
     v ∈ verbindungen verbindet ausschliesslich Bauteile innerhalb
     dieses Binders und ist nicht zugleich Bestandteil einer anderen
     Bauteilgruppe. Der Lebenszyklus der Verbindungen ist
     kaskadisch an den Binder gekoppelt (Entfernen des Binders
     entfernt die Verbindungen, nicht die einzelnen Bauteile).
- **Edge Cases**:
  - **Sparrenbinder als Mindestkonfiguration** (zwei Sparren plus
    Bundbalken, |bestandteile| = 3, |verbindungen| = 3 oder kombiniert
    zu 1 First-Knoten plus 2 Fusspunkten): zulässig.
  - **Einzelner BSH-Träger**: **nicht** als Binder zulässig
    (|bestandteile| = 1 verletzt Bedingung 1); als `bauteil` mit
    Werkstoff Brettschichtholz zu führen.
  - **Verschachtelte Binder** (Hauptbinder enthält eine
    Sub-Aussteifung als Bauteilgruppe): nach `bauteilgruppe`
    Bedingung 4 zulässig, solange der Aggregations-Graph azyklisch
    bleibt.
  - **Bauteil-Wechsel der Binder-Zugehörigkeit**: erfordert eine
    koordinierte Modifikation der betroffenen Binder über den
    Modell-Container; nicht durch direkten Bauteil-Zugriff.
  - **Mehrteilige Auflagerung** (Binder auf Pfettenwand, Stütze
    und Auswechslung): zulässig, sofern alle drei Auflagerpunkte
    in `auflagerpunkte` geführt werden.
  - **Krumme oder polygonale Untergurte** (Bogenbinder, Hetzer-
    Binder): die Tragebene bleibt eine Ebene; die Bauteilachsen der
    krummen Bestandteile liegen näherungsweise (im
    Toleranzbereich) in dieser Ebene, der Toleranzhorizont kann
    pro Sub-Typ erweitert werden.
- **Abgeleitete Eigenschaften** (als Funktionen, keine Felder):
  - `geometrieInWelt(): GeometrieInW` = `lage(huelle)` als
    transformierte Hülle in W (geerbt von `Bauteilgruppe`).
  - `bestandteilsVereinigung(): GeometrieInW` =
    ⋃_{b ∈ bestandteile} G_W(b); im Allgemeinen echte Teilmenge
    der Hülle.
  - `spannweite(): Double` (mm) = maximaler Abstand zwischen Paaren
    aus `auflagerpunkte`; bei genau zwei Auflagerpunkten gleich
    ‖p₁ − p₂‖.
  - `inzidenzgraph(): Graph<Bauteil, Verbindung>` = der ungerichtete
    Graph mit Bestandteilen als Knoten und Verbindungen als Kanten.
  - `tragebenenNormale(): Vektor` = Normalenvektor der Tragebene
    in W.

## Quellen

**Primär (normativ):**

- DIN EN 14250:2010-05, „Holzbauwerke – Produktanforderungen an
  vorgefertigte tragende Bauteile mit Nagelplattenverbindungen",
  Deutsches Institut für Normung, Berlin.
- DIN EN 1995-1-1:2010-12, „Eurocode 5: Bemessung und Konstruktion
  von Holzbauten – Teil 1-1: Allgemeines", Abschnitte 9 und 10.
- DIN EN 14080:2013-09, „Holzbauwerke – Brettschichtholz und
  Balkenschichtholz – Anforderungen".
- DIN 1052:2008-12, „Entwurf, Berechnung und Bemessung von
  Holzbauwerken – Allgemeine Bemessungsregeln und
  Bemessungsregeln für den Hochbau", Abschnitte 8 und 12.
- SIA 265:2021, „Holzbau", Schweizerischer Ingenieur- und
  Architektenverein, Zürich, Abschnitt 5.
- SIA 232/1:2020, „Geneigte Dächer", Schweizerischer Ingenieur- und
  Architektenverein, Zürich, Abschnitt 1.

**Sekundär:**

- Lignum (Hrsg.): *Holzbautabellen HBT.* Lignum, Zürich, aktuelle
  Auflage.
- Lignum (Hrsg.): *Lignatec „Geneigte Dächer in Holzbauweise".*
- Mönck, W.; Rug, W.: *Holzbau – Bemessung und Konstruktion.*
  16. Auflage, Beuth, Berlin 2015, Kap. 11.
- Blass, H. J.; Sandhaas, C.: *Ingenieurholzbau – Grundlagen der
  Bemessung.* KIT Scientific Publishing, Karlsruhe 2016, Kap. 12.
- Natterer, J.; Herzog, T.; Volz, M.: *Holzbau-Atlas.* 4. Auflage,
  Birkhäuser, Basel 2003.
- Gerner, M.: *Fachwerk – Instandsetzung, Sanierung, Neubau.* DVA,
  7. Auflage 2007.

**Korpus (nicht autoritativ):**

- de.wikipedia.org, Lemma „Dachbinder (Holzbau)" (abgerufen
  2026-05-14).
- de.wikipedia.org, Lemma „Binder (Tragwerk)" (abgerufen
  2026-05-14).
- en.wikipedia.org, Lemma „Timber roof truss" (abgerufen
  2026-05-14, für englische Begriffs-Abgrenzung).
- Recherchebericht `docs/recherche/2026-05-14_hg_binder.md`.

## Folgearbeit (trigger-basiert)

Sub-Typen werden definiert, sobald das jeweilige Tool sie
geometrisch oder bemessungstechnisch braucht. Die folgenden sieben
Folgearbeit-Trigger sind absehbar:

1. **`nagelplattenbinder`** — Bauart-Spezialisierung mit
   Stahl-Nagelplatten an den Knoten; normativer Anker in
   DIN EN 14250:2010 (Produktanforderungen, CE-Kennzeichnung).
   Trigger: erstes Tool, das einen Nagelplattenbinder geometrisch
   oder bemessungstechnisch modelliert.
2. **`sparrenbinder`** — statisches Dreieck aus zwei Sparren und
   einem Bundbalken; klassische zimmermannsmäßige Bauart.
   Trigger: erstes Tool, das einen Sparrenbinder als
   Aggregat aus benannten Bauteilrollen modelliert.
3. **`pfettenbinder`** — Hauptträger eines Hauptträger-
   Nebenträger-Systems; trägt Pfetten, die wiederum Sparren tragen.
   Trigger: erstes Tool, das ein Pfettenbinder-System (z. B.
   Hallendach mit Pfettenwand-Auflagerung) modelliert.
4. **`bsh_binder`** (Brettschichtholz-Binder, Leimbinder) —
   Werkstoff-/Verbindungs-Spezialisierung mit verleimten Lamellen
   nach DIN EN 14080. Trigger: erstes Tool, das einen BSH-Binder
   (Hallenbau, weitspannender Geschossbau) geometrisch modelliert.
5. **`fachwerkbinder`** — Bauart-Achse: Stab-Fachwerk mit Stäben
   und Knoten in der Tragebene. Trigger: erstes Tool, das die
   Fachwerk-Topologie (Knoten-Stab-Inzidenzen) explizit darstellt.
6. **`vollwandbinder`** — Bauart-Achse, Gegenpol zum Fachwerkbinder:
   flächige Tragebene. Trigger: erstes Tool, das vollwandige
   Binder mit flächigen Bestandteilen darstellt.
7. **`hauptbinder`** — Tragwerks-Hierarchie-Rolle (Primär-
   Lastabtragungs-Niveau in einem Hauptträger-Nebenträger-System).
   Trigger: erstes Tool, das die Hierarchie-Rolle Primär-/Sekundär-
   Binder in einem Tragwerk auflöst (etwa für die
   Werkstattzeichnung mit Achs-Numerierung). Offene Designfrage,
   ob „Hauptbinder" als eigener Eintrag oder als Annotation am
   Binder geführt wird; der Korpus-Sprachgebrauch ist
   uneinheitlich.

Ebenfalls als Folgearbeit auf Glossar-Ebene absehbar, aber nicht
in den sieben Trigger-Bindern enthalten:

- `binderdach` — das Tragwerks-System, in dem Binder die
  Primärtragglieder sind (parallel zu `sparrendach`,
  `pfettendach`, `kehlbalkendach` aus dem `tragwerk`-Eintrag).
- `bundbalken` — horizontales Zugglied im Sparrenbinder (verbindet
  die Sparrenfüße); aktuell als impliziter Bestandteil im
  Sparrenbinder-Block geführt. Trigger: erster Sparrenbinder-
  Eintrag (`sparrenbinder.md`), der die Mindestkonfiguration
  „zwei Sparren + Bundbalken" formal definiert.
- Eintragung des englischen Fachglossar-Mapping (`truss`,
  `girder`, `nail-plate truss`, `glulam beam`) als
  Korpus-Begriffe in einer späteren Übersetzungs-Schicht.
