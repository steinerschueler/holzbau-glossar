---
id: axiales_holz
benennung: Axiales Holz
synonyme: [eindirektionales Holz, Stabholz, "Holzwerkstoff mit einer Faserrichtung"]
abgelehnte_benennungen: [Einrichtungsholz, Richtholz, Linienholz, Vollholz, Schnittholz, Massivholz, "solid timber", "linear timber"]
oberbegriff: werkstoff
begriffstyp: generisch
voraussetzungen: [werkstoff, einheitsvektor, faserrichtung, faserrichtungs_modus, festigkeitsklasse, produktkennzeichnung, toleranzen]
abgrenzung_zu: [mehrlagenholz, gerichteter_plattenwerkstoff, isotroper_plattenwerkstoff, werkstoff_stahl, faserrichtung, bauteilachse]
status: entwurf
subglossar_pendant: notwendig
quellen_primär:
  - "DIN EN 1995-1-1:2010-12 (Eurocode 5), 'Bemessung und Konstruktion von Holzbauten – Teil 1-1', Abschnitt 3 (Werkstoffeigenschaften), Festigkeitswerte parallel und senkrecht zur Faser, Hankinson-Formel für f_α."
  - "SIA 265:2021, 'Holzbau', Schweizerischer Ingenieur- und Architektenverein, Abschnitt 3 (Werkstoffe)."
  - "DIN 4074-1:2012-06, 'Sortierung von Holz nach der Tragfähigkeit – Teil 1: Nadelschnittholz' (Sortierklassen S7, S10, S13)."
  - "DIN EN 14080:2013-09, 'Holzbauwerke – Brettschichtholz und Balkenschichtholz – Anforderungen' (Festigkeitsklassen GL20h … GL32c, BSH und BSc)."
  - "DIN EN 14081-1:2019-10, 'Holzbauwerke – Nach Festigkeit sortiertes Bauholz mit rechteckigem Querschnitt – Teil 1: Allgemeine Anforderungen'."
  - "DIN EN 14374:2005-02, 'Holzbauwerke – Furnierschichtholz für tragende Zwecke – Anforderungen' (LVL)."
  - "DIN EN 338:2016-07, 'Bauholz für tragende Zwecke – Festigkeitsklassen' (C14 … C50, D18 … D70)."
  - "DIN EN 15497:2014-07, 'Keilgezinktes Vollholz für tragende Zwecke – Leistungsanforderungen und Mindestanforderungen an die Herstellung' (KVH)."
quellen_sekundär:
  - "Niemz, P.; Sonderegger, W.: Physik des Holzes und der Holzwerkstoffe. Hanser, München 2017, Kap. 3 und 6 (Anatomie und Anisotropie)."
  - "Blass, H. J.; Sandhaas, C.: Ingenieurholzbau – Grundlagen der Bemessung. KIT Scientific Publishing, Karlsruhe 2016, Kap. 2 und 3."
  - "Lignum (Hrsg.): Holzbautabellen HBT, Lignum, Zürich, aktuelle Auflage, Kap. 'Vollholz, KVH, BSH, LVL'."
  - "Forest Products Laboratory: Wood Handbook FPL-GTR-282, USDA 2021, Kap. 4 und 5."
quellenkonflikt: |
  Es gibt keinen normativ etablierten Sammelbegriff für die Werkstoff-
  klasse „Holz mit einer einzigen, dominanten Faserrichtung entlang
  einer Bauteilachse" (Vollholz + KVH + BSH + LVL). EC5 und SIA 265
  führen die Einzelnormen nebeneinander, ohne sie durch einen
  Oberbegriff zu integrieren.

  Die in der Aufgabenstellung vorgeschlagene Bezeichnung
  „Einrichtungsholz" wurde nach Prüfung **abgelehnt**, weil
  „Einrichtung" in der Schweizer Branchensprache (Eric, Zimmermann)
  und in der DACH-Bauwirtschaft eindeutig den Möbelbau und Innenausbau
  bezeichnet (Wohnungseinrichtung, Inneneinrichtung) und mit der
  Werkstoff-Klassifikation kollidiert.

  Auch „Richtholz" wurde abgelehnt: in der Zimmermannssprache
  bezeichnet es eine Lehre / Schablone beim Aufrichten, nicht einen
  Werkstoff.

  Eigene Festlegung in diesem Glossar (Konvention zur Klassifikation
  der Faserrichtungs-Modi):

  - **Axiales Holz** ist die Glossar-interne Klassen-Bezeichnung für
    diejenige Werkstoff-Klasse, die durch genau **eine** dominante
    Faserrichtung entlang einer Bauteilachse charakterisiert ist
    (Faserrichtungs-Modus HART nach Memory
    `project_faserrichtung_modi`).
  - Der Begriff ist **kein normierter Holzbau-Begriff**; er ist eine
    Konvention dieses Glossars, geprägt analog zu „axial loaded"
    (axial belastet) im EC5-Kontext und „uniaxial fiber-aligned" im
    Composites-Kontext.
  - Konkrete normierte Subklassen: Vollholz (DIN EN 338, DIN EN 14081-1,
    DIN 4074-1), Konstruktionsvollholz / KVH (DIN EN 15497),
    Brettschichtholz / BSH (DIN EN 14080), Balkenschichtholz / BSc
    (DIN EN 14080), Furnierschichtholz / LVL (DIN EN 14374).
  - Der Klassen-Name entspricht der mathematischen Charakterisierung
    „eine ausgezeichnete Faserachse"; die Geschwister-Klassen
    `mehrlagenholz` (Lagenstruktur), `gerichteter_plattenwerkstoff`
    (schwache Plattenrichtung), `isotroper_plattenwerkstoff` (keine
    Faserrichtung in Plattenebene) sind analog konsistent benannt.
---

## Prosa-Definition

Ein **axiales Holz** ist ein Werkstoff der Klasse Faserrichtungs-Modus
HART, der durch genau eine dominante, eindeutige Faserrichtung
entlang einer Bauteilachse charakterisiert ist und der in einer der
konkreten Produktnormen-Klassen Vollholz, Konstruktionsvollholz,
Brettschichtholz, Balkenschichtholz oder Furnierschichtholz
ausgeführt ist.

## Mathematische Definition

Sei

- 𝓦 die Menge der Werkstoffe (siehe `werkstoff`),
- S² ⊂ ℝ³ die Einheitssphäre (siehe `einheitsvektor`),
- 𝓟_AH die Menge der Produktkennzeichnungen, die für die
  Subklassen Vollholz, KVH, BSH, BSc oder LVL zulässig sind
  (DIN EN 14081-1, DIN EN 15497, DIN EN 14080, DIN EN 14374),
- 𝓕𝓚_AH die Menge der für axiale Hölzer zulässigen
  Festigkeitsklassen (DIN EN 338: C14 … C50, D18 … D70;
  DIN EN 14080: GL20h … GL32c, GL20c … GL32c).

Dann ist ein **axiales Holz** das Tupel

```
AH := (faserrichtungs_modus, produktkennzeichnung, plattendicken_achse,
       faserrichtung, festigkeitsklasse)
```

mit

- **faserrichtungs_modus** = HART  (konstant für diese Subklasse),
- **produktkennzeichnung** ∈ 𝓟_AH,
- **plattendicken_achse** = ⊥  (konstant für diese Subklasse: kein
  Plattenwerkstoff, keine ausgezeichnete Plattendicken-Achse),
- **faserrichtung** ∈ S²  (Pflichtfeld; siehe `faserrichtung`):
  Einheitsvektor in W, der die Hauptachse der Holzfaser angibt
  (im strengen Sinn die L-Richtung der orthotropen Holzanisotropie),
- **festigkeitsklasse** ∈ 𝓕𝓚_AH  (eigener Folge-Eintrag
  `festigkeitsklasse`; typisch C24 für Konstruktionsvollholz,
  GL24h / GL28c für BSH).

Es ist 𝓐𝓗 ⊂ 𝓦, d. h. die Menge der axialen Hölzer ist eine
disjunkte Teilmenge der Werkstoff-Menge mit
`faserrichtungs_modus = HART`.

**Default-Konvention für die Faserrichtung** (prüfbare
Konstruktionsregel, analog IFC / BTLx / cadwork):

```
Wenn faserrichtung am Werkstoff nicht explizit gesetzt,
gilt für ein Bauteil B mit werkstoff = AH:
  faserrichtung(AH) := bauteil_lokale_x_achse(B).
```

Diese Default-Regel ist **prüfbar**: nach Auflösung muss
faserrichtung in S² liegen und die Norm-Invariante erfüllen. Eine
fehlende Faserrichtung **nach** Auflösung ist Validierungsfehler,
keine Warnung (Memory `project_faserrichtung_modi`).

## Wohldefiniertheit

- **Existenz**: Für jedes Vollholz-, KVH-, BSH-, BSc- oder
  LVL-Produkt am Markt ist die Faserrichtung anatomisch und
  produktnormativ wohldefiniert (parallel zur Lamellen- bzw.
  Stammachse).
- **Eindeutigkeit der Klassifikation**: Die Subklasse `axiales_holz`
  ist durch `faserrichtungs_modus = HART` extensional festgelegt;
  ein Werkstoff fällt genau dann in diese Klasse, wenn er einen
  einzigen, makroskopisch dominanten Faserverlauf hat.
- **Eindeutigkeit der Faserrichtung bis auf Vorzeichen**: f_hat ist als
  Annotation eines Bauteils eindeutig, sobald eine
  Vorzeichenkonvention festgelegt ist (typisch „f_hat zeigt in dieselbe
  Halbachse wie die Bauteillängsachse von Anfangs- zu Endpunkt";
  siehe `faserrichtung`).
- **Pflichtcharakter der Faserrichtung**: f_hat ist in dieser Subklasse
  Pflichtfeld. Die Default-Regel
  `faserrichtung := bauteil.lokale_x_achse` ist eine
  Konstruktionsregel, kein Erlaubnis-Mechanismus zum Weglassen:
  nach Auflösung muss ein konkreter Vektor vorliegen. Andernfalls
  ist EC5-Bemessung undurchführbar (Hankinson, Lochleibung,
  Mindestabstände).
- **Plattendicken-Achse trivial**: `plattendicken_achse = ⊥` ist
  Klassen-Invariante; axiales Holz ist kein Plattenwerkstoff.
- **Norm-Invariante**: f_hat erbt die Norm-Invariante
  | ‖f_hat‖² − 1 | ≤ Toleranzen.NORM_EPS aus `einheitsvektor`.
- **Nicht-Zirkularität**: Die Definition stützt sich auf
  `werkstoff`, `einheitsvektor`, `faserrichtung`,
  `produktkennzeichnung` und `toleranzen`. Sie verweist nicht auf
  die anderen Werkstoff-Subklassen in ihrer eigenen Definition.

## Erläuterung (nicht normativ)

### Subklassen-Spektrum

Der Sammelbegriff `axiales_holz` deckt die vier industriell
maßgeblichen, eindirektional faserorientierten Holzwerkstoffe ab:

| Subklasse | Norm | typische Festigkeitsklasse |
|-----------|------|----------------------------|
| Vollholz / Bauholz | DIN EN 14081-1, DIN 4074-1, DIN EN 338 | C24 (S10) |
| Konstruktionsvollholz / KVH | DIN EN 15497, DIN EN 14081-1 | C24 |
| Brettschichtholz / BSH | DIN EN 14080 | GL24h, GL28c, GL32h |
| Balkenschichtholz / BSc | DIN EN 14080 | GL20c, GL24c |
| Furnierschichtholz / LVL | DIN EN 14374 | LVL nach ETA, z. B. Kerto-S |

Allen gemeinsam ist die makroskopisch **eindirektionale**
Faserorientierung: die Lamellen, Furniere bzw. Schnitthölzer sind
parallel zur Bauteillängsachse ausgerichtet. Die Bauteillängsachse
und die Faserrichtung stimmen im Regelfall überein (Standardfall im
Holzbau: Sparren, Pfette, Stütze, Strebe).

### Default-Konvention zur Faserrichtung

Die Konvention „Bauteilachse = Faserrichtung" ist Industriepraxis:

- **IFC**: `IfcMaterial` mit Profile-Set `IfcProfileDef`, das die
  lokale Längsrichtung definiert.
- **BTLx**: Part-Element mit lokaler Achse `Reference Side 1`,
  Faser parallel.
- **cadwork**: Bauteilachse ist Default-Faserrichtung; Abweichungen
  sind explizit zu setzen.

Die App folgt dieser Konvention. Eine Abweichung (z. B. schräg
gesägter Sparrenfußklotz, Sonderfall Furnier quer eingebaut) muss
durch explizites Setzen der `faserrichtung` modelliert werden.

### Hankinson-Formel — Bemessungs-Konsequenz

Für axiales Holz ist die Hankinson-Formel zur Bestimmung der
Festigkeit unter beliebigem Faserwinkel α direkt anwendbar:

```
f_α = (f_0 · f_90) / (f_0 · sin²α + f_90 · cos²α)
```

mit f_0 = Festigkeit parallel zur Faser, f_90 = Festigkeit
rechtwinklig zur Faser. Die Anwendbarkeit hängt vom
Faserrichtungs-Modus ab (vgl. Tabelle in `faserrichtungs_modus`):

- HART (`axiales_holz`): direkt anwendbar mit
  α = ∠(Kraft, faserrichtung).
- STRUKTURIERT (`mehrlagenholz`): nicht direkt, sondern pro Lage
  separat anwendbar (Lagen-Mechanik nach EC5 / EN 16351).
- SCHWACH (`gerichteter_plattenwerkstoff`): abgeschwächt anwendbar;
  EC5 / EN 12369-1 verwenden vereinfachte Tabellen mit f_m,0 und
  f_m,90 ohne Hankinson-Auswertung. Im App-Kontext als
  Visualisierungsgröße zulässig, nicht als Bemessungsgrundlage.
- KEINE (`isotroper_plattenwerkstoff`, `werkstoff_stahl`): nicht
  anwendbar; bei `isotroper_plattenwerkstoff` gilt in der
  Plattenebene eine einzige Festigkeit pro Beanspruchungsart, bei
  `werkstoff_stahl` ist die Hankinson-Formel begrifflich nicht
  zutreffend (3D-Isotropie).

### Begriffliche Abgrenzung zu „Vollholz"

`axiales_holz` ist **nicht** synonym zu „Vollholz". Vollholz ist
**eine** Subklasse von axialem Holz (das einlagige, ungezinkte
Naturprodukt). KVH, BSH, BSc und LVL sind keine Vollhölzer im engeren
Sinn (geklebte oder geschichtete Produkte), gehören aber zur Klasse
axiales Holz, weil sie strukturell eine einzige Faserrichtung
aufweisen.

## Beziehungen

- **Oberbegriff**: `werkstoff`.
- **Subklassen** (eigene Einträge folgen):
  - **Vollholz** (`vollholz`): einlagig, ungezinkt; DIN EN 14081-1,
    DIN 4074-1.
  - **Konstruktionsvollholz / KVH** (`kvh`): keilgezinkt,
    technisch getrocknet; DIN EN 15497.
  - **Brettschichtholz / BSH** (`bsh`): mindestens drei parallel
    verklebte Lamellen; DIN EN 14080. (Trotz „Schicht-Holz" gehört
    BSH zu axiales_holz, nicht zu mehrlagenholz, weil alle Lamellen
    dieselbe Faserrichtung haben.)
  - **Balkenschichtholz / BSc** (`bsc` / `balkenschichtholz`):
    zwei oder drei parallel verklebte Lamellen; DIN EN 14080.
  - **Furnierschichtholz / LVL** (`lvl`): parallel verklebte
    Furniere; DIN EN 14374.
- **Pflichtfelder über `werkstoff` hinaus**:
  - **Faserrichtung** (`faserrichtung`): Einheitsvektor in W;
    Pflicht. Default-Regel siehe oben.
  - **Festigkeitsklasse** (`festigkeitsklasse`, eigener Folge-
    Eintrag): typisch C24 (Vollholz/KVH), GL24h / GL28c (BSH),
    LVL-Klasse nach ETA.
- **Verwendung**:
  - **Bauteil** (`bauteil`): trägt einen Werkstoff der Subklasse
    `axiales_holz`, wenn Stabbauteil aus Vollholz/KVH/BSH/BSc/LVL.
  - **Sparren**, **Pfette**, **Stütze**, **Strebe**, **Riegel**:
    Standardfall in der Holzbaupraxis.
- **Abgrenzung**:
  - **`mehrlagenholz`**: Lagenstruktur ≥ 3 Lagen mit kreuzweise
    wechselnden Faserrichtungen (CLT/BSP, Sperrholz, Multiplex).
    Axiales Holz hat **eine** Faserrichtung, Mehrlagenholz **mehrere**
    pro Lage. BSH ist trotz Lamellenstruktur axiales Holz, weil
    alle Lamellen parallel sind.
  - **`gerichteter_plattenwerkstoff`**: Plattenwerkstoff mit
    schwacher Vorzugsrichtung in der Plattenebene (OSB).
    Axiales Holz ist Stab-/Stützenwerkstoff, kein Plattenwerkstoff.
  - **`isotroper_plattenwerkstoff`**: Plattenwerkstoff ohne
    Faserrichtung in der Plattenebene (Spanplatte, MDF, HDF).
    Axiales Holz hat eine Faserrichtung, Isotrope keine.
  - **`faserrichtung`**: Einheitsvektor-Annotation an einem Bauteil;
    ist Eigenschaft eines Bauteils mit Werkstoff
    `axiales_holz`, nicht der Werkstoff-Klasse selbst.
  - **`bauteilachse`**: geometrische Längsachse eines Stabbauteils;
    fällt typisch mit der Faserrichtung zusammen, ist aber
    geometrisch und nicht werkstoff-spezifisch definiert.

## Implementierungshinweis

Datentyp (Domänen-Schicht, Kotlin, Schicht
`domain.holzbau.werkstoff`):

```kotlin
package domain.holzbau.werkstoff

import domain.geometrie.Einheitsvektor
import domain.holzbau.Faserrichtung
import domain.holzbau.Festigkeitsklasse  // eigener Eintrag folgt
import domain.identifikation.Produktkennzeichnung

/**
 * Axiales Holz: Werkstoff-Klasse mit genau einer dominanten
 * Faserrichtung entlang einer Bauteilachse (Faserrichtungs-Modus HART).
 * Glossar: hg_axiales_holz.md
 *
 * Subklassen: Vollholz, KVH, BSH, BSc, LVL (eigene Folge-Klassen).
 *
 * Pflichtfelder: faserrichtung, festigkeitsklasse plus geerbt von
 *                Werkstoff (faserrichtungsModus, produktkennzeichnung).
 * Plattendicken-Achse: konstant null (kein Plattenwerkstoff).
 *
 * Default-Konvention: Wenn faserrichtung am Bauteil nicht explizit
 * gesetzt, gilt faserrichtung := bauteil.lokale_x_achse. Die
 * Konstruktion eines AxialesHolz-Werkstoffs setzt diese Default-
 * Auflösung als Invariante voraus; ein Werkstoff ohne aufgelöste
 * Faserrichtung ist nicht valide.
 */
data class AxialesHolz(
    override val produktkennzeichnung: Produktkennzeichnung,
    val faserrichtung: Faserrichtung,
    val festigkeitsklasse: Festigkeitsklasse
) : Werkstoff {
    override val faserrichtungsModus: FaserrichtungsModus
        = FaserrichtungsModus.HART

    override val plattendickenAchse: Einheitsvektor? = null

    init {
        // 1. produktkennzeichnung kompatibel mit Subklasse
        //    (DIN EN 14081-1 | DIN EN 15497 | DIN EN 14080 |
        //     DIN EN 14374); Prüfung in Folge-Eintrag.
        // 2. festigkeitsklasse kompatibel mit Subklasse
        //    (C-Klassen oder GL-Klassen oder LVL-ETA).
        // 3. faserrichtung erfüllt Norm-Invariante
        //    (geerbt von Einheitsvektor).
    }
}
```

- **Einheit**: Faserrichtung dimensionsloser Einheitsvektor in W;
  Festigkeitsklasse aus eigener Aufzählung.
- **Identität**: Werkstoff trägt keine UUID; Identität wird auf
  Element-Ebene geführt.
- **Invarianten** (in Fabrikfunktionen / `init` prüfen, bei
  Verletzung `Resultat.Fehler` bzw. `Entartet`-Variante; niemals
  Exception):
  1. `faserrichtungsModus == HART` (Klassen-Invariante).
  2. `plattendickenAchse == null` (Klassen-Invariante).
  3. `faserrichtung` erfüllt Norm-Invariante
     | ‖f_hat‖² − 1 | ≤ Toleranzen.NORM_EPS.
  4. `produktkennzeichnung` und `festigkeitsklasse` sind konsistent
     zur konkreten Sub-Subklasse (Vollholz, KVH, BSH, BSc, LVL).
- **Default-Konvention zur Faserrichtung**: Die Auflösung
  `faserrichtung := bauteil.lokale_x_achse` erfolgt in der
  Bauteil-Konstruktion (nicht im Werkstoff selbst), damit der
  Werkstoff stets eine konkrete Faserrichtung trägt. Ein Werkstoff
  ohne aufgelöste Faserrichtung ist konstruktiv nicht erzeugbar.
- **Validierungsregel** (Bemessungs-Schicht): Eine Bauteil-Belastung
  rechtwinklig zur Faser über lange Distanz (z. B. „Sparren liegt
  flach unter der Last") ist Plausibilitätswarnung, kein Hartfehler.
- **Edge Cases**:
  - **Fehlende Faserrichtung nach Default-Auflösung**: nicht erlaubt;
    `Entartet.AxialesHolzOhneFaserrichtung`.
  - **Drehwuchs / Faserabweichung**: nicht durch einen einzelnen
    Vektor erfasst; Sortierklasse (DIN 4074-1) begrenzt die
    Abweichung. Eine ortsabhängige Faserrichtung ist Folgearbeit.
  - **Schräg gesägtes Holz** (Sparrenfußklotz, Auswechslungen):
    `faserrichtung` weicht von Bauteilachse ab; die Default-Regel
    wird durch explizites Setzen überschrieben.
- **Bezeichner-Konvention** (CLAUDE.md): Domänen-Klasse heißt
  `AxialesHolz` (deutsch, Glossarbegriff); Sub-Subklassen heißen
  `Vollholz`, `Kvh`, `Bsh`, `Bsc`, `Lvl`.

## Quellen

**Primär (normativ):**

- DIN EN 1995-1-1:2010-12, „Eurocode 5: Bemessung und Konstruktion
  von Holzbauten – Teil 1-1".
- SIA 265:2021, „Holzbau", Schweizerischer Ingenieur- und
  Architektenverein, Zürich.
- DIN 4074-1:2012-06, „Sortierung von Holz nach der Tragfähigkeit
  – Teil 1: Nadelschnittholz".
- DIN EN 14080:2013-09, „Holzbauwerke – Brettschichtholz und
  Balkenschichtholz – Anforderungen".
- DIN EN 14081-1:2019-10, „Holzbauwerke – Nach Festigkeit
  sortiertes Bauholz mit rechteckigem Querschnitt – Teil 1:
  Allgemeine Anforderungen".
- DIN EN 14374:2005-02, „Holzbauwerke – Furnierschichtholz für
  tragende Zwecke – Anforderungen".
- DIN EN 338:2016-07, „Bauholz für tragende Zwecke –
  Festigkeitsklassen".
- DIN EN 15497:2014-07, „Keilgezinktes Vollholz für tragende
  Zwecke – Leistungsanforderungen und Mindestanforderungen an die
  Herstellung".

**Sekundär:**

- Niemz, P.; Sonderegger, W.: *Physik des Holzes und der
  Holzwerkstoffe.* Hanser, München 2017.
- Blass, H. J.; Sandhaas, C.: *Ingenieurholzbau – Grundlagen der
  Bemessung.* KIT Scientific Publishing, Karlsruhe 2016.
- Lignum (Hrsg.): *Holzbautabellen HBT.* Lignum, Zürich,
  aktuelle Auflage.
- Forest Products Laboratory: *Wood Handbook FPL-GTR-282.* USDA,
  Madison WI 2021.

**Korpus (nicht autoritativ):**

- Holzbau Deutschland, Merkblatt „Begriffe und Klassifizierungen
  für den Holzbau" (abgerufen 2026-05-08).
- Wikipedia, Lemmata „Vollholz", „Brettschichtholz",
  „Furnierschichtholz" (abgerufen 2026-05-08).
