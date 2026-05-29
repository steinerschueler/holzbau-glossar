---
id: halbraum
benennung: Halbraum
synonyme: ["abgeschlossener Halbraum", "geschlossener Halbraum", "Halbraum (orientiert)"]
abgelehnte_benennungen: [Halbebene, Seite, Raumhälfte, "halfspace", "half-space"]
oberbegriff: null
begriffstyp: generisch
voraussetzungen: [punkt, vektor, ebene, toleranzen]
abgrenzung_zu: [ebene, halbgerade, polyeder]
status: entwurf
subglossar_pendant: optional  # Begründung (Abweichung vom Normalfall notwendig): interner geometrischer Baustein (Bauteilkörper = Schnitt von Halbräumen), im Holzbau-Korpus nicht gebräuchlich, kein Praxis-Lehrwert bis Meister; Stoff liegt bei ebene und polyeder (beide notwendig) (HG_KONVENTIONEN §7).
quellen_primär:
  - "DIN ISO 80000-2:2022-08, 'Größen und Einheiten – Teil 2: Mathematik', Abschnitt 2 (Geometrie und Vektoren), Hesse'sche Normalform."
quellen_sekundär:
  - "Bronstein, I. N. et al.: Taschenbuch der Mathematik. Kap. 3.5.2 'Ebenen im Raum', Hesse'sche Normalform und Halbräume."
  - "Fischer, G.: Lineare Algebra. 19. Aufl., Springer Spektrum 2020, Kap. 1 'Affine Geometrie'."
  - "Bär, C.: Elementargeometrie. Springer Spektrum, Kap. 5 'Ebenen und Halbräume'."
  - "Ziegler, G. M.: Lectures on Polytopes. Springer 1995, Kap. 0.6 (Halfspaces and Polytopes)."
quellenkonflikt: |
  Holzbau-Normen verwenden den Begriff Halbraum nicht. DIN ISO 80000-2
  führt die Hesse-Normalform einer Ebene, aus der sich Halbräume
  unmittelbar ergeben, jedoch nicht den Halbraum als eigenständigen
  Begriff. Eigene Festlegung: ein Halbraum ist einer der beiden
  abgeschlossenen oder offenen Teilräume von ℝ³, die durch eine Ebene
  abgegrenzt werden, mit einer Normalen, die per Konvention **in den
  Halbraum hinein** zeigt. Diese Festlegung ist konsistent mit
  Bronstein, Fischer, Bär und Ziegler und steht nicht in Konflikt zu
  den konsultierten Holzbau-Quellen.
---

## Prosa-Definition

Ein **Halbraum** ist eine der beiden zusammenhängenden Teilmengen
von ℝ³, in die der Raum durch eine Ebene zerlegt wird, festgelegt
durch einen Stützpunkt p₀ ∈ ℝ³ in der Randebene und einen
Nicht-Nullvektor n ∈ ℝ³, der per Konvention in den Halbraum hinein
zeigt; je nach Wahl gehört die Randebene zum Halbraum
(**geschlossener Halbraum**) oder nicht (**offener Halbraum**).

## Mathematische Definition

Sei

- p₀ ∈ ℝ³ ein **Stützpunkt** auf der Randebene,
- n ∈ ℝ³ \ {0} der in den Halbraum hinein gerichtete
  **Halbraum-Normalenvektor**.

Dann sind der durch (p₀, n) definierte **geschlossene Halbraum** H_bar
und der **offene Halbraum** H° ⊂ ℝ³ die Mengen

```
H_bar(p₀, n) := { x ∈ ℝ³ | ⟨n, x − p₀⟩ ≥ 0 },
H°(p₀, n) := { x ∈ ℝ³ | ⟨n, x − p₀⟩ > 0 }.
```

Der **Rand** beider Mengen ist die Ebene

```
∂H = E(p₀, n) = { x ∈ ℝ³ | ⟨n, x − p₀⟩ = 0 },
```

und es gilt H_bar = H° ∪ ∂H sowie H° = H_bar \ ∂H.

In **Hesse-Normalform** mit n_hat := n / ‖n‖ und d := ⟨n_hat, p₀⟩ wird

```
H_bar(p₀, n) = { x ∈ ℝ³ | ⟨n_hat, x⟩ ≥ d },
H°(p₀, n) = { x ∈ ℝ³ | ⟨n_hat, x⟩ > d }.
```

Wesentliche abgeleitete Größen für x ∈ ℝ³:

- **Vorzeichenbehafteter Abstand zur Randebene**:
  d_H(x) := ⟨n_hat, x − p₀⟩, in mm. d_H(x) > 0 ⇔ x ∈ H°,
  d_H(x) = 0 ⇔ x ∈ ∂H, d_H(x) < 0 ⇔ x ∉ H_bar.
- **Komplementärer Halbraum**: H_bar(p₀, −n) bzw. H°(p₀, −n); es gilt
  H_bar(p₀, n) ∪ H_bar(p₀, −n) = ℝ³ und
  H_bar(p₀, n) ∩ H_bar(p₀, −n) = ∂H.

## Wohldefiniertheit

- **Unabhängigkeit vom Stützpunkt innerhalb der Randebene**: Für
  jedes p₀' ∈ ∂H gilt H_bar(p₀', n) = H_bar(p₀, n) und analog für H°.
  Beweis wie bei `ebene`: aus ⟨n, p₀' − p₀⟩ = 0 folgt
  ⟨n, x − p₀'⟩ = ⟨n, x − p₀⟩.
- **Skaleninvarianz mit positivem Faktor**: Für jedes λ > 0 gilt
  H_bar(p₀, λ·n) = H_bar(p₀, n) (analog für H°), denn
  ⟨λn, ·⟩ ≥ 0 ⇔ ⟨n, ·⟩ ≥ 0.
- **Vorzeichenwechsel kehrt den Halbraum um**: H_bar(p₀, −n) ist der
  komplementäre Halbraum, **nicht** derselbe. Die Wahl von
  sign(n) ist also wesentlich; ein Halbraum ist orientiert.
- **Geschlossen vs. offen**: H_bar und H° sind verschiedene Mengen
  (sie unterscheiden sich um die Randebene ∂H). Beide werden
  benötigt; geschlossene Variante ist Default (siehe Implementierung).
- **Existenz**: Für jedes (p₀, n) mit n ≠ 0 sind H_bar und H° nicht-leer.
- **Nicht-Zirkularität**: Die Definition verwendet Punkt, Vektor,
  Skalarprodukt und Ordnungsrelation reeller Zahlen; sie greift auf
  `ebene` nur insofern zurück, als der Rand des Halbraums eine Ebene
  ist (Folgerung, nicht Voraussetzung).

## Erläuterung (nicht normativ)

Ein Halbraum ist die geometrische Abstraktion einer „Seite" einer
Ebene. Im Holzbau ist diese Unterscheidung allgegenwärtig:

- **Oberhalb / unterhalb einer Dachfläche**: der Halbraum oberhalb
  einer Dachebene (Außennormale weist nach außen-oben) ist der
  Außenraum, der Halbraum unterhalb der Innenraum unter Dach.
- **Innen / außen eines Bauteils**: Vollholz-Bauteile sind durch
  Schnitt mehrerer geschlossener Halbräume modellierbar; jede
  Begrenzungsfläche definiert „innen" als ihre Halbraumseite mit
  nach innen weisender Normale.
- **Liegt der Punkt p auf der richtigen Seite einer Schnittfläche?**
  ist ein Halbraum-Inzidenztest.

**Vorgesehen als Bausteine für Bauteilbegrenzungen**: Polyeder
(z. B. Balkenquader, beschnittene Sparrenenden, vollständige
Bauteilkörper) werden in der Domänen-Schicht als endliche
Schnittmengen geschlossener Halbräume dargestellt. Halbräume sind
damit der atomare Bestandteil aller volumetrischen Bauteilformen.

Die Konvention „Normale zeigt **in den Halbraum hinein**" wird
gewählt, weil sie den Inzidenztest in der natürlichen Form
⟨n, x − p₀⟩ ≥ 0 ⇔ x ∈ H_bar schreibt und damit für aufgebaute
Polyeder unmittelbar das Innere als Schnitt aller H_bar liefert. Diese
Konvention ist konsistent mit Ziegler („Lectures on Polytopes").
**Achtung**: für Dachflächen wird üblicherweise die nach außen
weisende Normale verwendet (siehe `dachflaeche`); beim Aufbau eines
Halbraums aus einer Dachfläche ist daher gegebenenfalls das
Vorzeichen umzukehren.

## Beziehungen

- **Oberbegriff**: dreidimensionaler abgeschlossener (bzw. offener)
  konvexer Teilraum von ℝ³, begrenzt durch eine Ebene. Im Glossar
  Primitiv.
- **Teilbegriffe / Rollen**: rollenbezogene Verwendungen wie
  „Außenhalbraum einer Dachfläche", „Innenhalbraum eines Bauteils"
  sind keine Subtypen, sondern Anwendungen.
- **Bestandteile (partitiv)**:
  - **Rand**: die Ebene ∂H = E(p₀, n).
  - **Inneres**: H° = H_bar \ ∂H.
- **Abgrenzung**:
  - **Ebene** (`ebene`): zweidimensionaler Rand des Halbraums;
    Dimension 2 statt 3. Eine Ebene zerlegt ℝ³ in zwei
    komplementäre Halbräume.
  - **Halbgerade** (`halbgerade`): einseitig begrenzter Ausschnitt
    einer Geraden, Dimension 1; vom Halbraum durch Dimension
    unterschieden.
  - **Polyeder** (eigener Eintrag in Folgearbeit): endliche
    Schnittmenge geschlossener Halbräume; ein Halbraum ist also
    der atomare Bestandteil eines Polyeders, jedoch selbst
    unbeschränkt.

## Implementierungshinweis

Datentyp (Domänen-Schicht, Kotlin, Schicht `domain.geometrie`):

```
enum class HalbraumArt { GESCHLOSSEN, OFFEN }

data class Halbraum internal constructor(
    val ebene: Ebene,                                      // Randebene mit Orientierung
    val art: HalbraumArt = HalbraumArt.GESCHLOSSEN,
) {
    val stuetzpunkt: Punkt get() = ebene.stuetzpunkt       // Convenience: p₀
    val normale: Einheitsvektor get() = ebene.normale      // Convenience: n_hat, in den Halbraum hinein
}
```

- **Repräsentation als `Ebene` + `art`**: Der Halbraum delegiert seine
  Randdaten an die bereits in der Domänen-Schicht etablierte
  [`Ebene`](hg_ebene.md), statt `stuetzpunkt` und `normale` direkt zu
  speichern. Das hat zwei Konsequenzen: (a) die Einheitsvektor-
  Invariante `‖n_hat‖ ≈ 1` ist **typsystem-getragen** (durch den Typ
  `Einheitsvektor`) und braucht keine `init`-Validierung; (b) die
  Identitätsprüfungen, Operationen und Toleranzen der Ebene werden
  konsistent wiederverwendet (`umkehrenNormale`, `abstand`, etc.).
  Convenience-Properties `stuetzpunkt` und `normale` halten die
  Glossar-nahe API-Optik erhalten.
- **Einheit**: Stützpunkt-Koordinaten in mm (Double). Die Normale ist
  per Typ `Einheitsvektor` normiert (`‖n_hat‖ ≈ 1`); eine Normierung in
  abgeleiteten Operationen entfällt.
- **Konvention der Normalenrichtung**: die Normale `n_hat` zeigt **in
  den Halbraum hinein**. Für x mit ⟨n_hat, x − p₀⟩ > 0 gilt x ∈ H°.
  Diese Konvention ist verbindlich und im KDoc jeder Konstruktor-
  und Operationsmethode zu nennen.
- **Default `art = GESCHLOSSEN`**: für Inzidenz-Tests und
  Bauteilbegrenzungen ist die geschlossene Variante mit Toleranz-
  test (`d_H(x) ≥ −Toleranzen.LAENGE_EPS`) numerisch robust und
  fachlich angemessen — Punkte exakt auf der Berandung gehören dazu.
  Die offene Variante ist nur für strikte Trennungstests
  vorgesehen.
- **Invarianten** (durch Konstruktion getragen, keine `init`-Prüfung
  nötig):
  1. `n_hat` ist Einheitsvektor — typsystem-getragen über `Einheitsvektor`.
  2. Alle Komponenten von `stuetzpunkt` und `n_hat` finit — durch die
     Factory `Ebene.ausStuetzpunktUndNormale` bzw. die Invarianten
     von `Einheitsvektor` und `Punkt` getragen.
- **Konstruktoren** (Companion-Factories, alle ohne Wurf):
  - `Halbraum.ausEbene(e: Ebene, art = GESCHLOSSEN): Resultat<Halbraum, EntartetGeometrie>`
    — übernimmt `e` direkt; liefert stets `Erfolg`, da die Ebene-
    Invarianten typsystem-getragen sind. Aufrufer ist verantwortlich,
    dass `e.normale` in den gewünschten Halbraum zeigt (vgl. Konvention
    bei `dachflaeche`, deren Außennormale in den Außen-Halbraum zeigt).
  - `Halbraum.ausStuetzpunktUndNormale(p, n_hat, art = GESCHLOSSEN): Resultat<Halbraum, EntartetGeometrie>`
    — delegiert an `Ebene.ausStuetzpunktUndNormale`; kann
    `Fehler(NichtFinit)` liefern, wenn `p` nicht-finit ist.
  - **Kein dedizierter `ausEbeneAndereSeite`** — die Operation ist
    durch `komplement()` (Methode auf der Instanz) bzw. `ausEbene(e.umkehrenNormale(), art)`
    substituiert.
- **Methoden** (auf der Instanz):
  - `komplement(): Halbraum` — `Halbraum(ebene.umkehrenNormale(), art)`,
    spiegelt die Normale, behält die `art`. Beschreibt den Halbraum
    auf der anderen Seite derselben Randebene; **nicht** das
    mengentheoretische Komplement (siehe unten).
  - `mitArt(neueArt: HalbraumArt): Halbraum` — Topologie-Wechsel ohne
    Geometrie-Änderung.
- **Edge Cases / Entartet-Varianten**:
  - **Nicht-finite Stützpunkt-Koordinaten** (`ausStuetzpunktUndNormale`):
    `EntartetGeometrie.NichtFinit`. Einzige strukturell erreichbare
    Entartung der aktuellen API.
  - **Numerische Lage am Rand**: für x mit |d_H(x)| ≤
    Toleranzen.LAENGE_EPS klassifiziert `enthaelt(x)` x als auf der
    Randebene liegend. Bei `art = GESCHLOSSEN` gilt x ∈ H_bar, bei
    `art = OFFEN` gilt x ∉ H°.
  - **NullNormale** ist in der aktuellen API **nicht erreichbar**, weil
    die Konstruktoren nur `Einheitsvektor` akzeptieren (Norm-Invariante
    typsystem-getragen). Folgearbeit: falls eine künftige API einen
    rohen `Vektor` als Normale akzeptieren sollte, ist
    `EntartetGeometrie.NullNormale` (`‖n‖² ≤ Toleranzen.NORM_EPS`) als
    weitere Entartet-Variante einzuführen.
- **Abgeleitete Operationen** (auf der Instanz, `Halbraum.kt`):
  - Randebene: direkt über `ebene` zugreifbar (kein Methodenwrapper nötig).
  - Signierter Abstand: `ebene.abstand(p)`, in mm. Vorzeichen folgt
    der Halbraum-Konvention (positiv im Inneren), da `ebene.normale`
    in den Halbraum zeigt.
  - `enthaelt(p: Punkt, eps: Double = Toleranzen.LAENGE_EPS): Boolean`
    je nach `art`:
    - `GESCHLOSSEN`: `ebene.abstand(p) ≥ −eps`.
    - `OFFEN`:       `ebene.abstand(p) >  eps`.
    Bei nicht-finitem `p` liefert `ebene.abstand(p)` `NaN`, und
    `enthaelt` gibt `false` zurück (NaN-Out-Konvention).
  - `komplement()` ist **nicht** das mengentheoretische Komplement: die
    `art` wird nicht zwischen GESCHLOSSEN und OFFEN gewechselt.
    Konsumenten, die das mengentheoretische Komplement benötigen,
    kombinieren `komplement().mitArt(...)` mit dem entsprechenden
    Art-Wechsel.

## Quellen

**Primär (normativ):**

- DIN ISO 80000-2:2022-08, „Größen und Einheiten – Teil 2: Mathematik".

**Sekundär:**

- Bronstein, I. N.; Semendjajew, K. A.; Musiol, G.; Mühlig, H.:
  *Taschenbuch der Mathematik.* Kap. 3.5.2.
- Fischer, G.: *Lineare Algebra.* 19. Aufl., Springer Spektrum 2020.
- Bär, C.: *Elementargeometrie.* Springer Spektrum.
- Ziegler, G. M.: *Lectures on Polytopes.* Springer, New York 1995.

**Korpus (nicht autoritativ):**

- Wikipedia, Lemmata „Halbraum" und „Hesse'sche Normalform"
  (abgerufen 2026-05-07).
