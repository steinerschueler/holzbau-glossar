---
id: ebene
benennung: Ebene
synonyme: [Hyperebene_in_R3, "affine Ebene"]
abgelehnte_benennungen: [Fläche, Plane, "plane"]
oberbegriff: null
begriffstyp: generisch
voraussetzungen: [punkt, vektor]
abgrenzung_zu: [polygon, dachflaeche, gerade, halbraum]
status: entwurf
subglossar_pendant: notwendig
quellen_primär:
  - "DIN ISO 80000-2:2022-08, Abschnitt 2 (Geometrie), Symbole und Bezeichnungen für die Ebene und die Hesse-Normalform."
quellen_sekundär:
  - "Bronstein, I. N. et al.: Taschenbuch der Mathematik. Kap. 3.5.2 'Ebenen im Raum', insbesondere Hesse'sche Normalform."
  - "Fischer, G.: Lineare Algebra. Kap. 1 'Affine Geometrie'."
  - "Bär, C.: Elementargeometrie. Kap. 5 'Ebenen im dreidimensionalen Raum'."
  - "Hesse, L. O.: Vorlesungen aus der analytischen Geometrie der geraden Linie, des Punktes und des Kreises in der Ebene. Teubner, Leipzig 1865 (historische Quelle der Hesse'schen Normalform)."
quellenkonflikt: |
  Holzbau-Normen verwenden den Begriff Ebene als gegeben (z. B.
  „Dachebene", „Fußebene"). DIN ISO 80000-2 verzeichnet die Hesse-
  Normalform, definiert die Ebene jedoch nicht axiomatisch. Eigene
  Festlegung: eine Ebene ist die Punktmenge { x ∈ ℝ³ | ⟨n, x − p₀⟩ = 0 }
  für einen Stützpunkt p₀ und einen Nicht-Nullvektor n. Die Hesse-
  Normalform mit ‖n‖ = 1 ist eine kanonische Repräsentation. Diese
  Festlegung ist konsistent mit Bronstein, Fischer, Bär und ISO
  80000-2.
---

## Prosa-Definition

Eine **Ebene** ist ein zweidimensionaler affiner Unterraum von ℝ³,
gegeben als die Menge aller Punkte, die einen festen Stützpunkt p₀
mit Verschiebungsvektor v erreichen, der rechtwinklig zu einem fest
gewählten Nicht-Nullvektor n (Normalenvektor) steht; in der
**Hesse-Normalform** wird n auf Einheitslänge normiert.

## Mathematische Definition

Sei

- p₀ ∈ ℝ³ ein **Stützpunkt**,
- n ∈ ℝ³ \ {0} ein **Normalenvektor**.

Dann ist die durch (p₀, n) definierte **Ebene** E ⊂ ℝ³ die Menge

```
E(p₀, n) := { x ∈ ℝ³ | ⟨n, x − p₀⟩ = 0 }.
```

Äquivalent in **Hesse-Normalform**: Sei n_hat := n / ‖n‖ ∈ S² und
d := ⟨n_hat, p₀⟩ ∈ ℝ. Dann gilt

```
E(p₀, n) = { x ∈ ℝ³ | ⟨n_hat, x⟩ = d }.
```

Das Paar (n_hat, d) ∈ S² × ℝ ist die **Hesse-Normalform** und
repräsentiert E bis auf das Vorzeichen (n_hat, d) ↔ (−n_hat, −d) eindeutig.

Wesentliche abgeleitete Größen für x ∈ ℝ³:

- **Vorzeichenbehafteter Abstand**: d_E(x) := ⟨n_hat, x⟩ − d (in mm).
- **Unsignierter Abstand**: |d_E(x)| (in mm).
- **Orthogonale Projektion**: π_E(x) := x − d_E(x) · n_hat.
- **Halbräume**: H⁺ := { x | d_E(x) > 0 }, H⁻ := { x | d_E(x) < 0 }.

## Wohldefiniertheit

- Die Punktmenge E(p₀, n) ist unabhängig von der Wahl des
  Stützpunktes innerhalb E: für jedes p₀' ∈ E gilt
  E(p₀', n) = E(p₀, n), denn aus ⟨n, p₀' − p₀⟩ = 0 folgt für jedes
  x mit ⟨n, x − p₀⟩ = 0 auch ⟨n, x − p₀'⟩ = ⟨n, x − p₀⟩ −
  ⟨n, p₀' − p₀⟩ = 0.
- Skaleninvarianz im Normalenvektor: für jedes λ ∈ ℝ \ {0} gilt
  E(p₀, λ·n) = E(p₀, n). Die Hesse-Normalform fixiert ‖n_hat‖ = 1
  und reduziert die Mehrdeutigkeit auf das Vorzeichen.
- Vorzeichenmehrdeutigkeit: (n_hat, d) und (−n_hat, −d) beschreiben dieselbe
  Ebene. Die Wahl der Orientierung ist eine zusätzliche Information
  (Außennormale bei Dachflächen, eigener Eintrag).
- Existenz: Für jedes (p₀, n) mit n ≠ 0 ist E nicht-leer (p₀ ∈ E)
  und enthält tatsächlich unendlich viele Punkte (jede Verschiebung
  von p₀ um einen zu n orthogonalen Vektor liegt in E).
- Nicht-Zirkularität: Definition stützt sich nur auf Punkt, Vektor
  und Skalarprodukt.

## Erläuterung (nicht normativ)

Die Ebene ist das geometrische Primitiv für alle ebenen Bauteile
und Bezugsflächen im Holzbau: Dachfläche, Fußebene (Dachfußebene
auf Höhe der Wandkrone), Wandebene, Schnittebenen für Risse.

Der **Reissboden** der traditionellen Zimmerei materialisiert eine
1:1-Ebene als Anriss-Untergrund — eines der historischen Welt-
Anschauungs-Objekte einer ebenen Fläche im Holzbau (Wikipedia
„Aufschnüren", „Schiftung").

**Sprach-Stolperstein „-ebene" im Holzrahmenbau.** Im modernen
Holzrahmenbau treten Komposita wie **Installationsebene**
(Aufbaustärke typisch 60–80 mm) und **Hinterlüftungsebene** auf,
die berufssprachlich „Ebene" im Namen tragen, fachlich aber
**Schichten mit Dicke** bezeichnen (begrenzt durch je zwei
parallele Ebenen im Sinne dieses Eintrags). Sie sind im engeren
geometrischen Sinn keine Ebenen.

Anschauliche Lesarten:

- **Stützpunkt + Normale**: ein Punkt der Ebene plus die Richtung
  „aus der Ebene heraus".
- **Hesse-Normalform** (n_hat, d): die Ebene als Höhenlinie der
  linearen Funktion x ↦ ⟨n_hat, x⟩ auf dem Niveau d. Der Wert d ist
  geometrisch der vorzeichenbehaftete Abstand vom Ursprung in
  Richtung n_hat.
- **Drei Punkte**: jede Ebene ist durch drei nicht-kollineare
  Punkte p₁, p₂, p₃ eindeutig festgelegt; n = (p₂ − p₁) × (p₃ − p₁).

## Beziehungen

- **Oberbegriff**: zweidimensionaler affiner Unterraum von ℝ³
  (formal). Im Glossar Primitiv.
- **Teilbegriffe / Rollen**:
  - **Dachfläche** verwendet eine Ebene als Träger.
  - **Wandebene**, **Fußebene**, **Schnittebene** sind weitere
    rollenbezogene Verwendungen (eigene Einträge in Folgearbeit).
- **Abgrenzung**:
  - **Polygon**: ein endliches, ebenes, geschlossenes Linien-
    stückgebilde innerhalb einer Ebene; nicht die Ebene selbst.
  - **Dachfläche**: ein durch ein Polygon berandeter, beschränkter
    Teil einer Ebene mit zusätzlicher Orientierung; nicht die
    Ebene selbst.
  - **Halbraum**: einer der beiden offenen oder abgeschlossenen
    Bereiche, in die ℝ³ durch eine orientierte Ebene zerlegt wird;
    eigener Eintrag.
  - **Gerade**: ein eindimensionaler affiner Unterraum von ℝ³;
    geringere Dimension.
  - **Schicht** (Holzrahmenbau-Verwendung): ein dreidimensionaler
    Volumen-Bereich, begrenzt durch zwei näherungsweise parallele
    Ebenen, mit ausgewiesener Dicke (Installationsebene 60–80 mm,
    Hinterlüftungsebene, Dämmebene). Eine Schicht ist nicht die
    Ebene selbst, sondern wird durch zwei Ebenen aufgespannt; das
    berufssprachliche Suffix „-ebene" im Schichtnamen ist ein
    Sprach-Stolperstein und keine geometrische Aussage.

## Implementierungshinweis

Datentyp (Domänen-Schicht, Kotlin, Schicht `domain.geometrie`):

```
data class Ebene(
    val stuetzpunkt: Punkt,   // p₀
    val normale: Vektor       // n, ‖normale‖ > Toleranzen.NORM_EPS
) {
    init {
        // ‖normale‖ > Toleranzen.NORM_EPS, sonst Entartet.NullNormale
    }
}

// Kanonische Repräsentation (Hesse-Normalform):
data class EbeneHesse(
    val einheitsNormale: Vektor,  // n_hat, ‖n_hat‖ ≈ 1
    val abstandUrsprung: Double    // d = ⟨n_hat, p₀⟩, in mm
)
```

- **Einheit**: Stützpunkt und Abstandswert in mm. Die Normale ist
  in der Standard-Repräsentation `Ebene` nicht zwingend normiert;
  in `EbeneHesse` ist sie auf 1 normiert.
- **Invarianten** (in `init` bzw. Factory):
  1. ‖normale‖ > Toleranzen.NORM_EPS (sonst keine Ebene, sondern
     entartet → `Entartet.NullNormale`).
  2. Alle Komponenten finit (kein NaN, kein ±∞).
- **Konstruktoren**:
  - `Ebene.ausStuetzpunktUndNormale(p0, n): Resultat<Ebene, EntartetGeometrie>`
  - `Ebene.ausDreiPunkten(p1, p2, p3): Resultat<Ebene, EntartetGeometrie>` mit
    Fehler-Variante `Entartet.Kollinear`, falls
    ‖(p₂ − p₁) × (p₃ − p₁)‖ ≤ Toleranzen.NORM_EPS.
  - `Ebene.ausHesseNormalform(nHat, d): Resultat<Ebene, EntartetGeometrie>`.
- **Edge Cases / Entartet-Varianten**:
  - **Nullnormale** (n = 0): `Entartet.NullNormale`. Keine Ebene
    definierbar.
  - **Drei kollineare Punkte**: `Entartet.Kollinear`. Die Drei-
    Punkte-Konstruktion liefert keinen eindeutigen Normalen-
    vektor.
  - **Nicht-finite Koordinaten**: `Entartet.NichtFinit`.
  - **Numerisch fast parallele Inputs** (Konstruktion aus zwei
    Strecken, deren Kreuzprodukt nahe null ist): `Entartet.FastKollinear`,
    konfigurierbarer Schwellwert `Toleranzen.KOLLINEAR_EPS`.
- **Abgeleitete Operationen** (`EbeneOps.kt`):
  - `fun einheitsNormale(): Vektor` = normale.normiert().werteOder { error("Invariante 1 verletzt") }
    (zur Laufzeit nie betroffen, durch Invariante 1 abgesichert).
  - `fun hesse(): EbeneHesse`.
  - `fun signierterAbstand(p: Punkt): Double` =
    ⟨einheitsNormale(), p − stuetzpunkt⟩, in mm. Vorzeichen folgt
    der Orientierung von `normale`.
  - `fun abstand(p: Punkt): Double` = |signierterAbstand(p)|.
  - `fun projizieren(p: Punkt): Punkt` = p − signierterAbstand(p) ·
    einheitsNormale().
  - `fun enthaelt(p: Punkt, eps: Double = Toleranzen.LAENGE_EPS):
    Boolean` = abstand(p) ≤ eps.
  - `fun umkehrenOrientierung(): Ebene` = Ebene(stuetzpunkt, −normale)
    (gleiche Punktmenge, entgegengesetzte Orientierung).
- **Bemerkung zur Orientierung**: Die Ebene als Punktmenge ist
  nicht orientiert; der Datentyp `Ebene` trägt jedoch durch das
  Vorzeichen von `normale` eine Orientierung mit. Konsumenten,
  die nur die Punktmenge benötigen (z. B. Schnitttests), dürfen
  sich darauf nicht verlassen; Konsumenten, die Halbräume
  unterscheiden (z. B. Dachfläche, Außennormale), nutzen das
  Vorzeichen explizit.

## Quellen

**Primär (normativ):**

- DIN ISO 80000-2:2022-08, „Größen und Einheiten – Teil 2: Mathematik",
  Abschnitt 2.

**Sekundär:**

- Bronstein, I. N.; Semendjajew, K. A.; Musiol, G.; Mühlig, H.:
  *Taschenbuch der Mathematik.* Kap. 3.5.2.
- Fischer, G.: *Lineare Algebra.* Springer Spektrum, aktuelle Auflage.
- Bär, C.: *Elementargeometrie.* Springer Spektrum.
- Hesse, L. O.: *Vorlesungen aus der analytischen Geometrie der
  geraden Linie, des Punktes und des Kreises in der Ebene.*
  Teubner, Leipzig 1865.

**Korpus (nicht autoritativ):**

- Wikipedia, Lemmata „Ebene (Mathematik)" und „Hesse'sche Normalform"
  (abgerufen 2026-05-07).
- wissenwiki.de „Installationsebene"; bubiza.de „Installationsebene"
  — Beleg für Holzrahmenbau-Kompositum mit Aufbaustärken 60–80 mm
  (Schicht trotz „-ebene"-Benennung; abgerufen 2026-05-14).
- Wikipedia, Lemma „Fachbegriffe des Zimmererhandwerks" —
  Hinterlüftungsebene als analog konstruiertes Schicht-Kompositum
  (abgerufen 2026-05-14).
- Wikipedia, Lemmata „Aufschnüren" und „Schiftung" — Reissboden
  als ebener Bretterboden, auf dem ein Dachprofil im Maßstab 1:1
  aufgeschnürt wird (abgerufen 2026-05-14).
