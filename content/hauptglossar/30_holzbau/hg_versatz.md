---
id: versatz
benennung: Versatz
synonyme: [Versatz-Verbindung, Stirnversatz, Fersenversatz, Rückversatz, Brustversatz, "doppelter Versatz", "Stirn-Fersen-Versatz", "single step joint", "double step joint"]
abgelehnte_benennungen: ["birdsmouth", "birdsmouth joint", "bird's mouth", "heel cut", "seat cut", "plumb cut", "step-lapped rafter seat", "rafter notch", "notch", "mortise", "tenon", Versetzung, Stirnschnitt, Schwalbenschwanzversatz]
oberbegriff: bearbeitung
begriffstyp: partitiv
voraussetzungen: [bearbeitung, bauteil, uuid, lokales_koordinatensystem, polyeder, bauteilachse, lotebene, toleranzen]
abgrenzung_zu: [kerve, bearbeitung, zapfen, zapfenloch, blatt, kamm, verbindung, anschnitt, schlitz, bohrung, sparren, fusspfette, querschnitt]
status: entwurf
subglossar_pendant: notwendig
quellen_primär:
  - "DIN EN 1995-1-1/NA:2013-08, Nationaler Anhang Deutschland zum Eurocode 5, NCI NA.12 'Zimmermannsmäßige Verbindungen': Regelinhalte zum Versatz (Versatztiefe in Abhängigkeit vom Strebenanschlusswinkel, Mindest-Vorholzlänge, Anschnittwinkel, Lagesicherung gegen Abheben). Bibliographisch und über mehrere unabhängige Sekundärbeschreibungen bestätigt; Volltext-Verifikation der Regelwerte aus dieser Recherche nicht möglich (DIN-Media-Paywall), siehe quellenkonflikt-Block."
  - "DIN EN 1995-1-1:2010-12 (Eurocode 5), Abschnitt 5.2 (Berücksichtigung von Querschnittsschwächungen) und Abschnitt 6.5 (Querzug- und Schubnachweise an ausgeklinkten Bauteilen): analoge Anwendung auf den Versatz; Vorholzlänge als Schub-Trag-Länge, Versatztiefe als Höhe der Ausklinkung."
  - "DIN EN 1995-1-1:2010-12, Abschnitt 6.1.5 'Druck unter einem Winkel zur Faser' (Hankinson): Druckspannungsnachweis in der Versatz-Anschnittfläche, ausgewertet am druckstabseitigen und am trägerbauteilseitigen Hankinson-Winkel."
  - "SIA 265:2021 'Holzbau', Schweizerischer Ingenieur- und Architektenverein, zimmermannsmäßige Verbindungen. Eine konkrete Annex-Stelle für den Versatz ist im Bestand-Eintrag `hg_verbindung.md` mit 'Anhang A' referenziert, durch diese Recherche aber nicht volltext-verifiziert; siehe quellenkonflikt-Block."
  - "DIN 1052:2008-12 (zurückgezogen, ersetzt durch DIN EN 1995-1-1 + NA): führte Versatz unter zimmermannsmäßiger Verbindung gemeinsam mit Verblattung, Verzapfung, Verkämmung; historische Etablierung des Begriffs."
quellen_sekundär:
  - "Colling, F.: Holzbau – Grundlagen, Bemessungshilfen. Springer Vieweg, Wiesbaden 2004 (1. Aufl.), Kap. 8.5 'Versätze'. Autoritative geometrische Definition der drei Versatzformen: Stirnversatz = Winkelhalbierende (Beanspruchungswinkel α_S = α_D = γ/2, Bild 8.14); **Fersenversatz/Rückversatz = Druckfläche rechtwinklig zur Strebe** (α_S = γ, α_D = 0, Beiwert k_V,γ, Bild 8.15); rechtwinkliger Versatz = lotrecht zum Gurt (α_S = 0, α_D = γ); doppelter Versatz = Stirn + Ferse (Bild 8.16, Tab. 8.4). Maßgebliche Quelle für die Benennung der ⊥-Strebe-Geometrie als Fersenversatz (s. quellenkonflikt Konflikt 6)."
  - "Mönck, W.; Rug, W.: Holzbau – Bemessung und Konstruktion. 16. Aufl., Beuth, Berlin 2015, Kap. 7 'Verbindungen', §§ Stirnversatz, Fersenversatz, doppelter Versatz."
  - "Peter, M.; Scheer, C. (Hrsg.): Holzbau-Taschenbuch. Wiley-VCH, Berlin 2015, Kap. 19 'Einfacher Versatz' und Kap. 20 'Doppelter Versatz'."
  - "Gerner, M.: Fachwerk – Instandsetzung, Sanierung, Neubau. DVA, 7. Aufl. 2007, Glossar 'Versatz'."
  - "Natterer, J.; Herzog, T.; Volz, M.: Holzbau-Atlas. 4. Aufl., Birkhäuser, Basel 2003, Kap. 'Zimmermannsmäßige Verbindungen'."
  - "Blass, H. J.; Sandhaas, C.: Timber Engineering – Principles for Design. KIT Scientific Publishing, Karlsruhe 2017, Kap. 'Carpentry Joints' (engl. Pendant 'single/double step joint')."
  - "Branco, J. M.; Descamps, T.: Analysis and strengthening of carpentry joints — Single step joint: overview. academia.edu (Korpus-Quelle für engl. Pendant)."
  - "design2machine: 'BTLx interface description', Version 2.1, 16.11.2023, Abschnitt 'StepJoint' und 'StepJointNotch' (Processings-Liste S. 8 ff.); Parameter-Schemata aus dieser Recherche nicht volltext-eingesehen."
  - "baunetzwissen.de: 'Zimmermannsmäßige Verbindungen' (abgerufen 2026-05-14), mit Sekundärzitat zu DIN EN 1995-1-1/NA NCI NA.12."
  - "Recherche-Bericht [intern] (Quellen-Lage und Auflösung der drei Subtypen)."
quellenkonflikt: |
  Es gibt **keine** im Volltext zugängliche normative Definition
  des Versatzes mit geschlossener geometrischer Charakterisierung;
  alle konsultierten Normen (DIN EN 1995-1-1 Hauptteil, SIA 265,
  DIN 1052 historisch) setzen den Begriff voraus und behandeln nur
  seine Bemessungsfolgen. Die geometrische Charakterisierung wird
  hier aus dem Lehrbuch- und Sekundärquellen-Konsens
  (Mönck/Rug Kap. 7, Holzbau-Taschenbuch Kap. 19/20,
  Natterer/Herzog, Gerner, baunetzwissen.de) rekonstruiert und
  durch die Recherche [intern]
  belegt.

  **Konflikt 1 — Normative Verankerung NCI NA.12 (DE) vs. SIA 265 Annex A (CH):**

  Der deutsche Nationale Anhang DIN EN 1995-1-1/NA:2013-08 trägt
  ausdrücklich einen Abschnitt NCI NA.12 „Zimmermannsmäßige
  Verbindungen", der den Versatz regelt; Existenz und fachlicher
  Umgriff sind durch mehrere unabhängige Sekundärquellen
  (Mönck/Rug, baunetzwissen.de, harzerstatik.de, statikweb.iivs.de)
  bestätigt. Der Volltext der NA.12-Regelinhalte (Versatztiefen-
  Begrenzung, Mindest-Vorholzlänge) ist über die zugänglichen
  Suchergebnisse **nicht im Volltext** verifizierbar (DIN-Media-
  Paywall).

  Die schweizerische SIA 265:2021 behandelt zimmermannsmäßige
  Verbindungen deutlich knapper. Der Bestand-Eintrag
  `hg_verbindung.md` (Zeilen 17, 194, 526) referenziert
  „SIA 265 Anhang A 'Verbindungen und Verbindungsmittel'"; diese
  Annex-Bezeichnung ist im Bestand gesetzt, aber durch die hiesige
  Recherche **nicht unabhängig volltext-verifiziert**.

  **Eigene Festlegung:**

  - Die deutsche NCI NA.12 wird als **schärfste verfügbare
    normative Quelle** für die Versatz-Bemessungsregeln geführt
    (Tier Hoch, indirekt belegt). Die in der Literatur durchgängig
    zitierten Regelwerte (`t_v ≤ h/4` bei flachem Strebenanschluss-
    winkel α ≤ 50°, `t_v ≤ h/6` bei steilem α ≥ 60°, lineare
    Interpolation dazwischen; `l_v ≥ 8·t_v` und `l_v ≥ 200 mm`)
    werden als App-Plausibilitätsregeln eingesetzt.
  - Die SIA-265-Annex-Bezeichnung wird vorläufig als „Anhang A"
    übernommen, konsistent mit `hg_verbindung.md`. Bei der nächsten
    Bearbeitung von `hg_verbindung.md` wird die Annex-Referenz
    gegen den SIA-265-Volltext verifiziert (Trigger B in der
    Recherche-Datei, siehe quellen_sekundär).

  **Konflikt 2 — Drei Subtypen vs. einheitliche Bemessungs-Klasse:**

  Stirnversatz, Fersenversatz und doppelter Versatz sind in der
  Lehrbuch- und Praxisliteratur trennscharf etabliert, **aber**:
  keine der konsultierten Normen (EC 5 Hauptteil, EC 5 NA NCI
  NA.12, SIA 265, DIN 1052 historisch) führt die drei
  Hauptausprägungen als eigene Bemessungs-Klassen mit getrennten
  Formeln. Sie unterscheiden sich in der **Geometrie** (Anzahl
  und Lage der Anschnittflächen), nicht in der **Bemessungs-
  Klasse**.

  **Eigene Festlegung:**

  - Die drei Hauptausprägungen werden im Glossar als kanonische
    Subtypen geführt und im Erläuterungsblock charakterisiert.
  - Im Datenmodell sind sie eine **Konfigurations-Achse**
    (`art: VersatzArt ∈ {STIRN, FERSE, DOPPELT}`), **keine
    sealed-Hierarchie** unter `Versatz`. Begründung: alle drei
    Varianten teilen die parametrische Definition, die Wirkung
    auf das Trägerbauteil und die Bemessungs-Klasse; der
    Unterschied liegt allein in der Anzahl und Lage der
    Anschnittflächen, die als gemeinsames Parametertupel
    repräsentierbar sind.

  **Konflikt 3 — „Verkämmter Versatz":**

  Die WebSearch-Recherche nach der exakten Phrase
  `"verkämmter Versatz"` hat **null Treffer** geliefert. Der
  Begriff ist im DACH-Holzbau-Korpus nicht als eigenständige
  Verbindungs-Klasse etabliert. Mögliche Lesarten (Schreibvariante
  für doppelten Versatz, Hybridform Versatz + Kamm, Tippfehler)
  führen alle auf bereits bestehende Begriffe zurück.

  **Eigene Festlegung:** Verkämmter Versatz wird **nicht** als
  eigenständiger Subtyp aufgenommen. Sollte später eine
  belastbare Quelle auftauchen, wird der Eintrag revidiert.

  **Konflikt 4 — Englische Falsche Freunde:**

  `birdsmouth`, `heel cut`, `seat cut`, `plumb cut` und
  `step-lapped rafter seat` werden in englischer Holzbau-Literatur
  (Wikipedia *Birdsmouth joint*, Carolina Timberworks Glossary,
  jointandpeg.com, timberframehq.com) **konsequent für die Kerve**
  bzw. Teilflächen innerhalb der Kerve verwendet, nicht für den
  Versatz. Die korrekten englischen Pendants zum Versatz sind
  `single step joint` und `double step joint` (Branco/Descamps,
  Blass/Sandhaas 2017, BTLx 2.1 `StepJoint`).

  **Eigene Festlegung:** Alle aufgeführten englischen Birdsmouth-
  Termini sind in `abgelehnte_benennungen` geführt; `single step
  joint` und `double step joint` werden als fachsprachliche
  englische Synonyme aufgenommen.

  **Konflikt 5 — Nur die Druckfläche ist geometrisch normiert:**

  Eine Recherche über neun Fachquellen (2026-06-02 + Colling-Nachtrag:
  **Colling §8.5 Bild 8.14/8.15 als autoritative Winkel-Quelle**; FRILO HO2+
  Berechnungsgrundlagen mit Schnittfiguren; Berner Fachhochschule
  „Historische Holzverbindungen" 2016 mit 3D-Renderings, SIA 265;
  D.I.E. Statik; bubiza-Wiki; zimmerer-treff; baubeaver; sowie die
  akademische step-joint-Literatur Branco/Descamps) ergab: **nur die
  Druckfläche** des Versatz-Ausschnitts ist konventionell festgelegt
  (Stirn = Winkelhalbierende δ_S = β/2, Beanspruchungswinkel γ/2; Ferse =
  rechtwinklig zur Strebe δ_F = β − π/2, Beanspruchungswinkel α_S = γ in der
  Schwelle — Colling Bild 8.15). Die **zweite Schnittfläche (Sohle)** ist in **keiner**
  Quelle mit einem Winkel definiert; die Ingenieur-Modelle
  idealisieren nur die **Scherfuge** als waagrechte Analyse-Ebene im
  Vorholz (Bruchebene des Schubnachweises), nicht als realen Schnitt.
  Branco/Descamps wörtlich: „no European standards detail how to
  design this connection … at the joint contact surfaces."

  **Eigene Festlegung:** Die Druckflächenwinkel sind **durch β
  bestimmt** (Stirn `δ_S = β/2`, Ferse `δ_F = β − π/2`) — nach
  EN 1995-1-1 „nicht frei wählbar" — und daher **abgeleitete Größen,
  kein Tupel-Feld** (Recherche-Bericht
  [intern]). Frei ist
  allein der **Stirn-Sohlenwinkel σ_S** (handwerkliche Freimachungs-
  Fläche), nur zur Wohlgeformtheit des V auf (0, π/2) beschränkt. Die
  Fersen-Sohle ist konstruktiv ∥ Strebe (`σ = π − β`, 90°-L). Belegt
  durch Recherche-Bericht 2026-06-02 und Anweiser-f3d-Review der drei Arten. Doppelt-Tiefen-Konvention (BFH/SIA):
  Stirn 1/6·h, Ferse 1/4·h; Ferse ≥ 1 cm (DIN) bzw. ≥ 1,5 cm
  (ÖNORM B 1995) tiefer als Stirn.

  **Konflikt 6 — „Fersenversatz" (⊥ Strebe) vs. „Brustversatz" (Synonym):**

  Die ⊥-Strebe-Geometrie (Druckfläche rechtwinklig zur Strebe,
  δ_F = β − π/2) heißt im **autoritativen Lehrbuch** (Colling, „Holzbau –
  Grundlagen", §8.5, Bild 8.15 „Fersen-/Rückversatz": Beanspruchungswinkel
  α_S = γ in der Schwelle, α_D = 0 in der Strebe, Bemessungs-Beiwert k_V,γ)
  der **Fersenversatz**. Ebenso bei **BTLx 2.1 / COMPAS Timber**
  (`StepJointNotch HEEL` — HEEL = Ferse, das Golden-Orakel dieses Eintrags)
  und bei FRILO. Ein Teil des Web-Korpus (de-academic, baubeaver, pcae)
  nennt dieselbe ⊥-Strebe-Geometrie **Brustversatz** und führt
  „Fersenversatz" als separate, weiter zurückversetzte Variante mit
  größerer Vorholzlänge.

  **Eigene Festlegung:** Maßgeblich ist Colling (autoritatives Lehrbuch)
  zusammen mit BTLx/COMPAS (unser Validierungs-Orakel): die ⊥-Strebe-Art
  heißt `FERSE` (Fersenversatz). **Brustversatz** ist als **Synonym** für
  dieselbe Geometrie geführt (Frontmatter). Der „zurückversetzte" Charakter
  (Strebennase ragt vor, größere Vorholzlänge) ist eine **Positions-Variante**
  über x_0/l_v, **kein** eigener Schnitt — Colling modelliert beide unter
  demselben ⊥-Strebe-Fersenversatz. (Recherche
  [intern], Colling-Addendum.
  Diese Festlegung **revidiert** eine zwischenzeitliche Umbenennung
  FERSE→BRUST, die nur den Web-Korpus konsultiert hatte.)

  Diese Festlegung ist konsistent mit allen konsultierten Quellen.
---

## Prosa-Definition

Ein **Versatz** ist eine subtraktive Bearbeitung an einem
Stab-Bauteil (dem Trägerbauteil, typischerweise einer Schwelle,
einem Rähm, einem Bundbalken oder einer Fußpfette), die eine
**keilförmige Ausnehmung** mit einer oder zwei ebenen, gegen die
Bauteilachse des Trägerbauteils geneigten Anschnittflächen
erzeugt, in die das druckbeanspruchte Anschlussbauteil (der
Druckstab, typischerweise eine Strebe, ein Kopfband oder ein
Sparren) mit seiner ebenen Stirnfläche oder mit zwei Stirnflächen
formschlüssig einsetzt, sodass eine Druckkraft längs der
Druckstab-Achse über die geneigten Druckkontaktflächen unter
einem Winkel zur Faser des Trägerbauteils übertragen wird.

## Mathematische Definition

Sei

- B ein Stab-Bauteil im Sinne von `bauteil` (das **Trägerbauteil**)
  mit Stabgeometrie (`geometrie ∈ 𝒢_stab`),
- L_B = (O_B, e_hat_x^B, e_hat_y^B, e_hat_z^B) das Bauteil-Lokal-
  Koordinatensystem (`lokales_koordinatensystem`) mit Konvention
  ```
  e_hat_x^B  =  Bauteilachse (Längsrichtung),
  e_hat_y^B  =  Bauteil-Querrichtung,
  e_hat_z^B  =  Bauteilhöhe (auf der Druckstab-Seite nach oben),
  ```
- h_B > 0 die Bauteilhöhe in lokaler z-Richtung (mm),
- b_B > 0 die Bauteilbreite in lokaler y-Richtung (mm),
- ℓ_B > 0 die Bauteillänge in lokaler x-Richtung (mm),
- d_hat_S ∈ ℝ³ der Einheits-Richtungsvektor der **Druckstab-Achse**
  (`bauteilachse` des druckbeanspruchten Anschlussbauteils),
  bezogen auf das Bauteil-Lokal-System L_B,
- β ∈ (0, π) der **Strebenanschlusswinkel** zwischen der
  Druckstab-Achse d_hat_S und der Trägerbauteil-Achse e_hat_x^B,
  gemessen als stumpfer Außenwinkel:
  ```
  β:=  π − arccos(|⟨d_hat_S, e_hat_x^B⟩|),
  ```
  d. h. β ∈ (π/2, π) bezeichnet die Öffnung zwischen Druckstab
  und Trägerbauteil auf der Druckstab-Seite,
- ε_L:= Toleranzen.LAENGE_EPS,
- ε_W:= Toleranzen.WINKEL_EPS.

Der **Anschnitt der Anschnittfläche** wird in der Lotebene
Π_⊥(B) des Trägerbauteils (`lotebene`: welt-vertikale Ebene
durch die Bauteilachse, die im allgemeinen Fall auch e_hat_y^B
enthält, sofern das Trägerbauteil horizontal eingebaut ist)
geführt. Im Folgenden wird das Trägerbauteil als horizontal
liegend angenommen (Standardfall: Schwelle, Rähm, Bundbalken,
Fußpfette); die Verallgemeinerung auf geneigte Trägerbauteile
ist trivial durch Anwendung der `lokalePlatzierung`.

### Konfigurations-Achse `art`

Der Versatz trägt eine diskrete **Art-Klassifikation**

```
art  ∈  𝒜:=  { STIRN, FERSE, DOPPELT }                          (1)
```

mit der Bedeutung

- **STIRN** (Stirnversatz, einfacher Versatz): genau eine
  geneigte Anschnittfläche, deren Tiefe zur Druckstab-Vorderseite
  hin am größten ist;
- **FERSE** (Fersenversatz, hinterer Versatz): genau eine
  geneigte Anschnittfläche, deren Tiefe zur Druckstab-
  Innenseite (Ferse) hin am größten ist;
- **DOPPELT** (doppelter Versatz, Stirn-Fersen-Versatz):
  zwei geneigte Anschnittflächen, eine vorne (Stirn) und eine
  hinten (Ferse).

### Parameter

Die **Parameter** eines Versatzes sind das Tupel

```
p_Versatz:=  (x_0, art, β, t_S?, σ_S?, t_F?, b_K?, l_v)              (2)
```

mit

- **x_0** ∈ ℝ: **Position** entlang der Trägerbauteil-Achse, in
  mm (Bauteil-Lokal-Koordinate). Bezugspunkt ist der **Stirn-
  Aufsetzpunkt** Q ∈ ℝ³ — der Schnittpunkt der Druckstab-Achse
  mit der Trägerbauteil-Oberseite (z = h_B im Lokalsystem); in
  Bauteil-Lokal-Koordinaten hat Q die Lage (x_0, 0, h_B).
- **art** ∈ 𝒜: Konfigurations-Achse nach (1).
- **β** ∈ (π/2, π): Strebenanschlusswinkel (rad), strukturell
  durch die Druckstab-Achse vorgegeben (kein freier Geometrie-
  Parameter im engeren Sinne, aber Pflichtfeld des Tupels, weil
  er die Anschnittwinkel bestimmt).
- **t_S** ∈ ℝ⁺ ∪ {⊥}: **Versatztiefe Stirn** (mm); Pflicht für
  art ∈ {STIRN, DOPPELT}, ⊥ für art = FERSE.
- **σ_S** ∈ (0, π/2) ∪ {⊥}: **Sohlenwinkel Stirn** (rad) der **zweiten**
  Stirn-Schnittfläche (Sohle, kein Hauptdruck) zur Faser. Der Ausschnitt-
  Apex-Innenwinkel ist `180° − δ_S − σ_S`; flach (σ_S < π/2 − δ_S) ⇒ stumpf.
  **Nicht normiert** — reine handwerkliche Freimachungs-Fläche (s.
  quellenkonflikt Konflikt 5). Pflicht für art ∈ {STIRN, DOPPELT}, ⊥ für
  art = FERSE.
- **t_F** ∈ ℝ⁺ ∪ {⊥}: **Versatztiefe Ferse** (mm); Pflicht für
  art ∈ {FERSE, DOPPELT}, ⊥ für art = STIRN.
- **b_K** ∈ ℝ⁺ ∪ {⊥}: **Versatzkamm-Breite** (mm) — Bemessungs-Kenngröße
  (Mindest-Steg zwischen den Scherfugen, EC5-Schubnachweis). **Ohne
  Geometrie-Wirkung** im Werkzeugkörper: der Versatzkamm ist eine **Spitze
  auf der Oberkante** (z = h_B), kein Plateau (s. Werkzeugkörper DOPPELT).
  Pflicht **nur** für art = DOPPELT, ⊥ sonst.
- **l_v** ∈ ℝ⁺: **Vorholzlänge** (mm), Abstand von der vordersten
  Versatz-Stirnkante (am Stirn-Aufsetzpunkt Q für art ∈ {STIRN,
  DOPPELT}, bzw. an der Fersen-Ausstiegskante für art = FERSE)
  bis zum Trägerbauteil-Ende.

**Abgeleitete Anschnittwinkel (durch β bestimmt, kein Tupel-Feld).** Die
Druckflächen-Winkel sind nach DACH-Konsens und EN 1995-1-1 **nicht frei**,
sondern durch den Strebenanschlusswinkel β festgelegt (Recherche-Bericht
[intern]):

```
δ_S      =  β / 2          Stirn-Druckfläche = Winkelhalbierende
δ_F      =  β − π/2        Ferse-Druckfläche = rechtwinklig zur Strebe
σ_Ferse  =  α  =  π − β    Ferse-Sohle = parallel zur Strebe
```

Die Winkelhalbierende `δ_S = β/2` ergibt gleichen Hankinson-Winkel in
Druckstab und Trägerbauteil (Hirnholz-auf-Hirnholz-Optimum); die Ferse weicht
ab (rechtwinklig zur Strebe) und bildet mit der ∥-Strebe-Sohle einen
rechtwinkligen L-Apex (90°). **Frei** ist allein die **Stirn-Sohle σ_S**
(handwerkliche Freimachungs-Fläche, kein Norm-Winkel).

### Geometrie der Anschnittflächen

Sei Π_⊥(B) ⊂ ℝ³ die Lotebene durch die Bauteilachse von B.
Im horizontalen Standardfall ist Π_⊥(B) die x-z-Ebene des
Bauteil-Lokalsystems. Der Druckstab-Aufsetzpunkt Q liegt nach
Konvention bei

```
Q:=  (x_0, 0, h_B)         in Bauteil-Lokal-Koordinaten.       (3)
```

**V-Ausschnitt (allgemein).** Jeder einfache Versatz-Ausschnitt ist ein
nach unten zeigendes **Dreieck-Prisma** (V) aus **zwei geneigten**
Schnitten — einer **Druckfläche** (Winkel δ zur Faser, nimmt den Hauptdruck
auf) und einer **Sohle** (Winkel σ zur Faser, kein Hauptdruck) —, **keiner
waagrecht (∥ Unterkante) und keiner lotrecht**. Beide Flächen zeigen
firstseitig zur Strebe. Damit fällt Collings vierte Form — der
**rechtwinklige Versatz** (Druckfläche lotrecht zum Gurt, α_S = 0,
α_D = γ; Colling §8.5, Tab. 8.3) — **aus diesem Modell heraus**: seine
lotrechte Druckfläche ist kein geneigter V-Schnitt. Modelliert sind
allein Stirn (Winkelhalbierende), Ferse (⊥ Strebe) und ihre Kombination
(DOPPELT); der rechtwinklige Versatz ist nicht abgebildet (selten, hoher
Querzug am Gurt).

In der Lotebene mit Aufsetzpunkt A = (x_A, 0, h_B):

```
A  =  (x_A, 0, h_B)                       Druckfläche ∩ Oberseite (fußseitig)
C  =  (x_A + t·cot δ, 0, h_B − t)          Apex (Druckfläche ∩ Sohle)        (4)
B  =  (x_A + t·(cot δ + cot σ), 0, h_B)    Sohle ∩ Oberseite (firstseitig)
```

mit der vertikalen Tiefe t (z-Abfall = t). Die nach innen (ins V) weisenden
Flächennormalen sind

```
ν_hat_Druck  =  sin δ · e_hat_x^B  +  cos δ · e_hat_z^B,                     (5)
ν_hat_Sohle  =  − sin σ · e_hat_x^B  +  cos σ · e_hat_z^B.
```

Der **Apex-Innenwinkel** (Öffnung des Ausschnitts) ist

```
∠(A, C, B)  =  π − δ − σ.                                            (6)
```

Der Anschnittquerschnitt ist der Durchschnitt dreier Halbräume in der
Lotebene (über [y_min, y_max] extrudiert kommen die zwei y-Deckel hinzu →
fünf Halbräume des prismatischen Werkzeugkörpers):

```
Δ  =  { z ≤ h_B }  ∩  { ⟨P − A, ν_hat_Druck⟩ ≥ 0 }
                    ∩  { ⟨P − C, ν_hat_Sohle⟩ ≥ 0 }.                 (7)
```

**Stirn-Ausschnitt** (art ∈ {STIRN, DOPPELT}): Druckfläche =
**Winkelhalbierende** `δ = δ_S = β/2` (aus β abgeleitet), Sohle = freier Winkel
`σ = σ_S` (nicht normiert, handwerkliche Freimachung). Flaches σ_S ⇒
**stumpfer** Apex (π − δ_S − σ_S > π/2). Aufsetzpunkt A_S:= Q.

**Fersen-Ausschnitt** (art ∈ {FERSE, DOPPELT}): Druckfläche **rechtwinklig
zur Strebe** `δ = δ_F = β − π/2`, Sohle **∥ Strebe** `σ = α = π − β`.
Damit ist der Apex `π − (β − π/2) − (π − β) = π/2` — ein **rechtwinkliger
L-Ausschnitt** (90°). **Kein** Spiegel der Stirn (gleiche Seite, andere
Neigungen). Aufsetzpunkt:
- für **art = FERSE** (einfach): A_F:= Q;
- für **art = DOPPELT**: A_F liegt firstseitig am **Gipfel** der Stirn-Sohle,
  `x_{A_F} = x_0 + t_S·(cot δ_S + cot σ_S)` (s. Werkzeugkörper DOPPELT).

### Werkzeugkörper

Der **Werkzeugkörper** des Versatzes ist das prismatische
Volumen, das den Anschnittquerschnitt in der Lotebene Π_⊥(B)
über die Bauteilbreite b_B (oder einen Teil davon, je nach
`lokalePlatzierung`) entlang e_hat_y^B extrudiert:

```
K_Versatz(p_Versatz):=  Δ_Versatz(art)  ×  [y_min, y_max]      (8)
```

mit dem Anschnittquerschnitt Δ_Versatz(art) ⊂ Π_⊥(B) als **V-Dreieck**
conv{A, C, B} nach (4) (Druckfläche A–C, Sohle C–B, offene Mündung B–A auf
z = h_B):

- **art = STIRN**: Δ_Versatz = conv{ A_S, C_S, B_S } mit A_S = Q, Druckwinkel
  δ = δ_S (Winkelhalbierende) und Sohlenwinkel σ = σ_S (frei). Fünf
  Halbräume (Innennormalen ins V): Oberseite z ≤ h_B, Druckfläche ν_hat_Druck,
  Sohle ν_hat_Sohle, zwei y-Deckel. Apex stumpf (π − δ_S − σ_S).
- **art = FERSE**: Δ_Versatz = conv{ A_F, C_F, B_F }, **gleiche Seite** wie die
  Stirn (firstseitig), Druckfläche **rechtwinklig zur Strebe** (δ_F = β − π/2),
  Sohle **∥ Strebe** (σ = α = π − β) ⇒ rechtwinkliger L-Apex (90°). **Kein**
  Spiegel. A_F = Q.
- **art = DOPPELT**: Der Werkzeugkörper ist die **nicht-konvexe Vereinigung**
  des **Stirn-V** (vorn, flach: δ_S, σ_S) und des **Fersen-V** (hinten, tief:
  δ_F, σ = α), **beide firstseitig** zur Strebe. Die Stirn-Sohle steigt
  firstseitig auf die Oberkante und trifft dort die Fersen-Druckfläche: der
  Fersen-Aufsetzpunkt sitzt am **Gipfel** der Stirn-Sohle,
  `x_{A_F} = x_0 + t_S·(cot δ_S + cot σ_S)`. Dazwischen bleibt der
  **Versatzkamm** als **Spitze auf z = h_B** (kein Plateau; die
  [versatzkammBreite] `b_K` ist nur Bemessungs-Kenngröße, **ohne
  Geometrie-Wirkung**). Wirkung (9): `Träger \ (Stirn-V ∪ Fersen-V)`,
  sequenzielle konvexe Differenz (Träger \ Stirn \ Ferse → `KonvexZerlegung`).

Die **Wirkung** des Versatzes auf das Trägerbauteil ist die
Boole'sche Differenz nach `bearbeitung`:

```
G_B'(F):=  G_B^lokal  \  K_Versatz(p_Versatz).                 (9)
```

Damit ist ein **Versatz** (als Subtyp von `bearbeitung`) das
Tupel

```
F:=  (uuid, typ = Versatz, parameter = p_Versatz,
       lokale_platzierung = T_F, bezeichnung?)                  (10)
```

mit den Pflicht- und Optionalfeldern aus `bearbeitung`. Das
zugehörige Trägerbauteil B ist **nicht Bestandteil des Tupels**,
sondern ergibt sich aus der partitiven Komposition: der Versatz
ist Element der Bearbeitungs-Liste genau eines Bauteils.

## Wohldefiniertheit

- **Existenz**: Für jeden zimmermannsmäßig hergestellten
  Versatz (Stirn-, Fersen- oder doppelten Versatz) an einer
  Schwelle, einem Rähm, einem Bundbalken oder einer Fußpfette
  lässt sich das Tupel angeben. Mindestkonfiguration: art =
  STIRN, β = 2π/3 (120°, entspricht einer 60°-Strebe),
  σ_S = π/12 (freie flache Sohle), t_S = h_B/6, t_F = ⊥,
  l_v = max(8·t_S, 200 mm), T_F = id_SE(3); daraus abgeleitet
  δ_S = β/2 = π/3.
- **Eindeutigkeit der Werkzeugkörper-Konstruktion**: Bei
  festgelegtem Parametertupel p_Versatz und Bauteil B mit
  bekannter `lokalePlatzierung` sind die V-Eckpunkte A, C, B
  (bzw. die analogen Fersen-Punkte) nach (3), (4) eindeutig
  bestimmt, der Anschnittquerschnitt Δ_Versatz(art) ist als
  konvexe Hülle eindeutig festgelegt, und das Werkzeugvolumen
  K_Versatz(p_Versatz) nach (8) ist eindeutig. Die Konstruktion
  ist unabhängig von der Wahl des typeigenen Bezugs-
  Koordinatensystems des Werkzeugkörpers (siehe `bearbeitung`,
  Wohldefiniertheit).
- **Geometrische Nicht-Degeneriertheit (harte Invarianten,
  Validierungsfehler bei Verletzung)**:
  1. **Strebenanschlusswinkel im stumpfen Bereich**:
     β ∈ (π/2 + ε_W, π − ε_W). Bei β ≤ π/2 (Strebe rechtwinklig
     oder steiler) ist ein Versatz im klassischen Sinn nicht
     mehr definiert; bei β ≥ π (Druckstab und Trägerbauteil
     antiparallel) ist die Geometrie entartet.
  2. **Tiefenpositivität pro aktiver Anschnittfläche**:
     für art ∈ {STIRN, DOPPELT} gilt t_S > ε_L; für art ∈
     {FERSE, DOPPELT} gilt t_F > ε_L.
  3. **Tiefenbeschränkung am Trägerbauteil**: für jede aktive
     Anschnittfläche gilt t_i ≤ h_B − ε_L (i ∈ {S, F}). Ein
     Versatz mit Tiefe ≥ Bauteilhöhe würde das Trägerbauteil
     durchtrennen.
  4. **Winkel-Wohlgeformtheit (offener Bereich (0, π/2))**: der
     **freie** Stirn-Sohlenwinkel σ_S ∈ (ε_W, π/2 − ε_W). Die
     **abgeleiteten** Druckflächen-Winkel δ_S = β/2 und δ_F = β − π/2
     folgen aus β und liegen für β ∈ (π/2 + ε_W, π − ε_W) in (0, π/2). Bei
     Winkel = 0 fällt die Fläche mit der Trägerbauteil-Oberseite
     zusammen (waagrecht); bei = π/2 mit der Stirnfläche (lotrecht)
     — in beiden Grenzfällen entartet das V. (σ_S ist nicht
     normiert, aber zur Wohlgeformtheit des V beschränkt.)
  5. **Vorholzlängen-Positivität**: l_v > ε_L.
  6. **Position innerhalb des Trägerbauteils**: x_0 muss so
     gewählt sein, dass sowohl der Stirn-/Fersen-Aufsetzpunkt
     als auch alle Anschnittausstiege auf der Bauteil-Oberseite
     im Intervall [ε_L, ℓ_B − ε_L] liegen, und dass die nach
     der Vorholzlänge l_v geforderte Holzstrecke bis zum
     Bauteilende vorhanden ist. Verletzung → Validierungsfehler
     `VersatzPositionAusserhalbBauteil` (analog zur Kerve).
  7. **Doppelter Versatz — Kammbreite-Positivität**: für
     art = DOPPELT gilt b_K > ε_L. b_K ist eine **Bemessungs-
     Kenngröße** (Mindeststeg zwischen den Scherfugen, EC5-Schub)
     ohne Geometrie-Wirkung — der Versatzkamm ist im Werkzeugkörper
     eine Spitze auf z = h_B (Stirn-Sohle ∩ Fersen-Druckfläche),
     kein Plateau der Breite b_K.
- **Plausibilität (weiche Invarianten, Warnung; kein
  Validierungsfehler — siehe quellenkonflikt-Block):**
  1. **Tiefen-Faustregel NCI NA.12**: für jede aktive
     Anschnittfläche gilt:
     - α ≤ 50° (flacher Strebenanschluss, α:= π − β):
       t_i ≤ h_B / 4,
     - α ≥ 60° (steiler Strebenanschluss):
       t_i ≤ h_B / 6,
     - 50° < α < 60°: lineare Interpolation zwischen h_B/4
       und h_B/6.
     Verletzung → `Warnung.VersatzZuTief`. Die App-Konstanten
     heißen `Toleranzen.VERSATZ_TIEFE_FLACH_VIERTEL` (Default
     1.0/4.0) und `Toleranzen.VERSATZ_TIEFE_STEIL_SECHSTEL`
     (Default 1.0/6.0).
  2. **Vorholzlänge-Faustregel NCI NA.12**:
     l_v ≥ max(8 · t_v, 200 mm), wobei t_v die maßgebende
     Versatztiefe ist (für art ∈ {STIRN, FERSE}: t_v = t_S
     bzw. t_F; für art = DOPPELT: t_v = max(t_S, t_F)).
     Verletzung → `Warnung.VersatzVorholzZuKurz` mit Hinweis
     auf EC 5 6.5 Schubnachweis.
  3. **Druckflächen-Winkel zwingend aus β (keine Warnung)**:
     δ_S = β/2 (Stirn, Winkelhalbierende) und δ_F = β − π/2 (Ferse,
     ⊥ Strebe) sind nach EN 1995-1-1 **nicht frei wählbar**, sondern
     aus β bestimmt (Recherche-Bericht
     [intern]). Die
     Winkelhalbierende ergibt gleichen Hankinson-Winkel (π − β)/2 in
     Druckstab und Trägerbauteil (Hirnholz-auf-Hirnholz-Optimum;
     Stufe-3-Theorie-Inhalt, folgt formal aus der Hankinson-
     Formulierung, siehe `hankinson_winkel`). Da δ_S/δ_F nicht
     abweichen können, entfällt die frühere Optimum-Warnung.
  4. **Doppelter Versatz — Tiefendifferenz**: für art = DOPPELT
     gilt die Praxisregel t_F ≥ t_S + 10 mm (Ferse mindestens
     1 cm tiefer als Stirn, sonst Abscher-Gefahr in der
     Versatzkamm-Sohle). Verletzung →
     `Warnung.VersatzKammSohleZuFlach`.
- **Subtraktivität (geerbt von `bearbeitung`)**: G_B'(F) ⊆
  G_B^lokal nach (9); siehe `bearbeitung`.
- **Zuordnungs-Eindeutigkeit**: Der Versatz ist über die
  partitive Komposition genau einem Bauteil (dem Trägerbauteil)
  zugeordnet. Dass er mit einem zweiten Bauteil (dem Druckstab)
  eine formschlüssige Druckkontakt-Beziehung herstellt, ist
  keine geometrische Voraussetzung der Versatz-Geometrie selbst,
  sondern ergibt sich erst im Tragwerks-Kontext (siehe
  `verbindung`, `tragwerk`).
- **Lagesicherung gegen Abheben**: Der Versatz überträgt
  ausschließlich Druckkräfte längs der Druckstab-Achse. Eine
  Sicherung gegen Abheben (Bolzen, Klammer, Lasche, Klebung)
  ist normativ vorgeschrieben (NCI NA.12), aber **nicht
  Bestandteil der Versatz-Geometrie selbst**; sie wird als
  separates `Verbindungsmittel` (`hg_verbindungsmittel.md`) am
  Verbindungs-Aggregat geführt.
- **Nicht-Zirkularität**: Die Definition stützt sich nur auf
  bereits definierte Begriffe (`bearbeitung`, `bauteil`,
  `uuid`, `lokales_koordinatensystem`, `polyeder`,
  `bauteilachse`, `lotebene`, `toleranzen`) sowie auf die
  abstrakte Art-Klassifikation 𝒜. Der Verweis auf
  `hankinson_winkel` in der Plausibilitäts-Bedingung 3 ist
  Theorie-Schicht-Referenz, nicht Definitionsbestandteil; die
  Geometrie des Versatzes ist auch ohne den Hankinson-Winkel
  vollständig definiert.

## Erläuterung (nicht normativ)

Der Versatz ist die klassische zimmermannsmäßige
**Druck-Verbindung**: er überträgt Druckkräfte zwischen einem
druckbeanspruchten Anschlussbauteil (Strebe, Kopfband, Sparren)
und einem aufnehmenden Trägerbauteil (Schwelle, Rähm,
Bundbalken, Fußpfette). Anders als die **Kerve** — die eine
**welt-horizontale Sohle** als Auflagefläche für
quer einlaufende Lasten erzeugt — hat der Versatz eine
**geneigte Anschnittfläche**, gegen die der Druckstab unter
einem Winkel zur Trägerbauteil-Faser drückt.

### Die drei kanonischen Subtypen

**Stirnversatz** (`art = STIRN`, Synonyme: einfacher Versatz,
einseitiger Versatz; engl. *single step joint*, *simple notched
joint*). Eine **einzige** geneigte Anschnittfläche der
keilförmigen Ausnehmung im Trägerbauteil. Das berufssprachliche
Konstruktionsmaß ist der **winkelhalbierende Stirnversatz** mit
Anschnittwinkel δ_S = β/2 (Winkelhalbierende des stumpfen
Außenwinkels β); dann sind die Hankinson-Winkel zur Faser in
Druckstab und Trägerbauteil **gleich groß** und gleich (π − β)/2,
und die Druckspannungen werden ausgewogen aufgenommen
(Mönck/Rug Kap. 7; Holzbau-Taschenbuch Kap. 19; Recherche
§D.3, §C.1). Anwendung: Strebenfuß auf Schwelle, Kopfband-Anschluss.

**Fersenversatz** (`art = FERSE`, Synonyme: hinterer Versatz,
**Brustversatz**, Rückversatz; engl. *heel notch*, *rear notch*). Eine
**einzige** geneigte Anschnittfläche **rechtwinklig zur Strebe** abgestirnt
(δ_F = β − π/2); ihr tiefster Punkt zeigt zur Druckstab-Innenseite (Ferse),
die Druckstab-Stirn ragt vor. Eingesetzt, wenn der Trägerbauteil-Überstand
reduziert werden soll, weil ein Teil der Vorholzlänge unter dem Druckstab
liegt. Die Kraftübertragung im Trägerbauteil ist **deutlich ungünstiger**
als beim Stirnversatz: der Beanspruchungswinkel zur Schwellen-Faser ist
α_S = γ (der volle Strebenwinkel) statt γ/2 — nach Hankinson überträgt der
Stirnversatz bei gleicher Versatztiefe rund 70 % höhere Kräfte (Colling §8.5,
Bild 8.15 + Tab. 8.4: Beiwert k_V,γ; α_D = 0 in der Strebe). Konstruktiv
vorteilhaft sind allein der kleinere Einschnitt und die geringere Ausmitte
e = (h_D − t_V/cos γ)/2 (Recherche §C.1; Colling §8.5; Holzbau-Taschenbuch
Kap. 19). **Benennung:** zur Begriffs-Kollision „Brustversatz" (Synonym,
Web-Korpus) ↔ „Fersenversatz" (Colling/BTLx-HEEL) s. quellenkonflikt
Konflikt 6.

**Doppelter Versatz** (`art = DOPPELT`, Synonyme:
Stirn-Fersen-Versatz, Doppel-Versatz; engl. *double step joint*).
Kombination aus Stirn- und Fersenversatz mit **zwei** V-Ausschnitten
im Trägerbauteil, die direkt aufeinander folgen; dazwischen bleibt der
**Versatzkamm** als **Spitze auf der Oberkante** (Stirn-Sohle trifft
firstseitig die Fersen-Druckfläche, kein Plateau). Höchste Anforderung
an Passgenauigkeit und höchste Druck-Tragfähigkeit der drei Varianten.
Konvention (BFH/SIA): Stirntiefe meist 1/6·h, Fersentiefe 1/4·h.
Praxisregel: der Fersenversatz muss mindestens 1 cm (DIN 1052) bzw.
**1,5 cm (ÖNORM B 1995)** tiefer als der Stirnversatz eingeschnitten
sein (`t_F ≥ t_S + 10…15 mm`), sonst tritt Abscheren im Versatzkamm
zwischen den beiden Scherfugen ein (Holzbau-Taschenbuch Kap. 20;
BFH 2016 Kap. 2; Recherche §C.1, §E.4).

### Englische Falsche Freunde

Die englische Holzbau-Literatur unterscheidet trennscharf
zwischen **birdsmouth** (= **Kerve**: Sattel mit waagerechter
Sohle, siehe `hg_kerve.md`) und **single/double step joint**
(= **Versatz**: geneigte Druckkontaktfläche). Innerhalb der
Birdsmouth-Geometrie heißen die Teilflächen **seat cut** (=
Sohle, Auflagefläche) und **heel cut** bzw. **plumb cut** (=
Senkel). Diese Begriffe gehören sämtlich zur Kerve, nicht zum
Versatz. Auch **step-lapped rafter seat** (eine Birdsmouth-
Variante mit zusätzlicher Verstemmung) ist Kerve. Die
abgelehnten Benennungen oben binden diese Übersetzungsfalle
strukturell.

### Versatz, Kerve und Versatzkerve

Versatz und Kerve sind **geometrisch und funktional disjunkt**
(Recherche §F): die Kerve hat eine welt-horizontale Sohle und
einen welt-vertikalen Senkel (90°-Bedingung, welt-aligned),
der Versatz hat eine geneigte Anschnittfläche (bauteil-aligned
am Trägerbauteil). In der zimmermannsmäßigen Praxis werden
beide am gleichen Anschluss (Sparrenfuß auf Bundbalken bei
steilen Dächern) oft **kombiniert**; diese Kombination ist in
`hg_kerve.md` als **Versatzkerve** geführt und modelliert als
zwei separate Bearbeitungen `Kerve` + `Versatz` an demselben
Bauteil, nicht als eigene Bearbeitungs-Klasse.

### Dachtyp-Bindung

Im **Pfettendach** ist die Kerve die Standard-Sparren-Pfetten-
Verbindung. Im **Sparrendach** und **Kehlbalkendach** sind
**Versätze** (Stirn-, Fersen-, doppelter Versatz) die
Standard-Sparren-zu-Bundbalken-Verbindung, weil die Druckkräfte
in Sparrenlängsrichtung dort erheblich sind und von der
einfachen Kerve nicht abgetragen werden können (Wikipedia
*Sparren*; Recherche §F, Konflikt 6 in `hg_kerve.md`).

### Tätigkeit vs. Resultat

Im zimmermannssprachlichen Sprachgebrauch bezeichnet „versetzen"
die Tätigkeit (das Einschneiden der Anschnittflächen), „Versatz"
das Resultat (die geometrische Ausnehmung am fertigen Bauteil).
Dieser Glossareintrag definiert ausschließlich die
**Resultatslesart**.

## Beziehungen

- **Oberbegriff**: `bearbeitung`. Strukturell ist der Versatz
  eine konkrete subtraktive Bearbeitung mit dem typspezifischen
  Parametertupel p_Versatz und der diskreten Konfigurations-
  Achse `art`.
- **Bestandteile (partitiv)** (geerbt von `bearbeitung`):
  - **UUID** (`uuid`): technische Identität, Pflicht.
  - **Typ**: konstant `Versatz`.
  - **Parameter** (typspezifisch): x_0, art, β, t_S, σ_S, t_F,
    b_K, l_v (mit Pflichtfeldern abhängig von `art`); die Druckflächen-
    winkel δ_S = β/2, δ_F = β − π/2 sind aus β abgeleitet, kein Feld.
  - **Lokale Platzierung**: SE(3); Identität im Standardfall.
  - **Bezeichnung**: optional.
  - **Keine Backref auf das Bauteil**: das Trägerbauteil ist
    über die partitive Komposition bestimmt (Versatz ist Element
    der Bearbeitungs-Liste eines Bauteils), nicht über ein Feld
    am Versatz-Objekt.
- **Verwendung**:
  - Bestandteil eines **Trägerbauteils** (typisch Schwelle,
    Rähm, Bundbalken, `fusspfette`): der Versatz erscheint als
    Bearbeitung in der Liste der Bauteil-Bearbeitungen;
    geometrisch sitzt er typischerweise an der Oberseite des
    Trägerbauteils an einer Position entlang der Bauteilachse,
    an der ein Druckstab aufsetzt.
  - **Druckkontakt mit einem Druckstab** (typisch `sparren`,
    Strebe, Kopfband): die Anschnittfläche bildet die
    formschlüssige Druckkontaktfläche. Die geometrische
    Beziehung Versatz ↔ Druckstab ist nicht in der Versatz-
    Bearbeitung selbst geführt (der Versatz „kennt" den
    Druckstab nicht), sondern wird über das Verbindungs-Aggregat
    hergestellt (`hg_verbindung.md`).
- **Spezialisierungen** (Geometrie-Varianten desselben Bemessungs-
  falls, **keine** eigenen Glossareinträge):
  - **Stirnversatz** (`art = STIRN`).
  - **Fersenversatz** (`art = FERSE`).
  - **Doppelter Versatz** (`art = DOPPELT`).
- **Abgrenzung**:
  - **Kerve** (`kerve`): Auflager-Bearbeitung mit
    welt-horizontaler Sohle (Bleischnitt) und welt-vertikalem
    Senkel; 90°-Bedingung welt-aligned. Der Versatz hat dagegen
    eine **geneigte Anschnittfläche** bauteil-aligned am
    Trägerbauteil. In der Praxis häufig kombiniert
    (Versatzkerve), aber zwei separate Bearbeitungs-Klassen.
  - **Bearbeitung** (`bearbeitung`): generischer Oberbegriff;
    Versatz ist eine von mehreren Bearbeitungs-Subtypen.
  - **Zapfen** (`zapfen`, Forward-Verweis): vorspringender
    Zapfen am Druckstab-Ende, der in ein Zapfenloch des
    Trägerbauteils einsetzt; **Längs-Verbindung** mit Sekundär-
    Sicherung (Holznagel) für Quer- und Zugkräfte. Der Versatz
    ist demgegenüber rein druckübertragend und ohne
    Zapfen-Geometrie.
  - **Zapfenloch** (`zapfenloch`, Forward-Verweis): rechteckige
    Subtraktion zur Aufnahme eines Zapfens am Trägerbauteil;
    geometrisch nicht keilförmig.
  - **Blatt** (`blatt`, Forward-Verweis Kategorie A): halbe
    Holzdicke beidseitig abgetragen, Hölzer greifen flach
    übereinander; **Längs-Stoss** oder Eckverbindung. Der
    Versatz hat keine halbierte Holzdicke, sondern eine
    keilförmige Ausnehmung.
  - **Kamm** (`kamm`, Forward-Verweis Kategorie A): einseitige
    Materialwegnahme am übergreifenden Holz; **Quer-Sicherung**
    kreuzend liegender Hölzer. Der Versatz ist eine geneigte
    Druckkontaktfläche, kein Übergreifen.
  - **Verbindung** (`verbindung`): Aggregat aus Bauteilen +
    Verbindungsmitteln + Verbindern an einem Knotenpunkt. Eine
    Verbindung enthält **keine** Versätze direkt; Versätze sind
    Eigenschaften ihrer Bauteile, das Verbindungs-Aggregat
    bündelt sie.
  - **Anschnitt** (`anschnitt`, Forward-Verweis): planare
    Stirn- oder Schrägfläche **am Bauteilende**; entfernt das
    Bauteilende, nicht eine Ausnehmung im Bauteilfeld. Der
    Versatz dagegen sitzt im Bauteilfeld als Ausnehmung; in
    Sonderfällen (Versatz an Trägerbauteil-Ende) kann ein
    Anschnitt mit dem Versatz zusammenfallen, modelliert wird
    er dann typabhängig.
  - **Schlitz** (`schlitz`, Forward-Verweis): längliche
    Subtraktion mit kleiner Breite und großer Tiefe zur
    Aufnahme eines Schlitzblechs; andere Topologie.
  - **Bohrung** (`bohrung`, Forward-Verweis): zylindrische,
    rotationssymmetrische Subtraktion; andere Topologie.
  - **Sparren** (`sparren`): typischerweise das Druckstab-
    Bauteil bei Sparren-zu-Bundbalken-Anschlüssen im
    Sparrendach; nicht der Versatz selbst.
  - **Fußpfette** (`fusspfette`): kann Trägerbauteil eines
    Versatzes sein, wenn Streben oder Kopfbänder dagegen
    drücken; nicht der Versatz selbst.
  - **Querschnitt** (`querschnitt`): die Querschnittsfläche
    eines Bauteils im ungeschwächten Zustand; der Versatz
    führt eine lokale Querschnittsschwächung herbei, die im
    Bemessungsschnitt am Versatzort durch die maßgebende
    Tiefe t_v erfasst wird.

## Quellen

**Primär (normativ):**

- DIN EN 1995-1-1/NA:2013-08, „Nationaler Anhang Deutschland
  zum Eurocode 5", NCI NA.12 „Zimmermannsmäßige Verbindungen"
  (bibliographisch und über mehrere unabhängige
  Sekundärbeschreibungen belegt; Volltext-Verifikation der
  Regelwerte aus dieser Recherche nicht möglich — DIN-Media-
  Paywall; siehe quellenkonflikt-Block).
- DIN EN 1995-1-1:2010-12, „Eurocode 5: Bemessung und
  Konstruktion von Holzbauten – Teil 1-1", Abschnitt 5.2,
  Abschnitt 6.1.5 und Abschnitt 6.5.
- SIA 265:2021, „Holzbau", Schweizerischer Ingenieur- und
  Architektenverein, Zürich. Annex-Stelle für den Versatz
  bibliographisch belegt (Bestand `hg_verbindung.md` referenziert
  „Anhang A"), durch diese Recherche nicht volltext-verifiziert.
- DIN 1052:2008-12 (zurückgezogen), „Entwurf, Berechnung und
  Bemessung von Holzbauwerken", Abschnitt zimmermannsmäßige
  Verbindungen.

**Sekundär:**

- Mönck, W.; Rug, W.: *Holzbau – Bemessung und Konstruktion.*
  16. Auflage, Beuth, Berlin 2015, Kap. 7.
- Peter, M.; Scheer, C. (Hrsg.): *Holzbau-Taschenbuch.*
  Wiley-VCH, Berlin 2015, Kap. 19 „Einfacher Versatz" und
  Kap. 20 „Doppelter Versatz".
- Gerner, M.: *Fachwerk – Instandsetzung, Sanierung, Neubau.*
  DVA, 7. Auflage 2007, Glossar.
- Natterer, J.; Herzog, T.; Volz, M.: *Holzbau-Atlas.*
  4. Auflage, Birkhäuser, Basel 2003.
- Blass, H. J.; Sandhaas, C.: *Timber Engineering – Principles
  for Design.* KIT Scientific Publishing, Karlsruhe 2017,
  Kap. „Carpentry Joints".
- Branco, J. M.; Descamps, T.: *Analysis and strengthening of
  carpentry joints — Single step joint: overview.* academia.edu
  (Korpus für engl. Pendant).
- design2machine: *BTLx interface description*, Version 2.1,
  16.11.2023, Processings `StepJoint` und `StepJointNotch`
  (Parameter-Schemata nicht volltext-verifiziert).
- baunetzwissen.de: „Zimmermannsmäßige Verbindungen" (abgerufen
  2026-05-14), mit Sekundärzitat zu DIN EN 1995-1-1/NA NCI NA.12.

**Korpus (nicht autoritativ):**

- Recherche-Bericht
  [intern] (Quellen-Lage,
  Auflösung der drei Subtypen, englisches Vergleichsmaterial).
- baubeaver.de: „Die 5 wichtigsten Versatz-Arten",
  „Stirnversatz" (Korpus für DACH-Praxisterminologie).
- statikweb.iivs.de: „Stirnversatz Formeln" (Korpus für
  Faustregeln).
- harzerstatik.de: „Holzversatz 10.0 EC5-1-1" (Korpus für
  EC-5-Anwendungspraxis).
- Wikipedia, Lemma *Birdsmouth joint* (Korpus für engl.
  Falsche-Freunde-Markierung).
- Carolina Timberworks Glossary, „step-lapped rafter seat"
  (Korpus für engl. Falsche-Freunde-Markierung).
