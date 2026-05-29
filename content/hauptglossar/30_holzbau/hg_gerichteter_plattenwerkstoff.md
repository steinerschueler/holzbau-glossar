---
id: gerichteter_plattenwerkstoff
benennung: Gerichteter Plattenwerkstoff
synonyme: ["Plattenwerkstoff mit schwacher Vorzugsrichtung", "schwach orthotroper Plattenwerkstoff"]
abgelehnte_benennungen: [OSB, "oriented strand board", Grobspanplatte, gerichteter_holzwerkstoff]
oberbegriff: werkstoff
begriffstyp: generisch
voraussetzungen: [werkstoff, einheitsvektor, faserrichtungs_modus, plattendicken_achse, plattenlaengsrichtung, festigkeitsklasse, produktkennzeichnung, toleranzen]
abgrenzung_zu: [axiales_holz, mehrlagenholz, isotroper_plattenwerkstoff, werkstoff_stahl, faserrichtung]
status: entwurf
subglossar_pendant: optional  # Überschreibung generisch-Default required → optional: abstrakter Klassenname (Praxis sagt "OSB"); der praxisrelevante Lehrstoff liegt bei faserrichtung und faserrichtungs_modus (beide required), nicht am Sammelbegriff (HG_KONVENTIONEN §7).
quellen_primär:
  - "DIN EN 300:2006-09, 'Platten aus langen, schlanken, gerichteten Spänen (OSB) – Definitionen, Klassifizierung und Anforderungen' (OSB/1, OSB/2, OSB/3, OSB/4)."
  - "DIN EN 1995-1-1:2010-12 (Eurocode 5), Abschnitt 9 (Plattenwerkstoffe und Bauteile aus Plattenwerkstoffen), insbesondere Tabellen mit f_m,0 und f_m,90 für OSB."
  - "DIN EN 13986:2015-06, 'Holzwerkstoffe zur Verwendung im Bauwesen – Eigenschaften, Bewertung der Konformität und Kennzeichnung'."
  - "DIN EN 12369-1:2001-04, 'Holzwerkstoffe – Charakteristische Werte für die Berechnung und Bemessung von Holzbauwerken – Teil 1: OSB, Spanplatten und Faserplatten' (charakteristische Festigkeits- und Steifigkeitswerte)."
quellen_sekundär:
  - "Blass, H. J.; Sandhaas, C.: Ingenieurholzbau – Grundlagen der Bemessung. KIT Scientific Publishing, Karlsruhe 2016, Kap. 3 'Holzwerkstoffe', Abschnitt OSB."
  - "Niemz, P.; Sonderegger, W.: Physik des Holzes und der Holzwerkstoffe. Hanser, München 2017, Kap. 7 (Spanwerkstoffe und OSB)."
  - "EGGER Holzwerkstoffe: Datenblatt EGGER OSB 4 TOP, EGGER OSB 3."
  - "Kronospan: Datenblatt Kronoply OSB 3, Kronoply OSB 4."
  - "Forest Products Laboratory: Wood Handbook FPL-GTR-282, USDA 2021, Kap. 12 'Wood-Based Composite Materials', Abschnitt OSB."
quellenkonflikt: |
  Es gibt keinen normativ etablierten Sammelbegriff für die Werkstoff-
  klasse „Plattenwerkstoff mit schwacher, aber bemessungsrelevanter
  Vorzugsrichtung in der Plattenebene". DIN EN 300 und EN 1995-1-1
  führen ausschließlich OSB; weitere Holzwerkstoffe mit dieser
  Eigenschaft sind im aktuellen Markt nicht zu identifizieren.

  Eigene Festlegung in diesem Glossar (Konvention zur Klassifikation
  der Faserrichtungs-Modi, Memory `project_faserrichtung_modi`):

  - **Gerichteter Plattenwerkstoff** ist die Glossar-interne Klassen-
    Bezeichnung für diejenige Werkstoff-Klasse, deren konstitutives
    Merkmal eine schwache, aber bemessungsrelevante Vorzugsrichtung
    in der Plattenebene ist (Faserrichtungs-Modus SCHWACH).
  - Der Begriff ist **kein normierter Holzbau-Begriff**; er ist eine
    Konvention dieses Glossars, geprägt analog zu „oriented strand
    board" (gerichtete Strands).
  - Zum Stand der Technik 2026 fällt nur **OSB** in diese Klasse.
    Der abstrakte Klassen-Name lässt zukünftige Werkstoffe mit
    ähnlicher Charakteristik (z. B. Stranded Veneer Lumber als
    Platte, gerichtete Faserplatten) offen, ohne den Klassen-Namen
    auf das Produkt OSB zu fixieren.
  - **Wichtige Klärung zur Lagenstruktur**: OSB hat zwar eine
    interne Schichtung (Decklagen-Strands längs, Mittellage quer),
    fällt aber **nicht** unter `mehrlagenholz`, weil die Bemessung
    nach EN 1995-1-1 / EN 12369-1 eine **effektive Plattenrichtung**
    verwendet, keine Einzellagen-Mechanik. EC5-Tabellen führen
    f_m,0 (parallel zur Plattenlängsrichtung) und f_m,90 (rechtwinklig);
    eine pro-Lage-Bemessung wie bei BSP gibt es nicht.
---

## Prosa-Definition

Ein **gerichteter Plattenwerkstoff** ist ein Werkstoff der Klasse
Faserrichtungs-Modus SCHWACH, dessen konstitutives Merkmal eine
schwache, aber bemessungsrelevante Vorzugsrichtung in der
Plattenebene ist, der durch eine einzige Plattenlängsrichtung
(Strand-Längsrichtung der Decklagen) und eine Plattendicken-Achse
charakterisiert ist und der zum gegenwärtigen Stand der Technik in
der Subklasse OSB nach DIN EN 300 ausgeführt ist.

## Mathematische Definition

Sei

- 𝓦 die Menge der Werkstoffe (siehe `werkstoff`),
- S² ⊂ ℝ³ die Einheitssphäre (siehe `einheitsvektor`),
- 𝓟_GP die Menge der Produktkennzeichnungen, die für die Subklasse
  OSB nach DIN EN 300 zulässig sind (OSB/1, OSB/2, OSB/3, OSB/4).

Dann ist ein **gerichteter Plattenwerkstoff** das Tupel

```
GP := (faserrichtungs_modus, produktkennzeichnung, plattendicken_achse,
       plattenlaengsrichtung)
```

mit

- **faserrichtungs_modus** = SCHWACH  (konstant für diese Subklasse),
- **produktkennzeichnung** ∈ 𝓟_GP,
- **plattendicken_achse** ∈ S²  (Pflicht: Einheitsvektor in W,
  rechtwinklig zur Plattenebene),
- **plattenlaengsrichtung** p_hat ∈ S²  (Pflicht: Einheitsvektor in W,
  Strand-Längsrichtung der Decklagen, rechtwinklig zur
  plattendicken_achse:
  ⟨p_hat, plattendicken_achse⟩ = 0 bis Toleranzen.WINKEL_EPS).

Es ist 𝓖𝓟 ⊂ 𝓦, d. h. die Menge der gerichteten Plattenwerkstoffe ist
eine disjunkte Teilmenge der Werkstoff-Menge mit
`faserrichtungs_modus = SCHWACH`.

**Default-Konvention für die Plattenlängsrichtung** (prüfbare
Konstruktionsregel):

```
Wenn plattenlaengsrichtung am Werkstoff nicht explizit gesetzt,
gilt für ein Bauteil B mit werkstoff = GP:
  plattenlaengsrichtung(GP) := bauteil_lokale_x_achse(B)
                              parallel zur längeren Plattenformat-Kante.
```

Beispiel: Standard-OSB-Plattenformate sind 1250 × 2500 mm; die
Längsachse 2500 mm ist Default-Plattenlängsrichtung. Abweichungen
(quer eingebaute Platte, Sonderzuschnitt) müssen explizit markiert
werden.

## Wohldefiniertheit

- **Existenz**: Für jedes OSB-Produkt am Markt ist die
  Plattenlängsrichtung (Strand-Längsrichtung der Decklagen)
  produktnormativ und herstellerseitig festgelegt
  (DIN EN 300, Hersteller-Datenblätter EGGER, Kronospan, Norbord,
  SmartPly).
- **Eindeutigkeit der Klassifikation**: Die Subklasse
  `gerichteter_plattenwerkstoff` ist durch
  `faserrichtungs_modus = SCHWACH` extensional festgelegt; zum
  Stand der Technik 2026 ist OSB die einzige Sub-Subklasse.
- **Eindeutigkeit der Plattenlängsrichtung bis auf Vorzeichen**:
  p_hat ist als Annotation eines Werkstoffs eindeutig, sobald eine
  Vorzeichenkonvention festgelegt ist (typisch „p_hat zeigt in dieselbe
  Halbachse wie die längere Plattenformat-Kante").
- **Pflichtcharakter**: p_hat und plattendicken_achse sind Pflicht.
  Eine fehlende Plattenlängsrichtung ist Validierungsfehler, weil
  EC5-Tabellen (f_m,0 ↔ f_m,90) ohne diese Richtung nicht
  auswertbar sind.
- **Plattendicken-Achse Pflicht**: SCHWACH ist Plattenwerkstoff;
  `plattendicken_achse ∈ S²` ist Pflicht (Klassen-Invariante).
- **Norm-Invarianten**: p_hat und plattendicken_achse erben
  Norm-Invarianten aus `einheitsvektor`.
- **Orthogonalität p_hat ⊥ plattendicken_achse**: Konstruktionsregel,
  da p_hat in der Plattenebene liegt.
- **Nicht-Zirkularität**: Die Definition stützt sich auf
  `werkstoff`, `einheitsvektor`, `produktkennzeichnung` und
  `toleranzen`. Sie verweist nicht auf die anderen Werkstoff-
  Subklassen.

## Erläuterung (nicht normativ)

### Was OSB ist

OSB („Oriented Strand Board", deutsch „Grobspanplatte mit gerichteten
Strands") besteht aus drei Lagen großformatiger Holzspäne (Strands,
typisch 75–150 mm lang, 5–25 mm breit, 0,3–0,7 mm dick), die mit
Phenolharz, MUF- oder PMDI-Klebstoff verpresst sind. Die Decklagen-
Strands sind in **eine Richtung ausgerichtet** (Plattenlängsrichtung),
die Mittellagen-Strands quer dazu.

### Warum SCHWACH und nicht STRUKTURIERT

Trotz der internen Schichtung verhält sich OSB nicht wie BSP:

- Die einzelnen Strands sind **kein homogenes Holz** mit klarer
  Faserrichtung, sondern nur grob ausgerichtet (Streuung mehrerer
  Grad pro Strand).
- Die EC5-Bemessung verwendet **eine einzige Plattenrichtung**
  (Plattenlängsrichtung) mit zwei Festigkeiten: f_m,0 (parallel)
  und f_m,90 (rechtwinklig). Es gibt keine pro-Lage-Mechanik wie bei
  BSP (γ-Verfahren EC5 Anhang B).
- DIN EN 12369-1 führt charakteristische Werte für f_m,0,k und
  f_m,90,k getrennt, das Verhältnis liegt typischerweise bei
  ca. 1,8 : 1 (deutlich schwächer als bei BSH parallel/rechtwinklig
  mit ca. 8 : 1).

### EC5-Tabellen für OSB (Auszug, normativer Hinweis)

| Klasse | f_m,0,k [N/mm²] | f_m,90,k [N/mm²] | Verhältnis |
|--------|-----------------|------------------|------------|
| OSB/2  | 18              | 9                | 2,0        |
| OSB/3  | 18              | 9                | 2,0        |
| OSB/4  | 24              | 13               | 1,8        |

(Zahlenwerte exemplarisch nach DIN EN 12369-1; verbindlich aus der
Norm.)

### Default-Plattenlängsrichtung

Standard-OSB-Plattenformate am Markt:

- **2500 × 1250 mm** (Großtafelformat) — Plattenlängsrichtung =
  2500-mm-Achse.
- **2500 × 675 mm** (Verlegeplatte mit Nut/Feder) —
  Plattenlängsrichtung = 2500-mm-Achse.
- **5000 × 2500 mm** (Sonderformat) — Plattenlängsrichtung =
  5000-mm-Achse.

Bei einer schief eingebauten OSB-Platte (z. B. quer als Aussteifung)
ist die Plattenlängsrichtung **nicht** die Hauptbelastungsrichtung
des Bauteils, sondern eine Werkstoff-Eigenschaft, die mit der Platte
unverändert bleibt.

### Schnittwinkel-Konsequenz

Für OSB (Modus SCHWACH, vgl. `faserrichtungs_modus`) ist die
Hankinson-Formel **abgeschwächt anwendbar**: weil das Verhältnis
f_m,0/f_m,90 deutlich kleiner ist als bei axialem Holz, ist der
Faserwinkel-Effekt geringer. EC5 / EN 12369-1 verwenden für die
Bemessung vereinfachte Tabellen mit f_m,0 und f_m,90 statt einer
Hankinson-Auswertung; die Hankinson-Formel ist also normativ nicht
Bemessungsgrundlage, sondern allenfalls eine zwischenzeitliche
Interpolation, die im App-Kontext als Visualisierungsgröße geführt
werden kann. Die App kann den Faserwinkel zur Plattenlängsrichtung
als Visualisierungsgröße führen, sollte aber die schwächere
Bemessungsrelevanz im UI kommunizieren.

## Beziehungen

- **Oberbegriff**: `werkstoff`.
- **Subklassen** (eigene Einträge folgen):
  - **OSB** (`osb`): DIN EN 300, einzige Sub-Subklasse zum Stand
    der Technik 2026.
  - Sub-Sub-Subklassen nach Nutzungsklasse (Folgearbeit):
    - `osb_1`: nicht-tragend, Trockenbereich
      (DIN EN 300, OSB/1).
    - `osb_2`: tragend, Trockenbereich (NKL 1).
    - `osb_3`: tragend, Feuchtbereich (NKL 2).
    - `osb_4`: hochbelastet, Feuchtbereich (NKL 2).
  - Alternative Modellierung: einheitlich `osb` mit Typ-Attribut
    `OsbTyp ∈ {OSB_1, OSB_2, OSB_3, OSB_4}`.
- **Pflichtfelder über `werkstoff` hinaus**:
  - **Plattenlängsrichtung** (`plattenlaengsrichtung`, eigener
    Folge-Eintrag): Strand-Längsrichtung der Decklagen.
  - **Plattendicken-Achse** (`plattendicken_achse`, eigener Folge-
    Eintrag): rechtwinklig zur Plattenebene.
- **Verwendung**:
  - **Bauteil** (`bauteil`): trägt einen Werkstoff der Subklasse
    `gerichteter_plattenwerkstoff`, wenn Flächenbauteil aus OSB.
  - **Plattenwerkstoff** (`plattenwerkstoff`, Folgearbeit):
    Spezialisierung von Flächenbauteil mit Werkstoff aus den
    drei Plattenwerkstoff-Klassen.
- **Abgrenzung**:
  - **`axiales_holz`**: eine ausgeprägte Faserrichtung entlang
    einer Bauteilachse (Stab-/Stützenwerkstoff). Gerichteter
    Plattenwerkstoff ist Plattenwerkstoff mit schwacher
    Plattenebenen-Richtung.
  - **`mehrlagenholz`**: mehrere ausgeprägte Faserrichtungen
    pro Lage mit pro-Lage-Bemessung (BSP, Sperrholz, Multiplex).
    OSB hat trotz Lagenstruktur **keine** pro-Lage-Bemessung;
    EC5 verwendet eine effektive Plattenrichtung.
  - **`isotroper_plattenwerkstoff`**: keine Vorzugsrichtung in
    Plattenebene (Spanplatte, MDF, HDF). Gerichteter
    Plattenwerkstoff hat eine schwache, aber bemessungsrelevante
    Vorzugsrichtung.
  - **`faserrichtung`** (im Sinne des Klasse-A-Glossarbegriffs):
    Einheitsvektor-Annotation an einem Bauteil mit Werkstoff
    `axiales_holz`. Bei OSB wird stattdessen die
    `plattenlaengsrichtung` geführt; sie ist semantisch
    unterschiedlich (Werkstoff-Eigenschaft, nicht
    Bauteil-Annotation einer L-Achse im strengen Sinn).

## Implementierungshinweis

Datentyp (Domänen-Schicht, Kotlin, Schicht
`domain.holzbau.werkstoff`):

```kotlin
package domain.holzbau.werkstoff

import domain.geometrie.Einheitsvektor
import domain.identifikation.Produktkennzeichnung

/**
 * Gerichteter Plattenwerkstoff: Plattenwerkstoff mit schwacher,
 * aber bemessungsrelevanter Vorzugsrichtung in der Plattenebene
 * (Faserrichtungs-Modus SCHWACH).
 * Glossar: hg_gerichteter_plattenwerkstoff.md
 *
 * Stand der Technik 2026: einzige Sub-Subklasse ist OSB nach
 * DIN EN 300 (OSB/1, OSB/2, OSB/3, OSB/4).
 *
 * Pflichtfelder: plattenlaengsrichtung, plattendickenAchse.
 *
 * Default-Konvention: Wenn plattenlaengsrichtung nicht explizit
 * gesetzt, gilt plattenlaengsrichtung := bauteil.lokale_x_achse,
 * d. h. die längere Plattenformat-Kante. Abweichungen explizit
 * markieren.
 */
data class GerichteterPlattenwerkstoff(
    override val produktkennzeichnung: Produktkennzeichnung,
    val plattenlaengsrichtung: Einheitsvektor,
    override val plattendickenAchse: Einheitsvektor
) : Werkstoff {
    override val faserrichtungsModus: FaserrichtungsModus
        = FaserrichtungsModus.SCHWACH

    init {
        // 1. ⟨plattenlaengsrichtung, plattendickenAchse⟩ <= WINKEL_EPS
        //    (plattenlaengsrichtung in der Plattenebene)
        // 2. Norm-Invarianten geerbt von Einheitsvektor.
        // 3. produktkennzeichnung kompatibel mit OSB nach DIN EN 300.
    }
}
```

- **Einheit**: Vektoren dimensionsloser Einheitsvektor in W.
- **Identität**: Werkstoff trägt keine UUID; Identität auf
  Element-Ebene.
- **Invarianten** (in Fabrikfunktionen / `init` prüfen, bei
  Verletzung `Resultat.Fehler` bzw. `Entartet`-Variante; niemals
  Exception):
  1. `faserrichtungsModus == SCHWACH` (Klassen-Invariante).
  2. `plattendickenAchse != null` (Klassen-Invariante; Pflichtfeld
     bei Plattenwerkstoffen).
  3. `plattenlaengsrichtung` ist Einheitsvektor.
  4. `plattenlaengsrichtung` ⊥ `plattendickenAchse` (innerhalb
     WINKEL_EPS).
  5. `produktkennzeichnung` ist eine OSB-Kennzeichnung nach
     DIN EN 300.
- **IFC-Mapping** (Persistenzschicht):
  - `IfcMaterial.Name` = „OSB/2" / „OSB/3" / „OSB/4".
  - Property Set `Pset_MaterialWoodBasedPanel` mit
    `LongitudinalDirection` = Plattenlängsrichtung.
  - `IfcMaterialLayerSet` mit einer Logischen Lage (die interne
    Strand-Schichtung wird nicht modelliert, weil
    bemessungstechnisch effektive Plattenrichtung verwendet wird).
- **Edge Cases**:
  - **Quer eingebaute OSB-Platte**: zulässig; Plattenlängsrichtung
    ist Werkstoff-Eigenschaft, nicht Bauteil-Hauptrichtung.
    Plattenlängsrichtung wird explizit gesetzt (z. B. parallel zur
    kurzen Bauteilkante).
  - **Sonderformate ohne klare Längsachse** (quadratische OSB-
    Platten): Plattenlängsrichtung muss aus Hersteller-
    Information (Strand-Ausrichtung) übernommen werden, nicht
    aus Plattenformat-Geometrie ableitbar.
  - **Faserrichtungs-Annotation an Bauteil**: bei Werkstoff
    `gerichteter_plattenwerkstoff` ist die `faserrichtung`-
    Annotation am Bauteil **nicht** zulässig (es gibt keine
    L-Richtung im strengen Sinn). Stattdessen wird die
    Plattenlängsrichtung am Werkstoff geführt.
- **Bezeichner-Konvention** (CLAUDE.md): Domänen-Klasse heißt
  `GerichteterPlattenwerkstoff` (deutsch, Glossarbegriff);
  Sub-Subklasse heißt `Osb` mit Typ-Attribut `OsbTyp`.

## Quellen

**Primär (normativ):**

- DIN EN 300:2006-09, „Platten aus langen, schlanken, gerichteten
  Spänen (OSB) – Definitionen, Klassifizierung und Anforderungen".
- DIN EN 1995-1-1:2010-12, „Eurocode 5: Bemessung und Konstruktion
  von Holzbauten – Teil 1-1", Abschnitt 9.
- DIN EN 13986:2015-06, „Holzwerkstoffe zur Verwendung im Bauwesen".
- DIN EN 12369-1:2001-04, „Holzwerkstoffe – Charakteristische Werte
  für die Berechnung und Bemessung von Holzbauwerken – Teil 1: OSB,
  Spanplatten und Faserplatten".

**Sekundär:**

- Blass, H. J.; Sandhaas, C.: *Ingenieurholzbau – Grundlagen der
  Bemessung.* KIT Scientific Publishing, Karlsruhe 2016, Kap. 3.
- Niemz, P.; Sonderegger, W.: *Physik des Holzes und der
  Holzwerkstoffe.* Hanser, München 2017, Kap. 7.
- EGGER Holzwerkstoffe: Datenblätter EGGER OSB 4 TOP, OSB 3.
- Kronospan: Datenblätter Kronoply OSB 3, OSB 4.
- Forest Products Laboratory: *Wood Handbook FPL-GTR-282.* USDA,
  Madison WI 2021, Kap. 12.

**Korpus (nicht autoritativ):**

- Wikipedia, Lemma „Oriented Strand Board" (abgerufen 2026-05-08).
