---
id: schnittgerade
benennung: Schnittgerade
kurz: "Eine Schnittgerade ist die gerade Linie, die entsteht, wo zwei flache Flächen aufeinandertreffen — wie die Kante, an der zwei Dachflächen am First zusammenstossen."
synonyme: ["Schnittlinie zweier Ebenen", "Verschneidungsgerade", "Schnittachse zweier Ebenen"]
abgelehnte_benennungen: [Schnittkante, Verschneidung, Schnitt, "intersection line", "line of intersection"]
oberbegriff: gerade
begriffstyp: generisch
voraussetzungen: [gerade, ebene, vektor, einheitsvektor, punkt, toleranzen]
abgrenzung_zu: [gerade, strecke, schnittpunkt, verschneidung, halbgerade]
status: entwurf
subglossar_pendant: notwendig
quellen_primär:
  - "DIN ISO 80000-2:2022-08, 'Größen und Einheiten – Teil 2: Mathematik', Abschnitt 2 (Geometrie und Vektoren), Symbole und Bezeichnungen für die Schnittmenge geometrischer Objekte."
quellen_sekundär:
  - "Bronstein, I. N.; Semendjajew, K. A.; Musiol, G.; Mühlig, H.: Taschenbuch der Mathematik. Edition Harri Deutsch, aktuelle Auflage, Kap. 3.5.2 'Ebenen im Raum', Abschnitt 'Schnittgerade zweier Ebenen'."
  - "Bär, C.: Elementargeometrie. Springer Spektrum, Kap. 5 'Ebenen im dreidimensionalen Raum'."
  - "Fischer, G.: Lineare Algebra. 19. Aufl., Springer Spektrum 2020, Kap. 1 'Affine Geometrie' (Schnittlagen affiner Unterräume)."
  - "de Berg, M.; Cheong, O.; van Kreveld, M.; Overmars, M.: Computational Geometry – Algorithms and Applications. 3. Aufl., Springer 2008, Kap. 1 (geometrische Primitive) und Anhang (numerisch stabile Berechnung von Ebenenschnitten)."
quellenkonflikt: |
  Es liegt kein Quellenkonflikt vor. Holzbau-Normen (DIN 1052,
  DIN EN 1995-1-1, SIA 265, SIA 232/1) verwenden den Begriff
  „Schnittgerade" oder „Schnittlinie" als gegeben, ohne ihn
  axiomatisch zu definieren; sie verweisen auf die elementare
  analytische Geometrie. DIN ISO 80000-2 verzeichnet das Symbol
  ∩ für die Schnittmenge, definiert die Schnittgerade jedoch nicht
  formal. Eigene Festlegung: die Schnittgerade zweier Ebenen E₁ und
  E₂ ist die Punktmenge E₁ ∩ E₂, sofern die beiden Ebenennormalen
  linear unabhängig sind; dann ist E₁ ∩ E₂ eine Gerade im Sinne von
  `gerade`. Diese Festlegung ist konsistent mit Bronstein, Bär,
  Fischer und de Berg/Cheong.

  Vorzeichen-/Orientierungsfrage: Das Kreuzprodukt v = n_hat₁ × n_hat₂ ist
  antisymmetrisch in der Reihenfolge der beiden Ebenen
  (n_hat₁ × n_hat₂ = −(n_hat₂ × n_hat₁)). Als **Gerade im Sinne von `gerade`** ist
  die Schnittgerade ungerichtet — beide Reihenfolgen liefern
  dieselbe Punktmenge. Wo eine Tangentenrichtung ausgezeichnet werden
  muss (z. B. zur Klassifikation von Grat vs. Kehle, vgl. `hg_grat.md`,
  `hg_kehle.md`), wird die Reihenfolge (E₁, E₂) durch die Polygon-
  Umlaufrichtung der zuerst genannten Dachfläche fixiert; diese
  Konvention ist Bestandteil der Aufrufer, nicht der Schnittgerade
  selbst.
---

## Prosa-Definition

Eine **Schnittgerade** ist eine Gerade, die als Schnittmenge zweier
Ebenen E₁ und E₂ entsteht und damit zugleich in beiden Ebenen liegt;
sie existiert genau dann, wenn die Normalen der beiden Ebenen linear
unabhängig sind, das heißt wenn die Ebenen weder identisch noch
parallel disjunkt sind.

## Mathematische Definition

Sei

- E₁ = (p₁, n_hat₁) und E₂ = (p₂, n_hat₂) zwei Ebenen im Sinne von `ebene`
  in Hesse-Normalform, also mit normierten Normalen ‖n_hat₁‖ = ‖n_hat₂‖ = 1
  und vorzeichenbehafteten Ursprungs­abständen
  d₁:= ⟨n_hat₁, p₁⟩ und d₂:= ⟨n_hat₂, p₂⟩ (in mm),
- ε_K:= Toleranzen.KOLLINEAR_EPS die Kollinearitätstoleranz,
- ε_L:= Toleranzen.LAENGE_EPS die Längentoleranz.

**Existenzbedingung.** Die Schnittgerade existiert genau dann, wenn

```
‖ n_hat₁ × n_hat₂ ‖ > ε_K                                             (E)
```

(Normalen nicht kollinear).

**Richtungsvektor.** Unter Bedingung (E) ist

```
v:= n_hat₁ × n_hat₂ ∈ ℝ³ \ {0},
t_hat:= v / ‖v‖    ∈ S².
```

**Stützpunkt.** Unter Bedingung (E) ist

```
x₀:= (d₁ · (n_hat₂ × t_hat)  +  d₂ · (t_hat × n_hat₁)) / ‖v‖             (S)
```

ein Punkt mit ⟨n_hat₁, x₀⟩ = d₁ und ⟨n_hat₂, x₀⟩ = d₂, also x₀ ∈ E₁ ∩ E₂.

**Schnittgerade.** Die durch (E₁, E₂) erzeugte **Schnittgerade**
g(E₁, E₂) ⊂ ℝ³ ist die Punktmenge

```
g(E₁, E₂):= E₁ ∩ E₂ = { x₀ + t · t_hat ∈ ℝ³ | t ∈ ℝ },
```

also die Gerade im Sinne von `gerade` mit Stützpunkt x₀ und
Richtungsvektor t_hat.

**Anwendung als Funktion.** Damit ist die Operation

```
Ebene × Ebene  ⟶  Gerade ∪ {Entartet.ParalleleEbenen,
                            Entartet.IdentischeEbenen}
```

mit

```
schnittGerade(E₁, E₂):=
  Entartet.IdentischeEbenen,    falls ‖n_hat₁ × n_hat₂‖ ≤ ε_K  und
                                       |⟨n_hat₁, p₂ − p₁⟩| ≤ ε_L
  Entartet.ParalleleEbenen,     falls ‖n_hat₁ × n_hat₂‖ ≤ ε_K  und
                                       |⟨n_hat₁, p₂ − p₁⟩| > ε_L
  g(E₁, E₂),                    sonst.
```

## Wohldefiniertheit

- **Existenz unter (E)**: Aus ‖n_hat₁ × n_hat₂‖ > ε_K folgt v ≠ 0 und damit
  t_hat ∈ S². Der durch (S) konstruierte Punkt x₀ erfüllt
  ⟨n_hat₁, x₀⟩ = d₁ und ⟨n_hat₂, x₀⟩ = d₂; das ist eine direkte Konsequenz
  der Identitäten

  ```
  ⟨n_hat₁, n_hat₂ × t_hat⟩ = ⟨t_hat, n_hat₁ × n_hat₂⟩ = ‖v‖,
  ⟨n_hat₁, t_hat × n_hat₁⟩ = 0,
  ⟨n_hat₂, n_hat₂ × t_hat⟩ = 0,
  ⟨n_hat₂, t_hat × n_hat₁⟩ = ⟨t_hat, n_hat₁ × n_hat₂⟩ · (−1)·(−1) = ‖v‖,
  ```
  d. h. ⟨n_hat₁, x₀⟩ = (d₁ · ‖v‖ + d₂ · 0) / ‖v‖ = d₁ und analog für n_hat₂.
  Also liegt x₀ in beiden Ebenen, und g(E₁, E₂) ist nicht-leer.
- **Eindeutigkeit als Punktmenge**: Da n_hat₁ und n_hat₂ linear unabhängig
  sind, ist E₁ ∩ E₂ ein eindimensionaler affiner Unterraum von ℝ³.
  Aus zwei verschiedenen, durch (E₁, E₂) konstruierten
  Repräsentanten (x₀, t_hat) und (x₀′, t_hat′) folgt deshalb
  g(x₀, t_hat) = g(x₀′, t_hat′) als Punktmenge — siehe Identitätsrelation
  in `hg_gerade.md`.
- **Vorzeichen der Richtung / Reihenfolge der Ebenen**: Beim
  Vertauschen von E₁ und E₂ wechselt v = n_hat₁ × n_hat₂ ↦ −v sein
  Vorzeichen, t_hat ↦ −t_hat. Die durch (S) konstruierte Position x₀ ist
  jedoch invariant: das Produkt d₁ · (n_hat₂ × t_hat) wird zu
  d₂ · (n_hat₁ × (−t_hat)) = d₂ · (t_hat × n_hat₁) und entsprechend; insgesamt bleibt
  x₀ unverändert. Als Gerade im Sinne von `gerade` gilt zudem
  g(p₀, v) = g(p₀, −v), so dass

  ```
  g(E₁, E₂) = g(E₂, E₁)   als Punktmenge.
  ```

  Die Schnittgerade ist als geometrisches Objekt in der Reihenfolge
  der beiden erzeugenden Ebenen **symmetrisch**. Wo eine
  Tangenten­orientierung benötigt wird, muss der Aufrufer eine
  Reihenfolge fixieren (siehe `hg_grat.md`, `hg_kehle.md`).
- **Disjunktheit der Entartungen**: Die Bedingung
  ‖n_hat₁ × n_hat₂‖ ≤ ε_K ist äquivalent zu „n_hat₁ und n_hat₂ kollinear (parallel
  oder antiparallel)". In diesem Fall sind die Trägerebenen entweder
  identisch (gleiche Hesse-Distanz, geprüft durch
  |⟨n_hat₁, p₂ − p₁⟩| ≤ ε_L) oder echt parallel und disjunkt. Beide
  Fälle sind disjunkt; die Fallunterscheidung in `schnittGerade`
  ist erschöpfend.
- **Konsistenz mit `gerade`**: Unter (E) erfüllt (x₀, t_hat) die
  Invarianten von `gerade` (t_hat ist Einheitsvektor, alle Komponenten
  finit). Die Schnittgerade ist damit eine Gerade im Sinne des
  Glossareintrags `gerade`.
- **Nicht-Zirkularität**: Die Definition stützt sich nur auf
  `gerade`, `ebene`, `vektor`, `einheitsvektor`, `punkt` und
  `toleranzen`; alle diese Begriffe sind zuvor definiert.

## Erläuterung (nicht normativ)

Die Schnittgerade ist das geometrische Standardobjekt für jede
Verschneidung zweier ebener Bauteilflächen oder Bezugsebenen. Im
Holzbau tritt sie als geometrischer Träger in mindestens drei
zentralen Rollen auf:

- als geometrischer Träger des **Firsts** (`first`): Schnittgerade
  zweier Dachflächen-Trägerebenen, deren Schnittstrecke näherungsweise
  horizontal in der höchsten gemeinsamen Lage liegt;
- als geometrischer Träger des **Grats** (`grat`): Schnittgerade
  zweier Dachflächen-Trägerebenen, deren Schnittstrecke geneigt und
  konvex (ausspringend) verläuft;
- als geometrischer Träger der **Kehle** (`kehle`): Schnittgerade
  zweier Dachflächen-Trägerebenen, deren Schnittstrecke geneigt und
  konkav (einspringend) verläuft.

Allgemein ist die Schnittgerade die Trägergerade jeder Verschneidung
zweier ebener Bauteilflächen — Wand zu Dach (Anschnitt am Wandkopf),
Wand zu Wand (Innen- oder Außenecke), Dachfläche zu Schalung etc.
Das tatsächliche Bauteil-Resultat ist in jedem Fall ein endliches
Streckenstück auf dieser Schnittgerade, beschnitten auf den
gemeinsamen Polygonbereich der beiden anliegenden Flächen.

Anschauliche Konstruktion (S): Der Term n_hat₂ × t_hat steht in E₁ orthogonal
zur Schnittgerade (da er auf t_hat und auf n_hat₂ orthogonal steht und t_hat
in E₁ liegt); analog steht t_hat × n_hat₁ in E₂ orthogonal zur
Schnittgerade. Die Linearkombination mit den Koeffizienten d₁ und d₂
(skaliert mit 1/‖v‖) liefert genau jenen Punkt auf der Schnittgerade,
dessen Stützung in der durch n_hat₁ und n_hat₂ aufgespannten Ebene liegt —
geometrisch der Lotfußpunkt vom Ursprung auf die Schnittgerade.

## Beziehungen

- **Oberbegriff**: `gerade`. Jede Schnittgerade IST eine Gerade
  (eindimensionaler affiner Unterraum von ℝ³). Die Schnittgerade
  trägt zusätzlich die Information ihrer beiden Erzeuger-Ebenen,
  die für die Klassifikation nachgelagerter Bauteilrollen (First,
  Grat, Kehle) gebraucht wird.
- **Erzeuger (Komponenten der Erzeugung)**: zwei Ebenen E₁, E₂ im
  Sinne von `ebene` mit linear unabhängigen Normalen.
- **Spezialisierungen / Rollen**: Die geometrischen Träger von
  `first`, `grat` und `kehle` sind jeweils Schnittgeraden zweier
  Dachflächen-Trägerebenen, die durch zusätzliche Lagebedingungen
  (Neigung, Konvexität, Höhenmaximum) zu Dachkanten klassifiziert
  werden.
- **Abgrenzung**:
  - **Gerade** (`gerade`): allgemein. Jede Schnittgerade ist eine
    Gerade, aber nicht jede Gerade ist eine Schnittgerade einer
    konkret gegebenen Ebenen­paarung. Eine als Schnittgerade
    klassifizierte Gerade trägt die Erzeuger-Information mit sich.
  - **Strecke** (`strecke`): endlicher Ausschnitt einer Geraden
    zwischen zwei Endpunkten. Im Holzbau wird die Schnittgerade
    typischerweise auf den gemeinsamen Polygonbereich zweier
    Dachflächen beschnitten; das Ergebnis ist eine Strecke (oder
    ein Streckenzug), nicht die ganze Schnittgerade.
  - **Schnittpunkt**: Schnitt einer Geraden mit einer Ebene oder
    dreier Ebenen — nulldimensionales Ergebnis, keine Gerade.
    Eigener Folge-Eintrag möglich.
  - **Verschneidung** (Operation): allgemeiner Begriff für jede
    Schnitt­operation zwischen geometrischen Objekten. Die
    Schnittgerade ist eine **spezielle** Verschneidung (Ebene ∩
    Ebene → Gerade). Andere Verschneidungen (Polygon ∩ Polygon,
    Strecke ∩ Ebene) liefern andere Ergebnis­typen.
  - **Halbgerade** (`halbgerade`): einseitig begrenzter Ausschnitt
    einer Geraden. Die Schnittmenge zweier Ebenen ist niemals eine
    Halbgerade, sondern stets unbegrenzt zweiseitig.

## Quellen

**Primär (normativ):**

- DIN ISO 80000-2:2022-08, „Größen und Einheiten – Teil 2:
  Mathematik", Abschnitt 2.

**Sekundär:**

- Bronstein, I. N.; Semendjajew, K. A.; Musiol, G.; Mühlig, H.:
  *Taschenbuch der Mathematik.* Edition Harri Deutsch, aktuelle
  Auflage, Kap. 3.5.2.
- Bär, C.: *Elementargeometrie.* Springer Spektrum, Kap. 5.
- Fischer, G.: *Lineare Algebra.* 19. Aufl., Springer Spektrum 2020.
- de Berg, M.; Cheong, O.; van Kreveld, M.; Overmars, M.:
  *Computational Geometry – Algorithms and Applications.* 3. Aufl.,
  Springer 2008.

**Korpus (nicht autoritativ):**

- Wikipedia, Lemma „Schnittgerade" (abgerufen 2026-05-08).
