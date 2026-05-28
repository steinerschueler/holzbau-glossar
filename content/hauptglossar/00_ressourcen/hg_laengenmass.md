---
id: laengenmass
benennung: Längenmaß
synonyme: ["lineares Maß", "Längen-Maßeintrag"]
abgelehnte_benennungen: [Maßstrecke, "linear dimension", "Maß"]
oberbegriff: strecke
begriffstyp: merkmal
voraussetzungen: [strecke, punkt]
abgrenzung_zu: [lineares_groessenmass, winkelmass, masstoleranz_din18202, bemassung]
status: entwurf
theorie_pflichtig: optional  # Überschreibung merkmal-Default required → optional: Bemaßungs-Begriff, in unterer Stufen-Didaktik nicht zentral; Code-Pendant Folgearbeit für Werkplan-/CNC-Modul (HG_KONVENTIONEN §7).
quellen_primär:
  - "DIN EN ISO 129-1:2022-02, 'Technische Produktdokumentation (TPD) — Angabe von Maßen und Toleranzen — Teil 1: Grundlagen', §3.2.4 'linear dimension' (deutsche Benennung: 'Längenmaß'). [einsicht: vorschau-pdf, Inhaltsverz.]"
  - "DIN EN ISO 129-1:2018-05, §3 (Vorgängerausgabe, gleichlautende Definition). [einsicht: vorschau-pdf, §3 Volltext]"
quellen_sekundär:
  - "Hoischen, H.; Fritz, A.: Technisches Zeichnen. 36. Aufl., Cornelsen, Kap. 'Bemaßung nach DIN EN ISO 129-1'."
  - "Quality-Office-Schulungsskript 'GPS – Lineare Größenmaße nach DIN EN ISO 14405-1' (Stand 09-2024) — Abgrenzung Längenmaß / Größenmaß."
quellenkonflikt: |
  Die früher zitierte DIN 406-10:1992-12 ist seit der Übernahme der
  ISO 129-Reihe zurückgezogen; sie führte „Maßstrecke" nicht als
  definierten Begriff. Im DACH-Holzbau- und Schul-Korpus ist
  „Maßstrecke" als didaktische Bezeichnung für die geometrische Strecke,
  über der ein Maßwert eingetragen wird, etabliert, aber **kein
  Norm-Begriff**. Die normative deutsche Benennung nach
  DIN EN ISO 129-1:2022-02 §3.2.4 ist „Längenmaß"; dieser Eintrag
  übernimmt diese Norm-Benennung und führt „Maßstrecke" in
  `abgelehnte_benennungen:`. Die geometrische Substanz (eine Strecke
  zwischen zwei Bezugspunkten oder zwei Bezugs-Features) ist
  unverändert; verschieden ist nur die terminologische Sicht: die
  `strecke` ist das geometrische Linienstück, das `laengenmass` ist die
  Bemaßungs-Sicht auf eine Strecke mit zugeordnetem Maßwert und
  Maßeinheit zur Eintragung in eine technische Zeichnung.
---

## Prosa-Definition

Ein **Längenmaß** ist die Bemaßungs-Sicht auf eine Strecke, die als
Tripel aus zwei Bezugspunkten in ℝ³, einem nicht-negativen reellen
Maßwert ℓ und einer Längeneinheit (in dieser App: Millimeter) zur
Eintragung in eine technische Zeichnung gemäß DIN EN ISO 129-1
zugeordnet ist.

## Mathematische Definition

Sei

- s = [a, b] eine `strecke` mit a, b ∈ ℝ³, a ≠ b (siehe `hg_strecke.md`),
- ℓ ∈ ℝ_{≥0} ein reeller Maßwert (in mm),
- u ∈ EINHEITEN eine Längeneinheit (für diese App: u = mm).

Dann ist das **Längenmaß** über s das Tripel

```
L(s, ℓ, u) := (s, ℓ, u)   mit   ℓ = ‖b − a‖   (numerische Konsistenz).
```

Die numerische Konsistenzbedingung ℓ = ‖b − a‖ ist im Sinne der
Bauwerks-Maßtoleranz (DIN 18202 / SIA 414) zu lesen, nicht im Sinne
exakter Gleichheit; in der Domänen-Schicht gilt
|ℓ − ‖b − a‖| ≤ Toleranzen.LAENGE_EPS.

## Wohldefiniertheit

- **Existenz und Eindeutigkeit:** Für jede Strecke [a, b] mit a ≠ b
  ist der zugeordnete Maßwert ℓ := ‖b − a‖ eindeutig bestimmt (siehe
  `hg_strecke.md`, Wohldefiniertheit der Länge).
- **Repräsentanten-Unabhängigkeit:** Das Längenmaß ist invariant
  unter Vertauschung (a, b) ↔ (b, a), weil ‖b − a‖ = ‖a − b‖.
- **Nicht-Zirkularität:** Die Definition stützt sich auf
  `strecke` und auf den reellen Skalar ℓ; weder „Längenmaß" noch
  „Maßstrecke" tauchen in der Definition auf.

## Erläuterung (nicht normativ)

DIN EN ISO 129-1:2022-02 §3.2.4 definiert „linear dimension"
(deutsche Benennung: „Längenmaß") als
„linear size of a feature of size or a linear distance between two
features" — also entweder als lineare Größe eines Form-Elements
(z. B. Durchmesser, Breite) oder als linearer Abstand zwischen zwei
Bezugs-Features (z. B. Lochabstand, Kantenabstand).

Im Holzbau-Werkplan tritt das Längenmaß auf als:

- Sparrenlänge zwischen Trauf- und First-Anschnitt,
- Pfettenlänge zwischen Auflagern,
- Kervenabstand vom Sparrenfußpunkt,
- Bohrungs-Achsabstand vom Bauteil-Rand.

Die didaktische DACH-Bezeichnung „Maßstrecke" steht für genau
denselben Inhalt, ist aber **kein Norm-Begriff**: weder
DIN EN ISO 129-1 noch die zurückgezogene DIN 406-10 führen sie
in der Begriffsliste. Dieser Eintrag verwendet die Norm-Benennung
„Längenmaß" und führt „Maßstrecke" als abgelehnte Benennung.

Das Längenmaß ist die **Bemaßungs-Sicht**: es trägt einen
Maßwert plus Einheit zur Eintragung in die Zeichnung, aber kein
Toleranzfeld. Die Tolerierungs-Sicht — Längenmaß plus Toleranzfeld
mit GPS-Festlegungen — ist die Spezialisierung
`lineares_groessenmass` (siehe `hg_lineares_groessenmass.md`).

## Beziehungen

- **Oberbegriff:** `strecke` — das Längenmaß ist eine Sicht auf eine
  Strecke mit zugeordnetem Maßwert und Einheit.
- **Teilbegriffe (Spezialisierung):**
  - `lineares_groessenmass` — Längenmaß mit Toleranzfeld zwischen
    Form-Element-Features im Sinne der GPS-Systematik
    (DIN EN ISO 14405-1).
- **Abgrenzung:**
  - **`strecke`:** das reine geometrische Linienstück ohne Maßwert
    und Bemaßungs-Sicht.
  - **`lineares_groessenmass`:** Spezialisierung mit Toleranzfeld.
  - **Winkelmaß:** Bemaßung eines Winkels (nicht eines linearen
    Abstands); im Glossar nicht eigenständig geführt.
  - **`masstoleranz_din18202`:** Bauwerks-Maßtoleranz im Sinne der
    Ausführungsnorm; eine Längenangabe nach DIN 18202 hat eine
    handwerkliche Toleranz und ist nicht im GPS-Sinne tolerierbar.
  - **Bemaßung:** Tätigkeit der Eintragung von Maßen in die
    Zeichnung; das Längenmaß ist das Resultat dieser Tätigkeit, nicht
    die Tätigkeit selbst. Im Glossar nicht eigenständig geführt
    (reiner Prozessbegriff).

## Implementierungshinweis

Datentyp (Domänen-Schicht, Kotlin, Schicht `domain.bemassung` —
künftiges Paket):

```
data class Laengenmass(
    val strecke: Strecke,
    val wert: Double,           // in mm
    val einheit: Laengeneinheit // MILLIMETER fix für diese App
) {
    init {
        // Konsistenz: |wert − strecke.laenge()| ≤ Toleranzen.LAENGE_EPS
        // wert ≥ 0
    }
}
```

- **Einheit:** Wert in mm (Double); Endpunkt-Koordinaten in mm.
- **Invarianten** (`init` oder Factory):
  1. `wert ≥ 0` (Längen sind nicht-negativ; bei Bedarf
     `wert > Toleranzen.LAENGE_EPS` für Nicht-Entartung).
  2. `|wert − strecke.laenge()| ≤ Toleranzen.LAENGE_EPS`
     (numerische Konsistenz mit der zugrundeliegenden Strecke).
  3. `wert` finit (kein NaN, kein ±∞).
- **Code-Pendant-Pflicht:** keine (`begriffstyp: merkmal`); die
  Klasse wird erst eingeführt, wenn das Bemaßungs-Modul gebaut wird
  (nicht Teil der aktuellen Sparren-mit-zwei-Kerven-Etappe).
- **Edge Cases:**
  - `wert ≈ 0`: degeneriertes Längenmaß (Punktmaß); im Werkplan
    nicht zulässig.
  - Diskrepanz `wert ≠ strecke.laenge()`: kennzeichnet entweder
    Maßeintragungs-Fehler im CAD-Workflow oder einen
    Soll-Ist-Vergleich (Soll-Wert manuell eingetragen, Ist-Wert
    aus Geometrie); die App entscheidet beim Bemaßungs-Modul, wie
    Soll/Ist getrennt geführt werden.

## Quellen

**Primär (normativ):**

- DIN EN ISO 129-1:2022-02, „Technische Produktdokumentation (TPD)
  — Angabe von Maßen und Toleranzen — Teil 1: Grundlagen", §3.2.4
  „linear dimension" (Längenmaß).
- DIN EN ISO 129-1:2018-05, §3 (Vorgängerausgabe, gleichlautende
  Definition).

**Sekundär:**

- Hoischen, H.; Fritz, A.: *Technisches Zeichnen.* 36. Aufl.,
  Cornelsen, Kap. „Bemaßung nach DIN EN ISO 129-1".

**Korpus (nicht autoritativ):**

- Quality-Office-Schulungsskript „GPS – Lineare Größenmaße nach
  DIN EN ISO 14405-1" (Stand 09-2024) — Abgrenzung
  Längenmaß / Größenmaß.
- DACH-Berufsschul-Korpus: didaktische Verwendung von „Maßstrecke"
  (kein Norm-Begriff, hier als abgelehnte Benennung geführt).
