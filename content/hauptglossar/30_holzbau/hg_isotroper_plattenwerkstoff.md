---
id: isotroper_plattenwerkstoff
benennung: Isotroper Plattenwerkstoff
synonyme: ["Plattenwerkstoff ohne Vorzugsrichtung", "in Plattenebene quasi-isotroper Holzwerkstoff"]
abgelehnte_benennungen: [Spanplatte, MDF, HDF, Faserplatte, "particleboard", "fibreboard", richtungsisotroper_plattenwerkstoff]
oberbegriff: werkstoff
begriffstyp: generisch
voraussetzungen: [werkstoff, einheitsvektor, faserrichtungs_modus, plattendicken_achse, festigkeitsklasse, produktkennzeichnung, toleranzen]
abgrenzung_zu: [axiales_holz, mehrlagenholz, gerichteter_plattenwerkstoff, werkstoff_stahl, faserrichtung]
status: entwurf
theorie_pflichtig: required
quellen_primär:
  - "DIN EN 312:2010-12, 'Spanplatten – Anforderungen' (P1, P2, P3, P4, P5, P6, P7)."
  - "DIN EN 622-2:2004-08, 'Faserplatten – Anforderungen – Teil 2: Anforderungen an harte Platten' (HB)."
  - "DIN EN 622-3:2004-08, 'Faserplatten – Anforderungen – Teil 3: Anforderungen an mittelharte Platten' (MBH, MBL)."
  - "DIN EN 622-5:2010-01, 'Faserplatten – Anforderungen – Teil 5: Anforderungen an Platten nach dem Trockenverfahren (MDF)'."
  - "DIN EN 1995-1-1:2010-12 (Eurocode 5), Abschnitt 9 (Plattenwerkstoffe und Bauteile aus Plattenwerkstoffen): eine einzige Festigkeit pro Beanspruchungsart in der Plattenebene."
  - "DIN EN 12369-1:2001-04, 'Holzwerkstoffe – Charakteristische Werte für die Berechnung und Bemessung von Holzbauwerken – Teil 1: OSB, Spanplatten und Faserplatten'."
  - "DIN EN 13986:2015-06, 'Holzwerkstoffe zur Verwendung im Bauwesen – Eigenschaften, Bewertung der Konformität und Kennzeichnung'."
quellen_sekundär:
  - "Niemz, P.; Sonderegger, W.: Physik des Holzes und der Holzwerkstoffe. Hanser, München 2017, Kap. 7 (Spanwerkstoffe, Faserplatten, MDF/HDF) und Kap. 8 (Holzwerkstoff-Eigenschaften)."
  - "Blass, H. J.; Sandhaas, C.: Ingenieurholzbau – Grundlagen der Bemessung. KIT Scientific Publishing, Karlsruhe 2016, Kap. 3."
  - "Forest Products Laboratory: Wood Handbook FPL-GTR-282, USDA 2021, Kap. 12 'Wood-Based Composite Materials'."
  - "Lignum (Hrsg.): Holzbautabellen HBT, Lignum, Zürich, aktuelle Auflage."
quellenkonflikt: |
  Die Begriffsabgrenzung „in Plattenebene quasi-isotrop" ist normativ
  konsistent: DIN EN 1995-1-1 Abschnitt 9 und DIN EN 12369-1 führen
  für Spanplatten, MDF, HDF und Faserplatten **eine einzige Festigkeit
  pro Beanspruchungsart** in der Plattenebene, ohne Richtungs-
  unterscheidung. Das ist die direkte normative Bestätigung der
  Klassifikation als Faserrichtungs-Modus KEINE.

  Eigene Festlegung in diesem Glossar (Konvention zur Klassifikation
  der Faserrichtungs-Modi, Memory `project_faserrichtung_modi`):

  - **Isotroper Plattenwerkstoff** ist die Glossar-interne Klassen-
    Bezeichnung für diejenige Werkstoff-Klasse, deren konstitutives
    Merkmal das Fehlen einer Vorzugsrichtung in der Plattenebene
    ist (Faserrichtungs-Modus KEINE).
  - „Isotrop" hier nur in der Plattenebene (LR-Ebene). In
    Plattendickenrichtung ist auch dieser Werkstoff weiterhin
    anisotrop (Spanorientierung in Schichten, Pressrichtung). Der
    präzise Term ist deshalb „**quasi-isotrop in der Plattenebene**"
    (Späne/Fasern regellos verteilt).
  - Subklassen: Spanplatte P4–P7 (DIN EN 312, tragend/feuchtbereich-
    differenziert), MDF (DIN EN 622-5), HDF (DIN EN 622-5 als
    hochdichte MDF), harte Faserplatten / HB (DIN EN 622-2),
    mittelharte Faserplatten / MBH/MBL (DIN EN 622-3).
  - Spanplatten P1, P2, P3 (nicht-tragend) sind technisch in dieser
    Klasse, werden aber im Holzbau-Glossar nur am Rande geführt
    (keine Bemessungsrelevanz nach EC5).

  Die Aussage „Faserrichtungs-Annotation an einem Element mit
  isotropem Plattenwerkstoff ist Validierungsfehler" wird als
  **harte Invariante** (nicht Warnung) festgelegt: weil EC5 für
  diese Klasse keine Faserrichtung als Bemessungseingabe verwendet,
  ist eine Faserrichtungs-Annotation semantisch falsch und die App
  weist sie zurück.
---

## Prosa-Definition

Ein **isotroper Plattenwerkstoff** ist ein Werkstoff der Klasse
Faserrichtungs-Modus KEINE, dessen konstitutives Merkmal das Fehlen
einer Vorzugsrichtung in der Plattenebene ist (quasi-isotrope
Verteilung von Spänen oder Fasern), der ausschließlich durch eine
Plattendicken-Achse charakterisiert ist und der in einer der
konkreten Produktnormen-Klassen Spanplatte, MDF, HDF oder
Faserplatte ausgeführt ist.

## Mathematische Definition

Sei

- 𝓦 die Menge der Werkstoffe (siehe `werkstoff`),
- S² ⊂ ℝ³ die Einheitssphäre (siehe `einheitsvektor`),
- 𝓟_IP die Menge der Produktkennzeichnungen, die für die Subklassen
  Spanplatte (DIN EN 312), MDF (DIN EN 622-5), HDF (DIN EN 622-5
  hochdicht), harte Faserplatte HB (DIN EN 622-2), mittelharte
  Faserplatten MBH/MBL (DIN EN 622-3) zulässig sind.

Dann ist ein **isotroper Plattenwerkstoff** das Tupel

```
IP := (faserrichtungs_modus, produktkennzeichnung, plattendicken_achse)
```

mit

- **faserrichtungs_modus** = KEINE  (konstant für diese Subklasse),
- **produktkennzeichnung** ∈ 𝓟_IP,
- **plattendicken_achse** ∈ S²  (Pflicht: Einheitsvektor in W,
  rechtwinklig zur Plattenebene).

**Das Tupel enthält weder eine Faserrichtung noch eine
Plattenlängsrichtung in der Plattenebene** — das ist die
Kernunterscheidung zu allen anderen Werkstoff-Subklassen.

Es ist 𝓘𝓟 ⊂ 𝓦, d. h. die Menge der isotropen Plattenwerkstoffe ist
eine disjunkte Teilmenge der Werkstoff-Menge mit
`faserrichtungs_modus = KEINE`.

**Validierungsregel** (harte Invariante): Eine Faserrichtungs-
Annotation an einem Bauteil B mit Werkstoff IP ist nicht zulässig:

```
∀ B mit werkstoff(B) ∈ 𝓘𝓟: faserrichtung(B) = ⊥.
```

Eine fehlende Faserrichtung ist hier **kein** Mangel, sondern die
korrekte Modellierung. Setzen einer Faserrichtung führt zu
`Entartet.IsotroperWerkstoffMitFaserrichtung`.

## Wohldefiniertheit

- **Existenz**: Für jedes Spanplatten-, MDF-, HDF- oder
  Faserplatten-Produkt am Markt ist die Plattendicken-Achse durch
  das Plattenformat eindeutig festgelegt (rechtwinklig zur größeren
  Fläche).
- **Eindeutigkeit der Klassifikation**: Die Subklasse
  `isotroper_plattenwerkstoff` ist durch
  `faserrichtungs_modus = KEINE` extensional festgelegt; alle
  Werkstoffe mit quasi-isotroper Plattenebene fallen in diese Klasse.
- **Pflichtcharakter der Plattendicken-Achse**: KEINE ist dennoch
  Plattenwerkstoff; `plattendicken_achse ∈ S²` ist Pflicht
  (Klassen-Invariante). Die Plattendicken-Achse ist die einzige
  geometrische Vektor-Eigenschaft dieser Klasse.
- **Nicht-Existenz einer Faserrichtung in Plattenebene**: harte
  Klassen-Invariante. Setzen einer `faserrichtung` an einem Bauteil
  mit diesem Werkstoff ist Validierungsfehler.
- **„Isotrop" nur in Plattenebene**: in Plattendickenrichtung
  ist auch dieser Werkstoff anisotrop (Schicht-Aufbau Decklage/
  Mittellage bei Spanplatten, Pressrichtung bei MDF). Der
  Glossarbegriff bezieht sich ausschließlich auf die Plattenebene.
- **Norm-Invariante**: plattendicken_achse erbt Norm-Invariante aus
  `einheitsvektor`.
- **Nicht-Zirkularität**: Die Definition stützt sich auf
  `werkstoff`, `einheitsvektor`, `produktkennzeichnung` und
  `toleranzen`. Sie verweist nicht auf die anderen Werkstoff-
  Subklassen.

## Erläuterung (nicht normativ)

### Subklassen-Spektrum

| Subklasse | Norm | Rohdichte [kg/m³] | typ. Anwendung |
|-----------|------|-------------------|----------------|
| Spanplatte P4 | DIN EN 312 | 600–700 | tragend, Trockenbereich |
| Spanplatte P5 | DIN EN 312 | 600–700 | tragend, Feuchtbereich |
| Spanplatte P6 | DIN EN 312 | 650–750 | hochbelastet, Trockenbereich |
| Spanplatte P7 | DIN EN 312 | 650–750 | hochbelastet, Feuchtbereich |
| MDF (Mitteldichte Faserplatte) | DIN EN 622-5 | 600–800 | Möbel, Innenausbau |
| HDF (Hochdichte Faserplatte) | DIN EN 622-5 | > 800 | Bodenbeläge, Türen |
| Harte Faserplatte (HB) | DIN EN 622-2 | > 900 | Rückwände, Schalungen |
| Mittelharte Faserplatte (MBH/MBL) | DIN EN 622-3 | 400–800 | Dämmung, Innenausbau |

Allen gemeinsam ist die **regellose Verteilung** der Späne bzw.
Fasern in der Plattenebene. Bei Spanplatten gibt es lediglich eine
Schichtung in Plattendickenrichtung (feinere Decklagen, gröbere
Mittellage), die in der Plattenebene aber keine Vorzugsrichtung
erzeugt.

### Warum „quasi-isotrop"

Die Späne und Fasern sind nicht perfekt richtungslos verteilt:
während der Streuung beim Plattenpressen entsteht eine geringe
statistische Vorzugsrichtung (typisch in Förderbandrichtung), die
aber so klein ist, dass sie in den EC5-Tabellen nicht gesondert
aufgeführt wird. Das EC5-Modell betrachtet diese Werkstoffe als
in der Plattenebene **isotrop**.

### EC5-Tabellen — Bemessungs-Konsequenz

DIN EN 12369-1 führt für Spanplatten und Faserplatten **eine
einzige Biegefestigkeit f_m** in der Plattenebene, ohne Index 0/90.
Vergleiche:

| Klasse | f_m,k [N/mm²] |
|--------|---------------|
| Spanplatte P4, 12 mm | 14,2 |
| Spanplatte P5, 12 mm | 14,2 |
| MDF, 12 mm | 22 |
| HDF, hochdichte MDF | typ. 30 |

(Zahlenwerte exemplarisch; verbindlich aus DIN EN 12369-1.)

Die Hankinson-Formel ist für diese Klasse **nicht erforderlich**.
Die App berechnet keine Faserwinkel-abhängige Festigkeit.

### Validierungsverhalten der App

Wird ein Bauteil mit Werkstoff `isotroper_plattenwerkstoff` und
einer expliziten Faserrichtungs-Annotation versucht zu instanziieren,
liefert die App eine harte Validierungsfehler-Antwort
(`Resultat.Fehler(Entartet.IsotroperWerkstoffMitFaserrichtung)`).
Begründung:

- EC5 verwendet keine Faserrichtung als Bemessungseingabe für diese
  Klasse.
- Die Annotation suggeriert eine anisotrope Modellierung, die der
  Werkstoff physikalisch nicht hat.
- Eine versehentliche Faserrichtungs-Annotation würde nachgelagerte
  Bemessungsschritte (Hankinson, Lochleibung, Mindestabstände)
  fehlerhaft auslösen.

Diese harte Invariante folgt der Setzung im Memory
`project_faserrichtung_modi`.

## Beziehungen

- **Oberbegriff**: `werkstoff`.
- **Subklassen** (eigene Einträge folgen):
  - **Spanplatte** (`spanplatte`): DIN EN 312.
    Sub-Sub-Subklassen nach Klasse:
    - `spanplatte_p4`, `spanplatte_p5`, `spanplatte_p6`,
      `spanplatte_p7`.
    - Alternative: einheitlich `spanplatte` mit Typ-Attribut.
  - **MDF** (`mdf`): DIN EN 622-5.
  - **HDF** (`hdf`): DIN EN 622-5 (hochdichte MDF).
  - **Harte Faserplatte / HB** (`harte_faserplatte`):
    DIN EN 622-2.
  - **Mittelharte Faserplatte / MBH/MBL**
    (`mittelharte_faserplatte`): DIN EN 622-3.
- **Pflichtfelder über `werkstoff` hinaus**:
  - **Plattendicken-Achse** (`plattendicken_achse`, eigener Folge-
    Eintrag): rechtwinklig zur Plattenebene. Einzige geometrische
    Vektor-Eigenschaft.
- **Verwendung**:
  - **Bauteil** (`bauteil`): trägt einen Werkstoff der Subklasse
    `isotroper_plattenwerkstoff`, wenn Flächenbauteil aus
    Spanplatte / MDF / HDF / Faserplatte.
  - **Plattenwerkstoff** (`plattenwerkstoff`, Folgearbeit):
    Spezialisierung von Flächenbauteil mit Werkstoff aus den drei
    Plattenwerkstoff-Klassen.
- **Abgrenzung**:
  - **`axiales_holz`**: eine ausgeprägte Faserrichtung entlang
    einer Bauteilachse (Stab-/Stützenwerkstoff).
  - **`mehrlagenholz`**: Lagenstruktur mit pro-Lage-Mechanik
    (BSP, Sperrholz, Multiplex).
  - **`gerichteter_plattenwerkstoff`**: schwache, aber
    bemessungsrelevante Vorzugsrichtung in der Plattenebene
    (OSB). Isotroper Plattenwerkstoff hat **keine** solche
    Richtung.
  - **`faserrichtung`** (im Sinne des Klasse-A-Glossarbegriffs):
    Einheitsvektor-Annotation an einem Bauteil mit Werkstoff
    `axiales_holz`. Bei isotropem Plattenwerkstoff ist die
    Faserrichtungs-Annotation **harte Invariante: nicht zulässig**.

## Implementierungshinweis

Datentyp (Domänen-Schicht, Kotlin, Schicht
`domain.holzbau.werkstoff`):

```kotlin
package domain.holzbau.werkstoff

import domain.geometrie.Einheitsvektor
import domain.identifikation.Produktkennzeichnung

/**
 * Isotroper Plattenwerkstoff: Plattenwerkstoff ohne Vorzugsrichtung
 * in der Plattenebene (Faserrichtungs-Modus KEINE).
 * Glossar: hg_isotroper_plattenwerkstoff.md
 *
 * Subklassen: Spanplatte (P4-P7), MDF, HDF, harte Faserplatte,
 *             mittelharte Faserplatte (eigene Folge-Klassen).
 *
 * Pflichtfelder: nur plattendickenAchse.
 * KEINE Faserrichtung, keine Plattenlängsrichtung in der Plattenebene.
 *
 * Validierungsregel: Eine Faserrichtungs-Annotation an einem Element
 * mit diesem Werkstoff ist semantisch falsch und führt zu
 * Resultat.Fehler(Entartet.IsotroperWerkstoffMitFaserrichtung).
 */
data class IsotroperPlattenwerkstoff(
    override val produktkennzeichnung: Produktkennzeichnung,
    override val plattendickenAchse: Einheitsvektor
) : Werkstoff {
    override val faserrichtungsModus: FaserrichtungsModus
        = FaserrichtungsModus.KEINE

    init {
        // 1. plattendickenAchse erfüllt Norm-Invariante
        //    (geerbt von Einheitsvektor).
        // 2. produktkennzeichnung ist eine Spanplatten-/MDF-/HDF-/
        //    Faserplatten-Kennzeichnung nach EN 312 / EN 622-2/-3/-5.
    }
}
```

- **Einheit**: Plattendicken-Achse dimensionsloser Einheitsvektor in
  W.
- **Identität**: Werkstoff trägt keine UUID; Identität auf
  Element-Ebene.
- **Invarianten** (in Fabrikfunktionen / `init` prüfen, bei
  Verletzung `Resultat.Fehler` bzw. `Entartet`-Variante; niemals
  Exception):
  1. `faserrichtungsModus == KEINE` (Klassen-Invariante).
  2. `plattendickenAchse != null` (Klassen-Invariante; einzige
     geometrische Vektor-Eigenschaft).
  3. `plattendickenAchse` erfüllt Norm-Invariante.
  4. `produktkennzeichnung` ist Spanplatten-/MDF-/HDF-/
     Faserplatten-Kennzeichnung.
- **Cross-Element-Invariante** (in Bauteil-Validierung): Wenn
  `bauteil.werkstoff` ∈ `IsotroperPlattenwerkstoff`, dann muss
  `bauteil.faserrichtung == null` gelten. Verletzung führt zu
  `Entartet.IsotroperWerkstoffMitFaserrichtung`.
- **IFC-Mapping** (Persistenzschicht):
  - `IfcMaterial.Name` = „Spanplatte P5" / „MDF" / „HDF" / etc.
  - Property Set `Pset_MaterialWoodBasedPanel`.
  - Keine `LongitudinalDirection`-Property gesetzt (würde
    Vorzugsrichtung suggerieren).
- **Edge Cases**:
  - **Beschichtete Spanplatte** (z. B. melaminbeschichtet):
    Werkstoff bleibt `IsotroperPlattenwerkstoff`; die Beschichtung
    erzeugt eine Vorzugsseite, aber keine Faserrichtung.
    Vorzugsseite ist eine separate Bauteil-Annotation, nicht
    Werkstoff-Eigenschaft.
  - **Versuch, Faserrichtung zu setzen**: harter Fehler,
    `Entartet.IsotroperWerkstoffMitFaserrichtung`.
  - **Versuch, Plattenlängsrichtung zu setzen**: nicht möglich
    (Feld existiert nicht in dieser Klasse). Statisch durch
    Datenmodell verhindert.
  - **Quadratische Plattenformate**: kein Konflikt; die fehlende
    Längsrichtung ist hier semantisch korrekt.
- **Bezeichner-Konvention** (CLAUDE.md): Domänen-Klasse heißt
  `IsotroperPlattenwerkstoff` (deutsch, Glossarbegriff);
  Sub-Subklassen heißen `Spanplatte`, `Mdf`, `Hdf`,
  `HarteFaserplatte`, `MittelharteFaserplatte`.

## Quellen

**Primär (normativ):**

- DIN EN 312:2010-12, „Spanplatten – Anforderungen".
- DIN EN 622-2:2004-08, „Faserplatten – Anforderungen – Teil 2:
  Anforderungen an harte Platten".
- DIN EN 622-3:2004-08, „Faserplatten – Anforderungen – Teil 3:
  Anforderungen an mittelharte Platten".
- DIN EN 622-5:2010-01, „Faserplatten – Anforderungen – Teil 5:
  Anforderungen an Platten nach dem Trockenverfahren (MDF)".
- DIN EN 1995-1-1:2010-12, „Eurocode 5: Bemessung und Konstruktion
  von Holzbauten – Teil 1-1", Abschnitt 9.
- DIN EN 12369-1:2001-04, „Holzwerkstoffe – Charakteristische Werte
  für die Berechnung und Bemessung von Holzbauwerken – Teil 1: OSB,
  Spanplatten und Faserplatten".
- DIN EN 13986:2015-06, „Holzwerkstoffe zur Verwendung im Bauwesen".

**Sekundär:**

- Niemz, P.; Sonderegger, W.: *Physik des Holzes und der
  Holzwerkstoffe.* Hanser, München 2017.
- Blass, H. J.; Sandhaas, C.: *Ingenieurholzbau – Grundlagen der
  Bemessung.* KIT Scientific Publishing, Karlsruhe 2016.
- Forest Products Laboratory: *Wood Handbook FPL-GTR-282.* USDA,
  Madison WI 2021.
- Lignum (Hrsg.): *Holzbautabellen HBT.* Lignum, Zürich, aktuelle
  Auflage.

**Korpus (nicht autoritativ):**

- Wikipedia, Lemmata „Spanplatte", „Mitteldichte Faserplatte",
  „Hochdichte Faserplatte" (abgerufen 2026-05-08).
