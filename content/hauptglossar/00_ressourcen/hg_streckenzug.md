---
id: streckenzug
benennung: Streckenzug
synonyme: [Polygonzug, Polylinie, "stückweise lineare Kurve", "gebrochener Linienzug"]
abgelehnte_benennungen: [Linienzug, Kurvenzug, Pfad, "polyline", "linestring", "polygonal chain", "broken line"]
oberbegriff: null
begriffstyp: generisch
voraussetzungen: [punkt, strecke, vektor, toleranzen]
abgrenzung_zu: [strecke, polygon, gerade, kurve]
status: entwurf
subglossar_pendant: optional  # Begründung (Abweichung vom Normalfall notwendig): geometrische Zwischenstufe zwischen strecke und polygon, als Begriff nicht praxisgebräuchlich; didaktische Substanz liegt bei strecke und polygon (beide notwendig) (HG_KONVENTIONEN §7).
quellen_primär:
  - "DIN ISO 80000-2:2022-08, 'Größen und Einheiten – Teil 2: Mathematik', Abschnitt 2 (Geometrie), Eintrag 'Streckenzug / gebrochene Linie'."
  - "DIN EN ISO 19107:2019 'Geographic information – Spatial schema', Abschnitt 6.4.7 'GM_LineString' (geordnete Folge von Strecken zwischen aufeinanderfolgenden Stützpunkten)."
quellen_sekundär:
  - "Bronstein, I. N.; Semendjajew, K. A.; Musiol, G.; Mühlig, H.: Taschenbuch der Mathematik. Kap. 3.1.5 'Vielecke' (Streckenzug als Verallgemeinerung des Polygonrands) und Kap. 3.5 'Geraden und Strecken im Raum'."
  - "de Berg, M.; Cheong, O.; van Kreveld, M.; Overmars, M.: Computational Geometry – Algorithms and Applications. 3. Aufl., Springer 2008, Kap. 2 (Line Segment Intersection) und Kap. 3 (Polygon Triangulation), Begriff 'polygonal chain'."
  - "Preparata, F. P.; Shamos, M. I.: Computational Geometry – An Introduction. Springer 1985, Kap. 1.3 (polygonal lines)."
  - "Bär, C.: Elementargeometrie. Springer Spektrum, Kap. 1 (Streckenzüge als stückweise lineare Kurven)."
quellenkonflikt: |
  Holzbau-Normen (SIA 232/1, DIN 1356) verwenden den Begriff
  „Streckenzug" implizit (z. B. „polygonal begrenzt", „gebrochene
  Trauflinie"), ohne ihn axiomatisch zu definieren. DIN ISO 80000-2
  führt den Begriff als „gebrochene Linie" ein, gibt jedoch keine
  formale Definition. Die Geomatik (ISO 19107) definiert
  GM_LineString als geordnete Folge von Stützpunkten mit linearer
  Interpolation; das ist äquivalent zur hier gewählten Festlegung.
  In der Computational Geometry (de Berg, Preparata/Shamos) ist die
  Standarddefinition die einer „polygonal chain" als Folge von
  Strecken mit übereinstimmenden Endpunkten.

  Eigene Festlegung: Ein Streckenzug ist eine endliche, geordnete
  Folge von n ≥ 1 Strecken (s_1, …, s_n), bei der der Endpunkt
  jeder Strecke s_i mit dem Anfangspunkt der nachfolgenden Strecke
  s_{i+1} zusammenfällt. Äquivalent ist die Repräsentation als
  Punktfolge (p_0, p_1, …, p_n) mit n+1 ≥ 2 Stützpunkten und
  s_i := [p_{i−1}, p_i]. Geschlossenheit (p_n = p_0) ist eine
  Eigenschaft, kein Subtyp. Selbstüberschneidungen sind zulässig,
  außer wo durch einen verwendenden Begriff (z. B. `polygon`)
  ausgeschlossen. Diese Festlegung ist konsistent mit DIN ISO 80000-2,
  ISO 19107 und der Computational-Geometry-Tradition.

  Die im Sprachgebrauch gleichbedeutend verwendeten Begriffe
  „Polygonzug" und „Polylinie" werden als Synonyme geführt; in der
  App-Domäne ist der Typ-Bezeichner `Streckenzug`.
---

## Prosa-Definition

Ein **Streckenzug** ist eine endliche, geordnete Folge von Strecken
in ℝ³, bei der jede Strecke mit ihrem Anfangspunkt am Endpunkt der
unmittelbar vorangehenden Strecke ansetzt, sodass die Vereinigung
aller Strecken eine zusammenhängende, stückweise lineare Kurve
zwischen einem Anfangs- und einem Endstützpunkt bildet.

## Mathematische Definition

Sei

- n ∈ ℕ_{≥1} die Anzahl der Strecken,
- (p_0, p_1, …, p_n) ∈ (ℝ³)^{n+1} eine geordnete Folge von n+1
  **Stützpunkten**,
- ε_L := Toleranzen.LAENGE_EPS die Längen-Toleranz.

Die zu der Stützpunktfolge gehörenden **Teilstrecken** sind

```
s_i := [p_{i−1}, p_i]    für i = 1, …, n.
```

Die Stützpunktfolge (p_0, …, p_n) heißt **Streckenzug** L genau dann,
wenn die folgende Nicht-Entartungsbedingung gilt:

1. **Keine Nullstrecke**: ‖p_i − p_{i−1}‖ > ε_L für alle i = 1, …, n.

(Bedingung 1 entspricht der Forderung, dass jede Teilstrecke s_i
selbst eine wohldefinierte Strecke im Sinne von `strecke` ist.)

Die **Anschlussbedingung** s_i.endpunkt = s_{i+1}.anfangspunkt für
i = 1, …, n−1 ist in der Punktfolge-Repräsentation per Konstruktion
erfüllt; sie ist die definitionelle Eigenschaft, die einen
Streckenzug von einer beliebigen Streckenmenge unterscheidet.

Der Streckenzug selbst ist die Vereinigung seiner Teilstrecken als
Punktmenge in ℝ³:

```
|L| := ⋃_{i=1}^{n} s_i ⊂ ℝ³,
```

zusammen mit der geordneten Stützpunktfolge (p_0, …, p_n) als
strukturelle Information. In implementierungsnaher Form ist L = (p_0,
…, p_n).

**Klassifikation nach Schließung**:

```
L heißt geschlossen   :⇔  ‖p_n − p_0‖ ≤ ε_L
L heißt offen         :⇔  L ist nicht geschlossen.
```

Beide Varianten sind gültig.

**Klassifikation nach Selbstschnitt** (optional, je nach
verwendendem Kontext):

```
L heißt einfach   :⇔  für alle i, j ∈ {1, …, n} mit i ≠ j gilt
                       s_i ∩ s_j = ∅, außer für benachbarte Indizes
                       j = i+1 (gemeinsamer Eckpunkt p_i) und im
                       geschlossenen Fall zusätzlich für (i, j) =
                       (1, n) (gemeinsamer Eckpunkt p_0 = p_n).
```

Einfachheit ist im Allgemeinen **nicht** Bestandteil der Definition
des Streckenzugs; sie ist ein Zusatzmerkmal, das verwendende
Begriffe (z. B. `polygon`) zusätzlich verlangen.

Wesentliche abgeleitete Größen:

- **Stützpunktanzahl**: |Stützpunkte(L)| = n + 1.
- **Streckenanzahl**: n.
- **Länge**: ℓ(L) := Σ_{i=1}^{n} ‖p_i − p_{i−1}‖ (in mm).
- **Anfangspunkt**: p_0; **Endpunkt**: p_n.
- **Sehnenvektor**: p_n − p_0; bei geschlossenem L gleich
  Nullvektor (innerhalb ε_L).
- **Anschlussvektor an Eckpunkt p_i** (1 ≤ i ≤ n−1):
  Knickwinkel θ_i := arccos(⟨e_hat_i, e_hat_{i+1}⟩) mit e_hat_i :=
  (p_i − p_{i−1}) / ‖p_i − p_{i−1}‖; θ_i = 0 entspricht
  fortgesetzter Kollinearität, θ_i = π einer Umkehr.

## Wohldefiniertheit

- **Existenz und Eindeutigkeit**: Eine Stützpunktfolge mit
  ‖p_i − p_{i−1}‖ > ε_L für alle i bestimmt die Teilstreckenfolge
  (s_1, …, s_n) eindeutig. Die Punktmenge |L| = ⋃ s_i ist als
  Vereinigung wohldefinierter Strecken eindeutig.
- **Repräsentantenwahl** (Punktfolge ↔ Streckenfolge): Aus
  (p_0, …, p_n) folgt die Streckenfolge (s_1, …, s_n) eindeutig.
  Umgekehrt liefert eine Streckenfolge mit der Anschlussbedingung
  die Punktfolge (s_1.anfang, s_1.ende, s_2.ende, …, s_n.ende)
  eindeutig. Die beiden Repräsentationen sind kanonisch
  äquivalent. Die Domänen-Schicht modelliert den Streckenzug als
  Punktfolge, da diese die Anschlussbedingung strukturell
  garantiert.
- **Orientierung**: Die Streckenfolge ist geordnet; die Umkehrung
  (p_n, p_{n−1}, …, p_0) liefert denselben Streckenzug als
  Punktmenge |L|, jedoch entgegengesetzt orientiert. Identität
  modulo Orientierung ist als separate Vergleichsoperation
  bereitgestellt (siehe Implementierungshinweis).
- **Wohldefiniertheit der Länge**: ℓ(L) = Σ‖p_i − p_{i−1}‖ ist als
  Summe wohldefinierter euklidischer Längen eindeutig und
  invariant unter Translation, Rotation und Spiegelung.
  ℓ(L) > 0 folgt aus Bedingung 1.
- **Wohldefiniertheit der Geschlossenheit**: Die Bedingung
  ‖p_n − p_0‖ ≤ ε_L ist symmetrisch und translations-invariant,
  also invariant unter zyklischer Verschiebung der Punktfolge bei
  geschlossenen Streckenzügen.
- **Nicht-Zirkularität**: Die Definition stützt sich nur auf
  `punkt`, `strecke`, `vektor` und `toleranzen`; sie kommt nicht in
  ihrer eigenen Definition vor.

## Erläuterung (nicht normativ)

Der Streckenzug ist das geometrische Grundmodell für jeden
zusammenhängenden, stückweise geraden Linienverlauf in ℝ³. Im
Holzbau und in der App treten Streckenzüge auf als:

- **Polygonrand** (`polygon`): geschlossener, einfacher, ebener
  Streckenzug;
- **Dachkante** (`dachkante`): offener oder geschlossener
  Streckenzug entlang einer Begrenzung der Dachgeometrie;
- **Trauflinie** (in segmentierter Form): mehrteilige horizontale
  Begrenzungslinie an der Traufe, etwa bei Gebäuden mit
  ein- oder ausspringenden Grundrissen;
- **Ortgang** mit Knick (`ortgang`): bei Mansarddach oder
  gestuftem Giebel besteht der Ortgang aus mehreren
  Teilstrecken mit gemeinsamen Knickpunkten;
- **Bauteil-Achsenverlauf** (zukünftig): die Schwerlinie eines
  geknickten oder mehrteiligen Stabbauteils.

Der zentrale Unterschied zur **Strecke** ist die mögliche
Mehrteiligkeit (n ≥ 2 ist zulässig); der zentrale Unterschied zum
**Polygon** ist die fehlende Forderung von Geschlossenheit,
Ebenheit und Einfachheit.

Die in der Computational Geometry und der Geomatik gebräuchlichen
englischen Begriffe **polyline** und **polygonal chain** sind
synonym; **linestring** ist der Begriff der ISO-19107-Schemafamilie
(GM_LineString). Der deutsche Begriff **Polygonzug** wird in der
Mathematik, **Polylinie** stärker in der Geomatik und CAD-Welt
verwendet; beide sind im Glossar Synonyme.

## Beziehungen

- **Oberbegriff**: keiner als formales Glossarprimitiv; im weiteren
  mathematischen Sinn ein **stückweise lineares Bild des
  Einheitsintervalls in ℝ³**, also eine spezielle stetige Kurve.
  Im Glossar primitiv geführt analog zu `strecke` und `polygon`.
- **Teilbegriffe (Spezialisierungen / Rollen)**:
  - **Strecke** (`strecke`): Streckenzug mit n = 1.
  - **Polygonrand**: ebener, einfacher, geschlossener Streckenzug.
  - **Polylinie/Polygonzug**: Synonyme.
  - **Dachkante** (`dachkante`): Streckenzug in der Rolle einer
    Begrenzungs- oder Schnittlinie der Dachgeometrie.
- **Bestandteile (partitiv)**:
  - Stützpunkte p_0, …, p_n;
  - Teilstrecken s_1, …, s_n;
  - Anfangspunkt p_0 und Endpunkt p_n als ausgezeichnete Stützpunkte.
- **Abgrenzung**:
  - **Strecke** (`strecke`): einzelne Strecke (n = 1). Jede Strecke
    ist ein (trivialer) Streckenzug, aber nicht jeder Streckenzug
    ist eine Strecke.
  - **Polygon** (`polygon`): geschlossener, einfacher, ebener
    Streckenzug zusammen mit dem von ihm berandeten Flächenstück.
    Ein Polygon ist also „mehr" als sein Polygonrand-Streckenzug,
    weil es auch das Innere umfasst; und es fordert zusätzlich
    Ebenheit und Einfachheit.
  - **Gerade** (`gerade`): unbegrenzte Punktmenge, kein
    Streckenzug.
  - **Kurve / Pfad**: allgemeiner Begriff einer stetigen Abbildung
    [0, 1] → ℝ³; ein Streckenzug ist die stückweise lineare,
    endliche Spezialisierung.
  - **Polylinie** vs. **Streckenzug**: identisch; beides sind
    Bezeichnungen für denselben Begriff.
  - **Selbstüberschneidende Streckenzüge**: zulässig in der
    allgemeinen Definition; werden erst dort ausgeschlossen, wo
    Einfachheit verlangt wird (z. B. `polygon`).

## Implementierungshinweis

Datentyp (Domänen-Schicht, Kotlin, Schicht `domain.geometrie`):

```
package domain.geometrie

import domain.Toleranzen

/**
 * Streckenzug in ℝ³ als geordnete Folge von Stützpunkten.
 * Glossar: hg_streckenzug.md
 *
 * Repräsentation als Punktfolge garantiert die Anschlussbedingung
 * strukturell (kein Inkonsistenzrisiko zwischen Endpunkt s_i und
 * Anfangspunkt s_{i+1}). Die Streckenfolge wird abgeleitet.
 */
data class Streckenzug internal constructor(
    val stuetzpunkte: List<Punkt>
) {
    // Konstruktion ausschliesslich ueber Streckenzug.aus(...);
    // der Default-Konstruktor ist `internal`, damit die Invarianten
    // (≥ 2 Stützpunkte, keine Nullstrecken, finite Koordinaten)
    // nicht umgangen werden können.

    companion object {
        fun aus(
            pts: List<Punkt>,
            epsL: Double = Toleranzen.LAENGE_EPS
        ): Resultat<Streckenzug, EntartetGeometrie> {
            if (pts.size < 2) return Resultat.Fehler(EntartetGeometrie.ZuWenigPunkte)
            if (pts.any { !it.istFinit() }) return Resultat.Fehler(EntartetGeometrie.NichtFinit)
            for (i in 1 until pts.size) {
                if ((pts[i] - pts[i-1]).norm <= epsL)
                    return Resultat.Fehler(EntartetGeometrie.NullStrecke)
            }
            return Resultat.Erfolg(Streckenzug(pts.toList()))
        }
    }
}
```

Die Entartungs-Varianten werden über die gemeinsame Sealed Class
`EntartetGeometrie` geführt (analog zu den anderen
Geometrieklassen), nicht über eine eigene `Streckenzug.Entartet`.

- **Einheit**: Stützpunkt-Koordinaten in mm (Double); Länge in mm.
- **Invarianten** (in Factory `Streckenzug.aus(...)` prüfen, bei
  Verletzung Entartet-Variante zurückgeben, niemals Exception):
  1. **Mindestpunktzahl**: stuetzpunkte.size ≥ 2 — sonst
     `EntartetGeometrie.ZuWenigPunkte` (entspricht n ≥ 1 Strecke).
  2. **Keine Nullstrecke**: für alle i ∈ 1..n−1 ist
     ‖pts[i] − pts[i−1]‖ > Toleranzen.LAENGE_EPS — sonst
     `EntartetGeometrie.NullStrecke` (gemeinsame Variante ohne
     Index-Parameter).
  3. **Finite Koordinaten**: keine NaN, keine ±∞ — sonst
     `EntartetGeometrie.NichtFinit`.
- **Bewusst nicht als Entartung modelliert**:
  - **Kollineare Stützpunkte**: drei aufeinanderfolgende
    kollineare Stützpunkte sind ein **gültiger** Sonderfall
    (z. B. eine Trauflinie, die durch einen Hilfspunkt geteilt
    ist). Eine Normalisierung kann durch
    `Streckenzug.normalisiert()` (entfernt kollineare
    Zwischenpunkte) explizit angefordert werden.
  - **Selbstschnitt**: nicht-benachbarte Strecken, die sich
    schneiden, sind in der allgemeinen Definition zulässig. Die
    Eigenschaft `istEinfach()` ist als Test verfügbar; ein
    Streckenzug, der die Einfachheit verletzt, ist deshalb nicht
    entartet, sondern nur „nicht einfach". Verwendende Begriffe
    (z. B. `polygon`) lehnen Selbstschnitt durch eigene
    Validierung ab.
- **Edge Cases / Klassifikationen**:
  - **Geschlossen**: `‖pts.last - pts.first‖ ≤ Toleranzen.LAENGE_EPS`
    — Eigenschaft, kein Defekt.
  - **Offen**: nicht geschlossen — Eigenschaft, kein Defekt.
  - **Trivialer Streckenzug** (n = 1): zulässig; entspricht einer
    einzelnen Strecke. Verwender, die n ≥ 2 erwarten, prüfen das
    explizit (z. B. `polygon` mit k ≥ 3).
  - **Sehr kurze Teilstrecken** (knapp über LAENGE_EPS):
    zulässig, aber numerisch sensibel für Knickwinkel- und
    Kollinearitätsberechnungen; die Domänen-Schicht warnt im
    Test, nicht zur Laufzeit.
- **Identität / Gleichheit**:
  - Standard-`equals`: strikt gleiche Punktfolge in derselben
    Reihenfolge.
  - `gleichInvers(other, eps)`: gleich modulo Umkehrung der
    Reihenfolge.
  - `gleichZyklisch(other, eps)`: nur sinnvoll für geschlossene
    Streckenzüge; gleich modulo zyklischer Verschiebung der
    Stützpunkte.
- **Abgeleitete Operationen** (`StreckenzugOps.kt`):
  - `fun strecken(): List<Strecke>` — abgeleitete Streckenfolge.
  - `fun laenge(): Double` — Σ ‖p_i − p_{i−1}‖ (mm).
  - `fun anfang(): Punkt` = pts.first;
    `fun ende(): Punkt` = pts.last.
  - `fun istGeschlossen(eps: Double = Toleranzen.LAENGE_EPS):
     Boolean` = `(ende() - anfang()).norm <= eps`.
  - `fun istEinfach(eps: Double): Boolean` — Selbstschnitt-Test
    in O(n²) (oder O(n log n) per Sweep-Line bei Bedarf).
  - `fun istKoplanar(eps: Double): Boolean` — Test, ob alle
    Stützpunkte in einer gemeinsamen Ebene liegen
    (Voraussetzung für Polygon-Bildung).
  - `fun normalisiert(eps: Double): Streckenzug` — entfernt
    kollineare Zwischenpunkte.
  - `fun umkehren(): Streckenzug` =
    Streckenzug(stuetzpunkte.reversed()).
  - `fun knickwinkel(i: Int): Double` für 1 ≤ i ≤ n−1 —
    Innenwinkel zwischen den anliegenden Strecken.

## Quellen

**Primär (normativ):**

- DIN ISO 80000-2:2022-08, „Größen und Einheiten – Teil 2: Mathematik",
  Abschnitt 2.
- DIN EN ISO 19107:2019, „Geographic information – Spatial schema",
  Abschnitt 6.4.7 (GM_LineString).

**Sekundär:**

- Bronstein, I. N.; Semendjajew, K. A.; Musiol, G.; Mühlig, H.:
  *Taschenbuch der Mathematik.* Kap. 3.1.5 und 3.5.
- de Berg, M.; Cheong, O.; van Kreveld, M.; Overmars, M.:
  *Computational Geometry – Algorithms and Applications.*
  3. Aufl., Springer 2008, Kap. 2 und 3.
- Preparata, F. P.; Shamos, M. I.: *Computational Geometry – An
  Introduction.* Springer 1985, Kap. 1.3.
- Bär, C.: *Elementargeometrie.* Springer Spektrum, Kap. 1.

**Korpus (nicht autoritativ):**

- Wikipedia, Lemma „Polygonzug" (abgerufen 2026-05-08).
