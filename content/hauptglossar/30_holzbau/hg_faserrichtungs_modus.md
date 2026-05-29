---
id: faserrichtungs_modus
benennung: Faserrichtungs-Modus
synonyme: ["Anisotropie-Modus", "Faserrichtungs-Klasse", "Werkstoff-Anisotropieklasse"]
abgelehnte_benennungen: [Anisotropie, Orthotropie, "fiber mode", "grain mode", Faserklasse, Faserrichtungstyp]
oberbegriff: null
begriffstyp: merkmal
voraussetzungen: [werkstoff, toleranzen]
abgrenzung_zu: [werkstoff, faserrichtung, festigkeitsklasse, plattendicken_achse, haupttragrichtung]
status: entwurf
subglossar_pendant: notwendig
quellen_primär:
  - "DIN EN 1995-1-1:2010-12 (Eurocode 5), 'Bemessung und Konstruktion von Holzbauten – Teil 1-1', Abschnitt 3 (Werkstoffeigenschaften), Abschnitt 6.1.5–6.1.7 (Beanspruchungen unter Winkel zur Faser, Hankinson-Formel) und Abschnitt 9 (Plattenwerkstoffe)."
  - "DIN EN 13986:2015-06, 'Holzwerkstoffe zur Verwendung im Bauwesen', Tabelle 1 (Werkstoff-Klassifikation: Vollholz / BSH / LVL / CLT / Sperrholz / OSB / Spanplatte / Faserplatte)."
  - "DIN EN 16351:2021-08 (Brettsperrholz), DIN EN 14080:2013-09 (BSH), DIN EN 14081-1:2019-10 (Vollholz), DIN EN 14374:2005-02 (LVL), DIN EN 636:2015-06 (Sperrholz), DIN EN 300:2006-09 (OSB), DIN EN 312:2010-12 (Spanplatten), DIN EN 622-2/3/5 (Faserplatten)."
  - "DIN EN 12369-1:2001-04, 'Charakteristische Werte für die Berechnung und Bemessung von Holzbauwerken – Teil 1: OSB, Spanplatten und Faserplatten' (eine einzige Festigkeit pro Beanspruchungsart bei Spanplatte/Faserplatte; f_m,0 und f_m,90 bei OSB)."
quellen_sekundär:
  - "Niemz, P.; Sonderegger, W.: Physik des Holzes und der Holzwerkstoffe. Hanser, München 2017, Kap. 6 (Mechanische Eigenschaften, Orthotropie L/R/T) und Kap. 7 (Holzwerkstoffe)."
  - "Blass, H. J.; Sandhaas, C.: Ingenieurholzbau – Grundlagen der Bemessung. KIT Scientific Publishing, Karlsruhe 2016, Kap. 2 und 3."
  - "ProHolz Austria: Brettsperrholz Bemessung Band I — Grundlagen für Statik und Konstruktion. Wien 2014 (Definition Haupttragrichtung 0° als Decklamellen-Richtung mit höherer Steifigkeit)."
  - "Schickhofer, G.; Bogensperger, T.; Moosbrugger, T. (Hrsg.): BSPhandbuch — Holz-Massivbauweise in Brettsperrholz. 2. Aufl., TU Graz 2010."
quellenkonflikt: |
  Keine normative Quelle führt einen Sammelbegriff für die Anisotropie-
  Klassifikation der Holzwerkstoffe; DIN EN 1995-1-1, DIN EN 13986 und
  die werkstoffspezifischen Produktnormen klassifizieren je Werkstoff,
  ohne eine Werkstoff-übergreifende Modus-Aufzählung zu definieren.

  Konfliktfrei in der konsultierten Literatur ist:

  - Vollholz, KVH, BSH, LVL haben eine einzige, dominante Faserrichtung
    (DIN EN 14080, DIN EN 14081-1, DIN EN 14374; Niemz/Sonderegger 2017).
  - CLT/BSP und Sperrholz haben pro Lage eine Faserrichtung mit kreuz-
    weise wechselnder Orientierung (DIN EN 16351, DIN EN 636;
    ProHolz 2014; Schickhofer 2010).
  - OSB hat eine schwache, bemessungsrelevante Vorzugsrichtung in der
    Plattenebene (DIN EN 300; DIN EN 12369-1 mit f_m,0 und f_m,90).
  - Spanplatten P4–P7, MDF, HDF und harte Faserplatten haben in der
    Plattenebene keine Vorzugsrichtung (DIN EN 12369-1: eine einzige
    Festigkeit pro Beanspruchungsart in der Plattenebene; quasi-
    isotrop).

  Eigene Festlegung in diesem Glossar (Memory `project_faserrichtung_modi`):

  - Der **Faserrichtungs-Modus** ist ein Aufzählungstyp mit genau vier
    Werten { HART, STRUKTURIERT, SCHWACH, KEINE }, die die vier
    konfliktfrei aus der Literatur ableitbaren Anisotropie-Klassen
    repräsentieren.
  - Die Werkstoff-Subklassen `axiales_holz`, `mehrlagenholz`,
    `gerichteter_plattenwerkstoff` sind durch genau einen festen Modus
    charakterisiert (HART, STRUKTURIERT, SCHWACH). Der Modus KEINE
    wird sowohl von `isotroper_plattenwerkstoff` (in Plattenebene
    quasi-isotrop) als auch von `werkstoff_stahl` (3D-isotrop)
    getragen — er steht für **„keine ausgezeichnete Faserrichtung im
    bemessungsrelevanten Sinn"**, unabhängig davon, ob die Isotropie
    in einer Plattenebene oder im Vollraum vorliegt. Die
    Modus-Subklassen-Zuordnung ist daher **keine Bijektion**: die
    drei nicht-isotropen Modi sind injektiv den entsprechenden
    Subklassen zugeordnet, während KEINE auf zwei Subklassen
    abbildet. Die Disjunktheit der beiden KEINE-Subklassen wird
    durch die sealed-Hierarchie auf der Werkstoff-Ebene getragen,
    nicht durch den Modus.
  - Der Faserrichtungs-Modus ist **bemessungsrelevant**, nicht
    Annotation: er bestimmt das Pflichtfeld-Profil im Datenmodell
    bezogen auf die Faserrichtungs-Annotationen (`faserrichtung`,
    `lagenstruktur`, `haupttragrichtung`, `plattenlaengsrichtung`)
    und die Anwendbarkeit der Hankinson-Formel. Plattendicken-Achse
    und Stahl-spezifische Felder werden zusätzlich subklassen-bezogen
    geführt, nicht modus-bezogen.
  - Die in EC5 vorhandene Belastungsfall-Indizierung (0 = parallel
    zur Faser, 90 = rechtwinklig zur Faser) ist durch diesen Modus
    formal interpretierbar:
    HART → ein Faserwinkel α, Hankinson direkt anwendbar.
    STRUKTURIERT → ein Faserwinkel je Lage.
    SCHWACH → eine Plattenlängsrichtung, Hankinson abgeschwächt.
    KEINE → kein Faserwinkel anwendbar (bei
    `isotroper_plattenwerkstoff` durch in-Plattenebene-Isotropie,
    bei `werkstoff_stahl` durch 3D-Isotropie).
---

## Prosa-Definition

Der **Faserrichtungs-Modus** ist ein Aufzählungswert aus genau vier
Modi { HART, STRUKTURIERT, SCHWACH, KEINE }, der einem Werkstoff
zugeordnet wird, dessen bemessungsrelevanten Anisotropie-Charakter
in Bezug auf eine ausgezeichnete Faserrichtung klassifiziert und
das Pflichtfeld-Profil der Faserrichtungs-Annotationen am Werkstoff
(Faserrichtung, Plattenlängsrichtung, Lagenstruktur,
Haupttragrichtung) eindeutig festlegt.

## Mathematische Definition

Sei

- 𝓦 die Menge der Werkstoffe (siehe `werkstoff`).

Dann ist der **Faserrichtungs-Modus** der Aufzählungstyp

```
𝓜𝓜 := { HART, STRUKTURIERT, SCHWACH, KEINE }
```

mit der Zuordnungsfunktion

```
faserrichtungs_modus : 𝓦 → 𝓜𝓜,
                     w ↦ faserrichtungs_modus(w),
```

die jedem Werkstoff w ∈ 𝓦 genau einen Modus zuordnet. Die vier
Modi partitionieren 𝓦 in vier disjunkte Anisotropie-Klassen; die
Disjunktheit ist auf der Modus-Ebene definiert.

**Pflichtfeld-Profil je Modus** (Faserrichtungs-Annotationen am
Werkstoff; Plattendicken-Achse und Stahl-spezifische Felder werden
subklassen-spezifisch geführt, siehe Subklassen-Einträge):

| Modus         | Pflicht-Faserrichtungs-Annotation                                      |
|---------------|-------------------------------------------------------------------------|
| HART          | `faserrichtung ∈ S²`                                                    |
| STRUKTURIERT  | `lagenstruktur` mit n ≥ 3, `haupttragrichtung ∈ S²`                     |
| SCHWACH       | `plattenlaengsrichtung ∈ S²`                                            |
| KEINE         | keine (weder Faserrichtung noch Plattenlängsrichtung noch Lagenstruktur) |

**Modus-Subklassen-Zuordnung** (extensional festgelegt durch die
Werkstoff-Hierarchie):

```
faserrichtungs_modus(w) = HART          ⇔  w ∈ 𝓐𝓗  (axiales_holz)
faserrichtungs_modus(w) = STRUKTURIERT  ⇔  w ∈ 𝓜𝓛  (mehrlagenholz)
faserrichtungs_modus(w) = SCHWACH       ⇔  w ∈ 𝓖𝓟  (gerichteter_plattenwerkstoff)
faserrichtungs_modus(w) = KEINE         ⇔  w ∈ 𝓘𝓟 ∪ 𝓦𝓢𝓽  (isotroper_plattenwerkstoff oder werkstoff_stahl)
```

Die Modi HART, STRUKTURIERT, SCHWACH sind injektiv den
entsprechenden Subklassen zugeordnet (`HART ⇔ 𝓐𝓗`,
`STRUKTURIERT ⇔ 𝓜𝓛`, `SCHWACH ⇔ 𝓖𝓟`). Der Modus KEINE wird
gemeinsam von `isotroper_plattenwerkstoff` (Plattenebene-Isotropie)
und `werkstoff_stahl` (3D-Isotropie) getragen; die Disjunktheit
dieser beiden Subklassen wird durch die sealed-Hierarchie auf der
Werkstoff-Ebene getragen, nicht durch den Modus. Der Modus ist
damit eine **partielle Diskriminante** der sealed-Hierarchie:
ausreichend zur Identifikation der drei nicht-isotropen Subklassen,
ungenügend zur Unterscheidung von `isotroper_plattenwerkstoff` und
`werkstoff_stahl`.

## Wohldefiniertheit

- **Existenz**: Für jeden in DIN EN 1995-1-1 / DIN EN 13986
  zugelassenen Holzwerkstoff lässt sich aus der Produktnorm und der
  bemessungsrelevanten Eigenschaft (Faserrichtung vs.
  Lagenstruktur vs. effektive Plattenrichtung vs. Isotropie in
  Plattenebene) genau einer der vier Modi ableiten.
- **Eindeutigkeit**: Die vier Modi sind paarweise disjunkt:
  - HART hat genau eine Faserrichtung; STRUKTURIERT hat
    mindestens drei mit lagenweise wechselnder Orientierung
    (DIN EN 16351 fordert n ≥ 3); SCHWACH hat eine
    Plattenlängsrichtung ohne Lagen-Mechanik; KEINE hat keine
    bemessungsrelevante Faserrichtung (entweder Isotropie in der
    Plattenebene wie bei Spanplatte/MDF/HDF oder 3D-Isotropie wie
    bei Stahl).
  - BSH (zwei oder mehr Lamellen, alle parallel) ist HART, nicht
    STRUKTURIERT, weil das Kriterium „lagenweise wechselnde
    Faserrichtung" nicht erfüllt ist.
  - OSB (Strands schichtweise gekreuzt) ist SCHWACH, nicht
    STRUKTURIERT, weil EC5/EN 12369-1 keine Einzellagen-Mechanik
    verwendet, sondern nur f_m,0 und f_m,90 in der Plattenebene
    führt.
- **Disjunktheit der KEINE-Subklassen**: Die beiden Subklassen, die
  Modus KEINE tragen — `isotroper_plattenwerkstoff` und
  `werkstoff_stahl` — sind nicht durch den Modus, sondern durch
  ihre Pflichtfelder und ihre sealed-Identität disjunkt:
  `isotroper_plattenwerkstoff` führt `plattendicken_achse ∈ S²` als
  Pflicht (siehe `hg_isotroper_plattenwerkstoff.md`), während
  `werkstoff_stahl` weder Plattendicken-Achse noch eine andere
  Werkstoff-Anisotropie-Achse führt (siehe `hg_werkstoff_stahl.md`).
- **Vollständigkeit**: Die vier Modi decken alle in den
  Produktnormen EN 14080, EN 14081, EN 14374, EN 16351, EN 636,
  EN 300, EN 312, EN 622 zugelassenen Holzwerkstoffe ab. Für Stahl
  (EN 1993, EN ISO 898-1, EN ISO 3506-1) ist Modus KEINE formal
  zutreffend: Stahl hat keine bemessungsrelevante Faserrichtung im
  Sinne der Holzbau-Anisotropie.
- **Konsistenz Modus ↔ Pflichtfelder**: Das Pflichtfeld-Profil je
  Modus ist eine **harte Invariante** der jeweiligen Werkstoff-
  Subklasse, nicht eine Empfehlung. Eine Modus-Pflichtfeld-Verletzung
  ist Validierungsfehler, kein Warning (Memory
  `project_faserrichtung_modi`).
- **Nicht-Zirkularität**: Die Definition verwendet ausschließlich den
  Begriff `werkstoff` als Träger der Modus-Zuordnung sowie
  `toleranzen`. Sie kommt nicht in ihrer eigenen Definition vor.

## Erläuterung (nicht normativ)

### Warum Aufzählungstyp und nicht kontinuierliche Größe

Das anisotrope Verhalten von Holz ist physikalisch ein Spektrum
(orthotrop mit 9 elastischen Konstanten, transversal-isotrop mit 5
Konstanten, quasi-isotrop in der Plattenebene mit effektivem
Mittelwert). Die App führt jedoch keine vollständige Tensor-
Beschreibung; sie führt nur die für EC5-Bemessung notwendigen
**Pflichtfelder**. Der Faserrichtungs-Modus diskretisiert das
physikalische Spektrum auf die vier Klassen, in denen sich die
Pflichtfelder unterscheiden.

### Konsequenzen für die Hankinson-Formel

Die Hankinson-Formel f_α = (f_0 · f_90) / (f_0 · sin²α + f_90 · cos²α)
ist je Modus unterschiedlich anwendbar:

| Modus          | Hankinson-Anwendung                                                  |
|----------------|----------------------------------------------------------------------|
| HART           | direkt anwendbar mit α = ∠(Kraft, faserrichtung).                    |
| STRUKTURIERT   | je Lage ℓᵢ separat anwendbar mit α_i = ∠(Kraft, ℓᵢ.faserrichtung).  |
| SCHWACH        | abgeschwächt anwendbar mit α = ∠(Kraft, plattenlaengsrichtung); EC5 / EN 12369-1 spezifizieren f_m,0 und f_m,90 als diskrete Werte. |
| KEINE          | nicht anwendbar. Bei `isotroper_plattenwerkstoff` gilt in der Plattenebene eine einzige Festigkeit pro Beanspruchungsart (EC5 / EN 12369-1); bei `werkstoff_stahl` ist die Hankinson-Formel begrifflich nicht zutreffend (3D-Isotropie, Bemessung nach EC3 / Johansen-Theorie). |

Die Schnittwinkel-Visualisierung dieser App (Kernfunktion) muss den
Modus berücksichtigen: bei STRUKTURIERT ist α nicht skalar, sondern
ein Vektor von Winkeln je Lage (siehe `hankinson_winkel`,
`mehrlagenholz`).

### Modus vs. Werkstoff-Subklasse

Der Faserrichtungs-Modus und die Werkstoff-Subklasse stehen in
einer **partiellen Bijektion**: HART, STRUKTURIERT und SCHWACH sind
injektiv den drei Holzwerkstoff-Subklassen `axiales_holz`,
`mehrlagenholz` und `gerichteter_plattenwerkstoff` zugeordnet; der
Modus KEINE wird dagegen von zwei Subklassen geteilt
(`isotroper_plattenwerkstoff` und `werkstoff_stahl`). Der Modus
ist damit eine **partielle Diskriminante** des sealed-Werkstoff-
Typs: er liefert die Anisotropie-Klasse für die Bemessung, aber
für die vollständige Diskriminanz innerhalb des Modus KEINE wird
die sealed-Subklasse herangezogen.

Die App führt den Modus dennoch als eigenes Feld am abstrakten
Werkstoff, weil:

1. EC5- und SIA-Bemessungslogik referenziert die Modus-Eigenschaften
   (parallel/rechtwinklig zur Faser, Hankinson) ohne explizit die
   Werkstoff-Subklasse zu nennen.
2. IFC `Pset_MaterialWoodBasedBeam` / `Pset_MaterialWoodBasedPanel`
   trennt Beam-Werkstoffe (typisch HART) und Panel-Werkstoffe
   (typisch STRUKTURIERT/SCHWACH/KEINE) am Property-Set, nicht an
   der Werkstoff-Klasse.
3. Die UI-Präsentation (Schnittwinkel-Tooltips, Bemessungs-Hinweise)
   greift direkt auf den Modus, nicht auf die Subklasse.

## Beziehungen

- **Oberbegriff**: keiner. Der Faserrichtungs-Modus ist ein
  Aufzählungstyp ohne Hierarchie.
- **Partielle Diskriminanten-Funktion** für die Werkstoff-Hierarchie:
  - `axiales_holz` (Modus HART, injektiv)
  - `mehrlagenholz` (Modus STRUKTURIERT, injektiv)
  - `gerichteter_plattenwerkstoff` (Modus SCHWACH, injektiv)
  - `isotroper_plattenwerkstoff` (Modus KEINE, gemeinsam mit
    `werkstoff_stahl`)
  - `werkstoff_stahl` (Modus KEINE, gemeinsam mit
    `isotroper_plattenwerkstoff`)
- **Verwendung**:
  - **Werkstoff** (`werkstoff`): trägt den Faserrichtungs-Modus als
    Pflichtfeld der abstrakten Klasse.
  - **Werkstoff Stahl** (`werkstoff_stahl`): trägt Modus KEINE im
    Sinne von 3D-Isotropie — semantisch eine Erweiterung der bei
    `isotroper_plattenwerkstoff` vorliegenden in-Plattenebene-
    Isotropie. Die beiden Subklassen werden durch ihre
    sealed-Identität und ihr Pflichtfeld-Profil (mit/ohne
    `plattendicken_achse`) unterschieden.
  - **Hankinson-Winkel** (`hankinson_winkel`): die Anwendbarkeit
    der Hankinson-Formel hängt vom Modus ab (siehe Tabelle in der
    Erläuterung).
- **Abgrenzung**:
  - **`faserrichtung`**: ein Einheitsvektor in der Rolle „Material-
    hauptachse parallel zum Faserverlauf"; nur bei Modus HART als
    skalares Pflichtfeld am Werkstoff. Der Modus ist eine
    Klassifikation, die Faserrichtung ein konkreter geometrischer
    Vektor.
  - **`festigkeitsklasse`**: bemessungsrelevante Werte (E-Modul,
    Festigkeiten) werkstoffspezifisch; orthogonal zum Modus (z. B.
    haben sowohl C24-Vollholz als auch GL24h-BSH den Modus HART, aber
    unterschiedliche Festigkeitsklassen).
  - **„Anisotropie"** (umgangssprachlich): physikalischer Oberbegriff;
    der Faserrichtungs-Modus ist eine konkrete, vierwertige
    Diskretisierung der Anisotropie-Klasse, kein Kontinuum.

## Implementierungshinweis

Datentyp (Domänen-Schicht, Kotlin, Schicht
`domain.holzbau.werkstoff`):

```kotlin
package domain.holzbau.werkstoff

/**
 * Faserrichtungs-Modus eines Werkstoffs.
 * Glossar: hg_faserrichtungs_modus.md — Memory project_faserrichtung_modi.
 *
 * Bestimmt das Pflichtfeld-Profil der Faserrichtungs-Annotationen
 * der Werkstoff-Subklasse:
 *   HART          -> 1 Vektor faserrichtung
 *   STRUKTURIERT  -> Lagenstruktur >= 3 + Haupttragrichtung
 *   SCHWACH       -> 1 Vektor plattenlaengsrichtung
 *   KEINE         -> keine Faserrichtungs-Annotation; getragen sowohl
 *                    von IsotroperPlattenwerkstoff (in Plattenebene
 *                    quasi-isotrop, mit plattendickenAchse) als auch
 *                    von WerkstoffStahl (3D-isotrop, ohne
 *                    plattendickenAchse).
 *
 * Partielle Diskriminante des sealed-Werkstoff-Typs: HART, STRUKTURIERT
 * und SCHWACH identifizieren ihre Subklasse eindeutig; KEINE wird von
 * zwei Subklassen geteilt, deren Disjunktheit über die sealed-Identität
 * getragen wird.
 */
enum class FaserrichtungsModus { HART, STRUKTURIERT, SCHWACH, KEINE }
```

- **Einheit**: dimensionslos (Aufzählung).
- **Identität**: keine. Aufzählungstyp ohne Felder.
- **Invarianten**: keine über die Aufzählung selbst hinaus; die
  Modus-Pflichtfeld-Konsistenz wird in der jeweiligen Werkstoff-
  Subklasse erzwungen (siehe `axiales_holz`, `mehrlagenholz`,
  `gerichteter_plattenwerkstoff`, `isotroper_plattenwerkstoff`,
  `werkstoff_stahl`).
- **IFC-Mapping** (Persistenzschicht): nicht direkt abgebildet; der
  Modus ergibt sich implizit aus der `IfcMaterial.Category` bzw. der
  Wahl von `Pset_MaterialWoodBasedBeam` vs.
  `Pset_MaterialWoodBasedPanel`.
- **Validierungsregel** (zur Konstruktionszeit der Werkstoff-
  Subklasse): Die Konsistenz Modus ↔ Subklasse ist Klassen-
  Invariante. Bei Verletzung `Resultat.Fehler` bzw.
  `Entartet.ModusSubklassenInkonsistenz`; niemals Exception.
- **Edge Cases**:
  - **Unbekannter Werkstoff** (Hybrid-Werkstoffe, neuartige Komposite):
    aktuell nicht abgedeckt. Folgearbeit `werkstoff_hybrid` mit
    eigenem Modus oder Modus-Erweiterung.
  - **Stahl als Werkstoff** (`werkstoff_stahl`): Modus KEINE im Sinne
    von 3D-Isotropie. Die Stahl-Klasse trägt keinerlei Faserrichtungs-,
    Lagen- oder Plattenrichtungs-Felder und keine Plattendicken-Achse
    (siehe `werkstoff_stahl`).

## Quellen

**Primär (normativ):**

- DIN EN 1995-1-1:2010-12, „Eurocode 5: Bemessung und Konstruktion
  von Holzbauten – Teil 1-1".
- DIN EN 13986:2015-06, „Holzwerkstoffe zur Verwendung im Bauwesen".
- DIN EN 16351:2021-08 (Brettsperrholz), DIN EN 14080:2013-09 (BSH),
  DIN EN 14081-1:2019-10 (Vollholz), DIN EN 14374:2005-02 (LVL),
  DIN EN 636:2015-06 (Sperrholz), DIN EN 300:2006-09 (OSB),
  DIN EN 312:2010-12 (Spanplatten), DIN EN 622-2/3/5 (Faserplatten).
- DIN EN 12369-1:2001-04, „Charakteristische Werte für die
  Berechnung und Bemessung von Holzbauwerken – Teil 1: OSB,
  Spanplatten und Faserplatten".

**Sekundär:**

- Niemz, P.; Sonderegger, W.: *Physik des Holzes und der
  Holzwerkstoffe.* Hanser, München 2017.
- Blass, H. J.; Sandhaas, C.: *Ingenieurholzbau – Grundlagen der
  Bemessung.* KIT Scientific Publishing, Karlsruhe 2016.
- ProHolz Austria: *Brettsperrholz Bemessung Band I.* Wien 2014.
- Schickhofer, G. et al. (Hrsg.): *BSPhandbuch.* TU Graz 2010.

**Korpus (nicht autoritativ):**

- Memory `project_faserrichtung_modi` (interner Projektkontext,
  Memory-System, abgerufen 2026-05-08).
- Wikipedia, Lemmata „Anisotropie", „Holzwerkstoff" (abgerufen
  2026-05-08).
