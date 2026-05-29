---
id: traufe
benennung: Traufe
synonyme: [Traufkante, Trauflinie, Tropfkante]
abgelehnte_benennungen: [Traufseite, Traufbereich, Dachrinne, Rinneneinhang, "eaves", "eaves edge"]
oberbegriff: dachkante
begriffstyp: partitiv
voraussetzungen: [strecke, dachflaeche, polygon, vektor, toleranzen, dachkante]
abgrenzung_zu: [first, ortgang, grat, kehle, pultkante, dachrinne, traufseite, traufbereich, dachueberstand]
status: entwurf
subglossar_pendant: notwendig
quellen_primär:
  - "SIA 232/1:2020 'Geneigte Dächer', Schweizerischer Ingenieur- und Architektenverein, Abschnitt 1 (Begriffe): Traufe als untere, wasserabführende Begrenzungskante einer Dachfläche."
  - "DIN 1356-1:1995-02 'Bauzeichnungen – Teil 1', Abschnitt 5 (Darstellung von Dächern): Traufe als horizontale untere Dachkante."
  - "DIN 18338:2019-09 'VOB Teil C: Dachdeckungs- und Dachabdichtungsarbeiten', Abschnitt 0 (Begriffe): Traufe als untere, dem Niederschlagsabfluss dienende Dachkante."
  - "DIN EN 1991-1-3:2010-12 'Eurocode 1 – Schneelasten', Anhang A (Geometrische Bezugsgrößen): Trauflinie als horizontale Bezugslinie für Schneelastansätze."
quellen_sekundär:
  - "Mönck, W.; Rug, W.: Holzbau – Bemessung und Konstruktion. 16. Aufl., Beuth Verlag 2015, Kap. Dachformen."
  - "Gerner, M.: Fachwerk – Instandsetzung, Sanierung, Neubau. DVA, 7. Aufl. 2007, Glossar 'Traufe'."
  - "Lignum (Hrsg.): Lignatec 'Geneigte Dächer in Holzbauweise', Lignum, Zürich, aktuelle Auflage."
quellenkonflikt: |
  Im Sprachgebrauch existieren drei Lesarten von „Traufe":
  (a) **eng/geometrisch**: Traufe = Trauf**kante**, also die untere
      Begrenzungslinie einer Dachfläche.
  (b) **bauteilbezogen**: Traufe = der Traufbereich, also der untere
      Dachflächen-Streifen mit Traufbohle, Rinneneinhang, Stirnbrett.
  (c) **lagebezogen**: Traufseite = jene Gebäudeseite, deren obere
      Wand parallel zur Trauflinie verläuft, im Gegensatz zur Giebel-
      seite.
  Normativ ist (a) am klarsten belegt (SIA 232/1, DIN 1356, DIN EN
  1991-1-3). DIN 18338 verwendet teilweise (b) im Leistungsbereich.
  **Festlegung dieses Glossars**: Traufe bezeichnet hier ausschließlich
  die geometrische **Traufkante** im Sinne (a). Die Lesarten (b) und
  (c) werden in `abgrenzung_zu` als eigenständige, hier nicht
  selbständig definierte Begriffe (`traufseite`, `traufbereich`)
  geführt; sie werden bei Bedarf in späteren Einträgen ergänzt.
---

## Prosa-Definition

Eine **Traufe** ist eine Dachkante einer geneigten Dachfläche, die
vollständig im Rand des Dachflächen-Polygons liegt, näherungsweise
horizontal verläuft und unter allen näherungsweise horizontalen
Polygonrandkanten dieser Dachfläche die niedrigste mittlere Höhe
besitzt; sie ist diejenige Kante, an der das von der Dachfläche
abfließende Niederschlagswasser die Dachfläche verlässt.

## Mathematische Definition

Sei

- D = (E, P, n_a) eine Dachfläche im Sinne von `dachflaeche` mit
  Trägerebene E, Umrisspolygon P = (v₁, …, v_k) und äußerer
  Normale n_a,
- (e₁, …, e_k) die zyklische Folge der Polygonrandkanten
  e_i := [v_i, v_{i+1}], v_{k+1} := v_1,
- e_z = (0, 0, 1)ᵀ die vertikale Achse,
- ε_W := Toleranzen.WINKEL_EPS die Winkeltoleranz,
- für eine Strecke s = [a, b] der **Höhenmittelwert**
  ```
  z_bar(s) := ½ · (a_z + b_z)
  ```
  und der **Horizontalitätsmaß**
  ```
  h(s) := |⟨e_hat(s), e_z⟩|       mit  e_hat(s) := (b − a) / ‖b − a‖.
  ```

Eine Polygonrandkante e_i heißt **näherungsweise horizontal**, wenn

```
h(e_i) ≤ ε_W.
```

Die Menge der näherungsweise horizontalen Randkanten von D sei

```
H(D) := { e_i | h(e_i) ≤ ε_W,  i = 1, …, k }.
```

Eine Strecke t ⊂ ℝ³ heißt **Traufe** der Dachfläche D genau dann,
wenn

1. t ∈ H(D), also t ist eine näherungsweise horizontale Polygonrand-
   kante von D, und
2. t hat unter allen Elementen von H(D) die niedrigste mittlere Höhe,
   d. h.
   ```
   z_bar(t) = min { z_bar(e) | e ∈ H(D) },
   ```
   ausgewertet mit Toleranz Toleranzen.LAENGE_EPS auf der Vertikalen
   (mehrere Kanten gleicher Mindesthöhe sind zulässig und werden
   gemeinsam als Traufe geführt).

Die Vereinigung aller so identifizierten Strecken bildet, falls sie
über gemeinsame Eckpunkte zusammenhängt, die **Trauflinie** als
Streckenzug; im Regelfall (Sattel-, Walm-, Pultdach mit gerader
Traufseite) besteht sie aus genau einer Strecke.

## Wohldefiniertheit

- **Existenz**: Bei einer geneigten Dachfläche (α > 0) hat jeder
  Polygonrand mindestens eine Kante mit niedrigster mittlerer Höhe,
  da F(P) kompakt und ∂F(P) endlich ist. Ist mindestens eine
  Polygonrandkante näherungsweise horizontal — was bei Sattel-,
  Walm-, Pultdächern aus der Konstruktion folgt —, so ist H(D) ≠ ∅
  und das Minimum in Bedingung 2 wird angenommen. Bei Flachdächern
  (α = 0) liegen alle Randkanten in einer horizontalen Ebene und
  haben dieselbe mittlere Höhe; in diesem Sonderfall ist die Traufe
  nicht eindeutig identifizierbar (siehe `Entartet.NichtIdentifizierbar`).
- **Eindeutigkeit**: Bei einer geneigten Dachfläche mit eindeutiger
  unterer Polygonseite (was im Holzbau die Regel ist) ist die Traufe
  als Strecke oder zusammenhängender Streckenzug eindeutig bestimmt.
  Bei Sonderformen (z. B. Krüppelwalm mit zwei gleichhohen unteren
  Kanten) liefert die Definition mehrere gleichberechtigte Strecken,
  die gemeinsam die Trauflinie bilden — das ist gewollt.
- **Unabhängigkeit von der Polygon-Parametrisierung**: Die Bedingungen
  hängen nur von der ungeordneten Streckenmenge { e_i } und ihren
  Höhenmittelwerten ab, nicht von der Wahl des Anfangsindex oder der
  Umlaufrichtung von P.
- **Konsistenz mit `dachkante`**: Eine Traufe ist nach Bedingung 1
  eine Randkante der Dachfläche D, also eine Dachkante im Sinne von
  `dachkante` (Fall „Randkante").
- **Nicht-Zirkularität**: Die Definition stützt sich nur auf
  `strecke`, `dachflaeche`, `polygon`, `vektor`, `toleranzen` und
  den bereits definierten Oberbegriff `dachkante`.

## Erläuterung (nicht normativ)

Die Traufe ist diejenige Kante, an der das Regenwasser von der
Dachfläche tropft — daher die Synonyme „Tropfkante" und
„Trauflinie". An ihr wird in der Regel die Dachrinne befestigt
(Anschluss über Rinnenhaken in der Traufbohle).

Geometrisch ist die Traufe bei einem normalen Sattel- oder Pultdach
eine einzige Strecke parallel zur xy-Ebene. Bei Walmdächern hat jede
der vier Dachflächen eine eigene Traufe (insgesamt vier
Trauflinien-Segmente, die zu einer geschlossenen umlaufenden
Trauflinie verbunden sein können). Bei Krüppelwalm- und Mansarddach-
Formen wird die untere Dachflächenkante mit der Walm- bzw. Knickkante
verknüpft; die Traufe bleibt jeweils die unterste horizontale
Randkante der jeweiligen Dachfläche.

Der **Dachüberstand** (Auskragung der Dachfläche über die Außenwand
hinaus) verschiebt die Traufkante horizontal nach außen, ändert aber
nicht ihre geometrische Identität — die Traufe bleibt die untere
Polygonrandkante der ausgekragten Dachfläche.

## Beziehungen

- **Oberbegriff**: `dachkante`, Spezialfall „Randkante" mit
  zusätzlicher Lagebedingung (näherungsweise horizontal, niedrigste
  mittlere Höhe).
- **Geschwister-Begriffe** (andere Spezialisierungen von Dachkante):
  `first`, `ortgang`, `grat`, `kehle`, `pultkante`.
- **Bestandteile (partitiv)**: Anfangspunkt und Endpunkt der
  Trauflinien-Strecke bzw. die Stützpunkte des Streckenzugs bei
  geknickter Trauflinie.
- **Abgrenzung**:
  - **First** (`first`): obere Schnittkante zweier nach oben
    zusammenlaufender Dachflächen; ebenfalls näherungsweise
    horizontal, aber höchste statt niedrigste Kante.
  - **Ortgang** (`ortgang`): seitliche, geneigte Randkante; nicht
    näherungsweise horizontal, schließt Bedingung 1 aus.
  - **Pultkante** (eigener Eintrag folgt): obere Randkante einer
    Pultdachfläche ohne anschließende zweite Dachfläche; horizontal,
    aber höchste statt niedrigste Kante.
  - **Traufseite**: Gebäudeseite, deren Wand parallel zur Trauflinie
    verläuft; ist eine Eigenschaft der Wand, nicht der Dachfläche.
    Hier nicht definiert.
  - **Traufbereich**: konstruktiver Detailbereich an der Traufe mit
    Traufbohle, Rinneneinhang, Stirnbrett; ist ein
    Bauteil-Aggregat, nicht eine Kante. Hier nicht definiert.
  - **Dachrinne**: am Traufbereich befestigtes Bauteil zur
    Wasserableitung; nicht Bestandteil der Dachfläche, sondern ein
    Anbauteil.
  - **Dachüberstand**: das ausgekragte Stück der Dachfläche jenseits
    der Außenwand; verschiebt die Trauflinie, ist aber selbst keine
    Kante.

## Implementierungshinweis

Datentyp (Domänen-Schicht, Kotlin, Schicht `domain.bauteil`):

```
sealed class Traufe : Dachkante() {

    data class Regulaer(
        override val polylinie: Streckenzug,
        val dachflaeche: Dachflaeche
    ) : Traufe()

    sealed class Entartet : Traufe() {
        object Nullkante : Entartet()
        object NichtIdentifizierbar : Entartet()
    }
}
```

Klassifikations-Prädikat in `DachkanteOps.kt`:

```
fun istTraufe(
    e: Strecke,
    d: Dachflaeche,
    eps_W: Double = Toleranzen.WINKEL_EPS,
    eps_L: Double = Toleranzen.LAENGE_EPS
): Boolean {
    // 1. e ist Polygonrandkante von d
    if (!d.umriss.enthaeltKante(e, eps_L)) return false
    // 2. e ist näherungsweise horizontal
    val eHat = e.einheitsRichtung().werteOder { return false }
    if (abs(eHat dot Vektor.E_Z) > eps_W) return false
    // 3. z_bar(e) ist Minimum unter allen näherungsweise horizontalen Polygonrandkanten
    val horizontale = d.umriss.kanten().filter { it.istHorizontal(eps_W) }
    val minZ = horizontale.minOf { it.hoehenMittelwert() }
    return abs(e.hoehenMittelwert() - minZ) <= eps_L
}
```

- **Einheit**: alle Koordinaten in mm (Double), Längen in mm.
- **Invarianten** (in Factory prüfen, niemals Exception):
  1. ℓ(polylinie) > Toleranzen.LAENGE_EPS — sonst `Entartet.Nullkante`.
  2. Jede Teilstrecke der Polylinie ist Polygonrandkante der
     übergebenen Dachfläche.
  3. Jede Teilstrecke ist näherungsweise horizontal:
     |e_hat · e_z| ≤ Toleranzen.WINKEL_EPS.
  4. Mittlere z-Höhe jeder Teilstrecke ist gleich dem Minimum der
     mittleren z-Höhen aller näherungsweise horizontalen
     Polygonrandkanten der Dachfläche, mit Toleranz
     Toleranzen.LAENGE_EPS.
- **Edge Cases**:
  - **Nullkante**: ℓ ≤ Toleranzen.LAENGE_EPS → `Entartet.Nullkante`.
  - **NichtIdentifizierbar**: Keine näherungsweise horizontale
    Polygonrandkante existiert (z. B. bei einer reinen Schräg-
    konstruktion ohne horizontale Untergrenze) oder die untere
    Kante ist nicht eindeutig (z. B. Flachdach, α = 0) →
    `Entartet.NichtIdentifizierbar`.
  - **Geknickte Traufe**: zulässig durch Streckenzug-Modellierung
    (z. B. bei polygonal abgeknicktem Grundriss).
  - **Dachüberstand**: nicht relevant für die Klassifikation; die
    Traufkante wird auf dem effektiv vorliegenden Dachflächen-
    Polygon ausgewertet.
- **Abgeleitete Operationen**:
  - `fun trauflaenge(): Double` (mm) = ℓ(polylinie).
  - `fun trauflinie(): Streckenzug` = polylinie.
  - `fun anschlussRichtungDachrinne(): Vektor` = Tangentenrichtung
    der Trauflinie (Hilfsgröße für UI/Rendering).

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
  16. Auflage, Beuth Verlag 2015.
- Gerner, M.: *Fachwerk – Instandsetzung, Sanierung, Neubau.* DVA,
  7. Auflage 2007.
- Lignum (Hrsg.): *Lignatec — Geneigte Dächer in Holzbauweise.*
  Lignum, Zürich, aktuelle Auflage.

**Korpus (nicht autoritativ):**

- Wikipedia, Lemma „Traufe" (abgerufen 2026-05-08).
