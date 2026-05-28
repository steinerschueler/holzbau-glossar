---
id: kehle
benennung: Kehle
synonyme: [Kehlkante, Kehllinie, Ixe]
abgelehnte_benennungen: [Kehlblech, Kehlbohle, Kehlsparren, "valley", "valley line"]
oberbegriff: dachkante
begriffstyp: partitiv
voraussetzungen: [strecke, dachflaeche, polygon, ebene, vektor, toleranzen, dachkante]
abgrenzung_zu: [traufe, first, ortgang, grat, pultkante, kehlblech, kehlbohle, kehlsparren]
status: entwurf
theorie_pflichtig: required
quellen_primär:
  - "SIA 232/1:2020 'Geneigte Dächer', Schweizerischer Ingenieur- und Architektenverein, Abschnitt 1 (Begriffe): Kehle als geneigte, einspringende Schnittkante zweier Dachflächen mit besonderer Bedeutung für die Wasserführung."
  - "DIN 1356-1:1995-02 'Bauzeichnungen – Teil 1', Abschnitt 5 (Darstellung von Dächern): Kehle als geneigte Dachkante an einer einspringenden Ecke zweier zusammentreffender Dachflächen."
  - "DIN 18338:2019-09 'VOB Teil C: Dachdeckungs- und Dachabdichtungsarbeiten', Abschnitt 0 (Begriffe): Kehle als geneigte Schnittlinie zweier nach innen einspringender Dachflächen, in der das Niederschlagswasser konzentriert abläuft."
quellen_sekundär:
  - "Mönck, W.; Rug, W.: Holzbau – Bemessung und Konstruktion. 16. Aufl., Beuth Verlag 2015, Kap. Dachformen (Verschneidungen, Gauben)."
  - "Gerner, M.: Fachwerk – Instandsetzung, Sanierung, Neubau. DVA, 7. Aufl. 2007, Glossar 'Kehle'."
  - "Lignum (Hrsg.): Lignatec 'Geneigte Dächer in Holzbauweise', Lignum, Zürich, aktuelle Auflage."
quellenkonflikt: |
  Im Sprachgebrauch existieren mehrere Lesarten von „Kehle":
  (a) **geometrisch**: Kehle = Kehlkante, also die geneigte konkave
      Schnittkante zweier Dachflächen.
  (b) **Bauteil Eindeckung**: Kehlblech / Kehlrinne = die in der Kehle
      eingelegte wasserführende Blechabdeckung.
  (c) **Bauteil Tragwerk**: Kehlsparren / Kehlbohle = der unter der
      Kehlkante verlaufende Tragwerksbalken.
  Normativ ist (a) belegt (SIA 232/1, DIN 1356, DIN 18338).
  **Festlegung dieses Glossars**: Kehle bezeichnet hier ausschließlich
  die geometrische **Kehlkante** im Sinne (a). Die Bauteile
  **Kehlblech**, **Kehlbohle**, **Kehlsparren** werden in
  `abgrenzung_zu` ausdrücklich abgegrenzt.

  Regionale Synonyme: „Ixe" ist im süddeutschen und schweizerischen
  Sprachraum für die Kehlkante geläufig; es wird hier als Synonym
  geführt, jedoch nicht als Hauptbenennung verwendet.

  Abgrenzung zu **First** und **Grat**: First, Grat und Kehle sind
  alle Schnittkanten zweier Dachflächen. Der First ist näherungsweise
  horizontal; Grat und Kehle sind geneigt. Grat und Kehle wiederum
  unterscheiden sich durch die Konvexität der Geometrie:
  - **Grat**: konvex/ausspringend (Außenecke).
  - **Kehle**: konkav/einspringend (Innenecke).
  Die mathematische Schärfung der qualitativen Begriffe „ausspringend"
  / „einspringend" durch das Vorzeichen des Spatprodukts
  ⟨n̂_a × n̂_b, t̂⟩ ist eigene Festlegung; sie ist konsistent mit allen
  konsultierten Quellen, die nur die qualitativen Begriffe verwenden.

  Klassifikation: Eine Kante einer Dachflächenfamilie soll genau einer
  der sechs Klassen (Traufe, First, Ortgang, Grat, Kehle, Pultkante)
  zugeordnet werden — siehe `hg_dachkante.md`. Kehle ist disjunkt zu
  First (durch Neigungsbedingung) und disjunkt zu Grat (durch
  Konkavitätsbedingung mit umgekehrtem Vorzeichen).
---

## Prosa-Definition

Eine **Kehle** ist eine Dachkante, die als Schnittkante zweier
benachbarter Dachflächen auf der Schnittgerade ihrer Trägerebenen
liegt, gegenüber der Horizontalen geneigt verläuft (also nicht
näherungsweise horizontal ist) und an einer einspringenden Innenecke
des Daches die beiden anliegenden Dachflächen so zusammenführt, dass
ihre äußeren Normalen in einen **gemeinsamen oberen Halbraum**
weisen (konkave Konfiguration), wodurch in der Kehle das von beiden
Dachflächen abfließende Niederschlagswasser zusammenläuft.

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

Sei ℓ(s_{ij}) > ε_L und t̂ der Einheits-Tangentenvektor von s_{ij},
mit der Konvention ⟨t̂, e_z⟩ > 0 (Tangente nach oben orientiert; vgl.
`grat`).

Eine Schnittstrecke s_{ij} heißt **geneigt**, wenn

```
|⟨t̂, e_z⟩| > ε_W                                            (1)
```

(d. h. t̂ ist nicht näherungsweise horizontal — diese Bedingung grenzt
Kehle und Grat gemeinsam vom First ab).

Eine geneigte Schnittstrecke s_{ij} heißt **konkav** (einspringend),
wenn das gemischte Spatprodukt der äußeren Normalen mit der
aufwärts gerichteten Tangente das **negative** Zeichen liefert.
Mit derselben kanonischen Vorzeichenwahl σ(i, j) wie in `hg_grat.md`
(Konvention: positives Spatprodukt = konvex/Grat) verlangen wir

```
⟨ n̂_{a,i} × n̂_{a,j}, t̂ ⟩  ·  σ(i, j)  <  −ε_W.            (2)
```

Äquivalente, vorzeichen-symmetrische Schreibweise:

```
sign( ⟨ n̂_{a,i} × n̂_{a,j}, t̂ ⟩ )_kanonisch  =  −                (2')
```

Anschaulich gleichwertig ist die Bedingung, dass die Winkelhalbierende
beider äußerer Normalen unterhalb der durch g_{ij} und t̂ aufgespannten
Ebene liegt, also nach innen-unten zeigt.

Eine Schnittstrecke s_{ij} heißt **Kehle** der Dachflächenfamilie 𝒟
genau dann, wenn

1. ℓ(s_{ij}) > ε_L (nicht-entartet),
2. s_{ij} ist **geneigt** im Sinne von (1),
3. s_{ij} ist **konkav** im Sinne von (2),
4. beide äußeren Normalen weisen in die obere Halbkugel:
   ⟨n̂_{a,i}, e_z⟩ > 0 und ⟨n̂_{a,j}, e_z⟩ > 0 (Ausschluss
   senkrechter Wände).

Die Vereinigung aller so identifizierten Schnittstrecken bildet,
falls sie über gemeinsame Eckpunkte zusammenhängt, die **Kehllinie**
als Streckenzug; im Regelfall (Verschneidung Hauptdach × Gaube,
Verschneidung zweier Sattel­dächer mit T-Grundriss) besteht sie aus
einer oder zwei Strecken pro einspringender Ecke.

## Wohldefiniertheit

- **Existenz der Tangente**: Wegen ℓ(s_{ij}) > ε_L ist t̂
  wohldefiniert. Die Konvention ⟨t̂, e_z⟩ > 0 ist wegen (1) erfüllbar
  und legt die Orientierung eindeutig fest.
- **Unabhängigkeit von der Indexreihenfolge**: Beim Vertauschen
  i ↔ j wechseln sowohl n̂_{a,i} × n̂_{a,j} als auch σ(i, j) ihr
  Vorzeichen; das Produkt in (2) bleibt invariant.
- **Unabhängigkeit von der Punktwahl**: t̂ ist auf der ganzen
  Strecke konstant; die Bedingungen (1) und (2) sind punktunabhängig.
- **Disjunktheit zu First**: First verlangt |⟨t̂, e_z⟩| ≤ ε_W;
  Kehle verlangt |⟨t̂, e_z⟩| > ε_W.
- **Disjunktheit zu Grat**: Grat verlangt das Spatprodukt
  > +ε_W (konvex), Kehle verlangt < −ε_W (konkav). Dazwischen
  liegt das Toleranzband [−ε_W, +ε_W], das als Entartung
  klassifiziert wird (`Entartet.NichtIdentifizierbar`).
- **Konsistenz mit `dachkante`**: Eine Kehle ist nach Konstruktion
  eine Schnittkante zweier Dachflächen, also eine Dachkante (Fall
  „Schnittkante").
- **Nicht-Zirkularität**: Die Definition stützt sich nur auf
  `strecke`, `dachflaeche`, `polygon`, `ebene`, `vektor`,
  `toleranzen` und den Oberbegriff `dachkante`.

## Erläuterung (nicht normativ)

Die Kehle ist die geneigte „Innenkante" zweier Dachflächen an einem
einspringenden Eck. Sie tritt typischerweise dort auf, wo zwei
Dachvolumina sich verschneiden — etwa beim T-förmigen Anbau eines
Satteldachs an ein anderes Satteldach, oder bei der Verschneidung
einer Satteldachgaube mit einer Hauptdachfläche. An solchen Stellen
fließt das Wasser beider Dachflächen in der Kehlinie zusammen; sie
ist daher konstruktiv besonders relevant.

Konstruktiv liegt in der Kehle üblicherweise ein **Kehlblech**
(metallene Kehlrinne, von der Eindeckung überdeckt) oder eine
**Kehlbohle** (Holzbohle als Unterkonstruktion); unter der Kehlinie
verläuft im Tragwerk häufig ein **Kehlsparren**. Diese Bauteile sind
nicht Bestandteil der geometrischen Kehlkante.

Anschauliche Konkavitätsprüfung: Die beiden äußeren Normalen
n̂_{a,i} und n̂_{a,j} weisen an einer Kehle gewissermaßen
**gegeneinander** (beide in Richtung der jeweils anderen Dachfläche
„über" der Kehlinie); ihre Winkelhalbierende zeigt nach
**oben-zentral** und die Geometrie öffnet sich nach oben wie eine
Rinne. An einem Grat hingegen weisen die Normalen voneinander weg,
und die Geometrie öffnet sich nach unten.

Regional ist die Bezeichnung „Ixe" (auch „Ix") in der Schweiz und
Süddeutschland für die Kehlinie geläufig und insbesondere bei der
Aufrissdarstellung des Dachs gebräuchlich.

## Beziehungen

- **Oberbegriff**: `dachkante`, Spezialfall „Schnittkante" mit
  zusätzlichen Lagebedingungen (geneigt, konkav, beide Normalen mit
  positiver z-Komponente).
- **Geschwister-Begriffe** (andere Spezialisierungen von
  `dachkante`): `traufe`, `first`, `ortgang`, `grat`, `pultkante`.
- **Bestandteile (partitiv)**: Anfangspunkt und Endpunkt der
  Kehllinien-Strecke; im Regelfall ist der untere Endpunkt zugleich
  Eckpunkt zweier Trauflinien (Trauf-Innenecke) und der obere
  Endpunkt zugleich Eckpunkt einer Firstlinie oder eines Grats.
- **Abgrenzung**:
  - **First** (`first`): horizontale Schnittkante zweier nach oben
    zusammenlaufender Dachflächen. Kehle ist im Gegensatz dazu
    geneigt (Bedingung (1)).
  - **Grat** (`grat`): geneigte konvexe Schnittkante. Kehle ist
    konkav; Vorzeichen in (2) umgekehrt zum Grat.
  - **Ortgang** (`ortgang`): geneigte Randkante einer einzelnen
    Dachfläche entlang ihrer Falllinie. Kehle ist Schnittkante
    zweier Dachflächen.
  - **Traufe** (`traufe`): horizontale, untere Randkante.
  - **Pultkante** (`pultkante`): obere Randkante einer einzelnen
    Pultdachfläche.
  - **Kehlblech / Kehlrinne**: Eindeckungs-Bauteil zur
    Wasserführung in der Kehle; nicht die Kante selbst. Hier nicht
    definiert.
  - **Kehlbohle**: Holz-Bauteil als Unterlage des Kehlblechs;
    Bauteil, nicht Kante. Hier nicht definiert.
  - **Kehlsparren** (`kehlsparren`, bereits angelegt):
    Tragwerksbalken unter der Kehlkante; Bauteil, nicht Kante.

## Implementierungshinweis

Datentyp (Domänen-Schicht, Kotlin, Schicht `domain.bauteil`):

```
sealed class Kehle : Dachkante() {

    data class Regulaer(
        override val polylinie: Streckenzug,
        val dachflaecheA: Dachflaeche,
        val dachflaecheB: Dachflaeche
    ) : Kehle()

    sealed class Entartet : Kehle() {
        object Nullkante : Entartet()
        object NichtIdentifizierbar : Entartet()
    }
}
```

Klassifikations-Prädikat in `DachkanteOps.kt`:

```
fun istKehle(
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
    // 5. Konkavitätsbedingung: Spatprodukt < -eps_W
    //    (Vorzeichen-Konvention: dieselbe wie in istGrat; konsistente Wahl
    //    der Reihenfolge (A, B) durch die Polygon-Umlaufrichtung der
    //    ersten Dachfläche.)
    val spat = (nA cross nB) dot tHat
    return spat < -eps_W
}
```

- **Einheit**: alle Koordinaten in mm (Double), Längen in mm.
- **Invarianten** (in Factory prüfen, niemals Exception):
  1. ℓ(polylinie) > Toleranzen.LAENGE_EPS — sonst `Entartet.Nullkante`.
  2. Jede Teilstrecke der Polylinie liegt im Schnittbereich
     F(P_A) ∩ F(P_B) der beiden anliegenden Dachflächen.
  3. Jede Teilstrecke ist geneigt: |t̂ · e_z| > Toleranzen.WINKEL_EPS.
  4. Beide äußeren Normalen weisen mit positiver z-Komponente nach
     oben.
  5. Konkavitätsbedingung (2) erfüllt.
- **Edge Cases**:
  - **Nullkante**: ℓ ≤ Toleranzen.LAENGE_EPS → `Entartet.Nullkante`.
  - **NichtIdentifizierbar**: Spatprodukt im Toleranzband
    [−ε_W, +ε_W] → die beiden Trägerebenen sind näherungsweise
    koplanar oder die Kante liegt im Grenzfall zwischen Grat und
    Kehle → `Entartet.NichtIdentifizierbar`.
  - **Parallele Trägerebenen**: keine Schnittgerade →
    `Entartet.NichtIdentifizierbar`.
  - **Horizontale Tangente**: Bedingung (1) verletzt → die Kante ist
    ein First, keine Kehle.
  - **Geknickte Kehlinie** (z. B. bei polygonal abgeknickten
    Verschneidungen): zulässig durch Streckenzug-Modellierung; jede
    Teilstrecke wird einzeln klassifiziert.
- **Abgeleitete Operationen**:
  - `fun kehllaenge(): Double` (mm) = ℓ(polylinie).
  - `fun kehllinie(): Streckenzug` = polylinie.
  - `fun kehlneigung(): Double` = arcsin(|t̂ · e_z|) (Winkel der
    Kehllinie gegen die Horizontale; Bezugsmaß für die Bemessung
    von Kehlsparren und Kehlblech-Längen).

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

- Wikipedia, Lemma „Dachkehle" (abgerufen 2026-05-08).
