---
id: kehlbalken
benennung: Kehlbalken
kurz: "Ein Kehlbalken ist ein waagrechter Balken, der zwei gegenüberliegende Dachsparren auf halber Höhe miteinander verbindet, damit sie sich nicht durchbiegen oder auseinanderdrücken."
synonyme: [Kehlriegel]
abgelehnte_benennungen: [Hahnenbalken, Spannriegel, Zange, Kehlzange, "collar beam", "collar tie", "collar", "rafter tie"]
oberbegriff: bauteil
begriffstyp: bauteilrolle
voraussetzungen: [bauteil, bauteilachse, strecke, einheitsvektor, ebene, sparren, weltkoordinatensystem, toleranzen]
abgrenzung_zu: [sparren, pfette, bundbalken, hahnenbalken, binder, sparrenbinder, kehlbalkenbinder, kehlbalkendach, zange, kehlzange, dachflaeche, kehle, knagge, bauteil, tragwerk]
status: entwurf
subglossar_pendant: notwendig
quellen_primär:
  - "SIA 265:2021 'Holzbau', Schweizerischer Ingenieur- und Architektenverein, führt 'Kehlbalken' nicht als Fachausdruck (§1.1 / Anhang G) noch als Lemma; §4 'Tragwerksanalyse und Bemessung' und §5 'Bauteile und Strukturen' behandeln nur generische Tragglieder (Träger §5.1, Scheiben §5.4, Platten §5.5), zusammengesetzte Stäbe über §5.3 'Zusammengesetzte Bauteile'. Vorausgesetzter Berufsbegriff. [direkt]"
  - "SIA 232/1:2020 'Geneigte Dächer', Abschnitt 1 (Begriffe und geometrische Grundlagen) — Kehlbalken als vorausgesetzter Berufsbegriff im Kontext geneigter Dächer; keine geschlossene Begriffsdefinition."
  - "DIN EN 1995-1-1:2010-12 (Eurocode 5), Abschnitt 5 (Tragwerksberechnung) und Abschnitt 6 (Grenzzustände der Tragfähigkeit, Knicken) — Kehlbalken implizit als wechselbeanspruchter Stab (Druck/Zug) eines statisch unbestimmten Sparrentragwerks; keine geschlossene Begriffsdefinition."
  - "DIN 1052:2008-12, Abschnitt 8 und Abschnitt 12 (Konstruktive Anforderungen) — Kehlbalken als vorausgesetzter Tragwerks-Begriff."
quellen_sekundär:
  - "Lignum (Hrsg.): Holzbautabellen HBT, Lignum, Zürich, aktuelle Auflage, Kap. 'Dachtragwerke / Kehlbalkendach'."
  - "Lignum (Hrsg.): Lignatec 'Geneigte Dächer in Holzbauweise', Abschnitt zu Kehlbalken- und Sparrenanschlüssen."
  - "Mönck, W.; Rug, W.: Holzbau – Bemessung und Konstruktion. 16. Aufl., Beuth, Berlin 2015, Kap. 11 'Dachtragwerke', § Kehlbalkendach."
  - "Blass, H. J.; Sandhaas, C.: Ingenieurholzbau – Grundlagen der Bemessung. KIT Scientific Publishing, Karlsruhe 2016, Kap. 5 (Stabbauteile, Knicken) und Kap. 7."
  - "Natterer, J.; Herzog, T.; Volz, M.: Holzbau-Atlas. 4. Aufl., Birkhäuser, Basel 2003, Kap. 'Dachtragwerke / Kehlbalkendach'."
  - "Gerner, M.: Fachwerk – Instandsetzung, Sanierung, Neubau. DVA, 7. Aufl. 2007, Glossar 'Kehlbalken'."
  - "Krämer, V.: Grundwissen des Zimmerers. Bruderverlag, Karlsruhe 1988, Kap. Dachtragwerke."
quellenkonflikt: |
  **Norm-Lücke.** Weder SIA 265:2021, SIA 232/1:2020, DIN EN 1995-1-1:2010
  noch DIN 1052:2008 enthalten eine geschlossene Begriffsdefinition für
  „Kehlbalken"; der Begriff wird in allen konsultierten Normen
  vorausgesetzt und nur über seine konstruktive Rolle
  (horizontales Aussteifungs- und Riegel-Bauteil zwischen einem
  Sparrenpaar) sowie die zugehörige Tragwerks-Bauart (Kehlbalkendach
  als statisch unbestimmtes System) charakterisiert. Die Quellenlage
  ist damit **identisch zu Sparren, Pfette und Binder**. Detail-Befund
  siehe [intern].

  Eigene Festlegung in diesem Glossar:

  - Ein Kehlbalken ist ein **Bauteil mit Bauteilrolle „Kehlbalken"**,
    dessen Bauteilachse horizontal verläuft, in der Tragebene eines
    Sparrenpaars liegt, beide Sparren des Paars an ihren Bauteilachsen
    miteinander verbindet und damit oberhalb des Sparrenfuß-Niveaus
    und unterhalb des Sparrenfirst-Niveaus angeordnet ist.
  - Die geometrische Definition stützt sich auf die topologische
    Lage **zwischen Sparrenfuß und Sparrenfirst**, nicht auf eine
    exakte Höhe oder ein exaktes Drittel der Sparrenlänge (siehe
    Höhenlage-Konflikt unten).

  **Höhenlage — Korpus-Konflikt.** Die konsultierten Quellen geben
  unterschiedliche Faustregeln für die Höhenlage des Kehlbalkens:

  - „auf halber Sparrenhöhe" — Wiktionary, Duden, BauNetz Wissen,
    Wikipedia (Mittel-Hoch).
  - „in Sparrenmitte (Ort maximaler Sparren-Durchbiegung)" — Statik-
    Lehrbücher, wissenwiki.de (Mittel).
  - „im oberen Drittel der Sparrenhöhe" — englische collar-tie-Lehre
    (finehomebuilding.com, internachi.org), Praxisempfehlungen
    (Niedrig).

  Statisch optimal liegt der Kehlbalken in Sparrenmitte (Knicklänge
  maximal halbiert; Mönck/Rug 16. Aufl. Kap. 11); konstruktiv wird er
  für Raumhöhe häufig höher angeordnet (oberes Drittel). Die App
  führt die Höhenlage als **Faustregel-Bandbreite (halbe bis obere
  Drittel-Sparrenhöhe)** in der Erläuterung, **nicht** als
  geometrische Constraint. Die Abgrenzung zu Bund- und Hahnenbalken
  erfolgt **topologisch** (oberhalb Sparrenfuß, unterhalb
  Sparrenfirstpunkt), nicht über eine numerische Höhe.

  **Etymologie — „Kehl-" ≠ Dachkehle.** Das Bestimmungswort „Kehl-"
  verweist auf die anatomische **Kehle** im Sinne von Hals und
  Schlund (althochdeutsch *kela*, mittelhochdeutsch *kel(e)*,
  idg. Wurzel *gel-* „verschlingen, Hohlraum"), **nicht** auf die
  **Dachkehle** als Schnittlinie zweier einspringend
  zusammenstoßender Dachflächen (siehe spätere Folgearbeit `kehle`).
  Bildlich liegt der Kehlbalken im sich verengenden, „kehligen"
  Raum zwischen den zusammenlaufenden Sparren („Hals des Daches").
  Beide Lesarten teilen die indogermanische Wurzel, sind im
  Holzbau aber strikt zu trennen. Quelle: DWDS-Eintrag „Kehle",
  Wiktionary-Eintrag „Kehlbalken".

  **Hahnenbalken — kein Synonym, eigenständiges Geschwister-Bauteil.**
  Der Hahnenbalken ist ein kurzer horizontaler Druckriegel
  **kurz unterhalb des Firstes** zwischen einem Sparrenpaar. Im
  DACH-Korpus (Wikipedia, oldenburg-zimmerei.com, bauen.wiki) ist
  er als **eigenständiges Bauteil oberhalb des Kehlbalkens**
  klar unterschieden — strukturell parallel zum Kehlbalken, aber
  geometrisch durch seine Lage nahe am First und konstruktiv durch
  seine kurze Länge (Faustregel < ca. 3,5 m, sonst Kehlbalken)
  von ihm getrennt. Etymologie „Hahnen-Balken" — Aufsitz für
  Hühner in Bauernhäusern (Wikipedia). Daraus folgt: Hahnenbalken
  ist hier in `abgelehnte_benennungen` geführt, weil er im Korpus
  gelegentlich verwirrend mit Kehlbalken gleichgesetzt wird, und
  zusätzlich in `abgrenzung_zu` als Forward-Verweis (Kategorie A,
  Trigger: erste historische Dachstuhl-Modellierung mit mehreren
  Querholz-Ebenen).

  **Bundbalken — kein Sonderfall, kein Synonym.** Der Bundbalken
  (Synonym: Binderbalken, Dachbalken) liegt horizontal **am
  Sparrenfuß** in derselben Sparrenpaar-Ebene wie der Kehlbalken
  und ist geometrisch in der **Richtung** identisch, in der
  **Höhenlage** und **statischen Rolle** aber **gegensätzlich**:

  - Bundbalken **am Sparrenfuß** (Höhe ≈ Traufniveau),
    Kehlbalken oberhalb des Sparrenfußes.
  - Bundbalken **dauerhaft Zugband** (Aufnahme des
    Horizontalschubs, schliesst das statische Sparrendreieck),
    Kehlbalken **wechselbeanspruchter Riegel** (Druck bei
    symmetrischer Last, Zug bei Wind/asymmetrischer Last).
  - Bundbalken ist konstitutiv für den **Sparrenbinder**
    (Bauteilgruppe nach `hg_binder.md`); Kehlbalken erweitert
    diesen zum **Kehlbalkenbinder**.

  Damit ist der Bundbalken **kein Sonderfall** des Kehlbalkens
  und der Kehlbalken **kein Sonderfall** des Bundbalkens; beide
  sind strukturell parallele Bauteilrollen unter `bauteil` und in
  `abgrenzung_zu` als Forward-Verweise (Kategorie A, Trigger:
  erste Sparrenbinder-Modellierung) geführt.

  **Spannriegel — mehrdeutig, in `abgelehnte_benennungen`.** Im
  Sparrendach-Kontext wird „Spannriegel" gelegentlich synonym zu
  Kehlbalken verwendet (Mönck/Rug-Sekundär, wissenwiki.de). Im
  Stuhl-Kontext (liegender Stuhl im Pfetten- oder Kehlbalkendach)
  bezeichnet „Spannriegel" jedoch ein eigenständiges Bauteil
  zwischen den liegenden Stuhlsäulen (technik.de-academic.com).
  Wegen der Mehrdeutigkeit wird „Spannriegel" hier **nicht** als
  Synonym geführt, sondern als abgelehnte Benennung; die Stuhl-
  Kontext-Lesart bleibt für den künftigen Eintrag `stuhl`
  (Folgearbeit aus `hg_dachstuhl.md`) reserviert.

  **Zange / Kehlzange — Anschluss-Form, nicht Synonym.** Eine
  Zange ist ein zweiteiliges Bauteil, beidseitig am Sparren mit
  Bolzen oder Stabdübeln angeschlagen (Wikipedia „Zange
  (Bauteil)"). Eine **Kehlzange** übernimmt die Rolle des
  Kehlbalkens als zweiteilige Bauart (anstelle eines
  einteiligen, zentral geführten Balkens). Die Anschluss- bzw.
  Querschnitts-Form ist damit eine Bauart-Klassifikation, **nicht**
  eine Synonymie. Geführt als Forward-Verweis (Kategorie A,
  Trigger: erstes Tool, das Zangen-Bauart modelliert).

  **Englische Anglizismen — false friend.** Im englischen
  Schrifttum gilt: *collar beam* / *collar tie* = Kehlbalken;
  *rafter tie* = **Bundbalken** (Zugband am Sparrenfuß), **nicht**
  Kehlbalken (Wikipedia „Collar beam", finehomebuilding.com,
  nachi.org). Die DACH-Trennung Bundbalken / Kehlbalken
  korrespondiert konsistent zur US-Trennung rafter tie / collar
  tie; eine Übernahme des englischen Begriffsapparats würde
  diese Korrespondenz zerstören. Daher sind alle englischen
  Bezeichnungen in `abgelehnte_benennungen` geführt; *rafter
  tie* ist zusätzlich explizit als false friend dokumentiert
  (US-Bedeutung = Bundbalken, nicht Kehlbalken).

  **CH/DE-Praxis.** Der Begriff ist in der Schweiz und in
  Deutschland **identisch** verwendet; ein länderspezifischer
  Bedeutungsunterschied ist nicht belegt. Praktisch ist das
  Kehlbalkendach im Schweizer Wohnbau aufgrund der Dominanz des
  Pfettendachs seltener als in Deutschland; diese
  Häufigkeits-Information ist Eigenschaft der Tragwerks-Bauart
  und gehört in den künftigen Eintrag `kehlbalkendach`.

  Diese Festlegungen sind konsistent mit allen konsultierten
  Quellen.
---

## Prosa-Definition

Ein **Kehlbalken** ist ein Stab-Bauteil eines Dachtragwerks, dessen
Bauteilachse horizontal verläuft, in der Tragebene eines Sparrenpaars
liegt und die Bauteilachsen der beiden Sparren des Paars zwischen
ihren Sparrenfuß- und Sparrenfirstpunkten verbindet, sodass die
Knicklänge der Sparren reduziert und die Sparrenpaar-Ebene durch
einen wechselbeanspruchten Druck- bzw. Zugriegel zu einem statisch
unbestimmten Tragwerk (Kehlbalkendach) ergänzt wird.

## Mathematische Definition

Sei

- B ein Bauteil im Sinne von `bauteil` mit Stabgeometrie
  (`geometrie ∈ 𝒢_stab`),
- a(B) = Bauteilachse.Gerade(p_a, p_e) die Bauteilachse von B im
  geraden Fall (siehe `bauteilachse`), mit
  d_hat:= (p_e − p_a) / ‖p_e − p_a‖ ∈ S² ⊂ ℝ³,
- (S₁, S₂) ein Sparrenpaar im Sinne von `sparren`, mit
  Sparrenfuß-Punkten p^{(i)}_fuß und Sparrenfirstpunkten
  p^{(i)}_first für i ∈ {1, 2},
- E_paar die **Sparrenpaar-Ebene**, d. h. die durch die vier
  Punkte p^{(1)}_fuß, p^{(1)}_first, p^{(2)}_fuß, p^{(2)}_first
  aufgespannte Ebene (siehe `ebene`); die vier Punkte sind
  voraussetzungsgemäss koplanar bis ε_L (geometrische
  Konsistenz-Bedingung eines Sparrenpaars),
- n_paar ∈ S² ein Einheitsnormalenvektor von E_paar,
- e_z:= (0, 0, 1)ᵀ die Welt-Lotachse,
- ε_K:= Toleranzen.KOLLINEAR_EPS,
  ε_W:= Toleranzen.WINKEL_EPS,
  ε_L:= Toleranzen.LAENGE_EPS.

Dann heißt B ein **Kehlbalken** des Sparrenpaars (S₁, S₂) genau
dann, wenn die folgenden Bedingungen erfüllt sind:

1. **Stabgeometrie**: B besitzt eine gerade Bauteilachse mit
   ‖p_e − p_a‖ > ε_L.

2. **Horizontalitätsbedingung**: Die Bauteilachsenrichtung ist
   horizontal,
   ```
   |⟨d_hat, e_z⟩| ≤ ε_K,
   ```
   d. h. die Bauteilachse steht rechtwinklig zur Welt-Lotachse.
   Die Form des Tests ist ein **Sinus-Test gegen `e_z`-
   Parallelität** und damit ein Lot-Prädikat; nach `HG_KONVENTIONEN.md`
   Sektion 4 ist `KOLLINEAR_EPS` die einschlägige Toleranzkonstante
   (bevorzugt für Lot- und Parallelitäts-Prädikate, weil der Sinus
   in der Nähe von 0 gut konditioniert ist). Diese Bedingung ist
   formal identisch zur Horizontalitätsbedingung der Pfette.

3. **Lage in der Sparrenpaar-Ebene**: Beide Endpunkte der
   Bauteilachse liegen in E_paar bis ε_L,
   ```
   |⟨n_paar, p_a − q₀⟩| ≤ ε_L  und  |⟨n_paar, p_e − q₀⟩| ≤ ε_L,
   ```
   wobei q₀ ein beliebiger Stützpunkt von E_paar ist (z. B.
   q₀ = p^{(1)}_fuß).

4. **Anschluss an beide Sparrenachsen**: Die beiden Endpunkte
   liegen — bis auf eine zuordnungsabhängige Permutation —
   auf den Bauteilachsen der beiden Sparren des Paars. Formal:
   es gibt eine Bijektion σ: {a, e} → {1, 2} und reelle
   Parameter t_a, t_e ∈ [0, 1] derart, dass
   ```
   ‖p_a − (p^{(σ(a))}_fuß + t_a · (p^{(σ(a))}_first − p^{(σ(a))}_fuß))‖ ≤ ε_L
   ‖p_e − (p^{(σ(e))}_fuß + t_e · (p^{(σ(e))}_first − p^{(σ(e))}_fuß))‖ ≤ ε_L.
   ```
   Die Endpunkte p_a, p_e liegen damit auf den geraden
   Bauteilachsen der beiden Sparren, jeweils im offenen Bereich
   zwischen Sparrenfuß und Sparrenfirst.

5. **Topologische Trennung zum Bundbalken (oberhalb Sparrenfuß)**:
   Die Endpunkt-Höhenkoordinaten liegen oberhalb der Sparrenfuß-
   Höhenkoordinaten,
   ```
   p_a.z > p^{(σ(a))}_fuß.z + ε_L
   p_e.z > p^{(σ(e))}_fuß.z + ε_L.
   ```
   Äquivalent: t_a > 0, t_e > 0 in Bedingung 4 (mit Sparren-
   Vorzeichenkonvention nach `hg_sparren.md` Bedingung 4,
   t = 0 am Sparrenfuß, t = 1 am Sparrenfirstpunkt).

6. **Topologische Trennung zum Hahnenbalken (unterhalb
   Sparrenfirst)**: Die Endpunkt-Höhenkoordinaten liegen
   unterhalb der Sparrenfirstpunkt-Höhenkoordinaten,
   ```
   p_a.z < p^{(σ(a))}_first.z − ε_L
   p_e.z < p^{(σ(e))}_first.z − ε_L.
   ```
   Äquivalent: t_a < 1, t_e < 1 in Bedingung 4.

Wesentliche abgeleitete Größen:

- **Kehlbalkenlänge**: L_K:= ‖p_e − p_a‖ (in mm), entlang der
  Bauteilachse zwischen den beiden Anschlusspunkten an den Sparren.
- **Kehlbalken-Höhenlage**: z_K:= (p_a.z + p_e.z) / 2; bei einer
  exakt horizontalen Bauteilachse gilt p_a.z = p_e.z = z_K nach
  Bedingung 2.
- **Sparrenpaar-Ebene** E_paar: die Tragebene des Kehlbalkens; sie
  ist rechtwinklig zur Trauflinie und enthält die beiden Sparren-
  Bauteilachsen.
- **Höhenparameter** t_bar:= (t_a + t_e) / 2 ∈ (0, 1): mittlerer
  Sparren-Längenparameter der beiden Anschlusspunkte; charakterisiert
  die Höhenlage des Kehlbalkens relativ zur Sparrenlänge. Dient als
  abgeleitete Klassifikations-Größe (Faustregel-Bandbreite), nicht
  als Definitions-Constraint.

## Wohldefiniertheit

- **Existenz**: Für ein Sparrenpaar (S₁, S₂) mit positiv
  überlappendem Höhenbereich der Sparrenachsen und nicht-entarteter
  Sparrenpaar-Ebene ist die Definition konstruktiv erfüllbar: man
  wähle t_a = t_e =: t ∈ (0, 1), nehme als p_a den Sparren-S₁-
  Achsenpunkt zum Parameter t und als p_e den Sparren-S₂-
  Achsenpunkt zum Parameter t. Bei symmetrischen Sparrenpaaren
  (gleiche Sparrenlänge, gleiche Neigung, spiegelsymmetrische Lage
  zur Firstebene) sind die beiden Punkte automatisch gleich hoch,
  und der so konstruierte Stab ist horizontal (Bedingung 2 erfüllt).
- **Eindeutigkeit der Bauteilachsen-Orientierung**: Anders als beim
  Sparren (`hg_sparren.md` Bedingung 4, Falllinien-orientiert) und
  anders als bei vorzeichen-konventionierten Pfetten gibt es beim
  Kehlbalken **keine kanonische** Welt-bezogene Orientierungs-
  Vorgabe: das Sparrenpaar ist gegenüber seiner Mittelsenkrechten
  spiegelsymmetrisch, und Welt-Lot e_z liegt rechtwinklig zu d_hat
  (Bedingung 2), sodass weder Falllinie noch Lot eine Richtung
  innerhalb d_hat auszeichnen. Die Bijektion σ: {a, e} → {1, 2}
  in Bedingung 4 ist daher **konventional** und keine Eigenschaft
  des Kehlbalkens selbst; sie ist Bestandteil der Bauteilachse-
  Konstruktion und kann etwa lexikographisch über die Bauteil-
  Identitäten der beiden Sparren festgelegt werden (S₁-anschluss
  → p_a, S₂-anschluss → p_e mit `id(S₁) < id(S₂)`). Diese
  Konvention ist nicht Bestandteil der Definition und wird in der
  Implementierung am Konstruktor festgehalten.
- **Symmetrie der Bedingungen 5 und 6**: Die topologische Trennung
  zu Bund- und Hahnenbalken erfolgt über die Sparren-Längsparameter
  t_a, t_e und nicht über eine numerische Höhenschwelle. Damit ist
  sie unabhängig von Welt-Koordinaten, von der absoluten Sparrenfuß-
  Höhe und von der Wahl der Sparrenpaar-Ebene; sie überträgt sich
  konsistent auf Pultdach-Kehlbalken (verschiedene Sparrenneigungen
  links/rechts) und auf asymmetrische Sparrenpaare, sofern dort die
  Definition eines Sparrenpaars trägt.
- **Toleranzen-Wahl**: Bedingung 2 ist ein Sinus-Test gegen
  e_z-Parallelität (→ `KOLLINEAR_EPS` nach `HG_KONVENTIONEN.md` §4);
  Bedingungen 3, 4, 5, 6 sind Längen- bzw. Koordinaten-Tests
  (→ `LAENGE_EPS`); ein expliziter Winkel-Skalar zwischen Bauteil-
  Vektoren wird in der Definition nicht gebildet, weshalb
  `WINKEL_EPS` nicht eingreift. Die Anwendung folgt der in
  `HG_KONVENTIONEN.md` §4 festgelegten **Form-des-Tests**-Regel.
- **Nicht-Zirkularität**: Die Definition stützt sich nur auf bereits
  definierte Begriffe (`bauteil`, `bauteilachse`, `strecke`,
  `einheitsvektor`, `ebene`, `sparren`, `weltkoordinatensystem`,
  `toleranzen`). Der Begriff Kehlbalken kommt nicht in seiner
  eigenen Definition vor und verweist insbesondere **nicht** auf
  Bund- oder Hahnenbalken (deren Abgrenzung topologisch über
  Sparren-Längsparameter erfolgt, nicht über die Bauteilbegriffe
  selbst).
- **Konsistenz Prosa ↔ Formal**: Die Prosa-Bedingungen
  „horizontal", „in der Tragebene eines Sparrenpaars",
  „verbindet die Bauteilachsen der beiden Sparren des Paars
  zwischen ihren Sparrenfuß- und Sparrenfirstpunkten" entsprechen
  formal Bedingungen 2, 3, 4 sowie 5+6 (Letztere zusammen
  realisieren das „zwischen"). Die in der Prosa genannte
  Knicklängen-Reduktion und der Druck-/Zug-Wechsel sind
  **Funktion**, nicht **Geometrie** des Kehlbalkens; sie sind
  Eigenschaften des Tragwerks Kehlbalkendach (siehe Erläuterung).
- **Pultdach-Grenzfall**: Bei einem Pultdach existiert kein
  Sparrenpaar im klassischen Sinn (es gibt nur eine geneigte
  Dachfläche, also nur eine Sparrenrichtung). Damit ist die
  Voraussetzung „Sparrenpaar (S₁, S₂)" nicht erfüllt und ein
  Kehlbalken im Sinne dieser Definition existiert nicht. Aussteifende
  Querhölzer in einem Pultdach gehören dann zu anderen Bauteilrollen
  (Wandriegel, Deckenbalken), nicht zum Kehlbalken.
- **Flachdach-Grenzfall**: Bei α → 0 entartet sowohl die Falllinie
  der Dachflächen als auch der Begriff des Sparrens; das Konstrukt
  Sparrenpaar ist nicht definiert, und damit auch kein Kehlbalken.

## Erläuterung (nicht normativ)

Der Kehlbalken ist das **horizontale Querholz zwischen einem
Sparrenpaar**, das die Sparren in halber bis oberer Drittel-Höhe
miteinander verbindet und damit ihre Knicklänge reduziert. Im
typischen Sparrendach-Schema (zwei Sparren + Bundbalken am Fuß,
statisch bestimmtes Dreigelenk-System) ergänzt der Kehlbalken den
vierten Stab und überführt das System in eine statisch unbestimmte
Konfiguration — das **Kehlbalkendach**.

### Höhenlage in der Praxis

Die Höhenlage des Kehlbalkens ist in den Quellen nicht einheitlich
festgelegt. Die in der App geführte Bandbreite umfasst:

- **halbe Sparrenhöhe** (Wiktionary, Duden, BauNetz Wissen): die
  Bauteilachsen-Anschlusspunkte liegen bei Sparren-Längsparameter
  t ≈ 0,5; statisch optimal, weil dort die Sparrendurchbiegung
  ohne Kehlbalken maximal ist und die Knicklängen-Halbierung
  voll wirkt;
- **Sparrenmitte** (Mönck/Rug-Sekundär, Statik-Lehrbücher): in
  Bemessungs-Kontexten der präferierte Ansatz;
- **oberes Drittel** (englische collar-tie-Lehre, Praxis-
  Empfehlungen): konstruktiv vorteilhaft, wenn unter dem
  Kehlbalken Raumhöhe für ein ausgebautes Dachgeschoss
  benötigt wird (t ≈ 2/3).

Welche dieser drei Lagen im konkreten Tragwerk gewählt wird,
ist Bemessungs- und Werkplan-Entscheidung; die Glossardefinition
fordert lediglich, dass die Anschlusspunkte oberhalb des
Sparrenfußes und unterhalb des Sparrenfirstpunkts liegen
(Bedingungen 5, 6).

### Tragwerks-Funktion

Im **Kehlbalkendach** wirkt der Kehlbalken als:

- **Knickaussteifung** der Sparren: die Sparren-Knicklänge wird
  bei mittiger Lage von L_S (volle Sparrenlänge) auf etwa L_S/2
  reduziert; dadurch sind Sparrenlängen bis ca. 7 m statisch
  möglich (gegenüber ca. 4,5 m im einfachen Sparrendach).
- **Druckstab bei symmetrischer Last** (Eigengewicht, Schnee
  symmetrisch): die Sparrenmittelpunkte gehen aufeinander zu, der
  Kehlbalken wird gestaucht.
- **Zugstab bei asymmetrischer Last** (Windsog, einseitige
  Schneelast): die Sparrenmittelpunkte streben auseinander, der
  Kehlbalken wird gezogen.
- **Biegestab bei ausgebautem Dachgeschoss**, wenn die
  Kehlbalkenlage zugleich als Geschossdecke dient (Verkehrs- und
  Eigenlasten der Decke).

Damit ist der Kehlbalken — anders als der Bundbalken — **nicht**
dauerhaft als Zugband, sondern als **wechselbeanspruchter
Riegel** mit Druck als typischer Hauptbeanspruchung zu
verstehen.

Die **Verschieblichkeit** des Kehlbalkendachs (verschiebliches
vs. unverschiebliches System je nach Vorhandensein einer
ausgesteiften Kehlscheibe) ist eine Eigenschaft des Tragwerks,
nicht des Kehlbalkens selbst; sie ist Gegenstand des künftigen
Eintrags `kehlbalkendach`.

### Querschnitt und Werkstoff

Kehlbalken werden im Schweizer Wohnbau typisch als **Vollholz**
in Festigkeitsklasse C24 (Fichte/Tanne) oder als
**Brettschichtholz** (BSH, GL24h) ausgeführt; übliche Querschnitte
liegen in derselben Größenordnung wie die der zugehörigen
Sparren oder geringfügig darunter. Die konkrete Querschnittsfindung
ist Gegenstand der Bemessung nach SIA 265 / EN 1995-1-1 und liegt
nicht im Definitionsbereich dieses Glossars.

### Faserrichtung

Die **Faserrichtung** eines Kehlbalkens ist im Regelfall
**parallel zur Bauteilachse**: das Bauteil wird so aus dem Stamm
geschnitten, dass die Längsfaser entlang der Bauteillänge
verläuft. In der Domänen-Schicht ist `faserrichtung` Annotation
des Bauteils und für Kehlbalken als **Default ‖ d_hat_Kehlbalken** zu
setzen.

### Anschluss-Bauarten am Sparren

Der Anschluss des Kehlbalkens am Sparren ist **keine geometrische
Constraint** des Kehlbalkens, sondern eine Bauart-Klassifikation:

- **Einteiliger Kehlbalken mit Versatz und Zapfen** (historische
  Bauart): zentral zwischen den Sparren geführt, an beiden
  Sparren mit Zapfen-mit-Versatz angeschlagen. Schwächt den
  Sparren am höchstbeanspruchten Punkt; heute unzeitgemäß.
- **Zweiseitige Kehlzange** (moderne Bauart): zwei Bretter
  beidseitig an den Sparren angeschlagen, mit Bolzen oder
  Stabdübeln verbunden. Keine Querschnittsschwächung der
  Sparren. Geführt als eigener Anschluss-Typ unter Forward-
  Verweis `zange` / `kehlzange`.
- **Einseitiger Kehlbalken mit Lasche und Knaggen**
  (Forward-Verweis `knagge`): Mischbauart mit einem zentralen
  Balken plus seitlichen Verbindungs-Brettern.

Eine Kehlzange übernimmt die **Rolle** Kehlbalken (in der
Glossar-Sicht: zweiteilige Realisierung derselben Bauteilrolle),
ist aber im engeren Sinn kein einteiliger Kehlbalken. Die
Abgrenzung wird im künftigen Eintrag `kehlzange` formal
geführt.

### Kehlbalken in Bauteilgruppen-Aggregaten

Ein Kehlbalken ist typisch Mitglied eines **Kehlbalkenbinders**
(Erweiterung des Sparrenbinders um einen Kehlbalken; siehe
`hg_binder.md` und Folgearbeit `kehlbalkenbinder`). Wie bei
allen Bauteilgruppen-Mitgliedschaften gilt **exklusive
Mitgliedschaft** (`hg_bauteilgruppe.md` Bed. 1): ein Kehlbalken
gehört höchstens zu einem Kehlbalkenbinder.

## Beziehungen

- **Oberbegriff**: `bauteil`. Strukturell ist der Kehlbalken ein
  Bauteil mit der zusätzlichen Rolle „Kehlbalken" und den oben
  formalisierten geometrischen Constraints. Eine zweistufige
  Hierarchie über einen abstrakten Sammelbegriff
  (etwa „Querbalken im Dach") ist nicht angelegt.
- **Voraussetzungen**: `bauteil`, `bauteilachse`, `strecke`,
  `einheitsvektor`, `ebene`, `sparren` (zwingend für die Lage-
  Constraint), `weltkoordinatensystem`, `toleranzen`.
- **Bestandteile (partitiv, vom Bauteil geerbt)**:
  - **Bauteilachse** (`bauteilachse.Gerade`) mit Anschlusspunkten
    an den Bauteilachsen der beiden Sparren des Paars;
  - **Querschnitt** (rechteckig im Regelfall);
  - **Werkstoff** (Vollholz oder BSH);
  - **Faserrichtung** (Annotation, Default ‖ d_hat_Kehlbalken).
- **Verwendung / Beziehung zu anderen Bauteilen**:
  - **Sparren** (`sparren`): jeweils ein Paar bildet die
    Grundlage der Kehlbalken-Definition; der Kehlbalken sitzt
    zwischen den Bauteilachsen der beiden Sparren des Paars.
  - **Bundbalken** (Forward A): paralleles Bauteil am
    Sparrenfuß, mit gegensätzlicher statischer Rolle (Zugband
    statt wechselbeanspruchter Riegel).
  - **Hahnenbalken** (Forward A): paralleles Bauteil oberhalb
    des Kehlbalkens, kurz unter dem First.
  - **Sparrenbinder** und **Kehlbalkenbinder** (`hg_binder.md`,
    Folgearbeit): Bauteilgruppen-Aggregate, in denen Sparren,
    Bundbalken und ggf. Kehlbalken als Bauteile mit exklusiver
    Mitgliedschaft zusammengefasst sind.
  - **Kehlbalkendach** (Folgearbeit): Tragwerks-Bauart, die das
    Sparrendach um den Kehlbalken zu einem statisch
    unbestimmten System ergänzt.
- **Abgrenzung**:
  - **Sparren** (`sparren`): geneigt entlang der Falllinie einer
    Dachfläche; Kehlbalken horizontal rechtwinklig dazu.
    Verletzt Bedingung 2 (Horizontalität).
  - **Pfette** (`pfette`): ebenfalls horizontal, aber **parallel
    zu einer Dachkante** (Traufe, First, Höhenlinie); Kehlbalken
    ist **rechtwinklig zur Trauflinie** und liegt in der
    Sparrenpaar-Ebene (Verletzt der Pfetten-Bedingung 3,
    Parallelität zu einer Dachkante).
  - **Bundbalken** (Forward A): horizontal in der Sparrenpaar-
    Ebene am Sparrenfuß; Anschlusspunkte am Sparrenlängsparameter
    t = 0. Verletzt Bedingung 5 (strikte Lage oberhalb des
    Sparrenfußes).
  - **Hahnenbalken** (Forward A): horizontal in der Sparrenpaar-
    Ebene kurz unterhalb des Sparrenfirstpunkts; kurzer
    Druckriegel mit Faustregel-Länge < ca. 3,5 m. Sehr nahe am
    Sparrenfirst (t → 1). Die Trennung Kehlbalken/Hahnenbalken
    ist im Korpus konventional und im Glossar als
    eigenständiges Geschwister-Bauteil geführt.
  - **Binder** (`binder`): mehrteiliges Trag-Aggregat
    (Bauteilgruppe). Kein Stab-Bauteil im Sinne des Kehlbalkens.
  - **Zange / Kehlzange** (Forward A): zweiteilige Anschluss-
    Bauart; eine Kehlzange übernimmt die Rolle Kehlbalken in
    zweiteiliger Realisierung, ist aber kein einteiliger
    Kehlbalken.
  - **Dachfläche** (`dachflaeche`): zweidimensionales
    geometrisches Bauteil; der Kehlbalken liegt nicht in einer
    Dachflächen-Trägerebene, sondern in der dazu rechtwinkligen
    Sparrenpaar-Ebene.
  - **Kehle** (Dachkehle, Forward A): konkave Schnittlinie zweier
    einspringend zusammenstoßender Dachflächen — **nichts mit dem
    Kehlbalken zu tun** (Etymologie-Klärung; siehe
    Quellenkonflikt-Block).
  - **Tragwerk** (`tragwerk`): Aggregat aus Bauteilen,
    Verbindungen und Auflagern; der Kehlbalken ist Element des
    Tragwerks, nicht selbst Tragwerk.

## Quellen

**Primär (normativ):**

- SIA 265:2021, „Holzbau", Schweizerischer Ingenieur- und
  Architektenverein, Zürich.
- SIA 232/1:2020, „Geneigte Dächer", Schweizerischer Ingenieur-
  und Architektenverein, Zürich.
- DIN EN 1995-1-1:2010-12, „Eurocode 5: Bemessung und Konstruktion
  von Holzbauten – Teil 1-1: Allgemeines".
- DIN 1052:2008-12, „Entwurf, Berechnung und Bemessung von
  Holzbauwerken".

**Sekundär:**

- Lignum (Hrsg.): *Holzbautabellen HBT.* Lignum, Zürich, aktuelle
  Auflage.
- Lignum (Hrsg.): *Lignatec — Geneigte Dächer in Holzbauweise.*
  Lignum, Zürich, aktuelle Auflage.
- Mönck, W.; Rug, W.: *Holzbau – Bemessung und Konstruktion.*
  16. Auflage, Beuth, Berlin 2015 (Kap. 11 Dachtragwerke,
  § Kehlbalkendach).
- Blass, H. J.; Sandhaas, C.: *Ingenieurholzbau – Grundlagen der
  Bemessung.* KIT Scientific Publishing, Karlsruhe 2016 (Kap. 5
  und 7).
- Natterer, J.; Herzog, T.; Volz, M.: *Holzbau-Atlas.* 4. Auflage,
  Birkhäuser, Basel 2003.
- Gerner, M.: *Fachwerk – Instandsetzung, Sanierung, Neubau.*
  DVA, 7. Auflage 2007.
- Krämer, V.: *Grundwissen des Zimmerers.* Bruderverlag,
  Karlsruhe 1988.

**Korpus (nicht autoritativ):**

- BauNetz Wissen, Glossar „Kehlbalken" und Artikel
  „Kehlbalkendach / Statisches System".
- Wikipedia, Lemmata „Sparrendach", „Hahnenbalken", „Kehlbalken",
  „Zange (Bauteil)" (abgerufen 2026-05-14).
- DWDS, Eintrag „Kehle" (etymologische Verankerung).
- Wiktionary, Eintrag „Kehlbalken" (lexikographische Definition).
- Recherche-Bericht [intern].
