---
id: sg_polyeder
benennung: Polyeder
glossar_ref: polyeder
cluster: ressourcen
theorie_pflichtig: required
status: entwurf
---

# Polyeder (Subglossar)

Brücke vom normativen Hauptglossar (`hauptglossar/00_ressourcen/hg_polyeder.md`) zu
den stufenweisen Theorie-Inhalten. Hier liegt die didaktische
Aufbereitung: die berufssprachliche Beobachtung, dass das Wort
„Polyeder" im DACH-Holzbau-Korpus praktisch unsichtbar bleibt, während
die Sache (jedes Bauteil mit ebenen Flächen, jeder Dachkörper, jedes
Gebäude-Hüllvolumen) allgegenwärtig ist; die Pflicht-Skizze des
Walmdachs als zusammengesetzter Polyeder aus einem dreieckigen Prisma
und zwei rechteckigen Pyramiden; die Polyeder-Rollen im Bauteil-,
Dachkörper- und Hüllvolumen-Maßstab; die Polyeder-Typen Quader,
Prisma, Schiefprisma, Pyramide, Pyramidenstumpf und konkaver
Bauteilkörper; und die
Negativ-Abgrenzung zu Polygon, Volumen, Körper, Bauteil und Mesh.

Stufen-Schwerpunkt **Meister**, mit einer schmalen Zimmermann-Sektion
zur Walmdach-Volumen-Zerlegung. Lehrling- und Schnuppi-Sektionen
bleiben bewusst leer (`SG_KONVENTIONEN.md` §7): das Wort „Polyeder"
hat in der Werkstattsprache der unteren Stufen keine eigenständige
Verankerung; eine erzwungene Schnuppi-Formulierung wäre eine
künstliche Konstruktion.

---

## Was der Polyeder im Holzbau ist

Ein **Polyeder** ist ein dreidimensionaler Körper, dessen Rand
vollständig aus ebenen, polygonal berandeten Flächen besteht — ein
**Vielflach**, wie die seltene deutsche Lehnübersetzung sagt, ein
Körper „mit vielen Sitzflächen", wie das griechische πολύεδρος in
seinem alltagssprachlichen Sinn meinte. Im DACH-Holzbau-Korpus tritt
das Substantiv „Polyeder" auffällig selten auf: DWDS markiert es als
**„selten"**, die Cadwork-Knowledgebase beschreibt die Bauteil-
Modellierung über **B-Rep**, **CSG** und **Extrusion**, ohne das Wort
„Polyeder" auch nur einmal zu nennen, und die BTLx-Spezifikation
arbeitet mit „Grundgeometrie plus Bearbeitungen", nicht mit
„Polyedern". Die Berufsschul-Mathematik der Zimmerei führt
**„Regelkörper" (Quader, Pyramide, Pyramidenstumpf, daneben Zylinder
und Kegel)**, nicht aber den mathematischen Oberbegriff Polyeder.

Die **Sache** dagegen ist überall: jeder Sparren, jede Pfette, jeder
Pfosten, jede Wandstütze, jede CLT-Platte, jeder BSH-Träger im
Rohzustand ist geometrisch ein Polyeder — typisch ein Quader, also
ein rechteckiges Prisma. Wird das Bauteil bearbeitet (Senkelschnitt,
Bleischnitt, Klauenkerve, Versatz, Zapfen, Schwalbenschwanz), wird
aus dem konvexen Quader ein **nicht-konvexes Polyeder mit
einspringenden Kanten** — die Sache verändert sich, das Wort
„Polyeder" wird trotzdem nicht ausgesprochen. Der Zimmermann sagt
„den Sparren kerven", „den Versatz ausarbeiten", „den Zapfen
herstellen"; gemeint ist jedes Mal die boolesche Differenz zweier
Polyeder.

Das macht „Polyeder" zu einem **Begriffs-Importbegriff** im Holzbau:
die Sache ist berufssprachlich verankert über die Spezialfälle
(Quader, Prisma, Pyramide), über die CAD-Modellierungs-Sprache (B-Rep
und CSG), über die BTLx-Datenstruktur und über die Werkstatt-
Beschreibung der Bearbeitungen — der Oberbegriff selbst lebt
hauptsächlich in der mathematischen und in der internationalen
CAD-Englisch-Schicht.

## Walmdach als zusammengesetzter Polyeder — Pflicht-Skizze

Die zentrale Anwendung des Polyeder-Konzepts mit Zimmermanns-
Verankerung ist die **Volumen-Lesart eines Daches**. Das
Walmdach-Hüllvolumen wird für die Volumenrechnung in **drei
einfachere Bausteine zerlegt**: ein dreieckiges Prisma im
Mittelbereich zwischen den beiden First-Endpunkten plus zwei
Pyramiden mit rechteckiger Grundfläche an den Walm-Enden. Diese
Zerlegung ist eine **didaktische Abstraktion** — die blauen
Trennebenen-Spuren haben am realen Dach keine Bauteil-Grenze,
sondern markieren die Zerlegung der Volumenrechnung.

<svg viewBox="0 0 720 480" xmlns="http://www.w3.org/2000/svg" role="img" font-family="sans-serif" font-size="13">
  <title>Walmdach zerlegt in Pyramide + Prisma + Pyramide — Schrägriss mit Trennebenen-Dreiecken</title>
  <desc>Schrägriss eines kompakten Walmdachs (a:b:h = 4:2:1,5) mit
        rechteckigem Grundriss. Zwei lotrechte Trennebenen durch die
        First-Endpunkte zerlegen den Körper in drei elementare Polyeder:
        zwei Pyramiden mit Rechteckgrundfläche an den Enden, ein
        dreieckiges Prisma in der Mitte. Die Spuren der Trennebenen
        bilden im Bauteil jeweils ein Dreieck (drei Kanten: eine
        sichtbar auf Hauptdach-vorn, eine verdeckt auf Hauptdach-hinten,
        eine verdeckt auf Grundfläche). Bauteil-Kanten schwarz dashed
        wenn verdeckt; Trennebenen-Spuren Okabe-Ito-Blau; First und
        sichtbarer Walmgrat rot.</desc>
  <rect width="100%" height="100%" fill="#f4f1ea"/>
  <!--
  ====================================================================
  SVG-DOKUMENTATION: sg_polyeder — Walmdach zerlegt in Pyramide +
  Prisma + Pyramide (Schrägriss)
  ====================================================================
  ZWECK
    Haupt-Skizze des SG-Eintrags. Walmdach als zusammengesetzter
    Polyeder, zerlegt in Pyramide_links + Prisma + Pyramide_rechts.
    Jede Trennebene als geschlossenes Dreieck im Bauteil sichtbar
    (drei Eckpunkte: T_v auf Front-Trauf, F auf First, T_h auf
    Hinter-Trauf; drei Kanten: eine sichtbar auf Hauptdach-vorn,
    zwei verdeckt auf Hauptdach-hinten und Grundfläche).
  PATTERN-NUTZUNG (SG_KONVENTIONEN.md §6)
    - Pattern 1 Karton-Hintergrund (Position 3 nach title/desc).
    - Pattern 2 Welt-Pfeile-Inset (translate(640, 450)).
    - Pattern 3 Punkt-Markierung mit Label und Rolle —
      sichtbar (F_L, F_R, T_Lv, T_Rv):
        circle r="4" fill="#c0392b" stroke="#2c3e50" stroke-width="1"
      verdeckt (T_Lh, T_Rh):
        circle r="4" fill="none" stroke="#c0392b" stroke-width="1.5"
                                 stroke-dasharray="2 2"
  STIL-KONVENTIONEN (Farben gemäss §6 Farbpalette)
    Karton              #f4f1ea  Hintergrund-Rechteck
    Pyramide-Fill       #c89a5a  beide Pyramiden + Walm-rechts
    Prisma-Fill         #e8c98a  Prisma-Front
    Holz-Umriss         #6a4c2a  Polygon-Stroke 1,5
    Bauteil verdeckt    #000     verdeckte Trauf- und Walmgrat-Kanten,
                                 stroke-width 1,5 dashed 5 5
    Akzent-Rot          #c0392b  First, Walmgrat, Punkt-Fill (sichtbar),
                                 Punkt-Stroke (verdeckt)
    Trennebene          #0072B2  Okabe-Ito-Blau, CVD-sicher (§6
                                 pre-allowed). Sichtbar 2,5 solid;
                                 verdeckt 1,5 dashed 3 5. Distinkt
                                 von Anthrazit (Welt-Pfeile) und
                                 Akzent-Rot (Bauteil-Schnittgeraden).
    Anthrazit           #2c3e50  Welt-Pfeile, Punkt-Stroke (sichtbar)
    Mittelgrau          #666     Rollen-Beschriftung, Sub-Hinweise
    Schrift-Hierarchie:
      15 italic            Skizzen-Titel oben
      13 italic            Prisma-Label (Trapez hat genug Platz)
      13 bold akzent-rot   Punkt-Namen (F_L, F_R, T_Lv, T_Rv),
                           First-Label
      11 italic            Pyramide-Labels (engerer Platz in
                           Pyramiden-Front-Dreiecken)
      11 bold akzent-rot   Punkt-Namen verdeckt (T_Lh, T_Rh)
      11 italic #666       Rollen ("Trennebenenpunkt", "First-
                           Endpunkt"), Sub-Titel, Klarstellungen
      11 italic #0072B2    Trennebene-Konzept-Label
  GEOMETRIE
    3D-Modell: l (lang) : b (kurz) : h (Höhe) = 4 : 2 : 1,5
      First-Endpunkte: F_L = (b/2, b/2, h) = (1, 1, 1,5)
                       F_R = (l-b/2, b/2, h) = (3, 1, 1,5)
      Trennebenen: x = 1 (LINKS) und x = 3 (RECHTS)
    Projektion: Cabinet-Oblique, Tiefen-Winkel 30°,
                Tiefen-Maßstab 0,4, Render-Scale 140 px/Welt-Einheit
      screen_x = (world_x + world_y · 0,866 · 0,4) · 140 + 32
      screen_y = 410 − (world_y · 0,5 · 0,4 + world_z) · 140
    Eckpunkte (alle Werte in px, Welt-Bedeutung in Klammern):
      C_FL (32, 410)   — Trauf-Vorne-Links
      C_FR (592, 410)  — Trauf-Walmecke-Vorne
      C_BL (129, 354)  — Trauf-Hinten-Links (verdeckt)
      C_BR (689, 354)  — Trauf-Walmecke-Hinten
      F_L  (220, 172)  — First-Endpunkt-Links / Pyramide-Apex links
      F_R  (500, 172)  — First-Endpunkt-Rechts / Pyramide-Apex rechts
      T_Lv (172, 410)  — Trennebene-LINKS auf Front-Trauf
      T_Rv (452, 410)  — Trennebene-RECHTS auf Front-Trauf
      T_Lh (269, 354)  — Trennebene-LINKS auf Hinter-Trauf (verdeckt)
      T_Rh (549, 354)  — Trennebene-RECHTS auf Hinter-Trauf (verdeckt)
    Trennebenen-Dreieck (linke, symmetrisch rechts):
      T_Lv → F_L → T_Lh → T_Lv
      Kanten:
        T_Lv → F_L : auf Hauptdach-vorn, SICHTBAR (blau solid 2,5)
        F_L → T_Lh : auf Hauptdach-hinten, VERDECKT (blau dashed 1,5)
        T_Lh → T_Lv: auf Grundfläche (z=0), VERDECKT (blau dashed 1,5)
  KRITISCHE FALLEN
    - Keine Leerzeilen im SVG-Block (auch nicht in XML-Kommentaren).
    - Zeichen-Reihenfolge:
        1. Polygone (Sub-Regionen Hauptdach-vorn + Walm-rechts)
        2. Verdeckte Bauteil-Kanten (schwarz dashed) ÜBER Polygonen
        3. Verdeckte Trennebenen-Spuren (blau dashed) ÜBER Polygonen
        4. Sichtbare Trennebenen-Spuren (blau solid)
        5. Sichtbare Schnittgeraden (rot solid)
        6. Labels und Welt-Inset
        7. Punkte ZULETZT (damit nicht hinter Geometrie verschwinden)
    - Verdeckte Kanten müssen NACH den Polygonen gezeichnet werden,
      sonst sind sie unsichtbar (technische-Zeichnungs-Konvention).
    - Trennebenen NICHT in Rot oder Anthrazit zeichnen — die Farben
      sind für Bauteil-Schnittgeraden bzw. Welt-Pfeile reserviert.
  -->
  <!-- ============ SICHTBARE FLÄCHEN — DREI SUB-REGIONEN VON HAUPTDACH-VORN + WALM-RECHTS ============ -->
  <!-- Pyramide-LINKS Front-Dreieck -->
  <polygon points="32,410 172,410 220,172" fill="#c89a5a" stroke="#6a4c2a" stroke-width="1.5" stroke-linejoin="round"/>
  <!-- Prisma Front-Trapez -->
  <polygon points="172,410 452,410 500,172 220,172" fill="#e8c98a" stroke="#6a4c2a" stroke-width="1.5" stroke-linejoin="round"/>
  <!-- Pyramide-RECHTS Front-Dreieck -->
  <polygon points="452,410 592,410 500,172" fill="#c89a5a" stroke="#6a4c2a" stroke-width="1.5" stroke-linejoin="round"/>
  <!-- Walm-rechts Dreieck (gehört zur Pyramide-RECHTS) -->
  <polygon points="592,410 689,354 500,172" fill="#c89a5a" stroke="#6a4c2a" stroke-width="1.5" stroke-linejoin="round"/>
  <!-- ============ VERDECKTE BAUTEIL-KANTEN (über Polygonen, schwarz gestrichelt) ============ -->
  <!-- Trauf-Walm-links: C_FL → C_BL -->
  <line x1="32" y1="410" x2="129" y2="354" stroke="#000" stroke-width="1.5" stroke-dasharray="5 5"/>
  <!-- Trauf-hinten: C_BL → C_BR (horizontal durch T_Lh und T_Rh) -->
  <line x1="129" y1="354" x2="689" y2="354" stroke="#000" stroke-width="1.5" stroke-dasharray="5 5"/>
  <!-- Walmgrat-hinten-links: C_BL → F_L -->
  <line x1="129" y1="354" x2="220" y2="172" stroke="#000" stroke-width="1.5" stroke-dasharray="5 5"/>
  <!-- ============ VERDECKTE TRENNEBENEN-SPUREN (blau gestrichelt) ============ -->
  <!-- Trennebene-LINKS auf Hauptdach-hinten: F_L → T_Lh -->
  <line x1="220" y1="172" x2="269" y2="354" stroke="#0072B2" stroke-width="1.5" stroke-dasharray="3 5"/>
  <!-- Trennebene-RECHTS auf Hauptdach-hinten: F_R → T_Rh -->
  <line x1="500" y1="172" x2="549" y2="354" stroke="#0072B2" stroke-width="1.5" stroke-dasharray="3 5"/>
  <!-- Trennebene-LINKS auf Grundfläche: T_Lv → T_Lh -->
  <line x1="172" y1="410" x2="269" y2="354" stroke="#0072B2" stroke-width="1.5" stroke-dasharray="3 5"/>
  <!-- Trennebene-RECHTS auf Grundfläche: T_Rv → T_Rh -->
  <line x1="452" y1="410" x2="549" y2="354" stroke="#0072B2" stroke-width="1.5" stroke-dasharray="3 5"/>
  <!-- ============ SICHTBARE TRENNEBENEN-SPUREN (Blau solid) ============ -->
  <!-- Trennebene-LINKS auf Hauptdach-vorn: T_Lv → F_L -->
  <line x1="172" y1="410" x2="220" y2="172" stroke="#0072B2" stroke-width="2.5"/>
  <!-- Trennebene-RECHTS auf Hauptdach-vorn: T_Rv → F_R -->
  <line x1="452" y1="410" x2="500" y2="172" stroke="#0072B2" stroke-width="2.5"/>
  <!-- ============ SICHTBARE SCHNITTGERADEN AM BAUTEIL (Akzent-Rot solid) ============ -->
  <!-- First: F_L → F_R -->
  <line x1="220" y1="172" x2="500" y2="172" stroke="#c0392b" stroke-width="3.5"/>
  <!-- Walmgrat-vorn-rechts: C_FR → F_R -->
  <line x1="592" y1="410" x2="500" y2="172" stroke="#c0392b" stroke-width="3.5"/>
  <!-- ============ SUB-VOLUMEN-LABELS ============ -->
  <text x="115" y="380" text-anchor="middle" font-size="11" font-style="italic">Pyramide</text>
  <text x="335" y="300" text-anchor="middle" font-style="italic">Prisma</text>
  <text x="515" y="330" text-anchor="middle" font-size="11" font-style="italic">Pyramide</text>
  <!-- ============ SCHNITTGERADEN-LABELS ============ -->
  <text x="360" y="162" text-anchor="middle" font-weight="bold" fill="#c0392b">First</text>
  <!-- Walmgrat-Label rechts neben unterem Drittel der Walmgrat-vorn-rechts-Linie -->
  <text x="620" y="376" text-anchor="middle" font-weight="bold" fill="#c0392b">Walmgrat</text>
  <!-- ============ TRENNEBENEN-KONZEPT-LABEL (mit Leitlinie) ============ -->
  <text x="130" y="118" text-anchor="end" font-size="11" font-style="italic" fill="#0072B2">Trennebene</text>
  <text x="130" y="132" text-anchor="end" font-size="11" font-style="italic" fill="#666">(rechtwinklig zur First)</text>
  <line x1="133" y1="122" x2="190" y2="240" stroke="#999" stroke-width="0.5" stroke-dasharray="2 3"/>
  <!-- ============ TITEL OBEN ============ -->
  <text x="360" y="40" text-anchor="middle" font-size="15" font-style="italic">Walmdach zerlegt: Pyramide + Prisma + Pyramide</text>
  <text x="360" y="58" text-anchor="middle" font-size="11" font-style="italic" fill="#666">jede Trennebene als geschlossenes Dreieck T_v – F – T_h im Bauteil</text>
  <!-- ============ WELT-PFEILE-INSET (Pattern 2) ============ -->
  <g transform="translate(640, 450)">
    <text x="-12" y="5" text-anchor="end" font-size="11" fill="#666">Welt:</text>
    <line x1="0" y1="0" x2="32" y2="0" stroke="#2c3e50" stroke-width="1.5"/>
    <polygon points="32,0 27,-3 27,3" fill="#2c3e50"/>
    <text x="36" y="5" font-style="italic">e_hat_h</text>
    <line x1="0" y1="0" x2="0" y2="-32" stroke="#2c3e50" stroke-width="1.5"/>
    <polygon points="0,-32 -3,-27 3,-27" fill="#2c3e50"/>
    <text x="4" y="-36" font-style="italic">e_hat_v</text>
  </g>
  <!-- ============ SCHLÜSSEL-PUNKTE NACH PATTERN 3 ============ -->
  <!-- F_L = First-Endpunkt links (sichtbar) -->
  <circle cx="220" cy="172" r="4" fill="#c0392b" stroke="#2c3e50" stroke-width="1"/>
  <text x="213" y="165" text-anchor="end" font-weight="bold" fill="#c0392b">F_L</text>
  <text x="213" y="151" text-anchor="end" font-size="11" font-style="italic" fill="#666">First-Endpunkt</text>
  <!-- F_R = First-Endpunkt rechts (sichtbar) -->
  <circle cx="500" cy="172" r="4" fill="#c0392b" stroke="#2c3e50" stroke-width="1"/>
  <text x="507" y="165" text-anchor="start" font-weight="bold" fill="#c0392b">F_R</text>
  <text x="507" y="151" text-anchor="start" font-size="11" font-style="italic" fill="#666">First-Endpunkt</text>
  <!-- T_Lv = Trennebene-Links auf Front-Trauf (sichtbar) -->
  <circle cx="172" cy="410" r="4" fill="#c0392b" stroke="#2c3e50" stroke-width="1"/>
  <text x="172" y="430" text-anchor="middle" font-weight="bold" fill="#c0392b">T_Lv</text>
  <text x="172" y="444" text-anchor="middle" font-size="11" font-style="italic" fill="#666">Trennebenenpunkt</text>
  <!-- T_Rv = Trennebene-Rechts auf Front-Trauf (sichtbar) -->
  <circle cx="452" cy="410" r="4" fill="#c0392b" stroke="#2c3e50" stroke-width="1"/>
  <text x="452" y="430" text-anchor="middle" font-weight="bold" fill="#c0392b">T_Rv</text>
  <text x="452" y="444" text-anchor="middle" font-size="11" font-style="italic" fill="#666">Trennebenenpunkt</text>
  <!-- T_Lh = Trennebene-Links auf Hinter-Trauf (verdeckt — offener Kreis) -->
  <circle cx="269" cy="354" r="4" fill="none" stroke="#c0392b" stroke-width="1.5" stroke-dasharray="2 2"/>
  <text x="269" y="370" text-anchor="middle" font-size="11" font-weight="bold" fill="#c0392b">T_Lh</text>
  <text x="269" y="384" text-anchor="middle" font-size="11" font-style="italic" fill="#666">Trennebenenpunkt</text>
  <!-- T_Rh = Trennebene-Rechts auf Hinter-Trauf (verdeckt — offener Kreis) -->
  <circle cx="549" cy="354" r="4" fill="none" stroke="#c0392b" stroke-width="1.5" stroke-dasharray="2 2"/>
  <text x="542" y="370" text-anchor="end" font-size="11" font-weight="bold" fill="#c0392b">T_Rh</text>
  <text x="542" y="384" text-anchor="end" font-size="11" font-style="italic" fill="#666">Trennebenenpunkt</text>
</svg>

Die Skizze macht die zentrale Beobachtung sichtbar: das Walmdach-
Hüllvolumen ist ein **zusammengesetzter Polyeder** aus drei konvexen
Bausteinen. Das **Prisma** im Mittelbereich hat eine dreieckige
Stirnfläche und läuft auf der Länge zwischen den beiden First-
Endpunkten `F_L` und `F_R` parallel zum First. An jedem First-Ende
schließt eine **Pyramide mit rechteckiger Grundfläche** an, deren
Spitze im First-Endpunkt sitzt. Jede Trennebene erscheint im Bauteil
als **geschlossenes Dreieck** mit drei Eckpunkten — je einem
Trennebenenpunkt auf der Front-Trauf, einem First-Endpunkt und einem
Trennebenenpunkt auf der Hinter-Trauf (linke Trennebene: `T_Lv`,
`F_L`, `T_Lh`; rechte Trennebene symmetrisch: `T_Rv`, `F_R`,
`T_Rh`). Die gestrichelten blauen Trennebenen-Spuren sind
**rechnerische Hilfslinien** — am realen Dach gibt es keine
Bauteil-Grenze zwischen Prisma und Pyramide; die Sparren laufen über
diese gedachten Trennebenen durchgehend hinweg. Die Zerlegung ist
eine **gedankliche Volumen-Aufteilung** für die Mengenrechnung,
keine konstruktive Bauteil-Aufteilung.

## Polyeder-Rollen im Holzbau

Polyeder treten im Holzbau auf drei Maßstabs-Ebenen plus als
Hilfs-Geometrie auf, immer als Geometrie-Beschreibung, nie als
eigenständiges Bauteil:

| Rolle | Maßstab | Beispiel |
|---|---|---|
| **Bauteil-Geometrie** | Bauteil-Skala | Sparren als Quader; Sparren mit Klauenkerve als nicht-konvexer Polyeder; CLT-Platte als flacher Quader (Plattenformat × Dicke); BSH-Träger als Quader im Rohzustand |
| **Dachkörper** | Gebäude-Skala | Walmdach als Prisma plus zwei Pyramiden; Satteldach als reines Prisma mit dreieckiger Stirn; Stuttgarter Dach mit Pyramidenstumpf-Krone |
| **Gebäude-Hüllvolumen** | Stadtmaßstab | das Polyeder, das ein Gebäude inklusive Erkern, Gauben und Anbauten umschließt — in der 3D-Stadtmodellierung explizit als Polyeder behandelt |
| **Konvexe Hülle einer Punktmenge** | Hilfs-Geometrie | das kleinste konvexe Polyeder, das eine gegebene Punktmenge umschließt — als Hilfsbegriff der Standsicherheits-Geometrie (Schwerpunkt muss innerhalb der Standfläche liegen) und als Bezugskörper für Hüll-Quader-Berechnungen (AABB) |

Die wichtigste praktische Unterscheidung ist die zwischen
**Bauteil-Geometrie** und **Bauteil-Identität**. Ein Bauteil im Sinne
von `hauptglossar/10_kern/hg_bauteil.md` trägt eine UUID, eine Positionsnummer,
einen Werkstoff und eine Lage; das Polyeder ist nur seine
**Geometrie-Hülle**. In den 3D-CAD-Systemen des Holzbaus (Cadwork,
Sema, Dietrichs) wird diese Trennung sauber abgebildet: das
**„Element"** (Cadwork) bzw. die **„Komponente"** (BTLx) trägt die
Identität, das **Volumen-Modell** trägt die Geometrie. Dasselbe
Polyeder kann an mehreren Bauteilen vorkommen (zwei identische
Sparren teilen ihre Geometrie); zwei Bauteile mit unterschiedlicher
Bearbeitung haben unterschiedliche Polyeder, auch wenn sie aus
demselben Rohling kommen.

## Zimmermann-Schicht — Walmdach-Volumen-Zerlegung

Die Volumen-Zerlegung des Walmdachs in **dreieckiges Prisma plus zwei
rechteckige Pyramiden** ist **Berufsschul-Standard der Zimmerei**.
Sie ist die natürliche zimmermännische Antwort auf die Frage „wie
viel Volumen umschließt das Dach?" — die Frage, die beim Eindeck-
Material (Ziegel, Sparrendämmung, Holzbedarf), bei der Container-
Disposition für den Abbund und bei der Aufmaß-Abrechnung praktisch
relevant wird.

Die kompakte **Volumen-Formel** der Berufsschul-Mathematik lautet

```
V = (1/6) · b · h · (2·l + f)
```

mit Breite *b* der Trauflinie, Höhe *h* zwischen Trauf- und First-
Niveau, Länge *l* der Trauflinie und Länge *f* des Firstes. Sie ist
die direkte Summe aus dem Prismen-Volumen (dreieckiger Querschnitt
mal Firstlänge) und den beiden Pyramiden-Volumina (rechteckige
Grundfläche mal Höhe geteilt durch drei) — auseinandergerechnet wird
sie wie folgt sichtbar:

- **Prisma:** V_Prisma = (1/2) · b · h · f   (Dreiecks-Stirn mal
  Firstlänge)
- **zwei Pyramiden:** V_2Pyramiden = 2 · (1/3) · b · ((l − f)/2) · h
  = (1/3) · b · (l − f) · h

Der Sonderfall f = 0 ergibt ein **Zeltdach** (zwei Pyramiden, kein
Mittel-Prisma): das Walmdach wird zur Pyramide; der andere Sonderfall
f = l ergibt ein **Satteldach** (reines Prisma, keine Pyramiden). Die
Zerlegung trägt also die ganze Familie zwischen Zelt- und Satteldach
in einer einzigen Formel.

Der HG-Eintrag `hauptglossar/00_ressourcen/hg_polyeder.md` listet im Erläuterungs-
Block „Walmverschneidungen, Kehlausarbeitungen, Anschnitt-Polygone"
als Beispiele für Polyeder-Schnitt-Operationen. Die hier geschilderte
**Volumen-Lesart des Walmdach-Körpers selbst** (das Dach als Prisma
plus zwei Pyramiden) ist im aktuellen HG-Stand noch nicht
explizit als CSG-Vereinigung notiert; sie ist in
`hauptglossar/ABWEICHUNGEN.md` als ergänzungswürdiger Hinweis am HG
eingetragen.

## Polyeder-Typen im Holzbau

Der Holzbau arbeitet praktisch mit einer kleinen, klar umrissenen
Familie von Polyeder-Typen:

| Typ | Was ihn auszeichnet | Holzbau-Beispiel |
|---|---|---|
| **Quader** | rechteckiges Prisma, sechs Flächen, alle Winkel 90° | unbearbeiteter Sparren, unbearbeitete Pfette, BSH-Träger im Rohzustand, CLT-Platte, OSB- und Spanplatte (Plattenformat × Dicke) |
| **Prisma** | konstanter polygonaler Querschnitt entlang einer geraden Achse, Stirnflächen orthogonal zur Achse | dreieckiger Prismen-Mittelbereich des Walmdachs; gerader Bauteil-Abschnitt mit konstantem Querschnitt; Cadwork nennt die Konstruktion **„Extrusion"** |
| **Schiefprisma** | konstanter Querschnitt, Stirnflächen aber **nicht** orthogonal zur Achse — die Stirnfläche ist mit einem Winkel angeschnitten | Sparren mit **Senkelschnitt** am Sparrenkopf am First; Sparren mit **Bleischnitt** am Sparrenfuß an der Traufe; gerade Strebe mit schrägem Anschnitt |
| **Pyramide** | spitz zulaufender Polyeder über einer polygonalen Grundfläche, eine Spitze | Walm-Endstück mit rechteckiger Grundfläche; Zeltdach als Sonderfall (vier Dachflächen über quadratischer Grundfläche) |
| **Pyramidenstumpf** | Pyramide mit abgeschnittener Spitze, zwei parallele polygonale Flächen | das **Stuttgarter Dach** historisch (Walmdach mit gestutzter Spitze, oft mit Blechplattform gekrönt) |
| **Konkaver Bauteilkörper** | nicht-konvexes Polyeder mit mindestens einer einspringenden Kante | Sparren mit Klauenkerve; Bauteil mit Versatz; Balken mit Zapfen oder Schwalbenschwanz — die praktisch häufigste Typ-Klasse, sobald irgendeine zimmermannsmäßige Verbindung am Bauteil ausgearbeitet ist |

Konkave Polyeder sind im Holzbau die Regel, nicht die Ausnahme: kaum
ein eingebautes Bauteil bleibt unbearbeitet bis zum Einbau. Die
**konvexen Polyeder** dominieren die Rohzustände, die
**Halbfertig-Bauteile** und die zusammengesetzten Volumen-Bausteine
der Dachkörper-Zerlegung; die **konkaven** dominieren die fertigen,
in den Knotenpunkten passgerecht ausgearbeiteten Stab-Bauteile am
fertigen Tragwerk.

## Was ein Polyeder nicht ist

Fünf nachbarschaftliche Begriffe stehen dem Polyeder im Holzbau nahe
und werden gelegentlich mit ihm verwechselt. Die Trennung ist
didaktisch tragend.

**Polygon.** Ein Polygon ist eine **2D-Berandung**: eine durch
Strecken in einer Ebene geschlossene Figur, ohne Tiefe, ohne Volumen.
Ein Polyeder ist ein **3D-Körper**: jede seiner Begrenzungsflächen
ist ein Polygon, das Polyeder selbst ist es nicht. Die Beziehung
spiegelt die Achse Strecke ↔ Gerade um eine Dimension höher: Polygon
ist die berandete 2D-Figur, Polyeder der berandete 3D-Körper. Schnitt
durch ein Bauteil-Polyeder ergibt im Werkplan ein Schnitt-Polygon.

**Volumen.** Volumen ist die **Maßzahl** in mm³, die zu einem Körper
gehört — eine reelle Zahl, kein geometrischer Körper. Das Walmdach
**ist** das Polyeder; das Walmdach **hat** das Volumen V. Die
Berufssprache der Volumen-Zerlegung trennt das sauber: „das Walmdach-
Volumen ist die Summe aus Prismen-Volumen und zweimal Pyramiden-
Volumen" — das Dach selbst ist nicht die Summe, das Dach ist der
zusammengesetzte Polyeder, dessen Volumen-Summe diesen Wert ergibt.

**Körper.** Der Begriff **Körper** ist im Holzbau-Korpus
**weiter** als Polyeder — er umfasst auch gekrümmte 3D-Objekte:
**Zylinder** (Rundholz, runde Stütze), **Kegel** (zugespitzter
Bauteil-Anschnitt), **Kugel** und **Halbkugel** (Ornament-Geometrien).
Die Berufsschul-„Regelkörper" sind Quader, Zylinder, Kegel, Pyramide,
Pyramidenstumpf — drei davon sind Polyeder (Quader, Pyramide,
Pyramidenstumpf), zwei nicht (Zylinder, Kegel). „Körper" ist deshalb
der gemeinsame Oberbegriff über Polyeder **und** gekrümmte Körper —
nicht spezifisch genug, um „Polyeder" als Synonym zu ersetzen. Das
HG-Frontmatter führt „Körper" und „Volumenkörper" konsequent in den
**abgelehnten Benennungen**; „Volumenkörper" zusätzlich, weil es ein
CAD-Anglizismus von „solid body" ist.

**Bauteil.** Ein Bauteil trägt **Identität** (UUID, Positionsnummer),
**Werkstoff**, **Lage**, **Annotationen** und einen Werkplan-Kontext;
ein Polyeder ist eine **reine Geometrie-Hülle** ohne diese Attribute.
Ein Bauteil **hat** einen Polyeder als Geometrie-Aspekt, ist aber
nicht selbst ein Polyeder. Cadwork trennt analog **„Element"**
(Bauteil mit Identität) von **Geometrie-Modell**; BTLx trennt
**„Komponente"** (mit GUID, Grundgeometrie, Bearbeitungs-Liste) von
ihrer Geometrie.

**Mesh.** Ein Mesh ist eine **diskrete Approximation** einer
3D-Geometrie, typisch aus dreieckigen oder viereckigen Facetten
zusammengesetzt, oft zur Annäherung gekrümmter Oberflächen verwendet.
Ein Polyeder hat per Definition **exakt ebene** Flächen — keine
Approximation, keine Krümmung. Im Render-Pfad eines CAD- oder
Holzbau-Tools werden die polyedrischen Bauteile vor der
Bildschirm-Anzeige in **Render-Meshes** umgewandelt (Tessellierung
der Flächen in Dreiecke), aber das Polyeder selbst bleibt die
mathematische Beschreibung. Die Verwechslung Polyeder ↔ Mesh ist
typisch für die Übergangsschicht zwischen CAD-Geometrie und
3D-Visualisierung; im fachlichen Holzbau-Korpus sind sie sauber
getrennt.

Die internationalen CAD-Englisch-Wörter **„polyhedron"** und
**„solid"** sind keine Synonyme im deutschen Werkplan- und
Werkstatt-Korpus — sie sind Software-Slang aus internationaler
Dokumentation. Der HG führt sie konsequent in den
**abgelehnten Benennungen**.

## Etymologie

**Polyeder** ist ein griechisches Lehnwort, abgeleitet von
**πολύεδρος** (polýedros) „vielsitzig, vielflächig", zusammengesetzt
aus **πολύς** (polýs) „viel" und **ἕδρα** (hedra) „Sitz, Sitzfläche,
Fläche". Die griechische Wort-Metapher meint einen Körper mit
**vielen Sitzflächen** — als ob jede Begrenzungsfläche ein Platz
wäre, auf den sich der Körper setzen könnte. Im modernen Deutsch ist
die Bedeutungslinie „Sitz" verblasst; der mathematische Fachgebrauch
hört in „Polyeder" nur noch die „Fläche".

Die deutschen Lehnübersetzungen, alle im modernen Korpus selten, sind
**Vielflach** (Neutrum, Substantivierung), **Vielflächner** (Maskulinum
mit Personen-Suffix) und **Ebenflächner** (betont die Ebenheit der
Flächen). DWDS markiert „Polyeder" als „selten"; im DACH-Holzbau-
Korpus tritt keine der drei deutschen Substantivierungen als
feststehender Begriff auf, ebenso wenig wie „Polyeder" selbst. Die
einzige Verankerung des Wortes liegt in der mathematischen Schicht
(Berufsschul-Mathematik, Lehrbücher, Normen-Diskussion) und in der
internationalen CAD-Sprache.

## Verweise

Diese Subglossar-Datei stützt sich auf die folgenden Hauptglossar-
Begriffe; bei Detailfragen ist dort die normative Definition zu
finden:

- `hauptglossar/00_ressourcen/hg_polyeder.md` — das normative Hauptglossar zum
  Polyeder, mit B-Rep-Definition (Eckpunkte, Kanten, Flächen,
  Inzidenz-Bedingungen 1–5), Euler-Polyederformel, Hauptsatz von
  Weyl-Minkowski (V-Rep ↔ H-Rep im konvexen Fall), CSG-Block,
  Implementierungshinweis und Quellenliste.
- `hauptglossar/00_ressourcen/hg_polygon.md` — die berandete, eben liegende
  2D-Figur; die Begrenzungsflächen eines Polyeders sind Polygone.
- `hauptglossar/00_ressourcen/hg_ebene.md` — die Trägerebene jeder Polyeder-
  Begrenzungsfläche.
- `hauptglossar/00_ressourcen/hg_halbraum.md` — der Halbraum als Bauelement der
  H-Rep konvexer Polyeder.
- `hauptglossar/10_kern/hg_bauteil.md` — das identitätstragende Bauteil
  gegenüber der reinen Geometrie-Hülle des Polyeders.
- `hauptglossar/00_ressourcen/hg_punkt.md`, `hauptglossar/00_ressourcen/hg_vektor.md` — die
  begrifflichen Voraussetzungen.

Verwandte Subglossar-Einträge:

- `theorie/subglossar/sg_ebene.md` — Walmdach in der **Flächen-
  Lesart** (drei Dachebenen, Schnittgeraden als Walmgrat und First);
  Komplementär-Skizze G.1 zu der hier dargestellten Volumen-Lesart.
- `theorie/subglossar/sg_polygon.md` — die 2D-Berandungs-Geschwister-
  Figur; gemeinsame Negativ-Abgrenzung Polyeder ↔ Polygon.
- `theorie/subglossar/sg_kerve.md` — die zimmermannsmäßige
  Bearbeitung, die einen konvexen Sparrenquader in einen
  nicht-konvexen Bauteilkörper überführt.

Verwandte Subglossar-Folgearbeit: `sg_quader`, `sg_prisma`,
`sg_bauteilkoerper`, ggf. `sg_pyramide` (falls `theorie_pflichtig`
heraufgesetzt).
