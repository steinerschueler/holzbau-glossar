---
id: pfette
benennung: Pfette
synonyme: []
abgelehnte_benennungen: [Längsbalken, Pfettenbalken, Pfettenträger, "purlin", Mauerlatte, Schwellpfette, Latte, Riegel]
oberbegriff: bauteil
begriffstyp: bauteilrolle
voraussetzungen: [bauteil, bauteilachse, strecke, einheitsvektor, dachflaeche, dachkante, weltkoordinatensystem, toleranzen]
abgrenzung_zu: [sparren, kehlbalken, riegel, latte, konterlatte, binder, dachflaeche, schwelle, raehm, knagge]
status: entwurf
theorie_pflichtig: required
quellen_primär:
  - "SIA 265:2021 'Holzbau', Schweizerischer Ingenieur- und Architektenverein, Abschnitt 4 (Bemessung) und Abschnitt 5 (Konstruktive Durchbildung), Pfette als horizontaler Längsträger des Dachtragwerks."
  - "SIA 232/1:2020 'Geneigte Dächer', Abschnitt 1 (Begriffe und geometrische Grundlagen)."
  - "DIN EN 1995-1-1:2010-12 (Eurocode 5), Abschnitt 5 (Tragwerksberechnung), Pfetten als biegebeanspruchte Stab-Bauteile in horizontaler Lage."
  - "DIN 1052:2008-12, Abschnitt 8 und Abschnitt 12 (Konstruktive Anforderungen), Pfetten als Längsträger des Dachtragwerks."
quellen_sekundär:
  - "Lignum (Hrsg.): Holzbautabellen HBT, Lignum, Zürich, aktuelle Auflage, Kap. 'Pfettendach' und 'Dachtragwerke'."
  - "Lignum (Hrsg.): Lignatec 'Geneigte Dächer in Holzbauweise', Abschnitt 'Pfetten und Pfettenanschlüsse'."
  - "Mönck, W.; Rug, W.: Holzbau – Bemessung und Konstruktion. 16. Aufl., Beuth, Berlin 2015, Kap. 11 'Dachtragwerke', § Pfetten."
  - "Blass, H. J.; Sandhaas, C.: Ingenieurholzbau – Grundlagen der Bemessung. KIT Scientific Publishing, Karlsruhe 2016, Kap. 5."
  - "Natterer, J.; Herzog, T.; Volz, M.: Holzbau-Atlas. 4. Aufl., Birkhäuser, Basel 2003, Kap. 'Dachtragwerke / Pfettendach'."
  - "Gerner, M.: Fachwerk – Instandsetzung, Sanierung, Neubau. DVA, 7. Aufl. 2007, Glossar 'Pfette'."
quellenkonflikt: |
  Weder SIA 265, SIA 232/1, EN 1995-1-1 noch DIN 1052 enthalten eine
  geschlossene Begriffsdefinition für „Pfette"; der Begriff wird in
  allen konsultierten Normen vorausgesetzt und über seine konstruktive
  Rolle (horizontaler Längsträger des Dachtragwerks) charakterisiert.

  In der Sekundärliteratur (Mönck/Rug, Blass/Sandhaas, Natterer/Herzog,
  Gerner, Lignum) wird die Pfette durchgängig als „horizontaler
  Längsträger eines Dachtragwerks, der die Sparrenlasten quer zur
  Sparrenrichtung sammelt und in Wände, Stützen oder Stuhlsäulen
  abträgt" beschrieben.

  Eigene Festlegung in diesem Glossar:

  - Eine Pfette ist ein **Bauteil mit Bauteilrolle „Pfette"**, dessen
    Bauteilachse näherungsweise horizontal verläuft und parallel zu
    einer Dachkante (Traufe, First oder einer dazu parallelen
    Höhenlinie der Dachfläche) liegt.
  - Pfette ist der **Oberbegriff** für die drei Spezialisierungen
    `firstpfette`, `mittelpfette` und `fusspfette`, die durch ihre
    Lage am Dach unterschieden werden.
  - „Mauerlatte" und „Schwellpfette" sind **nicht** Synonyme von
    „Pfette" als Oberbegriff, sondern eingeschränkte Benennungen für
    Spezialfälle der Fußpfette und werden in `hg_fusspfette.md`
    behandelt. Sie sind hier in `abgelehnte_benennungen` aufgeführt,
    weil sie als Synonym für die generische Pfette unzulässig wären.

  Diese Festlegung ist konsistent mit allen konsultierten Quellen.
---

## Prosa-Definition

Eine **Pfette** ist ein Stab-Bauteil eines Dachtragwerks, dessen
Bauteilachse näherungsweise horizontal verläuft und parallel zu einer
Dachkante (Traufe, First oder einer dazu parallelen Höhenlinie der
Dachfläche) liegt, das die Lasten der quer zu ihrer Bauteilachse
verlaufenden Sparren oder Binder aufnimmt und entlang seiner
Längsachse über seine Auflager (Wände, Stützen, Stuhlsäulen oder
Binder) abträgt.

## Mathematische Definition

Sei

- B ein Bauteil im Sinne von `bauteil` mit Stabgeometrie
  (`geometrie ∈ 𝒢_stab`),
- a(B) = Bauteilachse.Gerade(p_a, p_e) die Bauteilachse von B im
  geraden Fall (siehe `bauteilachse`), mit
  d̂ := (p_e − p_a) / ‖p_e − p_a‖ ∈ S² ⊂ ℝ³,
- e_z := (0, 0, 1)ᵀ die vertikale Achse,
- ε_K := Toleranzen.KOLLINEAR_EPS,
  ε_W := Toleranzen.WINKEL_EPS,
  ε_L := Toleranzen.LAENGE_EPS.

Dann heißt B eine **Pfette** genau dann, wenn die folgenden
Bedingungen erfüllt sind:

1. **Stabgeometrie**: B besitzt eine gerade Bauteilachse mit
   ‖p_e − p_a‖ > ε_L.

2. **Horizontalitätsbedingung**: Die Bauteilachsenrichtung ist
   horizontal,
   ```
   |⟨d̂, e_z⟩| ≤ ε_K,
   ```
   d. h. die Bauteilachse steht rechtwinklig zur Welt-Lotachse.
   Die Form des Tests ist ein **Sinus-Test gegen `e_z`-
   Parallelität** und damit ein Lot-Prädikat; nach
   `_KONVENTIONEN.md` Sektion 4 ist `KOLLINEAR_EPS` die
   einschlägige Toleranzkonstante (bevorzugt für Lot- und
   Parallelitäts-Prädikate, weil der Sinus in der Nähe von 0
   gut konditioniert ist).

3. **Parallelitätsbedingung zu einer Dachkante**: Es existiert
   mindestens eine Dachkante k (im Sinne von `dachkante`) der
   zugeordneten Dachfläche bzw. des Dachtragwerks, deren
   Richtungs-Einheitsvektor d̂_k mit d̂ kollinear ist:
   ```
   |⟨d̂, d̂_k⟩| ≥ 1 − ε_W.
   ```
   In der Regel ist k eine Traufe, ein First oder eine
   Höhenlinie der zugeordneten Dachfläche.

Wesentliche abgeleitete Größen:

- **Pfettenlänge**: L_P := ‖p_e − p_a‖ (in mm), entlang der
  Bauteilachse zwischen den Pfettenenden.
- **Pfettenrichtung**: d̂ ∈ S² mit |⟨d̂, e_z⟩| ≤ ε_K.
- **Pfetten-Höhenlage**: z_P := (p_a.z + p_e.z) / 2; bei einer
  exakt horizontalen Pfette gilt p_a.z = p_e.z = z_P.
- **Pfettenanfang** und **Pfettenende** als Punkte: p_a, p_e (die
  Vorzeichenkonvention wird durch die Bauteilrolle bzw. lokale
  Bezeichnungskonvention der Achse festgelegt; siehe
  `bauteilachse`).

## Wohldefiniertheit

- **Existenz**: Für jedes Stabbauteil mit positiver Achsenlänge,
  horizontaler Achse und Achsenrichtung kollinear zu einer
  Dachkante sind alle Bedingungen konstruktiv erfüllbar; jede
  Standardpfette eines Pfettendachs ist das Standardbeispiel.
- **Eindeutigkeit der Pfettenrolle**: Die Pfettenrolle eines
  Bauteils ist durch Bedingungen 1–3 vollständig festgelegt; die
  Spezialisierung in Fuß-, Mittel- oder Firstpfette erfolgt durch
  zusätzliche Lage-Bedingungen (Höhenlage, Anschluss an Traufe
  bzw. First; siehe `fusspfette`, `mittelpfette`, `firstpfette`).
- **Vorzeichenkonvention**: Die Bauteilachse einer Pfette ist
  gerichtet (`Bauteilachse.Gerade`), aber welcher Endpunkt p_a
  bzw. p_e ist, ist auf der Ebene des generischen Begriffs
  „Pfette" **nicht** durch eine Lagebedingung festgelegt
  (anders als beim Sparren, wo die vertikale Lage Traufe/First
  eindeutig orientiert). Empfehlung gemäß `hg_bauteilachse.md`:
  p_a am Bauteilanfang nach lokaler Bezeichnungskonvention
  (z. B. niedrigeres x in Welt-Koordinaten oder gemäß
  Achsplan A → B → …), p_e am Bauteilende. Konsumenten dürfen
  sich nicht auf eine geometrisch zwingende Orientierung
  verlassen.
- **Mehrfachzuordnung der Dachkante**: Bedingung 3 erfordert
  mindestens eine parallele Dachkante; mehrere parallele
  Dachkanten (z. B. Traufe und First desselben Satteldachs sind
  bei symmetrischer Geometrie parallel) sind zulässig. Die
  konkrete Zuordnung Pfette ↔ Dachkante erfolgt über die
  Spezialisierungen.
- **Konsistenz mit `hg_bauteilachse.md`**: Die in `hg_bauteilachse.md`
  empfohlene Vorzeichenkonvention für Pfetten („p_a am
  Bauteilanfang gemäß lokaler Bezeichnungskonvention") wird hier
  übernommen.
- **Nicht-Zirkularität**: Die Definition stützt sich nur auf
  bereits definierte Begriffe (`bauteil`, `bauteilachse`,
  `strecke`, `einheitsvektor`, `dachflaeche`, `dachkante`,
  `weltkoordinatensystem`, `toleranzen`). Sie kommt nicht in
  ihrer eigenen Definition vor und verweist nicht auf
  Pfetten-Spezialisierungen.
- **Auflagerung (qualitativ, nicht Bestandteil der Definition)**:
  Eine Pfette wird im Tragwerk durch zwei oder mehr Auflager
  gestützt (Stuhlsäulen, Wände, Binder); die Auflagerung ist
  Eigenschaft des Tragwerks (`tragwerk`), nicht der Pfette.

## Erläuterung (nicht normativ)

Die Pfette ist das **horizontale Gegenstück zum Sparren**: während
der Sparren entlang der Falllinie geneigt verläuft, liegt die
Pfette quer dazu, parallel zu Traufe und First. In der
charakteristischen Anordnung des **Pfettendachs** trägt eine
Pfette mehrere Sparren über einen längeren Dachabschnitt und
leitet deren Lasten zu wenigen Auflagerpunkten (Stuhlsäulen,
tragende Wände, Giebelwände, Binder).

### Querschnitt und Werkstoff

Pfetten werden im Schweizer Wohnbau typisch als **Vollholz** in
Festigkeitsklasse C24 oder als **Brettschichtholz** (BSH, GL24h
oder GL28c bei größerer Spannweite) ausgeführt. Übliche
Querschnitte:

- 100/200 mm bis 140/240 mm bei mittleren Spannweiten,
- 160/280 mm bis 200/400 mm bei großen Spannweiten und Bindern,
- BSH-Querschnitte je nach Bemessung größer.

Die Pfette ist häufig hochkant verlegt (Höhe > Breite), weil sie
um die horizontale, zur Bauteilachse rechtwinklige Achse hauptsächlich
auf Biegung beansprucht wird. Konkrete Querschnittsfindung gehört
in die Bemessung (SIA 265 / EN 1995-1-1).

### Faserrichtung

Die Faserrichtung einer Pfette ist im Regelfall **parallel zur
Bauteilachse**. Bei BSH-Pfetten verlaufen die Lamellen-
Faserrichtungen ebenfalls parallel zur Bauteilachse, mit der
besonderen Möglichkeit überhöhter Vorkrümmung (Schalung) bei
großen Spannweiten.

### Drei Pfetten-Typen am Dach

Die drei Pfetten-Typen unterscheiden sich nur durch ihre **Lage am
Dach**, nicht durch ihre geometrische oder konstruktive Natur als
Pfette:

- **Fußpfette** (`fusspfette`): am Sparrenfuß, traufseitig. Häufig
  unmittelbar auf Mauerwerk gelagert (dann auch „Mauerlatte").
- **Mittelpfette** (`mittelpfette`): zwischen Fuß- und Firstpfette,
  als zusätzliche Sparrenauflage zur Reduktion der Sparren-
  Spannweite.
- **Firstpfette** (`firstpfette`): unmittelbar am First, am
  Sparrenfirstpunkt.

In einem klassischen Pfettendach mit drei Pfettenreihen je
Dachseite (Fuß-, Mittel-, First-) ist die Mittelpfette die statisch
am stärksten beanspruchte; die Firstpfette teilt sich die
Sparrenfirstpunkt-Last mit dem gegenüberliegenden Sparren.

### Pfette ≠ Latte ≠ Riegel

Aus zimmermannssprachlicher Sicht ist die saubere Trennung dieser
drei Begriffe wichtig (siehe Abgrenzung):

- **Pfette**: Hauptträger des Dachtragwerks, trägt Sparren oder
  Binder. Querschnitt typ. ab 100/200 mm.
- **Latte** (Dachlatte): Sekundärbauteil **auf** dem Sparren, quer
  dazu, als Auflage für die Eindeckung. Querschnitt typ. 24/48
  bis 40/60 mm.
- **Riegel**: horizontales Bauteil im **Wandbau** (zwischen
  Pfosten/Ständern), nicht im Dach. Im Dachbau wird der Begriff
  „Riegel" gelegentlich für Aussteifungs-Querhölzer verwendet,
  was hier abgelehnt wird.

### Typische Verbindungen an der Pfette

Diese Verbindungen sind Geometrien an Pfette und Sparren bzw.
Pfette und Stütze; sie werden in eigenen Glossareinträgen
definiert. Hier nur als Verortung:

- **Versatz** des Sparrenfußes auf der Fußpfette,
- **Kammverbindung** des Sparrens auf der Mittelpfette,
- **Zapfen** zwischen Pfette und Stuhlsäule,
- **Stoß** zweier Pfetten in Längsrichtung (Schräg-, Schwalben-
  schwanz-, Hakenblattstoß) bei langen Pfettenzügen.

## Beziehungen

- **Oberbegriff**: `bauteil`. Strukturell ist die Pfette ein
  Bauteil mit der zusätzlichen Rolle „Pfette" und den oben
  formalisierten geometrischen Constraints.
- **Bestandteile (partitiv)**:
  - **Bauteilachse** (`bauteilachse.Gerade`, vom Bauteil geerbt);
  - **Querschnitt** (rechteckig, hochkant im Regelfall);
  - **Werkstoff** (Vollholz oder BSH);
  - **Faserrichtung** (Annotation, Default ‖ d̂_Pfette).
- **Spezialisierungen** (eigene Glossareinträge):
  - **Firstpfette** (`firstpfette`): Pfette am First.
  - **Mittelpfette** (`mittelpfette`): Pfette zwischen Fuß- und
    Firstpfette (Synonym: Zwischenpfette).
  - **Fußpfette** (`fusspfette`): Pfette am Sparrenfuß /
    traufseitig (Synonyme: Mauerlatte, regional Schwellpfette).
- **Verwendung / Beziehung zu anderen Bauteilen**:
  - **Sparren** (`sparren`): liegt **auf** der Pfette; die Pfette
    ist Auflager des Sparrens.
  - **Binder** (`binder`, eigener Eintrag folgt): kann statt
    Sparren auf einer Pfette aufliegen; in Mischformen (z. B.
    Hauptbinder + Pfette + Sparren) Bestandteil mehrstufiger
    Tragsysteme.
  - **Stuhlsäule** (`stuhlsaeule`, eigener Eintrag folgt):
    Stütze, die eine Pfette an Zwischenpunkten unterstützt
    (typisch im liegenden / stehenden Stuhl).
  - **Wand** / **Mauerwerk**: Auflager für Fußpfette (Mauerlatte)
    und Giebelwand-Auflagerung beliebiger Pfetten.
  - **Dachkante** (`dachkante`): die Pfettenachse ist parallel zu
    einer Dachkante (Traufe, First, Höhenlinie).
- **Abgrenzung**:
  - **Sparren** (`sparren`): geneigtes Stab-Bauteil entlang der
    Falllinie. Pfette ist horizontal entlang einer Höhenlinie.
    Sparren und Pfette sind orthogonal zueinander angeordnet
    (innerhalb der Trägerebene der Dachfläche).
  - **Kehlbalken** (`kehlbalken`): horizontaler Querbalken
    **zwischen** einem Sparrenpaar zur Aussteifung; verbindet
    zwei Sparren statt mehrere Sparren zu tragen. Kein
    Längsträger, sondern Querstab.
  - **Riegel**: horizontales Bauteil im Wandbau; nicht
    Dachtragwerk.
  - **Latte / Konterlatte**: deutlich kleinerer Querschnitt;
    Sekundärbauteil zur Eindeckungs-Auflage. Die Latte liegt
    quer zum Sparren und parallel zur Pfette, ist aber
    funktional und dimensional kein Hauptträger.
  - **Schwelle** (`schwelle`): horizontales unteres Auflager im
    Wandbau (Schwellholz auf dem Fundament). Trotz formaler
    Ähnlichkeit (horizontaler Stab) keine Pfette, da nicht im
    Dachtragwerk.
  - **Rähm** (`raehm`): oberster horizontaler Längsträger einer
    Wand, oft Auflager für Sparrenfüße. In manchen Konstruktionen
    übernimmt das Rähm die Funktion einer Fußpfette; die saubere
    Trennung ist zimmermannssprachlich: Rähm gehört zur Wand,
    Fußpfette gehört zum Dachtragwerk. Die in CH verbreitete
    Bauweisen-Konstellation „Massivbau-Außenwand mit Holz-
    Dachstuhl" ersetzt das Rähm nicht durch eine Mauerlatte
    (Mauerlatte ist ein Dach-Bauteil im Sinne der Fußpfette,
    kein Wand-Bauteil im Sinne des Rähms); sie macht das Rähm
    konstruktiv überflüssig, weil keine Holzwand vorhanden ist.
  - **Binder** (`binder`, bereits angelegt): vorgefertigtes
    Trag-Aggregat (`oberbegriff: bauteilgruppe`); kann eine Pfette
    ablösen oder ergänzen, ist aber selbst kein Längsträger.
    Eine Pfette kann **Bestandteil höchstens einer Bauteilgruppe**
    sein (`hg_bauteilgruppe.md` Bed. 1 — exklusive Mitgliedschaft).
    Eine Pfettenbinder-Pfette gehört exklusiv zu diesem Binder.

## Implementierungshinweis

Datentyp (Domänen-Schicht, Kotlin, Schicht `domain.bauteil`):

```kotlin
package domain.bauteil

import domain.Toleranzen
import domain.bauteil.Bauteil
import domain.bauteil.Bauteilachse
import domain.geometrie.Einheitsvektor
import domain.geometrie.Punkt
import kotlin.math.abs

/**
 * Pfette als Bauteilrolle: horizontaler Längsträger des
 * Dachtragwerks, parallel zu einer Dachkante.
 *
 * Glossar: hg_pfette.md
 *
 * Oberbegriff der drei Spezialisierungen Firstpfette, Mittelpfette,
 * Fußpfette. Die generische Pfette enthält keine Lage-Festlegung
 * relativ zum First/zur Traufe; das ist Sache der Subtypen.
 */
sealed class Pfette {
    abstract val bauteil: Bauteil

    val achse: Bauteilachse.Gerade
        get() = (bauteil.geometrie as Bauteilgeometrie.Stab).achse
                as Bauteilachse.Gerade
    val laenge: Double get() = achse.laenge          // mm
    val richtung: Einheitsvektor get() = achse.richtung
    val hoehe: Double                                 // mm, mittlere z-Lage
        get() = (achse.anfang.z + achse.ende.z) / 2.0

    /**
     * Horizontalitätsprädikat: |⟨d̂, e_z⟩| ≤ KOLLINEAR_EPS.
     *
     * Sinus-Test gegen e_z-Parallelität; KOLLINEAR_EPS ist
     * bevorzugt für Lot- und Parallelitäts-Prädikate
     * (siehe hauptglossar/_KONVENTIONEN.md Sektion 4).
     */
    fun istHorizontal(eps: Double = Toleranzen.KOLLINEAR_EPS): Boolean =
        abs(richtung.z) <= eps

    /** Subtypen mit konkreter Lage am Dach. */
    abstract class Firstpfette : Pfette()
    abstract class Mittelpfette : Pfette()
    abstract class Fusspfette : Pfette()
}

sealed class PfetteEntartet {
    object Nullachse        : PfetteEntartet()
    object NichtHorizontal  : PfetteEntartet()
    object KeineParallelKante : PfetteEntartet()
}
```

- **Einheit**: Längen in mm (Double); Winkel intern in Radiant.
- **Identität**: `BauteilId` aus dem zugrunde liegenden Bauteil.
- **Invarianten** (in der jeweiligen Subtyp-Factory prüfen, bei
  Verletzung `Resultat.Fehler` mit `PfetteEntartet`-Variante;
  niemals Exception):
  1. Stabgeometrie und Bauteilachse vom Typ `Bauteilachse.Gerade`.
  2. Achsenlänge > Toleranzen.LAENGE_EPS — sonst `Nullachse`.
  3. |⟨d̂, e_z⟩| ≤ Toleranzen.KOLLINEAR_EPS — sonst `NichtHorizontal`
     (Sinus-Test, bevorzugt für Lot-Prädikate; siehe
     `_KONVENTIONEN.md` Sektion 4).
  4. Existenz einer Dachkante k im Tragwerks-Kontext mit
     |⟨d̂, d̂_k⟩| ≥ 1 − ε_W — sonst `KeineParallelKante`. Die
     Bedingung wird in der Konstruktion mit Bezug auf die
     zugeordnete Dachfläche geprüft.
- **Edge Cases**:
  - **Geneigte Pfette** (Pultdach mit kontinuierlich abfallender
    Pfette, oder „abgesetzte" Pfette über mehrere Höhen): nicht
    durch den vorliegenden Pfettenbegriff abgedeckt; entweder
    als segmentierte Pfettenfolge mit individuellen horizontalen
    Pfettenabschnitten oder als eigener Begriff
    `geneigte_pfette` (Folgearbeit).
  - **Gekrümmte BSH-Pfette**: würde Bauteilachse.Gekruemmt
    erfordern; Bedingung 2 ist dann punktweise (Tangenten-
    Horizontalität) zu prüfen. Im Standardfall liegen Pfetten
    gerade vor.
  - **Pfette als Mauerlatte ohne tragende Wand-/Säulen-Auflager**:
    konstruktiv möglich, aber statisch nur sinnvoll als
    „kontinuierliche Auflagerung auf der Mauerkrone"; die
    Modellierung erfolgt dann über ein Linien-Auflager
    (`auflager`, eigener Eintrag folgt).
- **Abgeleitete Eigenschaften** (als Funktionen):
  - `parallelKantenIm(t: Tragwerk): List<Dachkante>` — Dachkanten
    in `t`, deren Richtung kollinear zur Pfettenachse ist.
  - `getrageneSparrenIn(t: Tragwerk): List<Sparren>` — Sparren in
    `t`, deren Bauteilachse die Pfettenachse innerhalb
    Toleranzen schneidet (Bemessungs-Hilfsfunktion).
- **Bezeichner-Konvention** (CLAUDE.md): Klasse heißt `Pfette`
  (deutsch, Glossarbegriff); Spezialisierungen heißen
  `Firstpfette`, `Mittelpfette`, `Fusspfette`.

## Quellen

**Primär (normativ):**

- SIA 265:2021, „Holzbau", Schweizerischer Ingenieur- und
  Architektenverein, Zürich.
- SIA 232/1:2020, „Geneigte Dächer", Schweizerischer Ingenieur-
  und Architektenverein, Zürich.
- DIN EN 1995-1-1:2010-12, „Eurocode 5: Bemessung und Konstruktion
  von Holzbauten – Teil 1-1".
- DIN 1052:2008-12, „Entwurf, Berechnung und Bemessung von
  Holzbauwerken".

**Sekundär:**

- Lignum (Hrsg.): *Holzbautabellen HBT.* Lignum, Zürich, aktuelle
  Auflage.
- Lignum (Hrsg.): *Lignatec — Geneigte Dächer in Holzbauweise.*
  Lignum, Zürich, aktuelle Auflage.
- Mönck, W.; Rug, W.: *Holzbau – Bemessung und Konstruktion.*
  16. Auflage, Beuth, Berlin 2015.
- Blass, H. J.; Sandhaas, C.: *Ingenieurholzbau – Grundlagen der
  Bemessung.* KIT Scientific Publishing, Karlsruhe 2016.
- Natterer, J.; Herzog, T.; Volz, M.: *Holzbau-Atlas.* 4. Auflage,
  Birkhäuser, Basel 2003.
- Gerner, M.: *Fachwerk – Instandsetzung, Sanierung, Neubau.*
  DVA, 7. Auflage 2007.

**Korpus (nicht autoritativ):**

- Holzbau Deutschland, Merkblatt „Begriffe und Klassifizierungen
  für den Holzbau" (abgerufen 2026-05-08).
- Wikipedia, Lemma „Pfette" (abgerufen 2026-05-08).
