---
id: haengesaeule
benennung: Hängesäule
kurz: "Eine Hängesäule ist ein senkrechtes Holz im Dachgerüst, das nicht von unten stützt, sondern einen darunterliegenden langen Balken in seiner Mitte von oben aufhängt, damit dieser nicht durchhängt."
synonyme: [Hängepfosten, Königsstiel, "king post", "queen post"]
abgelehnte_benennungen: [Säule, Stütze, Pfosten, Stiel, Hängestiel, "tie rod", Zugstab, "tension rod"]
oberbegriff: bauteil
begriffstyp: bauteilrolle
voraussetzungen: [bauteil, bauteilachse, strecke, einheitsvektor, weltkoordinatensystem, toleranzen]
abgrenzung_zu: [stuetze, saeule, stuhlsaeule, staender, sparren, bundbalken, strebe, kopfband, spannriegel, haengewerk, sprengwerk, dachtragwerk, dachstuhl, verbindungsmittel, verstaerkungselement, bauteil]
status: entwurf
subglossar_pendant: notwendig
quellen_primär:
  - "SIA 265:2021 'Holzbau', Schweizerischer Ingenieur- und Architektenverein, §1.1 Fachausdrücke [via: Lignum-Pressemitteilung 2021 'Anwendungshilfen für neue SIA-Norm Holzbau liegen vor']: Hängewerk-Konstruktionen und Hängesäule als Sonderform des Holzbau-Tragwerks; Volltext nicht direkt eingesehen."
  - "DIN EN 1995-1-1:2010-12 (Eurocode 5), Abschnitt 5 (Tragwerksberechnung): zugbeanspruchte Holzbauteile vorausgesetzt; Hängesäule nicht eigenständig lemmatisiert."
quellen_sekundär:
  - "Lignum (Hrsg.): Pressemitteilung 2021 'Anwendungshilfen für neue SIA-Norm Holzbau liegen vor', lignum.ch/auf_einen_klick/news/."
  - "Lignum (Hrsg.): Holzbautabellen HBT 1 (2024). Lignum, Zürich. Begriffsregister 'Hängesäule' (Volltext nicht zugänglich, Verlags-Schaufenster)."
  - "Mönck, W.; Rug, W.: Holzbau – Bemessung und Konstruktion. 16. Aufl., Beuth, Berlin 2015, Kap. 'Hängewerk und Sprengwerk'."
  - "Natterer, J.; Herzog, T.; Volz, M.: Holzbau-Atlas. 4. Aufl., Birkhäuser, Basel 2003, Kap. 'Hängewerk-Tragwerke'."
  - "Gerner, M.: Fachwerk – Instandsetzung, Sanierung, Neubau. DVA, 7. Aufl. 2007, Glossar 'Hängesäule', 'Hängewerk'."
  - "Wikipedia, Lemma 'Hängewerk' (de.wikipedia.org/wiki/H%C3%A4ngewerk): 'Die von oben getragenen Lasten werden über die Hängepfosten (Zugkraft), über die Streben (Druckkraft) in den Bundbalken (Zugkraft) und in die Auflager übertragen.' Einfaches Hängewerk (Bundbalken + 2 Streben + 1 Hängesäule), doppeltes Hängewerk (+ 1 zweite Hängesäule + 1 Spannriegel). Moderne Hallenkonstruktion ersetzt die hölzerne Hängesäule oft durch Stahl-Zugstäbe."
  - "Wikipedia, Lemma 'Hängesäule' (de.wikipedia.org/wiki/H%C3%A4nges%C3%A4ule): Hängepfosten als Synonym, drei Verwendungs-Kontexte (Dachtragwerk, Treppe, Bahn-Oberleitung)."
  - "Wikipedia, Lemma 'King post truss' (en.wikipedia.org/wiki/King_post) — englisches Pendant für einfaches Hängewerk."
  - "NIhK Glossary of Prehistoric and Historic Timber Buildings, Lemmata 'king post truss', 'queen post truss' — historische Hängewerk-Konstruktionen."
  - "Fraunhofer IBP: 'Konstruktion und Funktion einer Hängesäule', denkmalpflege.fraunhofer.de — Restaurierungs-Kontext (nicht direkt eingesehen)."
  - "Recherche-Bericht: [intern] §F."
quellenkonflikt: |
  Fünf Punkte sind in der Recherche
  ([intern] §F)
  auflösungs-bedürftig und werden hier ausdrücklich festgelegt.

  **(1) Zug-Element-Charakter — fundamentaler Unterschied zu
  Stütze und Stuhlsäule.** Die Hängesäule ist im Hängewerk
  konstitutiv **Zug-Element**: sie hängt den Bundbalken-Mittel-
  punkt nach oben an den Schnittpunkt der beiden druck-
  beanspruchten Streben (Wikipedia/Hängewerk direkt: „Die von
  oben getragenen Lasten werden über die Hängepfosten (Zugkraft),
  über die Streben (Druckkraft) in den Bundbalken (Zugkraft) und
  in die Auflager übertragen"). Damit unterscheidet sich die
  Hängesäule fundamental von Stütze (`hg_stuetze.md`) und
  Stuhlsäule (`hg_stuhlsaeule.md`), die beide **Druck-Elemente**
  sind.

  Eigene Festlegung: Der Zug-Element-Charakter ist
  **konstitutiver Bestandteil** der Bauteilrolle Hängesäule. Eine
  Hängesäule, die im Lastfall Druck trüge (etwa durch Sog oder
  unsymmetrische Lasten), wäre konzeptuell keine Hängesäule mehr,
  sondern eine umgekehrte Stütze. Die Bauteilrolle wird über die
  **topologische Einbindung** in das Hängewerk ausgezeichnet
  (Bundbalken-Anker am unteren Endpunkt, Strebe-Schnittpunkt-Anker
  am oberen Endpunkt), nicht über die geometrische Stab-Form
  allein (die geometrisch identisch zu einer schlanken Stütze
  ist).

  Geometrisch ist die Hängesäule typischerweise lotrecht, kann
  aber auch leicht geneigt sein (z. B. im doppelten Hängewerk
  mit Spannriegel zwischen den beiden Hängesäulen).

  **(2) Einfaches vs. doppeltes Hängewerk.** Wikipedia/Hängewerk
  (direkt eingesehen) trennt zwei Hauptvarianten:

  - **Einfaches Hängewerk** (king post): Bundbalken (horizontal,
    Zug) + 2 Streben (schräg, Druck) + 1 **Hängesäule** (lotrecht,
    Zug). Die Hängesäule hängt den Bundbalken-Mittelpunkt an den
    Streben-Schnittpunkt oben am First. Standard-Konstruktion für
    mittlere Spannweiten in historischen Kirchen, Mühlen,
    Bauernhäusern.
  - **Doppeltes Hängewerk** (queen post): zwei Hängesäulen an
    den Drittelpunkten des Bundbalkens, verbunden durch einen
    **Spannriegel** oben. Standard-Konstruktion für grössere
    Spannweiten.

  Im englischen Sprachgebrauch sind „king post" und „queen post"
  als feste Termini für die jeweiligen Hängesäulen-Konfigurationen
  etabliert; im deutschen DACH-Korpus heißen beide einfach
  „Hängesäule" (im einfachen oder doppelten Hängewerk).

  Eigene Festlegung: Die Definition deckt **beide Varianten** ab.
  Die Diskriminierung erfolgt über die Anzahl der Hängesäulen
  im Hängewerk-Aggregat (`hg_haengewerk.md`, Folgearbeit-
  Trigger), nicht über die Bauteilrolle selbst. Sub-
  Spezialisierungen `einfache_haengesaeule` und
  `doppelte_haengesaeule` sind nicht vorgesehen — die
  Konfigurations-Information lebt im Hängewerk-Aggregat.

  **(3) Werkstoff-Drift Holz ↔ Stahl-Zugstab im modernen
  Hallenbau.** Wikipedia/Hängewerk direkt: „Modern construction
  often substitutes steel tension elements for traditional wooden
  hanging posts." Im modernen BSH-Hallenbau (Pollmeier-/
  Hasslacher-/binderholz-Linie) sind die Mittel-Zug-Elemente in
  einem Hängewerk-Binder oft **Stahl-Zugstäbe** (Macalloy-
  Zugstangen, Spannschlösser, Stahlseile). Die konstruktive
  Funktion ist identisch zur historischen Holz-Hängesäule, der
  Werkstoff wechselt.

  Diese Werkstoff-Drift wirft eine **Element-Ontologie-Frage** auf: Wechselt mit dem
  Werkstoff das Element-Subtyp von `bauteil` zu `verbindungs-
  mittel` oder `verstaerkungselement`?

  **Eigene Festlegung — drei Fallunterscheidungen:**

  - **Fall A (konstitutives Hängewerk-Bauteil)**: Wenn der
    Stahl-Zugstab das **Haupt-Zug-Element** des Hängewerks ist
    (er trägt die Mittel-Last des Bundbalkens), bleibt er
    **Bauteil** in der Element-Ontologie. Die Bauteilrolle
    „Hängesäule" deckt beide Werkstoff-Varianten ab (Holz und
    Stahl); Werkstoff wird über das `werkstoff`-Merkmal des
    Bauteils geführt. **Empfehlung der App** für die häufige
    Hallenbau-Modellierung.

  - **Fall B (Zusatz-Verbinder zu einer hölzernen Hängesäule)**:
    Wenn der Stahl-Zugstab nur als **Stahl-Anschluss** in oder an
    eine hölzerne Hängesäule wirkt (z. B. Macalloy-Stange durch
    eine BSH-Hängesäule zur Querschnitts-Verstärkung), bleibt er
    **verbindungsmittel** (`hg_verbindungsmittel.md`, Welle 12).

  - **Fall C (Sanierungs-Verstärkung historischer Holz-
    Hängesäule)**: Wenn der Stahl-Zugstab eine **geschwächte
    historische Holz-Hängesäule nachträglich verstärkt**
    (parallele Zug-Stange neben der originalen Hängesäule), ist
    er **verstaerkungselement** (`hg_verstaerkungselement.md`,
    Welle 12).

  Die Klärung pro konkretem Konstruktions-Detail ist im aktuellen
  Glossarstand **dokumentiert als Folgearbeit-Trigger**, nicht
  formal umgesetzt. Die App führt im aktuellen Stand keinen
  Hallenbau-spezifischen Modellierungs-Code; die Fallunterscheidung
  wird bei der ersten Hallenbinder-Modellierung als ABW-Welle
  aufgelöst.

  **(4) Hängewerk-Aggregat-Folgearbeit.** Die Hängesäule ist
  konstitutiv Mitglied eines **Hängewerk-Aggregats** (Wikipedia/
  Hängewerk). Das Aggregat ist im aktuellen Glossarstand **nicht
  angelegt** — `hg_haengewerk.md` wäre analog zu `hg_walm.md`,
  `hg_binder.md`, `hg_dachstuhl.md` (Welle 12) zu strukturieren:
  Bauteilgruppe aus Bundbalken + 2 Streben + 1 (oder 2)
  Hängesäule(n) + ggf. Spannriegel, mit `oberbegriff: tragwerk`
  oder `bauteilgruppe`.

  Eigene Festlegung: `hg_haengewerk.md` ist als Folgearbeit-
  Trigger dokumentiert. Bei Anlage wird die Hängesäule als
  Mitglied einer Hängewerk-Bauteilgruppe geführt; im aktuellen
  Glossarstand bleibt der Hängewerk-Bezug Forward-Verweis.

  **(5) CH-Sanierungs-Kontext-Aktivität (historische CH-Brücken
  und Bauernhäuser).** Im modernen CH-Hochbau ist die Hängesäule
  weniger zentral als die Stuhlsäule (Welle-13 §G.1). Sie ist
  aber im **Sanierungs- und Restaurierungs-Kontext** aktiv:

  - **Historische CH-Brücken** mit Hängewerk-Tragwerken
    (z. B. überdachte Holzbrücken im Berner Oberland, in
    Graubünden, im Tessin; Punt da Suransuns ist Stahl, nicht
    Hängewerk — aber andere Brücken).
  - **Kirchen-Dachtragwerke** mit historischen Hängewerken
    (vgl. CH-Denkmalpflege).
  - **Mühlenbauten und alte Bauernhäuser** mit Hängewerk-
    Dachstühlen.

  Diese Konstruktionen sind im aktuellen App-Plan nicht zentraler
  Modellierungs-Gegenstand (das erste Tool ist Sparrenkerven-
  Werkzeug, kein Sanierungs-Tool); die Hängesäule ist aber als
  CH-Sanierungs-relevanter Begriff im Glossar geführt.

  Eigene Festlegung: Der CH-Sanierungs-Kontext wird in der
  Erläuterung dokumentiert. Eine Folgearbeit `hg_haengewerk.md`
  bei einer Sanierungs- oder Brücken-Tool-Welle aktiviert die
  Hängesäule als zentrales Aggregat-Mitglied.
---

## Prosa-Definition

Eine **Hängesäule** ist eine holz-spezifische Bauteilrolle im
Hängewerk-Dachtragwerk (oder Hängewerk-Deckentragwerk), deren
Bauteilachse lotrecht oder annähernd lotrecht verläuft, deren
oberer Endpunkt am Streben-Schnittpunkt des Hängewerks befestigt
ist und deren unterer Endpunkt den Bundbalken-Mittelpunkt (oder
den Drittelpunkt im doppelten Hängewerk) nach oben „aufhängt",
wobei sie als **Zug-Element** die nach unten wirkenden Lasten des
Bundbalkens über ihre Bauteilachse in die Streben-Schnittpunkte
weiterleitet, von wo aus die Streben sie als Druck-Element in die
Auflager am Bundbalken-Ende abtragen.

## Mathematische Definition

Sei

- B ein Bauteil im Sinne von `bauteil` mit Stabgeometrie
  (`geometrie ∈ 𝒢_stab`),
- a(B) = Bauteilachse.Gerade(p_a, p_e) die Bauteilachse von B mit
  d_hat:= (p_e − p_a) / ‖p_e − p_a‖ ∈ S² ⊂ ℝ³,
- BK ein Bundbalken (horizontales Zug-Element des Hängewerks) mit
  Bauteilachse a(BK) und Mittelpunkt m_BK = (p_a^BK + p_e^BK) / 2,
- S₁, S₂ zwei Streben (schräge Druck-Elemente des Hängewerks) mit
  Bauteilachsen a(S₁), a(S₂), die sich im Punkt s = a(S₁) ∩ a(S₂)
  schneiden,
- e_z:= (0, 0, 1)ᵀ die vertikale Welt-Achse,
- ε_K:= Toleranzen.KOLLINEAR_EPS,
- ε_L:= Toleranzen.LAENGE_EPS.

Dann heißt B eine **Hängesäule** des Hängewerks mit Bundbalken BK
und Streben S₁, S₂ genau dann, wenn die folgenden Bedingungen alle
erfüllt sind:

1. **Stabgeometrie**: B besitzt eine gerade Bauteilachse mit
   ‖p_e − p_a‖ > ε_L.

2. **Aufstrebende Bauteilachse**: Der untere Endpunkt p_a liegt
   höhenmäßig unterhalb des oberen Endpunktes p_e,
   ```
   p_a.z + ε_L < p_e.z.
   ```
   Im einfachen Hängewerk ist die Hängesäule typisch lotrecht
   (‖d_hat × e_z‖ ≤ ε_K), im doppelten Hängewerk können beide
   Hängesäulen leicht aus dem Lot geneigt sein.

3. **Bundbalken-Anker am unteren Endpunkt**: Der untere Endpunkt
   p_a liegt auf der Bundbalken-Bauteilachse a(BK) bis auf
   Toleranz,
   ```
   dist(p_a, a(BK)) ≤ ε_L.
   ```
   Im einfachen Hängewerk liegt p_a am Bundbalken-Mittelpunkt
   (‖p_a − m_BK‖ ≤ ε_L); im doppelten Hängewerk an einem der
   beiden Drittelpunkte des Bundbalkens.

4. **Streben-Schnittpunkt-Anker am oberen Endpunkt**: Der obere
   Endpunkt p_e liegt am Schnittpunkt der beiden Streben-
   Bauteilachsen,
   ```
   ‖p_e − s‖ ≤ ε_L  mit  s = a(S₁) ∩ a(S₂).
   ```
   Im doppelten Hängewerk ist p_e Endpunkt eines Spannriegels,
   der die beiden Hängesäulen oben verbindet — die Bedingung
   lockert in diesem Fall auf „p_e liegt auf der
   Spannriegel-Bauteilachse".

5. **Zug-Lastpfad-Zusicherung (qualitativ, nicht formal geprüft)**:
   B trägt im Hängewerk-Tragwerk primär **Zuglasten** entlang der
   Bauteilachse — die nach unten wirkende Bundbalken-Mittel-Last
   wird über die Hängesäulen-Achse nach oben in den Streben-
   Schnittpunkt geleitet. Die formale Lastpfad-Verifikation ist
   Aufgabe des `hg_statisches_system`-Eintrags und wird hier
   zugesichert, nicht überprüft.

6. **Holz-Werkstoff als Default (mit dokumentierter Stahl-Drift)**:
   Im klassischen Hängewerk ist B aus Holz (Vollholz, BSH); im
   modernen Hallenbau kann B durch einen Stahl-Zugstab ersetzt sein
   (siehe Quellenkonflikt-Punkt 3). Die Bauteilrolle deckt beide
   Werkstoff-Varianten ab; Werkstoff wird über das `werkstoff`-
   Merkmal geführt.

Wesentliche abgeleitete Größen:

- **Hängesäulen-Länge**: L_HS:= ‖p_e − p_a‖ (in mm).
- **Hängesäulen-Neigung**: α:= acos(⟨d_hat, e_z⟩) (in rad). Im
  einfachen Hängewerk gilt typisch α ≤ ε_W (Lotrechtheit); im
  doppelten Hängewerk α leicht > ε_W.

## Wohldefiniertheit

- **Existenz**: Für jede Hängesäule in einem einfachen oder
  doppelten Hängewerk (Wikipedia/Hängewerk, historische CH-/DE-
  Brücken, Kirchen-Dachtragwerke) sind alle Bedingungen 1–6
  konstruktiv erfüllbar.
- **Eindeutigkeit der Hängesäulen-Orientierung**: Bedingung 2
  fixiert die Achsen-Richtung vom Bundbalken (unten) zum Streben-
  Schnittpunkt (oben).
- **Disjunktheit zur Stütze**: Eine Stütze (`hg_stuetze.md`) ist
  Druck-Element ohne Bundbalken-Anker. Bedingung 5 schließt die
  Stütze aus (Zug-Lastpfad statt Druck-Lastpfad); zusätzlich
  fehlt der Bundbalken-Anker.
- **Disjunktheit zur Stuhlsäule**: Eine Stuhlsäule
  (`hg_stuhlsaeule.md`) ist Druck-Element mit Stuhlpfetten-
  Anschluss am Kopf. Bedingung 5 (Zug) und Bedingung 4 (Streben-
  Schnittpunkt statt Stuhlpfetten-Anschluss) trennen die beiden
  Bauteilrollen.
- **Konsistenz mit `bauteil`**: Alle Bedingungen aus `bauteil`
  sind erfüllt; die Bauteilrolle Hängesäule ergänzt die Lage- und
  Topologie-Constraints 1–6.
- **Geometrische Ähnlichkeit zur schlanken Stütze**: Geometrisch
  unterscheidet sich die Hängesäule nicht von einer schlanken
  Stütze; die Bauteilrolle-Auszeichnung erfolgt über die
  **topologische Einbindung** (Bundbalken-Anker unten, Streben-
  Schnittpunkt-Anker oben) und den **Zug-Lastpfad** (Bedingung 5).
- **Werkstoff-Drift Holz ↔ Stahl**: Bedingung 6 lässt beide
  Werkstoff-Varianten zu, mit dokumentierter Drift im
  Quellenkonflikt-Block. Die Disambiguation zu `verbindungs-
  mittel` und `verstaerkungselement` (Fall A vs. B vs. C in
  Quellenkonflikt-Punkt 3) bleibt Modellierungs-Entscheidung pro
  Konstruktions-Detail.
- **Nicht-Zirkularität**: Die Definition stützt sich nur auf
  bereits definierte Begriffe (`bauteil`, `bauteilachse`,
  `strecke`, `einheitsvektor`, `weltkoordinatensystem`,
  `toleranzen`). Forward-Verweise (`haengewerk`, `bundbalken`,
  `spannriegel`, `sprengwerk`, `dachtragwerk`,
  `statisches_system`) sind nach HG_KONVENTIONEN.md §6 zulässig.

## Erläuterung (nicht normativ)

Die Hängesäule ist im **klassischen Hängewerk-Tragwerk** das
zentrale Zug-Element, das das gesamte konstruktive Prinzip des
Hängewerks ermöglicht: einen großspannigen Bundbalken
**aufzuhängen**, statt ihn nur als Biegeträger zu verwenden. Das
Hängewerk löst damit eines der ältesten Bauprobleme: einen langen
Holzbalken über eine grosse Spannweite zu verlegen, ohne dass er
in der Mitte durchbiegt.

### Konstruktives Prinzip des Hängewerks

Das **einfache Hängewerk** besteht aus vier Holzbauteilen:

- **Bundbalken** (horizontal, Zug): der durchhängungs-gefährdete
  Hauptbalken.
- **2 Streben** (schräg, Druck): vom Bundbalken-Ende nach oben
  zum First-Schnittpunkt.
- **Hängesäule** (lotrecht, Zug): vom Bundbalken-Mittelpunkt nach
  oben zum Streben-Schnittpunkt.

Der Lastpfad geht **vom Bundbalken-Mittelpunkt nach oben** über
die Hängesäule (Zug), dann nach **schräg unten** über die Streben
(Druck) in die Auflager am Bundbalken-Ende. Die nach unten
gerichteten Lasten des Bundbalkens werden also „aufgehängt", was
die effektive Biegelänge des Bundbalkens halbiert. Das gleiche
Prinzip umgekehrt heißt **Sprengwerk** (`hg_sprengwerk.md`,
Folgearbeit) — dort wirkt eine Druck-Stütze nach oben statt einer
Zug-Säule nach unten.

Das **doppelte Hängewerk** erweitert die Konstruktion um eine
zweite Hängesäule und einen Spannriegel: die beiden Hängesäulen
hängen den Bundbalken an den Drittelpunkten auf; der Spannriegel
oben verbindet die beiden Hängesäulen-Köpfe als horizontales
Zug- oder Druck-Element. Dies erlaubt grössere Spannweiten als
das einfache Hängewerk.

### Englische Pendants

Im englischen Sprachgebrauch:

- **King post truss** = einfaches Hängewerk; die Hängesäule heißt
  „king post" oder „crown post".
- **Queen post truss** = doppeltes Hängewerk; die beiden
  Hängesäulen heißen „queen posts".

Diese englischen Termini sind im DACH-Korpus berufssprachlich
bekannt (Wikipedia/Hängesäule, NIhK-Glossar), werden aber **nicht**
als Hauptbenennung verwendet — „Hängesäule" ist das deutsche
Standard-Lemma.

### Werkstoff-Drift Holz ↔ Stahl im modernen Hallenbau

Im modernen **BSH-Hallenbau** und im **CLT-Anschluss-Tragwerk**
(Pollmeier, Hasslacher, binderholz) wird die hölzerne Hängesäule
oft durch **Stahl-Zugstäbe** ersetzt — Macalloy-Zugstangen,
Spannschlösser, gelegentlich Stahlseile. Konstruktiv ist die
Funktion identisch (Mittel-Zug-Element des Hängewerk-Tragwerks),
der Werkstoff wechselt. Die App-Modellierung führt für die
moderne Stahl-Variante denselben Bauteilrollen-Typ („Hängesäule")
mit `werkstoff = Stahl`; eine Sub-Spezialisierung
`hg_stahl_zugstab.md` ist Folgearbeit (siehe Quellenkonflikt-
Punkt 3).

Die Ausnahmen — wenn der Stahl-Zugstab als Verbindungsmittel zu
einer Holz-Hängesäule oder als nachträgliches Verstärkungselement
verbaut ist — sind im Quellenkonflikt-Block dokumentiert (Fall B
und C).

### CH-Aktivität: Sanierungs- und Restaurierungs-Kontext

In der **modernen CH-Hochbau-Praxis** ist die Hängesäule weniger
zentral als die Stuhlsäule (`hg_stuhlsaeule.md`). Sie tritt
aktiv auf in:

- **Sanierung historischer CH-Brücken**: viele überdachte
  Holzbrücken in der Schweiz (Berner Oberland, Graubünden,
  Tessin) tragen Hängewerk-Konstruktionen. Restaurierungs-
  Projekte aktivieren das Lemma.
- **Sanierung historischer Kirchen-Dachtragwerke**: viele
  Kirchen-Dachstühle in der CH verwenden Hängewerke. Denkmal-
  pflege-Projekte aktivieren das Lemma.
- **Sanierung alter Mühlenbauten und Bauernhäuser**.

Im **modernen Neubau** ist die hölzerne Hängesäule selten (durch
Beplankungs- oder Stahl-Aussteifung verdrängt); die Stahl-
Zugstab-Variante kommt im Hallenbau-Tragwerk vor.

### Hängewerk-Bauteil-Familie

Die Hängesäule ist Teil einer engen Bauteil-Familie (Wikipedia/
Hängewerk):

| Bauteil | Funktion |
|---|---|
| **Hängesäule** | tragendes Zug-Element zur Bundbalken-Aufhängung |
| **Bundbalken** | horizontaler Hauptbalken (Zug, da am Mittelpunkt aufgehängt) |
| **Strebe** | schräges Druck-Element vom Bundbalken-Ende zum Streben-Schnittpunkt |
| **Spannriegel** | beim doppelten Hängewerk: horizontales Element zwischen den beiden Hängesäulen-Köpfen |
| **Hängewerk** | Bauteilgruppe / Tragwerk aus den oben genannten Bauteilen |

Das **Hängewerk** als Aggregat (`hg_haengewerk.md`) ist
Folgearbeit-Trigger.

### Hängesäule vs. Sprengsäule

Das **Sprengwerk** (`hg_sprengwerk.md`, Folgearbeit) ist das
**inverse** Hängewerk: statt einer Zug-Hängesäule, die das
Hauptelement (Bundbalken) nach oben hängt, wirkt eine Druck-
**Sprengsäule** (oder Strebe) von unten nach oben gegen das
Hauptelement (typisch eine Deckenbalken-Verstärkung von unten
durch eine Stütze). Hängesäule (Zug) und Sprengsäule (Druck)
sind funktional invers.

### Andere Bedeutungen / Englisch

- **`king post`** / **`crown post`** / **`queen post`**: siehe
  oben.
- **`tie rod`** / **`tension rod`**: Stahl-Variante im modernen
  Hallenbau. Im Holzbau false friend (Stahl-Bauteil, nicht
  Holz-Hängesäule).
- **`hanger`** / **`hanging post`**: englische deskriptive
  Übersetzung der deutschen Hängesäule.

## Beziehungen

- **Oberbegriff**: `bauteil`. Strukturell ist die Hängesäule ein
  Bauteil mit der zusätzlichen Rolle „Hängesäule" und den oben
  formalisierten geometrischen und topologischen Constraints.
  Geschwister-Rolle zu `stuetze`, `stuhlsaeule`, `staender`,
  `sparren`, `pfette`.
- **Bestandteile (partitiv, vom Bauteil geerbt)**:
  - **Bauteilachse** (`bauteilachse.Gerade`), aufstrebend
    (Bedingung 2);
  - **Querschnitt** (rechteckig, im historischen Holz-Hängewerk
    typisch 140–200 mm Kantenmaß; im modernen Stahl-Hängewerk
    Rundstab oder Profilstab);
  - **Werkstoff** (Vollholz, BSH oder Stahl);
  - **Faserrichtung** (bei Holz axial entlang der Bauteilachse).
- **Topologische Inzidenz**:
  - **Bundbalken** (`bundbalken`, Forward-Verweis):
    Auflager-/Anker-Anschluss am unteren Endpunkt (Bedingung 3).
  - **Strebe** (`strebe`, Welle 10): zwei Streben treffen sich am
    oberen Endpunkt der Hängesäule (Bedingung 4).
  - **Spannriegel** (`spannriegel`, Forward-Verweis): beim
    doppelten Hängewerk Querholz zwischen den beiden Hängesäulen-
    Köpfen.
- **Verwendung**:
  - Mitglied eines **Hängewerks** (`haengewerk`, Folgearbeit-
    Trigger). Konstitutiv für das Hängewerk-Aggregat.
  - Mitglied eines **Dachtragwerks** (`dachtragwerk`,
    Forward-Verweis Welle 12) oder eines **Dachstuhls**
    (`dachstuhl`, Welle 12), wenn das Hängewerk Teil eines
    Dachtragwerks ist.
  - Mitglied eines **Deckentragwerks** (z. B. historische
    Holzbrücken-Decken-Tragwerke mit Hängewerk).
- **Abgrenzung**:
  - **Stütze** (`stuetze`, Welle 13): werkstoffneutrale Tragwerks-
    Bauteilrolle mit Druck-Lastpfad. Geschwister-Rolle der
    Hängesäule, nicht Oberbegriff. Trennlinie: Druck vs. Zug
    (Lastpfad), allgemeines Tragwerk vs. Hängewerk-Topologie.
  - **Säule** (`saeule`, Welle 13): architektonisch-klassischer
    Stütz-Subtyp mit freistehendem Charakter. Keine Hängesäule
    ist eine Säule — sie ist in das Hängewerk eingebunden
    (Bedingung 3 von `hg_saeule.md` verletzt) und Zug-Element
    statt Druck.
  - **Stuhlsäule** (`stuhlsaeule`, Welle 13): Druck-Element im
    Dachstuhl. Geschwister-Bauteilrolle mit invertiertem
    Lastpfad. Trennlinie über Bedingung 5 (Zug vs. Druck) und
    Bedingung 4 (Streben-Schnittpunkt vs. Stuhlpfetten-Anschluss).
  - **Ständer** (`staender`, Welle 9): Wand-Bauteilrolle.
    Geschwister-Rolle; Trennlinie über die Wand-Inzidenz
    (Schwelle/Rähm) gegen die Hängewerk-Inzidenz (Bundbalken/
    Streben-Schnittpunkt).
  - **Sparren** (`sparren`, Welle 8): geneigtes Dachflächen-
    Bauteil. Nicht im Hängewerk; gehört in die Sparrenebene des
    Dachtragwerks.
  - **Bundbalken** (`bundbalken`, Forward-Verweis): horizontaler
    Hauptbalken des Hängewerks. Konstitutives Auflager-Element
    der Hängesäule.
  - **Strebe** (`strebe`, Welle 10): schräges Druck-Element des
    Hängewerks. Trifft am oberen Endpunkt der Hängesäule.
  - **Kopfband** (`kopfband`, Welle 10): Diagonal-Aussteifung
    Pfosten-Kopf ↔ Längsholz. Im Hängewerk nicht direkter
    Bestandteil; das funktionale Pendant am Hängesäulen-Kopf
    ist die Strebe (die zugleich tragend und aussteifend wirkt).
  - **Spannriegel** (`spannriegel`, Forward-Verweis): Querholz
    im doppelten Hängewerk. Im einfachen Hängewerk nicht
    vorhanden.
  - **Hängewerk** (`haengewerk`, Folgearbeit-Trigger): Aggregat /
    Bauteilgruppe, deren konstitutives Mitglied die Hängesäule
    ist.
  - **Sprengwerk** (`sprengwerk`, Folgearbeit-Trigger): inverses
    Hängewerk. Im Sprengwerk gibt es keine Hängesäule, sondern
    eine Sprengsäule (Druck-Element).
  - **Dachtragwerk** (`dachtragwerk`, Welle-12-Folgearbeit aus
    `hg_dachstuhl.md`): SIA-265-Linie-Oberbegriff. Hängewerk ist
    eine spezielle Dachtragwerks-Variante.
  - **Dachstuhl** (`dachstuhl`, Welle 12): das zimmermannsmäßige
    Dachtragwerk. Klassisches Hängewerk fügt sich in den
    Dachstuhl ein (historische Kirchen-Dachstühle).
  - **Verbindungsmittel** (`verbindungsmittel`, Welle 12): bei
    Werkstoff-Drift Fall B (Stahl-Zugstab als Anschluss in eine
    Holz-Hängesäule); siehe Quellenkonflikt-Punkt 3.
  - **Verstärkungselement** (`verstaerkungselement`, Welle 12):
    bei Werkstoff-Drift Fall C (Stahl-Zugstab als nachträgliche
    Verstärkung einer historischen Holz-Hängesäule).
  - **Bauteil** (`bauteil`): Oberbegriff.

## Quellen

**Primär (normativ):**

- SIA 265:2021, „Holzbau", Schweizerischer Ingenieur- und
  Architektenverein, Zürich, §1.1 Fachausdrücke.
- DIN EN 1995-1-1:2010-12, „Eurocode 5: Bemessung und Konstruktion
  von Holzbauten – Teil 1-1".

**Sekundär:**

- Lignum: *Pressemitteilung 2021 — Anwendungshilfen für neue
  SIA-Norm Holzbau.* lignum.ch/auf_einen_klick/news/.
- Lignum (Hrsg.): *Holzbautabellen HBT 1 (2024).* Lignum, Zürich.
- Mönck, W.; Rug, W.: *Holzbau – Bemessung und Konstruktion.*
  16. Auflage, Beuth, Berlin 2015.
- Natterer, J.; Herzog, T.; Volz, M.: *Holzbau-Atlas.* 4. Auflage,
  Birkhäuser, Basel 2003.
- Gerner, M.: *Fachwerk – Instandsetzung, Sanierung, Neubau.*
  DVA, 7. Auflage 2007.
- NIhK: *Glossary of Prehistoric and Historic Timber Buildings*
  (Lemmata „king post truss", „queen post truss").
- Fraunhofer IBP: „Konstruktion und Funktion einer Hängesäule",
  denkmalpflege.fraunhofer.de.
- Wikipedia, Lemmata „Hängesäule", „Hängewerk", „Sprengwerk",
  „King post", „Queen post" (abgerufen 2026-05-16).
- Recherche-Bericht: [intern] §F.

**Korpus (nicht autoritativ):**

- hausjournal.net „Hängewerke einfach erklärt".
- Zeno.org „Hängewerke" Lueger/Meyers 1904/1905.
- architektur-lexikon.de „Hängewerk".
- DeWiki „Hängesäule".
- Pollmeier/Hasslacher/binderholz BSH-Hersteller — Hallenbau-
  Praxis-Belege für Stahl-Zugstab-Variante.
