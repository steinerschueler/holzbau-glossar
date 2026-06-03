---
id: first
benennung: First
synonyme: [Dachfirst, Firstkante, Firstlinie]
abgelehnte_benennungen: [Firstpfette, Firstziegel, Firstbalken, Höhe, "ridge", "ridgeline"]
oberbegriff: dachkante
begriffstyp: partitiv
voraussetzungen: [strecke, dachflaeche, polygon, ebene, vektor, toleranzen, dachkante]
abgrenzung_zu: [traufe, ortgang, grat, kehle, pultkante, firstpfette, firstziegel, firstabdeckung, dachhoehe]
status: entwurf
subglossar_pendant: notwendig
quellen_primär:
  - "SIA 232/1:2020 'Geneigte Dächer', Schweizerischer Ingenieur- und Architektenverein, Abschnitt 1 (Begriffe): First als oberste, horizontale Schnittkante zweier nach oben zusammenlaufender Dachflächen."
  - "DIN 1356-1:1995-02 'Bauzeichnungen – Teil 1', Abschnitt 5 (Darstellung von Dächern): First als horizontale obere Dachkante."
  - "DIN 18338:2019-09 'VOB Teil C: Dachdeckungs- und Dachabdichtungsarbeiten', Abschnitt 0 (Begriffe): First als oberste, dem Schließen der Dachdeckung dienende Dachkante."
  - "DIN EN 1991-1-3:2010-12 'Eurocode 1 – Schneelasten', Anhang A: First als horizontale Bezugslinie für Schneelastansätze auf Sattel- und Walmdächern."
quellen_sekundär:
  - "Mönck, W.; Rug, W.: Holzbau – Bemessung und Konstruktion. 16. Aufl., Beuth Verlag 2015, Kap. Dachformen."
  - "Gerner, M.: Fachwerk – Instandsetzung, Sanierung, Neubau. DVA, 7. Aufl. 2007, Glossar 'First'."
  - "Lignum (Hrsg.): Lignatec 'Geneigte Dächer in Holzbauweise', Lignum, Zürich, aktuelle Auflage."
quellenkonflikt: |
  Im Sprachgebrauch existieren mehrere Lesarten von „First":
  (a) **geometrisch**: First = Firstkante, also die Schnittkante
      zweier sich nach oben treffender Dachflächen.
  (b) **Bauteil Tragwerk**: Firstpfette = horizontaler Träger
      direkt unter der Firstkante.
  (c) **Bauteil Eindeckung**: Firstziegel/Firstabdeckung = die auf
      der Firstkante aufliegende Eindeckungsabdeckung.
  Normativ ist (a) am klarsten belegt (SIA 232/1, DIN 1356, DIN EN
  1991-1-3). **Festlegung dieses Glossars**: First bezeichnet hier
  ausschließlich die geometrische **Firstkante** im Sinne (a). Die
  Lesarten (b) und (c) werden in `abgrenzung_zu` als eigenständige,
  hier nicht selbständig definierte Bauteile geführt; sie werden bei
  Bedarf in späteren Einträgen ergänzt.

  Abgrenzung zu **Grat** und **Kehle**: First, Grat und Kehle sind
  alle drei Schnittkanten zweier Dachflächen. Der First unterscheidet
  sich dadurch, dass er näherungsweise horizontal verläuft und dass
  die beiden anliegenden Dachflächen nach oben zusammenlaufen (Λ,
  konvex — der First ist die lokal höchste Schneide). Grat und Kehle
  hingegen verlaufen geneigt; Kehle ist konkav (einspringend), Grat
  konvex (ausspringend). First und Grat teilen die Konvexität (nach
  oben zusammenlaufend); sie unterscheiden sich nur durch horizontal
  (First) vs. geneigt (Grat).
---

## Prosa-Definition

Ein **First** ist eine Dachkante, die als Schnittkante zweier
benachbarter Dachflächen auf der Schnittgerade ihrer Trägerebenen
liegt, näherungsweise horizontal verläuft und an der die beiden
Dachflächen nach oben zusammenlaufen (konvexe Firstschneide) — die
Flächen bilden ein nach oben gerichtetes Dach, dessen obere Schneide
der First ist.

## Mathematische Definition

Sei

- D_i = (E_i, P_i, n_{a,i}) und D_j = (E_j, P_j, n_{a,j}) zwei
  verschiedene Dachflächen im Sinne von `dachflaeche` mit
  i ≠ j,
- E_i und E_j nicht parallel, also E_i ∩ E_j eine Gerade
  g_{ij} ⊂ ℝ³ (Schnittgerade der Trägerebenen),
- F(P_i) ⊂ E_i und F(P_j) ⊂ E_j die berandeten abgeschlossenen
  Flächenstücke,
- e_z = (0, 0, 1)ᵀ die vertikale Achse,
- ε_W := Toleranzen.WINKEL_EPS die Winkeltoleranz,
- ε_L := Toleranzen.LAENGE_EPS die Längentoleranz.

Definiere die **gemeinsame Schnittstrecke** der beiden Dachflächen
als

```
s_{ij} := F(P_i) ∩ F(P_j).
```

Da E_i und E_j sich in der Geraden g_{ij} schneiden und beide F(P_•)
abgeschlossen und konvex-polygonal in ihren Ebenen sind, ist s_{ij}
ein abgeschlossenes (möglicherweise leeres oder einpunktiges)
Streckenstück auf g_{ij}. Sein Richtungs-Einheitsvektor sei

```
e_hat_{ij} := (Endpunkt − Anfangspunkt) / ‖Endpunkt − Anfangspunkt‖,
          falls ℓ(s_{ij}) > ε_L; andernfalls undefiniert.
```

Eine Schnittstrecke s_{ij} heißt **näherungsweise horizontal**,
wenn

```
|⟨e_hat_{ij}, e_z⟩| ≤ ε_W.
```

Eine näherungsweise horizontale, nicht-entartete Schnittstrecke s_{ij}
heißt **First** der Dachflächenfamilie 𝒟 genau dann, wenn die beiden
Dachflächen an ihr **nach oben zusammenlaufen** (konvexe Firstschneide,
Λ-Querschnitt) und beide äußeren Normalen nach oben weisen.

Die Bedingung „nach oben zusammenlaufen" ist — wie konvex/konkav bei
`grat`/`kehle` — über die **Lage der Flächenstücke** zu schärfen, nicht
über die Normalen allein: Ein First (Λ, Flächen fallen von der Kante
weg) und eine waagrechte Kehle/Rinne (V, Flächen steigen von der Kante
weg) besitzen dasselbe Normalenpaar und unterscheiden sich nur in der
Querlage ihrer Flächenstücke. Sei

```
w := (e_hat_{ij} × e_z) / ‖e_hat_{ij} × e_z‖   ∈ S²
```

die zur Firstkante orthogonale **horizontale** Querachse (wohldefiniert,
da s_{ij} horizontal ist, also ‖e_hat_{ij} × e_z‖ ≈ 1). Sei c_i ein
innerer Punkt (Flächenschwerpunkt) von F(P_i) und m ∈ s_{ij} ein
Kantenpunkt; die **signierte Querlage** ist τ_i := ⟨c_i − m, w⟩ (mit
τ_i · τ_j < 0). Dann ist s_{ij} ein **First** genau dann, wenn

```
1.  ℓ(s_{ij}) > ε_L  und  |⟨e_hat_{ij}, e_z⟩| ≤ ε_W   (horizontal)
2.  ⟨n_hat_{a,i}, w⟩ · sign(τ_i) > ε_W   und
    ⟨n_hat_{a,j}, w⟩ · sign(τ_j) > ε_W              (zusammenlaufend)
3.  ⟨n_{a,i}, e_z⟩ > 0   und   ⟨n_{a,j}, e_z⟩ > 0    (Normalen nach oben,
                                  Ausschluss senkrechter Wände).
```

Anschaulich kippen beide äußeren Normalen horizontal **nach außen**, zur
Querseite ihres eigenen Flächenstücks — die Flächen bilden ein nach oben
gerichtetes Dach (Λ), dessen Schneide der First ist. Kehrt sich das
Vorzeichen in (2) um (⟨n_hat_{a,i}, w⟩ · sign(τ_i) < −ε_W), so laufen die
Flächen nach oben auseinander: eine **waagrechte Kehle/Rinne**, kein
First.

Diese Definition ist **lokal** — jede Firstschneide wird für sich
erkannt; ein Dach mit mehreren Firsten (L-, T-, U-Grundriss, auch auf
verschiedenen Höhen) liefert alle Firste. Bedingung (2) ist pro
Flächenstück formuliert und damit unabhängig von der Reihenfolge der
beiden Dachflächen. Die Vereinigung aller so
identifizierten Schnittstrecken bildet, falls sie über gemeinsame
Eckpunkte zusammenhängt, die **Firstlinie** als Streckenzug; im
Regelfall (Sattel-, Walm-, Krüppelwalmdach) besteht sie aus genau
einer Strecke.

## Wohldefiniertheit

- **Existenz**: Bei einer Familie von Dachflächen mit mindestens
  einer horizontalen, nach oben zusammenlaufenden Schnittkante (z. B.
  Sattel-, Walm-, Krüppelwalmdach) existiert ein First. Bei einem
  Pultdach (m = 1) oder bei Dachflächenfamilien ohne gemeinsame
  horizontale Schnittstrecke existiert kein First — das ist baulich
  korrekt.
- **Mehrere Firste**: Da die Definition **lokal** ist (jede
  Firstschneide für sich), liefert ein Dach mit mehreren nach oben
  zusammenlaufenden horizontalen Schneiden — L-, T-, U-förmiger
  Grundriss, auch auf verschiedenen Höhen — korrekt **alle** als
  Firste; sie sind keine Entartung. Das ist der wesentliche Vorteil
  gegenüber einer globalen „höchste Kante"-Auswahl, die niedrigere
  Firste verfehlt hätte. Ein **Mansarddach** (oberer flacher Schenkel
  zusammenlaufend, unterer Knick auseinanderlaufend) liefert nur die
  obere, zusammenlaufende Schneide als First — der untere Knick läuft
  nach oben auseinander (waagrechte Kehle), ist also kein First.
- **Unabhängigkeit von der Indexwahl**: Bedingung (2) ist pro
  Flächenstück formuliert (je eine Ungleichung für i und j); ein
  Vertauschen i ↔ j benennt nur die beiden Ungleichungen um. Die
  Definition hängt nicht von der Reihenfolge der Dachflächen ab.
- **Konsistenz mit `dachkante`**: Ein First ist nach Konstruktion
  eine Schnittkante zweier Dachflächen, also eine Dachkante im
  Sinne von `dachkante` (Fall „Schnittkante").
- **Wohldefiniertheit der Querachse**: Da s_{ij} näherungsweise
  horizontal ist, ist e_hat_{ij} × e_z ≠ 0 und w wohldefiniert; die
  Querlagen τ_i, τ_j sind als Skalarprodukte von der Wahl der
  Repräsentation [a, b] vs. [b, a] unabhängig.
- **Nicht-Zirkularität**: Die Definition stützt sich nur auf
  `strecke`, `dachflaeche`, `polygon`, `ebene`, `vektor`,
  `toleranzen` und den bereits definierten Oberbegriff `dachkante`.

## Erläuterung (nicht normativ)

Der First ist die oberste, näherungsweise horizontale Linie eines
Sattel-, Walm- oder Krüppelwalmdaches. Geometrisch ist er die
Schnittkante zweier Dachflächen, die mit ihren äußeren Normalen nach
oben zusammenlaufen. Konstruktiv liegt unter dem First häufig die
**Firstpfette** (ein horizontaler Tragwerksbalken), und auf dem First
sitzt die **Firstabdeckung** der Eindeckung (Firstziegel oder
Firstblech).

Bei einem Pultdach gibt es keinen First, sondern eine **Pultkante**
(obere Polygonrandkante einer einzigen Dachfläche, an der keine
zweite Dachfläche anschließt) — siehe eigener Eintrag. Bei einem
Walmdach kommt zur First-Strecke (zwischen den beiden
Hauptdachflächen) die **Walmschnittkante** (zwischen Hauptdach und
Walmfläche) hinzu, die je nach Lage als kurzer First oder als Grat
klassifiziert wird.

## Beziehungen

- **Oberbegriff**: `dachkante`, Spezialfall „Schnittkante" mit
  zusätzlichen Lagebedingungen (näherungsweise horizontal, nach oben
  zusammenlaufend/konvex, beide Normalen mit positiver z-Komponente).
- **Geschwister-Begriffe** (andere Spezialisierungen von
  `dachkante`): `traufe`, `ortgang`, `grat`, `kehle`, `pultkante`.
- **Bestandteile (partitiv)**: Anfangspunkt und Endpunkt der
  Firstlinien-Strecke bzw. die Stützpunkte des Streckenzugs bei
  geknickter Firstlinie.
- **Abgrenzung**:
  - **Traufe** (`traufe`): untere, näherungsweise horizontale
    Randkante; ebenfalls horizontal, aber Polygonrandkante einer
    einzelnen Dachfläche statt zusammenlaufende Schnittkante zweier
    Flächen (und liegt unten statt oben).
  - **Ortgang** (`ortgang`): seitliche, geneigte Randkante; nicht
    näherungsweise horizontal.
  - **Grat** (eigener Eintrag folgt): geneigte konvexe
    Schnittkante zweier Dachflächen; First-ähnlich als Schnittkante,
    aber nicht horizontal.
  - **Kehle** (eigener Eintrag folgt): geneigte konkave
    Schnittkante zweier Dachflächen; einspringend statt
    ausspringend.
  - **Pultkante** (eigener Eintrag folgt): obere Polygonrandkante
    einer Pultdachfläche; ebenfalls oberste, aber Randkante statt
    Schnittkante (nur eine Dachfläche beteiligt).
  - **Firstpfette**: Tragwerksbalken unter dem First; Bauteil, nicht
    Kante. Hier nicht definiert.
  - **Firstziegel / Firstabdeckung**: Eindeckungselemente auf dem
    First; Materialbauteile, nicht Kante. Hier nicht definiert.
  - **Dachhöhe**: vertikaler Abstand zwischen Trauf- und
    Firsthöhe; ein Maß, keine Kante.

## Implementierungshinweis

Datentyp (Domänen-Schicht, Kotlin, Schicht `domain.bauteil`):

```
sealed class First : Dachkante() {

    data class Regulaer(
        override val polylinie: Streckenzug,
        val dachflaecheA: Dachflaeche,
        val dachflaecheB: Dachflaeche
    ) : First()

    sealed class Entartet : First() {
        object Nullkante : Entartet()
        object NichtIdentifizierbar : Entartet()
    }
}
```

Klassifikations-Prädikat in `DachkanteOps.kt`:

```
fun istFirst(
    s: Strecke,
    dA: Dachflaeche,
    dB: Dachflaeche,
    eps_W: Double = Toleranzen.WINKEL_EPS,
    eps_L: Double = Toleranzen.LAENGE_EPS
): Boolean {
    // 1. s liegt im gemeinsamen Polygonbereich von dA und dB
    if (!liegtImSchnitt(s, dA, dB, eps_L)) return false
    // 2. ℓ(s) > eps_L
    if (s.laenge() <= eps_L) return false
    // 3. s ist näherungsweise horizontal
    val sHat = s.einheitsRichtung().werteOder { return false }
    if (abs(sHat dot Vektor.E_Z) > eps_W) return false
    // 4. Beide äußeren Normalen weisen mit positiver z-Komponente nach oben
    val nA = dA.aeussereNormale.normiert().werteOder { return false }
    val nB = dB.aeussereNormale.normiert().werteOder { return false }
    if ((nA dot Vektor.E_Z) <= 0.0) return false
    if ((nB dot Vektor.E_Z) <= 0.0) return false
    // 5. Nach oben zusammenlaufend (konvex), lokal — kein globales z-Maximum:
    //    pro Fläche neigt sich die äußere Normale horizontal nach außen, zur
    //    Querseite ihres Flächenstücks. Reine Normalen trennen den First
    //    nicht von einer waagrechten Kehle/Rinne (= beide nach innen).
    val w = (sHat cross Vektor.E_Z).normiert().werteOder { return false }
    val m = s.mittelpunkt()
    val tauA = (dA.schwerpunkt() - m) dot w
    val tauB = (dB.schwerpunkt() - m) dot w
    val aussenA = (nA dot w) * sign(tauA) > eps_W
    val aussenB = (nB dot w) * sign(tauB) > eps_W
    return aussenA && aussenB
}
```

- **Einheit**: alle Koordinaten in mm (Double), Längen in mm.
- **Invarianten** (in Factory prüfen, niemals Exception):
  1. ℓ(polylinie) > Toleranzen.LAENGE_EPS — sonst `Entartet.Nullkante`.
  2. Jede Teilstrecke der Polylinie liegt im Schnittbereich
     F(P_A) ∩ F(P_B) der beiden anliegenden Dachflächen.
  3. Jede Teilstrecke ist näherungsweise horizontal:
     |e_hat · e_z| ≤ Toleranzen.WINKEL_EPS.
  4. Beide äußeren Normalen weisen mit positiver z-Komponente nach
     oben: n_{a,A} · e_z > 0 und n_{a,B} · e_z > 0.
  5. Nach oben zusammenlaufend (Bedingung (2)): pro Fläche
     ⟨n_hat_{a,i}, w⟩ · sign(τ_i) > Toleranzen.WINKEL_EPS, mit
     w = horizontale Querachse (s_hat × e_z) und τ_i = signierte
     Querlage des Flächenschwerpunkts. Lokal — kein Bezug auf andere
     Schnittstrecken.
- **Edge Cases**:
  - **Nullkante**: ℓ ≤ Toleranzen.LAENGE_EPS → `Entartet.Nullkante`.
  - **NichtIdentifizierbar**: ⟨n_hat_{a,i}, w⟩ · sign(τ_i) im
    Toleranzband [−ε_W, +ε_W] für eine der Flächen (Flächenstück kaum
    quer geneigt) oder gegenläufig (eine Fläche nach außen, die andere
    nach innen — weder First noch waagrechte Kehle) →
    `Entartet.NichtIdentifizierbar`. Eine durchgehend konkave
    horizontale Schneide (beide < −ε_W) ist eine **waagrechte
    Kehle/Rinne**, kein First.
  - **Parallele Trägerebenen** (E_A ∥ E_B): Schnittgerade existiert
    nicht; Definition liefert kein Element →
    `Entartet.NichtIdentifizierbar`.
  - **Geknickter First** (z. B. bei polygonal abgeknicktem
    Dachgrundriss): zulässig durch Streckenzug-Modellierung; jede
    Teilstrecke wird einzeln klassifiziert.
- **Abgeleitete Operationen**:
  - `fun firstlaenge(): Double` (mm) = ℓ(polylinie).
  - `fun firstlinie(): Streckenzug` = polylinie.
  - `fun firsthoehe(): Double` (mm) = mittlere z-Koordinate der
    Polylinie (Bezugsmaß für die Dachhöhe).

## Quellen

**Primär (normativ):**

- SIA 232/1:2020, „Geneigte Dächer", Schweizerischer Ingenieur- und
  Architektenverein, Abschnitt 1.
- DIN 1356-1:1995-02, „Bauzeichnungen – Teil 1: Arten, Inhalte und
  Grundregeln der Darstellung", Abschnitt 5.
- DIN 18338:2019-09, „VOB Teil C: Dachdeckungs- und
  Dachabdichtungsarbeiten", Abschnitt 0.
- DIN EN 1991-1-3:2010-12, „Eurocode 1: Einwirkungen auf Tragwerke –
  Teil 1-3: Schneelasten", Anhang A.

**Sekundär:**

- Mönck, W.; Rug, W.: *Holzbau – Bemessung und Konstruktion.*
  15. Auflage, Beuth Verlag 2015.
- Gerner, M.: *Fachwerk – Instandsetzung, Sanierung, Neubau.* DVA,
  7. Auflage 2007.
- Lignum (Hrsg.): *Lignatec — Geneigte Dächer in Holzbauweise.*
  Lignum, Zürich, aktuelle Auflage.

**Korpus (nicht autoritativ):**

- Wikipedia, Lemma „Dachfirst" (abgerufen 2026-05-08).
