---
id: festigkeitsklasse
benennung: Festigkeitsklasse
synonyme: ["Sortierklasse (im Sinne der Festigkeit)", "Strength class", "characteristic strength class"]
abgelehnte_benennungen: [Güteklasse, Sortimentsklasse, Holzklasse, "stress class", "strength grade", Tragklasse]
oberbegriff: null
begriffstyp: merkmal
voraussetzungen: [werkstoff, produktkennzeichnung]
abgrenzung_zu: [werkstoff, produktkennzeichnung, faserrichtungs_modus, faserrichtung]
status: entwurf
subglossar_pendant: notwendig
quellen_primär:
  - "DIN EN 338:2016-07, 'Bauholz für tragende Zwecke – Festigkeitsklassen': C14, C16, C18, C20, C22, C24, C27, C30, C35, C40, C45, C50 (Nadelholz und Pappel); D18, D24, D27, D30, D35, D40, D50, D60, D70 (Laubholz)."
  - "DIN EN 14080:2013-09, 'Holzbauwerke – Brettschichtholz und Balkenschichtholz – Anforderungen': GL-Klassen GL20h–GL32h (homogen) und GL20c–GL32c (kombiniert) für BSH; GL20–GL30 für Balkenschichtholz."
  - "DIN EN 14081-1:2019-10, 'Holzbauwerke – Nach Festigkeit sortiertes Bauholz mit rechteckigem Querschnitt – Teil 1: Allgemeine Anforderungen' (Festigkeitsklassen-Zuordnung über visuelle und maschinelle Sortierung)."
  - "DIN EN 14374:2005-02, 'Holzbauwerke – Furnierschichtholz für tragende Zwecke – Anforderungen' (LVL-Klassen über ETA, z. B. Kerto-S, Kerto-Q, BauBuche)."
  - "DIN EN 16351:2021-08, 'Holzbauwerke – Brettsperrholz – Anforderungen' (CLT-Klassifikation typisch über die Festigkeitsklasse jeder Lage, z. B. C24)."
  - "DIN EN 300:2006-09, 'Platten aus langen, schlanken, gerichteten Spänen (OSB)': Typ-Klassifikation OSB/1, OSB/2, OSB/3, OSB/4 (statt Festigkeitsklassen im engeren Sinn)."
  - "DIN EN 312:2010-12, 'Spanplatten – Anforderungen': Typ-Klassifikation P1, P2, P3, P4, P5, P6, P7."
  - "DIN EN 622-2:2004-08, 'Faserplatten – Anforderungen – Teil 2: Anforderungen an harte Platten' (HB)."
  - "DIN EN 622-3:2004-08, 'Faserplatten – Anforderungen – Teil 3: Anforderungen an mittelharte Platten' (MBH, MBL)."
  - "DIN EN 622-5:2010-01, 'Faserplatten – Anforderungen – Teil 5: Anforderungen an Platten nach dem Trockenverfahren (MDF)'."
  - "SIA 265:2021, 'Holzbau', Schweizerischer Ingenieur- und Architektenverein, Anhang A (Festigkeitsklassen-Tabellen, identisch zu EN 338 / EN 14080)."
  - "DIN 4074-1:2012-06, 'Sortierung von Holz nach der Tragfähigkeit – Teil 1: Nadelschnittholz' (Sortierklassen S7, S10, S13 → Festigkeitsklassen C16, C24, C30 nach Zuordnungstabelle)."
quellen_sekundär:
  - "Blass, H. J.; Sandhaas, C.: Ingenieurholzbau – Grundlagen der Bemessung. KIT Scientific Publishing, Karlsruhe 2016, Kap. 2 (Werkstoff Holz, Festigkeitsklassen)."
  - "Mönck, W.; Rug, W.: Holzbau – Bemessung und Konstruktion. 16. Aufl., Beuth, Berlin 2015, Kap. 3 (Sortierung und Klassifikation)."
  - "Niemz, P.; Sonderegger, W.: Physik des Holzes und der Holzwerkstoffe. Hanser, München 2017, Kap. 6 (Festigkeitsklassen, charakteristische Werte)."
  - "Lignum (Hrsg.): Holzbautabellen HBT, Lignum, Zürich, aktuelle Auflage."
  - "Schickhofer, G.; Bogensperger, T.; Moosbrugger, T. (Hrsg.): BSPhandbuch — Holz-Massivbauweise in Brettsperrholz. 2. Aufl., TU Graz 2010 (CLT-Lagen-Festigkeitsklassen)."
quellenkonflikt: |
  Die normative Grundlage der Festigkeitsklassen ist werkstoff-
  spezifisch ausdifferenziert: Bauholz (EN 338), BSH (EN 14080), LVL
  (EN 14374, ETA), CLT (EN 16351), OSB (EN 300, Typ-Klassifikation),
  Spanplatte (EN 312, Typ-Klassifikation), Faserplatten (EN 622).
  EC5 und SIA 265 verwenden „Festigkeitsklasse" als Sammelbegriff,
  ohne eine werkstoff-übergreifende Aufzählung zu definieren.

  Eigene Festlegung in diesem Glossar:

  - Die **Festigkeitsklasse** ist im Glossar ein **werkstoff-
    spezifischer Aufzählungswert**, der in einer sealed-Hierarchie
    nach Werkstoff-Subklasse organisiert ist:
    - **Vollholz / KVH** (Nadelholz): C14, C16, C18, C20, C22, C24,
      C27, C30, C35, C40, C45, C50 (DIN EN 338).
    - **Laubholz**: D18, D24, D27, D30, D35, D40, D50, D60, D70
      (DIN EN 338).
    - **BSH (Glulam) homogen**: GL20h, GL22h, GL24h, GL26h, GL28h,
      GL30h, GL32h (DIN EN 14080).
    - **BSH kombiniert**: GL20c, GL22c, GL24c, GL26c, GL28c, GL30c,
      GL32c (DIN EN 14080).
    - **Balkenschichtholz** (BSc): GL20–GL30 (DIN EN 14080).
    - **LVL**: ETA-Klassen je Hersteller (Kerto-S, Kerto-Q,
      BauBuche, …).
    - **CLT/BSP**: typisch über Lagen-Festigkeitsklassen (jede Lage
      z. B. C24); Hersteller-spezifische Bauteilklassen über ETAs.
    - **OSB**: Typ-Klassifikation OSB/1, OSB/2, OSB/3, OSB/4
      (DIN EN 300) — keine Festigkeitsklasse im engeren Sinn,
      sondern Verwendungs-Typ.
    - **Spanplatte**: P1, P2, P3, P4, P5, P6, P7 (DIN EN 312) —
      Typ-Klassifikation.
    - **MDF**: Typ-Klassifikation nach DIN EN 622-5.
    - **HDF**: Typ-Klassifikation nach DIN EN 622-5 (hochdichte
      MDF).
    - **Harte Faserplatte (HB)**: DIN EN 622-2.
    - **Mittelharte Faserplatte (MBH, MBL)**: DIN EN 622-3.
  - Die OSB-, Spanplatten- und Faserplatten-„Festigkeitsklassen"
    sind streng genommen **Verwendungs-Typen**, nicht Festigkeits-
    klassen im engeren Sinn (DIN EN 338 / EN 14080). Sie werden im
    Glossar dennoch unter `festigkeitsklasse` geführt, weil sie die
    bemessungsrelevante Materialklassifikation des Werkstoffs sind
    und in EC5 / EN 12369-1 als Eingabe der charakteristischen
    Werte dienen.
  - Bei **Stahl** (siehe `werkstoff_stahl`) übernimmt die
    Stahlgüte (4.6, 5.6, 8.8, 10.9, A2-70, A4-70) die Rolle der
    Festigkeitsklasse; sie wird dort in einem eigenen Subtyp
    geführt.
---

## Prosa-Definition

Die **Festigkeitsklasse** eines Werkstoffs ist ein werkstoff-
spezifischer Aufzählungswert aus einer durch die jeweilige
Produktnorm (DIN EN 338 / 14080 / 14374 / 16351 / 300 / 312 / 622)
festgelegten endlichen Klassenfolge, der die bemessungsrelevanten
charakteristischen Festigkeits-, Steifigkeits- und Rohdichtewerte
des Werkstoffs in tabellierter Form (EN 1995-1-1, EN 12369-1,
SIA 265) eindeutig adressiert und zusammen mit der Werkstoff-
Subklasse die Bemessungseingabe vollständig charakterisiert.

## Mathematische Definition

Sei

- 𝓦 die Menge der Werkstoffe (siehe `werkstoff`),
- 𝓢 die Werkstoff-Subklassenmenge { axiales_holz, mehrlagenholz,
  gerichteter_plattenwerkstoff, isotroper_plattenwerkstoff,
  werkstoff_stahl }.

Dann ist die **Festigkeitsklasse** ein abhängiger Aufzählungstyp
über der Subklasse:

```
𝓕𝓚 := ⊎_{s ∈ 𝓢} 𝓕𝓚_s
```

mit den werkstoff-spezifischen Klassenmengen

```
𝓕𝓚_axiales_holz_C  := { C14, C16, C18, C20, C22, C24, C27, C30,
                         C35, C40, C45, C50 }              (DIN EN 338)
𝓕𝓚_axiales_holz_D  := { D18, D24, D27, D30, D35, D40, D50,
                         D60, D70 }                        (DIN EN 338)
𝓕𝓚_axiales_holz_GLh:= { GL20h, GL22h, GL24h, GL26h, GL28h,
                         GL30h, GL32h }                    (DIN EN 14080, BSH homogen)
𝓕𝓚_axiales_holz_GLc:= { GL20c, GL22c, GL24c, GL26c, GL28c,
                         GL30c, GL32c }                    (DIN EN 14080, BSH kombiniert)
𝓕𝓚_axiales_holz_LVL:= ETA-Klassen je Hersteller            (DIN EN 14374; offen)
𝓕𝓚_mehrlagenholz   := indirekt über Lagen-Festigkeitsklassen
                       jeder Lage (typisch C24) plus
                       Hersteller-Bauteilklasse via ETA    (DIN EN 16351)
𝓕𝓚_gerichteter_plattenwerkstoff
                    := { OSB/1, OSB/2, OSB/3, OSB/4 }      (DIN EN 300)
𝓕𝓚_isotroper_plattenwerkstoff_P
                    := { P1, P2, P3, P4, P5, P6, P7 }      (DIN EN 312, Spanplatten)
𝓕𝓚_isotroper_plattenwerkstoff_F
                    := { HB, MBH, MBL, MDF, HDF }          (DIN EN 622-2/3/5, Faserplatten)
𝓕𝓚_werkstoff_stahl  := { 4.6, 5.6, 8.8, 10.9, A2-70, A4-70, … }
                                                            (DIN EN ISO 898-1, EN 10088;
                                                             siehe `werkstoff_stahl`)
```

Die Zuordnungsfunktion

```
festigkeitsklasse : 𝓦 → 𝓕𝓚,  w ↦ festigkeitsklasse(w)
```

erfüllt die **Konsistenzbedingung**

```
∀ w ∈ 𝓦 :  festigkeitsklasse(w) ∈ 𝓕𝓚_subklasse(w),
```

d. h. die Festigkeitsklasse eines Werkstoffs ist immer einer
werkstoff-konsistenten Klassenmenge entnommen.

## Wohldefiniertheit

- **Existenz**: Für jeden produktnormativ zertifizierten Werkstoff
  am Markt ist die Festigkeitsklasse eindeutig und durch die
  CE-Kennzeichnung ausgewiesen (siehe `produktkennzeichnung`).
- **Eindeutigkeit**: Die Festigkeitsklasse ist ein Aufzählungswert
  aus einer endlichen, normativ festgelegten Klassenfolge; ein
  Werkstoff trägt genau eine Festigkeitsklasse zur Zeit (Mehrfach-
  Klassifikation, z. B. „C24 oder C30 nach Sortierung", ist nicht
  zulässig — die Klassifikation muss vor Bemessung aufgelöst sein).
- **Konsistenz mit Subklasse**: Die Festigkeitsklasse muss aus der
  zur Subklasse passenden Klassenmenge stammen (z. B. C24 nur bei
  `axiales_holz` zulässig, nicht bei `isotroper_plattenwerkstoff`).
  Die Konsistenz ist Klassen-Invariante; eine Verletzung ist
  Validierungsfehler.
- **Bemessungs-Vollständigkeit**: Festigkeitsklasse + Subklasse +
  geometrische Annotationen (Faserrichtung, Lagenstruktur,
  Plattendicken-Achse) bilden zusammen die vollständige Eingabe
  für EC5- und SIA-265-Bemessung.
- **OSB / Spanplatte / Faserplatte als Sonderfall**: Die Typ-
  Klassifikation (OSB/3, P5, MDF) ist im strengen Sinn keine
  Festigkeitsklasse, sondern ein Verwendungs-Typ. EN 12369-1 führt
  die zugehörigen charakteristischen Festigkeitswerte als Funktion
  des Verwendungs-Typs; das Glossar führt sie aus
  Konsistenzgründen unter `festigkeitsklasse`.
- **Nicht-Zirkularität**: Die Definition stützt sich auf
  `werkstoff` und `produktkennzeichnung`. Sie kommt nicht in ihrer
  eigenen Definition vor.

## Erläuterung (nicht normativ)

### Übersicht der Klassen je Subklasse

| Subklasse                          | Klassenfolge (Beispiele)                  | Norm                |
|------------------------------------|---------------------------------------------|---------------------|
| Vollholz / KVH (Nadel)             | C14, C16, C20, **C24**, C30, C35, C40       | EN 338, EN 14081-1  |
| Vollholz Laub                      | D18, D24, D30, D40, D60                     | EN 338              |
| BSH homogen                        | GL20h, GL22h, **GL24h**, GL28h, GL32h       | EN 14080            |
| BSH kombiniert                     | GL20c, GL24c, **GL28c**, GL32c              | EN 14080            |
| LVL (z. B. Kerto-S, BauBuche)      | ETA-Klassen je Hersteller                    | EN 14374, ETA       |
| CLT / BSP                          | Lagen-Klassen (typ. C24) + Hersteller-Bauteilklasse via ETA | EN 16351            |
| OSB                                | OSB/1, OSB/2, **OSB/3**, OSB/4              | EN 300              |
| Spanplatte                         | P1, P2, P3, **P4**, P5, P6, P7              | EN 312              |
| MDF / HDF                          | MDF (Standard), MDF.HLS, HDF                | EN 622-5            |
| Harte Faserplatte                  | HB, HB.H, HB.E                              | EN 622-2            |
| Mittelharte Faserplatte            | MBH, MBL                                    | EN 622-3            |
| Stahl (Schrauben/Bolzen)           | 4.6, 5.6, **8.8**, 10.9                     | ISO 898-1           |
| Stahl (nichtrostend)               | A2-70, A4-70                                | EN 10088            |

Fettgedruckte Werte sind die im Holzbau dominanten Klassen.

### Sortierklassen vs. Festigkeitsklassen

DIN 4074-1 unterscheidet **Sortierklassen** (S7, S10, S13) als
visuelle bzw. maschinelle Sortiermerkmale; die Zuordnung zur
**Festigkeitsklasse** (C16, C24, C30) erfolgt nach
Zuordnungstabelle. Im Glossar wird ausschließlich die Festigkeits-
klasse geführt; die Sortierklasse ist Eingabe der
Produktkennzeichnung (siehe `produktkennzeichnung`), nicht des
Werkstoffs als Bemessungseingabe.

### CLT-Klassifikation als Sonderfall

Bei Brettsperrholz wird die Festigkeitsklasse nicht einheitlich
auf das Bauteil angewandt, sondern lagenweise (jede Lage typisch
C24). Die Hersteller (KLH, Stora Enso, Hasslacher, Binderholz)
führen zusätzlich eine **Bauteil-Festigkeitsklasse** über ETA
(z. B. KLH XL-CL3-h). Im Glossar wird die Festigkeitsklasse bei
Mehrlagenholz daher dual geführt: über die Lagen-Klassen (Pflicht)
und optional über eine Bauteil-Klasse (ETA).

## Beziehungen

- **Oberbegriff**: keiner. Festigkeitsklasse ist ein
  Aufzählungstyp über die Werkstoff-Subklasse.
- **Verwendung**:
  - **Werkstoff** (`werkstoff`): trägt die Festigkeitsklasse als
    Pflichtfeld.
  - **Axiales Holz** (`axiales_holz`): C-Klassen / D-Klassen / GL-
    Klassen / LVL-ETA.
  - **Mehrlagenholz** (`mehrlagenholz`): über Lagen-Klassen plus
    optionale Bauteil-Klasse.
  - **Gerichteter Plattenwerkstoff**
    (`gerichteter_plattenwerkstoff`): OSB-Typ.
  - **Isotroper Plattenwerkstoff**
    (`isotroper_plattenwerkstoff`): P-/MDF-/HDF-/HB-/MBH-/MBL-Typ.
  - **Werkstoff-Stahl** (`werkstoff_stahl`): Stahlgüte als
    Festigkeitsklasse.
  - **Lage** (`lage`): jede Lage eines Mehrlagenholzes trägt eine
    eigene Festigkeitsklasse.
- **Abgrenzung**:
  - **`werkstoff`**: die Werkstoff-Subklasse ist die *Klassen*-
    Wahl (was für ein Werkstoff); die Festigkeitsklasse ist die
    *Bemessungs*-Wahl (welche charakteristischen Werte).
  - **`produktkennzeichnung`**: identifiziert die Charge eines
    konkreten gelieferten Produkts; Festigkeitsklasse ist Teil der
    Produktkennzeichnung, aber als Bemessungseingabe eigenständig
    geführt.
  - **`faserrichtungs_modus`**: orthogonal zur Festigkeitsklasse —
    der Modus klassifiziert die Anisotropie, die Festigkeitsklasse
    die quantitativen Werte.
  - **„Sortierklasse"** (DIN 4074-1, S7/S10/S13): Sortiermerkmal,
    nicht Festigkeitsklasse. Zuordnung erfolgt über die Norm-
    Zuordnungstabelle.
  - **„Güteklasse"** (umgangssprachlich): unscharf; im Glossar
    ausgeschlossen.

## Implementierungshinweis

Datentyp (Domänen-Schicht, Kotlin, Schicht
`domain.holzbau.werkstoff`):

```kotlin
package domain.holzbau.werkstoff

/**
 * Festigkeitsklasse eines Werkstoffs.
 * Glossar: hg_festigkeitsklasse.md
 *
 * Sealed-Hierarchie nach Werkstoff-Subklasse. Jede Subklasse trägt
 * eine eigene endliche Klassenfolge nach Produktnorm.
 *
 * Konsistenzbedingung: festigkeitsklasse(w) ∈ FK_subklasse(w).
 * Wird in der Werkstoff-Subklasse erzwungen.
 */
sealed interface Festigkeitsklasse {
    val bezeichnung: String  // normative Kurzform, z. B. "C24"
    val normReferenz: String // z. B. "DIN EN 338"
}

sealed interface AxialesHolzFestigkeitsklasse : Festigkeitsklasse
enum class CKlasse(override val bezeichnung: String) : AxialesHolzFestigkeitsklasse {
    C14("C14"), C16("C16"), C18("C18"), C20("C20"), C22("C22"),
    C24("C24"), C27("C27"), C30("C30"), C35("C35"), C40("C40"),
    C45("C45"), C50("C50");
    override val normReferenz = "DIN EN 338"
}
enum class DKlasse(override val bezeichnung: String) : AxialesHolzFestigkeitsklasse {
    D18("D18"), D24("D24"), D27("D27"), D30("D30"), D35("D35"),
    D40("D40"), D50("D50"), D60("D60"), D70("D70");
    override val normReferenz = "DIN EN 338"
}
enum class GLKlasseHomogen(override val bezeichnung: String) : AxialesHolzFestigkeitsklasse {
    GL20h("GL20h"), GL22h("GL22h"), GL24h("GL24h"), GL26h("GL26h"),
    GL28h("GL28h"), GL30h("GL30h"), GL32h("GL32h");
    override val normReferenz = "DIN EN 14080"
}
enum class GLKlasseKombiniert(override val bezeichnung: String) : AxialesHolzFestigkeitsklasse {
    GL20c("GL20c"), GL22c("GL22c"), GL24c("GL24c"), GL26c("GL26c"),
    GL28c("GL28c"), GL30c("GL30c"), GL32c("GL32c");
    override val normReferenz = "DIN EN 14080"
}
data class LVLKlasse(
    override val bezeichnung: String,    // z. B. "Kerto-S", "BauBuche GL75"
    val etaNummer: String                // z. B. "ETA-14/0349"
) : AxialesHolzFestigkeitsklasse {
    override val normReferenz = "DIN EN 14374 (über $etaNummer)"
}

enum class OSBTyp(override val bezeichnung: String) : Festigkeitsklasse {
    OSB1("OSB/1"), OSB2("OSB/2"), OSB3("OSB/3"), OSB4("OSB/4");
    override val normReferenz = "DIN EN 300"
}

enum class SpanplattenTyp(override val bezeichnung: String) : Festigkeitsklasse {
    P1("P1"), P2("P2"), P3("P3"), P4("P4"), P5("P5"), P6("P6"), P7("P7");
    override val normReferenz = "DIN EN 312"
}

// MDF, HDF, HB, MBH, MBL analog (DIN EN 622-2/3/5).
// Stahlgüte siehe werkstoff_stahl.
```

- **Einheit**: dimensionslos (Aufzählung).
- **Identität**: keine; Werteklasse / enum.
- **Invariante**: Konsistenz Festigkeitsklasse ↔ Subklasse wird in
  der Werkstoff-Subklasse zur Konstruktionszeit geprüft (z. B.
  `AxialesHolz` akzeptiert nur `AxialesHolzFestigkeitsklasse`).
- **IFC-Mapping**: `IfcMaterial.Name` enthält die Festigkeitsklasse
  als Teil des Werkstoff-Namens (z. B. „Vollholz C24",
  „BSH GL24h", „OSB/3"). Property Sets
  `Pset_MaterialWoodBasedBeam` / `Pset_MaterialWoodBasedPanel`
  führen die charakteristischen Werte separat.
- **Edge Cases**:
  - **Werkstoff ohne Festigkeitsklasse**: nicht zulässig vor
    Bemessung. Platzhalter-Klasse `UNBEKANNT` während Entwurf;
    Pflichtauflösung vor Bemessung.
  - **Mehrfach-Klassifikation** (z. B. „C24 oder C30"): nicht
    zulässig; muss bei Eingabe aufgelöst werden.
  - **CLT-Bauteilklasse via ETA**: Folgearbeit; aktuell wird die
    Bemessung über die Lagen-Klassen geführt.

## Quellen

**Primär (normativ):**

- DIN EN 338:2016-07, „Bauholz für tragende Zwecke –
  Festigkeitsklassen".
- DIN EN 14080:2013-09, „Holzbauwerke – Brettschichtholz und
  Balkenschichtholz – Anforderungen".
- DIN EN 14081-1:2019-10, „Holzbauwerke – Nach Festigkeit
  sortiertes Bauholz".
- DIN EN 14374:2005-02, „Holzbauwerke – Furnierschichtholz für
  tragende Zwecke".
- DIN EN 16351:2021-08, „Holzbauwerke – Brettsperrholz".
- DIN EN 300:2006-09, „Platten aus langen, schlanken, gerichteten
  Spänen (OSB)".
- DIN EN 312:2010-12, „Spanplatten – Anforderungen".
- DIN EN 622-2/3/5, „Faserplatten – Anforderungen".
- DIN 4074-1:2012-06, „Sortierung von Holz nach der Tragfähigkeit
  – Teil 1: Nadelschnittholz".
- SIA 265:2021, „Holzbau".

**Sekundär:**

- Blass, H. J.; Sandhaas, C.: *Ingenieurholzbau – Grundlagen der
  Bemessung.* KIT Scientific Publishing, Karlsruhe 2016.
- Mönck, W.; Rug, W.: *Holzbau – Bemessung und Konstruktion.*
  16. Aufl., Beuth, Berlin 2015.
- Niemz, P.; Sonderegger, W.: *Physik des Holzes und der
  Holzwerkstoffe.* Hanser, München 2017.
- Lignum (Hrsg.): *Holzbautabellen HBT.* Lignum, Zürich.
- Schickhofer, G. et al. (Hrsg.): *BSPhandbuch.* TU Graz 2010.

**Korpus (nicht autoritativ):**

- ETAs der CLT-Hersteller (KLH, Stora Enso, Hasslacher, Binderholz)
  und LVL-Hersteller (Metsä Wood Kerto, Pollmeier BauBuche),
  abgerufen 2026-05-08.
- Wikipedia, Lemma „Festigkeitsklasse" (abgerufen 2026-05-08).
