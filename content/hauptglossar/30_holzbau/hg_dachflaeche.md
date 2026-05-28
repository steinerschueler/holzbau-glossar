---
id: dachflaeche
benennung: Dachfläche
synonyme: []
abgelehnte_benennungen: [Dachhaut, Dachdeckung, "roof surface", "roof slope"]
oberbegriff: ebene
begriffstyp: generisch
voraussetzungen: [ebene, polygon, strecke, toleranzen]
abgrenzung_zu: [dach, dachhaut, dachschraege, dachschraege_winkel, dachseite, traufe, first, ortgang]
status: entwurf
theorie_pflichtig: required
quellen_primär:
  - "DIN 18531-1:2017-07, Abschnitt 3 (Begriffe): Dachfläche als geometrische Bezugsfläche der Abdichtung."
  - "SIA 232/1:2020 'Geneigte Dächer', Abschnitt 1 (Begriffe und geometrische Grundlagen)."
quellen_sekundär:
  - "Mönck, W.: Schäden an Holzkonstruktionen. 4. Aufl., Verlag Bauwesen 2000, Kap. Dachtragwerke."
  - "Gerner, M.: Fachwerk – Instandsetzung, Sanierung, Neubau. DVA, 7. Aufl. 2007, Glossar 'Dach'."
  - "Wikipedia, Lemma 'Dach' und 'Dachhaut' (abgerufen 2026-05-07) — als Korpusbeleg, nicht als Autorität."
  - "Sanier.de: Fachbegriffe rund ums Dach (https://www.sanier.de/dach/fachbegriffe-rund-ums-dach) — Korpusbeleg."
quellenkonflikt: |
  Weder DIN 1052 / DIN EN 1995-1-1 noch SIA 265 enthalten einen
  expliziten Begriffseintrag „Dachfläche"; sie verwenden den Begriff
  vorausgesetzt. DIN 18531 und SIA 232/1 verwenden ihn als geometrische
  Bezugsfläche, ohne eine geschlossene mathematische Definition zu
  geben. Eigene Festlegung: Dachfläche ist die geometrische, ebene und
  polygonal begrenzte Teilfläche eines Daches; die materielle Schicht
  heißt Dachhaut (eigener Eintrag). Diese Festlegung ist konsistent mit
  allen konsultierten Quellen und löst die in Fachglossaren vorhandene
  Vermischung Geometrie ↔ Material auf.
---

## Prosa-Definition

Eine **Dachfläche** ist ein zusammenhängender, ebener und polygonal
begrenzter Teil einer Ebene im Raum, der als Außenfläche eines
Dachtragwerks die Begrenzung des umbauten Raumes nach oben
geometrisch vertritt und dessen Stützgerade entweder horizontal liegt
(Flachdachfläche) oder gegenüber der Horizontalebene um einen Winkel
α ∈ (0, π/2) geneigt ist (geneigte Dachfläche).

## Mathematische Definition

Sei

- E ⊂ ℝ³ eine Ebene mit Stützpunkt p₀ ∈ ℝ³ und Einheits-Normalenvektor
  n ∈ S² (also E = { x ∈ ℝ³ | ⟨n, x − p₀⟩ = 0 }),
- P = (v₁, v₂, …, v_k) ein einfaches, geschlossenes Polygon mit
  Eckpunkten v_i ∈ E und k ≥ 3,
- F(P) ⊂ E das von P berandete, abgeschlossene Flächenstück
  (innerer Bereich vereinigt mit Rand),
- α := arccos(⟨n, e_z⟩) der Winkel zwischen n und der vertikalen
  Achse e_z = (0, 0, 1)ᵀ.

Dann heißt das Tripel

```
D := (E, P, n_a)
```

mit n_a ∈ {+n, −n} als der nach außen weisenden Wahl der Normalen
(die nach außen weisende Halbraumseite ist die nicht vom Bauwerk
belegte) eine **Dachfläche** genau dann, wenn

1. F(P) ist nicht-degeneriert: Flächeninhalt(F(P)) > 0.
2. ⟨n_a, e_z⟩ ≥ 0  (die äußere Normale weist in die obere Halbkugel
   oder in die Horizontale, niemals nach unten).
3. Die Dachneigung α erfüllt α ∈ [0, π/2). Für α = 0 spricht man von
   einer **horizontalen Dachfläche** (Flachdach), für
   α ∈ (0, π/2) von einer **geneigten Dachfläche**.

Der **Träger** der Dachfläche ist E, der **Umriss** ist P, die
**äußere Normale** ist n_a, die **Dachneigung** ist α.

## Wohldefiniertheit

- Eindeutigkeit von α: Für jedes n ∈ S² mit ⟨n, e_z⟩ ≥ 0 ist
  α = arccos(⟨n, e_z⟩) ∈ [0, π/2] eindeutig bestimmt. Da n_a aus
  den beiden Vorzeichen ±n durch Bedingung 2 eindeutig festgelegt
  wird (außer im Grenzfall ⟨n, e_z⟩ = 0, der nach Bedingung 3 mit
  α < π/2 ausgeschlossen ist), ist α wohldefiniert.
- Unabhängigkeit vom Stützpunkt p₀: Die Ebene E hängt nicht von der
  Wahl von p₀ ab, solange p₀ ∈ E gilt; die Definition ist also
  invariant unter Wahl eines anderen Repräsentanten.
- Nicht-Zirkularität: Die Definition verwendet ausschließlich die
  Primitive Punkt, Ebene, Vektor, Polygon, Strecke, Winkel sowie das
  globale Koordinatensystem (e_z). Sie verweist auf keine anderen
  Bauteilbegriffe.

## Erläuterung (nicht normativ)

Die Dachfläche ist die geometrische Außenseite eines Daches,
abstrahiert von Material und Aufbau. Bei einem Satteldach besteht
das Dach aus genau zwei Dachflächen, die sich am First schneiden;
bei einem Walmdach kommen Walmflächen als zusätzliche Dachflächen
hinzu; bei einem Pultdach existiert nur eine einzige Dachfläche.

Die Begrenzungskanten einer Dachfläche tragen je nach räumlicher
Lage eigene Namen: die untere, näherungsweise horizontale Kante
heißt **Traufe**, die obere ist entweder **First** (Schnittkante
mit einer benachbarten Dachfläche) oder **Pultkante**, die
seitlichen Kanten heißen **Ortgang** (an einer Giebelwand) oder
**Grat** bzw. **Kehle** (Schnittkante mit einer benachbarten
Dachfläche bei einspringendem oder ausspringendem Eck).

## Beziehungen

- **Oberbegriff**: Ebene mit polygonaler Berandung (geometrisches
  Primitiv `ebene` zusammen mit `polygon`).
- **Teilbegriffe (Spezialisierungen)**:
  - Hauptdachfläche
  - Walmfläche
  - Pultdachfläche
  - Schleppdachfläche
  - Krüppelwalmfläche
- **Bestandteile (partitiv)**:
  - Begrenzungskanten: Traufe, First, Ortgang, Grat, Kehle,
    Pultkante.
- **Abgrenzung**:
  - **Dach** (eigener Eintrag): das gesamte Bauteil-Aggregat aus
    Tragwerk, Dachflächen und Dachhaut. Eine Dachfläche ist ein
    geometrischer Bestandteil eines Daches, nicht das Dach selbst.
  - **Dachhaut** (eigener Eintrag): die materielle, schichtweise
    aufgebaute Außendeckung (Ziegel, Folie, Blech). Die Dachhaut
    liegt auf der Dachfläche auf, ist aber nicht mit ihr identisch.
    Die Dachfläche ist Geometrie, die Dachhaut ist Material.
  - **Dachschräge** (umgangssprachlich): meint im Innenausbau die
    von unten sichtbare Untersicht der geneigten Dachkonstruktion.
    Geometrisch ist sie eine zur Dachfläche parallele, um die
    Sparrenhöhe nach innen versetzte Ebene. Wird in diesem Glossar
    als eigenständiger Begriff `dachschraege_innen` geführt und ist
    nicht synonym zur Dachfläche.
  - **Dachseite** (eigener Eintrag): keine bloße sprachliche Variante,
    sondern eine Spezialisierung der Dachfläche mit zusätzlicher
    Orientierungs-Annotation (Wetterseite, Sonnenseite, Himmelsrichtung)
    und damit bemessungsrelevant für Wind- und Solarlasten. Eine
    Dachseite ist eine Dachfläche mit zusätzlicher
    Orientierungs-Annotation (vgl. `hg_dachseite.md`).
  - **Dachneigungswinkel α**: ein Merkmal der Dachfläche, kein
    eigenständiges Bauteil.

## Implementierungshinweis

Datentyp (Domänen-Schicht, Kotlin, Schicht `domain.bauteil` bzw.
`domain.geometrie`):

```
data class Dachflaeche(
    val traeger: Ebene,        // E
    val umriss: Polygon,       // P, Eckpunkte ∈ traeger
    val aeussereNormale: Vektor // n_a, ‖n_a‖ = 1, n_a · e_z ≥ 0
)
```

- **Einheit**: Eckpunkt-Koordinaten in mm (Double); α intern in
  Radiant.
- **Invarianten** (in `init`-Block prüfen, bei Verletzung
  `Resultat.Fehler` bzw. `Entartet`-Variante zurückgeben, niemals
  Exception werfen):
  1. Alle v_i ∈ traeger, getestet mit
     |⟨n, v_i − p₀⟩| ≤ Toleranzen.LAENGE_EPS (Standardwert 1e-3 mm
     = 1 µm, bezogen auf normalisiertes n; siehe `hg_toleranzen.md` für
     die kanonischen Default-Werte).
  2. Polygon-Flächeninhalt > Toleranzen.FLAECHE_EPS.
  3. ‖n_a‖ ∈ 1 ± Toleranzen.NORM_EPS.
  4. n_a · e_z ≥ −Toleranzen.WINKEL_EPS  (kleine numerische
     Unterschreitung wird als 0 toleriert).
- **Edge Cases**:
  - α = 0: zulässig (Flachdach). Bei α = 0 ist die Wahl der äußeren
    Normalen durch die Bedingung n_a · e_z = 1 (statt ≥ 0) zu
    erzwingen; n_a = −e_z ist verboten (Kellerdecke wäre kein Dach).
  - α → π/2: degeneriert zur senkrechten Wand. Gemäß Definition
    ausgeschlossen (α < π/2). Die Domänen-Klasse liefert in diesem
    Fall `Entartet.Senkrecht`.
  - Nicht-planarer Polygonzug: numerische Punkte, die nicht exakt in
    E liegen, werden bis Toleranzen.LAENGE_EPS akzeptiert; darüber
    hinaus `Entartet.NichtPlanar`.
  - Nicht-einfaches Polygon (Selbstschnitt): `Entartet.Selbstschnitt`.
- **Abgeleitete Eigenschaften** (als Funktionen, keine Felder):
  - `dachneigung(): Radiant` = arccos(aeussereNormale · e_z).
  - `flaecheninhalt(): Double` (mm²) aus dem Umriss-Polygon.
  - `traufe(): Strecke?`, `first(): Strecke?`, `ortgang(): List<Strecke>`
    werden in Folge-Einträgen der genannten Kantenbegriffe definiert
    und greifen auf die Klassifikation der Polygonkanten nach
    Lage und Nachbarschaft zurück.

## Quellen

**Primär (normativ):**

- DIN 18531-1:2017-07, „Abdichtung von Dächern sowie von Balkonen,
  Loggien und Laubengängen – Teil 1: Nicht genutzte und genutzte
  Dächer – Anforderungen, Planungs- und Ausführungsgrundsätze",
  Abschnitt 3.
- SIA 232/1:2020, „Geneigte Dächer", Schweizerischer Ingenieur- und
  Architektenverein, Abschnitt 1.

**Sekundär:**

- Mönck, W.: *Schäden an Holzkonstruktionen.* 4. Auflage, Verlag
  Bauwesen, Berlin 2000.
- Gerner, M.: *Fachwerk – Instandsetzung, Sanierung, Neubau.* DVA,
  7. Auflage 2007.
- Lignum (Hrsg.): *Holzbautabellen HBT.* Lignum, Zürich, aktuelle
  Auflage.

**Korpus (nicht autoritativ, nur zur Belegung des Sprachgebrauchs):**

- Wikipedia, Lemmata „Dach" und „Dachhaut" (abgerufen 2026-05-07).
- Sanier.de: „Fachbegriffe rund ums Dach".
