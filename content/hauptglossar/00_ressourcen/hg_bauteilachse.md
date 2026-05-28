---
id: bauteilachse
benennung: Bauteilachse
synonyme: ["Stabachse", "Bauteilhauptachse", "geometrische Längsachse", "Schwerlinie (Stabbauteil)"]
abgelehnte_benennungen: [Mittellinie, Stablinie, "member axis", "centerline", "neutral axis"]
oberbegriff: achse
begriffstyp: generisch
voraussetzungen: [achse, gerade, strecke, streckenzug, bauteil, querschnitt, toleranzen]
abgrenzung_zu: [achse, gerade, faserrichtung, bauteil, falllinie, schwerlinie_querschnitt]
status: entwurf
theorie_pflichtig: required
quellen_primär:
  - "SIA 265:2021, 'Holzbau', Schweizerischer Ingenieur- und Architektenverein, Abschnitt 4 (Bemessung), Bezugsachsen für Querschnittswerte und Bauteillängen."
  - "DIN EN 1995-1-1:2010-12 (Eurocode 5), Abschnitt 5 (Tragwerksberechnung) und Abschnitt 6 (Grenzzustände der Tragfähigkeit), Stab- und Bauteilachsen als Bezug für Schnittgrößen."
  - "DIN 1052:2008-12, Abschnitt 5 (Berechnungsverfahren), Stabachsen als Bezugsachsen der Tragwerksberechnung."
  - "DIN 4074-1:2012-06, 'Sortierung von Holz nach der Tragfähigkeit – Teil 1: Nadelschnittholz', Abschnitt 5 (Sortiermerkmale), Faserneigung als Tangens des Winkels zwischen Faser und Bauteillängsachse."
quellen_sekundär:
  - "Lignum (Hrsg.): Holzbautabellen HBT, Lignum, Zürich, aktuelle Auflage, Kap. 'Bauteile und Querschnitte'."
  - "Mönck, W.; Rug, W.: Holzbau – Bemessung und Konstruktion. 16. Aufl., Beuth, Berlin 2015, Kap. 4 'Stabbauteile'."
  - "Blass, H. J.; Sandhaas, C.: Ingenieurholzbau – Grundlagen der Bemessung. KIT Scientific Publishing, Karlsruhe 2016, Kap. 5 'Stabwerke'."
  - "Natterer, J.; Herzog, T.; Volz, M.: Holzbau-Atlas. 4. Aufl., Birkhäuser, Basel 2003, Kap. 'Bauteile und Stabwerke'."
quellenkonflikt: |
  Weder SIA 265, EN 1995-1-1 noch DIN 1052 enthalten eine geschlossene
  Definition der „Bauteilachse" oder „Stabachse"; alle drei Normen
  verwenden den Begriff vorausgesetzt als Bezugsachse der Tragwerks-
  berechnung. DIN 4074-1 nennt die „Bauteillängsachse" als Bezug für
  die Faserneigung, ohne sie geometrisch zu definieren. In der
  Sekundärliteratur (Mönck/Rug, Blass/Sandhaas, Natterer/Herzog) wird
  die Stabachse durchgängig als „Verbindungslinie der Querschnitts-
  schwerpunkte entlang der Bauteillänge" verstanden.

  Eigene Festlegung: die Bauteilachse eines Stabbauteils ist die
  Verbindungslinie der Flächenschwerpunkte aller Querschnitte des
  Bauteils, gemessen rechtwinklig zu dieser Linie. Im häufigen geraden
  Fall (prismatisches Stabbauteil ohne Krümmung) reduziert sich die
  Bauteilachse auf eine Strecke zwischen Anfangs- und Endquerschnitts-
  schwerpunkt; im seltenen gekrümmten Fall (gebogenes BSH) auf einen
  Streckenzug oder eine Kurve.

  Die Bauteilachse ist eine Achse im Sinne von `achse` (Rolle:
  Bauteilhauptachse) und gleichzeitig eine **geometrische** Eigenschaft
  des Bauteils — abzugrenzen von der **materiellen** Hauptachse, der
  `faserrichtung` (siehe `hg_faserrichtung.md`, Abschnitt Beziehungen).
  Beide können übereinstimmen, müssen aber nicht.

  Diese Festlegung ist konsistent mit allen konsultierten Quellen.
---

## Prosa-Definition

Die **Bauteilachse** eines Stabbauteils ist die Achse, die durch die
Flächenschwerpunkte aller rechtwinklig zu ihr geschnittenen Querschnitte
des Bauteils verläuft, im häufigen geraden Fall als Strecke zwischen
Anfangs- und Endquerschnittsschwerpunkt, im allgemeinen Fall als
Streckenzug oder Kurve, und damit die geometrische Hauptachse des
Bauteils im Sinne der Längsausdehnung.

## Mathematische Definition

Sei

- B ein **Stabbauteil** im Sinne von `bauteil` mit
  `geometrie ∈ 𝒢_stab` (1D-dominant; siehe `bauteil`),
- K(s) ⊂ ℝ³ der **Querschnitt** von B an der Stelle s ∈ [0, L] der
  natürlichen Längsparameterisierung (eine ebene, beschränkte
  Punktmenge rechtwinklig zur Bauteilachse; siehe `querschnitt`),
- z(s) ∈ ℝ³ der **Flächenschwerpunkt** des Querschnitts K(s)
  (Centroid),
- L > 0 die Bauteillänge entlang der Bauteilachse.

Dann ist die **Bauteilachse** von B die Punktmenge

```
A(B) := { z(s) ∈ ℝ³ | s ∈ [0, L] }
```

zusammen mit ihrer natürlichen Parametrisierung s ↦ z(s).

**Gerader Fall** (prismatisches Stabbauteil, dominant im Holzbau):
Wenn alle Querschnittsschwerpunkte z(s) auf einer gemeinsamen Geraden
g ⊂ ℝ³ liegen, ist die Bauteilachse die Strecke

```
A(B) = [z(0), z(L)] ⊂ g,
```

mit Anfangspunkt p_a := z(0), Endpunkt p_e := z(L), Trägergerade
g = g(p_a, p_e − p_a) und Länge L = ‖p_e − p_a‖. Als Achse im Sinne
von `achse` ist A(B) = (g, ρ = Bauteilhauptachse).

**Gekrümmter Fall** (selten, z. B. gebogene Brettschichtholz-Bögen):
Wenn die Schwerpunkte z(s) keine gemeinsame Gerade bilden, ist A(B)
ein Streckenzug (bei polygonaler Approximation) oder eine glatte
Kurve. In der Domänen-Schicht wird der gekrümmte Fall durch
Diskretisierung als `Streckenzug` repräsentiert (siehe
`streckenzug`).

**Vorzeichenkonvention** (wesentlich, da eine Strecke zwei mögliche
Orientierungen hat): Die Bauteilachse trägt eine kanonische
Richtung d̂ = (p_e − p_a) / ‖p_e − p_a‖ ∈ S². Die Wahl von p_a
(Anfangspunkt) und p_e (Endpunkt) ist **nicht** auf der Ebene des
generischen Bauteilachsen-Begriffs festgelegt, sondern durch das
**konkrete Bauteil** (Sparren, Pfette, Stütze etc.) zu konkretisieren.
Empfohlene Konventionen für Spezialisierungen:

- **Stütze**: p_a unten, p_e oben (d̂ lotrecht nach oben,
  d̂ = +e_z im lotrechten Standardfall).
- **Sparren** (und andere Bauteilrollen mit Falllinien-Bezug —
  Gratsparren, Kehlsparren): p_a an der Traufe, p_e am
  Sparrenfirstpunkt; d̂ zeigt **entgegen** der Falllinie der
  getragenen Dachfläche, also **bergauf von der Traufe zum
  Sparrenfirstpunkt**. Formal:
  ```
  ⟨d̂, ê_fall⟩ < 0    (d̂ und ê_fall sind antiparallel im prismatischen
                       Idealfall).
  ```
  Hintergrund: `ê_fall` zeigt per Konvention nach unten
  (⟨ê_fall, e_z⟩ ≤ 0; siehe `falllinie`, Abschnitt
  „Symbol-Konvention"). Die anschauliche Lesart „d̂ in Falllinien-
  Richtung" ist damit zweideutig und wird hier zugunsten der
  präzisen Vorzeichen-Aussage „d̂ entgegen ê_fall" abgelöst.
- **Pfette** (horizontale Bauteilrolle ohne Falllinien-Bezug —
  Fußpfette, Mittelpfette, Firstpfette): Die Vorzeichen-Empfehlung
  ist hier nicht von einer Falllinie abgeleitet, sondern von der
  Bauteilrolle und dem lokalen Bezeichnungs-Kontext (z. B.
  niedrigeres x in Welt-Koordinaten als p_a, höheres als p_e; oder
  steigende Achs-Bezeichnung A → B → C). Die konkrete Festlegung
  steht in den Einträgen `hg_pfette.md`, `hg_fusspfette.md`,
  `hg_mittelpfette.md`, `hg_firstpfette.md` (Forward-Verweis nach
  `_KONVENTIONEN.md` Sektion 6).

Diese Konkretisierungen werden in den jeweiligen Bauteilrollen-
Einträgen (`stuetze`, `sparren`, `pfette`) festgelegt; auf der Ebene
des generischen Begriffs `bauteilachse` ist die Vorzeichenkonvention
**durch die Bauteilrolle festzulegen**. Insbesondere gilt: die
Falllinien-Vorzeichen-Aussage greift **nur** bei Bauteilrollen mit
Falllinien-Bezug; für horizontale Bauteilrollen ist sie nicht
anwendbar.

Wesentliche abgeleitete Größen (gerader Fall):

- **Trägergerade**: g = g(p_a, p_e − p_a).
- **Richtungs-Einheitsvektor**: d̂ = (p_e − p_a) / ‖p_e − p_a‖.
- **Bauteillänge**: L = ‖p_e − p_a‖ (in mm).
- **Anfangs- und Endquerschnitt**: K(0) bzw. K(L) als ebene
  Punktmengen rechtwinklig zu d̂ in p_a bzw. p_e.

## Wohldefiniertheit

- **Existenz**: Für jedes Stabbauteil mit nicht-degeneriertem
  Querschnitt entlang der Bauteillänge ist der Flächenschwerpunkt
  z(s) jedes Querschnitts wohldefiniert (klassisches Resultat der
  ebenen Geometrie); die Punktmenge A(B) = { z(s) | s ∈ [0, L] }
  ist daher als Bild einer stetigen Funktion existent.
- **Eindeutigkeit (gerader Fall)**: Wenn die z(s) kollinear sind,
  ist die Bauteilachse als Strecke [z(0), z(L)] eindeutig bestimmt
  (modulo Vorzeichenkonvention; siehe oben). Die Trägergerade ist
  durch zwei verschiedene Punkte p_a ≠ p_e eindeutig.
- **Wohldefiniertheit der Querschnitts-Rechtwinkligkeit**: Die
  Definition setzt voraus, dass jeder Querschnitt K(s) rechtwinklig
  zur Bauteilachse selbst gewählt ist — eine zirkuläre Bedingung
  beim ersten Lesen. Die Auflösung: in der Praxis wird die Bauteil-
  achse zuerst durch die Bauteilkonstruktion festgelegt (zwei
  Endpunkte oder eine Mittellinie), und die Querschnitte werden
  per Konstruktion rechtwinklig zu ihr definiert. Im prismatischen
  Fall (häufigster Fall im Holzbau) ist diese Konstruktion trivial.
  Bei gekrümmten Bauteilen ist die Bauteilachse als Schwerlinie der
  konstruktiv vorgegebenen Querschnitte definiert; Existenz und
  Eindeutigkeit folgen dann iterativ über das Frenet-Serret-System
  (siehe Sekundärliteratur, Differentialgeometrie der
  Schwerlinien).
- **Vorzeichenkonvention**: Die Wahl von d̂ ∈ {±(p_e − p_a)/L} ist
  durch die Bauteilrolle festzulegen; ohne diese Festlegung ist
  die Bauteilachse als ungerichtete Achse wohldefiniert (Element
  von `achse` ohne Richtungsannotation), als gerichtete Achse jedoch
  nur modulo Vorzeichen.
- **Nicht-Zirkularität**: Die Definition stützt sich auf `achse`,
  `gerade`, `strecke`, `streckenzug`, `bauteil` und den
  **Flächenschwerpunkt** als bekanntes Konstrukt der ebenen
  Geometrie (Folgearbeit als eigener Eintrag möglich). Sie kommt
  nicht in ihrer eigenen Definition vor.
- **Bauteilachse ≠ Faserrichtung**: Die Bauteilachse ist eine
  geometrische Größe (Strecke bzw. Achse in ℝ³); die Faserrichtung
  ist eine materialbezogene Größe (Einheitsvektor in der Rolle
  „Materialhauptachse"). Beide werden in der Domänen-Schicht
  getrennt geführt; die `Faserneigung` (siehe `hg_faserrichtung.md`)
  ist der Tangens des Winkels zwischen ihnen.

## Erläuterung (nicht normativ)

Die Bauteilachse ist die zentrale Bezugsachse jedes Stabbauteils im
Holzbau. An ihr werden gemessen:

- die **Bauteillänge** als Abstand der Endquerschnittsschwerpunkte
  entlang der Achse;
- die **Schnittgrößen** (Normalkraft, Querkraft, Biegemoment) der
  Tragwerksberechnung, die als Belastungen entlang und quer zur
  Bauteilachse formuliert sind;
- die **Faserneigung** nach DIN 4074-1 als Winkel zwischen Faser
  und Bauteillängsachse;
- die **Anschlusspunkte** mit anderen Bauteilen (z. B. „Sparren-
  fuß" als Punkt auf der Bauteilachse mit Abstand 0 vom Anfangs-
  punkt).

**Anwendungsbeispiele für die Vorzeichenkonvention**:

- **Sparren**: typischerweise hat p_a an der Traufe (unten am
  Dach) und p_e am Sparrenfirstpunkt (oben am Dach); d̂ zeigt
  **entgegen** der Falllinie der getragenen Dachfläche, also
  bergauf von der Traufe zum Sparrenfirstpunkt
  (⟨d̂, ê_fall⟩ < 0; siehe `falllinie`). Das ist konsistent mit
  der Konvention im Werkplan, dass Sparrenlängen „vom Sparrenfuß
  bis zum Firstanschnitt" gemessen werden.
- **Pfette** (Fußpfette, Mittelpfette, Firstpfette): typischerweise
  horizontal entlang der Traufe oder des Firsts; p_a und p_e an den
  Enden gemäß lokaler Bezeichnungskonvention (z. B. nach
  steigender Achsbezeichnung A → B → C).
- **Stütze**: typischerweise lotrecht mit p_a unten (am Schwellen-
  oder Fundamentanschluss) und p_e oben (am Pfetten- oder
  Rähmanschluss); d̂ ist die Welt-z-Achse.

**Bauteilachse vs. Faserrichtung** (zur Auflösung der
Querbeziehung in `hg_faserrichtung.md`): Im Idealfall — geradfaseriges,
prismatisches Vollholzbauteil ohne Drehwuchs, Verzug oder
Faserabweichung — sind Bauteilachse und Faserrichtung kollinear:
d̂ ∈ {f̂, −f̂}. Die Faserneigung ist dann 0. In allen abweichenden
Fällen (schräg gesägtes Holz, verzogene Hölzer, Drehwuchs, Bauteile
aus mehreren keilgezinkten Stäben mit unterschiedlichen Faserrichtungen)
sind die beiden Achsen verschieden:

- die **Bauteilachse** bleibt die geometrische Hauptachse (Linie
  der Querschnittsschwerpunkte) und ist invariant unter Faserwirrnis,
- die **Faserrichtung** folgt dem tatsächlichen Materialaufbau und
  weicht von der Bauteilachse ab.

Die Faserneigung nach DIN 4074-1 quantifiziert diese Abweichung als
Tangens des eingeschlossenen Winkels und wird zur Festigkeits-
sortierung verwendet.

## Beziehungen

- **Oberbegriff**: `achse` mit Rolle ρ = Bauteilhauptachse. Die
  Bauteilachse ist eine Achse im Sinne von `hg_achse.md`, deren Rolle
  durch den Bezug zu einem konkreten Bauteilkörper konkretisiert
  wird.
- **Spezialisierungen (eigene Einträge folgen)**:
  - **Sparrenachse** (`sparrenachse`, in Folgearbeit): Bauteilachse
    eines Sparrens mit konkretisierter Vorzeichenkonvention
    (Traufe → First).
  - **Pfettenachse** (`pfettenachse`, in Folgearbeit): Bauteilachse
    einer Pfette.
  - **Stützenachse** (`stuetzenachse`, in Folgearbeit): Bauteilachse
    einer Stütze (lotrecht, Vorzeichenkonvention von unten nach
    oben).
- **Bestandteile (partitiv) — gerader Fall**:
  - Anfangspunkt p_a (Schwerpunkt des Anfangsquerschnitts);
  - Endpunkt p_e (Schwerpunkt des Endquerschnitts);
  - Trägergerade g (unbegrenzte Verlängerung der Achsstrecke);
  - Richtungs-Einheitsvektor d̂.
- **Bestandteile (partitiv) — gekrümmter Fall**:
  - geordnete Folge von Stützpunkten z(s_i) als
    Streckenzug-Repräsentation;
  - Anfangs- und Endpunkt;
  - lokale Tangentenrichtung an jeder Stelle.
- **Abgrenzung**:
  - **`achse`**: allgemeiner Oberbegriff (Gerade in einer Rolle);
    `bauteilachse` ist die Spezialisierung mit Rolle
    „Bauteilhauptachse" und Bezug auf einen konkreten Bauteilkörper.
  - **`gerade`**: die Trägergerade einer geraden Bauteilachse ist
    eine Gerade; die Bauteilachse selbst ist die endliche Strecke
    auf dieser Geraden, qualifiziert durch die Bauteilrolle.
  - **`strecke`**: die Bauteilachse eines geraden Bauteils ist als
    Punktmenge eine Strecke; sie ist aber zusätzlich annotiert als
    Achse mit Bauteilrolle. Die Strecke selbst ist achs-frei.
  - **`faserrichtung`**: materialbezogene Hauptachse
    (Einheitsvektor in S², ortsfrei). Die Bauteilachse ist
    geometrisch (Strecke in ℝ³, ortsgebunden). Die beiden können
    übereinstimmen (geradfaseriges prismatisches Bauteil), müssen
    aber nicht (Drehwuchs, Verzug, schräggesägt, keilgezinkt). Der
    Winkel zwischen ihnen ist die **Faserneigung** nach DIN 4074-1.
  - **Schwerlinie eines Querschnitts**: die Schwerlinie eines
    einzelnen Querschnitts K(s) ist ein Punkt z(s) ∈ K(s) (der
    Flächenschwerpunkt); die Bauteilachse ist der **geometrische
    Ort** dieser Punkte über die Bauteillänge.
  - **Neutrale Faser** (Statik): die neutrale Faser ist die Linie
    durch das Bauteil, an der die Biegespannung null ist. Bei
    homogenen prismatischen Bauteilen mit symmetrischem Querschnitt
    fällt die neutrale Faser mit der Bauteilachse zusammen, im
    allgemeinen Fall nicht. Die Bauteilachse ist geometrisch, die
    neutrale Faser mechanisch.

## Implementierungshinweis

Datentyp (Domänen-Schicht, Kotlin, Schicht
`zimmermann.domain.geometrie`, D4-Stand):

```kotlin
package zimmermann.domain.geometrie

/**
 * Bauteilachse als geometrische Hauptachse eines Stabbauteils,
 * realisiert als Wrapper über einer Strecke.
 * Glossar: hg_bauteilachse.md
 */
@ConsistentCopyVisibility
public data class Bauteilachse internal constructor(
    public val strecke: Strecke,
) {
    public companion object {
        public fun aus(strecke: Strecke): Resultat<Bauteilachse, EntartetGeometrie>
        public fun ausPunkten(anfang: Punkt, ende: Punkt): Resultat<Bauteilachse, EntartetGeometrie>
    }
}
```

- **Strukturelle Beziehung zu `Achse` (semantisch, nicht
  strukturell)**: Die im Glossar ausgewiesene Hierarchie
  `bauteilachse oberbegriff achse` wird im Code **nicht** als
  Kotlin-Vererbung umgesetzt. `Achse` (Wrapper über `Gerade`,
  unbegrenzt, ungerichtet) und `Bauteilachse` (Wrapper über
  `Strecke`, begrenzt, gerichtet) sind strukturell verschiedene
  Datentypen mit verschiedenen Trägergeometrien. Eine Vererbung
  wäre semantisch falsch (eine Bauteilachse ist als Punktmenge
  endlich, eine Achse beidseitig unbegrenzt). Die Hierarchie ist
  daher als Querverweis im KDoc dokumentiert, nicht als
  Sealed-Interface umgesetzt.
- **Einheit**: Punktkoordinaten in mm; Länge in mm; Richtungsvektor
  dimensionslos (Einheitsvektor).
- **Vorzeichenkonvention (normativ, verschoben auf die
  Bauteilrolle)**: Auf der Ebene des generischen Typs `Bauteilachse`
  ist die Reihenfolge `anfang → ende` festgelegt (geerbt aus
  `Strecke`), aber **welcher** geometrische Endpunkt als Anfang
  gilt, ist durch die konkrete Bauteilrolle zu konkretisieren
  (siehe Spezialisierungs-Einträge `sparrenachse`, `pfettenachse`,
  `stuetzenachse`). Bei Konstruktion einer Bauteilachse ohne
  konkrete Rolle ist die Reihenfolge willkürlich und der
  Konsumenten-Code darf sich nicht darauf verlassen. Die
  Vorzeichenkonvention ist Teil der Identität: `umkehren()`
  produziert eine semantisch andere Bauteilachse (anders als bei
  `Strecke.istGleichUngerichtet`, das die Orientierung ignoriert).
- **Invarianten** (geerbt aus `Strecke`):
  - ‖ende − anfang‖² > `Toleranzen.NORM_EPS`.
  - Beide Endpunkte finit.
- **Konstruktoren** (Companion-Factories, geprüft):
  - `Bauteilachse.aus(strecke: Strecke): Resultat<Bauteilachse, EntartetGeometrie>`
    — trivialer Erfolg (Strecke-Invariante reicht; das
    Resultat-Wrapping wahrt API-Konsistenz mit den anderen
    Geometrie-Factories).
  - `Bauteilachse.ausPunkten(anfang: Punkt, ende: Punkt): Resultat<Bauteilachse, EntartetGeometrie>`
    — delegiert an `Strecke.ausPunkten` und propagiert deren
    Entartungs-Resultate (`NichtFinit`, `NullStrecke`).
- **Identität / Gleichheit**: `equals` ist strukturell-exakt
  (data-class-Standard). Für gerichtete geometrische Identität
  steht `istGleicheBauteilachse(other, eps)` zur Verfügung; sie
  ignoriert **nicht** die Reihenfolge — Bauteilachse ist
  gerichtet.
- **Bezug zur Faserrichtung**: Die Klasse `Bauteilachse` enthält
  **keine** Faserrichtung als Feld. Die Faserrichtung ist
  Annotation des `Bauteil`s, nicht der Achse (siehe `hg_bauteil.md`
  und `hg_faserrichtung.md`). Eine Hilfsfunktion
  `faserneigung(achse: Bauteilachse, faser: Faserrichtung): Double`
  liegt in der Bemessungs-Schicht und nicht im Geometrie-Modul.
- **Verwendungsregel**: Funktionen, die eine Bauteilachse
  benötigen, nehmen `Bauteilachse` als Parametertyp und nicht den
  nackten `Strecke`. Damit ist am API-Rand sichtbar, dass die
  Strecke eine Bauteilrolle trägt; eine willkürliche Strecke kann
  nicht versehentlich als Bauteilachse verwendet werden.

**Folgearbeit (trigger-basiert):**

- **Bauteil-Referenz auf der Bauteilachse** (z. B. `bauteilId: UUID`)
  — wenn die Bauteilachse aus dem Bauteil heraus referenziert
  werden muss (etwa für Konsistenz-Prüfung „Achse durch
  Querschnittsschwerpunkte"). Bis dahin lebt die Bauteilachse als
  reines Geometrie-Objekt.
- **Gekrümmte Bauteilachse als `Streckenzug`-Variante**
  (z. B. `sealed interface Bauteilachse` mit `Gerade(strecke: Strecke)`
  und `Gekruemmt(zug: Streckenzug)`) — wenn ein Anwendungsfall
  einen gebogenen BSH-Bogen modellieren muss. Bis dahin ist nur
  der gerade Fall (häufigster Fall im Holzbau) implementiert.
- **Konkretisierung der Vorzeichenkonvention** in den
  rollenspezifischen Klassen `Sparrenachse`, `Pfettenachse`,
  `Stuetzenachse` — wenn die konkreten Bauteil-Begriffe
  (Sparren, Pfette, Stütze) implementiert werden (D8).

## Quellen

**Primär (normativ):**

- SIA 265:2021, „Holzbau", Schweizerischer Ingenieur- und
  Architektenverein, Zürich.
- DIN EN 1995-1-1:2010-12, „Eurocode 5: Bemessung und Konstruktion
  von Holzbauten – Teil 1-1: Allgemeines – Allgemeine Regeln und
  Regeln für den Hochbau".
- DIN 1052:2008-12, „Entwurf, Berechnung und Bemessung von
  Holzbauwerken".
- DIN 4074-1:2012-06, „Sortierung von Holz nach der Tragfähigkeit –
  Teil 1: Nadelschnittholz".

**Sekundär:**

- Lignum (Hrsg.): *Holzbautabellen HBT.* Lignum, Zürich, aktuelle
  Auflage.
- Mönck, W.; Rug, W.: *Holzbau – Bemessung und Konstruktion.*
  16. Auflage, Beuth, Berlin 2015.
- Blass, H. J.; Sandhaas, C.: *Ingenieurholzbau – Grundlagen der
  Bemessung.* KIT Scientific Publishing, Karlsruhe 2016.
- Natterer, J.; Herzog, T.; Volz, M.: *Holzbau-Atlas.* 4. Auflage,
  Birkhäuser, Basel 2003.

**Korpus (nicht autoritativ):**

- Holzbau Deutschland, Merkblatt „Begriffe und Klassifizierungen
  für den Holzbau" (abgerufen 2026-05-08).
- Wikipedia, Lemma „Stabachse" (abgerufen 2026-05-08).
