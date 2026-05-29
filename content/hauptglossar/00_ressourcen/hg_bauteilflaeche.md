---
id: bauteilflaeche
benennung: Bauteilfläche
synonyme: ["Bauteilseite", "Bezugsseite"]
abgelehnte_benennungen: ["Flächenrolle", "Fläche", "face", "component face"]
oberbegriff: null
begriffstyp: generisch
voraussetzungen: [bauteil, polygon, ebene, polyeder, toleranzen]
abgrenzung_zu: [laengsseite, stirnseite, dachseite, polygon, ebene, polyeder, querschnitt, bauteil]
status: entwurf
subglossar_pendant: optional
quellen_primär:
  - "ISO 16739-1:2024 (IFC 4.3.2), buildingSMART, Entitäten `IfcFace` (8.20.3.7), `IfcFaceBound` (8.20.3.8), `IfcFaceSurface` (8.20.3.10), `IfcConnectionSurfaceGeometry` (8.7.3.9) — topologisches Pendant zur einzelnen Bauteilfläche; semantische Klassifikation (Längsseite/Stirnseite) trägt das Schema nicht. [einsicht: snippet]"
  - "design2machine, BTLx Schema 2.3.1 (2025-07-08) bzw. BTL V10 — Reference Sides RS1–RS6 als indizierte Adressierung der sechs ausgezeichneten Aussenflächen eines prismatischen Stab-Bauteils; RS1–RS4 für Längsflächen, RS5/RS6 für Stirnflächen, `ReferencePlaneID`-Attribut an jedem Bearbeitungs-Element. [einsicht: snippet]"
quellen_sekundär:
  - "Tekla/Trimble: 'Timber NC – BTL', Knowledgebase (`support.tekla.com/article/timber-nc-btl`) — Reference-Side-Konvention für Holzbau-Maschinen-Übergabe."
  - "Dietrich's: 'Timber Coordinate Systems', `docs.dietrichs.com` — Reference Sides als 'bridge between component geometry, machining operations and CNC programming'."
  - "cadwork Knowledgebase, IFC-Workflow (`kb.cadwork.ch/holzbau/manual/1064`, `1018`, `1081`) — interne BTL/BTLx-Reference-Side-Logik bei Abbund-Export."
  - "Hundegger Maschinenbau GmbH, BVN/BVX-Format-Dokumentation — Numerierung 1–4 für Längsseiten, 'Front'/'Rear' für Stirnseiten."
  - "Hoffmann, C. M.: Geometric and Solid Modeling – An Introduction. Morgan Kaufmann 1989, Kap. 3 (B-Rep): Polyeder-Facette als Trägerstruktur."
  - "Mäntylä, M.: An Introduction to Solid Modeling. Computer Science Press 1988, Kap. 6 (Boundary Representation): Face-with-Role-Pattern als Annotations-Schicht über der Topologie."
quellenkonflikt: |
  **Asymmetrie zwischen Recherche-Empfehlung und App-Festlegung.** Die
  Vorabrecherche (`docs/recherche/2026-05-14_hg_bauteilflaeche.md`) hat
  die Hypothese, „Bauteilfläche" sei im DACH-Holzbau-Korpus ein
  etablierter Single-Word-Fachbegriff, **falsifiziert**: weder in den
  konsultierten Normen (DIN 4074-1, DIN EN 14081-1, DIN EN 14080,
  DIN EN 1995-1-1, DIN 1052, DIN 68800-2, DIN EN 350,
  DIN ISO 80000-2, SIA 260, SIA 265, SIA 232/1, ISO 16739-1) noch in
  der einschlägigen Lehrbuchliteratur (Natterer/Herzog, Mönck/Rug,
  Blass/Sandhaas, Gerner, Lignum HBT) noch in den durchsuchten
  Berufsglossaren tritt „Bauteilfläche" als geschlossener Sammel-
  Oberbegriff für Längsseite, Stirnseite und vergleichbare
  ausgezeichnete Aussenflächen eines Bauteils auf. Die Normen
  verwenden spezialisierte Bezeichnungen (Schmalseite, Breitseite,
  Hirnseite, Stirnseite, Längsseite) **ohne** Sammel-Oberbegriff. Die
  Recherche-Empfehlung lautete entsprechend: Eintrag erst beim
  Eintreten des Folgearbeit-Triggers (`HG_KONVENTIONEN.md` §6.A)
  anlegen.

  **Eric/Hauptinstanz hat dennoch entschieden, den Eintrag jetzt
  anzulegen** — als App-eigener Konstruktbegriff mit CAD/CAM-Anker
  statt Norm-Anker. Begründung dieser Entscheidung:

  - Die Domänen-Schicht der App benötigt absehbar einen einheitlichen
    Adressierungs-Begriff für die ebenen Aussenflächen eines Bauteils
    (Sammel-Iteration im Renderer, BTLx-Export-Schicht mit
    Reference-Side-Mapping, Bearbeitungs-Verortung). Die Symmetrie
    zwischen `laengsseite` und `stirnseite` ist im bisherigen Glossar
    bereits präfiguriert (`hg_laengsseite.md` und `hg_stirnseite.md`
    führen einen gleichlautenden Folgearbeit-Block); der jetzt
    angelegte Sammelbegriff schliesst diese Symmetrie.
  - Die CAD/CAM-Praxis (BTL/BTLx Reference Sides RS1–RS6 seit 2006
    cadwork/SEMA-Standard; Hundegger BVN/BVX; Dietrich's Timber
    Coordinate Systems) trägt das Konzept einer indexierten,
    semantisch addressierbaren Aussenflächen-Familie eines Bauteils
    durchgehend. Sie liefert den **technologischen Anker** anstelle
    eines normativen.
  - IFC 4.3 trägt das Konzept **topologisch** über `IfcFace` /
    `IfcFaceBound` / `IfcFaceSurface` und die Verbindungs-Sicht
    `IfcConnectionSurfaceGeometry`, ohne eine semantische
    Klassifikation der einzelnen Bauteilfläche zu persistieren.
    Die App schliesst diese Klassifikations-Lücke explizit durch den
    `bauteilflaeche`-Begriff.

  **Verhältnis zu den Spezialisierungs-Einträgen.** Die bestehenden
  Einträge `hg_laengsseite.md` und `hg_stirnseite.md` tragen
  `oberbegriff: bauteilflaeche` (Migration im selben R-Schritt
  nachgezogen, in dem dieser Eintrag entstand). Der entsprechende
  Trigger-Eintrag in `HG_KONVENTIONEN.md` §6.A wurde mit derselben
  R-Schritt-Welle gestrichen.

  **Festlegung dieses Glossars** (konsistent mit allen konsultierten
  Quellen):

  - **Bauteilfläche** ist eine **Facette des Bauteilpolyeders** im
    Sinne von `polyeder` (B-Rep-Modell), die zugleich eine
    Bauteilrolle (Aussenfläche eines bestimmten Bauteils mit
    Aussennormalen-Konvention und Adressierungs-Identität) trägt. Die
    Bauteilfläche bündelt damit drei Bestandteile: ein Polygon in
    Berandungs-Lesart, die Trägerebene des Polygons und die
    Bauteilrolle (Aussennormale, Bauteil-Referenz, Adressierungs-
    Index).
  - **Die App führt die Rolle, nicht das Polyeder.** Geometrisch ist
    eine Bauteilfläche eine bereits am Bauteilpolyeder vorhandene
    Polygon-Facette; die App fügt die semantische Klassifikation
    (Längsseite/Stirnseite/Dachseite/…) als separate Indizierungs-/
    Annotationsschicht über der Polyeder-Topologie hinzu. Diese
    Modellierungslinie folgt der CAD/CAM-Praxis (BTL/BTLx, cadwork
    intern, Dietrich's) und entspricht in der mathematisch-CAD-
    Literatur dem „Face-with-Role"-Pattern (Hoffmann, Mäntylä).
  - **Hauptbenennung „Bauteilfläche"** (Eric-Festlegung im Auftrag).
    „Bauteilseite" ist als Synonym geführt, weil alle bisherigen
    Spezialisierungen (Längsseite, Stirnseite, Schmalseite, Breitseite,
    Dachseite) `-seite`-Komposita sind. „Bezugsseite" ist als
    Spezialisierungs-Synonym im CAD/CAM-Kontext geführt (entspricht
    BTLx Reference Side / RS-Index).
  - **Abgelehnt** sind „Flächenrolle" (abstrakt-neologistisch, im
    Holzbau nicht anschlussfähig), „Fläche" (zu allgemein —
    konkurriert mit Dachfläche/Wandfläche), „face" / „component face"
    (englische Lehnwörter; in deutscher Glossarsprache abgelehnt).
  - **Bauteilfläche ist ausschliesslich auf Aussenflächen mit ebener
    Trägerebene beschränkt.** Nicht-ebene Aussenflächen
    (Mantelfläche einer Rundholzstütze, gekrümmter Bogenträger-Mantel)
    werden in eigenen Folge-Einträgen erfasst (`mantelflaeche`,
    Folgearbeit).
  - **`oberbegriff: null`.** Strukturell ist die Bauteilfläche keine
    Spezialisierung von `polygon` allein (sie bündelt drei
    Bestandteile, nicht eines), und sie ist keine Spezialisierung von
    `polyeder` (sie ist Bestandteil eines Polyeders, nicht selbst
    eines). Sie wird als eigener Sammelknoten unterhalb der Schicht
    (`polygon`, `polyeder`, `bauteil`) geführt; ihre Spezialisierungen
    sind aktuell `laengsseite`, `stirnseite`, `dachseite` (mit der
    bereits existierenden, im Folgearbeit-Block dokumentierten
    Migrations-Vormerkung).
---

## Prosa-Definition

Eine **Bauteilfläche** ist eine ebene, polygonal berandete
Aussenfläche eines Bauteils, die als Facette des Bauteilpolyeders
auf einer eindeutig bestimmten Trägerebene liegt, mit aus dem
Bauteil heraus zeigender Aussennormale orientiert ist und eine im
Kontext des zugehörigen Bauteils eindeutige Adressierungs-Identität
trägt.

## Mathematische Definition

Sei

- B ein **Bauteil** im Sinne von `bauteil` mit identifizierter UUID
  und einem Bauteilkörper, dessen geometrische Repräsentation ein
  Polyeder P(B) = (V_B, E_B, F_B, ι_F, ι_E) im Sinne von `polyeder`
  (B-Rep) ist,
- F_B = (F_1, …, F_k) die Familie der Begrenzungsflächen von P(B);
  jedes F_l ist ein **Polygon** in Berandungs-Lesart (siehe
  `polygon`, Abschnitt „Zwei zulässige Lesarten") in einer
  zugehörigen Trägerebene E_l (siehe `ebene`),
- n_hat_l ∈ S² die nach `polyeder` (Mannigfaltigkeits-Orientierung)
  eindeutig bestimmte aus P(B) heraus zeigende Einheitsnormale der
  Facette F_l,
- I_B eine endliche Indexmenge zur Adressierung der ausgezeichneten
  Aussenflächen von B (zum Beispiel `I_B ⊆ {RS1, …, RS6}` im
  prismatischen BTLx-Fall),
- ρ : I_B → F_B eine **Rollen-Zuordnung**, die jedem
  Adressierungs-Index ι ∈ I_B genau eine Facette ρ(ι) ∈ F_B
  zuordnet, mit ρ injektiv (jede ausgezeichnete Aussenfläche trägt
  genau einen Index).

Eine **Bauteilfläche** von B ist ein Tupel

```
BF(B, ι) := (F_l, E_l, n_hat_l, B, ι)                                    (1)
            mit F_l := ρ(ι),   ι ∈ I_B,   l ∈ {1, …, k}.
```

Die Tupel-Bestandteile sind:

1. **Polygon-Berandung** F_l ∈ F_B (Polygon in Berandungs-Lesart in
   E_l; siehe `polygon`).
2. **Trägerebene** E_l (Ebene im Sinne von `ebene`, durch einen
   beliebigen Eckpunkt von F_l und n_hat_l in Hesse-Normalform
   eindeutig bestimmt).
3. **Aussennormale** n_hat_l (aus P(B) heraus zeigend, Mannigfaltigkeits-
   Orientierung der Hülle ∂P(B); siehe `polyeder`, Bedingung 4).
4. **Bauteil-Referenz** B (UUID des zugehörigen Bauteils).
5. **Adressierungs-Index** ι ∈ I_B (Rolle der Bauteilfläche im
   Kontext von B; im prismatischen BTLx-Fall einer der Werte
   RS1–RS6).

Die **Menge aller Bauteilflächen** von B ist

```
𝓑𝓕(B) := { BF(B, ι) | ι ∈ I_B } ⊆ F_B × ℰ × S² × {B} × I_B,         (2)
```

mit |𝓑𝓕(B)| = |I_B|. Die Abbildung ι ↦ BF(B, ι) ist injektiv.

## Wohldefiniertheit

- **Existenz.** Für jedes Bauteil B mit nicht-degenerierter Polyeder-
  Hülle existiert mindestens eine Begrenzungsfläche (per `polyeder`-
  Definition gilt k ≥ 4); die App-typischen prismatischen Stab-
  Bauteile mit Rechteck-Querschnitt liefern genau k = 6 Facetten und
  damit |I_B| ≤ 6. Plattenbauteile liefern typisch k = 6
  (zwei Plattenflächen + vier Plattenkanten), gekrümmte oder
  ausgeschnittene Bauteile haben k entsprechend größer. Die
  Indexmenge I_B wird durch die zugehörige Bauteilrolle-Konvention
  festgelegt; im prismatischen Stab-Standardfall gilt I_B = {RS1,
  RS2, RS3, RS4, RS5, RS6} mit ρ(RS1)…ρ(RS4) = vier Längsseiten,
  ρ(RS5) = Anfangs-Stirnseite, ρ(RS6) = End-Stirnseite (BTL/BTLx-
  Konvention).

- **Eindeutigkeit.** Bei festgelegtem Bauteilpolyeder P(B) und
  festgelegter Rollen-Zuordnung ρ ist BF(B, ι) für jeden Index
  ι ∈ I_B eindeutig durch die Facette ρ(ι), ihre Trägerebene, ihre
  Aussennormale und das zugehörige Bauteil bestimmt. Die
  Trägerebene ist nach `ebene` (modulo Vorzeichen); die kanonische
  Vorzeichenwahl ist „Aussennormale" und damit eindeutig.

- **Wohldefiniertheit der Aussennormale.** Da P(B) per `polyeder`-
  Bedingung 4 eine geschlossene, orientierbare 2-Mannigfaltigkeits-
  Hülle besitzt, ist die Aussen-Orientierung jeder Facette eindeutig
  bestimmt; n_hat_l ist damit ohne weitere Wahl festgelegt.

- **Repräsentanten-Unabhängigkeit der Trägerebene.** Die Trägerebene
  E_l hängt nicht vom gewählten Stützpunkt der Hesse-Normalform ab
  — jeder Eckpunkt von F_l liefert dieselbe Ebene (siehe `ebene`,
  Wohldefiniertheits-Abschnitt). Insbesondere ist die Trägerebene
  unabhängig von der zyklischen Reihenfolge der Polygon-Eckpunkte.

- **Disjunktheit zwischen verschiedenen Bauteilflächen desselben
  Bauteils.** Die Bauteilflächen-Polygone F_l und F_m (l ≠ m) eines
  Bauteilpolyeders teilen höchstens Randkanten (per `polyeder`-
  Mannigfaltigkeits-Bedingung 2), nicht aber Innenpunkte; die Tupel
  BF(B, ι_l) und BF(B, ι_m) unterscheiden sich folglich bereits in
  ihrer Polygon-Berandungs-Komponente.

- **Nicht-Zirkularität.** Die Definition stützt sich auf `bauteil`,
  `polyeder` (B-Rep), `polygon` (Berandungs-Lesart), `ebene` und
  nimmt nicht auf `laengsseite`, `stirnseite` oder `dachseite`
  Bezug. Die Spezialisierungen werden im Beziehungs-Abschnitt
  benannt, aber nicht in der Definition vorausgesetzt.

- **Eliminierbarkeit.** Jede Verwendung von „Bauteilfläche" lässt
  sich durch das Tupel (Facette, Trägerebene, Aussennormale,
  Bauteil-Referenz, Adressierungs-Index) ersetzen.

- **Grenzfälle.**
  - **Bauteil mit Rundquerschnitt** (Rundholzstütze, Bogenträger):
    die Mantelfläche ist nicht eben und folglich keine
    Polyeder-Facette im strengen Sinne. Solche Aussenflächen werden
    in eigenen Folge-Einträgen erfasst (`mantelflaeche`, Folgearbeit);
    der Bauteilflächen-Begriff bleibt auf ebene Facetten beschränkt.
    In der App-Praxis werden gekrümmte Mantelflächen typisch
    durch polygonale Approximation (Tessellierung) in eine endliche
    Familie ebener Facetten zerlegt, jede davon eine Bauteilfläche
    im Sinne dieses Eintrags.
  - **Bauteilfläche mit Bearbeitung** (Kerve, Versatz, Schlitz): die
    Polygon-Berandung wird durch die Bearbeitung modifiziert; die
    bearbeitete Polygonkette ist die neue Bauteilflächen-Berandung
    (siehe `bearbeitung`, Folgearbeit). Der Adressierungs-Index ι
    ändert sich nicht.
  - **Plattenbauteile mit Faserrichtungs-Modus SCHWACH / KEINE**
    (OSB, Spanplatte, siehe Memory `project_faserrichtung_modi`):
    die Bauteilflächen-Geometrie ist unberührt; die semantische
    Spezialisierungs-Familie ist eine andere (Plattenfläche /
    Plattenkante / Schmalseite / Breitseite im
    Plattenwerkstoff-Sinn, siehe Folgearbeit-Block).

## Erläuterung (nicht normativ)

### Hinweis zur Theorie-Pflicht

`subglossar_pendant: optional` (Abweichung vom Normalfall `notwendig`,
`HG_KONVENTIONEN.md` §7) ist hier **bewusst** gewählt: die didaktische
Substanz liegt bei den Spezialisierungen (`laengsseite`, `stirnseite`,
`dachseite` — alle `notwendig`), die ihre eigenen Subglossar-Pendants
tragen. Der abstrakte Sammelbegriff selbst trägt keinen eigenständigen
Stufen-Inhalt, der nicht schon durch die Spezialisierungen abgedeckt
ist.

### Was die Bauteilfläche bündelt

Eine Bauteilfläche ist die App-eigene Zusammenfassung von drei
Schichten:

1. **Topologische Schicht**: eine Facette des Bauteilpolyeders (im
   IFC-Vokabular: ein `IfcFace` mit `IfcFaceBound`).
2. **Geometrische Schicht**: das Polygon in Berandungs-Lesart und
   seine Trägerebene mit Aussennormale.
3. **Rollen-Schicht**: die Bauteil-Identifikation (UUID), der
   Adressierungs-Index ι (zum Beispiel BTLx RS1–RS6) und – über die
   konkrete Spezialisierung – die semantische Klassifikation
   (Längsseite / Stirnseite / Dachseite / Schmalseite / Breitseite /
   Plattenfläche / Plattenkante).

Diese Bündelung ist im DACH-Holzbau-Korpus **nicht als stehender
Fachbegriff etabliert** (siehe `quellenkonflikt:`-Block), in der
CAD/CAM-Werkzeugkette und in der IFC-Schicht jedoch in
verschiedenen, kompatiblen Varianten technisch vorhanden:

| Werkzeug / Standard         | Pendant zur Bauteilfläche                     |
|-----------------------------|------------------------------------------------|
| BTL / BTLx                  | Reference Side RS1–RS4 (Längs), RS5/RS6 (Stirn) |
| Hundegger BVN/BVX           | Längsseiten 1–4, „Front"/„Rear" (Stirn)       |
| Dietrich's, cadwork intern  | Reference Sides als Adressierung von Bearbeitungen |
| IFC 4.3 (topologisch)       | `IfcFace` + `IfcFaceBound` (+ ggf. `IfcFaceSurface`) |
| IFC 4.3 (relational)        | `IfcConnectionSurfaceGeometry` als Verbindungs-Sicht |
| Solid-Modeling-Literatur    | Face-with-Role-Pattern (Hoffmann, Mäntylä)    |

Die App führt die **Rolle**, nicht das Polyeder: der Polyeder-Begriff
trägt die Topologie und die Aussennormalen-Orientierung; die
Bauteilfläche fügt die semantische Klassifikation und die
Adressierungs-Identität als separate Schicht hinzu.

### Geschwister-Familie der Bauteilflächen

Die Spezialisierungen der Bauteilfläche unterscheiden sich nach
Bauteilart und Bezugsrichtung:

| Spezialisierung      | Bauteilart                | Lage zur Bauteilachse / Bauteilrolle             |
|----------------------|---------------------------|---------------------------------------------------|
| `laengsseite`        | Stabbauteil               | Trägerebene parallel zur Bauteilachse             |
| `stirnseite`         | Stabbauteil               | Trägerebene rechtwinklig (oder geneigt) zur Bauteilachse, an Bauteilende |
| `schmalseite` (Folgearbeit) | Rechteck-Stab     | Längsseite parallel zur Querschnittsbreite        |
| `breitseite` (Folgearbeit)  | Rechteck-Stab     | Längsseite parallel zur Querschnittshöhe          |
| `mantelflaeche` (Folgearbeit) | Rundholz-Stab    | nicht-eben; durch Tessellierung als Familie ebener Bauteilflächen darstellbar |
| `plattenflaeche` (Folgearbeit) | Plattenbauteil  | grosse Aussenfläche der Platte (Ober-/Unterseite) |
| `plattenkante` (Folgearbeit)   | Plattenbauteil  | schmale Aussenfläche der Platte (Stirn-Entsprechung) |
| `plattenschmalseite` /         |                   |                                                   |
| `plattenbreitseite` (Folgearbeit) | Plattenbauteil | Plattenkanten-Familie nach Faserrichtungs-Modus  |
| `dachseite`          | Dachbauteil-Gruppen-Sicht | Dachfläche unter Orientierungs-Annotation (Wetter-, Sonnen-, Trauf-, Giebelseite) |

Die Familie ist nicht abgeschlossen: weitere Bauteilarten (Hohlkasten-
Aussenflächen, Brettstapel-Schnittflächen, gekrümmte Träger) ziehen
weitere Spezialisierungen nach sich, sobald sie in der App
modelliert werden.

### Verhältnis zur Dachseite

`dachseite` ist im aktuellen Glossar `begriffstyp: merkmal` (eine
Dachfläche unter Orientierungs-Annotation) und steht unter
`oberbegriff: dachflaeche`, nicht unter `polygon` wie `laengsseite`
und `stirnseite`. Die Dachseite ist daher eine **gemischte
Spezialisierung**: geometrisch eine Dachfläche, semantisch eine
Bauteilfläche eines Dachbauteils-Aggregats unter zusätzlicher
Orientierungs-Annotation. Eine Migration ihrer Beziehung in die
Bauteilflächen-Familie ist möglich, aber nicht zwingend; sie wird
im Folgearbeit-Block vorgemerkt.

### Plattenwerkstoff-Familie (Memory `project_faserrichtung_modi`)

Plattenwerkstoffe mit Faserrichtungs-Modi STRUKTURIERT, SCHWACH
oder KEINE tragen eine eigene Bauteilflächen-Familie:

- **Plattenflächen** (Ober-/Unterseite): die beiden grossen
  Aussenflächen einer Platte; geometrisch parallel und in der App
  ggf. ohne ausgezeichnete Ober-/Unterseiten-Unterscheidung (Modus
  KEINE oder SCHWACH ohne Annotation).
- **Plattenkanten** (Stirn-Entsprechung): die vier (im Rechteck-
  Standardfall) schmalen Aussenflächen. Bei gerichtetem
  Plattenwerkstoff (LVL, CLT mit Hauptrichtung) zerfallen sie weiter
  in **Plattenschmalseite** und **Plattenbreitseite** je nach Bezug
  zur Plattenlängsrichtung. Bei isotropem Plattenwerkstoff
  (Spanplatte) entfällt diese Unterscheidung.

Diese Familie ist eine **eigenständige Spezialisierungs-Achse** der
Bauteilfläche und nicht mit der Stab-Familie (Längsseite /
Stirnseite / Schmalseite / Breitseite) zu vermengen. Die App
unterscheidet sie strukturell über den Werkstoff-Modus des
Bauteils (`werkstoff`, `faserrichtungs_modus`); die Bauteilflächen-
Definition selbst bleibt einheitlich.

## Beziehungen

- **Oberbegriff**: `null`. Die Bauteilfläche ist als App-eigener
  Sammelknoten ohne übergeordneten Glossarbegriff geführt. Ihre
  unmittelbaren strukturellen Voraussetzungen — `polygon` (in
  Berandungs-Lesart als topologische Substanz der Facette) und
  `bauteil` (als Träger der Rollen-Identität) — stehen in
  `voraussetzungen:`, nicht in `oberbegriff:`.
- **Spezialisierungen**:
  - **`laengsseite`** (bereits angelegt; `oberbegriff: bauteilflaeche`).
  - **`stirnseite`** (bereits angelegt; `oberbegriff: bauteilflaeche`).
  - **`dachseite`** (bereits angelegt; aktuell `oberbegriff:
    dachflaeche` mit `begriffstyp: merkmal`; mögliche zusätzliche
    Sicht als Spezialisierung von `bauteilflaeche`, siehe
    Folgearbeit-Block).
  - **`schmalseite`** / **`breitseite`** (Folgearbeit, Längsseiten-
    Spezialisierungen bei Rechteck-Querschnitt).
  - **`mantelflaeche`** (Folgearbeit, rotationssymmetrische
    Stab-Bauteile).
  - **`plattenflaeche`** / **`plattenkante`** (Folgearbeit,
    Plattenbauteile).
- **Bestandteile (partitiv)** (im Sinne der Tupel-Bestandteile von
  Gleichung (1)):
  - Polygon-Berandung F_l in Berandungs-Lesart (geerbt von `polygon`).
  - Trägerebene E_l (geerbt von `ebene`).
  - Aussennormalen-Vektor n_hat_l (Mannigfaltigkeits-Orientierung des
    Bauteilpolyeders).
  - Bauteil-Referenz B (UUID).
  - Adressierungs-Index ι ∈ I_B (zum Beispiel BTLx RS1–RS6).
- **Verwendung**:
  - **Sammel-Iteration** über die Aussenflächen eines Bauteils im
    Renderer und im Werkplan-Modul.
  - **BTLx-Export** (Folgearbeit Phase 4): jede Bearbeitung
    referenziert eine Bauteilfläche über ihren Adressierungs-Index
    (`ReferencePlaneID` im BTLx-Schema).
  - **Verbindungs-Modellierung** (`verbindung`, `verbindungsmittel`):
    Verbindungs-Aufstandsflächen und Verbindungsmittel-
    Eindringungspunkte werden Bauteilflächen zugeordnet.
  - **3D-Visualisierung**: einheitliche Aussennormalen-Behandlung
    aller Bauteilflächen eines Bauteils für Backface-Culling und
    Materialzuweisung im Renderer.
  - **IFC-Export** (Folgearbeit Phase 4): jede Bauteilfläche wird
    auf eine Kombination aus `IfcFace` / `IfcFaceBound` /
    `IfcFaceSurface` abgebildet; die Rollen-Klassifikation wird über
    `IfcPropertySet` (kein normativer Standard, App-Konvention)
    persistiert.
- **Abgrenzung**:
  - **`polygon`**: geometrisches Primitiv ohne Bauteilrolle und
    ohne Aussennormalen-Konvention. Eine Bauteilfläche enthält ein
    Polygon (in Berandungs-Lesart) als topologische Substanz, ist
    aber selbst kein Polygon.
  - **`ebene`**: die Trägerebene einer Bauteilfläche ist eine Ebene
    im Sinne von `ebene`; die Bauteilfläche selbst ist eine
    **beschränkte** Teilmenge dieser Ebene mit Bauteilrolle.
  - **`polyeder`**: der Bauteilkörper als Ganzes ist ein Polyeder;
    eine Bauteilfläche ist eine **einzelne Facette** dieses
    Polyeders zusammen mit ihrer Bauteilrolle. Das Polyeder bündelt
    alle Bauteilflächen eines Bauteils zur geschlossenen Hülle.
  - **`querschnitt`**: Schnittfigur eines Stab-Bauteils mit einer
    Ebene rechtwinklig zur Bauteilachse an einer beliebigen Stelle.
    Ein Querschnitt liegt im **Inneren** des Bauteilkörpers (per
    Definition; siehe `hg_querschnitt.md`) — es sei denn am
    Bauteilende, wo der Querschnitt mit der prismatisch-
    rechtwinkligen Stirnseite zusammenfällt. Eine Bauteilfläche ist
    grundsätzlich eine **Aussenfläche** und damit Bestandteil der
    Bauteilhülle, kein Inneren-Schnitt.
  - **`bauteil`**: ein Bauteil hat eine Familie von Bauteilflächen;
    es ist aber selbst keine Bauteilfläche, sondern das übergeordnete
    Element mit Identität, Geometrie und Werkstoff.
  - **`laengsseite`**, **`stirnseite`**, **`dachseite`** als bereits
    existierende Spezialisierungen sind im Spezialisierungs-Block
    geführt; die Abgrenzung gegen den Sammelbegriff besteht in der
    Spezialisierungs-Beziehung (Bauteilfläche-Sein impliziert eine
    der Spezialisierungen).

## Implementierungshinweis

Datentyp (Domänen-Schicht, Kotlin, Schicht
`domain.bauteil.flaeche`):

```kotlin
package domain.bauteil.flaeche

import domain.bauteil.Bauteil
import domain.geometrie.Ebene
import domain.geometrie.Polygon
import domain.geometrie.Vektor
import domain.identifikation.Uuid

/**
 * Bauteilfläche: ebene Aussenfläche eines Bauteils als Facette des
 * Bauteilpolyeders mit Aussennormalen-Konvention, Bauteil-Referenz
 * und Adressierungs-Index (z. B. BTLx RS1–RS6).
 *
 * Glossar: hg_bauteilflaeche.md
 *
 * Die Klasse ist eine sealed-Basis für die konkreten
 * Spezialisierungen (Längsseite, Stirnseite, Dachseite, Schmalseite,
 * Breitseite, Plattenfläche, Plattenkante, …). Die Spezialisierungen
 * tragen rollenspezifische Constraints (Lage zur Bauteilachse,
 * Faserrichtungs-Bezug, Plattenwerkstoff-Achse).
 *
 * Aussennormale n_hat_l zeigt per Konvention aus dem Bauteilpolyeder
 * heraus; ihre Orientierung folgt aus der Mannigfaltigkeits-
 * Orientierung der Bauteilhülle (siehe hg_polyeder.md).
 */
sealed class Bauteilflaeche {
    abstract val polygon: Polygon               // F_l in Berandungs-Lesart
    abstract val traegerebene: Ebene             // E_l, durch p_0 ∈ F_l und n_hat_l
    abstract val aussennormale: Vektor           // n_hat_l, ‖aussennormale‖ ≈ 1
    abstract val bauteil: Uuid                   // B (UUID-Referenz)
    abstract val adressierung: AdressierungsIndex // ι ∈ I_B (z. B. BTLx RS1–RS6)
}

/**
 * Adressierungs-Index einer Bauteilfläche im Kontext ihres Bauteils.
 * Im prismatischen Stab-Standardfall entspricht der Index der
 * BTLx-Reference-Side-Konvention (RS1–RS4 Längs, RS5/RS6 Stirn).
 *
 * Folgearbeit: Plattenbauteil-Adressierung (RS-Schema oder eigenes)
 * und gekrümmte Bauteile.
 */
sealed class AdressierungsIndex {
    data class BtlxReferenceSide(val nummer: Int) : AdressierungsIndex()
    // weitere Adressierungs-Schemata folgen
}
```

- **Einheit**: Polygonkoordinaten in mm; Aussennormale dimensionslos
  (Einheitsvektor).
- **Identität**: keine eigene UUID. Die Bauteilfläche ist eine
  **abgeleitete Sicht** auf das Bauteilpolyeder und trägt ihre
  Identität indirekt über die Kombination aus `bauteil` (UUID-
  Referenz) und `adressierung` (Index). Diese Wahl ist konsistent
  mit den bereits existierenden Spezialisierungen `laengsseite` und
  `stirnseite` (beide ohne eigene UUID).
- **Pflicht- und Optionalfelder**:
  - `polygon` — Pflicht; ebenes Polygon in Berandungs-Lesart.
  - `traegerebene` — Pflicht; durch das Polygon und die
    Aussennormale eindeutig bestimmt (siehe Wohldefiniertheit).
  - `aussennormale` — Pflicht; aus dem Bauteilpolyeder heraus zeigend.
  - `bauteil` — Pflicht; UUID-Referenz auf das zugehörige Bauteil.
  - `adressierung` — Pflicht; Index ι ∈ I_B im Kontext des Bauteils.
- **Invarianten** (in Companion-Factory der jeweiligen
  Spezialisierung, `Resultat.Fehler` bei Verletzung; keine
  Exception):
  1. `aussennormale` ist normiert (‖aussennormale‖² ≈ 1 innerhalb
     `Toleranzen.NORM_EPS`).
  2. `traegerebene` enthält alle Eckpunkte von `polygon`
     (Polygon-Berandung liegt in der Trägerebene; per `polygon`-
     Definition Bedingung 1).
  3. `traegerebene.normale` ist parallel zu `aussennormale`
     (Mannigfaltigkeits-Orientierungs-Konsistenz; siehe
     `Toleranzen.KOLLINEAR_EPS`).
  4. `bauteil` referenziert eine existierende Bauteil-Instanz im
    Modell-Zustand.
  5. `adressierung` ist im Kontext des referenzierten Bauteils
     eindeutig (jeder Index nur einer Bauteilfläche zugeordnet;
     Rollen-Zuordnung ρ ist injektiv).
- **Konstruktion**: Bauteilflächen werden aus dem Bauteil-Polyeder
  und der Rollen-Zuordnung abgeleitet, nicht unabhängig
  konstruiert. Die Domänen-Schicht stellt Faktor-Funktionen
  `Bauteil.bauteilflaechen()` und
  `Bauteil.bauteilflaecheBeiIndex(adressierung)` bereit.
- **IFC-Mapping** (Persistenzschicht, Phase 4):
  - Bauteilfläche → `IfcFace` mit `IfcFaceBound` und (sofern
    Trägergeometrie persistiert) `IfcFaceSurface` auf einer
    `IfcPlane`.
  - Adressierungs-Index und Rollen-Klassifikation → `IfcPropertySet`
    am `IfcFace` (App-Konvention; kein normatives IFC-Property-Set
    für diese Klassifikation vorhanden).
  - Verbindungs-Sicht zweier Bauteilflächen →
    `IfcConnectionSurfaceGeometry` mit `SurfaceOnRelatingElement`
    und `SurfaceOnRelatedElement`.
- **BTLx-Mapping** (Persistenzschicht, Phase 4):
  - Bauteilfläche → BTLx Reference Side (RS1–RS6 im prismatischen
    Stab-Standardfall).
  - Bearbeitung auf einer Bauteilfläche → `ReferencePlaneID`-
    Attribut des zugehörigen Bearbeitungs-Elements im BTLx-Schema.
- **Edge Cases**:
  - **Bauteilfläche an Bauteil mit Rundquerschnitt**: nicht-ebene
    Mantelfläche; nicht als Bauteilfläche im engen Sinne dieses
    Eintrags geführt, sondern als `mantelflaeche` (Folgearbeit) oder
    als tessellierte Familie ebener Bauteilflächen (App-Wahl).
  - **Bauteilfläche an Bauteil mit Bearbeitung** (Kerve, Versatz,
    Schlitz, Bohrung): die Polygon-Berandung enthält die durch die
    Bearbeitung erzeugten zusätzlichen Eckpunkte. Bei
    durchgehenden Bohrungen entsteht keine neue Bauteilfläche
    (die Bohrung wird über `bearbeitung` referenziert, nicht über
    eine eigene Bauteilfläche).
  - **Bauteilfläche an Plattenbauteil**: die Spezialisierungs-
    Familie ist eine andere (`plattenflaeche` / `plattenkante` /
    `plattenschmalseite` / `plattenbreitseite` — Folgearbeit). Die
    Bauteilflächen-Definition selbst bleibt anwendbar.
  - **Sehr kleine Bauteilflächen** (Polygon-Flächeninhalt < etwa
    Toleranzen.FLAECHE_EPS): tritt typisch bei Tessellierung
    auf; die App kann solche Mikro-Facetten zusammenfassen oder
    als entartet ausweisen (Geometrie-Schicht-Entscheidung).
- **Bezeichner-Konvention** (CLAUDE.md): Klasse heißt
  `Bauteilflaeche` (deutsch, Glossarbegriff; ASCII-Schreibweise
  wegen Kotlin-Identifier-Konvention). Die `sealed class`-Hierarchie
  trägt die bereits existierenden Spezialisierungs-Klassen
  `Laengsseite` und `Stirnseite` als Subtypen (Migrations-
  Folgearbeit, siehe unten).

**Folgearbeit (trigger-basiert):**

- **Migration der Code-Hierarchie**: Umstellung von
  `data class Laengsseite` und `data class Stirnseite` auf
  `class Laengsseite : Bauteilflaeche()` bzw.
  `class Stirnseite : Bauteilflaeche()` mit gemeinsamer
  sealed-Basis. Auslöser: erste Domänen-Operation, die einheitlich
  über die Bauteilflächen eines Bauteils iteriert.
- **Schmalseite / Breitseite** (Stab-Spezialisierungen bei
  Rechteck-Querschnitt): Folgearbeit gemäss Folgearbeit-Block in
  `hg_laengsseite.md`.
- **Mantelfläche** (rotationssymmetrische Stab-Bauteile): eigener
  Glossar-Eintrag und Code-Subtyp; Auslöser: erstes Bauteil mit
  Rundquerschnitt.
- **Plattenflächen-Familie**: `plattenflaeche` (Ober-/Unterseite),
  `plattenkante` (Stirn-Entsprechung), bei gerichtetem
  Plattenwerkstoff zusätzlich `plattenschmalseite` und
  `plattenbreitseite`. Auslöser: erstes Plattenbauteil mit
  expliziter Flächenmodellierung. Diese Familie ist eine
  eigenständige Spezialisierungs-Achse der Bauteilfläche und
  orthogonal zur Stab-Familie (Längsseite / Stirnseite); ihre
  Differenzierung folgt dem Faserrichtungs-Modus des Bauteils
  (Memory `project_faserrichtung_modi`).
- **Dachseite-Verhältnis klären**: aktuell `oberbegriff:
  dachflaeche` mit `begriffstyp: merkmal`. Eine zusätzliche Sicht
  als Spezialisierung von `bauteilflaeche` (über die Dachbauteil-
  Aussenflächen eines Dachflächen-Aggregats) ist möglich, aber
  nicht zwingend. Auslöser: erste App-Operation, die Dachseiten und
  Stab-Bauteilflächen einheitlich adressieren muss.
- **Adressierungs-Index-Vereinheitlichung**: aktuell ist der Index
  als sealed `AdressierungsIndex` mit `BtlxReferenceSide` als
  einzigem Konstruktor angelegt. Weitere Adressierungs-Schemata
  (Plattenbauteil-Codes, gekrümmte Bauteile, Hohlkasten) werden
  bei Bedarf ergänzt.
- **`IfcPropertySet`-Schema** für die Rollen-Klassifikation:
  App-Konvention, ohne IFC-normativen Standard. Folgearbeit Phase 4
  bei IFC-Export-Etappe.

## Quellen

**Primär (normativ und technisch-standard):**

- ISO 16739-1:2024, „Industry Foundation Classes (IFC) for data
  sharing in the construction and facility management industries
  – Part 1: Data schema". buildingSMART International; insbesondere
  Entitäten `IfcFace` (Abschnitt 8.20.3.7), `IfcFaceBound`
  (8.20.3.8), `IfcFaceSurface` (8.20.3.10),
  `IfcConnectionSurfaceGeometry` (8.7.3.9).
- design2machine: BTLx Schema Version 2.3.1 (Stand 2025-07-08), und
  BTL V10. <https://www.design2machine.com/btlx/> bzw.
  <https://www.design2machine.com/btl/>. Reference Sides RS1–RS6 als
  Adressierungs-Konvention für Bearbeitungen.

**Sekundär (CAD/CAM-Hersteller-Dokumentation und akademisch):**

- Tekla / Trimble: „Timber NC – BTL". Knowledgebase,
  <https://support.tekla.com/article/timber-nc-btl> (abgerufen
  2026-05-14).
- Dietrich's: „Timber Coordinate Systems".
  <https://docs.dietrichs.com> (abgerufen 2026-05-14).
- cadwork Knowledgebase: IFC-Workflow.
  <https://kb.cadwork.ch/holzbau/manual/1064> sowie 1018 und 1081
  (abgerufen 2026-05-14).
- Hundegger Maschinenbau GmbH: BVN/BVX-Format-Dokumentation
  (Hersteller-internes Datenformat; öffentlich über zertifizierte
  Integratoren).
- Hoffmann, C. M.: *Geometric and Solid Modeling – An Introduction.*
  Morgan Kaufmann 1989, Kap. 3 „Boundary Representation".
- Mäntylä, M.: *An Introduction to Solid Modeling.* Computer Science
  Press 1988, Kap. 6 „Boundary Representation".

**Korpus (Negativ-Beleg, „Bauteilfläche" nicht als Lemma):**

- DIN 4074-1:2012-06, DIN EN 14081-1:2019-10, DIN EN 14080:2013-09,
  DIN EN 1995-1-1:2010-12, DIN 1052:2008-12, DIN 68800-2:2022-02,
  DIN EN 350:2016-12, DIN ISO 80000-2:2022-08, SIA 260:2013,
  SIA 265:2021, SIA 232/1:2020 — keine dieser Normen führt
  „Bauteilfläche" als geschlossenen Sammelbegriff.
- Mönck/Rug (2015), Natterer/Herzog/Volz (2003),
  Blass/Sandhaas (2016), Gerner (2007), Lignum HBT — verwenden
  spezialisierte Flächenbezeichnungen ohne Sammel-Oberbegriff.
- Holzbau Deutschland Merkblatt „Begriffe und Klassifizierungen
  für den Holzbau"; zimmerei-neuss.de Lexikon; baubeaver.de Glossar;
  lignocam.com BTLx-Übersicht (DE) — „Bauteilfläche" tritt in
  keinem dieser Glossare als Lemma auf.
- Recherche-Bericht: `docs/recherche/2026-05-14_hg_bauteilflaeche.md`.
