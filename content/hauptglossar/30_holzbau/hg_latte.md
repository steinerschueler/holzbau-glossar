---
id: latte
benennung: Latte
synonyme: [Dachlatte, Traglatte, Ziegellatte]
abgelehnte_benennungen: [Konterlatte, Schalung, Bretterlattung, Schalungsbrett, Lattung, Traglattung, Riegel, Solarlatte, Stahllatte, "batten", "lath", "roof batten", "tile batten"]
oberbegriff: bauteil
begriffstyp: bauteilrolle
voraussetzungen: [bauteil, bauteilachse, strecke, einheitsvektor, ebene, dachflaeche, sparren, weltkoordinatensystem, toleranzen]
abgrenzung_zu: [sparren, pfette, konterlatte, schalung, brett, dachaufbau, dachflaeche, dachhaut, eindeckung, ziegel, hoehenlinie, falllinie, bauteil]
status: entwurf
subglossar_pendant: notwendig
quellen_primär:
  - "SIA 232/1:2020 'Geneigte Dächer', Schweizerischer Ingenieur- und Architektenverein, Abschnitt 1 (Begriffe) und Abschnitt 2 (Aufbau geneigter Dächer): Lattung als Bestandteil des Dachaufbaus, Auflage der Eindeckung."
  - "SIA 265:2021 'Holzbau', Schweizerischer Ingenieur- und Architektenverein, Abschnitt 4 (Bemessung): Latten als biegebeanspruchte Sekundär-Stab-Bauteile."
  - "SIA 265/2:2023 'Sortierung von Holz nach der Tragfähigkeit — Nadelschnittholz gemäss DIN 4074-1', Schweizerischer Ingenieur- und Architektenverein, Zürich."
  - "DIN EN 1995-1-1:2010-12 (Eurocode 5), Abschnitt 5 (Tragwerksberechnung): Latten als biegebeanspruchte Stab-Bauteile."
  - "DIN EN 14081-1:2019-10 'Holzbauwerke — Nach Festigkeit sortiertes Bauholz mit rechteckigem Querschnitt — Teil 1: Allgemeine Anforderungen', harmonisiertes CE-Regelwerk."
  - "DIN 4074-1 'Sortierung von Holz nach der Tragfähigkeit — Teil 1: Nadelschnittholz' (Sortierklassen S10/S13 für Dachlatten)."
  - "DIN 4070-1:1958-01 'Nadelholz; Querschnittsmaße und statische Werte für Schnittholz, Vorratskantholz und Dachlatten' (Standardquerschnitte 24/48, 30/50, 40/60 mm)."
quellen_sekundär:
  - "Lignum (Hrsg.): Lignatec 'Geneigte Dächer in Holzbauweise', Lignum, Zürich, aktuelle Auflage, Kap. 'Lattung'."
  - "Lignum (Hrsg.): Holzbautabellen HBT, Lignum, Zürich, aktuelle Auflage."
  - "Mönck, W.; Rug, W.: Holzbau – Bemessung und Konstruktion. 16. Aufl., Beuth, Berlin 2015, Kap. 11 'Dachtragwerke'."
  - "Natterer, J.; Herzog, T.; Volz, M.: Holzbau-Atlas. 4. Aufl., Birkhäuser, Basel 2003, Kap. 'Dachaufbau / Lattung'."
  - "Gerner, M.: Fachwerk – Instandsetzung, Sanierung, Neubau. DVA, 7. Aufl. 2007, Glossar 'Dachlatte'."
quellenkonflikt: |
  Weder SIA 232/1, SIA 265, EN 1995-1-1 noch DIN 1052 enthalten eine
  geschlossene Begriffsdefinition für „Latte"; der Begriff wird in
  allen konsultierten Normen vorausgesetzt und über seine konstruktive
  Rolle (Sekundär-Stab-Bauteil quer auf dem Sparren, als Auflage für
  die Eindeckung) charakterisiert. Die DIN 4070-1 fasst „Dachlatten"
  geometrisch über Querschnittsmaße (drei Standardquerschnitte
  24/48, 30/50, 40/60 mm); DIN 4074-1 regelt die Festigkeitssortierung
  in S10/S13. SIA 265/2:2023 verweist explizit auf DIN 4074-1, womit
  CH und DE in der Sortierregel identisch sind.

  In der Sekundärliteratur (Mönck/Rug, Natterer/Herzog/Volz, Lignum-
  Lignatec, Gerner) wird die Latte durchgängig als „stabförmiges
  Sekundärbauteil, rechtwinklig zum Sparren auf dessen Oberseite
  bzw. auf einer Konterlatte verlegt, als Auflager der Eindeckung
  (Ziegel, Schiefer, Schindel, Blechprofil)" beschrieben.

  Eigene Festlegung in diesem Glossar:

  - Eine Latte ist ein **Bauteil mit Bauteilrolle „Latte"**, dessen
    Bauteilachse rechtwinklig zur Sparrenachse einer zugeordneten
    Dachfläche verläuft, horizontal liegt (parallel zu Traufe und
    First, also parallel zu einer Höhenlinie der Trägerebene der
    Dachfläche) und parallel-versetzt zur Trägerebene der Dachfläche
    liegt (versetzt um die Sparrenhöhe bzw. Sparrenhöhe plus
    Konterlattenhöhe nach außen).
  - „Dachlatte", „Traglatte" und „Ziegellatte" sind synonyme
    Benennungen derselben Bauteilrolle; sie werden im DACH-
    Holzbau-Korpus austauschbar verwendet. „Traglatte" betont die
    Abgrenzung zur Konterlatte; „Dachlatte" ist historisch und
    allgemeinsprachlich dominant; „Ziegellatte" ist die ältere,
    materialbezogene Benennung.
  - Eine **Verschachtelung in `traglatte`-Subtyp** wird **nicht**
    eingeführt: „Traglatte" ist Synonym, keine echte Spezialisierung.
  - **„Konterlatte"** ist eine **eigene Bauteilrolle** (parallel zum
    Sparren statt rechtwinklig, andere Funktion: Hinterlüftung statt
    Eindeckungs-Auflage) und wird im eigenen Eintrag `konterlatte`
    geführt; sie ist hier in `abgelehnte_benennungen` aufgeführt,
    weil sie als Synonym für die Latte unzulässig wäre.
  - **„Lattung" / „Traglattung"** bezeichnen die Schicht-Aggregate
    mehrerer Latten zusammen und sind als Funktionsklassen
    `KONTERLATTUNG` / `TRAGLATTUNG` bereits in `dachaufbau` getragen;
    sie sind hier in `abgelehnte_benennungen` aufgeführt, weil sie
    sich auf die Schicht beziehen, nicht auf das Einzelbauteil.
  - **„Solarlatte" / „Stahllatte"** sind Produktbezeichnungen ohne
    normative Verankerung; sie werden hier abgelehnt und allenfalls
    als Korpus-Begriffe in der Erläuterung erwähnt.

  Diese Festlegung ist konsistent mit allen konsultierten Quellen.
---

## Prosa-Definition

Eine **Latte** ist ein stabförmiges Sekundärbauteil eines Daches,
dessen Bauteilachse rechtwinklig zur Sparrenachse einer zugeordneten
Dachfläche und parallel-versetzt zur Trägerebene dieser Dachfläche
horizontal verläuft, das die Lasten der Eindeckung (Ziegel,
Schindeln, Blech) sowie die Verkehrs-, Schnee- und Windlasten
flächig sammelt und über seine Auflager (die quer zur Latte
verlaufenden Sparren oder eine zwischengelegte Konterlatte) als
Streckenlast in das Sparrentragwerk einträgt.

## Mathematische Definition

Sei

- B ein Bauteil im Sinne von `bauteil` mit Stabgeometrie
  (`geometrie ∈ 𝒢_stab`),
- a(B) = Bauteilachse.Gerade(p_a, p_e) die Bauteilachse von B im
  geraden Fall (siehe `bauteilachse`), mit
  d_hat := (p_e − p_a) / ‖p_e − p_a‖ ∈ S² ⊂ ℝ³,
- D = (E, P, n_a) eine Dachfläche im Sinne von `dachflaeche` mit
  Trägerebene E (Stützpunkt p₀, Normalenvektor n_a), Polygon P und
  äußerer Normaler n_a,
- S ein Sparren der Dachfläche D im Sinne von `sparren`, mit
  Richtungs-Einheitsvektor d_hat_S der Sparrenachse,
- e_z := (0, 0, 1)ᵀ die vertikale Achse,
- ε_K := Toleranzen.KOLLINEAR_EPS,
  ε_W := Toleranzen.WINKEL_EPS,
  ε_L := Toleranzen.LAENGE_EPS.

Dann heißt B eine **Latte** der Dachfläche D genau dann, wenn die
folgenden Bedingungen erfüllt sind:

1. **Stabgeometrie**: B besitzt eine gerade Bauteilachse mit
   ‖p_e − p_a‖ > ε_L.

2. **Parallelität zur Trägerebene**: Die Bauteilachsenrichtung d_hat
   liegt parallel zur Trägerebene E,
   ```
   |⟨n_a, d_hat⟩| ≤ ε_K.
   ```
   Die Achse selbst liegt typischerweise nicht in E, sondern in einer
   zu E parallel-versetzten Ebene E' mit Versatz ≈ Sparrenhöhe (bzw.
   Sparrenhöhe + Konterlattenhöhe) entlang n_a; der Versatz selbst
   ist nicht Bestandteil dieser Definition, sondern Eigenschaft des
   `dachaufbau`.

3. **Horizontalität**: Die Bauteilachsenrichtung steht rechtwinklig
   zur Welt-Lotachse,
   ```
   |⟨d_hat, e_z⟩| ≤ ε_K.
   ```
   Die Form des Tests ist ein **Sinus-Test gegen e_z-Parallelität**
   (Lot-Prädikat); nach `_KONVENTIONEN.md` Sektion 4 ist
   `KOLLINEAR_EPS` die einschlägige Toleranzkonstante.

4. **Rechtwinkligkeit zur Sparrenachse**: Es existiert mindestens
   ein Sparren S der zugeordneten Dachfläche D mit
   ```
   |⟨d_hat, d_hat_S⟩| ≤ ε_K.
   ```
   Die Lattenachse steht damit rechtwinklig zur Sparrenachse;
   nach Bedingungen 2–4 zusammen liegt sie parallel zu einer
   Höhenlinie der Trägerebene E (Höhenlinie der Trägerebene =
   horizontale Gerade in einer Ebene parallel zu E; siehe
   `abgrenzung_zu` Forward-Verweis `hoehenlinie`).

Wesentliche abgeleitete Größen:

- **Lattenlänge**: L_L := ‖p_e − p_a‖ (in mm), entlang der
  Bauteilachse zwischen den Lattenenden.
- **Lattenrichtung**: d_hat ∈ S² mit |⟨d_hat, e_z⟩| ≤ ε_K und
  |⟨d_hat, d_hat_S⟩| ≤ ε_K.
- **Latten-Höhenlage**: z_L := (p_a.z + p_e.z) / 2; bei einer
  exakt horizontalen Latte gilt p_a.z = p_e.z = z_L.
- **Lattenachsabstand** (Lattenweite): bei einer parallelen
  Lattenschar L_1, …, L_n auf derselben Dachfläche der
  Abstand benachbarter Bauteilachsen, gemessen entlang d_hat_S
  in der parallel-versetzten Ebene E'. Der Lattenachsabstand
  ist Eigenschaft des `dachaufbau` (eindeckungsabhängig) und
  nicht Bestandteil der Latten-Definition.

## Wohldefiniertheit

- **Existenz**: Für jedes Stabbauteil mit positiver Achsenlänge,
  Achsenrichtung parallel zur Trägerebene und rechtwinklig
  sowohl zur Welt-Lotachse als auch zur Sparrenachse einer
  zugeordneten Dachfläche sind alle vier Bedingungen konstruktiv
  erfüllbar; jede Standard-Dachlatte auf einer Satteldachhälfte ist
  das Standardbeispiel.
- **Eindeutigkeit der Lattenrichtung**: Bedingungen 3 und 4
  zusammen fixieren d_hat bis auf das Vorzeichen: für eine geneigte
  Dachfläche mit gegebener Sparrenrichtung d_hat_S existiert (bis auf
  Vorzeichen) genau ein Einheitsvektor d_hat, der sowohl rechtwinklig
  zu e_z als auch rechtwinklig zu d_hat_S steht — nämlich
  d_hat = ±(d_hat_S × e_z) / ‖d_hat_S × e_z‖. Auf einer horizontalen
  Dachfläche (α = 0) ist d_hat_S undefiniert, sodass die Latten-
  Definition keine Anwendung findet; dies ist der Flachdach-
  Sonderfall (siehe Edge Cases).
- **Vorzeichenkonvention**: Die Bauteilachse einer Latte ist
  gerichtet (`Bauteilachse.Gerade`), aber welcher Endpunkt p_a
  bzw. p_e ist, ist auf der Ebene des Begriffs „Latte" **nicht**
  durch eine geometrische Bedingung festgelegt (analog zur Pfette).
  Empfehlung gemäß `hg_bauteilachse.md`: p_a nach lokaler
  Bezeichnungskonvention (z. B. niedrigeres x in Welt-Koordinaten
  oder gemäß Achsplan). Konsumenten dürfen sich nicht auf eine
  geometrisch zwingende Orientierung verlassen.
- **Konsistenz mit `sparren` und `pfette`**: Die Lattenrichtung
  ist nach Bedingung 4 rechtwinklig zur Sparrenrichtung; nach
  Bedingung 3 ist sie horizontal. Sie ist damit **parallel zu
  einer Pfettenrichtung** desselben Dachs (`pfette` Bedingung 2
  Horizontalität + Bedingung 3 Parallelität zu einer Dachkante
  Traufe/First/Höhenlinie). Latte und Pfette unterscheiden sich
  geometrisch nur durch Höhenlage und Querschnitt-Größenordnung
  (siehe Beziehungen: Abgrenzung Latte ↔ Pfette).
- **Konsistenz mit `dachaufbau`**: Die Latten bilden in der
  geordneten Schichtfolge des `dachaufbau` die Funktionsklasse
  `TRAGLATTUNG` (zweitäußerste Schicht des geneigten Dachs,
  unmittelbar unter der Eindeckung). Der Versatz der Latten-
  achse gegenüber der Trägerebene E der Dachfläche entspricht
  der summarischen Dicke der darunterliegenden Schichten (Sparren-
  Oberseite zu Lattenachse = Sparrenhöhe + ggf. Konterlattenhöhe +
  halbe Lattenhöhe).
- **Nicht-Zirkularität**: Die Definition stützt sich nur auf
  bereits definierte Begriffe (`bauteil`, `bauteilachse`,
  `strecke`, `einheitsvektor`, `ebene`, `dachflaeche`, `sparren`,
  `weltkoordinatensystem`, `toleranzen`). Sie kommt nicht in
  ihrer eigenen Definition vor und verweist nicht auf Latten-
  Spezialisierungen.
- **Mindestens-ein-Sparren-Bedingung**: Bedingung 4 fordert die
  Existenz mindestens eines rechtwinklig zur Lattenachse
  stehenden Sparrens. In der Praxis liegt jede Latte auf
  mindestens zwei Sparren auf; die Bemessung als Mehrfeldträger
  und die Auflagerung sind Eigenschaften des Tragwerks
  (`tragwerk`), nicht der Latte selbst.
- **Auflagerung (qualitativ, nicht Bestandteil der Definition)**:
  Eine Latte wird im Dachaufbau durch zwei oder mehr Sparren
  (bzw. Konterlatten) als Auflager gestützt; die Auflagerung
  ist Eigenschaft des Tragwerks bzw. des Dachaufbaus, nicht der
  Latte selbst.

## Erläuterung (nicht normativ)

Die Latte ist das **prägende Sekundärbauteil eines geneigten
Daches**: ihre regelmäßige, parallele Anordnung quer zum Sparren
in der äußersten oder zweitäußersten Lattungsebene des
Dachaufbaus erzeugt das Raster, das die Eindeckung aufnimmt.
Geometrisch ist die Latte das **horizontale Gegenstück zur
Sparrenrichtung**, materiell ist sie ein **Sekundärbauteil
mit deutlich kleinerem Querschnitt als jede Pfette**.

### Querschnitt und Sortierung

Die drei Standard-Querschnitte für Dachlatten in der DACH-Region
gehen auf DIN 4070-1 (1958) zurück und werden in DIN EN 14081-1
und DIN 4074-1 fortgeführt:

| Querschnitt (h × b) | typische Verwendung | Sortierklasse |
|---|---|---|
| **24 × 48 mm** | Sparrenabstand ≤ ca. 70 cm, leichte Eindeckung | S13 |
| **30 × 50 mm** | Standard bei Ziegel-Eindeckung, Sparrenabstand bis ca. 80 cm | S10 |
| **40 × 60 mm** | Sparrenabstand > 80 cm, schwere Eindeckung, hohe Schneelast | S10 oder S13 |

Sortier-Konvention (DIN 4074-1, in der Schweiz nach SIA 265/2:2023
identisch): S10 entspricht der Festigkeitsklasse C24, S13
entspricht C30 (nach DIN EN 338).

**Verlegerichtung**: Die Latte wird **liegend** verlegt (Breite
parallel zur Sparrenoberseite, kürzere Kante als Höhe), Biegung
um die starke Achse rechtwinklig zur Sparrenoberseite. Diese
Verlegung ist die bewusste Umkehrung zur Pfette, die hochkant
gestellt wird.

### Lattenachsabstand (Lattenweite)

Der Achsabstand benachbarter Latten ist **eindeckungsabhängig**
und damit Eigenschaft des Dachaufbaus, nicht des Tragwerks:

| Eindeckung | Lattenabstand (Achsmaß) |
|---|---|
| Tondachziegel (Falzziegel) | 32–36 cm |
| Betondachstein | 31–34 cm |
| Biberschwanz-Doppeldeckung | 16–18 cm |
| Naturschiefer | 12–18 cm |
| Holzschindel | ≈ 1/3 der Schindellänge |
| Blechprofil | 30–40 cm |

Diese Werte sind aus dem Branchen-Korpus zusammengetragen und
nicht als normative Vorgaben zu verstehen; die konkrete
Lattenweite ergibt sich aus dem Format der Eindeckungselemente
und der vom Hersteller vorgegebenen Decklänge.

### Faserrichtung

Die Faserrichtung einer Latte ist im Regelfall **parallel zur
Bauteilachse**: das Bauteil wird so aus dem Stamm geschnitten,
dass die Längsfaser entlang der Lattenlänge verläuft. Die
Faserneigung ist im prismatischen Idealfall 0; Abweichungen
werden über die Sortierklasse begrenzt (DIN 4074-1). In der
Domänen-Schicht ist `faserrichtung` Annotation des Bauteils und
für Latten als **Default ‖ d_hat_Latte** zu setzen.

### Statisches System und Bemessung

Die Latte wird typischerweise als **Mehrfeldträger** über zwei
oder mehr Sparrenauflager bemessen; maßgeblich sind:

- **Biegung um die starke Achse** unter Eindeckungs- und
  Verkehrslast (1,0 kN Mannlast als Punktlast für
  Begehbarkeit nach DIN EN 1991-1 / SIA 261),
- **Durchbiegungs-Begrenzung** (Gebrauchstauglichkeit, typisch
  L/200).

Schub und Auflagerpressung sind selten maßgeblich. Die konkrete
Bemessung erfolgt nach SIA 265 / DIN EN 1995-1-1 und liegt nicht
im Definitionsbereich dieses Glossars.

### Latte ≠ Konterlatte ≠ Pfette

Aus zimmermannssprachlicher Sicht ist die saubere Trennung
dieser drei Begriffe wichtig (siehe Abgrenzung):

- **Latte** (Traglatte): rechtwinklig zum Sparren, obere
  Lattenebene, trägt Eindeckung. Querschnitt 24/48 bis 40/60 mm.
- **Konterlatte**: **parallel** zum Sparren, untere Lattenebene,
  schafft die Hinterlüftungsebene zwischen Unterdach und
  Traglattung. Eigener Glossareintrag (`konterlatte`).
- **Pfette**: horizontaler Hauptträger des Dachtragwerks,
  Querschnitt ab 100/200 mm, trägt die Sparren. Geometrisch
  parallel zur Latte (beide horizontal, rechtwinklig zum
  Sparren), aber statisch und dimensional ein anderer Bauteiltyp.

### Hinweis zu Marketingvarianten

„Solarlatte" und „Stahllatte" sind Produktbezeichnungen ohne
normative Verankerung. Die „Solarlatte" ist eine in der
Eindeckungs-Ebene installierte Halterung für Solarmodule, oft als
Aluminiumprofil mit Lattenquerschnitt; sie ist kein Holzbauteil
und in diesem Glossar nicht als Latte zu modellieren. Die
„Stahllatte" ist ein Stahlprofil als Lattenersatz, ebenfalls
außerhalb der Holzbau-Modellierung dieses Glossars.

## Beziehungen

- **Oberbegriff**: `bauteil`. Strukturell ist die Latte ein
  Bauteil mit der zusätzlichen Rolle „Latte" und den oben
  formalisierten geometrischen Constraints.
- **Bestandteile (partitiv, vom Bauteil geerbt)**:
  - **Bauteilachse** (`bauteilachse.Gerade`);
  - **Querschnitt** (rechteckig, liegend verlegt;
    Standardquerschnitte 24/48, 30/50, 40/60 mm);
  - **Werkstoff** (Vollholz, Festigkeitsklasse C24 bzw. C30
    entsprechend Sortierklasse S10/S13);
  - **Faserrichtung** (Annotation, Default ‖ d_hat_Latte).
- **Verwendung / Beziehung zu anderen Bauteilen**:
  - **Sparren** (`sparren`): Auflager der Latte; die Latte liegt
    **auf** dem Sparren (ggf. über eine zwischengelegte
    Konterlatte), rechtwinklig zur Sparrenachse.
  - **Konterlatte** (Forward-Verweis, eigener Eintrag folgt):
    liegt parallel zum Sparren zwischen Sparrenoberseite und
    Latte; trägt die Latte, sofern eine Hinterlüftungsebene
    vorgesehen ist.
  - **Dachfläche** (`dachflaeche`): zugeordnete geometrische
    Bezugsebene; die Lattenachsen liegen in einer zu deren
    Trägerebene parallel-versetzten Ebene E'.
  - **Dachaufbau** (`dachaufbau`): die Latte ist Bestandteil
    der Funktionsklasse `TRAGLATTUNG` des Dachaufbaus.
  - **Eindeckung** (Forward-Verweis, eigener Eintrag folgt):
    liegt **auf** der Latte und überträgt ihre Lasten als
    Flächenlast in die Latte; das konkrete Eindeckungsmaterial
    (Ziegel, Schiefer, Blechprofil) bestimmt den Lattenabstand.
- **Abgrenzung**:
  - **Sparren** (`sparren`): geneigtes Stab-Bauteil entlang der
    Falllinie. Die Latte ist horizontal entlang einer
    Höhenlinie. Sparren und Latte sind rechtwinklig zueinander
    angeordnet (in der parallel-versetzten Ebene zur Trägerebene
    der Dachfläche).
  - **Pfette** (`pfette`): horizontaler Hauptträger des
    Dachtragwerks; trägt Sparren (nicht die Eindeckung).
    Geometrisch parallel zur Latte (horizontal, rechtwinklig
    zum Sparren), aber **Primärbauteil** mit deutlich größerem
    Querschnitt (ab 100/200 mm) und größerem Achsabstand
    (1–5 m statt 16–40 cm). Die Latte liegt im Dachaufbau
    **über** der Sparrenoberseite, die Pfette **unter** dem
    Sparren als sein Auflager.
  - **Konterlatte** (`konterlatte`, eigener Eintrag folgt):
    parallel zum Sparren statt rechtwinklig; andere Funktion
    (Hinterlüftung statt Eindeckungs-Auflage). Eigene Bauteilrolle.
  - **Schalung** / **Brett** (Forward-Verweise, eigene Einträge
    folgen): flächige Holzschalung (Bretter mit Querschnitt
    typisch h ≤ 40 mm, b ≥ 80 mm nach DIN 4070-1) als
    vollflächige Unterkonstruktion; die Latte hat nach DIN 4070-1
    eine Breite < 80 mm und ist damit geometrisch kein Brett.
    Funktional ist die Schalung eine flächige Auflage, die Latte
    eine punktuell-lineare Auflage.
  - **Eindeckung** (Forward-Verweis, eigener Eintrag folgt):
    die äußerste materielle Schicht des Dachaufbaus (Ziegel,
    Schindel, Blech), die **auf** der Latte aufliegt. Die Latte
    ist Auflager der Eindeckung, nicht selbst Eindeckung.
  - **Ziegel** (Forward-Verweis, eigener Eintrag folgt):
    Einzelelement der Eindeckung; die Latte trägt eine Reihe
    von Ziegeln und definiert über ihren Achsabstand die
    Decklänge.
  - **Dachaufbau** (`dachaufbau`): die Latte ist Bestandteil
    einer Schicht (Funktionsklasse `TRAGLATTUNG`), nicht der
    gesamte Schichtaufbau. Der Dachaufbau ist das Schicht-
    Aggregat, die Latte ist das Einzelbauteil innerhalb der
    Lattungsschicht.
  - **Dachfläche** (`dachflaeche`): zweidimensionales
    geometrisches Bauteil (Bezugsebene); die Latte ist ein
    Stab-Bauteil parallel-versetzt zu deren Trägerebene.
  - **Dachhaut** (`dachhaut`): geometrische Hüllfläche über
    der Eindeckung. Die Latte liegt **unter** der Eindeckung
    und damit deutlich unterhalb der Dachhaut.
  - **Höhenlinie** (Forward-Verweis): mathematisches Korpus-
    Konzept (horizontale Schnittlinie einer geneigten Ebene mit
    einer Horizontalebene); die Lattenachse fällt mit einer
    Höhenlinie der parallel-versetzten Ebene E' zusammen.
  - **Bauteil** (`bauteil`): die Latte ist eine Spezialisierung
    von Bauteil mit zusätzlichen geometrischen Constraints; ein
    Bauteil ohne Bauteilrolle ist keine Latte.

## Implementierungshinweis

Datentyp (Domänen-Schicht, Kotlin, Schicht `domain.bauteil`):

```kotlin
package domain.bauteil

import domain.Toleranzen
import domain.bauteil.Bauteil
import domain.bauteil.Bauteilachse
import domain.geometrie.Einheitsvektor
import domain.geometrie.Punkt
import kotlin.math.abs

/**
 * Latte als Bauteilrolle: stabförmiges Sekundärbauteil quer auf
 * Sparren als Auflage der Eindeckung.
 *
 * Glossar: hg_latte.md
 *
 * Vorzeichenkonvention: Die Bauteilachse ist gerichtet, aber welcher
 * Endpunkt p_a bzw. p_e ist, ist nicht durch eine geometrische
 * Bedingung festgelegt (analog zur Pfette). Empfehlung gemäß
 * hg_bauteilachse.md: p_a nach lokaler Bezeichnungskonvention.
 */
data class Latte(
    val bauteil: Bauteil,
    val dachflaeche: Dachflaeche
) {
    init {
        require(bauteil.geometrie is Bauteilgeometrie.Stab) {
            "Latte erfordert Stabgeometrie"
        }
        // Lage-, Horizontalitäts- und Orthogonalitäts-Bedingungen
        // werden in der Factory latteAusBauteil(...) geprüft und
        // liefern bei Verletzung ein Resultat.Fehler mit
        // LatteEntartet-Variante (siehe unten).
    }

    val achse: Bauteilachse.Gerade
        get() = (bauteil.geometrie as Bauteilgeometrie.Stab).achse
                as Bauteilachse.Gerade
    val laenge: Double get() = achse.laenge          // mm
    val richtung: Einheitsvektor get() = achse.richtung
    val hoehe: Double                                 // mm, mittlere z-Lage
        get() = (achse.anfang.z + achse.ende.z) / 2.0

    /**
     * Horizontalitätsprädikat: |⟨d_hat, e_z⟩| ≤ KOLLINEAR_EPS.
     *
     * Sinus-Test gegen e_z-Parallelität; KOLLINEAR_EPS ist
     * bevorzugt für Lot- und Parallelitäts-Prädikate
     * (siehe hauptglossar/HG_KONVENTIONEN.md Sektion 4).
     */
    fun istHorizontal(eps: Double = Toleranzen.KOLLINEAR_EPS): Boolean =
        abs(richtung.z) <= eps

    /**
     * Rechtwinkligkeitsprädikat zur Sparrenachse:
     * |⟨d_hat, d_hat_S⟩| ≤ KOLLINEAR_EPS.
     */
    fun stehtRechtwinkligZuSparren(
        sparren: Sparren,
        eps: Double = Toleranzen.KOLLINEAR_EPS
    ): Boolean = abs(richtung.dot(sparren.richtung)) <= eps
}

sealed class LatteEntartet {
    object Nullachse                  : LatteEntartet()
    object NichtParallelZurDachflaeche: LatteEntartet()
    object NichtHorizontal            : LatteEntartet()
    object NichtOrthogonalZumSparren  : LatteEntartet()
    object AusserStandardquerschnitt  : LatteEntartet()  // Warnung
    object FlacheDachflaeche          : LatteEntartet()  // α = 0
}
```

- **Einheit**: Längen in mm (Double), Winkel intern in Radiant.
- **Identität**: `BauteilId` aus dem zugrunde liegenden Bauteil.
- **Invarianten** (in der Factory `latteAusBauteil(...)` prüfen,
  bei Verletzung `Resultat.Fehler` mit `LatteEntartet`-Variante;
  niemals Exception):
  1. Stabgeometrie und Bauteilachse vom Typ `Bauteilachse.Gerade`.
  2. Achsenlänge > Toleranzen.LAENGE_EPS — sonst `Nullachse`.
  3. |⟨n_a, d_hat⟩| ≤ Toleranzen.KOLLINEAR_EPS — sonst
     `NichtParallelZurDachflaeche` (Sinus-Test gegen Normalen-
     Parallelität).
  4. |⟨d_hat, e_z⟩| ≤ Toleranzen.KOLLINEAR_EPS — sonst
     `NichtHorizontal` (Sinus-Test gegen e_z-Parallelität).
  5. |⟨d_hat, d_hat_S⟩| ≤ Toleranzen.KOLLINEAR_EPS für mindestens einen
     Sparren S der Dachfläche — sonst `NichtOrthogonalZumSparren`.
  6. Dachfläche geneigt (α > 0) — sonst `FlacheDachflaeche`
     (Sparrenrichtung undefiniert).
  7. **Optional/Warnung**: Querschnitt ∈ { 24/48, 30/50, 40/60 mm }
     — sonst `AusserStandardquerschnitt` als Hinweis, nicht
     als harter Fehler.
- **Edge Cases**:
  - **Pultlatte am Pultdach**: die zugeordnete Dachfläche besitzt
    nur eine einzige Sparrenrichtung (entlang der Falllinie der
    einzigen Dachfläche); Bedingung 4 wird gegen diese
    Sparrenrichtung geprüft. Definition unverändert anwendbar.
  - **Sehr flache Dachfläche** (α → 0): Falllinie und damit
    Sparrenrichtung werden entartet; in diesem Fall ist die
    Latten-Modellierung nicht anwendbar (Flachdach hat keine
    Lattung; siehe `dachaufbau` Edge Case Flachdach mit
    Funktionsklasse `ABDICHTUNG`).
  - **Latte am Walm / am Grat**: Latten enden an Grat- bzw.
    Kehlsparren auf Gehrung. Die geometrische Latten-Definition
    bleibt anwendbar; die Endpunkte p_a, p_e liegen auf der
    Schnittlinie der parallel-versetzten Ebene E' mit der
    benachbarten parallel-versetzten Ebene E''.
  - **Geschiftete Latte** (Latte zwischen Schiftsparren auf einer
    Walmfläche): geometrisch identisch zur Standardlatte, nur
    kürzer.
  - **Ausser-Standard-Querschnitt** (z. B. 50/30 mm hochkant
    statt liegend): Bedingung 7 schlägt mit Warnung an; die
    Latten-Definition bleibt geometrisch erfüllt.
- **Abgeleitete Eigenschaften** (als Funktionen):
  - `getrageneSparrenIn(t: Tragwerk): List<Sparren>` — Sparren in
    `t`, deren Bauteilachse die Lattenbauteilachse innerhalb
    Toleranzen schneidet (Bemessungs-Hilfsfunktion).
  - `lattenabstandZuNachbar(l: Latte): Double?` — Achsabstand zur
    Nachbarlatte entlang d_hat_S, falls beide auf derselben
    Dachfläche und parallel.
  - `faserneigung(): Double?` — falls Faserrichtung gesetzt:
    Winkel zwischen Faserrichtung und Lattenachse; sonst null.
- **Bezeichner-Konvention** (CLAUDE.md): Klasse heißt `Latte`
  (deutsch, Glossarbegriff). Spezialisierungen sind nicht
  vorgesehen; „Traglatte" und „Dachlatte" sind Synonyme, keine
  Subtypen.

## Quellen

**Primär (normativ):**

- SIA 232/1:2020, „Geneigte Dächer", Schweizerischer Ingenieur-
  und Architektenverein, Zürich.
- SIA 265:2021, „Holzbau", Schweizerischer Ingenieur- und
  Architektenverein, Zürich.
- SIA 265/2:2023, „Sortierung von Holz nach der Tragfähigkeit —
  Nadelschnittholz gemäss DIN 4074-1", Schweizerischer Ingenieur-
  und Architektenverein, Zürich.
- DIN EN 1995-1-1:2010-12, „Eurocode 5: Bemessung und Konstruktion
  von Holzbauten – Teil 1-1".
- DIN EN 14081-1:2019-10, „Holzbauwerke — Nach Festigkeit
  sortiertes Bauholz mit rechteckigem Querschnitt — Teil 1:
  Allgemeine Anforderungen".
- DIN 4074-1, „Sortierung von Holz nach der Tragfähigkeit —
  Teil 1: Nadelschnittholz".
- DIN 4070-1:1958-01, „Nadelholz; Querschnittsmaße und statische
  Werte für Schnittholz, Vorratskantholz und Dachlatten".

**Sekundär:**

- Lignum (Hrsg.): *Lignatec — Geneigte Dächer in Holzbauweise.*
  Lignum, Zürich, aktuelle Auflage.
- Lignum (Hrsg.): *Holzbautabellen HBT.* Lignum, Zürich, aktuelle
  Auflage.
- Mönck, W.; Rug, W.: *Holzbau – Bemessung und Konstruktion.*
  16. Auflage, Beuth, Berlin 2015.
- Natterer, J.; Herzog, T.; Volz, M.: *Holzbau-Atlas.* 4. Auflage,
  Birkhäuser, Basel 2003.
- Gerner, M.: *Fachwerk – Instandsetzung, Sanierung, Neubau.*
  DVA, 7. Auflage 2007.

**Korpus (nicht autoritativ):**

- Holzbau Deutschland, Merkblatt „Begriffe und Klassifizierungen
  für den Holzbau" (abgerufen 2026-05-14).
- Wikipedia, Lemma „Dachlatte" und „Konterlattung" (abgerufen
  2026-05-14).
- DWDS, Duden, Lemma „Dachlatte".
- Adelung 1793, Lemma „Ziegellatte" (sprachhistorischer Beleg).
