---
id: sg_polygon
benennung: Polygon
glossar_ref: polygon
cluster: ressourcen
theorie_pflichtig: required
status: entwurf
---

# Polygon (Subglossar)

Brücke vom normativen Hauptglossar (`hauptglossar/00_ressourcen/hg_polygon.md`)
zu den stufenweisen Theorie-Inhalten. Hier liegt die didaktische
Aufbereitung: das Polygon als sachlich allgegenwärtige, sprachlich
fast unsichtbare Form im Holzbau-Korpus; die L-Dach-Grundriss-Skizze
als zentrale Lese-Erfahrung; die drei Rollen am Dachgrundriss, am
Bauteilprofil und am Schnurgerüst; die direkte Korrespondenz
zwischen Polygon-Eckform und Dachausmittlungs-Schnittlinie; sowie
die Negativ-Abgrenzung zu Strecke, Streckenzug, Polyeder, Kontur,
Fläche und dem Maschinenbau-Stolperstein „Polygonprofil".

Das Polygon hat in der Schnuppi-Stufe keine eigene berufssprachliche
Verankerung — das Wort „Polygon" und das mit ihm gemeinte abstrakte
Konzept liegen außerhalb der zugänglichen Alltagssprache. Dieser
SG-Eintrag setzt deshalb beim Lehrling (Walmdach-Grundriss als
„Vieleck mit Ecken und Seiten") an, trägt seinen Schwerpunkt bei
Zimmermann (Bauteilkontur, Schnurgerüst) und Meister
(Dachausmittlung, konvex/konkav → Grat/Kehle) und überlässt die
mathematische Definition dem Hauptglossar (Ingenieur-Stufe).

---

## Was das Polygon im Holzbau ist

Ein **Polygon** ist eine in einer Ebene liegende geschlossene Folge
von Strecken — drei oder mehr Eckpunkte, durch Kanten zyklisch
verbunden, die einander nicht schneiden, zusammen mit dem von ihnen
berandeten Flächenstück. Das ist die geometrische Sache, kurz
gesagt: Ecken, Kanten, eine Innenfläche.

Im Holzbau-Korpus tritt das Polygon **sachlich überall** auf —
jeder Dachgrundriss, jeder Sparrenquerschnitt, jede Bauteilkontur,
jedes Schnurgerüst am Bauplatz ist geometrisch ein Polygon — und
**sprachlich fast nirgends**. Das Wort „Polygon" wird in der
DACH-Berufssprache der Zimmerei nur selten direkt benutzt; der
Zimmermann redet von **Grundriss**, **Umriss**, **Kontur**,
**Profil** und **Querschnitt**. Die Wikipedia-Liste der
Fachbegriffe des Zimmererhandwerks führt kein Polygon-Lemma, das
Zimmerei-Lexikon (zimmerei-neuss.de) kein Polygon-Stichwort,
baubeaver-Dachausmittlung verwendet „Grundriss" durchgängig statt
„Polygon".

Das Wort selbst stammt aus altgriechisch *polygṓnion*
(πολύς *polýs* „viel" + γωνία *gōnía* „Winkel"), kam über das
mittellateinische *polygonum* im 16. bis 17. Jahrhundert ins
Deutsche. Im Holzbau lebt das Polygon-Konzept hinter
**Rollen-Komposita** — Grundriss, Umriss, Kontur, Profil,
Querschnitt — und tritt als nacktes Wort nur dort wieder auf, wo
die mathematisch-importierte Begriffsschicht direkt verwendet wird:
in CAD-Software (Cadwork, Sema, Dietrichs) als interner Datentyp
und Werkzeug-Name, in der Vermessungs-Schicht (Schnurgerüst) als
**Polygonzug**, und in Mathematik- und Geometrie-Quellen als
Standardbegriff.

## Pflicht-Skizze: L-Dach-Grundriss als konkaves Polygon

Die folgende Skizze zeigt einen L-förmigen Dachgrundriss in der
Draufsicht — ein klassisches Walm-Kehl-Dach über einem L-förmigen
Gebäude-Grundriss. Das Grundriss-Polygon hat **sechs Eckpunkte**,
fünf davon **ausspringend** (konvex) und einer **einspringend**
(konkav). Die Skizze schließt visuell an die Walmdach-Darstellung
in `sg_ebene.md` an: dort wurde der Walmdach-Körper im Schrägriss
mit drei Dachebenen gezeigt, hier liegt der Grundriss in der
Draufsicht — beide Skizzen zusammen ergeben ein vollständiges Bild
der Walm-Kehl-Dach-Geometrie.

Die Welt-Pfeile **e_hat_h** und **e_hat_v** unten rechts orientieren die
Draufsicht; in der Draufsicht zeigen beide Pfeile in der Welt
horizontal — sie spannen die welt-horizontale Grundrissebene auf,
auf der das Polygon liegt.

<svg viewBox="0 0 720 480" xmlns="http://www.w3.org/2000/svg" font-family="sans-serif" font-size="13">
  <rect width="100%" height="100%" fill="#f4f1ea"/>
  <!--
  ====================================================================
  SVG-DOKUMENTATION: sg_polygon — L-Dach-Grundriss als konkaves Polygon
  (Pflicht-Skizze, Draufsicht)
  ====================================================================
  (XML-Kommentar innerhalb des SVG-Tags; im Preview unsichtbar.
  KEINE Leerzeilen innerhalb des <svg>-Blocks erlaubt, sonst bricht
  der Markdown-Parser den SVG-Block ab — Erfahrung aus sg_punkt /
  sg_strecke / sg_gerade / sg_ebene / sg_kerve.)
  ZWECK
    L-foermiger Dachgrundriss in der Draufsicht. Sechs Eckpunkte;
    fuenf ausspringend (konvex, Grat-Anker), einer einspringend
    (konkav, Kehl-Anker). Andeutung der Dachausmittlungs-Linien:
    von jeder ausspringenden Ecke geht eine Grat-Linie als
    Winkelhalbierende ins Polygoninnere; von der einspringenden
    Ecke geht eine Kehl-Linie als Winkelhalbierende ebenfalls ins
    Polygoninnere. First-Andeutung als Treffpunkt der Grat- und
    Kehl-Linien.
  STIL-KONVENTIONEN (uebernommen aus sg_punkt.md / sg_ebene.md / sg_kerve.md)
    Farben:
      #f5e6c8 Polygon-Fuellung (Holzton, hell — Dachflaeche-Andeutung)
      #6a4c2a Polygon-Umriss (Holz-Umriss)
      #c0392b Punkt-Markierung (Holzbau-Rot) — fuer ALLE markanten
              Polygon-Ecken, in Linie mit der SG-Konvention
              (alle markanten Punkte rot)
      #2c3e50 Stroke fuer Punkt-Markierungen und Welt-Pfeile
      #999    Dachausmittlungs-Linien (Grat / Kehle / First) gepunktet
      #666    Rolle-Erlaeuterung-Schrift (klein, mittelgrau)
    Schriftgrößen: 13 Standard, 12 italic, 11 klein-italic
    Punkt-Markierung: circle r=4, fill #c0392b, stroke #2c3e50.
    Eckpunkt-Bezeichner: font-weight=bold, Farbe #c0392b.
    Eckform-Etikett (ausspringend/einspringend): italic, #666.
  GEOMETRIE-PARAMETER
    L-Grundriss als geschlossenes Polygon mit 6 Eckpunkten im
    Uhrzeigersinn:
      E1 = (140, 100)  ausspringend (Nordwest-Ecke)
      E2 = (520, 100)  ausspringend (Nordost-Ecke)
      E3 = (520, 250)  ausspringend (Mittel-Ost-Ecke)
      E4 = (320, 250)  EINSPRINGEND (Innenecke des L, Kehl-Anker)
      E5 = (320, 400)  ausspringend (Suedost-Ecke des Anbau-Teils)
      E6 = (140, 400)  ausspringend (Suedwest-Ecke)
    Polygon-Umlauf E1 -> E2 -> E3 -> E4 -> E5 -> E6 -> E1.
    Innenwinkel-Pruefung:
      Bei E4 kommt der Pfad von rechts (-x-Richtung) und geht nach
      unten (+y-SVG, also "Sued" in der Draufsicht). Das Polygon-
      Innere liegt links und oberhalb des Pfades — der Innenwinkel
      bei E4 betraegt 270 Grad, d.h. > 180 Grad: einspringend.
      Bei E1..E3, E5, E6 ist der Innenwinkel jeweils 90 Grad < 180
      Grad: ausspringend.
    Welt-Achsen (Draufsicht): e_hat_h nach rechts (Welt-horizontal Ost),
    e_hat_v nach oben (Welt-horizontal Nord). In der Draufsicht zeigt
    KEIN Pfeil das Lot — das Lot weist aus dem Bild heraus auf den
    Betrachter zu. Beide Bild-Pfeile spannen die Grundrissebene auf.
  DACHAUSMITTLUNG (gepunktet, andeutend)
    Bei gleicher Dachneigung und gleicher Traufhoehe an allen Seiten
    sind die Schnittlinien der Dachflaechen Winkelhalbierende der
    Innenwinkel des Grundriss-Polygons (Wikipedia "Dachausmittlung").
    Von jeder ausspringenden Ecke geht ein GRAT als
    45-Grad-Winkelhalbierende ins Polygoninnere.
    Von der einspringenden Ecke E4 geht eine KEHLE als
    Winkelhalbierende des einspringenden Winkels ins Polygoninnere
    (Richtung x-positiv und y-positiv im SVG, also "Nord-Ost" rein).
    KORREKTUR: Bei einspringender Ecke mit 270-Grad-Innenwinkel
    halbiert die Kehle den 270-Grad-Winkel auf 135 Grad pro Seite,
    geht also in Richtung "Nordwest" relativ zur Innenecke. Da die
    Innenecke E4 = (320, 250) im "Innen-Eck" des L sitzt (links-oben
    von ihr ist Polygoninneres? Nein, Polygoninneres ist links UND
    unterhalb der Kante E3->E4 sowie links UND oberhalb der Kante
    E4->E5). Die Kehle laeuft von E4 ins Polygoninnere in Richtung
    diagonale Bisektrix der zwei Kanten E3->E4 (waagrecht) und
    E4->E5 (senkrecht-nach-unten). Bisektrix: in Richtung
    "rechts-unten" relativ zur Polygon-Innenseite — also vom Punkt
    E4 in Richtung (+x, +y) im SVG, hineingehend ins Polygon.
    Pragmatische Bauweise: alle Schnittlinien werden als kurze
    gepunktete Andeutungen ins Polygoninnere gezeichnet, ohne
    konstruktiv exakte First-Schnittpunkte (Skizze ist Begriffs-
    Skizze, nicht Konstruktionsplan). Ein angedeuteter First-Punkt
    in der Mitte des Polygon-Hauptteils.
  KRITISCHE FALLEN
    (1) KEINE Leerzeilen im <svg>-Block.
    (2) Punkt-Markierung farblich konsistent rot — die Etikette
        "ausspringend" und "einspringend" tragen den didaktischen
        Inhalt, NICHT die Punkt-Farbe. (In aelteren Skizzen-
        Konventionen wurde "konvex blau / konkav rot" diskutiert;
        wir bleiben hier bei der etablierten roten Punkt-Markierung
        der SG-Pilots — die Eckform wird durch das Text-Etikett
        und das Wort "G" / "K" daneben markiert.)
    (3) Draufsicht: SVG-y wachst nach unten; in der Welt ist das
        "Sued" (negative Nordrichtung). Welt-Pfeil e_hat_v zeigt aber
        Welt-NORD = SVG-y-negativ = nach OBEN im Bild — das ist
        in den anderen SG-Pilots gleich gehandhabt.
  ====================================================================
  -->
  <!-- ============ L-GRUNDRISS-POLYGON ============ -->
  <polygon points="140,100 520,100 520,250 320,250 320,400 140,400" fill="#f5e6c8" stroke="#6a4c2a" stroke-width="1.8"/>
  <!-- ============ DACHAUSMITTLUNG: Grat-Linien (Winkelhalbierende) ============ -->
  <!-- E1 (140,100): Grat ins Polygoninnere, Richtung (+x,+y), 45 Grad -->
  <line x1="140" y1="100" x2="200" y2="160" stroke="#999" stroke-width="1" stroke-dasharray="3 3"/>
  <!-- E2 (520,100): Grat ins Polygoninnere, Richtung (-x,+y), 45 Grad -->
  <line x1="520" y1="100" x2="460" y2="160" stroke="#999" stroke-width="1" stroke-dasharray="3 3"/>
  <!-- E3 (520,250): Grat ins Polygoninnere, Richtung (-x,-y), 45 Grad -->
  <line x1="520" y1="250" x2="460" y2="190" stroke="#999" stroke-width="1" stroke-dasharray="3 3"/>
  <!-- E5 (320,400): Grat ins Polygoninnere, Richtung (-x,-y), 45 Grad -->
  <line x1="320" y1="400" x2="260" y2="340" stroke="#999" stroke-width="1" stroke-dasharray="3 3"/>
  <!-- E6 (140,400): Grat ins Polygoninnere, Richtung (+x,-y), 45 Grad -->
  <line x1="140" y1="400" x2="200" y2="340" stroke="#999" stroke-width="1" stroke-dasharray="3 3"/>
  <!-- ============ DACHAUSMITTLUNG: Kehl-Linie an einspringender Ecke E4 ============ -->
  <!-- E4 (320,250): Kehle als Winkelhalbierende des 270-Grad-Innenwinkels;
       Bisektrix in Richtung (+x,+y) relativ zur Ecke (rein ins Polygon) -->
  <line x1="320" y1="250" x2="385" y2="315" stroke="#c0392b" stroke-width="1.2" stroke-dasharray="4 3"/>
  <!-- ============ FIRST-ANDEUTUNG (Mitte des Hauptteils, Treffpunkt der Grate) ============ -->
  <line x1="200" y1="160" x2="460" y2="160" stroke="#999" stroke-width="1" stroke-dasharray="3 3"/>
  <line x1="200" y1="340" x2="260" y2="340" stroke="#999" stroke-width="1" stroke-dasharray="3 3"/>
  <!-- ============ ECKPUNKTE (alle rot, Standard-SG-Konvention) ============ -->
  <!-- E1: ausspringend, Nordwest -->
  <circle cx="140" cy="100" r="4" fill="#c0392b" stroke="#2c3e50" stroke-width="1"/>
  <text x="132" y="95" text-anchor="end" fill="#c0392b" font-weight="bold">E1</text>
  <text x="132" y="109" text-anchor="end" font-style="italic" font-size="11" fill="#666">ausspringend · G</text>
  <!-- E2: ausspringend, Nordost -->
  <circle cx="520" cy="100" r="4" fill="#c0392b" stroke="#2c3e50" stroke-width="1"/>
  <text x="528" y="95" fill="#c0392b" font-weight="bold">E2</text>
  <text x="528" y="109" font-style="italic" font-size="11" fill="#666">ausspringend · G</text>
  <!-- E3: ausspringend, Mittel-Ost (Walm-Ende des Hauptteils) -->
  <circle cx="520" cy="250" r="4" fill="#c0392b" stroke="#2c3e50" stroke-width="1"/>
  <text x="528" y="248" fill="#c0392b" font-weight="bold">E3</text>
  <text x="528" y="262" font-style="italic" font-size="11" fill="#666">ausspringend · G</text>
  <!-- E4: EINSPRINGEND, Innenecke -->
  <circle cx="320" cy="250" r="4.5" fill="#c0392b" stroke="#2c3e50" stroke-width="1.5"/>
  <text x="312" y="245" text-anchor="end" fill="#c0392b" font-weight="bold">E4</text>
  <text x="312" y="259" text-anchor="end" font-style="italic" font-size="11" fill="#c0392b">einspringend · K</text>
  <!-- E5: ausspringend, Suedost (Anbau-Ende) -->
  <circle cx="320" cy="400" r="4" fill="#c0392b" stroke="#2c3e50" stroke-width="1"/>
  <text x="328" y="408" fill="#c0392b" font-weight="bold">E5</text>
  <text x="328" y="422" font-style="italic" font-size="11" fill="#666">ausspringend · G</text>
  <!-- E6: ausspringend, Suedwest -->
  <circle cx="140" cy="400" r="4" fill="#c0392b" stroke="#2c3e50" stroke-width="1"/>
  <text x="132" y="408" text-anchor="end" fill="#c0392b" font-weight="bold">E6</text>
  <text x="132" y="422" text-anchor="end" font-style="italic" font-size="11" fill="#666">ausspringend · G</text>
  <!-- ============ LEGENDE: G und K erklaeren ============ -->
  <text x="40" y="450" font-style="italic" font-size="11" fill="#666">G = Grat-Anker (ausspringende Ecke)</text>
  <text x="40" y="465" font-style="italic" font-size="11" fill="#c0392b">K = Kehl-Anker (einspringende Ecke)</text>
  <!-- ============ TITEL UNTEN ============ -->
  <text x="360" y="450" text-anchor="middle" font-style="italic" font-size="12">L-Dach-Grundriss als konkaves Polygon (Draufsicht)</text>
  <text x="360" y="465" text-anchor="middle" font-style="italic" font-size="11" fill="#666">Sechs Eckpunkte: fünf ausspringend (Grat-Anker), einer einspringend (Kehl-Anker)</text>
  <!-- ============ WELT-PFEILE (Draufsicht: beide horizontal in der Welt) ============ -->
  <g transform="translate(660, 425)">
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

Zwei Beobachtungen zur Skizze. Erstens: das Polygon ist
**geschlossen** und **einfach** — der Streckenzug E1→E2→E3→E4→E5→E6→E1
endet, wo er begonnen hat, und keine zwei Kanten schneiden einander.
Das ist die Geometrie-Eigenschaft, die das Polygon vom offenen
Streckenzug abgrenzt. Zweitens: die Eckform ist im Polygon **nicht
einheitlich**. Fünf der sechs Ecken sind **ausspringend** — der
Innenwinkel ist kleiner als 180°, das Polygon biegt an dieser
Ecke nach innen. Die sechste Ecke, **E4** im Innen-Eck des L, ist
**einspringend** — der Innenwinkel ist größer als 180° (hier
genau 270°), das Polygon biegt an dieser Ecke nach außen. Polygone
mit mindestens einer einspringenden Ecke heißen **konkav**;
Polygone, bei denen alle Ecken ausspringend sind, heißen **konvex**.

Der einspringende Eckpunkt E4 hat im Holzbau dieselbe Rolle wie der
**Kerveckpunkt** am Sparrenprofil mit Klauenkerve (siehe
`sg_kerve.md`): beide sind einspringende Polygon-Ecken — die eine
am Dachgrundriss in der Draufsicht, die andere am
Sparrenquerschnitt in der Lotebene. Sie unterscheiden sich nur in
der Bauteil-Skala und der Bezugsebene; geometrisch sind sie
dieselbe Sache, und beide sind im Holzbau-Alltag der häufigere
Fall, nicht der Ausnahme-Fall.

## Polygon-Rollen im Holzbau

Das Polygon tritt im Holzbau in drei zentralen Rollen auf, die im
Berufsalltag jeweils ein eigenes Vokabular tragen:

| Rolle | Berufsbegriff | Wo es lebt | Stufe |
|---|---|---|---|
| **Dachgrundriss-Polygon** | Grundriss, Dachgrundriss, Umriss | Werkplan in der Draufsicht; Eingabe der Dachausmittlung | Lehrling (Brücke), Meister |
| **Bauteilkontur-Polygon** | Querschnitt, Profil, Bauteilkontur, Stirnseite | Werkplan-Detail am Bauteil; Sparrenprofil mit Kerve, Pfettenquerschnitt, Plattenwerkstoff-Zuschnitt | Zimmermann |
| **Schnurgerüst-Polygon** | Schnurgerüst, Bauachsen, Achspunkte; in der Vermessung: Polygonzug, Polygonpunkt | Bauplatz, Vermessungs-Phase vor dem Aufbau | Zimmermann (Bauplatz), Meister (Vermessungs-Schnittstelle) |

Daneben gibt es weitere, weniger zentrale Polygon-Auftrittsorte:
der **Reissboden** der traditionellen Zimmerei trägt eine
aufgeschnürte Polygon-Kontur als 1:1-Anriss eines Bauteils (siehe
`sg_ebene.md` zum Reissboden als materialisierter Ebene); die
**Schiftung** bringt Polygone als Schnittfiguren der Dachflächen
mit Hilfsebenen hervor (im Korpus „Abgratung", „Auskehlung",
„Schnittfigur" — nicht „Polygon"); die **Auflagerfläche** unter
einem Stab oder einer Wandtafel ist als Vertikalprojektion ein
Polygon, das in der Standsicherheits-Betrachtung als
„Auflagerpolygon" bezeichnet wird (Ingenieur-Schicht, in der
DACH-Holzbau-Berufssprache nicht stark verankert).

In allen drei zentralen Rollen ist das Polygon **die geometrische
Substanz**, der Berufsbegriff trägt **die Rolle**. Wer „Grundriss"
sagt, meint geometrisch ein Polygon in einer welt-horizontalen
Bezugsebene; wer „Sparrenquerschnitt" sagt, meint ein Polygon in
einer rechtwinklig zur Sparrenachse stehenden Schnittebene. Diese
Trennung zwischen Substanz und Rolle ist im SG-Eintrag zur Ebene
(`sg_ebene.md`) ausführlicher entfaltet — sie gilt für das Polygon
analog.

## Konvex und konkav — Grat und Kehle

Die Unterscheidung **konvex** (alle Ecken ausspringend) gegenüber
**konkav** (mindestens eine Ecke einspringend) ist im Holzbau
nicht nur eine Form-Klassifikation, sondern hat eine **direkte
konstruktive Konsequenz** am Dachgrundriss-Polygon: bei der
**Dachausmittlung** über einem Grundriss mit gleicher Dachneigung
und gleicher Traufhöhe folgen die Schnittlinien der Dachflächen
den Winkelhalbierenden der Polygon-Innenwinkel. Daraus ergibt sich
die zentrale Korrespondenz:

- **Ausspringende (konvexe) Polygon-Ecke → Grat.** Über einer
  ausspringenden Ecke des Dachgrundriss-Polygons treffen sich zwei
  benachbarte Dachflächen in einer **Grat**-Linie, die nach oben
  ansteigt und auf den First zuläuft. Jede Ecke E1, E2, E3, E5 und
  E6 der Pflicht-Skizze trägt einen solchen Grat.
- **Einspringende (konkave) Polygon-Ecke → Kehle.** Über einer
  einspringenden Ecke treffen sich zwei benachbarte Dachflächen in
  einer **Kehl**-Linie, die ebenfalls nach oben ansteigt und auf
  den First zuläuft. Die Ecke E4 der Pflicht-Skizze trägt eine
  solche Kehle.

Diese Korrespondenz erklärt, warum **konkave Grundrisse im Holzbau
der praktische Standard** sind: jeder nicht-rechteckige
Wohnhaus-Grundriss — L-Form, U-Form, T-Form, freie Grundrisse mit
Erker — bringt mindestens eine einspringende Ecke mit, und an
jeder einspringenden Ecke entsteht eine Kehle, die statisch
(Schubkonzentration, abgehängte Sparrenteile) und bauphysikalisch
(Wasserführung, Schneefänger) eine eigene Sorgfalt verlangt.
Konvexe Grundrisse — reine Rechtecke, Sechseck-Pavillons,
Achteck-Türme — sind im Holzbau der **Ausnahme-Fall**, nicht der
Standard. Das ist eine bemerkenswerte Umkehrung des
Schulbuch-Bildes der Geometrie, in dem das konvexe Polygon als
Standardform und das konkave als Sonderfall vorgestellt wird.

Eine kleine Übersicht der im Holzbau auftretenden Polygon-Formen:

| Polygon-Form | Eckenzahl | Holzbau-Anwendung | Eckform |
|---|---|---|---|
| Rechteck | 4 | Sattel- oder Walmdach über Rechteck-Grundriss; Pfettenquerschnitt | konvex |
| Trapez | 4 | Pultdach-Grundriss; Walmdach-Trapez über trapezförmigem Grundriss | konvex |
| L-Form | 6 | Walm-Kehl-Dach über L-Grundriss; ein Grat plus eine Kehle | konkav (eine einspringende Ecke) |
| U- oder T-Form | 8 | Walm-Kehl-Dach über U- oder T-Grundriss | konkav (zwei einspringende Ecken) |
| Sechseck | 6 | Sechseck-Pavillon, Zelt-/Spitzdach | konvex (oft regelmäßig) |
| Achteck | 8 | Achteck-Pavillon, Turm | konvex (oft regelmäßig) |
| Sparrenprofil mit Klauenkerve | 7 | Sparrenquerschnitt mit einem Kerveinschnitt | konkav (eine einspringende Ecke am Kerveckpunkt) |
| Sparrenprofil mit Klauen- und First-Kerve | 10 | Sparrenquerschnitt mit zwei Kerven (siehe `sg_punkt.md`) | konkav (zwei einspringende Ecken) |

Die Korrespondenz konvex/konkav → Grat/Kehle ist im Hauptglossar
zum Polygon nicht explizit ausgeführt (die HG-Definition bleibt
geometrisch allgemein); sie wird hier als didaktische
Beobachtung über den Holzbau-Korpus eingeführt, gestützt durch
die einschlägige Dachausmittlungs-Literatur (Wikipedia
„Dachausmittlung", baubeaver „Walmdach-Workshop", zimmerin
„Dachausmittlung-Einführung").

## Was ein Polygon nicht ist

Mehrere geometrische und sprachliche Nachbar-Begriffe werden im
Holzbau-Alltag mit dem Polygon verwechselt oder vermengt, sind
aber **nicht** identisch.

**Strecke.** Eine Strecke hat zwei Endpunkte und ist genau ein
Segment; das Polygon hat drei oder mehr Eckpunkte und besteht aus
drei oder mehr Segmenten, die zyklisch geschlossen sind. Die
Strecke ist eine **Kante** des Polygons, nicht das Polygon selbst.

**Streckenzug / Polygonzug.** Ein Streckenzug ist eine Folge
zusammenhängender Strecken; er kann offen oder geschlossen sein,
und er muss nicht einfach sein. Das Polygon ist die **geschlossene
einfache** Spezialisierung samt berandetem Flächenstück. Im
Mathematik-Korpus ist „Polygonzug" das Synonym für Streckenzug —
mit derselben Allgemeinheit (offen oder geschlossen, einfach oder
nicht). Auch das Hauptglossar führt `streckenzug` als
Abgrenzungs-Begriff mit Synonymen „Polygonzug, Polylinie". In der
**Vermessungs-Schicht** (Geodäsie) ist „Polygonzug" hingegen das
**primäre** Wort — eine Folge gemessener Geradenstücke zwischen
Polygonpunkten, am Bauplatz als Schnurgerüst materialisiert. Wer
am Bauplatz „Polygonzug" hört, hört das Vermessungs-Wort, nicht
das Mathematik-Wort; beide Lesarten leben nebeneinander und
treffen sich am Schnurgerüst-Polygon.

**Polyeder.** Ein Polyeder ist ein dreidimensionaler Körper, der
von Polygonen als Seitenflächen begrenzt wird — ein Quader, eine
Pyramide, ein Walmdach-Hüllvolumen. Das Polygon ist zweidimensional
(in einer Ebene liegend); das Polyeder ist dreidimensional (im
Raum liegend, mit Volumen). Polygone sind die Bausteine der
Polyeder-Berandung.

**Kontur.** Die Kontur ist im Holzbau ein weicher,
beschreibender Begriff für die Begrenzungslinie eines Bauteils.
Sie kann polygonal sein (eine Folge von Strecken), sie kann aber
auch gekrümmt sein (Bögen, Rundungen, freie Kurven). Das Polygon
ist eine **rein geradlinige** Kontur — sobald Krümmungen
auftreten, ist die Kontur kein Polygon mehr.

**Fläche.** Im Holzbau ist „Fläche" ein bauteilbezogener Begriff
(Dachfläche, Wandfläche, Auflagerfläche). Das Polygon kann als
**Berandung** einer Fläche dienen — der Umriss einer Dachfläche
ist ein Polygon — oder als **Punktmenge mit Inhalt** verstanden
werden (das berandete Flächenstück gehört zur Polygon-Definition
dazu). Beide Lesarten sind im Hauptglossar abgehandelt; im
Subglossar genügt der Hinweis, dass „Fläche" das Bauteil-Wort und
„Polygon" das Geometrie-Wort ist — sie liegen auf verschiedenen
Ebenen.

**Vieleck.** Im deutschen Mathematik-Korpus sind „Polygon" und
„Vieleck" synonym; das Hauptglossar führt „Vieleck" als Synonym im
Frontmatter. Im Holzbau-Korpus ist **keines** der beiden Wörter
verbreitet — der Zimmermann sagt weder „Polygon" noch „Vieleck",
sondern eines der Rollen-Komposita. Die Form „Mehreck" gilt als
**abgelehnte Benennung** (HG-Frontmatter).

**Polygonprofil (Maschinenbau).** Das „Polygonprofil" nach
DIN 32711 bezeichnet eine **Welle-Nabe-Verbindung** mit
P3G-Querschnitt aus dem Maschinenbau und hat mit dem
Holzbau-Polygon nichts zu tun. Es taucht in Suchmaschinen
prominent auf und ist deshalb hier als Negativ-Abgrenzung
erwähnt — der Holzbau-Werkplan kennt diesen Begriff nicht.

## Polygonzug im Schnurgerüst

Das **Schnurgerüst** am Bauplatz spannt vor dem Aufbau die
Gebäudekanten als Schnüre zwischen Pfostenkopf-Nägeln auf. Es
materialisiert in der Welt-Geometrie ein geschlossenes Polygon
der Gebäude- oder Bauachsen-Eckpunkte. In der **Vermessungs-
Sprache** (Geodäsie) heißt diese Folge gemessener Strecken
zwischen Eckpunkten ein **Polygonzug**, die Eckpunkte heißen
**Polygonpunkte**, die geschlossene Variante (Schnurgerüst um ein
ganzes Gebäude herum) ein **Ringpolygon**. Diese
Vermessungs-Vokabeln treten am Bauplatz auf, sobald die
Vermessungs-Phase berührt wird — der Zimmermann selbst spricht von
„Bauachsen" und „Achspunkten", der Vermesser von „Polygonzug" und
„Polygonpunkten" (siehe Achspunkt-Skizze in `sg_punkt.md` für das
Schnurgerüst-Bild).

Das ist ein **didaktischer Stolperstein**: dasselbe geometrische
Objekt — eine geschlossene Folge gemessener Strecken — trägt in
der Mathematik-, Holzbau- und Vermessungs-Schicht jeweils andere
Wörter. Im Hauptglossar wird der mathematische Polygon-Begriff
geführt (geschlossen, einfach, mit berandetem Flächenstück); der
vermessungs-spezifische Gebrauch („Polygonzug" am Schnurgerüst)
ist eine eigenständige Lesart desselben Wort-Stamms und in der
DACH-Bauplatz-Praxis fest verankert.

## Etymologie und Berufssprache

Das Wort **Polygon** ist ein Lehnwort aus altgriechisch
*polygṓnion* (πολυγώνιον), zusammengesetzt aus *polýs* „viel"
und *gōnía* „Winkel". Wörtlich also „Vielwinkel" — die deutsche
**Lehnübersetzung** „Vieleck" greift dieselbe Wort-Architektur
auf („viel" + „Ecke"). Beide Wörter sind im Mathematik-Korpus
gleichwertig, das Hauptglossar führt beide als Synonyme. Der
Eintritt ins Deutsche erfolgte über das mittellateinische
*polygonum* ab dem 16. bis 17. Jahrhundert.

Im **Holzbau-Korpus** ist keines der beiden Wörter Berufs-Standard.
Die DACH-Berufssprache hat eigenständige rollenbezogene Komposita
ausgebildet — **Grundriss**, **Umriss**, **Kontur**, **Profil**,
**Querschnitt** — die das Polygon-Konzept in seinen verschiedenen
Anwendungs-Rollen tragen. Das nackte Wort „Polygon" tritt nur in
**drei Schichten** auf, in denen es nicht als
Holzbau-Berufsbegriff, sondern als importierter Fachbegriff aus
einer Nachbar-Disziplin lebt:

- **CAD-Software-Schicht.** Cadwork (Schweiz), Sema (Deutschland)
  und Dietrichs (Deutschland) führen „Polygon" als internen
  Datentyp und als Werkzeug-Name in ihrer Bedien-Oberfläche.
  Cadwork-Manuals sprechen von „polygonaler Linie / Polygon mit
  Tiefe", Sema-Dokumentation von Grundrissen, die „jede beliebige
  Form haben können, einschließlich Polygon".
- **Vermessungs-Schicht.** Die Geodäsie führt „Polygonzug" und
  „Polygonpunkt" als feststehende Fachbegriffe (Wikipedia
  „Polygonzug (Geodäsie)"); am Bauplatz lebt das Vokabular im
  Schnurgerüst- und Bauvermessungs-Kontext.
- **Mathematik-Schicht.** Im Geometrie-Lehrbuch und im Berufsschul-
  Mathematik-Unterricht ist „Polygon" der Standardbegriff für die
  ebene geschlossene Figur aus drei oder mehr Strecken.

Zwischen **Schweiz**, **Deutschland** und **Österreich** zeigt
sich kein nachweisbarer Unterschied: alle drei Länder teilen
denselben Befund — das Polygon lebt als mathematischer
Importbegriff in CAD- und Vermessungs-Schicht, in der gewachsenen
Berufssprache der Zimmerei ist es unsichtbar. Diese Lage ist
analog zur **Geraden** (siehe `sg_gerade.md`): ein
mathematisch-importierter Begriff ohne berufssprachlich gewachsene
Wurzeln, der seine konstruktive Verankerung über
Rollen-Komposita findet.

## Verweise

Diese Subglossar-Datei stützt sich auf die folgenden Hauptglossar-
Begriffe; bei Detailfragen ist dort die normative Definition zu
finden:

- `hauptglossar/00_ressourcen/hg_polygon.md` — das normative Hauptglossar zum
  Polygon, mit mathematischer Definition als geschlossener
  einfacher ebener Streckenzug mit k ≥ 3 Eckpunkten samt
  berandetem Flächenstück, den zwei zulässigen Lesarten
  (Punktmengen- und Berandungs-Lesart), Wohldefiniertheit,
  Implementierungshinweis (`KonvexesPolygon` zuerst,
  `EinfachesPolygon` als Folgearbeit) und Quellenliste.
- `hauptglossar/00_ressourcen/hg_punkt.md`, `hauptglossar/00_ressourcen/hg_strecke.md`,
  `hauptglossar/00_ressourcen/hg_ebene.md` — die drei begrifflichen
  Voraussetzungen des Polygons (Eckpunkte, Kanten, Trägerebene).
- `hauptglossar/00_ressourcen/hg_streckenzug.md` — der Oberbegriff im
  Mathematik-Korpus (offen oder geschlossen, nicht notwendig
  einfach); Synonym „Polygonzug" als Negativ-Abgrenzung zum
  Polygon.
- `hauptglossar/00_ressourcen/hg_polyeder.md` — der dreidimensionale Geschwister-
  Begriff; Polyeder werden von Polygonen berandet.
- `hauptglossar/30_holzbau/hg_dachflaeche.md`, `hauptglossar/00_ressourcen/hg_stirnseite.md`,
  `hauptglossar/00_ressourcen/hg_laengsseite.md` — Bauteilflächen, deren
  Berandung jeweils ein Polygon ist (Rollen-Spezialisierungen).
- `hauptglossar/00_ressourcen/hg_weltkoordinatensystem.md` — das Welt-
  Bezugssystem, gegen das die Trägerebene des Polygons verortet
  wird (Grundrissebene welt-horizontal, Querschnittsebene
  rechtwinklig zur Bauteilachse).

Verwandte Subglossar-Einträge:

- `theorie/subglossar/sg_punkt.md` — Polygon-Eckpunkte als
  benannte Punkte mit Rollen; Achspunkte des Schnurgerüsts als
  Polygonpunkte.
- `theorie/subglossar/sg_strecke.md` — Polygon-Kanten als
  Strecken; Bauteilkanten als Polygon-Berandungs-Strecken.
- `theorie/subglossar/sg_ebene.md` — die Trägerebene, in der das
  Polygon liegt; Grundrissebene und Querschnittsebene als
  Polygon-Träger.
- `theorie/subglossar/sg_kerve.md` — der **Kerveckpunkt** als
  einspringende Polygon-Ecke am Sparrenquerschnitt, in
  geometrischer Parallele zur einspringenden Ecke E4 des
  L-Dach-Grundrisses dieser Skizze.
- Folgearbeit: `sg_dachflaeche`, `sg_polyeder`, `sg_streckenzug`.
