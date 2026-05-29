---
id: sg_gerade
benennung: Gerade
glossar_ref: gerade
cluster: ressourcen
subglossar_pendant: notwendig
status: entwurf
---

# Gerade (Subglossar)

Brücke vom normativen Hauptglossar (`hauptglossar/00_ressourcen/hg_gerade.md`) zu
den stufenweisen Theorie-Inhalten. Hier liegt die didaktische
Aufbereitung: berufssprachliche Verankerung über die Rollen, in
denen Geraden im Holzbau tatsächlich auftreten, Pflicht-Skizze der
Schnittgerade zweier Dachflächen am Walmgrat, Negativ-Abgrenzung
zu Strecke, Halbgerade, Achse und „Linie" sowie die etymologische
Brücke vom Adjektiv „gerade" zur substantivierten „Geraden" des
18. Jahrhunderts.

---

## Was die Gerade im Holzbau ist

Eine **Gerade** ist eine beidseitig unbegrenzte, eindimensionale
Punktmenge im Raum — die gedachte zweiseitige Verlängerung jeder
Strecke ohne Anfang und Ende. Im DACH-Holzbau-Korpus tritt sie fast
nie als nacktes Substantiv auf; der Zimmermann redet nicht von „der
Geraden", sondern von **Sparrenachse**, **Pfettenachse**, **Grat**,
**Kehle**, **First**, **Wirkungslinie** oder **Anriss** — alles
Rollen-Komposita, in denen das Geraden-Konzept stillschweigend mitläuft.
Dieselbe Beobachtung wie beim Punkt: die Gerade lebt im Holzbau **als
Gerade von etwas**.

Das Wort selbst ist eine **Substantivierung** des Adjektivs „gerade".
Die ältere Phrase **„gerade Linie"** wurde nach DWDS seit Anfang des
18. Jahrhunderts in der Geometrie zur **„Geraden"** verkürzt — die
nackte „Gerade" ist also ein **mathematischer Importbegriff**, kein
zimmermannssprachlich gewachsener. Das erklärt, warum der Werkplan
fast immer das Kompositum trägt, nicht das nackte Wort.

## Geraden im Werkstatt- und Tragwerksbild

Die folgende kleine Eröffnungs-Skizze (Sparren im Profil) zeigt die
Begriffsbrücke vom Strecke-Anriss am Bauteil zur gedanklichen
Geraden-Verlängerung: der **Anriss** ist als kurze rote Strecke auf
der Sparrenoberseite markiert, beidseitig gepunktet weitergeführt
über die Sparrenränder hinaus — die **Trägergerade**, an der das
Anrissmaß hängt.

<svg viewBox="0 0 700 220" xmlns="http://www.w3.org/2000/svg" font-family="sans-serif" font-size="13">
  <rect width="100%" height="100%" fill="#f4f1ea"/>
  <!--
  ====================================================================
  SVG-DOKUMENTATION: sg_gerade F.1 — Anriss-Strecke mit Geraden-
  Verlaengerung am Sparren-Profil
  ====================================================================
  ZWECK
    Sparren im Profil (28 Grad Neigung, analog sg_kerve), darauf eine
    konkrete Anriss-Strecke (rot, durchgezogen) quer ueber die Sparren-
    Oberseite, beidseitig gepunktet weitergefuehrt ueber die Sparren-
    raender hinaus als "Traegergerade". Begriffsbruecke
    Strecke <-> Gerade.
  STIL-KONVENTIONEN (Pilot sg_punkt / sg_kerve)
    #f5e6c8 Sparren-Fuellung, #6a4c2a Holz-Umriss
    #c0392b Anriss-Strecke (durchgezogen, rot, stroke-width 2.5)
    #c0392b Geraden-Verlaengerung beidseitig (gestrichelt fein, stroke-
            dasharray 2 4, stroke-width 1.5)
    #2c3e50 Welt-Pfeile, Endpunkt-Marker
    #666    Bezeichner-Schrift italic-klein
  GEOMETRIE
    Sparrenachse von links unten (90,180) nach rechts oben (610,40),
    Neigung ca. 15 Grad (flach, damit die Anriss-Strecke perpendikular
    zur Sparrenachse als deutliche Quer-Strecke sichtbar bleibt).
    Sparrenhoehe perpendikular zur Achse: 36 px.
    Oberkante  (90,180-h) bis (610,40-h), h berechnet aus Neigung
    Anriss-Strecke perpendikular zur Sparrenachse bei x=300 (Sparren-
    mitte), beidseitig 18 px ueber die Sparrenkanten hinausgesetzt
    als gepunktete Verlaengerung.
  KRITISCHE FALLEN
    KEINE Leerzeilen im SVG-Block (CommonMark HTML Type 6).
  ====================================================================
  -->
  <!-- Sparren-Polygon: flache Neigung ca. 15 Grad, Achse von (90,160)
       nach (610,76). Hoehe perpendikular zur Achse = 36 px.
       Perpendikularer Versatz: dx=-sin(15)*36, dy=cos(15)*36 fuer
       Unterkante, entgegengesetzt fuer Oberkante.
       Vereinfachte Variante: Sparren als Parallelogramm mit
       vertikalen Endkanten — Aufgabe ist Anriss-Demonstration, nicht
       Stirnform.
       Ecken: (90,180), (90,144), (610,60), (610,96). -->
  <polygon points="90,180 90,144 610,60 610,96" fill="#f5e6c8" stroke="#6a4c2a" stroke-width="1.5"/>
  <!-- Sparrenachse als duenne Mittellinie (graustichig, dasharray fein) -->
  <line x1="90" y1="162" x2="610" y2="78" stroke="#999" stroke-width="0.8" stroke-dasharray="3 3"/>
  <text x="615" y="82" font-size="11" font-style="italic" fill="#666">Sparrenachse</text>
  <!-- Anriss-Strecke perpendikular zur Sparrenachse bei x=300 (Mitte).
       Sparrenachse-Tangente: dx=520, dy=-84; Normale: dx=84, dy=520
       (nach unten-rechts) oder (-84, -520) (nach oben-links).
       Mittelpunkt auf Achse bei (300, ca. 113.5).
       Normale auf Laenge 18 px (halbe Sparrenhoehe = 18) skaliert:
       Normalenlaenge sqrt(84^2+520^2)=526.7, Skalierungsfaktor 18/526.7
       =0.0342. Versatz: dx_n=2.87, dy_n=17.77.
       Anriss-Endpunkte:
         Oberkante: (300-2.87, 113.5-17.77) = (297.1, 95.7)
         Unterkante: (300+2.87, 113.5+17.77) = (302.9, 131.3)
       Verlaengerung zusaetzlich um Faktor 1.5 (= 27 px) auf beiden
       Seiten:
         Gerade-Endpunkt oben: (297.1-2.87*1.5, 95.7-17.77*1.5)
                              = (292.8, 69.05)
         Gerade-Endpunkt unten: (302.9+2.87*1.5, 131.3+17.77*1.5)
                              = (307.2, 157.95) -->
  <!-- Gepunktete Verlaengerung oberhalb der Sparrenoberkante (Gerade) -->
  <line x1="297.1" y1="95.7" x2="292.8" y2="69" stroke="#c0392b" stroke-width="1.5" stroke-dasharray="2 4"/>
  <!-- Anriss-Strecke selbst (durchgezogen) -->
  <line x1="297.1" y1="95.7" x2="302.9" y2="131.3" stroke="#c0392b" stroke-width="2.5"/>
  <!-- Gepunktete Verlaengerung unterhalb der Sparrenunterkante (Gerade) -->
  <line x1="302.9" y1="131.3" x2="307.2" y2="158" stroke="#c0392b" stroke-width="1.5" stroke-dasharray="2 4"/>
  <!-- Bezeichner Anriss-Strecke -->
  <text x="270" y="115" text-anchor="end" fill="#c0392b" font-weight="bold">Anriss</text>
  <text x="270" y="129" text-anchor="end" font-size="11" font-style="italic" fill="#666">(Strecke am Bauteil)</text>
  <!-- Bezeichner Gerade (Verlaengerung) — am oberen Ende -->
  <text x="310" y="60" fill="#c0392b" font-weight="bold">Trägergerade</text>
  <text x="310" y="74" font-size="11" font-style="italic" fill="#666">(gedankliche Verlängerung)</text>
  <!-- Welt-Koordinaten-Hilfsdarstellung unten rechts -->
  <g transform="translate(630, 195)">
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

Die kräftige rote Strecke ist das, was am Bauteil tatsächlich
materialisiert ist — Bleistift- oder Reissnadelspur über die
Sparrenbreite. Die beidseitig gepunktete Fortsetzung ist die zugehörige
**Trägergerade**: unbegrenzt nach oben und nach unten, ohne Anfang
und Ende. Wo der Meister sagt, „die Anrisslinie geht über den Sparren
hinaus weiter" — etwa beim Schiften, wenn die gedachte Verlängerung
über das Sparrenende ins Nichts hinein einen Schnittpunkt mit der
Trauflinien-Geraden trifft — meint er genau diese Trägergerade.

## Geraden-Rollen im Holzbau — Pflicht-Skizze

Die zentrale Geraden-Anwendung im Dach ist die **Schnittgerade**
zweier Dachflächen. Sie materialisiert sich als Bauteil — als
**Grat**, **Kehle** oder **First** —, ist geometrisch aber die
Trägergerade einer beidseitig unbegrenzten Schnittlinie zweier
Ebenen. Die folgende Skizze zeigt einen Walmdach-Eckraum mit zwei
geneigten Dachflächen, deren Schnittgerade als **Walmgrat**
hervorgehoben ist, beidseitig gepunktet als unbegrenzter Träger
über die Dachflächen hinaus fortgesetzt.

<svg viewBox="0 0 720 480" xmlns="http://www.w3.org/2000/svg" role="img" font-family="sans-serif" font-size="13">
  <title>Walmgrat als Schnittgerade zweier Dachflächen am Walmdach-Eckraum</title>
  <desc>Axonometrischer Schrägriss eines Walmdach-Eckraums. Eine
        Hauptdachfläche und eine Walmfläche treffen sich am Walmgrat,
        der als rote durchgezogene Strecke zwischen P_T (Trauf-Walmecke)
        und P_F (First-Walmecke) hervorgehoben ist und beidseitig durch
        gepunktete Verlängerungen über die Bauteil-Enden hinaus als
        unbegrenzte Trägergerade fortgesetzt wird.</desc>
  <rect width="100%" height="100%" fill="#f4f1ea"/>
  <!--
  ====================================================================
  SVG-DOKUMENTATION: sg_gerade F.2 — Schnittgerade zweier Dachflächen
                     als Walmgrat (Pflicht-Skizze)
  ====================================================================
  ZWECK
    Pflicht-Skizze zur Schnittgeraden. Am Walmdach-Eckraum treffen
    sich zwei Dachflächen am Walmgrat. Der begriffliche Unterschied
    zwischen Strecke und Gerade ist sichtbar gemacht:
      - der WALMGRAT ist eine endliche STRECKE zwischen P_T und P_F,
        rote durchgezogene Linie (stroke-width 3.5);
      - beidseitig läuft die TRÄGERGERADE als gepunktete Verlängerung
        über die Bauteil-Endpunkte hinaus weiter (stroke-width 2,
        dasharray 3 5).
    Schwester: sg_ebene G.1 verwendet dieselbe Walmdach-Form und
    denselben Eckpunkt-Satz, hebt dort aber die schneidenden Ebenen
    hervor statt die Schnittgerade. Beide Skizzen direkt vergleichbar.
  PATTERN-NUTZUNG (SG_KONVENTIONEN.md §6)
    - Pattern 1 Skizzen-Karton-Hintergrund (Position 3 nach <title>
      und <desc>).
    - Pattern 2 Welt-Pfeile-Inset (translate(640, 450)).
    - Pattern 5 Geraden-Verlängerung (beidseitig 80 px, gepunktet).
    - Pattern 6 Standard-Walmdach (Eckpunkte und Beschriftungs-Slots
      verbindlich).
  STIL-KONVENTIONEN (Farben gemäss §6 Farbpalette)
    Karton                #f4f1ea  Hintergrund-Rechteck
    Hauptdach-Füllung     #e8c98a  hell-warmer Holz-Hue
    Walmfläche-Füllung    #c89a5a  dunkler-warmer Holz-Hue
                                   (Tiefenkontrast)
    Holz-Umriss           #6a4c2a  Polygon-Stroke aller Dachflächen
    Akzent-Rot            #c0392b  Walmgrat, Punkt-Marker, Bold-Label
    Anthrazit             #2c3e50  Welt-Pfeile, Punkt-Stroke
    Mittelgrau            #666     italic-Klarstellungen, Hinweise
    Schrift-Hierarchie:
      13 bold              identifizierende Begriffe (Walmgrat, P_T)
      13 italic            sekundäre Begriffe (Hauptdachfläche)
      11 italic + #666     Klarstellungen, Rollen, Trauf-Hinweise
  GEOMETRIE — Standard-Walmdach-Eckpunkte (Pattern 6)
    Hauptdach-Trapez     : (40,380) (260,380) (370,170) (170,170)
    Walmfläche-Dreieck   : (260,380) (460,360) (370,170)
    Polygon-Reihenfolge: Hauptdach zuerst, Walmfläche darüber. Die
    Walmgrat-<line> wird nach beiden Polygonen gezeichnet, damit die
    rote Hervorhebung sichtbar oben liegt.
    Markante Punkte:
      P_T = (260, 380)  Trauf-Walmecke vorn         — Walmgrat unten
      P_F = (370, 170)  First-Walmecke              — Walmgrat oben
      P_R = (170, 170)  First-Innenecke links       — First-Ende
      P_W = (460, 360)  Walm-Trauf-Außenecke        — kein Label
    Walmgrat-Strecke P_T → P_F:
      Richtungsvektor (110, -210), Länge sqrt(110² + 210²) ≈ 237.08
      Einheitsvektor (0.4640, -0.8857)
    Verlängerungen (Pattern 5, beidseitig 80 px):
      unten = P_T − 80·Unit ≈ (222, 451)
      oben  = P_F + 80·Unit ≈ (407,  99)
  BESCHRIFTUNGS-SLOTS und Reserven
    Pro Label: Position, Anchor, Bounding-Box (Approximation
    chars·0.6·font-size), Reserve zu Nachbar-Geometrie.
    Flächen-Labels (italic 13, fill #6a4c2a):
      Hauptdachfläche   (200, 240) middle, Bereich 145.5 – 254.5
                        Im oberen Drittel des Hauptdach-Trapezes,
                        19 px Reserve zur linken Walmgrat-Kante,
                        79 px zum Walmgrat-Schnitt rechts.
      Walmfläche        (363, 303) middle, Bereich 322 – 404
                        Im Walmflächen-Schwerpunkt, 22 px Reserve
                        zur Walmgrat-Linie links, 31 px zur
                        Walmflächen-Rückseite rechts.
    Walmgrat-Beschriftung (Standard-Slot Pattern 6, anchor=end):
      "Walmgrat"            (303, 268) end, bold 13 #c0392b
                            Bereich 241 – 303. Grat-Strich-x bei
                            y=268 ist 318.7 → 15.7 px Reserve.
      "(Bauteil = Strecke)" (303, 282) end, italic 11 #666
                            Bereich 178 – 303. Klarstellung: das
                            Bauteil ist eine Strecke, die
                            Schnittgerade die Verlängerung.
    Punkt-Marker und Label (circle r=4 fill #c0392b stroke #2c3e50;
    Label bold 13 #c0392b; Rolle italic 11 #666):
      P_T-Marker        circle bei (260, 380)
      P_T-Label         (252, 372) end   "P_T"
      P_T-Rolle         (252, 358) end   "Trauf-Walmecke"
                        Oberhalb des Markers ins Hauptdach-Inneres,
                        klar getrennt von der gepunkteten
                        Verlängerung und ihrem Hinweis-Text unten.
      P_F-Marker        circle bei (370, 170)
      P_F-Label         (378, 166) start "P_F"
      P_F-Rolle         (378, 180) start "First-Walmecke"
                        Nach rechts-oben in den Luftraum, ausserhalb
                        der Dach-Polygone.
      P_R-Marker        circle bei (170, 170)
      P_R-Label         (162, 166) end   "P_R"
      P_R-Rolle         (162, 180) end   "First-Innenecke"
                        Symmetrisch zu P_F, nach links-oben.
    Trauflinien-Hinweise (italic 11 #666):
      Hauptdach-Trauf   (70, 396) start, Bereich 70 – 189
                        16 px unterhalb der Trauflinie y=380,
                        40 px Reserve zum P_T-Label-Cluster rechts.
      Walm-Trauf        (360, 380) start, rotate(-6 360 380)
                        Walm-Trauf-Linie (260,380)→(460,360) hat
                        Steigung -0.1, also ca. -6°. Drehung um den
                        Ankerpunkt für parallelen Lauf zur Linie.
    First-Andeutung (italic 11 #666):
      "First"           (270, 158) middle, Bereich 247 – 293
                        Oberhalb y=170. Keine separate Hilfslinie —
                        die Polygon-Oberkanten bilden den First
                        implizit.
    Verlängerungs-Hinweise (italic 11 #c0392b):
      Hinweis unten     (212, 470) end, Bereich 116 – 212, y=470
      Hinweis oben      (418, 93) start, Bereich 418 – 524, y=93
                        Beide knapp neben den Linien-Endpunkten der
                        Verlängerung.
    Globale Titel-Zeile (italic 13/11, oben zentriert):
      Zeile 1           (360, 40) middle, font-size 13
      Zeile 2           (360, 56) middle, font-size 11, #666
    Welt-Pfeile-Inset (Pattern 2):
      g translate(640, 450) — e_hat_h-Text endet global bei x ≈ 700,
      20 px Reserve zum viewBox-Rand 720.
  KONFLIKT-MATRIX
    Alle Text-Cluster sind vertikal mindestens 24 px voneinander
    getrennt oder horizontal in unterschiedlichen Regionen.
    Vertikale Cluster-Reihen:
       y=40-56    Titel-Zeile (zentriert oben)
       y=93       Verlängerungs-Hinweis oben
       y=158      First-Beschriftung
       y=166-180  P_F-Cluster (rechts) + P_R-Cluster (links)
       y=240      Hauptdachfläche-Label
       y=268-282  Walmgrat-Cluster (anchor=end, x bis 303)
       y=303      Walmflächen-Label
       y=358-372  P_T-Cluster (anchor=end, oberhalb des Markers)
       y=380-396  Trauf-Hinweise und Marker-y-Linie
       y=450      Welt-Inset
       y=470      Verlängerungs-Hinweis unten
  KRITISCHE FALLEN
    (1) Keine Leerzeilen innerhalb des <svg>...</svg>-Blocks.
        CommonMark beendet HTML-Blöcke vom Typ 6 bei der ersten
        leeren Zeile.
    (2) Öffnungstag <svg ...> auf einer einzigen Zeile. Mehrzeilig
        umbrochene Attribute brechen das HTML-Block-Rendering in
        manchen Markdown-Renderern ab.
    (3) Standard-Walmdach-Eckpunkte (Pattern 6) sind verbindlich.
        Verschiebung würde die Pattern-Wiederverwendbarkeit
        zerstören.
  ====================================================================
  -->
  <!-- ============ DACHFLÄCHEN (Standard-Walmdach) ============ -->
  <!-- Hauptdachfläche (Trapez, hell-warmer Holz-Hue) — zuerst, damit
       Walmfläche oben aufliegt -->
  <polygon points="40,380 260,380 370,170 170,170"
           fill="#e8c98a" stroke="#6a4c2a" stroke-width="1.5"/>
  <!-- Walmfläche vorn (Dreieck, dunkler-warmer Tiefenkontrast) -->
  <polygon points="260,380 460,360 370,170"
           fill="#c89a5a" stroke="#6a4c2a" stroke-width="1.5"/>
  <!-- ============ FIRST (sekundär, nur Andeutung mit Beschriftung) ============ -->
  <!-- First (P_R → P_F) als Hilfslinie sichtbar, italic-Beschriftung -->
  <text x="270" y="158" text-anchor="middle" font-size="11" font-style="italic" fill="#666">First</text>
  <!-- ============ TRAUFLINIEN-HINWEISE (klein, italic) ============ -->
  <text x="70" y="396" font-size="11" font-style="italic" fill="#666">Traufe (Hauptdach)</text>
  <text x="360" y="380" font-size="11" font-style="italic" fill="#666" transform="rotate(-6 360 380)">Traufe (Walm)</text>
  <!-- ============ FLÄCHEN-BESCHRIFTUNG (Standard-Slots) ============ -->
  <text x="200" y="240" text-anchor="middle" font-style="italic" fill="#6a4c2a">Hauptdachfläche</text>
  <text x="363" y="303" text-anchor="middle" font-style="italic" fill="#6a4c2a">Walmfläche</text>
  <!-- ============ WALMGRAT (Schnittgerade — Pflicht-Hervorhebung) ============ -->
  <!-- Verlängerung UNTEN (über P_T hinaus ins Bodenniveau hinein) -->
  <line x1="222" y1="451" x2="260" y2="380"
        stroke="#c0392b" stroke-width="2" stroke-dasharray="3 5"/>
  <!-- Walmgrat-Strecke am Bauteil P_T → P_F (durchgezogen, dick) -->
  <line x1="260" y1="380" x2="370" y2="170"
        stroke="#c0392b" stroke-width="3.5"/>
  <!-- Verlängerung OBEN (über P_F hinaus in die Luft) -->
  <line x1="370" y1="170" x2="407" y2="99"
        stroke="#c0392b" stroke-width="2" stroke-dasharray="3 5"/>
  <!-- ============ MARKANTE PUNKTE (P_T, P_F, P_R) ============ -->
  <!-- P_T = Trauf-Walmecke vorn. Label oberhalb des Markers im
       Hauptdach-Inneres, getrennt von der gepunkteten Verlängerung
       und ihrem Hinweis-Text unten. -->
  <circle cx="260" cy="380" r="4" fill="#c0392b" stroke="#2c3e50" stroke-width="1"/>
  <text x="252" y="372" text-anchor="end" fill="#c0392b" font-weight="bold">P_T</text>
  <text x="252" y="358" text-anchor="end" font-size="11" font-style="italic" fill="#666">Trauf-Walmecke</text>
  <!-- P_F = First-Walmecke -->
  <circle cx="370" cy="170" r="4" fill="#c0392b" stroke="#2c3e50" stroke-width="1"/>
  <text x="378" y="166" fill="#c0392b" font-weight="bold">P_F</text>
  <text x="378" y="180" font-size="11" font-style="italic" fill="#666">First-Walmecke</text>
  <!-- P_R = First-Innenecke links -->
  <circle cx="170" cy="170" r="4" fill="#c0392b" stroke="#2c3e50" stroke-width="1"/>
  <text x="162" y="166" text-anchor="end" fill="#c0392b" font-weight="bold">P_R</text>
  <text x="162" y="180" text-anchor="end" font-size="11" font-style="italic" fill="#666">First-Innenecke</text>
  <!-- ============ WALMGRAT-BESCHRIFTUNG (Standard-Slot Pattern 6, anchor=end) ============ -->
  <text x="303" y="268" text-anchor="end" fill="#c0392b" font-weight="bold">Walmgrat</text>
  <text x="303" y="282" text-anchor="end" font-size="11" font-style="italic" fill="#666">(Bauteil = Strecke)</text>
  <!-- ============ VERLÄNGERUNGS-HINWEISE ============ -->
  <text x="212" y="470" text-anchor="end" fill="#c0392b" font-size="11" font-style="italic">Verlängerung (Gerade)</text>
  <text x="418" y="93" fill="#c0392b" font-size="11" font-style="italic">Verlängerung (Gerade)</text>
  <!-- ============ GLOBALE TITEL-ZEILE OBEN ============ -->
  <text x="360" y="40" text-anchor="middle" font-style="italic" font-size="13">Walmgrat als Schnittgerade zweier Dachflächen</text>
  <text x="360" y="56" text-anchor="middle" font-size="11" font-style="italic" fill="#666">Bauteil ist ein endliches Stück; die Trägergerade läuft beidseitig unbegrenzt weiter</text>
  <!-- ============ WELT-PFEILE-INSET (Pattern 2) ============ -->
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

Die rote durchgezogene Strecke zwischen **G_1** (Trauf-Walmecke) und
**G_2** (First-Walmecke) ist der **Walmgrat** als Bauteil — ein
endlich langes Stück Holz, das der Zimmermann zuschneidet und
einbaut. Die beidseitig gepunktete Fortsetzung ist die
**Schnittgerade** der beiden Dachebenen: unbegrenzt nach unten ins
Bodenniveau und unbegrenzt nach oben in die Luft hinein. Der Grat
selbst ist nur ein Ausschnitt dieser Geraden.

Dasselbe Verhältnis gilt für **Kehle** (Schnittgerade zweier
gegeneinander geneigter Dachflächen mit konkaver Knickkante) und
**First** (Schnittgerade zweier zueinander gegenüberliegender
Dachflächen am höchsten Punkt): in allen drei Fällen ist das Bauteil
eine Strecke, die zugrunde liegende Schnittlinie der Dachebenen eine
Gerade.

## Wo Geraden auftreten — drei Rollen

Im Holzbau-Korpus lassen sich drei klar trennbare Rollen unterscheiden,
in denen die Gerade tatsächlich vorkommt. Sie sind keine geometrischen
Subtypen — eine Gerade ist eine Gerade —, sondern unterschiedliche
**Funktionen** im Werk- oder Tragwerksplan.

| Rolle | Wo sie auftritt | Verhältnis zum Bauteil |
|---|---|---|
| **Trägergerade einer Achse** | Sparrenachse, Pfettenachse, Stuhlsäulenachse — die Bauteilhauptachse eines Stab-Bauteils | Das Bauteil selbst ist eine **Strecke** zwischen den Bauteil-Enden; ihre beidseitig unbegrenzte Verlängerung ist die Trägergerade. Wird bei der Schiftung gebraucht, wo Trauflinien-Gerade und Sparrenachsen-Gerade ihren Schnittpunkt am Sparrenfuss bekommen. |
| **Wirkungslinie einer Kraft** | Statik — Linie, längs derer eine Kraft am starren Körper wirkt | **Einziger Korpus-Begriff mit expliziter Geraden-Definition.** Die Statik nutzt die Linienflüchtigkeit der Kraft am starren Körper: eine Kraft darf entlang ihrer Wirkungslinie verschoben werden, ohne dass sich ihre Wirkung am Tragwerk ändert. Damit ist die Wirkungslinie geometrisch eine Gerade, nicht eine Strecke. |
| **Schnittgerade zweier Ebenen** | Grat-, Kehl- und Firstlinie als Schnitt benachbarter Dachflächen | Das Bauteil (Gratsparren, Kehlsparren, Firstpfette) ist die Strecke; die geometrische Schnittgerade läuft beidseitig unbegrenzt über die Bauteil-Enden hinaus. In der Dachausmittlung wird diese Geraden-Eigenschaft ausgenutzt, um Schmiegen und Anschlusswinkel an der Walmecke konstruktiv zu finden. |

Die drei Rollen teilen sich ein gemeinsames Muster: am Bauteil
materialisiert eine endliche Strecke, in der Konstruktion lebt die
unbegrenzte Trägergerade als gedanklicher Verlängerer. Wo der
Werkplan misst und der Sägeschnitt liegt, ist es Strecke; wo
geschnitten, geschiftet oder verlängert wird, wird sie zur Geraden
gedacht.

## Was eine Gerade nicht ist — Strecke, Halbgerade, Achse, Linie

Vier Begriffe stehen im Holzbau in unmittelbarer Nähe zur Geraden
und werden gern mit ihr verwechselt. Die Abgrenzung ist didaktisch
wichtig, weil sie zugleich die Werkstatt-Wirklichkeit von der
geometrischen Idealisierung trennt.

**Strecke.** Im realen Bauteil ist eine Sparrenachse, eine Anrisslinie
oder ein Grat **immer eine Strecke** — endlich, mit zwei Endpunkten.
Die Gerade ist die zweiseitige Verlängerung. Zu jeder Strecke gibt es
genau eine Trägergerade; auf einer Geraden liegen dagegen unendlich
viele Strecken. Praxis-Faustregel: wo am Bauteil gemessen, gezeichnet
oder gesägt wird, ist es Strecke. Wo über das Bauteil hinaus verlängert,
projiziert oder geschnitten wird, wird sie zur Geraden gedacht.

**Halbgerade.** Eine Halbgerade ist einseitig begrenzt — sie hat einen
Anfangspunkt, läuft aber nur in eine Richtung unbegrenzt weiter. Im
Holzbau ist sie didaktisch fast bedeutungslos; das einzige konstruierte
Beispiel ist die gerichtete Wirkungslinie einer einseitig wirkenden
Last, und auch dort wird in der Praxis mit der Geraden plus separatem
Vorzeichen gearbeitet. Ein Satz reicht zur Abgrenzung: Gerade
beidseitig unbegrenzt, Halbgerade einseitig.

**Achse.** Eine Achse ist im Holzbau eine **Gerade mit Rolle** —
Sparrenachse, Bauachse, Symmetrieachse, Drehachse, Bezugsachse. Die
Achse ist also kein Synonym für Gerade, sondern eine **Spezialisierung**:
jede Achse ist eine Gerade in einer bestimmten konstruktiven
Funktion, aber nicht jede Gerade ist eine Achse. Wenn der Korpus
„Sparrenachse" sagt, meint er die Bauteilhauptachse — geometrisch
die Trägergerade der Sparren-Strecke, mit der Rolle
„Bauteilhauptachse" annotiert.

**„Linie".** Das Wort „Linie" ist im DACH-Korpus das Allerwelts-Wort,
das alles abdeckt von Strecke (Trauflinie, Anrisslinie) über Kurve
(Wölbung einer Sparrendecke) bis Gerade (Wirkungslinie,
Schnittlinie). Wegen dieser Mehrdeutigkeit ist „Linie" als nackter
Begriff für die Gerade ungeeignet. Zwei besonders trügerische
Komposita lohnen den Hinweis: die **Falllinie** trägt das Wort „Linie"
im Namen, ist geometrisch aber **ein Einheitsvektor** (die Richtung
des größten Gefälles in einer geneigten Ebene) und nicht eine Gerade
im Sinne dieses Eintrags. Die **Höhenlinie auf einer Dachfläche** ist
im Korpus die Schnittlinie der Dachfläche mit einer horizontalen
Hilfsebene — am Bauteil eine Strecke, geometrisch trägt sie eine
Gerade, der Begriff selbst meint aber das Schnittobjekt, nicht die
Trägergerade.

## Verweise

Diese Subglossar-Datei stützt sich auf die folgenden Hauptglossar-
Begriffe; bei Detailfragen ist dort die normative Definition zu
finden:

- `hauptglossar/00_ressourcen/hg_gerade.md` — das normative Hauptglossar zur
  Geraden, mit mathematischer Definition als eindimensionaler
  affiner Unterraum, Wohldefiniertheit, Implementierungshinweis
  und Quellenliste.
- `hauptglossar/00_ressourcen/hg_strecke.md` — der endliche Ausschnitt einer
  Geraden mit zwei Endpunkten; die im Bauteil tatsächlich
  materialisierte Form.
- `hauptglossar/00_ressourcen/hg_halbgerade.md` — der einseitig begrenzte
  Ausschnitt; im Holzbau am Rand didaktisch.
- `hauptglossar/00_ressourcen/hg_achse.md` — die Gerade mit Rolle; spezialisierte
  Verwendung als Bauteil-, Symmetrie-, Bezugsachse.
- `hauptglossar/00_ressourcen/hg_schnittgerade.md` — die Schnittgerade zweier
  Ebenen, geometrische Grundlage von Grat, Kehle und First.
- `hauptglossar/00_ressourcen/hg_bauteilachse.md` — die Bauteilhauptachse als
  konstruktive Spezialisierung der Achse.
- `hauptglossar/00_ressourcen/hg_falllinie.md` — der gleichnamige „Linien"-Begriff,
  der trotz Wortbestandteil **keine** Gerade ist, sondern ein
  Einheitsvektor.
- `hauptglossar/00_ressourcen/hg_punkt.md`, `hauptglossar/00_ressourcen/hg_vektor.md` — die
  begrifflichen Voraussetzungen der Geraden.

Verwandte Subglossar-Einträge (Folgearbeit): `sg_strecke`,
`sg_achse`, `sg_schnittgerade`, `sg_wirkungslinie`.
