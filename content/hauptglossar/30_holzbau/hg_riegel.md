---
id: riegel
benennung: Riegel
synonyme: [Wandriegel, Querriegel, Querholz]
abgelehnte_benennungen: [Brustriegel, Sturzriegel, Stockwerksriegel, Brüstungsriegel, Kopfriegel, Schwellenriegel, Fußriegel, Rähmriegel, Zwischenriegel, Druckriegel, Spannriegel, Sprengriegel, Binderriegel, Latte, Pfette, "nogging", "noggin", "cripple stud", "girt", "header", "rail"]
oberbegriff: bauteil
begriffstyp: bauteilrolle
voraussetzungen: [bauteil, bauteilachse, strecke, einheitsvektor, ebene, weltkoordinatensystem, toleranzen]
abgrenzung_zu: [pfette, latte, schwelle, raehm, pfosten, staender, strebe, kopfband, fussband, knagge, wand, mann, andreaskreuz, sturz, kehlbalken, bauteil]
status: entwurf
subglossar_pendant: notwendig
quellen_primär:
  - "SIA 265:2021 'Holzbau', Schweizerischer Ingenieur- und Architektenverein, Abschnitt 4 (Bemessung) und Abschnitt 5 (Konstruktive Durchbildung): Riegel als horizontales Bauteil des Wandtragwerks vorausgesetzt."
  - "DIN EN 1995-1-1:2010-12 (Eurocode 5), Abschnitt 5 (Tragwerksberechnung): Riegel als biegebeanspruchtes Stab-Bauteil im Wandverband vorausgesetzt."
  - "DIN 1052:2008-12, Abschnitt 8 und 12 (Konstruktive Anforderungen): Riegel als Bestandteil des Wandtragwerks vorausgesetzt, nicht eigenständig definiert."
quellen_sekundär:
  - "Lignum (Hrsg.): Holzbautabellen HBT 1 (2024). Lignum, Zürich. Begriffsregister 'Riegel' (Volltext nicht zugänglich; Verankerung über HBT-Schaufenster und lignum.ch/holz_a_z/konstruktion/)."
  - "Mönck, W.; Rug, W.: Holzbau – Bemessung und Konstruktion. 16. Aufl., Beuth, Berlin 2015, Kap. 'Wandbau' und 'Fachwerk'."
  - "Natterer, J.; Herzog, T.; Volz, M.: Holzbau-Atlas. 4. Aufl., Birkhäuser, Basel 2003, Kap. 'Wandbauteile' und 'Fachwerkkonstruktionen'."
  - "Gerner, M.: Fachwerk – Instandsetzung, Sanierung, Neubau. DVA, 7. Aufl. 2007, Glossar 'Riegel', 'Brustriegel', 'Sturzriegel'."
  - "Thesaurus traditioneller Holzbau (TTH), RWTH Aachen, Lemma 'Riegel (Fachwerk)' (begriff_id 971)."
  - "RDK Labor — Reallexikon zur Deutschen Kunstgeschichte, Lemma 'Fachwerk, Fachwerkbau'."
  - "DWDS — Etymologisches Wörterbuch des Deutschen, Lemma 'Riegel', dwds.de/wb/etymwb/Riegel."
quellenkonflikt: |
  Weder SIA 265:2021 noch DIN EN 1995-1-1:2010-12 noch DIN 1052:2008-12
  enthalten eine geschlossene Begriffsdefinition für „Riegel"; der
  Begriff wird in allen konsultierten Normen vorausgesetzt und über
  seine konstruktive Rolle im Wandtragwerk charakterisiert. Lignum
  HBT 1 (2024) führt den Begriff im Register, Volltext nicht
  zugänglich.

  In der Sekundärliteratur (Mönck/Rug, Natterer/Herzog/Volz, Gerner,
  Thesaurus traditioneller Holzbau, RDK Labor) wird der Riegel
  durchgängig als „horizontal verlaufender Balken zwischen zwei
  Pfosten / Ständern einer Wand, der das geschosshohe Gefach in
  kleinere Ausfachungsfelder unterteilt und die Wandebene aussteift"
  beschrieben. Das Wikipedia-Lemma `Riegel (Bauteil)` formuliert die
  Funktion wörtlich als „lediglich aussteifende und unterteilende
  Funktion" und steht damit in Konvergenz mit den höherrangigen
  Sekundärquellen.

  Eigene Festlegung in diesem Glossar:

  - Der **Default-Sinn** des Begriffs „Riegel" ist der **Wand-Riegel**:
    horizontales Stab-Bauteil zwischen zwei vertikalen Wandbauteilen
    (`pfosten` / `ständer`) in einer gemeinsamen Wandebene.
  - Die im DACH-Korpus verbreiteten Komposita **Brustriegel**,
    **Sturzriegel**, **Stockwerksriegel**, **Brüstungsriegel**,
    **Kopfriegel**, **Schwellenriegel** (Fußriegel), **Rähmriegel**
    und **Zwischenriegel** bezeichnen denselben Wand-Riegel mit
    **unterschiedlicher Höhen- bzw. Öffnungs-Bezug-Position** in der
    Wand. Sie sind **keine eigenständigen Bauteilrollen** mit eigenen
    geometrischen oder statischen Constraints, sondern
    **Positions-Annotationen** an demselben Riegel-Bauteil. Diese
    Festlegung folgt aus der Konvergenz der konsultierten Sekundär-
    quellen: keine der Sub-Lesarten trägt eigene geometrische
    Constraints jenseits ihrer Höhen- oder Öffnungs-Lage, und keine
    trägt eigene statische Defaults jenseits derer, die sich aus dem
    Wandsystem ergeben. Konsequenz für die Modellierung: ein
    `RiegelPosition`-Merkmal am Riegel-Bauteil (siehe
    Implementierungshinweis), keine sealed-class-Sub-Hierarchie.
    Die Komposita stehen daher in `abgelehnte_benennungen`, soweit
    sie als alleinstehende Bauteilbenennung verwendet werden sollen;
    als Positions-Etikett bleiben sie zulässig.
  - Der **Sturzriegel** trägt eine **funktionale Doppelnatur**: er ist
    geometrisch Riegel (horizontal zwischen zwei Pfosten) und
    funktional **Sturz** (lastüberbrückendes Bauteil über einer
    Wand-Öffnung, vgl. den noch nicht angelegten Eintrag `sturz`).
    Diese Doppelnatur ist im Erläuterungsblock thematisiert und
    rechtfertigt keine eigene Bauteilrolle.
  - Eine **zweite Lesart** des Wortes „Riegel" tritt im **Dachtragwerk
    historischer Bauformen** in den Komposita **Druckriegel**,
    **Spannriegel**, **Sprengriegel** und **Binderriegel** auf
    (Hängewerk, Sprengwerk, Stuhltragwerke). Diese Dach-Riegel sind
    statisch tragende Bauteile (Druck oder Zug zwischen Sparren bzw.
    Stuhlsäulen) und gehören **nicht** zur Wand-Riegel-Lesart dieses
    Eintrags; sie sind in `abgelehnte_benennungen` als alleinstehende
    Verwendung von „Riegel" für den Wand-Bauteil ausgeschlossen. Ein
    eigener Glossareintrag für die Dach-Riegel-Lesart wird erst beim
    Hängewerk- bzw. Sprengwerk-Tool angelegt (Folgearbeit-Trigger).
  - **„Querholz"** ist etymologisch direkt mit „Riegel" verwandt
    (lat. `regula` → ahd. `rigil`; vgl. DWDS) und im breiteren DACH-
    Sprachgebrauch belegt, ist aber im modernen Schweizer Holzbau-
    Korpus (Lignum HBT, lignum.ch/holz_a_z) **nicht** als technischer
    Bauteilname für die Wand-Riegel-Rolle etabliert. Es wird hier in
    `synonyme` mit Vorbehalt geführt: berufssprachlich umgangs-
    sprachlich verwendbar, aber als technische Hauptbenennung
    abzuraten.
  - Englische Bezeichnungen sind nach CLAUDE.md-Architektur-Verbot
    nicht als Synonyme aufzunehmen. **„cripple stud"** ist zusätzlich
    ein **false friend**: das englische Wort bezeichnet einen
    **verkürzten Pfosten** (vertikal!) ober- oder unterhalb einer
    Öffnung, nicht den horizontalen Wand-Riegel. **„nogging"** (UK)
    ist funktional die nächste englische Entsprechung, aber als
    Anglizismus abgelehnt; **„girt"** und **„header"** decken nur
    Spezialfälle ab und sind ebenfalls abgelehnt.

  Diese Festlegung ist konsistent mit allen konsultierten Quellen.
---

## Prosa-Definition

Ein **Riegel** ist ein stabförmiges Bauteil eines Wandtragwerks,
dessen Bauteilachse zwischen zwei vertikal stehenden Stab-Bauteilen
einer gemeinsamen Wandebene horizontal und rechtwinklig zu diesen
verläuft und das die Wandebene aussteift, das Gefach in kleinere
Ausfachungsfelder unterteilt und Lasten der Wandbekleidung,
Öffnungs-Einfassungen oder Installationen aufnimmt, ohne primärer
vertikaler Lastpfad der Wand zu sein.

## Mathematische Definition

Sei

- B ein Bauteil im Sinne von `bauteil` mit Stabgeometrie
  (`geometrie ∈ 𝒢_stab`),
- a(B) = Bauteilachse.Gerade(p_a, p_e) die Bauteilachse von B im
  geraden Fall (siehe `bauteilachse`), mit
  d_hat := (p_e − p_a) / ‖p_e − p_a‖ ∈ S² ⊂ ℝ³,
- E_W eine Wandebene (Ebene im Sinne von `ebene`) mit Stützpunkt
  p_W und Normalenvektor n_hat_W ∈ S², wobei n_hat_W horizontal liegt
  (|⟨n_hat_W, e_z⟩| ≤ ε_K — die Wand steht senkrecht im Sinne von
  HG_KONVENTIONEN.md §1, d. h. lotrecht),
- P₁, P₂ zwei vertikal stehende Stab-Bauteile in E_W (vgl.
  Forward-Verweis `pfosten`) mit Bauteilachsen entlang
  Einheitsvektoren v_hat₁, v_hat₂ ∈ S², wobei
  |⟨v_hatᵢ, e_z⟩| ≥ 1 − ε_K  (Lotrechtheit, Sinus-Test gegen e_z),
- e_z := (0, 0, 1)ᵀ die vertikale Welt-Achse,
- ε_K := Toleranzen.KOLLINEAR_EPS,
  ε_W := Toleranzen.WINKEL_EPS,
  ε_L := Toleranzen.LAENGE_EPS.

Dann heißt B ein **Riegel** zwischen P₁ und P₂ in der Wandebene
E_W genau dann, wenn die folgenden Bedingungen erfüllt sind:

1. **Stabgeometrie**: B besitzt eine gerade Bauteilachse mit
   ‖p_e − p_a‖ > ε_L.

2. **Horizontalität der Riegelachse**: Die Bauteilachsenrichtung
   steht rechtwinklig zur Welt-Lotachse,
   ```
   |⟨d_hat, e_z⟩| ≤ ε_K.
   ```
   Der Test ist ein **Sinus-Test gegen e_z-Parallelität**
   (Lot-Prädikat); nach HG_KONVENTIONEN.md §4 ist `KOLLINEAR_EPS`
   die einschlägige Toleranzkonstante.

3. **Lage in der Wandebene**: Beide Endpunkte liegen in E_W,
   ```
   |⟨p_a − p_W, n_hat_W⟩| ≤ ε_L  ∧  |⟨p_e − p_W, n_hat_W⟩| ≤ ε_L.
   ```

4. **Rechtwinkligkeit zu den begrenzenden Pfosten**: Die Riegel-
   achse steht rechtwinklig zu beiden Pfostenachsen,
   ```
   |⟨d_hat, v_hatᵢ⟩| ≤ ε_K  für i = 1, 2.
   ```
   Aus Bedingung 2 (Horizontalität d_hat) und der Lotrechtheit der
   Pfosten (v_hatᵢ ≈ ±e_z) folgt Bedingung 4 bereits geometrisch; sie
   bleibt als Konsistenz-Bedingung stehen, um schiefstehende
   Pfosten (z. B. Schwellenverdrehung beim Aufrichten) numerisch
   abzufangen.

5. **Eingespannte Lage zwischen den Pfosten**: Die beiden
   Endpunkte fallen mit den Pfostenachsen zusammen (bis auf
   Toleranz):
   ```
   dist(p_a, achse(P₁)) ≤ ε_L  ∧  dist(p_e, achse(P₂)) ≤ ε_L,
   ```
   oder die symmetrische Vertauschung p_a ↔ p_e. Hierbei ist
   dist(p, a) der Punkt-Geraden-Abstand zur jeweiligen
   Pfostenachse.

Wesentliche abgeleitete Größen:

- **Riegellänge**: L_R := ‖p_e − p_a‖ (in mm), entlang der
  Bauteilachse zwischen den Anschlüssen an P₁ und P₂.
- **Riegelrichtung**: d_hat ∈ S² mit |⟨d_hat, e_z⟩| ≤ ε_K.
- **Riegel-Höhenlage**: z_R := (p_a.z + p_e.z) / 2; bei einer
  exakt horizontalen Riegelachse gilt p_a.z = p_e.z = z_R.

## Wohldefiniertheit

- **Existenz**: Für jedes Stabbauteil mit positiver Achsenlänge,
  horizontaler Achse, Lage in einer lotrechten Wandebene und
  Anschluss an zwei lotrecht stehende Pfostenachsen sind alle
  fünf Bedingungen konstruktiv erfüllbar; jeder Riegel eines
  klassischen Fachwerk-Gefachs ist Standardbeispiel.
- **Eindeutigkeit der Riegelrichtung**: Bedingungen 2 und 3
  zusammen fixieren d_hat bis auf Vorzeichen: d_hat liegt in E_W
  (rechtwinklig zu n_hat_W) und ist horizontal (rechtwinklig zu
  e_z). Da n_hat_W selbst horizontal ist (Wand lotrecht), ist d_hat
  damit kollinear zu n_hat_W × e_z bzw. dem in E_W liegenden
  Horizontalvektor; das Vorzeichen wird durch die Reihung der
  Endpunkte p_a → p_e festgelegt.
- **Vorzeichenkonvention**: Welcher Endpunkt p_a bzw. p_e ist,
  ist auf der Ebene des Begriffs „Riegel" **nicht** durch eine
  geometrische Lagebedingung festgelegt (analog zu Pfette und
  Latte). Empfehlung gemäß `hg_bauteilachse.md`: p_a am
  Bauteilanfang gemäß lokaler Bezeichnungskonvention.
  Konsumenten dürfen sich nicht auf eine geometrisch zwingende
  Orientierung verlassen.
- **Konsistenz Bedingung 2 ↔ Bedingung 4**: Bei exakt lotrechten
  Pfosten (v_hatᵢ = ±e_z) und horizontaler Riegelachse (Bedingung 2)
  ist Bedingung 4 redundant; bei numerisch leicht schiefstehenden
  Pfosten ist Bedingung 4 die stärkere Aussage und entscheidet
  über die Annahme/Ablehnung. Beide Bedingungen werden in der
  Factory geprüft, um schwer aufdeckbare Sequenz-Effekte zu
  vermeiden.
- **Mindestens-zwei-Pfosten-Bedingung**: Bedingung 5 fordert die
  Existenz zweier Pfosten, an deren Achsen die Riegel-Endpunkte
  anschließen. Die Bedingung schließt freistehende Riegel
  (etwa fliegende Quer-Hölzer ohne Endauflager) aus; solche
  Bauteile sind keine Riegel im Sinne dieses Eintrags.
- **Robustheit gegen Wahl der Wandebene**: Die Wandebene E_W ist
  durch die Pfostenachsen P₁ und P₂ bis auf Toleranz eindeutig
  bestimmt (Ebene durch die beiden Pfostenachsen, sofern diese
  nicht kollinear sind); Bedingung 3 ist dann automatisch
  erfüllt, wenn p_a und p_e auf den Pfostenachsen liegen
  (Bedingung 5). Die Wandebene ist insofern Folgerung aus den
  Pfostenachsen, nicht eigenständige Eingabe.
- **Nicht-Zirkularität**: Die Definition stützt sich nur auf
  bereits definierte Begriffe (`bauteil`, `bauteilachse`,
  `strecke`, `einheitsvektor`, `ebene`, `weltkoordinatensystem`,
  `toleranzen`). Der Begriff `pfosten` / `ständer` ist im
  aktuellen Hauptglossar noch nicht eigenständig angelegt; er
  steht als Forward-Verweis in `abgrenzung_zu` und wird in der
  Definition durch die geometrische Umschreibung „vertikal
  stehende Stab-Bauteile in einer gemeinsamen Wandebene"
  ersetzt. Die formale Bedingung ist nicht auf den
  Glossareintrag `pfosten` angewiesen, sondern nur auf das
  geometrische Merkmal der Lotrechtheit (Sinus-Test gegen e_z).
- **Sturzriegel-Doppelnatur (qualitativ, nicht Bestandteil der
  Definition)**: Wenn der Riegel über einer Wand-Öffnung liegt
  und Lasten oberhalb der Öffnung überbrückt, übernimmt er
  zusätzlich die Funktion eines Sturzes (vgl. Forward-Verweis
  `sturz`). Die Riegel-Definition bleibt geometrisch erfüllt;
  die Sturz-Funktion ist Eigenschaft der Tragwerks-Analyse,
  nicht der Riegelrolle.

## Erläuterung (nicht normativ)

Der Riegel ist im DACH-Holzbau das **horizontale Quer-Bauteil
einer Wand** und Pendant der vertikalen Pfosten / Ständer. Das
**tragende Grundgerüst einer Holzwand** im Riegelbau (CH) bzw.
Fachwerkbau (DE/AT) besteht aus Schwelle (unten, durchlaufend),
Rähm (oben, durchlaufend), Pfosten (vertikal) und dazwischen
gespannten Riegeln (horizontal-quer); diagonale Streben können
die Aussteifung verstärken. Das Wandfeld, das zwei Pfosten und
zwei Riegel umschließen, heißt im Fachwerk **Gefach** (regional
auch „Riegelfach").

### Funktion und Lastpfad

Der primäre vertikale Lastpfad einer Holzwand läuft über die
**Pfosten**, die das Eigengewicht der Geschossdecke und ggf. des
Dachtragwerks abtragen. Der Riegel selbst ist **kein primärer
vertikaler Lastträger**: seine Funktionen sind

- **Aussteifung der Wandebene** gegen Verformung in Wand-Ebene
  (Knicksicherung der Pfosten, Stabilisierung des Wand-Rasters),
- **Unterteilung des Gefachs** in handhabbare Ausfachungsfelder
  (Ausmauerung, Lehmstaken, Holzfüllung, im modernen Holzrahmen-
  bau Dämmung),
- **Aufnahme der Wandbekleidung** (Bretter, Putzträger, im
  modernen Holzrahmenbau OSB- oder Gipsfaser-Beplankung),
- **Befestigungsfläche** für Fenster-, Tür- und Installations-
  Einbauten,
- **Montage-Erleichterung** beim Aufrichten der Wand (Abstands-
  fixierung und Knicksicherung der Pfosten).

### Riegelpositionen in der Wand

Riegel werden im DACH-Korpus nach ihrer **Höhenlage in der Wand**
bzw. ihrer **Beziehung zu Öffnungen** benannt. Diese Benennungen
sind **Positions-Annotationen** am gleichen Bauteil, keine
eigenständigen Bauteilrollen (siehe Quellenkonflikt-Block):

- **Brustriegel** (auch Brüstungsriegel): unterhalb einer Fenster-
  Öffnung, auf Brüstungshöhe; Auflager der Fensterbank.
- **Sturzriegel**: oberhalb einer Tür- oder Fenster-Öffnung;
  überbrückt die Öffnung und übernimmt **zusätzlich** die
  Funktion eines Sturzes (geometrisch Riegel, funktional Sturz).
- **Zwischenriegel**: zwischen Brust- und Sturzriegel oder
  zwischen anderen Riegeln, ohne Öffnungs-Bezug; reine Gefach-
  Unterteilung.
- **Stockwerksriegel**: oberster Riegel pro Stockwerk im
  geschosshohen Wandbau; im klassischen Stockwerkbau ersetzt
  durch das Rähm.
- **Schwellenriegel** / **Fußriegel**: unmittelbar über der
  Schwelle, konstruktive Doppelung der Schwellen-Ebene; selten.
- **Kopfriegel** / **Rähmriegel**: unmittelbar unter dem Rähm,
  Schnittstelle zur Geschossdecke; regional unterschiedlich
  verwendet.

In der Domänen-Schicht werden diese Positionen als Wert eines
Merkmals `RiegelPosition` am Riegel-Bauteil geführt (siehe
Implementierungshinweis), nicht als Subtyp-Hierarchie.

### Sturzriegel-Doppelnatur

Der Sturzriegel ist die einzige Sub-Position, die eine
**zusätzliche tragende Funktion** annimmt. Er überbrückt eine
Wand-Öffnung und trägt damit das Eigengewicht der über der
Öffnung liegenden Riegel, Pfosten-Stummel, Ausmauerungen oder
Beplankungen. In dieser Rolle fungiert er als **Sturz** im
Hochbau-Sinn — Pendant des Stahl- oder Stahlbeton-Sturzes in
massiven Wänden — und ist damit Schnittstelle zum Glossarbegriff
`sturz` (Forward-Verweis; eigener Eintrag bei der ersten
Wand-Öffnungs-Modellierung). Im traditionellen Fachwerk wird der
Sturzriegel durch zusätzliche Sturzstrebe oder Kopfwinkelhölzer
entlastet.

Die Doppelnatur rechtfertigt **keine eigene Bauteilrolle**: die
Riegel-Geometrie bleibt unverändert; die Sturz-Funktion ist
Eigenschaft der Tragwerks-Analyse und der Position relativ zu
einer Öffnung in der Wand, nicht der Bauteilrolle „Riegel"
selbst.

### Querschnitt und Werkstoff

Riegel werden im Schweizer Wohnbau typisch als **Vollholz** in
Festigkeitsklasse C24 ausgeführt, in vorgefertigten Holzrahmen-
Wandelementen oft auch als **KVH** (Konstruktionsvollholz). Im
modernen Holzrahmenbau ist der Riegel-Querschnitt häufig
**identisch** zum Pfosten-Querschnitt (z. B. 60/120 mm,
60/160 mm, 80/200 mm), während im historischen Fachwerk der
Riegel-Querschnitt oft **kleiner** als der Pfosten-Querschnitt
gewählt wurde. Die konkrete Querschnittsfindung gehört in die
Bemessung (SIA 265 / DIN EN 1995-1-1).

### Anschluss an die Pfosten

Klassisch wird der Riegel durch **Verzapfung** in den Pfosten
angeschlossen (Zapfen mit Holznagel), modern durch **Bolzen-,
Schraub- oder Stahlwinkel-Verbindungen**. Die Verbindungs-
geometrie wird in eigenen Glossareinträgen behandelt
(`zapfen`, `bolzen` etc., Folgearbeit).

### Zweite Lesart: Dach-Riegel (Druck-/Spann-/Spreng-/Binderriegel)

Im Dachtragwerk historischer Bauformen (Hängewerk, Sprengwerk,
liegender und stehender Stuhl) tritt der Begriff „Riegel" in den
Komposita **Druckriegel**, **Spannriegel**, **Sprengriegel** und
**Binderriegel** auf. Diese Bauteile sind **statisch tragende
Dach-Bauteile** (Druck oder Zug zwischen Sparren oder
Stuhlsäulen) und gehören **nicht** zur Wand-Riegel-Lesart dieses
Eintrags. Strukturell sind sie näher am `kehlbalken` (Dach-
Querbalken zwischen Sparrenpaar) als am Wand-Riegel. Sie sind in
`abgelehnte_benennungen` als alleinstehende Verwendung von
„Riegel" für das Wand-Bauteil ausgeschlossen; ein eigener
Glossareintrag wird erst bei Aufnahme historischer Dachformen in
der App angelegt (Folgearbeit-Trigger: Hängewerk- bzw.
Sprengwerk-Tool).

### Riegel ≠ Pfette ≠ Latte ≠ Schwelle ≠ Rähm

Aus zimmermannssprachlicher Sicht ist die saubere Trennung dieser
fünf Begriffe wichtig:

- **Riegel**: horizontales Wand-Querholz zwischen zwei Pfosten;
  primär aussteifend, kein primärer Lastpfad.
- **Pfette**: horizontaler Dach-Längsträger entlang Traufe, First
  oder Höhenlinie; trägt Sparren.
- **Latte**: kleines Sekundärbauteil quer auf dem Sparren als
  Auflage der Eindeckung.
- **Schwelle** (Forward-Verweis): unterstes durchlaufendes
  Wand-Längsholz; trägt die Pfosten und überträgt Vertikallasten
  auf das Fundament.
- **Rähm** (Forward-Verweis): oberstes durchlaufendes Wand-
  Längsholz; trägt die Geschossdecke bzw. das Dachtragwerk.

Die geometrische Klasse „horizontaler Balken in einer Wandebene"
ist Schwelle, Rähm und Riegel gemein; sie unterscheiden sich
durch **Position und Funktion**: Schwelle und Rähm sind
**Wand-Längsbauteile** (durchlaufend über mehrere Pfosten),
Riegel ist ein **Wand-Querbauteil** (zwischen jeweils zwei
Pfosten eingespannt).

### Strukturanalogie Riegel ↔ Kehlbalken

Der Kehlbalken ist im Dachtragwerk das geometrische Pendant des
Wand-Riegels: ein horizontaler Querbalken zwischen zwei vertikal
oder geneigt verlaufenden Stab-Bauteilen (Sparren) zur
Aussteifung. Die Strukturanalogie rechtfertigt **keine**
gemeinsame Oberbegriffs-Klasse im aktuellen Hauptglossar; sie ist
hier nur als Lesehilfe genannt.

## Beziehungen

- **Oberbegriff**: `bauteil`. Strukturell ist der Riegel ein
  Bauteil mit der zusätzlichen Rolle „Riegel" und den oben
  formalisierten geometrischen Constraints. Welle-12-Auflösung:
  die Mitgliedschaft als Wand-Bauteil erfolgt über das
  `wand`-Aggregat (siehe `hg_wand.md`); eine Zwischenebene
  `wandbauteil` wurde verworfen (App-Drift, kein
  DACH-Korpus-Begriff).
- **Bestandteile (partitiv, vom Bauteil geerbt)**:
  - **Bauteilachse** (`bauteilachse.Gerade`);
  - **Querschnitt** (rechteckig, oft gleich Pfostenquerschnitt
    im modernen Holzrahmenbau);
  - **Werkstoff** (Vollholz oder KVH, Festigkeitsklasse C24);
  - **Faserrichtung** (Annotation, Default ‖ d_hat_Riegel).
- **Positions-Annotation** (Merkmal am Riegel, kein Subtyp):
  - **Riegelposition** (`riegelposition`, Folgearbeit): Wert
    aus { Brust, Sturz, Stockwerk, Zwischen, Sonstige }.
- **Verwendung / Beziehung zu anderen Bauteilen**:
  - **Pfosten** / **Ständer** (Forward-Verweis, eigener Eintrag
    folgt): vertikales Stab-Bauteil; Auflager und Endpunkt-
    Anschluss des Riegels.
  - **Schwelle** (Forward-Verweis, eigener Eintrag folgt):
    unterstes Wand-Längsholz; trägt die Pfosten, an denen die
    Riegel hängen.
  - **Rähm** (Forward-Verweis, eigener Eintrag folgt): oberstes
    Wand-Längsholz; bildet den oberen Wand-Abschluss, kann von
    der obersten Riegel-Ebene überlagert sein (Kopfriegel-
    Position).
  - **Sturz** (Forward-Verweis, eigener Eintrag folgt): Sturzriegel
    übernimmt funktional die Sturzfunktion über einer Wand-
    Öffnung; eigener Eintrag bei der ersten Wand-Öffnungs-
    Modellierung.
- **Abgrenzung**:
  - **Pfette** (`pfette`): horizontaler Längsträger des **Dach**-
    Tragwerks (parallel zu Traufe, First, Höhenlinie der
    Dachfläche). Der Riegel ist horizontales Wand-Bauteil
    (in einer lotrechten Wandebene), keine Pfette. Die
    Pfette ist primär lasttragend für Sparrenlasten; der
    Riegel ist primär aussteifend ohne vertikalen Lastpfad.
  - **Latte** (`latte`): kleines Sekundärbauteil quer auf dem
    Sparren als Auflage der Eindeckung. Geometrisch sehr
    kleiner Querschnitt (24/48 bis 40/60 mm), nicht im
    Wandbau verortet.
  - **Schwelle** (Forward-Verweis): unterstes **Längs**-Holz der
    Wand, durchlaufend über mehrere Pfosten; nicht zwischen
    Pfosten eingespannt. Der Riegel ist **Quer**-Bauteil zwischen
    je zwei Pfosten.
  - **Rähm** (Forward-Verweis): oberstes Längs-Holz der Wand,
    durchlaufend über mehrere Pfosten; trägt die Geschossdecke
    bzw. das Dachtragwerk. Der Riegel hat keine vergleichbare
    primäre Lasttrag-Funktion.
  - **Pfosten** / **Ständer** (Forward-Verweis): vertikales Stab-
    Bauteil im Wandbau; trägt Vertikallasten. Der Riegel ist
    horizontal und ist gerade nicht der Pfosten.
  - **Sturz** (Forward-Verweis): tragendes Bauteil über einer
    Wand-Öffnung. Im Holzbau **kann** ein Sturzriegel die
    Sturzfunktion übernehmen (Doppelnatur, siehe Erläuterung);
    der Sturz im allgemeinen Hochbau-Sinn ist werkstoffneutral
    (Mauerwerk, Stahl, Stahlbeton, Holz) und kein Riegel.
  - **Kehlbalken** (`kehlbalken`): horizontaler Querbalken
    zwischen einem Sparrenpaar zur Dachaussteifung. Strukturell
    analog zum Wand-Riegel (Querbalken zwischen zwei vertikal
    oder geneigt verlaufenden Stäben), aber im Dachtragwerk
    statt in der Wand verortet.
  - **Bauteil** (`bauteil`): der Riegel ist eine Spezialisierung
    von Bauteil mit zusätzlichen geometrischen Constraints; ein
    Bauteil ohne Bauteilrolle ist kein Riegel.

## Implementierungshinweis

Datentyp (Domänen-Schicht, Kotlin, Schicht `domain.bauteil`):

```kotlin
package domain.bauteil

import domain.Toleranzen
import domain.bauteil.Bauteil
import domain.bauteil.Bauteilachse
import domain.geometrie.Einheitsvektor
import domain.geometrie.Ebene
import domain.geometrie.Punkt
import kotlin.math.abs

/**
 * Riegel als Bauteilrolle: horizontales Stab-Bauteil zwischen zwei
 * vertikal stehenden Stab-Bauteilen (Pfosten / Ständern) in einer
 * gemeinsamen Wandebene; primär aussteifend, ohne primären
 * vertikalen Lastpfad.
 *
 * Glossar: hg_riegel.md
 *
 * Die Sub-Lesarten Brust-/Sturz-/Stockwerks-/Zwischen-/Kopf-/
 * Schwellen-/Rähm-Riegel sind Positions-Annotationen, keine
 * Subtypen. Sie werden über das Merkmal `position` getragen.
 *
 * Vorzeichenkonvention: Die Bauteilachse ist gerichtet, aber welcher
 * Endpunkt p_a bzw. p_e ist, ist nicht durch eine geometrische
 * Bedingung festgelegt (analog zu Pfette und Latte). Empfehlung
 * gemäß hg_bauteilachse.md: p_a nach lokaler
 * Bezeichnungskonvention.
 */
data class Riegel(
    val bauteil: Bauteil,
    /** Wandebene; aus den Pfostenachsen abgeleitet. */
    val wandebene: Ebene,
    /** Positions-Annotation in der Wand. Default UNSPEZIFIZIERT. */
    val position: RiegelPosition = RiegelPosition.UNSPEZIFIZIERT,
) {
    val achse: Bauteilachse.Gerade
        get() = (bauteil.geometrie as Bauteilgeometrie.Stab).achse
                as Bauteilachse.Gerade
    val laenge: Double get() = achse.laenge          // mm
    val richtung: Einheitsvektor get() = achse.richtung
    val hoehe: Double                                 // mm, mittlere z-Lage
        get() = (achse.anfang.z + achse.ende.z) / 2.0

    /**
     * Horizontalitätsprädikat: |⟨d_hat, e_z⟩| ≤ KOLLINEAR_EPS.
     *
     * Sinus-Test gegen e_z-Parallelität; KOLLINEAR_EPS ist
     * bevorzugt für Lot- und Parallelitäts-Prädikate
     * (siehe hauptglossar/HG_KONVENTIONEN.md §4).
     */
    fun istHorizontal(eps: Double = Toleranzen.KOLLINEAR_EPS): Boolean =
        abs(richtung.z) <= eps
}

/**
 * Positions-Annotation eines Riegels in der Wand. Die Sub-Lesarten
 * unterscheiden sich durch Höhenlage und Öffnungs-Bezug, nicht
 * durch eigene geometrische oder statische Constraints. Daher
 * Merkmal, nicht Subtyp.
 *
 * Glossar: hg_riegel.md (siehe Erläuterung „Riegelpositionen in
 * der Wand").
 */
enum class RiegelPosition {
    /** Unterhalb einer Fenster-Öffnung, auf Brüstungshöhe. */
    BRUST,
    /** Oberhalb einer Tür- oder Fenster-Öffnung; Doppelnatur mit Sturz. */
    STURZ,
    /** Oberster Riegel pro Stockwerk, nahe Geschossdecke. */
    STOCKWERK,
    /** Zwischen anderen Riegeln, ohne Öffnungs-Bezug. */
    ZWISCHEN,
    /** Kopf-, Schwellen-, Rähm-Riegel und nicht klassifizierbare Lagen. */
    SONSTIGE,
    /** Position nicht zugewiesen (Default). */
    UNSPEZIFIZIERT,
}

sealed class RiegelEntartet {
    object Nullachse                    : RiegelEntartet()
    object NichtHorizontal              : RiegelEntartet()
    object NichtInWandebene             : RiegelEntartet()
    object NichtRechtwinkligZuPfosten   : RiegelEntartet()
    object EndpunktNichtAnPfosten       : RiegelEntartet()
    object WandebeneNichtLotrecht       : RiegelEntartet()
}
```

- **Einheit**: Längen in mm (Double); Winkel intern in Radiant.
- **Identität**: `BauteilId` aus dem zugrunde liegenden Bauteil
  (Memory `project_bauteil_identifikation`).
- **Invarianten** (in der Factory `riegelAusBauteil(...)` prüfen,
  bei Verletzung `Resultat.Fehler` mit `RiegelEntartet`-Variante;
  niemals Exception):
  1. Stabgeometrie und Bauteilachse vom Typ `Bauteilachse.Gerade`.
  2. Achsenlänge > Toleranzen.LAENGE_EPS — sonst `Nullachse`.
  3. |⟨d_hat, e_z⟩| ≤ Toleranzen.KOLLINEAR_EPS — sonst
     `NichtHorizontal` (Sinus-Test gegen e_z-Parallelität;
     KOLLINEAR_EPS, vgl. HG_KONVENTIONEN.md §4).
  4. Wandebene lotrecht: |⟨n_hat_W, e_z⟩| ≤ Toleranzen.KOLLINEAR_EPS
     — sonst `WandebeneNichtLotrecht`.
  5. Beide Endpunkte in Wandebene (Punkt-Ebene-Abstand ≤
     Toleranzen.LAENGE_EPS) — sonst `NichtInWandebene`.
  6. Rechtwinkligkeit zu beiden begrenzenden Pfostenachsen:
     |⟨d_hat, v_hatᵢ⟩| ≤ Toleranzen.KOLLINEAR_EPS für i = 1, 2 — sonst
     `NichtRechtwinkligZuPfosten` (Sinus-Test).
  7. Endpunkte fallen mit Pfostenachsen zusammen
     (Punkt-Gerade-Abstand ≤ Toleranzen.LAENGE_EPS) — sonst
     `EndpunktNichtAnPfosten`.
- **Edge Cases**:
  - **Sturzriegel** mit Doppelnatur Sturz: `position = STURZ`;
    die Riegel-Constraints bleiben anwendbar; die Sturz-
    Funktion ist Eigenschaft der Tragwerks-Analyse und wird in
    einer eigenen Sturz-Modellierung getragen (Folgearbeit).
  - **Schiefstehende Pfosten** (Schwellenverdrehung beim
    Aufrichten): die Lot-Bedingung an v_hatᵢ schlägt fehl; der
    Riegel würde dann nicht mehr horizontal an die Pfosten
    anschließen. In der Praxis wird die Wand vor dem Einsetzen
    der Riegel ausgerichtet; ein kleiner Toleranzbereich ist
    durch KOLLINEAR_EPS abgedeckt.
  - **Dach-Riegel** (Druckriegel, Spannriegel, Sprengriegel,
    Binderriegel): NICHT als `Riegel` instanziieren; eigene
    Bauteilrolle bei Aufnahme historischer Dachformen
    (Folgearbeit: Hängewerk-/Sprengwerk-Tool).
  - **Fliegender Quer-Balken ohne Endauflager an zwei
    Pfosten**: ist kein Riegel im Sinne dieses Eintrags;
    Bedingung 5 (`EndpunktNichtAnPfosten`) schlägt fehl. Solche
    Bauteile werden als allgemeines Stab-Bauteil ohne Rolle
    geführt.
  - **Sehr kurze Riegel** (Stürze über schmaler Öffnung
    zwischen eng stehenden Pfosten): Definition unverändert
    anwendbar; Bedingung 1 (`Nullachse`) schlägt nur bei
    entarteter Achse fehl.
- **Abgeleitete Eigenschaften** (als Funktionen):
  - `pfostenAnSchluss(t: Tragwerk): Pair<Pfosten, Pfosten>?` —
    die beiden Pfosten, an denen der Riegel anschließt; null,
    wenn keine eindeutige Zuordnung möglich.
  - `gefachOben(t: Tragwerk): Riegel?` /
    `gefachUnten(t: Tragwerk): Riegel?` — angrenzende Riegel
    im selben Gefach-Stapel (Folgearbeit: erste Gefach-
    Modellierung).
- **Bezeichner-Konvention** (CLAUDE.md): Klasse heißt `Riegel`
  (deutsch, Glossarbegriff); Positions-Enum heißt
  `RiegelPosition`. Spezialisierungs-Subtypen sind nicht
  vorgesehen.
- **Folgearbeit-Trigger** (für `_FOLGEARBEITEN_*.md` oder die
  Wand-Welle-Planung):
  - `pfosten` / `ständer`: Träger des Riegels; Pflicht-
    Eintrag der Wand-Welle.
  - `schwelle`: unterstes Wand-Längsholz; Wand-Welle.
  - `raehm`: oberstes Wand-Längsholz; Wand-Welle.
  - `sturz`: bei erster Wand-Öffnungs-Modellierung
    (Tür/Fenster), trägt die Doppelnatur-Funktion des
    Sturzriegels.
  - `druckriegel` / `spannriegel` / `sprengriegel` /
    `binderriegel`: Dach-Riegel-Lesart; eigener
    Hauptglossar-Eintrag erst beim Hängewerk- oder
    Sprengwerk-Tool — diese App führt die Lesart **jetzt
    nicht**.
  - `wand` (Aggregat, mit Welle 12 angelegt, siehe
    `hg_wand.md`): der Riegel ist Mitglied einer
    Wand-Bauteilgruppe. Eine Zwischenebene `wandbauteil`
    wurde mit Welle 12 verworfen (App-Drift); die
    Sammel-Funktion „Wand-Bauteilrolle" wird über die
    Aggregat-Mitgliedschaft realisiert.

## Quellen

**Primär (normativ):**

- SIA 265:2021, „Holzbau", Schweizerischer Ingenieur- und
  Architektenverein, Zürich.
- DIN EN 1995-1-1:2010-12, „Eurocode 5: Bemessung und Konstruktion
  von Holzbauten – Teil 1-1".
- DIN 1052:2008-12, „Entwurf, Berechnung und Bemessung von
  Holzbauwerken".

**Sekundär:**

- Lignum (Hrsg.): *Holzbautabellen HBT 1 (2024).* Lignum, Zürich.
- Lignum-Glossar `konstruktion`: lignum.ch/holz_a_z/konstruktion/.
- Mönck, W.; Rug, W.: *Holzbau – Bemessung und Konstruktion.*
  16. Auflage, Beuth, Berlin 2015.
- Natterer, J.; Herzog, T.; Volz, M.: *Holzbau-Atlas.* 4. Auflage,
  Birkhäuser, Basel 2003.
- Gerner, M.: *Fachwerk – Instandsetzung, Sanierung, Neubau.* DVA,
  7. Auflage 2007.
- Thesaurus traditioneller Holzbau (TTH), RWTH Aachen, Lemma
  „Riegel (Fachwerk)" (begriff_id 971).
- RDK Labor — Reallexikon zur Deutschen Kunstgeschichte, Lemma
  „Fachwerk, Fachwerkbau".
- DWDS — Etymologisches Wörterbuch des Deutschen, Lemma „Riegel"
  (dwds.de/wb/etymwb/Riegel).

**Korpus (nicht autoritativ):**

- Wikipedia, Lemma „Riegel (Bauteil)", „Fachwerkhaus",
  „Ständerbauweise" (abgerufen 2026-05-14).
- bauredakteur.de — „Fachwerk – Begriffe und Konstruktion"
  (abgerufen 2026-05-14).
- architektvergleich.ch — „Riegelbau Schweiz" (abgerufen
  2026-05-14).
- Recherche-Bericht: `docs/recherche/2026-05-14_hg_riegel.md`.
