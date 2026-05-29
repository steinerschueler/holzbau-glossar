---
id: faserrichtung
benennung: Faserrichtung
synonyme: [Holzfaserrichtung, Faserlaengsachse, "lokale Materialachse (parallel)"]
abgelehnte_benennungen: [Maserung, Wuchsrichtung, Faserung, "grain direction", "fibre direction"]
oberbegriff: einheitsvektor
begriffstyp: merkmal
voraussetzungen: [vektor, einheitsvektor, faserrichtungs_modus, toleranzen]
abgrenzung_zu: [einheitsvektor, vektor, bauteilachse, faserneigung, faserrichtungs_modus, haupttragrichtung, plattenlaengsrichtung, plattendicken_achse, lagenstruktur, axiales_holz, mehrlagenholz, gerichteter_plattenwerkstoff, isotroper_plattenwerkstoff, hankinson_winkel]
status: entwurf
theorie_pflichtig: required
quellen_primär:
  - "SIA 265:2021, 'Holzbau', Schweizerischer Ingenieur- und Architektenverein, Abschnitt 3 (Werkstoffe) und Abschnitt 4 (Bemessung), Festigkeiten parallel und senkrecht zur Faser."
  - "DIN EN 1995-1-1:2010-12 (Eurocode 5), 'Bemessung und Konstruktion von Holzbauten – Teil 1-1: Allgemeines', Abschnitt 2.3 (Grundvariablen) und Abschnitt 3 (Werkstoffeigenschaften), Festigkeitsangaben f_{c,0,k}, f_{c,90,k}, f_{t,0,k}, f_{t,90,k}, σ_{m,α,d} mit Faserwinkel α."
  - "DIN 4074-1:2012-06, 'Sortierung von Holz nach der Tragfähigkeit – Teil 1: Nadelschnittholz', Abschnitt 5 (Sortiermerkmale), Faserneigung als Sortierkriterium."
quellen_sekundär:
  - "Wagenführ, R.: Holzatlas. 6. Aufl., Fachbuchverlag Leipzig 2007, Kap. 2 'Bau und Eigenschaften des Holzes'."
  - "Niemz, P.; Sonderegger, W.: Holzphysik. Hanser, München 2017, Kap. 3 'Anatomischer Aufbau' und Kap. 6 'Mechanische Eigenschaften' (Anisotropie längs/radial/tangential)."
  - "Mönck, W.; Rug, W.: Holzbau – Bemessung und Konstruktion. 16. Aufl., Beuth, Berlin 2015, Kap. 1 'Werkstoff Holz'."
  - "Blass, H. J.; Sandhaas, C.: Ingenieurholzbau – Grundlagen der Bemessung. KIT Scientific Publishing, Karlsruhe 2016, Kap. 2 'Werkstoff Holz'."
quellenkonflikt: |
  SIA 265, EN 1995-1-1 und DIN 4074-1 verwenden „Faserrichtung" bzw.
  „Richtung der Holzfaser" als gegebenen Begriff in Festigkeits- und
  Sortiervorschriften, definieren ihn jedoch nicht formal als
  geometrische Größe. EN 1995-1-1 und SIA 265 unterscheiden lediglich
  die Belastungsfälle „parallel zur Faser" (Index 0) und „senkrecht zur
  Faser" (Index 90) und führen einen Faserwinkel α zwischen Kraft- und
  Faserrichtung ein. DIN 4074-1 definiert die „Faserneigung" als
  Tangens des Winkels zwischen Faser und Bauteillängsachse, fixiert die
  Faserrichtung selbst aber nicht als Vektor. Eigene Festlegung: die
  Faserrichtung eines Bauteils ist ein Einheitsvektor im
  Welt-Koordinatensystem, der die idealisierte lokale Hauptachse der
  Holzfaser angibt; die Faserneigung nach DIN 4074-1 ist eine daraus
  abgeleitete skalare Größe (Winkel zwischen Faserrichtung und
  Bauteillängsachse). Diese Festlegung ist konsistent mit allen
  konsultierten Quellen und schließt die in EN 1995-1-1 erforderliche
  Berechnung von σ_{m,α,d} formal an.
---

## Prosa-Definition

Die **Faserrichtung** eines Bauteils aus Holz oder Holzwerkstoff ist
ein Einheitsvektor im Welt-Koordinatensystem, der die idealisierte
lokale Hauptachse des Holzfaserverlaufs (Längsfaser, parallel zur
Stammachse des verwendeten Rundholzes) am Bauteil angibt und damit
die Bezugsrichtung für alle anisotropen mechanischen Eigenschaften
des Werkstoffs definiert.

## Mathematische Definition

Sei

- B ein Bauteil aus Vollholz, Brettschichtholz oder einem Holzwerkstoff
  mit ausgewiesener Hauptfaserrichtung (Bauteil-Begriff in Folgearbeit;
  hier nur als annotierter Träger vorausgesetzt),
- f_hat ∈ S² ⊂ ℝ³ ein Einheitsvektor (siehe `einheitsvektor`).

Dann ist die **Faserrichtung** des Bauteils B eine Annotation

```
faserrichtung(B) := f_hat ∈ S²,
```

die die idealisierte lokale Längsachse des Holzfaserverlaufs in B
angibt. Die mechanischen Festigkeits- und Steifigkeitskennwerte des
Werkstoffs werden bezüglich dieser Achse als Bezugsrichtung
spezifiziert (parallel zur Faser: Index 0; senkrecht zur Faser:
Index 90; siehe SIA 265 und EN 1995-1-1).

**Faserwinkel** zu einer beliebigen Richtung r_hat ∈ S² (z. B. Richtung
der angreifenden Kraft, Richtung einer Bauteilachse): der Winkel
α(f_hat, r_hat) ∈ [0, π/2] zwischen Faserrichtung und r_hat ist

```
α(f_hat, r_hat) := arccos( | ⟨f_hat, r_hat⟩ | ),
```

wobei der Betrag des Skalarproduktes die antipodale Mehrdeutigkeit
{f_hat, −f_hat} berücksichtigt: die Faserrichtung ist physikalisch eine
ungerichtete Achse, die mathematische Repräsentation als
Einheitsvektor wählt willkürlich eines der beiden Vorzeichen.

**Faserneigung** nach DIN 4074-1: ist a die Bauteillängsachse des
Bauteils B (siehe `bauteilachse`, in Folgearbeit), so ist die
Faserneigung

```
tan(α(f_hat, a_hat)) = sin(α(f_hat, a_hat)) / cos(α(f_hat, a_hat))
```

der Tangens des Winkels zwischen Faserrichtung und Bauteillängsachse.

## Wohldefiniertheit

- **Existenz**: Für jedes Bauteil aus Vollholz oder Brettschichtholz
  mit anatomisch klar definiertem Längsfaserverlauf ist die
  Faserrichtung als Einheitsvektor festgelegt; der Idealisierungs-
  schritt (Mittelung über lokale Faserabweichungen) wird in der
  Erläuterung ausgewiesen.
- **Eindeutigkeit bis auf Vorzeichen**: f_hat ist als Annotation eines
  Bauteils eindeutig, sobald eine Vorzeichenkonvention festgelegt ist
  (z. B. „f_hat zeigt in die positive Richtung der Bauteillängsachse").
  Ohne Konvention ist die Faserrichtung ein Element von S²/{±1}
  (projektive Linie), repräsentiert durch das antipodale Paar
  {f_hat, −f_hat}.
- **Wohldefiniertheit des Faserwinkels**: α(f_hat, r_hat) ∈ [0, π/2] ist
  durch den Betrag des Skalarproduktes invariant unter
  Vorzeichenwechsel von f_hat und r_hat; damit ist α unabhängig von der
  Vorzeichenkonvention.
- **Numerische Wohldefiniertheit**: f_hat erbt die Norm-Invariante
  | ‖f_hat‖² − 1 | ≤ NORM_EPS aus `einheitsvektor`. Der Faserwinkel ist
  numerisch stabil, da arccos auf [0, 1] gut konditioniert ist und
  | ⟨f_hat, r_hat⟩ | ∈ [0, 1] für Einheitsvektoren f_hat, r_hat gilt.
- **Nicht-Zirkularität**: Die Definition verwendet ausschließlich
  `einheitsvektor` und `toleranzen` sowie den noch nicht definierten
  Begriff `bauteil` als bloßen Träger der Annotation. Sie kommt nicht
  in ihrer eigenen Definition vor.

## Erläuterung (nicht normativ)

### Geltungsbereich (werkstoffklassen-spezifisch)

Faserrichtung im engen Sinn — als ein einzelner Vektor f_hat ∈ S² am
Bauteil — ist nur bei der Werkstoff-Subklasse `axiales_holz`
sinnvoll definiert (Faserrichtungs-Modus HART, siehe
`faserrichtungs_modus` und Memory `project_faserrichtung_modi`).
Für die übrigen Werkstoff-Subklassen treten andere Begriffe an die
Stelle der Faserrichtung:

| Werkstoff-Subklasse              | Modus         | Bauteilebene-Begriff                          |
|----------------------------------|---------------|-----------------------------------------------|
| `axiales_holz`                   | HART          | `faserrichtung` (dieser Eintrag)              |
| `mehrlagenholz`                  | STRUKTURIERT  | `lagenstruktur` + `haupttragrichtung`         |
| `gerichteter_plattenwerkstoff`   | SCHWACH       | `plattenlaengsrichtung`                       |
| `isotroper_plattenwerkstoff`     | KEINE         | (in Plattenebene undefiniert)                 |

Die Diskriminante, welcher Begriff am konkreten Bauteil pflichtig
ist, ist der `faserrichtungs_modus` der Werkstoff-Subklasse. Bei
Mehrlagenholz ist die Faserrichtung **lagenweise** definiert
(`lage.faserrichtung` jeder Einzellage), auf Bauteilebene jedoch
nicht — dort wirkt `haupttragrichtung`. Bei gerichteten
Plattenwerkstoffen (OSB) ist die Hauptachse der Decklagen-Strands
schwach ausgeprägt, aber bemessungsrelevant — sie heißt
`plattenlaengsrichtung`. Bei isotropen Plattenwerkstoffen
(Spanplatte, MDF, HDF) ist eine Faserrichtung in der Plattenebene
physikalisch und normativ undefiniert.

### Hankinson-Winkel

Der **Hankinson-Winkel** α(F_hat, f_hat) zwischen einer Kraftrichtung F_hat
und der Faserrichtung f_hat (siehe `hankinson_winkel`) ist die
zentrale Eingangsgröße der Hankinson-Formel für die
richtungsabhängige Lochleibungs- und Druckfestigkeit nach
DIN EN 1995-1-1. Er ist gleich dem oben definierten Faserwinkel
α(f_hat, F_hat) ∈ [0, π/2] und unterliegt derselben antipodalen
Vorzeicheninvarianz.

### Anisotropie und Idealisierung

Holz ist ein **anisotroper Werkstoff**: seine mechanischen
Eigenschaften (Druck-, Zug-, Biegefestigkeit, E-Modul) hängen stark
davon ab, in welchem Winkel die Last zur Faserrichtung wirkt. Ein
Sparren aus Fichte hält bei Druck parallel zur Faser etwa
f_{c,0,k} ≈ 21 N/mm² aus, rechtwinklig zur Faser nur etwa
f_{c,90,k} ≈ 2,5 N/mm² — ein Faktor von rund acht. Aus diesem Grund
ist die Faserrichtung kein dekoratives Attribut, sondern eine
**bemessungsrelevante geometrische Größe**.

Der Glossarbegriff bezeichnet eine **Idealisierung**:

- Im Realholz weicht die lokale Faserrichtung an jeder Stelle des
  Bauteils geringfügig von einer mittleren Hauptrichtung ab
  (Faserabweichung, Drehwuchs, Faserstörung um Äste). DIN 4074-1
  beschränkt diese Abweichung über die **Faserneigung** als
  Sortiermerkmal (z. B. ≤ 1:10 für Sortierklasse S10).
- Im Glossarbegriff ist die Faserrichtung eine **mittlere
  Hauptrichtung** über das Bauteil; lokale Abweichungen werden auf
  der Werkstoffseite (Festigkeitsklasse) erfasst, nicht auf der
  geometrischen Seite.

Bei **Brettschichtholz** ist die Faserrichtung jeder einzelnen
Lamelle annähernd parallel zur Bauteillängsachse; die makroskopische
Faserrichtung des Bauteils stimmt im Regelfall mit der
Bauteillängsachse überein. Bei **Keilzinkenstößen** und
Universal-Zinkenverbindungen ist die Faserrichtung **lokal
mehrdeutig**: an der Verbindungsstelle laufen Fasern verschiedener
Stäbe in verschiedenen Richtungen. Im Glossar wird die Faserrichtung
für solche Verbindungen **nicht** auf der Verbindungsgeometrie
definiert, sondern bleibt eine Annotation der einzelnen
verbundenen Bauteile.

In der Holzkonstruktion stimmt die Faserrichtung **typischerweise**
mit der Bauteillängsachse überein (Sparren, Pfette, Ständer:
Faserrichtung längs des Stabes). Sie kann aber **abweichen**:

- **Schräg gesägtes Holz** (etwa für Sparrenfußklötze, Auswechslungen):
  die Faser läuft schräg zur Bauteillängsachse.
- **Verzogene Hölzer**: die Faser ist nicht mehr exakt parallel zur
  ursprünglichen Stammachse.
- **Drehwuchs**: die Faser folgt einer schraubenförmigen Bahn um die
  Stammachse, der Mittelwert weicht von der geraden Längsachse ab.
- **Plattenwerkstoffe** (Sperrholz, OSB, Brettsperrholz mit
  gekreuzten Lagen): keine einzige globale Faserrichtung;
  stattdessen mehrere Lagen mit jeweils eigener Faserrichtung.
  Solche Werkstoffe sind durch den vorliegenden Glossarbegriff nicht
  direkt abgedeckt, sondern durch die Geschwister-Begriffe
  `mehrlagenholz` mit `lagenstruktur` und `haupttragrichtung`,
  `gerichteter_plattenwerkstoff` mit `plattenlaengsrichtung`,
  `isotroper_plattenwerkstoff` (Plattenebene faserrichtungslos).

## Beziehungen

- **Oberbegriff**: `einheitsvektor`. Strukturell ist die Faserrichtung
  ein Einheitsvektor; das Holzbau-Spezifikum ist die semantische
  Rolle „Materialhauptachse parallel zum Faserverlauf".
- **Verwendungskontext (nachgelagert, noch nicht definiert)**:
  - **Bauteil** (`bauteil`, in Folgearbeit): Träger der Annotation
    Faserrichtung. Jedes Vollholz- oder Brettschichtholz-Bauteil
    erhält genau eine Faserrichtung; Plattenwerkstoffe mit
    gekreuzten Lagen bleiben außerhalb des Geltungsbereichs.
  - **Sparren**, **Pfette**, **Ständer** (`sparren`, `pfette`,
    `staender`, in Folgearbeit): Spezialisierungen von Bauteil mit
    typischer Übereinstimmung Faserrichtung ≈ Bauteillängsachse.
- **Abgrenzung**:
  - **`einheitsvektor`** (allgemein): trägt keine semantische Rolle.
    Eine Faserrichtung ist ein Einheitsvektor in der spezifischen
    Rolle „Materialhauptachse"; ein Normalenvektor einer Ebene oder
    eine Geraden-Richtung sind Einheitsvektoren in anderen Rollen.
    Auf der Ebene der Geometrie sind alle drei strukturell gleich.
  - **`bauteilachse`** (geometrische Längsachse, in Folgearbeit):
    die geometrische Hauptachse des Bauteils, definiert über
    Bauteilgeometrie (z. B. Schwerlinie des Querschnittsschwerpunkt-
    verlaufs, Kantenrichtung des umhüllenden Quaders).
    Faserrichtung und Bauteilachse **können** übereinstimmen, müssen
    es aber nicht (siehe Erläuterung). Der Winkel zwischen ihnen ist
    die **Faserneigung** nach DIN 4074-1.
  - **`faserneigung`** (in Folgearbeit, falls erforderlich): skalare
    Größe (Tangens oder Winkel) zwischen Faserrichtung und
    Bauteillängsachse. Begriffstyp `merkmal` als
    Sortier-/Festigkeitsattribut, abgeleitet aus `faserrichtung` und
    `bauteilachse`.
  - **„Maserung"**, **„Wuchsrichtung"**: umgangssprachliche bzw.
    optische Begriffe; nicht synonym zur geometrischen
    Faserrichtung. „Maserung" bezeichnet das sichtbare Muster der
    Jahrringe, nicht die mechanisch relevante Längsfaserachse.
  - **`haupttragrichtung`** (für Mehrlagenholz, BSP/CLT, Sperrholz):
    Vektor in der Plattenebene mit höherer Decklagen-Steifigkeit;
    tritt an die Stelle der Faserrichtung auf Bauteilebene, da bei
    gekreuzten Lagen keine einheitliche globale Faserrichtung
    existiert.
  - **`plattenlaengsrichtung`** (für gerichtete Plattenwerkstoffe,
    OSB): schwach ausgeprägte Vorzugsrichtung der Decklagen-Strands;
    auf Bauteilebene Pflichtfeld bei OSB.
  - **`plattendicken_achse`** (für alle Plattenwerkstoffe):
    Einheitsvektor rechtwinklig zur Plattenebene; orthogonal sowohl zu
    `haupttragrichtung` als auch zu `plattenlaengsrichtung`.
  - **`lagenstruktur`** (für Mehrlagenholz): Liste von Einzellagen
    mit jeweils eigener Faserrichtung pro Lage. Die globale
    Faserrichtung des Bauteils existiert dort nicht — Faserrichtung
    ist auf Lagenebene zerlegt.
  - **`faserrichtungs_modus`**: Diskriminante, die je Werkstoff-
    Subklasse festlegt, welcher dieser Begriffe am Bauteil
    pflichtig ist (HART → Faserrichtung; STRUKTURIERT →
    Lagenstruktur + Haupttragrichtung; SCHWACH →
    Plattenlängsrichtung; KEINE → nur Plattendickenachse).
  - **`hankinson_winkel`** (`hankinson_winkel`): aus Faserrichtung
    und Kraftrichtung abgeleiteter Winkel α ∈ [0, π/2], Eingang in
    die Hankinson-Formel für richtungsabhängige Festigkeit.

## Implementierungshinweis

Datentyp (Domänen-Schicht, Kotlin, Schicht `domain.holzbau`):

```
package domain.holzbau

import domain.geometrie.Einheitsvektor

/**
 * Faserrichtung eines Bauteils: Einheitsvektor in der Rolle
 * 'lokale Hauptachse der Holzfaser parallel zur Stammachse'.
 * Glossar: hg_faserrichtung.md
 *
 * Strukturell ein Wrapper um Einheitsvektor, der die semantische
 * Rolle typsicher kommuniziert. Verhindert Verwechslung mit anderen
 * Einheitsvektor-Rollen (Normalenvektor, Achsenrichtung) am API-Rand.
 */
@JvmInline
value class Faserrichtung(val richtung: Einheitsvektor) {

    /**
     * Faserwinkel zu einer beliebigen Richtung r_hat. Ergebnis in [0, π/2].
     * Berücksichtigt die antipodale Mehrdeutigkeit der Faserachse durch
     * Betrag des Skalarproduktes.
     * Glossar: faserrichtung#faserwinkel.
     */
    fun faserwinkel(r: Einheitsvektor): Double {
        val cos = kotlin.math.abs(
            richtung.x * r.x + richtung.y * r.y + richtung.z * r.z
        ).coerceIn(0.0, 1.0)
        return kotlin.math.acos(cos)
    }
}
```

- **Einheit**: dimensionslos (geerbt von `einheitsvektor`).
- **Invariante**: alle Invarianten von `Einheitsvektor`, insbesondere
  | ‖f_hat‖² − 1 | ≤ Toleranzen.NORM_EPS.
- **Vorzeichenkonvention**: Wird mit der Konstruktion eines Bauteils
  festgelegt, in der Regel „f_hat zeigt in dieselbe Halbachse wie die
  Bauteillängsachse von Anfangs- zu Endpunkt". Diese Konvention ist
  beim jeweiligen Bauteil zu dokumentieren; der Faserwinkel ist
  vorzeicheninvariant.
- **Edge Cases**:
  - **Bauteil ohne wohldefinierte Faserrichtung** (Plattenwerkstoffe
    mit gekreuzten Lagen, Holzwerkstoffe mit isotroper Verteilung):
    nicht durch diesen Typ abgedeckt. Solche Bauteile erhalten
    entweder mehrere Faserrichtungen pro Lage oder einen separaten
    Werkstoff-Begriff in Folgearbeit.
  - **Verbindungsstelle (Keilzinken, Zapfen, Versatz)**: lokale
    Faserrichtung mehrdeutig; die Annotation `Faserrichtung` ist
    Eigenschaft des einzelnen Bauteils, nicht der Verbindung.
    Verbindungen werden auf der Verbindungs-Geometrieebene separat
    behandelt.
  - **Drehwuchs/Faserabweichung über Bauteillänge**: durch die
    Idealisierung als einzelner Einheitsvektor nicht erfasst. Die
    Sortierklasse (DIN 4074-1) begrenzt die zulässige Abweichung;
    eine ortsabhängige Faserrichtung wäre eine künftige
    Verfeinerung (Vektorfeld f_hat(x) auf dem Bauteilkörper).
  - **Faserrichtung antiparallel zur Bauteillängsachse**: zulässig.
    Der Faserwinkel zu antipodalen Richtungen ist 0 (nicht π); die
    Implementierung verwendet `abs(skalarprodukt)`.
- **Verwendungsregel**: Funktionen, die werkstoffabhängige
  Festigkeiten oder Steifigkeiten berechnen, nehmen `Faserrichtung`
  als Parametertyp und nicht den nackten `Einheitsvektor`. Dadurch
  wird die semantische Rolle am API-Rand sichtbar und Vertauschungen
  mit Normalenvektoren oder Bauteillängsachsen werden zur
  Compile-Zeit verhindert.

## Quellen

**Primär (normativ):**

- SIA 265:2021, „Holzbau", Schweizerischer Ingenieur- und
  Architektenverein, Zürich.
- DIN EN 1995-1-1:2010-12, „Eurocode 5: Bemessung und Konstruktion
  von Holzbauten – Teil 1-1: Allgemeines – Allgemeine Regeln und
  Regeln für den Hochbau".
- DIN 4074-1:2012-06, „Sortierung von Holz nach der Tragfähigkeit –
  Teil 1: Nadelschnittholz".

**Sekundär:**

- Wagenführ, R.: *Holzatlas.* 6. Auflage, Fachbuchverlag Leipzig 2007.
- Niemz, P.; Sonderegger, W.: *Holzphysik – Eigenschaften, Prüfung
  und Kennwerte.* Hanser, München 2017.
- Mönck, W.; Rug, W.: *Holzbau – Bemessung und Konstruktion.*
  16. Auflage, Beuth, Berlin 2015.
- Blass, H. J.; Sandhaas, C.: *Ingenieurholzbau – Grundlagen der
  Bemessung.* KIT Scientific Publishing, Karlsruhe 2016.

**Korpus (nicht autoritativ):**

- Holzbau Deutschland, Merkblatt „Begriffe und Klassifizierungen für
  den Holzbau" (abgerufen 2026-05-08).
- Wikipedia, Lemma „Holz – Anatomie" (abgerufen 2026-05-08).
