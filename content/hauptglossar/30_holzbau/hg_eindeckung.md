---
id: eindeckung
benennung: Eindeckung
synonyme: [Dacheindeckung, Dachdeckung, Bedachung]
abgelehnte_benennungen: [Dachhaut, Dachabdichtung, Dachaufbau, "roof covering", "roofing", "roof skin"]
oberbegriff: schicht
begriffstyp: generisch
voraussetzungen: [schicht, dachflaeche, dachaufbau, dachhaut, dachneigung, polygon, ebene, toleranzen]
abgrenzung_zu: [dachhaut, dachaufbau, dachflaeche, dachabdichtung, unterdach, latte, konterlatte, traglattung, konterlattung]
status: entwurf
theorie_pflichtig: required
quellen_primär:
  - "SIA 232/1:2011 (mit Korrigendum 232/1-C1:2013) 'Geneigte Dächer', Schweizerischer Ingenieur- und Architektenverein, Abschnitt 1 (Begriffe) und Abschnitt 2 (Aufbau und Eindeckung geneigter Dächer)."
  - "DIN 18338:2019-09 'VOB Teil C: Allgemeine Technische Vertragsbedingungen für Bauleistungen — Dachdeckungsarbeiten', Abschnitt 0 (Hinweise zum Leistungsbereich). Titel seit 2019 ohne Bestandteil 'Dachabdichtungsarbeiten'; die Abdichtungs-Inhalte sind in DIN 18336 ausgelagert."
  - "DIN 18336:2019-09 'VOB Teil C: Abdichtungsarbeiten' (aus DIN 18338-Aufspaltung 2019); zur normativen Abgrenzung zitiert, kein Bestandteil der Eindeckungs-Definition."
  - "DIN EN 1304:2013-08 'Dachziegel und Formziegel — Begriffe und Produktanforderungen', Abschnitt 3 (Begriffe)."
  - "DIN EN 14782:2006-03 'Selbsttragende Metallbleche für Bedachung, äußere Bekleidung und innere Auskleidung — Produktanforderungen und Prüfverfahren'."
  - "DIN EN 14783:2013-06 'Vollständig unterstützte Bleche und Bänder aus Metall für Bedachungen, äußere Bekleidungen und innere Auskleidungen'."
  - "DIN EN 50583-2:2016-12 'Photovoltaik in Gebäuden — Teil 2: Anforderungen an BIPV-Systeme'."
  - "ZVDH-Fachregel für Dachdeckungen mit Dachziegeln und Dachsteinen, Ausgabe 2024-04."
  - "ZVDH-Fachregel Reetdach, Ausgabe 2025-03."
  - "ISO 6707-1:2020 'Buildings and civil engineering works — Vocabulary — Part 1: General terms'."
quellen_sekundär:
  - "Lignum (Hrsg.): Lignatec 'Geneigte Dächer in Holzbauweise', Lignum, Zürich, aktuelle Auflage."
  - "Lignum (Hrsg.): Holzbautabellen HBT, Lignum, Zürich, aktuelle Auflage, Kap. 'Dachaufbau / Eindeckung'."
  - "Mönck, W.; Rug, W.: Holzbau – Bemessung und Konstruktion. 16. Aufl., Beuth Verlag 2015."
  - "Gerner, M.: Fachwerk – Instandsetzung, Sanierung, Neubau. DVA, 7. Aufl. 2007."
  - "AGZ (Arbeitsgemeinschaft Ziegelindustrie Schweiz): Mindestdachneigungen 2022."
  - "Holzbau Deutschland, Merkblatt 'Begriffe und Klassifizierungen für den Holzbau'."
  - "Polybau / suissetec: Wegleitung zur Norm SIA 232/1."
  - "Recherchebericht docs/recherche/2026-05-14_hg_eindeckung.md."
quellenkonflikt: |
  **Trennung Dachdeckung ↔ Dachabdichtung.** Die DACH-Normen ziehen
  seit der Ausgabe 2019 von VOB/C eine **harte Linie** zwischen
  Dachdeckung (geneigtes Dach, regensicher, schuppige
  Einzelelemente) und Dachabdichtung (Flachdach, wasserdicht,
  durchgehende Membran). Bis 2016 hieß DIN 18338 noch
  „Dachdeckungs- und Dachabdichtungsarbeiten"; mit der Ausgabe
  2019-09 ist „Dachabdichtungsarbeiten" aus dem Titel entfernt
  und in DIN 18336 ausgelagert. SIA 232/1 trennt analog gegen
  SIA 271 „Abdichtungen von Hochbauten". Die Eindeckung dieses
  Eintrags ist deshalb **strikt auf das geneigte Dach mit
  regensicherer schuppiger Schicht** festgelegt; die wasserdichte
  Flachdach-Schicht wird unter `dachabdichtung` (Forward-Verweis,
  Trigger Kategorie A) eigenständig geführt.

  **Synonymie „Dachdeckung" / „Dacheindeckung".** Im DACH-Korpus
  sind „Eindeckung", „Dacheindeckung", „Dachdeckung" und
  (älter, weiter) „Bedachung" funktional austauschbar; Branchen-
  Tendenz: „Eindeckung" beim Werkstoff, „Dachdeckung" beim Werk
  (DIN 18338-Werkbegriff). Normativ identisch — alle drei sind
  Synonyme dieses Eintrags. **Migration in `hg_dachhaut.md`
  erledigt** (im selben R-Schritt nachgezogen): „Dachdeckung" und
  „Dacheindeckung" stehen dort nun in `abgelehnte_benennungen:`
  (nicht in `synonyme:`), weil sie nicht die geometrische Hüllfläche,
  sondern die materielle äußere Schicht bezeichnen.

  **Wahl des `oberbegriff: schicht`.** Der Oberbegriff `schicht`
  (`hg_schicht.md`) ist im selben R-Schritt entstanden und sammelt
  alle Funktionsschichten des Dachaufbaus. `dachhaut` schied als
  Oberbegriff aus: die Dachhaut ist die geometrische Hüllfläche
  **über** der Eindeckung, also ein geometrisches Resultat, nicht
  eine fachliche Spezialisierungs-Linie der materiellen Schicht.
  `dachaufbau` ist Aggregat-Träger der Eindeckung als Schicht, aber
  im ISO-704-Sinne keine Spezialisierungs-Linie.

  **Wahl des `begriffstyp: generisch`.** Die Eindeckung trägt
  interne Struktur (Material + Profil + Lagigkeit + Befestigung)
  und eine sealed-Hierarchie pro Material (Ziegeleindeckung,
  Schiefereindeckung, Metalleindeckung mit Subtypen Stehfalz und
  Trapezprofil, Bitumenschindeleindeckung, Holzschindeleindeckung,
  Reeteindeckung, Solareindeckung, Glaseindeckung). Sie ist nicht
  Lebenszyklus-gekoppelt an `dachaufbau` (eine Eindeckung kann
  erneuert werden, ohne dass der Aufbau insgesamt entfernt wird);
  damit nicht `partitiv`. Die Einzelelemente (jeder Ziegel, jede
  Tafel) werden im Geltungsbereich des ersten Tools nicht mit
  eigener Identität modelliert; damit vorerst nicht `aggregat`.
  Sobald Einzelmodul-Identität (z. B. BIPV-Modul-IDs) verlangt
  ist, kann der Begriffstyp zu `aggregat` migrieren.

  **Quellenzugriff.** Detail-Lesung der Original-Normtexte (SIA
  232/1 Abschnitt 1, DIN 18338:2019-09 Abschnitt 0, DIN EN 1304,
  DIN EN 14782) war in der Recherche nicht durchführbar (Paywall
  / WebFetch denied); Aussagen stützen sich auf Norm-Vorwort-
  Snippets, DIN-Media-Übersichten und auf die ZVDH-Fachregeln
  als Sekundärträger der Norm-Inhalte (Tier Hoch). Die im
  Erläuterungsblock genannten Mindestneigungs-Richtwerte sind
  **Branchen-Orientierungswerte**, nicht Normwerte dieses Glossars.
---

## Prosa-Definition

Eine **Eindeckung** ist die äußerste materielle Schicht eines
geneigten Daches, gebildet aus überlappten oder gefalzten,
schuppig angeordneten Einzelelementen (Ziegel, Schindeln,
Tafeln, Bahnen oder Module), die den Niederschlag konstruktiv
über die Dachneigung in die Rinne ableiten und dabei
**regensicher**, jedoch nicht zwingend wasserdicht, ausgeführt
ist.

## Mathematische Definition

Sei

- D = (E, P, n_a) eine Dachfläche im Sinne von `dachflaeche`
  mit Trägerebene E, Umrisspolygon P und nach außen gerichteter
  Einheits-Normalen n_a ∈ S²,
- α(D) = arccos(⟨n_a, e_z⟩) ∈ [0, π/2) die Dachneigung
  von D im Sinne von `dachneigung`,
- A = (𝒟, 𝒮, H) ein Dachaufbau im Sinne von `dachaufbau`
  mit Trägerflächen 𝒟 = { D₁, …, D_m }, geordneter
  Schichtfolge 𝒮 = (S₁, …, S_k) (von innen nach außen) und
  abgeleiteter Dachhaut H im Sinne von `dachhaut`,
- F = ⋃_{i=1..m} F(P_i) ⊂ ℝ³ der Trägerbereich des Aufbaus,
- α_min ∈ (0, π/2) ein material-spezifischer Schwellwert
  (**Mindestdachneigung**), unterhalb dessen die schuppige
  Anordnung allein keine Regensicherheit mehr leistet (siehe
  Erläuterung).

Eine **Eindeckung** ist die äußerste Schicht S_k ∈ 𝒮 eines
Dachaufbaus A genau dann, wenn

1. **Außenposition:** S_k ist die nach außen weisende, am
   höchsten gelegene Schicht des Aufbaus 𝒮; die obere
   Hüllfläche der Außenseite von S_k ist die Dachhaut H = H(A)
   im Sinne von `dachhaut`.
2. **Geneigte Trägerfläche:** Für jede Dachfläche
   D_i ∈ 𝒟 gilt α(D_i) ≥ α_min(S_k) mit material-spezifischem
   α_min(S_k) > 0. Anders ausgedrückt: F enthält keine
   horizontale Teilfläche, die unterhalb der für das
   Eindeckungs-Material zulässigen Mindestneigung liegt.
3. **Schuppige Struktur:** S_k ist als endliche, geordnete
   Familie σ = (σ₁, …, σ_N) von Einzelelementen σ_j ⊂ ℝ³
   realisiert (Ziegel, Schindeln, Tafeln, Bahnen, Module), für
   die paarweise eine **Überlappungsrelation** ≻ ⊂ σ × σ
   existiert mit der Eigenschaft, dass für jeden Punkt q ∈ F
   die nach oben gerichtete vertikale Halbgerade
   { q + t·e_z | t ≥ 0 } mindestens ein σ_j trifft (Decke
   des Trägerbereichs durch die schuppige Familie).
4. **Regensicherheit über Neigung:** Niederschlagswasser, das
   auf S_k fällt, wird ausschließlich durch die Dachneigung
   α(D_i) und die Überlappungsrelation ≻ in Richtung der
   Falllinie abgeführt; eine flächige Wasserundurchlässigkeit
   wie bei einer Membran (siehe `dachabdichtung`, Forward-
   Verweis) wird **nicht** gefordert.

Die **Eindeckung** des Daches ist dann das Paar

```
Eindeckung := (S_k, σ)
```

mit S_k als der Schicht-Funktionsklasse (im Sinne der
Aufbau-Funktionsenumeration `EINDECKUNG`) und σ als der
endlichen Familie ihrer Einzelelemente.

## Wohldefiniertheit

- **Existenz.** Für jeden Dachaufbau A = (𝒟, 𝒮, H) mit
  Außenabschluss S_k.funktion = EINDECKUNG (Bedingung 4 in
  `dachaufbau`) und mit α(D_i) ≥ α_min(S_k) für alle
  D_i ∈ 𝒟 existiert genau eine Eindeckung als äußerste
  Schicht.
- **Eindeutigkeit.** S_k ist als letzte Element der geordneten
  Liste 𝒮 eindeutig bestimmt; die Wahl der Eindeckungs-
  Familie σ ist Modellierungsentscheidung der Domänen-Schicht
  (Material, Produkt, Verlegungsmuster), die obigen
  Bedingungen sind invariant unter unterschiedlichen
  Realisierungen.
- **Trägerbezug.** Die Eindeckung ist über demselben
  Trägerbereich F = ⋃_i F(P_i) definiert wie der zugrunde
  liegende Aufbau A; sie hat keine eigenständige geometrische
  Erstreckung jenseits des Aufbaus.
- **Konsistenz mit `dachhaut`.** Die Dachhaut H ist die obere
  Hüllfläche der äußeren Punktwolke der Eindeckung; sie wird
  in `dachhaut` als Funktion von M (Punktwolke der äußersten
  Schicht) konstruiert. Hier ist M = ⋃_j ∂σ_j ∩ {äußere Seite}.
  Die Konstruktion ist konsistent und führt zu der Dachhaut
  des umfassenden Aufbaus.
- **Konsistenz mit `dachneigung`.** Die Bedingung
  α(D_i) ≥ α_min(S_k) verbindet die Eindeckung mit der
  Dachneigung jeder Trägerfläche. Für α(D_i) < α_min(S_k)
  ist S_k entweder unzulässig oder muss durch Zusatzmaßnahmen
  (höher klassifiziertes Unterdach) auf das Schutzniveau einer
  Abdichtung gehoben werden; dieser Bereich (zwischen
  Mindestneigung und Regeldachneigung) ist normativer Inhalt
  der materialspezifischen Fachregeln, nicht dieser Definition.
- **Grenzfall α = 0 (Flachdach).** α(D_i) = 0 verletzt
  Bedingung 2 für jedes material-spezifische α_min > 0; eine
  Eindeckung im Sinne dieser Definition existiert auf einem
  Flachdach nicht. Die äußerste Schicht eines Flachdaches ist
  stattdessen eine `dachabdichtung` (Forward-Verweis).
- **Nicht-Zirkularität.** Die Definition verwendet die
  Primitive Punkt, Vektor, Halbgerade, endliche Familie sowie
  die bereits definierten Begriffe `dachflaeche`,
  `dachneigung`, `dachaufbau`, `dachhaut`. Sie verweist auf
  `dachabdichtung`, `unterdach`, `latte`, `konterlatte`,
  `traglattung` und `konterlattung` nur erläuternd und
  abgrenzend, nicht definitorisch.

## Erläuterung (nicht normativ)

Die Eindeckung ist im DACH-Korpus die **Werkstoff-getragene
äußerste Schicht eines geneigten Daches**. Sie übernimmt
gemeinsam mit dem darunterliegenden Unterdach (zweite
wasserführende Ebene) und dem Dachaufbau insgesamt die
Funktion der Wetterabwehr; die Eindeckung selbst leistet
**Regensicherheit**, nicht Wasserdichtheit. Diese normative
Trennung ist seit der Ausgabe 2019 von VOB/C auf Norm-Titel-
Ebene vollzogen: DIN 18338 heißt seither nur noch
„Dachdeckungsarbeiten", die wasserdichten Membran-Inhalte
sind in DIN 18336 „Abdichtungsarbeiten" ausgelagert.

### Subtypen (sealed-Hierarchie pro Material)

Die Eindeckung wird im Glossar als generischer Oberbegriff
geführt; je Material existiert ein eigener Subtyp mit
material-spezifischer Mindestdachneigung, Regeldachneigung
und Verlegungsregel. Vorgesehene Subtypen (eigene Einträge
trigger-basiert):

- **Ziegeleindeckung** (Tonziegel nach DIN EN 1304;
  Betondachsteine analog).
- **Schiefereindeckung** (Naturschiefer; Altdeutsche Deckung,
  Rechteckdeckung).
- **Metalleindeckung**, mit Subtypen:
  - **Stehfalzeindeckung** (nicht selbsttragend, EN 14783).
  - **Trapezprofileindeckung** (selbsttragend, EN 14782).
- **Bitumenschindeleindeckung** (geneigt, schuppig; abzugrenzen
  von der Bitumenbahn, die als Flachdach-Abdichtung auftritt).
- **Holzschindeleindeckung** (Lärche, Eiche; DE/AT/CH-Werte
  differieren).
- **Reeteindeckung** (ZVDH-Fachregel Reetdach 2025-03).
- **Solareindeckung** (Indach-PV / BIPV nach DIN EN 50583;
  Indach-Module ersetzen die übliche Eindeckung vollständig
  und sind selbst eine Eindeckung im Sinne dieser Definition.
  Aufdach-PV ist demgegenüber **keine** Eindeckung, sondern
  ein aufgesetztes Sekundärsystem).
- **Glaseindeckung** (Wintergartendach, Lichtkuppel-Glas; TRLV).

### Regeldachneigung (RDN) vs. Mindestdachneigung (MDN)

Die material-spezifische Schwelle α_min in der mathematischen
Definition entspricht der **Mindestdachneigung (MDN)** der
ZVDH-Fachregel: der Dachneigung, unterhalb welcher das
Material **nicht mehr als Dachdeckung verwendet werden darf**.
Davon zu unterscheiden ist die **Regeldachneigung (RDN)**: die
Dachneigung, bei der das Material **ohne zusätzliche
Maßnahmen** als regensicher gilt. Zwischen MDN und RDN sind
**Zusatzmaßnahmen** (verschweißtes Unterdach, höher
klassifiziertes Unterdach, zusätzliche Sicherung) erforderlich;
unterhalb MDN ist die Eindeckung außerhalb der Fachregel und
darf nur als Abdichtung oder über individuelle
Eignungsprüfung ausgeführt werden.

Branchen-Orientierungswerte (nicht normativ, aus ZVDH-
Fachregeln und Sekundärquellen; verbindlich sind die jeweils
referenzierten Norm- bzw. Fachregel-Werte):

| Material                             | RDN (typ.)  | MDN (Minimum) |
|---|---|---|
| Tonziegel (Standard)                 | ≈ 22°       | 10°           |
| Betondachsteine                      | ≈ 22°       | 10°           |
| Naturschiefer (Altdeutsche Deckung)  | 25°         | 15°           |
| Metall nicht selbsttragend (Stehfalz)| produktabh. | 3° (mit Zusatz)|
| Metall selbsttragend (Trapezprofil)  | produktabh. | 3°–7°         |
| Bitumenschindeln                     | ≥ 20°       | ≥ 15°         |
| Holzschindeln (gespalten, DE)        | 30°         | 14°–18° krit. |
| Reet                                 | 45°         | 40° (Sonderfall)|
| BIPV / Indach-PV                     | analog Metall, produktabh. | Hersteller-Zulassung |
| Glas (Wintergarten)                  | ≥ 7°        | ≥ 5°          |

In der Schweiz publiziert die Arbeitsgemeinschaft
Ziegelindustrie Schweiz (AGZ) eine eigene Mindest-
dachneigungs-Liste je Marktziegel (AGZ 2022); die deutschen
ZVDH-Werte und die AGZ-Werte können sich modell-abhängig
unterscheiden.

### IFC-Pendant

Im IFC-Schema entspricht der Eindeckung **`IfcCovering`** mit
`PredefinedType = ROOFING`. `IfcCovering` ist im Schema-Modul
`IfcSharedBldgElements` als generisches Decklayer-Element
definiert; die Trennung zwischen Tragstruktur (`IfcRoof`,
`IfcBeam`) und Belags-/Deckschicht (`IfcCovering`) ist im
Schema explizit. IFC trennt auf der Enum-Ebene **nicht**
zwischen schuppiger Eindeckung und durchgehender Abdichtung;
beide werden als `IfcCovering.ROOFING` geführt. Die
Unterscheidung wird in der App über die `dachneigung` und den
`material`-/`schicht`-Aufbau abgeleitet.

## Beziehungen

- **Oberbegriff:** `schicht` (Sammelbegriff für die einzelnen
  Schichten des Dachaufbaus, im selben R-Schritt angelegt).
- **Bestandteil von:** `dachaufbau` (als äußerste Schicht
  S_k einer geordneten Schichtfolge); `dach` (mittelbar über
  den Dachaufbau).
- **Spezialisierungen (sealed, trigger-basiert):**
  Ziegeleindeckung, Schiefereindeckung, Metalleindeckung
  (mit Subtypen Stehfalz und Trapezprofil),
  Bitumenschindeleindeckung, Holzschindeleindeckung,
  Reeteindeckung, Solareindeckung, Glaseindeckung.
- **Abgrenzung:**
  - **`dachhaut`:** die geometrische, fiktive Hüllfläche
    **über** der Eindeckung. Die Dachhaut ist Geometrie
    (kein materielles Bauteil); die Eindeckung ist Material.
    Die Dachhaut wird aus der äußeren Punktwolke der
    Eindeckung konstruiert (siehe `dachhaut`,
    Höhenfunktion ρ über dem Trägerbereich F).
  - **`dachaufbau`:** die gesamte geordnete Schichtfolge
    oberhalb des Tragwerks. Die Eindeckung ist nur die
    äußerste Schicht dieses Aufbaus, nicht der Aufbau selbst.
  - **`dachflaeche`:** die geometrische, dickenlose
    Bezugsebene **unter** dem Aufbau. Die Eindeckung liegt
    über der Dachfläche im Halbraum der äußeren Normalen.
  - **`dachabdichtung`** (Forward-Verweis, Trigger Kategorie
    A — Flachdach-Pendant): die wasserdichte, durchgehende
    Membran als äußerste Schicht eines Flachdaches oder
    eines geneigten Daches unterhalb der Mindestdachneigung.
    Normativ in DIN 18336 (DE) bzw. SIA 271 (CH) geregelt
    und vom Geltungsbereich der Eindeckung (DIN 18338,
    SIA 232/1) ausdrücklich getrennt.
  - **`unterdach`** (Forward-Verweis, Trigger Kategorie A):
    die zweite wasserführende Ebene unterhalb der
    Eindeckung. Unterhalb von Konterlattung und Eindeckung;
    nicht Bestandteil der Eindeckung selbst.
  - **`latte`**, **`konterlatte`**, **`traglattung`**,
    **`konterlattung`** (Forward-Verweise, Trigger
    Kategorie A): tragende Lattenebene und
    Hinterlüftungs-Lattenebene unterhalb der Eindeckung.
    Konterlatte (parallel zum Sparren, Hinterlüftung) und
    Traglatte (quer zum Sparren, Auflager der
    Eindeckungselemente) gehören dem Dachaufbau an, aber
    nicht der Eindeckung selbst.

## Implementierungshinweis

Datentyp (Domänen-Schicht, Kotlin, Schicht `domain.bauteil`):

```
package domain.bauteil

import domain.geometrie.Polygon
import domain.Toleranzen
import kotlin.math.PI

/**
 * Eindeckung als äußerste Schicht eines geneigten Daches.
 * Glossar: hg_eindeckung.md
 *
 * Sealed mit Subtypen pro Material; jeder Subtyp trägt seine
 * material-spezifische Mindestdachneigung (alpha_min) und
 * Regeldachneigung (alpha_rdn) als Konstante.
 */
sealed class Eindeckung {
    abstract val alphaMin: Double          // Radiant, > 0
    abstract val alphaRdn: Double          // Radiant, >= alphaMin
    abstract val materialKennung: String   // Produkt-/Norm-Identifikator

    /** Test, ob die Eindeckung auf der gegebenen Dachfläche
     *  zulässig (>= MDN) bzw. innerhalb der Regelausführung
     *  (>= RDN) ist. */
    fun zulaessig(neigung: Double): Boolean =
        neigung >= alphaMin - Toleranzen.WINKEL_EPS

    fun innerhalbRegelausfuehrung(neigung: Double): Boolean =
        neigung >= alphaRdn - Toleranzen.WINKEL_EPS
}

data class Ziegeleindeckung(
    val ziegeltyp: Ziegeltyp,
    override val materialKennung: String
) : Eindeckung() {
    override val alphaMin: Double = 10.0 * PI / 180.0    // ZVDH MDN Ziegel
    override val alphaRdn: Double get() = ziegeltyp.rdn
}

data class Stehfalzeindeckung(
    val blechmaterial: Blechmaterial,
    override val materialKennung: String
) : Eindeckung() {
    override val alphaMin: Double = 3.0 * PI / 180.0
    override val alphaRdn: Double = 7.0 * PI / 180.0
}

// weitere Subtypen analog: Schiefereindeckung,
// Trapezprofileindeckung, Bitumenschindeleindeckung,
// Holzschindeleindeckung, Reeteindeckung,
// Solareindeckung, Glaseindeckung
```

- **Einheit:** Mindest- und Regeldachneigung intern in
  **Radiant** (Double). Anzeige in Grad oder Prozent
  ausschließlich am API-Rand (analog zu `dachneigung`).
- **Invarianten** (in `init` prüfen, bei Verletzung
  `Resultat.Fehler` bzw. `Entartet`-Variante zurückgeben,
  niemals Exception werfen):
  1. `alphaMin > Toleranzen.WINKEL_EPS` (positive
     Mindestneigung; Flachdach-Material ist keine Eindeckung
     im Sinne dieser Definition) ⇒ sonst
     `Entartet.FlachdachMaterial`.
  2. `alphaRdn >= alphaMin - Toleranzen.WINKEL_EPS`
     (Regeldachneigung nicht unter Mindestdachneigung) ⇒
     sonst `Entartet.RdnUnterMdn`.
  3. `alphaMin < PI / 2.0` (Mindestneigung kleiner als
     Senkrechte) ⇒ sonst `Entartet.SenkrechteEindeckung`.
- **Edge Cases:**
  - **Flachdach (α = 0):** keine Eindeckung; die äußerste
    Schicht ist eine `dachabdichtung`. Wird durch Bedingung 2
    der mathematischen Definition (α ≥ α_min > 0) und durch
    `Entartet.FlachdachMaterial` erfasst.
  - **Zwischenbereich MDN ≤ α < RDN:** Eindeckung zulässig,
    aber außerhalb der Regelausführung; erfordert
    Zusatzmaßnahmen am Unterdach. Wird durch
    `innerhalbRegelausfuehrung()` als Boolean-Sicht
    ausgewiesen, nicht als harter Fehler.
  - **BIPV / Indach-PV als Eindeckung:** zulässig; das Modul
    übernimmt die regensichere Funktion und ist selbst eine
    Eindeckung. Aufdach-PV ist demgegenüber **keine**
    Eindeckung (kein Subtyp).
  - **Material-spezifische RDN- und MDN-Werte** sind
    Konstante des jeweiligen Subtyps; die normativen Werte
    der ZVDH-Fachregeln bzw. der AGZ-Tabelle werden als
    Default vorgehalten und können produkt-spezifisch
    überschrieben werden.
- **IFC-Mapping** (am API-Rand des IFC-Exporters, nicht im
  Datentyp selbst): `IfcCovering` mit `PredefinedType =
  ROOFING`; Material-Schichtung über
  `IfcRelAssociatesMaterial` und `IfcMaterialLayerSet`;
  Verknüpfung zum `IfcRoof`-Aggregat über
  `IfcRelCoversBldgElements`.
- **Beziehung zum `dachaufbau`-Datentyp:** Die Eindeckung
  ist die `schichten.last()` eines `Dachaufbau`-Tupels mit
  `funktion = SchichtFunktion.EINDECKUNG`. Die sealed-
  Hierarchie hier ergänzt das materialspezifische Verhalten,
  das `Schicht` allein nicht trägt; ein `Dachaufbau` mit
  Eindeckung referenziert den `Eindeckung`-Subtyp über das
  `material`-Feld der äußersten `Schicht`.

## Quellen

**Primär (normativ):**

- SIA 232/1:2011 (mit Korrigendum 232/1-C1:2013), „Geneigte
  Dächer", Schweizerischer Ingenieur- und Architektenverein,
  Zürich, Abschnitt 1 und Abschnitt 2.
- DIN 18338:2019-09, „VOB Teil C: Allgemeine Technische
  Vertragsbedingungen für Bauleistungen —
  Dachdeckungsarbeiten", Abschnitt 0.
- DIN 18336:2019-09, „VOB Teil C: Abdichtungsarbeiten" (zur
  normativen Abgrenzung).
- DIN 18531-1:2017-07, „Abdichtung von Dächern sowie von
  Balkonen, Loggien und Laubengängen – Teil 1" (zur
  Abgrenzung gegen `dachabdichtung`).
- DIN EN 1304:2013-08, „Dachziegel und Formziegel — Begriffe
  und Produktanforderungen".
- DIN EN 14782:2006-03, „Selbsttragende Metallbleche für
  Bedachung, äußere Bekleidung und innere Auskleidung".
- DIN EN 14783:2013-06, „Vollständig unterstützte Bleche und
  Bänder aus Metall für Bedachungen, äußere Bekleidungen und
  innere Auskleidungen".
- DIN EN 50583-2:2016-12, „Photovoltaik in Gebäuden — Teil 2".
- ZVDH-Fachregel für Dachdeckungen mit Dachziegeln und
  Dachsteinen, Ausgabe 2024-04.
- ZVDH-Fachregel Reetdach, Ausgabe 2025-03.
- ZVDH-Fachregeln Schiefer / Metall / Bitumen-Schindel
  (jeweilige aktuelle Ausgaben).
- ISO 6707-1:2020, „Buildings and civil engineering works —
  Vocabulary — Part 1".
- buildingSMART IFC 4.3.2, `IfcCovering` und
  `IfcCoveringTypeEnum` (Spezifikation, Lexical Section).

**Sekundär:**

- Lignum (Hrsg.): *Lignatec — Geneigte Dächer in Holzbauweise.*
  Lignum, Zürich, aktuelle Auflage.
- Lignum (Hrsg.): *Holzbautabellen HBT.* Lignum, Zürich,
  aktuelle Auflage.
- Mönck, W.; Rug, W.: *Holzbau – Bemessung und Konstruktion.*
  16. Auflage, Beuth Verlag 2015.
- Gerner, M.: *Fachwerk – Instandsetzung, Sanierung, Neubau.*
  DVA, 7. Auflage 2007.
- AGZ (Arbeitsgemeinschaft Ziegelindustrie Schweiz):
  Mindestdachneigungen 2022.
- Holzbau Deutschland, Merkblatt „Begriffe und
  Klassifizierungen für den Holzbau".
- Polybau / suissetec: Wegleitung zur Norm SIA 232/1.

**Korpus (nicht autoritativ):**

- Recherchebericht
  `docs/recherche/2026-05-14_hg_eindeckung.md`.
- BauNetz Wissen: „Dachabdichtungsnorm DIN 18531",
  „Normen zu Deckungsmaterialien".
- Wissenwiki: „Regeldachneigung", „Fachregel für
  Dachdeckungen mit Dachziegeln und Dachsteinen".
- Wikipedia, Lemmata „Dachdeckung", „Dachabdichtung",
  „Flachdach" (abgerufen 2026-05-14).
