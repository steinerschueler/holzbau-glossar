---
id: sg_strecke
benennung: Strecke
glossar_ref: strecke
cluster: ressourcen
subglossar_pendant: notwendig
status: entwurf
---

# Strecke (Subglossar)

Brücke vom normativen Hauptglossar (`hauptglossar/00_ressourcen/hg_strecke.md`) zu
den stufenweisen Theorie-Inhalten. Hier liegt die didaktische
Aufbereitung: das auffallend selten gebrauchte nackte Wort „Strecke"
in seiner Verankerung über Längen-Komposita, die Werkplan-Bemaßung
als sichtbare Repräsentation einer geometrischen Strecke zwischen
zwei Bauteil-Punkten, Werkzeug- und Anriss-Bezug, sowie Negativ-
Abgrenzung zu den im Holzbau-Alltag konkurrierenden Wörtern Linie,
Gerade, Segment und Kante.

---

## Was die Strecke im Holzbau ist

Eine **Strecke** ist das geradlinige, beidseitig begrenzte Linienstück
zwischen zwei verschiedenen Punkten mit messbarer, endlicher Länge.
Sie ist die einfachste eindimensionale Figur, an der sich im Holzbau
**eine Länge in mm** festmachen lässt.

Im Holzbau-Korpus tritt das nackte Wort „Strecke" auffallend selten
auf. Der Begriff lebt fast immer in **Längen-Komposita** —
Sparrenlänge, Stablänge, Pfettenlänge, Auflagertiefe, Spannweite —
und in **Rollen** wie Bauteilachse, Bauteilkante, Anriss-Linie oder
der bemaßten Strecke auf einem Werkplan. Etymologisch geht „Strecke"
auf das Verb *strecken* (zu *strack* „gerade, straff") zurück, hat
sich aber erst im 18. Jahrhundert aus dem Bergbau-Vokabular zur
heutigen geometrischen Bedeutung verdichtet — eine Wortwurzel mit
weniger direktem Werkstatt-Bezug als beim Punkt.

## Werkplan-Skizze: eine Strecke wird zur Sparrenlänge

Die folgende Skizze zeigt einen Sparren im Werkplan-Schnitt, dessen
Achse vom **Sparrenfusspunkt** am Vordach zum **Firstpunkt** am
Sparrenkopf läuft. Daneben ist die Bemaßung „Sparrenlänge"
eingetragen — eine Maßlinie mit zwei Maßpfeilen und der Maßzahl
zwischen Maßhilfslinien, die von den beiden Bauteil-Punkten
abgehen. Die Maßlinie ist die zeichnerische Repräsentation einer
geometrischen Strecke zwischen zwei Punkten am Bauteil.

<svg viewBox="0 0 720 440" xmlns="http://www.w3.org/2000/svg" font-family="sans-serif" font-size="13">
  <rect width="100%" height="100%" fill="#f4f1ea"/>
  <!--
  ====================================================================
  SVG-DOKUMENTATION: sg_strecke — Werkplan-Sparren mit Bemaßung
                     "Sparrenlaenge" (Pflicht-Skizze F.1)
  ====================================================================
  (XML-Kommentar innerhalb des SVG-Tags; im Preview unsichtbar.
  Keine Leerzeilen innerhalb erlaubt, sonst bricht der Markdown-
  Parser den SVG-Block ab — siehe Erfahrung aus sg_punkt.md.)
  ZWECK
    Eine Strecke zwischen zwei benannten Bauteil-Punkten wird als
    Sparrenlaenge bemaßt. Sichtbar werden: die zwei Endpunkte
    (Sparrenfusspunkt F, Firstpunkt P_F), die geometrische Strecke
    als Sparren-Mittellinie (gestrichelt) und die Bemaßung
    (Maßlinie mit Maßpfeilen und Maßzahl, Maßhilfslinien).
  GLOBALE STRUKTUR
    viewBox 720 x 440. Einzelner Ausschnitt: Sparren als Profil,
    rechtsneigend (Vordach unten links, Firstpfette oben rechts).
    Welt-Pfeile e_h/e_v unten rechts.
  STIL-KONVENTIONEN (Pilot aus sg_punkt.md / sg_kerve.md)
    Farben:
      #d4a76a Pfetten-Fuellung
      #f5e6c8 Sparren-Fuellung
      #6a4c2a Holz-Umriss
      #c0392b Punkt-Markierung (Holzbau-Rot fuer benannte Punkte)
                und Bemaßungs-Hervorhebung (Maßlinie + Maßzahl)
      #2c3e50 Stroke fuer Punkt, Welt-Pfeile, Achs-Strichelung
      #666    Hinweis-Schrift (mittelgrau, klein)
    Schriftgrößen: 13 Standard, 12 italic, 11 klein-italic
    Punkt-Markierung (Standard):
      circle r=4, fill #c0392b, stroke #2c3e50
      Bezeichner: font-weight=bold, Farbe #c0392b
      Rolle:      font-style=italic, font-size=11, Farbe #666
  GEOMETRIE-PARAMETER
    Dachneigung alpha = 30 Grad. tan(alpha) ca. 0.577.
    Sparrenachse vom Sparrenfusspunkt F=(120, 340) zum
    Firstpunkt P_F=(560, 86). dx=440, dy=-254, Laenge ca. 508 px.
    Sparrenachse als gestrichelte Linie (stroke-dasharray 6 3).
    Sparren-Polygon (Achsen-rechtwinklige Stirnen, Hoehe 28 px):
      Oberkante parallel zur Achse, 14 px senkrecht zur Achse
      ueber dieser; Unterkante 14 px darunter. Stirnen rechtwinklig
      zur Achse. Pragmatische Eckpunkte (etwa):
        Vordach-Stirn oben:   (113, 327)
        Vordach-Stirn unten:  (127, 353)
        Firstpfetten-Stirn oben:  (553, 73)
        Firstpfetten-Stirn unten: (567, 99)
    Firstpfette (Hintergrund-Auflager):
      rect (540, 86) bis (590, 124). Sparren liegt darauf auf,
      Firstpunkt P_F=(560, 86) liegt an der Sparrenachsen-Endkante.
    Fusspfette (knapp angedeutet am Sparrenfusspunkt-Niveau):
      rect (104, 340) bis (154, 378). Sparrenfusspunkt F=(120, 340)
      sitzt am Pfettenoberkanten-Niveau.
    Bemaßung "Sparrenlaenge" (parallel zur Sparrenachse, achsen-
    parallel versetzt um 38 px senkrecht zur Achse, sparrenoberseitig):
      Achsen-Einheitsvektor: e_a = (440/508, -254/508) ca. (0.866, -0.500)
      Normalen-Einheitsvektor (sparrenoberseitig, oben-links zeigend):
        n_a = (-0.500, -0.866)
      Endpunkte der Maßlinie (Versatz 38 px in Richtung n_a):
        Maßlinie-Anfang  = F  + 38*n_a  = (120 - 19, 340 - 33) = (101, 307)
        Maßlinie-Ende    = P_F + 38*n_a = (560 - 19,  86 - 33) = (541,  53)
      Maßpfeile an beiden Enden, gefuellt, Spitze auf die Maßlinie-
      Endpunkte zeigend (Pfeil-Schaft entlang der Achse).
      Maßhilfslinien (Maßhilfslinie = duenne Linie von Bauteil-
      Punkt zum jeweiligen Maßlinie-Ende):
        F  = (120, 340)  --> Maßlinie-Anfang (101, 307)
        P_F= (560,  86)  --> Maßlinie-Ende   (541,  53)
      Maßzahl "Sparrenlaenge = 4'820 mm" entlang der Maßlinie,
      mittig zwischen den Pfeilen, schreibgerecht gedreht.
      Drehwinkel der Maßzahl: alpha = -30 Grad (in SVG-Koordinaten,
      d.h. y nach unten = positiv: tatsaechlich rotate -30 um den
      Mittelpunkt M = ((101+541)/2, (307+53)/2) = (321, 180)).
  KRITISCHE FALLEN
    (1) KEINE Leerzeilen innerhalb des <svg>...</svg>-Blocks.
        CommonMark beendet HTML-Bloecke vom Typ 6 bei der ersten
        Leerzeile; der Rest der SVG wuerde als Markdown geparst.
    (2) Bemaßungs-Konvention (Maßlinie, Maßhilfslinie, Maßzahl,
        Maßpfeil) folgt der verbreiteten Werkstatt- und Werkplan-
        Sprache. Normative Termini sind heute "Längenmaß"
        (DIN EN ISO 129-1, Bemaßungs-Sicht) und "Lineares
        Größenmaß" (DIN EN ISO 14405-1, Tolerierungs-Sicht);
        "Maßstrecke" ist didaktischer DACH-Korpus-Begriff ohne
        Norm-Definition.
  ====================================================================
  -->
  <!-- ============ AUFLAGER (zuerst, damit Sparren oben liegt) ============ -->
  <!-- Fusspfette am Sparrenfusspunkt (Querschnitt im Profil) -->
  <rect x="104" y="340" width="50" height="38" fill="#d4a76a" stroke="#6a4c2a" stroke-width="1.5"/>
  <!-- Firstpfette am Firstpunkt (Querschnitt im Profil) -->
  <rect x="540" y="86" width="50" height="38" fill="#d4a76a" stroke="#6a4c2a" stroke-width="1.5"/>
  <!-- ============ SPARREN (Profil-Polygon, Stirnen rechtwinklig zur Achse) ============ -->
  <polygon points="113,327 553,73 567,99 127,353" fill="#f5e6c8" stroke="#6a4c2a" stroke-width="1.5"/>
  <!-- Sparrenachse als gestrichelte Mittellinie (vom Sparrenfusspunkt zum Firstpunkt) -->
  <line x1="120" y1="340" x2="560" y2="86" stroke="#2c3e50" stroke-width="1" stroke-dasharray="6 3"/>
  <text x="370" y="225" text-anchor="middle" font-style="italic" font-size="11" fill="#666">Sparrenachse</text>
  <!-- ============ BAUTEIL-PUNKTE (rote Punkte, sg_punkt-Konvention) ============ -->
  <!-- Sparrenfusspunkt F (am Vordach-Ende, auf Fusspfetten-Oberkante) -->
  <circle cx="120" cy="340" r="4" fill="#c0392b" stroke="#2c3e50" stroke-width="1"/>
  <text x="116" y="372" text-anchor="end" fill="#c0392b" font-weight="bold">F</text>
  <text x="116" y="386" text-anchor="end" font-style="italic" font-size="11" fill="#666">Sparrenfusspunkt</text>
  <!-- Firstpunkt P_F (am Sparrenkopf, an Firstpfetten-Oberkante) -->
  <circle cx="560" cy="86" r="4" fill="#c0392b" stroke="#2c3e50" stroke-width="1"/>
  <text x="572" y="82" fill="#c0392b" font-weight="bold">P_F</text>
  <text x="572" y="96" font-style="italic" font-size="11" fill="#666">Firstpunkt</text>
  <!-- ============ BEMASSUNG "Sparrenlaenge" ============ -->
  <!-- Maßhilfslinien (duenn, vom Bauteil-Punkt zum Maßlinie-Endpunkt) -->
  <line x1="120" y1="340" x2="101" y2="307" stroke="#c0392b" stroke-width="0.8"/>
  <line x1="560" y1="86" x2="541" y2="53" stroke="#c0392b" stroke-width="0.8"/>
  <!-- Maßlinie parallel zur Sparrenachse, 38 px sparrenoberseitig versetzt -->
  <line x1="101" y1="307" x2="541" y2="53" stroke="#c0392b" stroke-width="1.2"/>
  <!-- Maßpfeil am Anfangs-Ende (Spitze auf 101,307, Schaft entlang der Achse) -->
  <polygon points="101,307 113,303 110,313" fill="#c0392b"/>
  <!-- Maßpfeil am Ende (Spitze auf 541,53) -->
  <polygon points="541,53 529,57 532,47" fill="#c0392b"/>
  <!-- Maßzahl "Sparrenlaenge = 4'820 mm" entlang der Maßlinie, gedreht -->
  <text x="321" y="174" text-anchor="middle" fill="#c0392b" font-style="italic" font-size="13" transform="rotate(-30 321 174)">Sparrenlänge = 4'820 mm</text>
  <!-- ============ BESCHRIFTUNG ============ -->
  <text x="360" y="420" text-anchor="middle" font-style="italic" font-size="12">Werkplan-Sparren mit Bemaßung „Sparrenlänge"</text>
  <text x="360" y="434" text-anchor="middle" font-style="italic" font-size="11" fill="#666">die Maßlinie repräsentiert die geometrische Strecke zwischen F und P_F</text>
  <!-- ============ WELT-KOORDINATEN-HILFSDARSTELLUNG ============ -->
  <g transform="translate(660, 410)">
    <text x="-12" y="5" text-anchor="end" font-size="11" fill="#666">Welt:</text>
    <line x1="0" y1="0" x2="38" y2="0" stroke="#2c3e50" stroke-width="1.5"/>
    <polygon points="38,0 33,-3 33,3" fill="#2c3e50"/>
    <text x="42" y="5" font-style="italic">e_hat_h</text>
    <line x1="0" y1="0" x2="0" y2="-38" stroke="#2c3e50" stroke-width="1.5"/>
    <polygon points="0,-38 -3,-33 3,-33" fill="#2c3e50"/>
    <text x="4" y="-42" font-style="italic">e_hat_v</text>
    <circle cx="0" cy="0" r="2" fill="#2c3e50"/>
  </g>
</svg>

Die beiden roten Endpunkte **F** und **P_F** sind die geometrischen
Anker der Strecke; die gestrichelte Sparrenachse zeigt das
unsichtbare geometrische Objekt, das den Sparren als Stab
idealisiert; die rote Maßlinie mit ihren Maßpfeilen ist die
zeichnerische Repräsentation dieser Strecke auf dem Werkplan, mit
ihrem Maßzahl-Wert in Millimetern. Die Maßlinie ist nicht die
Strecke selbst — die Strecke liegt am Bauteil und wird durch die
Maßlinie lediglich ausgedrückt.

In der normativen Bemaßungs-Sprache heißt der so eingetragene
Wert **Längenmaß** (DIN EN ISO 129-1, Bemaßungs-Sicht); aus
Tolerierungs-Sicht spricht dieselbe Norm-Familie vom **Linearen
Größenmaß** (DIN EN ISO 14405-1). Die im DACH-Lehr-Korpus
verbreitete Bezeichnung **Maßstrecke** ist demgegenüber ein
didaktischer Begriff ohne eigene Norm-Definition.

## Strecke als Längen-Wert: die Komposita

Im Holzbau-Alltag tritt die Strecke fast immer als **Längen-Wert in
mm** auf, eingebunden in ein Kompositum, das verrät, **was die
Strecke verbindet** und **wo sie gemessen oder berechnet wird**. Die
folgende Tabelle sammelt die im Werkplan- und Bemessungs-Korpus
geläufigen Komposita:

| Kompositum | Was die Strecke verbindet | In welchem Plan oder welcher Berechnung |
|---|---|---|
| **Sparrenlänge** | Sparrenfusspunkt am Vordach mit Firstpunkt am Sparrenkopf | Werkplan (Bemaßung); Materiallisten-Position |
| **Stablänge** | Stab-Anfang mit Stab-Ende eines Tragwerks-Stabs | Statik-Modell; Werkplan bei Stabwerken |
| **Pfettenlänge** | Pfetten-Anfang mit Pfetten-Ende längs der Bauachse | Werkplan; Materialliste der Pfetten |
| **Sparrenüberstand** | Sparrenfusspunkt mit Vordach-Außenkante | Werkplan, Vordach-Detail |
| **Auflagertiefe** | Auflager-Anfangskante mit Auflager-Endkante am Pfetten-Auflager | Werkplan; Tragfähigkeits-Plausibilität |
| **Spannweite** (Stützweite) | Auflagerpunkt zu Auflagerpunkt eines Trägers | Statik-Bemessung (EC5, SIA 265) |
| **Knicklänge** | rechnerischer Anfang mit rechnerischem Ende des Stab-Knickbereichs | Druckstab-Bemessung |
| **innerer Hebelarm** | Zug-Resultierende mit Druck-Resultierende im Querschnitt | Biegebemessung (Wert, nicht eigenständig benannt) |

Zwei Beobachtungen sind didaktisch wichtig. Erstens: die Komposita
sind sprachlich **Längen-Werte** (man sagt „die Sparrenlänge beträgt
4'820 mm"), geometrisch aber **Strecken** (von Punkt zu Punkt). Der
Werkplan stellt diese Beziehung über die Maßlinie her — die Maßlinie
ist die zeichnerische Brücke zwischen Wert und Strecke. Zweitens: der
**innere Hebelarm** der Biegung ist ein Wert in mm, der in
Bemessungsgleichungen eingeht; im Bemessungs-Korpus wird er nicht
als eigenständige Strecke benannt, sondern als Zahl behandelt. Wer
ihn ausschließlich als „die Strecke zwischen Zug- und Druckresultierende"
versteht, hat das Konzept geometrisch richtig erfasst, aber die
Berufssprache verwendet das Wort „Strecke" hier nicht.

## Strecke als geometrisches Objekt: Werkzeug und Plan

Eine Strecke kann am Bauteil oder auf dem Werkplan auf
unterschiedliche Weise **sichtbar gemacht** werden — und an dieser
Stelle ist die Trennung zwischen **Markieren** und **Messen**
didaktisch entscheidend.

| Werkzeug oder Mittel | Was es mit der Strecke tut | Resultat |
|---|---|---|
| **Schlagschnur** | markiert eine gerade Strecke zwischen zwei vorher gesetzten Endpunkten am Holz oder am Bauplatz | sichtbare Kreide- oder Farb-Linie längs der Strecke |
| **Reissnadel / Bleistift / Reissleiste** | markiert eine Anriss-Linie zwischen zwei Anrisspunkten am Holz | präzise gerissene Linie auf dem Werkstück |
| **Schmiege** | führt das Werkzeug längs der Anrisslinie unter eingestelltem Winkel — z. B. an einer Walmkerve oder einem Versatz | schräg gerissene Linie unter eingestelltem Winkel |
| **Reissboden mit Aufschnüren** | überträgt 1:1 ein Profil als aufgeschnürte Linien zwischen Profil-Eckpunkten auf den Bretterboden | aufgeschnürte Linien zwischen Profil-Eckpunkten |
| **Schnurgerüst** | spannt eine gerade Strecke zwischen zwei Pfostenkopf-Nägeln am Bauplatz | gespannte Schnur als materialisierte Bauachs-Strecke |
| **Maßband / Zollstock / Lasermessgerät** | misst die Distanz zwischen zwei Punkten | Längen-Wert in mm — die Strecke selbst wird nicht markiert |

Die Trennung **Tätigkeit ↔ Resultat** ist im Werkstattkorpus genauso
streng wie beim Punkt: **Anreissen** ist die Tätigkeit, der
**Anriss** das Resultat als sichtbare Linie auf dem Holz;
**Aufschnüren** ist die Tätigkeit, die **aufgeschnürte Linie** das
Resultat auf dem Reissboden. Die Schlagschnur und die
Werkstatt-Werkzeuge **markieren** eine Strecke, indem sie sie als
Linie sichtbar machen; Maßband, Zollstock und Lasermessgerät
**messen** eine Strecke, indem sie ihre Länge als Zahl liefern, ohne
am Material etwas zu hinterlassen.

Eine zweite Beobachtung: die Schlagschnur-Linie auf dem Reissboden,
der Anriss am Sparren, die gespannte Schnur am Schnurgerüst — sie
alle bekommen ihren Namen **nicht vom Werkzeug**, sondern von dem,
**was sie repräsentieren** (Bauachs-Schnur, Sparren-Mittellinie,
Trauflinie, Profil-Eckpunkt-zu-Eckpunkt). Das Werkzeug stellt das
Mittel zur Verfügung, die Begriffe kommen aus dem konstruktiven
Kontext.

## Was eine Strecke nicht ist — Linie, Gerade, Segment, Kante

Vier Wörter werden im Holzbau-Alltag gern als Synonym für „Strecke"
verwendet, lassen sich aber im fachlichen Kontext sauber abgrenzen:

**„Linie"** ist im Mathematik-Korpus ein Oberbegriff über Gerade,
Strahl, Strecke und Kurve und im Holzbau-Alltag das **häufigste
Wort** für die markierte Strecke am Holz oder auf dem Werkplan
(Anrisslinie, Trauflinie, Maßlinie, Bauachslinie). Eben weil das
Wort so breit ist, ist es als normativ-eindeutiger Begriff zu
mehrdeutig — eine „Linie" kann eine Strecke, eine Gerade-
Repräsentation oder ein Polygonzug sein. In der Werkstatt sagt man
deshalb weiterhin „die Linie", im normativen Glossar heißt es „die
Strecke".

**„Gerade"** ist eine in beide Richtungen **unbegrenzte** Figur ohne
endliche Länge. Die Strecke ist demgegenüber beidseitig durch ihre
Endpunkte begrenzt; ihr endlicher Längen-Wert ist es, was sie für
den Holzbau erst greifbar macht. **„Halbgerade" (Strahl)** ist die
einseitig begrenzte Geschwister-Figur — ein Endpunkt fix, in die
andere Richtung unbegrenzt — und tritt im Werkplan-Korpus selten
auf, ist aber in Schiftungs- und Statik-Geometrie sinnvoll.

**„Segment" und „line segment"** sind Anglizismen aus der CAD- und
IFC-Software-Sprache (CAD-Software, Vermessung, BIM-Datenmodelle
führen „LineSegment" als interne Klassen). Im deutschen Holzbau-
Korpus tritt das Wort selten auf; wenn doch, ist es
Übersetzungs-Drift aus englischer Doku und sollte nicht als
gleichwertiges Synonym etabliert werden.

**„Kante"** ist eine Strecke in einer **bauteilspezifischen Rolle**:
sie begrenzt zwei Bauteil-Flächen gegeneinander (Sparrenoberkante,
Sparrenunterkante, Trauflinie an der Pfettenkante) oder zwei
Polygon-Innenwinkel. **Alle Kanten sind Strecken, nicht alle
Strecken sind Kanten.** Die Bauteilachse, die als Schwerlinie eines
Stabbauteils gedacht ist, ist eine Strecke, aber keine Kante; die
Maßlinie auf dem Werkplan ist eine Strecke, aber keine Kante; die
Schlagschnur-Linie am Reissboden ist eine Strecke, aber keine
Kante. „Kante" ist also ein abgeleiteter Rollen-Begriff, kein
fundamentaler.

## Verweise

Diese Subglossar-Datei stützt sich auf die folgenden Hauptglossar-
Begriffe; bei Detailfragen ist dort die normative Definition zu
finden:

- `hauptglossar/00_ressourcen/hg_strecke.md` — das normative Hauptglossar zur
  Strecke, mit mathematischer Definition als abgeschlossene konvexe
  Hülle zweier Punkte, Wohldefiniertheit, Implementierungshinweis
  und Quellenliste.
- `hauptglossar/00_ressourcen/hg_punkt.md` — Endpunkte einer Strecke; die Strecke
  hängt fundamental am Punkt.
- `hauptglossar/00_ressourcen/hg_vektor.md` — die ortsfreie Schwester-Figur:
  Richtung und Länge ohne Lage. Eine Strecke ist die ortsgebundene
  Realisierung eines Vektors zwischen zwei festen Punkten.
- `hauptglossar/00_ressourcen/hg_gerade.md`, `hauptglossar/00_ressourcen/hg_halbgerade.md` — die
  unbegrenzten Geschwister-Figuren.
- `hauptglossar/00_ressourcen/hg_polygon.md` — Strecken als Polygon-Kanten
  zusammengesetzt.
- `hauptglossar/00_ressourcen/hg_koordinatensystem.md` — das Bezugssystem, in dem
  die Endpunkte einer Strecke durch ihre Koordinaten dargestellt
  werden.

Verwandte Subglossar-Einträge (Folgearbeit): `sg_kante`,
`sg_bauteilachse`, `sg_sparrenueberstand`, `sg_anriss`.
