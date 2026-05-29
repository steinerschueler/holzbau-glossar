---
id: saeule
benennung: Säule
synonyme: [Säulenstütze, "freistehende Säule", "klassische Säule"]
abgelehnte_benennungen: [Stütze, Pfeiler, Pilaster, column, pillar, "free-standing column"]
oberbegriff: stuetze
begriffstyp: bauteilrolle
voraussetzungen: [stuetze, bauteil, bauteilachse, einheitsvektor, weltkoordinatensystem, toleranzen]
abgrenzung_zu: [stuetze, staender, haengesaeule, stuhlsaeule, pfeiler, pilaster, kapitell, basis, schaft, bauteil]
status: entwurf
theorie_pflichtig: required
quellen_primär:
  - "DIN 1045-1 'Tragwerke aus Beton, Stahlbeton und Spannbeton — Teil 1: Bemessung und Konstruktion', Beuth, Berlin [via: Wikipedia/Stütze (Bauteil)]: Querschnitts-Bedingung (q_max ≤ 4·q_min) für Stützen, geerbt für die Säule als Spezialisierung. Volltext nicht direkt eingesehen."
quellen_sekundär:
  - "Wikipedia, Lemma 'Säule', de.wikipedia.org/wiki/S%C3%A4ule: 'Eine Säule ist ein lotrechter, freistehender Pfeiler, eine Stütze aus Holz, Stein, Ziegel oder Metall mit rundem oder polygonalem Querschnitt.' Klassische Komponenten Basis, Schaft, Kapitell; Säulenordnungen (Dorisch, Ionisch, Korinthisch, Toskanisch, Komposit); Entasis als subtile Schaft-Verjüngung."
  - "Wikipedia, Lemma 'Säulenordnung', de.wikipedia.org/wiki/S%C3%A4ulenordnung — architektonische Klassifikation der Säulenproportionen."
  - "Wikipedia, Lemma 'Liste von Fachbegriffen des Zimmererhandwerks' [via: Welle-9-Recherche §B.2]: 'Säule = Stütze mit gleichbleibendem Querschnitt' — in Konflikt mit Wikipedia/Säule (Entasis-Befund), siehe Quellenkonflikt-Punkt 2."
  - "Vitruvius: De architectura libri decem (etwa 25 v. Chr.) — antike Säulenordnungen, klassische Säulen-Proportionsregeln. Nicht direkt eingesehen, über Wikipedia/Säulenordnung."
  - "Recherche-Bericht: docs/recherche/2026-05-16_tragglieder_vertikal.md §D."
quellenkonflikt: |
  Vier Punkte sind in der Recherche
  (`docs/recherche/2026-05-16_tragglieder_vertikal.md` §D)
  auflösungs-bedürftig und werden hier ausdrücklich festgelegt.

  **(1) Säule als Subtyp von Stütze (klassisch-architektonisch).**
  Wikipedia/Säule definiert die Säule als „lotrechten, freistehenden
  Pfeiler, eine Stütze aus Holz, Stein, Ziegel oder Metall mit
  rundem oder polygonalem Querschnitt". Strukturell ist jede Säule
  eine Stütze (sie erfüllt die Geometrie- und Lastpfad-Bedingungen
  der Stütze), aber nicht jede Stütze ist eine Säule — der
  architektonisch-klassische Charakter (Säulenordnung, Basis-Schaft-
  Kapitell-Dreigliederung, oft runder oder polygonaler Querschnitt
  mit Entasis) macht die Säule zu einer Spezialisierung.

  Eigene Festlegung: `oberbegriff: stuetze`. Die Säule ist
  bauteilrolle-Subtyp der Stütze; sie erbt die DIN-1045-1-
  Querschnitts-Bedingung (q_max ≤ 4·q_min) und ergänzt sie um die
  architektonische Gliederung in Basis, Schaft und Kapitell.
  Strukturell sind diese drei Bereiche partitive Bestandteile der
  Säule, im aktuellen Glossarstand aber nicht als eigene
  Hauptglossar-Einträge geführt (Folgearbeit-Trigger bei einer
  hypothetischen Tempelbau-/Restaurierungs-Tool-Phase).

  **(2) Falsifikation „Säule = konstanter Querschnitt".** Die
  Wikipedia-Liste-der-Fachbegriffe-des-Zimmererhandwerks führt
  „Säule = Stütze mit gleichbleibendem Querschnitt". Wikipedia/Säule
  selbst (Haupt-Lemma) widerlegt diese Lesart: die klassische Säule
  wird mit **Entasis** (subtile Verjüngung des Schafts zum Kapitell
  hin) ausgeführt, die Säulenordnungen schreiben präzise
  Verjüngungs-Verhältnisse vor (Dorisch ≈ 1:6, Ionisch ≈ 1:8,
  Korinthisch ≈ 1:10 — Schafthöhe zum unteren Säulendurchmesser).

  Eigene Festlegung: Die Säule ist **nicht** durch konstanten
  Querschnitt charakterisiert, sondern durch die architektonische
  Gliederung (Basis, Schaft, Kapitell) und die klassischen
  Säulenordnungen. „Konstanter Querschnitt" trifft eher die
  Ingenieur-Stütze (DIN-1045-1) ohne architektonische Gliederung,
  ist aber auch dort keine konstitutive Bedingung.

  Die Wikipedia-Liste-Fachbegriffe ist als sekundär-aggregierende
  Quelle einzustufen und wird vom Haupt-Lemma Wikipedia/Säule
  überstimmt.

  **(3) Im modernen Holzbau-Korpus nicht alleinstehend aktiv.** Im
  modernen Holzbau (Lignum, SIA 265, ETH-Lehre, CH-Praxis) tritt
  „Säule" als alleinstehende Bauteilbenennung **nicht aktiv** auf.
  Sie ist primär ein **Wortstamm-Anker** für die Komposita
  `stuhlsaeule` (Welle 13) und `haengesaeule` (Welle 13), die
  ihrerseits eigenständige Bauteilrollen sind und **nicht** als
  Subtypen der Säule geführt werden — denn ihre konstruktive
  Funktion (Druck-Element im Dachstuhl bzw. Zug-Element im
  Hängewerk) ist primär, nicht der ästhetisch-architektonische
  Säulen-Charakter.

  Eigene Festlegung: `hg_saeule.md` ist als Disambiguations-
  Splitter und Wortstamm-Anker geführt. Die Komposita
  `stuhlsaeule` und `haengesaeule` haben **nicht** `saeule` als
  `oberbegriff:`, sondern direkt `bauteil`. Diese Asymmetrie ist
  konzeptuell vertretbar, weil die Komposita nicht
  architektonisch-klassische Säulen sind, sondern konstruktiv
  spezialisierte Vertikalbauteile, die nur den Wortstamm teilen.

  **(4) Säulenordnungen außerhalb des App-Scope.** Die fünf
  klassischen Säulenordnungen (Dorisch, Ionisch, Korinthisch,
  Toskanisch, Komposit) sind eine architektonische Klassifikation
  mit präzisen Proportions-Regeln (Schaft:Durchmesser-Verhältnis,
  Kapitell-Geometrie, Triglyphen/Akanthus-Schmuck etc.). Diese
  Klassifikation ist im aktuellen App-Scope (Phase D7/D8
  Sparrenkerven-Tool) **nicht** abgebildet; sie ist Folgearbeit-
  Trigger bei einer hypothetischen Tempelbau-/Restaurierungs-Tool-
  Phase, in der barocke Innenraum-Holzsäulen, klassische
  Holztempel-Säulen oder restauratorische Säulen-Modellierung
  relevant würden.

  Eigene Festlegung: Die `Saeulenordnung`-Klassifikation wird im
  Eintrag erwähnt (Erläuterung), aber nicht als Pflicht-Merkmal
  der Säule geführt; eine `saeule`-Instanz im App-Code hat
  optional ein `ordnung:`-Merkmal mit den fünf klassischen
  Werten plus `UNGEORDNET` als Default.
---

## Prosa-Definition

Eine **Säule** ist eine Bauteilrolle, die als architektonisch-
klassische Spezialisierung der Stütze auftritt, deren Bauteilachse
lotrecht verläuft, deren Querschnitt typisch rund oder polygonal ist
und deren Schaft in eine Dreigliederung aus Basis (Sockel-Element am
Stützenfuß), Schaft (eigentlicher tragender Stab) und Kapitell
(Bekrönungs-Element am Stützenkopf) gegliedert ist, gegebenenfalls
nach einer der klassischen Säulenordnungen proportioniert.

## Mathematische Definition

Sei

- B ein Bauteil im Sinne von `bauteil`,
- S eine Stütze im Sinne von `stuetze` mit zugrunde liegendem Bauteil
  B (alle Stützen-Bedingungen 1–6 von `hg_stuetze.md` erfüllt),
- a(B) = Bauteilachse.Gerade(p_a, p_e) die Bauteilachse mit
  d_hat := (p_e − p_a) / ‖p_e − p_a‖,
- e_z := (0, 0, 1)ᵀ die vertikale Welt-Achse,
- ε_K := Toleranzen.KOLLINEAR_EPS.

Dann heißt B eine **Säule** genau dann, wenn die folgenden
Bedingungen alle erfüllt sind:

1. **Stützen-Konformität**: B ist eine Stütze im Sinne von
   `hg_stuetze.md` (alle dortigen Bedingungen 1–6).

2. **Strikte Lotrechtheit**: Die Bauteilachse ist exakt lotrecht (im
   Toleranz-Rahmen):
   ```
   ‖d_hat × e_z‖ ≤ ε_K,
   ```
   geerbt von `stuetze` Bedingung 2; bei der Säule ohne mögliche
   Neigung (anders als bei der schräggestellten Stuhlsäule im
   liegenden Stuhl, die per Definition nicht als Säule
   qualifiziert).

3. **Freistehender Charakter**: B ist nicht in eine Wand-, Stuhl-
   oder Hängewerk-Bauteilgruppe eingebunden; B steht frei im
   architektonischen Raum (Säulenhalle, Tempel, barocker Innenraum)
   oder dient als freistehender Lastträger einer Decken-Auflagerung.

4. **Architektonische Gliederung (zugesichert, nicht formal
   geprüft)**: B trägt eine Dreigliederung aus Basis, Schaft und
   Kapitell, oder ist als Schaft-Säule ohne explizite Basis/Kapitell-
   Glieder ausgeführt (vereinfachte moderne Säule). Diese Bedingung
   ist eine **architektonische Zusicherung**, die im Glossar nicht
   formal überprüft wird — sie unterscheidet die Säule
   konzeptuell-architektonisch von einer reinen Ingenieur-Stütze
   gleicher Geometrie.

Optional kann B eine **Säulenordnung** ordnung(B) ∈
{Dorisch, Ionisch, Korinthisch, Toskanisch, Komposit, Ungeordnet}
tragen.

## Wohldefiniertheit

- **Existenz**: Für jede klassische Holzsäule (barocker Innenraum,
  Tempelarchitektur mit Holzsäulen, restauratorisch erhaltene
  historische Holzsäule), jede klassische Stein-/Mauerwerk-Säule
  und jede moderne Stahl-/Stahlbeton-Säule mit Säulen-Gestus sind
  alle Bedingungen erfüllbar.

- **Eindeutigkeit der Säulenrichtung**: Bedingung 2 fixiert die
  Stützenrichtung auf d_hat ≈ +e_z bis auf ε_K, geerbt von `stuetze`.

- **Konsistenz mit `stuetze`**: Per Bedingung 1 ist jede Säule eine
  Stütze. Die Stützen-Substanz (Werkstoff-Neutralität, Querschnitts-
  Bedingung q_max ≤ 4·q_min, Druck-Lastpfad, Ausschluss der Wand-
  Inzidenz) wird vollständig geerbt.

- **Disjunktheit zu `stuhlsaeule` und `haengesaeule`**: Beide
  Komposita-Bauteilrollen sind **nicht** Säulen im Sinne dieses
  Eintrags, weil sie Bedingung 3 (freistehender Charakter)
  verletzen — die Stuhlsäule ist in eine Stuhl-Konstruktion
  eingebunden (Stuhlpfetten-Anschluss am Kopf, Stuhlschwellen-
  Anschluss am Fuß), die Hängesäule in ein Hängewerk (Bundbalken-
  Anker unten, Strebe-Schnittpunkt-Anker oben). Die App führt
  Stuhlsäule und Hängesäule daher als Geschwister-Bauteilrollen
  direkt unter `bauteil`, nicht unter `saeule`.

- **Nicht-formale Architektur-Zusicherung**: Bedingung 4 wird im
  Glossar nicht formal überprüft. Eine moderne Säule ohne explizite
  Basis/Kapitell-Glieder (reine Schaft-Säule) qualifiziert auch als
  Säule, sofern der freistehende Charakter und die architektonische
  Inszenierung gegeben sind. Die formale Überprüfung wäre Aufgabe
  einer hypothetischen Architektur-/Tempelbau-Modellierungs-
  Schicht.

- **Nicht-Zirkularität**: Die Definition stützt sich auf `stuetze`
  (Welle 13, dieselbe Welle) und die weiter unten liegenden
  Primitive. Welle-13-interne Verweise sind nach
  HG_KONVENTIONEN.md §6 zulässig.

## Erläuterung (nicht normativ)

Die Säule ist im **klassisch-architektonischen Bauwesen** das
ästhetisch und konstruktiv aufgeladene Vertikalbauteil. Ihre lange
Geschichte (von antiker Tempelarchitektur über romanische,
gotische, Renaissance- und barocke Architektur bis in moderne
Reinterpretationen) hat ein präzises Vokabular von
Proportions-Regeln, Schmuck-Elementen und Material-Konventionen
hervorgebracht.

### Klassische Dreigliederung

Eine klassische Säule besteht aus drei vertikal aufeinander
gestapelten Teilen:

- **Basis** (Sockel-Element am Stützenfuß): überträgt die Säulen-
  Last in das Stylobat (Tempelboden) oder das Säulen-Postament;
  vermittelt zwischen Stützenfuß und Boden. In der toskanischen
  und dorischen Ordnung oft fehlend.
- **Schaft** (eigentlicher tragender Stab): der lotrechte,
  druckbeanspruchte Stab. Klassisch oft mit **Entasis** versehen —
  einer subtilen, mathematisch ausgefeilten Verjüngung von unten
  nach oben (Vitruv schreibt unterschiedliche Verjüngungs-
  Verhältnisse je Säulenordnung vor). Die Schaft-Oberfläche kann
  glatt, kanneliert (mit senkrechten Rillen) oder mit Reliefschmuck
  ausgeführt sein.
- **Kapitell** (Bekrönungs-Element am Stützenkopf): vermittelt
  zwischen dem schlanken Schaft und der breiteren Tragebene
  (Architrav, Decke, Gewölbe). Trägt das Schmuck-Repertoire der
  jeweiligen Säulenordnung: dorische Echinus-Volute, ionische
  Voluten, korinthisches Akanthus-Blätterwerk.

Diese Dreigliederung ist konstruktiv eher Tradition als
Konstruktions-Notwendigkeit; eine moderne Säule kann als reine
Schaft-Säule ohne explizite Basis und Kapitell ausgeführt sein
und qualifiziert dennoch als Säule.

### Klassische Säulenordnungen

Die fünf klassischen Säulenordnungen (Vitruv, vier Bücher zum
griechisch-römischen Bau-Kanon) sind:

| Ordnung | Schaft:Durchmesser | Kapitell-Merkmal | Herkunft |
|---|---|---|---|
| **Toskanisch** | ≈ 1:7 | schlicht, ohne Schmuck | etruskisch/römisch |
| **Dorisch** | ≈ 1:6 (griechisch) bis 1:7 (römisch) | Echinus mit Abakus | griechisch |
| **Ionisch** | ≈ 1:8 bis 1:9 | Volutenkapitell | griechisch (Kleinasien) |
| **Korinthisch** | ≈ 1:10 | Akanthus-Blätter | griechisch (Korinth) |
| **Komposit** | ≈ 1:10 | Ionische Voluten + korinthische Akanthus | römisch |

Diese Ordnungen sind im aktuellen App-Scope **nicht modelliert**;
die `Saeulenordnung`-Klassifikation steht als optionales Merkmal
am Säulen-Bauteil zur Verfügung, wird aber nicht formal überprüft.

### Säule im modernen Holzbau

Im **modernen Holzbau-Korpus** (Lignum, SIA 265, ETH-Lehre, CH-
Praxis) tritt die Säule als alleinstehende Bauteilbenennung **nicht
aktiv** auf. Sie ist primär ein **Wortstamm-Anker** für die
Komposita **Stuhlsäule** (`hg_stuhlsaeule.md`) und **Hängesäule**
(`hg_haengesaeule.md`), die ihrerseits eigenständige Bauteilrollen
mit konstruktiver Funktion im Dachstuhl bzw. Hängewerk sind. Die
moderne CH-Holzbau-Praxis verwendet für freistehende lotrechte
Holz-Tragglieder durchgängig **Stütze** (`hg_stuetze.md`), nicht
Säule.

Historische Holzsäulen treten in barocker Innenraum-Architektur,
in klassischen Holztempel-Bauten und in restauratorisch erhaltenen
Bauwerken (Schloss-Kapellen, Empore-Tragwerke etc.) auf; sie sind
im aktuellen App-Plan nicht zentraler Modellierungs-Gegenstand,
aber als Disambiguations-Splitter und Wortstamm-Anker im Glossar
geführt.

### Säule vs. Pfeiler vs. Pilaster

- **Säule**: freistehend, lotrecht, runder oder polygonaler
  Querschnitt mit ästhetisch-architektonischer Gliederung
  (Basis-Schaft-Kapitell).
- **Pfeiler** (`pfeiler`, kein eigener Eintrag): freistehendes
  Mauerwerks- oder Stein-Vertikalbauteil mit oft rechteckigem
  Querschnitt; im DACH-Bauwesen abgegrenzt von der Säule durch
  Werkstoff (Mauerwerk/Stein vs. überwiegend Stein/Holz für die
  Säule) und Querschnitts-Form (rechteckig vs. rund). Die Trennung
  ist allerdings unscharf — historisch werden „Pfeiler" und „Säule"
  je nach Sprachgebrauch verwendet.
- **Pilaster** (`pilaster`, kein eigener Eintrag): an eine Wand
  angelagerte (nicht freistehende) flache Säule mit ornamentaler
  Funktion; nicht primär tragend. Im Holzbau praktisch nicht
  vorkommend.

### Andere Bedeutungen / Englisch

- **`column`**: Standard-Übersetzung der Säule und der Stütze; im
  Englischen wird die architektonische Differenzierung weniger
  scharf gezogen.
- **`pillar`**: oft synonym, gelegentlich mit Pfeiler-Konnotation.
- **`pilaster`**: international, wie deutsch.

## Beziehungen

- **Oberbegriff**: `stuetze`. Die Säule ist Bauteilrolle-Subtyp
  der werkstoffneutralen Stütze; sie erbt alle Stützen-Bedingungen
  und ergänzt sie um Architektur-Zusicherung und freistehenden
  Charakter.
- **Bestandteile (partitiv, geerbt von `bauteil` und `stuetze`)**:
  - **Bauteilachse** (`bauteilachse.Gerade`), lotrecht;
  - **Querschnitt** (rund, polygonal, oder rechteckig; q_max ≤
    4·q_min);
  - **Werkstoff** (Holz, Stein, Mauerwerk, Beton, Stahl,
    Aluminium);
  - **Faserrichtung** (bei Holzsäulen axial).
- **Architektonische Bestandteile (zugesichert, nicht im aktuellen
  Glossar formal geführt; Folgearbeit-Trigger)**:
  - **Basis** (`basis`, Forward-Verweis, kein eigener Eintrag):
    Sockel-Element am Stützenfuß.
  - **Schaft** (`schaft`, Forward-Verweis, kein eigener Eintrag):
    tragender Stab mit Entasis.
  - **Kapitell** (`kapitell`, Forward-Verweis, kein eigener
    Eintrag): Bekrönungs-Element am Stützenkopf.
- **Spezialisierungen**:
  - Im aktuellen Glossar keine. Die fünf klassischen
    Säulenordnungen (Dorisch, Ionisch, Korinthisch, Toskanisch,
    Komposit) sind als optionales Merkmal `ordnung:`, nicht als
    Subtyp-Hierarchie geführt.
- **Abgrenzung**:
  - **Stütze** (`stuetze`): Oberbegriff. Jede Säule ist eine
    Stütze; nicht jede Stütze ist eine Säule (Architektur-
    Zusicherung und freistehender Charakter fehlen).
  - **Ständer** (`staender`): Wand-Bauteilrolle. Keine Säule kann
    Ständer sein (Bedingung 6 von `stuetze` schließt Wand-Inzidenz
    aus, wird in `saeule` geerbt).
  - **Hängesäule** (`haengesaeule`): Zug-Element im Hängewerk;
    nicht freistehend, holz-spezifisch. Wortstamm-Verwandtschaft
    nur formal.
  - **Stuhlsäule** (`stuhlsaeule`): Druck-Element im Dachstuhl;
    nicht freistehend, holz-spezifisch. Wortstamm-Verwandtschaft
    nur formal.
  - **Pfeiler** (`pfeiler`, Forward-Verweis, kein eigener Eintrag):
    freistehendes Mauerwerks-/Stein-Vertikalbauteil. Trennung
    durch Werkstoff und Querschnitts-Form.
  - **Pilaster** (`pilaster`, Forward-Verweis, kein eigener
    Eintrag): wand-angelagerte flache Säule; im Holzbau nicht
    relevant.
  - **Kapitell** (`kapitell`, Forward-Verweis, kein eigener
    Eintrag): partitiver Bestandteil der Säule am Stützenkopf.
  - **Basis** (`basis`, Forward-Verweis, kein eigener Eintrag):
    partitiver Bestandteil der Säule am Stützenfuß.
  - **Schaft** (`schaft`, Forward-Verweis, kein eigener Eintrag):
    partitiver Bestandteil der Säule.
  - **Bauteil** (`bauteil`): über `stuetze` mittelbarer
    Oberbegriff.

## Implementierungshinweis

Datentyp (Domänen-Schicht, Kotlin, Schicht `domain.bauteil`):

```kotlin
package domain.bauteil

import domain.bauteil.Stuetze

/**
 * Säule als architektonisch-klassischer Subtyp der Stütze: lotrechtes
 * Stab-Bauteil mit Dreigliederung Basis-Schaft-Kapitell und ggf.
 * Säulenordnung. Konstruktiv eine Stütze; ästhetisch eine
 * architektonisch inszenierte Sonderform.
 *
 * Glossar: hg_saeule.md
 *
 * Architektur-Zusicherung (Basis-Schaft-Kapitell) wird im Glossar
 * nicht formal überprüft. Säulenordnung ist optionales Merkmal.
 *
 * Im modernen Holzbau-Korpus nicht alleinstehend aktiv; primär als
 * Wortstamm-Anker für stuhlsaeule und haengesaeule geführt.
 */
data class Saeule(
    val stuetze: Stuetze,
    val ordnung: Saeulenordnung = Saeulenordnung.UNGEORDNET,
)

enum class Saeulenordnung {
    DORISCH,
    IONISCH,
    KORINTHISCH,
    TOSKANISCH,
    KOMPOSIT,
    UNGEORDNET,
}
```

- **Einheit**: Längen in mm (Double); Winkel intern in Radiant.
- **Identität**: `BauteilId` aus dem zugrunde liegenden Bauteil
  (geerbt von `Stuetze`).
- **Invarianten** (in der Factory `saeuleAusStuetze(...)` prüfen):
  1. Alle Stützen-Invarianten (Stab-Geometrie, Lotrechtheit,
     Vorzeichen, Querschnitts-Verhältnis, keine Wand-Inzidenz)
     sind erfüllt.
  2. Freistehender Charakter: keine Mitgliedschaft in einer
     Stuhl-, Hängewerk- oder Wand-Bauteilgruppe (Cross-Aggregat-
     Prüfung).
  3. Architektur-Zusicherung wird nicht formal geprüft.
- **Edge Cases**:
  - **Säule ohne Basis/Kapitell** (moderne Schaft-Säule): zulässig;
    die Architektur-Zusicherung ist nicht formal überprüft.
  - **Polygonale Säule** (achteckiger Schaft, statt rund):
    zulässig; Querschnitts-Form ist nicht eingeschränkt, solange
    q_max ≤ 4·q_min erfüllt ist (geerbt von Stütze).
  - **Kannelierte Säule** (mit senkrechten Rillen am Schaft):
    zulässig; die Schaft-Oberflächengestaltung ist nicht
    konstitutiv für die Säulen-Bauteilrolle.
- **Folgearbeit-Trigger**:
  - `hg_kapitell.md`, `hg_basis.md`, `hg_schaft.md`: partitive
    Säulen-Bestandteile. Trigger: erste architektonische
    Modellierung mit Säulen-Detail (Tempelbau-Tool,
    Restaurierungs-Tool).
  - `hg_pfeiler.md`: Mauerwerks-/Stein-Pfeiler als Geschwister-
    Bauteilrolle. Trigger: erste Mauerwerk-Modellierung.
  - `hg_pilaster.md`: wand-angelagerte flache Säule. Trigger:
    erste klassische Innenarchitektur-Modellierung.
  - **Tempelbau-/Restaurierungs-Tool**: aktiviert die
    Architektur-Zusicherung und die Säulenordnungs-Klassifikation
    formal. Trigger: erste konkrete App-Phase, die Säulenordnungen
    modelliert.

## Quellen

**Primär (normativ):**

- DIN 1045-1, „Tragwerke aus Beton, Stahlbeton und Spannbeton —
  Teil 1: Bemessung und Konstruktion", Beuth, Berlin.

**Sekundär:**

- Wikipedia, Lemmata „Säule", „Säulenordnung", „Kapitell", „Basis
  (Architektur)", „Schaft (Architektur)", „Entasis", „Pfeiler",
  „Pilaster" (abgerufen 2026-05-16).
- Vitruvius: *De architectura libri decem.* etwa 25 v. Chr.
- Recherche-Bericht: `docs/recherche/2026-05-16_tragglieder_vertikal.md` §D.

**Korpus (nicht autoritativ):**

- architektur-lexikon.de „Säule" — konvergent.
- de.wikipedia.org „Liste von Fachbegriffen des Zimmererhandwerks"
  (Konflikt-Quelle, siehe Quellenkonflikt-Punkt 2).
