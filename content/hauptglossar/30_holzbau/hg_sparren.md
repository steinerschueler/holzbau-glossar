---
id: sparren
benennung: Sparren
synonyme: [Dachsparren]
abgelehnte_benennungen: [Dachbalken, "rafter", "common rafter", "Dachstange"]
oberbegriff: bauteil
begriffstyp: bauteilrolle
voraussetzungen: [bauteil, bauteilachse, strecke, einheitsvektor, ebene, dachflaeche, falllinie, dachneigung, weltkoordinatensystem, toleranzen]
abgrenzung_zu: [pfette, kehlbalken, gratsparren, kehlsparren, binder, latte, konterlatte, dachflaeche, sparrenueberstand, kerve, sparrenlaenge]
status: entwurf
theorie_pflichtig: required
quellen_primär:
  - "SIA 265:2021 'Holzbau', Schweizerischer Ingenieur- und Architektenverein, Abschnitt 4 (Bemessung) und Abschnitt 5 (Konstruktive Durchbildung), Sparren als geneigte stabförmige Tragglieder von Dachtragwerken."
  - "SIA 232/1:2020 'Geneigte Dächer', Abschnitt 1 (Begriffe und geometrische Grundlagen), Sparren als geneigtes Dach-Tragglied entlang der Falllinie."
  - "DIN EN 1995-1-1:2010-12 (Eurocode 5), Abschnitt 5 (Tragwerksberechnung) und Abschnitt 6 (Grenzzustände der Tragfähigkeit), Sparren (engl. rafter) als biegebeanspruchtes Stab-Bauteil."
  - "DIN 1052:2008-12, Abschnitt 8 und Abschnitt 12 (Konstruktive Anforderungen), Sparren als geneigtes Tragglied."
  - "DIN EN 14081-1:2019-10, 'Holzbauwerke – Nach Festigkeit sortiertes Bauholz mit rechteckigem Querschnitt – Teil 1: Allgemeine Anforderungen' (Querschnittsanforderungen für Sparren als Vollholz-Stabbauteil)."
quellen_sekundär:
  - "Lignum (Hrsg.): Holzbautabellen HBT, Lignum, Zürich, aktuelle Auflage, Kap. 'Dachtragwerke / Sparren'."
  - "Lignum (Hrsg.): Lignatec 'Geneigte Dächer in Holzbauweise', Abschnitt 'Sparren und Sparrenanschlüsse'."
  - "Mönck, W.; Rug, W.: Holzbau – Bemessung und Konstruktion. 16. Aufl., Beuth, Berlin 2015, Kap. 11 'Dachtragwerke', § Sparren."
  - "Blass, H. J.; Sandhaas, C.: Ingenieurholzbau – Grundlagen der Bemessung. KIT Scientific Publishing, Karlsruhe 2016, Kap. 5 und Kap. 7 (Stabbauteile, Knicken)."
  - "Natterer, J.; Herzog, T.; Volz, M.: Holzbau-Atlas. 4. Aufl., Birkhäuser, Basel 2003, Kap. 'Dachtragwerke'."
  - "Gerner, M.: Fachwerk – Instandsetzung, Sanierung, Neubau. DVA, 7. Aufl. 2007, Glossar 'Sparren'."
quellenkonflikt: |
  Weder SIA 265, SIA 232/1, EN 1995-1-1 noch DIN 1052 enthalten eine
  geschlossene Begriffsdefinition für „Sparren"; der Begriff wird in
  allen konsultierten Normen vorausgesetzt und über seine konstruktive
  Rolle (geneigtes, lastabtragendes Stab-Bauteil eines Dachtragwerks)
  charakterisiert. SIA 232/1 und Lignum-Lignatec verwenden ihn als
  Tragglied entlang der Falllinie der Dachfläche.

  In der Sekundärliteratur (Mönck/Rug, Blass/Sandhaas, Natterer/Herzog,
  Gerner) wird der Sparren durchgängig als „geneigtes, in regelmäßigen
  Abständen parallel verlegtes Stab-Bauteil zur Übertragung der
  Dachflächenlasten auf Pfetten oder ein Sparrenpaar-Gegenstück"
  beschrieben.

  Eigene Festlegung in diesem Glossar:

  - Ein Sparren ist ein **Bauteil mit Bauteilrolle „Sparren"**, dessen
    Bauteilachse näherungsweise in der Trägerebene einer zugeordneten
    Dachfläche und entlang ihrer Falllinie liegt.
  - Die Vorzeichenkonvention für die Bauteilachse ist normativ
    festgelegt: p_a am Sparrenfuß (Traufe), p_e am Sparrenfirstpunkt
    (First); damit zeigt der Richtungs-Einheitsvektor d̂ entlang
    der Falllinie der Dachfläche **nach oben**, also entgegen der
    Falllinie ê_fall (siehe `hg_falllinie.md`). Das ist konsistent mit
    der Empfehlung in `hg_bauteilachse.md`, Abschnitt
    Vorzeichenkonvention.
  - Die Sparrenneigung ist gleich der Dachneigung der zugeordneten
    Dachfläche; beide Begriffe sind über `hg_dachneigung.md` formal
    verknüpft.

  Sonderformen wie **Gratsparren** (entlang eines Grats) und
  **Kehlsparren** (entlang einer Kehle) sind eigene Folge-Begriffe;
  sie liegen nicht auf der Falllinie einer einzelnen Dachfläche,
  sondern auf der Schnittkante zweier Dachflächen. Sie werden in
  `abgrenzung_zu` aufgeführt und in der Erläuterung kurz
  charakterisiert.

  **Benennung des firstseitigen Endpunkts (Sparrenfirstpunkt
  statt Sparrenkopf):** Eine frühere Fassung dieses Eintrags
  bezeichnete den firstseitigen Bauteilachsen-Endpunkt p_e als
  „Sparrenkopf". Die DACH-Korpus-Recherche (Wikipedia, allgemeines
  Zimmerei-Schrifttum, Gerner) hat ergeben, dass „Sparrenkopf"
  dort durchgängig in der **traufseitigen Lesart** verwendet
  wird, nämlich als Bezeichnung für das **traufseitige, über die
  Fußpfette hinausragende untere Ende** des Sparrens — also für
  das, was im Glossareintrag `hg_sparrenueberstand.md` als Synonym
  zum Sparrenüberstand geführt wird. Die App-interne Verwendung
  von „Sparrenkopf" für den firstseitigen Endpunkt hat keine
  Stütze in den konsultierten Quellen und kollidiert mit der
  Korpus-Bedeutung. Zur Vermeidung einer doppelt belegten
  Benennung wird der firstseitige Endpunkt p_e in diesem Glossar
  durchgängig **Sparrenfirstpunkt** genannt; der Bezeichner
  „Sparrenkopf" bleibt damit für die traufseitige Lesart in
  `hg_sparrenueberstand.md` reserviert.

  Diese Festlegung ist konsistent mit allen konsultierten Quellen.
---

## Prosa-Definition

Ein **Sparren** ist ein Stab-Bauteil eines Dachtragwerks, dessen
Bauteilachse in der Trägerebene einer zugeordneten Dachfläche entlang
ihrer Falllinie verläuft, das die Lasten der Dachflächen-Konstruktion
(Eigengewicht der Dachhaut, Schnee, Wind sowie Eigengewicht der
Sparren-Lattung und gegebenenfalls Ausbau-Lasten) aufnimmt und
entlang seiner Längsachse über seine Auflager (Pfetten oder, im
Sparrendach, das Gegenstück-Sparrenpaar nebst Zugglied) abträgt.

## Mathematische Definition

Sei

- B ein Bauteil im Sinne von `bauteil` mit Stabgeometrie
  (`geometrie ∈ 𝒢_stab`),
- a(B) = Bauteilachse.Gerade(p_a, p_e) die Bauteilachse von B im
  geraden Fall (siehe `bauteilachse`), mit
  d̂ := (p_e − p_a) / ‖p_e − p_a‖ ∈ S² ⊂ ℝ³,
- D = (E, P, n_a) eine Dachfläche im Sinne von `dachflaeche` mit
  Trägerebene E, Polygon P und äußerer Normaler n_a,
- ê_fall(E) ∈ S² die Falllinie der Trägerebene E (siehe
  `falllinie`); d. h. ⟨ê_fall, e_z⟩ ≤ 0,
- ε_W := Toleranzen.WINKEL_EPS, ε_L := Toleranzen.LAENGE_EPS.

Dann heißt B ein **Sparren** der Dachfläche D genau dann, wenn die
folgenden Bedingungen erfüllt sind:

1. **Stabgeometrie**: B besitzt eine gerade Bauteilachse mit
   ‖p_e − p_a‖ > ε_L.

2. **Lage in der Trägerebene**: Beide Endpunkte der Bauteilachse
   liegen in E im Sinne von
   ```
   |⟨n_a, p_a − p₀⟩| ≤ ε_L  und  |⟨n_a, p_e − p₀⟩| ≤ ε_L,
   ```
   wobei p₀ ein beliebiger Stützpunkt von E ist (Lage-Bedingung
   geerbt von `dachflaeche.istInEbene`).

3. **Falllinien-Kollinearität**: Die Bauteilachsenrichtung ist
   kollinear zur Falllinie der Trägerebene,
   ```
   |⟨d̂, ê_fall(E)⟩| ≥ 1 − ε_W,
   ```
   d. h. der Winkel zwischen d̂ und ê_fall ist 0 oder π (modulo
   ε_W).

4. **Vorzeichenkonvention (Sparrenrichtung von Traufe zu First)**:
   Die Bauteilachse ist so gerichtet, dass d̂ **entgegen** ê_fall
   verläuft, also nach oben:
   ```
   ⟨d̂, ê_fall(E)⟩ ≤ −1 + ε_W,
   ```
   äquivalent ⟨d̂, e_z⟩ ≥ 0. p_a ist damit der Sparrenfuß
   (an oder nahe der Traufe), p_e der Sparrenfirstpunkt (an oder nahe
   am First bzw. der Pultkante).

Wesentliche abgeleitete Größen:

- **Sparrenlänge**: L_S := ‖p_e − p_a‖ (in mm), entlang der
  Bauteilachse zwischen Sparrenfuß und Sparrenfirstpunkt.
- **Sparrenneigung** (= Dachneigung der zugeordneten Dachfläche):
  ```
  α_S := arccos(⟨n_a, e_z⟩) = arccos(⟨d̂, ê_horiz⟩),
  ```
  wobei ê_horiz := −(ê_fall − ⟨ê_fall, e_z⟩ · e_z) /
  ‖ê_fall − ⟨ê_fall, e_z⟩ · e_z‖ die in die Horizontalebene
  projizierte und nach oben in die Sparrenrichtung umgekehrte
  Falllinie ist.
- **Sparrenfuß** und **Sparrenfirstpunkt** (als Punkte): F_fuß := p_a,
  F_first := p_e.
- **Sparrenabstand**: bei einer parallelen Sparrenschar
  S_1, …, S_k auf derselben Dachfläche der rechtwinklige Abstand
  benachbarter Bauteilachsen, gemessen in der Trägerebene
  orthogonal zu d̂; der Sparrenabstand ist Bemessungs-Eingangsgröße
  und nicht Bestandteil der Sparren-Definition.

## Wohldefiniertheit

- **Existenz**: Für jedes Stabbauteil mit positiver Achsenlänge,
  Endpunkten in der Trägerebene einer geneigten Dachfläche und
  Achsenrichtung kollinear zur Falllinie sind alle vier Bedingungen
  konstruktiv erfüllbar; ein typischer Sparren auf einer
  Satteldachhälfte ist das Standardbeispiel.
- **Eindeutigkeit der Vorzeichenkonvention**: Die Bedingung 4
  fixiert eine der beiden Achsenorientierungen (d̂ oder −d̂)
  eindeutig: für eine geneigte Dachfläche (Geneigtheits-
  Voraussetzung der Falllinie, α_S > 0) ist
  ⟨d̂, ê_fall⟩ ≠ 0, und genau einer der beiden Werte ±1 (modulo
  ε_W) liegt im Bereich „nach oben".
- **Konsistenz mit `hg_bauteilachse.md`**: Die in
  `hg_bauteilachse.md` empfohlene Vorzeichenkonvention für Sparren
  („p_a an der Traufe, p_e am First, d̂ in Falllinien-Richtung,
  von Traufe zu First") wird hier formal übernommen. Achtung:
  „in Falllinien-Richtung von Traufe zu First" ist gegen ê_fall
  gerichtet, da ê_fall per Definition (siehe `hg_falllinie.md`,
  Vorzeichenkonvention ⟨ê_fall, e_z⟩ ≤ 0) **nach unten** zeigt.
  Bedingung 4 löst diese Vorzeichen-Subtilität explizit auf.
- **Sparrenneigung = Dachneigung**: Aus der Falllinien-
  Kollinearität (Bed. 3) folgt, dass d̂ in der von e_z und n_a
  aufgespannten Vertikalebene liegt; damit ist der Winkel α_S
  zwischen d̂ und der Horizontalebene gleich dem Winkel zwischen
  ê_fall und der Horizontalebene und nach `hg_dachneigung.md`
  gleich der Dachneigung der zugeordneten Dachfläche.
- **Mehrfachzuordnung**: Ein Sparren ist Bauteil **genau einer**
  Dachfläche; bei Verschneidungs-Sparren (Gratsparren, Kehlsparren),
  die auf zwei Dachflächen liegen, ist die Falllinien-
  Kollinearitätsbedingung **nicht** zu beiden Dachflächen
  gleichzeitig erfüllbar, weshalb diese Sonderformen eigene
  Begriffsdefinitionen erhalten (siehe Abgrenzung).
- **Nicht-Zirkularität**: Die Definition stützt sich nur auf
  bereits definierte Begriffe (`bauteil`, `bauteilachse`,
  `strecke`, `einheitsvektor`, `ebene`, `dachflaeche`,
  `falllinie`, `dachneigung`, `weltkoordinatensystem`,
  `toleranzen`). Sie kommt nicht in ihrer eigenen Definition vor
  und verweist nicht auf Sparren-Spezialisierungen oder Pfetten.
- **Auflagerung (qualitativ, nicht Bestandteil der Definition)**:
  Ein Sparren wird im Tragwerk durch ein oder mehrere Auflager
  gestützt; in einem Pfettendach typischerweise durch eine
  Fußpfette am Sparrenfuß und eine Firstpfette am Sparrenfirstpunkt,
  ggf. eine zwischenliegende Mittelpfette; im Sparrendach durch
  das Gegenstück-Sparrenpaar (Druck am First) und ein horizontales
  Zugglied (Deckenbalken oder Kehlbalken) am Fuß. Die Auflagerung
  ist Eigenschaft des Tragwerks (siehe `hg_tragwerk.md`), nicht des
  Sparrens selbst. Die **Drei-Schichten-Trennung Kerve / Auflage-
  fläche / Auflager** (`hg_auflager.md` Quellenkonflikt-Block) gilt
  am Sparrenfuß sinngemäss: die Kerve ist die Bearbeitung am
  Sparrenpolyeder, die Kerv-Sohle ist die Auflagefläche, das
  Auflager-Aggregat trägt Wertigkeit und Lagerreaktion.

## Erläuterung (nicht normativ)

Der Sparren ist das **prägende Stab-Bauteil eines Dachtragwerks**:
seine regelmäßige, parallele Anordnung entlang der Falllinie einer
Dachfläche bestimmt das geometrische und statische Erscheinungsbild
des Daches.

### Sparrenlängen

In der Werkplan- und Abbund-Praxis treten am Sparren mehrere
Längsmasse auf, die sich auf unterschiedliche Endpunkte der
Bauteilachse beziehen. Die vorliegende Sektion fixiert die
glossarweit verbindliche Symbol- und Endpunkt-Konvention. Sie ist
so geschrieben, dass sie später leicht in einen eigenen
Glossareintrag `sparrenlaenge.md` ausgelagert werden kann; bis
dahin ist sie die normative Referenz für alle C4-Einträge.

Konvention: Alle hier eingeführten Längen werden **entlang der
Bauteilachse** A(B) zwischen zwei Punkten auf A(B) gemessen. Die
beiden Anker-Endpunkte sind der **Sparrenfußpunkt** p_a (an oder
nahe der Traufe; Anfangspunkt der Bauteilachse nach Bedingung 4
der mathematischen Definition) und der **Sparrenfirstpunkt** p_e
(an oder nahe dem First; Endpunkt der Bauteilachse). Ein dritter
ausgezeichneter Punkt auf A(B) ist der **Bleischnitt-Punkt der
Fußpfettenkerve** p_K nach `hg_kerve.md` Gleichungen (7a)/(7b);
er teilt die Bauteilachse in den traufseitigen Sparrenüberstand
[p_K, p_a] und das tragende Innenstück [p_K, p_e].

#### Symbol-Tabelle

| Symbol | Endpunkte auf A(B) | Bedeutung | Verwendet in |
|---|---|---|---|
| **`L_S`** | p_a (Sparrenfußpunkt) ↔ p_e (Sparrenfirstpunkt) | **Sparrenlänge im engeren Sinn**: volle Bauteilachsen-Länge des Sparrens; glossarweit normative Lesart von „Sparrenlänge" | `hg_sparren.md` (Definition), `hg_bauteilachse.md` (als Spezialfall von L), Werkplan-Hauptmaß |
| `s` | p_K ↔ Bleischnitt-Punkt der Firstpfettenkerve (analog p_K, aber an der Firstpfettenkerve) | **Axialer Kervenabstand**: Distanz der beiden Kervenmittelpunkte entlang der Bauteilachse; abgeleitet aus Firstpfetten- und Fußpfettenhöhe und der Dachneigung α via `s = (firstpfetteHoehe − fusspfetteHoehe) / sin(α)` | `hg_firstpfette.md`, BTLx-Export |
| `ℓ_K-S` | p_K (Fußpfettenkerve) ↔ p_e (Sparrenfirstpunkt) | **Sparrenlänge ohne Überstand** / **Tragspannweiten-Achsenlänge**: Bauteilachsen-Strecke vom Bleischnitt-Punkt der Fußpfettenkerve bis zum Sparrenfirstpunkt; im Pfettendach das tragende Innenstück | `hg_sparrenueberstand.md` Gleichung (6) |
| `ℓ_üb` | p_K (Fußpfettenkerve) ↔ p_a (Sparrenfußpunkt) | **Sparrenüberstand**: Bauteilachsen-Strecke vom Bleischnitt-Punkt der Fußpfettenkerve bis zum Sparrenfußpunkt; traufseitig auskragender Abschnitt | `hg_sparrenueberstand.md` Gleichung (3) |

#### Beziehungen

Aus der Definition der drei Punkte p_a, p_K, p_e auf der
Bauteilachse A(B) und der Vorzeichenkonvention (Bedingung 4
der mathematischen Definition: d̂ entgegen ê_fall, p_a unten,
p_e oben) folgt die Anordnung

```
p_a   −−−−   p_K   −−−−   p_e          (auf A(B), d̂ bergauf)
   ◄── ℓ_üb ──►  ◄────── ℓ_K-S ──────►
   ◄──────────── L_S ────────────────►
```

und damit die Zerlegung

```
L_S = ℓ_üb + ℓ_K-S.                                                (*)
```

Der axiale Kervenabstand `s` zwischen Fußpfetten- und
Firstpfettenkerve ist die Strecke zwischen den beiden p_K-
Punkten der beiden Kerven; bei Sparren ohne Firstpfettenkerve
(reine Auflagerung am First, Sparren-an-Sparren-Stoss) ist `s`
nicht definiert.

#### Empfohlene Lesart

- **„Sparrenlänge"** ohne weiteren Zusatz bezeichnet in dieser
  App und im Glossar die **volle Bauteilachsen-Länge L_S**
  zwischen Sparrenfußpunkt und Sparrenfirstpunkt; alle anderen
  Sparren-Längsmasse werden mit qualifiziertem Bezeichner
  („Sparrenüberstand", „Sparrenlänge ohne Überstand", „axialer
  Kervenabstand") geführt.
- Im einfachsten Werkmodell (Sparren ohne Kerve, ohne Anschnitt,
  ohne Überstand) reduziert sich die Differenzierung; L_S bleibt
  das einzige relevante Längsmass und p_K fällt mit p_a zusammen.

#### Folgearbeit (trigger-basiert)

Bei Werkplan-Beschriftungs-Tools werden weitere Längen-Begriffe
relevant, etwa:

- **Sparrenlänge inklusive Anschnitt** (vom äussersten Punkt des
  Sparrenfuß-Anschnitts bis zum äussersten Punkt des First-Anschnitts,
  also die Roh-Bauteillänge vor Abbund); ergänzt die Tabelle um
  einen vierten Längs-Begriff.
- **Abgewickelte Sparrenlänge** (für die Werkplan-Bemassung der
  Lattenraster-Längen entlang der Sparren-Oberseite, falls
  Lattung modelliert wird).

Diese können dann als zusätzliche Zeilen der Symbol-Tabelle
nachgezogen oder gemeinsam mit den vier oben genannten in einen
eigenen Glossareintrag `sparrenlaenge.md` ausgelagert werden.
Trigger: erstes Werkplan-Beschriftungs-Tool, das explizite
Längen-Annotationen am Sparren erzeugt.

### Querschnitt und Werkstoff

Sparren werden im Schweizer Wohnbau typisch als **Vollholz** in
Festigkeitsklasse C24 (Fichte/Tanne, sortiert nach SIA 265 / DIN
4074-1) ausgeführt; im größeren Spannweitenbereich oder bei
sichtbaren Dachstühlen auch als **Brettschichtholz** (BSH, GL24h).
Übliche Querschnitte:

- 60/120 mm bis 80/160 mm bei kleinen Spannweiten,
- 80/200 mm bis 100/240 mm bei mittleren Spannweiten,
- größere Querschnitte bei großen Achsabständen oder hohen Lasten.

Die konkrete Querschnittsfindung ist Gegenstand der **Bemessung**
nach SIA 265 / EN 1995-1-1 und liegt nicht im Definitionsbereich
dieses Glossars.

### Faserrichtung

Die **Faserrichtung** eines Sparrens ist im Regelfall **parallel
zur Bauteilachse**: das Bauteil wird so aus dem Stamm geschnitten,
dass die Längsfaser entlang der Bauteillänge verläuft. Die
Faserneigung (siehe `faserrichtung`) ist im prismatischen Idealfall
0; Abweichungen werden über die Sortierklasse begrenzt (DIN 4074-1).
In der Domänen-Schicht ist `faserrichtung` Annotation des Bauteils
und für Sparren als **Default ‖ d̂_Sparren** zu setzen.

### Sparren in den vier Hauptsystemen

- **Sparrendach**: Sparrenpaare bilden mit einem horizontalen
  Zugglied (Deckenbalken oder Kehlbalken) ein statisches Dreieck.
  Auflager sind das Gegenstück-Sparrenpaar (Druck am First) und
  das Zugglied (Aufnahme des Horizontalschubs am Fuß). Es gibt
  **keine Firstpfette und keine Mittelpfette**.
- **Pfettendach**: Sparren liegen auf horizontalen Pfetten
  (Fußpfette am Sparrenfuß, ggf. Mittelpfette in Sparrenmitte,
  Firstpfette am Sparrenfirstpunkt). Die Pfetten leiten die
  Sparrenlasten in Wände, Stützen oder Stuhlsäulen ab.
- **Kehlbalkendach**: Erweiterung des Sparrendachs um einen
  horizontalen Kehlbalken auf etwa halber Sparrenhöhe; halbiert
  die Knicklänge des Sparrens.
- **Binderdach**: Sparren als Sekundärtragwerk auf vorgefertigten
  Bindern (Nagelbinder, BSH-Binder), in regelmäßigem Achsabstand
  des Binders.

### Typische Verbindungen am Sparren

Diese Verbindungen sind Geometrien an Sparren und/oder Pfetten;
sie werden in eigenen Glossareinträgen definiert. Hier nur als
Verortung:

- **Versatz** am Sparrenfuß auf der Fußpfette
  (Stirn-, Fersen-, doppelter Versatz);
- **Kammverbindung** am Übergang zur Mittelpfette;
- **Anschnitt** am Firstanschluss (Stirn-Anschnitt zweier
  gegenüberstehender Sparren oder Auflagerung auf Firstpfette);
- **Sparrenanschlag** an der Fußpfette (Querholz-Auflagerung
  ohne Versatz).

### Sonderformen (eigene Folge-Einträge)

- **Gratsparren** (`gratsparren`): Sparren entlang eines Grats
  (konvexe Schnittkante zweier Dachflächen, etwa an einer
  Walmdach-Ecke). Liegt **nicht** auf einer einzelnen Dachfläche,
  sondern auf der Schnittgeraden zweier Trägerebenen. Querschnitt
  meist größer als der Standardsparren.
- **Kehlsparren** (`kehlsparren`): Sparren entlang einer Kehle
  (konkave Schnittkante zweier Dachflächen, an einspringender Ecke).
  Geometrisch analog zum Gratsparren, statisch und konstruktiv
  anders (sammelt Wasser, höhere Auflasten durch Schneeansammlung).
- **Schiftsparren** (`schiftsparren`, regional auch
  „Verschneidungssparren", uneinheitlich auch als Sammelbegriff
  für Grat-/Kehlsparren verwendet — siehe `hg_gratsparren.md`):
  verkürzte Sparren, die an einem Grat- oder Kehlsparren ansetzen
  statt am First.

## Beziehungen

- **Oberbegriff**: `bauteil`. Strukturell ist der Sparren ein
  Bauteil mit der zusätzlichen Rolle „Sparren" und den oben
  formalisierten geometrischen Constraints.
- **Bestandteile (partitiv)**:
  - **Bauteilachse** (`bauteilachse.Gerade`, vom Bauteil geerbt)
    mit Sparrenfuß als Anfangs- und Sparrenfirstpunkt als Endpunkt;
  - **Querschnitt** (vom Bauteil geerbt; rechteckig im Regelfall);
  - **Werkstoff** (vom Bauteil geerbt; Vollholz oder BSH);
  - **Faserrichtung** (Annotation, Default ‖ d̂_Sparren);
  - **Sparrenfuß-Punkt** und **Sparrenfirstpunkt** als
    abgeleitete Endpunkte der Bauteilachse.
- **Spezialisierungen (eigene Folge-Einträge)**:
  - **Gratsparren** (`gratsparren`)
  - **Kehlsparren** (`kehlsparren`)
  - **Schiftsparren** (`schiftsparren`)
- **Verwendung / Beziehung zu anderen Bauteilen**:
  - **Pfette** (`pfette`): Auflager des Sparrens im Pfettendach
    (Fuß-, Mittel-, Firstpfette).
  - **Kehlbalken** (`kehlbalken`): Aussteifungs-Querholz zwischen
    Sparrenpaar im Kehlbalkendach.
  - **Binder** (`binder`, bereits angelegt): mehrteiliges
    Trag-Aggregat (`oberbegriff: bauteilgruppe`); ein Sparren
    kann **Bestandteil höchstens einer Bauteilgruppe** sein
    (`hg_bauteilgruppe.md` Bed. 1 — exklusive Mitgliedschaft).
    Ein Sparrenbinder-Sparren gehört exklusiv zu diesem Binder.
  - **Latte** (`latte`, bereits angelegt): liegt **auf** dem
    Sparren, quer zur Bauteilachse (rechtwinklig zur Sparrenachse,
    parallel zu einer Höhenlinie), als Auflage für die Eindeckung.
  - **Konterlatte** (`konterlatte`, bereits angelegt):
    liegt zwischen Sparren und Latte, parallel zum Sparren entlang
    Falllinie, zur Hinterlüftung des Unterdachs.
  - **Dachfläche** (`dachflaeche`): zugeordnete geometrische
    Fläche; die Sparrenachsen liegen in deren Trägerebene.
- **Abgrenzung**:
  - **Pfette** (`pfette`): horizontaler Längsträger; quer zum
    Sparren. Ein Sparren ist geneigt entlang der Falllinie, eine
    Pfette ist horizontal entlang einer Höhenlinie der
    Dachfläche.
  - **Kehlbalken** (`kehlbalken`): horizontaler Querbalken
    zwischen einem Sparrenpaar zur Aussteifung. Kein Sparren
    (anderer Lagebezug, andere Funktion).
  - **Gratsparren / Kehlsparren**: liegen auf der Schnittkante
    zweier Dachflächen, nicht in einer einzelnen Trägerebene
    entlang ihrer Falllinie. Erfüllen Bed. 3 nicht.
  - **Binder**: vorgefertigtes, mehrteiliges Trag-Aggregat
    (Nagelbinder, BSH-Binder, Fachwerkbinder). Kein Stabbauteil
    im Sinne des Sparrens.
  - **Latte / Konterlatte**: Sekundärbauteile mit kleinerem
    Querschnitt zur Auflage der Dachhaut bzw. Hinterlüftung; sie
    liegen quer (Latte) bzw. parallel (Konterlatte) zum Sparren,
    sind aber nicht selbst Sparren.
  - **Dachfläche**: zweidimensionales geometrisches Bauteil; der
    Sparren ist ein Stab-Bauteil mit Achse in der Trägerebene
    der Dachfläche.

## Implementierungshinweis

Datentyp (Domänen-Schicht, Kotlin, Schicht `domain.bauteil`):

```kotlin
package domain.bauteil

import domain.Toleranzen
import domain.bauteil.Bauteil
import domain.bauteil.Bauteilachse
import domain.bauteil.BauteilId
import domain.geometrie.Einheitsvektor
import domain.geometrie.Punkt
import domain.holzbau.Faserrichtung

/**
 * Sparren als Bauteilrolle: Stab-Bauteil entlang der Falllinie einer
 * Dachfläche.
 *
 * Glossar: hg_sparren.md
 *
 * Vorzeichenkonvention (normativ):
 *   p_a = Sparrenfuß  (an/nahe der Traufe)
 *   p_e = Sparrenfirstpunkt (an/nahe dem First / der Pultkante)
 *   d̂  zeigt nach oben (⟨d̂, e_z⟩ ≥ 0), entgegen der Falllinie ê_fall.
 *
 * Querschnitts- und Werkstoff-Annotationen werden vom umschlossenen
 * Bauteil übernommen. Faserrichtung ist im Regelfall parallel zur
 * Bauteilachse zu setzen.
 */
data class Sparren(
    val bauteil: Bauteil,
    val dachflaeche: Dachflaeche
) {
    init {
        require(bauteil.geometrie is Bauteilgeometrie.Stab) {
            "Sparren erfordert Stabgeometrie"
        }
        // Lage- und Falllinien-Bedingungen werden in der Factory
        // sparrenAusBauteil(...) geprüft und liefern bei Verletzung
        // ein Resultat.Fehler mit SparrenEntartet-Variante (siehe unten).
    }

    val sparrenfuss: Punkt get() = achse().anfang
    val sparrenfirstpunkt: Punkt get() = achse().ende
    val laenge: Double get() = achse().laenge        // mm
    val sparrenneigung: Double                        // rad
        get() = dachflaeche.dachneigung()

    private fun achse(): Bauteilachse.Gerade =
        (bauteil.geometrie as Bauteilgeometrie.Stab).achse as Bauteilachse.Gerade
}

sealed class SparrenEntartet {
    object NichtInTraegerebene : SparrenEntartet()
    object NichtAufFalllinie  : SparrenEntartet()
    object FalscheRichtung    : SparrenEntartet()   // d̂ zeigt nach unten
    object Nullachse          : SparrenEntartet()
    object FlacheDachflaeche  : SparrenEntartet()   // α = 0, Falllinie undef.
}
```

- **Einheit**: Längen in mm (Double), Winkel intern in Radiant.
- **Identität**: `BauteilId` aus dem zugrunde liegenden Bauteil.
- **Invarianten** (in der Factory `sparrenAusBauteil(...)` prüfen,
  bei Verletzung `Resultat.Fehler` mit der jeweiligen
  `SparrenEntartet`-Variante; niemals Exception):
  1. Stabgeometrie und Bauteilachse vom Typ `Bauteilachse.Gerade`.
  2. Achsenlänge > Toleranzen.LAENGE_EPS — sonst `Nullachse`.
  3. p_a, p_e ∈ Trägerebene der Dachfläche bis ε_L — sonst
     `NichtInTraegerebene`.
  4. Dachfläche geneigt (α > 0) — sonst `FlacheDachflaeche`.
  5. |⟨d̂, ê_fall⟩| ≥ 1 − ε_W — sonst `NichtAufFalllinie`.
  6. ⟨d̂, ê_fall⟩ ≤ −1 + ε_W (d̂ zeigt nach oben) — sonst
     `FalscheRichtung` (Konsumenten können hier durch Achsen-
     Umkehr automatisch korrigieren).
- **Edge Cases**:
  - **Pultsparren**: Pultdach mit nur einer Dachfläche; Sparren
    geht von der Traufe zur Pultkante. Definition unverändert
    anwendbar; p_e liegt dann auf der Pultkante statt am First.
  - **Sparren am Ortgang**: identisch zum Standardsparren, aber
    der Bauteilachse fällt mit einer Ortgangkante zusammen
    (siehe `ortgang`). Nicht zu verwechseln mit dem Sparren als
    Geometrie der Ortgangkante; der Ortgangsparren ist ein
    Sparren mit Achse = Ortgangstrecke.
  - **Aufgekämmter Sparren** (mit eingearbeitetem Versatz an der
    Fußpfette): die Bauteilachse bleibt die geometrische
    Schwerlinie; der Versatz ist eine separate Geometrie-
    Modifikation am Bauteil und nicht Bestandteil der
    Sparren-Definition.
  - **Sehr flache Dachfläche** (α → 0): Falllinie wird entartet;
    in diesem Fall ist die App auf eine Pultdach- bzw. Flachdach-
    Modellierung ohne klassische Sparrenrichtung umzustellen.
- **Abgeleitete Eigenschaften** (als Funktionen):
  - `sparrenneigung(): Double` — = Dachneigung der zugeordneten
    Dachfläche, in Radiant.
  - `auflagerKandidaten(t: Tragwerk): List<Pfette>` — Pfetten in
    `t`, deren Bauteilachse die Sparrenbauteilachse innerhalb
    Toleranzen schneidet (Bemessungs-Hilfsfunktion).
  - `faserneigung(): Double?` — falls Faserrichtung gesetzt:
    Winkel zwischen Faserrichtung und Sparrenachse; sonst null.
- **Bezeichner-Konvention** (CLAUDE.md): Klasse heißt `Sparren`
  (deutsch, Glossarbegriff); Spezialisierungen heißen
  `Gratsparren`, `Kehlsparren`, `Schiftsparren`.

## Quellen

**Primär (normativ):**

- SIA 265:2021, „Holzbau", Schweizerischer Ingenieur- und
  Architektenverein, Zürich.
- SIA 232/1:2020, „Geneigte Dächer", Schweizerischer Ingenieur-
  und Architektenverein, Zürich.
- DIN EN 1995-1-1:2010-12, „Eurocode 5: Bemessung und Konstruktion
  von Holzbauten – Teil 1-1: Allgemeines".
- DIN 1052:2008-12, „Entwurf, Berechnung und Bemessung von
  Holzbauwerken".
- DIN EN 14081-1:2019-10, „Holzbauwerke – Nach Festigkeit
  sortiertes Bauholz mit rechteckigem Querschnitt – Teil 1".

**Sekundär:**

- Lignum (Hrsg.): *Holzbautabellen HBT.* Lignum, Zürich, aktuelle
  Auflage.
- Lignum (Hrsg.): *Lignatec — Geneigte Dächer in Holzbauweise.*
  Lignum, Zürich, aktuelle Auflage.
- Mönck, W.; Rug, W.: *Holzbau – Bemessung und Konstruktion.*
  16. Auflage, Beuth, Berlin 2015.
- Blass, H. J.; Sandhaas, C.: *Ingenieurholzbau – Grundlagen der
  Bemessung.* KIT Scientific Publishing, Karlsruhe 2016.
- Natterer, J.; Herzog, T.; Volz, M.: *Holzbau-Atlas.* 4. Auflage,
  Birkhäuser, Basel 2003.
- Gerner, M.: *Fachwerk – Instandsetzung, Sanierung, Neubau.*
  DVA, 7. Auflage 2007.

**Korpus (nicht autoritativ):**

- Holzbau Deutschland, Merkblatt „Begriffe und Klassifizierungen
  für den Holzbau" (abgerufen 2026-05-08).
- Wikipedia, Lemma „Sparren" (abgerufen 2026-05-08).
