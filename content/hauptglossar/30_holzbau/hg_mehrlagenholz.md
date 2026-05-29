---
id: mehrlagenholz
benennung: Mehrlagenholz
synonyme: [Lagenholz, "Holzwerkstoff mit kreuzweise verleimten Lagen", "cross-layered timber"]
abgelehnte_benennungen: [Schichtholz, Lagenwerkstoff, Schichtwerkstoff, "layered wood", "multi-layer timber"]
oberbegriff: werkstoff
begriffstyp: generisch
voraussetzungen: [werkstoff, einheitsvektor, vektor, faserrichtungs_modus, plattendicken_achse, lage, lagenstruktur, haupttragrichtung, nebentragrichtung, festigkeitsklasse, toleranzen]
abgrenzung_zu: [axiales_holz, gerichteter_plattenwerkstoff, isotroper_plattenwerkstoff, werkstoff_stahl, faserrichtung]
status: entwurf
subglossar_pendant: notwendig
quellen_primär:
  - "DIN EN 16351:2021-08, 'Holzbauwerke – Brettsperrholz – Anforderungen' (CLT/BSP/X-LAM)."
  - "DIN EN 636:2015-06, 'Sperrholz – Anforderungen' (Furniersperrholz, Multiplex)."
  - "DIN EN 13986:2015-06, 'Holzwerkstoffe zur Verwendung im Bauwesen – Eigenschaften, Bewertung der Konformität und Kennzeichnung'."
  - "DIN EN 1995-1-1:2010-12 (Eurocode 5), Abschnitt 9 (Plattenwerkstoffe und Bauteile aus Plattenwerkstoffen)."
  - "ETA-06/0138 (KLH Massivholz), ETA-14/0349 (Stora Enso CLT), ETA-12/0281 (Hasslacher CLT), ETA-11/0210 (Binderholz CLT) — exemplarische europäische technische Bewertungen für Brettsperrholz."
  - "ÖNORM B 1995-1-1:2019, nationale Anwendungsbestimmungen zu EC 5, Abschnitt 9."
quellen_sekundär:
  - "Blaß, H. J.; Flaig, M.: Stabförmige Bauteile aus Brettsperrholz. Karlsruher Berichte zum Ingenieurholzbau, Bd. 24, KIT Scientific Publishing, Karlsruhe 2012, DOI 10.5445/KSP/1000030362."
  - "Schickhofer, G.; Bogensperger, T.; Moosbrugger, T. (Hrsg.): BSPhandbuch — Holz-Massivbauweise in Brettsperrholz. 2. Aufl., Verlag der TU Graz 2010."
  - "ProHolz Austria: Brettsperrholz Bemessung Band I — Grundlagen für Statik und Konstruktion. ProHolz Austria, Wien 2014 (Definition Haupttragrichtung 0° = Decklamellen-Richtung mit höherer Steifigkeit)."
  - "Niemz, P.; Sonderegger, W.: Physik des Holzes und der Holzwerkstoffe. Hanser, München 2017, Kap. 7 (Sperrholz, Brettsperrholz, Multiplex)."
  - "Blass, H. J.; Sandhaas, C.: Ingenieurholzbau – Grundlagen der Bemessung. KIT Scientific Publishing, Karlsruhe 2016, Kap. 3 'Holzwerkstoffe'."
quellenkonflikt: |
  Die normative Begriffsabgrenzung zwischen den Subklassen ist klar:
  Brettsperrholz/CLT/BSP/X-LAM (DIN EN 16351), Furniersperrholz
  (DIN EN 636), Multiplex (DIN EN 636 Untergruppe). Es gibt keinen
  normativ etablierten Sammelbegriff für die Werkstoff-Klasse „Holz mit
  mindestens drei kreuzweise verleimten Lagen, deren Faserrichtungen
  lagenweise um 90° wechseln".

  Eigene Festlegung in diesem Glossar (Konvention zur Klassifikation
  der Faserrichtungs-Modi, Memory `project_faserrichtung_modi`):

  - **Mehrlagenholz** ist die Glossar-interne Klassen-Bezeichnung für
    diejenige Werkstoff-Klasse, deren konstitutives Merkmal eine
    Lagenstruktur ≥ 3 Lagen mit kreuzweise wechselnden
    Faserrichtungen ist (Faserrichtungs-Modus STRUKTURIERT).
  - Der Begriff ist **kein normierter Holzbau-Begriff**; er ist eine
    Konvention dieses Glossars, geprägt analog zu „cross-layered" und
    „layered timber".
  - Brettschichtholz / BSH (DIN EN 14080) gehört trotz Lamellen-
    Struktur **nicht** zu Mehrlagenholz, weil alle Lamellen
    **dieselbe** Faserrichtung haben; BSH ist `axiales_holz`.
    Brettsperrholz / BSP (DIN EN 16351) gehört zu Mehrlagenholz, weil
    die Lagen kreuzweise wechseln.
  - Die ProHolz-Definition „Haupttragrichtung (0°) = Decklamellen-
    Richtung mit höherer Steifigkeit" wird übernommen und auf alle
    Subklassen verallgemeinert.
---

## Prosa-Definition

Ein **Mehrlagenholz** ist ein Werkstoff der Klasse Faserrichtungs-
Modus STRUKTURIERT, dessen konstitutives Merkmal eine Lagenstruktur
aus mindestens drei kreuzweise verleimten Lagen ist, deren
Faserrichtungen lagenweise um typischerweise 90° wechseln, der dadurch
keine einheitliche Faserrichtung des Gesamtbauteils, sondern pro Lage
eine eigene Faserrichtung sowie eine abgeleitete Haupttragrichtung
besitzt und der in einer der konkreten Produktnormen-Klassen
Brettsperrholz, Furniersperrholz oder Multiplex ausgeführt ist.

## Mathematische Definition

Sei

- 𝓦 die Menge der Werkstoffe (siehe `werkstoff`),
- S² ⊂ ℝ³ die Einheitssphäre (siehe `einheitsvektor`),
- 𝓛𝓢 die Menge der Lagenstrukturen (eigener Folge-Eintrag
  `lagenstruktur`): geordnete Listen von Lagen-Tupeln
  (siehe `lage`),
- 𝓟_ML die Menge der Produktkennzeichnungen, die für die Subklassen
  Brettsperrholz (DIN EN 16351), Furniersperrholz / Multiplex
  (DIN EN 636) zulässig sind.

Eine **Lage** ℓᵢ ist ein Tupel
(dicke_i ∈ ℝ⁺, faserrichtung_i ∈ S², festigkeitsklasse_i, position_i)
(formale Definition im Folge-Eintrag `lage`).

Eine **Lagenstruktur** L ist eine endliche, geordnete Folge
L = (ℓ₁, …, ℓₙ) mit n ≥ 3.

Dann ist ein **Mehrlagenholz** das Tupel

```
ML := (faserrichtungs_modus, produktkennzeichnung, plattendicken_achse,
       lagenstruktur, haupttragrichtung, nebentragrichtung)
```

mit

- **faserrichtungs_modus** = STRUKTURIERT  (konstant für diese
  Subklasse),
- **produktkennzeichnung** ∈ 𝓟_ML,
- **plattendicken_achse** ∈ S²  (Pflicht: Einheitsvektor in W,
  rechtwinklig zur Plattenebene),
- **lagenstruktur** L = (ℓ₁, …, ℓₙ) ∈ 𝓛𝓢, n ≥ 3,
- **haupttragrichtung** h_hat ∈ S²  (Decklage-Richtung mit höherer
  Steifigkeit, rechtwinklig zu plattendicken_achse:
  ⟨h_hat, plattendicken_achse⟩ = 0 bis Toleranzen.WINKEL_EPS),
- **nebentragrichtung** n_hat ∈ S²  (90° zu h_hat in der Plattenebene;
  abgeleitet aus h_hat und plattendicken_achse durch
  n_hat = plattendicken_achse × h_hat; redundant aber explizit als
  Convenience).

Es ist 𝓜𝓛 ⊂ 𝓦, d. h. die Menge der Mehrlagenhölzer ist eine
disjunkte Teilmenge der Werkstoff-Menge mit
`faserrichtungs_modus = STRUKTURIERT`.

**Validierungsregeln** (im Body als Konstruktions-Invarianten):

1. Mindest-Lagenanzahl: n = |L| ≥ 3.
2. Klassische Symmetrie-Regel für CLT (DIN EN 16351, Standardlayout):
   n ungerade UND ℓ₁.faserrichtung = ℓₙ.faserrichtung
   (Decklage(0).faserrichtung = Decklage(n−1).faserrichtung).
   Diese Regel ist für CLT-Standardlayouts Pflicht; abweichende
   Lagenaufbauten sind zulässig, müssen aber explizit als
   „abweichender Lagenaufbau" markiert werden.
3. Lagenausrichtung: ∀ i ∈ {1, …, n}: ℓᵢ.faserrichtung ist
   parallel oder rechtwinklig zur Haupttragrichtung
   (∠(ℓᵢ.faserrichtung, h_hat) ∈ {0, π/2} bis Toleranzen.WINKEL_EPS),
   ODER explizit als „abweichender Lagenaufbau" markiert
   (z. B. 45°-Lagen für Sonderfälle).
4. Decklage steuert Haupttragrichtung:
   ℓ₁.faserrichtung = h_hat (bis auf Vorzeichen).

**Schnittwinkel pro Lage**: Bei einer angreifenden Kraft F im Bauteil
ist der Faserwinkel α(F, ℓᵢ.faserrichtung) **je Lage** anders. Eine
einzelne „Faserrichtung des Bauteils" gibt es bei Mehrlagenholz
**nicht**.

## Wohldefiniertheit

- **Existenz**: Für jedes Brettsperrholz-, Sperrholz- oder Multiplex-
  Produkt am Markt ist die Lagenstruktur in der ETA bzw. im
  Datenblatt explizit dokumentiert. Die ProHolz-Definition der
  Haupttragrichtung ist eindeutig (Decklage mit höherer Steifigkeit).
- **Eindeutigkeit der Klassifikation**: Die Subklasse
  `mehrlagenholz` ist durch `faserrichtungs_modus = STRUKTURIERT`
  und `|lagenstruktur| ≥ 3` extensional festgelegt. BSH (zwei
  parallele Lamellen) und Balkenschichtholz fallen nicht in diese
  Klasse, sondern in `axiales_holz`.
- **Eindeutigkeit der Haupttragrichtung bis auf Vorzeichen**: h_hat ist
  durch die Decklage bestimmt; Vorzeichenkonvention typisch „h_hat
  zeigt in dieselbe Halbachse wie die längere Plattenformat-Kante"
  oder analog zu IFC `IfcMaterialLayerSet.LayerSetDirection`.
- **Eindeutigkeit der Nebentragrichtung**: n_hat ist algebraisch
  bestimmt durch n_hat = plattendicken_achse × h_hat. Mit
  ⟨h_hat, plattendicken_achse⟩ = 0 ist ‖n_hat‖ = 1; n_hat ∈ S² ist eindeutig
  bis auf das durch das Kreuzprodukt vorgegebene Vorzeichen
  (Rechte-Hand-Regel mit dem Welt-Rechtssystem konsistent).
- **Lagenstruktur-Invarianten**:
  - n = |L| ≥ 3 (sonst ist es Brettschichtholz oder Sperrholz mit
    weniger als 3 Lagen, fällt nicht in diese Klasse).
  - Klassische CLT-Symmetrie ist optional, aber Standard.
- **Plattendicken-Achse Pflicht**: STRUKTURIERT ist Plattenwerkstoff;
  `plattendicken_achse ∈ S²` ist Pflicht (Klassen-Invariante).
- **Norm-Invarianten**: h_hat, n_hat, plattendicken_achse, ℓᵢ.faserrichtung
  erben Norm-Invarianten aus `einheitsvektor`.
- **Nicht-Zirkularität**: Die Definition stützt sich auf
  `werkstoff`, `einheitsvektor`, `vektor`, `toleranzen` und die
  Folge-Begriffe `lagenstruktur`, `lage`, `haupttragrichtung`,
  `nebentragrichtung`, `plattendicken_achse`. Sie verweist nicht auf
  die anderen Werkstoff-Subklassen.

## Erläuterung (nicht normativ)

### Subklassen-Spektrum

| Subklasse | Norm | typ. Lagenanzahl | typ. Lagenstärke |
|-----------|------|------------------|------------------|
| Brettsperrholz / CLT / BSP / X-LAM | DIN EN 16351 | 3, 5, 7 (ungerade) | 20–40 mm pro Lage |
| Furniersperrholz | DIN EN 636 | 3, 5, 7 (ungerade) | ca. 1–4 mm pro Furnier |
| Multiplex | DIN EN 636 (Untergruppe) | ≥ 5 | ca. 1–2 mm pro Furnier |

Allen gemeinsam ist die **kreuzweise wechselnde Faserorientierung**:
benachbarte Lagen stehen typischerweise rechtwinklig zueinander.
Diese Konstruktion neutralisiert das anisotrope Verhalten teilweise
und liefert einen flächigen Werkstoff mit zweidimensionaler
Tragfähigkeit.

### Haupttragrichtung — ProHolz-Definition

ProHolz Austria definiert in „Brettsperrholz Bemessung Band I":

> **Haupttragrichtung (0°)**: Richtung der Decklamellen mit höherer
> Steifigkeit der Platte.

Diese Definition wird hier übernommen und verallgemeinert: bei
Sperrholz und Multiplex ist die Haupttragrichtung die Faserrichtung
der Decklage (außenliegende Furnier-/Lamellenschicht).

Die **Nebentragrichtung (90°)** ist die dazu rechtwinklige Richtung
in der Plattenebene. Sie hat geringere, aber nicht null Steifigkeit
(im Gegensatz zu BSH, wo die Quersteifigkeit annähernd null ist).

### Schnittwinkel-Konsequenz für die App

Die Hankinson-Formel für den Faserwinkel ist bei Mehrlagenholz
**nicht direkt anwendbar**, weil die Faserrichtung pro Lage variiert.
Konsequenz für die Schnittwinkel-Visualisierung dieser App
(Kernfunktion):

> Die Schnittwinkel-Visualisierung muss alle Lagen mit ihren
> Faserrichtungen darstellen; eine einzelne „Faserrichtung des
> Bauteils" ist hier ungeeignet.

Die statische Bemessung von BSP-Bauteilen erfolgt entweder über die
Schubanalogie (γ-Verfahren EC5 Anhang B) oder über die γ-Methode
nach Schickhofer. Bei stabförmigen BSP-Bauteilen (z. B. BSP-Träger)
gilt die Bemessungstheorie nach Blaß/Flaig 2012 (KIT, DOI
10.5445/KSP/1000030362).

### Klassische CLT-Symmetrie

Standard-CLT-Layouts haben eine ungerade Lagenanzahl mit
identischer Faserrichtung in der ersten und letzten Lage:

```
3-lagig:   0° / 90° / 0°
5-lagig:   0° / 90° / 0° / 90° / 0°
7-lagig:   0° / 90° / 0° / 90° / 0° / 90° / 0°
```

Diese Symmetrie macht das Bauteil **zweiseitig gleichwertig** und
verhindert Verzug. Die App erlaubt abweichende Lagenaufbauten
(asymmetrische Layouts, 45°-Lagen für Erdbebenanwendungen,
Diagonalverbund), markiert sie aber explizit.

### Begriffliche Abgrenzung zu BSH

Brettschichtholz (BSH) hat ebenfalls eine Lamellen-Struktur, aber
**alle Lamellen sind parallel** (gleiche Faserrichtung). BSH ist
deshalb Klasse `axiales_holz`, nicht Mehrlagenholz. Das
konstitutive Merkmal des Mehrlagenholzes ist die
**kreuzweise wechselnde** Faserorientierung.

## Beziehungen

- **Oberbegriff**: `werkstoff`.
- **Subklassen** (eigene Einträge folgen):
  - **Brettsperrholz / CLT / BSP / X-LAM** (`brettsperrholz` /
    `clt` / `bsp`): DIN EN 16351, ETAs der Hersteller (KLH,
    Stora Enso, Hasslacher, Binderholz).
  - **Furniersperrholz** (`sperrholz`): DIN EN 636, mehrlagig
    aus dünnen Furnieren.
  - **Multiplex** (`multiplex`): DIN EN 636 Untergruppe,
    typisch ≥ 5 Furnierlagen.
- **Pflichtfelder über `werkstoff` hinaus**:
  - **Lagenstruktur** (`lagenstruktur`, eigener Folge-Eintrag):
    geordnete Liste von Lage-Objekten, n ≥ 3.
  - **Haupttragrichtung** (`haupttragrichtung`, eigener Folge-
    Eintrag): Decklage-Richtung mit höherer Steifigkeit.
  - **Nebentragrichtung** (`nebentragrichtung`, eigener Folge-
    Eintrag): 90° zur Haupttragrichtung in Plattenebene;
    abgeleitet, redundant.
  - **Plattendicken-Achse** (`plattendicken_achse`, eigener Folge-
    Eintrag): rechtwinklig zur Plattenebene.
- **Verwendung**:
  - **Bauteil** (`bauteil`): trägt einen Werkstoff der Subklasse
    `mehrlagenholz`, wenn Flächen-/Volumenbauteil aus BSP/Sperrholz/
    Multiplex.
  - **Brettsperrholz-Element** (`brettsperrholz_element`,
    Folgearbeit): Spezialisierung von Flächenbauteil mit Werkstoff
    Brettsperrholz.
- **Abgrenzung**:
  - **`axiales_holz`**: eine einzige, dominante Faserrichtung
    (Vollholz, KVH, BSH, BSc, LVL). Mehrlagenholz hat **mehrere**
    Faserrichtungen pro Lage.
  - **`gerichteter_plattenwerkstoff`**: schwache Vorzugsrichtung
    in der Plattenebene (OSB), ohne Lagen-Mechanik. OSB hat
    trotz Strand-Schichtung keine bemessungsrelevante
    Einzellagen-Mechanik.
  - **`isotroper_plattenwerkstoff`**: keine Vorzugsrichtung in
    Plattenebene (Spanplatte, MDF, HDF).
  - **`faserrichtung`** (im Sinne des Klasse-A-Glossarbegriffs):
    Einheitsvektor-Annotation an einem Bauteil mit Werkstoff
    `axiales_holz`. Bei Mehrlagenholz wird die geometrische
    Annotation pro Lage geführt, nicht als globale Bauteil-
    Annotation.

## Implementierungshinweis

Datentyp (Domänen-Schicht, Kotlin, Schicht
`domain.holzbau.werkstoff`):

```kotlin
package domain.holzbau.werkstoff

import domain.geometrie.Einheitsvektor
import domain.holzbau.Lagenstruktur     // eigener Eintrag folgt
import domain.identifikation.Produktkennzeichnung

/**
 * Mehrlagenholz: Werkstoff-Klasse mit mindestens drei kreuzweise
 * verleimten Lagen mit lagenweise wechselnder Faserrichtung
 * (Faserrichtungs-Modus STRUKTURIERT).
 * Glossar: hg_mehrlagenholz.md
 *
 * Subklassen: Brettsperrholz / CLT, Sperrholz, Multiplex
 *             (eigene Folge-Klassen).
 *
 * Pflichtfelder: lagenstruktur (n >= 3), haupttragrichtung,
 *                nebentragrichtung, plattendickenAchse.
 *
 * Schnittwinkel-Konsequenz: keine einheitliche Bauteil-Faserrichtung;
 * Visualisierung muss alle Lagen mit ihren Faserrichtungen darstellen.
 */
data class Mehrlagenholz(
    override val produktkennzeichnung: Produktkennzeichnung,
    val lagenstruktur: Lagenstruktur,
    val haupttragrichtung: Einheitsvektor,
    val nebentragrichtung: Einheitsvektor,
    override val plattendickenAchse: Einheitsvektor
) : Werkstoff {
    override val faserrichtungsModus: FaserrichtungsModus
        = FaserrichtungsModus.STRUKTURIERT

    init {
        // 1. lagenstruktur.lagen.size >= 3
        // 2. ⟨haupttragrichtung, plattendickenAchse⟩ <= WINKEL_EPS
        //    (haupttragrichtung orthogonal zur Plattendicken-Achse)
        // 3. ⟨nebentragrichtung, plattendickenAchse⟩ <= WINKEL_EPS
        //    UND ⟨nebentragrichtung, haupttragrichtung⟩ <= WINKEL_EPS
        // 4. nebentragrichtung == plattendickenAchse × haupttragrichtung
        //    (algebraisch konsistent)
        // 5. Klassische CLT-Symmetrie:
        //    optional, aber wenn nicht erfüllt -> Marker
        //    "abweichender Lagenaufbau" gesetzt.
        // 6. Decklage steuert Haupttragrichtung:
        //    lagenstruktur.lagen.first().faserrichtung == haupttragrichtung
        //    (bis auf Vorzeichen).
    }
}
```

- **Einheit**: Vektoren dimensionsloser Einheitsvektor in W;
  Lagendicken in mm.
- **Identität**: Werkstoff trägt keine UUID; Identität auf
  Element-Ebene.
- **Invarianten** (in Fabrikfunktionen / `init` prüfen, bei
  Verletzung `Resultat.Fehler` bzw. `Entartet`-Variante; niemals
  Exception):
  1. `faserrichtungsModus == STRUKTURIERT` (Klassen-Invariante).
  2. `lagenstruktur.lagen.size >= 3`.
  3. `haupttragrichtung` orthogonal zu `plattendickenAchse`
     (innerhalb WINKEL_EPS).
  4. `nebentragrichtung == plattendickenAchse × haupttragrichtung`
     (algebraisch konsistent, NORM_EPS-Toleranz).
  5. Decklage-Konsistenz: `lagenstruktur.lagen.first().faserrichtung`
     stimmt mit `haupttragrichtung` überein (bis auf Vorzeichen).
  6. Lagenausrichtung: alle Lagen-Faserrichtungen parallel oder
     rechtwinklig zur Haupttragrichtung, ODER Marker
     „abweichender Lagenaufbau" gesetzt.
  7. Klassische CLT-Symmetrie (Decklage 0 = Decklage n−1, n
     ungerade): optional, Standard für CLT.
- **IFC-Mapping** (Persistenzschicht):
  - `IfcMaterialLayerSet` mit `IfcMaterialLayer` pro Lage.
  - `LayerSetDirection` = `AXIS3` (Plattendicken-Achse).
  - `IfcMaterialLayer.LayerThickness` = Lagendicke.
  - Property Set `Pset_MaterialWoodBasedPanel`.
- **Edge Cases**:
  - **Lagenstruktur mit < 3 Lagen**: nicht zulässig in dieser
    Klasse; `Entartet.MehrlagenholzZuWenigeLagen`. Zwei parallele
    Lagen sind Balkenschichtholz (`axiales_holz`); zwei kreuzweise
    Lagen sind ein Sonderfall, der nicht zu STRUKTURIERT zählt.
  - **Asymmetrischer Lagenaufbau**: zulässig mit explizitem
    Marker; in der App ist eine Eigenschaft `abweichenderLagenaufbau:
    Boolean` zu führen (Folgearbeit, Eintrag `lagenstruktur`).
  - **45°-Lagen** (Erdbebenanwendung, Sonderfall): zulässig mit
    explizitem Marker; Lagenausrichtungs-Invariante 6 wird durch
    den Marker ausgesetzt.
  - **Schnittwinkel-Anfrage**: liefert eine Liste von Faser-
    winkeln je Lage, nicht einen einzelnen Wert. Funktion
    `faserwinkelProLage(F: Vektor): List<Double>`.
- **Bezeichner-Konvention** (CLAUDE.md): Domänen-Klasse heißt
  `Mehrlagenholz` (deutsch, Glossarbegriff); Sub-Subklassen heißen
  `Brettsperrholz` (Synonym `Clt`, `Bsp`), `Sperrholz`, `Multiplex`.

## Quellen

**Primär (normativ):**

- DIN EN 16351:2021-08, „Holzbauwerke – Brettsperrholz –
  Anforderungen".
- DIN EN 636:2015-06, „Sperrholz – Anforderungen".
- DIN EN 13986:2015-06, „Holzwerkstoffe zur Verwendung im
  Bauwesen".
- DIN EN 1995-1-1:2010-12, „Eurocode 5: Bemessung und Konstruktion
  von Holzbauten – Teil 1-1", Abschnitt 9.
- ETA-06/0138 (KLH Massivholz), ETA-14/0349 (Stora Enso CLT),
  ETA-12/0281 (Hasslacher CLT), ETA-11/0210 (Binderholz CLT).
- ÖNORM B 1995-1-1:2019.

**Sekundär:**

- Blaß, H. J.; Flaig, M.: *Stabförmige Bauteile aus Brettsperrholz.*
  Karlsruher Berichte zum Ingenieurholzbau, Bd. 24, KIT
  Scientific Publishing, Karlsruhe 2012, DOI
  10.5445/KSP/1000030362.
- Schickhofer, G.; Bogensperger, T.; Moosbrugger, T. (Hrsg.):
  *BSPhandbuch — Holz-Massivbauweise in Brettsperrholz.* 2. Aufl.,
  TU Graz 2010.
- ProHolz Austria: *Brettsperrholz Bemessung Band I.* ProHolz
  Austria, Wien 2014.
- Niemz, P.; Sonderegger, W.: *Physik des Holzes und der
  Holzwerkstoffe.* Hanser, München 2017.
- Blass, H. J.; Sandhaas, C.: *Ingenieurholzbau – Grundlagen der
  Bemessung.* KIT Scientific Publishing, Karlsruhe 2016.

**Korpus (nicht autoritativ):**

- BIMwood-Pset (in Entwicklung), buildingSMART
  (abgerufen 2026-05-08).
- Wikipedia, Lemmata „Brettsperrholz", „Sperrholz", „Multiplexplatte"
  (abgerufen 2026-05-08).
