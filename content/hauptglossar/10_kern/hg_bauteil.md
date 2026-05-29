---
id: bauteil
benennung: Bauteil
synonyme: [Bauelement, Konstruktionselement]
abgelehnte_benennungen: [Bauglied, Element, Stück, "structural component", "building component", "member"]
oberbegriff: element
begriffstyp: generisch
voraussetzungen: [element, uuid, positionsnummer, produktkennzeichnung, querschnitt, werkstoff, faserrichtungs_modus, faserrichtung, haupttragrichtung, plattenlaengsrichtung, plattendicken_achse, lagenstruktur, polyeder, punkt, vektor, weltkoordinatensystem, toleranzen]
abgrenzung_zu: [element, verbindungsmittel, verbinder, verstaerkungselement, verbindung, bauteilgruppe, bausystem, bauwerk, konstruktionsdetail, werkstoff, bauteilachse]
status: entwurf
subglossar_pendant: notwendig
quellen_primär:
  - "SIA 265:2021 'Holzbau', Schweizerischer Ingenieur- und Architektenverein, Abschnitt 1 (Geltungsbereich) und Abschnitt 4 (Bemessung): „Bauteil“ als Bemessungsgegenstand vorausgesetzt."
  - "DIN EN 1995-1-1:2010-12 (Eurocode 5), Abschnitt 1.5 (Begriffe) und Abschnitt 5 (Tragwerksberechnung): „member“/„Bauteil“ als statisches Element."
  - "DIN 1052:2008-12, Abschnitt 3 (Begriffe), Bauteil als konstruktiv abgegrenzter Tragwerksbestandteil."
  - "DIN EN 14080:2013-09 'Holzbauwerke – Brettschichtholz und Balkenschichtholz', Abschnitt 3 (Begriffe)."
  - "DIN EN 14081-1:2019-10 'Holzbauwerke – Nach Festigkeit sortiertes Bauholz mit rechteckigem Querschnitt – Teil 1: Allgemeine Anforderungen'."
  - "SIA 260:2013 'Grundlagen der Projektierung von Tragwerken', Abschnitt 2.2 (Bauteil als Bemessungseinheit)."
quellen_sekundär:
  - "Lignum (Hrsg.): Holzbautabellen HBT, Lignum, Zürich, aktuelle Auflage, Kap. 'Bauteile und Querschnitte'."
  - "Mönck, W.; Rug, W.: Holzbau – Bemessung und Konstruktion. 16. Aufl., Beuth, Berlin 2015, Kap. 1 und 4."
  - "Blass, H. J.; Sandhaas, C.: Ingenieurholzbau – Grundlagen der Bemessung. KIT Scientific Publishing, Karlsruhe 2016, Kap. 1 und 5."
  - "Gerner, M.: Fachwerk – Instandsetzung, Sanierung, Neubau. DVA, 7. Aufl. 2007, Glossar."
  - "Natterer, J.; Herzog, T.; Volz, M.: Holzbau-Atlas. 4. Aufl., Birkhäuser, Basel 2003, Kap. 'Bauteile'."
quellenkonflikt: |
  Weder SIA 265:2021 noch DIN EN 1995-1-1 noch DIN 1052 enthalten eine
  geschlossene Begriffsdefinition für „Bauteil"; alle Normen verwenden
  den Begriff vorausgesetzt und beschränken sich auf seine Bemessungs-
  und Klassifikationseigenschaften (Querschnitt, Festigkeitsklasse,
  Tragfähigkeitsnachweis). Auch SIA 260 als Grundlagennorm setzt
  „Bauteil" voraus.

  In der Sekundärliteratur (Mönck/Rug, Blass/Sandhaas, Lignum HBT,
  Natterer/Herzog) wird „Bauteil" überwiegend als „abgegrenzter,
  konstruktiv eigenständiger Bestandteil eines Tragwerks mit eigener
  Geometrie, Material und Funktion" verwendet, ohne formale Definition.

  Eigene Festlegung in diesem Glossar (konsistent mit allen
  konsultierten Quellen):

  - Ein Bauteil ist ein generischer Sammelbegriff für alle stoff-
    lichen, geometrisch abgegrenzten und in der App geometrisch
    repräsentierten Bestandteile eines Bauwerks.
  - Ein Bauteil hat genau eine Lage in W (Weltkoordinatensystem),
    genau eine Geometrie (deren Repräsentation je nach
    Geometriedominanz wechselt), genau ein Material und genau eine
    eindeutige Identität.
  - Annotationen wie Vorzugsseite, Festigkeitsklasse und
    Bezeichnung sind optional. Die Faserrichtung dagegen ist eine
    Pflichtangabe, deren Form vom Werkstoff abhängt: bei
    `axiales_holz` ein Vektor (Pflicht); bei `mehrlagenholz` über
    `lagenstruktur` und `haupttragrichtung` (Pflicht); bei
    `gerichteter_plattenwerkstoff` über `plattenlaengsrichtung`
    (Pflicht); bei `isotroper_plattenwerkstoff` keine
    Faserrichtung in Plattenebene (semantisch nicht definiert,
    nur `plattendicken_achse`). Siehe Memory
    `project_faserrichtung_modi`.
  - Verbindungsmittel (Nägel, Schrauben, Bolzen, Stabdübel) zählen
    in dieser App nicht als Bauteile, sondern bilden eigene
    Element-Subklassen unter `element` — siehe `verbindungsmittel`,
    `verbinder`, `verstaerkungselement` (Memory
    `project_element_ontologie`).

  Spezialisierungen (Stab-, Flächen-, Volumenbauteil) und konkrete
  Bauteilrollen (Sparren, Pfette, Stütze, Strebe, Schalung,
  Plattenwerkstoff, Brettsperrholz-Element) folgen in eigenen
  Einträgen. Die Geometrie-Repräsentationen `polyeder` und
  `bauteilachse` werden in Folgeeinträgen formal definiert; im
  vorliegenden Eintrag werden sie als noch zu definierende
  Repräsentations-Bausteine namentlich vermerkt.

  Ein Aggregat-Oberbegriff `bauteil_aggregat` (für Dach, Wand, Decke
  als Komposition mehrerer Bauteile) wird als Schwesterbegriff
  geführt, nicht als Oberbegriff von `bauteil`. Bauteil und
  Bauteilaggregat liegen auf verschiedenen Ebenen der Komposition.

  Hinweis: `Element` erscheint sowohl als Oberbegriff
  (`oberbegriff: element` — die abstrakte App-Ontologie-Klasse, aus
  der Bauteil erbt) als auch als abgelehnte Benennung (im Sinne von
  „Bauteil" — Bauteil soll im engeren EC5-/SIA-Sinn benannt werden,
  nicht generisch als „Element"). Die beiden Verwendungen sind
  zwei unterschiedliche Begriffe und stehen nicht im Widerspruch.
---

## Prosa-Definition

Ein **Bauteil** ist ein abgegrenzter, identifizierbarer, materieller
Bestandteil eines Bauwerks mit eindeutiger Identität, einer
festgelegten Lage im Weltkoordinatensystem, einer festgelegten
Geometrie, einem festgelegten Werkstoff und einer konstruktiven oder
tragenden Funktion, der in der Domänen-Schicht als atomare Einheit
behandelt und durch Verbindungen oder Aggregation mit anderen
Bauteilen zu einem Tragwerk oder einem Bauteil-Aggregat zusammengefügt
wird.

## Mathematische Definition

Sei

- W das Weltkoordinatensystem (siehe `weltkoordinatensystem`),
- 𝒰 der UUID-Raum nach `uuid`,
- ℘ der Positionsnummer-Raum nach `positionsnummer`,
- ℘𝒦 der Produktkennzeichnungs-Raum nach `produktkennzeichnung`,
- 𝒲 die Menge der zulässigen Werkstoffe nach `werkstoff`, gegliedert
  nach Werkstoff-Subklasse:
  - `axiales_holz` (Vollholz, KVH, BSH, BSH-Lamellen, LVL/FSH …),
  - `mehrlagenholz` (Brettsperrholz/CLT/BSP, Sperrholz, Multiplex …),
  - `gerichteter_plattenwerkstoff` (OSB),
  - `isotroper_plattenwerkstoff` (Spanplatte P4–P7, MDF, HDF,
    Faserplatte),
  - `werkstoff_stahl` (typisch nicht für Holzbau-Bauteile, Ausnahme
    z. B. Stahltragglieder in Mischsystemen);
  - 𝒲 := axiales_holz ∪ mehrlagenholz ∪ gerichteter_plattenwerkstoff
    ∪ isotroper_plattenwerkstoff ∪ werkstoff_stahl,
- 𝒢 die Menge der zulässigen Geometrie-Repräsentationen, gegliedert
  nach Dominanzdimension:
  - 𝒢_stab : Achse + Querschnitt (1D-dominant; Repräsentation
    siehe `bauteilachse`, eigener Eintrag folgt),
  - 𝒢_flaeche : begrenzte Trägerfläche + Dicke (2D-dominant;
    Repräsentation über `ebene`, `polygon` und einen Dickenwert),
  - 𝒢_volumen : Polyeder (3D, allgemein; Repräsentation siehe
    `polyeder`, eigener Eintrag folgt),
  - 𝒢 := 𝒢_stab ∪ 𝒢_flaeche ∪ 𝒢_volumen.

Dann ist ein **Bauteil** ein Tupel

```
B := (uuid, positionsnummer?, produktkennzeichnung?,
      lage, geometrie, werkstoff, annotationen)
```

mit den von `element` ererbten Identifikatoren

- **uuid** ∈ 𝒰 (Pflicht, technischer Surrogatschlüssel, persistent;
  alle Foreign Keys anderer Domänenobjekte zeigen ausschließlich auf
  diese UUID, siehe Memory `project_bauteil_identifikation`),
- **positionsnummer** ∈ ℘ ∪ {⊥} (optional, mutable, humanlesbarer
  Geschäftsschlüssel für Werkpläne und Baustelle),
- **produktkennzeichnung** ∈ ℘𝒦 ∪ {⊥} (optional, normierte Material-/
  Chargen-Identifikation nach DIN 4074, EN 14081, EN 14080, CE),

und den bauteil-spezifischen Pflicht- und Optionalfeldern

- **lage** ∈ SE(3): die Starrkörpertransformation, die das lokale
  Bauteil-Koordinatensystem nach W überführt
  (Rotation R ∈ SO(3) und Translation t ∈ ℝ³),
- **geometrie** ∈ 𝒢: die geometrische Repräsentation im lokalen
  Bauteil-Koordinatensystem, klassifiziert nach Dominanzdimension,
- **werkstoff** ∈ 𝒲: der Werkstoff, aus dem das Bauteil besteht
  (eine der Subklassen `axiales_holz`, `mehrlagenholz`,
  `gerichteter_plattenwerkstoff`, `isotroper_plattenwerkstoff` —
  oder ausnahmsweise `werkstoff_stahl`),
- **annotationen** ∈ 𝒜: ein Tupel optionaler und werkstoffklassen-
  spezifischer Annotationen (siehe unten).

Die Punktmenge des Bauteils im Weltkoordinatensystem ist

```
G_W(B) := { lage(p) | p ∈ G_lokal(geometrie) } ⊂ ℝ³,
```

wobei G_lokal(geometrie) die durch die jeweilige Geometrie-
Repräsentation erzeugte Punktmenge im lokalen System ist
(Stabachse fortgesetzt zu einem Volumen über den Querschnitt;
Trägerfläche fortgesetzt zu einem Volumen über die Dicke;
Polyeder selbst).

Die Annotationen 𝒜 sind ein Tupel, **dessen Pflichtfeld-Profil von
der Werkstoff-Subklasse bestimmt wird** (Memory
`project_faserrichtung_modi`; siehe `faserrichtungs_modus`):

| Werkstoff-Subklasse              | Modus         | Pflicht-Annotationen                                  |
|----------------------------------|---------------|-------------------------------------------------------|
| `axiales_holz`                   | HART          | `faserrichtung` ∈ S² (Default-Konvention: lokale x-Achse) |
| `mehrlagenholz`                  | STRUKTURIERT  | `lagenstruktur` + `haupttragrichtung` ∈ S²           |
| `gerichteter_plattenwerkstoff`   | SCHWACH       | `plattenlaengsrichtung` ∈ S² (Default: lokale Plattenlängskante) + `plattendicken_achse` |
| `isotroper_plattenwerkstoff`     | KEINE         | nur `plattendicken_achse` (in Plattenebene undefiniert) |

In jedem Modus zusätzlich optional:

- **vorzugsseite?** ∈ {Oberseite, Unterseite, beidseitig markiert}
  ∪ {⊥}: optionale Seitenorientierung — `vorzugsseite` ist immer
  optional, weil nicht alle Plattenwerkstoffe eine Sichtseite haben
  (Memory `project_plattenwerkstoffe`); ⊥ für seitenisotrope Bauteile.
- **festigkeitsklasse?**: Werkstoff-Festigkeitsklasse nach
  EN 14081-1, EN 14080 etc. (z. B. C24, GL24h, BSP-Q3) — siehe
  `festigkeitsklasse` — oder ⊥.
- **bezeichnung?**: dem Bauteil zugewiesener Name oder ⊥.

Damit ist die Faserrichtung bzw. ihre werkstoffklassen-spezifische
Entsprechung **keine** generisch-optionale Annotation des Bauteils,
sondern ihr Pflichtcharakter ergibt sich konditional aus dem
Werkstoff. Ein Vollholz-Bauteil ohne `faserrichtung` ist
unzulässig (Validierungsfehler, nicht Warnung); ein Spanplatten-
Bauteil mit gesetztem `faserrichtung`-Vektor in der Plattenebene ist
ebenfalls unzulässig.

## Wohldefiniertheit

- **Existenz**: Für jedes konkrete Holzbauwerk lässt sich jedes
  einzelne Bauteil als Tupel (uuid, positionsnummer?,
  produktkennzeichnung?, lage, geometrie, werkstoff, annotationen)
  erfassen. Mindestkonfiguration: uuid ≠ ∅, lage = id_SE(3)
  (Identität), geometrie ∈ 𝒢_stab, werkstoff ∈ axiales_holz,
  faserrichtung = lokale x-Achse, alle übrigen Optionalfelder = ⊥.
- **Eindeutigkeit der Identität**: Innerhalb eines Modells gilt
  ∀ B₁, B₂ : (B₁ ≠ B₂) ⇒ (B₁.uuid ≠ B₂.uuid). Die UUID ist
  konstruktionsseitig zu vergeben (UUID v7 nach RFC 9562) und
  persistent über den gesamten Lebenszyklus. Die optionale
  Positionsnummer ist mutable und unterliegt keiner Foreign-Key-
  Verpflichtung.
- **Unabhängigkeit von der Wahl des lokalen Bauteil-Koordinaten-
  systems**: Für jede zulässige Wahl des lokalen Systems liefert die
  zugehörige Lage SE(3)-Transformation dieselbe Punktmenge G_W(B).
  Die Wahl des lokalen Systems ist Modellierungskonvention (siehe
  Implementierungshinweis); semantisch invariant.
- **Konsistenz Werkstoff ↔ Annotationen** (werkstoffklassen-
  spezifische Pflichtfelder, siehe `faserrichtungs_modus`):
  - Bei `werkstoff` ∈ axiales_holz: `faserrichtung` ∈ S² ist Pflicht
    (Norm-Invariante geerbt von `einheitsvektor`); ihre Bedeutung
    ist die idealisierte lokale Längsachse des Faserverlaufs (siehe
    `faserrichtung`).
  - Bei `werkstoff` ∈ mehrlagenholz: `lagenstruktur` (Liste von
    `lage`-Objekten ≥ 3 mit Symmetrie-Invariante) und
    `haupttragrichtung` ∈ S² sind Pflicht; eine einzelne globale
    `faserrichtung` ist unzulässig.
  - Bei `werkstoff` ∈ gerichteter_plattenwerkstoff:
    `plattenlaengsrichtung` ∈ S² (Default: lokale Plattenlängskante)
    und `plattendicken_achse` sind Pflicht.
  - Bei `werkstoff` ∈ isotroper_plattenwerkstoff: nur
    `plattendicken_achse` ist Pflicht; in der Plattenebene ist keine
    Faserrichtung definiert.
  Wenn `vorzugsseite` gesetzt ist, muss die zugrunde liegende
  Geometrie eine ausgewiesene „Außenrichtung" haben (Flächenbauteil
  mit positiver Dickenseite; Stab- und Volumenbauteile haben in der
  Regel keine Vorzugsseite).
- **Nicht-Zirkularität**: Die Definition verwendet ausschließlich
  `element` als Oberbegriff, die Identifikator-Begriffe `uuid`,
  `positionsnummer`, `produktkennzeichnung`, die Werkstoff-Hierarchie
  (`werkstoff` und Subklassen), die Faserrichtungs-Modi-Hilfsbegriffe
  (`faserrichtungs_modus`, `faserrichtung`, `haupttragrichtung`,
  `lagenstruktur`, `plattenlaengsrichtung`, `plattendicken_achse`),
  die Primitive `punkt`, `vektor`, `weltkoordinatensystem`,
  `toleranzen` sowie die noch zu definierenden Repräsentations-
  Bausteine `bauteilachse` und `polyeder`. Sie verweist nicht auf
  Spezialisierungen von Bauteil (Sparren, Pfette etc.) und nicht auf
  Bauteil-Aggregate.
- **Optionalität**: Nur die Optionalfelder `positionsnummer`,
  `produktkennzeichnung`, `vorzugsseite`, `festigkeitsklasse`,
  `bezeichnung` sind algebraisch optional (Wert ∪ {⊥}); ⊥ ist
  zulässig. Die werkstoffklassen-spezifischen Faserrichtungs-Felder
  sind **nicht** optional, sondern bedingt pflichtig.

## Erläuterung (nicht normativ)

Der Bauteilbegriff dieses Glossars ist bewusst **generisch und
gegliedert** statt monolithisch:

- **Gegliedert nach Geometriedominanz**: Stab- (Sparren, Pfette,
  Stütze, Strebe, Kehlbalken), Flächen- (Schalung, Plattenwerkstoff,
  Brettsperrholz-Element) und Volumenbauteile (Massivholzelemente,
  zusammengesetzte BSP-Wandelemente). Diese drei Klassen verwenden
  unterschiedliche Geometrie-Repräsentationen, sind aber alle
  Bauteile.
- **Gegliedert nach Bauteilrolle**: Spezialisierungen wie `sparren`,
  `pfette`, `stuetze` erben die Bauteil-Eigenschaften und ergänzen
  rollenspezifische Constraints (z. B. „eine Pfette liegt
  näherungsweise waagerecht", „eine Stütze steht näherungsweise
  senkrecht").

**Faserrichtung folgt aus dem Werkstoff, nicht aus dem Bauteil.**
Welcher Richtungsbegriff am Bauteil pflichtig ist (`faserrichtung`,
`haupttragrichtung`, `plattenlaengsrichtung`, oder keiner), wird
durch die Werkstoff-Subklasse bestimmt (siehe
`faserrichtungs_modus`, Memory `project_faserrichtung_modi`):

- `axiales_holz` (Vollholz, KVH, BSH, LVL): einzelner
  `faserrichtung`-Vektor — Pflicht.
- `mehrlagenholz` (BSP/CLT, Sperrholz): keine einzelne globale
  Faserrichtung; statt dessen `lagenstruktur` plus
  `haupttragrichtung`.
- `gerichteter_plattenwerkstoff` (OSB): `plattenlaengsrichtung`
  als schwache Vorzugsrichtung der Decklagen-Strands.
- `isotroper_plattenwerkstoff` (Spanplatte, MDF, HDF): keine
  Faserrichtung in der Plattenebene; nur `plattendicken_achse`.

**Vorzugsseite bleibt optional**, weil viele Plattenwerkstoffe (auch
solche mit Faserrichtung wie OSB) keine ausgezeichnete Sichtseite
haben (Memory `project_plattenwerkstoffe`). Die Optionalität der
Vorzugsseite ist eine eigenständige Modellierungs-Festlegung, nicht
gekoppelt an die Faserrichtungs-Modi.

**Verbindungsmittel, Verbinder und Verstärkungselemente sind keine
Bauteile**, sondern eigene Element-Subklassen unter dem gemeinsamen
Oberbegriff `element` (Memory `project_element_ontologie`):

- `verbindungsmittel` (Nagel, Schraube, Bolzen, Stabdübel, Klammer,
  Holzdübel, Klebung): das einzelne kraftübertragende Stück;
  Bemessung nach EC5 Kap. 8 (Anschlussbemessung).
- `verbinder` (Balkenschuh, Winkel, Knotenblech, Schlitzblech,
  Sherpa): vermittelndes Element zwischen Bauteilen, das selbst
  durch Verbindungsmittel befestigt ist.
- `verstaerkungselement`: physisch eine Vollgewindeschraube, aber
  in funktionaler Verstärkungsrolle (Querzug-, Querdruck-,
  Schubverstärkung) mit eigener axialer Bemessung nach EC5:2022 /
  ETA. **Funktion bestimmt die Klasse, nicht das Material**:
  dieselbe Vollgewindeschraube wird im klassischen Abscher-Anschluss
  als `verbindungsmittel`, als ETA-konforme Querzugverstärkung als
  `verstaerkungselement` instanziiert — niemals als „Bauteil-
  ähnlich".

**Verbindungsdetails** (Zapfen, Versatz, Blattung, Schwalbenschwanz)
sind geometrische Modifikationen von Bauteilen, kein eigener
Bauteiltyp. **Verbindungen** im aggregativen Sinn (Verbindung als
Knotenpunkt mit Bauteilen + Verbindungsmitteln + ggf. Verbindern +
Verstärkungen) sind eine eigene Aggregat-Klasse `verbindung`, kein
Bauteil.

**Bauteil-Aggregate** wie Dach, Wand, Decke sind Kompositionen
**aus** Bauteilen plus konstruktiven Schichten und stehen eine
Stufe über dem Bauteilbegriff. Sie haben einen eigenen
Aggregat-Oberbegriff (`bauteil_aggregat`, eigener Eintrag folgt).

## Beziehungen

- **Oberbegriff**: `element` (abstrakter Oberbegriff der App-
  Ontologie, trägt UUID, Positionsnummer, Produktkennzeichnung,
  Geometrie, Werkstoff, Lebenszyklus). Bauteil ist eine von vier
  konkreten Element-Subklassen (neben `verbindungsmittel`,
  `verbinder`, `verstaerkungselement`). Ein Aggregat-Oberbegriff
  `bauteil_aggregat` existiert als Schwesterbegriff für
  Kompositionen aus Bauteilen (Dach, Wand, Decke).
- **Spezialisierungen nach Geometriedominanz** (eigene Einträge
  folgen):
  - **Stabbauteil** (`stabbauteil`): 1D-dominant, repräsentiert
    durch Achse + Querschnitt + Material. Untertypen:
    - **Sparren** (`sparren`), inkl. Spezialisierungen
      **Gratsparren** (`gratsparren`), **Kehlsparren** (`kehlsparren`)
    - **Pfette** (`pfette`), inkl. Spezialisierungen
      **Fußpfette** (`fusspfette`), **Mittelpfette** (`mittelpfette`),
      **Firstpfette** (`firstpfette`)
    - **Latte** (`latte`)
    - **Konterlatte** (`konterlatte`)
    - **Stütze** (`stuetze`)
    - **Strebe** (`strebe`)
    - **Kehlbalken** (`kehlbalken`)
    - **Riegel** (`riegel`)
    - **Schwelle** (`schwelle`)
    - **Rähm** (`raehm`)
    - **Pfosten** (Folgearbeit)
  - **Flächenbauteil** (`flaechenbauteil`): 2D-dominant,
    repräsentiert durch begrenzte Trägerfläche + Dicke + Material.
    Untertypen:
    - **Schalung** (`schalung`)
    - **Plattenwerkstoff** (`plattenwerkstoff`)
    - **Brettsperrholz-Element** (`brettsperrholz_element`)
  - **Volumenbauteil** (`volumenbauteil`): 3D-allgemein,
    repräsentiert durch Polyeder + Material. Untertypen:
    Massivholzelemente, zusammengesetzte BSP-Bauteile
    (Folgearbeit).
- **Annotationen** (eigene Einträge; werkstoffabhängig pflichtig
  oder optional, siehe `faserrichtungs_modus`):
  - **Faserrichtung** (`faserrichtung`, Pflicht bei
    `axiales_holz`): einzelne lokale Längsachse des
    Holzfaserverlaufs.
  - **Lagenstruktur** (`lagenstruktur`, Pflicht bei
    `mehrlagenholz`): Liste von `lage`-Objekten ≥ 3 mit
    Symmetrie-Invariante.
  - **Haupttragrichtung** (`haupttragrichtung`, Pflicht bei
    `mehrlagenholz`): Vektor in Plattenebene mit höherer
    Decklagen-Steifigkeit.
  - **Plattenlängsrichtung** (`plattenlaengsrichtung`, Pflicht bei
    `gerichteter_plattenwerkstoff`): schwache Vorzugsrichtung der
    Decklagen-Strands.
  - **Plattendickenachse** (`plattendicken_achse`, Pflicht bei
    allen Plattenwerkstoffen): rechtwinklig zur Plattenebene.
  - **Vorzugsseite** (`vorzugsseite`, optional, eigener Eintrag
    folgt): Ober-/Unterseiten-Markierung bei seitenanisotropen
    Flächenbauteilen.
  - **Festigkeitsklasse** (`festigkeitsklasse`, optional):
    Werkstoff-Klassifikation nach EN 14081-1, EN 14080.
  - **Bauteilachse** (`bauteilachse`, eigener Eintrag folgt):
    geometrische Hauptachse stabförmiger Bauteile.
- **Bestandteile (partitiv) eines Bauteils** (rein geometrisch):
  - **Geometrie** (Achse, Trägerfläche oder Polyeder)
  - **Lage** in W (SE(3)-Transformation)
- **Abgrenzung**:
  - **Verbindungsmittel** (Nagel, Schraube, Bolzen, Stabdübel,
    Klammer, Holzdübel; eigene Kategorie, eigener Eintrag folgt):
    sind keine Bauteile dieser App, sondern Verbindungselemente
    zwischen Bauteilen. Geometrie und Funktion sind beschreibbar,
    aber die Bauteilrolle (Tragglied im Sinne der Bemessung) wird
    ihnen nicht zugewiesen.
  - **Bauteil-Aggregat** (`bauteil_aggregat`, eigener Eintrag
    folgt): Komposition mehrerer Bauteile zu einer übergeordneten
    Einheit (Dach, Wand, Decke). Ein Aggregat ist kein Bauteil,
    sondern eine Stufe darüber.
  - **Bauwerk** (Gebäude als Ganzes): die übergeordnete Einheit,
    aus Bauteilaggregaten und Bauteilen zusammengesetzt; Bauteil
    ist Bestandteil eines Bauwerks.
  - **Konstruktionsdetail** (Anschlussdetail, Knoten): kann
    mehrere Bauteile mitsamt Verbindungsmitteln umfassen und ist
    eine modellhafte Repräsentation der lokalen Verbindungs-
    geometrie, kein eigenes Bauteil. Eigener Eintrag folgt.
  - **Werkstoff** (`werkstoff`): die Stoffeigenschaft eines Bauteils,
    nicht das Bauteil selbst. Eigene Begriffshierarchie mit den
    Subklassen `axiales_holz`, `mehrlagenholz`,
    `gerichteter_plattenwerkstoff`, `isotroper_plattenwerkstoff`
    sowie `werkstoff_stahl`. Konkrete Werkstoffe (Vollholz, BSH,
    BSP, LVL, OSB, Spanplatte, MDF, Sperrholz) ordnen sich diesen
    Subklassen zu; eigene Folge-Einträge.
  - **Verbindungsmittel** (`verbindungsmittel`), **Verbinder**
    (`verbinder`), **Verstärkungselement** (`verstaerkungselement`):
    Geschwister-Element-Subklassen, keine Bauteile (siehe oben).
  - **Verbindung** (`verbindung`): Aggregat-Klasse über Bauteilen +
    Verbindungsmitteln + Verbindern + Verstärkungen an einem
    Knotenpunkt; keine Element-Subklasse, sondern eigene
    Aggregat-Hierarchie.

## Implementierungshinweis

Datentyp (Domänen-Schicht, Kotlin, Schicht `domain.bauteil`):

```kotlin
package domain.bauteil

import domain.bauteil.Element
import domain.bauteil.Geometrie
import domain.bauteil.LokalePlatzierung
import domain.holzbau.Einheitsvektor
import domain.holzbau.Faserrichtung
import domain.holzbau.Lagenstruktur
import domain.holzbau.Positionsnummer
import domain.holzbau.Produktkennzeichnung
import domain.holzbau.Werkstoff
import java.util.UUID

/** Geometrie-Repräsentation, klassifiziert nach Dominanzdimension. */
sealed interface Bauteilgeometrie : Geometrie {
    /** 1D-dominant: Achse + Querschnitt. Achse-Eintrag folgt. */
    data class Stab(val achse: Bauteilachse, val querschnitt: Querschnitt) : Bauteilgeometrie
    /** 2D-dominant: Trägerfläche + Dicke. */
    data class Flaeche(val traeger: Trägerflaeche, val dicke: Double) : Bauteilgeometrie
    /** 3D-allgemein: Polyeder. Eintrag folgt. */
    data class Volumen(val polyeder: Polyeder) : Bauteilgeometrie
}

/** Optionale Seitenorientierung; null für seitenisotrope Bauteile. */
enum class Seitenorientierung { OBERSEITE_MARKIERT, UNTERSEITE_MARKIERT, BEIDSEITIG_UNTERSCHIEDLICH }

/**
 * Werkstoffklassen-spezifisches Annotations-Tupel. Der Subtyp wird
 * durch die Werkstoff-Subklasse bestimmt (harte Invariante, siehe
 * Memory `project_faserrichtung_modi`).
 */
sealed class BauteilAnnotationen {
    /** axiales_holz: Vollholz, KVH, BSH, LVL. */
    data class Axial(val faserrichtung: Faserrichtung) : BauteilAnnotationen()
    /** mehrlagenholz: BSP/CLT, Sperrholz, Multiplex. */
    data class Mehrlagig(
        val lagenstruktur: Lagenstruktur,
        val haupttragrichtung: Einheitsvektor
    ) : BauteilAnnotationen()
    /** gerichteter_plattenwerkstoff: OSB. */
    data class Gerichtete_Platte(
        val plattenlaengsrichtung: Einheitsvektor
    ) : BauteilAnnotationen()
    /** isotroper_plattenwerkstoff: Spanplatte, MDF, HDF, Faserplatte. */
    data class Isotrope_Platte(
        val plattendicken_achse: Einheitsvektor
    ) : BauteilAnnotationen()
}

/**
 * Generisches Bauteil. Konkrete Bauteilrollen (Sparren, Pfette,
 * Stütze, Strebe, Schalung, Plattenwerkstoff, BSP-Element) sind
 * Spezialisierungen mit zusätzlichen Constraints.
 *
 * Glossar: hg_bauteil.md
 *
 * Pflichtfelder (ererbt aus Element bzw. werkstoffklassen-spezifisch):
 * uuid, werkstoff, geometrie, lokalePlatzierung, annotationen.
 * Optional: positionsnummer, produktkennzeichnung, bezeichnung.
 *
 * Falls die Element-Basis als `sealed class` modelliert ist, statt
 * `: Element` durch `: Element()` ersetzen; das Schema bleibt gleich.
 */
data class Bauteil(
    override val uuid: UUID,                                  // Element, Pflicht (RFC 9562 v7)
    override val positionsnummer: Positionsnummer? = null,    // Element, mutable, optional
    override val produktkennzeichnung: Produktkennzeichnung? = null,  // Element, optional
    override val werkstoff: Werkstoff,                        // Element, Pflicht
    override val geometrie: Geometrie,                        // Element
    override val lokalePlatzierung: LokalePlatzierung,        // Element
    val annotationen: BauteilAnnotationen,                    // werkstoffklassen-spezifisch
    val bezeichnung: String? = null,
) : Element {
    companion object {
        /**
         * Konstruktor-Helper: erzeugt ein Bauteil mit frisch
         * generierter UUID v7. Die uuid7-Generierung liegt in der
         * Persistenzschicht; hier inline als Platzhalter angedeutet.
         */
        fun neu(
            werkstoff: Werkstoff,
            geometrie: Geometrie,
            lokalePlatzierung: LokalePlatzierung,
            annotationen: BauteilAnnotationen,
            positionsnummer: Positionsnummer? = null,
            produktkennzeichnung: Produktkennzeichnung? = null,
            bezeichnung: String? = null,
        ): Bauteil = Bauteil(
            uuid = uuid7Generieren(),  // siehe Persistenzschicht
            positionsnummer = positionsnummer,
            produktkennzeichnung = produktkennzeichnung,
            werkstoff = werkstoff,
            geometrie = geometrie,
            lokalePlatzierung = lokalePlatzierung,
            annotationen = annotationen,
            bezeichnung = bezeichnung,
        )
    }
}
```

- **Einheit**: Längen in mm (Double); Winkel intern in Radiant; Lage
  als SE(3)-Element (Rotation + Translation, siehe `lage`/Folgearbeit).
- **Identität**: `uuid` ist Pflicht und persistent (RFC 9562 v7);
  Vergabe beim Konstruieren des Bauteils, nicht aus Geometrie
  abgeleitet. Verbindungen, Bemessungen und Anschlussdetails
  referenzieren Bauteile ausschließlich über `uuid`, nicht über
  Geometrie-Vergleich. Foreign-Key-Regel siehe Memory
  `project_bauteil_identifikation`.
- **Pflicht- und Optionalfelder (normativ)**:
  - `annotationen: BauteilAnnotationen` — Pflicht; der Subtyp ist
    durch die Werkstoff-Subklasse bestimmt (harte Invariante,
    siehe unten). Niemals weglassen, niemals Defaults der
    werkstoffklassen-fremden Modi setzen.
  - `positionsnummer: Positionsnummer?` — `null` zulässig
    (mutable, humanlesbarer Geschäftsschlüssel).
  - `produktkennzeichnung: Produktkennzeichnung?` — `null` zulässig
    während des Entwurfsstadiums (z. B. vor Materialbestellung).
  - `bezeichnung: String?` — `null` zulässig; Anzeige fällt dann auf
    `uuid`, `positionsnummer` oder Bauteilrolle zurück.
- **Invarianten** (im `init`-Block bzw. in Fabrikfunktionen prüfen,
  bei Verletzung `Resultat.Fehler` bzw. `Entartet`-Variante; niemals
  Exception werfen):
  1. Norm-Invariante aller in `annotationen` enthaltenen
     Einheitsvektoren (`faserrichtung`, `haupttragrichtung`,
     `plattenlaengsrichtung`, `plattendicken_achse`):
     | ‖v_hat‖² − 1 | ≤ Toleranzen.NORM_EPS (geerbt von
     `einheitsvektor`).
  2. Geometrie-spezifische Nicht-Degeneriertheit:
     - Stab: Achsenlänge > Toleranzen.LAENGE_EPS,
       Querschnitt-Fläche > Toleranzen.FLAECHE_EPS.
     - Fläche: Trägerflächeninhalt > Toleranzen.FLAECHE_EPS,
       Dicke > Toleranzen.LAENGE_EPS.
     - Volumen: Polyeder-Volumen > Toleranzen.VOLUMEN_EPS.
  3. Werkstoff ↔ Annotationen: Diese Konsistenz ist eine **harte**
     Invariante (Validierungsfehler bei Verstoß): das
     Annotations-Subtyp muss zum Werkstoff passen
     (`axiales_holz` ↔ `Axial`,
     `mehrlagenholz` ↔ `Mehrlagig`,
     `gerichteter_plattenwerkstoff` ↔ `Gerichtete_Platte`,
     `isotroper_plattenwerkstoff` ↔ `Isotrope_Platte`).
     Bei Verstoß `Resultat.Fehler` bzw.
     `Entartet.WerkstoffAnnotationenInkonsistent` zurückgeben.
     Plausibilitätsprüfungen gegen die Belastung (z. B. Sparren
     rechtwinklig zur Faser belastet) sind weiche Invarianten in
     der Bemessungs-Schicht.
- **Edge Cases**:
  - **Bauteil ohne festgelegte Lage**: nicht erlaubt; Lage ist
    Pflichtfeld (mindestens Identität in SE(3)).
  - **Bauteil mit isotropem Plattenwerkstoff** (Spanplatte, MDF):
    `annotationen = BauteilAnnotationen.Isotrope_Platte(...)`
    mit ausschließlich `plattendicken_achse`; in der Plattenebene
    keine Faserrichtung (siehe Memory `project_faserrichtung_modi`).
  - **Bauteil mit beidseitig unterschiedlicher Sichtseite**
    (z. B. einseitig beschichtete Spanplatte): die Vorzugsseite
    wird, falls modelliert, separat geführt (eigener Eintrag
    `vorzugsseite` folgt); Geometrieseite oben/unten ist durch
    Trägerfläche-Normale festgelegt.
  - **Verbindungsmittel-Modellierung**: NICHT als Bauteil
    instanziieren; eigene Klasse `Verbindungsmittel`
    (Folgearbeit).
  - **Aggregate**: NICHT als Bauteil instanziieren; eigene Klasse
    `BauteilAggregat` (Folgearbeit).
- **Abgeleitete Eigenschaften** (als Funktionen, keine Felder):
  - `geometrieInWelt(): GeometrieInW` — Geometrie unter Anwendung
    der Lage transformiert nach W.
  - `boundingBox(): AABB` — achsenparalleler Hüllquader in W.
  - `volumen(): Double` (mm³) — abhängig von Geometrie-Variante.
  - `faserwinkelZu(r: Einheitsvektor): Double?` — liefert Winkel
    zwischen Faserrichtung (bzw. werkstoffklassen-spezifischer
    Hauptrichtung im Annotations-Subtyp) und Referenzrichtung r;
    `null` bei `BauteilAnnotationen.Isotrope_Platte`, weil in der
    Plattenebene keine Richtung definiert ist.
- **Bezeichner-Konvention** (CLAUDE.md): Domänen-Klasse heißt
  `Bauteil` (deutsch, Glossarbegriff); Spezialisierungen heißen
  `Sparren`, `Pfette` etc. (deutsch). Technische Hilfstypen heißen
  englisch (`UUID`, `Lage`, `AABB`).

## Quellen

**Primär (normativ):**

- SIA 265:2021, „Holzbau", Schweizerischer Ingenieur- und
  Architektenverein, Zürich.
- SIA 260:2013, „Grundlagen der Projektierung von Tragwerken".
- DIN EN 1995-1-1:2010-12, „Eurocode 5: Bemessung und Konstruktion
  von Holzbauten – Teil 1-1: Allgemeines – Allgemeine Regeln und
  Regeln für den Hochbau".
- DIN 1052:2008-12, „Entwurf, Berechnung und Bemessung von
  Holzbauwerken – Allgemeine Bemessungsregeln und Bemessungsregeln
  für den Hochbau".
- DIN EN 14080:2013-09, „Holzbauwerke – Brettschichtholz und
  Balkenschichtholz – Anforderungen".
- DIN EN 14081-1:2019-10, „Holzbauwerke – Nach Festigkeit
  sortiertes Bauholz mit rechteckigem Querschnitt – Teil 1:
  Allgemeine Anforderungen".

**Sekundär:**

- Lignum (Hrsg.): *Holzbautabellen HBT.* Lignum, Zürich, aktuelle
  Auflage.
- Mönck, W.; Rug, W.: *Holzbau – Bemessung und Konstruktion.*
  16. Auflage, Beuth, Berlin 2015.
- Blass, H. J.; Sandhaas, C.: *Ingenieurholzbau – Grundlagen der
  Bemessung.* KIT Scientific Publishing, Karlsruhe 2016.
- Gerner, M.: *Fachwerk – Instandsetzung, Sanierung, Neubau.* DVA,
  7. Auflage 2007.
- Natterer, J.; Herzog, T.; Volz, M.: *Holzbau-Atlas.* 4. Auflage,
  Birkhäuser, Basel 2003.

**Korpus (nicht autoritativ):**

- Holzbau Deutschland, Merkblatt „Begriffe und Klassifizierungen
  für den Holzbau" (abgerufen 2026-05-08).
- Wikipedia, Lemma „Bauteil" (abgerufen 2026-05-08).
