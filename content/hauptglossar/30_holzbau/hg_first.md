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
theorie_pflichtig: required
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
  beide anliegenden Dachflächen mit ihrer äußeren Normalen nach oben
  zusammenlaufen (d. h. der First ist der höchste Punkt des
  gemeinsamen Bereichs). Grat und Kehle hingegen verlaufen geneigt;
  Kehle ist konkav (einspringend), Grat konvex (ausspringend).
---

## Prosa-Definition

Ein **First** ist eine Dachkante, die als Schnittkante zweier
benachbarter Dachflächen auf der Schnittgerade ihrer Trägerebenen
liegt, näherungsweise horizontal verläuft und im gemeinsamen
abgeschlossenen Polygonbereich der beiden Dachflächen die höchste
mittlere z-Höhe aller näherungsweise horizontalen Schnittkanten
besitzt.

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
ê_{ij} := (Endpunkt − Anfangspunkt) / ‖Endpunkt − Anfangspunkt‖,
          falls ℓ(s_{ij}) > ε_L; andernfalls undefiniert.
```

Eine Schnittstrecke s_{ij} heißt **näherungsweise horizontal**,
wenn

```
|⟨ê_{ij}, e_z⟩| ≤ ε_W.
```

Sei 𝒮 die Menge aller näherungsweise horizontalen, nicht-entarteten
Schnittstrecken zwischen Paaren von Dachflächen der betrachteten
Familie 𝒟,

```
𝒮 := { s_{ij} | i < j,  ℓ(s_{ij}) > ε_L,  |⟨ê_{ij}, e_z⟩| ≤ ε_W }.
```

Eine Schnittstrecke s_{ij} ∈ 𝒮 heißt **First** der Dachflächen-
familie 𝒟 genau dann, wenn ihr **Höhenmittelwert**

```
z̄(s_{ij}) := ½ · (a_z + b_z)   mit  s_{ij} = [a, b]
```

das Maximum unter allen Elementen von 𝒮 ist:

```
z̄(s_{ij}) = max { z̄(s) | s ∈ 𝒮 }.
```

Zusätzlich muss gelten, dass beide äußeren Normalen n_{a,i}, n_{a,j}
am First „nach oben zusammenlaufen", formal

```
⟨n_{a,i}, e_z⟩ > 0   und   ⟨n_{a,j}, e_z⟩ > 0
```

(beide Dachflächen sind nach oben geneigt; ausgeschlossen sind
Anschlüsse an senkrechte Wände). Die Vereinigung aller so
identifizierten Schnittstrecken bildet, falls sie über gemeinsame
Eckpunkte zusammenhängt, die **Firstlinie** als Streckenzug; im
Regelfall (Sattel-, Walm-, Krüppelwalmdach) besteht sie aus genau
einer Strecke.

## Wohldefiniertheit

- **Existenz**: Bei einer Familie von Dachflächen, die nach oben
  zusammenlaufen (z. B. Sattel-, Walm-, Krüppelwalmdach), enthält
  𝒮 mindestens ein Element, da die zentrale obere Schnittkante
  konstruktiv vorliegt. Bei einem Pultdach (m = 1) oder bei
  Dachflächenfamilien ohne gemeinsame Schnittstrecke ist 𝒮 = ∅, und
  ein First existiert nicht — das ist baulich korrekt.
- **Eindeutigkeit**: Bei einer Dachflächenfamilie mit eindeutiger
  oberster horizontaler Schnittkante (Regelfall im Holzbau) ist der
  First als Strecke oder zusammenhängender Streckenzug eindeutig
  bestimmt. Bei Sonderformen mit mehreren gleichhohen Schnittkanten
  (z. B. Mansarddach mit oberen und unteren Schnittkanten gleicher
  Höhe — geometrisch ungewöhnlich, aber konstruierbar) liefert die
  Definition mehrere gleichberechtigte Strecken; in diesem Fall
  sollte die Domänen-Schicht `Entartet.NichtIdentifizierbar`
  zurückgeben.
- **Unabhängigkeit von der Indexwahl**: Die Schnittstrecke s_{ij}
  ist symmetrisch in i und j; die Definition hängt nicht vom Vorzeichen
  oder der Reihenfolge ab.
- **Konsistenz mit `dachkante`**: Ein First ist nach Konstruktion
  eine Schnittkante zweier Dachflächen, also eine Dachkante im
  Sinne von `dachkante` (Fall „Schnittkante").
- **Wohldefiniertheit des Höhenvergleichs**: Die mittlere z-Höhe
  z̄(s) hängt nur von den Endpunkten der Strecke ab, nicht von
  der Wahl der Repräsentation [a, b] vs. [b, a].
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
  zusätzlichen Lagebedingungen (näherungsweise horizontal, höchste
  mittlere Höhe, beide Normalen mit positiver z-Komponente).
- **Geschwister-Begriffe** (andere Spezialisierungen von
  `dachkante`): `traufe`, `ortgang`, `grat`, `kehle`, `pultkante`.
- **Bestandteile (partitiv)**: Anfangspunkt und Endpunkt der
  Firstlinien-Strecke bzw. die Stützpunkte des Streckenzugs bei
  geknickter Firstlinie.
- **Abgrenzung**:
  - **Traufe** (`traufe`): untere, näherungsweise horizontale
    Randkante; ebenfalls horizontal, aber niedrigste statt höchste
    Kante und Polygonrandkante statt Schnittkante.
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
    alleSchnittstrecken: List<Strecke>,
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
    if (dA.aeussereNormale dot Vektor.E_Z <= 0.0) return false
    if (dB.aeussereNormale dot Vektor.E_Z <= 0.0) return false
    // 5. z̄(s) ist Maximum unter allen näherungsweise horizontalen Schnittstrecken
    val horizontaleSchnitte = alleSchnittstrecken.filter { it.istHorizontal(eps_W) }
    val maxZ = horizontaleSchnitte.maxOf { it.hoehenMittelwert() }
    return abs(s.hoehenMittelwert() - maxZ) <= eps_L
}
```

- **Einheit**: alle Koordinaten in mm (Double), Längen in mm.
- **Invarianten** (in Factory prüfen, niemals Exception):
  1. ℓ(polylinie) > Toleranzen.LAENGE_EPS — sonst `Entartet.Nullkante`.
  2. Jede Teilstrecke der Polylinie liegt im Schnittbereich
     F(P_A) ∩ F(P_B) der beiden anliegenden Dachflächen.
  3. Jede Teilstrecke ist näherungsweise horizontal:
     |ê · e_z| ≤ Toleranzen.WINKEL_EPS.
  4. Beide äußeren Normalen weisen mit positiver z-Komponente nach
     oben: n_{a,A} · e_z > 0 und n_{a,B} · e_z > 0.
  5. Mittlere z-Höhe jeder Teilstrecke ist gleich dem Maximum der
     mittleren z-Höhen aller näherungsweise horizontalen
     Schnittstrecken in der gesamten Dachflächenfamilie, mit
     Toleranz Toleranzen.LAENGE_EPS.
- **Edge Cases**:
  - **Nullkante**: ℓ ≤ Toleranzen.LAENGE_EPS → `Entartet.Nullkante`.
  - **NichtIdentifizierbar**: Keine eindeutig höchste horizontale
    Schnittkante (z. B. zwei gleichhohe Schnittkanten in
    unterschiedlichen Dachbereichen) → `Entartet.NichtIdentifizierbar`.
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
