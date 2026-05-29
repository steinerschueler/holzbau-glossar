---
id: ortgang
benennung: Ortgang
synonyme: [Ortgangkante, Giebelkante, "seitliche Dachkante"]
abgelehnte_benennungen: [Ortbrett, Windbrett, Ortgangbrett, Giebel, Giebelseite, "rake", "verge", "gable edge"]
oberbegriff: dachkante
begriffstyp: partitiv
voraussetzungen: [strecke, dachflaeche, polygon, vektor, toleranzen, dachkante]
abgrenzung_zu: [traufe, first, grat, kehle, pultkante, ortbrett, windbrett, giebel, giebelseite, falllinie]
status: entwurf
subglossar_pendant: notwendig
quellen_primär:
  - "SIA 232/1:2020 'Geneigte Dächer', Schweizerischer Ingenieur- und Architektenverein, Abschnitt 1 (Begriffe): Ortgang als seitliche Begrenzungskante einer Dachfläche an einer Giebelwand."
  - "DIN 1356-1:1995-02 'Bauzeichnungen – Teil 1', Abschnitt 5 (Darstellung von Dächern): Ortgang als geneigte seitliche Dachkante."
  - "DIN 18338:2019-09 'VOB Teil C: Dachdeckungs- und Dachabdichtungsarbeiten', Abschnitt 0 (Begriffe): Ortgang als seitliche, dem Giebel zugeordnete Dachkante."
quellen_sekundär:
  - "Mönck, W.; Rug, W.: Holzbau – Bemessung und Konstruktion. 16. Aufl., Beuth Verlag 2015, Kap. Dachformen."
  - "Gerner, M.: Fachwerk – Instandsetzung, Sanierung, Neubau. DVA, 7. Aufl. 2007, Glossar 'Ortgang'."
  - "Lignum (Hrsg.): Lignatec 'Geneigte Dächer in Holzbauweise', Lignum, Zürich, aktuelle Auflage."
quellenkonflikt: |
  Im Sprachgebrauch existieren mehrere Lesarten von „Ortgang":
  (a) **geometrisch**: Ortgang = Ortgangkante, also die seitliche
      geneigte Begrenzungslinie einer Dachfläche an einer Giebelwand.
  (b) **bauteilbezogen**: Ortgang = der Ortgangbereich mit Ortbrett,
      Windbrett und Eindeckungsabschluss.
  Normativ ist (a) belegt (SIA 232/1, DIN 1356, DIN 18338). DIN 18338
  verwendet teilweise (b) im Leistungsbereich. **Festlegung dieses
  Glossars**: Ortgang bezeichnet hier ausschließlich die geometrische
  **Ortgangkante** im Sinne (a). Das Bauteil **Ortbrett** (auch
  „Windbrett", „Ortgangbrett") wird in `abgrenzung_zu` ausdrücklich
  abgegrenzt.

  Der Eintrag erfasst auch geneigte Giebel (z. B. bei abgewalmten
  Giebeln, Schräg-Giebeln); die in einigen Fachglossaren
  vorgeschlagene Sonderbenennung „Schrägortgang" wird hier nicht als
  separater Begriff geführt — die Definition ist allgemein genug,
  jeden Anschluss an einen Giebel zu erfassen, gleich ob die
  Giebelwand vertikal oder geneigt ist. Die Bedingung „liegt entlang
  der Falllinie der Dachfläche" ist die geometrische Charakterisierung,
  die unabhängig von der Giebelwand-Geometrie gilt.
---

## Prosa-Definition

Ein **Ortgang** ist eine Dachkante, die vollständig im Rand des
Polygons einer geneigten Dachfläche liegt, in der Trägerebene dieser
Dachfläche entlang der Falllinie verläuft (also in Richtung des
größten Gefälles bzw. dazu antiparallel) und an einer Giebelseite
des Gebäudes den seitlichen Abschluss der Dachfläche bildet.

## Mathematische Definition

Sei

- D = (E, P, n_a) eine geneigte Dachfläche im Sinne von
  `dachflaeche` mit Trägerebene E, Umrisspolygon P = (v₁, …, v_k),
  äußerer Normale n_a und Dachneigung α ∈ (0, π/2),
- (e₁, …, e_k) die zyklische Folge der Polygonrandkanten,
- e_z = (0, 0, 1)ᵀ die vertikale Achse,
- ε_W := Toleranzen.WINKEL_EPS die Winkeltoleranz.

Die **Falllinie** der Dachfläche D im Sinne von `hg_falllinie.md`
ist der eindeutige in E liegende Einheitsvektor mit minimaler
z-Komponente; mit der dort fixierten Vorzeichenkonvention gilt
⟨e_hat_fall, e_z⟩ ≤ 0 (Falllinie zeigt **nach unten**, geometrische
Bergab-Richtung). Operational liefert die Projektionsform aus
`hg_falllinie.md` Gleichung (vgl. dortige Symbol-Konvention)

```
e_hat_fall := −(e_z − ⟨e_z, n_a⟩ · n_a) / ‖e_z − ⟨e_z, n_a⟩ · n_a‖.
```

Lesart des Minus-Zeichens: Der Term v := e_z − ⟨e_z, n_a⟩·n_a
ist die orthogonale Projektion von e_z in den Richtungsraum von
E und zeigt entlang der steilsten Richtung in E **nach oben**;
das vorangestellte Minus dreht die Richtung gemäß der
Vorzeichenkonvention in die Bergab-Richtung. e_hat_fall ist
wohldefiniert für α > 0 (denn dann ist e_z nicht parallel zu
n_a und der Nenner positiv); siehe `hg_falllinie.md` für die
vollständige Wohldefiniertheits-Argumentation.

Eine Polygonrandkante e_i = [v_i, v_{i+1}] heißt **entlang der
Falllinie verlaufend**, wenn ihr Einheits-Richtungsvektor

```
e_hat_i := (v_{i+1} − v_i) / ‖v_{i+1} − v_i‖
```

mit e_hat_fall kollinear ist:

```
‖e_hat_i × e_hat_fall‖ ≤ ε_W,    äquivalent  |⟨e_hat_i, e_hat_fall⟩| ≥ 1 − ε_W²/2.
```

Eine Strecke o ⊂ ℝ³ heißt **Ortgang** der Dachfläche D genau dann,
wenn

1. **Randkante**: o ⊂ ∂F(P) — o liegt vollständig im Polygonrand
   von D.
2. **Falllinien-Lage**: o verläuft entlang der Falllinie:
   ‖e_hat(o) × e_hat_fall‖ ≤ ε_W.
3. **Geneigt**: ⟨e_hat(o), e_z⟩ ≠ 0 (genauer: |⟨e_hat(o), e_z⟩| > ε_W);
   damit ist o im Gegensatz zur Traufe nicht horizontal. Diese
   Bedingung folgt automatisch aus 2 zusammen mit α > 0.

Die Vereinigung aller so identifizierten Strecken bildet, falls sie
über gemeinsame Eckpunkte zusammenhängt, die **Ortganglinie** als
Streckenzug; im Regelfall (Sattel-, Pult-, Krüppelwalmdach) besteht
sie aus genau einer Strecke pro Giebelseite.

## Wohldefiniertheit

- **Existenz von e_hat_fall**: Für jede geneigte Dachfläche
  (α ∈ (0, π/2)) ist e_z − ⟨e_z, n_a⟩ · n_a ≠ 0, denn sonst wäre
  e_z parallel zu n_a, also α = 0. Damit ist e_hat_fall eindeutig
  bestimmt. Bei einer horizontalen Dachfläche (α = 0) ist e_hat_fall
  nicht definiert; in diesem Fall existiert auch geometrisch kein
  Ortgang (siehe `Entartet.NichtIdentifizierbar`).
- **Existenz des Ortgangs**: Bei einer geneigten Dachfläche, deren
  Polygonrand mindestens eine Kante entlang der Falllinie enthält
  (Regelfall im Holzbau bei orthogonalen Grundrissen), ist die Menge
  der Ortgangs-Kandidaten nicht leer.
- **Eindeutigkeit**: Bei einem Sattel- oder Pultdach mit
  rechteckigem Grundriss hat jede Dachfläche genau zwei Ortgänge
  (links und rechts); die Definition liefert beide gleichberechtigt.
  Bei Walmdächern hat die Hauptdachfläche keinen Ortgang (statt
  dessen Grat-Schnittkanten); die Definition liefert dann die leere
  Menge — ebenfalls baulich korrekt.
- **Symmetrie**: Die Bedingung 2 ist symmetrisch unter der
  Vertauschung e_hat(o) ↔ −e_hat(o), denn ‖−v × w‖ = ‖v × w‖. Sie ist
  unabhängig von der Orientierung der Strecke.
- **Konsistenz mit `dachkante`**: Ein Ortgang ist nach Bedingung 1
  eine Randkante der Dachfläche, also eine Dachkante im Sinne von
  `dachkante` (Fall „Randkante").
- **Nicht-Zirkularität**: Die Definition stützt sich nur auf
  `strecke`, `dachflaeche`, `polygon`, `vektor`, `toleranzen` und
  den bereits definierten Oberbegriff `dachkante`.

## Erläuterung (nicht normativ)

Der Ortgang ist die seitliche, geneigte Begrenzung einer Dachfläche
an einem Giebel. Bei einem Satteldach mit rechteckigem Grundriss
hat jede der beiden Dachflächen zwei Ortgänge: einen am linken und
einen am rechten Giebel. Sie verlaufen parallel zur Falllinie der
Dachfläche, also in Richtung des größten Gefälles, und schließen
oben am First, unten an der Traufe an.

Bei abgewalmten Dächern (Walmdach, Krüppelwalmdach) entfällt der
Ortgang an den Walmseiten — dort bilden die Walmflächen zusätzliche
Dachflächen, und die Schnittkanten zwischen Hauptdach und Walm sind
**Grate**, keine Ortgänge.

Konstruktiv liegt am Ortgang häufig ein **Ortbrett** (auch
„Windbrett") als sichtbarer seitlicher Eindeckungsabschluss; das ist
ein Bauteil, kein Bestandteil der geometrischen Ortgangkante selbst.

Bei geneigten Giebeln (Sondertopologien, etwa bei in den Grundriss
einspringenden oder ausspringenden Giebeln) bleibt die Falllinien-
Bedingung das definierende Merkmal — der Ortgang ist und bleibt
diejenige Polygonrandkante, die in der Dachflächen-Ebene das
Gefälle abläuft.

## Beziehungen

- **Oberbegriff**: `dachkante`, Spezialfall „Randkante" mit
  zusätzlicher Lagebedingung (Verlauf entlang der Falllinie der
  zugehörigen Dachfläche).
- **Geschwister-Begriffe** (andere Spezialisierungen von
  `dachkante`): `traufe`, `first`, `grat`, `kehle`, `pultkante`.
- **Bestandteile (partitiv)**: Anfangspunkt und Endpunkt der
  Ortgangs-Strecke; im Regelfall ist der untere Endpunkt zugleich
  Eckpunkt der Trauflinie und der obere Endpunkt zugleich Eckpunkt
  der Firstlinie (oder einer Pultkante, oder eines Grats).
- **Abgrenzung**:
  - **Traufe** (`traufe`): untere, näherungsweise horizontale
    Polygonrandkante; verläuft rechtwinklig zur Falllinie.
  - **First** (`first`): obere, näherungsweise horizontale
    Schnittkante; verläuft rechtwinklig zur Falllinie.
  - **Grat** (eigener Eintrag folgt): geneigte Schnittkante
    zweier Dachflächen an einem ausspringenden Eck (Walmdach-Ecke);
    geometrisch in einer einzelnen Dachfläche **nicht** entlang
    der Falllinie, sondern entlang der Schnittgeraden zweier
    Dachflächen-Ebenen — daher Schnittkante, nicht Randkante.
  - **Kehle** (eigener Eintrag folgt): geneigte Schnittkante
    zweier Dachflächen an einem einspringenden Eck.
  - **Pultkante** (eigener Eintrag folgt): obere Polygonrandkante
    einer Pultdachfläche; horizontal, nicht entlang der Falllinie.
  - **Ortbrett / Windbrett**: konstruktives Bauteil am Ortgang;
    nicht Bestandteil der geometrischen Kante. Hier nicht definiert.
  - **Giebel / Giebelseite**: jene Wand des Gebäudes, an die der
    Ortgang anschließt; ist Eigenschaft der Wand, nicht der Dachfläche.
    Hier nicht definiert.
  - **Falllinie**: die Richtung des größten Gefälles auf der
    Dachfläche; ist eine Richtung, keine Kante. Wird im Eintrag als
    Hilfsgröße eingeführt; eigener Glossareintrag folgt bei Bedarf.

## Implementierungshinweis

Datentyp (Domänen-Schicht, Kotlin, Schicht `domain.bauteil`):

```
sealed class Ortgang : Dachkante() {

    data class Regulaer(
        override val polylinie: Streckenzug,
        val dachflaeche: Dachflaeche
    ) : Ortgang()

    sealed class Entartet : Ortgang() {
        object Nullkante : Entartet()
        object NichtIdentifizierbar : Entartet()
    }
}
```

Klassifikations-Prädikat in `DachkanteOps.kt`:

```
fun istOrtgang(
    e: Strecke,
    d: Dachflaeche,
    eps_W: Double = Toleranzen.WINKEL_EPS,
    eps_L: Double = Toleranzen.LAENGE_EPS
): Boolean {
    // 0. Dachfläche muss geneigt sein, sonst keine Falllinie
    val nA = d.aeussereNormale
    val nzZ = nA dot Vektor.E_Z
    if (1.0 - nzZ <= eps_W) return false   // α ≈ 0 (Flachdach)
    // 1. e ist Polygonrandkante von d
    if (!d.umriss.enthaeltKante(e, eps_L)) return false
    // 2. e verläuft entlang der Falllinie
    val eHat = e.einheitsRichtung().werteOder { return false }
    val fallrichtung = (-(Vektor.E_Z - nA * nzZ)).normiert().werteOder { return false }
    val kreuz = (eHat cross fallrichtung).norm
    if (kreuz > eps_W) return false
    // 3. e ist nicht horizontal (folgt aus 0+2, hier nur Sicherheit)
    if (abs(eHat dot Vektor.E_Z) <= eps_W) return false
    return true
}
```

- **Einheit**: alle Koordinaten in mm (Double), Längen in mm.
- **Invarianten** (in Factory prüfen, niemals Exception):
  1. ℓ(polylinie) > Toleranzen.LAENGE_EPS — sonst `Entartet.Nullkante`.
  2. Jede Teilstrecke der Polylinie ist Polygonrandkante der
     übergebenen Dachfläche.
  3. Die Dachfläche ist geneigt (α > Toleranzen.WINKEL_EPS), sonst
     `Entartet.NichtIdentifizierbar`.
  4. Jede Teilstrecke verläuft entlang der Falllinie der Dachfläche
     (Kollinearität mit e_hat_fall, geprüft mit Kreuzprodukt-
     Toleranz Toleranzen.WINKEL_EPS).
- **Edge Cases**:
  - **Nullkante**: ℓ ≤ Toleranzen.LAENGE_EPS → `Entartet.Nullkante`.
  - **Flachdach** (α = 0): keine Falllinie definierbar →
    `Entartet.NichtIdentifizierbar`.
  - **NichtIdentifizierbar**: Polygonrand enthält keine entlang der
    Falllinie verlaufende Kante (z. B. bei einer rein dreieckigen
    Walmfläche, deren beide nicht-horizontalen Kanten Grate sind) →
    `Entartet.NichtIdentifizierbar`.
  - **Geknickter Ortgang** (z. B. bei Mansarddach mit gestuftem
    Giebel): zulässig durch Streckenzug-Modellierung; jede
    Teilstrecke wird einzeln klassifiziert.
- **Abgeleitete Operationen**:
  - `fun ortganglaenge(): Double` (mm) = ℓ(polylinie).
  - `fun ortganglinie(): Streckenzug` = polylinie.
  - `fun gefaelle(): Double` = ⟨−e_hat(polylinie), e_z⟩ (sin der
    Dachneigung; korrespondiert zu α der Dachfläche).

## Quellen

**Primär (normativ):**

- SIA 232/1:2020, „Geneigte Dächer", Schweizerischer Ingenieur- und
  Architektenverein, Abschnitt 1.
- DIN 1356-1:1995-02, „Bauzeichnungen – Teil 1: Arten, Inhalte und
  Grundregeln der Darstellung", Abschnitt 5.
- DIN 18338:2019-09, „VOB Teil C: Dachdeckungs- und
  Dachabdichtungsarbeiten", Abschnitt 0.

**Sekundär:**

- Mönck, W.; Rug, W.: *Holzbau – Bemessung und Konstruktion.*
  15. Auflage, Beuth Verlag 2015.
- Gerner, M.: *Fachwerk – Instandsetzung, Sanierung, Neubau.* DVA,
  7. Auflage 2007.
- Lignum (Hrsg.): *Lignatec — Geneigte Dächer in Holzbauweise.*
  Lignum, Zürich, aktuelle Auflage.

**Korpus (nicht autoritativ):**

- Wikipedia, Lemma „Ortgang" (abgerufen 2026-05-08).
