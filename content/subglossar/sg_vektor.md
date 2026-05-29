---
id: sg_vektor
benennung: Vektor
glossar_ref: vektor
cluster: ressourcen
theorie_pflichtig: optional
status: entwurf
---

# Vektor (Subglossar)

Brücke vom normativen Hauptglossar (`hauptglossar/00_ressourcen/hg_vektor.md`) zu
den stufenweisen Theorie-Inhalten. Hier liegt die didaktische
Aufbereitung: der Vektor lebt im DACH-Holzbau **nur in
Rollen-Komposita** — Kraftvektor, Richtungsvektor, Normalenvektor —,
nicht als nacktes Werkstatt-Wort. Schwerpunkt liegt auf der
Meister-Stufe; die unteren Stufen bleiben ehrlich leer, weil dem
Vektor jeder zimmermannssprachlich gewachsene Wortstamm fehlt
(`SG_KONVENTIONEN.md` §7).

---

## Was der Vektor im Holzbau ist

Ein **Vektor** ist eine **gerichtete Verschiebung mit Länge, ohne
festen Anfangspunkt** — eine ortsfreie Größe, die Richtung und
Betrag trägt, aber keine Stelle in der Welt. Anders als der Punkt,
der genau eine Lage benennt, und anders als die Strecke, die zwei
konkrete Endpunkte am Bauteil verbindet, darf ein Vektor parallel
verschoben werden: zwei Pfeile gleicher Richtung und gleicher Länge
an verschiedenen Stellen sind **derselbe Vektor**.

Im DACH-Holzbau-Korpus tritt das nackte Wort „Vektor" **nicht** im
Werkstattgespräch auf. Es lebt durchgängig in **Rollen-Komposita aus
dem Statik- und CAD-Register**: **Kraftvektor** in der
Tragwerksstatik, **Richtungsvektor** an der Bauteilachse,
**Normalenvektor** an der Dachfläche, **Ortsvektor** vom Welt-Ursprung
zu einem Bauwerkspunkt. Wo der Zimmermann etwas Vektor-Artiges meint,
sagt er ein **Werkzeug-Wort** (Lot, Senkel, Schmiege) oder ein
**Tätigkeits-Wort** (Schub, Auszug, Versatz) — alles Wörter, die im
Hauptglossar eigene Begriffe sind oder als abgelehnte Benennungen
geführt werden. Der Vektor ist damit, schärfer noch als die Gerade,
ein **mathematischer Importbegriff**: er kommt über die
Ingenieur-Statik (Eurocode-Generation) und die CAD-Verbreitung
(Cadwork, SEMA) ins Holzbau-Feld, nicht aus dem Werkstatt-Korpus
heraus gewachsen.

Die Wortwurzel selbst trägt diese Lesart treffend: lateinisch
***vector*** „Träger, Fahrer", zum Verb ***vehere*** „tragen,
fahren" — ein Vektor **trägt** einen Punkt von A nach B, das ist
genau die Verschiebungs-Bedeutung. In der Mathematik wurde der
Begriff im 19. Jahrhundert durch William Rowan Hamilton geprägt; in
den Holzbau gelangt er erst mit der modernen Statik und CAD.

## Welt-Einheitsvektoren e_hat_h und e_hat_v am Welt-Ursprung

In allen bisherigen P1-Skizzen (sg_punkt, sg_strecke, sg_gerade,
sg_ebene, sg_kerve) sitzt rechts unten als kleines Inset ein Paar
Pfeile: ein horizontaler e_hat_h und ein welt-vertikaler e_hat_v am
Welt-Ursprung. Diese Pfeile sind **Einheitsvektoren** — Vektoren mit
Länge 1 — und orientieren das Welt-Koordinatensystem, in dem alle
Bauteil-Punkte liegen. Sie sind das einfachste Vektor-Bild dieses
Subglossars und liefern den Anschluss an die übrigen P1-Einträge.

<svg viewBox="0 0 360 280" xmlns="http://www.w3.org/2000/svg" font-family="sans-serif" font-size="13">
  <rect width="100%" height="100%" fill="#f4f1ea"/>
  <!--
  ====================================================================
  SVG-DOKUMENTATION: sg_vektor F.1 — Welt-Einheitsvektoren e_h und e_v
                     am Welt-Ursprung (Pflicht-Skizze)
  ====================================================================
  ZWECK
    Die zwei Welt-Einheitsvektoren e_hat_h (horizontal) und e_hat_v (welt-
    vertikal nach oben) als beschriftete Pfeile am Welt-Ursprung,
    zentral und groß dargestellt — die gleiche Darstellung, die in
    allen P1-Skizzen rechts unten als kleines Inset auftaucht, hier
    nun als eigene Hauptdarstellung erklaert.
    Zusaetzlich: ein zweites, paralleles Pfeil-Paar links oben am Bild,
    das demselben Vektor entspricht (Ortsfreiheit-Illustration —
    parallel verschobene Pfeile gleicher Richtung und Laenge
    repraesentieren denselben Vektor).
  STIL-KONVENTIONEN (Pilot sg_punkt / sg_strecke / sg_kerve)
    Farben:
      #2c3e50 Welt-Pfeile (Anthrazit, Pilot der P1-Inset-Konvention)
      #999    Geist-Kopie (Ortsfreiheits-Illustration), gestrichelt
      #666    italic-Bezeichner klein
    Schriftgrößen: 13 Standard, 11 italic-klein
  GEOMETRIE
    Welt-Ursprung O bei (130, 200), Pfeile in voller Größe:
      e_h: (130,200) -> (240,200), Laenge 110 px
      e_v: (130,200) -> (130, 90), Laenge 110 px (nach OBEN in
            SVG-Koordinaten = -y)
    Geist-Kopie (parallel verschoben) bei Ursprung (250, 90):
      e_h-Kopie: (250,90) -> (310,90), gleiche Richtung, halbe
                 Darstellungs-Laenge nur zur Andeutung
      Hier WICHTIG: Im didaktischen Bild zeigen die Geist-Kopie und
      das Original GLEICHE Laenge, sonst waere es nicht "derselbe
      Vektor". Deshalb Geist-Kopie ebenfalls 110 px. Position so
      gewaehlt, dass sie nicht ueber die Hauptdarstellung laeuft.
    Korrektur: Geist-Kopie nur fuer e_h, am rechten oberen Rand:
      Start (210, 60), Ende (210+110, 60) = (320, 60).
    Skala-Hinweis (Laenge 1) als kleine eckige Klammer unter e_h.
  KRITISCHE FALLEN
    KEINE Leerzeilen im SVG-Block.
  ====================================================================
  -->
  <!-- Welt-Ursprung-Markierung -->
  <circle cx="130" cy="200" r="3" fill="#2c3e50"/>
  <text x="118" y="218" text-anchor="end" font-size="11" font-style="italic" fill="#666">O</text>
  <text x="118" y="232" text-anchor="end" font-size="11" font-style="italic" fill="#666">(Welt-Ursprung)</text>
  <!-- e_hat_h horizontal -->
  <line x1="130" y1="200" x2="240" y2="200" stroke="#2c3e50" stroke-width="2"/>
  <polygon points="240,200 232,195 232,205" fill="#2c3e50"/>
  <text x="252" y="205" fill="#2c3e50" font-style="italic" font-weight="bold">e_hat_h</text>
  <text x="252" y="220" font-size="11" font-style="italic" fill="#666">horizontal, Länge 1</text>
  <!-- e_hat_v vertikal nach oben -->
  <line x1="130" y1="200" x2="130" y2="90" stroke="#2c3e50" stroke-width="2"/>
  <polygon points="130,90 125,98 135,98" fill="#2c3e50"/>
  <text x="138" y="86" fill="#2c3e50" font-style="italic" font-weight="bold">e_hat_v</text>
  <text x="138" y="100" font-size="11" font-style="italic" fill="#666">welt-vertikal, Länge 1</text>
  <!-- Geist-Kopie von e_hat_h: parallel verschoben, GLEICHE Laenge, GLEICHE Richtung
       — derselbe Vektor an anderer Stelle (Ortsfreiheits-Illustration). -->
  <line x1="210" y1="50" x2="320" y2="50" stroke="#999" stroke-width="1.6" stroke-dasharray="4 3"/>
  <polygon points="320,50 312,45 312,55" fill="#999"/>
  <text x="265" y="40" text-anchor="middle" font-size="11" font-style="italic" fill="#666">parallel verschobene Geist-Kopie von e_hat_h</text>
  <text x="265" y="28" text-anchor="middle" font-size="11" font-style="italic" fill="#666">— derselbe Vektor, andere Stelle</text>
  <!-- Titelzeile -->
  <text x="180" y="262" text-anchor="middle" font-style="italic" font-size="12">Welt-Einheitsvektoren e_hat_h und e_hat_v am Welt-Ursprung</text>
</svg>

Beide Pfeile am Welt-Ursprung haben Länge 1 und sind paarweise
rechtwinklig. Der e_hat_h liegt in der horizontalen Welt-Ebene, der e_hat_v
zeigt welt-vertikal nach oben — entgegen der Schwerkraft, in der
Richtung, in die das Senkel-Schnur**ende** zeigt, wenn das
Senkel-Gewicht losgelassen ist. Die graue, gestrichelte Kopie rechts
oben hat dieselbe Richtung und dieselbe Länge wie e_hat_h, sitzt aber an
einer anderen Stelle: sie ist **derselbe Vektor**. Die Ortsfreiheit
ist die zentrale Eigenschaft, die den Vektor von der Strecke trennt
— eine Strecke darf man nicht parallel verschieben, ohne dass sie zu
einer anderen Strecke wird.

## Drei Vektor-Rollen im Holzbau

Im Holzbau-Korpus treten drei Rollen klar trennbar auf, in denen der
Vektor tatsächlich vorkommt. Sie sind keine geometrischen Subtypen —
ein Vektor ist ein Vektor —, sondern unterschiedliche **Funktionen**
im Tragwerksplan oder im CAD-Modell.

| Rolle | Wo sie auftritt | Was sie trägt |
|---|---|---|
| **Kraftvektor** | Tragwerksstatik: Lasten (Eigengewicht, Schnee, Wind), Auflagerreaktionen, Stab-Schnittkräfte (Normalkraft, Querkraft) | Betrag in kN, Richtung im Raum, Angriffspunkt am Bauteil. Am starren Körper darf der Kraftvektor entlang seiner **Wirkungslinie** verschoben werden, ohne dass sich die Wirkung am Tragwerk ändert — er ist dort linienflüchtig. |
| **Richtungsvektor** an Bauteilachse / Sparrenachse | CAD-Datenmodell (Cadwork, SEMA): das Bauteil wird intern durch einen Achs-Punkt plus Richtungsvektor (oder durch zwei Endpunkte, deren Differenz den Richtungsvektor liefert) beschrieben | reine Richtungs- und Längen-Information der Bauteilachse. Im Werkstatt-Gespräch heißt die Information **Achse** oder **Schmiege** (für die Winkel-Seite bei der Schiftung), nicht „Richtungsvektor". |
| **Normalenvektor** an Dachfläche | Dachebene mit ausgezeichnetem, rechtwinklig auf der Fläche stehendem Einheitsvektor; Hintergrund für Schiftung und Dachausmittlung | rechtwinklige Richtung der Dachfläche. Im Werkstatt-Korpus wird die Information nicht als Normalenvektor benannt — sie lebt implizit in den Schmiegen, Auszugs-Maßen und der Schiftungs-Tafel. |

Alle drei Rollen teilen ein Muster: der Vektor lebt als
**Hintergrund-Begriff** in der Statik- und CAD-Schicht, ohne dass
das Wort selbst im Werkstattgespräch fällt. Die Werkstatt spricht
von Schub, Auszug, Schmiege, Achse; das CAD rechnet im Hintergrund
mit Vektoren.

## Kraftvektor am Sparren — die Last in zwei Komponenten zerlegt

Die didaktisch tragende Vektor-Anwendung im Holzbau ist die
**Zerlegung des Last-Kraftvektors am geneigten Sparren** in eine
Komponente parallel zur Sparrenachse (Schub-Komponente) und eine
Komponente rechtwinklig zur Sparrenachse (Druck-Komponente). Diese
Zerlegung ist die Grund-Operation der Sparren-Statik und nutzt die
volle Vektor-Algebra (Komponentenzerlegung).

<svg viewBox="0 0 720 380" xmlns="http://www.w3.org/2000/svg" font-family="sans-serif" font-size="13">
  <rect width="100%" height="100%" fill="#f4f1ea"/>
  <!--
  ====================================================================
  SVG-DOKUMENTATION: sg_vektor F.2 — Kraftvektor am Sparren, zerlegt
                     in Schub- und Druckkomponente (Optional-Skizze)
  ====================================================================
  ZWECK
    Sparren im Profil (analog sg_strecke / sg_gerade, ca. 30 Grad
    Neigung). An der Sparrenmitte greift ein Kraftvektor F welt-
    vertikal nach unten an (z. B. Schneelast). Er wird in zwei
    Komponenten zerlegt:
      F_parallel: parallel zur Sparrenachse (Schub-Komponente),
      F_normal:   rechtwinklig zur Sparrenachse (Druck-Komponente).
    Die Hauptkraft F ist durchgezogen (kraeftig rot), die zwei
    Komponenten sind gestrichelt (rot, dasharray) — beide an
    demselben Angriffspunkt P_M an der Sparrenoberkante.
  STIL-KONVENTIONEN (Pilot sg_punkt / sg_strecke / sg_gerade)
    Farben:
      #f5e6c8 Sparren-Fuellung
      #6a4c2a Holz-Umriss
      #c0392b Kraftvektor (durchgezogen, stroke-width 3) und
              Komponenten (gestrichelt, stroke-width 2,
              dasharray 5 4)
      #2c3e50 Welt-Pfeile, Angriffspunkt-Marker
      #666    italic-Bezeichner klein
    Schriftgrößen: 13 Standard, 11 italic-klein
  GEOMETRIE
    Sparrenachse 30 Grad: vom Sparrenfusspunkt F=(110, 280) zum
    Firstpunkt P_F=(610, 90). dx=500, dy=-190.
    Laenge: sqrt(500^2 + 190^2) ≈ 535. tan(alpha) = 190/500 = 0.38;
    alpha ≈ 20.8 Grad (etwas flacher als nominell 30, aber visuell
    klar als geneigter Sparren).
    Sparrenhoehe perpendikular zur Achse: 28 px.
    Achsen-Einheitsvektor:    e_a = ( 500/535, -190/535) ≈ ( 0.935, -0.355)
    Normalen-Einheitsvektor:  n_a = ( 190/535,  500/535) ≈ ( 0.355,  0.935)
       (zeigt nach UNTEN-RECHTS, also sparrenunterseitig)
       Negativ: -n_a = (-0.355, -0.935) zeigt sparrenoberseitig.
    Sparren-Polygon (Oberkante 14 px in -n_a-Richtung, Unterkante 14
    px in +n_a-Richtung von der Achse aus):
      Vordach-Stirn oben:      F + (-n_a)*14 ≈ (110 - 5, 280 - 13) = (105, 267)
      Vordach-Stirn unten:     F + (+n_a)*14 ≈ (110 + 5, 280 + 13) = (115, 293)
      Firstpfetten-Stirn oben: P_F + (-n_a)*14 ≈ (610 - 5, 90 - 13) = (605, 77)
      Firstpfetten-Stirn unten:P_F + (+n_a)*14 ≈ (610 + 5, 90 + 13) = (615, 103)
    Angriffspunkt P_M auf der Sparren-OBERSEITE in Mitte:
      Mitte der Achse: (360, 185). Oberseite: (360 + (-n_a)*14) ≈ (355, 172).
    Kraftvektor F welt-vertikal nach unten, Laenge 120 px:
      F-Spitze (Pfeilspitze): (355, 172 + 120) = (355, 292)
      WICHTIG: Pfeil von Angriffspunkt P_M=(355, 172) NACH UNTEN zur
      Spitze (355, 292) gezeichnet — Kraftvektor zeigt in
      Wirkungsrichtung.
    Komponente F_parallel = (F · e_a) * e_a:
      F = (0, +120) in (SVG-y-nach-unten-positiv-)Welt-Koordinaten.
      e_a = (0.935, -0.355) ist in derselben Welt-Konvention.
      F · e_a = 0*0.935 + 120*(-0.355) = -42.6.
      F_parallel = -42.6 * e_a = (-39.83, 15.13)
      Die Schub-Komponente zeigt bergab am Sparren (negativ in
      Achsen-Richtung = vom First zum Sparrenfuss).
      Endpunkt von P_M=(355,172) aus: (315.17, 187.13).
    Komponente F_normal = F - F_parallel:
      F_normal = (0, 120) - (-39.83, 15.13) = (39.83, 104.87)
      Endpunkt von P_M aus: (394.83, 276.87).
      Pruefen: |F_normal| = sqrt(39.83^2 + 104.87^2) ≈ 112.18
      |F_parallel| = sqrt(39.83^2 + 15.13^2) ≈ 42.61
      Pythagoras: 42.61^2 + 112.18^2 ≈ 14400 = 120^2. ✓
      Bild-Summe: (-39.83 + 39.83, 15.13 + 104.87) = (0, 120) = F. ✓
    EINHEITLICHE SKALIERUNG (Faktor 1.0): alle drei Pfeile sind
    masstabsgetreu in derselben Laengen-Skala. F = 120 px,
    F_parallel = 42.61 px, F_normal = 112.18 px. Damit bilden die
    drei Pfeile geometrisch ein rechtwinkliges Parallelogramm mit
    F als Diagonale — wie der Fliesstext es behauptet (sg_vektor-
    Review 2026-05-14, mittlerer Befund: keine unabhaengig
    skalierten Komponenten).
    Wichtige didaktische Anmerkung: F_parallel und F_normal sind
    die zwei Vektor-Summanden, deren Summe wieder F ist. Verzichten
    auf die Parallelogramm-Linien (sonst ueberladen); nur F,
    F_parallel, F_normal als drei Pfeile vom gemeinsamen
    Angriffspunkt P_M aus.
  KRITISCHE FALLEN
    KEINE Leerzeilen im SVG-Block.
  ====================================================================
  -->
  <!-- Sparren-Polygon (30 Grad nominell, ca. 20.8 Grad im Bild) -->
  <polygon points="105,267 605,77 615,103 115,293" fill="#f5e6c8" stroke="#6a4c2a" stroke-width="1.5"/>
  <!-- Sparrenachse als duenne gestrichelte Mittellinie -->
  <line x1="110" y1="280" x2="610" y2="90" stroke="#999" stroke-width="0.8" stroke-dasharray="3 3"/>
  <text x="618" y="94" font-size="11" font-style="italic" fill="#666">Sparrenachse</text>
  <!-- Sparrenfusspunkt und Firstpunkt als kleine schwarze Marker (Kontext) -->
  <circle cx="110" cy="280" r="3" fill="#2c3e50"/>
  <text x="100" y="300" text-anchor="end" font-size="11" font-style="italic" fill="#666">Sparrenfusspunkt</text>
  <circle cx="610" cy="90" r="3" fill="#2c3e50"/>
  <text x="622" y="88" font-size="11" font-style="italic" fill="#666">Firstpunkt</text>
  <!-- Angriffspunkt P_M an der Sparrenoberseite, Mitte -->
  <circle cx="355" cy="172" r="4" fill="#c0392b" stroke="#2c3e50" stroke-width="1"/>
  <text x="346" y="166" text-anchor="end" fill="#c0392b" font-weight="bold">P_M</text>
  <text x="346" y="160" text-anchor="end" font-size="11" font-style="italic" fill="#666">Angriffspunkt</text>
  <!-- Kraftvektor F (durchgezogen, dick, welt-vertikal nach unten) -->
  <line x1="355" y1="172" x2="355" y2="292" stroke="#c0392b" stroke-width="3"/>
  <polygon points="355,292 349,282 361,282" fill="#c0392b"/>
  <text x="362" y="240" fill="#c0392b" font-weight="bold">F</text>
  <text x="362" y="254" font-size="11" font-style="italic" fill="#666">Last-Kraftvektor</text>
  <text x="362" y="268" font-size="11" font-style="italic" fill="#666">(welt-vertikal)</text>
  <!-- Komponente F_parallel (gestrichelt, Sparrenachse-parallel, bergab) -->
  <line x1="355" y1="172" x2="315.2" y2="187.1" stroke="#c0392b" stroke-width="2" stroke-dasharray="5 4"/>
  <polygon points="315.2,187.1 322.2,180.2 325,187.7" fill="#c0392b"/>
  <text x="306" y="180" text-anchor="end" fill="#c0392b" font-weight="bold" font-style="italic">F_parallel</text>
  <text x="306" y="194" text-anchor="end" font-size="11" font-style="italic" fill="#666">Schub (parallel zur Achse)</text>
  <!-- Komponente F_normal (gestrichelt, rechtwinklig zur Achse) -->
  <line x1="355" y1="172" x2="394.8" y2="276.9" stroke="#c0392b" stroke-width="2" stroke-dasharray="5 4"/>
  <polygon points="394.8,276.9 387.9,269.9 395.4,267" fill="#c0392b"/>
  <text x="402" y="246" fill="#c0392b" font-weight="bold" font-style="italic">F_normal</text>
  <text x="402" y="260" font-size="11" font-style="italic" fill="#666">Druck (rechtwinklig zur Achse)</text>
  <!-- Titel und Welt-Pfeile-Inset -->
  <text x="360" y="334" text-anchor="middle" font-style="italic" font-size="12">Last-Kraftvektor F am Sparren, zerlegt in Schub- und Druckkomponente</text>
  <text x="360" y="350" text-anchor="middle" font-size="11" font-style="italic" fill="#666">F = F_parallel + F_normal (Vektor-Summe)</text>
  <g transform="translate(640, 350)">
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

Drei Pfeile setzen am gemeinsamen Angriffspunkt **P_M** an der
Sparrenoberseite an: die durchgezogene **Last-Kraft F** zeigt
welt-vertikal nach unten (Eigengewicht plus Schneelast), die
gestrichelte **F_parallel** läuft bergab längs der Sparrenachse, die
gestrichelte **F_normal** steht rechtwinklig auf der Sparrenachse
und drückt auf den Sparren. Die Vektor-Summe F_parallel + F_normal
ist wieder F — geometrisch sind die zwei Komponenten zwei Kanten
eines rechtwinkligen Parallelogramms, dessen Diagonale F ist.

Diese Zerlegung trägt zwei Hinweise auf die Statik-Feinheit, die im
Hauptglossar nur in der Erläuterung anklingt. **Erstens**: Eine Kraft
ist nicht „nur" ein Vektor wie in der Schul-Mathematik, sondern eine
**gerichtete Größe mit physikalischer Einheit** (kN) **plus
Angriffspunkt am Bauteil** — drei Angaben, nicht zwei. **Zweitens**:
Am starren Tragwerk darf der Kraftvektor entlang seiner Wirkungslinie
verschoben werden (linienflüchtige Lesart); am verformten Bauteil
zählt der Angriffspunkt mit (gebundene Lesart). Im Holzbau-Alltag
wird die Last typischerweise als linienflüchtig modelliert — der
Sparren ist im Bemessungsmodell ein Stab.

## Was ein Vektor nicht ist — Strecke, Punkt, Pfeil, Tupel

Vier Begriffe stehen dem Vektor unmittelbar nah und werden
gern mit ihm verwechselt. Die Abgrenzungen sind didaktisch wichtig,
weil sie die Werkstatt-Wirklichkeit (Bauteil, Werkplan) von der
ortsfreien Mathematik trennen.

**Strecke.** Die Strecke ist **ortsgebunden** — sie hat zwei konkrete
Endpunkte am Bauteil und liegt fest in der Welt. Der Vektor ist
**ortsfrei** — er trägt Richtung und Länge ohne Stelle. Dieselbe
Pfeil-Form am Werkplan kann je nach Lesart entweder eine Strecke
(Sparrenkante, Anriss, Maßlinie) oder einen Vektor (parallel
verschiebbare Verschiebungs-Information) bezeichnen. Faustregel:
wo zwei Endpunkte fest am Bauteil sitzen, ist es Strecke; wo der
Pfeil ohne Bedeutungsverlust parallel verschoben werden darf, ist er
Vektor.

**Punkt.** Ein Punkt benennt eine **Lage** im Raum (drei
Koordinaten); ein Vektor benennt eine **Verschiebung** (drei
Komponenten ohne Stelle). Die zulässigen Mischoperationen sind
„Punkt + Vektor → Punkt" (Verschiebung trägt einen Punkt zu einem
anderen) und „Punkt − Punkt → Vektor" (die Differenz zweier
Lagen ist eine ortsfreie Verschiebung). „Vektor + Vektor → Vektor"
ist erlaubt; „Punkt + Punkt" ist es nicht.

**Pfeil.** Der Pfeil ist die **Darstellungsform** des Vektors auf
dem Papier oder am Bildschirm, nicht der Vektor selbst. Alle Pfeile
gleicher Länge, gleicher Richtung und gleicher Orientierung
repräsentieren **denselben** Vektor — ein Vektor ist die
Äquivalenzklasse paralleler, gleich langer, gleich orientierter
Pfeile. Genau das zeigt die gestrichelte Geist-Kopie in der
Eröffnungs-Skizze. Das Hauptglossar führt „Pfeil" deshalb als
abgelehnte Benennung für den Vektor.

**Tupel / Koordinaten.** Das geordnete Zahlentripel (v_x, v_y, v_z)
ist die **Zahlendarstellung** eines Vektors **bezüglich einer
Basis**. Wechselt die Basis — etwa von den Welt-Koordinaten zu
einem lokalen, an der Sparrenachse orientierten Bauteilkoordinaten-
system —, ändern sich die Zahlen, der Vektor bleibt derselbe.
Dieselbe Trennung wie bei Pfeil und Vektor, eine Schicht höher:
die Zahlen sind eine Repräsentation, nicht der Vektor selbst.

**Kraft.** Eine Kraft ist Vektor **plus physikalische Einheit
Newton** (oder Kilonewton) **plus Wirkungslinie bzw. Angriffspunkt**.
Der nackte Vektor des Hauptglossars trägt Längen-Komponenten (mm) im
Differenz-Kontext oder ist dimensionslos im Einheitsvektor-Kontext —
keine Kraft-Einheit. Im Alltag fallen die beiden Begriffe oft
zusammen („Kräfte sind Vektoren"), fachlich liegt eine Einheits- und
Anwendungs-Schicht dazwischen.

## Falsche Freunde aus dem Holzbau-Korpus

Drei Komposita oder Stichworte tauchen in Briefings und Werk-Korpora
auf, in denen man sie zunächst dem Vektor zuordnen möchte — die
genauere fachliche Lesart läuft aber an anderer Stelle des
Hauptglossars.

**„Falllinie".** Die Falllinie auf einer geneigten Dachfläche ist die
Richtung des grössten Gefälles — die Richtung, in die das Wasser
abläuft. Sie trägt im Namen das Wort „Linie", ist aber geometrisch
**weder Strecke noch Vektor im engeren Sinn**, sondern ein
**Einheitsvektor** (Vektor mit Länge 1) in der Dachebene. Das
Hauptglossar führt sie unter `oberbegriff: einheitsvektor`. Die
Falllinie ist also eine reine **Richtungsangabe** mit Norm 1 — und
gehört didaktisch zum Einheitsvektor-Eintrag, nicht in den
allgemeinen Vektor-Eintrag.

**„Schwerkraft-Vektor".** Die welt-vertikale Wirkung der Schwerkraft
auf ein Bauteil wird im Volksmund gern „Schwerkraft-Vektor" genannt.
Fachlich ist sie ein **Kraftvektor** in der welt-vertikalen Richtung,
mit Einheit Newton (Eigengewicht × Erdbeschleunigung) und der
Wirkungslinie längs des Senkels — nicht ein nackter Vektor im Sinne
des Hauptglossars. Im Werkstatt-Korpus heißt die Sache schlicht
**„Eigengewicht"** oder **„Schwerkraft"**; das Kompositum
„Schwerkraft-Vektor" ist eine Schul-Mathematik-Übertragung, kein
Zimmermanns-Wort.

**„Versatz-Vektor am Werkplan".** Das Differenz-Maß zwischen zwei
Werkplan-Punkten — etwa „Bauachsen-Abstand 4'250 mm" oder
„Pfettenhöhe ab Bodenplatte 3'120 mm" — ist mathematisch der
**Betrag** eines Vektors (Punkt minus Punkt liefert einen Vektor),
und die Bemaßungs-Linie steht für seine Richtung. Im
Werkstatt-Gespräch wird das aber **nie** so gesagt; man sagt schlicht
**„Maß"** oder **„Differenz"**. „Versatz-Vektor" als Korpus-Begriff
am Werkplan ist nicht zimmermannssprachlich verfestigt — er bleibt
eine didaktische Brücke zwischen Werkplan und CAD-Datenmodell.

## Verweise

Diese Subglossar-Datei stützt sich auf die folgenden Hauptglossar-
Begriffe; bei Detailfragen ist dort die normative Definition zu
finden:

- `hauptglossar/00_ressourcen/hg_vektor.md` — das normative
  Hauptglossar zum Vektor, mit mathematischer Definition als Element
  des Vektorraums ℝ³, Wohldefiniertheit, Implementierungshinweis und
  Quellenliste.
- `hauptglossar/00_ressourcen/hg_punkt.md` — die ortsgebundene
  Schwester-Figur: Lage ohne Richtung. „Punkt + Vektor → Punkt" und
  „Punkt − Punkt → Vektor" sind die zulässigen Mischoperationen.
- `hauptglossar/00_ressourcen/hg_strecke.md` — der ortsgebundene
  Geschwister-Begriff: konkrete Verbindung zweier Punkte am Bauteil.
  Ein Vektor ist die ortsfreie Differenz dieser zwei Punkte.
- `hauptglossar/00_ressourcen/hg_einheitsvektor.md` — der Vektor mit
  Länge 1; reine Richtungs-Information. Faserrichtung, Falllinie und
  Dachflächen-Normale sind Einheitsvektoren.
- `hauptglossar/00_ressourcen/hg_falllinie.md` — der gleichnamige
  „Linien"-Begriff, der trotz Wortbestandteil **kein** allgemeiner
  Vektor ist, sondern ein Einheitsvektor in der Dachebene.
- `hauptglossar/00_ressourcen/hg_koordinatensystem.md` — das
  Bezugssystem, in dem die Komponenten eines Vektors als Zahlentripel
  dargestellt werden; bei Basiswechsel ändern sich die Zahlen, der
  Vektor bleibt derselbe.
- `hauptglossar/00_ressourcen/hg_ebene.md` — Trägerbegriff der
  Dachfläche; die rechtwinklig auf der Ebene stehende Richtung ist
  der Normalenvektor.

Verwandte Subglossar-Einträge (Folgearbeit): `sg_einheitsvektor`,
`sg_faserrichtung`, `sg_kraftvektor`, `sg_wirkungslinie`.
