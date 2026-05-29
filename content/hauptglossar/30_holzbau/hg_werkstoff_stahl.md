---
id: werkstoff_stahl
benennung: Werkstoff Stahl
synonyme: ["Stahl (Werkstoff)", "Stahlwerkstoff", "Werkstoff von Verbindungsmitteln und Verbindern"]
abgelehnte_benennungen: [Stahl, Eisen, Metall, "steel", "metal", "fastener material"]
oberbegriff: werkstoff
begriffstyp: generisch
voraussetzungen: [werkstoff, produktkennzeichnung, faserrichtungs_modus, toleranzen]
abgrenzung_zu: [axiales_holz, mehrlagenholz, gerichteter_plattenwerkstoff, isotroper_plattenwerkstoff, festigkeitsklasse, faserrichtung]
status: entwurf
subglossar_pendant: notwendig
quellen_primär:
  - "DIN EN 1993-1-1:2010-12 (Eurocode 3), 'Bemessung und Konstruktion von Stahlbauten – Teil 1-1: Allgemeine Bemessungsregeln und Regeln für den Hochbau', Abschnitt 3 (Werkstoffe)."
  - "DIN EN ISO 898-1:2013-05, 'Mechanische Eigenschaften von Verbindungselementen aus Kohlenstoffstahl und legiertem Stahl – Teil 1: Schrauben mit festgelegten Eigenschaften – Regelgewinde und Feingewinde' (Festigkeitsklassen 4.6, 4.8, 5.6, 5.8, 6.8, 8.8, 9.8, 10.9, 12.9)."
  - "DIN EN ISO 3506-1:2020-08, 'Mechanische Eigenschaften von Verbindungselementen aus nichtrostenden Stählen – Teil 1: Schrauben' (Klassen A1, A2, A3, A4, A5 mit Festigkeitsstufen -50, -70, -80)."
  - "DIN EN 10088-1:2014-12, 'Nichtrostende Stähle – Teil 1: Verzeichnis der nichtrostenden Stähle' (Werkstoff-Nummern 1.4301, 1.4404 etc., Bezeichnung A2 / A4)."
  - "DIN EN 10025-1:2005-02, 'Warmgewalzte Erzeugnisse aus Baustählen – Teil 1: Allgemeine technische Lieferbedingungen' (S235, S275, S355, S420, S460)."
  - "DIN EN 14592:2022-09, 'Holzbauwerke – Stiftförmige Verbindungsmittel – Anforderungen' (Produktnorm für Nägel, Klammern, Schrauben, Bolzen, Stabdübel im Holzbau)."
  - "DIN EN 14545:2009-02, 'Holzbauwerke – Verbinder – Anforderungen' (Produktnorm für Balkenschuhe, Winkel, Knotenbleche und weitere Verbinder im Holzbau)."
  - "DIN EN 1995-1-1:2010-12 (Eurocode 5), Abschnitt 8 (Verbindungen mit stiftförmigen Verbindungsmitteln): Verweis auf Stahl-Festigkeitsklassen für f_u,k und f_y,k."
quellen_sekundär:
  - "Blass, H. J.; Sandhaas, C.: Ingenieurholzbau – Grundlagen der Bemessung. KIT Scientific Publishing, Karlsruhe 2016, Kap. 5 (Verbindungen) und Kap. 5.2 (Stahl als Verbindungsmittel-Werkstoff: f_u,k, f_y,k)."
  - "Mönck, W.; Rug, W.: Holzbau – Bemessung und Konstruktion. 16. Aufl., Beuth, Berlin 2015, Kap. 9 (Verbindungstechniken)."
  - "Lignum (Hrsg.): Holzbautabellen HBT, Lignum, Zürich, aktuelle Auflage, Kap. Verbindungsmittel (Stahlgüten der gängigen Schrauben, Bolzen, Stabdübel)."
  - "Werner, G.; Zimmer, K.; Bohnsack, R.: Holzbau Teil 2: Dach- und Hallentragwerke. 7. Aufl., Springer Vieweg, Wiesbaden 2018, Kap. Verbindungsmittel."
quellenkonflikt: |
  Anders als bei den vier Holzwerkstoff-Subklassen führt Stahl im
  Holzbau **keine** vergleichbare Anisotropie-Klassifikation: Stahl
  ist im Bemessungssinn isotrop (DIN EN 1993-1-1: linear-elastisch
  isotrop bis zur Streckgrenze). Die Holzbau-relevanten
  Stahleigenschaften sind:

  - **Streckgrenze f_y,k** (z. B. 240 N/mm² bei Klasse 4.6,
    640 N/mm² bei Klasse 8.8, 900 N/mm² bei Klasse 10.9; aus
    Stahlgüte ableitbar, EN ISO 898-1 Tab. 5).
  - **Zugfestigkeit f_u,k** (z. B. 400 N/mm² bei 4.6, 800 N/mm² bei
    8.8, 1000 N/mm² bei 10.9; aus Stahlgüte ableitbar).
  - **E-Modul** ≈ 210 000 N/mm² (für alle gängigen Stahlgüten
    annähernd konstant).

  Die Holzbau-Bemessung (EN 1995-1-1 Abschnitt 8) verwendet die
  charakteristischen Werte f_y,k und f_u,k als Eingaben in die
  Tragfähigkeitsformeln (Johansen-Theorie für Lochleibung,
  Ausziehfestigkeit Vollgewindeschrauben).

  Eigene Festlegung in diesem Glossar:

  - **Werkstoff Stahl** ist die fünfte Werkstoff-Subklasse als
    Geschwister zu den vier Holzwerkstoff-Subklassen
    (`axiales_holz`, `mehrlagenholz`, `gerichteter_plattenwerkstoff`,
    `isotroper_plattenwerkstoff`) und extensional Bestandteil der
    Werkstoff-Menge 𝓦 (siehe `werkstoff`).
  - Sie trägt **keine Faserrichtung, keine Lagenstruktur, keine
    Plattendicken-Achse** im Holzbau-Sinn — Stahl ist isotrop und
    geometrisch durch das Verbindungsmittel-/Verbinder-
    Bauteil selbst beschrieben, nicht durch Werkstoff-Anisotropie.
  - **Faserrichtungs-Modus** wird mit `KEINE` belegt. Der Modus
    KEINE steht im Glossar für „keine bemessungsrelevante
    Faserrichtung" und wird sowohl von `isotroper_plattenwerkstoff`
    (in Plattenebene quasi-isotrop) als auch von `werkstoff_stahl`
    (3D-isotrop) getragen; die Modus-Subklassen-Zuordnung ist
    deshalb keine Bijektion (siehe `faserrichtungs_modus`). Die
    Disjunktheit von `werkstoff_stahl` zu
    `isotroper_plattenwerkstoff` wird durch die sealed-Subklassen-
    Identität und die unterschiedlichen Pflichtfelder
    (`plattendicken_achse` Pflicht bei
    `isotroper_plattenwerkstoff`, `plattendicken_achse = ⊥` bei
    `werkstoff_stahl`) getragen, nicht durch den Modus.
  - **Festigkeitsklasse** wird durch die **Stahlgüte** ersetzt:
    sealed enum mit den Werten 4.6, 5.6, 8.8, 10.9 (unlegierter
    Stahl, EN ISO 898-1) sowie A2-70, A4-70 (nichtrostend,
    EN ISO 3506-1). Streckgrenze f_y,k und Zugfestigkeit f_u,k sind
    aus der Stahlgüte ableitbar (Stahlgütentabelle als
    Tabellen-Funktion).
  - **Pflichtfelder** am Werkstoff Stahl:
    1. `faserrichtungsModus = KEINE` (Klassen-Invariante).
    2. `produktkennzeichnung` (CE nach EN 14592 für stiftförmige
       Verbindungsmittel; CE nach EN 14545 für Verbinder; je nach
       Element-Subklasse).
    3. `stahlguete: Stahlguete` (Aufzählungstyp).
    4. `streckgrenze: Stress?` (in N/mm²; aus Stahlgüte ableitbar
       oder explizit überschreibbar).
    5. `zugfestigkeit: Stress?` (analog).
    6. `plattendickenAchse = null` (keine Plattengeometrie).

  Mit dieser fünften Subklasse ist die Werkstoff-Hierarchie
  vollständig für die App-Ontologie: Bauteile aus Holzwerkstoff
  (4 Subklassen) und Verbindungsmittel/Verbinder/
  Verstärkungselemente aus Stahl (1 Subklasse).
---

## Prosa-Definition

Ein **Werkstoff Stahl** ist ein Werkstoff im Sinne der App-
Werkstoff-Hierarchie, dessen materialphysikalische Klasse Stahl ist
(unlegierter Kohlenstoff- oder legierter nichtrostender Stahl), der
ohne Faserrichtungs-, Lagen- oder Plattenrichtungs-Annotation
auskommt (Faserrichtungs-Modus KEINE im Sinne von 3D-Isotropie),
der durch eine Stahlgüte nach DIN EN ISO 898-1 (4.6, 5.6, 8.8, 10.9
etc.) bzw. DIN EN ISO 3506-1 (A2-70, A4-70 etc.) klassifiziert ist,
der charakteristische Streckgrenze f_y,k und Zugfestigkeit f_u,k
als ableitbare oder explizite Eigenschaften trägt und der als
Werkstoff von Verbindungsmitteln (Schraube, Nagel, Bolzen,
Stabdübel), Verbindern (Balkenschuh, Knotenblech) und
Verstärkungselementen (Vollgewindeschrauben) im Holzbau verwendet
wird.

## Mathematische Definition

Sei

- 𝓦 die Menge der Werkstoffe (siehe `werkstoff`),
- 𝓜𝓜 = { HART, STRUKTURIERT, SCHWACH, KEINE } die Menge der
  Faserrichtungs-Modi (siehe `faserrichtungs_modus`),
- 𝓟_St die Menge der für Verbindungsmittel/Verbinder zulässigen
  Produktkennzeichnungen (CE nach DIN EN 14592, DIN EN 14545,
  je nach Element-Subklasse),
- 𝓢𝓖 die Menge der Stahlgüten (siehe unten).

Dann ist ein **Werkstoff Stahl** das Tupel

```
WSt := (faserrichtungs_modus, produktkennzeichnung,
        plattendicken_achse, stahlguete, streckgrenze?, zugfestigkeit?)
```

mit

- **faserrichtungs_modus** = KEINE (konstant für diese Subklasse,
  im Sinne von 3D-Isotropie; siehe Wohldefiniertheit und
  `faserrichtungs_modus`),
- **produktkennzeichnung** ∈ 𝓟_St,
- **plattendicken_achse** = ⊥ (konstant: kein Plattenwerkstoff,
  keine geometrische Werkstoff-Anisotropie-Achse),
- **stahlguete** ∈ 𝓢𝓖,
- **streckgrenze** ∈ ℝ_{>0} ∪ {null} (in N/mm²; aus Stahlgüte
  ableitbar, optional explizit gesetzt),
- **zugfestigkeit** ∈ ℝ_{>0} ∪ {null} (in N/mm²; analog).

Die **Stahlgüte** 𝓢𝓖 ist der disjunkte Aufzählungstyp

```
𝓢𝓖 := 𝓢𝓖_unlegiert ⊎ 𝓢𝓖_nichtrostend ⊎ 𝓢𝓖_baustahl,
```

mit

```
𝓢𝓖_unlegiert  := { 4.6, 4.8, 5.6, 5.8, 6.8, 8.8, 9.8, 10.9, 12.9 }
                                              (DIN EN ISO 898-1)
𝓢𝓖_nichtrostend := { A1-50, A1-70, A1-80, A2-50, A2-70, A2-80,
                     A3-50, A3-70, A4-50, A4-70, A4-80, A5-50, A5-70 }
                                              (DIN EN ISO 3506-1)
𝓢𝓖_baustahl   := { S235, S275, S355, S420, S460 }
                                              (DIN EN 10025-1, für
                                               Verbinder-Stahlbleche)
```

**Stahlgüten-Tabelle** (Funktion von 𝓢𝓖 → ℝ⁺ × ℝ⁺ → (f_y,k, f_u,k);
DIN EN ISO 898-1 Tab. 5 und EN ISO 3506-1):

```
4.6   :  f_y,k = 240,   f_u,k = 400   N/mm²
5.6   :  f_y,k = 300,   f_u,k = 500   N/mm²
6.8   :  f_y,k = 480,   f_u,k = 600   N/mm²
8.8   :  f_y,k = 640,   f_u,k = 800   N/mm²
10.9  :  f_y,k = 900,   f_u,k = 1000  N/mm²
12.9  :  f_y,k = 1080,  f_u,k = 1200  N/mm²
A2-70 :  f_y,k = 450,   f_u,k = 700   N/mm²
A4-70 :  f_y,k = 450,   f_u,k = 700   N/mm²
A2-80 :  f_y,k = 600,   f_u,k = 800   N/mm²
S235  :  f_y,k = 235,   f_u,k = 360   N/mm²  (Bauteildicke ≤ 16 mm)
S275  :  f_y,k = 275,   f_u,k = 410   N/mm²
S355  :  f_y,k = 355,   f_u,k = 490   N/mm²
```

Es ist 𝓦𝓢𝓽 ⊂ 𝓦, d. h. die Menge der Stahl-Werkstoffe ist die
fünfte Geschwister-Teilmenge der Werkstoff-Menge
(`𝓦 := 𝓐𝓗 ⊎ 𝓜𝓛 ⊎ 𝓖𝓟 ⊎ 𝓘𝓟 ⊎ 𝓦𝓢𝓽`, siehe `werkstoff`) mit
`faserrichtungs_modus = KEINE`. Die Disjunktheit zu
`isotroper_plattenwerkstoff` (gleicher Modus) wird über die
sealed-Subklassen-Identität und das unterschiedliche
Pflichtfeld-Profil (`plattendicken_achse = ⊥` bei `werkstoff_stahl`
vs. `plattendicken_achse ∈ S²` bei `isotroper_plattenwerkstoff`)
getragen.

## Wohldefiniertheit

- **Existenz**: Für jedes nach DIN EN 14592, DIN EN 14545,
  EN ISO 898-1 oder EN ISO 3506-1 zertifizierte Verbindungsmittel
  bzw. Verbinder am Markt ist die Stahlgüte und damit der
  Werkstoff Stahl produktnormativ definiert (CE-Kennzeichnung).
- **Eindeutigkeit der Klassifikation**: Werkstoff Stahl ist
  disjunkt zu den vier Holzwerkstoff-Subklassen, weil:
  1. Stahl trägt keine Faserrichtung, keine Lagenstruktur, keine
     Plattenlängsrichtung — disjunkt zu HART, STRUKTURIERT,
     SCHWACH.
  2. Stahl ist 3D-isotrop, nicht „in der Plattenebene quasi-
     isotrop wie Spanplatte" — disjunkt zu
     `isotroper_plattenwerkstoff` durch sealed-Subklassen-Identität
     und durch das Pflichtfeld `plattendicken_achse = ⊥` (vs.
     `plattendicken_achse ∈ S²` Pflicht bei
     `isotroper_plattenwerkstoff`).
  Die `faserrichtungs_modus = KEINE`-Belegung ist semantisch
  konsistent: KEINE steht im Glossar generisch für „keine
  bemessungsrelevante Faserrichtung" und deckt sowohl
  in-Plattenebene-Isotropie als auch 3D-Isotropie ab (siehe
  `faserrichtungs_modus`).
- **Eindeutigkeit der Stahlgüte**: pro Werkstoff-Instanz genau
  eine Stahlgüte; Mehrfach-Klassifikation („8.8 oder 10.9") ist
  nicht zulässig.
- **Streckgrenze und Zugfestigkeit aus Stahlgüte ableitbar**: die
  Stahlgütentabelle (DIN EN ISO 898-1 Tab. 5 et al.) ist eine
  endliche, normativ tabellierte Funktion. Wenn `streckgrenze`
  oder `zugfestigkeit` explizit gesetzt sind, müssen sie konsistent
  zur Stahlgüte sein (Toleranzbereich nach Norm); andernfalls
  Validierungswarnung.
- **Plattendicken-Achse trivial null**: `plattendicken_achse = ⊥`
  ist Klassen-Invariante; Stahl ist kein Plattenwerkstoff im Sinne
  der EC5-Plattenwerkstoff-Bemessung.
- **Faserrichtungs-Modus = KEINE**: semantisch „keine
  bemessungsrelevante Faserrichtung", bei Stahl ausgeprägt als
  3D-Isotropie (anders als bei `isotroper_plattenwerkstoff`, das
  nur in der Plattenebene quasi-isotrop ist). Hankinson-Winkel ist
  nicht zutreffend.
- **Konsistenz produktkennzeichnung ↔ Element-Subklasse**:
  EN 14592 (stiftförmige Verbindungsmittel: Schraube, Nagel,
  Bolzen, Stabdübel), EN 14545 (Verbinder: Balkenschuh, Winkel,
  Knotenblech), EN 1090-1 (allgemeiner Stahlbau für
  Verbindungselemente) sind je nach Element zugeordnet.
- **Nicht-Zirkularität**: Die Definition stützt sich auf
  `werkstoff`, `produktkennzeichnung`, `faserrichtungs_modus`,
  `toleranzen`. Sie kommt nicht in ihrer eigenen Definition vor.

## Erläuterung (nicht normativ)

### Stahlgüte und Festigkeitsklassen-Bezeichnung

Bei unlegiertem Stahl (DIN EN ISO 898-1) ist die Stahlgüte
zweistellig kodiert:

```
8.8 → f_u,k = 800 N/mm²,  f_y,k / f_u,k = 0,8 → f_y,k = 640 N/mm²
10.9 → f_u,k = 1000 N/mm², f_y,k / f_u,k = 0,9 → f_y,k = 900 N/mm²
```

Bei nichtrostendem Stahl (DIN EN ISO 3506-1) ist die Bezeichnung
zweiteilig: A2 / A4 / A5 ist die Werkstoffklasse (austenitisch,
mit unterschiedlichen Legierungselementen), -70 / -80 ist die
Festigkeitsstufe (f_u,k = 700 / 800 N/mm²).

### Anwendung im Holzbau

Stahl als Werkstoff im Holzbau tritt in drei Element-Rollen auf:

| Element-Rolle              | Beispiele                            | Produktnorm |
|----------------------------|--------------------------------------|-------------|
| Verbindungsmittel          | Schraube, Nagel, Bolzen, Stabdübel  | EN 14592    |
| Verbinder                  | Balkenschuh, Winkel, Knotenblech    | EN 14545    |
| Verstärkungselement        | Vollgewindeschraube                  | EN 14592    |

Alle drei Elemente sind Geschwister unter `element` (siehe
`element`, Memory `project_element_ontologie`); sie tragen
gemeinsam einen Werkstoff der Subklasse Stahl.

### Holzbau-Bemessung mit Stahleigenschaften

EN 1995-1-1 Abschnitt 8 verwendet für Verbindungsbemessung
(Johansen-Theorie):

- **Lochleibungsfestigkeit** des Holzes f_h,α,k (Hankinson, siehe
  `hankinson_winkel`).
- **Fließmoment** der Schraube/des Bolzens M_y,Rk = 0,3 · f_u,k · d^2,6
  (EN 1995-1-1 Gl. 8.30).
- **Zugfestigkeit f_u,k** der Schraube für Ausziehfestigkeit.

Damit gehen die Stahl-Eigenschaften direkt in die Holzbau-
Bemessung ein; sie sind nicht „nur" Stahlbau-Größen.

### Warum Modus = KEINE und nicht „STAHL"

Eine Erweiterung der Modus-Aufzählung um einen fünften Wert
„STAHL" wurde geprüft und verworfen:

1. Der Faserrichtungs-Modus klassifiziert die bemessungsrelevante
   Faserrichtung; ein fünfter Wert wäre semantisch redundant —
   Stahl gehört, wie Spanplatte/MDF/HDF, in die Klasse „keine
   bemessungsrelevante Faserrichtung".
2. Die App-Domänen-Schicht trennt die Subklassen über sealed-
   Hierarchien (`Werkstoff` als sealed interface mit fünf
   Subklassen), nicht über die Modus-Aufzählung allein. Der Modus
   ist eine **partielle Diskriminante** (siehe
   `faserrichtungs_modus`).
3. Die Modus-Aufzählung ist EC5-bemessungsrelevant für
   Holzwerkstoffe (Hankinson, Lochleibung); für Stahl ist sie
   nicht anwendbar — das ist gerade die Aussage von KEINE.

`faserrichtungs_modus = KEINE` für Stahl ist damit nicht
Formalkonvention, sondern die semantisch korrekte Belegung im
Rahmen der vier Modi.

## Beziehungen

- **Oberbegriff**: `werkstoff`. Geschwister-Subklasse zu
  `axiales_holz`, `mehrlagenholz`, `gerichteter_plattenwerkstoff`,
  `isotroper_plattenwerkstoff`.
- **Pflichtfelder über `werkstoff` hinaus**:
  - **Stahlgüte** (`stahlguete`): sealed enum, oben definiert.
  - **Streckgrenze** (`streckgrenze`): N/mm², optional explizit;
    aus Stahlgüte ableitbar.
  - **Zugfestigkeit** (`zugfestigkeit`): N/mm², optional explizit;
    aus Stahlgüte ableitbar.
- **Verwendung**:
  - **Verbindungsmittel** (`verbindungsmittel`): Pflicht-Werkstoff
    Stahl (Schraube, Nagel, Bolzen, Stabdübel).
  - **Verbinder** (`verbinder`): Pflicht-Werkstoff Stahl
    (Balkenschuh, Winkel, Knotenblech).
  - **Verstärkungselement** (`verstaerkungselement`): typisch
    Werkstoff Stahl (Vollgewindeschraube).
- **Abgrenzung**:
  - **`axiales_holz`, `mehrlagenholz`,
    `gerichteter_plattenwerkstoff`,
    `isotroper_plattenwerkstoff`**: Holzwerkstoffe mit
    Bemessungsanisotropie; disjunkt zu Stahl. Stahl trägt keine
    Faserrichtung, keine Lagenstruktur, keine Plattenrichtung.
  - **`festigkeitsklasse`** (Holzwerkstoffe): Aufzählungstyp
    werkstoff-spezifisch; bei Stahl wird die Rolle durch die
    `stahlguete` übernommen. Beide sind Subtypen von
    Festigkeitsklasse-Aggregaten in der `festigkeitsklasse`-
    Hierarchie.
  - **`faserrichtung`**, **`lagenstruktur`**,
    **`plattenlaengsrichtung`**, **`haupttragrichtung`**,
    **`plattendicken_achse`**: alle nicht anwendbar für Stahl.
  - **„Stahl"** (umgangssprachlich): unscharf; im Glossar als
    Oberbegriff der konkreten Stahlgüten zu verstehen, nicht als
    Werkstoff-Instanz.
  - **Stahlbau-Werkstoff** (DIN EN 1993-1-1, Baustähle S235–S460):
    auch als Stahlgüte führbar (Verbinder-Bleche), aber im
    Holzbau-Glossar nur über die Stahlgüten-Aufzählung
    referenziert; Stahlbau-spezifische Bemessung fällt
    außerhalb des App-Geltungsbereichs.

## Implementierungshinweis

Datentyp (Domänen-Schicht, Kotlin, Schicht
`domain.holzbau.werkstoff`):

```kotlin
package domain.holzbau.werkstoff

import domain.geometrie.Einheitsvektor
import domain.identifikation.Produktkennzeichnung

/**
 * Stahlgüte als Festigkeits-Aufzählung für Verbindungsmittel,
 * Verbinder und Verstärkungselemente.
 * Glossar: hg_werkstoff_stahl.md (Subtyp `Festigkeitsklasse` in
 * der allgemeinen Festigkeitsklassen-Hierarchie).
 */
sealed interface Stahlguete {
    val bezeichnung: String
    val streckgrenze: Double  // N/mm²
    val zugfestigkeit: Double // N/mm²
    val normReferenz: String
}

enum class StahlgueteUnlegiert(
    override val bezeichnung: String,
    override val streckgrenze: Double,
    override val zugfestigkeit: Double
) : Stahlguete {
    SG_4_6 ("4.6",  240.0, 400.0),
    SG_5_6 ("5.6",  300.0, 500.0),
    SG_6_8 ("6.8",  480.0, 600.0),
    SG_8_8 ("8.8",  640.0, 800.0),
    SG_10_9("10.9", 900.0, 1000.0),
    SG_12_9("12.9", 1080.0, 1200.0);
    override val normReferenz = "DIN EN ISO 898-1"
}

enum class StahlgueteNichtrostend(
    override val bezeichnung: String,
    override val streckgrenze: Double,
    override val zugfestigkeit: Double
) : Stahlguete {
    A2_70("A2-70", 450.0, 700.0),
    A4_70("A4-70", 450.0, 700.0),
    A2_80("A2-80", 600.0, 800.0);
    override val normReferenz = "DIN EN ISO 3506-1"
}

enum class StahlgueteBaustahl(
    override val bezeichnung: String,
    override val streckgrenze: Double,
    override val zugfestigkeit: Double
) : Stahlguete {
    S235("S235", 235.0, 360.0),
    S275("S275", 275.0, 410.0),
    S355("S355", 355.0, 490.0);
    override val normReferenz = "DIN EN 10025-1"
}

/**
 * Werkstoff Stahl: fünfte Werkstoff-Subklasse, für Verbindungsmittel,
 * Verbinder und Verstärkungselemente im Holzbau.
 * Glossar: hg_werkstoff_stahl.md
 *
 * Trägt keine Faserrichtung, keine Lagenstruktur, keine
 * Plattenrichtung. Faserrichtungs-Modus = KEINE im Sinne von
 * 3D-Isotropie (siehe hg_faserrichtungs_modus.md).
 *
 * Pflichtfelder: stahlguete plus geerbt von Werkstoff
 *                (faserrichtungsModus = KEINE, produktkennzeichnung).
 * Optionalfelder: streckgrenzeExplizit, zugfestigkeitExplizit (aus
 *                 Stahlgüte ableitbar, optional explizit
 *                 überschreibbar).
 * Plattendicken-Achse: konstant null.
 *
 * Validierung: Konstruktor `internal`; Erzeugung erfolgt
 * ausschliesslich über die Factory `WerkstoffStahl.aus(...)` mit
 * Rückgabetyp `Resultat<WerkstoffStahl, WerkstoffStahlUngueltig>`.
 * Invarianten werden in der Factory geprueft, nicht in `init+require`.
 * Bei Verletzung wird `Resultat.Fehler` zurueckgegeben; es wird nie
 * eine Exception geworfen. Vorbild: `LokalePlatzierung.aus(...)`.
 */
data class WerkstoffStahl internal constructor(
    override val produktkennzeichnung: Produktkennzeichnung,
    val stahlguete: Stahlguete,
    /** Optional explizit; default ableiten aus stahlguete. */
    val streckgrenzeExplizit: Double? = null,
    /** Optional explizit; default ableiten aus stahlguete. */
    val zugfestigkeitExplizit: Double? = null
) : Werkstoff {
    override val faserrichtungsModus: FaserrichtungsModus
        = FaserrichtungsModus.KEINE

    override val plattendickenAchse: Einheitsvektor? = null

    /** Effektive Streckgrenze (explizit oder aus Stahlgüte). */
    val streckgrenze: Double
        get() = streckgrenzeExplizit ?: stahlguete.streckgrenze

    /** Effektive Zugfestigkeit (explizit oder aus Stahlgüte). */
    val zugfestigkeit: Double
        get() = zugfestigkeitExplizit ?: stahlguete.zugfestigkeit

    companion object {
        /**
         * Erzeugt einen WerkstoffStahl. Validierung:
         *  1. streckgrenzeExplizit, sofern gesetzt, > 0.
         *  2. zugfestigkeitExplizit, sofern gesetzt, > 0.
         *  3. produktkennzeichnung kompatibel mit Element-Subklasse
         *     (EN 14592 / EN 14545 / EN 10025-1) — Folgearbeit.
         *  4. streckgrenzeExplizit konsistent mit
         *     stahlguete.streckgrenze innerhalb Norm-Toleranz —
         *     Folgearbeit.
         * Bei Verletzung wird Resultat.Fehler zurueckgegeben.
         */
        fun aus(
            produktkennzeichnung: Produktkennzeichnung,
            stahlguete: Stahlguete,
            streckgrenzeExplizit: Double? = null,
            zugfestigkeitExplizit: Double? = null
        ): Resultat<WerkstoffStahl, WerkstoffStahlUngueltig> = when {
            streckgrenzeExplizit != null && streckgrenzeExplizit <= 0.0 ->
                Resultat.Fehler(WerkstoffStahlUngueltig.StreckgrenzeNichtPositiv)
            zugfestigkeitExplizit != null && zugfestigkeitExplizit <= 0.0 ->
                Resultat.Fehler(WerkstoffStahlUngueltig.ZugfestigkeitNichtPositiv)
            else -> Resultat.Erfolg(
                WerkstoffStahl(
                    produktkennzeichnung,
                    stahlguete,
                    streckgrenzeExplizit,
                    zugfestigkeitExplizit
                )
            )
        }
    }
}

/** Domänen-Fehlerfälle der WerkstoffStahl-Validierung (keine Exceptions). */
sealed interface WerkstoffStahlUngueltig {
    object StreckgrenzeNichtPositiv : WerkstoffStahlUngueltig
    object ZugfestigkeitNichtPositiv : WerkstoffStahlUngueltig
    // weitere Varianten (Produktkennzeichnungs-Kompatibilitaet,
    // Stahlgueten-Konsistenz) in Folgearbeit.
}
```

- **Einheit**: `streckgrenze` und `zugfestigkeit` in N/mm²
  (= MPa). Anzeige in N/mm² (Holzbau-Konvention).
- **Identität**: keine; Werteklasse / data class. Stahl-Werkstoff
  ist durch (Stahlgüte, Produktkennzeichnung) identisch.
- **Invarianten** (ausschliesslich in der Factory
  `WerkstoffStahl.aus(...): Resultat<WerkstoffStahl,
  WerkstoffStahlUngueltig>` prüfen; bei Verletzung
  `Resultat.Fehler` zurückgeben. Kein `init+require` und keine
  Exception; der Konstruktor ist `internal` und wird nur aus der
  Factory aufgerufen. Vorbild: `LokalePlatzierung.aus(...)`):
  1. `faserrichtungsModus == KEINE` (Klassen-Invariante).
  2. `plattendickenAchse == null` (Klassen-Invariante).
  3. `streckgrenze > 0` und `zugfestigkeit > 0`.
  4. Wenn `streckgrenzeExplizit` gesetzt: konsistent mit
     `stahlguete.streckgrenze` innerhalb Norm-Toleranz
     (Folgearbeit; aktuell ohne Strikt-Prüfung).
  5. `produktkennzeichnung` konsistent zur Element-Subklasse
     (EN 14592 / EN 14545 / EN 10025-1).
- **IFC-Mapping** (Persistenzschicht):
  - `IfcMaterial.Name` ← „Stahl " + Stahlgüte (z. B. „Stahl 8.8",
    „Stahl A2-70", „Stahl S355").
  - `IfcMaterial.Category` ← „steel".
  - Property Set `Pset_MaterialSteel` (IFC-Standard) mit
    `YieldStress` ← `streckgrenze`, `UltimateStress` ←
    `zugfestigkeit`.
- **Edge Cases**:
  - **Streckgrenze ohne Stahlgüte** (nur explizit): nicht
    zulässig; Stahlgüte ist Pflichtfeld. Eine Stahlgüte ohne
    Tabellen-Zuordnung wird über `StahlgueteIndividuell` als
    Folge-Subtyp geführt (Folgearbeit).
  - **Stahl mit ungewöhnlichen Eigenschaften** (Sonderlegierungen
    z. B. Wetterfeste Stähle S355J0W): Folgearbeit; eigener
    Stahlgüten-Eintrag.
  - **Verzinkter / Galvanisierter Stahl**: Beschichtung ist
    Korrosionsschutz, kein Werkstoff-Merkmal. Wird in der
    `produktkennzeichnung` geführt (CE-Klasse mit Korrosions-
    Stufe), nicht im Werkstoff selbst.
- **Bezeichner-Konvention** (CLAUDE.md): Domänen-Klasse heißt
  `WerkstoffStahl` (deutsch, Glossarbegriff zusammengezogen, weil
  „Werkstoff Stahl" als Token nicht zulässig).

## Quellen

**Primär (normativ):**

- DIN EN 1993-1-1:2010-12, „Eurocode 3: Bemessung und Konstruktion
  von Stahlbauten – Teil 1-1".
- DIN EN ISO 898-1:2013-05, „Mechanische Eigenschaften von
  Verbindungselementen aus Kohlenstoffstahl und legiertem Stahl
  – Teil 1: Schrauben mit festgelegten Eigenschaften".
- DIN EN ISO 3506-1:2020-08, „Mechanische Eigenschaften von
  Verbindungselementen aus nichtrostenden Stählen – Teil 1:
  Schrauben".
- DIN EN 10088-1:2014-12, „Nichtrostende Stähle – Teil 1:
  Verzeichnis der nichtrostenden Stähle".
- DIN EN 10025-1:2005-02, „Warmgewalzte Erzeugnisse aus
  Baustählen".
- DIN EN 14592:2022-09, „Holzbauwerke – Stiftförmige
  Verbindungsmittel – Anforderungen".
- DIN EN 14545:2009-02, „Holzbauwerke – Verbinder – Anforderungen".
- DIN EN 1995-1-1:2010-12, „Eurocode 5", Abschnitt 8
  (Verbindungen).

**Sekundär:**

- Blass, H. J.; Sandhaas, C.: *Ingenieurholzbau – Grundlagen der
  Bemessung.* KIT Scientific Publishing, Karlsruhe 2016.
- Mönck, W.; Rug, W.: *Holzbau – Bemessung und Konstruktion.*
  16. Aufl., Beuth, Berlin 2015.
- Lignum (Hrsg.): *Holzbautabellen HBT.* Lignum, Zürich.
- Werner, G.; Zimmer, K.; Bohnsack, R.: *Holzbau Teil 2:
  Dach- und Hallentragwerke.* 7. Aufl., Springer Vieweg,
  Wiesbaden 2018.

**Korpus (nicht autoritativ):**

- Würth, SFS, Heco, Spax: Datenblätter Vollgewindeschrauben,
  Holzbauschrauben (abgerufen 2026-05-08).
- Simpson Strong-Tie: Datenblätter Balkenschuhe, Winkel
  (abgerufen 2026-05-08).
- Wikipedia, Lemmata „Festigkeitsklasse (Schrauben)",
  „Nichtrostender Stahl" (abgerufen 2026-05-08).
