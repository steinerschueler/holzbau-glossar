---
id: stuhlsaeule
benennung: Stuhlsäule
synonyme: [Stuhlpfosten, Binderstiel, Stuhlstiel]
abgelehnte_benennungen: [Stuhl, Säule, Bundpfosten, Pfosten, Ständer, "king post (engerer Sinn)", "queen post"]
oberbegriff: bauteil
begriffstyp: bauteilrolle
voraussetzungen: [bauteil, bauteilachse, strecke, einheitsvektor, weltkoordinatensystem, toleranzen]
abgrenzung_zu: [stuetze, saeule, haengesaeule, staender, pfette, stuhlpfette, stuhlschwelle, dachstuhl, stehender_stuhl, liegender_stuhl, stuhl, stuhlwand, kopfband, fussband, sparren, spannriegel, kehlbalken, strebe, strebesaeule, bauteil]
status: entwurf
theorie_pflichtig: required
quellen_primär:
  - "SIA 265:2021 'Holzbau', Schweizerischer Ingenieur- und Architektenverein, §1.1 Fachausdrücke [via: Lignum-Pressemitteilung 2021 'Anwendungshilfen für neue SIA-Norm Holzbau liegen vor']: Stuhl-Konstruktion und Stuhlsäule als Standard-Dachtragwerks-Bauteilrolle in der CH-Holzbau-Norm. Volltext nicht direkt eingesehen."
  - "DIN EN 1995-1-1:2010-12 (Eurocode 5), Abschnitt 9 (Bauliche Einzelheiten): Stuhl-Konstruktionen als Sonderform des Pfettendachs vorausgesetzt; Stuhlsäule nicht eigenständig lemmatisiert."
quellen_sekundär:
  - "Lignum (Hrsg.): Pressemitteilung 2021 'Anwendungshilfen für neue SIA-Norm Holzbau liegen vor', lignum.ch/auf_einen_klick/news/."
  - "Lignum (Hrsg.): Holzbautabellen HBT 1 (2024). Lignum, Zürich. Begriffsregister 'Stuhlsäule' (Volltext nicht zugänglich, Verlags-Schaufenster)."
  - "Holzer, S.; Steiger, R.: ETH Zürich, Lehrunterlage 'Holz IV — Dachwerke mit liegendem Stuhl', FS 2023 — Stuhl-Konstruktionen mit liegenden Stuhlsäulen als CH-Lehrkanon. Indirekt via hg_dachstuhl.md-Frontmatter."
  - "Mönck, W.; Rug, W.: Holzbau – Bemessung und Konstruktion. 16. Aufl., Beuth, Berlin 2015, Kap. 11 'Dachtragwerke', Pfettendach mit Stuhl-Konstruktion."
  - "Natterer, J.; Herzog, T.; Volz, M.: Holzbau-Atlas. 4. Aufl., Birkhäuser, Basel 2003, Kap. 'Dachtragwerke / Stuhl-Konstruktionen'."
  - "Gerner, M.: Fachwerk – Instandsetzung, Sanierung, Neubau. DVA, 7. Aufl. 2007, Glossar 'Stuhlsäule', 'Stuhlrähm', 'Stuhlschwelle'."
  - "Krämer, V.: Grundwissen des Zimmerers. 2. Aufl., Bruderverlag, Karlsruhe 1988 — Standardwerk der Zimmerer-Berufssprache."
  - "Thesaurus Traditioneller Holzbau (TTH), RWTH Aachen, Hierarchie-Facette 1922 'Fachwerk-Bauteile' — 'Stuhlsäule' als belegtes Lemma; Quelle Großmann 1987."
  - "Wikipedia, Lemma 'Dachstuhl' (de.wikipedia.org/wiki/Dachstuhl): 'Bei einer hölzernen Stuhlkonstruktion in einem Dachtragwerk werden die Stützen beziehungsweise Stiele auch als Stuhlpfosten, Stuhlsäulen oder Binderstiele bezeichnet.'"
  - "Wikipedia, Lemma 'Stehender Stuhl' (de.wikipedia.org/wiki/Stehender_Stuhl) — einfach/doppelt/mehrfach stehend, Bauteil-Familie Stuhlsäule + Stuhlpfette + Stuhlschwelle + Kopfband + Fußband bildet die Stuhlwand."
  - "Wikipedia, Lemma 'Liegender Stuhl' — schräggestellte Stuhlsäulen mit Spannriegel; stützenfreier Dachraum."
  - "Recherche-Bericht: docs/recherche/2026-05-16_tragglieder_vertikal.md §E."
quellenkonflikt: |
  Sechs Punkte sind in der Recherche
  (`docs/recherche/2026-05-16_tragglieder_vertikal.md` §E)
  auflösungs-bedürftig und werden hier ausdrücklich festgelegt.

  **(1) Druck-Element-Charakter.** Die Stuhlsäule ist im
  Dachstuhl-Tragwerk konstitutiv **Druck-Element**: sie nimmt die
  Pfetten-Auflagerlast (Dachflächen-Gewicht, Schnee, Wind über die
  Sparren in die Pfette) am Säulen-Kopf auf und leitet sie über
  ihre lotrechte oder schräge Bauteilachse in die Stuhlschwelle
  oder direkt in die Geschossdecke ein. Dies unterscheidet sie
  fundamental von der **Hängesäule** (`hg_haengesaeule.md`), die
  Zug-Element ist.

  Eigene Festlegung: Der Druck-Element-Charakter ist
  **konstitutiver Bestandteil** der Bauteilrolle Stuhlsäule. Eine
  Stuhlsäule, die im Lastfall Zug trüge (z. B. durch Abheben des
  Dachs bei Sog), wäre konzeptuell keine Stuhlsäule mehr, sondern
  eine umgekehrte Hängesäule. Die Bauteilrolle wird über die
  **topologische Einbindung** in den Dachstuhl ausgezeichnet
  (Stuhlpfetten-Anschluss am Kopf, Stuhlschwellen-/Decken-Anschluss
  am Fuß), nicht über die geometrische Stab-Form allein.

  **(2) Stehender vs. liegender Stuhl.** Wikipedia/Stehender Stuhl
  und Wikipedia/Liegender Stuhl trennen zwei Hauptvarianten:

  - **Stehender Stuhl**: Stuhlsäulen lotrecht (parallel zur
    Lotachse, e_z-Richtung). Sub-Varianten:
    - *Einfach stehend*: eine Längsreihe lotrechter Stuhlsäulen
      unter dem First, trägt Firstpfette oder mittiges Kehlbalken-
      Lager.
    - *Doppelt stehend*: zwei Reihen, je eine Stuhlsäule pro
      Sparrengespärre links und rechts der Mitte, tragen die
      Mittelpfetten.
    - *Mehrfach stehend*: Kombinationen.
  - **Liegender Stuhl**: Stuhlsäulen **schräg geneigt** (typisch
    in der Sparrenebene, vom Stuhlschwellen-Punkt zur Spann-
    riegel-Auflage geneigt). Vorteil: stützenfreier Innenraum,
    Lastpfad geht direkt in die Wand-Auflager statt in die
    Feldmitte der Decke.

  Eigene Festlegung: Die Stuhlsäule deckt **beide Varianten** ab
  (lotrecht und schräg). Die geometrische Bedingung 2 in der
  mathematischen Definition lockert die Lotrechtheits-Anforderung
  zugunsten einer **schwächeren Bedingung** (Stab-Achse hat
  positive z-Komponente und Anschluss an eine Stuhlpfette oben).
  Sub-Spezialisierungen `stehende_stuhlsaeule` und
  `liegende_stuhlsaeule` sind als Folgearbeit-Trigger
  dokumentiert.

  **(3) Stuhlpfette-Anschluss als topologisches Anker-Merkmal.**
  Die Stuhlsäule ist konstitutiv durch den **Anschluss an eine
  Stuhlpfette** am Säulen-Kopf charakterisiert; ohne diesen
  Anschluss ist sie keine Stuhlsäule, sondern eine allgemeine
  Stütze. Die Stuhlpfette ihrerseits trägt die Sparren oder
  Kehlbalken; der Lastpfad geht von der Dachfläche über Sparren →
  Stuhlpfette → Stuhlsäule → Stuhlschwelle / Geschossdecke.

  Eigene Festlegung: Das Anker-Merkmal „Stuhlpfetten-Anschluss"
  ist Bedingung 4 in der mathematischen Definition. Die
  Stuhlpfette ist im aktuellen Glossarstand als Pfetten-
  Spezialisierung Folgearbeit (`hg_stuhlpfette.md`), wird hier
  als Forward-Verweis geführt.

  **(4) Stuhlwand-Bauteilgruppe als Folgearbeit-Trigger.**
  Wikipedia/Stehender Stuhl führt die **Stuhlwand** als
  Bauteilgruppe aus Stuhlsäule + Stuhlpfette + Stuhlschwelle +
  Kopfband + Fußband (Längsverband-Aussteifung des Dachstuhls).
  Die Stuhlwand ist konzeptuell eine **Bauteilgruppe** (analog
  `hg_wand.md` für die Wandebene, oder `hg_walm.md` für den
  Walm-Bereich), die im aktuellen Glossarstand nicht angelegt
  ist.

  Eigene Festlegung: `hg_stuhlwand.md` ist als Folgearbeit-
  Trigger dokumentiert (analog `hg_walm.md`, `hg_binder.md`,
  `hg_dachstuhl.md`). Die Mitgliedschaft der Stuhlsäule in einer
  Stuhlwand-Bauteilgruppe wird beim Anlegen dieser Bauteilgruppe
  über die Aggregat-Mitgliedschaft modelliert.

  **(5) Stuhlsäulenkopf-Kämpfer als Konstruktionsdetail-
  Folgearbeit.** Am Kopf der Stuhlsäule wird die Stuhlpfette über
  ein **Kämpfer-Detail** (zimmermannsmäßiger Versatz mit Zapfen
  und gegebenenfalls Kopfband-Anschluss) aufgenommen. Dieses
  Konstruktionsdetail ist eine eigene Detail-Klasse (analog
  `hg_konstruktionsdetail.md` aus `20_tragwerk/`), nicht eine
  Bauteilrolle. Folgearbeit-Trigger bei einer Dachstuhl-Aggregat-
  Welle, die Konstruktionsdetails explizit modelliert.

  **(6) „Stuhlbalken" als Synonym oder regionaler Begriff zur
  Stuhlschwelle.** Im DACH-Korpus tritt „Stuhlbalken" gelegentlich
  als Synonym oder regionale Variante zu „Stuhlschwelle"
  (horizontales Auflager am Stuhlsäulen-Fuß) auf. Die TTH-Linie
  führt „Stuhlschwelle" als Standard-Lemma. Im aktuellen
  Glossarstand ist weder „Stuhlbalken" noch „Stuhlschwelle" als
  eigener HG-Eintrag geführt; beide sind als Folgearbeit-Trigger
  dokumentiert. „Stuhlbalken" wird gegebenenfalls als Synonym in
  `hg_stuhlschwelle.md` aufgenommen.

  Eigene Festlegung: Der Fuss-Anschluss der Stuhlsäule (Bedingung
  5 in der mathematischen Definition) wird auf einen
  **horizontalen Balken** verwiesen (Stuhlschwelle, Geschoss-
  Deckenbalken, Bundbalken — je nach Konstruktion), ohne den
  Anschluss-Balken-Typ vorzuschreiben.
---

## Prosa-Definition

Eine **Stuhlsäule** ist eine holz-spezifische Bauteilrolle im
Dachstuhl, deren Bauteilachse lotrecht (im stehenden Stuhl) oder
schräg in der Sparrenebene (im liegenden Stuhl) verläuft, deren
oberer Endpunkt an eine Stuhlpfette anschließt und deren unterer
Endpunkt auf einem horizontalen Auflagerbalken (Stuhlschwelle,
Geschoss-Deckenbalken oder Bundbalken) aufliegt, wobei sie als
Druck-Element die Pfetten-Auflagerlast in die Stuhlschwelle oder
das darunterliegende Tragwerk weiterleitet.

## Mathematische Definition

Sei

- B ein Bauteil im Sinne von `bauteil` mit Stabgeometrie
  (`geometrie ∈ 𝒢_stab`),
- a(B) = Bauteilachse.Gerade(p_a, p_e) die Bauteilachse von B im
  geraden Fall (siehe `bauteilachse`), mit
  d̂ := (p_e − p_a) / ‖p_e − p_a‖ ∈ S² ⊂ ℝ³,
- P eine Stuhlpfette (Pfetten-Spezialisierung im Dachstuhl, im
  aktuellen Glossarstand Forward-Verweis `stuhlpfette`) mit
  Bauteilachse a(P) = (p_a^P, p_e^P),
- T ein horizontaler Auflagerbalken (Stuhlschwelle, Geschoss-
  Deckenbalken oder Bundbalken) mit Bauteilachse a(T),
- e_z := (0, 0, 1)ᵀ die vertikale Welt-Achse,
- ε_K := Toleranzen.KOLLINEAR_EPS,
- ε_L := Toleranzen.LAENGE_EPS,
- ε_W := Toleranzen.WINKEL_EPS.

Dann heißt B eine **Stuhlsäule** mit zugehöriger Stuhlpfette P und
Auflagerbalken T genau dann, wenn die folgenden Bedingungen alle
erfüllt sind:

1. **Stabgeometrie**: B besitzt eine gerade Bauteilachse mit
   ‖p_e − p_a‖ > ε_L.

2. **Aufstrebende Bauteilachse** (gelockerte Lotrechtheit für die
   liegende Variante): Die Bauteilachse hat eine **positive
   z-Komponente** (Kopf liegt höher als Fuß),
   ```
   p_a.z + ε_L < p_e.z.
   ```
   Die Lotrechtheit selbst (‖d̂ × e_z‖ ≤ ε_K) ist im **stehenden
   Stuhl** erfüllt, im **liegenden Stuhl** jedoch nicht (die Stuhl-
   säule ist schräg geneigt). Die Bedingung 2 lockert die
   Lotrechtheit und fordert nur die aufstrebende Orientierung.

3. **Vorzeichenkonvention Fuß → Kopf**: Der untere Endpunkt p_a
   liegt auf dem Auflagerbalken T, der obere Endpunkt p_e an der
   Stuhlpfette P. Die Bauteilachse ist vom Fuß (unten, am Auflager)
   zum Kopf (oben, an der Stuhlpfette) gerichtet.

4. **Stuhlpfetten-Anschluss am Kopf**: Der obere Endpunkt p_e liegt
   auf der Stuhlpfetten-Bauteilachse a(P) bis auf Toleranz,
   ```
   dist(p_e, a(P)) ≤ ε_L,
   ```
   wobei dist(p, a) der Punkt-Geraden-Abstand zur Pfetten-Achse
   ist. Die Stuhlpfette ist horizontal,
   ```
   |⟨d̂_P, e_z⟩| ≤ ε_K,
   ```
   d. h. ihre Achse steht rechtwinklig zur Lotachse.

5. **Auflagerbalken-Anschluss am Fuß**: Der untere Endpunkt p_a
   liegt auf der Bauteilachse a(T) eines horizontalen
   Auflagerbalkens bis auf Toleranz,
   ```
   dist(p_a, a(T)) ≤ ε_L.
   ```
   Der Auflagerbalken T ist horizontal (analog zur Pfette) oder
   ein Geschoss-Deckenbalken / Bundbalken.

6. **Druck-Lastpfad-Zusicherung (qualitativ, nicht formal geprüft)**:
   B trägt im Dachstuhl-Tragwerk primär Drucklasten entlang der
   Bauteilachse (Pfetten-Auflagerlast am Kopf → Bauteilachse →
   Auflagerbalken am Fuß). Die formale Lastpfad-Verifikation ist
   Aufgabe des `hg_statisches_system`-Eintrags und wird hier
   zugesichert, nicht überprüft.

Wesentliche abgeleitete Größen:

- **Stuhlsäulenlänge**: L_SS := ‖p_e − p_a‖ (in mm).
- **Stuhlsäulen-Neigung**: α := acos(⟨d̂, e_z⟩) (in rad). Im
  stehenden Stuhl gilt α ≤ ε_W (Lotrechtheit); im liegenden Stuhl
  ist α > ε_W (typisch 15°–35° gegen die Lotachse).
- **Stuhlsäulen-Variante**: V := stehend, wenn α ≤ ε_W; sonst
  liegend.

## Wohldefiniertheit

- **Existenz**: Für jede Stuhlsäule in einem stehenden oder
  liegenden Stuhl (Wikipedia/Stehender Stuhl, Wikipedia/Liegender
  Stuhl, ETH-Lehrunterlage Holzer/Steiger „Holz IV") sind alle
  Bedingungen 1–6 konstruktiv erfüllbar.
- **Eindeutigkeit der Stuhlsäulen-Orientierung**: Bedingung 3
  fixiert die Achsen-Richtung vom Fuß zum Kopf (positive z-
  Komponente).
- **Disjunktheit zur Stütze**: Eine allgemeine Stütze
  (`hg_stuetze.md`) ohne Stuhlpfetten-Anschluss qualifiziert nicht
  als Stuhlsäule. Bedingung 4 ist konstitutiv.
- **Disjunktheit zur Hängesäule**: Eine Hängesäule trägt Zug am
  unteren Endpunkt (hängender Bundbalken-Anker) und Zug an den
  Strebe-Schnittpunkten oben; sie ist kein Druck-Element.
  Bedingung 6 schließt die Hängesäule aus, weil deren Lastpfad
  invertiert ist.
- **Konsistenz mit `bauteil`**: Alle Bedingungen aus `bauteil`
  sind erfüllt; die Bauteilrolle Stuhlsäule ergänzt die Lage- und
  Topologie-Constraints 1–6.
- **Stehender vs. liegender Stuhl als Sub-Spezialisierung**: Die
  Definition deckt beide Varianten ab; Sub-Spezialisierungen
  `stehende_stuhlsaeule` und `liegende_stuhlsaeule` sind als
  Folgearbeit dokumentiert. Die Diskriminierung erfolgt über die
  Stuhlsäulen-Neigung α.
- **Holz-Exklusivität**: Die Stuhlsäule ist konstitutiv holz-
  spezifisch. In Stahl-/Stahlbeton-Dachtragwerken gibt es keine
  Stuhlsäule, sondern andere Tragsysteme (Stahlbinder, Rahmen-
  binder, Fachwerkbinder). Diese Holz-Exklusivität ist Grund für
  die Cluster-Verortung in `30_holzbau/`.
- **Nicht-Zirkularität**: Die Definition stützt sich nur auf
  bereits definierte Begriffe (`bauteil`, `bauteilachse`,
  `strecke`, `einheitsvektor`, `weltkoordinatensystem`,
  `toleranzen`). Forward-Verweise (`stuhlpfette`, `stuhlschwelle`,
  `stehender_stuhl`, `liegender_stuhl`, `stuhl`, `stuhlwand`,
  `spannriegel`) sind nach HG_KONVENTIONEN.md §6 zulässig.

## Erläuterung (nicht normativ)

Die Stuhlsäule ist im **zimmermannsmäßig gefertigten Dachstuhl**
das vertikale oder schräge Tragglied, das die **Stuhlpfette** als
Last-Verteil-Element zwischen den Sparren und der darunterliegenden
Geschossdecke / Stuhlschwelle einhängt. Sie ist eines der
Inbegriff-Bauteile des Pfettendachs mit Stuhl-Konstruktion und
deckt einen breiten konstruktiven Bedeutungsraum ab.

### Funktion und Lastpfad

Der Lastpfad eines Dachstuhls mit Stuhl-Konstruktion geht
typischerweise:

1. **Dachhaut** (Eindeckung, Lattung) → **Sparren** (geneigte
   Stab-Bauteile entlang der Falllinie),
2. **Sparren** → **Stuhlpfette** (horizontaler Längsträger
   zwischen Sparren-Mitte),
3. **Stuhlpfette** → **Stuhlsäule** (Druck-Element),
4. **Stuhlsäule** → **Stuhlschwelle** oder direkt **Decken-
   balken** (horizontaler Auflagerbalken),
5. **Stuhlschwelle / Deckenbalken** → **Aussenwände** oder
   **innere tragende Wände** → **Fundament**.

Die Stuhlsäule ist damit Bestandteil eines **lastpfad-bündelnden
Sub-Tragwerks** im Dachstuhl, das den Lastpfad nicht direkt durch
die Sparren-Verlängerung führt, sondern auf einen separaten
Stütz-Stiel verschiebt — was den Vorteil hat, dass die Sparrenlängen
unabhängig von der Geschosstiefe optimiert werden können.

### Stehender Stuhl

Im **stehenden Stuhl** sind die Stuhlsäulen **lotrecht**. Sub-
Varianten:

- **Einfach stehend**: eine Längsreihe lotrechter Stuhlsäulen
  unter dem First; trägt die Firstpfette oder ein mittiges
  Kehlbalken-Lager. Typisch für kleinere Spannweiten und mittlere
  Dachneigungen.
- **Doppelt stehend**: zwei Reihen lotrechter Stuhlsäulen pro
  Sparrengespärre (links und rechts der Mitte); tragen die zwei
  Mittelpfetten. Standard-Konstruktion für grössere Spannweiten
  und Dachneigungen über 30°.
- **Mehrfach stehend**: Kombinationen aus First- und Mittel-
  Stuhlsäulen für sehr grosse Spannweiten oder mehrgeschossige
  Dachaufbauten.

### Liegender Stuhl

Im **liegenden Stuhl** sind die Stuhlsäulen **schräg geneigt** —
typisch von der Stuhlschwellen-Auflage am Geschossdecken-Rand zur
Spannriegel-Auflage oben in der Mitte. Der schräge Lastpfad hat
zwei wesentliche Vorteile:

- **Stützenfreier Innenraum**: die Stuhlsäulen stehen nicht in
  der Feldmitte der Decke, sondern an den Auflagern; der unter
  dem Dach liegende Raum bleibt frei (Speicher, Dachgeschoss-
  Wohnraum).
- **Reduziertes Biegemoment im Deckenbalken**: weil die Last nahe
  am Auflager eingeleitet wird, statt in der Feldmitte.

Der **Spannriegel** als oberes Querholz zwischen den geneigten
Stuhlsäulen ist konstitutiv für den liegenden Stuhl. Historisch
ab etwa 1400 belegt; in der CH-Praxis (ETH-Lehrkanon Holzer/
Steiger „Holz IV") aktiv unterrichtet.

### Bauteil-Familie der Stuhl-Konstruktion

Die Stuhlsäule ist Teil einer engen Bauteil-Familie (Wikipedia/
Stehender Stuhl, ETH Holzer/Steiger):

| Bauteil | Funktion |
|---|---|
| **Stuhlsäule** | tragendes Druck-Element zur Pfettenauflagerung |
| **Stuhlpfette** | trägt Sparren oder Kehlbalken am Stuhlsäulen-Kopf |
| **Stuhlschwelle** | trägt Stuhlsäulen-Füsse, verteilt Last auf Deckenbalken |
| **Kopfband** | Diagonal-Aussteifung Stuhlsäulen-Kopf ↔ Stuhlpfette |
| **Fußband** | Diagonal-Aussteifung Stuhlsäulen-Fuß ↔ Stuhlschwelle |
| **Spannriegel** | beim liegenden Stuhl: Querriegel zwischen den schrägen Stuhlsäulen oben |
| **Strebe** | bei doppelt stehendem Stuhl: Schrägaussteifung der Stuhl-Reihe längs |
| **Stuhlwand** | Bauteilgruppe aus Stuhlsäule + Stuhlpfette + Stuhlschwelle + Kopfband + Fußband |

Die **Stuhlwand** als Bauteilgruppe wird im aktuellen Glossarstand
noch nicht geführt; Folgearbeit-Trigger.

### Querschnitt und Werkstoff

Stuhlsäulen werden traditionell als **behauenes Vollholz** in
Querschnitten 140/140 bis 240/240 mm ausgeführt; im modernen
Holzbau auch als **BSH** (Brettschichtholz) für grosse Spannweiten
oder Sanierungs-Verstärkungen. Faserrichtung axial entlang der
Bauteilachse, Festigkeitsklasse typisch C24 oder GL24h.

### Anschluss am Stuhlsäulen-Kopf (Kämpfer)

Der **Kämpfer** ist das Konstruktionsdetail am Stuhlsäulen-Kopf,
wo die Stuhlpfette aufgenommen wird:

- Klassisch durch **Zapfen** der Stuhlsäule in ein **Zapfenloch** in
  der Stuhlpfetten-Unterseite, gesichert mit Holznagel und
  ergänzt durch ein **Kopfband** als Diagonal-Aussteifung.
- Modern durch **Stahlblech-Schuhe** (Knapp, Sherpa) oder
  durchlaufende Stuhlpfette mit Stuhlsäulen-Auflagerschuh.

Das Kämpfer-Detail ist Folgearbeit-Trigger (`hg_konstruktions-
detail.md`-Spezialisierung).

### Stuhlsäule vs. Strebesäule

Die **Strebesäule** (`hg_strebesaeule.md`, Forward-Verweis,
TTH-Sub-Lemma) ist eine Mischform aus Strebe und Säule —
typischerweise eine schräggestellte Säule, die als
Aussteifungs-Element in einer Stuhl-Konstruktion fungiert. Die
Trennlinie zur Stuhlsäule liegt in der konstruktiven Funktion:
Strebesäule ist primär Aussteifung (Diagonal-Stabilisierung),
Stuhlsäule ist primär Tragglied (Pfetten-Auflagerung). Folgearbeit
zur Klärung im Recherche-Bericht §I.2.

### Andere Bedeutungen / Englisch

- **`king post`**: in der englischen Tradition primär für die
  **Hängesäule** im einfachen Hängewerk verwendet, nicht für die
  Stuhlsäule. False friend.
- **`crown post`** / **`queen post`**: ebenfalls eher Hängewerk-
  Begriffe.
- **`strut`** / **`post`**: zu allgemein.

Im englischen Holzbau-Korpus gibt es kein präzises Pendant zur
deutschen „Stuhlsäule"; eine genaue Übersetzung wäre „**stand-
post in a roof-stool construction**" oder paraphrasiert „**vertical
post supporting a purlin in a traditional German/Swiss roof
truss**".

## Beziehungen

- **Oberbegriff**: `bauteil`. Strukturell ist die Stuhlsäule ein
  Bauteil mit der zusätzlichen Rolle „Stuhlsäule" und den oben
  formalisierten geometrischen und topologischen Constraints.
  Geschwister-Rolle zu `staender` (Wand), `stuetze` (Skelettbau),
  `sparren` (Dachfläche), `pfette` (Dach-Längsträger),
  `haengesaeule` (Hängewerk).
- **Bestandteile (partitiv, vom Bauteil geerbt)**:
  - **Bauteilachse** (`bauteilachse.Gerade`), aufstrebend
    (Bedingung 2);
  - **Querschnitt** (rechteckig, typisch 140–240 mm Kantenmass);
  - **Werkstoff** (Vollholz oder BSH, Festigkeitsklasse C24 oder
    GL24h);
  - **Faserrichtung** (Annotation, Default ‖ d̂_Stuhlsäule).
- **Topologische Inzidenz**:
  - **Stuhlpfette** (`stuhlpfette`, Forward-Verweis): trägt am
    Stuhlsäulen-Kopf (Bedingung 4).
  - **Auflagerbalken** (Stuhlschwelle / Deckenbalken /
    Bundbalken; `stuhlschwelle` Forward-Verweis): trägt den
    Stuhlsäulen-Fuß (Bedingung 5).
  - **Kopfband** (`kopfband`, Welle 10): Diagonal-Aussteifung
    zwischen Stuhlsäulen-Kopf und Stuhlpfette.
  - **Fußband** (`fussband`, Welle 10/11): Diagonal-Aussteifung
    zwischen Stuhlsäulen-Fuß und Stuhlschwelle.
  - **Strebe** (`strebe`, Welle 10): bei doppelt stehendem Stuhl
    Schrägaussteifung längs der Stuhl-Reihe.
  - **Spannriegel** (`spannriegel`, Forward-Verweis): beim
    liegenden Stuhl Querriegel zwischen den geneigten
    Stuhlsäulen.
- **Spezialisierungen** (Folgearbeit-Trigger):
  - `stehende_stuhlsaeule`: lotrechte Variante im stehenden
    Stuhl.
  - `liegende_stuhlsaeule`: schräggestellte Variante im
    liegenden Stuhl.
- **Verwendung**:
  - Mitglied des **Dachstuhls** (`dachstuhl`, Welle 12) als
    eine seiner zentralen Bauteilrollen im Pfettendach mit
    Stuhl-Konstruktion.
  - Mitglied einer **Stuhlwand**-Bauteilgruppe
    (`stuhlwand`, Folgearbeit-Trigger).
- **Abgrenzung**:
  - **Stütze** (`stuetze`, Welle 13): werkstoffneutrale Tragwerks-
    Bauteilrolle ohne Stuhlpfetten-Anschluss. Geschwister-Rolle
    der Stuhlsäule, nicht Oberbegriff. Trennlinie:
    Stuhlpfetten-Anschluss (Bedingung 4) und Holz-Exklusivität.
  - **Säule** (`saeule`, Welle 13): architektonisch-klassischer
    Subtyp der Stütze. Keine Stuhlsäule ist eine Säule
    (Bedingung 3 von `hg_saeule.md` — freistehender Charakter —
    ist bei der Stuhlsäule verletzt, sie ist in den Dachstuhl
    eingebunden).
  - **Hängesäule** (`haengesaeule`, Welle 13): Zug-Element im
    Hängewerk; Geschwister-Bauteilrolle mit invertiertem
    Lastpfad. Bedingung 6 trennt: Stuhlsäule trägt Druck,
    Hängesäule Zug.
  - **Ständer** (`staender`, Welle 9): Wand-Bauteilrolle.
    Geschwister-Rolle; Trennlinie über die Wand-Inzidenz (Schwelle/
    Rähm) gegen die Stuhl-Inzidenz (Stuhlpfette/Stuhlschwelle).
  - **Pfette** (`pfette`, Welle 8): horizontaler Dach-Längsträger;
    liegt auf den Stuhlsäulen-Köpfen, ist nicht selbst Stuhlsäule.
    Die **Stuhlpfette** (`stuhlpfette`, Forward-Verweis) ist die
    Pfetten-Spezialisierung am Stuhlsäulen-Kopf.
  - **Stuhl** (`stuhl`, Forward-Verweis, Welle-12-Folgearbeit aus
    `hg_dachstuhl.md`): Stütz-Bauteilgruppe; die Stuhlsäule ist
    Bestandteil eines Stuhls, nicht selbst der Stuhl.
  - **Stehender Stuhl** / **Liegender Stuhl** (Forward-Verweise):
    Varianten der Stuhl-Konstruktion, in denen die Stuhlsäule
    lotrecht bzw. schräg verbaut ist.
  - **Stuhlwand** (`stuhlwand`, Folgearbeit-Trigger):
    Bauteilgruppe aus Stuhlsäule + Stuhlpfette + Stuhlschwelle +
    Kopfband + Fußband.
  - **Kopfband** (`kopfband`, Welle 10): Diagonal-Aussteifung am
    Stuhlsäulen-Kopf. Wechselseitige Inzidenz.
  - **Fußband** (`fussband`, Welle 10/11): Diagonal-Aussteifung
    am Stuhlsäulen-Fuß. Wechselseitige Inzidenz.
  - **Sparren** (`sparren`, Welle 8): geneigtes Dachflächen-
    Bauteil; liegt auf der Stuhlpfette auf, nicht direkt auf der
    Stuhlsäule. Trennlinie: schräge Lage in der Dachfläche vs.
    aufstrebende oder lotrechte Lage der Stuhlsäule.
  - **Spannriegel** (`spannriegel`, Forward-Verweis):
    Querholz im liegenden Stuhl. Bestandteil der Stuhl-
    Konstruktion, nicht selbst Stuhlsäule.
  - **Kehlbalken** (`kehlbalken`, Welle 8): horizontaler
    Aussteifungs-Riegel zwischen Sparren; kann auf einer
    Stuhlpfette (und damit indirekt auf der Stuhlsäule)
    aufliegen.
  - **Strebe** (`strebe`, Welle 10): Diagonal-Aussteifung im
    Längsverband des Stuhls.
  - **Strebesäule** (`strebesaeule`, Forward-Verweis, TTH-Sub-
    Lemma): Strebe-/Säule-Mischform. Folgearbeit-Trigger zur
    Klärung.
  - **Dachstuhl** (`dachstuhl`, Welle 12): Aggregat. Die
    Stuhlsäule ist Mitglied des Dachstuhls in Lesart 2
    (zimmermannsmäßiges Dachtragwerk).
  - **Bauteil** (`bauteil`): Oberbegriff.

## Implementierungshinweis

Datentyp (Domänen-Schicht, Kotlin, Schicht `domain.bauteil`):

```kotlin
package domain.bauteil

import domain.Toleranzen
import domain.bauteil.Bauteil
import domain.bauteil.Bauteilachse
import domain.geometrie.Einheitsvektor
import domain.geometrie.Punkt
import kotlin.math.acos

/**
 * Stuhlsäule als holz-spezifische Bauteilrolle: aufstrebendes Stab-
 * Bauteil im Dachstuhl mit Stuhlpfetten-Anschluss am Kopf und
 * Auflagerbalken-Anschluss (Stuhlschwelle / Deckenbalken /
 * Bundbalken) am Fuß. Druck-Element im Pfettendach mit Stuhl-
 * Konstruktion.
 *
 * Glossar: hg_stuhlsaeule.md
 *
 * Variante: stehender Stuhl (lotrecht) oder liegender Stuhl
 * (schräg). Diskriminierung über die Stuhlsäulen-Neigung gegen die
 * Lotachse.
 *
 * Holz-Exklusivität: konstitutiv. Im Stahl-/Stahlbeton-Tragwerk
 * existieren keine Stuhlsäulen.
 *
 * Vorzeichenkonvention: p_a = Fuß (am Auflagerbalken), p_e = Kopf
 * (an der Stuhlpfette).
 */
data class Stuhlsaeule(
    val bauteil: Bauteil,
    val variante: StuhlsaeulenVariante = StuhlsaeulenVariante.UNBESTIMMT,
) {
    val achse: Bauteilachse.Gerade
        get() = (bauteil.geometrie as Bauteilgeometrie.Stab).achse
                as Bauteilachse.Gerade
    val laenge: Double get() = achse.laenge          // mm
    val richtung: Einheitsvektor get() = achse.richtung
    val fuss: Punkt get() = achse.anfang
    val kopf: Punkt get() = achse.ende

    /** Neigung gegen die Lotachse e_z, in rad. */
    val neigungGegenLot: Double
        get() = acos(richtung.z.coerceIn(-1.0, 1.0))

    fun istStehend(eps: Double = Toleranzen.WINKEL_EPS): Boolean =
        neigungGegenLot <= eps
}

/**
 * Variante der Stuhlsäule: stehender Stuhl (lotrecht) oder
 * liegender Stuhl (schräg).
 *
 * Folgearbeit-Trigger für sealed-Subtypen StehendeStuhlsaeule und
 * LiegendeStuhlsaeule als bauteilrolle-Verschachtelung
 * (HG_KONVENTIONEN §3 erlaubt das).
 */
enum class StuhlsaeulenVariante {
    STEHEND,
    LIEGEND,
    UNBESTIMMT,
}

sealed class StuhlsaeuleEntartet {
    object Nullachse                 : StuhlsaeuleEntartet()
    object NichtAufstrebend          : StuhlsaeuleEntartet()  // p_a.z ≥ p_e.z
    object KeinStuhlpfettenAnschluss : StuhlsaeuleEntartet()
    object KeinAuflagerbalken        : StuhlsaeuleEntartet()
    object PfetteNichtHorizontal     : StuhlsaeuleEntartet()
}
```

- **Einheit**: Längen in mm (Double); Winkel intern in Radiant.
- **Identität**: `BauteilId` aus dem zugrunde liegenden Bauteil.
- **Invarianten** (in der Factory `stuhlsaeuleAusBauteil(...)`
  prüfen):
  1. Stabgeometrie und Bauteilachse vom Typ `Bauteilachse.Gerade`.
  2. Achsenlänge > Toleranzen.LAENGE_EPS — sonst `Nullachse`.
  3. p_a.z + Toleranzen.LAENGE_EPS < p_e.z — sonst
     `NichtAufstrebend`.
  4. Stuhlpfetten-Anschluss am Kopf: Punkt-Geraden-Abstand
     ≤ Toleranzen.LAENGE_EPS — sonst `KeinStuhlpfettenAnschluss`.
  5. Stuhlpfette horizontal: |⟨d̂_P, e_z⟩| ≤ Toleranzen.KOLLINEAR_EPS
     — sonst `PfetteNichtHorizontal`.
  6. Auflagerbalken-Anschluss am Fuß: Punkt-Geraden-Abstand
     ≤ Toleranzen.LAENGE_EPS — sonst `KeinAuflagerbalken`.
- **Edge Cases**:
  - **Stehende Stuhlsäule** (Lotrecht): typisch im einfach oder
    doppelt stehenden Stuhl; Neigung gegen Lot ≤ Toleranzen.WINKEL_EPS.
  - **Liegende Stuhlsäule** (schräg): typisch in der Sparrenebene
    geneigt, mit Anschluss am Spannriegel oben statt direkter
    Stuhlpfetten-Anschluss; die Definition lockert auf
    Stuhlpfette ODER Spannriegel als oberes Auflager.
  - **Mehrfach stehende Stuhlsäulen** (drei oder mehr Reihen): pro
    Stuhlsäulen-Instanz eine eigene Stuhlpfette und Stuhlschwelle.
  - **Stuhlsäule am First** (einfach stehender Stuhl): obere
    Stuhlpfette ist die Firstpfette; konstruktive Sonderform.
  - **Stuhlsäule mit Stuhlschwellen-Fuss vs. direkter Deckenbalken-
    Fuss**: die Definition lässt beide Auflagerbalken-Typen zu
    (Bedingung 5). In der historischen CH-Praxis (vor 1900) oft
    direkter Deckenbalken-Auflauf ohne separate Stuhlschwelle.
  - **Sehr kurze Stuhlsäule** (Zwerg-Stuhlsäule unter Kehlbalken-
    Dach): zulässig, sofern die geometrischen und topologischen
    Bedingungen 1–6 erfüllt sind.
- **Folgearbeit-Trigger**:
  - `hg_stuhlpfette.md`: Pfetten-Spezialisierung am Stuhlsäulen-
    Kopf (analog `hg_firstpfette.md`/`hg_mittelpfette.md`/
    `hg_fusspfette.md` aus Welle 8). Trigger: Welle-13-Folge.
  - `hg_stuhlschwelle.md`: Schwelle-Spezialisierung am Stuhlsäulen-
    Fuß; auch Welle-8-Folgearbeit-Trigger aus `hg_schwelle.md`.
  - `hg_stuhlwand.md`: Bauteilgruppe aus Stuhlsäule + Stuhlpfette
    + Stuhlschwelle + Kopfband + Fußband. Trigger:
    Dachstuhl-Aggregat-Verfeinerung.
  - `hg_spannriegel.md`: Querholz im liegenden Stuhl. Trigger:
    Liegender-Stuhl-Folgearbeit oder Hängewerk-Folgearbeit.
  - `hg_stehender_stuhl.md` und `hg_liegender_stuhl.md`:
    Aggregate / Bauteilgruppen, die die Stuhlsäulen-Varianten
    konstruktiv umfassen. Trigger: erste konkrete Dachstuhl-Tool-
    Modellierung.
  - `hg_stuhl.md` (Welle-12-Folgearbeit aus `hg_dachstuhl.md`):
    Stütz-Bauteilgruppe, Lesart 1 von „Dachstuhl".
  - `hg_strebesaeule.md`: Strebe-/Säule-Mischform; TTH-Sub-Lemma
    1922. Trigger: Klärung TTH-Sub-Lemma.
  - **Stuhlsäulenkopf-Kämpfer**: Konstruktionsdetail-Eintrag
    (analog `hg_konstruktionsdetail.md`). Trigger: erste
    Detail-Modellierung.
  - **SIA-265-Verifikation**: bei Volltext-Zugriff (Eric) SIA
    265:2021 §1.1 Fachausdrücke direkt prüfen.

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
- Holzer, S.; Steiger, R.: ETH Zürich, Lehrunterlage „Holz IV —
  Dachwerke mit liegendem Stuhl", FS 2023.
- Mönck, W.; Rug, W.: *Holzbau – Bemessung und Konstruktion.*
  16. Auflage, Beuth, Berlin 2015, Kap. 11 „Dachtragwerke".
- Natterer, J.; Herzog, T.; Volz, M.: *Holzbau-Atlas.* 4. Auflage,
  Birkhäuser, Basel 2003.
- Gerner, M.: *Fachwerk – Instandsetzung, Sanierung, Neubau.*
  DVA, 7. Auflage 2007.
- Krämer, V.: *Grundwissen des Zimmerers.* Bruderverlag, Karlsruhe
  1988.
- Thesaurus Traditioneller Holzbau (TTH), RWTH Aachen,
  Hierarchie-Facette 1922 „Fachwerk-Bauteile" — „Stuhlsäule" als
  belegtes Lemma. thesaurus-traditioneller-holzbau.net.
- Wikipedia, Lemmata „Dachstuhl", „Stehender Stuhl", „Liegender
  Stuhl", „Liste von Fachbegriffen des Zimmererhandwerks"
  (abgerufen 2026-05-16).
- Recherche-Bericht: `docs/recherche/2026-05-16_tragglieder_vertikal.md` §E.

**Korpus (nicht autoritativ):**

- baunetzwissen.de „Dachstuhl-Konstruktionen" (HTTP 403 blockiert).
- dach24.online „Der Dachstuhl: Arten, Konstruktion und Kosten".
- fertighauswelt.de „Der Dachstuhl".
