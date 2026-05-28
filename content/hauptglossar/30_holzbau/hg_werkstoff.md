---
id: werkstoff
benennung: Werkstoff
synonyme: [Baustoff]
abgelehnte_benennungen: [Material, Stoff, Substanz, Werkmaterial, "material", "structural material"]
oberbegriff: null
begriffstyp: generisch
voraussetzungen: [vektor, einheitsvektor, produktkennzeichnung, faserrichtungs_modus, toleranzen]
abgrenzung_zu: [bauteil, element, produktkennzeichnung, festigkeitsklasse, faserrichtung, faserrichtungs_modus, werkstoff_stahl]
status: entwurf
theorie_pflichtig: required
quellen_primär:
  - "DIN EN 1995-1-1:2010-12 (Eurocode 5), 'Bemessung und Konstruktion von Holzbauten – Teil 1-1', Abschnitt 1.5 (Begriffe), Abschnitt 3 (Werkstoffeigenschaften)."
  - "SIA 265:2021, 'Holzbau', Schweizerischer Ingenieur- und Architektenverein, Abschnitt 3 (Werkstoffe), Abschnitt 4 (Bemessung): Werkstoffeigenschaften als bemessungsrelevante Eingabegrößen."
  - "DIN EN 13986:2015-06, 'Holzwerkstoffe zur Verwendung im Bauwesen – Eigenschaften, Bewertung der Konformität und Kennzeichnung'."
  - "ISO 16739-1:2024, 'Industry Foundation Classes (IFC) for data sharing in the construction and facility management industries — Part 1: Data schema', Entitäten IfcMaterial, IfcMaterialDefinition, Property Sets Pset_MaterialWoodBasedBeam, Pset_MaterialWoodBasedPanel. [direkt]"
quellen_sekundär:
  - "Niemz, P.; Sonderegger, W.: Physik des Holzes und der Holzwerkstoffe. Hanser, München 2017, Kap. 3 'Anatomischer Aufbau' und Kap. 6 'Mechanische Eigenschaften' (Orthotropie L/R/T, transversale Isotropie als Ingenieuransatz)."
  - "Blass, H. J.; Sandhaas, C.: Ingenieurholzbau – Grundlagen der Bemessung. KIT Scientific Publishing, Karlsruhe 2016, Kap. 2 'Werkstoff Holz' und Kap. 3 'Holzwerkstoffe'."
  - "Forest Products Laboratory (FPL): Wood Handbook — Wood as an Engineering Material. General Technical Report FPL-GTR-282, USDA, Madison WI 2021, Kap. 4 'Mechanical Properties of Wood' und Kap. 5 'Mechanical Properties of Clear Wood'."
  - "Schickhofer, G.: Forschungs- und Entwicklungsarbeiten zum Brettsperrholz. TU Graz, Institut für Holzbau und Holztechnologie, diverse Berichte 2003–2024."
  - "Lignum (Hrsg.): Holzbautabellen HBT, Lignum, Zürich, aktuelle Auflage."
quellenkonflikt: |
  Weder DIN EN 1995-1-1 noch SIA 265 noch DIN EN 13986 enthalten eine
  geschlossene Begriffsdefinition für „Werkstoff" als ontologische
  Klasse; alle Normen verwenden den Begriff vorausgesetzt und führen
  Werkstoffeigenschaften (Festigkeit, Steifigkeit, Rohdichte) als
  Bemessungseingabegrößen.

  IFC führt mit `IfcMaterial` eine ontologische Werkstoff-Klasse, die
  als Eigenschaft eines `IfcElement` zugewiesen wird. Die App folgt
  diesem Modell.

  Konfliktfrei in der konsultierten Literatur ist die anisotropie-
  bezogene Klassifikation:

  - Holz im engeren Sinn (Vollholz, BSH, LVL) ist orthotrop mit drei
    Hauptrichtungen Longitudinal/Radial/Tangential und 9 unabhängigen
    elastischen Konstanten (Niemz/Sonderegger 2017, Wood Handbook
    Kap. 4, Blass/Sandhaas Kap. 2). Im Ingenieurholzbau wird typisch
    transversale Isotropie unterstellt (R = T → 5 Konstanten).
    „Faserrichtung" im strengen Sinn ist die L-Richtung.
  - Lagenwerkstoffe (CLT/BSP, Sperrholz) haben pro Lage eine
    Faserrichtung, gesamt keine einheitliche; ProHolz Austria
    definiert „Haupttragrichtung (0°)" als Decklagen-Richtung mit
    höherer Steifigkeit.
  - OSB hat eine schwache, bemessungsrelevante Vorzugsrichtung
    (Decklagen-Strands).
  - Spanplatte/MDF/HDF sind in der Plattenebene quasi-isotrop;
    EC5-Tabellen führen eine einzige Festigkeit pro Beanspruchungsart
    in der Plattenebene.

  Eigene Festlegung in diesem Glossar (konsistent mit allen
  konsultierten Quellen, zusätzlich Memory
  `project_faserrichtung_modi`):

  - **Werkstoff** ist hier der **abstrakte Oberbegriff** der App-
    Werkstoff-Hierarchie und damit eine **Materialklassen-Wurzel**,
    nicht eine Holzwerkstoff-spezifische Wurzel. Die App führt
    neben den vier Holzwerkstoff-Subklassen eine fünfte Subklasse
    für Stahl (Werkstoff von Verbindungsmitteln, Verbindern und
    Verstärkungselementen), siehe `werkstoff_stahl`. Eine
    Werkstoff-Instanz ist nicht direkt instanziierbar; konkrete
    Instanzen sind Subklassen mit je festem Faserrichtungs-Modus.
  - Die vier Holzwerkstoff-Subklassen `axiales_holz`,
    `mehrlagenholz`, `gerichteter_plattenwerkstoff`,
    `isotroper_plattenwerkstoff` sind nach dem
    **Faserrichtungs-Modus** disjunkt (HART / STRUKTURIERT /
    SCHWACH / KEINE). Diese Klassifikation ist bemessungsrelevant
    (EC5-Hankinson, Lochleibung, Mindestabstände) und nicht
    Ornament.
  - **Werkstoff Stahl** ist die fünfte Subklasse (Memory
    `project_element_ontologie`: Verbindungsmittel, Verbinder,
    Verstärkungselemente tragen einen Stahl-Werkstoff). Sie ist
    extensional Bestandteil der Werkstoff-Menge 𝓦, trägt aber
    keine Bemessungsanisotropie im Holzwerkstoff-Sinn (Stahl ist
    3D-isotrop). Der Werkstoff-Begriff dieses Glossars ist also
    eine **Materialklassen-Wurzel** und nicht ausschließlich
    Holzwerkstoff-Wurzel.
  - Die in EN 1995-1-1 / SIA 265 verwendete enge Lesart
    („Werkstoff als reine Festigkeitsklassen-Bezeichnung") ist hier
    ausdrücklich nicht gemeint; die Festigkeitsklasse ist eine
    Eigenschaft eines konkreten Werkstoffs.
  - **App-interne Konvention „Modus ↔ Plattendicken-Achse"**
    (siehe Wohldefiniertheits-Abschnitt):
    HART → `plattendickenAchse = ⊥` (null);
    STRUKTURIERT / SCHWACH / KEINE → `plattendickenAchse ∈ S²`
    Pflicht. Diese Regel ist **nicht aus einer Norm zitierbar**:
    DIN EN 13986 normiert Plattenwerkstoff-Eigenschaften und
    Kennzeichnung, aber keine Pflicht-Achse pro Werkstoff-Subklasse;
    EC5 / SIA 265 nutzen Plattendicke und Faserrichtung als
    Bemessungseingabe, ohne eine geometrische Achsen-Festlegung pro
    Werkstoff-Subklasse zu fordern; Niemz/Sonderegger und
    Blass/Sandhaas behandeln Anisotropie physikalisch ohne diese
    binäre Strukturregel. Die Festlegung ist eine eigenständige
    App-interne Modellierungsentscheidung, die konsistent aus der
    Anisotropie-Charakterisierung der vier Faserrichtungs-Modi
    folgt (Memory `project_faserrichtung_modi`), und wird hier —
    analog zur App-internen Konvention „Welt-zu-Lokal-Trennung" —
    offen als solche markiert.
---

## Prosa-Definition

Ein **Werkstoff** ist ein abstrakter Oberbegriff für die
materialphysikalische Klasse, aus der ein Element der App-Ontologie
besteht, die durch eine Anisotropie-Charakterisierung
(Faserrichtungs-Modus), eine Produktkennzeichnung nach den
einschlägigen Werkstoffnormen und gegebenenfalls eine ausgezeichnete
Plattendicken-Achse beschrieben ist und die in einer der vier
konkreten Holzwerkstoff-Subklassen **axiales Holz**,
**Mehrlagenholz**, **gerichteter Plattenwerkstoff** oder
**isotroper Plattenwerkstoff** beziehungsweise in der fünften
Subklasse **Werkstoff Stahl** (für Verbindungsmittel, Verbinder
und Verstärkungselemente) instanziiert wird.

## Mathematische Definition

Sei

- 𝓜𝓜 := { HART, STRUKTURIERT, SCHWACH, KEINE } die Menge der
  **Faserrichtungs-Modi** (Memory `project_faserrichtung_modi`),
- 𝓟 die Menge der zulässigen Produktkennzeichnungen (siehe
  `produktkennzeichnung`),
- S² ⊂ ℝ³ die Einheitssphäre (siehe `einheitsvektor`),
- 𝓐 := S² ⊎ {⊥} die Menge der zulässigen Plattendicken-Achsen
  (Vektor oder „nicht gesetzt").

Dann ist ein **Werkstoff** das Tupel

```
W := (faserrichtungs_modus, produktkennzeichnung, plattendicken_achse?,
      ⟨subklassen-spezifische Felder⟩)
```

mit den Pflichtkomponenten

- **faserrichtungs_modus** ∈ 𝓜𝓜  (bestimmt das Pflichtfeld-Profil
  der konkreten Subklasse),
- **produktkennzeichnung** ∈ 𝓟  (CE / DIN 4074 / EN 14080 / EN 14081 /
  EN 14374 / EN 16351 / EN 312 / EN 622 / EN 300 / EN 636,
  je nach Subklasse),

und der Optionalkomponente

- **plattendicken_achse?** ∈ 𝓐  (Pflicht bei Plattenwerkstoffen;
  ⊥ bei axialem Holz).

Der Werkstoff ist **abstrakt**: Werkstoff selbst ist nicht
instanziierbar, sondern bezeichnet die Vereinigung der fünf
konkreten Subklassen-Mengen

```
𝓦 := 𝓐𝓗 ⊎ 𝓜𝓛 ⊎ 𝓖𝓟 ⊎ 𝓘𝓟 ⊎ 𝓦𝓢𝓽
```

mit

- 𝓐𝓗  = Menge der axialen Hölzer (siehe `axiales_holz`),
- 𝓜𝓛  = Menge der Mehrlagenhölzer (siehe `mehrlagenholz`),
- 𝓖𝓟  = Menge der gerichteten Plattenwerkstoffe (siehe
  `gerichteter_plattenwerkstoff`),
- 𝓘𝓟  = Menge der isotropen Plattenwerkstoffe (siehe
  `isotroper_plattenwerkstoff`),
- 𝓦𝓢𝓽 = Menge der Stahl-Werkstoffe (siehe `werkstoff_stahl`,
  für Verbindungsmittel, Verbinder und
  Verstärkungselemente).

Die Subklassen sind durch ihren Faserrichtungs-Modus charakterisiert:

```
∀ w ∈ 𝓐𝓗  : faserrichtungs_modus(w) = HART
∀ w ∈ 𝓜𝓛  : faserrichtungs_modus(w) = STRUKTURIERT
∀ w ∈ 𝓖𝓟  : faserrichtungs_modus(w) = SCHWACH
∀ w ∈ 𝓘𝓟  : faserrichtungs_modus(w) = KEINE
∀ w ∈ 𝓦𝓢𝓽 : faserrichtungs_modus(w) = KEINE
```

Die fünf Mengen sind paarweise disjunkt und ihre Vereinigung deckt
𝓦 ab. Der Modus KEINE wird sowohl von 𝓘𝓟 als auch von 𝓦𝓢𝓽 getragen
(siehe `faserrichtungs_modus`); die Disjunktheit zwischen 𝓘𝓟 und
𝓦𝓢𝓽 wird durch die sealed-Subklassen-Identität gewährleistet, nicht
durch den Modus.

**Zugehörigkeit zu Element**: Jedes Element E ∈ 𝓔 (siehe `element`)
trägt genau einen Werkstoff w(E) ∈ 𝓦 als Pflichtfeld.

## Wohldefiniertheit

- **Existenz**: Für jeden konkreten Holzwerkstoff am Markt lässt
  sich der Faserrichtungs-Modus eindeutig bestimmen
  (Memory `project_faserrichtung_modi`). Die vier Holzwerkstoff-
  Subklassen decken alle in EC5 / SIA 265 / EN 13986 zugelassenen
  Holzwerkstoffe ab; die fünfte Subklasse `werkstoff_stahl` deckt
  die für den Holzbau relevanten Stahl-Elemente (Verbindungsmittel,
  Verbinder, Verstärkungselemente) ab.
- **Eindeutigkeit der Klassifikation**: Jeder konkrete Werkstoff
  fällt in genau eine der fünf Subklassen. Die Disjunktheit wird
  bei den Holzwerkstoffen durch die paarweise disjunkten Modi
  HART, STRUKTURIERT, SCHWACH, KEINE getragen; die zusätzliche
  Disjunktheit zwischen `isotroper_plattenwerkstoff` und
  `werkstoff_stahl` (beide tragen Modus KEINE) wird durch die
  sealed-Subklassen-Identität getragen (siehe
  `faserrichtungs_modus`).
- **Abstrakt, nicht instanziierbar**: Werkstoff selbst hat keine
  Konstruktoren in der Domänen-Schicht (Kotlin: `sealed
  interface`). Jede Instanz ist notwendigerweise einer der fünf
  Subklassen zugeordnet.
- **Disjunktheit der Subklassen**: 𝓐𝓗, 𝓜𝓛, 𝓖𝓟, 𝓘𝓟, 𝓦𝓢𝓽 sind
  paarweise disjunkt. Die Klassifikation eines konkreten Werkstoffs
  in eine der fünf Mengen ist eine Werkstoff-Eigenschaft, die aus
  der Produktnorm (CE-Kennzeichnung) ableitbar ist und nicht
  konstruktionsseitig variiert.
- **Konsistenz Modus ↔ Plattendicken-Achse**:
  - Bei Modus HART (axiales Holz) ist `plattendicken_achse = ⊥`
    (kein Plattenwerkstoff).
  - Bei Modi STRUKTURIERT, SCHWACH ist `plattendicken_achse ∈ S²`
    Pflicht (Plattenwerkstoffe mit Faserrichtungs-Annotation
    haben eine ausgezeichnete Plattendicken-Achse).
  - Bei Modus KEINE hängt der Pflichtcharakter von der
    Subklasse ab: `isotroper_plattenwerkstoff` führt
    `plattendicken_achse ∈ S²` als Pflicht; `werkstoff_stahl`
    führt `plattendicken_achse = ⊥` (Stahl ist kein
    Plattenwerkstoff).
- **Nicht-Zirkularität**: Die Definition verwendet ausschließlich
  die Primitive `vektor`, `einheitsvektor`, `produktkennzeichnung`,
  `toleranzen` und den abstrakten Typ Faserrichtungs-Modus. Sie
  verweist nicht auf Subklassen in ihrer eigenen Definition,
  sondern grenzt sich nur extensional zu deren Vereinigung 𝓦 ab.

## Erläuterung (nicht normativ)

### Anisotropie-Charakterisierung

Holz im engeren Sinn ist **orthotrop** mit drei Hauptrichtungen:

- **L** (Longitudinal): parallel zur Stammachse, parallel zur
  Faserlängsachse.
- **R** (Radial): radial vom Markstrahl nach außen.
- **T** (Tangential): tangential zu den Jahrringen.

Vollständige orthotrope Beschreibung benötigt **9 unabhängige
elastische Konstanten** (3 E-Moduln, 3 Schubmoduln, 3 Querkontraktions-
zahlen). Im Ingenieurholzbau wird typisch **transversale Isotropie**
unterstellt (R ≈ T, Reduktion auf 5 unabhängige Konstanten); diese
Annahme ist Grundlage der EC5-Bemessungsformeln.

„**Faserrichtung**" im strengen physikalischen Sinn ist die
**L-Richtung**. Festigkeit und Steifigkeit parallel zur Faser sind
um Faktor 8 bis 30 höher als rechtwinklig zur Faser; die Faserrichtung
ist daher direkte Bemessungseingabe (Hankinson-Formel, Lochleibungs-
festigkeit f_h,α,k, Mindestabstände der Verbindungsmittel).

### Vier Faserrichtungs-Modi (Memory `project_faserrichtung_modi`)

| Modus           | Subklasse                          | Pflichtfeld im Datenmodell                     |
|-----------------|------------------------------------|------------------------------------------------|
| HART            | `axiales_holz`                     | 1 Vektor `faserrichtung`                       |
| STRUKTURIERT    | `mehrlagenholz`                    | Lagenstruktur ≥ 3 Lagen + Haupttragrichtung    |
| SCHWACH         | `gerichteter_plattenwerkstoff`     | 1 Vektor `plattenlaengsrichtung`               |
| KEINE           | `isotroper_plattenwerkstoff`       | nur `plattendicken_achse` (Plattenebene-Isotropie) |
| KEINE           | `werkstoff_stahl`                  | weder `plattendicken_achse` noch Faserrichtung (3D-Isotropie) |

Diese Klassifikation ist die **strukturelle Grundlage** der
Werkstoff-Hierarchie und konsistent mit:

- **EC5-Bemessungslogik**: Hankinson-Formel ist nur für HART
  wohldefiniert; bei STRUKTURIERT je Lage; bei SCHWACH abgeschwächt;
  bei KEINE nicht erforderlich.
- **EC5-Tabellen**: führen für KEINE-Werkstoffe eine einzige
  Festigkeit pro Beanspruchungsart in der Plattenebene; für
  SCHWACH-Werkstoffe (OSB) f_m,0 und f_m,90; für STRUKTURIERT pro
  Lage; für HART parallel/senkrecht plus Hankinson.
- **Produktnormen**: EN 14080 (BSH), EN 14081 (Bauholz), EN 14374
  (LVL), EN 16351 (CLT), EN 636 (Sperrholz), EN 300 (OSB),
  EN 312 (Spanplatte), EN 622 (Faserplatten/MDF/HDF) sind je
  Werkstoffklasse spezifisch.

### Werkstoff vs. Element

Werkstoff ist **Eigenschaft** eines Elements, nicht das Element
selbst. Ein Sparren ist ein **Bauteil** (Element-Subklasse) **aus**
einem Werkstoff (typisch axiales Holz, Festigkeitsklasse C24). Eine
Vollgewindeschraube ist ein **Verbindungsmittel** (Element-
Subklasse) **aus** einem Werkstoff (Stahl, später eigener Eintrag).
Die Trennung Element-Hierarchie ↔ Werkstoff-Hierarchie ist
orthogonal und folgt dem IFC-Modell (`IfcMaterial` als Property
von `IfcElement`).

### Werkstoff vs. Produktkennzeichnung

Werkstoff identifiziert die **Klasse** (axiales Holz,
Festigkeitsklasse C24), Produktkennzeichnung identifiziert die
**Charge** eines konkreten gelieferten Produkts (CE-Kennzeichen mit
Hersteller, Werkscharge, Lieferdatum). Beide sind orthogonal: zwei
Bauteile aus derselben Werkstoffklasse können verschiedene
Produktkennzeichnungen tragen.

## Beziehungen

- **Oberbegriff**: keiner. Werkstoff ist die Wurzel der
  Werkstoff-Hierarchie.
- **Subklassen** (fünf Geschwister, je ein eigener Eintrag):
  - **Axiales Holz** (`axiales_holz`): Modus HART. Vollholz, KVH,
    BSH, LVL, Balkenschichtholz.
  - **Mehrlagenholz** (`mehrlagenholz`): Modus STRUKTURIERT.
    Brettsperrholz/CLT/BSP/X-LAM, Furniersperrholz, Multiplex.
  - **Gerichteter Plattenwerkstoff**
    (`gerichteter_plattenwerkstoff`): Modus SCHWACH. OSB.
  - **Isotroper Plattenwerkstoff**
    (`isotroper_plattenwerkstoff`): Modus KEINE (in Plattenebene
    quasi-isotrop). Spanplatte P4–P7, MDF, HDF, harte
    Faserplatten.
  - **Werkstoff Stahl** (`werkstoff_stahl`): Modus KEINE
    (3D-isotrop). Werkstoff von Verbindungsmitteln (Schraube,
    Nagel, Bolzen, Stabdübel), Verbindern (Balkenschuh,
    Knotenblech) und Verstärkungselementen
    (Vollgewindeschrauben).
- **Bestandteile (partitiv) eines Werkstoffs**:
  - **Faserrichtungs-Modus** (`faserrichtungs_modus`, eigener
    Eintrag folgt; Aufzählungstyp): Pflicht.
  - **Produktkennzeichnung** (`produktkennzeichnung`): Pflicht.
  - **Plattendicken-Achse** (`plattendicken_achse`, eigener
    Eintrag folgt): bei Plattenwerkstoffen Pflicht, bei
    axialem Holz nicht definiert.
- **Verwendung**:
  - **Element** (`element`): trägt genau einen Werkstoff als
    Pflichtfeld.
  - **Bauteil** (`bauteil`): erbt das Werkstoff-Pflichtfeld von
    Element; Update-Task #16 stellt das bestehende Bauteil-
    Werkstoff-Feld auf diese Hierarchie um.
  - **Verbindungsmittel** (`verbindungsmittel`): trägt typisch
    einen Stahl-Werkstoff (Folge-Eintrag `werkstoff_stahl`).
- **Abgrenzung**:
  - **Bauteil** (`bauteil`): Werkstoff ist Eigenschaft, Bauteil
    ist Element. Werkstoff trägt keine Geometrie und keine Lage
    in W; Bauteil trägt beides plus einen Werkstoff.
  - **Element** (`element`): Element ist die App-Ontologie-
    Wurzel der verbauten Einzelobjekte; Werkstoff ist
    Eigenschaft eines Elements, kein Element.
  - **Produktkennzeichnung** (`produktkennzeichnung`):
    identifiziert die Charge eines konkreten Werkstoff-Produkts;
    Werkstoff identifiziert die Klasse. Beide orthogonal.
  - **Festigkeitsklasse** (`festigkeitsklasse`, Folgearbeit):
    Werkstoff-Eigenschaft (z. B. C24, GL24h, BSP-Q3); ist
    Bestandteil eines konkreten Werkstoffs, nicht synonym
    zum Werkstoff.
  - **Faserrichtung** (`faserrichtung`): geometrische
    Annotation eines Bauteils (Einheitsvektor in W); ist nicht
    der Werkstoff, sondern wird **gemäß Werkstoff-Subklasse**
    typisiert (HART: ein Vektor; STRUKTURIERT: lagenweise;
    SCHWACH: Plattenlängsrichtung; KEINE: nicht definiert).
  - **„Material"** (umgangssprachlich): in der Branche oft
    synonym zu „Werkstoff" verwendet, aber zu unscharf für die
    Ontologie. „Material" wird im Phase-1-Schema dieses Glossars
    nicht als Synonym geführt — vgl. `abgelehnte_benennungen`.
  - **Werkstoff-Eigenschaften** (E-Modul, Rohdichte, Festigkeit
    parallel/senkrecht): sind quantitative Attribute eines
    konkreten Werkstoffs, nicht der abstrakten Klasse Werkstoff.
    Werden in der Festigkeitsklassen-Hierarchie geführt.

## Implementierungshinweis

Datentyp (Domänen-Schicht, Kotlin, Schicht `zimmermann.domain.holzbau.werkstoff`):

```kotlin
package zimmermann.domain.holzbau.werkstoff

import zimmermann.domain.geometrie.Einheitsvektor
import zimmermann.domain.identifikation.Produktkennzeichnung

/**
 * Faserrichtungs-Modus eines Werkstoffs.
 * Glossar: hg_werkstoff.md — Memory project_faserrichtung_modi.
 *
 * Bestimmt das Pflichtfeld-Profil der Werkstoff-Subklasse:
 *   HART          -> 1 Vektor faserrichtung
 *   STRUKTURIERT  -> Lagenstruktur >= 3 + Haupttragrichtung
 *   SCHWACH       -> 1 Vektor plattenlaengsrichtung
 *   KEINE         -> nur plattendicken_achse
 */
enum class FaserrichtungsModus { HART, STRUKTURIERT, SCHWACH, KEINE }

/**
 * Wurzel der App-Werkstoff-Hierarchie.
 * Glossar: hg_werkstoff.md
 *
 * Abstrakt, nicht direkt instanziierbar. Konkrete Subklassen sind
 * AxialesHolz, Mehrlagenholz, GerichteterPlattenwerkstoff,
 * IsotroperPlattenwerkstoff (eigene Folge-Klassen).
 *
 * Pflichtfelder: faserrichtungsModus, produktkennzeichnung.
 * Optionalfeld: plattendickenAchse (Pflicht bei Plattenwerkstoffen,
 *               null bei axialem Holz).
 *
 * Validierung: konkrete Subklassen stellen Konstruktoren auf
 * `internal` und exponieren ausschliesslich Factory-Methoden
 * `aus(...): Resultat<KonkreterWerkstoff>`. Invarianten werden
 * in der Factory geprueft, nicht in `init+require`. Bei Verletzung
 * wird `Resultat.Fehler` zurueckgegeben; es wird nie eine Exception
 * geworfen. Vorbild: `LokalePlatzierung.aus(...)`.
 */
sealed interface Werkstoff {
    /** Anisotropie-Charakterisierung; je Subklasse fest. */
    val faserrichtungsModus: FaserrichtungsModus

    /** Normative Produktkennzeichnung (CE / DIN 4074 / EN 14080 / …). */
    val produktkennzeichnung: Produktkennzeichnung

    /**
     * Plattendicken-Achse (Einheitsvektor in W) bei Plattenwerkstoffen;
     * null bei axialem Holz.
     */
    val plattendickenAchse: Einheitsvektor?
}
```

- **Einheit**: Faserrichtungs-Modus dimensionslos (Aufzählung);
  Plattendicken-Achse dimensionsloser Einheitsvektor.
- **Identität**: Werkstoff trägt **keine** UUID. Werkstoff ist eine
  Werteklasse (value class / data class), nicht ein identifiziertes
  Objekt. Identität wird auf der Element-Ebene geführt; mehrere
  Elemente dürfen denselben Werkstoff-Wert teilen.
- **Subklassenpflicht**: `Werkstoff` ist `sealed`; jede Instanz ist
  notwendigerweise einer der fünf konkreten Subklassen zugeordnet
  (vier Holzwerkstoff-Subklassen plus `WerkstoffStahl`). Die
  Subklassen prüfen je eigene Invarianten (siehe ihre
  Implementierungshinweise).
- **Invarianten** (ausschliesslich in Factory-Methoden
  `KonkreterWerkstoff.aus(...): Resultat<KonkreterWerkstoff>`
  prüfen; bei Verletzung `Resultat.Fehler` zurückgeben. Kein
  `init+require` und keine Exception; Konstruktoren der Subklassen
  sind `internal` und werden nur aus der Factory aufgerufen.
  Vorbild: `LokalePlatzierung.aus(...)` und das Factory-Pattern
  der D6-Skizzen):
  1. `faserrichtungsModus` ist gesetzt.
  2. `produktkennzeichnung` ist gesetzt und konsistent zur
     Subklasse (z. B. `EN 14080` nur bei `AxialesHolz`-BSH).
  3. Konsistenz Modus ↔ Plattendicken-Achse:
     - HART: `plattendickenAchse == null`.
     - STRUKTURIERT, SCHWACH: `plattendickenAchse != null` und
       Norm-Invariante geerbt von `Einheitsvektor`.
     - KEINE: subklassen-abhängig. `IsotroperPlattenwerkstoff`
       fordert `plattendickenAchse != null`; `WerkstoffStahl`
       fordert `plattendickenAchse == null`.
- **IFC-Mapping** (Persistenzschicht):
  - `IfcMaterial.Name` ← Subklasse + Festigkeitsklasse
    (z. B. „Vollholz C24", „BSH GL24h", „BSP CL3-h").
  - `IfcMaterial.Category` ← Subklasse (z. B. „axial timber",
    „cross-laminated timber").
  - Property Sets: `Pset_MaterialWoodBasedBeam` (axiales Holz),
    `Pset_MaterialWoodBasedPanel` (Plattenwerkstoffe).
- **Edge Cases**:
  - **Werkstoff ohne Faserrichtungs-Modus**: nicht erlaubt;
    Validierungsfehler bei Konstruktion.
  - **Werkstoff ohne Produktkennzeichnung**: nicht erlaubt;
    in frühen Entwurfsphasen darf eine Platzhalter-
    Produktkennzeichnung `Produktkennzeichnung.UNBEKANNT`
    geführt werden, die vor Bemessung aufgelöst sein muss.
  - **Mischwerkstoffe** (z. B. Hybrid CLT-Beton): nicht durch
    diese Hierarchie abgedeckt; eigene Folge-Klasse
    `werkstoff_hybrid` (Folgearbeit).
- **Bezeichner-Konvention** (CLAUDE.md): Domänen-Klasse heißt
  `Werkstoff` (deutsch, Glossarbegriff); Subklassen heißen
  `AxialesHolz`, `Mehrlagenholz`, `GerichteterPlattenwerkstoff`,
  `IsotroperPlattenwerkstoff`.

## Quellen

**Primär (normativ):**

- DIN EN 1995-1-1:2010-12, „Eurocode 5: Bemessung und Konstruktion
  von Holzbauten – Teil 1-1: Allgemeines – Allgemeine Regeln und
  Regeln für den Hochbau".
- SIA 265:2021, „Holzbau", Schweizerischer Ingenieur- und
  Architektenverein, Zürich.
- DIN EN 13986:2015-06, „Holzwerkstoffe zur Verwendung im Bauwesen
  – Eigenschaften, Bewertung der Konformität und Kennzeichnung".
- ISO 16739-1:2024, „Industry Foundation Classes (IFC) for data
  sharing in the construction and facility management industries
  — Part 1: Data schema".

**Sekundär:**

- Niemz, P.; Sonderegger, W.: *Physik des Holzes und der
  Holzwerkstoffe.* Hanser, München 2017.
- Blass, H. J.; Sandhaas, C.: *Ingenieurholzbau – Grundlagen der
  Bemessung.* KIT Scientific Publishing, Karlsruhe 2016.
- Forest Products Laboratory (FPL): *Wood Handbook — Wood as an
  Engineering Material.* General Technical Report FPL-GTR-282,
  USDA, Madison WI 2021.
- Schickhofer, G.: Forschungsarbeiten zum Brettsperrholz, TU Graz,
  Institut für Holzbau und Holztechnologie.
- Lignum (Hrsg.): *Holzbautabellen HBT.* Lignum, Zürich, aktuelle
  Auflage.

**Korpus (nicht autoritativ):**

- Holzbau Deutschland, Merkblatt „Begriffe und Klassifizierungen
  für den Holzbau" (abgerufen 2026-05-08).
- ProHolz Austria, „Brettsperrholz Bemessung Band I" (abgerufen
  2026-05-08).
- Wikipedia, Lemma „Holzwerkstoff" (abgerufen 2026-05-08).
