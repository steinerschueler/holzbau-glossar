---
id: querschnitt
benennung: Querschnitt
synonyme: ["Bauteilquerschnitt", "Stabquerschnitt", "Profilquerschnitt", "Schnittfigur (rechtwinklig zur Bauteilachse)"]
abgelehnte_benennungen: [Profil, Schnitt, Querschnittsfläche, "cross section", "section"]
oberbegriff: null
begriffstyp: generisch
voraussetzungen: [punkt, vektor, ebene, polygon, bauteilachse, toleranzen]
abgrenzung_zu: [polygon, ebene, bauteilachse, bauteil, dachflaeche, polyeder]
status: entwurf
theorie_pflichtig: required
quellen_primär:
  - "DIN EN 1995-1-1:2010-12 (Eurocode 5), 'Bemessung und Konstruktion von Holzbauten – Teil 1-1', Abschnitt 1.5 (Begriffe), Abschnitt 5 (Tragwerksberechnung) und Abschnitt 6 (Grenzzustände der Tragfähigkeit): Querschnitt als Bemessungs-Bezugsfläche für Schnittgrössen, Spannungs- und Stabilitätsnachweise."
  - "SIA 265:2021, 'Holzbau', Schweizerischer Ingenieur- und Architektenverein, Abschnitt 4 (Bemessung): Querschnittswerte (A, I, W) als Bemessungseingang."
  - "DIN EN 14081-1:2019-10, 'Holzbauwerke – Nach Festigkeit sortiertes Bauholz mit rechteckigem Querschnitt – Teil 1: Allgemeine Anforderungen': Querschnitt als geometrisches Klassifikationsmerkmal (rechteckig)."
  - "DIN 1052:2008-12, 'Entwurf, Berechnung und Bemessung von Holzbauwerken', Abschnitt 5 (Berechnungsverfahren) und Abschnitt 9 (Querschnittswerte)."
  - "ISO 16739-1:2024, 'Industry Foundation Classes (IFC)', Entitäten 'IfcProfileDef' und Subtypen 'IfcRectangleProfileDef', 'IfcCircleProfileDef', 'IfcIShapeProfileDef': normative Klasse 'Querschnittsprofil' und Subtyp-Hierarchie."
quellen_sekundär:
  - "Lignum (Hrsg.): Holzbautabellen HBT, Lignum, Zürich, aktuelle Auflage, Kap. 'Bauteile und Querschnitte'."
  - "Mönck, W.; Rug, W.: Holzbau – Bemessung und Konstruktion. 16. Aufl., Beuth, Berlin 2015, Kap. 4 'Stabbauteile' und Kap. 5 'Querschnittswerte'."
  - "Blass, H. J.; Sandhaas, C.: Ingenieurholzbau – Grundlagen der Bemessung. KIT Scientific Publishing, Karlsruhe 2016, Kap. 5 'Stabwerke', Querschnittsdefinition und Querschnittswerte."
  - "Natterer, J.; Herzog, T.; Volz, M.: Holzbau-Atlas. 4. Aufl., Birkhäuser, Basel 2003, Kap. 'Bauteile und Querschnitte'."
  - "Bronstein, I. N. et al.: Taschenbuch der Mathematik. Kap. 3.1 'Geometrische Figuren in der Ebene' und Kap. 4 'Mechanik' (Flächenschwerpunkt, Flächenträgheitsmomente)."
quellenkonflikt: |
  Weder DIN EN 1995-1-1 noch SIA 265 noch DIN 1052 enthalten eine
  geschlossene Begriffsdefinition für „Querschnitt"; alle Normen
  verwenden den Begriff vorausgesetzt und behandeln ausschliesslich
  seine Bemessungs-Eigenschaften (Querschnittsfläche A, Flächen-
  trägheitsmomente I_y, I_z, Widerstandsmomente W_y, W_z, Polartrag-
  heitsmoment I_p). DIN EN 14081-1 setzt einen rechteckigen Quer-
  schnitt als Klassifikationsmerkmal voraus, definiert „Querschnitt"
  selbst aber nicht.

  IFC führt mit `IfcProfileDef` eine ontologische Querschnitts-Klasse
  als abstrakten Oberbegriff einer Sealed-Hierarchie konkreter Profile
  (`IfcRectangleProfileDef`, `IfcCircleProfileDef`, `IfcIShapeProfileDef`,
  `IfcArbitraryClosedProfileDef`, …). Die App folgt dieser ontologischen
  Modellierung.

  Eigene Festlegung in diesem Glossar (konsistent mit allen
  konsultierten Quellen):

  - **Querschnitt** ist hier der **abstrakte Oberbegriff** der App-
    Querschnitts-Hierarchie für **Stabbauteile** (Sparren, Pfette,
    Stütze, Strebe, Riegel). Eine Querschnitt-Instanz ist nicht
    direkt instanziierbar; konkrete Instanzen sind Subklassen
    (`rechteck_querschnitt`, später `rund_querschnitt`,
    `i_profil_querschnitt`, …).
  - Ein Querschnitt ist eine **ebene, beschränkte, zusammenhängende
    Punktmenge** in einer Ebene rechtwinklig zur Bauteilachse, zusammen
    mit ihrem **Flächenschwerpunkt** als ausgezeichnetem Punkt der
    Punktmenge. Der Flächenschwerpunkt ist Teil der Definition,
    nicht eine abgeleitete Grösse, weil er die Verbindung zur
    Bauteilachse trägt (siehe `hg_bauteilachse.md`: die Bauteilachse
    ist die Verbindungslinie der Querschnittsschwerpunkte).
  - Querschnitt wird vorerst **nur für Stabbauteile** geführt.
    Plattenbauteile (CLT-Element, Schalungstafel) tragen keinen
    Querschnitt im Sinne dieses Eintrags, sondern Plattendicke und
    Plattengeometrie. Eine eventuelle Erweiterung auf Plattenbauteile
    ist Folgearbeit (Trigger: erstes Plattenbauteil mit
    Querschnitts-Bezug).
  - **Querschnittseigenschaften** (Querschnittsfläche A, Flächen-
    trägheitsmomente I_y, I_z, Widerstandsmomente W_y, W_z) sind
    quantitative Attribute eines konkreten Querschnitts und werden
    in einem eigenen Folge-Eintrag `querschnittseigenschaften`
    geführt (Trigger: erste Bemessungs-Operation in der App).
  - Subklassen ausser `rechteck_querschnitt` (Rund-, I-, T-, L-,
    beliebig-polygonal-Querschnitt) sind Folgearbeit (Trigger:
    erstes Bauteil mit nicht-rechteckigem Querschnitt).
  - Die in EN 14081-1 verwendete enge Lesart („Querschnitt = Rechteck")
    ist hier ausdrücklich nicht gemeint; rechteckiger Querschnitt ist
    **eine** Subklasse der Hierarchie, allerdings die im Holzbau
    dominierende.
---

## Prosa-Definition

Ein **Querschnitt** ist ein abstrakter Oberbegriff für die
Schnittfigur eines Stabbauteils mit einer Ebene im rechten Winkel zur
Bauteilachse, charakterisiert als ebene, beschränkte, zusammen-
hängende Punktmenge zusammen mit ihrem Flächenschwerpunkt, der den
Bezug zur Bauteilachse herstellt, und der in einer der konkreten
Subklassen (Rechteck-, Rund-, I-Profil-, …) instanziiert wird.

## Mathematische Definition

Sei

- E ⊂ ℝ³ eine **Ebene** (siehe `ebene`) mit Normalenvektor n_hat ∈ S²,
- Q ⊂ E eine ebene, **beschränkte**, **zusammenhängende**,
  **abgeschlossene** Punktmenge mit nicht-leerem Inneren
  (Lebesgue-Mass 𝓛²(Q) > 0),
- z ∈ Q ⊂ E der **Flächenschwerpunkt** (Centroid) von Q, definiert
  als

```
z := (1 / 𝓛²(Q)) · ∫_Q x dx,
```

wobei das Integral koordinatenweise über das ebene Lebesgue-Mass
in E genommen ist.

Dann ist ein **Querschnitt** das Tupel

```
QS := (form, ebene, flaechenschwerpunkt)
```

mit den Pflichtkomponenten

- **form** ∈ 𝓠 := { RECHTECK, RUND, I_PROFIL, T_PROFIL, L_PROFIL,
  BELIEBIG_POLYGONAL, … } (bestimmt das Pflichtfeld-Profil der
  konkreten Subklasse; aktuell nur RECHTECK implementiert),
- **ebene** = E (die Ebene, in der die Punktmenge Q liegt),
- **flaechenschwerpunkt** = z ∈ E.

Der Querschnitt ist **abstrakt**: Querschnitt selbst ist nicht
instanziierbar, sondern bezeichnet die Vereinigung der konkreten
Subklassen-Mengen

```
𝓠𝓢 := 𝓡𝓠 ⊎ ⟨weitere Subklassen, Folgearbeit⟩
```

mit

- 𝓡𝓠 = Menge der Rechteck-Querschnitte (siehe
  `rechteck_querschnitt`),
- weitere Subklassen sind Folgearbeit.

**Lokales Querschnittssystem**: Jeder Querschnitt definiert in
seiner Ebene E ein **lokales 2D-Koordinatensystem** (u, v) mit
Ursprung im Flächenschwerpunkt z und einer rechtshändigen
Orthonormalbasis (u_hat, v_hat) ⊂ E. Die konkrete Wahl von (u_hat, v_hat) ist
Subklassen-Aufgabe (z. B. u_hat parallel zur Breitenkante, v_hat parallel
zur Höhenkante beim Rechteck-Querschnitt).

**Bezug zur Bauteilachse**: Für ein Stabbauteil B mit Bauteilachse
A(B) (siehe `bauteilachse`) und Querschnitt QS(s) an der Stelle s
gelten die Beziehungen

```
flaechenschwerpunkt(QS(s)) = z(s) ∈ A(B),
normale(ebene(QS(s)))      = ±d_hat(s),
```

wobei z(s) der Punkt der Bauteilachse an der Stelle s und d_hat(s) die
lokale Tangentenrichtung der Bauteilachse ist. Die Querschnittsebene
steht also per Konstruktion rechtwinklig zur Bauteilachse, und der
Flächenschwerpunkt liegt auf der Bauteilachse.

## Wohldefiniertheit

- **Existenz**: Für jede ebene, beschränkte, zusammenhängende
  Punktmenge Q ⊂ E mit positivem Flächenmass 𝓛²(Q) > 0 ist der
  Flächenschwerpunkt z als Lebesgue-Integral wohldefiniert
  (klassisches Resultat der Mass- und Integrationstheorie;
  Bronstein Kap. 4).
- **Eindeutigkeit des Flächenschwerpunkts**: z ist als gewichtetes
  Mittel über Q eindeutig durch Q bestimmt, unabhängig von der
  Wahl der Parametrisierung von E.
- **Lage des Flächenschwerpunkts**: Bei konvexen Querschnitten
  (Rechteck, Rund, regelmässige Polygone) ist z ∈ Q garantiert.
  Bei nicht-konvexen Querschnitten (z. B. L-Profil, U-Profil) kann
  z ausserhalb von Q liegen; die Definition fordert nur z ∈ E,
  nicht z ∈ Q.
- **Abstrakt, nicht instanziierbar**: Querschnitt selbst hat in der
  Domänen-Schicht keine Konstruktoren (Kotlin: `sealed interface`).
  Jede Instanz ist notwendigerweise einer der konkreten Subklassen
  zugeordnet.
- **Disjunktheit der Subklassen**: 𝓡𝓠 und die weiteren Subklassen-
  Mengen sind durch das Diskriminator-Feld `form` paarweise
  disjunkt. Ein konkreter Querschnitt fällt in genau eine Subklasse.
- **Wohldefiniertheit der Bauteilachsen-Beziehung**: Die Forderung
  „Querschnittsebene rechtwinklig zur Bauteilachse" wird per
  Konstruktion erfüllt (siehe `hg_bauteilachse.md`, Wohldefiniertheits-
  Abschnitt zur Querschnitts-Rechtwinkligkeit), nicht durch
  nachträgliche Prüfung.
- **Nicht-Zirkularität**: Die Definition stützt sich auf `punkt`,
  `vektor`, `ebene`, `polygon`, `bauteilachse` und `toleranzen`. Sie
  verweist nicht auf Subklassen in ihrer eigenen Definition, sondern
  grenzt sich nur extensional zu deren Vereinigung 𝓠𝓢 ab. Der
  Verweis auf `bauteilachse` ist nicht zirkulär: `bauteilachse`
  setzt „Querschnitt" begrifflich voraus und verweist auf den
  vorliegenden Eintrag (vgl. `hg_bauteilachse.md`, Mathematische
  Definition, Verweis „siehe `querschnitt`" sowie `voraussetzungen`-
  Listung); der vorliegende Eintrag löst diese Voraussetzung auf,
  ohne dass `bauteilachse` neu definiert werden muss.

## Erläuterung (nicht normativ)

### Querschnitt im Holzbau

Im Holzbau ist der Querschnitt das zentrale geometrische
Klassifikationsmerkmal eines Stabbauteils. Er bestimmt zusammen mit
der Bauteillänge die Geometrie des Bauteils und ist Eingabe für
sämtliche Bemessungsnachweise:

- **Querschnittsfläche A** für Normalkraftnachweise.
- **Flächenträgheitsmomente I_y, I_z** für Biegesteifigkeit.
- **Widerstandsmomente W_y, W_z** für Biegespannungs-Nachweise.
- **Polartraegheitsmoment I_p** für Torsionsnachweise.
- **Schubflächen A_v** für Querkraftnachweise.

Diese **Querschnittseigenschaften** sind Funktionen der Quer-
schnittsgeometrie und werden in einem eigenen Folge-Eintrag
(`querschnittseigenschaften`) geführt; sie sind nicht Bestandteil
des Querschnitts selbst, sondern aus ihm berechnet.

### Subtyp-Spektrum

Im Holzbau dominieren wenige Querschnittsformen:

| Subklasse | Anwendung | Anteil im Holzbau |
|-----------|-----------|-------------------|
| Rechteck | Sparren, Pfette, Stütze, Strebe (Vollholz, KVH, BSH) | > 95 % |
| Rund | Rundholzstütze, Rundholzbinder | < 3 % |
| I-Profil | Steg-Träger (TJI, OSB-Steg), seltener BSH-I-Profile | < 2 % |
| T-Profil | Schalungsträger (Doka H20, Peri T-Träger) | Schalungsbau |
| beliebig-polygonal | abgebundene Sonderbauteile (Drempel, Auswechslungen) | Sonderfall |

Daher wird in der App zunächst nur der **rechteckige** Querschnitt
implementiert (siehe `hg_rechteck_querschnitt.md`); weitere Subklassen
folgen trigger-basiert.

### Querschnitt vs. Bauteilachse

Querschnitt und Bauteilachse sind **dual**:

- die **Bauteilachse** ist der **geometrische Ort der
  Querschnittsschwerpunkte** entlang der Bauteillänge (1D),
- der **Querschnitt** ist die **Schnittfigur rechtwinklig zur
  Bauteilachse** an einer Stelle s (2D).

Beide zusammen rekonstruieren die volle 3D-Geometrie eines
Stabbauteils als Extrusion (im prismatischen Fall) oder Sweep (im
allgemeinen Fall) des Querschnitts entlang der Bauteilachse.

### Konstanter Querschnitt vs. veränderlicher Querschnitt

Ein **prismatisches** Stabbauteil hat einen **konstanten**
Querschnitt entlang der Bauteilachse: QS(s) = QS₀ für alle
s ∈ [0, L]. Das ist der Standardfall im Holzbau (Sparren, Pfetten,
Stützen aus Vollholz, KVH, BSH).

Ein Stabbauteil mit **veränderlichem** Querschnitt (Satteldach-
Binder mit BSH-Verjüngung, Pultdach-Binder, abgeschrägte Stütze)
trägt eine Querschnittsfunktion s ↦ QS(s). Dieser Fall ist
Folgearbeit und wird in der App zunächst nicht modelliert.

In der D8a-Implementierung trägt jedes Stabbauteil zunächst nur
**einen** Querschnitt als Pflichtfeld, der implizit als konstant
über die Bauteillänge angenommen wird.

## Beziehungen

- **Oberbegriff**: keiner. Querschnitt ist die Wurzel der
  Querschnitts-Hierarchie.
- **Subklassen** (eigene Einträge):
  - **Rechteck-Querschnitt** (`rechteck_querschnitt`): rechteckige
    Schnittfigur mit Breite b und Höhe h. Standardfall im Holzbau.
  - **Rund-Querschnitt** (`rund_querschnitt`, Folgearbeit): kreis-
    förmige Schnittfigur mit Durchmesser d. Trigger: erste
    Rundholz-Stütze.
  - **I-Profil-Querschnitt** (`i_profil_querschnitt`, Folgearbeit):
    I-förmige Schnittfigur (TJI, OSB-Steg-Träger). Trigger: erstes
    I-Profil-Bauteil.
  - **T-Profil-Querschnitt** (`t_profil_querschnitt`, Folgearbeit):
    T-förmige Schnittfigur (Schalungsträger). Trigger: erste
    Schalung mit T-Träger.
  - **Beliebig-polygonaler Querschnitt**
    (`polygonaler_querschnitt`, Folgearbeit): beliebige polygonale
    Schnittfigur als Polygon (siehe `polygon`). Trigger: erstes
    abgebundenes Sonderbauteil mit nicht-standardisiertem
    Querschnitt.
- **Bestandteile (partitiv) eines Querschnitts**:
  - **Form-Diskriminator** (`form`): Aufzählungstyp; bestimmt die
    Subklasse.
  - **Ebene** (`ebene`): die Trägerebene des Querschnitts; ihre
    Normale stimmt bis auf Vorzeichen mit der Bauteilachsen-
    Tangente überein.
  - **Flächenschwerpunkt** (Punkt in der Ebene): liegt auf der
    Bauteilachse.
- **Eigenschaften (Folgearbeit)**:
  - **Querschnittseigenschaften** (`querschnittseigenschaften`):
    A, I_y, I_z, W_y, W_z, I_p, A_v als abgeleitete Grössen.
- **Verwendung**:
  - **Bauteil** (`bauteil`): jedes **Stabbauteil** trägt genau
    einen Querschnitt als Pflichtfeld (D8a; siehe Memory
    `project_grobplan_erstes_tool`). Plattenbauteile und
    Volumenbauteile tragen keinen Querschnitt im Sinne dieses
    Eintrags.
  - **Bauteilachse** (`bauteilachse`): die Verbindungslinie der
    Querschnittsschwerpunkte; ist ohne Querschnitt nicht
    konstruierbar (siehe Hinweis im Wohldefiniertheits-Abschnitt
    von `hg_bauteilachse.md`).
  - **Sparren**, **Pfette**, **Stütze**, **Strebe** (eigene
    Einträge): tragen typisch einen Rechteck-Querschnitt.
- **Abgrenzung**:
  - **Polygon** (`polygon`): Polygon ist eine ebene, polygonal
    berandete Punktmenge; Querschnitt ist eine ebene Punktmenge mit
    Flächenschwerpunkt und Bauteilrolle. Ein polygonaler Querschnitt
    enthält ein Polygon als Berandung, ist aber nicht damit
    identisch.
  - **Ebene** (`ebene`): die Trägerebene eines Querschnitts ist eine
    Ebene; der Querschnitt selbst ist eine **beschränkte** Teilmenge
    dieser Ebene mit Flächenschwerpunkt.
  - **Bauteilachse** (`bauteilachse`): geometrische 1D-Längsachse;
    Querschnitt ist die dazu duale 2D-Schnittfigur. Bauteilachse
    sammelt Querschnittsschwerpunkte; Querschnitt sitzt auf einem
    Punkt der Bauteilachse.
  - **Bauteil** (`bauteil`): Querschnitt ist Eigenschaft eines
    Stabbauteils, nicht das Bauteil selbst. Querschnitt trägt keine
    Lage in W (lokal in der Querschnittsebene definiert);
    Bauteil trägt Lage in W plus einen Querschnitt.
  - **Dachfläche** (`dachflaeche`): Dachfläche ist eine ebene,
    polygonal berandete Punktmenge in W mit Bezug zum Dach;
    Querschnitt ist eine ebene, beschränkte Punktmenge mit Bezug
    zur Bauteilachse. Beide sind „ebene Punktmenge", haben aber
    verschiedene Rollen.
  - **Polyeder** (`polyeder`): Polyeder ist die volle 3D-Geometrie
    eines Bauteils; Querschnitt ist die 2D-Schnittfigur. Bei
    prismatischen Stabbauteilen ist der Polyeder die Extrusion des
    Querschnitts entlang der Bauteilachse.

## Implementierungshinweis

Datentyp (Domänen-Schicht, Kotlin, Schicht
`zimmermann.domain.bauteil.querschnitt`):

```kotlin
package zimmermann.domain.bauteil.querschnitt

import zimmermann.domain.geometrie.Ebene
import zimmermann.domain.geometrie.Punkt

/**
 * Form-Diskriminator eines Querschnitts.
 * Glossar: hg_querschnitt.md
 *
 * Bestimmt die Querschnitt-Subklasse:
 *   RECHTECK             -> RechteckQuerschnitt (b, h)
 *   RUND                 -> RundQuerschnitt (d), Folgearbeit
 *   I_PROFIL             -> IProfilQuerschnitt, Folgearbeit
 *   T_PROFIL             -> TProfilQuerschnitt, Folgearbeit
 *   BELIEBIG_POLYGONAL   -> PolygonalerQuerschnitt, Folgearbeit
 */
enum class QuerschnittsForm {
    RECHTECK,
    RUND,
    I_PROFIL,
    T_PROFIL,
    BELIEBIG_POLYGONAL,
}

/**
 * Wurzel der App-Querschnitts-Hierarchie für Stabbauteile.
 * Glossar: hg_querschnitt.md
 *
 * Abstrakt, nicht direkt instanziierbar. Konkrete Subklasse aktuell:
 *   - RechteckQuerschnitt (hg_rechteck_querschnitt.md)
 *
 * Weitere Subklassen (Rund, I-Profil, T-Profil, polygonal) sind
 * Folgearbeit, getrieben durch erste Anwendungsfaelle.
 *
 * Pflichtfelder: form (Diskriminator), zusaetzlich subklassen-
 * spezifische Geometriefelder (b, h beim Rechteck etc.).
 *
 * Lokales 2D-Koordinatensystem: Querschnitt ist intern in einem
 * lokalen (u, v)-System mit Ursprung im Flaechenschwerpunkt
 * definiert. Die Einbettung in W erfolgt erst durch das Bauteil
 * (Querschnittsebene + Querschnittsorientierung), nicht durch den
 * Querschnitt selbst. Damit ist ein Querschnitt eine reine
 * Werteklasse (data class), die fuer mehrere Bauteile geteilt
 * werden kann (z. B. Standardgroesse 80x160 KVH).
 *
 * Validierung: konkrete Subklassen stellen Konstruktoren auf
 * `internal` und exponieren ausschliesslich Factory-Methoden
 * `aus(...): Resultat<KonkreterQuerschnitt>`. Vorbild: `Werkstoff`
 * und `LokalePlatzierung.aus(...)`.
 */
sealed interface Querschnitt {
    /** Form-Diskriminator; je Subklasse fest. */
    val form: QuerschnittsForm

    /**
     * Querschnittsflaeche A in mm^2. Subklassen-Implementierung.
     * Folgearbeit: voller Querschnittseigenschaften-Eintrag
     * (querschnittseigenschaften.md).
     */
    val flaeche: Double
}
```

- **Einheit**: Form dimensionslos (Aufzählung); Querschnitts-
  geometrie in mm; Flächenmasse in mm² (Folgearbeit
  `querschnittseigenschaften` für I in mm⁴, W in mm³).
- **Identität**: Querschnitt trägt **keine** UUID. Querschnitt ist
  eine Werteklasse (value class / data class), nicht ein
  identifiziertes Objekt. Identität wird auf der Bauteil-Ebene
  geführt; mehrere Bauteile dürfen denselben Querschnitt-Wert teilen
  (z. B. alle Sparren eines Daches mit Standardquerschnitt
  80 mm × 160 mm).
- **Lokales vs. globales System**: Querschnitt ist intern lokal in
  einem 2D-System (u, v) ⊂ Querschnittsebene mit Ursprung im
  Flächenschwerpunkt definiert. Die Einbettung in W (Lage und
  Orientierung der Querschnittsebene in W) ist Sache des
  **Bauteils**, das Querschnitt + Bauteilachse + lokale Orientierung
  zusammenführt. Diese Trennung ist konsistent mit IFC
  (`IfcProfileDef` ist 2D, Einbettung über `IfcExtrudedAreaSolid`
  und `IfcAxis2Placement3D`).
- **Subklassenpflicht**: `Querschnitt` ist `sealed`; jede Instanz
  ist notwendigerweise einer der konkreten Subklassen zugeordnet.
  Die Subklassen prüfen je eigene Invarianten (siehe ihre
  Implementierungshinweise).
- **Invarianten** (ausschliesslich in Factory-Methoden
  `KonkreterQuerschnitt.aus(...): Resultat<KonkreterQuerschnitt>`
  prüfen; bei Verletzung `Resultat.Fehler` zurückgeben. Kein
  `init+require` und keine Exception. Vorbild: `Werkstoff`-Hierarchie
  und `LokalePlatzierung.aus(...)`):
  1. `form` ist gesetzt und konsistent zur konkreten Subklasse.
  2. `flaeche > Toleranzen.NORM_EPS` (positives Flächenmass).
  3. Subklassen-spezifische Geometrieinvarianten (b, h > 0 beim
     Rechteck etc.).
- **IFC-Mapping** (Persistenzschicht):
  - `IfcProfileDef` ← Querschnitt (abstrakte Wurzel).
  - `IfcRectangleProfileDef` ← `RechteckQuerschnitt`.
  - `IfcCircleProfileDef` ← `RundQuerschnitt` (Folgearbeit).
  - `IfcIShapeProfileDef` ← `IProfilQuerschnitt` (Folgearbeit).
  - Profile-Position (`IfcAxis2Placement2D`): Ursprung im
    Flächenschwerpunkt, RefDirection als u_hat-Achse.
- **BTLx-Mapping**: BTLx Part-Element trägt Breite/Höhe direkt;
  Mapping aus `RechteckQuerschnitt.breite/hoehe` ist 1:1.
- **Edge Cases**:
  - **Querschnitt ohne Form-Diskriminator**: nicht erlaubt;
    Validierungsfehler bei Konstruktion (sealed-Subklasse setzt ihn
    konstant).
  - **Entarteter Querschnitt** (Fläche 0, z. B. Linie oder Punkt):
    nicht erlaubt; Factory liefert `Resultat.Fehler`.
  - **Veränderlicher Querschnitt** (s ↦ QS(s)): nicht durch diese
    Hierarchie abgedeckt; Folgearbeit (Trigger: erstes Bauteil mit
    Verjüngung).
  - **Querschnitt für Plattenbauteile**: nicht durch diese Hierarchie
    abgedeckt; Plattenbauteile tragen Plattendicke und
    Plattengeometrie statt Querschnitt. Eventuelle Erweiterung ist
    Folgearbeit.
- **Bezeichner-Konvention** (CLAUDE.md): Domänen-Klasse heisst
  `Querschnitt` (deutsch, Glossarbegriff); Subklassen heissen
  `RechteckQuerschnitt`, `RundQuerschnitt`, `IProfilQuerschnitt`,
  `TProfilQuerschnitt`, `PolygonalerQuerschnitt`.

**Folgearbeit (trigger-basiert):**

- **`querschnittseigenschaften`-Eintrag und -Klasse**: A, I_y, I_z,
  W_y, W_z, I_p, A_v als abgeleitete Grössen mit geschlossenen
  Formeln je Subklasse. Trigger: erste Bemessungs-Operation.
- **`rund_querschnitt`-Eintrag und -Klasse**: kreisförmiger
  Querschnitt mit Durchmesser d. Trigger: erste Rundholz-Stütze.
- **`i_profil_querschnitt`-Eintrag und -Klasse**: I-Profil-
  Querschnitt mit Steg- und Flanschmassen. Trigger: erstes TJI- /
  OSB-Steg-Bauteil.
- **`polygonaler_querschnitt`-Eintrag und -Klasse**: beliebiger
  polygonaler Querschnitt als `Polygon`. Trigger: erstes
  abgebundenes Sonderbauteil mit nicht-standardisiertem Querschnitt.
- **Veränderlicher Querschnitt** (Querschnittsfunktion
  s ↦ QS(s)): Trigger: erster BSH-Binder mit Verjüngung.
- **Querschnitt für Plattenbauteile**: Trigger: erstes
  Plattenbauteil mit Querschnitts-Bezug (z. B. Kantenprofil bei
  CLT-Element).

## Quellen

**Primär (normativ):**

- DIN EN 1995-1-1:2010-12, „Eurocode 5: Bemessung und Konstruktion
  von Holzbauten – Teil 1-1: Allgemeines – Allgemeine Regeln und
  Regeln für den Hochbau".
- SIA 265:2021, „Holzbau", Schweizerischer Ingenieur- und
  Architektenverein, Zürich.
- DIN EN 14081-1:2019-10, „Holzbauwerke – Nach Festigkeit
  sortiertes Bauholz mit rechteckigem Querschnitt – Teil 1:
  Allgemeine Anforderungen".
- DIN 1052:2008-12, „Entwurf, Berechnung und Bemessung von
  Holzbauwerken".
- ISO 16739-1:2024, „Industry Foundation Classes (IFC) for data
  sharing in the construction and facility management industries
  — Part 1: Data schema".

**Sekundär:**

- Lignum (Hrsg.): *Holzbautabellen HBT.* Lignum, Zürich, aktuelle
  Auflage.
- Mönck, W.; Rug, W.: *Holzbau – Bemessung und Konstruktion.*
  16. Auflage, Beuth, Berlin 2015.
- Blass, H. J.; Sandhaas, C.: *Ingenieurholzbau – Grundlagen der
  Bemessung.* KIT Scientific Publishing, Karlsruhe 2016.
- Natterer, J.; Herzog, T.; Volz, M.: *Holzbau-Atlas.* 4. Auflage,
  Birkhäuser, Basel 2003.
- Bronstein, I. N. et al.: *Taschenbuch der Mathematik.* Verlag
  Harri Deutsch, Frankfurt am Main, aktuelle Auflage.

**Korpus (nicht autoritativ):**

- Holzbau Deutschland, Merkblatt „Begriffe und Klassifizierungen
  für den Holzbau" (abgerufen 2026-05-09).
- Wikipedia, Lemma „Querschnitt (Bauwesen)" (abgerufen 2026-05-09).
