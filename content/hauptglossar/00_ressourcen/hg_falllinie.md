---
id: falllinie
benennung: Falllinie
synonyme: [Gefällelinie, "Linie des größten Gefälles", Steilrichtung]
abgelehnte_benennungen: [Hangrichtung, Aspekt, Dachgefälle, Neigungsrichtung, "fall line", "line of steepest descent", "slope direction"]
oberbegriff: einheitsvektor
begriffstyp: generisch
voraussetzungen: [ebene, vektor, einheitsvektor, toleranzen]
abgrenzung_zu: [hoehenlinie, dachneigung, faserrichtung, gerade]
status: entwurf
subglossar_pendant: notwendig
quellen_primär:
  - "DIN ISO 80000-2:2022-08, 'Größen und Einheiten – Teil 2: Mathematik', Abschnitt 2 (Geometrie und Vektoren), Eintrag zum Gradienten einer skalaren Funktion."
  - "DIN EN ISO 19107:2019 'Geographic information – Spatial schema', Abschnitt 6 (Begriff der Steilrichtung / aspect bei TIN-Oberflächen)."
quellen_sekundär:
  - "Bronstein, I. N.; Semendjajew, K. A.; Musiol, G.; Mühlig, H.: Taschenbuch der Mathematik. Kap. 6.2.4 'Gradient skalarer Felder' und Kap. 3.5 'Ebenen im Raum'."
  - "Fischer, G.: Lineare Algebra. 19. Aufl., Springer Spektrum 2020, Kap. 6.2 (orthogonale Projektion auf einen Untervektorraum)."
  - "Lignum (Hrsg.): Lignatec 'Geneigte Dächer in Holzbauweise', Lignum, Zürich, aktuelle Auflage, Abschnitt 'Dachgeometrie' (Falllinie als Bezugsrichtung für Wasserführung und Eindeckung)."
  - "Mönck, W.; Rug, W.: Holzbau – Bemessung und Konstruktion. 16. Aufl., Beuth Verlag 2015, Kap. 'Dachformen' (Falllinie als senkrechte Richtung zur Trauflinie)."
quellenkonflikt: |
  Keine Holzbau-Norm definiert die Falllinie axiomatisch; sie wird in
  SIA 232/1, DIN 1356-1 und Lignum-Schriften als „Linie des größten
  Gefälles" oder „Richtung senkrecht zur Trauflinie" anschaulich
  beschrieben, ohne Formalisierung. In der Geomatik (ISO 19107) und
  in der Differentialgeometrie ist die Falllinie der negative
  Gradient der Höhenfunktion.

  Eigene Festlegung: Die Falllinie einer geneigten Ebene ist der
  eindeutige in der Ebene liegende Einheitsvektor mit minimaler
  z-Komponente, äquivalent der negative, normierte Gradient der
  Höhenfunktion z(x,y) auf dieser Ebene. Diese Festlegung ist
  konsistent mit Bronstein, Fischer und der Geomatik-Tradition und
  impliziert die anschauliche Holzbau-Charakterisierung „senkrecht
  zur Trauflinie, in Richtung des Gefälles".

  Die Begriffe „Hangrichtung" und „Aspekt" aus der Geomatik werden
  als verwandt, aber nicht synonym geführt: sie bezeichnen typisch
  den Azimut der horizontalen Projektion der Falllinie (Winkel in
  der Horizontalebene), nicht den Vektor selbst. Der hier definierte
  Begriff ist der dreidimensionale Einheitsvektor in der Ebene.
---

## Prosa-Definition

Die **Falllinie** einer nicht-horizontalen Ebene ist der eindeutige in
dieser Ebene liegende Einheitsvektor, dessen z-Komponente unter allen
in der Ebene liegenden Einheitsvektoren minimal (also „am stärksten
nach unten gerichtet") ist; sie zeigt damit in die Richtung des
größten Gefälles, in welcher eine Höhenfunktion auf der Ebene
maximal abnimmt.

## Mathematische Definition

Sei

- E ⊂ ℝ³ eine Ebene im Sinne von `ebene` mit nach oben gerichteter
  Einheits-Normalen n_hat ∈ S², ⟨n_hat, e_z⟩ > 0,
- e_z:= (0, 0, 1)ᵀ die vertikale Achse,
- ε_W:= Toleranzen.WINKEL_EPS die Winkeltoleranz.

**Geneigtheits-Voraussetzung**: ‖n_hat × e_z‖ > 0 (äquivalent
⟨n_hat, e_z⟩ < 1) — die Ebene ist nicht horizontal, also α > 0 in der
Charakterisierung über die Dachneigung α:= arccos(⟨n_hat, e_z⟩). Der
operative Geneigtheits-Test nutzt nach §4 die Kreuzprodukt-Norm
‖n_hat × e_z‖ = sin α (Wohldefiniertheit).

Setze den **horizontalen Anteil von e_z relativ zu E**

```
v:= e_z − ⟨e_z, n_hat⟩ · n_hat   ∈ E_0,
```

wobei E_0 ⊂ ℝ³ der Richtungsraum von E (die durch Translation in den
Ursprung verschobene Ebene) ist. v ist die orthogonale Projektion
von e_z auf E_0; v zeigt nach **oben** entlang der steilsten Richtung
in E_0. Es gilt

```
‖v‖² = 1 − ⟨e_z, n_hat⟩² > 0   (für α > 0),
```

also v ≠ 0.

Die **Falllinie** der Ebene E ist der Einheitsvektor

```
e_hat_fall(E):= −v / ‖v‖
           = −(e_z − ⟨e_z, n_hat⟩ · n_hat) / ‖e_z − ⟨e_z, n_hat⟩ · n_hat‖   ∈ S² ∩ E_0.
```

Das Vorzeichen ist so gewählt, dass ⟨e_hat_fall, e_z⟩ ≤ 0 (die Falllinie
zeigt **nach unten**); das fixiert die antipodale Mehrdeutigkeit.

**Äquivalente Charakterisierung über das doppelte Kreuzprodukt**: Mit
der Lagrange-Identität (a × b) × c = (a · c) b − (b · c) a folgt für
einen Einheitsnormalenvektor n_hat

```
(n_hat × e_z) × n_hat = (n_hat · n_hat) · e_z − (e_z · n_hat) · n_hat = e_z − ⟨e_z, n_hat⟩ · n_hat = v,
```

und damit

```
e_hat_fall(E) = −((n_hat × e_z) × n_hat) / ‖(n_hat × e_z) × n_hat‖.
```

Beide Formen liefern denselben Vektor; die Projektionsform ist
numerisch günstiger, da sie ein Skalarprodukt anstelle zweier
Kreuzprodukte erfordert.

**Charakterisierung als negativer Gradient**: Sei z: E → ℝ die
Einschränkung der Koordinatenfunktion (x, y, z) ↦ z auf E. z ist
linear auf E mit Gradient ∇_E z = v / ‖v‖ ∈ E_0. Damit ist

```
e_hat_fall(E) = −∇_E z / ‖∇_E z‖,
```

die Falllinie ist die normierte Richtung des steilsten Abfalls von z
auf E.

Wesentliche abgeleitete Größen:

- **Dachneigung entlang der Falllinie**: tan(α) = |⟨e_hat_fall, e_z⟩| /
  ‖e_hat_fall − ⟨e_hat_fall, e_z⟩ · e_z‖ — die Höhenänderung pro
  horizontalem Weg entlang der Falllinie ist exakt der
  Steigungs-Tangens (siehe `dachneigung`).
- **Höhenlinienrichtung**: jeder Einheitsvektor in E_0, der
  orthogonal zu e_hat_fall steht, hat z-Komponente 0 und liegt
  horizontal; das ist die Richtung der Höhenlinien (Niveaulinien
  von z auf E).

### Symbol-Konvention

Das Symbol für die Falllinie ist im gesamten Glossar **`e_hat_fall`**
(Einheitsvektor in S² ∩ E_0 mit ⟨e_hat_fall, e_z⟩ ≤ 0).

**Vorzeichenkonvention**: Aus der Definition folgt
`⟨e_hat_fall, e_z⟩ ≤ 0`, d. h. die Falllinie zeigt **nach unten**
(geometrische Bergab-Richtung). Diese Konvention ist bindend für
alle abgeleiteten Vorzeichen-Aussagen — insbesondere für die
Vorzeichen-Empfehlung der Bauteilachse eines Sparrens, die
**entgegen** `e_hat_fall` (bergauf, von Traufe zu Sparrenfirstpunkt)
zu wählen ist (siehe `bauteilachse`).

## Wohldefiniertheit

- **Existenz**: Für ⟨e_z, n_hat⟩ < 1 ist v = e_z − ⟨e_z, n_hat⟩ · n_hat ≠ 0,
  da e_z ≠ ⟨e_z, n_hat⟩ · n_hat (sonst wäre e_z parallel zu n_hat, also
  ⟨e_z, n_hat⟩ = 1). Damit ist die Division durch ‖v‖ wohldefiniert
  und e_hat_fall ∈ S².
- **Eindeutigkeit**: e_hat_fall ist als Lösung des Optimierungsproblems
  „minimiere ⟨e_hat, e_z⟩ unter e_hat ∈ E_0 ∩ S²" eindeutig bestimmt, da
  E_0 ∩ S² ein Großkreis auf S² ist und die Linearform ⟨·, e_z⟩
  auf einem Großkreis genau ein Minimum und ein Maximum hat
  (außer im entarteten Fall E_0 = e_z^⊥, der durch die
  Geneigtheits-Voraussetzung ausgeschlossen ist).
- **Lage in E**: e_hat_fall liegt in E_0, denn
  ⟨e_hat_fall, n_hat⟩ = −⟨v, n_hat⟩ / ‖v‖ und
  ⟨v, n_hat⟩ = ⟨e_z, n_hat⟩ − ⟨e_z, n_hat⟩ · ⟨n_hat, n_hat⟩ = 0 (für ‖n_hat‖ = 1).
- **Vorzeichenkonvention**: Die Wahl des negativen Vorzeichens
  liefert ⟨e_hat_fall, e_z⟩ = −⟨v, e_z⟩/‖v‖ = −‖v‖²/‖v‖ = −‖v‖ ≤ 0.
  Im Spezialfall α = π/2 (vertikale Ebene) wäre ⟨n_hat, e_z⟩ = 0 und
  ‖v‖ = 1, also e_hat_fall = −e_z; dieser Fall liegt jedoch außerhalb
  des Anwendungsbereichs für Dachflächen (`dachflaeche`-Bedingung 3:
  α < π/2).
- **Unabhängigkeit von der Normalenwahl**: Die Definition verwendet
  n_hat mit ⟨n_hat, e_z⟩ > 0; die Wahl ist eindeutig (siehe
  `dachflaeche`, äußere Normale). Die Vorzeichenwahl von n_hat
  ändert v nicht, da v in n_hat quadratisch eingeht.
- **Numerische Wohldefiniertheit**: Der Geneigtheits-Test ist ein
  Parallelitäts-Test n_hat ∥ e_z (horizontale Ebene) und wird nach
  HG-Konvention §4 über die Kreuzprodukt-Norm geführt: die Ebene ist
  geneigt genau dann, wenn ‖v‖ = ‖n_hat × e_z‖ = sin α > KOLLINEAR_EPS.
  Diese Sinus-Form ist nahe α = 0 gut konditioniert (anders als die
  Cosinus-Form 1 − ⟨e_z, n_hat⟩, die dort Auslöschung erleidet); die
  Division durch ‖v‖ ist damit numerisch sicher.
- **Entartung bei α = 0**: Bei einer horizontalen Ebene (n_hat = ±e_z)
  ist v = 0 und e_hat_fall ist nicht definiert; jeder horizontale
  Einheitsvektor in E_0 ist gleich „flach". Die Domänen-Schicht
  liefert in diesem Fall `Entartet.HorizontaleEbene`.
- **Nicht-Zirkularität**: Die Definition stützt sich nur auf
  `ebene`, `vektor`, `einheitsvektor` und `toleranzen`; sie kommt
  nicht in ihrer eigenen Definition vor.

## Erläuterung (nicht normativ)

Die Falllinie ist die geometrische Antwort auf die Frage „wohin
fließt das Wasser auf dieser geneigten Fläche?". Sie steht rechtwinklig
zu den Höhenlinien der Fläche und ist im Holzbau die
Bezugsrichtung für:

- den **Verlauf des Ortgangs** (siehe `ortgang`): die seitliche
  Begrenzung einer Dachfläche an einem Giebel verläuft in der
  Trägerebene parallel zur Falllinie;
- die **Sparrenrichtung**: ein Sparren liegt typisch entlang oder
  nahe der Falllinie der von ihm getragenen Dachfläche;
- die **Wasserführung** und Eindeckungsausrichtung (Ziegel,
  Schindeln werden quer zur Falllinie gelegt, sodass das Wasser
  entlang der Falllinie über die Eindeckung fließt);
- die **Definition der Dachneigung** als Steigungswinkel der
  Falllinie gegen die Horizontale (siehe `dachneigung`).

Die in der Geomatik gebräuchlichen Begriffe **Hangrichtung** und
**Aspekt** (engl. *aspect*) bezeichnen typisch nicht den
dreidimensionalen Vektor selbst, sondern dessen Azimut, also den
Winkel der horizontalen Projektion der Falllinie gemessen
gegen Norden im Uhrzeigersinn. Sie sind aus der Falllinie
ableitbar, aber nicht mit ihr identisch.

Die zur Falllinie rechtwinklige Richtung in derselben Ebene ist die
**Höhenlinienrichtung**; sie verläuft horizontal (z-Komponente
gleich Null) und ist im Spezialfall einer Dachfläche parallel zur
**Trauflinie**. Diese Begriffe werden in der App verwendet, sind
aber bisher nicht als eigenständige Glossareinträge geführt.

## Beziehungen

- **Oberbegriff**: `einheitsvektor`. Die Falllinie ist ein
  Einheitsvektor mit zwei zusätzlichen Lagebedingungen: er liegt in
  einer gegebenen Ebene und ist dort der Vektor mit minimaler
  z-Komponente.
- **Dual / komplementär**: **Höhenlinienrichtung** — der
  Einheitsvektor in derselben Ebene mit verschwindender
  z-Komponente; orthogonal zu e_hat_fall in E_0. Eigenständiger
  Glossareintrag folgt bei Bedarf.
- **Verwendungskontext**:
  - `dachneigung`: tan(α) ist der Quotient aus vertikaler und
    horizontaler Komponente der Falllinie.
  - `ortgang`: eine Polygonrandkante einer Dachfläche ist Ortgang
    genau dann, wenn ihr Einheits-Richtungsvektor mit der
    Falllinie der Dachfläche kollinear ist.
  - **Wasserführungs-Modellierung** (zukünftig): integraler Verlauf
    eines Tropfens auf der Dachoberfläche folgt stückweise der
    Falllinie der jeweils berührten Dachfläche.
- **Abgrenzung**:
  - **Höhenlinie** (`hoehenlinie`, eigener Eintrag folgt bei
    Bedarf): die zur Falllinie orthogonale Richtung in der Ebene;
    horizontal verlaufende Niveaulinie der z-Funktion auf E. Eine
    Höhenlinie ist eine **Linie** (Strecke oder Gerade), keine
    bloße Richtung; die Höhenlinienrichtung ist der zugehörige
    Einheitsvektor.
  - **Dachneigung** (`dachneigung`): der Steigungswinkel α der
    Falllinie gegenüber der Horizontalen. α ist ein Skalar
    (Winkel), die Falllinie ein Vektor (Richtung). Beide
    Begriffe sind eng verknüpft: die Falllinie trägt die volle
    Richtungsinformation, die Dachneigung extrahiert daraus den
    Steigungswinkel.
  - **Faserrichtung** (`faserrichtung`): Einheitsvektor entlang der
    Holzfaser eines Bauteils; trägt Materialachsen-Bedeutung, kein
    geometrischer Bezug zu einer Ebene.
  - **Hangrichtung / Aspekt** (Geomatik): Azimut der horizontalen
    Projektion der Falllinie. Nicht synonym, sondern abgeleitete
    skalare Größe.
  - **Dachgefälle**: in einigen Quellen für die Falllinie verwendet,
    in der Schweiz aber stärker mit der Flachdach-Abdichtungspraxis
    konnotiert (Gefälleeinlagen). Hier abgelehnt zugunsten von
    „Falllinie" für die Richtung und „Dachneigung" für den Winkel.

## Quellen

**Primär (normativ):**

- DIN ISO 80000-2:2022-08, „Größen und Einheiten – Teil 2: Mathematik",
  Abschnitt 2.
- DIN EN ISO 19107:2019, „Geographic information – Spatial schema",
  Abschnitt 6.

**Sekundär:**

- Bronstein, I. N.; Semendjajew, K. A.; Musiol, G.; Mühlig, H.:
  *Taschenbuch der Mathematik.* Kap. 6.2.4 und 3.5.
- Fischer, G.: *Lineare Algebra.* 19. Aufl., Springer Spektrum 2020,
  Kap. 6.2.
- Lignum (Hrsg.): *Lignatec — Geneigte Dächer in Holzbauweise.*
  Lignum, Zürich, aktuelle Auflage.
- Mönck, W.; Rug, W.: *Holzbau – Bemessung und Konstruktion.*
  16. Auflage, Beuth Verlag 2015.

**Korpus (nicht autoritativ):**

- Wikipedia, Lemma „Falllinie" (abgerufen 2026-05-08).
