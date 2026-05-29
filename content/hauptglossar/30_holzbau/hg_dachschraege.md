---
id: dachschraege
benennung: Dachschräge
synonyme: [Dachuntersicht, "innere Dachuntersicht", "raumseitige Dachfläche"]
abgelehnte_benennungen: [Dachneigung, Dachschrägung, Schräge, "sloped ceiling", "roof underside"]
oberbegriff: ebene
begriffstyp: generisch
voraussetzungen: [ebene, polygon, vektor, einheitsvektor, dachflaeche, dachaufbau, toleranzen]
abgrenzung_zu: [dachflaeche, dachneigung, dachseite, dachhaut, dachaufbau, decke]
status: entwurf
subglossar_pendant: notwendig
quellen_primär:
  - "SIA 232/1:2020 'Geneigte Dächer', Schweizerischer Ingenieur- und Architektenverein, Abschnitt 2 (Aufbau geneigter Dächer): innere Bekleidung als raumseitige Begrenzung."
  - "DIN 4108-3:2018-10 'Wärmeschutz und Energie-Einsparung in Gebäuden – Teil 3: Klimabedingter Feuchteschutz', Abschnitt 5: raumseitige Bauteilebene als feuchteschutztechnische Bezugsfläche."
  - "DIN 18181:2014-08 'Gipsplatten im Hochbau – Verarbeitung', Abschnitt 5 (Bekleidung von Dachschrägen)."
quellen_sekundär:
  - "Lignum (Hrsg.): Lignatec 'Geneigte Dächer in Holzbauweise', Lignum, Zürich, aktuelle Auflage, Kap. 'Innenbekleidung'."
  - "Mönck, W.; Rug, W.: Holzbau – Bemessung und Konstruktion. 16. Aufl., Beuth Verlag 2015, Kap. 'Dachausbau'."
  - "Gerner, M.: Fachwerk – Instandsetzung, Sanierung, Neubau. DVA, 7. Aufl. 2007, Glossar 'Dachschräge'."
  - "Holzbau Deutschland, Merkblatt 'Begriffe und Klassifizierungen für den Holzbau', Eintrag 'Dachschräge'."
quellenkonflikt: |
  Keine konsultierte Norm definiert „Dachschräge" formal; SIA 232/1
  und DIN 4108-3 verwenden „raumseitige Begrenzung" oder „innere
  Bekleidung", DIN 18181 spricht von „Dachschräge" im Sinn der zu
  bekleidenden Innenfläche, ohne sie geometrisch zu fixieren. Im
  Sprachgebrauch wird „Dachschräge" zudem häufig synonym für die
  „Dachneigung" (also den Winkel) verwendet.

  Eigene Festlegung dieses Glossars: „Dachschräge" bezeichnet die
  raumseitige, der jeweiligen Dachfläche **parallele** und um die
  Dicke des Dachaufbaus nach innen versetzte Flächenebene; sie ist
  damit ein eigenständiges geometrisches Objekt, abgegrenzt von der
  Dachfläche (außenseitig) und vom Winkel α (Dachneigung). Diese
  Festlegung ist mit allen konsultierten Quellen verträglich und
  trennt den im Holzausbau und in der Trockenbau-Praxis (DIN 18181)
  verwendeten Resultats-Begriff sauber von der dimensions- und
  bedeutungsverschiedenen Dachneigung.
---

## Prosa-Definition

Eine **Dachschräge** ist diejenige zur Trägerebene einer Dachfläche
parallele, ebene und polygonal begrenzte Fläche, die innerhalb des
umbauten Raumes als raumseitige Begrenzung des Dachgeschosses sichtbar
ist und gegenüber der zugehörigen Dachfläche um die Dicke des
Dachaufbaus entlang der nach innen gerichteten Flächennormalen
versetzt ist.

## Mathematische Definition

Sei

- D = (E, P, n_a) eine Dachfläche im Sinne von `dachflaeche` mit
  Trägerebene
  ```
  E = { x ∈ ℝ³ | ⟨n_a, x − p₀⟩ = 0 },
  ```
  Umrisspolygon P = (v₁, …, v_k) und nach außen gerichteter
  Einheits-Normale n_a ∈ S² mit ⟨n_a, e_z⟩ ≥ 0,
- A = (𝒟, 𝒮, H) ein Dachaufbau im Sinne von `dachaufbau` mit
  D ∈ 𝒟 und Schichtfolge 𝒮 = (S₁, …, S_k) (von innen nach außen,
  S_j mit Dicke d_j > 0),
- d_A := Σ_{j=1..k} d_j die Gesamtdicke des Dachaufbaus auf D
  (siehe `dachaufbau`).

Dann ist die **Dachschräge** zu D die Fläche

```
S(D, A) := (E_S, P_S, n_S)
```

mit

- **innenseitiger Trägerebene**
  ```
  E_S := { x ∈ ℝ³ | ⟨n_a, x − p₀⟩ = 0 } − d_A · n_a
       = { y + (− d_A) · n_a | y ∈ E }
       = { z ∈ ℝ³ | ⟨n_a, z − (p₀ − d_A · n_a)⟩ = 0 },
  ```
  also der um −d_A · n_a verschobenen Ebene E,
- **innenseitigem Polygon**
  ```
  P_S := (v₁ − d_A · n_a, …, v_k − d_A · n_a),
  ```
  also dem starr nach innen verschobenen Umriss von D,
- **innenseitiger Normale**
  ```
  n_S := − n_a ∈ S²,
  ```
  also der raumseitigen, in den Innenraum weisenden Einheits-Normale
  (⟨n_S, e_z⟩ ≤ 0).

Die so definierte Fläche heißt **Dachschräge** der Dachfläche D
(unter dem Dachaufbau A) genau dann, wenn

1. d_A > Toleranzen.LAENGE_EPS  (positiver Versatz),
2. F(P_S) ist nicht-degeneriert, also Flächeninhalt(F(P_S)) > 0
   (folgt aus 1 und der Nichtentartetheit von P, da starre
   Translation den Flächeninhalt erhält),
3. ⟨n_a, e_z⟩ > Toleranzen.WINKEL_EPS  (D ist nicht horizontal —
   bei α(D) = 0 spricht man im Innenausbau von einer **Decke**, nicht
   von einer Dachschräge; siehe Edge Cases).

## Wohldefiniertheit

- **Existenz**: Für jede geneigte Dachfläche D mit zugeordnetem
  Dachaufbau A positiver Gesamtdicke ist S(D, A) konstruktiv
  wohldefiniert; die starre Translation x ↦ x − d_A · n_a ist
  bijektiv und ebenenerhaltend.
- **Eindeutigkeit**: S(D, A) ist eindeutig bestimmt durch D und A
  (über d_A = Σ d_j und n_a). Wechselt der Aufbau A (z. B. durch
  zusätzliche Innenbekleidung), ändert sich d_A und damit S
  entsprechend.
- **Unabhängigkeit vom Stützpunkt p₀**: Die Konstruktion verwendet
  p₀ nur, um E zu beschreiben; das Ergebnis hängt nur von der
  Trägerebene als Punktmenge ab, nicht von der Wahl von p₀ ∈ E.
  Eine andere Wahl p₀' ∈ E liefert dieselbe Ebene E_S.
- **Konsistenz mit Dachaufbau**: Die Dicke d_A wird ausschließlich
  aus der Schichtfolge 𝒮 gebildet (siehe `dachaufbau`); damit ist
  S(D, A) konsistent mit der dort gewählten Schichtmodellierung
  (insbesondere auch bei nur einer einzelnen Schicht).
- **Parallelität zur Dachfläche**: E und E_S haben dieselbe
  Normale n_a (bis aufs Vorzeichen) und sind daher parallel; der
  Abstand zwischen ihnen ist exakt d_A.
- **Inversion**: Aus S lässt sich D zurückgewinnen über die
  Translation x ↦ x + d_A · (−n_S) = x + d_A · n_a. Die Konstruktion
  ist also umkehrbar.
- **Nicht-Zirkularität**: Die Definition stützt sich nur auf
  `ebene`, `polygon`, `vektor`, `einheitsvektor`, `dachflaeche`,
  `dachaufbau` und `toleranzen`. Sie kommt nicht in ihrer eigenen
  Definition vor.

## Erläuterung (nicht normativ)

Die Dachschräge ist die **vom Wohnraum aus sichtbare Untersicht der
Dachkonstruktion**. In einem zum Wohnraum ausgebauten Dachgeschoss
ist sie die Fläche, die der Bewohner über sich sieht — bei
Sichtsparrenkonstruktionen direkt die Holzschalung zwischen den
Sparren, bei klassischer Trockenbau-Ausführung die Innenbekleidung
aus Gipsplatten oder Holzpaneelen.

Geometrisch ist die Dachschräge die zur Dachfläche **parallele**
innenseitige Bezugsfläche, verschoben um die Dicke des Dachaufbaus
nach innen. Während die Dachfläche D die **außen**-bezogene
Geometrie für Eindeckung, Schneelast und Windlast trägt, ist die
Dachschräge S(D, A) die **innen**-bezogene Geometrie für:

- Raumvolumen und Wohnfläche (Anrechenbarkeit nach jeweiligem
  kantonalem Baurecht bzw. nach DIN 277),
- Stehhöhe und ergonomische Möblierungsplanung,
- Innenausbau-Flächen (Bekleidung mit Gipsplatten nach DIN 18181,
  Holzpaneelen, Sichtschalung),
- Lichtreflexion und visuelle Wirkung des Dachgeschossraumes.

**Verhältnis zu Dachneigung und Dachfläche** (häufige
Verwechslung):

- **Dachneigung** ist ein **Winkel** (Skalar in [0, π/2]), kein
  geometrisches Objekt.
- **Dachfläche** ist die **außenseitige** Bezugsfläche.
- **Dachschräge** ist die **innenseitige** Bezugsfläche.
- Dachfläche und Dachschräge haben dieselbe Dachneigung α (sie sind
  parallel); der Winkel α ist eine Eigenschaft beider.

**Idealisierung**: Die Definition setzt voraus, dass der Dachaufbau
in der relevanten Dicke d_A **konstant** über der Dachfläche ist.
Bei Aufdoppelungen, Gefälledämmungen oder lokaler Mehrlagigkeit
weicht die reale Innensicht von der idealisierten Dachschräge ab;
solche Fälle erfordern eine ortsabhängige Schichtmodellierung
(siehe `dachaufbau`-Erläuterung).

**Bauphysikalische Relevanz**: Die Dachschräge ist die
**raumseitige Bauteilebene** im Sinne von DIN 4108-3; an ihr werden
die Innenraumtemperatur und -feuchte angesetzt, was für die
Tauwasserrechnung im Schichtaufbau maßgeblich ist.

## Beziehungen

- **Oberbegriff**: `ebene` mit polygonaler Berandung (analog zu
  `dachflaeche`).
- **Verwandt (parallel-versetzt)**: `dachflaeche`. Eine Dachschräge
  ist die zur Dachfläche parallele, raumseitige Versatz-Fläche.
- **Bestandteile (partitiv)**: Polygonpunkte v_i − d_A · n_a;
  Trägerebene E_S; raumseitige Normale n_S = −n_a.
- **Verwendungskontext**:
  - **Innenausbau** (Bekleidung mit Gipsplatten nach DIN 18181,
    Holzschalung, Sichtsparren): die Dachschräge ist die Bezugs-
    fläche für die Bekleidungsmontage.
  - **Wohnflächenrechnung**: Stehhöhe und anrechenbare Fläche
    werden über die Schnittlinie der Dachschräge mit horizontalen
    Höhenniveaus (z. B. 1,00 m, 2,00 m) bestimmt.
- **Abgrenzung**:
  - **Dachfläche** (`dachflaeche`): außenseitige Bezugsfläche; die
    Dachschräge ist die zugehörige innenseitige Versatzfläche um
    d_A · (−n_a). Beide sind Flächen, parallel, aber verschieden.
  - **Dachneigung** (`dachneigung`): Winkel α, kein
    geometrisches Objekt. Im umgangssprachlichen Gebrauch oft mit
    Dachschräge verwechselt; im Glossar trennscharf.
  - **Dachseite** (`dachseite`, eigener Eintrag): eine Dachfläche
    unter Orientierungs-Annotation (Wetterseite, Sonnenseite).
    Außenseitig bezogen, nicht innenseitig.
  - **Dachhaut** (`dachhaut`): geometrische Außen-Hüllfläche über
    dem Dachaufbau. Die Dachschräge ist das innenseitige
    Gegenstück, nicht synonym.
  - **Dachaufbau** (`dachaufbau`): die materielle Schichtfolge
    zwischen Dachfläche und Dachschräge. Die Dachschräge ist die
    untere (raumseitige) Hüllfläche dieser Schichtfolge.
  - **Decke**: bei α(D) = 0 (Flachdach) wird die innenseitige
    Bezugsfläche **Decke** genannt, nicht Dachschräge. Die
    Bedingung 3 in der Definition schließt diesen Fall aus.
  - **Kniestockwand**: senkrechte Wand zwischen Dachschräge und
    Geschossdecke; eigener Begriff, hier nicht weiter behandelt.
- **Entartet-Variante**: `Entartet.KeineInnenSichtbar` —
  pragmatisch, falls der Dachgeschossraum durch eine abgehängte
  Decke gegen den Sparrenraum abgetrennt ist und die Dachschräge
  nicht als raumseitig sichtbare Fläche existiert; die formale
  Geometrie bleibt aber konstruierbar, die Entartung ist
  semantisch (Sichtbarkeit), nicht geometrisch.

## Implementierungshinweis

Datentyp (Domänen-Schicht, Kotlin, Schicht `domain.bauteil`):

```
package domain.bauteil

import domain.geometrie.Ebene
import domain.geometrie.Polygon
import domain.geometrie.Vektor
import domain.geometrie.Einheitsvektor
import domain.Toleranzen

/**
 * Dachschräge: raumseitige Bezugsfläche zu einer Dachfläche,
 * parallel verschoben um die Gesamtdicke des Dachaufbaus.
 * Glossar: hg_dachschraege.md
 */
data class Dachschraege(
    val traeger: Ebene,                 // E_S
    val umriss: Polygon,                // P_S, Eckpunkte ∈ traeger
    val raumseitigeNormale: Einheitsvektor   // n_S = −n_a
) {
    init {
        // Invarianten siehe unten
    }

    companion object {
        /**
         * Konstruiert die Dachschräge aus einer Dachfläche und ihrem
         * Dachaufbau über starre Translation um −d_A · n_a.
         */
        fun ausDachflaeche(
            d: Dachflaeche,
            a: Dachaufbau
        ): Resultat<Dachschraege, EntartetGeometrie> {
            val dA = a.gesamtdicke()
            if (dA <= Toleranzen.LAENGE_EPS)
                return Resultat.Fehler(EntartetGeometrie.NullVersatz)
            val nA = d.aeussereNormale
            // Versatz nach innen
            val versatz = Vektor(-dA * nA.x, -dA * nA.y, -dA * nA.z)
            val neuesPolygon = Polygon(
                d.umriss.eckpunkte.map { it + versatz }
            )
            val nS = Einheitsvektor.ausVektor(
                Vektor(-nA.x, -nA.y, -nA.z)
            ).werteOder { return Resultat.Fehler(it) }
            val neueEbene = Ebene.ausPunktUndNormale(
                neuesPolygon.eckpunkte.first(), nS
            )
            return Resultat.Erfolg(
                Dachschraege(neueEbene, neuesPolygon, nS)
            )
        }
    }

    sealed class Entartet {
        object KeineInnenSichtbar : Entartet()    // semantisch, nicht geometrisch
        object NullVersatz : Entartet()           // d_A ≤ LAENGE_EPS
        object Horizontal : Entartet()            // α(D) ≈ 0 → Decke, nicht Dachschräge
    }
}
```

- **Einheit**: Polygonpunkte in mm (Double); Normale dimensionslos.
- **Invarianten** (in `init`-Block bzw. Factory prüfen, niemals
  Exception werfen):
  1. Alle Eckpunkte ∈ `traeger` (mit Toleranzen.LAENGE_EPS).
  2. Polygon-Flächeninhalt > Toleranzen.FLAECHE_EPS.
  3. ‖raumseitigeNormale‖ ∈ 1 ± Toleranzen.NORM_EPS.
  4. ⟨raumseitigeNormale, e_z⟩ ≤ Toleranzen.WINKEL_EPS  (n_S zeigt
     in die untere Halbkugel oder Horizontale, da n_a in die obere).
- **Edge Cases**:
  - **d_A → 0** (kein Dachaufbau, etwa offene Pergola): Konstruktion
    liefert `Resultat.Fehler` bzw. `EntartetGeometrie.NullVersatz`. Die
    Dachschräge wäre mit der Dachfläche identisch und damit kein
    eigenständiges Objekt.
  - **α(D) = 0** (Flachdach): per Definition ausgeschlossen
    (Bedingung 3). Die innenseitige Fläche ist dann eine **Decke**;
    die Domänen-Klasse liefert `Entartet.Horizontal`.
  - **Nicht-konstanter Aufbau** (Aufdoppelung, Gefälledämmung):
    nicht von dieser Definition abgedeckt; die Idealisierung als
    Skalar d_A versagt. Erweiterung über ortsabhängige Dicke d_A(x)
    erforderlich.
  - **Abgehängte Innenbekleidung**: bildet eine **zweite**
    raumseitige Fläche unterhalb der idealisierten Dachschräge;
    formale Behandlung über einen erweiterten `Dachaufbau`, der
    die Innenbekleidung als zusätzliche Schicht trägt, und
    Re-Konstruktion der Dachschräge mit aktualisiertem d_A.
  - **Sichtsparren-Konstruktion**: die Dachschräge ist nicht
    durchgängig eine ebene Fläche, sondern wechselt zwischen
    Sparren-Untersicht und Schalungs-Untersicht. Idealisiert wird
    sie auf die unterste, raumseitig sichtbare Holzschicht
    bezogen; eine differenzierte Modellierung erfolgt erst in
    Folgearbeit (eigener Eintrag `sichtdach`).
- **Abgeleitete Operationen**:
  - `dachneigung(): Double` (Radiant) = arccos(⟨−raumseitigeNormale,
    e_z⟩); identisch zur Dachneigung der zugehörigen Dachfläche.
  - `flaecheninhalt(): Double` (mm²) aus dem Umriss-Polygon;
    identisch zur Dachfläche, da starre Translation
    flächenerhaltend ist.
  - `stehhoehenLinie(z₀: Double): Strecke?` — Schnitt der Dachschräge
    mit der Horizontalebene z = z₀, als Hilfsgröße für
    Wohnflächenrechnungen (z. B. z₀ = 2000 mm). In Folgearbeit
    näher zu definieren.

## Quellen

**Primär (normativ):**

- SIA 232/1:2020, „Geneigte Dächer", Schweizerischer Ingenieur- und
  Architektenverein, Zürich, Abschnitt 2.
- DIN 4108-3:2018-10, „Wärmeschutz und Energie-Einsparung in
  Gebäuden – Teil 3: Klimabedingter Feuchteschutz".
- DIN 18181:2014-08, „Gipsplatten im Hochbau – Verarbeitung",
  Abschnitt 5.

**Sekundär:**

- Lignum (Hrsg.): *Lignatec — Geneigte Dächer in Holzbauweise.*
  Lignum, Zürich, aktuelle Auflage.
- Mönck, W.; Rug, W.: *Holzbau – Bemessung und Konstruktion.*
  16. Auflage, Beuth Verlag 2015.
- Gerner, M.: *Fachwerk – Instandsetzung, Sanierung, Neubau.*
  DVA, 7. Auflage 2007.
- Holzbau Deutschland, Merkblatt „Begriffe und Klassifizierungen
  für den Holzbau".

**Korpus (nicht autoritativ):**

- Wikipedia, Lemma „Dachschräge" (abgerufen 2026-05-08).
