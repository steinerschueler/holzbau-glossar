---
id: wand
benennung: Wand
synonyme: [Wandscheibe, Wandtafel, Wandelement]
abgelehnte_benennungen:
  [Wandbauteil, Mauer, Bretterwand, Trennwand-Konstruktion,
   Riegelwand, Fachwerkwand,
   "wall", "wall panel", "wall assembly", "stud wall",
   "timber frame wall"]
oberbegriff: bauteilgruppe
begriffstyp: aggregat
voraussetzungen:
  [bauteilgruppe, bauteil, schwelle, raehm, staender, riegel,
   strebe, kopfband, fussband, knagge, verbindung, ebene,
   weltkoordinatensystem, lokales_koordinatensystem,
   polyeder, strecke, uuid, toleranzen]
abgrenzung_zu:
  [bauteilgruppe, tragwerk, dach, decke, dachstuhl, binder,
   walm, andreaskreuz, mann, schwelle, raehm, staender,
   riegel, strebe, kopfband, fussband, knagge, fachwerk,
   riegelbau, holzrahmenbau, holzskelettbau, holztafelbau,
   wandtafel, vorgefertigtes_wandelement, schicht, beplankung,
   waermedaemmung, eindeckung, konstruktionsdetail, bausystem,
   raumwand, brandwand, trennwand]
status: entwurf
theorie_pflichtig: required
quellen_primär:
  - "ISO 16739-1:2024 'Industry Foundation Classes (IFC) for data sharing in the construction and facility management industries — Part 1: Data schema' (IFC 4.3.2), Entität `IfcWall` mit `IfcWallStandardCase` und `PredefinedType` (MOVABLE, PARAPET, PARTITIONING, PLUMBINGWALL, SHEAR, SOLIDWALL, STANDARD, POLYGONAL, ELEMENTEDWALL): Wand als eigenständiges Element-Konzept; `IfcWallStandardCase.SHEAR` belegt die tragwerksrelevante Wandscheibe; die im Holzbau übliche `IfcElementAssembly`-Form (PredefinedType BRACED_FRAME oder RIGID_FRAME) bildet die Bauteilgruppen-Sicht für aus Holzbauteilen zusammengesetzte Wände."
  - "DIN EN 1995-1-1:2010-12 (Eurocode 5), Abschnitt 9 'Bauliche Einzelheiten' und insbesondere Abschnitt 9.2 'Aussteifende Wandscheiben': Wandscheibe als tragwerks-konstruktive Einheit aus Rippen (Ständer), Schwelle, Rähm und Beplankung oder diagonalen Aussteifungs-Bauteilen; Lasteinleitung über Schubverbund."
  - "DIN 1052:2008-12, Abschnitt 8 und Abschnitt 12 (Konstruktive Anforderungen): Wandkonstruktionen aus Holz mit Ständern zwischen Schwelle und Rähm vorausgesetzt; aussteifende Funktion über Diagonalen oder Beplankung."
  - "SIA 265:2021 'Holzbau', Schweizerischer Ingenieur- und Architektenverein, §1.1 Fachausdrücke und Abschnitt 5 (Konstruktive Durchbildung) [via: Lignum-Pressemitteilung 2021 'Anwendungshilfen für neue SIA-Norm Holzbau liegen vor']: Wand-Konstruktion mit Schwelle, Ständer und Rähm vorausgesetzt; Volltext paywall-blockiert."
quellen_sekundär:
  - "Lignum, 'Holz A–Z / Konstruktion', lignum.ch/holz_a_z/konstruktion/: Wand als 'Verbundkonstruktion mit Holzrahmen und Beplankungsmaterial' (Tafelbau-Lesart); Skelettbau-Wand als raumabschliessende Schicht-Konstruktion."
  - "Wikipedia, Lemma 'Fachwerkhaus' (de.wikipedia.org/wiki/Fachwerkhaus): Wand-Konstruktion aus Schwelle, Eckständern, Riegeln, Streben und Rähm; CH-Riegelhaus-Verbreitung Nordostschweiz (Thurgau, Zürcher Weinland); rote Balken und weisse Ausfachung."
  - "Lignum (Hrsg.): Holzbautabellen HBT 1 (2024). Lignum, Zürich. Begriffsregister (Volltext nicht zugänglich, Verlags-Schaufenster); Wand-Aussteifungs-Tabellen im Holzrahmenbau und Riegelbau."
  - "Lignum: Pressemitteilung 2021 'Anwendungshilfen für neue SIA-Norm Holzbau liegen vor', lignum.ch/auf_einen_klick/news/."
  - "Mönck, W.; Rug, W.: Holzbau – Bemessung und Konstruktion. 16. Aufl., Beuth, Berlin 2015, Kap. 'Wandkonstruktionen', 'Wandscheiben' und 'Aussteifung'."
  - "Natterer, J.; Herzog, T.; Volz, M.: Holzbau-Atlas. 4. Aufl., Birkhäuser, Basel 2003, Kap. 'Wandbau', 'Fachwerk' und 'Holzrahmenbau'."
  - "Gerner, M.: Fachwerk – Instandsetzung, Sanierung, Neubau. DVA, 7. Aufl. 2007, Glossar 'Wand', 'Wandgefüge', 'Wandständer'."
  - "Großmann, R.: Konstruktionen des deutschen Fachwerkbaus. 1987 — TTH-Primärquelle der Fachwerk-Wand-Komposition."
  - "Thesaurus Traditioneller Holzbau (TTH), RWTH Aachen, Hierarchie-Facette 1922 'Fachwerk-Bauteile'."
  - "buildingSMART International: 'IFC4.3 Documentation' (Version 4.3.2.0, 2024), `IfcWall` und `IfcElementAssembly` (PredefinedType BRACED_FRAME, RIGID_FRAME)."
  - "Recherche-Bericht: docs/recherche/2026-05-16_wand_aggregat.md (§B Aggregat-Architektur, §C Wand-Aggregat, §G Drift-Funde, §J CH-Asymmetrie)."
quellenkonflikt: |
  Sechs Punkte werden hier ausdrücklich aufgelöst.

  **(1) Lesart Architektur vs. Tragwerk.** Im DACH-Korpus
  bezeichnet „Wand" zwei strukturell unterschiedliche Konzepte:

  - **Lesart A (Architektur)**: raumbegrenzende Fläche oder
    Konstruktion, material- und tragwerksneutral. Wikipedia
    „Wand" führt die generische Architektur-Lesart; eine Wand
    kann gemauert, geschüttet, gestapelt oder als Holz-
    Verbundkonstruktion ausgeführt sein. In dieser Lesart ist
    die Wand primär eine räumliche Trennung, nicht eine
    konstruktive Tragwerks-Einheit.
  - **Lesart B (Tragwerk / Holzbau)**: aussteifende oder
    lastabtragende Wandscheibe aus Holzbauteilen, die durch
    ihre Komposition (Schwelle + Ständer + Rähm + optional
    Riegel/Streben/Kopf-/Fussbänder) als konstruktive
    Funktionseinheit definiert ist. DIN EN 1995-1-1 §9.2,
    Lignum „Holz A–Z / Konstruktion", Gerner 2007.

  **App-Wahl: Lesart B.** Dieser Eintrag belegt „Wand"
  ausschliesslich mit der Tragwerks-/Holzbau-Lesart als
  Bauteilgruppe aus konkreten Holz-Bauteilrollen. Lesart A
  bleibt ausserhalb dieses Glossars; falls in einer späteren
  Tool-Linie (Raumplanung, Architektur-Sicht) benötigt, wird
  sie unter einer eigenen Bezeichnung `raumwand` im Cluster
  `40_architektur/` als Folgearbeit geführt (Trigger). Die
  Architektur-Synonyme `Mauer`, `Trennwand-Konstruktion` sind
  in `abgelehnte_benennungen:` aufgenommen, weil sie die hier
  festgelegte Lesart B nicht treffen oder materialgebunden
  sind (Mauer = Stein).

  **(2) Wand-Schichten als orthogonale Aggregat-Familie.**
  Eine Holzbau-Wand trägt im fertigen Zustand typisch
  mehrere Schichten: Beplankung (Gipskarton, OSB,
  Dreischichtplatte), Dämmung (Mineralwolle, Holzfaser,
  Zellulose), Innenverkleidung, Fassade. Die naheliegende
  Modellierung „Schichten sind Bestandteile der Wand-
  Bauteilgruppe" wird hier **bewusst nicht** getroffen:

  - Schichten sind keine Bauteile im Sinne von `bauteil`
    (Stab- oder Plattenform mit Bauteilachse oder
    Bauteilebene); sie sind **Flächen-Aggregate** mit eigener
    Material-Struktur, oft material-übergreifend
    (Verbundwerkstoffe).
  - Die exklusive Mitgliedschaft (Bauteilgruppen-Bedingung 1)
    wäre fragwürdig: dieselbe Beplankungs-Platte kann mehrere
    Wand-Aggregate übergreifen (z. B. durchlaufende
    Fassadenplatte über zwei Ständer-Wand-Aggregate).
  - Der Lebenszyklus von Beplankung und Dämmung ist im
    Sanierungs-Kontext oft anders als der der tragenden
    Holzkonstruktion (Beplankung ersetzbar ohne Eingriff in
    das Wand-Tragwerk).

  Eigene Festlegung: das Wand-Aggregat enthält **nur die
  tragenden Holzbauteile** (Schwelle, Rähm, Ständer, Riegel,
  Strebe, Kopfband, Fussband, Knagge). Beplankung, Dämmung
  und Verkleidung werden als **eigene orthogonale Aggregat-
  Familie** (Schicht-Aggregate, Folgearbeit) geführt und
  einer Wand über das `bausystem`-Konzept (funktionale
  Sicht) oder über eine getrennte Schicht-Aggregat-Linie
  zugeordnet.

  **(3) CH-Asymmetrie: Riegelbau vs. Tafelbau vs. Skelettbau.**
  Die CH-Praxis zeigt drei Wand-Konstruktions-Linien mit
  unterschiedlicher Wand-Modellierung:

  - **Riegelbau** (CH-Pendant zum DE-Fachwerk, traditionell,
    Nordostschweiz): Wand aus Schwelle, Eckständern,
    Zwischen-/Bundständern, Riegeln und diagonalen
    Aussteifungs-Bauteilen (Strebe, Kopf-/Fussband,
    Andreaskreuz). Diese **Riegelbau-CH-Lesart ist die
    Default-Modellierung** dieses Eintrags.
  - **Tafelbau** (Holzrahmenbau / Holztafelbau, modern):
    Wand als „Verbundkonstruktion mit Holzrahmen und
    Beplankungsmaterial" (Lignum). Aussteifung über
    Beplankung (Schicht-Aggregat), nicht über Diagonal-
    Bauteile. Die Wand-Bauteilgruppe besteht in dieser
    Sub-Lesart aus Schwelle + Ständern + Rähm; Streben und
    Bänder können fehlen, weil die Beplankung die
    Aussteifungs-Funktion übernimmt.
  - **Skelettbau** (Holzskelettbau, modern): Tragskelett
    und raumabschliessende Wände sind unabhängig (Lignum);
    die Wand ist primär raumabschliessend, nicht
    tragwerksrelevant. In dieser Lesart kollabiert das
    Wand-Aggregat zu einer Schicht-Konstruktion ohne
    Holz-Rahmen-Bauteile.

  Die App-Modellierung wählt **Riegelbau-CH als Default**
  mit Tafelbau als zulässiger Sub-Lesart (alle
  Aussteifungs-Bauteile optional). Skelettbau-Wände liegen
  ausserhalb des aktuellen Tool-Scopes und werden über
  Folgearbeit-Trigger (Schicht-Aggregat) abgedeckt.
  Lignum HBT 1 (2024) Volltext wäre für die CH-Praxis-
  Verifikation hilfreich; aktuell snippet-basiert.

  **(4) Wandscheibe als tragwerksspezifischer Synonym-Begriff.**
  DIN EN 1995-1-1 §9.2 und Mönck/Rug 2015 verwenden
  „Wandscheibe" für die tragwerks-aussteifende Wand-Lesart
  (vgl. IFC `IfcWallStandardCase.SHEAR`). „Wand" ist der
  generische, „Wandscheibe" der tragwerks-funktionale
  Begriff. Eigene Festlegung: „Wandscheibe" als Synonym
  führen, weil die hier definierte Wand-Bauteilgruppe in
  ihrer tragwerks-aussteifenden Funktion eine Wandscheibe
  **ist**. Die Differenzierung „Wand mit/ohne aussteifender
  Funktion" wird über das optionale `funktion?`-Feld der
  Bauteilgruppe (siehe `hg_bauteilgruppe.md` Z. 105–108)
  ausgedrückt; eine eigene `wandscheibe`-Spezialisierung
  wird nicht angelegt.

  **(5) Wandtafel und Wandelement — vorgefertigt vs. Default.**
  - „**Wandtafel**" bezeichnet im Holztafelbau die
    werkseitig vorgefertigte Liefereinheit: Holzrahmen +
    Beplankung als ein Bauteil, das auf der Baustelle als
    Einheit eingebaut wird (Lignum Tafelbau-Linie). Im
    Sinne von IFC ist eine Wandtafel eine
    `IfcElementAssembly` mit `PredefinedType` ähnlich
    BRACED_FRAME, aber mit anderer
    Vorfertigungs-Charakteristik.
  - „**Wandelement**" ist generischer Synonym-Begriff für
    eine Wand-Liefereinheit (Lignum, Mönck/Rug).
  - „**Vorgefertigtes Wandelement**" (`hg_bauteilgruppe.md`
    Z. 268–286 listet als geplante Spezialisierung) ist die
    spezialisierte Form, die zukünftig als Sub-Eintrag
    angelegt werden kann.

  Eigene Festlegung: alle drei Begriffe als **Synonyme**
  führen, mit dem Hinweis, dass die Default-Wand dieses
  Eintrags **vor Ort gezimmert** ist; eine eigene
  Vorfertigungs-Variante (`vorgefertigtes_wandelement`)
  als Folgearbeit-Trigger.

  **(6) `wandbauteil` als App-Drift aufgelöst.** Die
  Welle-9/10/11-Praxis hat in mehreren Einträgen (`hg_strebe.md`,
  `hg_kopfband.md`, `hg_fussband.md`, `hg_riegel.md`,
  `hg_staender.md`) den Begriff `wandbauteil` als geplante
  Zwischenebene / Sammel-Sealed-Hierarchie für die fünf
  bis sieben Wand-Bauteilrollen erwähnt (jeweils in
  Folgearbeit-Triggern, **nicht** als Frontmatter-`abgrenzung_zu:`).
  Im DACH-Korpus ist `wandbauteil` **kein normfester
  Begriff** — weder Wikipedia/Riegelbau, Lignum
  „Holz A–Z / Konstruktion" noch TTH-Hierarchie 1922
  führen das Lemma. Die Welle-12-Setzung löst die
  App-Drift auf: die Funktion „Sammel-Oberbegriff für
  alle Wand-Bauteilrollen" wird **nicht** als
  Zwischenebene `wandbauteil` modelliert, sondern direkt
  als **Mitgliedschaft im Wand-Aggregat** (`Wand.bestandteile`).
  Konsequenz: `wandbauteil` ist in `abgelehnte_benennungen:`
  aufgenommen; die Folgearbeit-Trigger in den Welle-9/10/11-
  Einträgen, die `wandbauteil` als Zwischenebene erwähnen,
  werden bei nächstem R-Schritt durch den Hinweis auf
  `wand` (dieses Aggregat) ersetzt.
---

## Prosa-Definition

Eine **Wand** ist eine Bauteilgruppe aus mindestens einer
Schwelle, einem Rähm und mindestens zwei Ständern, ergänzt um
eine möglicherweise leere Menge von Riegeln und diagonalen
Aussteifungs-Bauteilen (Strebe, Kopfband, Fussband, Knagge),
deren Bauteilachsen alle in einer gemeinsamen lotrechten
Wandebene liegen und die zusammen eine konstruktive Funktions-
einheit zur raumabschliessenden und lastabtragenden Wand-
Konstruktion eines Holz-Tragwerks bilden.

## Mathematische Definition

Sei

- W das Weltkoordinatensystem (siehe `weltkoordinatensystem`),
- 𝓑 die Menge aller Bauteile im Sinne von `bauteil`,
- 𝓢_Schw, 𝓢_Räh, 𝓢_Stä, 𝓢_Rie, 𝓢_Str, 𝓢_Kbd, 𝓢_Fbd, 𝓢_Kna ⊂ 𝓑
  die Teilmengen mit den Bauteilrollen `schwelle`, `raehm`,
  `staender`, `riegel`, `strebe`, `kopfband`, `fussband`,
  `knagge`,
- 𝒫 die Menge der Ebenen im Sinne von `ebene`,
- 𝒰 der UUID-Raum nach `uuid`,
- 𝒢_huelle die Menge der zulässigen Hüllgeometrie-Repräsentationen
  einer Bauteilgruppe (siehe `bauteilgruppe`),
- e_z := (0, 0, 1)ᵀ die vertikale Welt-Achse,
- ε_K := Toleranzen.KOLLINEAR_EPS,
  ε_L := Toleranzen.LAENGE_EPS.

Dann ist eine **Wand** ein Tupel

```
W := (uuid, schwellen, raehm, staender, riegel, streben,
      kopfbaender, fussbaender, knaggen, wandebene,
      lage, huelle, funktion?, bezeichnung?)
```

mit

- **uuid** ∈ 𝒰: technischer Surrogatschlüssel der Wand (Pflicht,
  persistent, RFC 9562 v7); externe Referenzen auf die Wand
  gehen ausschliesslich auf diese UUID (Aggregat-Wurzel im
  Sinne von `bauteilgruppe`).
- **schwellen** ⊂ 𝓢_Schw, |schwellen| ≥ 1: die endliche, nicht-
  leere Menge der Schwellen am unteren Wand-Rand. Im Regelfall
  |schwellen| = 1; bei mehrteiligem unterem Längsholz (z. B.
  Stockschwelle + Aufdoppelung) sind mehrere zulässig.
- **raehm** ⊂ 𝓢_Räh, |raehm| ≥ 1: die endliche, nicht-leere
  Menge der Rähm-Bauteile am oberen Wand-Rand. Im Regelfall
  |raehm| = 1; bei Doppelrähm oder zweiteiligem oberem
  Längsholz mehrere.
- **staender** ⊂ 𝓢_Stä, |staender| ≥ 2: die endliche Menge der
  lotrechten Ständer der Wand. Mindestens zwei (Eck-/Endständer
  beidseits), sonst kein Wandgefach.
- **riegel** ⊂ 𝓢_Rie, |riegel| ≥ 0: optionale horizontale
  Zwischenhölzer zwischen den Ständern.
- **streben** ⊂ 𝓢_Str, |streben| ≥ 0: optionale Diagonal-
  Aussteifungen.
- **kopfbaender** ⊂ 𝓢_Kbd, |kopfbaender| ≥ 0: optionale Kopf-
  Diagonalbänder am Pfosten-Kopf.
- **fussbaender** ⊂ 𝓢_Fbd, |fussbaender| ≥ 0: optionale Fuss-
  Diagonalbänder am Pfosten-Fuss.
- **knaggen** ⊂ 𝓢_Kna, |knaggen| ≥ 0: optionale Knaggen am
  Wandgefüge.
- **wandebene** ∈ 𝒫: die geometrische Bezugsebene der Wand
  (lotrechte Ebene), in der alle Bauteilachsen liegen. n̂_W ∈ S²
  mit |⟨n̂_W, e_z⟩| ≤ ε_K (lotrecht).
- **lage** ∈ SE(3): die Starrkörpertransformation, die das
  lokale Wand-Koordinatensystem nach W überführt (siehe
  `lokales_koordinatensystem`).
- **huelle** ∈ 𝒢_huelle: die geometrische Hülle der Wand im
  lokalen Koordinatensystem (Polyeder oder Bounding-Volume).
- **funktion?**: optionale Klassifikation der konstruktiven
  Funktion (Werte z. B. AUSSTEIFEND, LASTTRAGEND_NICHT_AUSSTEIFEND,
  NICHT_TRAGEND); die Wandscheiben-Sub-Lesart entspricht dem
  Wert AUSSTEIFEND.
- **bezeichnung?**: optionaler humanlesbarer Name (z. B.
  „Aussenwand Süd", „Innenwand A–B").

und den Konsistenzbedingungen

1. **Bauteilgruppen-Konformität**: das Tupel
   (uuid, bestandteile, lage, huelle, funktion?, bezeichnung?)
   mit
   ```
   bestandteile := schwellen ∪ raehm ∪ staender ∪ riegel ∪
                   streben ∪ kopfbaender ∪ fussbaender ∪ knaggen
   ```
   erfüllt alle Konsistenzbedingungen 1–4 von `bauteilgruppe`
   (exklusive Mitgliedschaft, kaskadische Lebenszyklus-Bindung,
   Hüllen-Inklusion, azyklische Verschachtelung). Insbesondere
   |bestandteile| ≥ 4 (mindestens 1 Schwelle + 1 Rähm + 2 Ständer).

2. **Wandebene lotrecht**: Der Normalenvektor n̂_W der Wandebene
   ist horizontal,
   ```
   |⟨n̂_W, e_z⟩| ≤ ε_K.
   ```

3. **Schwellen horizontal in der Wandebene**: Für jede Schwelle
   s ∈ schwellen liegt a(s) in der Wandebene
   (Punkt-Ebene-Abstand der Endpunkte ≤ ε_L), und der
   Richtungsvektor d̂_s erfüllt |⟨d̂_s, e_z⟩| ≤ ε_K (horizontal).
   Die z-Koordinate aller Schwellen-Endpunkte liegt nahe dem
   unteren Wand-Rand z_min^W.

4. **Rähm horizontal in der Wandebene am oberen Rand**: Für jedes
   r ∈ raehm gilt analog zu (3), aber mit z-Koordinaten am
   oberen Wand-Rand z_max^W.

5. **Ständer lotrecht in der Wandebene**: Für jeden Ständer
   p ∈ staender liegt a(p) in der Wandebene, und der
   Richtungsvektor d̂_p ist kollinear zu e_z
   (||d̂_p × e_z|| ≤ ε_K).

6. **Ständer zwischen Schwelle und Rähm**: Für jeden Ständer
   p ∈ staender existieren s ∈ schwellen und r ∈ raehm, sodass
   ein Endpunkt von a(p) auf a(s) liegt (Punkt-Gerade-Abstand
   ≤ ε_L) und der andere Endpunkt auf a(r).

7. **Riegel horizontal zwischen Ständern**: Für jeden Riegel
   q ∈ riegel liegt a(q) in der Wandebene, ist horizontal, und
   verbindet zwei Ständer aus staender (analog zu `hg_riegel.md`).

8. **Aussteifungs-Bauteile in der Wandebene**: Für jedes
   b ∈ streben ∪ kopfbaender ∪ fussbaender liegen beide
   Endpunkte von a(b) in der Wandebene (Punkt-Ebene-Abstand
   ≤ ε_L). Die jeweiligen Anker-Bedingungen (Strebe, Kopfband,
   Fussband) ihrer Bauteilrolle gegen die Bauteile dieser Wand
   sind erfüllt (siehe `hg_strebe.md` Bedingung 5,
   `hg_kopfband.md` Bedingung 5, `hg_fussband.md` Bedingung 5).
   Knaggen werden ebenfalls in der Wandebene oder nahe daran
   (Knagge ragt aus der Wand heraus, ist aber in der Wand
   verankert) erfasst.

9. **Hüllen-Inklusion**: Die geometrische Punktmenge aller
   Bestandteile liegt im Toleranzband um die Wandebene und in
   der Hülle huelle:
   ```
   ⋃_{b ∈ bestandteile} G_W(b) ⊆ G_W(W).
   ```

Die **geometrische Punktmenge** der Wand in W ist

```
G_W(W) := lage(G_lokal(huelle)) ⊂ ℝ³
```

(transformierte Hülle); die Vereinigung der Bestandteils-
Punktmengen ist im Allgemeinen eine echte Teilmenge davon
(siehe `bauteilgruppe` Bedingung 3).

## Wohldefiniertheit

- **Existenz**: Für jedes Wandgefüge mit mindestens einer
  Schwelle, einem Rähm und zwei Ständern in einer gemeinsamen
  lotrechten Wandebene lässt sich eine Wand als Tupel der
  angegebenen Form erfassen. Mindestkonfiguration:
  |schwellen| = 1, |raehm| = 1, |staender| = 2, alle anderen
  Mengen leer; Wandebene aus den drei Bauteilachsen abgeleitet.
- **Eindeutigkeit der Identität**: Bedingung 1 (Bauteilgruppen-
  Konformität) erbt die Aggregat-Wurzel-Auflösung von
  `bauteilgruppe`; die Wand-UUID ist konstruktionsseitig zu
  vergeben und persistent.
- **Eindeutigkeit der Wandebene**: aus zwei nicht-kollinearen
  lotrechten Ständer-Bauteilachsen plus einer horizontalen
  Schwelle ist die Wandebene eindeutig bestimmt (drei Punkte
  in allgemeiner Lage spannen die Ebene auf).
- **Trivial wohldefinierte Bestandteils-Mengen**: alle
  Bauteil-Mengen sind unsortiert; alle Aussagen über die Wand
  sind invariant unter Permutation der Bestandteile innerhalb
  der jeweiligen Menge.
- **Unabhängigkeit von der Wahl des lokalen Koordinatensystems**:
  für jede zulässige Wahl liefert die zugehörige
  Lage-Transformation dieselbe Punktmenge G_W(W); semantisch
  invariant.
- **Konsistenz mit `bauteilgruppe`**: jede Konsistenzbedingung
  von `bauteilgruppe` (exklusive Mitgliedschaft, kaskadische
  Löschung, Hüllen-Inklusion, Azyklizität) gilt für die Wand,
  weil sie Subtyp von `bauteilgruppe` ist. Die Wand-spezifischen
  Bedingungen 2–9 treten additiv hinzu und schwächen keine
  Bauteilgruppen-Bedingung ab.
- **Konsistenz mit den Bauteilrollen**: jedes Bauteil
  b ∈ bestandteile trägt die in seiner jeweiligen Rolle
  (`hg_schwelle.md` etc.) definierten Constraints; die
  Wand-Bedingungen fordern zusätzlich die gemeinsame Lage
  in der Wandebene und die wechselseitigen Anker-Beziehungen
  (Bedingungen 6–8).
- **Exklusivität gegenüber benachbarten Wänden**: jeder Ständer
  und jedes Wand-Bauteil gehört zu höchstens einer Wand-
  Bauteilgruppe (Spezialisierung von Bauteilgruppen-
  Bedingung 1). Eck-Ständer, an denen zwei Wände aneinander-
  stossen, werden in der Regel einer der beiden Wände
  zugeordnet (Modell-Entscheidung beim Aufbau).
- **Nicht-Zirkularität**: die Definition verwendet
  `bauteilgruppe`, `bauteil`, `schwelle`, `raehm`, `staender`,
  `riegel`, `strebe`, `kopfband`, `fussband`, `knagge`,
  `verbindung`, `ebene`, `strecke`, `polyeder`, `uuid`,
  `lokales_koordinatensystem`, `weltkoordinatensystem`,
  `toleranzen` — alle bereits definiert. Sie referenziert
  `andreaskreuz` und `mann` als geometrisch verwandte
  Aggregate (geschwisterlich unter `bauteilgruppe`) in
  `abgrenzung_zu:`, nicht in `voraussetzungen:`.
- **Eliminierbarkeit**: jede Verwendung von „Wand" in der
  App-Tragwerks-Lesart lässt sich durch das obige Tupel mit
  den neun Konsistenzbedingungen ersetzen.

## Erläuterung (nicht normativ)

Die Wand ist die ontologische Antwort auf das Wand-Bauteilgefüge
im Holzbau: ein Bündel von Stab-Bauteilen in einer gemeinsamen
lotrechten Ebene, das geometrisch räumliche Trennung leistet
und statisch eine eigene Tragwerks-Einheit bildet — die
Wandscheibe — mit eigener Auflagerung, eigenen Lastpfaden und
eigener Aussteifungs-Konfiguration.

### Geometrische Erscheinung

Die Default-Wand reicht von einer unteren Schwelle bis zu
einem oberen Rähm, beidseitig von Eckständern begrenzt; Höhe
typisch eine Geschosshöhe (2.4–3.0 m), Länge je nach
Grundriss (1–10 m). Zwischen Eckständern stehen
Zwischenständer (Achsabstand 60–120 cm im Holzrahmenbau;
80–150 cm im historischen Fachwerk). Zwischen den Ständern
können horizontale Riegel die Wand in Gefache untergliedern.
Diagonal-Aussteifung erfolgt durch Streben, Kopfbänder,
Fussbänder oder ihre Komposite (Andreaskreuz im Gefach,
Mann-Figur am Pfosten).

### Bestandteile in der App-Modellierung

Konstitutiv sind eine Schwelle, ein Rähm und mindestens zwei
Ständer (zusammen mindestens vier Bauteile). Variabel sind
Riegel (Anzahl ≥ 0), Streben, Kopf-/Fussbänder und Knaggen
(jeweils ≥ 0). Bauteilachsen aller Bestandteile liegen
**ausnahmslos** in der gemeinsamen Wandebene (Toleranzband
ε_L). Eine Wand mit Bauteilen ausserhalb der Wandebene ist
kein Wand-Aggregat, sondern eine Wand-plus-Wand- oder Wand-
plus-Riegel-Kombination.

### Aussteifungs-Lesarten

Vier Aussteifungs-Typologien sind im DACH-Holzbau verbreitet:

1. **Riegelbau / Fachwerk** (historisch, CH-Default): die
   Wand wird durch eingelassene **diagonale Holzbauteile**
   (Strebe, Kopfband, Fussband) ausgesteift. Die Wand-
   Bauteilgruppe enthält diese Bauteile. Mann-Figuren und
   Andreaskreuze sind eigene Aggregate, geschwisterlich
   unter `bauteilgruppe`, die ihre Bestandteile (Streben,
   Bänder) mit der Wand teilen können — aber **exklusiv**:
   ein bestimmter Strebe-Stab ist Mitglied entweder der
   Wand-Bauteilgruppe oder des Andreaskreuz-Aggregats,
   nicht beider. Die Aggregat-Aufteilung ist eine
   Modell-Entscheidung (typisch wird das Andreaskreuz-
   Aggregat als Bestandteil der Wand-Bauteilgruppe oder
   als Schwester-Aggregat geführt — die App folgt der
   Schwester-Lesart, Bauteilgruppe-Bedingung 4
   Verschachtelung, weil Andreaskreuz-Aggregate auch
   geschossübergreifend modelliert werden können).

2. **Holzrahmenbau** (modern): die Wand wird **durch
   Beplankung** (OSB, Dreischichtplatte, Gipsfaser)
   ausgesteift. Streben und Bänder können fehlen; die
   Aussteifung erfolgt über die Schicht-Aggregat-Familie
   (Folgearbeit), die orthogonal zur Wand-Bauteilgruppe
   geführt wird.

3. **Holztafelbau** (modern, vorgefertigt): die Wand wird
   als **Wandtafel** vorgefertigt geliefert; Beplankung
   ist werkseitig montiert. Die Wand-Bauteilgruppe ist
   strukturell identisch zur Holzrahmenbau-Wand, hat aber
   eine eigene Spezialisierung als Aggregat-Subtyp
   `vorgefertigtes_wandelement` (Folgearbeit).

4. **Holzskelettbau** (modern): die tragenden Stützen
   sind keine Ständer einer Wand, sondern eigenständige
   Säulen des Tragskeletts; die raumabschliessenden
   Wände sind primär Schicht-Konstruktionen ohne
   tragende Holzbauteile. Diese Lesart liegt ausserhalb
   des Wand-Aggregats; die Holzskelett-Stützen werden
   über `staender` mit Bauteilrolle oder über Folgearbeit
   `stuetze` modelliert.

### Verhältnis zur Wandscheibe (tragwerks-funktional)

DIN EN 1995-1-1 §9.2 und Mönck/Rug 2015 verwenden
„Wandscheibe" für die tragwerks-aussteifende Wand-Lesart.
In der App-Modellierung ist die Wandscheibe **funktionale
Sicht** auf das Wand-Aggregat (Wert AUSSTEIFEND im
`funktion?`-Feld der Bauteilgruppe). Eine Wand kann
aussteifend (Wandscheibe) oder nicht-aussteifend (rein
raumabschliessend) wirken; die Aussteifungs-Funktion ist
Ergebnis der Bauteil-Komposition und der Verbindungen,
nicht eine separate Wand-Klasse.

### Verhältnis zu Mann-Figur und Andreaskreuz

Die Wand-Bauteilgruppe enthält in der Riegelbau-Lesart
einzelne Streben, Kopfbänder und Fussbänder. Wenn diese
einzelnen Bauteile in einer übergeordneten Bündel-
Konfiguration auftreten — zwei kreuzende Streben im
gleichen Gefach, vier Bänder am gleichen Pfosten — wird
die übergeordnete Konfiguration durch ein eigenes
Geschwister-Aggregat unter `bauteilgruppe` modelliert:

- **Andreaskreuz** (`andreaskreuz`): zwei sich kreuzende
  Streben im selben Gefach. Geschwister-Aggregat unter
  `bauteilgruppe`; nicht Bestandteil der Wand-Bauteilgruppe,
  sondern paralleles Aggregat.
- **Mann** (`mann`) und Sub-Varianten (Halber, Wilder,
  Hessen, Schwäbisch): Bündel-Aussteifung am Pfosten aus
  Kopf-/Fussbändern und optional einer zentralen Strebe.
  Geschwister-Aggregat unter `bauteilgruppe`.

Die exklusive Mitgliedschaft (Bauteilgruppen-Bedingung 1)
bedeutet: ein bestimmter Strebe-Stab gehört zu **genau
einem** Aggregat — entweder zur Wand oder zum
Andreaskreuz/Mann, nicht zu beiden. Die App-Entscheidung
folgt der **Schwester-Lesart**: die Wand-Bauteilgruppe
enthält die einzelnen Streben und Bänder; Andreaskreuze
und Mann-Figuren sind eigenständige Geschwister-Aggregate
und referenzieren die geteilten Bauteile **nicht**. Eine
alternative Modellierung (Wand enthält das Andreaskreuz
als verschachteltes Aggregat) ist zulässig, wenn das
Andreaskreuz konstitutiv zur Wand gehört; die Entscheidung
ist Modell-zeitlich.

### CH/DE-Asymmetrie

| Bauweise | Wand-Aussteifung typisch | Wand-Aggregat |
|---|---|---|
| Fachwerkbau (DE/AT, historisch) | Strebe + Kopf-/Fussband + Mann/Andreaskreuz | breit gefüllt |
| Riegelbau (CH, traditionell) | Strebe + Kopf-/Fussband (Mann/Andreaskreuz seltener) | breit gefüllt |
| Holzrahmenbau (modern) | Beplankung (Schicht-Aggregat) | nur Schwelle/Ständer/Rähm |
| Holztafelbau (modern, vorgef.) | Beplankung werkseitig | als Wandtafel-Subtyp |
| Holzskelettbau (modern) | tragendes Skelett unabhängig | Wand-Konzept entfällt |

Die Default-Modellierung dieses Eintrags ist die
**Riegelbau-CH-Lesart** mit allen Aussteifungs-Bauteilen
optional. Eric als CH-Zimmermann arbeitet primär in dieser
Lesart; die Welle-12-Setzung ist auf seinen
CH-Berufskorpus zugeschnitten.

## Beziehungen

- **Oberbegriff**: `bauteilgruppe`. Die Wand erfüllt alle
  Bauteilgruppen-Merkmale (exklusive Mitgliedschaft,
  kaskadische Lebenszyklus-Bindung, eigene Hülle, eigene
  Identität, konstruktive Funktionseinheit) und fügt
  wand-spezifische Merkmale hinzu: gemeinsame lotrechte
  Wandebene, Schwelle-Ständer-Rähm-Grundstruktur, optionale
  Aussteifungs-Bauteile.
- **Bestandteile (partitiv)**:
  - **Schwelle** (`schwelle`, ≥ 1 Stück): unteres horizontales
    Längsholz; Auflagerung des Wandgefüges auf der Decke oder
    dem Fundament.
  - **Rähm** (`raehm`, ≥ 1 Stück): oberes horizontales
    Längsholz; trägt Geschossdecke, Sparren oder oberen
    Lastpfad.
  - **Ständer** (`staender`, ≥ 2 Stück): lotrechte
    Stab-Bauteile zwischen Schwelle und Rähm. Eck-,
    Bund-, Zwischenständer (siehe `StaenderPosition`-
    Annotation).
  - **Riegel** (`riegel`, ≥ 0): horizontale
    Zwischenhölzer.
  - **Strebe** (`strebe`, ≥ 0): diagonale Aussteifung mit
    Pfosten-Mittel- oder Doppel-Horizontal-Anker.
  - **Kopfband** (`kopfband`, ≥ 0): diagonale Aussteifung
    am Pfosten-Kopf.
  - **Fussband** (`fussband`, ≥ 0): diagonale Aussteifung
    am Pfosten-Fuss.
  - **Knagge** (`knagge`, ≥ 0): dreieckiges Vollholz als
    Konsole am Wandgefüge.
- **Geometrische Bezugsobjekte (nicht Mitglieder)**:
  - **Wandebene** (`ebene`): die lotrechte Bezugsebene; alle
    Bauteilachsen liegen in ihr.
  - **Wand-Eckpunkte**: geometrische Referenzpunkte am
    Schnitt von Schwelle, Rähm und Eckständern.
- **Funktionale Sicht (über `funktion?`-Feld)**:
  - **AUSSTEIFEND** (Wandscheibe): tragwerks-aussteifende
    Wand, DIN EN 1995-1-1 §9.2.
  - **LASTTRAGEND_NICHT_AUSSTEIFEND**: trägt vertikale Lasten,
    aber nicht horizontale Aussteifung.
  - **NICHT_TRAGEND**: rein raumabschliessend.
- **Spezialisierungen** (eigene Einträge folgen, trigger-basiert):
  - **Vorgefertigtes Wandelement** (`vorgefertigtes_wandelement`,
    Folgearbeit, in `hg_bauteilgruppe.md` Z. 268–286 bereits
    als Spezialisierung gelistet): Holztafelbau-Wand als
    werkseitig vorgefertigte Liefereinheit.
  - **Raumwand** (`raumwand`, Cluster `40_architektur/`,
    Folgearbeit): architektonische Wand-Lesart.
- **Verwendung**:
  - Bestandteil eines **Tragwerks** (`tragwerk`) — als
    Bauteilgruppe des Wandsystems.
  - Bestandteil eines **Bauwerks** (`bauwerk`) —
    raumabschliessende und tragende Funktion.
  - Auflager-Träger für **Decken**, **Dachflächen**,
    **Sparren** über das obere Rähm.
- **Abgrenzung**:
  - **Bauteilgruppe** (`bauteilgruppe`): Oberbegriff.
  - **Tragwerk** (`tragwerk`): das übergeordnete Aggregat,
    in dem die Wand als Bauteilgruppe geführt wird.
  - **Dach** (`dach`), **Dachstuhl** (`dachstuhl`): andere
    Aggregat-Familie (geneigte Bauteilgruppe auf dem oberen
    Rähm der Wand).
  - **Decke** (Folgearbeit): horizontale Bauteilgruppe,
    geschwisterlich zur Wand.
  - **Binder** (`binder`): strukturparalleles Geschwister-
    Aggregat (Tragebene, Spannweiten-Überbrückung).
  - **Walm** (`walm`): geschwisterliches Aggregat im
    Dachstuhl.
  - **Andreaskreuz** (`andreaskreuz`): geschwisterliches
    Aggregat innerhalb derselben Wandebene — Bündelung
    zweier sich kreuzender Streben in einem Gefach. Die
    Wand-Bauteilgruppe kann Streben einzeln enthalten; das
    Andreaskreuz-Aggregat führt sie als bündelnde Schwester-
    Komposition (siehe Erläuterung).
  - **Mann** (`mann`) und Sub-Varianten: geschwisterliche
    Aggregate innerhalb derselben Wandebene — Bündelung der
    Aussteifungs-Bauteile am Pfosten.
  - **Schwelle**, **Rähm**, **Ständer**, **Riegel**,
    **Strebe**, **Kopfband**, **Fussband**, **Knagge**:
    Bauteilrollen der Wand; sind Bestandteile, nicht die
    Wand selbst.
  - **Wandtafel**, **Vorgefertigtes Wandelement**: Synonyme
    bzw. Spezialisierungen (Vorfertigungs-Charakteristik).
  - **Schicht**, **Beplankung**, **Wärmedämmung**,
    **Eindeckung**: orthogonale Schicht-Aggregat-Familie
    (Folgearbeit); nicht Bestandteile der Wand-
    Bauteilgruppe.
  - **Konstruktionsdetail** (`konstruktionsdetail`):
    Detail-Begriff für Anschlüsse innerhalb der Wand;
    eigene Begriffsfamilie.
  - **Bausystem** (`bausystem`): orthogonaler funktionaler
    Aggregations-Mechanismus; die Wand kann Mitglied eines
    aussteifenden Bausystems sein, ist aber nicht selbst
    ein Bausystem.
  - **Fachwerk**, **Riegelbau**, **Holzrahmenbau**,
    **Holzskelettbau**, **Holztafelbau**: Bauweisen-
    Klassifikationen; eine Wand wird in einer dieser
    Bauweisen errichtet, ist aber nicht selbst eine
    Bauweise (Folgearbeit).
  - **Raumwand**, **Brandwand**, **Trennwand**:
    Architektur- bzw. brandschutztechnische Wand-Lesarten
    (Folgearbeit, ausserhalb der Tragwerks-Lesart B).
  - **Verbindung** (`verbindung`): die Wand enthält
    Verbindungen zwischen ihren Bestandteilen
    (Schwelle-Ständer-Zapfen, Rähm-Ständer-Zapfen,
    Strebe-Pfosten-Zapfen); sie ist selbst keine
    Verbindung.

## Implementierungshinweis

**Im aktuellen Glossarstand wird keine eigene Code-Klasse
`Wand` angelegt.** Die ontologische Vorbereitung lebt zunächst
nur im Glossar; eine Code-Klasse entsteht zusammen mit dem
ersten konkreten Tool, das eine Wand als Bauteilgruppe
modelliert (zugleich Trigger für `vorgefertigtes_wandelement`
und ggf. die Schicht-Aggregat-Familie). Der folgende Skizzen-
Code ist ausschliesslich orientierender Implementierungshinweis
für diesen Zeitpunkt und folgt der Sealed-Hierarchie unter
`Bauteilgruppe` aus `hg_bauteilgruppe.md`, strukturparallel zur
Walm-/Binder-Skizze in `hg_walm.md`/`hg_binder.md`.

```kotlin
// SKIZZE — nicht jetzt anlegen.
// Glossar: hg_wand.md

package domain.bauteil

import domain.bauteil.Bauteilgruppe
import domain.bauteil.Schwelle
import domain.bauteil.Raehm
import domain.bauteil.Staender
import domain.bauteil.Riegel
import domain.bauteil.Strebe
import domain.bauteil.Kopfband
import domain.bauteil.Fussband
import domain.bauteil.Knagge
import domain.geometrie.Ebene
import java.util.UUID

/**
 * Wand: Bauteilgruppe aus Schwelle(n), Rähm(en), Ständern und
 * optional Riegeln, Streben, Kopf-/Fussbändern und Knaggen,
 * deren Bauteilachsen in einer gemeinsamen lotrechten Wandebene
 * liegen.
 *
 * Sealed unter Bauteilgruppe; konkrete Sub-Typen
 * (vorgefertigtes Wandelement, Aussenwand, Innenwand) entstehen
 * trigger-basiert.
 */
sealed class Wand : Bauteilgruppe() {
    abstract val schwellen: Set<Schwelle>          // |schwellen| >= 1
    abstract val raehm: Set<Raehm>                 // |raehm| >= 1
    abstract val staender: Set<Staender>           // |staender| >= 2
    abstract val riegel: Set<Riegel>               // >= 0
    abstract val streben: Set<Strebe>              // >= 0
    abstract val kopfbaender: Set<Kopfband>        // >= 0
    abstract val fussbaender: Set<Fussband>        // >= 0
    abstract val knaggen: Set<Knagge>              // >= 0
    abstract val wandebene: Ebene                  // lotrecht
    abstract val funktion: WandFunktion?           // optional

    init {
        // 1. schwellen.size >= 1
        // 2. raehm.size >= 1
        // 3. staender.size >= 2
        // 4. wandebene lotrecht
        // 5. alle Bauteilachsen in Wandebene (Toleranzband eps_L)
        // 6. Ständer zwischen Schwelle und Rähm verankert
        // 7. Bauteilrollen-Constraints geerbt
        // 8. Bauteilgruppen-Bedingungen geerbt
    }
}

enum class WandFunktion {
    AUSSTEIFEND,                     // Wandscheibe (DIN EN 1995-1-1 §9.2)
    LASTTRAGEND_NICHT_AUSSTEIFEND,   // trägt vertikal, nicht horizontal
    NICHT_TRAGEND,                   // rein raumabschliessend
}
```

- **Einheit**: Längen in mm (Double); Winkel intern in Radiant;
  Lage als SE(3)-Element.
- **Identität**: `uuid` ist Pflicht und persistent (RFC 9562 v7);
  externe Referenzen auf eine Wand gehen ausschliesslich auf
  diese UUID. Bestandteile (Schwellen, Rähm, Ständer, ...)
  werden über ihre jeweiligen UUIDs referenziert (Foreign-Key-
  Regel, Memory `project_bauteil_identifikation`).
- **Invarianten** (in `init` bzw. Fabrikfunktionen prüfen, bei
  Verletzung `Resultat.Fehler` bzw. `Entartet`-Variante; niemals
  Exception werfen):
  1. `schwellen.size >= 1` ⇒ sonst `Entartet.KeineSchwelle`.
  2. `raehm.size >= 1` ⇒ sonst `Entartet.KeinRaehm`.
  3. `staender.size >= 2` ⇒ sonst `Entartet.ZuWenigStaender`.
  4. Wandebene lotrecht: `|n̂_W · e_z| ≤ Toleranzen.KOLLINEAR_EPS`
     ⇒ sonst `Entartet.WandebeneNichtLotrecht`.
  5. Für jedes Bauteil b ∈ bestandteile: beide Endpunkte der
     Bauteilachse liegen in der Wandebene
     (Punkt-Ebene-Abstand ≤ `Toleranzen.LAENGE_EPS`) ⇒ sonst
     `Entartet.BauteilAusserhalbWandebene`.
  6. Für jeden Ständer p ∈ staender: ein Endpunkt von a(p) liegt
     auf einer Schwellen-Achse, der andere auf einer Rähm-Achse
     ⇒ sonst `Entartet.StaenderOhneAnschluss`.
  7. **Exklusive Mitgliedschaft** (geerbt von `bauteilgruppe`):
     kein Bauteil b ∈ bestandteile ist zugleich Bestandteil
     einer anderen Wand-Bauteilgruppe oder eines geschwister-
     lichen Aggregats, das es als Mitglied führen würde
     (Andreaskreuz, Mann). Bei Verletzung
     `Entartet.MehrfachMitgliedschaft`.
- **Edge Cases**:
  - **Wand mit nur Schwelle + Rähm + 2 Ständern (Eckwand-
    Mindestform)**: zulässig; entartet zu einem einzigen
    Gefach ohne Aussteifung.
  - **Wand mit Doppel-Rähm oder Stockschwelle**: zulässig;
    |raehm| > 1 oder |schwellen| > 1.
  - **Eckwand-Übergang**: zwei Wände treffen rechtwinklig in
    einem Eckständer; der Eckständer wird einer der beiden
    Wände zugeordnet (Modell-Entscheidung).
  - **T-Stoss-Wand**: eine Wand stösst in der Mitte an eine
    andere; die anschliessende Wand hat einen Eckständer,
    der nicht zur Hauptwand gehört.
  - **Wand mit Andreaskreuz / Mann-Figur**: die Bauteile des
    Andreaskreuzes/Manns werden je nach Modell-Entscheidung
    entweder der Wand-Bauteilgruppe **oder** dem
    Andreaskreuz-/Mann-Aggregat zugeordnet, nicht beiden
    (exklusive Mitgliedschaft).
  - **Holzrahmenbau-Wand ohne Diagonal-Bauteile**: zulässig;
    alle Aussteifungs-Mengen leer. Die Aussteifungs-Funktion
    erfolgt über das parallele Schicht-Aggregat (Folgearbeit).
  - **Wand mit gebrochener oder geknickter Grundrissform**:
    nicht zulässig — eine geknickte Wand-Form wird als
    **zwei oder mehr separate Wand-Bauteilgruppen**
    modelliert, je eine pro Wandebene. Polygonal-Wände
    sind Folgearbeit (IFC `IfcWall.PredefinedType.POLYGONAL`).
- **Abgeleitete Eigenschaften** (als Funktionen, keine Felder):
  - `geometrieInWelt(): GeometrieInW` = `lage(huelle)` als
    transformierte Hülle in W (geerbt von `Bauteilgruppe`).
  - `laenge(): Double` (mm) = horizontale Ausdehnung der
    Wand in der Wandebene; aus Schwelle abgeleitet.
  - `hoehe(): Double` (mm) = vertikale Ausdehnung der Wand;
    aus z-Differenz Schwelle/Rähm.
  - `istWandscheibe(): Boolean` = `funktion == AUSSTEIFEND`.
  - `aussteifungs_typ(): Set<Aussteifungstyp>` =
    {DIAGONAL_STREBE, DIAGONAL_BAND, ANDREASKREUZ_VERWANDT,
    BEPLANKUNG_VERWANDT, ...} abgeleitet aus der
    Komposition.

## Quellen

**Primär (normativ):**

- ISO 16739-1:2024, „Industry Foundation Classes (IFC) for data
  sharing in the construction and facility management
  industries — Part 1: Data schema" (IFC 4.3.2), `IfcWall`,
  `IfcWallStandardCase`, `IfcElementAssembly`.
- DIN EN 1995-1-1:2010-12, „Eurocode 5: Bemessung und Konstruktion
  von Holzbauten — Teil 1-1", insbesondere Abschnitt 9.2
  (Aussteifende Wandscheiben).
- DIN 1052:2008-12, „Entwurf, Berechnung und Bemessung von
  Holzbauwerken", Abschnitte 8 und 12.
- SIA 265:2021, „Holzbau", Schweizerischer Ingenieur- und
  Architektenverein, Zürich, §1.1 Fachausdrücke
  [via: Lignum-Pressemitteilung 2021].

**Sekundär:**

- Lignum, „Holz A–Z / Konstruktion", lignum.ch/holz_a_z/
  konstruktion/ (abgerufen 2026-05-16).
- Lignum (Hrsg.): *Holzbautabellen HBT 1 (2024).* Lignum,
  Zürich.
- Lignum: *Pressemitteilung 2021 — Anwendungshilfen für neue
  SIA-Norm Holzbau.*
- Mönck, W.; Rug, W.: *Holzbau – Bemessung und Konstruktion.*
  16. Aufl., Beuth, Berlin 2015.
- Natterer, J.; Herzog, T.; Volz, M.: *Holzbau-Atlas.*
  4. Aufl., Birkhäuser, Basel 2003.
- Gerner, M.: *Fachwerk – Instandsetzung, Sanierung, Neubau.*
  DVA, 7. Aufl. 2007.
- Großmann, R.: *Konstruktionen des deutschen Fachwerkbaus.*
  1987.
- Thesaurus Traditioneller Holzbau (TTH), RWTH Aachen.

**Korpus (nicht autoritativ):**

- Wikipedia, Lemma „Fachwerkhaus" (de.wikipedia.org/wiki/
  Fachwerkhaus, abgerufen 2026-05-16).
- Wikipedia, Lemma „Wand" (allgemeine Architektur-Lesart).
- Wikipedia, Lemma „Riegelbau" / „Ständerbauweise".
- Recherche-Bericht:
  `docs/recherche/2026-05-16_wand_aggregat.md`.
- Recherche-Bericht (Vorgänger):
  `docs/recherche/2026-05-15_pfosten_staender.md`,
  `docs/recherche/2026-05-15_strebe_kopfband_bug.md`,
  `docs/recherche/2026-05-15_fussband_knagge.md`.

## Folgearbeit (trigger-basiert)

1. **`vorgefertigtes_wandelement`** — Holztafelbau-Wand als
   werkseitig vorgefertigte Liefereinheit. Trigger: erstes
   Tool zur Holztafelbau-Modellierung.
2. **Schicht-Aggregat-Familie** (`schicht_aggregat`,
   `beplankungs_aggregat`, `daemm_aggregat`) — orthogonale
   Aggregat-Linie für Wand-Schichten (Beplankung, Dämmung,
   Verkleidung). Trigger: erste Holzrahmenbau-/Tafelbau-
   Modellierung mit Beplankungs-Aussteifung.
3. **`raumwand`** (Cluster `40_architektur/`) — architektonische
   Wand-Lesart (Lesart A). Trigger: erste Raumplanungs-/
   Architektur-Tool-Linie.
4. **`brandwand`**, **`trennwand`** — brandschutz- bzw.
   nutzungstechnische Wand-Spezialisierungen. Trigger:
   Brandschutz-/Raumakustik-Tool-Erweiterung.
5. **Code-Klasse `Wand`** und Sealed-Hierarchie. Trigger:
   erstes Tool, das Wand-Aggregate als Modell-Entität führt
   (`hg_bauteilgruppe.md` Z. 325–333).
6. **SIA-265-Verifikation**: bei Volltext-Zugriff (Eric)
   SIA 265:2021 §1.1 Fachausdrücke direkt prüfen, ob „Wand"
   und „Wandscheibe" als Lemmata geführt sind.
7. **Lignum HBT 1 (2024)-Verifikation der CH-Aussteifungs-
   Praxis**: bei Eric-Zugang punktuelle Begriffsregister-
   Sichtung; bestätigt oder präzisiert die Riegelbau-CH-
   Default-Modellierung.

**R-Schritt-Drift in bestehenden Einträgen** (bei R2 dieser
Welle nachgezogen):

- **`hg_strebe.md`, `hg_kopfband.md`, `hg_fussband.md`,
  `hg_riegel.md`, `hg_staender.md`** verwenden in
  Folgearbeit-Triggern und Beziehungs-Abschnitten den
  Begriff `wandbauteil` als geplante Zwischenebene /
  Sammel-Sealed-Hierarchie. Dieser Begriff ist mit Welle 12
  aufgelöst (siehe Quellenkonflikt-Block (6)): die
  Sammel-Funktion wird durch die Mitgliedschaft im
  `wand`-Aggregat erfüllt, eine `wandbauteil`-Zwischenebene
  ist nicht erforderlich. Bei R2 werden die fünf Einträge
  textuell aktualisiert (Folgearbeit-Trigger umformuliert
  auf `wand`-Aggregat-Mitgliedschaft).
