---
id: zapfen
benennung: Zapfen
synonyme: [Holzzapfen, Kantzapfen, "tenon"]
abgelehnte_benennungen: [Zapfenverbindung, Verzapfung, "mortise and tenon", "joint", Stift, Duebel, Holzduebel, Holznagel, Pinne, Stollen, "peg"]
oberbegriff: bearbeitung
begriffstyp: partitiv
voraussetzungen: [bearbeitung, bauteil, lokales_koordinatensystem, bauteilachse, stirnseite, rechteck_querschnitt, polyeder, toleranzen]
abgrenzung_zu: [zapfenloch, kerve, versatz, blatt, kamm, bohrung, schlitz, anschnitt, bearbeitung, verbindung, verbindungsmittel]
status: entwurf
subglossar_pendant: notwendig
quellen_primär:
  - "DIN EN 1995-1-1:2010-12 (Eurocode 5), Abschnitt 6.1.5 (Druck rechtwinklig zur Faser): allgemeines Verfahren für den Querdrucknachweis. Der Wirkungsmechanismus der Zapfenverbindung beruht auf Querdruck an der Lochwandung des Gegenholzes und an der Zapfenwange; die einschlägige Nachweisstelle ist EC5 §6.1.5, nicht §8 (Letzteres betrifft ausschliesslich Anschlüsse mit metallischen Verbindungsmitteln)."
  - "DIN EN 1995-1-1/NA:2013-08, Nationaler Anhang Deutschland: regelt die in EC5 nicht direkt geführten zimmermannsmässigen Verbindungen (Versatz, Zapfen, Holznagel) durch Rückverweis auf DIN 1052."
  - "DIN 1052:2008-12, Abschnitt 15 (Zimmermannsmässige Verbindungen): geometrische und bemessungstechnische Anforderungen an Zapfen und Zapfenlöcher; Faustregeln zu Zapfenbreite und Zapfenlänge in Abhängigkeit der Bauteilabmessungen."
  - "SIA 265:2021 'Holzbau', Anhang A: zimmermannsmässige Verbindungen einschliesslich Versatz und Zapfen; Schweizer Pendant zu DIN 1052 §15."
  - "design2machine: 'BTLx interface description', Version 2.1, 16.11.2023, Abschnitt 'List of Processings', Processings 'Tenon' und 'DovetailTenon' (S. 8 ff.): parametrische Spezifikation des Zapfens als materialabtragende Bearbeitung am Bauteilende mit den Parametern ReferencePlaneId, StartX/StartY, StartDepth, Angle, Inclination, Length, Width, Height (sowie ConeAngle für DovetailTenon). 'Tenon' und 'Mortise' sind in BTLx zwei eigenständige Processings an zwei verschiedenen Bauteilen."
quellen_sekundär:
  - "Mönck, W.; Rug, W.: Holzbau – Bemessung und Konstruktion. 16. Aufl., Beuth, Berlin 2015, Kap. 7 'Verbindungen', § Zapfenverbindungen (einfacher Zapfen, Brustzapfen, Doppelzapfen, Schwalbenschwanz-Zapfen)."
  - "Blass, H. J.; Sandhaas, C.: Ingenieurholzbau – Grundlagen der Bemessung. KIT Scientific Publishing, Karlsruhe 2016, Kap. 8 'Zimmermannsmässige Verbindungen'."
  - "Gerner, M.: Fachwerk – Instandsetzung, Sanierung, Neubau. DVA, 7. Aufl. 2007, Glossar 'Zapfen', 'Schwalbenschwanz', 'Brustzapfen'."
  - "Natterer, J.; Herzog, T.; Volz, M.: Holzbau-Atlas. 4. Aufl., Birkhäuser, Basel 2003, Kap. 'Verbindungen und Anschlüsse', § Zapfenverbindungen."
  - "Krämer, F.: Grundwissen des Zimmerers. Bruderverlag, Karlsruhe, § Zapfenverbindung — Holznagel- und Keilsicherung."
  - "Claus, T.: Zapfenverbindungen im Holzbau – bruchmechanische Analyse und Vorschlag eines Berechnungsmodells. Bautechnik 97 (2020), Wiley."
  - "Lignum (Hrsg.): Holzbautabellen HBT, Lignum, Zürich, aktuelle Auflage, Kap. 'Zimmermannsmässige Verbindungen'."
  - "Informationsdienst Holz, 'Tragverhalten zimmermannsmässiger Holzverbindungen'."
  - "Wikipedia, Lemma 'Zapfenverbindung' (de.wikipedia.org, abgerufen 2026-05-14): Beschreibung der komplementären Geometrie Zapfen / Zapfenloch und der Zapfenluft (5–10 mm)."
  - "Wikipedia, Lemma 'Mortise and tenon' (en.wikipedia.org, abgerufen 2026-05-14): internationale Pendantbenennung."
quellenkonflikt: |
  **Konflikt 1 — Normverankerung des Zapfens.**

  Der Auftragsbriefing-Stand vermutete EC5 §8 als zentrale
  Bemessungsstelle. Die Recherche
  (`docs/recherche/2026-05-14_hg_zapfen.md`, §E) zeigt: EC5 §8
  trägt den Titel „Anschlüsse mit metallischen Verbindungsmitteln"
  und deckt zimmermannsmässige Verbindungen **nicht direkt** ab.
  Die einschlägigen Stellen sind stattdessen:

  - **Wirkungsmechanismus**: EC5 §6.1.5 (Druck rechtwinklig zur
    Faser), weil die Lastübertragung an der Zapfenwange und an
    der Lochwandung des Gegenholzes primär durch Querdruck
    erfolgt.
  - **Normativer Anker**: EC5 Nationaler Anhang (DIN EN
    1995-1-1/NA) plus **DIN 1052:2008-12 §15** (Deutschland) bzw.
    **SIA 265:2021 Anhang A** (Schweiz). Die fachlich-
    strukturellen Aussagen beider Normen sind inhaltlich
    vergleichbar (Querdrucknachweis, Faustregeln zur Geometrie);
    der konkrete Wortlaut weicht ab.

  Eigene Festlegung: Die Bemessungs-Stelle dieses Eintrags ist
  **EC5 §6.1.5 (Querdruck)** in Verbindung mit dem nationalen
  Anhang und DIN 1052 §15 / SIA 265 Anhang A. Diese Festlegung
  ist konsistent mit dem Schwester-Eintrag `hg_zapfenloch.md`
  und mit der Querverweis-Lage in `hg_bearbeitung.md` und
  `hg_kerve.md`.

  **Konflikt 2 — Zapfenbreite als Faustregel oder als Definition.**

  Die DACH-Berufssprache (Wikipedia 'Zapfenverbindung',
  baubeaver.de, zimmerer-treff.com) sowie referenzierte
  Lehrbuch-Stellen (Mönck/Rug, Krämer) geben einheitlich die
  Faustregel an: **Zapfenbreite ≈ 1/3 der Holzdicke des
  stärkeren Holzes**. Der normative Ursprung (DIN 1052 §15
  bzw. ältere DIN 1052:1988) ist in den zugänglichen Quellen
  nur referenziert, nicht zitiert; SIA 265 Anhang A und der
  EC5 NA sind im Volltext nicht eingesehen worden.

  Eigene Festlegung analog zur Kerv-Tiefen-Konvention
  (`hg_kerve.md`, Konflikt 1): Die **Zapfenbreite ist ein
  freier Parameter** des Zapfens und wird **nicht** durch eine
  geometrische Definitionsbedingung auf einen Bruchteil der
  Bauteildicke begrenzt. Die App führt eine **weiche
  Plausibilitätsprüfung** (Warnung, kein Validierungsfehler):
  Zapfenbreite ≈ 1/3 der Bauteildicke entspricht der
  zimmermannsmässigen Praxis; Verletzung erzeugt eine Warnung,
  blockiert die Modellierung nicht. App-Konstante:
  `Toleranzen.ZAPFENBREITE_FAUSTREGEL_DRITTEL` (defaultmässig
  1.0/3.0).

  **Konflikt 3 — Zapfen als subtraktive oder additive Geometrie.**

  IFC und der intuitive Bauteilblick legen den Zapfen als
  **Form** des Bauteilkörpers nahe: er ist eine
  Hervorragung am Bauteilende, kein Loch. BTLx (`Tenon`) und
  die App-interne Bearbeitungs-Ontologie (`hg_bearbeitung.md`,
  partitive Komposition, ausschliesslich subtraktiv) verlangen
  jedoch eine subtraktive Lesart.

  Eigene Festlegung: **Der Zapfen ist subtraktiv definiert** —
  er entsteht durch Entfernen der **Wangen** (typisch zwei,
  ggf. drei oder vier) am Bauteilende des hervorstehenden
  Bauteils. Der „Zapfen-Stumpf" selbst ist nicht hinzugefügtes,
  sondern stehengebliebenes Material. Der Werkzeugkörper
  K_Zapfen(p) ist die **Vereinigung der entfernten
  Wangenkörper**. Diese Festlegung ist konsistent mit
  `hg_bearbeitung.md` Gleichung (1) und mit der BTLx-
  Modellierung. Sie ist asymmetrisch zum Zapfenloch
  (`hg_zapfenloch.md`), das in jeder Modellierungsschicht
  trivial subtraktiv ist.

  **Konflikt 4 — Zapfen vs. Zapfenverbindung vs. Verzapfung
  (Begriffsumfang).**

  Im DACH-Korpus wird „Zapfen" durchgängig für das
  **hervorstehende geometrische Element am einen Bauteil**
  verwendet, „Zapfenverbindung" / „Verzapfung" für die
  **komplementäre Gesamtverbindung** zweier Bauteile.
  Berufssprachlich werden „Zapfen" und „Verzapfung" jedoch
  teils synonym gebraucht.

  Eigene Festlegung: Sowohl „Zapfenverbindung" als auch
  „Verzapfung" sind **abgelehnte Benennungen**, weil sie das
  **Aggregat zweier Bauteile** (Bauteil + Zapfen + Zapfenloch +
  ggf. Sicherung) bezeichnen und damit zum Verbindungs-Begriff
  (`hg_verbindung.md`, `VerbindungsTyp.
  ZimmermannsmaessigerAnschluss`) gehören, nicht zum
  Bearbeitungs-Begriff. Diese Festlegung ist konsistent mit
  dem Schwester-Eintrag `hg_zapfenloch.md`, der „Verzapfung"
  ebenfalls ablehnt. Das englische BTLx-Pendant **„tenon"**
  ist hingegen als Synonym geführt — parallel zu „mortise"
  in `hg_zapfenloch.md` und „single step joint" in
  `hg_versatz.md`: englische BTLx-Begriffe sind als Synonyme
  zulässig, weil sie 1:1 dieselbe geometrische Bearbeitung
  bezeichnen (nicht das Aggregat).

  **Konflikt 5 — Typologie (Subtypen).**

  Die DACH-Berufssprache kennt mehrere Zapfen-Varianten:
  einfacher Zapfen (Standardfall), Doppelzapfen, Schlitz und
  Zapfen (Gabelzapfen), Schwalbenschwanz-Zapfen, Brustzapfen,
  verkämmter Zapfen, abgesetzter Zapfen, Jagdzapfen. Davon
  sind einfacher Zapfen, Doppelzapfen, Schlitz und Zapfen,
  Schwalbenschwanz-Zapfen und Brustzapfen norm- bzw.
  lehrbuchgestützt; verkämmter Zapfen, abgesetzter Zapfen und
  Jagdzapfen sind berufssprachlich belegt, jedoch ohne
  Norm-Beleg im verfügbaren Korpus.

  „Verkämmter Zapfen" ist eine im alpinen Schweizer Holzbau
  (Stuhlsäule ↔ Pfette) etablierte berufssprachliche Variante;
  ein Norm-Beleg liegt aus dem zugänglichen Korpus nicht vor.
  Im Erläuterungsblock wird die Variante als regional etablierte
  berufssprachliche Form thematisiert, erhält aber keinen
  eigenen Glossareintrag.

  Eigene Festlegung: Die App-Klasse `Zapfen` modelliert den
  Zapfen als generischen Bearbeitungs-Subtyp mit
  parametrisierbarer Geometrie (Länge, Breite, Höhe, optionale
  Schwalbenschwanz-Konizität). Die Varianten werden über
  Parameter-Konfigurationen und über Kombination mit anderen
  Bearbeitungen abgebildet:

    - **Einfacher Zapfen**: Standardfall, eine Instanz von `Zapfen`.
    - **Doppelzapfen**: zwei Instanzen `Zapfen` mit eigenen
      UUIDs in derselben Bearbeitungs-Liste.
    - **Schlitz und Zapfen**: `Zapfen`-Geometrie am
      hervorstehenden Bauteil; das Pendant am Gegenholz ist
      ein nach einer Seite offenes Zapfenloch (geführt im
      Eintrag `hg_zapfenloch.md`).
    - **Schwalbenschwanz-Zapfen**: `Zapfen` mit Konizitäts-
      Parameter (ConeAngle in der BTLx-Lesart);
      Folgearbeit (eigener Subtyp `dovetail_zapfen` oder als
      Konfiguration).
    - **Brustzapfen**: Kombination `Zapfen` + zusätzlicher
      Schulter-/Anschnitt-Bearbeitung (`anschnitt`) am selben
      Bauteilende; nicht eigener Subtyp.
    - **Verkämmter Zapfen**: Kombination `Zapfen` + Querverzahnungs-
      Bearbeitung (`kamm`) an den Schulterflächen; nicht
      eigener Subtyp.
    - **Abgesetzter Zapfen**: zweistufiger Zapfen; Folgearbeit
      (eigener Subtyp oder Parameter-Erweiterung).
    - **Jagdzapfen**: Zapfen mit schräger Einbaurichtung;
      Folgearbeit.

  Stemmzapfen, durchgestemmter Zapfen, Stemmzapfen mit Nut
  sind Schreinerei-/Möbelbau-Korpus und werden nicht im
  Holzbau-Glossar geführt.

  **Konflikt 6 — Topologie und Konvexität des Werkzeugkörpers
  K_Zapfen.**

  Der Werkzeugkörper der Zapfen-Bearbeitung ist im typischen
  Fall (0 < w_Z < b_B und 0 < h_Z < h_B) **nicht konvex**:
  vier Wangen rahmen die zentrale Zapfen-Hervorragung. Eine
  erste Entwurfsfassung (Pilot-Eintrag, Gleichung (3) vor der
  Verifikation 2026-05-14) hatte K_Zapfen als Mengen-Differenz
  `{x ∈ [ℓ_B − ℓ_Z, ℓ_B]} \ Z(p_Zapfen)` definiert und auf
  „endliche Polyederzerlegung" verwiesen. Das Kohärenz-Review
  hat festgestellt, dass diese Form (a) die Nicht-Konvexität
  nicht explizit ausweist, (b) die Implementierung als
  Vereinigung konvexer Bausteine nicht direkt liefert und
  (c) im Sonderfall w_Z = b_B nicht zusammenhängend ist
  (zwei disjunkte Wangen) — ein Detail, das in der vagen
  Mengen-Differenz-Form nicht sichtbar war.

  **Eigene Festlegung**: K_Zapfen wird **konstruktiv als
  Vereinigung von bis zu vier konvexen Wangen-Quadern**
  W_y^±, W_z^± definiert (Gleichung (3)). Die deskriptive
  Form als Mengen-Differenz (Gleichung (3')) wird als
  beweisbare Äquivalenz beibehalten. Diese Festlegung ist
  konsistent mit:

  - **`hg_polyeder.md`** (Zeile 148–159, CSG-Konstruktion;
    Zeile 493, „nicht-konvexe Polyeder sind gültige Polyeder"):
    nicht-konvexe Polyeder sind explizit zugelassen.
  - **`KonvexerPolyeder`-Code-Eingrenzung** (`hg_polyeder.md`
    Zeile 319–331): jede einzelne Wange ist konvex und
    instanzierbar als `KonvexerPolyeder`; die Vereinigung
    wird als CSG-Operation des `BearbeitungsAggregator`
    realisiert, nicht als nicht-konvexer `BRepPolyeder`-
    Domänen-Typ.
  - **Strukturparallele zu `hg_bohrung.md`** (Bohrung mit
    DURCHGANG): dort werden bei Durchgangsbohrungen ggf.
    mehrere Halbraum-Bausteine kombiniert; analog werden
    beim Zapfen mehrere Wangen-Quader vereinigt.
  - **Schwester-Symmetrie zu `hg_zapfenloch.md`**: das
    Zapfenloch hat einen einzelnen konvexen Werkzeugkörper
    (Prisma bzw. Pyramidenstumpf), der Zapfen hat eine
    Vereinigung mehrerer konvexer Werkzeugkörper. Diese
    Asymmetrie folgt aus der **ontologischen Asymmetrie**
    der beiden Bearbeitungen (Konflikt 3): Zapfenloch =
    geometrisch direkt subtraktiv; Zapfen = subtraktiv
    durch Entfernen der **Wangen**, die das stehenbleibende
    Material rahmen. Die Wangen sind konstruktiv die
    Bausteine des Zapfen-Werkzeugkörpers.

  Diese Festlegung schärft den Pilot-Eintrag, ändert aber
  weder Tupel-Struktur (1), Konizitätsparameter κ,
  BTLx-Mapping (`Tenon` / `DovetailTenon`) noch
  Bemessungs-Stelle (EC 5 §6.1.5) und ist insofern keine
  inhaltliche Re-Definition, sondern eine
  konstruktiv-mathematische Schärfung.
---

## Prosa-Definition

Ein **Zapfen** ist eine subtraktive Bearbeitung an einem Stab-
Bauteil, die durch Entfernen zweier oder mehrerer Wangenkörper
am Bauteilende eine **rechteckige (oder schwalbenschwanzförmige)
Hervorragung** entlang der Bauteilachse stehen lässt, deren
Längsachse rechtwinklig zur Stirnseite des Bauteils orientiert
ist und deren Querschnitt — typisch mit einer Breite von etwa
einem Drittel der Bauteildicke — als formschlüssiges
Gegenstück zu einem Zapfenloch im aufnehmenden Bauteil
ausgebildet ist.

## Mathematische Definition

Sei

- B ein Stab-Bauteil im Sinne von `bauteil` mit Stabgeometrie
  (`geometrie ∈ 𝒢_stab`), typischerweise eine Stuhlsäule, ein
  Stiel, eine Strebe oder ein Riegel mit hervorstehendem
  Bauteilende,
- L_B = (O_B, e_hat_x^B, e_hat_y^B, e_hat_z^B) das Bauteil-Lokal-
  Koordinatensystem (`lokales_koordinatensystem`) mit Konvention
  ```
  e_hat_x^B  =  Bauteilachse (Längsrichtung, vom Bauteilanfang zum
            Bauteilende zeigend),
  e_hat_y^B  =  Bauteil-Querrichtung (Bauteilbreite),
  e_hat_z^B  =  Bauteilhöhe (Bauteildicke).
  ```
- b_B > 0 die Bauteilbreite in lokaler y-Richtung (mm),
- h_B > 0 die Bauteildicke in lokaler z-Richtung (mm),
- ℓ_B > 0 die Bauteillänge in lokaler x-Richtung (mm),
- die **Stirnseite** S_B des Bauteils (`stirnseite`) jene
  Bauteilfläche mit x = ℓ_B im Lokalsystem; ihr Flächennormalen-
  Vektor ist e_hat_x^B,
- ε_L := Toleranzen.LAENGE_EPS.

Die **Parameter** eines Zapfens sind das Tupel

```
p_Zapfen := (ℓ_Z, w_Z, h_Z, y_Z, z_Z, κ)                          (1)
```

mit

- **ℓ_Z** ∈ ℝ⁺: **Zapfenlänge** (in mm), 0 < ℓ_Z ≤ ℓ_B − ε_L;
  gemessen als perpendikuläre Tiefe vom Niveau der Stirnseite
  (lokales x = ℓ_B) in Richtung −e_hat_x^B in das Bauteilinnere.
- **w_Z** ∈ ℝ⁺: **Zapfenbreite** (in mm), 0 < w_Z ≤ b_B − 2ε_L;
  die Ausdehnung des Zapfen-Querschnitts in lokaler y-Richtung.
- **h_Z** ∈ ℝ⁺: **Zapfenhöhe** (in mm), 0 < h_Z ≤ h_B − 2ε_L;
  die Ausdehnung des Zapfen-Querschnitts in lokaler z-Richtung.
- **y_Z** ∈ ℝ: **y-Position der Zapfen-Mitte** (in mm) im
  Bauteil-Lokal-System; typischer Standardwert b_B/2 (achsmittig).
- **z_Z** ∈ ℝ: **z-Position der Zapfen-Mitte** (in mm) im
  Bauteil-Lokal-System; typischer Standardwert h_B/2 (achsmittig).
- **κ** ∈ ℝ: **Konizitätswinkel** (in rad), 0 ≤ κ < π/4; κ = 0
  entspricht dem rechteckigen Kantzapfen, κ > 0 dem
  Schwalbenschwanz-Zapfen mit nach hinten zunehmender Breite
  (BTLx-Parameter `ConeAngle`).

Die **Zapfen-Hervorragung** Z(p_Zapfen) ⊂ ℝ³ ist im Bauteil-
Lokal-System der abgeschlossene Polyeder

```
Z(p_Zapfen) := { (x, y, z) ∈ ℝ³ :
    ℓ_B − ℓ_Z  ≤  x  ≤  ℓ_B,
    |y − y_Z|  ≤  w_Z/2  +  (ℓ_B − x) · tan κ,                    (2)
    |z − z_Z|  ≤  h_Z/2 }.
```

Für κ = 0 ist Z ein achsparalleler Quader; für κ > 0 ein
abgeschnittener Pyramidenstumpf mit Schwalbenschwanz-Querschnitt
in der xy-Ebene.

Sei G_B^lokal ⊂ ℝ³ die ungeschwächte Bauteilgeometrie im
Bauteil-Lokal-System (siehe `hg_bauteil.md`,
`hg_bauteilkoerper.md`); für einen rechteckigen Stab-
Querschnitt entspricht G_B^lokal dem Quader
[0, ℓ_B] × [0, b_B] × [0, h_B].

Der **Werkzeugkörper** der Zapfen-Bearbeitung ist die
**Vereinigung der vier Wangen-Quader** am Bauteilend-Bereich,
die das Material entfernen, das den Zapfen-Querschnitt
umgibt — analog zur Konstruktion einer Bohrung mit
Durchgangs-Effekt. Konkret:

```
W_y^- := { (x, y, z) ∈ ℝ³ :
            ℓ_B − ℓ_Z ≤ x ≤ ℓ_B,
            0 ≤ y ≤ y_Z − w_Z/2 − (ℓ_B − x) · tan κ,
            0 ≤ z ≤ h_B }

W_y^+ := { (x, y, z) ∈ ℝ³ :
            ℓ_B − ℓ_Z ≤ x ≤ ℓ_B,
            y_Z + w_Z/2 + (ℓ_B − x) · tan κ ≤ y ≤ b_B,
            0 ≤ z ≤ h_B }

W_z^- := [ℓ_B − ℓ_Z, ℓ_B] × [0, b_B] × [0,         z_Z − h_Z/2]
W_z^+ := [ℓ_B − ℓ_Z, ℓ_B] × [0, b_B] × [z_Z + h_Z/2, h_B]

K_Zapfen(p_Zapfen) := (W_y^- ∪ W_y^+ ∪ W_z^- ∪ W_z^+) ∩ G_B^lokal.        (3)
```

W_y^- und W_y^+ sind die **seitlichen Wangen** in lokaler
y-Richtung; W_z^- und W_z^+ sind die **oberen und unteren
Wangen** in lokaler z-Richtung. Für κ = 0 sind alle vier
Wangen achsparallele Quader und damit konvexe Polyeder im
Sinne von `hg_polyeder.md` (`KonvexerPolyeder`); für κ > 0
sind W_y^- und W_y^+ konvexe Prismen mit trapezförmigem
xy-Querschnitt (eine begrenzende Fläche ist um κ gegen e_hat_y^B
geneigt), W_z^- und W_z^+ bleiben achsparallele Quader.

K_Zapfen ist damit eine **Vereinigung höchstens vier konvexer
Polyeder** und ein abgeschlossener, beschränkter (im
Allgemeinen **nicht-konvexer**) Polyeder im Sinne von
`hg_polyeder.md`. Im **typischen zimmermannsmässigen Fall**
(achsmittiger Zapfen mit z_Z = h_Z/2 + h_R für gleiche obere
und untere Restholz-Stärke, w_Z < b_B) ist K_Zapfen
zusammenhängend, aber nicht-konvex; im **Sonderfall**
w_Z = b_B (Zapfen über die volle Bauteilbreite, „Schlitz
und Zapfen"-Variante am hervorstehenden Bauteil) entfallen
W_y^- und W_y^+ und K_Zapfen reduziert sich auf die
**Vereinigung von zwei konvexen Quadern** (obere und untere
Wange); im Sonderfall h_Z = h_B (Zapfen über die volle
Bauteildicke) entfallen W_z^- und W_z^+ entsprechend.

Äquivalent gilt:

```
K_Zapfen(p_Zapfen) = { (x, y, z) ∈ G_B^lokal :
    ℓ_B − ℓ_Z ≤ x ≤ ℓ_B } \ Z(p_Zapfen),                          (3')
```

d. h. der Werkzeugkörper ist das Komplement der Zapfen-
Hervorragung innerhalb des Bauteilend-Bereichs. Die
Darstellung (3) ist die **konstruktive Form** (Vereinigung
konvexer Bausteine), (3') die **deskriptive Form** (Mengen-
Differenz). Beide bezeichnen dieselbe Punktmenge; (3) ist
die für die Implementierung verbindliche Konstruktion.

Ein **Zapfen** ist dann die Bearbeitung

```
F_Zapfen := (uuid, τ = Zapfen, p_Zapfen, T_F = identitaet,
             bezeichnung)                                          (4)
```

im Sinne von `hg_bearbeitung.md` Gleichung (Tupel-Definition),
deren Werkzeugkörper K_Zapfen(p_Zapfen) gemäss (3) gegeben ist.
Die lokale Platzierung T_F = id_SE(3) ist Standard (Werkzeug-
Bezugssystem ≡ Bauteil-Lokal), weil die Parameter (1) bereits
direkt im Bauteil-Lokal-System ausgedrückt sind.

Die **Wirkung** auf das Bauteil ist nach `hg_bearbeitung.md`
Gleichung (1):

```
G_B'(F_Zapfen)  :=  G_B^lokal  \  K_Zapfen(p_Zapfen)
                 =  G_B^lokal ∩ (ℝ³ \ K_Zapfen(p_Zapfen))         (5)

   =  (G_B^lokal  ∩  { x  <  ℓ_B − ℓ_Z })
       ∪  (G_B^lokal  ∩  Z(p_Zapfen)),
```

also: das ungeschwächte Bauteil **bis zur Zapfenwurzel** plus
**der Zapfen-Hervorragung selbst**. Die zweite Komponente ist
genau der „Zapfen-Stumpf" der zimmermannssprachlichen
Anschauung.

## Wohldefiniertheit

- **Existenz**: Für jedes Stab-Bauteil B mit hervorstehendem
  Bauteilende und jeden zimmermannsmässig vorkommenden Zapfen
  (einfacher Zapfen, Doppelzapfen-Halb-Element, Schlitz und
  Zapfen, Schwalbenschwanz) lässt sich (1)–(5) angeben.
  Mindestkonfiguration (einfacher achsmittiger Kantzapfen):
  ℓ_Z = h_B (Zapfenlänge ≈ Bauteildicke), w_Z = b_B/3,
  h_Z = h_B/3, y_Z = b_B/2, z_Z = h_B/2, κ = 0.
- **Eindeutigkeit der Identität**: über `uuid` nach
  RFC 9562 v7; vgl. `hg_bearbeitung.md` Wohldefiniertheit
  „Eindeutigkeit der Identität".
- **Eindeutigkeit der Wirkung**: Die Polyeder Z(p_Zapfen) und
  K_Zapfen(p_Zapfen) sind durch p_Zapfen eindeutig festgelegt
  (kanonische geometrische Konstruktion aus (2) und (3)). Die
  resultierende Bauteilgeometrie G_B' nach (5) ist damit
  eindeutig.
- **Äquivalenz der konstruktiven und deskriptiven Form (3)
  ↔ (3')**: Die Vereinigung der vier Wangen-Quader
  W_y^± ∪ W_z^± ist genau die Punktmenge im Bauteilend-
  Bereich [ℓ_B − ℓ_Z, ℓ_B] × [0, b_B] × [0, h_B], die
  **nicht** in Z(p_Zapfen) liegt: ein Punkt (x, y, z) in
  diesem Bereich liegt genau dann in einer der vier Wangen,
  wenn er die Zapfen-Querschnittsbedingung
  |y − y_Z| ≤ w_Z/2 + (ℓ_B − x) · tan κ und
  |z − z_Z| ≤ h_Z/2 (gleichzeitig) verletzt, also genau dann,
  wenn er **nicht** in Z liegt. Damit liefert (3) genau
  dieselbe Punktmenge wie (3').
- **Polyeder-Wohlgeformtheit als Vereinigung konvexer Bausteine**:
  Jede der vier Wangen W_y^±, W_z^± ist nach Konstruktion ein
  konvexer Polyeder (achsparalleler Quader für κ = 0; für
  κ > 0 sind W_y^± konvexe Prismen mit trapezförmigem
  xy-Querschnitt, weil die schräge Begrenzungsfläche
  y = y_Z ∓ (w_Z/2 + (ℓ_B − x) · tan κ) eine affine Halbraum-
  Grenze ist). Damit ist K_Zapfen nach (3) eine **endliche
  Vereinigung von vier konvexen Polyedern**, im Sinne der
  CSG-Konstruktion in `hg_polyeder.md` (Zeile 148–159) ein
  beschränkter, abgeschlossener, im Allgemeinen **nicht-
  konvexer** Polyeder. Die `hg_polyeder.md`-Definition
  lässt nicht-konvexe Polyeder explizit zu (Zeile 493: „Konkavität
  / Geschlecht > 0: nicht-konvexe Polyeder … sind **gültige**
  Polyeder; lediglich die Konvexitäts-Annotation ist dann
  false"). Die `KonvexerPolyeder`-Code-Eingrenzung
  (`hg_polyeder.md` Zeile 319–331) ist davon unberührt, weil
  jede einzelne Wange konvex ist und K_Zapfen als CSG-
  Vereinigung von vier `KonvexerPolyeder`-Instanzen dargestellt
  wird (siehe Implementierungshinweis); der Domänen-Typ
  `KonvexerPolyeder` muss die Vereinigung nicht selbst tragen.
- **Topologie von K_Zapfen**:
  - **Standardfall** (0 < w_Z < b_B und 0 < h_Z < h_B,
    achsmittig oder asymmetrisch): K_Zapfen ist
    **zusammenhängend, aber nicht-konvex** — vier Wangen
    rahmen die Zapfen-Hervorragung; zwei Wangen-Paare grenzen
    jeweils an gemeinsamen Eckkanten an.
  - **Sonderfall w_Z = b_B** (Schlitz und Zapfen am
    hervorstehenden Bauteil): W_y^± entfallen; K_Zapfen ist
    die **Vereinigung zweier disjunkter konvexer Quader**
    (obere und untere Wange) und damit **nicht
    zusammenhängend**.
  - **Sonderfall h_Z = h_B** (Zapfen über die volle
    Bauteildicke): W_z^± entfallen; K_Zapfen ist die
    Vereinigung zweier disjunkter konvexer Prismen
    (seitliche Wangen).
  - **Trivialfall w_Z = b_B und h_Z = h_B**: K_Zapfen wird
    leer, der Zapfen füllt den gesamten Bauteilend-Bereich.
    Dieser Fall ist durch die harten Invarianten
    w_Z ≤ b_B − 2ε_L bzw. h_Z ≤ h_B − 2ε_L ausgeschlossen.
- **Unabhängigkeit der Wahl des Werkzeug-Bezugssystems**: Die
  Parameter (1) sind direkt im Bauteil-Lokal-System
  ausgedrückt; die Wahl T_F = id_SE(3) ist konventionell. Eine
  äquivalente Parametrisierung im Welt-System würde dieselbe
  Wirkung (5) erzeugen (Glossar-übergreifend bewiesen in
  `hg_bearbeitung.md` Wohldefiniertheit).
- **Subtraktivität**: Strukturell aus (5) und
  `hg_bearbeitung.md` Gleichung (4):
  G_B' ⊆ G_B^lokal. Die ontologische Asymmetrie zum
  intuitiven Bauteilblick (Zapfen als „Form" / „Hervorragung")
  wird durch die Definition des Werkzeugkörpers als
  Komplement (3) konsistent in den subtraktiven Bearbeitungs-
  Rahmen eingebettet.
- **Plausibilität der Querschnittsschwächung** (weiche
  Invariante, nicht Bestandteil der Definition): Die
  Zapfenbreite-Faustregel w_Z ≈ b_B/3 nach
  DIN 1052 §15 / Berufssprache wird in der App als Warnung
  über `Toleranzen.ZAPFENBREITE_FAUSTREGEL_DRITTEL` geführt.
  Verletzung erzeugt eine Warnung; Validierungsfehler entsteht
  nur bei Verletzung der harten Bedingungen aus (1)
  (w_Z ≤ b_B − 2ε_L, h_Z ≤ h_B − 2ε_L, ℓ_Z ≤ ℓ_B − ε_L).
- **Nicht-Zirkularität**: Die Definition stützt sich nur auf
  bereits definierte Begriffe (`bearbeitung`, `bauteil`,
  `lokales_koordinatensystem`, `bauteilachse`, `stirnseite`,
  `rechteck_querschnitt`, `polyeder`, `toleranzen`). Sie kommt
  nicht in ihrer eigenen Definition vor; der komplementäre
  Begriff `zapfenloch` ist im `abgrenzung_zu:`-Feld geführt,
  aber **nicht** in der mathematischen Definition verwendet.

## Erläuterung (nicht normativ)

### Die Zapfenverbindung als Paar Zapfen ↔ Zapfenloch

Der Zapfen ist nie ein für sich stehendes geometrisches
Element; er existiert ausschliesslich als **eine Hälfte einer
Zapfenverbindung**, also einer komplementären Zwei-Bauteile-
Konstellation, in der der Zapfen am hervorstehenden Bauteil B₁
in das **Zapfenloch** (`zapfenloch`) am aufnehmenden Bauteil
B₂ eingreift. Die App-Ontologie zerlegt diese Gesamtverbindung
in:

- ein `zapfen`-Bearbeitung an B₁ (dieser Eintrag),
- ein `zapfenloch`-Bearbeitung an B₂ (Eintrag
  `hg_zapfenloch.md`),
- ein `verbindung`-Aggregat (`hg_verbindung.md`) mit
  `typ = ZimmermannsmaessigerAnschluss`, das die beiden
  Bauteile und ihre Bearbeitungen klammernd zusammenhält.

Diese Zerlegung folgt aus drei Konsistenz-Gründen:

1. **Bauteil-Lokalität der Bearbeitung** (siehe
   `hg_bearbeitung.md`): jede Bearbeitung gehört zu **genau
   einem** Bauteil. Die Zapfenverbindung lebt physisch an zwei
   Bauteilen und ist damit nicht eine einzelne Bearbeitung,
   sondern zwei.
2. **BTLx-Pendant 1:1**: BTLx 2.1 listet `Tenon` (Zapfen) und
   `Mortise` (Zapfenloch) als zwei eigenständige Processings
   an zwei verschiedenen Parts. Die Glossar-Struktur spiegelt
   diese Trennung exakt.
3. **Aggregation auf `verbindung`-Ebene**: die übergreifende
   Konzeption „Zapfenverbindung" wird durch
   `hg_verbindung.md` mit
   `VerbindungsTyp.ZimmermannsmaessigerAnschluss` getragen; ein
   eigenes Aggregat `zapfen_verbindung` ist nicht erforderlich.

### Wirkungsmechanismus

Die Zapfenverbindung überträgt Lasten in folgender Aufteilung:

- **Druck längs zur Faser des hervorstehenden Bauteils**:
  primär durch **Vollholz-Kontakt der Brust- bzw.
  Schulterflächen** des Zapfen-Bauteils auf die Kopf- bzw.
  Längsfläche des Zapfenloch-Bauteils. **Nicht** durch die
  Zapfenstirn — dort ist die **Zapfenluft** (5–10 mm) bewusst
  einberechnet, um die Krafteinleitung in die kontaktstarke
  Schulterfläche zu zwingen.
- **Querkraft / Schub rechtwinklig zur Bauteilachse**: durch
  den Zapfenschaft, der gegen die Lochwandung drückt;
  Bemessungs-Mechanismus: Druck rechtwinklig zur Faser des
  Zapfenloch-Bauteils (EC5 §6.1.5).
- **Zug längs der Bauteilachse**: bei der Standard-
  Zapfenverbindung **nicht direkt** durch den Zapfen
  übertragen. Zugfestigkeit entsteht entweder durch
  zusätzliche Sicherung (Holznagel, Keil; siehe
  `hg_verbindungsmittel.md`) oder durch die zugfeste
  Geometrie des **Schwalbenschwanz-Zapfens** in einer
  Richtung.
- **Biegung um Querachsen**: nur sehr eingeschränkt; die
  Zapfenverbindung wird in der Tragwerksanalyse klassisch
  als **gelenkartiger Anschluss** modelliert.

Daraus folgt die Charakterisierung des Zapfens als
**Positionssicherung mit Querkraft-Übertragung**, **nicht**
als Hauptdruckpfad in Achsrichtung. Diese Funktionalität ist
die Begründung für die Zapfenluft und für die geometrische
Faustregel w_Z ≈ b_B/3 (kleiner Zapfen = saubere
Lasttrennung; grosser Zapfen würde die Schulter schwächen).

### Zapfenluft und ihre ontologische Konsequenz

Die Zapfenlänge ℓ_Z ist im verbauten Zustand stets **kleiner
als die Tiefe des Zapfenlochs** (typisch um 5–10 mm). Diese
Differenz heisst **Zapfenluft**. Konsequenzen:

- **Geometrische Konsistenz**: beim Zusammenfügen der beiden
  Bauteile B₁ und B₂ liegen ihre kontaktrelevanten Flächen
  (Schulter von B₁ auf Kopf-/Längsfläche von B₂)
  formschlüssig aneinander; die Zapfenstirn liegt **nicht**
  auf dem Grund des Zapfenlochs auf.
- **Modellierungskonsequenz**: Die Zapfenlänge ℓ_Z am
  hervorstehenden Bauteil und die Zapfenloch-Tiefe ℓ_M am
  aufnehmenden Bauteil sind **unabhängige Parameter** der
  beiden Bearbeitungen. Die Konsistenz-Invariante
  ℓ_M ≥ ℓ_Z + Δ (mit Δ = Zapfenluft, typisch 5 mm) wird auf
  der **`verbindung`-Ebene** geprüft, nicht in der
  Zapfen-Definition selbst.

### Typologie der Zapfen-Varianten

Die DACH-Berufssprache kennt mehrere geometrische und
funktionale Varianten:

| Variante                | Geometrie                                                                                   | App-Modellierung |
|-------------------------|---------------------------------------------------------------------------------------------|------------------|
| **Einfacher Zapfen**    | ein achsmittiger Kantzapfen, κ = 0; Standardfall.                                          | eine `Zapfen`-Instanz |
| **Doppelzapfen**        | zwei parallele Zapfen nebeneinander; bei grosser Bauteildicke zur Vergrösserung der Schubfläche. | zwei `Zapfen`-Instanzen mit unterschiedlichen y_Z |
| **Schlitz und Zapfen** (*Gabelzapfen*) | Zapfen am hervorstehenden Bauteil + nach einer Seite offenes Zapfenloch am Gegenholz; Standard im Eck-/Kreuzanschluss.   | `Zapfen` + nach offener Seite parametrisiertes `zapfenloch` am Gegenholz |
| **Schwalbenschwanz-Zapfen** | konische Geometrie κ > 0 (typ. Steigung 1:7 bei Nadelholz, 1:8 bei Laubholz); zugfest in einer Richtung; klassisch Nebenträger ↔ Hauptträger. | `Zapfen` mit κ > 0; Folgearbeit: ggf. eigener Subtyp |
| **Brustzapfen**         | Zapfen mit zusätzlicher **Schulter** (flächiger Anschlag rechtwinklig zur Bauteilachse); druckfest, waagerecht/senkrecht unverschieblich; klassisch Balken-Wechsel. | `Zapfen` + zusätzliche `anschnitt`-Bearbeitung an der Schulterfläche |
| **Verkämmter Zapfen**   | Zapfenverbindung kombiniert mit Querverzahnung (Kamm) der Schulterflächen; alpine Schweizer Stuhlkonstruktionen Stuhlsäule ↔ Pfette. | `Zapfen` + `kamm`-Bearbeitung an den Schulterflächen |
| **Abgesetzter Zapfen**  | zweistufiger Zapfen-Schaft mit reduziertem Querschnitt; nimmt zwei Bauteile übereinander auf. | Folgearbeit: Parameter-Erweiterung oder eigener Subtyp |
| **Jagdzapfen**          | schräg eingedrehter Zapfen zum nachträglichen Einbau einer Strebe.                          | Folgearbeit |

Die App-Klasse `Zapfen` modelliert den einfachen Kantzapfen
und den Schwalbenschwanz-Zapfen direkt über die Parameter (1);
alle anderen Varianten entstehen durch **Kombination** mit
weiteren Bearbeitungen am selben Bauteilende. Insbesondere
ist der „verkämmte Zapfen" als alpine Schweizer
berufssprachliche Variante explizit modellierbar (über
`Zapfen` + `kamm`), erhält aber keinen eigenen
Glossareintrag — die Norm-Belege im verfügbaren Korpus
reichen nicht für eine eigenständige Definition.

### BTLx- und IFC-Übersetzung

| App-Konfiguration            | BTLx-Processing | IFC-Konstrukt |
|------------------------------|-----------------|---------------|
| `Zapfen` mit κ = 0           | `Tenon`         | Bauteilkörper-Body am Bauteilende (Form, nicht Subtraktion) |
| `Zapfen` mit κ > 0           | `DovetailTenon` | Bauteilkörper-Body am Bauteilende mit konischer Querschnittsverengung |
| `Zapfen` + `anschnitt`       | `Tenon` + Schulter-Processing | Bauteilkörper-Body mit zurückspringender Schulter |
| `Zapfen` + `kamm`            | `Tenon` + `House` | komplexer Bauteilkörper-Body |

**IFC-Asymmetrie zum Zapfenloch**: Während das Zapfenloch
in IFC unmittelbar als `IfcOpeningElement` mit
`IfcRelVoidsElement`-Beziehung modelliert wird, ist der
Zapfen in IFC **typischerweise keine Subtraktion**, sondern
**Teil der Body-Repräsentation des Bauteils selbst**. Diese
ontologische Asymmetrie ist eine Eigenschaft der Export-
Schicht (Phase 4) und steht nicht im Widerspruch zur
glossarinternen subtraktiven Modellierung: für die App-
Domänen-Schicht ist der Zapfen über (3) als subtraktiver
Werkzeugkörper definiert, der die Wangen entfernt; beim
IFC-Export wird die Wirkung in die Body-Repräsentation
zusammengeführt.

### Sicherung der Zapfenverbindung

Die Standard-Zapfenverbindung ist **nicht zugfest**.
Konstruktiv sichern den Zapfen gegen Herausziehen:

- **Holznagel**: querstehende, durch beide Bauteile geführte
  Stange aus hartem Holz; in der App als
  `verbindungsmittel`-Instanz mit eigener UUID modelliert
  (`hg_verbindungsmittel.md`).
- **Keil**: in den Zapfen oder neben den Zapfen eingetriebene
  Keile, die die Verbindung formschlüssig spannen.
- **Schwalbenschwanz-Geometrie**: bei κ > 0 ist die
  Zugfestigkeit in einer Richtung bereits geometrisch
  gegeben; keine zusätzliche Sicherung in dieser Richtung
  erforderlich.

Die Sicherung ist eine **eigene Element-Instanz** und nicht
Bestandteil der Zapfen-Definition.

### Tätigkeit vs. Resultat

Im zimmermannssprachlichen Sprachgebrauch bezeichnen
„Zapfen", „Verzapfung" und „Zapfen schlagen" sowohl die
Tätigkeit (Abbund) als auch das geometrische Resultat. Dieser
Glossareintrag definiert ausschliesslich die
**Resultatslesart**: das geometrische Merkmal am bearbeiteten
Bauteil. Die Tätigkeit (Stemmen, Sägen, Fräsen, CNC-
Programmierung) ist Gegenstand der Fertigungs-Schicht und
nicht im Glossar geführt.

## Beziehungen

- **Oberbegriff**: `bearbeitung` (`hg_bearbeitung.md`). Zapfen
  ist ein partitiver Subtyp der subtraktiven Bearbeitung am
  Bauteil; eigene UUID, gehört genau einem Bauteil, kaskadiert
  bei dessen Löschung.
- **Komplementäre Schwesterbearbeitung**: `zapfenloch`
  (`hg_zapfenloch.md`). Zapfen und Zapfenloch sind die zwei
  Hälften einer Zapfenverbindung; sie leben an zwei
  verschiedenen Bauteilen und werden durch ein
  `verbindung`-Aggregat klammernd zusammengehalten.
- **Verwendung**:
  - Bestandteil eines **Bauteils** (`bauteil`): der Zapfen
    erscheint in der Bearbeitungs-Liste seines hervorstehenden
    Bauteils.
  - Aggregiert über ein **Verbindungs-Aggregat**
    (`verbindung`) zusammen mit dem zugehörigen `zapfenloch`
    am Gegenholz; die Verbindungs-Instanz trägt
    `typ = ZimmermannsmaessigerAnschluss`.
  - Optional gesichert durch **Verbindungsmittel**
    (`verbindungsmittel`): Holznagel, Keil; eigene Element-
    Instanzen, nicht Teil des Zapfens.
- **Abgrenzung**:
  - **Zapfenloch** (`zapfenloch`, Schwester-Eintrag): die
    aufnehmende Aussparung am Gegenholz. Topologisch und
    ontologisch das Pendant zum Zapfen; gleicher Oberbegriff
    `bearbeitung`, aber an verschiedenem Bauteil.
  - **Kerve** (`kerve`): zweiflächiger Einschnitt aus der
    Unterseite eines Sparrens zur Auflagerung auf einer
    Pfette. Kerve liegt **mittig in der Bauteillänge** und
    schwächt das Bauteil von der Unterseite her; Zapfen liegt
    **am Bauteilende** und schwächt durch seitliche Wangen.
    Keine Funktions- und keine Geometrie-Überschneidung.
  - **Versatz** (`versatz`, Forward-Verweis): flache, schräge
    Druckfläche quer zur Faser am Bauteilende; trägt Druck
    schräg über eine grosse Druckfläche, **ohne**
    hervorstehenden Stift. Versatz und Zapfen sind beide
    am Bauteilende, aber topologisch verschieden:
    Versatz = Druckfläche, Zapfen = Stift.
  - **Blatt** (`blatt`, Forward-Verweis A,
    `HG_KONVENTIONEN.md` §6 Tabelle): flächige Längs-
    Überlappung (halbe Holzdicke abgetragen) zweier Bauteile
    in derselben Lage. Im Gegensatz zum Zapfen, der ein
    Stift in einem Loch ist, ist das Blatt eine Flächen-
    Überlappung.
  - **Kamm** (`kamm`, Forward-Verweis A): einseitige
    Materialwegnahme zur verzahnten Querverbindung am
    Kreuzungspunkt. Kann mit `Zapfen` kombiniert werden
    (verkämmter Zapfen), ist aber eigenständig als
    Bearbeitungs-Subtyp geführt.
  - **Bohrung** (`bohrung`, Forward-Verweis): zylindrische
    Subtraktion mit rundem Querschnitt. Zapfen-Querschnitt
    ist rechteckig (oder schwalbenschwanzförmig); ein
    Rundzapfen ist im DACH-Holzbau-Korpus selten und wird
    in dieser App nicht als Sonderfall des Zapfens, sondern
    ggf. als eigene Bearbeitung modelliert.
  - **Schlitz** (`schlitz`, Forward-Verweis): längliche
    Subtraktion mit geringer Breite und grosser Tiefe zur
    Aufnahme eines Schlitzblechs oder einer Lasche. Im
    DACH-Korpus terminologisch doppeldeutig (auch
    „Schlitz und Zapfen"); dort meint „Schlitz" die nach
    einer Seite offene Zapfenloch-Variante, **nicht** den
    Schlitz für Schlitzbleche.
  - **Anschnitt** (`anschnitt`, Forward-Verweis): planare
    Stirn- oder Schrägfläche am Bauteilende. Kann mit
    `Zapfen` kombiniert werden (Brustzapfen) und liefert die
    Schulterfläche, ist aber eigene Bearbeitung.
  - **Bearbeitung** (`bearbeitung`): Oberbegriff; trägt die
    generischen Eigenschaften (UUID, lokale Platzierung,
    Subtraktivität, Lebenszyklus-Kopplung).
  - **Verbindung** (`verbindung`): Aggregat aus Bauteilen +
    Verbindungsmitteln + Bearbeitungen an einem
    Knotenpunkt. Zapfen ist **keine Verbindung**, sondern
    eine Bearbeitung; die übergreifende „Zapfenverbindung"
    ist das `verbindung`-Aggregat mit
    `typ = ZimmermannsmaessigerAnschluss`.
  - **Verbindungsmittel** (`verbindungsmittel`): Element,
    das Kräfte zwischen ≥ 2 Bauteilen überträgt (Schraube,
    Bolzen, Holznagel, Klammer). Zapfen ist **kein
    Verbindungsmittel**, sondern die formgebende Bearbeitung
    des hervorstehenden Bauteils; das Holznagel-Pendant zum
    Sicherungs-Konzept liegt als eigene Element-Instanz vor.

## Implementierungshinweis

Datentyp (Domänen-Schicht, Kotlin, Schicht
`domain.bauteil.bearbeitung`):

```kotlin
package domain.bauteil.bearbeitung

import domain.geometrie.LokalePlatzierung
import java.util.UUID

/**
 * Zapfen — subtraktive Bearbeitung am Bauteilende, die durch
 * Entfernen der Wangen eine rechteckige (oder schwalbenschwanz-
 * förmige) Hervorragung entlang der Bauteilachse stehen lässt.
 *
 * Glossar: hg_zapfen.md.
 *
 * Komplementärbearbeitung: [Zapfenloch] am aufnehmenden
 * Bauteil (`hg_zapfenloch.md`); aggregiert über
 * `Verbindung` mit `typ = ZimmermannsmaessigerAnschluss`.
 */
data class Zapfen(
    override val uuid: UUID,
    override val lokalePlatzierung: LokalePlatzierung,
    override val bezeichnung: String?,
    /** Zapfenlänge in mm, > 0; siehe hg_zapfen.md (1) ℓ_Z. */
    val zapfenlaenge: Double,
    /** Zapfenbreite in mm, > 0; siehe hg_zapfen.md (1) w_Z. */
    val zapfenbreite: Double,
    /** Zapfenhöhe in mm, > 0; siehe hg_zapfen.md (1) h_Z. */
    val zapfenhoehe: Double,
    /** y-Position der Zapfen-Mitte im Bauteil-Lokal-System in mm.
     *  Default b_B/2 (achsmittig). */
    val yPosition: Double,
    /** z-Position der Zapfen-Mitte im Bauteil-Lokal-System in mm.
     *  Default h_B/2 (achsmittig). */
    val zPosition: Double,
    /** Konizitätswinkel in rad, 0 ≤ κ < π/4. κ = 0 entspricht
     *  dem Kantzapfen, κ > 0 dem Schwalbenschwanz-Zapfen. */
    val konizitaet: Double,
) : Bearbeitung
```

- **Einheit**: Längen in mm (Double); Konizitätswinkel in
  Radiant (Double, intern); Anzeige der Konizität in Grad ist
  Aufgabe der UI-Schicht. Lokale Platzierung als SE(3)-Element
  (Rotation + Translation), Standardwert `LokalePlatzierung.
  IDENTITAET`.
- **Identität**: `uuid` Pflicht und persistent (RFC 9562 v7);
  Bauteil-Zugehörigkeit über die Container-Beziehung in der
  Bearbeitungs-Liste des Bauteils (`hg_bearbeitung.md`); keine
  Backref am Zapfen-Objekt.
- **Toleranzen**:
  - `LAENGE_EPS` (mm): für Vergleiche der Längen-Parameter
    gegen Null und gegen die Bauteilgeometrie-Schranken
    (ℓ_Z ≤ ℓ_B − ε_L, w_Z ≤ b_B − 2ε_L, h_Z ≤ h_B − 2ε_L).
  - `WINKEL_EPS` (rad): für den Konizitäts-Vergleich
    (0 ≤ κ < π/4 − ε_W).
- **Invarianten** (in Fabrikfunktion / `init` prüfen, bei
  Verletzung `Resultat.Fehler` mit subtypspezifischer
  `BearbeitungAmBauteilUngueltig`-Variante zurückgeben, keine
  Exception):
  1. `zapfenlaenge > LAENGE_EPS`.
  2. `zapfenbreite > LAENGE_EPS`.
  3. `zapfenhoehe > LAENGE_EPS`.
  4. `0 ≤ konizitaet < π/4 − WINKEL_EPS`.
  5. `zapfenlaenge ≤ bauteillaenge − LAENGE_EPS`.
  6. `zapfenbreite ≤ bauteilbreite − 2·LAENGE_EPS`.
  7. `zapfenhoehe ≤ bauteildicke − 2·LAENGE_EPS`.
  8. Zapfen liegt vollständig im Bauteilquerschnitt
     (yPosition ± zapfenbreite/2 innerhalb [0, b_B] mit
     Toleranz, analog für z).
- **Weiche Plausibilitätsprüfung** (Warnung, kein
  Validierungsfehler):
  - `zapfenbreite ≈ bauteilbreite · TOLERANZEN.
    ZAPFENBREITE_FAUSTREGEL_DRITTEL` (default 1.0/3.0).
    Abweichungen erzeugen eine Warnung in der Bemessungs-
    Schicht, blockieren die Modellierung nicht.
- **Lebenszyklus / Komposition**: Eigentum genau eines
  Bauteils; bei Löschung kaskadiert (siehe
  `hg_bearbeitung.md`).
- **Berechnung der Wirkung**: nach `hg_bearbeitung.md`
  Gleichung (1) lazy on demand in der Geometrie-Schicht; die
  Domänen-Schicht hält ausschliesslich die Parameter, die
  Boole'sche Differenz ist Aufgabe von
  `domain.bauteil.geometrie.BearbeitungsAggregator`.
- **Werkzeugkörper-Konstruktion in Code** (Geometrie-Schicht,
  Folgearbeit): K_Zapfen wird gemäss Definition (3) als
  **Vereinigung von bis zu vier `KonvexerPolyeder`-Instanzen**
  konstruiert: W_y^- und W_y^+ (seitliche Wangen, Quader für
  κ = 0 bzw. konvexe trapezoide Prismen für κ > 0), W_z^- und
  W_z^+ (obere und untere Wangen, stets achsparallele Quader).
  Wangen mit Volumen ≤ `LAENGE_EPS³` werden weggelassen (Fall
  w_Z = b_B oder h_Z = h_B, dann reduziert sich K_Zapfen auf
  zwei Wangen). Jede Wange ist als `KonvexerPolyeder` über
  ihre Halbraum-Darstellung (H-Rep, sechs Halbräume für einen
  Quader, fünf bzw. sechs für ein konvexes Prisma mit
  trapezförmigem Querschnitt) konstruierbar; die Vereinigung
  ist eine CSG-Operation, die der `BearbeitungsAggregator`
  beim Anwenden der Bauteilkörper-Differenz (5) durchführt
  (`G_B' = G_B^lokal \ (W_y^- ∪ W_y^+ ∪ W_z^- ∪ W_z^+) =
  ((G_B^lokal \ W_y^-) \ W_y^+) \ W_z^-) \ W_z^+`,
  sukzessive Differenz mit den vier konvexen Wangen).
- **BTLx-Export** (Persistenzschicht, Phase 4):
  - `Zapfen` mit `konizitaet = 0` → BTLx-Processing `Tenon`
    mit Parametern `ReferencePlaneId`, `StartX`, `StartY`,
    `StartDepth = 0`, `Angle = 0`, `Inclination = 0`,
    `Length = zapfenlaenge`, `Width = zapfenbreite`,
    `Height = zapfenhoehe`.
  - `Zapfen` mit `konizitaet > 0` → BTLx-Processing
    `DovetailTenon` mit `ConeAngle = konizitaet`.
- **IFC-Export** (Persistenzschicht, Phase 4):
  - Asymmetrisch zum Zapfenloch (`zapfenloch` →
    `IfcOpeningElement`): der Zapfen wird **nicht** als
    eigenständiges IFC-Subtraktionselement exportiert,
    sondern in die Body-Repräsentation
    (`IfcProductRepresentation`) des Bauteils selbst
    eingerechnet — die Bauteilgeometrie nach Bearbeitung
    (G_B' nach (5)) ist der IFC-Body. Die Bearbeitungs-UUID
    wird als `IfcPropertySet`-Eintrag mit Verweis auf das
    BTLx-Processing geführt.
- **Edge Cases**:
  - **Zapfenlänge grösser als Bauteilrest**: ℓ_Z > ℓ_B − ε_L
    → Validierungsfehler
    `ZapfenLaengeUeberschreitetBauteil`.
  - **Zapfen nicht achsmittig**: y_Z oder z_Z so verschoben,
    dass die Zapfen-Hervorragung über den Bauteilquerschnitt
    hinausragt → Validierungsfehler
    `ZapfenPositionAusserhalbQuerschnitt`.
  - **Konizität in negative Richtung**: κ < 0 ist verboten
    (käme einer „Hinterschneidung am Stumpf" gleich, die
    geometrisch nicht durch Wangen-Wegnahme realisierbar
    wäre) → Validierungsfehler `ZapfenKonizitaetNegativ`.
  - **Zapfen am Bauteilanfang statt Bauteilende**: durch
    Drehung des Bauteil-Lokal-Systems abbildbar; die
    Standardform dieses Eintrags definiert den Zapfen am
    Ende (x = ℓ_B). Eine alternative Konvention „Zapfen am
    Anfang" ist über `LokalePlatzierung` mit Rotation um
    π um e_hat_y^B oder e_hat_z^B parametrisierbar.
  - **Mehrere Zapfen am selben Bauteilende** (Doppelzapfen):
    zulässig; jeder Zapfen ist eine eigene Bearbeitungs-
    Instanz mit eigener UUID in der Bauteil-
    Bearbeitungsliste, unterschiedlichen y_Z (oder z_Z) und
    eventuell unterschiedlichen Breiten.
- **Bezeichner-Konvention** (`docs/_CODE_KONVENTIONEN.md`):
  Domänen-Klasse `Zapfen` (deutsch, Glossarbegriff);
  Parameter `zapfenlaenge`, `zapfenbreite`, `zapfenhoehe`,
  `yPosition`, `zPosition`, `konizitaet`.

## Quellen

**Primär (normativ):**

- DIN EN 1995-1-1:2010-12, „Eurocode 5: Bemessung und
  Konstruktion von Holzbauten – Teil 1-1", Abschnitt 6.1.5
  (Druck rechtwinklig zur Faser).
- DIN EN 1995-1-1/NA:2013-08, Nationaler Anhang Deutschland.
- DIN 1052:2008-12, „Entwurf, Berechnung und Bemessung von
  Holzbauwerken", Abschnitt 15 (Zimmermannsmässige
  Verbindungen).
- SIA 265:2021, „Holzbau", Schweizerischer Ingenieur- und
  Architektenverein, Zürich, Anhang A.
- design2machine: *BTLx interface description*, Version 2.1,
  16.11.2023, Processings `Tenon` und `DovetailTenon`.

**Sekundär:**

- Mönck, W.; Rug, W.: *Holzbau – Bemessung und Konstruktion.*
  16. Auflage, Beuth, Berlin 2015, Kap. 7.
- Blass, H. J.; Sandhaas, C.: *Ingenieurholzbau – Grundlagen
  der Bemessung.* KIT Scientific Publishing, Karlsruhe 2016,
  Kap. 8.
- Gerner, M.: *Fachwerk – Instandsetzung, Sanierung, Neubau.*
  DVA, 7. Auflage 2007.
- Natterer, J.; Herzog, T.; Volz, M.: *Holzbau-Atlas.*
  4. Auflage, Birkhäuser, Basel 2003.
- Krämer, F.: *Grundwissen des Zimmerers.* Bruderverlag,
  Karlsruhe.
- Claus, T.: *Zapfenverbindungen im Holzbau – bruchmechanische
  Analyse und Vorschlag eines Berechnungsmodells.* Bautechnik
  97 (2020), Wiley.
- Lignum (Hrsg.): *Holzbautabellen HBT.* Lignum, Zürich.
- Informationsdienst Holz: *Tragverhalten zimmermannsmässiger
  Holzverbindungen.*

**Korpus (nicht autoritativ):**

- Wikipedia, Lemma „Zapfenverbindung" (abgerufen 2026-05-14).
- Wikipedia, Lemma „Mortise and tenon" (abgerufen 2026-05-14).
- baunetzwissen.de, „Zimmermannsmässige Verbindungen".
- baubeaver.de, „Über 34 zimmermannsmässige Holzverbindungen".
- bauredakteur.de, „Holzverbindungen — so machen es Zimmerer
  und Schreiner".
- zimmerer-treff.com, „Zapfenverbindungen".
- schreiner-seiten.de, „Schlitz und Zapfen — Traditionelle
  Holzverbindung".

**Recherche-Bericht:**

- `docs/recherche/2026-05-14_hg_zapfen.md` (2026-05-14):
  Konsolidierte Recherche zu Zapfen und Zapfenloch.
