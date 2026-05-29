---
id: grat
benennung: Grat
synonyme: [Gratkante, Gratlinie, Walmkante]
abgelehnte_benennungen: [Gratsparren, Walmgrat, Eckgrat, "hip", "hip ridge", "arris"]
oberbegriff: dachkante
begriffstyp: partitiv
voraussetzungen: [strecke, dachflaeche, polygon, ebene, vektor, toleranzen, dachkante]
abgrenzung_zu: [traufe, first, ortgang, kehle, pultkante, gratsparren, walm, walmflaeche]
status: entwurf
subglossar_pendant: notwendig
quellen_primär:
  - "SIA 232/1:2020 'Geneigte Dächer', Schweizerischer Ingenieur- und Architektenverein, Abschnitt 1 (Begriffe): Grat als geneigte, ausspringende Schnittkante zweier Dachflächen am Walmdach."
  - "DIN 1356-1:1995-02 'Bauzeichnungen – Teil 1', Abschnitt 5 (Darstellung von Dächern): Grat als geneigte Dachkante an der Außenecke zweier zusammentreffender Dachflächen."
  - "DIN 18338:2019-09 'VOB Teil C: Dachdeckungs- und Dachabdichtungsarbeiten', Abschnitt 0 (Begriffe): Grat als geneigte Schnittkante zweier nach außen geneigter Dachflächen."
quellen_sekundär:
  - "Mönck, W.; Rug, W.: Holzbau – Bemessung und Konstruktion. 16. Aufl., Beuth Verlag 2015, Kap. Dachformen (Walmdach)."
  - "Gerner, M.: Fachwerk – Instandsetzung, Sanierung, Neubau. DVA, 7. Aufl. 2007, Glossar 'Grat'."
  - "Lignum (Hrsg.): Lignatec 'Geneigte Dächer in Holzbauweise', Lignum, Zürich, aktuelle Auflage."
quellenkonflikt: |
  Im Sprachgebrauch existieren mehrere Lesarten von „Grat":
  (a) **geometrisch**: Grat = Gratkante, also die geneigte konvexe
      Schnittkante zweier Dachflächen.
  (b) **Bauteil Tragwerk**: Gratsparren = Sparren entlang der Gratkante.
  Normativ ist (a) belegt (SIA 232/1, DIN 1356, DIN 18338).
  **Festlegung dieses Glossars**: Grat bezeichnet hier ausschließlich
  die geometrische **Gratkante** im Sinne (a). Das Bauteil
  **Gratsparren** wird in `abgrenzung_zu` ausdrücklich abgegrenzt.

  Abgrenzung zu **First** und **Kehle**: First, Grat und Kehle sind
  alle Schnittkanten zweier Dachflächen. Der First ist näherungsweise
  horizontal; Grat und Kehle sind geneigt. Grat und Kehle wiederum
  unterscheiden sich durch die Konvexität der Geometrie:
  - **Grat**: konvex/ausspringend — die beiden anliegenden Dachflächen
    bilden zusammen eine nach außen weisende Kante (Außenecke).
  - **Kehle**: konkav/einspringend — die beiden anliegenden Dachflächen
    bilden eine nach innen weisende Kante (Innenecke).
  Die mathematische Schärfung der qualitativen Begriffe „ausspringend"
  / „einspringend" durch das Vorzeichen des Spatprodukts
  ⟨n_hat_a × n_hat_b, t_hat⟩ ist eigene Festlegung; sie ist konsistent mit allen
  konsultierten Quellen, die nur die qualitativen Begriffe verwenden.

  Klassifikation: Eine Kante einer Dachflächenfamilie soll genau einer
  der sechs Klassen (Traufe, First, Ortgang, Grat, Kehle, Pultkante)
  zugeordnet werden — siehe `hg_dachkante.md`. Grat ist disjunkt zu
  First (durch Neigungsbedingung) und disjunkt zu Kehle (durch
  Konvexitätsbedingung).
---

## Prosa-Definition

Ein **Grat** ist eine Dachkante, die als Schnittkante zweier
benachbarter Dachflächen auf der Schnittgerade ihrer Trägerebenen
liegt, gegenüber der Horizontalen geneigt verläuft (also nicht
näherungsweise horizontal ist) und an einer ausspringenden Außenecke
des Daches die beiden anliegenden Dachflächen so zusammenführt, dass
ihre äußeren Normalen vom umbauten Raum **wegweisen** (konvexe
Konfiguration).

## Mathematische Definition

Sei

- D_i = (E_i, P_i, n_{a,i}) und D_j = (E_j, P_j, n_{a,j}) zwei
  verschiedene Dachflächen im Sinne von `dachflaeche` mit i ≠ j,
- E_i und E_j nicht parallel, also E_i ∩ E_j eine Gerade
  g_{ij} ⊂ ℝ³ (Schnittgerade der Trägerebenen),
- F(P_i) ⊂ E_i und F(P_j) ⊂ E_j die berandeten abgeschlossenen
  Flächenstücke,
- s_{ij} := F(P_i) ∩ F(P_j) die gemeinsame Schnittstrecke (vgl.
  `first`),
- e_z = (0, 0, 1)ᵀ die vertikale Achse,
- ε_W := Toleranzen.WINKEL_EPS die Winkeltoleranz,
- ε_L := Toleranzen.LAENGE_EPS die Längentoleranz.

Sei ℓ(s_{ij}) > ε_L. Dann existiert ein Einheits-Tangentenvektor

```
t_hat := (b − a) / ‖b − a‖    mit  s_{ij} = [a, b].
```

Eine Schnittstrecke s_{ij} heißt **geneigt**, wenn

```
|⟨t_hat, e_z⟩| > ε_W                                            (1)
```

(d. h. t_hat ist nicht näherungsweise horizontal — diese Bedingung grenzt
Grat und Kehle gemeinsam vom First ab).

Eine geneigte Schnittstrecke s_{ij} heißt **konvex** (ausspringend),
wenn das gemischte Spatprodukt der äußeren Normalen mit der
**aufwärts gerichteten** Tangente das positive Zeichen liefert.

**Globale Vorzeichenkonvention für t_hat** (gilt für diesen Eintrag und
alle Einträge, die `hg_grat.md` voraussetzen — insbesondere
`hg_gratsparren.md`): Die Tangente t_hat ist **immer bergauf** gewählt,
formal ⟨t_hat, e_z⟩ > 0 (nach (1) wohldefiniert; bei ⟨t_hat, e_z⟩ < 0
ersetze t_hat durch −t_hat). Dann verlangen wir

```
⟨ n_hat_{a,i} × n_hat_{a,j}, t_hat ⟩  ·  σ(i, j)  >  ε_W,            (2)
```

wobei σ(i, j) ∈ {+1, −1} das Vorzeichen ist, das die zyklische
Reihenfolge (i, j) so wählt, dass die beiden Dachflächen am Grat
**im Uhrzeigersinn um t_hat herum** angeordnet sind, wenn man von oben
auf t_hat schaut. Konkret: Setze σ(i, j) := +1, wenn (i, j) so gewählt
ist, dass die Drehung von n_hat_{a,i} nach n_hat_{a,j} um die Achse t_hat im
mathematisch positiven Sinn erfolgt; sonst σ(i, j) := −1. Da das
Spatprodukt antisymmetrisch in (i, j) ist, ist die Bedingung (2)
unabhängig von der Reihenfolge der beiden Dachflächen.

Äquivalente, vorzeichen-symmetrische Schreibweise:

```
sign( ⟨ n_hat_{a,i} × n_hat_{a,j}, t_hat ⟩ )  =  sign( ⟨ n_hat_{a,i} − n_hat_{a,j}, e_hat_⊥ ⟩ )    (2')
```

mit e_hat_⊥ := (e_z − ⟨e_z, t_hat⟩ · t_hat) / ‖…‖ als der zur Tangente
orthogonalen, nach oben weisenden Komponente. Die Bedingung (2'/(2))
ist genau dann erfüllt, wenn die Winkelhalbierende beider äußerer
Normalen oberhalb der durch g_{ij} und t_hat aufgespannten Ebene liegt,
also konvex/ausspringend ist.

Eine Schnittstrecke s_{ij} heißt **Grat** der Dachflächenfamilie 𝒟
genau dann, wenn

1. ℓ(s_{ij}) > ε_L (nicht-entartet),
2. s_{ij} ist **geneigt** im Sinne von (1),
3. s_{ij} ist **konvex** im Sinne von (2),
4. beide äußeren Normalen weisen in die obere Halbkugel:
   ⟨n_hat_{a,i}, e_z⟩ > 0 und ⟨n_hat_{a,j}, e_z⟩ > 0 (Ausschluss
   senkrechter Wände).

Die Vereinigung aller so identifizierten Schnittstrecken bildet,
falls sie über gemeinsame Eckpunkte zusammenhängt, die **Gratlinie**
als Streckenzug; im Regelfall (Walmdach, Krüppelwalm) besteht sie
aus genau einer Strecke pro Walmecke.

## Wohldefiniertheit

- **Existenz der Tangente**: Wegen ℓ(s_{ij}) > ε_L ist t_hat
  wohldefiniert. Die Konvention ⟨t_hat, e_z⟩ > 0 ist wegen (1) erfüllbar
  und legt die Orientierung eindeutig fest.
- **Unabhängigkeit von der Indexreihenfolge**: Beim Vertauschen
  i ↔ j wechseln sowohl n_hat_{a,i} × n_hat_{a,j} als auch σ(i, j) ihr
  Vorzeichen; das Produkt in (2) bleibt invariant. Die Definition
  hängt also nicht von der Reihenfolge der beiden anliegenden
  Dachflächen ab.
- **Unabhängigkeit von der Punktwahl auf s_{ij}**: t_hat ist auf der
  ganzen Strecke konstant; die Bedingungen (1) und (2) sind
  punktunabhängig.
- **Disjunktheit zu First**: First verlangt |⟨t_hat, e_z⟩| ≤ ε_W; Grat
  verlangt |⟨t_hat, e_z⟩| > ε_W. Beide Klassen sind disjunkt.
- **Disjunktheit zu Kehle**: Kehle verlangt das umgekehrte Vorzeichen
  in (2). Bei strikter Ungleichung > ε_W bzw. < −ε_W in beiden
  Klassen sind sie disjunkt; der Grenzbereich |⟨…⟩| ≤ ε_W bedeutet,
  dass die Trägerebenen näherungsweise koplanar sind und die Kante
  als Entartung behandelt wird.
- **Konsistenz mit `dachkante`**: Ein Grat ist nach Konstruktion eine
  Schnittkante zweier Dachflächen, also eine Dachkante (Fall
  „Schnittkante").
- **Nicht-Zirkularität**: Die Definition stützt sich nur auf
  `strecke`, `dachflaeche`, `polygon`, `ebene`, `vektor`,
  `toleranzen` und den Oberbegriff `dachkante`.

## Erläuterung (nicht normativ)

Der Grat ist die geneigte „Außenkante" zweier Dachflächen an einer
Walmdach-Ecke. Anschaulich: Wenn man bei einem Walmdach von außen
auf eine Ecke blickt, läuft die obere Kante der Walmfläche schräg
nach oben zum First — diese schräge Kante ist der Grat. Auf der
anderen Walmecke entsteht spiegelbildlich ein zweiter Grat. Bei
einem klassischen Walmdach gibt es vier Grate, die jeweils vom
Trauf-Eckpunkt bis zum First (oder zum Endpunkt der Firstlinie)
verlaufen.

Konstruktiv liegt entlang des Grats üblicherweise ein
**Gratsparren**, ein verstärkter Sparren, der die Last beider
anliegender Dachflächen trägt. Auf dem Grat sitzt die Eindeckung
mit eigenen Gratziegeln oder Gratabdeckungen.

Anschauliche Konvexitätsprüfung: Die beiden äußeren Normalen
n_hat_{a,i} und n_hat_{a,j} weisen am Grat **voneinander weg** (Außenecke);
ihre Winkelhalbierende zeigt nach **außen-oben**. An einer Kehle
hingegen weisen die Normalen gewissermaßen **gegeneinander**, und
die Winkelhalbierende zeigt nach **innen-unten** (Wassersammelpunkt).

## Beziehungen

- **Oberbegriff**: `dachkante`, Spezialfall „Schnittkante" mit
  zusätzlichen Lagebedingungen (geneigt, konvex, beide Normalen mit
  positiver z-Komponente).
- **Geschwister-Begriffe** (andere Spezialisierungen von
  `dachkante`): `traufe`, `first`, `ortgang`, `kehle`, `pultkante`.
- **Bestandteile (partitiv)**: Anfangspunkt und Endpunkt der
  Gratlinien-Strecke; im Regelfall ist der untere Endpunkt zugleich
  Eckpunkt zweier Trauflinien (Walmdach-Trauf-Eckpunkt) und der
  obere Endpunkt zugleich Eckpunkt der Firstlinie.
- **Abgrenzung**:
  - **First** (`first`): horizontale Schnittkante zweier nach oben
    zusammenlaufender Dachflächen. Grat ist im Gegensatz dazu
    geneigt (Bedingung (1)).
  - **Kehle** (`kehle`): geneigte konkave Schnittkante. Grat ist
    konvex; Vorzeichen in (2) umgekehrt zur Kehle.
  - **Ortgang** (`ortgang`): geneigte Randkante einer einzelnen
    Dachfläche entlang ihrer Falllinie. Grat ist Schnittkante
    zweier Dachflächen, kein Polygonrand einer einzelnen Fläche.
  - **Traufe** (`traufe`): horizontale, untere Randkante. Grat ist
    geneigt und Schnittkante.
  - **Pultkante** (`pultkante`): obere Randkante einer einzelnen
    Pultdachfläche. Grat ist Schnittkante zweier Dachflächen.
  - **Gratsparren** (`gratsparren`, bereits angelegt):
    Tragwerksbalken entlang der Gratlinie; Bauteil, nicht Kante.
  - **Walmfläche**: jene Dachfläche eines Walmdachs, deren
    Trapezform an drei Seiten von Graten und einer Traufe
    begrenzt wird; Fläche, nicht Kante.

## Implementierungshinweis

Datentyp (Domänen-Schicht, Kotlin, Schicht `domain.bauteil`):

```
sealed class Grat : Dachkante() {

    data class Regulaer(
        override val polylinie: Streckenzug,
        val dachflaecheA: Dachflaeche,
        val dachflaecheB: Dachflaeche
    ) : Grat()

    sealed class Entartet : Grat() {
        object Nullkante : Entartet()
        object NichtIdentifizierbar : Entartet()
    }
}
```

Klassifikations-Prädikat in `DachkanteOps.kt`:

```
fun istGrat(
    s: Strecke,
    dA: Dachflaeche,
    dB: Dachflaeche,
    eps_W: Double = Toleranzen.WINKEL_EPS,
    eps_L: Double = Toleranzen.LAENGE_EPS
): Boolean {
    // 1. Schnittkante: s liegt im gemeinsamen Polygonbereich von dA und dB
    if (!liegtImSchnitt(s, dA, dB, eps_L)) return false
    if (s.laenge() <= eps_L) return false
    // 2. Tangente, nach oben orientiert
    var tHat = s.einheitsRichtung().werteOder { return false }
    if ((tHat dot Vektor.E_Z) < 0.0) tHat = -tHat
    // 3. Geneigt (nicht horizontal): grenzt Grat/Kehle gegen First ab
    if (abs(tHat dot Vektor.E_Z) <= eps_W) return false
    // 4. Beide Normalen in oberer Halbkugel
    val nA = dA.aeussereNormale.normiert().werteOder { return false }
    val nB = dB.aeussereNormale.normiert().werteOder { return false }
    if ((nA dot Vektor.E_Z) <= 0.0) return false
    if ((nB dot Vektor.E_Z) <= 0.0) return false
    // 5. Konvexitätsbedingung: Spatprodukt > +eps_W
    //    (Vorzeichen abhängig von der konsistenten Wahl der Normalenreihenfolge;
    //    siehe Wohldefiniertheit. In der Implementierung wird die kanonische
    //    Reihenfolge (i, j) durch die Polygon-Umlaufrichtung der ersten
    //    Dachfläche fixiert.)
    val spat = (nA cross nB) dot tHat
    return spat > eps_W
}
```

- **Einheit**: alle Koordinaten in mm (Double), Längen in mm.
- **Invarianten** (in Factory prüfen, niemals Exception):
  1. ℓ(polylinie) > Toleranzen.LAENGE_EPS — sonst `Entartet.Nullkante`.
  2. Jede Teilstrecke der Polylinie liegt im Schnittbereich
     F(P_A) ∩ F(P_B) der beiden anliegenden Dachflächen.
  3. Jede Teilstrecke ist geneigt: |t_hat · e_z| > Toleranzen.WINKEL_EPS.
  4. Beide äußeren Normalen weisen mit positiver z-Komponente nach
     oben.
  5. Konvexitätsbedingung (2) erfüllt.
- **Edge Cases**:
  - **Nullkante**: ℓ ≤ Toleranzen.LAENGE_EPS → `Entartet.Nullkante`.
  - **NichtIdentifizierbar**: Spatprodukt im Toleranzband
    [−ε_W, +ε_W] → die beiden Trägerebenen sind näherungsweise
    koplanar oder die Kante liegt im Grenzfall zwischen Grat und
    Kehle → `Entartet.NichtIdentifizierbar`.
  - **Parallele Trägerebenen**: keine Schnittgerade →
    `Entartet.NichtIdentifizierbar`.
  - **Horizontale Tangente**: Bedingung (1) verletzt → die Kante ist
    ein First, kein Grat (siehe `hg_first.md`).
  - **Geknickter Grat**: zulässig durch Streckenzug-Modellierung;
    jede Teilstrecke wird einzeln klassifiziert.
- **Abgeleitete Operationen**:
  - `fun gratlaenge(): Double` (mm) = ℓ(polylinie).
  - `fun gratlinie(): Streckenzug` = polylinie.
  - `fun gratneigung(): Double` = arcsin(|t_hat · e_z|) (Winkel der
    Gratlinie gegen die Horizontale; Bezugsmaß für Gratsparren-
    Bemessung).

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

- Wikipedia, Lemma „Dachgrat" (abgerufen 2026-05-08).
