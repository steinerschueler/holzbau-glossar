---
id: dachseite
benennung: Dachseite
synonyme: ["Seite des Daches", "geneigte Außenseite eines Daches"]
abgelehnte_benennungen: [Dachfläche, Dachschräge, Dachhälfte, "roof side"]
oberbegriff: dachflaeche
begriffstyp: merkmal
voraussetzungen: [dachflaeche, vektor, einheitsvektor, toleranzen]
abgrenzung_zu: [dachflaeche, dachschraege, dachneigung, traufseite, giebelseite]
status: entwurf
theorie_pflichtig: required
quellen_primär:
  - "SIA 232/1:2020 'Geneigte Dächer', Schweizerischer Ingenieur- und Architektenverein, Abschnitt 1 (Begriffe): die Begriffe Wetterseite, Sonnenseite, Wind- und Sonnenexposition werden als Dachseiten-Eigenschaften eingeführt."
  - "DIN EN 1991-1-4:2010-12 'Eurocode 1 – Windlasten', Abschnitt 7.2 (Dächer): die windangeströmte Dachseite (luvseitig) und die abgewandte (leeseitig) treten als bemessungsrelevante Unterscheidung auf."
  - "DIN 1356-1:1995-02 'Bauzeichnungen – Teil 1: Arten, Inhalte und Grundregeln der Darstellung', Abschnitt 5: Bezeichnung der Dachseiten in Aufrissen."
quellen_sekundär:
  - "Lignum (Hrsg.): Lignatec 'Geneigte Dächer in Holzbauweise', Lignum, Zürich, aktuelle Auflage."
  - "Mönck, W.; Rug, W.: Holzbau – Bemessung und Konstruktion. 16. Aufl., Beuth Verlag 2015, Kap. 'Dachformen'."
  - "Gerner, M.: Fachwerk – Instandsetzung, Sanierung, Neubau. DVA, 7. Aufl. 2007, Glossar 'Dachseite'."
quellenkonflikt: |
  Im Glossareintrag `dachflaeche` ist „Dachseite" derzeit als
  Synonym ausgewiesen. Diese Festlegung ist in der allgemeinen
  Bauliteratur tatsächlich verbreitet, jedoch unscharf: „Dachseite"
  trägt im praktischen Sprachgebrauch (Wetterseite, Sonnenseite,
  Wind- und Sonnenexposition) eine **Orientierungs-Annotation**, die
  „Dachfläche" als rein geometrischer Begriff nicht hat.

  Eigene Festlegung dieses Glossars: „Dachseite" ist ein
  Merkmal-Begriff über `dachflaeche` und führt eine zusätzliche
  Orientierungsangabe (Himmelsrichtung, Wind-/Sonnenexposition).
  Strukturell ist eine Dachseite eine Dachfläche; semantisch ist
  sie eine Dachfläche „in der Rolle einer Außenseite des Gebäudes
  unter Orientierungsannotation".

  Diese Festlegung löst den Konflikt im Eintrag `hg_dachflaeche.md`
  auf: dort sollte „Dachseite" künftig als **`verwandter_begriff`**
  geführt werden, nicht als Synonym im engen Sinn. Der Eintrag
  `hg_dachflaeche.md` wird im Rahmen einer separaten Konsistenz-
  Überarbeitung entsprechend angepasst (TODO).
---

## Prosa-Definition

Eine **Dachseite** ist eine Dachfläche unter zusätzlicher
Orientierungs-Annotation, die ihre Lage zur Hauptachse des Gebäudes
oder zu einer Himmelsrichtung benennt und damit eine fachpraktische
Identifikation als Wetterseite, Sonnenseite, Trauf- oder Giebelseite
ermöglicht.

## Mathematische Definition

Sei

- D = (E, P, n_a) eine Dachfläche im Sinne von `dachflaeche` mit
  nach außen gerichteter Einheits-Normale n_a ∈ S²,
- e_N = (0, 1, 0)ᵀ die Nordrichtung des Welt-Koordinatensystems
  (Konvention der App: x = Ost, y = Nord, z = oben),
- n_hat_h ∈ S² ∩ {z = 0} die horizontale Projektion der äußeren
  Normalen,
  ```
  n_hat_h := normiere(n_a − ⟨n_a, e_z⟩ · e_z)
  ```
  (definiert nur, falls ‖n_a − ⟨n_a, e_z⟩ · e_z‖ > Toleranzen.NORM_EPS,
  also α(D) > 0 und n_a nicht vertikal).

Dann ist die **Orientierung** der Dachseite zu D der Winkel
ψ(D) ∈ [0, 2π) zwischen n_hat_h und e_N, gemessen im Uhrzeigersinn um
e_z (geographische Konvention: 0° = Norden, 90° = Osten,
180° = Süden, 270° = Westen):

```
ψ(D) := atan2( ⟨n_hat_h, e_E⟩ , ⟨n_hat_h, e_N⟩ )  mod 2π,
```

mit e_E = (1, 0, 0)ᵀ.

Eine **Dachseite** ist das Tupel

```
DS(D) := (D, ψ(D))
```

aus der zugrundeliegenden Dachfläche D und ihrer Orientierung ψ(D).
Aus ψ ergeben sich abgeleitete Annotationen über
Toleranz-Intervalle:

- **Südseite (Sonnenseite, Nordhalbkugel)**:
  ψ ∈ [π · 3/4, π · 5/4] (135° – 225°),
- **Nordseite**:
  ψ ∈ [0, π/4] ∪ [π · 7/4, 2π) (315° – 45°),
- **Ostseite** und **Westseite** analog.

Die in der Schweiz vorherrschende **Wetterseite** entspricht im
Mittel der Westseite (atlantische Hauptwetterrichtung West-Südwest);
die exakte Zuordnung erfolgt standortabhängig über meteorologische
Daten und ist hier nicht festgelegt.

## Wohldefiniertheit

- **Existenz von n_hat_h**: Für jede geneigte Dachfläche
  (α(D) ∈ (0, π/2)) ist ‖n_a − ⟨n_a, e_z⟩ · e_z‖ > 0; n_hat_h ist also
  wohldefiniert.
- **Sonderfall α(D) = 0** (Flachdach): n_a = e_z, n_hat_h ist nicht
  definiert; eine Flachdachfläche besitzt keine Orientierung im
  Sinne dieser Definition. In diesem Fall ist DS(D) entartet
  (siehe `Entartet.Horizontal`).
- **Eindeutigkeit von ψ**: atan2 liefert auf [−π, π); die
  Reduktion mod 2π ergibt einen eindeutigen Wert in [0, 2π).
- **Konsistenz mit Dachfläche**: DS(D) erbt sämtliche Invarianten
  von D; ψ ist eine zusätzliche skalare Annotation, kein neues
  geometrisches Objekt.
- **Unabhängigkeit von der Polygon-Parametrisierung**: ψ hängt nur
  von n_a ab, nicht von P; insbesondere nicht von der Reihenfolge
  der Polygonpunkte oder ihrer Translation.
- **Konvention der Nordrichtung**: e_N = (0, 1, 0)ᵀ ist eine
  Modellierungskonvention der App; bei abweichenden CAD-
  Importkonventionen (etwa e_N = (1, 0, 0)) muss die Eingabe vor
  Anwendung dieser Definition rotiert werden.
- **Nicht-Zirkularität**: Die Definition stützt sich nur auf
  `dachflaeche`, `vektor`, `einheitsvektor` und `toleranzen`. Sie
  kommt nicht in ihrer eigenen Definition vor.

## Erläuterung (nicht normativ)

Im Sprachgebrauch des Holzbaus ist „Dachseite" ein
**handlungsrelevanter** Begriff: der Zimmermann unterscheidet
„Wetterseite" und „Sonnenseite", weil sich daraus konkrete
Entscheidungen ableiten:

- **Wetterseite**: vorzugsweise dichtere Eindeckung, sorgfältigere
  Anschlüsse, robustere Dachhaut-Detailierung; oft die West-
  oder Südwestseite.
- **Sonnenseite**: bevorzugte Lage für Solarthermie- und
  Photovoltaikanlagen, Dachflächenfenster für Wohnräume, höhere
  thermische Belastung der Eindeckung.
- **Traufseite vs. Giebelseite** des Gebäudes (nicht der
  Dachfläche, sondern der zugehörigen Wand): die Traufseite ist
  die Wand parallel zur Trauflinie, die Giebelseite die Wand
  parallel zum Ortgang. Diese Begriffe sind Eigenschaften der
  **Wand**, nicht der Dachfläche selbst.

Strukturell ist eine Dachseite **dieselbe Geometrie** wie eine
Dachfläche; der Begriff fügt lediglich eine
Orientierungs-Annotation hinzu. Das rechtfertigt einen
**Merkmal-Begriff** statt eines neuen geometrischen Typs.

In Glossaren und Lehrwerken wird „Dachseite" oft synonym zu
„Dachfläche" verwendet (z. B. Gerner, einige regionale
Fachglossare). Dieser Sprachgebrauch ist nicht falsch, sondern
unspezifischer; im vorliegenden Glossar wird er durch trennscharfe
Definition ersetzt: Dachfläche ist Geometrie, Dachseite ist
Geometrie + Orientierungsmerkmal.

## Beziehungen

- **Oberbegriff**: `dachflaeche`. Eine Dachseite ist eine
  Dachfläche mit zusätzlicher Orientierungs-Annotation.
- **Verwandte Begriffe**:
  - **Wetterseite**, **Sonnenseite**, **Nord-/Süd-/Ost-/Westseite**:
    spezifische Werte der Orientierungs-Annotation. Sie werden
    nicht als eigenständige Glossareinträge geführt, sondern als
    abgeleitete Klassifikationen über ψ.
  - **Traufseite**, **Giebelseite**: Eigenschaften der **Wand**,
    nicht der Dachfläche. Sie betreffen die Lage der
    Anschlusswand zur Trauflinie bzw. zum Ortgang. Eigene
    Glossareinträge in Folgearbeit.
- **Abgrenzung**:
  - **Dachfläche** (`dachflaeche`): rein geometrischer Begriff
    ohne Orientierungs-Annotation. Eine Dachseite ist genau eine
    Dachfläche, aber zusätzlich orientierungs-annotiert.
  - **Dachschräge** (`dachschraege`): innenseitige, raumseitige
    Bezugsfläche; Dachseite ist außenseitig.
  - **Dachneigung** (`dachneigung`): Winkelmerkmal; Dachseite ist
    Lagemerkmal. Beide sind Merkmale derselben Dachfläche, aber
    verschiedene.
  - **Dachhälfte**: nicht synonym; bei einem Satteldach gibt es
    zwei Dachseiten und gleichzeitig zwei Dachhälften, bei einem
    Walmdach gibt es jedoch vier Dachseiten und nur zwei
    geometrische „Hälften". „Dachhälfte" ist hier abgelehnt.

## Implementierungshinweis

Datentyp (Domänen-Schicht, Kotlin, Schicht `domain.bauteil`):

```
package domain.bauteil

import domain.Toleranzen
import kotlin.math.atan2
import kotlin.math.PI
import kotlin.math.sqrt

/**
 * Dachseite: Dachfläche mit Orientierungs-Annotation.
 * Glossar: hg_dachseite.md
 *
 * Strukturell ein Wrapper um Dachflaeche; trägt die Orientierung ψ
 * als abgeleitete skalare Eigenschaft.
 */
data class Dachseite(
    val dachflaeche: Dachflaeche
) {
    /**
     * Orientierung ψ ∈ [0, 2π) als Kompasswinkel der äußeren
     * Normalen-Horizontalprojektion (0 = Nord, 90° = Ost,
     * 180° = Süd, 270° = West). Liefert null bei Flachdach
     * (α = 0), wenn keine eindeutige horizontale Orientierung
     * existiert. Glossar: dachseite#orientierung.
     */
    fun orientierung(): Double? {
        val n = dachflaeche.aeussereNormale
        val hx = n.x          // Ost
        val hy = n.y          // Nord
        val laenge = sqrt(hx * hx + hy * hy)
        if (laenge <= Toleranzen.NORM_EPS) return null   // Flachdach
        val psi = atan2(hx / laenge, hy / laenge)         // 0 = Nord
        return (psi + 2.0 * PI) % (2.0 * PI)
    }

    fun ausrichtung(): Ausrichtung? {
        val psi = orientierung() ?: return null
        val grad = psi * 180.0 / PI
        return when {
            grad < 22.5 || grad >= 337.5 -> Ausrichtung.NORD
            grad < 67.5                   -> Ausrichtung.NORDOST
            grad < 112.5                  -> Ausrichtung.OST
            grad < 157.5                  -> Ausrichtung.SUEDOST
            grad < 202.5                  -> Ausrichtung.SUED
            grad < 247.5                  -> Ausrichtung.SUEDWEST
            grad < 292.5                  -> Ausrichtung.WEST
            else                          -> Ausrichtung.NORDWEST
        }
    }

    enum class Ausrichtung {
        NORD, NORDOST, OST, SUEDOST, SUED, SUEDWEST, WEST, NORDWEST
    }

    sealed class Entartet {
        object Horizontal : Entartet()    // α(D) = 0, keine Orientierung
    }
}
```

- **Einheit**: ψ intern in **Radiant** (Double); Anzeige in Grad
  (Kompasskonvention) am API-Rand.
- **Konvention**: Welt-Koordinatensystem mit x = Ost, y = Nord,
  z = oben. Bei abweichender CAD-Konvention ist eine
  Vorab-Rotation erforderlich.
- **Invarianten**: alle Invarianten von `Dachflaeche`. Die
  Orientierung ist eine **abgeleitete** Eigenschaft, kein
  zusätzliches Feld mit eigener Invariante.
- **Edge Cases**:
  - **Flachdach (α = 0)**: `orientierung()` liefert `null`. Eine
    Flachdachseite hat keine Himmelsrichtung. Die Domänen-Klasse
    liefert `Entartet.Horizontal`, falls eine
    Orientierungs-Annotation zwingend erforderlich ist.
  - **Numerisch fast horizontale Dächer** (α ≪ ε_W): die
    Orientierung wird numerisch instabil; die Schwelle
    `laenge ≤ Toleranzen.NORM_EPS` liefert in diesem Fall `null`.
  - **Mehrere Dachseiten gleicher Orientierung** (z. B.
    Krüppelwalm mit zwei südorientierten Teilflächen): jede
    Dachfläche wird unabhängig orientiert; die Klassifikation in
    Sektoren liefert dann zwei Dachseiten gleicher Ausrichtung.
- **Verwendungsregel**: Funktionen, die orientierungsabhängige
  Größen berechnen (Solarstrahlungsertrag, Schlagregenexposition,
  Windlast-Hauptangriffsrichtung), nehmen `Dachseite` als
  Parametertyp und nicht den nackten `Dachflaeche`. Damit ist die
  Notwendigkeit einer Orientierungs-Annotation am API-Rand
  erkennbar.

## Quellen

**Primär (normativ):**

- SIA 232/1:2020, „Geneigte Dächer", Schweizerischer Ingenieur- und
  Architektenverein, Zürich.
- DIN EN 1991-1-4:2010-12, „Eurocode 1: Einwirkungen auf Tragwerke –
  Teil 1-4: Windlasten".
- DIN 1356-1:1995-02, „Bauzeichnungen – Teil 1: Arten, Inhalte und
  Grundregeln der Darstellung".

**Sekundär:**

- Lignum (Hrsg.): *Lignatec — Geneigte Dächer in Holzbauweise.*
  Lignum, Zürich, aktuelle Auflage.
- Mönck, W.; Rug, W.: *Holzbau – Bemessung und Konstruktion.*
  16. Auflage, Beuth Verlag 2015.
- Gerner, M.: *Fachwerk – Instandsetzung, Sanierung, Neubau.*
  DVA, 7. Auflage 2007.

**Korpus (nicht autoritativ):**

- Wikipedia, Lemmata „Wetterseite", „Sonnenseite", „Dach"
  (abgerufen 2026-05-08).
