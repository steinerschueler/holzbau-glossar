---
id: sg_ebene
benennung: Ebene
glossar_ref: ebene
cluster: ressourcen
subglossar_pendant: notwendig
status: entwurf
---

# Ebene (Subglossar)

Brücke vom normativen Hauptglossar (`hauptglossar/00_ressourcen/hg_ebene.md`) zu
den stufenweisen Theorie-Inhalten. Hier liegt die didaktische
Aufbereitung: die berufssprachliche Verankerung der Ebene über
eine dichte Familie von Rollen-Komposita, die Pflicht-Skizze des
Walmdachs mit drei Dachebenen und ihren Schnittgeraden als Grat
und First, Werkzeug-Bezug am Bauplatz und am Bauteil, sowie die
Negativ-Abgrenzung zu Fläche, Polygon, Dachfläche und Schicht —
einschließlich des sprachlichen Stolpersteins „Installations-
ebene", in dessen Namen „Ebene" steht, deren Sache aber eine
Schicht mit Dicke ist.

---

## Was die Ebene im Holzbau ist

Eine **Ebene** ist eine beidseitig unbegrenzte, nirgends gekrümmte
zweidimensionale Punktmenge im Raum — die gedachte zweiseitige
Fortsetzung jeder ebenen Fläche ohne Rand und Material. Im
DACH-Holzbau-Korpus tritt sie fast nie als nacktes Substantiv auf;
der Zimmermann redet nicht von „der Ebene", sondern von
**Dachebene**, **Wandebene**, **Bodenebene**, **Bezugsebene**,
**Auflagerebene**, **Mittelebene**, **Symmetrieebene**,
**Schalungsebene**, **Horizontalebene** und **Lotebene** — eine
ganze Familie von Rollen-Komposita, in denen das Ebenen-Konzept
stillschweigend mitläuft. Wie schon beim Punkt und bei der Geraden
lebt die Ebene im Holzbau **als Ebene von etwas**.

Das Wort selbst ist eine **Substantivierung** des Adjektivs
„eben". Althochdeutsch *ebanī* (8. Jahrhundert) bedeutet „Glätte,
Gleichheit, das Flachsein" und ist abgeleitet von *eban* „glatt,
flach, gleich". Die **mathematische Lesart** „unbegrenzte,
nirgends gekrümmte Fläche" tritt im Deutschen erst ab dem
16. Jahrhundert auf, als Übersetzung des mittellateinischen
*planum*. Der Bedeutungsstrang „flach" lebt in „eine ebene
Fläche", „ebenes Holz", „ebene Schalung"; der Bedeutungsstrang
„gleich" überlebt in „ebenbürtig". Die Substantivierung „eine
ebene Fläche" → „eine Ebene" folgt derselben Sprach-Mechanik wie
„eine gerade Linie" → „eine Gerade" (siehe `sg_gerade.md`), ist
aber rund zwei Jahrhunderte älter.

## Drei Dachebenen am Walmdach — Pflicht-Skizze

Die zentrale Ebenen-Anwendung im Holzbau ist das Dach. Ein
Walmdach besteht aus mehreren geneigten Dachebenen, die sich
paarweise in Geraden schneiden: zwei gegenüberliegende
Dachebenen treffen sich am **First**, zwei benachbarte am
**Grat**. Die Skizze knüpft direkt an `sg_gerade.md` F.2 an —
dort wurde die Schnittgerade zweier Dachflächen am Walmgrat
gezeigt; hier werden die **schneidenden Ebenen selbst** sichtbar
gemacht, mit allen drei beteiligten Dachebenen und beiden
Schnittgeraden (Grat und First).

<svg viewBox="0 0 720 480" xmlns="http://www.w3.org/2000/svg" font-family="sans-serif" font-size="13">
  <rect width="100%" height="100%" fill="#f4f1ea"/>
  <!--
  ====================================================================
  SVG-DOKUMENTATION: sg_ebene G.1 — Walmdach mit drei Dachebenen,
  Schnittgeraden als Grat und First (Pflicht-Skizze)
  ====================================================================
  (XML-Kommentar innerhalb des SVG-Tags; im Preview unsichtbar.
  KEINE Leerzeilen innerhalb des <svg>-Blocks erlaubt, sonst bricht
  der Markdown-Parser den SVG-Block ab — Erfahrung aus sg_punkt /
  sg_strecke / sg_gerade.)
  ZWECK
    Walmdach im axonometrischen Schraegriss (Tiefenwirkung, keine
    geometrisch korrekte 3D-Projektion). Drei Dachebenen sichtbar:
      (1) Hauptdachflaeche links (Trapez, helle Fuellung)
      (2) Walmflaeche vorn (Dreieck, mittlere Fuellung — Tiefen-
          kontrast zur Hauptdachflaeche)
      (3) Hauptdachflaeche rechts (Trapez, helle Fuellung wie 1)
    Zwei Schnittgeraden hervorgehoben:
      Vorderer Walmgrat (Schnitt Hauptdach-links x Walmflaeche)
      First (Schnitt Hauptdach-links x Hauptdach-rechts)
    Beide als rote durchgezogene Strecken am Bauteil, beidseitig
    durch gepunktete Geraden-Verlaengerungen fortgesetzt — die
    Ebenen-Begruendung der Geraden wird sichtbar.
    (Der hintere Walmgrat und die Rueckseite des Daches werden in
    der gewaehlten Ansicht nicht gezeigt, um die Skizze nicht zu
    ueberfrachten; die Logik ist dieselbe.)
    Drei markante Punkte:
      P_T = vordere Trauf-Walmecke (Grundriss-Ecke des Hauptdachs)
      P_F = First-Walmecke (Hochpunkt am gemeinsamen First-Ende)
      P_R = rechte First-Ecke (Hauptdach-rechts-Ende des Firstes)
    Welt-Pfeile e_h horizontal, e_v vertikal — die Lage der
    Schraegriss-Welt orientieren.
  STIL-KONVENTIONEN (Pilot sg_punkt / sg_gerade)
    Farben:
      #e8c98a Hauptdachflaeche links + rechts (helle Dachhaut)
      #c89a5a Walmflaeche vorn (Tiefenkontrast, dunkler)
      #6a4c2a Dachumriss
      #c0392b Schnittgeraden (Grat + First) — durchgezogen
              stroke-width 3.5
      #c0392b Geraden-Verlaengerung — dasharray 3 5, stroke-width 2
      #2c3e50 Punktmarkierungen, Welt-Pfeile
      #c0392b Punkt-Beschriftung bold
      #666    Rolle-Beschriftung italic 11
    Punkt-Markierung (Standard): circle r=4, fill #c0392b,
                                 stroke #2c3e50
  GEOMETRIE — axonometrische Andeutung (Schraegriss)
    Grundriss-Rechteck Hauptdach (vereinfacht):
      Linke Trauflinie:  (40, 380)   — vordere Ecke unten links
      Vordere Walm-Ecke: (260, 380)  — Hauptdach trifft Walm vorn
      Rechte Walm-Ecke:  (260+200,360)=(460,360) — Tiefe in den
                                                   Schraegriss
                                                   hinein
      Hintere linke Ecke: (40+200,360)=(240,360) — Tiefe analog
    First-Ebene (oberste Schnittlinie) auf y=170:
      Vorderes First-Ende:   (170, 170) — von Hauptdach-links-Walm
      Hinteres First-Ende:   (370, 170) — entspricht Tiefe
                                          (Versatz 200 in x, -10 in y
                                          analog zum Grundriss)
      Wird gesetzt durch: Mittelpunkt zwischen (40,380) und (260,380)
        in der Tiefe gehoben — fuer den Schraegriss vereinfacht.
    Dachebenen-Polygone:
      (1) Hauptdach-links (Trapez): (40,380) (260,380) (370,170) (170,170)
          NOTE: Polygon enthaelt linke Trauflinie unten + First oben
          + zwei schraege Seitenkanten (linke Hauptdach-Kante und
          vorderer Walmgrat).
      (2) Walmflaeche vorn (Dreieck): (260,380) (460,360) (370,170)
          Drei Kanten: vordere Walm-Trauflinie schraeg in die Tiefe,
          hinterer Walm-Kante (= Schnitt mit Hauptdach-rechts),
          vorderer Walmgrat.
      (3) Hauptdach-rechts (Trapez): (240,360) (460,360) (370,170) ... 
          Achtung: Skizze zeigt nur Walmflaeche + Hauptdach-links als
          vordere Flaechen prominent. Die Hauptdach-rechts-Flaeche
          ist hinter dem First / Walm und nur durch Andeutung
          (First-Strecke + hintere Kante) sichtbar.
    Vereinfachung: Hauptdach-rechts wird als FLACHE PARTITION hinter
    dem First gezeichnet (Trapez mit hinterer Trauflinie y=360,
    geht hinter Walmflaeche / Firstebene zurueck).
    Drei beschriftete Punkte:
      P_T = (260, 380) vordere Trauf-Walmecke
      P_F = (370, 170) First-Walmecke (Schnittpunkt der zwei
                                       Schnittgeraden)
      P_R = (170, 170) linke First-Ecke (Hauptdach-links-Walm-Ende
                                         des Firstes — Knick zur
                                         hinteren Dachseite)
    Schnittgerade vorderer Walmgrat:
      Endpunkte: G_T = (260, 380) und P_F = (370, 170)
      Richtung: dx=110, dy=-210, Laenge=237.5, Unit=(0.463, -0.884)
      Verlaengerung 60 px ueber jede Seite:
        unten: (260-60*0.463, 380+60*0.884) = (232.2, 433.1)
        oben:  (370+60*0.463, 170-60*0.884) = (397.8, 116.9)
    Schnittgerade First:
      Endpunkte: P_R = (170, 170) und P_F = (370, 170)
      Richtung: dx=200, dy=0
      Verlaengerung 60 px ueber jede Seite:
        links:  (110, 170)
        rechts: (430, 170)
  KRITISCHE FALLEN
    (1) KEINE Leerzeilen im SVG-Block.
    (2) Axonometrie ist Andeutung — keine echte 3D-Projektion.
        Tiefenwirkung wird durch (a) heller/dunkler-Kontrast der
        Dachfuellungen, (b) leichten y-Versatz der hinteren Ecken
        nach oben (10 px), (c) gestaffeltes Zeichnen (hinten zuerst)
        erzeugt. Wer perfekte axonometrische Konsistenz erwartet,
        wird Maß-Diskrepanzen finden — die Skizze ist didaktisch,
        nicht konstruktiv.
  ====================================================================
  -->
  <!-- ============ DACHEBENEN (drei Polygone) ============ -->
  <!-- Hauptdach-rechts (hinten, wird teilweise verdeckt) — als
       Trapez angedeutet, das hinter Walm und Hauptdach-links liegt.
       Eckpunkte: (260,380) vordere Walm-Trauf, (460,360) Walm-
       Rueck-Ecke, (370,170) First-Walmecke, weiter zur hinteren
       linken First-Ecke und zurueck zur Trauf — vereinfacht. -->
  <polygon points="260,380 460,360 370,170 170,170" fill="#e8c98a" stroke="#6a4c2a" stroke-width="1.5"/>
  <!-- Hauptdach-links (vorn, Trapez) -->
  <polygon points="40,380 260,380 370,170 170,170" fill="#e8c98a" stroke="#6a4c2a" stroke-width="1.5"/>
  <!-- Walmflaeche vorn (Dreieck, Tiefenkontrast — dunkler) -->
  <polygon points="260,380 460,360 370,170" fill="#c89a5a" stroke="#6a4c2a" stroke-width="1.5"/>
  <!-- ============ BESCHRIFTUNG DER DACHEBENEN ============ -->
  <text x="140" y="318" font-style="italic" fill="#6a4c2a">Dachebene 1</text>
  <text x="140" y="334" font-size="11" font-style="italic" fill="#666">(Hauptdach, vorn)</text>
  <text x="363" y="303" font-style="italic" fill="#6a4c2a" text-anchor="middle">Dachebene 2</text>
  <text x="363" y="319" font-size="11" font-style="italic" fill="#666" text-anchor="middle">(Walmfläche)</text>
  <!-- Dachebene 3 (Hauptdach hinten) bewusst NICHT beschriftet — sie
       ist in dieser Ansicht ohnehin nur durch First + hintere Kante
       angedeutet; eine Beschriftung würde mehr verwirren als helfen.
       Hinweis bleibt im Fließtext der Sektion. -->
  <!-- ============ SCHNITTGERADEN ============ -->
  <!-- Vorderer Walmgrat — Verlaengerung UNTEN (gepunktet, unter
       Trauf-Walmecke hinaus ins Bodenniveau hinein) -->
  <line x1="260" y1="380" x2="232.2" y2="433" stroke="#c0392b" stroke-width="2" stroke-dasharray="3 5"/>
  <!-- Vorderer Walmgrat — Strecke am Bauteil (durchgezogen, dick) -->
  <line x1="260" y1="380" x2="370" y2="170" stroke="#c0392b" stroke-width="3.5"/>
  <!-- Vorderer Walmgrat — Verlaengerung OBEN (gepunktet, ueber
       First-Walmecke hinaus in die Luft) -->
  <line x1="370" y1="170" x2="397.8" y2="117" stroke="#c0392b" stroke-width="2" stroke-dasharray="3 5"/>
  <!-- First — Verlaengerung LINKS (gepunktet, ueber linke First-
       Ecke hinaus zur Seite) -->
  <line x1="170" y1="170" x2="110" y2="170" stroke="#c0392b" stroke-width="2" stroke-dasharray="3 5"/>
  <!-- First — Strecke am Bauteil (durchgezogen, dick) -->
  <line x1="170" y1="170" x2="370" y2="170" stroke="#c0392b" stroke-width="3.5"/>
  <!-- First — Verlaengerung RECHTS (gepunktet, ueber First-Walmecke
       hinaus zur Seite) -->
  <line x1="370" y1="170" x2="430" y2="170" stroke="#c0392b" stroke-width="2" stroke-dasharray="3 5"/>
  <!-- ============ MARKANTE PUNKTE ============ -->
  <!-- P_T = vordere Trauf-Walmecke (rote Punktmarkierung) -->
  <circle cx="260" cy="380" r="4" fill="#c0392b" stroke="#2c3e50" stroke-width="1"/>
  <text x="252" y="400" text-anchor="end" fill="#c0392b" font-weight="bold">P_T</text>
  <text x="252" y="414" text-anchor="end" font-size="11" font-style="italic" fill="#666">Trauf-Walmecke</text>
  <!-- P_F = First-Walmecke (Schnittpunkt zweier Schnittgeraden) -->
  <circle cx="370" cy="170" r="4" fill="#c0392b" stroke="#2c3e50" stroke-width="1"/>
  <text x="378" y="166" fill="#c0392b" font-weight="bold">P_F</text>
  <text x="378" y="180" font-size="11" font-style="italic" fill="#666">First-Walmecke</text>
  <!-- P_R = linke First-Ecke (Hauptdach-links-Walm-Ende des Firstes) -->
  <circle cx="170" cy="170" r="4" fill="#c0392b" stroke="#2c3e50" stroke-width="1"/>
  <text x="162" y="166" text-anchor="end" fill="#c0392b" font-weight="bold">P_R</text>
  <text x="162" y="180" text-anchor="end" font-size="11" font-style="italic" fill="#666">First-Walmecke (hinten)</text>
  <!-- ============ BESCHRIFTUNG SCHNITTGERADEN ============ -->
  <!-- Walmgrat-Beschriftung (Standard-Slot Pattern 6): links der
       Grat-Mitte ins Hauptdach versetzt, anchor=end. -->
  <text x="303" y="268" text-anchor="end" fill="#c0392b" font-weight="bold">Walmgrat</text>
  <text x="303" y="282" text-anchor="end" font-size="11" font-style="italic" fill="#666">(Schnitt Dachebene 1 ∩ 2)</text>
  <!-- First-Beschriftung (rot, fett) oberhalb des Firstes -->
  <text x="270" y="158" text-anchor="middle" fill="#c0392b" font-weight="bold">First</text>
  <text x="270" y="144" text-anchor="middle" font-size="11" font-style="italic" fill="#666">(Schnitt Dachebene 1 ∩ 3)</text>
  <!-- Verlaengerungs-Hinweise (klein, italic) -->
  <text x="225" y="453" text-anchor="end" fill="#c0392b" font-size="11" font-style="italic">Verlängerung (Gerade)</text>
  <text x="405" y="113" fill="#c0392b" font-size="11" font-style="italic">Verlängerung (Gerade)</text>
  <text x="105" y="166" text-anchor="end" fill="#c0392b" font-size="11" font-style="italic">Verl.</text>
  <text x="435" y="166" fill="#c0392b" font-size="11" font-style="italic">Verl.</text>
  <!-- ============ TITEL UND WELT-ACHSEN ============ -->
  <text x="360" y="40" text-anchor="middle" font-style="italic" font-size="13">Walmdach mit drei Dachebenen — Grat und First als Schnittgeraden</text>
  <text x="360" y="56" text-anchor="middle" font-size="11" font-style="italic" fill="#666">Jede Dachebene laeuft als geometrische Trägerebene unbegrenzt weiter; das Bauteil zeigt nur den endlichen Polygon-Ausschnitt</text>
  <!-- Welt-Koordinaten-Hilfsdarstellung unten rechts -->
  <g transform="translate(640, 450)">
    <text x="-12" y="5" text-anchor="end" font-size="11" fill="#666">Welt:</text>
    <line x1="0" y1="0" x2="32" y2="0" stroke="#2c3e50" stroke-width="1.5"/>
    <polygon points="32,0 27,-3 27,3" fill="#2c3e50"/>
    <text x="36" y="5" font-style="italic">e_hat_h</text>
    <line x1="0" y1="0" x2="0" y2="-32" stroke="#2c3e50" stroke-width="1.5"/>
    <polygon points="0,-32 -3,-27 3,-27" fill="#2c3e50"/>
    <text x="4" y="-36" font-style="italic">e_hat_v</text>
    <circle cx="0" cy="0" r="2" fill="#2c3e50"/>
  </g>
</svg>

Drei Dachebenen sind in der Skizze sichtbar: zwei gegenüberliegende
**Hauptdachebenen** (1 und 3) und die **Walmebene** (2). Jede ist
am Bauteil ein berandetes Polygon — die eigentliche Dachfläche mit
ihrem Umriss aus Traufe, Walmgrat und First —, geometrisch aber
der endliche Ausschnitt einer beidseitig unbegrenzten **Trägerebene**.
Wo zwei dieser Trägerebenen sich schneiden, entsteht eine Gerade:
am **Walmgrat** schneiden sich Dachebene 1 und Dachebene 2, am
**First** schneiden sich Dachebene 1 und Dachebene 3. Die rote
durchgezogene Strecke ist jeweils das, was als Bauteil ausgeführt
wird (Gratsparren, Firstpfette); die beidseitig gepunktete
Fortsetzung markiert die rechnerisch unbegrenzte Schnittgerade.

Genau diese **Schnittlogik** ist die zentrale konstruktive
Anwendung der Ebene im Holzbau und die Grundlage der
Dachausmittlung — der raumgeometrischen Ermittlung des
Zusammenschlusses mehrerer Dachflächen in der Grundriss-Projektion.
Wo der Lehrling die Dachfläche als geneigte Ebene am Sparrendach
erstmals begegnet, geht der Meister einen Schritt weiter und
behandelt sie als Glied einer Ebenen-Schar, die sich an den
Kanten kreuzt.

## Ebenen-Rollen im Werkplan und am Bauteil

Die Berufssprache benennt Ebenen — wie die Punkte und die Geraden
— nach ihrer Rolle in der Konstruktion. Dieselbe geometrische
Sache, eine zweidimensionale unbegrenzte Punktmenge, heißt je
nach Funktion anders. Die Familie der „-ebene"-Komposita ist
auffällig dicht und funktional klar gegliedert.

**Bauteil-tragende Ebenen** — die Trägerebenen ausgeführter
ebener Bauteile:

| Kompositum | Wo sie auftritt | Bauteil-Bezug |
|---|---|---|
| **Dachebene** | jede schräge oder horizontale Dachseite eines Daches | Trägerebene der Dachfläche; das Sparrenbündel liegt in dieser Ebene. Im Lehrlings-Vokabular die zugänglichste Ebenen-Rolle. |
| **Wandebene** | vertikale Trägerebene einer Außen- oder Innenwand; Außenkante des Holzrahmenbaus | Bezugsfläche der Wandbeplankung; durch zwei Wandebenen lassen sich Gebäude-Längsachsen ablesen. |
| **Bodenebene** / **Deckenebene** | horizontale Trägerebene eines Geschoss-Fussbodens oder einer Decken-Unterkante | Höhenreferenz innerhalb eines Geschosses; ablesbar am Schnurgerüst und am Aufmaß. |
| **Schalungsebene** | bei Brettschalung die formgebende Ebene der Schal-Haut | Die Schalebene begrenzt eine Schalung; sie ist die Sicht-Ebene des fertigen Bauteils. |

**Bezugs- und Hilfs-Ebenen** — ohne Bauteil-Identität, aber als
geometrische Referenz unentbehrlich:

| Kompositum | Wo sie auftritt | Bezug |
|---|---|---|
| **Bezugsebene** | Höhenreferenz z = 0 für die Höhenmaße eines Bauwerks | An der Bezugsebene werden alle Höhenkoten gemessen. Im Werkplan typischerweise die Oberkante des fertigen Erdgeschoss-Fussbodens („± 0,00"). |
| **Symmetrieebene** | konstruktive Spiegelebene eines symmetrischen Bauteils | Beim Satteldach die welt-vertikale Ebene durch den First; beide Dachflächen sind zueinander spiegelbildlich. |
| **Mittelebene** | Symmetrieebene eines mehrschichtigen Plattenwerkstoffs | Bei Brettsperrholz die zur Mittelebene symmetrische Schicht-Anordnung; der Aufbau ist beidseits der Mittelebene spiegelbildlich. |
| **Horizontalebene** / **waagrechte Ebene** | rechtwinklig zur Welt-Lotachse | Bezugsebene für jede Höhenmessung; die Wasserwaage gibt sie lokal an. |
| **Lotebene** / **lotrechte Ebene** | welt-vertikale Ebene durch eine Bauteilachse | Im Holzbau die natürliche Bezugs-Vertikalebene für ein geneigtes Stabbauteil; eigene Spezialisierung mit zwei Lage-Bedingungen, siehe `hauptglossar/00_ressourcen/hg_lotebene.md`. |
| **Auflagerebene** | waagrechte Oberkante einer Pfette als Auflage des Sparrens | Das Wort tritt als Substantiv selten auf, die Sache aber überall, wo ein Stabbauteil auf ein anderes auflastet. |

**Anriss-Ebenen** — Werkstatt- und Übertragungs-Ebenen:

Die traditionelle Zimmerei kennt mit dem **Reissboden** eine der
wenigen Welt-Anschauungs-Realisierungen einer geometrischen
Ebene: ein ebener Bretterboden, auf den ein Dachprofil mit der
Schlagschnur im Maßstab 1:1 aufgeschnürt wird. Der Reissboden ist
keine abstrakte Bezugsebene, sondern eine **materialisierte**
Ebene als Anriss-Untergrund — ein Stück mathematischer Ebene,
das man begehen kann. In der modernen Praxis ist er durch
Abbund-Software weitgehend ersetzt; als Lehr-Bezugsobjekt für
Aufriss, Schiftung und Profilübertragung ist er nicht
verschwunden.

Eine Beobachtung zur Lese-Hilfe: die Berufssprache trennt
**Trägerebene** und **Rolle** nicht immer sauber. „Dachebene" und
„Dachfläche" werden im Korpus gelegentlich austauschbar gebraucht;
fachlich genau bezeichnet **Dachebene** die unbegrenzte
Trägerebene, **Dachfläche** den durch ein Polygon berandeten,
material gewordenen Ausschnitt. Dieselbe Trennung Strecke ↔
Gerade gilt eine Dimension höher: Fläche ↔ Ebene.

## Wie eine Ebene am Bau festgelegt wird

Drei berufspraktische Wege, eine Ebene am Bauplatz oder am
Bauteil festzulegen, plus eine vierte Konstruktion über den
Schnitt:

**Drei Punkte** — die häufigste Bestimmung am Bauplatz. Am
**Schnurgerüst** werden drei oder mehr Pfostenkopf-Punkte mit
Schlauchwaage oder Nivelliergerät auf dieselbe Welt-Höhe gesetzt;
sie liegen dann automatisch in einer horizontalen Bezugsebene.
Geometrisch reichen drei nicht-kollineare Punkte, um genau eine
Ebene festzulegen — vier Pfostenköpfe sind eine praktische
Redundanz, keine geometrische Notwendigkeit. Auch der
Reissboden ruht geometrisch auf drei Stützpunkten, auch wenn die
Praxis ihn vollflächig auflegt.

**Ein Punkt plus zwei Vektoren** — der Achspunkt eines Bauteils
zusammen mit zwei aufspannenden Richtungen. Die welt-vertikale
Lotebene eines Sparrens entsteht so: ein Punkt auf der
Sparrenachse, die Sparrenachsen-Richtung und die Welt-Lotachse
spannen die Ebene auf.

**Ein Punkt plus Normalenvektor** — etwa eine Bezugsebene
rechtwinklig zu einer Bauteilachse. Eingestellt wird der
Normalenvektor durch die Werkzeug-Ausrichtung der Säge oder
Schmiege.

**Schnitt zweier Ebenen ist eine Gerade** — die dual-konstruktive
Variante zu „drei Punkte". An Walmdach und Satteldach lebt
die Konstruktion (siehe Pflicht-Skizze): jede Schnittgerade
zweier Dachebenen materialisiert sich als Grat, Kehle oder
First. In der Dachausmittlung werden die Dachebenen als geneigte
Ebenen behandelt; horizontale Hilfs-Ebenen (Höhenlinien-
Konstruktion) werden eingelegt, um die wahre Lage der
Schnittgeraden zu finden.

Die zentrale Werkzeug-Trias am Bau:

| Werkzeug | Welche Ebene wird realisiert |
|---|---|
| **Wasserwaage** | waagrechte Ebene lokal auf einem Bauteil (über die horizontale Libelle); lotrechte Ebene über die senkrechte Libelle |
| **Schlauchwaage** / **Nivelliergerät** / **Rotationslaser** | waagrechte Bezugsebene über größere Distanzen am Bauplatz (Meterriss am Schnurgerüst) |
| **Senkel** / Senklot | zwei Senkel-Schnüre spannen eine welt-vertikale Ebene auf; der Senkelschnitt am Sparren realisiert eine lotrechte Schnittebene |
| **Schmiege** / **Schiftlehre** | schräge Schnittebene unter einem eingestellten Winkel |
| **Reissboden** | 1:1-Ebene als materialisierter Anriss-Untergrund — eines der wenigen Werkzeuge, in dem die Ebene selbst Werkzeug ist |
| **Schnurgerüst** | drei oder vier Pfostenkopf-Punkte definieren eine waagrechte Bezugsebene am Bauplatz; die Bauachsen werden auf dieser Ebene aufgespannt |

Methodisch wichtig: das Schnurgerüst wird mit einer Toleranz von
wenigen Millimetern eingerichtet — alle Pfostenköpfe auf
derselben Welt-Höhe; die so realisierte Bezugsebene ist eine
der präzisesten ebenen Realisierungen am Bauplatz und Grundlage
aller weiteren Maß-Übertragungen.

## Was eine Ebene nicht ist — Fläche, Polygon, Dachfläche, Schicht

Vier Begriffe stehen im Holzbau in unmittelbarer Nähe zur Ebene
und werden gern mit ihr verwechselt. Die Trennung ist
didaktisch tragend, weil sie die Werkstatt-Wirklichkeit von der
geometrischen Idealisierung trennt.

**Fläche.** Eine Bauteilfläche — Dachfläche, Wandfläche, Bodenfläche
— ist **endlich**, **konkret** und **orientiert**: sie hat einen
Umriss (ein Polygon als Rand), eine Materialität (Holz, Schalung,
Eindeckung) und meistens eine ausgezeichnete Seite (außen/innen,
oben/unten). Eine Ebene dagegen ist **unbegrenzt**, **abstrakt**
und ohne inhärente Orientierung — kein Rand, kein Material, keine
ausgezeichnete Seite. Die Beziehung ist strukturell parallel zu
Strecke ↔ Gerade: die Bauteilfläche ist die endlich berandete
Realisierung, die Ebene der beidseitig unbegrenzte Träger.

**Polygon.** Ein Polygon ist eine durch eine geschlossene Folge
von Strecken berandete, zweidimensionale, aber nicht-volumige
Figur. Es liegt **in einer Ebene** (es ist „eben"), ist aber
nicht die Ebene selbst — wie ein Streckenzug nicht eine Gerade
ist. Im Werkplan ist der Umriss einer Dachfläche ein Polygon, der
Träger eine Ebene.

**Dachfläche.** Die Dachfläche ist die Bauteil-Spezialisierung
der Ebene: ein durch ein Polygon berandeter, beschränkter Teil
einer Ebene **mit zusätzlicher Orientierung** (die Außennormale
weist nach oben). Eine Dachebene ohne Polygon-Berandung wäre ein
abstraktes geometrisches Objekt ohne Bauteil-Identität; eine
Dachfläche ist die Ebene-plus-Polygon-plus-Orientierung. Wenn der
Korpus zwischen „Dachebene" und „Dachfläche" gleitet, ist meist
die Dachfläche gemeint — die App-Konvention trennt sauber:
Dachebene = der unendliche Träger, Dachfläche = das endliche
Bauteil.

**Schicht.** Eine Schicht im modernen Wandaufbau —
Dämm-Schicht, Konstruktions-Schicht, Lufdichtheits-Schicht —
hat **Dicke**, also **Volumen**. Eine Ebene dagegen ist eine
zweidimensionale Punktmenge ohne Dicke. Hier liegt ein
sprachlicher Stolperstein des modernen Holzrahmenbaus: Komposita
wie **Installationsebene** und **Hinterlüftungsebene** tragen
„Ebene" im Namen, bezeichnen aber Schichten — die Installations-
ebene zwischen Dampfsperre und Innenverkleidung ist in der
Praxis 60 bis 80 mm dick, die Hinterlüftungsebene zwischen
Konterlattung und Dachhaut ist ein durchlüfteter Hohlraum mit
Querschnitt. Beide sind **Schichten**, die jeweils durch zwei
Ebenen (Schicht-Oberseite und Schicht-Unterseite) begrenzt
werden — die Schicht selbst ist nicht die Ebene. Wer die Wörter
hört, soll wissen, dass „Ebene" hier im Sinne von „Funktions-
Schicht im Wandaufbau" gebraucht wird, nicht im geometrischen
Sinn dieses Eintrags.

Englische CAD-Anglizismen wie **„plane"** für Ebene oder
**„datum plane"** für Bezugsebene sind im deutschen Werkplan
unüblich und Software-Slang; **„level"** für Horizontalebene ist
ein Werkzeug-Anglizismus aus dem englischen „spirit level". Sie
werden im DACH-Holzbau-Korpus nicht als Synonyme geführt.

## Verweise

Diese Subglossar-Datei stützt sich auf die folgenden Hauptglossar-
Begriffe; bei Detailfragen ist dort die normative Definition zu
finden:

- `hauptglossar/00_ressourcen/hg_ebene.md` — das normative Hauptglossar zur
  Ebene, mit mathematischer Definition als zweidimensionaler
  affiner Unterraum von ℝ³, Hesse-Normalform, Wohldefiniertheit,
  Implementierungshinweis und Quellenliste.
- `hauptglossar/30_holzbau/hg_dachflaeche.md` — die Spezialisierung
  Ebene + Polygon + Außennormale; das im Bauteil tatsächlich
  realisierte Dachflächen-Objekt.
- `hauptglossar/00_ressourcen/hg_bezugsebene.md` — Ebene mit Bezugsrolle
  (Höhenreferenz z = 0 in einem Tool).
- `hauptglossar/00_ressourcen/hg_lotebene.md` — welt-vertikale Ebene durch eine
  Bauteilachse; geodätisch gelesene Spezialisierung.
- `hauptglossar/00_ressourcen/hg_senkel.md`, `hauptglossar/00_ressourcen/hg_bleischnitt.md` —
  Lot-Lage-Klassifikationen über Ebenen (welt-horizontal /
  welt-vertikal).
- `hauptglossar/00_ressourcen/hg_polygon.md` — die berandete, eben liegende
  Geschwister-Figur (Negativ-Abgrenzung).
- `hauptglossar/00_ressourcen/hg_halbraum.md` — die durch eine Ebene zerteilte
  Raumhälfte (eigener Eintrag).
- `hauptglossar/00_ressourcen/hg_gerade.md` — als Schnitt zweier Ebenen.
- `hauptglossar/00_ressourcen/hg_punkt.md`, `hauptglossar/00_ressourcen/hg_vektor.md` — die
  begrifflichen Voraussetzungen der Ebene.
- `hauptglossar/00_ressourcen/hg_weltkoordinatensystem.md` — das Welt-
  Bezugssystem, gegen das Welt-Lage-Eigenschaften (waagrecht,
  lotrecht) einer Ebene formuliert werden.

Verwandte Subglossar-Einträge (Folgearbeit): `sg_dachflaeche`,
`sg_bezugsebene`, `sg_polygon`, `sg_halbraum`, `sg_lotebene`
(falls `subglossar_pendant` heraufgesetzt).
