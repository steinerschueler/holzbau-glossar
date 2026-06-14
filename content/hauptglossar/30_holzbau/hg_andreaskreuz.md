---
id: andreaskreuz
benennung: Andreaskreuz
kurz: "Ein Andreaskreuz sind zwei schräge Hölzer, die in einem Wandfeld über Kreuz gespannt sind — wie ein grosses X —, damit die Wand bei Wind nicht seitlich wegkippt."
synonyme: [Kreuzstrebe, Strebenkreuz]
abgelehnte_benennungen:
  [Creutzzug, Feuerbock, Malkreuz, Kreuzbock,
   "St. Andrew's Cross", "X-bracing", "cross bracing",
   "saltire brace"]
oberbegriff: bauteilgruppe
begriffstyp: aggregat
voraussetzungen:
  [bauteilgruppe, bauteil, strebe, verbindung, ebene,
   weltkoordinatensystem, lokales_koordinatensystem,
   polyeder, strecke, uuid, toleranzen]
abgrenzung_zu:
  [bauteilgruppe, strebe, kopfband, fussband, knagge,
   mann, wand, schwelle, raehm, staender, riegel,
   verbindung, gefach, fachwerk, riegelbau, brueckmauer,
   brueckschnurmauer, walm, binder]
status: entwurf
subglossar_pendant: notwendig
quellen_primär:
  - "DIN EN 1995-1-1:2010-12 (Eurocode 5), Abschnitt 9 (Bauliche Einzelheiten, Wandscheiben): X-förmige Diagonalverbände als aussteifende Konfiguration konstruktiv vorausgesetzt; alle horizontalen Kräfte in der Ebene des Elements werden aufgenommen."
  - "DIN 1052:2008-12, Abschnitt 8 und 12 (Konstruktive Anforderungen): Diagonalverbände aus Holz für aussteifende Wandverbände vorausgesetzt."
  - "SIA 265:2021 'Holzbau', Schweizerischer Ingenieur- und Architektenverein, führt 'Andreaskreuz' nicht als Fachausdruck (§1.1 / Anhang G geprüft) noch als Lemma; aussteifende Diagonalverbände werden generisch unter §5.8 'Räumliche Stabilisierung und Verbände' behandelt. Vorausgesetzter Berufsbegriff. [direkt]"
  - "Thesaurus Traditioneller Holzbau (TTH), RWTH Aachen, Hierarchie-Facette 1922 'Fachwerk-Bauteile': Andreaskreuz als Konfiguration zweier sich kreuzender Streben in einem Gefach; Primärquelle Großmann 1987 (über TTH indirekt zitiert)."
quellen_sekundär:
  - "Wikipedia, Lemma 'Andreaskreuz (Fachwerk)' (de.wikipedia.org/wiki/Andreaskreuz_(Fachwerk)): X-förmiges Bauteilelement aus diagonal angeordneten Hölzern, das als statisch wirksame Wandaussteifung und Schmuck dient; zwei sich kreuzende Hölzer in einem Gefach; früheste Belege 1452/1457; im 19. Jahrhundert geschosshohe Ausführung; abgelehnte Begriffe Feuerbock und Malkreuz historisch ungenau."
  - "Gerner, M.: Fachwerk – Instandsetzung, Sanierung, Neubau. DVA, 7. Aufl. 2007, Glossar 'Andreaskreuz', 'Kreuzstrebe'."
  - "Mönck, W.; Rug, W.: Holzbau – Bemessung und Konstruktion. 16. Aufl., Beuth, Berlin 2015, Kap. 'Wandscheiben' und 'Aussteifung'."
  - "Natterer, J.; Herzog, T.; Volz, M.: Holzbau-Atlas. 4. Aufl., Birkhäuser, Basel 2003, Kap. 'Wandbau' und 'Fachwerk'."
  - "Großmann, R.: Konstruktionen des deutschen Fachwerkbaus. 1987 — TTH-Primärquelle der Andreaskreuz-Konfiguration."
  - "Wikipedia, Lemma 'Strebe' (de.wikipedia.org/wiki/Strebe): Strebe als generisches Diagonal-Bauteil; Andreaskreuz als Komposition zweier Streben."
  - "Wikipedia, Lemma 'Fachwerkhaus': Andreaskreuz als regionales Ornament-Element in DE-Mitteldeutschland (Frankenwald), Sachsen (Vogtland) und Niedersachsen."
  - "BauNetz Wissen, Glossar-Holz, Lemma 'Andreaskreuz' (baunetzwissen.de)."
  - "Lignum (Hrsg.): Holzbautabellen HBT 1 (2024). Lignum, Zürich. CH-Riegelbau-Diagonalverbände (Volltext nicht zugänglich)."
  - "Recherche-Bericht: [intern] (§D Andreaskreuz)."
  - "Recherche-Bericht (Vorgänger): [intern] (Welle 10, §A.2 Lemma-Disambiguator-Befund, §D.2 Andreaskreuz/Mann-Komposition)."
quellenkonflikt: |
  Fünf Punkte werden hier ausdrücklich aufgelöst.

  **(1) Gefach-Einbau: einfach-Gefach vs. geschossübergreifend.**
  Wikipedia/Andreaskreuz (Fachwerk) führt zwei
  Ausführungs-Varianten:

  - **Einfach-Gefach** (Default, am häufigsten belegt):
    zwei sich kreuzende Streben überspannen **ein
    gemeinsames Gefach** (Wand-Feld zwischen zwei
    benachbarten Ständern oder zwischen Schwelle/Rähm und
    zwei Riegeln). Diese Variante ist seit den frühesten
    Belegen 1452/1457 in Mitteldeutschland und Sachsen
    dokumentiert.
  - **Geschossübergreifend** (19. Jahrhundert, seltener):
    die Diagonalen reichen über mehrere Gefache oder
    sogar mehrere Geschosshöhen.

  Eigene Festlegung: **Default-Lesart ist Einfach-Gefach**;
  die geschossübergreifende Ausführung ist als Edge Case
  im Implementierungs-Hinweis erfasst, hat aber keinen
  eigenen Glossar-Status (gleiche strukturelle
  Komposition aus zwei Streben, lediglich Geometrie-Ausmass
  unterschiedlich).

  **(2) Statisch wirksam und dekorativ — Doppelfunktion.**
  Wikipedia/Andreaskreuz (Fachwerk) formuliert ausdrücklich:
  „statisch wirksame Wandaussteifung **und** Schmuck". Beide
  Funktionen sind im Korpus normativ belegt:

  - **Statisch**: bei wechselnder Windrichtung wirkt
    jeweils eine Strebe als Druck-Diagonale (knickfest),
    die andere als Zug-Diagonale (zugfest). Die X-förmige
    Aussteifung nimmt **alle horizontalen Kräfte in der
    Ebene des Elements auf** (Wikipedia: „erlaubt es, alle
    horizontalen Kräfte in der Ebene des Elements
    aufzunehmen"). Strukturell ist das Andreaskreuz die
    aussteifungs-effizienteste Bauteilgruppe im Gefach.
  - **Dekorativ**: insbesondere in der mitteldeutschen
    Schmuck-Fachwerkbau-Tradition (Vogtländer Fachwerk-
    Schmuckformen, niedersächsisches Fachwerk) wird das
    Andreaskreuz auch als reines Ornament ohne statische
    Wirkung eingesetzt (z. B. an Brüstungsfeldern, an
    Giebeln, an dekorativen Ausfachungen).

  Eigene Festlegung: das Andreaskreuz als Bauteilgruppe
  trägt **strukturell beide Funktionen**; die Differenzierung
  „statisch wirksam vs. rein dekorativ" wird optional über
  das `funktion?`-Feld der Bauteilgruppe (Werte AUSSTEIFEND
  oder DEKORATIV) gemacht, **nicht** durch eigene
  Sub-Begriffe.

  **(3) Abgelehnte Bezeichnungen: Creutzzug, Feuerbock,
  Malkreuz.** Wikipedia/Andreaskreuz (Fachwerk) macht
  explizit:

  - „**Creutzzug**" ist historisch (16.–18. Jahrhundert) für
    das Andreaskreuz belegt, gilt heute aber als
    veralteter Begriff.
  - „**Feuerbock**" und „**Malkreuz**" werden als
    **fachlich falsch** markiert: Feuerbock ist im DACH-
    Korpus ein Eisengestell zum Halten von Brennholz im
    Kamin, kein Holzbau-Bauteil; Malkreuz ist ein
    christliches Ikonografie-Element ohne Holzbau-
    Bedeutung. „Diese Begriffe beruhen auf veralteten
    oder unzutreffenden Interpretationen" (Wikipedia).

  Eigene Festlegung: alle drei in `abgelehnte_benennungen:`,
  Creutzzug mit Begründung „historischer Begriff, heute
  veraltet"; Feuerbock und Malkreuz mit Begründung
  „fachlich falsch (Wikipedia-Klarstellung)".

  **(5) CH-Verbreitung.** Im CH-Riegelbau ist das
  Andreaskreuz belegt, aber **weniger prominent** als in
  DE-Fachwerk-Mitteldeutschland (Frankenwald), Sachsen
  (Vogtland) und Niedersachsen (Wikipedia/Fachwerkhaus,
  Wikipedia/Andreaskreuz (Fachwerk) — Beispiele Göttingen,
  Frankfurt, Weismain, Weimar). Anweiser als CH-Zimmermann
  kennt das Andreaskreuz als Begriff, hat es aber in
  der CH-Praxis seltener im Bestand. Die Welle-12-
  Modellierung führt das Andreaskreuz als allgemeine
  Bauteilgruppe; der CH-Schwerpunkt ist im
  Erläuterungs-Block und in der `funktion?`-Feld-
  Modellierung (dekorativ vs. statisch) abgedeckt.
  Lignum HBT 1 (2024)-Volltext wäre für die CH-Praxis-
  Verifikation hilfreich; aktuell snippet-basiert.
---

## Prosa-Definition

Ein **Andreaskreuz** ist eine Bauteilgruppe aus genau zwei
sich kreuzenden Streben in einer gemeinsamen Wandebene, die in
einem gemeinsamen Gefach zwischen denselben begrenzenden
Holzbauteilen (zwei Ständern und gegebenenfalls Schwelle,
Riegel oder Rähm) eingebaut sind und gemeinsam alle in der
Wandebene wirkenden horizontalen Lasten als wechselseitiges
Druck-Zug-Strebenpaar aufnehmen.

## Mathematische Definition

Sei

- W das Weltkoordinatensystem (siehe `weltkoordinatensystem`),
- 𝓑 die Menge aller Bauteile im Sinne von `bauteil`,
- 𝓢_Str ⊂ 𝓑 die Teilmenge mit Bauteilrolle `strebe`,
- 𝒫 die Menge der Ebenen im Sinne von `ebene`,
- 𝒰 der UUID-Raum nach `uuid`,
- 𝒢_huelle die Menge der zulässigen Hüllgeometrie-Repräsentationen
  einer Bauteilgruppe,
- e_z:= (0, 0, 1)ᵀ die vertikale Welt-Achse,
- ε_K:= Toleranzen.KOLLINEAR_EPS,
  ε_L:= Toleranzen.LAENGE_EPS,
  ε_W:= Toleranzen.WINKEL_EPS.

Dann ist ein **Andreaskreuz** ein Tupel

```
A:= (uuid, streben, wandebene, kreuzungspunkt,
      lage, huelle, funktion?, bezeichnung?)
```

mit

- **uuid** ∈ 𝒰: technischer Surrogatschlüssel des
  Andreaskreuzes (Pflicht, persistent, RFC 9562 v7).
- **streben** ⊂ 𝓢_Str, |streben| = 2: die genau zwei
  Streben des Kreuzes.
- **wandebene** ∈ 𝒫: die gemeinsame Wandebene mit
  Normalenvektor n_hat_W ∈ S² horizontal (|⟨n_hat_W, e_z⟩| ≤ ε_K).
- **kreuzungspunkt** ∈ ℝ³: der Schnittpunkt der beiden
  Streben-Bauteilachsen in der Wandebene; abgeleitete
  Grösse (siehe Bedingung 4).
- **lage** ∈ SE(3): die Starrkörpertransformation des
  lokalen Andreaskreuz-Koordinatensystems nach W.
- **huelle** ∈ 𝒢_huelle: die geometrische Hülle.
- **funktion?**: optionale Klassifikation (AUSSTEIFEND,
  DEKORATIV); siehe Quellenkonflikt-Block (2).
- **bezeichnung?**: optionaler Name (z. B. „Andreaskreuz
  Brüstungsfeld Süd").

und den Konsistenzbedingungen

1. **Bauteilgruppen-Konformität**: das Tupel
   (uuid, bestandteile = streben, lage, huelle, funktion?,
   bezeichnung?) erfüllt alle Konsistenzbedingungen 1–4 von
   `bauteilgruppe`. Insbesondere |bestandteile| = |streben| = 2
   ≥ 2.

2. **Beide Streben in der Wandebene**: Für beide s ∈ streben
   liegen beide Endpunkte der Bauteilachse a(s) in der
   Wandebene (Punkt-Ebene-Abstand der Endpunkte ≤ ε_L).

3. **Beide Streben echt diagonal in der Wandebene**: Für
   jede Strebe s ∈ streben ist der Winkel α(s) der
   Bauteilachse gegen die Lotachse e_z im Bereich
   ε_W < α(s) < π/2 − ε_W (weder lotrecht noch horizontal).
   Diese Bedingung erbt die Strebe-Definition
   (`hg_strebe.md` Bedingung 3).

4. **Streben kreuzen sich strikt im Inneren beider
   Bauteilachsen**: Bezeichne mit s₁, s₂ ∈ streben die zwei
   Streben mit a(s_i) = (p_a^{i}, p_e^{i}), und mit
   L_i:= {p_a^{i} + t · (p_e^{i} − p_a^{i}): t ∈ [0, 1]}
   die abgeschlossene Strecke (innere Punktmenge der
   Bauteilachse). Es existiert ein Punkt
   k = kreuzungspunkt ∈ ℝ³ mit
   ```
   k ∈ relative_interior(L_1) ∩ relative_interior(L_2),
   ```
   d. h. die zwei Strecken schneiden sich strikt im Inneren
   (nicht an einem ihrer Endpunkte). Der Kreuzungspunkt ist
   eindeutig, weil die zwei Strecken in derselben Ebene
   liegen (Bedingung 2) und nicht parallel sind (Bedingung 5).

5. **Streben nicht parallel** (X-Form, nicht II-Form): Die
   Richtungsvektoren d_hat_1, d_hat_2 der beiden Bauteilachsen
   erfüllen
   ```
   |⟨d_hat_1, d_hat_2⟩| ≤ 1 − ε_K,
   ```
   d. h. die zwei Streben sind echt nicht-parallel; der
   Kreuzungswinkel
   ```
   γ:= arccos(|⟨d_hat_1, d_hat_2⟩|) ∈ (ε_W, π/2]
   ```
   ist positiv. Default-Wert im Korpus γ ≈ π/2 (rechtwinkliges
   X), praktische Range 60°–90°.

6. **Beide Streben überspannen dasselbe Gefach**: Es
   existiert ein Gefach G_g (zwischen denselben begrenzenden
   Holzbauteilen — typisch zwei Ständer plus Schwelle/Rähm
   oder zwei Ständer plus zwei Riegel —), in dessen Berandung
   beide Strecken L_1, L_2 ihre Endpunkte haben:
   ```
   ∀ i ∈ {1, 2}: {p_a^{i}, p_e^{i}} ⊂ ∂G_g
   ```
   (bis auf Toleranz ε_L). Die Endpunkte liegen typisch
   diagonal gegenüber: p_a^{1} und p_e^{2} an einer
   Gefach-Ecke, p_e^{1} und p_a^{2} an der diagonal
   gegenüberliegenden. Forward-Verweis: der Gefach-Begriff
   ist Folgearbeit; bis dahin operationalisiert über die
   begrenzenden Bauteile (Ständer + Längsholz).

Die **geometrische Punktmenge** des Andreaskreuzes in W ist

```
G_W(A):= lage(G_lokal(huelle)) ⊂ ℝ³.
```

## Wohldefiniertheit

- **Existenz**: Für jedes Gefach mit zwei sich darin
  kreuzenden, in der gemeinsamen Wandebene liegenden
  Diagonal-Streben sind alle Bedingungen 1–6 erfüllbar.
- **Eindeutigkeit der Identität**: Bedingung 1 erbt die
  Aggregat-Wurzel-Auflösung von `bauteilgruppe`.
- **Eindeutigkeit des Kreuzungspunkts**: aus Bedingung 4
  (Schnitt im inneren der beiden Strecken) und Bedingung 5
  (Streben nicht parallel) folgt: in einer gemeinsamen
  Ebene mit nicht-parallelen Richtungen existiert genau ein
  Schnittpunkt; durch Inneres-Bedingung ist er eindeutig im
  inneren beider Strecken.
- **Trivial wohldefinierte Strebe-Menge**: streben ist als
  Menge unsortiert (zwei Streben unbenannt); alle Aussagen
  sind invariant unter Tausch der beiden Streben.
- **Unabhängigkeit von der Wahl des lokalen
  Koordinatensystems**: trivial; siehe `bauteilgruppe`.
- **Konsistenz mit `bauteilgruppe`**: alle vier
  Bauteilgruppen-Bedingungen gelten; die Andreaskreuz-
  Bedingungen 2–6 treten additiv hinzu.
- **Konsistenz mit `strebe`**: jede Strebe s ∈ streben
  trägt die in `hg_strebe.md` definierten Constraints
  (Bauteilachse, Diagonal-Lage in Wandebene, Anker-
  Bedingungen). Das Andreaskreuz fügt die wechselseitige
  Kreuzungs-Bedingung hinzu.
- **Nicht-Zirkularität**: die Definition verwendet
  `bauteilgruppe`, `bauteil`, `strebe`, `ebene`, `strecke`,
  `polyeder`, `uuid`, `lokales_koordinatensystem`,
  `weltkoordinatensystem`, `toleranzen` — alle bereits
  definiert. `gefach` ist Forward-Verweis (Folgearbeit-
  Trigger); die Definition operationalisiert die Gefach-
  Bedingung über die Endpunkte der Streben und die
  begrenzenden Bauteile, ohne den `gefach`-Eintrag
  vorauszusetzen.
- **Eliminierbarkeit**: Jede Verwendung von „Andreaskreuz"
  in der App lässt sich durch das obige Tupel mit den
  sechs Konsistenzbedingungen ersetzen.

## Erläuterung (nicht normativ)

Das Andreaskreuz ist die ontologische Antwort auf die
**X-förmige Diagonalverstrebung** im Fachwerk- und Riegelbau:
zwei in einem Gefach diagonal gegenüberliegende Ecken durch
zwei sich kreuzende Streben verbindende Bauteilgruppe.

### Geometrische Erscheinung

Die zwei Streben sind in der Regel **echt durchlaufende
Bauteile** (vom unteren zum oberen Gefach-Eck) und kreuzen
sich frei im Inneren des Gefachs — sie sind **nicht** „zwei
halbe Streben mit Schwert in der Mitte". Diese Geometrie-
Setzung ist im Korpus belegt (Wikipedia/Andreaskreuz
(Fachwerk)). Der Kreuzungspunkt der zwei Bauteilachsen ist
typisch im geometrischen Zentrum des Gefachs (bei
symmetrischer X-Form), aber nicht zwingend (asymmetrische
Andreaskreuze, etwa bei Brüstungsfeldern mit ungleichmässiger
Ausfachung, sind belegt).

Die Verbindung der zwei Streben am Kreuzungspunkt erfolgt
typisch durch:

- **Blattung** (Halb-Holz-Überschnitt): jede Strebe wird auf
  halbe Stärke abgeflacht, die zwei Flächen ineinander
  gelegt; oft mit Holznagel gesichert.
- **Holznagel-Verbindung**: bei vollem Querschnitt der
  Streben werden sie am Kreuzungspunkt mit einem Holznagel
  (oder Bolzen) verbunden.
- **Einfacher Überschnitt** (ohne Blattung): die zwei
  Streben kreuzen sich räumlich (eine vor der anderen) und
  sind nur an den Endpunkten gegen die Rahmenhölzer
  angeschlossen. Strukturell schwächer.

### Statische Funktion

Die X-förmige Aussteifung leistet eine vollständige
Aufnahme aller in der Wandebene wirkenden horizontalen
Lasten (Wikipedia/Andreaskreuz (Fachwerk): „erlaubt es,
alle horizontalen Kräfte in der Ebene des Elements
aufzunehmen"). Bei wechselnder Windrichtung wirkt jeweils
**eine** Strebe als Druck-Diagonale (knickfest, weil sie
am Kreuzungspunkt eine Zwischenlagerung erhält), die
andere als Zug-Diagonale (zugfest, kann ohne Knick-Sorge
auf Zug arbeiten). Das Andreaskreuz ist damit die
aussteifungs-effizienteste **Bauteilgruppen-Konfiguration**
im Gefach und kompensiert die Schwäche der reinen
Einzel-Strebe (die nur in einer Druck-Richtung wirkt).

### Dekorative Funktion

In der mitteldeutschen, sächsischen und niedersächsischen
Schmuck-Fachwerkbau-Tradition wird das Andreaskreuz auch
als reines **Ornament** ohne statische Wirkung eingesetzt:
an Brüstungsfeldern unterhalb von Fenstern, an Giebeln, an
dekorativen Ausfachungen. In dieser Lesart sind die
Strebe-Stäbe oft schwächer dimensioniert (weniger
tragfähig) und die Anschlüsse einfacher; die Funktion ist
visuell, nicht statisch.

Die App-Modellierung trennt die zwei Funktionen über das
optionale `funktion?`-Feld (Werte AUSSTEIFEND, DEKORATIV).
Beide tragen denselben strukturellen Aufbau (zwei sich
kreuzende Streben), unterscheiden sich nur in der
funktionalen Klassifikation.

### Historische Verortung

Die frühesten Belege im DACH-Fachwerkbau sind nach
Wikipedia/Andreaskreuz (Fachwerk) **1452** und **1457**.
Im 19. Jahrhundert wurde das Andreaskreuz teils in voller
Geschosshöhe ausgeführt (mehrere Gefache überspannend),
was im Default-Glossar-Modell die Sub-Lesart
„geschossübergreifend" (Quellenkonflikt-Block (1))
darstellt. Regionale Schwerpunkte: Frankenwald,
Vogtland, Niedersachsen, Mittelhessen.

### CH/DE-Asymmetrie

Im **CH-Riegelbau** ist das Andreaskreuz belegt, aber
weniger prominent als in DE-Fachwerk. Wikipedia/Fachwerkhaus
(CH-Sektion) erwähnt „rote Balken und weisse Ausfachung"
als CH-Riegelhaus-Charakteristikum, aber keine spezifische
Andreaskreuz-Verbreitung. Im Erläuterungs-Block dieses
Eintrags wird der DE-Schwerpunkt thematisiert; Anweiser als
CH-Zimmermann kennt den Begriff als Bestandteil des
Holzbau-Fachvokabulars, hat ihn aber in der CH-Praxis
seltener im Bestand.

### Abgrenzung zur Mann-Figur

Beide sind Wand-Aussteifungs-Aggregate; die Trennlinie ist
geometrisch:

- **Andreaskreuz**: zwei sich kreuzende Streben im
  **Gefach** (Wandfeld zwischen zwei Ständern und ggf.
  Schwelle/Rähm/Riegel). Die Anker-Punkte liegen an den
  Gefach-Ecken (Schnittpunkte der Rahmenhölzer).
- **Mann-Figur** (`mann`): Bündel-Aussteifung am
  **Pfosten** (Ständer-Achse). Die Bauteile (Kopfband,
  Fussband, optional Strebe) sind alle an einem
  gemeinsamen Pfosten als zentraler Achse verankert.

Die Abgrenzung ist als
„geometrisch sauber getrennt" formuliert: Andreaskreuz am
Gefach, Mann am Pfosten. Keine geometrische Überlappung,
auch wenn beide Aggregate in derselben Wand vorkommen
können (in DE-Schmuckfachwerk z. B. ein Mann am Eckständer
plus ein Andreaskreuz im Brüstungsfeld).

### Andere Bedeutungen / Englisch

- **`St. Andrew's Cross`**: englischer Standard-Anglizismus;
  als Synonym im Heraldik-/Flaggen-Korpus (X-förmiges
  Kreuz auf Schottland-Flagge); im Holzbau-Korpus als
  abgelehnter Anglizismus geführt.
- **`X-bracing`** / **`cross bracing`** / **`saltire brace`**:
  generische Anglizismen aus dem US-Holzbau-Korpus;
  abgelehnt.

## Beziehungen

- **Oberbegriff**: `bauteilgruppe`. Das Andreaskreuz erfüllt
  alle Bauteilgruppen-Merkmale (exklusive Mitgliedschaft,
  kaskadische Lebenszyklus-Bindung, eigene Hülle, eigene
  Identität, konstruktive Funktionseinheit) und fügt
  andreaskreuz-spezifische Merkmale hinzu: genau zwei
  Streben als Pflicht-Bestandteile, ihre wechselseitige
  Kreuzungsbedingung in einer gemeinsamen Wandebene.
- **Bestandteile (partitiv)**:
  - **Strebe** (`strebe`, genau 2 Stück): die zwei sich
    kreuzenden Diagonal-Stab-Bauteile.
- **Geometrische Bezugsobjekte (nicht Mitglieder)**:
  - **Wandebene** (`ebene`): die gemeinsame lotrechte
    Trägerebene beider Streben.
  - **Kreuzungspunkt** (Punkt ∈ ℝ³): der Schnittpunkt
    der zwei Bauteilachsen; abgeleitete Grösse.
  - **Gefach** (`gefach`, Forward-Verweis, Folgearbeit):
    das umschliessende Wandfeld; geometrische Referenz,
    nicht Bestandteil.
  - **Begrenzende Bauteile**: zwei Ständer plus Schwelle/
    Rähm oder Riegel; geometrische Referenz für die
    Anker-Endpunkte der Streben, nicht Mitglieder des
    Andreaskreuz-Aggregats.
- **Funktionale Sicht (über `funktion?`-Feld)**:
  - **AUSSTEIFEND**: tragwerks-aussteifende Konfiguration.
  - **DEKORATIV**: rein ornamentale Konfiguration ohne
    statische Wirkung.
- **Verwendung**:
  - Bestandteil einer **Wand** (`wand`) — als
    geschwisterliches Aggregat innerhalb derselben
    Wandebene; die Wand-Bauteilgruppe enthält die zwei
    Streben **nicht** zusätzlich, weil exklusive
    Mitgliedschaft gilt (siehe `hg_wand.md` Erläuterungs-
    Block).
- **Abgrenzung**:
  - **Bauteilgruppe** (`bauteilgruppe`): Oberbegriff.
  - **Strebe** (`strebe`): Bauteilrolle der zwei
    Mitglieder; eine Einzel-Strebe ist nicht ein
    Andreaskreuz.
  - **Kopfband** (`kopfband`), **Fussband** (`fussband`):
    diagonale Aussteifungs-Bauteile mit Pfosten-Kopf-
    bzw. Pfosten-Fuss-Anker; **nicht** Bestandteile des
    Andreaskreuzes (das Andreaskreuz verwendet
    ausschliesslich Streben, nicht Bänder).
  - **Knagge** (`knagge`): Konsole; keine Diagonal-Stab-
    Bauteile, nicht Bestandteil.
  - **Mann** (`mann`): geschwisterliches Bündel-
    Aussteifungs-Aggregat am Pfosten (nicht am Gefach);
    siehe Erläuterungs-Block.
  - **Wand** (`wand`): das übergeordnete Wand-Aggregat,
    in dessen Wandebene das Andreaskreuz liegt; die
    Wand enthält das Andreaskreuz als geschwisterliches
    Aggregat oder als verschachteltes Aggregat (Modell-
    Entscheidung).
  - **Schwelle**, **Rähm**, **Ständer**, **Riegel**:
    Bauteilrollen, die das umschliessende Gefach bilden;
    Anker-Bauteile für die Streben, nicht Bestandteile
    des Andreaskreuzes.
  - **Verbindung** (`verbindung`): das Andreaskreuz
    enthält Verbindungen zwischen seinen Bestandteilen
    (Strebe-Strebe-Blattung am Kreuzungspunkt, Strebe-
    Rahmen-Anker an den vier Eckpunkten); es ist selbst
    keine Verbindung.
  - **Gefach** (`gefach`, Forward-Verweis): das
    umschliessende Wand-Feld; geometrische Referenz,
    nicht Aggregat-Mitglied.
  - **Fachwerk**, **Riegelbau**: Bauweisen-
    Klassifikationen, in denen das Andreaskreuz primär
    auftritt.
  - **Brueckmauer** / **Brueckschnurmauer** (Folgearbeit-
    Trigger im historischen Korpus): regionale
    Sub-Lesarten von Fachwerk-Brüstungsfeldern.
  - **Walm** (`walm`), **Binder** (`binder`):
    strukturparallele Geschwister-Aggregate unter
    `bauteilgruppe`, mit anderer geometrischer
    Konfiguration.

## Quellen

**Primär (normativ):**

- DIN EN 1995-1-1:2010-12, „Eurocode 5: Bemessung und Konstruktion
  von Holzbauten — Teil 1-1", Abschnitt 9.
- DIN 1052:2008-12, „Entwurf, Berechnung und Bemessung von
  Holzbauwerken", Abschnitte 8 und 12.
- SIA 265:2021, „Holzbau", Schweizerischer Ingenieur- und
  Architektenverein, §1.1 Fachausdrücke / Anhang G (Volltext
  direkt eingesehen, 2026-06-14): „Andreaskreuz" ist **nicht** als
  Fachausdruck oder Lemma geführt; aussteifende Diagonalverbände
  werden generisch unter §5.8 behandelt (Negativ-Befund).
- Thesaurus Traditioneller Holzbau (TTH), RWTH Aachen,
  Hierarchie-Facette 1922 „Fachwerk-Bauteile".

**Sekundär:**

- Wikipedia, Lemma „Andreaskreuz (Fachwerk)", de.wikipedia.org/
  wiki/Andreaskreuz_(Fachwerk) (abgerufen 2026-05-16).
- Wikipedia, Lemma „Fachwerkhaus" (abgerufen 2026-05-16).
- Gerner, M.: *Fachwerk – Instandsetzung, Sanierung, Neubau.*
  DVA, 7. Aufl. 2007.
- Mönck, W.; Rug, W.: *Holzbau – Bemessung und Konstruktion.*
  16. Aufl., Beuth, Berlin 2015.
- Natterer, J.; Herzog, T.; Volz, M.: *Holzbau-Atlas.*
  4. Aufl., Birkhäuser, Basel 2003.
- Großmann, R.: *Konstruktionen des deutschen Fachwerkbaus.*
  1987.
- BauNetz Wissen, Glossar-Holz, Lemma „Andreaskreuz".
- Lignum (Hrsg.): *Holzbautabellen HBT 1 (2024).* Lignum, Zürich.

**Korpus (nicht autoritativ):**

- Recherche-Bericht:
  [intern].
- Recherche-Bericht (Vorgänger):
  [intern] (Welle 10).
