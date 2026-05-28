---
id: sg_punkt
benennung: Punkt
glossar_ref: punkt
cluster: ressourcen
theorie_pflichtig: required
status: entwurf
---

# Punkt (Subglossar)

Brücke vom normativen Hauptglossar (`hauptglossar/00_ressourcen/hg_punkt.md`) zu
den stufenweisen Theorie-Inhalten. Hier liegt die didaktische
Aufbereitung: berufssprachliche Verankerung über die Rollen-Komposita
am Werkplan und am Bauwerk, Werkzeug-Bezug, Negativ-Abgrenzung zu
„Stelle", „Position" und „Marker" sowie etymologische Brücke vom
lateinischen *punctum* zum Körner-Einstich des Zimmermanns.

---

## Was der Punkt im Holzbau ist

Ein **Punkt** ist eine benannte Stelle im Raum — nicht das Wort
„Stelle" im umgangssprachlichen Sinn, sondern eine ohne Ausdehnung
gedachte Lage, eindeutig bestimmt durch ihre drei Koordinaten in
der Welt.

Im Holzbau-Korpus tritt der Punkt fast nie als nacktes Substantiv
auf. Er lebt in **Rollen-Komposita**: Sparrenfusspunkt, Firstpunkt,
Knotenpunkt, Auflagerpunkt, Achspunkt, Lotpunkt, Bezugspunkt,
Anrisspunkt. Das ist kein Zufall der Sprache, sondern Ausdruck der
Sache — ein Punkt ist im Holzbau immer der Punkt von etwas: der Fuss
des Sparrens, der First eines Daches, der Knoten eines Stabwerks,
das Auflager an einer Pfette.

Das Wort selbst stammt aus lateinisch ***punctum*** „Einstich, das
Gestochene" (zu *pungere* „stechen"). Etymologisch ist der Punkt
also das Ergebnis eines Stech-Vorgangs — eine Brücke, die für die
zimmermannssprachliche Praxis treffender liegt als für die
mathematische Abstraktion: der mit dem Körner ins Holz geschlagene
Anrisspunkt **ist** in der Wortwurzel genau das, was der Begriff
benennt.

## Geometrie und Welt-Bezug — eine Werkplan-Skizze

Die folgende Skizze zeigt einen Ausschnitt aus einem Werkplan: links
das Schnurgerüst am Bauplatz mit zwei Achspunkten am Schnittpunkt
der Bauachsen, rechts darüber der Dachschnitt mit Sparrenfusspunkt
und Firstpunkt. Die beschrifteten Punkte sind dieselbe Sorte
geometrisches Objekt — drei Koordinaten in der Welt — aber jeder
trägt eine andere **Rolle** im Plan.

<svg viewBox="0 0 720 440" xmlns="http://www.w3.org/2000/svg" role="img" font-family="sans-serif" font-size="13">
  <title>Werkplan-Ausschnitt mit Punkt-Rollen — Schnurgerüst und Dachschnitt</title>
  <desc>Zwei Ausschnitte nebeneinander: links das Schnurgerüst am
        Bauplatz mit zwei Achspunkten A_1 und A_2 als Schnittpunkten
        von Bauachsen, rechts ein Dachschnitt im Pfettendach mit
        Sparrenfusspunkten F_l und F_r am Vordach-Ende, vier
        Kerveckpunkten K an Fusspfetten und Firstpfette sowie einem
        Firstpunkt P_F an der Spitze der Sparrenköpfe.</desc>
  <rect width="100%" height="100%" fill="#f4f1ea"/>
  <!--
  ====================================================================
  SVG-DOKUMENTATION: sg_punkt — Werkplan-Ausschnitt mit Punkt-Rollen
  ====================================================================
  ZWECK
    Pflicht-Skizze zu Punkt-Rollen im Holzbau. Zwei Ausschnitte
    nebeneinander zeigen dieselbe Begriffsart „Punkt" in verschiedenen
    konstruktiven Rollen:
      (A) Schnurgerüst am Bauplatz (Hochformat-Block links) mit zwei
          Achspunkten A_1, A_2 als Schnittpunkten von Bauachsen.
      (B) Dachschnitt im Pfettendach (Querformat-Block rechts) mit
          Sparrenfusspunkten F_l und F_r, vier Kerveckpunkten K und
          einem Firstpunkt P_F.
    Trennlinie x=160 (gestrichelt) trennt die zwei Ausschnitte.
  PATTERN-NUTZUNG (SG_KONVENTIONEN.md §6)
    - Pattern 1 Skizzen-Karton-Hintergrund (Position 3 nach <title>
      und <desc>).
    - Pattern 2 Welt-Pfeile-Inset (translate(640, 410)).
    - Pattern 3 Punkt-Markierung mit Label und Rolle.
  STIL-KONVENTIONEN (Farben gemäss §6 Farbpalette)
    Karton                 #f4f1ea  Hintergrund-Rechteck
    Pfetten-Füllung        #d4a76a  warmer Holz-Hue
    Sparren-Füllung        #f5e6c8  hell-warmer Holz-Hue
    Holz-Umriss            #6a4c2a  Polygon-Stroke der Bauteile
    Schnurgerüst-Pfosten   #8a6a3a  kleine Rechtecke an Achsenden
    Akzent-Rot             #c0392b  Punkt-Marker, Bold-Label
    Anthrazit              #2c3e50  Welt-Pfeile, Punkt-Stroke,
                                    Bauachsen-Strichelung,
                                    Bruchsymbol-Wellen
    Trennlinie schwach     #999     gestrichelte Trennlinie x=160
    Mittelgrau             #666     Klarstellungen, Rollen, Sub-Block-
                                    Untertitel
    Schrift-Hierarchie:
      13 bold              identifizierende Begriffe (A_1, A_2, F_l,
                           F_r, P_F, K)
      12 italic            Sub-Block-Titel
      11 italic + #666     Klarstellungen, Rollen, Sub-Block-Untertitel
  GEOMETRIE
    viewBox 720 × 440. Symmetrieachse Dachschnitt x=445. Dachneigung
    30°. Polygon-Stirnen senkrecht zur Welt geschnitten (Werkplan-
    Konvention: Stirn = Senkelschnitt), nicht rechtwinklig zur
    Sparrenachse.
    (A) Schnurgerüst (Hochformat-Block, x=20..140):
      Bauachse 1 (Längs)   vertikal x=60,  y=80..320, dasharray 6 3
      Bauachse 3 (Längs)   vertikal x=100, y=80..320, dasharray 6 3
      Bauachse 2 (Quer)    horizontal y=200, x=25..135
      Schnurgerüst-Pfosten (Rechtecke #8a6a3a 6×14 oder 14×6) an den
      sechs Achsenden — stehende Rechtecke an den Längs-Enden,
      liegende Rechtecke an den Quer-Enden.
      Achspunkte (Schnittpunkte der Bauachsen):
        A_1 = (60, 200)    Achse 1 × Achse 2
        A_2 = (100, 200)   Achse 3 × Achse 2
    (B) Dachschnitt (Pfettendach mit Klauen- und First-Kerve,
        x=170..710):
      Pfetten-Querschnitt 30×38 (gleich für alle drei Pfetten).
      Sparren-Polygon mit V-förmiger Aussparung an Fusspfette UND
      an Firstpfette.
      Pfetten:
        Fusspfette links     rect (305, 200) (Außenkante x=305,
                                              Innenkante x=335)
        Fusspfette rechts    rect (555, 200) (Innenkante x=555,
                                              Außenkante x=585)
        Firstpfette          rect (430, 130). Zuerst gezeichnet im
                             Hintergrund; Sparren-Polygone überdecken
                             sie an den Auflage-Stellen. Sichtbar
                             im 2-px-Spalt zwischen den Sparrenkopf-
                             Stirnen.
      Sparren-Polygon links (10 Eckpunkte im Uhrzeigersinn von
      Vordach-Stirn-oben; Sparrenunterkante an beiden Kerven
      V-förmig unterbrochen):
        (205, 240)   Vordach-Stirn oben
        (444, 102)   Sparrenkopf-Stirn oben (Sparrenoberkante endet
                     am Firstpunkt-Niveau)
        (444, 130)   Sparrenkopf-Stirn unten = Sohle-Ausstieg
                     First-Kerve
        (430, 130)   First-Kerveckpunkt (Sohle-Senkel-Eck)
        (430, 138)   Senkel-Ausstieg First-Kerve
        (323, 200)   Sohle-Ausstieg Fusspfetten-Kerve
        (305, 200)   Fusspfetten-Kerveckpunkt
        (305, 210)   Senkel-Ausstieg Fusspfetten-Kerve
        (216, 262)   Bleischnitt-Anfangspunkt an Sparrenunterkante
        (205, 262)   Sparrenfusspunkt = Treffpunkt Senkelschnitt +
                     Bleischnitt am Vordach-Ende
      Rechts gespiegelt an x=445. Sparrenkopf-Stirn-Spalt 2 px
      (zwischen x=444 und x=446) ≈ 2 cm Praxis-Toleranz.
      Klauenkerve auf Fusspfette: Senkel an Pfetten-Außenkante
      (Vordach-Seite), Sohle horizontal nach innen über die
      Pfettenoberkante. Verschluckt etwa 60 % der Pfettenoberseite.
      First-Kerve auf Firstpfette: Senkel an Firstpfetten-Außenkante
      (zur Traufe hin), Sohle horizontal auf der Firstpfetten-
      Oberkante. Der Sparren liegt formschlüssig mit V-Aussparung
      oben auf der Firstpfette.
      Sparrenfusspunkt = Schnittpunkt zweier welt-rechtwinkliger
      Schnitte am Vordach-Ende:
        Senkelschnitt   welt-vertikal von Sparrenoberkante nach
                        unten, Länge 22 px (262 − 240)
        Bleischnitt     welt-horizontal von Sparrenunterkante nach
                        außen zum Vordach, Länge 11 px (216 − 205)
      Verhältnis ≈ 2:1 (klassische Holzbau-Proportion).
      Begriffsparallele zu sg_kerve.md / hg_kerve.md:
        Sparrenfusspunkt am Vordach-Ende  ↔  Kerveckpunkt P bei Kerve
        Senkelschnitt + Bleischnitt        ↔  Senkel + Sohle
      Beide sind innere Ecken zweier welt-rechtwinkliger Schnitt-
      flächen; Sparrenfusspunkt ist eine ausspringende Ecke der
      Sparrenkontur, der Kerveckpunkt eine einspringende Ecke im
      Sparreninneren.
    Bruchsymbol pro Sparren („Double Break"-Konvention,
    signalisiert „Sparren in Wirklichkeit länger"):
      Zwei parallele Wellen mit je 4 Q-Bezier-Segmenten
      (= 2 Schwingungen), stroke-width 1.6 #2c3e50. Welle-Endpunkte
      über die Sparrenkanten verlängert, sodass sie die Kanten
      visuell durchkreuzen. Weißes Zwischen-Polygon trennt die
      zwei Wellen vom Sparren-Fill.
      Linker Sparren: Welle-Achsenmitte 1 bei (354, 168), Welle-
      Achsenmitte 2 bei (358, 166). Rechter Sparren gespiegelt
      an x=445.
  BESCHRIFTUNGS-SLOTS und Reserven
    (A) Schnurgerüst-Block:
      A_1-Marker         circle r=4 bei (60, 200)
      A_1-Label          (60, 188) middle, bold 13 #c0392b
      A_2-Marker         circle r=4 bei (100, 200)
      A_2-Label          (100, 188) middle, bold 13 #c0392b
      Klarstellung       „Achspunkte" (80, 174) middle, italic 11
                         #666. Eine gemeinsame Klarstellung statt
                         zwei einzelner — die zwei Marker liegen
                         nur 40 px auseinander, separate Texte
                         würden horizontal überlappen.
      Sub-Block-Titel    (80, 360) middle, italic 12
                         „Schnurgerüst"
      Sub-Block-Untertitel (80, 376) middle, italic 12
                         „(Bauplatz)"
    (B) Dachschnitt-Block:
      F_l-Marker         circle r=4 bei (205, 262)
      F_l-Label          (205, 280) middle, bold 13 #c0392b
      F_l-Rolle          (205, 294) start, italic 11 #666
                         „Sparrenfusspunkt"
      F_r-Marker         circle r=4 bei (685, 262)
      F_r-Label          (685, 280) middle, bold 13 #c0392b
      F_r-Rolle          (685, 294) end, italic 11 #666
                         „Sparrenfusspunkt"
                         Asymmetrische Anchors (F_l start /
                         F_r end), beide Klarstellungen laufen
                         zur Bildmitte hin — mit middle-Anchor
                         würde die F_r-Klarstellung über die
                         viewBox-Kante 720 hinausragen.
      K-Marker (4×)      circle r=4. Bezeichner „K" je diagonal
                         vom Marker, innerhalb des Sparren-
                         Polygons:
                         Fusspfetten links  (305, 200) — Label (312, 195) start
                         First links        (430, 130) — Label (420, 137) end
                         First rechts       (460, 130) — Label (470, 137) start
                         Fusspfetten rechts (585, 200) — Label (578, 195) end
      P_F-Marker         circle r=4 bei (445, 102)
      P_F-Label          (445, 92) middle, bold 13 #c0392b
      P_F-Klarstellung   (445, 78) middle, italic 11 #666
                         „Firstpunkt"
      Sub-Block-Titel    (445, 360) middle, italic 12
                         „Dachschnitt — Pfettendach mit Klauen-
                         und First-Kerve (Werkplan)"
      Sub-Block-Untertitel (445, 376) middle, italic 11 #666
                         „K = Kerveckpunkt (an jeder Kerve einer)"
    Welt-Pfeile-Inset (Pattern 2):
      g translate(640, 410) — ê_h-Text endet global bei x ≈ 700,
      20 px Reserve zum viewBox-Rand 720.
  KRITISCHE FALLEN
    (1) Keine Leerzeilen innerhalb des <svg>...</svg>-Blocks.
        CommonMark beendet HTML-Blöcke vom Typ 6 bei der ersten
        leeren Zeile.
    (2) Öffnungstag <svg ...> auf einer einzigen Zeile.
    (3) Sparren-Polygon-Pfad: Sparrenunterkante ist an den zwei
        Kerven (Fusspfetten-Kerve und First-Kerve) V-förmig
        unterbrochen; der Pfad zickzackt durch die Kerveckpunkte
        an beiden Pfetten.
    (4) Polygon-Stirnen senkrecht zur Welt geschnitten (Werkplan-
        Konvention: Stirn = Senkelschnitt).
    (5) Firstpfette wird ZUERST gezeichnet (Hintergrund), Sparren-
        Polygone überdecken sie an den Auflage-Stellen. Sichtbar
        bleibt sie im 2-px-Spalt zwischen den Sparrenkopf-Stirnen.
  ====================================================================
  -->
  <!-- ============ SCHNURGERUEST (Hochformat, linke Spalte x=30..140) ============ -->
  <!-- Bauachse 1 (Laengs): vertikal -->
  <line x1="60" y1="80" x2="60" y2="320" stroke="#2c3e50" stroke-width="1" stroke-dasharray="6 3"/>
  <!-- Bauachse 3 (Laengs, parallel): vertikal -->
  <line x1="100" y1="80" x2="100" y2="320" stroke="#2c3e50" stroke-width="1" stroke-dasharray="6 3"/>
  <!-- Bauachse 2 (Quer): horizontal -->
  <line x1="25" y1="200" x2="135" y2="200" stroke="#2c3e50" stroke-width="1" stroke-dasharray="6 3"/>
  <!-- Schnurgeruest-Pfosten an den Achsenden -->
  <rect x="57" y="73" width="6" height="14" fill="#8a6a3a"/>
  <rect x="57" y="313" width="6" height="14" fill="#8a6a3a"/>
  <rect x="97" y="73" width="6" height="14" fill="#8a6a3a"/>
  <rect x="97" y="313" width="6" height="14" fill="#8a6a3a"/>
  <rect x="20" y="197" width="14" height="6" fill="#8a6a3a"/>
  <rect x="126" y="197" width="14" height="6" fill="#8a6a3a"/>
  <!-- Achspunkte A_1, A_2: Schnittpunkte der zwei Längs-Achsen mit
       der Quer-Achse. Labels über den Markern, damit kein Konflikt
       mit den Quer-Bauachs-Pfosten (y=197..203) entsteht. Gemeinsame
       Klarstellung "Achspunkte" zentral zwischen den beiden, weil
       zwei separate "Achspunkt"-Texte horizontal überlappen würden. -->
  <circle cx="60" cy="200" r="4" fill="#c0392b" stroke="#2c3e50" stroke-width="1"/>
  <text x="60" y="188" text-anchor="middle" fill="#c0392b" font-weight="bold">A_1</text>
  <circle cx="100" cy="200" r="4" fill="#c0392b" stroke="#2c3e50" stroke-width="1"/>
  <text x="100" y="188" text-anchor="middle" fill="#c0392b" font-weight="bold">A_2</text>
  <text x="80" y="174" text-anchor="middle" font-style="italic" font-size="11" fill="#666">Achspunkte</text>
  <text x="80" y="360" text-anchor="middle" font-style="italic" font-size="12">Schnurgerüst</text>
  <text x="80" y="376" text-anchor="middle" font-style="italic" font-size="12">(Bauplatz)</text>
  <!-- ============ DACHSCHNITT (rechter Bereich, Symmetrieachse x=445) ============ -->
  <!-- Fusspfette links: Außenkante x=305 (Vordach-Seite), Innenkante x=335 (weiter außen) -->
  <rect x="305" y="200" width="30" height="38" fill="#d4a76a" stroke="#6a4c2a" stroke-width="1.5"/>
  <!-- Fusspfette rechts: gespiegelt an x=445 (Innenkante x=555, Außenkante x=585) -->
  <rect x="555" y="200" width="30" height="38" fill="#d4a76a" stroke="#6a4c2a" stroke-width="1.5"/>
  <!-- Firstpfette im Hintergrund; Sparren-Polygone überdecken sie an den
       Auflage-Stellen, sichtbar im 2-px-Spalt zwischen den Sparrenkopf-
       Stirnen und an den Pfetten-Rändern. -->
  <rect x="430" y="130" width="30" height="38" fill="#d4a76a" stroke="#6a4c2a" stroke-width="1.5"/>
  <!-- Sparren links: Polygon mit V-förmiger Aussparung an Fusspfette
       und an Firstpfette. Eckpunkte siehe Haupt-Doku-Block Geometrie. -->
  <polygon points="205,240 444,102 444,130 430,130 430,138 323,200 305,200 305,210 216,262 205,262" fill="#f5e6c8" stroke="#6a4c2a" stroke-width="1.5"/>
  <!-- Sparren rechts: gespiegelt an x=445 -->
  <polygon points="685,240 446,102 446,130 460,130 460,138 567,200 585,200 585,210 674,262 685,262" fill="#f5e6c8" stroke="#6a4c2a" stroke-width="1.5"/>
  <!-- Bruchsymbol pro Sparren ("Double Break"-Konvention): zwei
       parallele Wellen mit weißem Zwischen-Polygon zur Trennung
       vom Sparren-Fill. -->
  <!-- LINKER Sparren — weißes Zwischen-Polygon -->
  <polygon points="346,155 351,153 366,179 362,181" fill="white" stroke="none"/>
  <!-- LINKER Sparren — Welle 1 (Vordach-seitig, 4 Q-Segmente = 2 Schwingungen) -->
  <path d="M 346,155 Q 351,157 350,162 Q 349,167 354,168 Q 359,170 358,175 Q 357,180 362,181" stroke="#2c3e50" stroke-width="1.6" fill="none" stroke-linecap="round"/>
  <!-- LINKER Sparren — Welle 2 (First-seitig, parallel mit 5 px Versatz entlang Achse) -->
  <path d="M 351,153 Q 356,155 355,160 Q 354,164 358,166 Q 363,168 362,173 Q 362,177 366,179" stroke="#2c3e50" stroke-width="1.6" fill="none" stroke-linecap="round"/>
  <!-- RECHTER Sparren — gespiegelt an x=445 -->
  <polygon points="544,155 539,153 524,179 528,181" fill="white" stroke="none"/>
  <path d="M 544,155 Q 539,157 540,162 Q 541,167 536,168 Q 531,170 532,175 Q 533,180 528,181" stroke="#2c3e50" stroke-width="1.6" fill="none" stroke-linecap="round"/>
  <path d="M 539,153 Q 534,155 535,160 Q 536,164 532,166 Q 527,168 528,173 Q 528,177 524,179" stroke="#2c3e50" stroke-width="1.6" fill="none" stroke-linecap="round"/>
  <!-- Sparrenfusspunkte F_l, F_r am Vordach-Ende (Treffpunkt
       Senkelschnitt + Bleischnitt). Bezeichner direkt unter dem
       Marker; Klarstellung "Sparrenfusspunkt" zur Bildmitte hin
       orientiert (F_l start, F_r end). -->
  <circle cx="205" cy="262" r="4" fill="#c0392b" stroke="#2c3e50" stroke-width="1"/>
  <text x="205" y="280" text-anchor="middle" fill="#c0392b" font-weight="bold">F_l</text>
  <text x="205" y="294" font-style="italic" font-size="11" fill="#666">Sparrenfusspunkt</text>
  <!-- Sparrenfusspunkt F_r = gespiegelt -->
  <circle cx="685" cy="262" r="4" fill="#c0392b" stroke="#2c3e50" stroke-width="1"/>
  <text x="685" y="280" text-anchor="middle" fill="#c0392b" font-weight="bold">F_r</text>
  <text x="685" y="294" text-anchor="end" font-style="italic" font-size="11" fill="#666">Sparrenfusspunkt</text>
  <!-- Kerveckpunkte (4×, je zwei pro Sparren): Sohle-Senkel-Ecken
       der Fusspfetten-Kerven und der First-Kerven. Bezeichner "K"
       innerhalb der Sparren-Polygone, je diagonal vom Marker. -->
  <!-- Fusspfetten-Kerveckpunkt links -->
  <circle cx="305" cy="200" r="4" fill="#c0392b" stroke="#2c3e50" stroke-width="1"/>
  <text x="312" y="195" fill="#c0392b" font-weight="bold">K</text>
  <!-- First-Kerveckpunkt links -->
  <circle cx="430" cy="130" r="4" fill="#c0392b" stroke="#2c3e50" stroke-width="1"/>
  <text x="420" y="137" text-anchor="end" fill="#c0392b" font-weight="bold">K</text>
  <!-- First-Kerveckpunkt rechts -->
  <circle cx="460" cy="130" r="4" fill="#c0392b" stroke="#2c3e50" stroke-width="1"/>
  <text x="470" y="137" fill="#c0392b" font-weight="bold">K</text>
  <!-- Fusspfetten-Kerveckpunkt rechts -->
  <circle cx="585" cy="200" r="4" fill="#c0392b" stroke="#2c3e50" stroke-width="1"/>
  <text x="578" y="195" text-anchor="end" fill="#c0392b" font-weight="bold">K</text>
  <!-- Firstpunkt P_F an der Spitze der Sparrenköpfe -->
  <circle cx="445" cy="102" r="4" fill="#c0392b" stroke="#2c3e50" stroke-width="1"/>
  <text x="445" y="92" text-anchor="middle" fill="#c0392b" font-weight="bold">P_F</text>
  <text x="445" y="78" text-anchor="middle" font-style="italic" font-size="11" fill="#666">Firstpunkt</text>
  <text x="445" y="360" text-anchor="middle" font-style="italic" font-size="12">Dachschnitt — Pfettendach mit Klauen- und First-Kerve (Werkplan)</text>
  <text x="445" y="376" text-anchor="middle" font-style="italic" font-size="11" fill="#666">K = Kerveckpunkt (an jeder Kerve einer)</text>
  <!-- ============ STRUKTUR-ELEMENTE ============ -->
  <!-- Trennlinie zwischen Schnurgeruest- und Dachschnitt-Ausschnitt -->
  <line x1="160" y1="40" x2="160" y2="400" stroke="#999" stroke-width="1" stroke-dasharray="2 4"/>
  <!-- ============ WELT-PFEILE-INSET (Pattern 2) ============ -->
  <g transform="translate(640, 410)">
    <text x="-12" y="5" text-anchor="end" font-size="11" fill="#666">Welt:</text>
    <line x1="0" y1="0" x2="32" y2="0" stroke="#2c3e50" stroke-width="1.5"/>
    <polygon points="32,0 27,-3 27,3" fill="#2c3e50"/>
    <text x="36" y="5" font-style="italic">ê_h</text>
    <line x1="0" y1="0" x2="0" y2="-32" stroke="#2c3e50" stroke-width="1.5"/>
    <polygon points="0,-32 -3,-27 3,-27" fill="#2c3e50"/>
    <text x="4" y="-36" font-style="italic">ê_v</text>
    <circle cx="0" cy="0" r="2" fill="#2c3e50"/>
  </g>
</svg>

Fünf Punkte sind in der Skizze beschriftet: zwei Achspunkte
**A_1**, **A_2** am Schnurgerüst (Nägel im Pfostenkopf, an denen die
Bauachs-Schnüre fixiert sind), zwei Sparrenfusspunkte **F_l**, **F_r**
am Anschluss der Sparren an die jeweilige Fusspfette, und der
Firstpunkt **P_F** am gemeinsamen Treffpunkt der beiden Sparren am
First. Jeder dieser Punkte ist als Drei-Koordinaten-Lage in der Welt
beschreibbar, jeder trägt eine eigene **Rolle** in der Konstruktion.

## Punkt-Rollen im Werk- und Tragwerksplan

Die Berufssprache benennt Punkte nach ihrer Rolle. Dieselbe
geometrische Sache — eine Lage im Raum — heißt je nach Funktion
anders.

| Rollen-Kompositum | Wo der Punkt auftritt | Womit er erzeugt oder fixiert wird |
|---|---|---|
| **Sparrenfusspunkt** | unteres Sparrenende am Pfetten- oder Schwellholz-Anschluss; Lastabtragung nach unten | Werkplan-Bemaßung; in der Werkstatt durch Anriss am Sparren |
| **Firstpunkt** | oberes Sparrenende; Gelenk in der Statik des Sparrendachs | Werkplan; in der Aufrichte durch Zusammenführung der beiden Firstsparren |
| **Knotenpunkt** | Stelle, an der mehrere Stäbe im Tragwerk zusammenstoßen; kraftschlüssige Verbindung | Werkplan, Statik-Modell; in der Ausführung durch Verbinder oder Versatz |
| **Auflagerpunkt** | punktförmig idealisiertes Auflager; Eingangsgröße der Schnittkraft-Berechnung | Statik-Modell (Bemessung); in der Ausführung über die tatsächliche Auflagerfläche |
| **Achspunkt** / **Achsenschnittpunkt** | Schnittpunkt zweier Bauachsen; Lage-Anker für die Übertragung Grundriss → Bauplatz | am Schnurgerüst durch Nagel im Pfostenkopf materialisiert; im Plan als Achsen-Kreuz |
| **Lotpunkt** / **Lotfusspunkt** | Schnittpunkt eines Lotes mit der Bezugsebene | Senklot oder Senkel mit Schnur; Bodenmarkierung am Lotfuss |
| **Bezugspunkt** | Punkt, auf den sich Maße oder Höhenkoten beziehen (Nullpunkt einer Bauachse, Bezugshöhe ±0.00) | Werkplan-Festlegung; am Bau über eine Höhenmarke (Nivellier-Festpunkt) |
| **Anrisspunkt** / **Körnerpunkt** | punktförmiges Resultat des Anreissens; Schnittpunkt zweier Anriss-Linien | Bleistift-Kreuz, Reissnadel-Ritzkreuz oder Körner-Einstich |

Eine Beobachtung zur Lese-Hilfe: der Werkplan kennt Punkte vor
allem als **Schnittpunkte** (Achsen, Linien, Flächen treffen sich)
und als **Endpunkte** (eine Strecke endet hier). Die Rolle hängt
nicht am Punkt selbst, sondern am umgebenden Bauwerk.

## Werkzeug und Markierung — wie ein Punkt entsteht

Der Übergang vom geometrisch abstrakten Punkt zum **materialisierten**
Punkt am Holz oder am Bauplatz läuft über eine kleine Werkzeug-Trias
plus zwei Hilfsmittel für längere Distanzen:

| Werkzeug | Mark-Art | Permanenz |
|---|---|---|
| **Bleistift / Zimmermannsstift** | Kreuz oder feine Spitze auf einer Anriss-Linie | gering — wischt ab, wird übertüncht |
| **Reissnadel** | feine Ritzspur, geeignet für Hartholz, Sperrholz, Metall | mittel — bleibt erkennbar, lässt sich nicht ausradieren |
| **Körner + Hammer** | konische Vertiefung im Material („Körnung") | hoch — bleibt dauerhaft, dient als Bohr-Vorzentrierung |
| **Schlagschnur** | gerade Linie zwischen zwei vorher gesetzten Endpunkten, mit Kreide oder Farbe | mittel — Linie, keine Punkte |
| **Senkel** / Senklot | flüchtiger Lotpunkt am Boden unter dem Aufhängepunkt | flüchtig — übertragen, dann durch Bleistift-Kreuz oder Nagel fixiert |
| **Schnurgerüst mit Nagel** | Achsenschnittpunkt am Bauplatz | hoch — bleibt bis zum Abbruch des Gerüsts stehen |

Methodisch wichtig: die Berufssprache unterscheidet **Tätigkeit**
und **Resultat** genau. **Anreissen** ist die Tätigkeit, der **Anriss**
ist die entstandene Linie, der **Anrisspunkt** das punktförmige
Resultat — typischerweise der Schnittpunkt zweier Anriss-Linien
oder der mit dem Körner verstärkte Endpunkt einer Anriss-Linie.
Analog: **Ankörnen** ist die Tätigkeit, die **Körnung** das
Resultat. Lehrlinge verwechseln das gern, weil die Werkstattsprache
beides bedarfsweise kürzt.

Eine zweite Beobachtung: die Schlagschnur **markiert keine Punkte**.
Sie zieht eine gerade Linie zwischen zwei Endpunkten, die vorher mit
einem der ersten drei Werkzeuge fixiert worden sind. Die Endpunkte
einer Schlagschnur-Linie tragen dann ihren Rollennamen
(Sparrenfusspunkt, Firstpunkt, Achspunkt) — nicht einen Werkzeug-Namen.

## Was ein Punkt nicht ist — Stelle, Position, Marker

Drei Wörter werden im Alltag gern als Synonym für „Punkt"
verwendet, lassen sich aber im Holzbau-Kontext fachlich abgrenzen:

**„Stelle"** ist in der Mathematik-Didaktik **eindimensional** — die
Nullstelle, die Extremstelle, die Wendestelle einer Funktion sind
x-Werte, nicht vollständige Koordinaten-Tupel. Im Holzbau wird das
Wort umgangssprachlich auch räumlich verwendet („eine Stelle am
Sparren markieren"), trifft aber die Drei-Koordinaten-Lage nicht
sauber. Ein Maß am Messstab — „bei 1235 mm" — ist genau so eine
Stelle: ein 1D-Wert, erst mit zweiter und dritter Koordinate ein
Punkt.

**„Position"** ist im Bauwesen mit der **Positionsnummer** belegt:
die Stücklisten-Nummer eines Bauteils im Werkplan, das Identifikations-
Etikett. Eine Position bezeichnet ein **Bauteil**, kein
Koordinaten-Tupel. „Position" als Synonym für „Stelle im Raum" ist
ein Drift, oft aus CAD-Software-Sprache übernommen, und sollte für
geometrische Lagen vermieden werden.

**„Marker"** ist Software-Slang (CAD, Vermessung); ein Marker
ist die **Visualisierung** eines Punkts auf einem Bildschirm,
nicht der Punkt selbst. „Node" für „Knotenpunkt" ist ähnlich gelagert
— Statik-Software-Slang, nicht zimmermannssprachlich. Beide Wörter
gehören in die Werkzeug-Bedienung, nicht in die Bauteil-Geometrie.

Zur Trennung **Punkt vs. Vektor** in einem Satz, ohne die HG-
Abgrenzung zu doppeln: ein Punkt benennt eine Lage, ein Vektor eine
gerichtete Verschiebung — der Punkt hat keine Richtung, der Vektor
keine Lage.

## Verweise

Diese Subglossar-Datei stützt sich auf die folgenden Hauptglossar-
Begriffe; bei Detailfragen ist dort die normative Definition zu
finden:

- `hauptglossar/00_ressourcen/hg_punkt.md` — das normative Hauptglossar zum Punkt,
  mit mathematischer Definition als Element des affinen Raumes ℝ³,
  Wohldefiniertheit, Implementierungshinweis und Quellenliste.
- `hauptglossar/00_ressourcen/hg_vektor.md` — der konzeptionell abgegrenzte
  Nachbar-Begriff (gerichtete Verschiebung, keine Lage).
- `hauptglossar/00_ressourcen/hg_koordinatensystem.md` — das Bezugssystem, in dem
  ein Punkt durch drei Koordinaten dargestellt wird.
- `hauptglossar/00_ressourcen/hg_toleranzen.md` — die Sammelstelle für
  Plausibilitäts-Schwellen; Punkt-Gleichheit ist in der Praxis immer
  toleranzbehaftet.
