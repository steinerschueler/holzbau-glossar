---
id: dach
benennung: Dach
synonyme: [Bedachung]
abgelehnte_benennungen: [Dachstuhl, Dachkonstruktion, Dachwerk, "roof"]
oberbegriff: null
begriffstyp: aggregat
voraussetzungen: [tragwerk, dachflaeche, dachaufbau, dachhaut, toleranzen]
abgrenzung_zu: [dachflaeche, dachaufbau, dachhaut, dachstuhl, tragwerk, dachform, dachkonstruktion, gebaeudehuelle, bauwerk]
status: entwurf
theorie_pflichtig: required
quellen_primär:
  - "SIA 232/1:2020 'Geneigte Dächer', Schweizerischer Ingenieur- und Architektenverein, Abschnitt 1 (Begriffe und geometrische Grundlagen)."
  - "DIN 18531-1:2017-07, 'Abdichtung von Dächern sowie von Balkonen, Loggien und Laubengängen – Teil 1', Abschnitt 3 (Begriffe)."
  - "DIN EN 1995-1-1:2010-12 (Eurocode 5), Abschnitt 1.5 (Begriffe), für 'Dachtragwerk' als statisch-konstruktive Teilkomponente."
  - "Musterbauordnung (MBO) 2002, § 32 (Dächer)."
quellen_sekundär:
  - "Mönck, W.; Rug, W.: Holzbau – Bemessung und Konstruktion. 16. Aufl., Beuth Verlag 2015, Kap. 'Dachtragwerke'."
  - "Gerner, M.: Fachwerk – Instandsetzung, Sanierung, Neubau. DVA, 7. Aufl. 2007, Glossar 'Dach' und 'Dachstuhl'."
  - "Lignum (Hrsg.): Holzbautabellen HBT, Lignum, Zürich, aktuelle Auflage, Kap. 'Dachaufbau'."
  - "NIhK Glossary of Prehistoric and Historic Timber Buildings, Lemma 'roof'."
  - "Wikipedia, Lemma 'Dach' (abgerufen 2026-05-08) — als Korpusbeleg, nicht als Autorität."
quellenkonflikt: |
  Weder DIN 1052 / DIN EN 1995-1-1 noch SIA 265 enthalten einen
  geschlossenen Begriffseintrag „Dach"; sie verwenden ihn vorausgesetzt
  und definieren stattdessen Teilkomponenten (Dachtragwerk, Dachscheibe).
  DIN 18531 und SIA 232/1 verwenden „Dach" funktional („oberer
  raumabschließender Bauteil"), ohne eine geschlossene mathematische
  Definition zu geben. Im Fachsprachgebrauch (Gerner, Lignum, NIhK)
  wird „Dach" außerdem teils synonym mit „Dachstuhl" (= Tragwerk),
  teils synonym mit „Dachkonstruktion" (= Tragwerk + Dachhaut)
  verwendet — die Quellen sind hier unscharf.

  Eigene Festlegung in diesem Glossar (folgt der Domain-Expert-Hierarchie
  und ist konsistent mit DIN 18531, SIA 232/1, MBO):

  - **Tragwerk**: lastableitende Bauteile (Sparren, Pfetten, Binder).
  - **Dachflächen**: geometrische Bezugsebenen, polygonal begrenzt.
  - **Dachaufbau**: alle materiellen Schichten oberhalb des Tragwerks
    (Dampfbremse, Dämmung, Unterdach, Konterlattung, Traglattung,
    Eindeckung bzw. Abdichtung).
  - **Dachhaut**: ausschließlich die äußerste, fiktive Hüllfläche
    über der Eindeckung bzw. Abdichtung — geometrisch, nicht
    materiell.

  Damit ist Dach das Aggregat aus Tragwerk, Dachflächen-Familie und
  Dachaufbau (die Dachhaut ist abgeleitete Größe des Dachaufbaus,
  nicht selbst Bestandteil des Tripels). „Dachstuhl" wird als enger
  gefasster Begriff (nur Tragwerk) ausdrücklich nicht als Synonym
  geführt; eigener Eintrag folgt.

  Ein Oberbegriff `bauteil` bzw. `bauteil_aggregat` existiert im
  Glossar noch nicht. Bis zu dessen Einführung wird `oberbegriff: null`
  gesetzt; eine Eingliederung erfolgt, sobald dieser Eintrag angelegt
  ist (analog zu `ebene` und `toleranzen`).

  Der Eintrag `tragwerk` ist als Voraussetzung gelistet, aber selbst
  noch nicht definiert. Die formale Auflager-Relation wird mit dem
  späteren Eintrag `tragwerk` nachgeliefert.
---

## Prosa-Definition

Ein **Dach** ist das oberste raumabschließende Bauteil-Aggregat eines
Gebäudes, bestehend aus einem **Tragwerk** (lastabtragende
Holzkonstruktion), einer endlichen, nicht-leeren Familie von
**Dachflächen** (geometrische Bezugsebenen) und einem **Dachaufbau**
(geordnete Schichtfolge oberhalb des Tragwerks bis einschließlich der
äußersten wettertrennenden Schicht), wobei die obere Hüllfläche des
Dachaufbaus die **Dachhaut** des Daches bildet.

## Mathematische Definition

Sei

- T eine endliche Menge konstruktiver Tragwerks-Bauteile (Sparren,
  Pfetten, Binder, Kehlbalken, Aussteifungen, Verbindungsmittel; im
  aktuellen Glossarstand als Sammelbegriff geführt; eigener Eintrag
  `tragwerk` folgt),
- 𝒟 = { D₁, …, D_m } mit m ≥ 1 eine endliche, nicht-leere Familie
  von Dachflächen D_i = (E_i, P_i, n_{a,i}) im Sinne von
  `dachflaeche`,
- A ein Dachaufbau im Sinne von `dachaufbau`, definiert über dem
  Trägerbereich F := ⋃_{i=1..m} F(P_i),
- H = H(A) die aus A abgeleitete Dachhaut im Sinne von `dachhaut`
  (obere Hüllfläche der äußersten Schicht von A).

Dann ist ein **Dach** das Tripel

```
Dach := (T, 𝒟, A)
```

mit den Konsistenzbedingungen

1. **Trägerbezug des Dachaufbaus**: Der Dachaufbau A ist genau
   über F := ⋃_i F(P_i) definiert, d. h. seine Trägerflächen sind
   die Elemente von 𝒟.
2. **Statische Auflagerung der Dachflächen**: Jede Dachfläche
   D_i ∈ 𝒟 wird konstruktiv von Elementen aus T getragen
   (im aktuellen Glossarstand als zugesicherte Konsistenzbedingung,
   nicht als formal überprüfbares Prädikat — die formale Auflager-
   Relation wird mit dem späteren Eintrag `tragwerk` nachgeliefert).
3. **Geschlossenheit der Hülle nach oben**: Der gerichtete
   Halbraum-Verband H⁺ := ⋃_i { x | ⟨n_{a,i}, x − p_{0,i}⟩ > 0 }
   ist die nach außen weisende Seite des Daches. Es existiert kein
   Punkt im umbauten Raum, der durch eine vertikale Halbgerade nach
   oben den Verband ⋃_i F(P_i) verfehlt (Wohldefiniertheit der
   Funktion „raumabschließend nach oben").

Der **geometrische Anteil** des Daches ist die durch 𝒟 erzeugte
Punktmenge

```
G(Dach) := ⋃_{i=1..m} F(P_i) ⊂ ℝ³,
```

die **äußere Hüllfläche** des Daches ist die Dachhaut H = H(A).

## Wohldefiniertheit

- **Existenz**: Für jedes konkrete Bauwerk mit T ≠ ∅, 𝒟 ≠ ∅ und
  einem wohldefinierten Dachaufbau A über F = ⋃ F(P_i) ist das
  Tripel (T, 𝒟, A) ein Dach. Bauliche Mindestkonfiguration:
  m = 1 (Pultdach mit einer Dachfläche), k = 1 (einlagiger Aufbau).
- **Eindeutigkeit der Komponentenzuordnung**: Aus einem gegebenen
  Bauwerk lassen sich T, 𝒟 und A eindeutig extrahieren, wenn die
  Klassifikation der einzelnen Bauteile nach ihrer Rolle (Tragwerk
  vs. Dachfläche-Geometrie vs. Dachaufbau-Schicht) festgelegt ist.
  Die Klassifikation selbst ist Modellierungsentscheidung der
  Domänen-Schicht.
- **Eindeutigkeit der Dachhaut**: H = H(A) ist durch A vollständig
  bestimmt (siehe Eintrag `dachhaut`); die Dachhaut tritt im
  Tripel nicht zusätzlich auf, sondern wird als abgeleitete
  Größe verfügbar gemacht (`dach.dachhaut()`).
- **Unabhängigkeit von der Reihenfolge**: 𝒟 ist als Menge
  unsortiert; alle Aussagen über das Dach sind invariant unter
  Permutation der Dachflächen. Der Dachaufbau A hingegen besitzt
  eine geordnete Schichtfolge — die Permutation seiner Schichten
  ändert das Bauteil.
- **Konsistenz mit `dachflaeche`**: Der Eintrag `dachflaeche`
  schließt α = π/2 aus; damit ist G(Dach) keine vertikale Wand und
  Bedingung 3 sinnvoll formulierbar. Der Grenzfall α = 0
  (Flachdach mit m = 1) ist zulässig und erfüllt Bedingung 3 trivial.
- **Nicht-Zirkularität**: Die Definition verwendet nur die
  Primitive Punkt, Vektor, Halbraum, das Aggregat-Konzept und die
  bereits definierten Begriffe `dachflaeche`, `dachaufbau`,
  `dachhaut`. Sie verweist auf `tragwerk` als bislang noch nicht
  definierten Sammelbegriff — diese Abhängigkeit ist im
  Frontmatter als `voraussetzung` geführt; die formale Auflager-
  Relation wird nachgereicht.

## Erläuterung (nicht normativ)

Ein Dach ist im Sinne dieses Glossars kein einzelnes geometrisches
Objekt, sondern ein **Container** mit drei Schichten von
Begriffen:

1. **Tragwerk** (statisch, materiell): die lastabtragende
   Holzkonstruktion (Sparren, Pfetten, Binder, Kehlbalken,
   Stuhlsäulen, Aussteifungen). Im traditionellen Sprachgebrauch
   der Zimmerleute als „Dachstuhl" bezeichnet.
2. **Dachflächen** (geometrisch, dickenlos): die ebenen,
   polygonal begrenzten Bezugsflächen, an denen sich Form und
   Neigung des Daches ausdrücken (siehe `dachflaeche`).
3. **Dachaufbau** (materiell, geschichtet): die Schichtfolge
   oberhalb des Tragwerks (Dampfbremse, Wärmedämmung, Unterdach,
   Konterlattung, Traglattung, Eindeckung — siehe `dachaufbau`).
   Seine obere Hüllfläche ist die **Dachhaut** (geometrische
   Außenfläche des Daches, siehe `dachhaut`).

Form-Klassen (Sattel, Walm, Pult, Mansarde, Krüppelwalm, Zelt)
ergeben sich aus der Konfiguration der Dachflächen-Familie 𝒟 und
sind ein **Klassifikationsmerkmal**, kein eigener Bauteil-Begriff.

Die saubere Trennung **Geometrie / Material / Hüllfläche** dieses
Glossars (Dachfläche / Dachaufbau / Dachhaut) löst die in der
Fachliteratur verbreitete Vermischung dieser drei Konzepte auf.

## Beziehungen

- **Oberbegriff**: derzeit `null`. Künftig `bauteil_aggregat`
  (oberste Aggregatklasse für Bauteile, die selbst aus mehreren
  Bauteilen bestehen). Eintrag wird angelegt, sobald weitere
  Aggregate (Wandaufbau, Deckenaufbau) hinzukommen.
- **Bestandteile (partitiv)**:
  - **Tragwerk** (`tragwerk`, eigener Eintrag folgt): Sparren,
    Pfetten, Binder, Kehlbalken, Aussteifungen,
    Verbindungsmittel.
  - **Dachflächen** (`dachflaeche`): geometrische Bezugsebenen.
  - **Dachaufbau** (`dachaufbau`): materielle Schichtfolge.
  - **Dachhaut** (`dachhaut`, abgeleitet): obere Hüllfläche
    des Dachaufbaus.
- **Spezialisierungen nach Dachform**: siehe `hg_dachform.md` für
  den vollständigen Werte-Katalog (zwölf Formen plus Freiform:
  Flach-, Pult-, Sattel-, Walm-, Krüppelwalm-, Zelt-, Mansard-,
  Schmetterlings-, Shed-, Tonnen-, Bogen-, Trogdach + Freiform).
  Eigene HG-Einträge für die einzelnen Werte folgen trigger-basiert
  je nach erstem Tool-Bedarf.
- **Abgrenzung**:
  - **Dachfläche** (`dachflaeche`): rein geometrischer
    Bestandteil eines Daches, kein Aggregat. Ein Dach hat eine
    oder mehrere Dachflächen; eine Dachfläche ist nicht das Dach.
  - **Dachaufbau** (`dachaufbau`): die materielle Schichtfolge
    oberhalb des Tragwerks. Bestandteil eines Daches, nicht das
    Dach selbst.
  - **Dachhaut** (`dachhaut`): die geometrische Hüllfläche
    **über** dem Dachaufbau. Aus dem Dachaufbau abgeleitet, nicht
    eigenständiges Bauteil.
  - **Dachstuhl** (umgangssprachlich): in der
    zimmermannssprachlichen Tradition meist nur das **Tragwerk**.
    Wegen der schwankenden Verwendung in Fachglossaren
    ausdrücklich **nicht** als Synonym geführt; eigener Eintrag
    `dachstuhl` (= Tragwerk) folgt.
  - **Tragwerk** (Dachtragwerk): Bestandteil des Daches, nicht
    das Dach selbst. Eigener Eintrag folgt.
  - **Dachform** (Sattel-, Walm-, Pultdach …): ein
    Klassifikationsmerkmal eines Daches, kein eigenständiges
    Bauteil. Wird als Aufzählungs-Typ modelliert.
  - **Dachkonstruktion**: in DIN/SIA uneinheitlich verwendet,
    mal synonym zu Tragwerk, mal synonym zum hier definierten
    Dach. Wegen Mehrdeutigkeit kein Synonym.
  - **Bedachung**: zulässiges Synonym im Sinne „das Dach als
    Gesamtheit". In Fachsprache eher nordwestdeutsch; in der
    Schweiz selten.
  - **Gebäudehülle**: das gesamte raumabschließende
    Hüllaggregat (Dach + Außenwände + Bodenplatte).
    Übergeordneter Aggregatbegriff, nicht Synonym.

## Implementierungshinweis

Datentyp (Domänen-Schicht, Kotlin, Schicht `domain.bauteil`):

```
data class Dach(
    val tragwerk: Tragwerk,                  // T, eigener Typ folgt
    val dachflaechen: List<Dachflaeche>,     // 𝒟, Reihenfolge bedeutungslos
    val dachaufbau: Dachaufbau               // A
) {
    init {
        // 1. dachflaechen.isNotEmpty()                  → sonst Entartet.LeeresDach
        // 2. dachaufbau.dachflaechen entspricht
        //    dachflaechen (gleicher Trägerbereich)      → sonst Entartet.AufbauTraegerInkonsistent
        // 3. Kein flächiger Selbstüberlapp der Dachflächen
        //    außer entlang gemeinsamer Ränder
        //    (First, Grat, Kehle)                       → sonst Entartet.SelbstUeberlapp
    }

    fun dachhaut(): Dachhaut = dachaufbau.dachhaut()
}
```

- **Einheit**: alle Geometrie-Komponenten in mm; Dachneigungen
  intern in Radiant.
- **Invarianten** (in `init` prüfen, bei Verletzung
  `Resultat.Fehler` bzw. `EntartetGeometrie`-Variante zurückgeben, niemals
  Exception werfen):
  1. `dachflaechen.isNotEmpty()` ⇒ sonst `Entartet.LeeresDach`.
  2. Trägerbereich des Dachaufbaus deckt sich mit
     `dachflaechen` bis auf Toleranzen.LAENGE_EPS am Rand;
     Verletzung ⇒ `Entartet.AufbauTraegerInkonsistent`.
  3. Paarweise Dachflächen-Schnitte sind entweder leer oder
     bestehen aus gemeinsamen Randstrecken (First, Grat, Kehle);
     ein flächiger Selbstüberlapp ist verboten ⇒
     `Entartet.SelbstUeberlapp`.
  4. Auflagerung jeder D_i ∈ 𝒟 durch Elemente aus T;
     Verletzung ⇒ `Entartet.NichtAufgelagert` (formal nachgeliefert,
     sobald `tragwerk` definiert ist).
- **Edge Cases**:
  - **Pultdach** (m = 1): zulässig.
  - **Flachdach** (alle α_i ≤ Toleranzen.WINKEL_EPS): zulässig,
    Sonderfall der Definition; Außenabschluss des Dachaufbaus
    typischerweise eine ABDICHTUNG.
  - **Mehrere getrennte Dächer auf einem Gebäude** (z. B. zwei
    Satteldachflügel mit Lichthof dazwischen): werden als zwei
    getrennte `Dach`-Instanzen modelliert, nicht als ein einziges
    Dach mit nicht-zusammenhängender Dachflächen-Familie.
  - **Aufbauten** (Gauben, Schornsteindurchführungen): die
    Gaubenflächen sind eigenständige Dachflächen in 𝒟, die
    Schornsteindurchführung ist eine lokale Aussparung in
    Dachfläche und Dachaufbau (Modellierung in späterem Eintrag
    `dachoeffnung`).
- **Abgeleitete Eigenschaften** (als Funktionen, keine Felder):
  - `geometrischerAnteil(): Geometrie` = Vereinigung der F(P_i).
  - `gesamtflaeche(): Double` (mm²) = Σ flaecheninhalt(D_i).
  - `dachform(): Dachform` = Klassifikation aus Anzahl,
    Neigungen und Topologie der D_i (eigener Eintrag `dachform`
    folgt).
  - `dachhaut(): Dachhaut` = abgeleitete Hüllfläche aus
    `dachaufbau`.
  - `enthaelt(p: Punkt, eps): Boolean` = ∃ D_i ∈ 𝒟 mit
    `D_i.enthaelt(p, eps)`.

## Quellen

**Primär (normativ):**

- SIA 232/1:2020, „Geneigte Dächer", Schweizerischer Ingenieur-
  und Architektenverein, Abschnitt 1.
- DIN 18531-1:2017-07, „Abdichtung von Dächern sowie von
  Balkonen, Loggien und Laubengängen – Teil 1: Nicht genutzte
  und genutzte Dächer – Anforderungen, Planungs- und
  Ausführungsgrundsätze", Abschnitt 3.
- DIN EN 1995-1-1:2010-12, „Eurocode 5: Bemessung und
  Konstruktion von Holzbauten – Teil 1-1: Allgemeines",
  Abschnitt 1.5.
- Musterbauordnung (MBO) 2002, § 32.

**Sekundär:**

- Mönck, W.; Rug, W.: *Holzbau – Bemessung und Konstruktion.*
  16. Auflage, Beuth Verlag 2015.
- Gerner, M.: *Fachwerk – Instandsetzung, Sanierung, Neubau.*
  DVA, 7. Auflage 2007.
- Lignum (Hrsg.): *Holzbautabellen HBT.* Lignum, Zürich, aktuelle
  Auflage.
- NIhK: *Glossary of Prehistoric and Historic Timber Buildings.*

**Korpus (nicht autoritativ):**

- Wikipedia, Lemma „Dach" (abgerufen 2026-05-08).
