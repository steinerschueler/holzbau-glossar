---
id: schicht
benennung: Schicht
synonyme: [Bauteilschicht, Funktionsschicht, Funktionsebene]
abgelehnte_benennungen: [Lage, Ebene, "layer", "building layer"]
oberbegriff: null
begriffstyp: generisch
voraussetzungen: [werkstoff, toleranzen]
abgrenzung_zu: [bauteil, dachaufbau, dachhaut, lage, lagenstruktur, ebene, eindeckung, unterdach, dachabdichtung, dampfbremse, waermedaemmung]
status: entwurf
theorie_pflichtig: required
quellen_primär:
  - "DIN 4108-3:2018-10 'Wärmeschutz und Energie-Einsparung in Gebäuden – Teil 3: Klimabedingter Feuchteschutz', Abschnitt 3 (Begriffe): „Bauteilschicht“ als Schicht eines Bauteils; diffusionsdichte Bauteilschicht über Sd ≥ 1500 m."
  - "DIN 4108-7:2011-01 'Wärmeschutz und Energie-Einsparung in Gebäuden – Teil 7: Luftdichtheit', Abschnitt 3 (Begriffe): „Luftdichtheitsschicht“ als Schicht, die die Luftströmung durch Bauteile hindurch verhindert."
  - "DIN 68800-2:2022-02 'Holzschutz – Teil 2: Vorbeugende bauliche Maßnahmen im Hochbau', Anhang B (feuchtevariable Schichten)."
  - "SIA 232/1:2011 (mit Korrigenda C1:2013) 'Geneigte Dächer', Schweizerischer Ingenieur- und Architektenverein, Abschnitt 2 (Aufbau geneigter Dächer; Schichtenfolge Eindeckung / Konter-/Traglatte / Unterdach / Schalung / Wärmedämmung / Dampfbremse)."
  - "SIA 271:2021 'Abdichtungen von Hochbauten', Abschnitt 1 (flächige Abdichtungen mit den dazugehörigen Schichten: Trenn-, Schutz-, Nutzschicht)."
  - "SIA 180:2014 'Wärmeschutz, Feuchteschutz und Raumklima', Abschnitt 'Luftdichte Ebene' und Sd-Wert-Klassifikation."
  - "DIN 18531-1:2017-07 'Abdichtung von Dächern – Teil 1', Abschnitt 5 (Schichtenfolge: Trennlage, Wärmedämmung, Abdichtung, Schutz-, Nutzschicht)."
  - "ISO 16739-1:2024 / IFC 4.3 'Industry Foundation Classes', Entity IfcMaterialLayer: A single and identifiable part of an element which is constructed of a number of layers (one or more). Each IfcMaterialLayer has a constant thickness and is located relative to the referencing IfcMaterialLayerSet along the material layer set base (MlsBase). Attribute: Material, LayerThickness, IsVentilated, Name, Description, Category, Priority. [direkt]"
  - "ISO 16739-1:2024 / IFC 4.3, Entity IfcMaterialLayerSet: geordnete Liste von IfcMaterialLayer ohne Lücken und Überlappungen, Gesamtdicke = Summe der Einzeldicken, ausgezeichnete Basislinie MlsBase. [direkt]"
  - "ISO 16739-1:2024 / IFC 4.3, Entity IfcMaterialLayerSetUsage: vorkommnisspezifische Verwendung eines IfcMaterialLayerSet mit LayerSetDirection, DirectionSense, OffsetFromReferenceLine. [direkt]"
quellen_sekundär:
  - "Mönck, W.; Rug, W.: Holzbau – Bemessung und Konstruktion. 16. Aufl., Beuth Verlag 2015, Kap. 'Dachaufbau' / 'Wandaufbau'."
  - "Natterer, J.; Herzog, T.; Volz, M.: Holzbau-Atlas. 4. Aufl., Birkhäuser, Basel 2003, Kap. 'Schichtaufbau der Gebäudehülle'."
  - "Lignum (Hrsg.): Lignatec 'Geneigte Dächer in Holzbauweise', Lignum, Zürich, aktuelle Auflage, Kap. 'Schichtaufbau'."
  - "SIGA (Hrsg.): Technischer Leitfaden 'Witterungsschutz und Luftdichtheit für den Holzbau', aktuelle Auflage."
  - "ZVDH-Fachregel für Dachdeckungen, Stand 2024-04 (Schichtbegriffe für geneigte Dächer)."
  - "baunormenlexikon.de zu DIN 4108-3 (Bauteilschicht) und DIN 4108-7 (Luftdichtheitsschicht)."
  - "Recherchebericht docs/recherche/2026-05-14_hg_schicht.md."
quellenkonflikt: |
  **(1) Norm-Definitions-Lücke.** Keine der konsultierten DACH-Normen
  (SIA 232/1, SIA 271, SIA 180, DIN 4108-3, DIN 4108-7, DIN 18531-1,
  DIN 68800-2) liefert eine geschlossene, abstrakte Definition von
  „Schicht". Der Begriff wird wie „Bauteil" durchgängig vorausgesetzt
  und nur über Funktionsklassen, Materialien und konstruktive
  Anforderungen näher bestimmt. Die einzige fast-Definition steht in
  DIN 4108-3 als **„Bauteilschicht“** — komponenten-relativ als
  „Schicht eines Bauteils", nicht abstrakt. DIN 4108-7 führt die
  Funktions-Schicht „Luftdichtheitsschicht“ funktional definiert
  („Schicht, die die Luftströmung … verhindert").

  Diese Situation ist strukturell parallel zu `hg_bauteil.md`: auch
  dort ist der Wurzelbegriff norm-undefiniert und wird in diesem
  Glossar konstitutiv festgelegt.

  **(2) IFC 4.3 als verbindliches Pendant.** IFC liefert mit
  `IfcMaterialLayer` + `IfcMaterialLayerSet` + `IfcMaterialLayerSetUsage`
  eine vollständige, ISO-standardisierte Begriffstrias mit klaren
  Attributen (`LayerThickness`, `Material`, `Category`, `Priority`,
  `IsVentilated`) und Komposistionsinvarianten (geordnete Liste, keine
  Lücken oder Überlappungen, ausgezeichnete Basislinie). Die App-
  Definition wird **auf diese Trias ausgerichtet**; `IfcMaterialLayer`
  ist Mapping-Ziel für `schicht`, `IfcMaterialLayerSet` für die
  Schichtfolge eines Träger-Aggregats (z. B. `dachaufbau`),
  `IfcMaterialLayerSetUsage` für deren Verwendung am konkreten
  Trägerbauteil.

  **(3) Drei nicht-normativ verankerte Subtypen.** Drei der dreizehn
  Funktions-Subtypen tragen keine eigene Norm-Definition:
  `Luftdichtheitsebene` (DIN 4108-7 als Funktionsschicht definiert —
  Tier hoch, aufgenommen), `Installationsebene` (Holzbau-Praxis,
  nicht normativ — Tier mittel, aufgenommen als App-Konvention) und
  `Innenverkleidung` (Praxis „Bekleidung"/„Innenbeplankung" ohne
  Wurzel-Norm — Tier mittel, aufgenommen als App-Konvention,
  IFC `Category = "Finish"`). Die App-Konvention ist im jeweiligen
  Subtyp-Eintrag bzw. in der Erläuterung dieses Eintrags markiert.

  **(4) Abgrenzung „Schicht" vs. „Lage" vs. „Ebene".** Im DACH-Holzbau-
  Korpus werden alle drei Begriffe als Funktionsschicht-Bezeichnung
  verwendet („Dampfbremsschicht", „Luftdichtheitsebene", „luftdichte
  Ebene", „Tragschicht", „Lage Mineralwolle"). Im Glossar ist
  **„Lage"** bereits an die Lamelle einer `lagenstruktur` (BSP/CLT)
  vergeben und **„Ebene"** an das geometrische Primitiv `hg_ebene.md`.
  Kollisionsfrei ist daher nur **„Schicht"** als Hauptbenennung.
  Komposita-Formen wie „Luftdichtheitsebene" und „Installationsebene"
  bleiben in den Subtyp-Benennungen erhalten, weil sie berufssprachlich
  fest verankert sind und nicht den Wurzelbegriff `ebene` re-
  definieren.

  **(5) Komposition statt Vererbung für Funktionsschicht-Begriffe.**
  Die HG-Einträge `hg_eindeckung.md`, `hg_unterdach.md`,
  `hg_dampfbremse.md`, `hg_waermedaemmung.md`, `hg_dachabdichtung.md`
  bleiben als eigenständige Top-Level-Einträge bestehen und sind
  jeweils mit `oberbegriff: schicht` an die Funktionsschicht angebunden
  (fachliche Spezialisierungs-Linie). Die App-Strategie für die
  **Code-Realisierung** ist jedoch **Komposition statt Vererbung**:
  jeder Funktionsschicht-Begriff ist eine eigene sealed-Klasse (mit
  ihrer materialspezifischen oder beanspruchungs-spezifischen
  Sub-Hierarchie), die eine `schicht: Schicht`-Komponente hält. `Schicht`
  selbst ist eine schlanke `data class` mit Funktionsklassen-Enum-Feld
  (`SchichtFunktion`) und ohne sealed-Subtypen für die Funktionsschicht-
  Begriffe. Diese Asymmetrie zwischen `oberbegriff:` (fachliche
  Spezialisierung) und Code-Realisierung (Komposition) ist nach
  HG-Konvention §3 zulässig — sie ist strukturparallel zur
  `tragwerk`/`bausystem`-Asymmetrie und zur `bauteilkoerper`/`polyeder`-
  Asymmetrie. Die material- bzw. klassen-spezifische Hierarchie bleibt
  in den jeweiligen HG-Einträgen verankert; `schicht` ist der generische
  Wertetyp mit konstanter Dicke, einem Material und einer
  Funktionsklasse, der als Komponente in die Funktionsschicht-
  Aggregate eingebettet wird.

  **(6) `oberbegriff: null`.** Ein konzeptioneller Oberbegriff
  `bauteil_aggregat` für die geordneten Bestandteile eines
  Schichtenpakets existiert im Glossar nicht; eine Spezialisierung
  von `bauteil` ist nicht zutreffend, weil die Schicht gerade nicht
  die identitäts- und geometrie-konstituierenden Merkmale eines
  Bauteils trägt (siehe Beziehungen). Bis zur etwaigen Einführung
  eines Oberbegriffs bleibt das Feld `null`, analog zu `dachaufbau`,
  `eindeckung`, `unterdach`. Der einmalige Re-Parent-Schritt für
  `eindeckung` und `unterdach` auf `schicht` ist als kleiner
  R-Schritt nach Anlage dieses Eintrags vorgesehen (siehe
  Folgearbeiten).
---

## Prosa-Definition

Eine **Schicht** ist ein funktional klassifizierter, materieller
Bestandteil eines geordneten Bauteil-Aufbaus, der über einer
geerbten Trägerfläche mit konstanter Dicke aus einem einzelnen
Material aufgetragen ist und in der App keine eigene Identität
oder Lage im Weltkoordinatensystem trägt, sondern aus Trägerbauteil
und Position in der Schichtfolge abgeleitet wird.

## Mathematische Definition

Sei

- M ∈ 𝓦 ein Material-Identifikator aus der Werkstoff-Menge gemäß
  `werkstoff`,
- d ∈ ℝ mit d > `Toleranzen.LAENGE_EPS` eine konstante Dicke (in mm),
- 𝓕 die diskrete Funktionsklassen-Menge
  ```
  𝓕 := { Dampfbremse, Wärmedämmung, Schalung, Unterdach,
         Konterlattung, Traglattung, Eindeckung, Abdichtung,
         Trennlage, Luftdichtheitsebene, Installationsebene,
         Innenverkleidung, Sonstige }
  ```
  und f ∈ 𝓕 die Funktionsklasse,
- π ∈ 𝓟 ein optionaler funktionsspezifischer Parameter-Tupel-Wert
  aus der zur Funktion f gehörigen Parameter-Menge 𝓟_f (Beispiel:
  für f = Dampfbremse ist π = (s_d) mit s_d ≥ 0 in m; für
  f = Wärmedämmung ist π = (λ) mit λ > 0 in W/(m·K); für viele
  Funktionsklassen ist 𝓟_f = ∅).

Dann ist eine **Schicht** das Tupel

```
S := (M, d, f, π)
```

mit den Konsistenzbedingungen

1. **Materialbindung**: M ist ein gültiger Werkstoff-Identifikator
   gemäß `werkstoff`.
2. **Positive Dicke**: d > `Toleranzen.LAENGE_EPS`.
3. **Funktionsklasse**: f ∈ 𝓕.
4. **Parameter-Wohlgeformtheit**: π ∈ 𝓟_f (funktionsspezifische
   Wertebereiche).
5. **Material-Funktions-Verträglichkeit**: das Paar (M, f) ist im
   bauphysikalischen Sinne zulässig (z. B. f = Dampfbremse erfordert
   M aus einer dampfdiffusionshemmenden Materialklasse). Diese
   Bedingung ist im allgemeinen Eintrag weich gefasst und wird in
   den Funktions-Subtyp-Einträgen geschärft.

Die **Position** einer Schicht im Weltkoordinatensystem ist nicht
Bestandteil von S. Sie folgt aus Trägerbauteil und Index in der
Schichtfolge des Träger-Aggregats — siehe Wohldefiniertheit.

Die **abgeleitete Geometrie** einer Schicht ist
```
G(S, F, i, A) := { p + t · n_hat(p) : p ∈ F, t ∈ [t_i, t_i + d] }
```
mit

- F dem von einem Träger-Aggregat A geerbten Trägerbereich
  (z. B. F = ⋃ F(P_i) bei `dachaufbau`),
- n_hat(p) der nach außen gerichteten Trägerflächen-Normalen an p,
- i ∈ {1, …, k} dem Index der Schicht in der Folge 𝒮 = (S₁, …, S_k)
  des Trägers,
- t_i := Σ_{j=1..i-1} d_j dem Basis-Offset der Schicht.

## Wohldefiniertheit

- **Existenz**: Für jeden gültigen Werkstoff M, jede positive Dicke
  d und jede Funktionsklasse f mit verträglichem Parameter-Tupel π
  ist S wohldefiniert.

- **Eindeutigkeit der Geometrie ohne eigene Felder**: Die abgeleitete
  Geometrie G(S, F, i, A) hängt nur von S, dem Trägerbereich F (aus A),
  dem Index i (aus A) und der Außennormalen-Konvention von A ab.
  Wechselt die Schicht das Träger-Aggregat oder den Index, ändert
  sich die Geometrie deterministisch mit; die Schicht selbst trägt
  keinen Geometrie-Zustand. Die Konvention „1 = innen, k = außen"
  wird vom Träger-Aggregat (z. B. `hg_dachaufbau.md` Bedingung 2)
  festgelegt und stimmt mit der IFC-Konvention `MlsBase` →
  letzte Schicht überein.

- **Eindeutigkeit der Identität**: Eine Schicht besitzt **keine
  UUID**. Sie ist ein Wert-Tupel (data class) und wird im Modell
  ausschließlich über ihre Position in der Schichtfolge eines
  identifizierten Träger-Aggregats referenziert. Diese Wahl folgt
  IFC: `IfcMaterialLayer` ist `IfcMaterialDefinition`, kein
  `IfcRoot`, hat also keine `GlobalId`. Sollen einzelne Platten,
  Bretter oder Bahnen, aus denen sich eine Schicht physisch
  zusammensetzt, mit eigener Identität geführt werden, geschieht
  das auf der **Bauteil-Ebene** parallel zur Schicht-Ebene, nicht
  innerhalb der Schicht (siehe Beziehungen).

- **Konsistenz zu Funktionsschicht-Aggregaten**: Die eigenständigen
  Begriffe `eindeckung`, `unterdach`, `dampfbremse`, `waermedaemmung`,
  `dachabdichtung` sind im Code keine Subtypen von `Schicht`, sondern
  eigene sealed-Klassen mit einer `schicht: Schicht`-Komponente
  (Komposition, siehe Quellenkonflikt 5). Die Konsistenz-Bedingungen
  jener Einträge (Eindeckungsklasse, Beanspruchungs-Klasse, sd-Wert-
  Funktion, λ-Wertebereich, Druckwasserhöhe) bleiben dort verankert.
  An der Schnittstelle zwischen Funktionsschicht-Aggregat und
  enthaltener Schicht gilt die Pflicht-Bedingung
  `schicht.funktion == SchichtFunktion.<XXX>` für die jeweilige
  Funktionsklasse — als Konstruktor-Invariante des
  Funktionsschicht-Aggregats, nicht der Schicht selbst.

- **Nicht-Zirkularität**: Die Definition verwendet die bereits
  angelegten Begriffe `werkstoff` und `toleranzen` sowie die
  geometrischen Primitive Punkt, Vektor, Strecke. Sie verweist auf
  einzelne Funktions-Subtypen erläuternd, nicht definitorisch — die
  Funktionsklasse f ist ein diskreter Aufzählungswert, kein
  Funktionsaufruf in einen anderen Eintrag.

- **Konservativität gegenüber `dachaufbau`**: Der bereits angelegte
  Eintrag `hg_dachaufbau.md` verwendet eine inline-`data class Schicht`
  (Z. 226 ff.) mit denselben drei Pflichtfeldern (Material, Dicke,
  Funktion). Dieser Eintrag verallgemeinert die Inline-Klasse zum
  generischen Schicht-Wertetyp mit optionalem
  `SchichtParameter`-Feld; die `data class Schicht` in
  `hg_dachaufbau.md` bleibt in der ersten Migrationsstufe
  unverändert und wird in einer Folgeetappe gegen die hier
  festgelegte Form abgeglichen (siehe Folgearbeiten). Die
  Funktionsschicht-Aggregate (`eindeckung`, `unterdach`,
  `dampfbremse`, `waermedaemmung`, `dachabdichtung`) leben
  unabhängig daneben und halten eine `Schicht`-Komponente.

## Erläuterung (nicht normativ)

Eine Schicht beschreibt **was wozu in welcher Dicke** an einer
Stelle des Aufbaus liegt — Material, Funktion, Dicke — ohne
festzulegen, **wo absolut im Raum** sie liegt. Letzteres folgt
erst, sobald die Schicht in eine Schichtfolge eingeordnet ist und
diese Folge ihrerseits an einem konkreten Trägerbauteil verwendet
wird. Diese Trennung entspricht der IFC-Architektur:
`IfcMaterialLayer` beschreibt das **Was**, `IfcMaterialLayerSet`
die **Reihenfolge**, `IfcMaterialLayerSetUsage` das **Wo am
konkreten Bauteil**.

### Funktionsklassen

Die App führt eine `SchichtFunktion`-Enum über alle dreizehn
Funktionsklassen. Sieben der dreizehn Funktionen sind in DACH-Normen
explizit verankert; die zehn aktuell in `SchichtFunktion`-Enum
geführten Werte (`hg_dachaufbau.md` Z. 232 ff.) werden um drei
ergänzt. Fünf der Funktionsklassen besitzen ein eigenständiges
Funktionsschicht-Aggregat (HG-Eintrag mit `oberbegriff: schicht`),
das eine `Schicht`-Instanz mit passender Funktionsklasse als
Komposition hält — siehe Spalte „Funktionsschicht-Aggregat".

| Funktionsklasse | Norm-Verankerung | Funktionsschicht-Aggregat |
|---|---|---|
| `DAMPFBREMSE` | DIN 4108-3, SIA 180 | `Dampfbremse` (`hg_dampfbremse.md`) — eigene sealed-Hierarchie, hält `schicht: Schicht`. |
| `WAERMEDAEMMUNG` | DIN 4108-3, SIA 180 | `Waermedaemmung` (`hg_waermedaemmung.md`) — eigene sealed-Hierarchie, hält `schicht: Schicht`. |
| `SCHALUNG` | SIA 232/1, ZVDH | (kein Aggregat; nur Schicht-Wert mit dieser Funktion) |
| `UNTERDACH` | SIA 232/1, DIN EN 13859-1, ZVDH | `Unterdach` (`hg_unterdach.md`) — eigene sealed-Hierarchie, hält `schicht: Schicht`. |
| `KONTERLATTUNG` | SIA 232/1, ZVDH | (kein eigenständiges Funktionsschicht-Aggregat; Sammelbegriff für eine Schicht aus `hg_konterlatte.md`-Bauteilen.) |
| `TRAGLATTUNG` | SIA 232/1, ZVDH | (analog für `hg_latte.md`-Bauteile) |
| `EINDECKUNG` | SIA 232/1, DIN 18338 | `Eindeckung` (`hg_eindeckung.md`) — eigene sealed-Hierarchie, hält `schicht: Schicht` (bzw. äquivalente Felder; Pendant-Anpassung in Folgeetappe). |
| `ABDICHTUNG` | SIA 271, DIN 18531, DIN 18336 | `Dachabdichtung` (`hg_dachabdichtung.md`) — eigene sealed-Hierarchie, hält `schicht: Schicht`. |
| `TRENNLAGE` | SIA 271, DIN 18531 | (kein Aggregat) |
| `LUFTDICHTHEITSEBENE` | DIN 4108-7, SIA 180 | (kein Aggregat im aktuellen Bestand) |
| `INSTALLATIONSEBENE` | Holzbau-Praxis, nicht normativ (App-Konvention) | (kein Aggregat) |
| `INNENVERKLEIDUNG` | Praxis „Bekleidung", nicht normativ (App-Konvention; IFC `Category = "Finish"`) | (kein Aggregat) |
| `SONSTIGE` | App-Reserve | (kein Aggregat) |

### Schicht ↔ Bauteil-Beziehung

Eine Schicht im Sinne dieser Definition kann physisch aus **mehreren
Einzelbauteilen** zusammengesetzt sein (Wärmedämmschicht aus n
Mineralwolle-Bahnen; Schalungsschicht aus n Schalbrettern;
Traglattung aus n Latten) **oder** aus einer einzigen durchgehenden
Bahn (Dampfbremse, Abdichtungsmembran). Diese Mehrfachheit ist
**nicht** auf der Schicht-Ebene modelliert: die Schicht abstrahiert
über konstante Dicke und einheitliche Funktion. Falls die einzelnen
Platten/Bretter/Bahnen als eigenständige `Bauteil`-Instanzen mit
UUID geführt werden sollen, geschieht das in einer **parallelen
Bauteil-Liste** am Träger-Aggregat (analog
`IfcRelAggregates`); die Beziehung Schicht ↔ Bauteile dieser Schicht
ist eine separate Aggregations-Relation und nicht Bestandteil der
Schicht-Definition.

### CH-/DE-Sprachräume

Strukturell sind CH- und DE-Normwerke äquivalent: beide führen
Schichten als funktional klassifizierte Bestandteile eines
Bauteil-Aufbaus, ohne den Wurzelbegriff abstrakt zu definieren.
Funktions-spezifische Begriffslandschafts-Unterschiede (CH:
Unterdach in drei Beanspruchungs-Klassen; DE: dreigliedrige
Realisierungs-Hierarchie Unterspannung/Unterdeckung/Unterdach;
Eindeckung vs. Dachabdichtung seit 2019 hart getrennt) werden in
den Funktions-Subtyp-Einträgen verankert, nicht hier.

## Beziehungen

- **Oberbegriff**: derzeit `null` (siehe Quellenkonflikt 6).
  Konzeptionell denkbar ist ein künftiger Wurzelbegriff
  `bauteil_aggregat_bestandteil` analog zu `bauteil`; die Einführung
  ist nicht geplant, solange `schicht` der einzige Bestandteils-Typ
  bleibt.

- **Spezialisierungen (fachlich, nicht Code-Vererbung)**:
  Die folgenden Begriffe tragen `oberbegriff: schicht` und sind
  damit fachlich Spezialisierungen der Funktionsschicht. Im Code
  sind sie **keine** sealed-Subtypen von `Schicht`, sondern eigene
  sealed-Klassen mit einer `schicht: Schicht`-Komponente
  (Komposition, siehe Quellenkonflikt 5 und Implementierungshinweis):
  - `eindeckung` (`hg_eindeckung.md`) — sealed pro Material.
  - `unterdach` (`hg_unterdach.md`) — sealed pro Beanspruchungs-
    Klasse.
  - `dampfbremse` (`hg_dampfbremse.md`) — sealed pro sd-Wert-Profil.
  - `waermedaemmung` (`hg_waermedaemmung.md`) — sealed pro Lage
    (Zwischensparren / Aufsparren / Untersparren / Sonstige).
  - `dachabdichtung` (`hg_dachabdichtung.md`) — sealed pro Material.

  Für die übrigen Funktionsklassen (`SCHALUNG`, `KONTERLATTUNG`,
  `TRAGLATTUNG`, `TRENNLAGE`, `LUFTDICHTHEITSEBENE`,
  `INSTALLATIONSEBENE`, `INNENVERKLEIDUNG`, `SONSTIGE`) existiert
  im aktuellen Bestand kein eigenständiges Funktionsschicht-
  Aggregat; sie werden allein über den `SchichtFunktion`-Enumwert
  am Schicht-Tupel getragen.

- **Verwendung**:
  - Bestandteil eines `dachaufbau` (geordnete Schichtfolge 𝒮).
  - Analog Bestandteil künftiger Wand-, Decken-, Bodenaufbauten.

- **Abgrenzung**:
  - **`bauteil`**: einzelnes konstruktives Element mit eigener
    Identität (UUID), eigener Lage in W und eigener Geometrie.
    Schicht hat keines davon. Die einzelnen Platten/Bretter/Bahnen
    *unter* einer Schicht sind Bauteile; die Schicht selbst nicht.
  - **`dachaufbau`**: Träger-Aggregat über einer geordneten
    Schicht-Liste; eigene UUID, eigener Lebenszyklus, eigene
    Konsistenz über der Komposition. Die Schicht ist Bestandteil
    eines Dachaufbaus, nicht selbst der Aufbau.
  - **`dachhaut`**: geometrische Hüllfläche über der äußersten
    Schicht eines Dachaufbaus; keine Material- oder Dickenangabe.
    Die Schicht ist materiell und mit Dicke; die Dachhaut ist
    geometrisch und dickenlos.
  - **`lage`** (Lamelle in `lagenstruktur`): geometrisch identische
    Struktur (gestapelte Wertschichten mit Dicke), aber auf einer
    anderen Ebene angesiedelt — eine Lage ist eine Lamelle
    *innerhalb* eines Mehrlagenholzes (BSP/CLT, Brettsperrholz,
    Furnierschichtholz), die Schicht ist ein Bestandteil
    *zwischen* Bauteilen eines Aufbaus. Eine Lamelle gehört zu
    einem Werkstoff, eine Schicht zu einem Aufbau.
  - **`lagenstruktur`**: Aggregat von `lage`-Lamellen *innerhalb*
    eines einzelnen Holzbauteils. Eine Lagenstruktur ist Eigenschaft
    eines Werkstoffs, eine Schichtfolge ist Eigenschaft eines
    Aufbaus. Die Begriffe sind strukturell parallel, aber auf
    unterschiedlichen Ebenen.
  - **`ebene`**: geometrisches Primitiv (Punkt + Normalenvektor).
    Trotz Praxis-Sprache („luftdichte Ebene", „Installationsebene")
    ist `Schicht` kein Spezialfall von `ebene` — eine Schicht hat
    Dicke, eine Ebene nicht.
  - **`eindeckung`**: speziell die äußerste, regensicher schuppige
    Schicht eines geneigten Daches. Eigenständiger HG-Eintrag mit
    `oberbegriff: schicht`; im Code als sealed-Klasse mit
    `schicht: Schicht`-Komponente realisiert (Komposition).
  - **`unterdach`**: speziell die zweite wasserführende Schicht
    eines geneigten Daches (CH: drei Beanspruchungs-Klassen).
    Eigenständiger HG-Eintrag mit `oberbegriff: schicht`; Code:
    Komposition.
  - **`dachabdichtung`**: wasserdichte Membran-Schicht eines
    Flachdaches. Eigenständiger HG-Eintrag mit
    `oberbegriff: schicht`; Code: Komposition.
  - **`dampfbremse`**: dampfdiffusionshemmende Schicht.
    Eigenständiger HG-Eintrag mit `oberbegriff: schicht`; Code:
    Komposition.
  - **`waermedaemmung`**: wärmeleitfähigkeitsarme Schicht.
    Eigenständiger HG-Eintrag mit `oberbegriff: schicht`; Code:
    Komposition.

## Implementierungshinweis

Datentyp (Domänen-Schicht, Kotlin, Package `domain.bauteil` oder
`domain.aufbau`):

```kotlin
/**
 * Generischer Wertetyp für eine Bauteilschicht: Material + Dicke +
 * Funktionsklasse + funktions-spezifische Parameter. Trägt **keine**
 * eigene Identität (keine UUID, kein IfcRoot-Pendant) und **keine**
 * sealed-Subtypen für die Funktionsschicht-Begriffe `eindeckung`,
 * `unterdach`, `dampfbremse`, `waermedaemmung`, `dachabdichtung` —
 * diese sind eigene sealed-Klassen, die `Schicht` als Komponente
 * halten (Komposition statt Vererbung, siehe Quellenkonflikt 5).
 */
@GlossarBegriff(GlossarTerm.SCHICHT)
data class Schicht(
    val material: MaterialId,            // 𝓦, siehe `werkstoff`
    val dicke: Double,                   // mm, > Toleranzen.LAENGE_EPS
    val funktion: SchichtFunktion,       // Funktionsklasse, Enum
    val parameter: SchichtParameter = SchichtParameter.Keine
) {
    init {
        // Konstruktor-Pre-Conditions: in der App über
        // Resultat<Schicht>-Factory geprüft (Konvention, siehe
        // unten). Die hier dokumentierten Bedingungen entsprechen
        // Konsistenzbedingungen 1–5 der mathematischen Definition.
    }
}

/**
 * Funktions-spezifische Parameter-Tupel (Menge 𝓟_f). Für die meisten
 * Funktionsklassen ist 𝓟_f = ∅ (`SchichtParameter.Keine`); für
 * `DAMPFBREMSE`, `WAERMEDAEMMUNG`, `LUFTDICHTHEITSEBENE` gibt es
 * skalare Parameter, die hier als plausibilitätswirksame
 * **Zusatz-Annotation** an der Schicht stehen. Die normative
 * Detail-Modellierung (z. B. sd-Wert-Funktion einer
 * feuchteadaptiven Bahn) lebt im jeweiligen Funktionsschicht-
 * Aggregat (`hg_dampfbremse.md` etc.), nicht hier.
 */
sealed class SchichtParameter {
    object Keine : SchichtParameter()

    /** sd-Wert in m; für DAMPFBREMSE oder LUFTDICHTHEITSEBENE. */
    data class SdWert(val sd: Double) : SchichtParameter()

    /** Bemessungs-Wärmeleitfähigkeit in W/(m·K); für WAERMEDAEMMUNG. */
    data class Lambda(val lambda: Double) : SchichtParameter()
}

enum class SchichtFunktion {
    DAMPFBREMSE, WAERMEDAEMMUNG, SCHALUNG, UNTERDACH,
    KONTERLATTUNG, TRAGLATTUNG, EINDECKUNG, ABDICHTUNG,
    TRENNLAGE, LUFTDICHTHEITSEBENE, INSTALLATIONSEBENE,
    INNENVERKLEIDUNG, SONSTIGE
}
```

**Komposition statt Vererbung — Beispiel `Unterdach`** (analog für
`Eindeckung`, `Dampfbremse`, `Waermedaemmung`, `Dachabdichtung`,
siehe jeweilige HG-Einträge):

```kotlin
sealed class Unterdach {
    abstract val dachflaechen: List<Dachflaeche>
    abstract val schicht: Schicht        // mit funktion = UNTERDACH
    abstract val maxStauwasserhoehe: Double
    // ... pro Beanspruchungs-Klasse weitere Subtypen
}
```

Konstruktor-Invariante an jedem Funktionsschicht-Aggregat:

```kotlin
require(schicht.funktion == SchichtFunktion.UNTERDACH)
// (bzw. EINDECKUNG / DAMPFBREMSE / WAERMEDAEMMUNG / ABDICHTUNG)
```

Damit ist das Pairing Funktionsschicht-Aggregat ↔ Schichtfunktion
hart geprüft, und die Schicht-Klasse bleibt schlank.

- **Einheit**: Dicke in mm (Double), Sd-Wert in m, Wärmeleitfähigkeit
  λ in W/(m·K). Winkel kommen in der Schicht-Definition nicht vor.

- **Invarianten** (geprüft beim Eintritt in das Modell — Konvention
  `Resultat<Schicht>`-Konstruktoren, niemals `init { require(...) }`):
  1. `material` ist ein gültiger Werkstoff-Identifikator
     gemäss `werkstoff` ⇒ sonst `Entartet.UnbekannterWerkstoff`.
  2. `dicke > Toleranzen.LAENGE_EPS` ⇒ sonst
     `Entartet.NullDickeSchicht`.
  3. funktions-spezifische Parameter-Wertebereiche (Sd > 0;
     λ > 0; …) ⇒ jeweils funktions-spezifische Fehlervariante.
  4. **Optional/konfigurierbar**: Material-Funktions-Verträglichkeit
     als Plausibilitäts-Hinweis (z. B. `funktion = DAMPFBREMSE`
     impliziert Materialklasse Folie / Bahn / Pappe / variable
     Membran). Nicht harter Fehler, sondern
     `Schicht.validierePlausibilitaet(): List<Hinweis>`.

- **Keine UUID**. Die Schicht ist Wert-Tupel. Referenz auf eine
  Schicht im Modell erfolgt über (Träger-Aggregat-UUID, Index in 𝒮),
  analog `IfcMaterialLayerSet`-Position.

- **Edge Cases**:
  - **Sehr dünne Folienschicht** (Dampfbremse, d ≈ 0,2 mm):
    `LAENGE_EPS = 1·10⁻³ mm` ist hinreichend klein.
  - **Schicht aus einer einzigen durchgehenden Membran**:
    keine zusätzliche Bauteil-Liste nötig.
  - **Schicht aus n Einzelbauteilen** (Mineralwolle-Bahnen,
    Schalbretter, Latten): parallele `List<Bauteil>` am Träger-
    Aggregat; nicht im Schicht-Tupel.
  - **Nicht-konstante Dicke** (Gefälledämmung, Aufdoppelung): nicht
    von dieser Definition abgedeckt; spätere Erweiterung mit
    Schichtdicken-Funktion d(p) statt Skalar.
  - **Hinterlüftungsebene** (Luftspalt zwischen Konter- und
    Traglatten): wird im Modell als `Schicht` mit
    `funktion = SchichtFunktion.KONTERLATTUNG` und
    `material = MaterialId.LUFT` oder als App-Konvention separat
    geführt — Festlegung in `hg_konterlatte.md`.

- **IFC-Mapping**:
  | App | IFC 4.3 |
  |---|---|
  | `Schicht` | `IfcMaterialLayer` |
  | `Schicht.dicke` | `IfcMaterialLayer.LayerThickness` |
  | `Schicht.material` | `IfcMaterialLayer.Material` (`IfcMaterial`) |
  | `Schicht.funktion` | `IfcMaterialLayer.Category` (`IfcLabel`-String) |
  | Schichtfolge `𝒮` eines `dachaufbau` | `IfcMaterialLayerSet.MaterialLayers` (geordnet) |
  | Verwendung am Bauteil | `IfcMaterialLayerSetUsage` |

  Empfohlene `Category`-Strings beim Export (kompatibel mit Praxis-CAD):
  `"VaporRetarder"`, `"Insulation"`, `"Sheathing"`, `"Membrane"`,
  `"Counterbattens"`, `"Battens"`, `"Covering"`, `"WaterproofMembrane"`,
  `"Separation"`, `"AirSealing"`, `"InstallationLayer"`, `"Finish"`,
  `"Other"`.

## Quellen

**Primär (normativ):**

- DIN 4108-3:2018-10, „Wärmeschutz und Energie-Einsparung in
  Gebäuden – Teil 3: Klimabedingter Feuchteschutz", Abschnitt 3
  (Begriffe, „Bauteilschicht“; Sd-Wert-Klassifikation).
- DIN 4108-7:2011-01, „Wärmeschutz und Energie-Einsparung in
  Gebäuden – Teil 7: Luftdichtheit", Abschnitt 3
  („Luftdichtheitsschicht“).
- DIN 68800-2:2022-02, „Holzschutz – Teil 2", Anhang B
  (feuchtevariable Schichten).
- SIA 232/1:2011 mit Korrigenda C1:2013, „Geneigte Dächer",
  Abschnitt 2 (Schichtenfolge).
- SIA 271:2021, „Abdichtungen von Hochbauten", Abschnitt 1
  (flächige Abdichtung mit Trenn-, Schutz-, Nutzschicht).
- SIA 180:2014, „Wärmeschutz, Feuchteschutz und Raumklima"
  (Sd-Wert, luftdichte Ebene).
- DIN 18531-1:2017-07, „Abdichtung von Dächern – Teil 1",
  Abschnitt 5.
- ISO 16739-1:2024 / IFC 4.3, Entities `IfcMaterialLayer`,
  `IfcMaterialLayerSet`, `IfcMaterialLayerSetUsage`. Online:
  https://ifc43-docs.standards.buildingsmart.org/ .

**Sekundär:**

- Mönck, W.; Rug, W.: *Holzbau – Bemessung und Konstruktion.*
  16. Aufl., Beuth Verlag 2015.
- Natterer, J.; Herzog, T.; Volz, M.: *Holzbau-Atlas.*
  4. Aufl., Birkhäuser, Basel 2003.
- Lignum (Hrsg.): *Lignatec — Geneigte Dächer in Holzbauweise.*
  Lignum, Zürich, aktuelle Auflage.
- SIGA (Hrsg.): *Technischer Leitfaden Witterungsschutz und
  Luftdichtheit für den Holzbau.* Aktuelle Auflage.
- ZVDH, Fachregel für Dachdeckungen, Stand 2024-04.
- baunormenlexikon.de — Einträge zu DIN 4108-3 und DIN 4108-7.
- Recherchebericht `docs/recherche/2026-05-14_hg_schicht.md`.
