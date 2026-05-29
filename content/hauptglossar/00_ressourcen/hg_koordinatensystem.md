---
id: koordinatensystem
benennung: Koordinatensystem
synonyme: ["Referenzsystem"]
abgelehnte_benennungen:
  - Bezugssystem
  - Bezugsrahmen
  - "coordinate system"
  - "coordinate reference system"
  - CRS
  - "reference frame"
  - frame
abgrenzung_zu: [weltkoordinatensystem, lokales_koordinatensystem, bezugssystem, punkt, vektor, achse]
oberbegriff: null
begriffstyp: hilfsbegriff
voraussetzungen: [punkt, vektor]
status: entwurf
subglossar_pendant: optional
quellen_primär:
  - "ISO 19111:2019, 'Geographic information — Referencing by coordinates', Abschnitt 3.1.13 (Definition 'coordinate system': 'set of mathematical rules for specifying how coordinates are to be assigned to points') und Abschnitt 7 (Coordinate systems). Schärfste verfügbare Definitions-Quelle für den Oberbegriff. [einsicht: snippet, via OGC 18-005r4]"
  - "DIN ISO 80000-2:2022-08, 'Größen und Einheiten – Teil 2: Mathematik', Abschnitt 2 (Geometrie und Vektoren); ISO 80000-2:2019, Symbole für kartesische, polare, zylindrische und sphärische Koordinatensysteme (autoritativ für Symbolwahl, kein geschlossener Oberbegriff). [einsicht: vorschau-pdf]"
  - "DIN EN ISO 80000-3:2020-12, 'Größen und Einheiten – Teil 3: Raum und Zeit', Abschnitt 3 (Raum), Koordinaten als Tripel reeller Zahlen mit zugeordneter Längeneinheit."
quellen_sekundär:
  - "Bronstein, I. N. et al.: Taschenbuch der Mathematik. Kap. 3.5 'Analytische Geometrie des Raumes' und 'spezielle Koordinatensysteme/Transformationen'. Mindest-Bestandteile: Ursprung O; geordnete Familie ausgezeichneter Geraden (Achsen); Koordinaten-Zuordnungs-Regel."
  - "Berger, M.: Geometry I. Springer 1987, §2 'Affine spaces', §2.6 'Affine frames': Koordinatensystem als Frame (O, B) über einem affinen Raum; in der affinen Geometrie sind Frame und Koordinatensystem synonym."
  - "OGC 18-005r4 (2019), 'Geographic information — Well-known text representation of coordinate reference systems', Abschnitt zur Trennung Coordinate System ↔ Coordinate Reference System (CRS = CS + Datum)."
  - "ISO 10303-42:2022, 'Industrial automation systems and integration — Product data representation and exchange — Part 42': Entität 'axis2_placement_3d' als operative Realisierung eines lokalen kartesischen 3D-Koordinatensystems durch Ursprung + Z-Richtung + X-Approximation."
  - "ISO 16739-1:2024 (IFC 4.3), 'Industry Foundation Classes': 'IfcAxis2Placement3D' und 'IfcGeometricRepresentationContext.WorldCoordinateSystem' — operative Subtyp-Konvention (rechtshändig, kartesisch)."
  - "swisstopo (Bundesamt für Landestopografie): 'Bezugssystem — Basis für Koordinaten' und 'Bezugsrahmen — das Bezugssystem wird physisch fassbar'. Geodätische Vokabel-Pyramide Bezugssystem → Bezugsrahmen → Koordinatensystem."
  - "EN ISO 5459:2011 / 5459:2024, 'Geometrische Produktspezifikation (GPS) – Bezüge und Bezugssysteme'. Maschinenbau-Lesart: 'Bezugssystem' = Bauteil-Aufspann-Konfiguration, 'Bezugskoordinatensystem' (5459:2024) als neuer Begriff getrennt vom Mess-Koordinatensystem."
quellenkonflikt: |
  Es gibt keine Holzbau-Norm (DIN 1052, DIN EN 1995-1-1, SIA 265,
  SIA 232/1, Holzbau-Deutschland-Merkblätter), die ein
  Koordinatensystem als Oberbegriff festlegt. Im Holzbau-Korpus
  (SIA 265, DIN 1052, EN 1995-1-1, Cadwork, BTLx) wird der Begriff
  durchgängig verwendet, aber nicht definiert; „Bezugssystem" tritt
  als technischer Begriff nicht auf. Die einschlägigen Quellen sind
  geoinformatisch (ISO 19111, swisstopo), produktdatentechnisch
  (ISO 10303, ISO 16739/IFC), maschinenbau-tolerierungstechnisch
  (ISO 5459) und allgemein-mathematisch (DIN ISO 80000-2, Bronstein,
  affine Geometrie).

  Konflikt 1 — Abgrenzung Koordinatensystem ↔ Bezugssystem
  (vier inkompatible Lesarten):

  | Lager                 | „Bezugssystem"                       | „Koordinatensystem"         |
  |-----------------------|--------------------------------------|-----------------------------|
  | Geodäsie (ISO 19111,  | physische Erd-Verankerung            | mathematische Code-Schicht  |
  |   swisstopo)          | (Datum); CRS = CS + Datum            | (UTM, Gauss-Krüger, X-Y-Z)  |
  | Physik                | Bewegungszustand des Beobachters     | mathematische Sprache       |
  |   (de.wikipedia       | (Inertialsystem, beschleunigtes      | zur Beschreibung des        |
  |   'Bezugssystem')     | System)                              | Bezugssystems               |
  | Maschinenbau          | geordnete Angabe von Bezügen         | Mess-Code; ab 5459:2024     |
  |   (ISO 5459)          | (Datums-Merkmalen) im Toleranzrahmen | „Bezugskoordinatensystem"   |
  | affine Geometrie      | Synonym zu Frame =                   | (siehe links)               |
  |   (Berger, Encyclopedia| Koordinatensystem                   |                             |
  |   of Math)            |                                      |                             |

  Geodäsie hat Bezugssystem ⊃ Koordinatensystem (Bezugssystem ist
  das grössere Konzept); affine Geometrie hat sie als Synonyme;
  Physik und ISO 5459 trennen sie auf einer dritten Achse
  (physikalisch/operativ vs. mathematisch).

  App-Festlegung: „Koordinatensystem" ist die Hauptbenennung. Die
  Bedeutung folgt der Linie ISO 19111 / affine Geometrie:
  mathematische Regel zur Zuordnung von Koordinaten zu Punkten,
  ohne physische Erd- oder Aufspann-Verankerung. „Bezugssystem"
  wird wegen der oben dokumentierten Mehrdeutigkeit **nicht** als
  Synonym geführt und steht in `abgelehnte_benennungen:`. Die
  app-interne Erd-Verankerung wird durch das
  `weltkoordinatensystem` getragen (Ursprung in Bauwerksnähe, Ost/
  Nord/Zenit), die Bauteil-Aufspannung durch das
  `lokales_koordinatensystem`.

  Konflikt 2 — Stufe-a vs. Stufe-b der Definition:
  Eine engere Definition (Stufe a: rechtshändig, kartesisch,
  3-dimensional, in mm) deckt die beiden bestehenden Sub-Einträge
  knapp ab, schliesst aber künftige Folge-Einträge `lv95`, `wgs84`
  (geo-projiziert bzw. ellipsoidisch, in Metern) als
  Koordinatensysteme aus. App-Festlegung: Stufe b (allgemeines
  Tupel (O, B, n, η) über einem affinen Raum, ohne kartesische,
  rechtshändige oder einheitliche Festlegung am Oberbegriff). Die
  App-internen Einschränkungen kartesisch + rechtshändig + mm +
  Radiant liegen bei den Sub-Einträgen `weltkoordinatensystem` und
  `lokales_koordinatensystem` und werden dort als Spezialisierung
  begründet.

  Konflikt 3 — Subtyp-Achsen:
  Aus den Quellen ergibt sich eine zweiachsige Klassifikation:
  Struktur (affin/kartesisch/krummlinig — Bronstein, Wikipedia,
  Encyclopedia of Math) und Bezug (welt/lokal/geo/maschinen — IFC,
  swisstopo, ISO 5459). Beide Achsen sind orthogonal. Die App-
  Sub-Einträge belegen die kombinierten Zellen „kartesisch + welt"
  und „kartesisch + lokal"; künftige Einträge belegen „kartesisch
  projiziert + geo" (LV95) und „ellipsoidisch + geo" (WGS84). Der
  Oberbegriff trägt keine eigene Subtyp-Hierarchie, sondern erlaubt
  die Spezialisierung über die jeweiligen Sub-Einträge.

  Diese Festlegungen sind konfliktfrei mit allen konsultierten
  Quellen, sobald sie als App-interne Konventionen (nicht als
  Aussagen über die Quellen selbst) verstanden werden.
---

## Prosa-Definition

Ein **Koordinatensystem** ist eine mathematische Festlegung über
einem affinen Raum, bestehend aus einem ausgezeichneten Ursprung,
einer geordneten Familie von Basis-Elementen, einer Dimension und
einer bijektiven Zuordnungs-Regel, die jedem Punkt des Raumes
eindeutig ein Tupel reeller Zahlen — seine Koordinaten — zuweist.

## Mathematische Definition

Sei

- 𝔸 ein reeller affiner Raum endlicher Dimension n ∈ ℕ_{>0} mit
  zugehörigem Vektorraum V,
- O ∈ 𝔸 ein **Ursprung**,
- B = (b_1, …, b_n) eine geordnete **Basis** von V (linear
  unabhängige n-elementige Familie aus V, die V erzeugt),
- η : 𝔸 → ℝⁿ die **Koordinatenabbildung**
  ```
  η(p) = (x_1, …, x_n)  ⇔  p = O + x_1·b_1 + … + x_n·b_n.
  ```

Dann ist ein **Koordinatensystem** auf 𝔸 das Tupel

```
K := (O, B, n, η).
```

η heisst die durch (O, B) erzeugte Koordinatenabbildung.

### Optionale Spezialisierungen

Die folgenden Eigenschaften sind **keine** Bestandteile der
Definition, sondern beweisbare Zusatzmerkmale, die ein konkretes
Koordinatensystem tragen kann oder nicht:

- **Orthogonalität**: für i ≠ j gilt ⟨b_i, b_j⟩ = 0
  (paarweise rechtwinklige Basis-Vektoren).
- **Orthonormalität**: zusätzlich ‖b_i‖ = 1 für alle i.
  Ein orthonormales System heisst **kartesisch**.
- **Rechtshändigkeit** (nur für n = 3 sinnvoll):
  b_1 × b_2 = b_3, gleichwertig det(b_1 | b_2 | b_3) = +1.
- **Längeneinheit**: eine Festlegung, in welcher Einheit die
  Koordinaten zu interpretieren sind (z. B. mm, m).
- **Winkelkonvention**: eine Festlegung der Drehsinn-Richtung für
  Winkel um ausgezeichnete Basis-Vektoren (z. B. gegen den
  Uhrzeigersinn um b_3, in Radiant).

Welche dieser Spezialisierungen ein konkretes Koordinatensystem
trägt, wird in seinem eigenen Glossareintrag normativ festgelegt
(siehe `hg_weltkoordinatensystem.md`, `hg_lokales_koordinatensystem.md`).

## Wohldefiniertheit

- **Existenz**: Zu jedem endlich-dimensionalen reellen affinen Raum
  𝔸 mit zugehörigem Vektorraum V existiert mindestens ein
  Koordinatensystem — wähle ein beliebiges O ∈ 𝔸 und eine
  beliebige Basis B von V. Die Existenz einer Basis folgt aus dem
  Basisexistenzsatz der linearen Algebra für endlich-dimensionale
  Vektorräume.
- **Eindeutigkeit von η bei gegebenem (O, B)**: Die
  Koordinatenabbildung η ist durch (O, B) eindeutig bestimmt, weil
  jeder Punkt p ∈ 𝔸 sich gemäss dem affinen Raum-Axiom eindeutig
  als p = O + v mit v ∈ V darstellen lässt und v in der Basis B
  eindeutig in Komponenten zerfällt.
- **Bijektivität von η**: η ist bijektiv. Surjektivität folgt aus
  der Konstruktion η⁻¹(x_1, …, x_n) := O + x_1·b_1 + … + x_n·b_n.
  Injektivität folgt aus der eindeutigen Basisdarstellung in V.
- **Unabhängigkeit der Operationen von der Wahl des Repräsentanten**:
  Bei festgelegtem (O, B) ist η eine Bijektion, und alle
  abgeleiteten Operationen (Differenz, Norm sofern V ein
  Skalarprodukt trägt, lineare Kombination) sind unter η
  wohldefiniert. Die Wohldefiniertheit von Operationen, die ein
  Skalarprodukt voraussetzen (Winkel, Orthogonalität), benötigt
  zusätzlich die Festlegung eines Skalarprodukts auf V; sie ist
  dann trivial.
- **Nicht-Zirkularität**: Die Definition stützt sich auf den
  affinen Raum (in den Voraussetzungen `punkt` als Element von
  𝔸 etabliert) und den Vektorraum V (in den Voraussetzungen
  `vektor` als Element von V etabliert) sowie auf die linear-
  algebraischen Begriffe „Basis" und „Koordinatenabbildung", die
  rein durch die affine und Vektorraum-Struktur gegeben sind.
  Das Koordinatensystem selbst kommt in seiner Definition nicht
  vor.

## Erläuterung (nicht normativ)

Ein Koordinatensystem ist die mathematische Brücke zwischen
**geometrischen Objekten** (Punkten im Raum, gerichteten
Verschiebungen) und **Zahlentupeln**, mit denen sich rechnen lässt.
Ohne ein gewähltes Koordinatensystem hat ein Punkt keine
„Koordinaten"; er ist nur ein Element eines affinen Raumes.

Im Holzbau-Kontext der App treten zwei konkrete Koordinatensysteme
auf, die beide eine kartesische, rechtshändige, 3-dimensionale
Spezialisierung des Oberbegriffs sind:

- das **Weltkoordinatensystem** als eindeutiges globales
  Bezugs-System mit fester Ost/Nord/Zenit-Zuordnung;
- ein **lokales Koordinatensystem** pro Bauteil oder
  Konstruktionsteil, das durch eine starre Transformation auf das
  Weltkoordinatensystem bezogen ist.

Künftige Sub-Einträge können weitere Spezialisierungen tragen:
**LV95** (kartesisch projiziert, geo-verankert, in Metern) und
**WGS84** (ellipsoidisch, geo-verankert). Beide passen unter den
hier definierten Oberbegriff, ohne dass dessen Definition geändert
werden muss.

### Bezugssystem — bewusste Abgrenzung

Der deutschsprachige Begriff „Bezugssystem" ist über die
Fachgebiete mehrdeutig (siehe `quellenkonflikt:` Konflikt 1):
geodätisch bezeichnet er die physische Erd-Verankerung
(Bezugssystem ⊃ Koordinatensystem); physikalisch den
Bewegungszustand des Beobachters; im Maschinenbau (ISO 5459) die
Bauteil-Aufspann-Konfiguration; in der affinen Geometrie ist er
synonym zu „Koordinatensystem". Die App verwendet ihn deshalb
**nicht** als Hauptbenennung und nicht als Synonym; sie führt
stattdessen „Koordinatensystem" als mathematischen Begriff und
trägt die geodätische bzw. operative Verankerung über die
Spezialisierungen `weltkoordinatensystem` (Ost/Nord/Zenit) und
`lokales_koordinatensystem` (Bauteil-Platzierung).

## Beziehungen

- **Oberbegriff**: keiner. „Koordinatensystem" ist im Glossar selbst
  der Wurzel-Begriff für die Familie aller Bezugs-Festlegungen über
  einem affinen Raum.
- **Spezialisierungen (im Glossar verankert)**:
  - **Weltkoordinatensystem** (`hg_weltkoordinatensystem.md`):
    eindeutige rechtshändige kartesische 3-dimensionale
    Spezialisierung mit fester geographischer Einbettung
    (e_x = Ost, e_y = Nord, e_z = Zenit), Längen in mm, Winkel um
    e_z in Radiant ab +x gegen den Uhrzeigersinn.
  - **Lokales Koordinatensystem**
    (`hg_lokales_koordinatensystem.md`): bauteileigene
    rechtshändige kartesische 3-dimensionale Spezialisierung, die
    durch eine starre Transformation T ∈ SE(3) auf das
    Weltkoordinatensystem bezogen ist.
- **Spezialisierungen (Folgearbeit, Forward-Verweise)**:
  - **LV95** (`lv95.md`, geplant): kartesisch projizierte
    2-dimensionale Spezialisierung des Schweizer
    Landeskoordinatensystems, Längen in Metern.
  - **WGS84** (`wgs84.md`, geplant): ellipsoidische
    Spezialisierung; Koordinaten sind geographische Länge,
    geographische Breite und ellipsoidische Höhe.
- **Abgrenzung**:
  - **Bezugssystem** (Korpus-Begriff ohne eigenen Eintrag):
    deutschsprachiger Begriff mit drei inkompatiblen Lesarten
    (geodätisch, physikalisch, maschinenbau-tolerierungstechnisch);
    in der App nicht als Synonym verwendet, weil die
    Mehrdeutigkeit nicht durch eine einzelne Quelle aufgelöst
    werden kann (siehe `quellenkonflikt:` Konflikt 1).
  - **Weltkoordinatensystem** / **Lokales Koordinatensystem**:
    konkrete kartesische Spezialisierungen des Oberbegriffs in
    der App-Domäne; sie tragen die App-internen Festlegungen
    (rechtshändig, kartesisch, mm, Radiant), die der Oberbegriff
    bewusst offen lässt.
  - **Punkt** (`hg_punkt.md`): Element des affinen Raumes 𝔸; ein
    Koordinatensystem ordnet einem Punkt sein Koordinatentupel zu,
    ist aber selbst kein Punkt.
  - **Vektor** (`hg_vektor.md`): Element des zugehörigen
    Vektorraumes V; die Basis B eines Koordinatensystems besteht
    aus Vektoren, das Koordinatensystem selbst ist aber kein
    Vektor.
  - **Achse** (`hg_achse.md`): ausgezeichnete Gerade durch den
    Ursprung mit ausgezeichneter Richtung. Eine Achse eines
    Koordinatensystems wird durch (O, b_i) festgelegt; ein
    Koordinatensystem hat n Achsen, ist aber selbst keine Achse.

## Implementierungshinweis

Der Oberbegriff `koordinatensystem` ist als `hilfsbegriff`
gekennzeichnet (HG-Konvention §3, Tabelle Code-Pendant-Pflicht);
er **muss kein** eigenes Code-Pendant in der Domänen-Schicht
tragen. In der aktuellen Implementierung existieren ausschliesslich
Pendants für die kartesischen 3-dimensionalen Spezialisierungen:

- `zimmermann.domain.koordinaten.Weltkoordinatensystem` — Singleton
  (Kotlin-`object`) für die globale Festlegung.
- `zimmermann.domain.koordinaten.LokalePlatzierung` und
  `zimmermann.domain.koordinaten.Rotation` — `data class`-Familie
  für bauteileigene Lokalsysteme als starre Transformation
  T ∈ SE(3) relativ zum Weltsystem.

Eine gemeinsame abstrakte Basisklasse oder ein `sealed interface`
über beiden Spezialisierungen ist **nicht vorgesehen**: die
strukturellen Unterschiede zwischen Singleton (Welt) und
data-class-Familie (Lokal) sind so gross, dass eine gemeinsame
Schnittstelle keine sinnvolle Abstraktion trägt; die
fachsprachliche Familienzugehörigkeit reicht aus.

**Trigger-basierte Folgearbeit:**

- **`lv95`-Eintrag** anlegen, sobald die App eine
  Georeferenzierung gegen den Schweizer Bezugsrahmen LV95
  vornimmt. Das Code-Pendant ist eine reine Importrand-Operation
  (Welt-Ursprungs-Anker mit (E, N, H) in Metern), nicht eine
  eigene Domänen-Klasse.
- **`wgs84`-Eintrag** analog für GNSS-Importschnittstellen.
- **`bezugssystem`-Eintrag** **nicht** geplant: der Begriff ist im
  Holzbau-Korpus nicht etabliert und in den angrenzenden Korpora
  mehrdeutig (siehe `quellenkonflikt:` Konflikt 1). Sollte die
  App eine geodätische Schicht (CRS = CS + Datum) brauchen,
  würde sie über `lv95` und `wgs84` als konkrete CRS-Pendants
  realisiert, nicht über einen abstrakten `bezugssystem`-Eintrag.

## Quellen

**Primär (normativ):**

- ISO 19111:2019, „Geographic information — Referencing by
  coordinates", Abschnitt 3.1.13 und Abschnitt 7.
- DIN ISO 80000-2:2022-08, „Größen und Einheiten – Teil 2:
  Mathematik".
- ISO 80000-2:2019, Symbole und Bezeichnungen für Koordinaten-
  systeme.
- DIN EN ISO 80000-3:2020-12, „Größen und Einheiten – Teil 3:
  Raum und Zeit".

**Sekundär:**

- Bronstein, I. N. et al.: *Taschenbuch der Mathematik.* Kap. 3.5
  „Analytische Geometrie des Raumes".
- Berger, M.: *Geometry I.* Springer 1987, §2 „Affine spaces".
- Encyclopedia of Mathematics: „Affine coordinate system".
- OGC 18-005r4 (2019), „Geographic information — Well-known text
  representation of coordinate reference systems".
- ISO 10303-42:2022, „Industrial automation systems and
  integration — Product data representation and exchange —
  Part 42", Entität `axis2_placement_3d`.
- ISO 16739-1:2024 (IFC 4.3), „Industry Foundation Classes",
  `IfcAxis2Placement3D`, `IfcGeometricRepresentationContext`.
- swisstopo: „Bezugssystem — Basis für Koordinaten",
  „Bezugsrahmen — das Bezugssystem wird physisch fassbar".
- EN ISO 5459:2011 / 5459:2024, „Geometrische Produktspezifikation
  (GPS) – Bezüge und Bezugssysteme".

**Nur in der Abgrenzung referenziert (nicht als Definitionsquelle):**

- de.wikipedia.org, Lemma „Bezugssystem" — Physik-Lesart
  (Bewegungszustand des Beobachters), abgerufen 2026-05-14.

**Korpus (nicht autoritativ):**

- Wikipedia (de/en), Lemmata „Koordinatensystem", „Kartesisches
  Koordinatensystem", „Affine Koordinaten", „Krummlinige
  Koordinaten", „Affine space" (abgerufen 2026-05-14).
- Recherche-Bericht
  `docs/recherche/2026-05-14_hg_koordinatensystem.md`.
