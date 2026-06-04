---
id: pultkante
benennung: Pultkante
synonyme: [Pultdachoberkante, "obere Dachkante (Pultdach)", Pultfirst]
abgelehnte_benennungen: [First, Firstkante, "obere Dachkante", Wandanschluss, Attikakante, "shed roof ridge", "high eaves"]
oberbegriff: dachkante
begriffstyp: partitiv
voraussetzungen: [strecke, dachflaeche, polygon, vektor, toleranzen, dachkante]
abgrenzung_zu: [traufe, first, ortgang, grat, kehle, wandanschlusskante, attika]
status: entwurf
subglossar_pendant: notwendig
quellen_primär:
  - "SIA 232/1:2020 'Geneigte Dächer', Schweizerischer Ingenieur- und Architektenverein, Abschnitt 1 (Begriffe): Pultdach mit oberer Begrenzungskante als horizontaler Randkante einer einzigen Dachfläche."
  - "DIN 1356-1:1995-02 'Bauzeichnungen – Teil 1', Abschnitt 5 (Darstellung von Dächern): obere Dachkante des Pultdachs als horizontale Randlinie."
quellen_sekundär:
  - "Mönck, W.; Rug, W.: Holzbau – Bemessung und Konstruktion. 16. Aufl., Beuth Verlag 2015, Kap. Dachformen (Pultdach)."
  - "Lignum (Hrsg.): Lignatec 'Geneigte Dächer in Holzbauweise', Lignum, Zürich, aktuelle Auflage."
quellenkonflikt: |
  Weder SIA 232/1 noch DIN 1356 führen einen eigenständigen Begriff
  „Pultkante" — die obere Begrenzungskante eines Pultdachs wird in
  beiden Normen kontextuell beschrieben, aber nicht benannt. In der
  Praxis sind drei Bezeichnungen verbreitet:
  (a) **Pultkante** / **Pultdachoberkante**: präziser, abgrenzend zum
      First, weil keine zweite Dachfläche anschließt.
  (b) **Pultfirst**: umgangssprachlich; verwischt die Abgrenzung zum
      First (der Begriff First ist normativ als Schnittkante zweier
      Dachflächen definiert — siehe `hg_first.md`).
  (c) **obere Dachkante**: deskriptiv, aber mehrdeutig.
  **Festlegung dieses Glossars**: Pultkante bezeichnet hier
  ausschließlich die geometrisch obere Polygonrandkante einer
  einzelnen geneigten Dachfläche, an der **keine zweite Dachfläche**
  anschließt. „Pultfirst" wird in `abgelehnte_benennungen` aufgeführt,
  weil der Begriff First konsequent für Schnittkanten zweier
  Dachflächen reserviert bleibt.

  **Mehrdeutigkeit am Wandanschluss**: Stößt die obere Kante eines
  Pultdachs an eine aufgehende Wand (Brandwand, Nachbarwand, Attika),
  so kann dieselbe geometrische Kante zugleich als **Pultkante** der
  Dachfläche und als **Wandanschlusskante** der Wand klassifiziert
  werden. Die hier gegebene Definition betrifft nur die Klassifikation
  als Dachkante; die Wand-Klassifikation ist davon unabhängig und wird
  in einem eigenen Eintrag (`wandanschlusskante`, folgt) behandelt.
  Die beiden Klassifikationen schließen einander **nicht** aus — eine
  Kante kann sowohl Pultkante als auch Wandanschlusskante sein.

  **Horizontalitätsforderung**: Im Regelfall ist die Pultkante
  horizontal (Pultdach mit waagerechter Oberkante). Die Definition
  fordert Horizontalität als Klassifikationsbedingung; geneigte
  obere Polygonrandkanten (z. B. bei einem Pultdach mit schrägem
  Wandanschluss) sind als **Ortgang** zu klassifizieren, nicht als
  Pultkante. Diese Festlegung hält die sechs Klassen disjunkt.

  Klassifikation: Eine Kante einer Dachflächenfamilie soll genau
  einer der sechs Klassen (Traufe, First, Ortgang, Grat, Kehle,
  Pultkante) zugeordnet werden — siehe `hg_dachkante.md`. Pultkante ist
  disjunkt zu First (Randkante statt Schnittkante), zu Traufe
  (oberste statt unterste horizontale Randkante) und zu Ortgang
  (horizontal statt entlang Falllinie).
---

## Prosa-Definition

Eine **Pultkante** ist eine Dachkante einer geneigten Dachfläche, die
vollständig im Rand des Dachflächen-Polygons liegt, näherungsweise
horizontal verläuft, unter allen näherungsweise horizontalen
Polygonrandkanten dieser Dachfläche die höchste, von der untersten
(der Traufe) verschiedene mittlere Höhe besitzt und nicht zugleich
Schnittkante mit einer zweiten Dachfläche der Familie ist.

## Mathematische Definition

Sei

- 𝒟 = { D₁, …, D_m } eine endliche Familie von Dachflächen,
- D = (E, P, n_a) ∈ 𝒟 eine geneigte Dachfläche im Sinne von
  `dachflaeche` mit Trägerebene E, Umrisspolygon P = (v₁, …, v_k),
  äußerer Normale n_a und Dachneigung α ∈ (0, π/2),
- (e₁, …, e_k) die zyklische Folge der Polygonrandkanten
  e_i:= [v_i, v_{i+1}], v_{k+1}:= v_1,
- e_z = (0, 0, 1)ᵀ die vertikale Achse,
- ε_W:= Toleranzen.WINKEL_EPS die Winkeltoleranz,
- ε_L:= Toleranzen.LAENGE_EPS die Längentoleranz,
- für eine Strecke s = [a, b] der **Höhenmittelwert**
  z_bar(s):= ½ · (a_z + b_z) und das **Horizontalitätsmaß**
  h(s):= |⟨e_hat(s), e_z⟩| (vgl. `traufe`).

Die Menge der näherungsweise horizontalen Polygonrandkanten von D ist

```
H(D):= { e_i | h(e_i) ≤ ε_W,  i = 1, …, k }.
```

Eine Polygonrandkante e_i heißt **Schnittkante mit einer anderen
Dachfläche der Familie**, wenn ein j ≠ i existiert mit

```
e_i ⊂ F(P_j),                                                (∗)
```

d. h. wenn e_i auch im abgeschlossenen Polygonbereich F(P_j) einer
zweiten Dachfläche D_j liegt (geprüft mit Toleranz ε_L auf den
Punkt-Polygon-Abstand). Bedingung (∗) charakterisiert genau die
Konfiguration, in der e_i Bestandteil eines Firsts, Grats oder einer
Kehle wäre.

Eine Strecke p ⊂ ℝ³ heißt **Pultkante** der Dachfläche D in der
Familie 𝒟 genau dann, wenn

1. **Randkante**: p ⊂ ∂F(P) — p ist Polygonrandkante von D,
2. **Horizontal**: h(p) ≤ ε_W — p verläuft näherungsweise horizontal,
3. **Höchste Höhe**: z_bar(p) ist Maximum unter allen Elementen
   von H(D), formal
   ```
   z_bar(p) = max { z_bar(e) | e ∈ H(D) },
   ```
   ausgewertet mit Toleranz ε_L auf der Vertikalen (mehrere Kanten
   gleicher Maximalhöhe sind zulässig und werden gemeinsam als
   Pultkante geführt), **und dieses Maximum liegt echt über dem
   Minimum**,
   ```
   max { z_bar(e) | e ∈ H(D) } − min { z_bar(e) | e ∈ H(D) } > ε_L;
   ```
   andernfalls (H(D) auf einer einzigen Höhe) existiert keine
   Pultkante — die Kante ist die Traufe. Diese Teilbedingung sichert
   die Disjunktheit zur Traufe **definitorisch**, nicht erst über die
   Auswertungsreihenfolge,
4. **Keine zweite Dachfläche**: p erfüllt nicht (∗), d. h. es gibt
   keine andere Dachfläche D_j ∈ 𝒟 (j ≠ i), in deren Polygonbereich
   F(P_j) p ganz enthalten wäre. Anders ausgedrückt: p ist
   Randkante **genau einer** Dachfläche.

Die Vereinigung aller so identifizierten Strecken bildet, falls sie
über gemeinsame Eckpunkte zusammenhängt, die **Pultlinie** als
Streckenzug; im Regelfall (Pultdach mit rechteckigem Grundriss)
besteht sie aus genau einer Strecke.

## Wohldefiniertheit

- **Existenz**: Bei einer geneigten Dachfläche D mit nichtleerem
  H(D) wird das Maximum in Bedingung 3 angenommen, da F(P) kompakt
  und ∂F(P) endlich ist. Bedingung 4 ist bei einem isolierten
  Pultdach (m = 1) trivial erfüllt; bei einem Pultdach an einer
  Brandwand bleibt sie erfüllt, weil die Wand keine Dachfläche
  ist (siehe Quellenkonflikt zur Wandanschlusskante).
- **Eindeutigkeit**: Bei einer geneigten Dachfläche mit eindeutiger
  oberer Polygonseite (Regelfall im Holzbau) ist die Pultkante als
  Strecke oder zusammenhängender Streckenzug eindeutig bestimmt.
  Bei Sonderformen mit mehreren gleichhohen oberen Randkanten
  liefert die Definition mehrere gleichberechtigte Strecken — das
  ist gewollt.
- **Disjunktheit zu Traufe**: Traufe ist die Polygonrandkante mit
  **niedrigster** mittlerer Höhe in H(D); Pultkante diejenige mit
  **höchster** — und nach Bedingung 3 nur dann, wenn sich Minimum und
  Maximum um mehr als ε_L unterscheiden (H(D) mehr-höhig). Bei einer
  Dachfläche mit nur einer einzigen horizontalen Randkante (z. B.
  Walmflächen-Dreieck mit einziger Traufkante) sind Minimum und
  Maximum dieselbe Kante; Bedingung 3 ist dann **nicht** erfüllt, und
  es gibt keine Pultkante — die Kante ist die Traufe. Die Disjunktheit
  ist damit **definitorisch** gesichert, nicht erst über die
  Auswertungsreihenfolge. Eine vorgelagerte Schnittkanten-Prüfung
  (First/Grat/Kehle) bleibt als Optimierung sinnvoll, ist für die
  Korrektheit der Klassifikation aber nicht mehr nötig.
- **Disjunktheit zu First**: First ist Schnittkante zweier
  Dachflächen; Bedingung 4 schließt das aus.
- **Disjunktheit zu Ortgang**: Ortgang verläuft entlang der
  Falllinie und ist nicht horizontal; Bedingung 2 schließt das aus.
- **Konsistenz mit `dachkante`**: Eine Pultkante ist nach Bedingung 1
  eine Randkante der Dachfläche D, also eine Dachkante (Fall
  „Randkante").
- **Nicht-Zirkularität**: Die Definition stützt sich nur auf
  `strecke`, `dachflaeche`, `polygon`, `vektor`, `toleranzen` und
  den Oberbegriff `dachkante`.

## Erläuterung (nicht normativ)

Die Pultkante ist die obere, horizontale Randkante einer
Pultdachfläche — das Gegenstück zur Traufe am unteren Rand. Im
Gegensatz zum First entsteht sie nicht durch das Zusammentreffen
zweier Dachflächen, sondern durch das einseitige Ende der Dachfläche.
Konstruktiv schließt sie häufig an eine aufgehende Wand an
(Brandwand, höhere Nachbarwand, Attikabereich); in diesem Fall ist
der Wandanschluss durch eine Wandanschlussabdichtung herzustellen
(Eindeckung mit Wandanschlussblech, Z-Profil oder Hochzug der
Dachhaut).

Bei einem klassischen Pultdach mit rechteckigem Grundriss hat die
einzige Dachfläche genau vier Polygonrandkanten:
- eine Traufe (untere horizontale Kante),
- eine Pultkante (obere horizontale Kante),
- zwei Ortgänge (seitliche, geneigte Kanten entlang der Falllinie).

Komplexere Pultdachformen (z. B. mit polygonal abgeknicktem Grundriss
oder mit gestaffelten Höhen) ergeben Pultlinien aus mehreren
Streckenstücken, die durch die Streckenzug-Modellierung erfasst
werden.

## Beziehungen

- **Oberbegriff**: `dachkante`, Spezialfall „Randkante" mit
  zusätzlichen Lagebedingungen (näherungsweise horizontal, höchste
  mittlere Höhe, keine Schnittkante mit einer zweiten Dachfläche).
- **Geschwister-Begriffe** (andere Spezialisierungen von
  `dachkante`): `traufe`, `first`, `ortgang`, `grat`, `kehle`.
- **Bestandteile (partitiv)**: Anfangspunkt und Endpunkt der
  Pultlinien-Strecke bzw. die Stützpunkte des Streckenzugs.
- **Abgrenzung**:
  - **Traufe** (`traufe`): untere horizontale Randkante; gleiches
    Schema, aber Minimum statt Maximum der mittleren Höhe.
  - **First** (`first`): obere horizontale Schnittkante zweier
    Dachflächen; Bedingung 4 (keine zweite Dachfläche) schließt
    diese Klassifikation aus.
  - **Ortgang** (`ortgang`): seitliche, geneigte Randkante entlang
    der Falllinie; nicht horizontal.
  - **Grat** (`grat`) / **Kehle** (`kehle`): geneigte Schnittkanten
    zweier Dachflächen.
  - **Wandanschlusskante** (eigener Eintrag folgt bei Bedarf): jene
    Kante, an der eine Dachfläche an eine aufgehende Wand stößt;
    kann mit der Pultkante geometrisch zusammenfallen, ist aber eine
    von der Wand-Klassifikation ausgehende, davon **unabhängige**
    Eigenschaft. Eine Kante kann zugleich Pultkante und
    Wandanschlusskante sein.
  - **Attika** / **Attikakante**: aufgehende Mauerkrone an einem
    Flachdachrand; betrifft nicht das Pultdach und ist hier nicht
    definiert.

## Quellen

**Primär (normativ):**

- SIA 232/1:2020, „Geneigte Dächer", Schweizerischer Ingenieur- und
  Architektenverein, Abschnitt 1.
- DIN 1356-1:1995-02, „Bauzeichnungen – Teil 1: Arten, Inhalte und
  Grundregeln der Darstellung", Abschnitt 5.

**Sekundär:**

- Mönck, W.; Rug, W.: *Holzbau – Bemessung und Konstruktion.*
  15. Auflage, Beuth Verlag 2015.
- Lignum (Hrsg.): *Lignatec — Geneigte Dächer in Holzbauweise.*
  Lignum, Zürich, aktuelle Auflage.

**Korpus (nicht autoritativ):**

- Wikipedia, Lemma „Pultdach" (abgerufen 2026-05-08).
