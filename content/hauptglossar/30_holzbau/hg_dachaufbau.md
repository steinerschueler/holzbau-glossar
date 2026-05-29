---
id: dachaufbau
benennung: Dachaufbau
synonyme: [Dacheindeckungsschichten]
abgelehnte_benennungen: [Dachhaut, Dachpaket, "roof build-up", "roof assembly"]
oberbegriff: null
begriffstyp: aggregat
voraussetzungen: [dachflaeche, dachhaut, toleranzen]
abgrenzung_zu: [dachflaeche, dachhaut, dach, tragwerk, eindeckung, unterdach, waermedaemmung, dampfbremse, konterlattung, traglattung]
status: entwurf
subglossar_pendant: notwendig
quellen_primär:
  - "SIA 232/1:2020 'Geneigte Dächer', Schweizerischer Ingenieur- und Architektenverein, Abschnitt 2 (Aufbau geneigter Dächer)."
  - "SIA 271:2007 'Abdichtungen von Hochbauten', Abschnitt 2 (Schichtenfolge bei Flachdächern)."
  - "DIN 18531-1:2017-07 'Abdichtung von Dächern – Teil 1', Abschnitt 5 (Schichtenfolge)."
  - "DIN 4108-3:2018-10 'Wärmeschutz und Energie-Einsparung in Gebäuden – Teil 3: Klimabedingter Feuchteschutz', Abschnitt 5 (Bauteilanforderungen Dach)."
quellen_sekundär:
  - "Lignum (Hrsg.): Lignatec 'Geneigte Dächer in Holzbauweise', Lignum, Zürich, aktuelle Auflage, Kap. 'Schichtaufbau'."
  - "Lignum (Hrsg.): Holzbautabellen HBT, Lignum, Zürich, Kap. 'Dachaufbau'."
  - "Mönck, W.; Rug, W.: Holzbau – Bemessung und Konstruktion. 16. Aufl., Beuth Verlag 2015, Kap. 'Dachaufbau'."
  - "Gerner, M.: Fachwerk. DVA, 7. Aufl. 2007, Glossar 'Dachaufbau'."
quellenkonflikt: |
  Im umgangssprachlichen Gebrauch wird „Dachhaut" häufig auf den
  gesamten Schichtaufbau ausgedehnt; in normativen Quellen (MBO,
  DIN 18531, SIA 232/1) ist „Dachhaut" jedoch enger gefasst (siehe
  Eintrag `dachhaut`). Der korrekte Sammelbegriff für die gesamte
  Schichtfolge oberhalb des Tragwerks ist `dachaufbau` bzw.
  synonym `dacheindeckungsschichten`. Diese Wahl folgt SIA 232/1
  und DIN 18531 und ist mit allen konsultierten Quellen verträglich.

  Ein Oberbegriff `bauteil_aggregat` existiert im Glossar noch
  nicht. Bis zu dessen Einführung wird `oberbegriff: null` gesetzt
  (analog zu `dach`, `ebene`, `toleranzen`).

  Begriffstyp: `aggregat` ist eindeutig — der Dachaufbau ist eine
  geordnete, partitive Zusammenfassung mehrerer Schicht-Bauteile.
---

## Prosa-Definition

Ein **Dachaufbau** ist die geordnete, materielle Schichtfolge eines
Daches oberhalb des Tragwerks bis einschließlich der äußersten
wettertrennenden Schicht, deren obere Hüllfläche die Dachhaut bildet.

## Mathematische Definition

Sei

- 𝒟 = { D₁, …, D_m } mit m ≥ 1 eine endliche, nicht-leere Familie
  von Dachflächen D_i = (E_i, P_i, n_{a,i}) im Sinne von
  `dachflaeche` (geometrische Auflagefläche des Aufbaus),
- F := ⋃_{i=1..m} F(P_i) ⊂ ℝ³ der Trägerbereich,
- 𝒮 = (S₁, S₂, …, S_k) mit k ≥ 1 eine endlich indizierte, von **innen
  nach außen** geordnete Folge von Schicht-Bauteilen, wobei jede
  Schicht S_j durch
  - ein Material m_j (Identifikator; eigener Eintrag `material`
    folgt),
  - eine Dicke d_j ∈ ℝ_{>0} (in mm),
  - eine Funktionsklasse f_j ∈ { Dampfbremse, Wärmedämmung,
    Schalung, Unterdach, Konterlattung, Traglattung, Eindeckung,
    Trennlage, sonstige }
  beschrieben ist, und
- die letzte (äußerste) Schicht S_k die Funktionsklasse Eindeckung
  (geneigtes Dach) bzw. Abdichtung (Flachdach) trägt.

Dann ist der **Dachaufbau** das Tripel

```
A := (𝒟, 𝒮, H)
```

mit

- 𝒟 als geometrischer Auflagefläche,
- 𝒮 als geordneter Schichtfolge,
- H der **Dachhaut** des Daches im Sinne von `dachhaut` als
  geometrischer Hüllfläche über S_k,

und den Konsistenzbedingungen

1. **Trägerbezug**: Alle Schichten S_j sind über F definiert.
2. **Reihenfolge**: Die Indizierung 1, …, k geht von innen
   (tragwerksseitig, j = 1) nach außen (wetterseitig, j = k).
3. **Positive Schichtdicken**: d_j > Toleranzen.LAENGE_EPS für alle j.
4. **Außenabschluss**: f_k ∈ { Eindeckung, Abdichtung }.
5. **Konsistenz mit Dachhaut**: Die Dachhaut H ist die obere
   Hüllfläche der Punktwolke der Außenseite von S_k (siehe
   `dachhaut`).

Die **Gesamtdicke** des Dachaufbaus ist

```
d_A := Σ_{j=1..k} d_j   (in mm).
```

## Wohldefiniertheit

- **Existenz**: Für jede nicht-leere Dachflächen-Familie 𝒟 und jede
  nicht-leere Schichtfolge 𝒮 mit positiven Dicken und gültigem
  Außenabschluss ist A wohldefiniert.
- **Eindeutigkeit der Reihenfolge**: 𝒮 ist eine Liste, keine Menge.
  Reihenfolge ist Bestandteil der Definition.
- **Konsistenz mit `dachhaut`**: Die Dachhaut H ist nicht
  unabhängig wählbar, sondern aus 𝒮 (insbesondere aus S_k)
  ableitbar. Sie wird im Eintrag `dachhaut` als obere Hüllfläche
  der Eindeckungs-/Abdichtungs-Punktwolke definiert. Die hier
  notierte Komponente H im Tripel A ist deshalb redundant
  (abgeleitet) und dient nur der expliziten Verfügbarkeit.
- **Konsistenz mit `dachflaeche`**: Die Dachfläche ist die
  geometrische Bezugsebene; der Dachaufbau ist die materielle
  Schichtfolge darüber. Beide sind streng getrennt.
- **Variabilität der Reihenfolge**: Die übliche Reihenfolge im
  geneigten Holzdach ist (von innen nach außen): Innenbekleidung
  (außerhalb der Definition) – Dampfbremse – Wärmedämmung –
  Schalung (optional) – Unterdach – Konterlattung – Traglattung –
  Eindeckung. Die Definition fordert nur Geordnetheit und einen
  gültigen Außenabschluss; abweichende, normgerechte Reihenfolgen
  (z. B. Aufsparrendämmung mit anderer Schichtreihenfolge) sind
  zugelassen, solange Bedingung 4 erfüllt ist.
- **Nicht-Zirkularität**: Die Definition verwendet die Primitive
  Punkt, Vektor, Strecke sowie die bereits definierten Begriffe
  `dachflaeche`, `dachhaut`. Sie verweist auf einzelne Schicht-
  Begriffe (`unterdach`, `dampfbremse`, …) nur erläuternd, nicht
  definitorisch — diese werden über die Funktionsklasse f_j
  parametrisch eingeführt.

## Erläuterung (nicht normativ)

Der Dachaufbau ist die **materielle Substanz des Daches oberhalb
des Tragwerks**. Er erfüllt die bauphysikalischen Funktionen
(Wärmeschutz, Feuchteschutz, Wind- und Wetterabwehr, Schallschutz,
Brandschutz). Die Dachhaut als geometrische Hüllfläche liegt über
ihm; das Tragwerk als lastabtragende Holzkonstruktion liegt unter
ihm.

Typische Schichtfolge eines geneigten Daches in Holzbauweise (von
innen nach außen, exemplarisch nach SIA 232/1 und Lignatec):

1. **Dampfbremse** (raumseitig, dampfdiffusionshemmend).
2. **Wärmedämmung** (Mineralwolle, Holzfaser, Zellulose, EPS).
3. **Schalung** (Holzschalung, OSB) — optional, je nach Aufbau.
4. **Unterdach / Unterdeckbahn** (zweite wasserführende Ebene).
5. **Konterlattung** (Längshölzer entlang der Sparren, schaffen
   die Hinterlüftungsebene).
6. **Traglattung** (Querlatten als Auflager der Eindeckung).
7. **Eindeckung** (Ziegel, Schindeln, Blech) — äußerste Schicht.

Bei Flachdächern entfallen Konter-/Traglattung und Eindeckung;
stattdessen tritt eine **Abdichtung** (Bitumenbahn,
Polymerbahn, Folie, Flüssigkunststoff) als äußerste Schicht auf.

**Hinweis zu Plattenwerkstoffen**: Einzelne Schichten können
Plattenwerkstoffe enthalten (z. B. OSB-Schalung, Holzschalung als
Unterdach, Holzfaser-Unterdachplatten). Für solche Schichten sind
**Faserrichtung** und **Seitenorientierung** im Allgemeinen nicht
über die ganze Schicht hinweg garantiert, sondern variieren
plattenweise. Die geometrische und mechanische Modellierung
einzelner Plattenelemente ist Gegenstand späterer Glossareinträge
(`plattenwerkstoff`, `holzschalung`, `osb`).

Der Begriff `dacheindeckungsschichten` ist im Branchenvokabular
ebenfalls etabliert, insbesondere wenn Architekt und Dachdecker
über das gesamte Schichtenpaket sprechen.

## Beziehungen

- **Oberbegriff**: derzeit `null`. Künftig `bauteil_aggregat`
  (analog zu `dach`).
- **Bestandteile (partitiv, geordnet)**: die Schichten S₁, …, S_k.
  Einzelne Schichten erhalten eigene Glossareinträge:
  `dampfbremse`, `waermedaemmung`, `schalung`, `unterdach`,
  `konterlattung`, `traglattung`, `eindeckung`,
  ggf. `dachabdichtung`.
- **Verwendung**:
  - Bestandteil eines `dach` (partitive Beziehung).
  - Trägermaterial der Dachhaut (`dachhaut`): die obere Hüllfläche
    der äußersten Schicht S_k bildet die Dachhaut.
- **Abgrenzung**:
  - **Dachhaut** (`dachhaut`): geometrische Hüllfläche **über**
    dem Dachaufbau. Nicht das Schichtenpaket selbst, sondern die
    fiktive obere Außenfläche. Im Sprachgebrauch oft mit dem
    Dachaufbau verwechselt — siehe Quellenkonflikt im
    Eintrag `dachhaut`.
  - **Dachfläche** (`dachflaeche`): geometrische Bezugsebene
    **unter** dem Dachaufbau (auf der die innerste Schicht
    aufliegt). Dickenlos, keine Materialeigenschaften.
  - **Tragwerk** (`tragwerk`, eigener Eintrag folgt): die
    lastabtragende Holzkonstruktion (Sparren, Pfetten, Binder)
    **unter** dem Dachaufbau. Der Dachaufbau ist nicht selbst
    tragend, sondern wird vom Tragwerk getragen.
  - **Dach** (`dach`): das Gesamtaggregat aus Tragwerk,
    Dachflächen und Dachaufbau (mit der Dachhaut als oberer
    Hüllfläche).
  - **Eindeckung** (`eindeckung`, bereits angelegt): nur die
    äußerste Schicht eines geneigten Dachaufbaus, nicht der
    gesamte Aufbau.
  - **Unterdach, Wärmedämmung, Dampfbremse, Konterlattung,
    Traglattung**: einzelne Schichten innerhalb des Dachaufbaus,
    je mit eigenem Glossareintrag (folgen).

## Implementierungshinweis

Datentyp (Domänen-Schicht, Kotlin, Schicht `domain.bauteil`):

```
data class Dachaufbau(
    val dachflaechen: List<Dachflaeche>,    // 𝒟, geometrische Auflage
    val schichten: List<Schicht>            // 𝒮, von innen nach außen
) {
    init {
        // 1. dachflaechen.isNotEmpty()           → sonst Entartet.LeerTraeger
        // 2. schichten.isNotEmpty()              → sonst Entartet.LeererAufbau
        // 3. ∀ s ∈ schichten: s.dicke > Toleranzen.LAENGE_EPS
        //                                         → sonst Entartet.NullDickeSchicht
        // 4. schichten.last().funktion ∈
        //      { EINDECKUNG, ABDICHTUNG }        → sonst Entartet.KeinAussenabschluss
    }

    fun gesamtdicke(): Double = schichten.sumOf { it.dicke }   // mm
    fun aussenschicht(): Schicht = schichten.last()
    fun innenschicht(): Schicht = schichten.first()

    fun dachhaut(): Dachhaut = Dachhaut.ausAussenschicht(this)
}

data class Schicht(
    val material: MaterialId,         // Platzhalter, eigener Typ folgt
    val dicke: Double,                // mm, > 0
    val funktion: SchichtFunktion
)

enum class SchichtFunktion {
    DAMPFBREMSE, WAERMEDAEMMUNG, SCHALUNG, UNTERDACH,
    KONTERLATTUNG, TRAGLATTUNG, EINDECKUNG, ABDICHTUNG,
    TRENNLAGE, SONSTIGE
}
```

- **Einheit**: Schichtdicken in mm (Double).
- **Invarianten** (in `init` prüfen, bei Verletzung
  `Resultat.Fehler` bzw. `Entartet`-Variante zurückgeben, niemals
  Exception werfen):
  1. `dachflaechen.isNotEmpty()` ⇒ sonst `Entartet.LeerTraeger`.
  2. `schichten.isNotEmpty()` ⇒ sonst `Entartet.LeererAufbau`.
  3. Jede Schichtdicke d_j > Toleranzen.LAENGE_EPS ⇒ sonst
     `Entartet.NullDickeSchicht`.
  4. Funktion der äußersten Schicht ∈
     { EINDECKUNG, ABDICHTUNG } ⇒ sonst
     `Entartet.KeinAussenabschluss`.
  5. **Optional/konfigurierbar**: bauphysikalische
     Plausibilität (Dampfbremse warmseitig der Wärmedämmung,
     Konterlattung unter Traglattung). Kein harter Fehler,
     sondern Warnung über `dachaufbau.validierePlausibilitaet():
     List<Hinweis>`.
- **Edge Cases**:
  - **Einlagig** (k = 1, nur Eindeckung): zulässig (z. B.
    historischer Stadel ohne Dämmung). Dachaufbau besteht dann
    aus einer einzigen Schicht.
  - **Sehr dünne Folienschichten** (Dampfbremse, d ≈ 0,2 mm):
    Toleranz LAENGE_EPS = 1·10⁻³ mm ist hinreichend klein, um
    auch sehr dünne Schichten als positive Dicke zu erkennen.
  - **Mehrere Dachflächen mit unterschiedlichem Aufbau** (z. B.
    Hauptdach gedämmt, Vordach ungedämmt): werden als
    **getrennte** `Dachaufbau`-Instanzen modelliert, jeweils mit
    der zugehörigen Teilmenge der Trägerflächen.
  - **Plattenwerkstoffe** (OSB, Holzschalung, Holzfaserplatten):
    werden auf dieser Aggregations-Ebene als Schicht mit
    konstanter Dicke modelliert. Die Geometrie einzelner Platten
    inkl. Faserrichtung und Seitenorientierung wird in späteren
    Glossareinträgen behandelt.
  - **Schichten mit nicht-konstanter Dicke** (Aufdoppelungen,
    Gefälledämmung): nicht von dieser Definition abgedeckt;
    erfordern eine spätere Erweiterung mit Schichtdicken-Funktion
    d_j(p) statt Skalar.
  - **Flachdach** (alle α_i ≈ 0): zulässig; äußerste Schicht ist
    typischerweise eine ABDICHTUNG, nicht eine EINDECKUNG.
- **Abgeleitete Eigenschaften** (als Funktionen, keine Felder):
  - `gesamtdicke(): Double` (mm) = Σ d_j.
  - `aussenschicht(): Schicht` = `schichten.last()`.
  - `innenschicht(): Schicht` = `schichten.first()`.
  - `dachhaut(): Dachhaut` = obere Hüllfläche der Außenseite von
    `aussenschicht()`.

## Quellen

**Primär (normativ):**

- SIA 232/1:2020, „Geneigte Dächer", Schweizerischer Ingenieur-
  und Architektenverein, Abschnitt 2.
- SIA 271:2007, „Abdichtungen von Hochbauten", Schweizerischer
  Ingenieur- und Architektenverein, Abschnitt 2.
- DIN 18531-1:2017-07, „Abdichtung von Dächern – Teil 1",
  Abschnitt 5.
- DIN 4108-3:2018-10, „Wärmeschutz und Energie-Einsparung in
  Gebäuden – Teil 3", Abschnitt 5.

**Sekundär:**

- Lignum (Hrsg.): *Lignatec — Geneigte Dächer in Holzbauweise.*
  Lignum, Zürich, aktuelle Auflage.
- Lignum (Hrsg.): *Holzbautabellen HBT.* Lignum, Zürich,
  aktuelle Auflage.
- Mönck, W.; Rug, W.: *Holzbau – Bemessung und Konstruktion.*
  15. Auflage, Beuth Verlag 2015.
- Gerner, M.: *Fachwerk – Instandsetzung, Sanierung, Neubau.*
  DVA, 7. Auflage 2007.
