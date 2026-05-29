# Hauptglossar-Konventionen

Meta-Datei. Kein Glossarbegriff (kein YAML-Frontmatter, kein
`GlossarTerm`-Eintrag). Diese Datei sammelt Sprach- und Stilregeln,
die für alle **Hauptglossar**-Einträge gelten.

**Datei-Ablage:** Seit 2026-05-14 liegen die Einträge in vier
Cluster-Unterordnern: `hauptglossar/<cluster>/hg_<id>.md`. Die
verbindliche Cluster-Liste, Mapping-Regeln und das NPK-Anker-Mapping
stehen in §9.

**Pendant-Datei:** `lerninhalt/subglossar/SG_KONVENTIONEN.md` —
Konvention für das **Subglossar** (`lerninhalt/subglossar/sg_<id>.md`).
Die beiden Dateien sind eng aufeinander bezogen; eine Übersichtstabelle
der Korrespondenz steht am Anfang von `SG_KONVENTIONEN.md`. Bei
Konflikt: für **HG-Belange** gilt dieses Dokument, für **SG-Belange**
das SG-Dokument.

**Stand-Pflege:** Hauptglossar-Welle-Logs, Kohärenz-Reviews und
Konsolidierungs-Etappen werden in **`STAND_HAUPTGLOSSAR.md`**
(gleichem Verzeichnis) geführt. `STAND_AKTUELL.md` im Projekt-Root
behält nur einen kurzen Verweis-Block mit dem aktuellen HG-Stichwort.
Pendant für das Subglossar: `lerninhalt/subglossar/SUBGLOSSAR_STAND.md`.

## 1. Sprachregel: senkrecht / rechtwinklig / orthogonal

Im Glossar wird **„rechtwinklig"** oder **„im rechten Winkel zu"**
verwendet, wenn ein 90°-Winkel zwischen zwei geometrischen Objekten
gemeint ist (relationale Bedeutung).

**„Senkrecht"** wird ausschließlich im Sinne von **„lotrecht"**
verwendet (absolute, welt-bezogene Bedeutung mit Schwerkraft-Richtung,
also parallel zur globalen z-Achse). Diese Bedeutung ist im Holzbau
einschlägig — etwa bei Stützen, die per Definition senkrecht stehen
sollen, oder bei der Ausrichtung einer Wand.

**„Orthogonal"** ist Synonym zu „rechtwinklig" und kann verwendet
werden, wenn der mathematische Kontext es nahelegt (Skalarprodukt,
Vektorraum, lineare Algebra).

Begründung: „Senkrecht" hat im Deutschen zwei nicht zur Deckung zu
bringende Bedeutungen — relational (rechtwinklig zu …) und absolut
(lotrecht im Sinne der Schwerkraft). Im Glossar führt diese
Mehrdeutigkeit zu vermeidbarer Unklarheit, sobald zugleich vom
Welt-Koordinatensystem (z-Achse vertikal nach oben) und von
Bauteil-Lokalsystemen die Rede ist.

| Aussage | Bedeutung | Empfohlener Wortlaut |
|---|---|---|
| Faserrichtung im 90°-Winkel zur Last | relational | „rechtwinklig zur Faser" |
| Plattendicken-Achse im 90°-Winkel zur Plattenebene | relational | „rechtwinklig zur Plattenebene" |
| Wand steht in Schwerkraftrichtung | absolut | „die Wand steht senkrecht" |
| Stütze ist lotrecht ausgerichtet | absolut | „die Stütze steht senkrecht" |
| Schnittfläche parallel zur Lotachse (zimmermannssprachlich) | absolut | „**Senkel**" / „Senkelschnitt" (siehe `hg_senkel.md`) |
| Schnittfläche rechtwinklig zur Lotachse (zimmermannssprachlich) | absolut | „**Bleischnitt**" / „Blei" (siehe `hg_bleischnitt.md`) |
| Vektor `n̂` mit `n̂ · t̂ = 0` | mathematisch-relational | „n̂ steht orthogonal zu t̂" oder „rechtwinklig" |

Die beiden zimmermannssprachlichen Realisierungen der absoluten
Lot-Bezogenheit — **Senkel** (parallel zur Lotachse) und
**Bleischnitt** (rechtwinklig zur Lotachse) — sind als eigene
Glossarbegriffe geführt (`hg_senkel.md`, `hg_bleischnitt.md`). Sie
spannen die ausgezeichnete Lot-Lage-Klassifikation einer Ebene
auf und ersetzen in der Glossarsprache die mehrdeutigen
Wortlauten „vertikaler Schnitt" / „horizontaler Schnitt", die
weder die berufssprachliche Verankerung noch die explizite
Lot-Bezogenheit transportieren.

## 2. Methodik: Bestand-Audit beim Etablieren neuer Konventionen

Wenn eine neue Konvention in dieser Datei aufgenommen wird, ist ein
**Bestand-Audit** integraler Bestandteil des R-Schritts: alle
existierenden Glossareinträge werden auf Verstöße gegen die neue
Konvention geprüft und konsequent angeglichen. Dasselbe gilt für
KDoc-Texte und Code-Bezeichner in der Domänen-Schicht, sofern die
Konvention auch dort sprachlich greift.

Begründung: Eine Konvention, die nur prospektiv für künftige Einträge
gilt, erzeugt eine inkonsistente Glossar-Oberfläche und entwertet
sich selbst. Die Korrekturkosten sind im Moment der Festlegung am
geringsten, weil der Anlass präsent ist und die Entscheidung frisch
begründet ist; je länger die Korrektur aufgeschoben wird, desto mehr
Drift sammelt sich an.

Praktisch: nach dem Schreibvorgang an dieser Datei einen `grep` über
das Glossar ausführen, Treffer sichten, Korrekturen einarbeiten,
Grenzfälle (Zitate, lotrecht/welt-bezogene Bedeutungen, Code-
Identifier) ausdrücklich melden statt mechanisch ersetzen.

## 3. Klassifikation `begriffstyp:`

Jeder Glossareintrag trägt im Frontmatter genau einen `begriffstyp:`-
Wert aus der folgenden Tabelle (acht Werte: `primitiv`, `generisch`,
`aggregat`, `partitiv`, `relation`, `bauteilrolle`, `merkmal`,
`hilfsbegriff`). Die Klassifikation ordnet den Eintrag einer
strukturellen Rolle im Begriffssystem zu und ist orthogonal zum
`oberbegriff:` (der eine fachliche Spezialisierungs-Linie ausdrückt).

| Wert | Bedeutung | Strukturmerkmal | Beispiele |
|---|---|---|---|
| `primitiv` | Unzerlegbares Konzept ohne weitere innere Struktur. | Atomar (Tupel von Skalaren oder identisch mit einem Vorbegriff); keine eigenen Subtypen. | `punkt`, `vektor`, `gerade` |
| `generisch` | Eigenständiges Konzept mit interner Struktur und ggf. eigenen Spezialisierungen, aber ohne partitive Eigentümerschaft an einem Trägerbegriff. | `data class` oder `sealed` mit Subtypen; Invarianten an den eigenen Feldern. | `ebene`, `polygon`, `polyeder`, `werkstoff` |
| `aggregat` | Komposition aus mehreren eigenständigen Begriffen mit eigener Identität (UUID). Mitglieder sind selbst vollwertige Begriffe; das Aggregat bündelt sie und führt eigene Konsistenzbedingungen über der Komposition. | Tupel aus mehreren Begriffsmengen plus Inzidenzbedingungen; eigene UUID. | `bauteilgruppe`, `verbindung`, `tragwerk`, `dach` |
| `partitiv` | Strenger Bestandteil eines Trägerbegriffs ohne eigenständige Identität im Modell. Lebenszyklus an den Träger gekoppelt (kaskadische Löschung). Eigene UUID nur zur Referenzierbarkeit innerhalb des Trägers, nicht als globaler Lebenszyklus-Marker. | Enthalten in einer Liste/Menge am Träger; keine freistehende Existenz. | `bearbeitung`, `lage`, `lagenstruktur` |
| `relation` | Beziehung zwischen zwei oder mehr Trägerbegriffen, ohne eigene partitive Komposition oder geometrische Substanz. Trägt eigene Konsistenzbedingungen über der Beziehung, aber keine eigene innere Struktur jenseits der Beziehungs-Inzidenzen. Vorgesehen für funktionale Sichten und Mitgliedschafts-Klassifikationen. | Mengen-Beziehung über Mitgliedern; nicht-exklusive Mitgliedschaft. | `bausystem` (und seine Spezialisierungen, soweit sie nicht selbst zum Aggregat werden) |
| `bauteilrolle` | Spezialisierter Bauteil-Subtyp, der eine konstruktive Rolle im Tragwerk definiert. Strukturell `sealed class`-Subtyp unter einem Bauteil-Rollen-Knoten; trägt rollenspezifische geometrische Constraints (Lage-, Richtungs-, Auflagerungs-Bedingungen) und Default-Werte für Querschnitt und Faserrichtung. | sealed-Subtyp unter `Bauteil`-Rolle; rollenspezifische Constraints. | `sparren`, `pfette`, `firstpfette`, `mittelpfette`, `fusspfette` |
| `merkmal` | Eigenschaft, Annotation oder klassifikatorischer Wert an einem Trägerbegriff. Trägt selbst weder Identität noch eigene Subtyp-Hierarchie; ist ein **Wert**, kein **Objekt**. | Enum-artig oder einfache annotierende Datenklasse mit ≤ wenigen Skalaren. | `faserrichtung` (als Wert/Annotation), `dachneigung` (als Wert), Lage-Klassifikationen einer Ebene |
| `hilfsbegriff` | Meta-Eintrag, der eine **infrastrukturelle Festlegung** der Domänen-Schicht beschreibt (Identifikator-Schema, Bezugssystem, globale Konstanten-Sammlung) und keine fachliche Holzbau-Substanz im Sinne der anderen Werte trägt. Kein eigener Träger im Modell; wird von vielen anderen Begriffen vorausgesetzt, aber selbst nicht als Datenklasse instanziiert oder nur als Singleton/Konstantenobjekt geführt. | Singleton, globale Konstanten-Sammlung, Identifikator-Format, Welt- oder Lokal-Bezugssystem. | `toleranzen`, `uuid`, `weltkoordinatensystem`, `lokales_koordinatensystem` |

### Erläuterungen zu den einzelnen Werten

**`primitiv`** wird gewählt, wenn der Begriff im Sinne von ISO 704
ein **Vorbegriff** des Systems ist: er hat keinen weiter zerlegbaren
inneren Aufbau und keine eigenen Subtypen, sondern wird durch
Skalare oder ein Tupel von Skalaren vollständig repräsentiert.
Beispiele: `punkt` (Tripel reeller Koordinaten), `vektor`,
`gerade` als Stützpunkt-plus-Richtung. Sobald ein Begriff eine
sealed-Hierarchie hat oder Invarianten an mehreren Feldern trägt,
ist er `generisch`, nicht `primitiv`.

**`generisch`** ist die Grundkategorie für eigenständige Konzepte
mit interner Struktur. Der entscheidende Unterschied zu `primitiv`
ist die Möglichkeit eigener Subtypen oder nicht-trivialer
Konstruktor-Invarianten; der entscheidende Unterschied zu
`aggregat` ist das Fehlen einer Komposition aus mehreren
eigenständigen Trägerbegriffen mit eigener Identität.

**`aggregat`** ist eine Komposition mehrerer eigenständiger
Begriffe und führt eigene Konsistenzbedingungen über der
Komposition (Inzidenz, Zusammenhang, Vollständigkeit). Ein
Aggregat hat eine eigene UUID, weil es als Ganzes adressierbar
sein muss (z. B. für Persistenz, Bemessungs-Nachweis,
Lifecycle-Operationen). Beispiele: `verbindung` (Bauteile +
Verbindungsmittel + Verbinder an einem Knoten), `tragwerk`
(Bauteile + Verbindungen + Auflager + Lastfälle), `dach` (Tragwerk
+ Dachflächen + Dachaufbau).

**`partitiv`** ist die Kategorie für Bestandteile mit Lebenszyklus-
Kopplung an einen Trägerbegriff. Der `partitiv`-Eintrag hat zwar
eine eigene UUID für Referenzierbarkeit (etwa aus
Verbindungsmittel-Folgegeometrie, Bemessungs-Nachweisen oder
externen Austauschformaten wie BTLx/IFC), aber er existiert nicht
ohne seinen Träger und wird bei dessen Löschung mitentfernt.
`bearbeitung` ist der paradigmatische Fall: jede Bearbeitung
gehört genau einem Bauteil; eine freistehende Bearbeitung hat
keinen Modellzustand.

**`relation`** ist die Kategorie für funktionale Sichten und
Mitgliedschafts-Klassifikationen ohne partitive Eigentümerschaft.
Im aktuellen Glossar trägt sie `bausystem`: ein Bausystem
gruppiert Bauteile funktional (lastabtragend, aussteifend,
hüllbildend), die Mitgliedschaft ist nicht-exklusiv, und das
Entfernen des Bausystems löscht die Mitglieder nicht. Wird eine
funktionale Sicht zusätzlich um partitive Bestandteile (Auflager,
Lastfälle) und Konsistenzbedingungen über der Komposition
erweitert, kippt sie typweise zu `aggregat` — siehe `tragwerk`,
das den Bausystem-Charakter als `oberbegriff: bausystem` erbt,
strukturell aber als Aggregat mit Auflager- und
Verbindungs-Inzidenzen geführt wird (`begriffstyp: aggregat`).
Diese Asymmetrie zwischen `oberbegriff` (fachliche Spezialisierung)
und `begriffstyp` (strukturelle Rolle) ist zulässig und beabsichtigt.

**`bauteilrolle`** beschreibt einen konstruktiv definierten
Bauteil-Subtyp mit eigenen geometrischen Constraints (Sparren
liegt entlang der Falllinie einer Dachfläche, Pfette ist
horizontal entlang einer Höhenlinie). Strukturell ist die
Bauteilrolle ein sealed-Subtyp unter einem Bauteilrollen-Knoten,
nicht eine Annotation am abstrakten Bauteil.

**`merkmal`** bleibt für **Werte und Annotationen** reserviert,
die selbst weder Identität noch eigene Subtyp-Hierarchie tragen:
ein Faserrichtungs-Wert (Einheitsvektor mit semantischer Lesart),
ein Dachneigungs-Wert (Winkel mit Wertebereichs-Constraint), eine
Lage-Klassifikation einer Ebene. Der Unterschied zu
`bauteilrolle`: eine Rolle ist ein **Objekt** im Modell mit
eigenen Constraints, ein Merkmal ist ein **Wert** am Träger-
Objekt.

### Differenzierungs-Hilfen

- **`primitiv` vs. `generisch`**: ein `primitiv`-Eintrag erlaubt
  keine eigenen Subtypen und trägt keine Invarianten jenseits der
  Tupel-Wohlgeformtheit; sobald ein Eintrag sealed-Hierarchie hat
  oder konstruktive Felder mit Invarianten, ist er `generisch`.
- **`aggregat` vs. `partitiv`**: das Aggregat hat eigene Identität
  und existiert unabhängig vom „Eigentümer" (es hat keinen); der
  partitive Eintrag ist gerade nicht eigentümerlos, sondern
  Lebenszyklus-gekoppelt.
- **`aggregat` vs. `relation`**: beide bündeln mehrere Begriffe,
  aber das Aggregat hat eigene partitive Bestandteile und
  Konsistenz über deren Komposition; die Relation ist eine reine
  Mitgliedschafts-Beziehung mit nicht-exklusiver, lifecycle-
  unabhängiger Mitgliedschaft.
- **`bauteilrolle` vs. `merkmal`**: die Rolle ist ein eigener
  Bauteil-Subtyp im Code; das Merkmal ist ein annotierter Wert.
  Wenn der Eintrag eine sealed-class-Hierarchie unter Bauteil
  begründet, ist er Rolle; wenn er einen Wertebereich oder eine
  Annotation an einem Bauteil beschreibt, ist er Merkmal.
- **`bauteilrolle`-Verschachtelung** (transitive Spezialisierung):
  zulässig. Eine Bauteilrolle darf eine andere Bauteilrolle als
  `oberbegriff:` haben, sofern die innere Spezialisierung eine
  echte Sub-Sealed-Hierarchie der äusseren ist. Beispiel:
  `sparren` ist `bauteilrolle` mit `oberbegriff: bauteil`;
  `gratsparren` ist `bauteilrolle` mit `oberbegriff: sparren`.
  Im Code: `sealed class Sparren : Bauteil()` und
  `class Gratsparren : Sparren()`. Die Pendant-Pflicht aus dieser
  Sektion gilt für jede Rolle in der Kette einzeln.
- **`hilfsbegriff` vs. `merkmal`**: ein Merkmal ist ein **Wert
  an einem fachlichen Trägerbegriff** (Faserrichtung an einem
  Bauteil, Dachneigung an einer Dachfläche). Ein Hilfsbegriff
  ist eine **infrastrukturelle Festlegung der Domänen-Schicht
  selbst** ohne fachlichen Trägerbegriff; er wird breit
  vorausgesetzt, ist aber keine Eigenschaft eines konkreten
  Holzbau-Konzepts, sondern Voraussetzung für die geometrische
  Modellierung als solche.
- **`merkmal` als Spezialisierung eines `generisch`-Oberbegriffs**:
  zulässig, wenn der spezialisierte Eintrag eine **abgeleitete
  Sicht** auf den Oberbegriff trägt, ohne eigene Identität und
  ohne eigene Subtyp-Hierarchie zu begründen. Beispiel:
  `bauteilkoerper` ist eine Sicht eines `bauteil` durch die
  Polyeder-Brille; der Oberbegriff `polyeder` ist `generisch`, die
  Sicht selbst trägt keine `GlobalId` und keine sealed-Hierarchie,
  also bleibt sie `merkmal`. Die Asymmetrie ist im jeweiligen
  Eintrag zu begründen (Erläuterungs-Block).

### Konflikt-Regel

Die Tabelle dieser Sektion ist die verbindliche Referenz für
`begriffstyp:`. Bei Konflikt zwischen einem Eintrag und der
Tabelle wird der Eintrag korrigiert, nicht die Tabelle.

### Pflicht zur Code-Pendant-Verankerung

Der Build prüft mechanisch, dass jeder Eintrag mit einem der
folgenden `begriffstyp:`-Werte ein Code-Pendant in der Domänen-
Schicht hat — Klasse mit Annotation `@GlossarBegriff(GlossarTerm.X)`:

| `begriffstyp:` | Pendant-pflichtig | Begründung |
|---|---|---|
| `primitiv` | ja | unzerlegbares Konzept; im Code als data class / value class realisiert |
| `generisch` | ja | eigenständiges Konzept mit interner Struktur; im Code als data class / sealed class |
| `aggregat` | ja | Komposition mit eigener UUID; im Code als data class |
| `partitiv` | ja | Bestandteil mit Lebenszyklus-Kopplung; im Code als sealed-Subtyp einer Träger-Hierarchie |
| `bauteilrolle` | ja | spezialisierter Bauteil-Subtyp; im Code als sealed-Subtyp unter Bauteilrolle |
| `merkmal` | nein | Werte und Annotationen sind oft Primitive ohne eigene Klasse (Beispiel: `dachneigung` als `Double` in rad; `senkel`/`bleischnitt` als Prädikate auf `Ebene`). Wenn ein Pendant existiert, soll es `@GlossarBegriff` tragen; es ist aber nicht erzwungen. |
| `relation` | nein | reine Mitgliedschafts-Sicht ohne eigene Substanz |
| `hilfsbegriff` | nein | infrastrukturelle Festlegung ohne fachlichen Träger; existierende Pendants tragen `@GlossarBegriff` freiwillig |

**Ausnahme — Code-Pattern-Klassen ohne Glossar-Pendant:** Klassen,
die im Modell keine Begriffsentsprechung haben (sealed-Resultat-
Fehlertypen wie `BauteilUngueltig`, technische Hilfsklassen),
tragen die Annotation `@CodePattern` und sind damit vom
Coverage-Linter ausgenommen. Klassen im Package `domain.fehler.*`
(falls eingeführt) gelten implizit als Code-Pattern, ohne
Annotation.

## 4. Toleranz-Konstanten und ihre Anwendung

Die fünf in `hg_toleranzen.md` definierten Toleranz-Konstanten haben
unterschiedliche Anwendungsbereiche. Die folgende Tabelle ist die
zentrale Anwendungs-Regel; bei Konflikt zwischen Tabelle und
Einzeleintrag wird der Eintrag korrigiert.

| Konstante | Einheit | Anwendung | Beispiele |
|---|---|---|---|
| `LAENGE_EPS` | mm | Längen-, Abstands- und Koordinatenvergleich; Punkt-Identität; Ebenen-Enthaltensein eines Punktes; Strecken-Entartung; doppelter Polygon-Eckpunkt. | `Punkt.gleich`, `Punkt.istInEbene`, `Strecke.istEntartet`, Sparrenlängen-Vergleich, Bauteil-Endpunkt-Identität |
| `WINKEL_EPS` | rad | Winkel-Vergleich, wenn der Winkel **explizit** berechnet ist (`acos`, `atan2`); Klassifikation Flach- vs. Geneigtdach am Rand; Dachneigungs-Wertebereich; Hankinson-Winkel; Faser-zu-Last-Winkel. | `hankinson_winkel`, `dachflaeche.init` (Toleranz auf `n_a · e_z ≥ −WINKEL_EPS`), Dachneigungs-Klassifikation |
| `KOLLINEAR_EPS` | dimensionslos | Kollinearitäts- und Parallelitäts-Tests zwischen Vektoren über das normierte Kreuzprodukt `‖û × v̂‖ = |sin∠(û, v̂)|`; alle Lot- und Lage-Prädikate, die als Parallelitäts-Test gegen eine ausgezeichnete Welt-Richtung (z. B. `e_z`) formuliert sind. | `senkel.istSenkel`, `bleischnitt.istBleischnitt`, `pfette.istHorizontal`, Falllinien-Kollinearität des Sparrens, drei Punkte kollinear |
| `NORM_EPS` | mm² bzw. dimensionslos | Nullvektor-Test über `‖v‖² ≤ NORM_EPS`; Einheitsvektor-Test über `|‖v‖² − 1| ≤ NORM_EPS`. Niemals für Längen- oder Winkelvergleiche verwenden. | Eingangsprüfung von Normalenvektoren in `Ebene` und `Dachflaeche`; `Vektor.istNull`, `Vektor.istEinheit` |
| `FLAECHE_EPS` | mm² | Polygon-Flächeninhalt-Test gegen null; Dachflächen-Mindestfläche. | `Polygon.istEntartet`, `Dachflaeche.init` (Flächeninhalt > FLAECHE_EPS) |

### Erläuterung zur Trennung `WINKEL_EPS` vs. `KOLLINEAR_EPS`

Beide Konstanten haben in `hg_toleranzen.md` denselben empfohlenen
Default (`1·10⁻⁹`), unterscheiden sich aber in der **Form des
Tests**, nicht im **Schwellenwert**:

- `WINKEL_EPS` wird angewandt, wenn der Winkel zwischen zwei
  Objekten **explizit als Skalar** berechnet wurde (typischer
  Aufruf: `acos(û · v̂)` oder `atan2(…)`). Der Test ist
  `|α − α_soll| ≤ WINKEL_EPS`.
- `KOLLINEAR_EPS` wird angewandt, wenn der Test **direkt über
  das normierte Kreuzprodukt** geführt wird, ohne Winkel-
  Extraktion. Der Test ist `‖û × v̂‖ ≤ KOLLINEAR_EPS`, was
  numerisch dem Sinus des eingeschlossenen Winkels entspricht.
  Diese Form ist **bevorzugt für Parallelitäts- und Lot-
  Prädikate**, weil der Sinus in der Nähe von 0 gut konditioniert
  ist (im Gegensatz zum Cosinus, der in der Nähe von ±1
  Auslöschung erleidet).

Daraus folgt die Anwendungs-Regel: **alle Lot- und Lage-Prädikate
(Senkel-Test, Bleischnitt-Test, Pfetten-Horizontalitäts-Test,
Falllinien-Kollinearität) verwenden `KOLLINEAR_EPS`**, weil sie
geometrisch Parallelitäts-Tests zwischen einem Bauteil-Vektor
und einer ausgezeichneten Welt-Richtung sind. **Allgemeine Winkel-
Vergleiche, bei denen der Winkel selbst als Größe gefragt ist
(Hankinson-Winkel zwischen Faser und Last, Dachneigung als
gemessener Winkel), verwenden `WINKEL_EPS`**.

Die Zuordnung folgt der **Form des Tests**: Sinus-Test
(bevorzugt für Lot- und Parallelitäts-Prädikate) →
`KOLLINEAR_EPS`; expliziter Winkel-Skalar → `WINKEL_EPS`.

## 5. Spezialisierungs-Synonyme bei abgelehnter Oberbegriffs-Benennung

Ein Synonym darf bei einem **Spezial-Eintrag** geführt werden, auch
wenn der zugehörige Oberbegriff dasselbe Wort in
`abgelehnte_benennungen:` führt, sofern beide Bedingungen erfüllt
sind:

1. Das Synonym ist im **Spezial-Kontext** im DACH-Holzbau-Korpus
   eine etablierte Berufssprache; sein Bezug auf gerade diesen
   spezialisierten Begriff ist berufssprachlich eindeutig.
2. Der Spezial-Eintrag thematisiert die Synonymie und ihre
   Abgrenzung zum Oberbegriff im Erläuterungsblock oder im
   `quellenkonflikt:`-Block ausdrücklich.

Die `abgelehnte_benennungen:`-Liste des Oberbegriffs bindet
ausschließlich die **Wurzel-Lesart** des Oberbegriffs, nicht
seine Spezialisierungen.

### Beispiel

„Mauerlatte" ist im DACH-Korpus berufssprachlich an die
**Fußpfette** (auf der Mauerkrone aufliegend) gebunden; für
**Pfetten allgemein** ist die Bezeichnung irreführend, weil
First- und Mittelpfetten gerade nicht auf einer Mauer liegen.
Daraus folgt die zulässige Konstellation:

- `pfette.abgelehnte_benennungen: [Mauerlatte, …]` — die Wurzel-
  Lesart „Pfette" lehnt die Mauer-spezifische Benennung ab.
- `fusspfette.synonyme: [Mauerlatte, …]` — die Spezialisierung
  übernimmt die berufssprachliche Benennung, weil sie genau diese
  Spezialisierung trifft.

Beide Einträge sind nach dieser Konvention kompatibel. Der
Fußpfetten-Eintrag thematisiert die Synonymie im
Erläuterungsblock und verweist auf den Oberbegriff zur
Klarstellung, dass „Mauerlatte" nicht für andere Pfetten-Subtypen
verwendet werden darf.

Die Regel schränkt die `abgelehnte_benennungen:`-Bindung auf
die jeweilige Lesart ein und wirkt nicht auf die gesamte
Spezialisierungs-Hierarchie.

### 5a. `abgelehnte_benennungen:` bei gegenseitig ausschliessenden Bauteilrollen

`abgelehnte_benennungen:` ist nicht nur für orthografische
Varianten oder echte Synonyme reserviert, sondern auch zulässig
für **Begriffe, die in der Praxis irrtümlich synonym verwendet
werden, obwohl sie strukturell andere Bauteilrollen bezeichnen**.
Das Feld wirkt dann als „Drift-Warnschild": die App-Suche nach
einer abgelehnten Benennung leitet auf den korrekten Eintrag, der
Quellenkonflikt-/Erläuterungs-Block dokumentiert die strukturelle
Trennung.

**Beispiel:** `hg_kopfband.md` und `hg_knagge.md` führen sich
gegenseitig in `abgelehnte_benennungen:`. Beide Bauteile sind
strukturell unterschiedlich (Kopfband = Stab im Wandgefach;
Knagge = Volumen-Konsole aus dem Gefüge heraus), werden aber im
Praxis-Korpus gelegentlich irrtümlich vertauscht (vgl. „Kopfwinkel-
holz" als uneindeutiger Drift-Begriff in beiden Einträgen). Die
Doppel-Listung in `abgelehnte_benennungen:` UND `abgrenzung_zu:`
ist konventionskonform:

- `abgrenzung_zu:` führt den Begriff als **eigenständige
  Geschwister-Rolle** (Querverweis zur App-Navigation, Theorie-
  Anker).
- `abgelehnte_benennungen:` führt ihn als **abgelehnte
  Bezeichnung im engeren Wurzel-Eintragskontext** (Drift-
  Warnschild für die App-Suche, mit Begründung im Quellenkonflikt-
  Block).

Diese Konstellation ist **nicht** auf orthografische Varianten
reduzierbar — sie reflektiert die Praxis-Drift, in der zwei
unterschiedliche Bauteilrollen mit ähnlichem Anwendungsbereich
und überlappendem Korpus-Vokabular verwechselt werden. Die
Trennlinie im Quellenkonflikt-Block muss strukturell genau sein
(z. B. Geometrie-Klasse, Anker-Topologie, Lage im Wandgefüge).

**Methodisch:** wenn eine neue Bauteilrolle einen bestehenden
Eintrag in `abgrenzung_zu:` aufnimmt UND in der Praxis Drift
besteht, ist die symmetrische Aufnahme in
`abgelehnte_benennungen:` zulässig und erwünscht. Wenn keine
Praxis-Drift besteht (Trennung ist berufssprachlich eindeutig),
reicht `abgrenzung_zu:` allein.

## 6. Forward-Verweise in `abgrenzung_zu:`

Die Frontmatter-Felder eines Glossareintrags unterscheiden sich
in ihrer Verbindlichkeit gegenüber dem Glossar-Bestand:

| Feld | Verbindlichkeit |
|---|---|
| `voraussetzungen:` | **nur** existierende Glossareinträge. Diese Einschränkung sichert Zirkel-Freiheit und Build-Konsistenz. Eine Voraussetzung auf einen noch nicht angelegten Begriff ist unzulässig. |
| `abgrenzung_zu:` | existierende **oder** noch nicht angelegte Begriffe. Forward-Verweise sind zulässig, sofern die Erläuterung den Abgrenzungs-Grund nennt und der Begriff im DACH-Holzbau-Korpus etabliert ist. |
| `synonyme:` | freie Strings; keine Glossareintrag-Pflicht. |
| `abgelehnte_benennungen:` | freie Strings; keine Glossareintrag-Pflicht. |
| `oberbegriff:` | existierender Glossareintrag oder `null`. |

Begründung: das Glossar wird inkrementell aufgebaut; viele
Abgrenzungs-Beziehungen sind aber **kontextklärend** und sollen
schon dann benannt werden, wenn der abzugrenzende Begriff noch
keinen eigenen Eintrag hat. `voraussetzungen:` darf das nicht, weil
es die zirkelfreie Aufbaureihenfolge des Glossars trägt;
`abgrenzung_zu:` darf das, weil eine Abgrenzung den abgrenzten
Begriff nicht definitorisch benötigt, sondern nur benennt.

### Hinweis zur Sichtung

Forward-Verweise in `abgrenzung_zu:` werden bewusst geduldet,
müssen aber periodisch gesichtet werden. Phantom-Begriffe — Begriffe,
die in `abgrenzung_zu:` auftauchen, ohne im DACH-Holzbau-Korpus
etabliert zu sein — sollen identifiziert und entweder als
Folgearbeit-Trigger formuliert oder ersatzlos gestrichen werden.

### Klassifikation der Forward-Verweise

Forward-Verweise in `abgrenzung_zu:` werden in drei Kategorien
geführt.

**(A) Legitime Forward-Verweise mit Folgearbeit-Trigger.** Der
Begriff ist im DACH-Holzbau-Korpus oder in einem unmittelbar
angrenzenden Fachgebiet (Geometrie, Vermessung) etabliert; eine
zukünftige Aufnahme als eigener Glossareintrag ist absehbar. Der
Forward-Verweis bleibt in `abgrenzung_zu:` stehen; in den
betroffenen Einträgen ist der Trigger entweder bereits in der
Erläuterung als Folgearbeit benannt oder wird im jeweils nächsten
Etappenschritt nachgezogen, sobald der Begriff fachlich gebraucht
wird.

| Begriff | Forward-Verweis in | Trigger (Folgearbeit) |
|---|---|---|
| `kante` | `hg_strecke.md` | Polyeder-Topologie / B-Rep-Modell (Ecken, Kanten, Flächen am `polyeder`). |
| `hoehenlinie` | `hg_falllinie.md`, `hg_bleischnitt.md` | Erstes Tool, das Höhenlinien einer Dachfläche bemasst (Vermassung, Werkplan). |
| `lv95` | `hg_weltkoordinatensystem.md` | Erste Georeferenzierung der App-Daten gegen den Schweizer Bezugsrahmen LV95. |
| `wgs84` | `hg_weltkoordinatensystem.md` | Erste Georeferenzierung der App-Daten gegen GNSS / WGS84. |
| `faserneigung` | `hg_hankinson_winkel.md`, `hg_faserrichtung.md`, `hg_bauteilachse.md` | Erste Festigkeits- oder Sortier-Modellierung nach DIN 4074-1 (Faserneigung als Sortiermerkmal). |
| `verschneidung` | `hg_schnittgerade.md` | Erstes Tool zur Dachflächen-Verschneidung (Walmdach, Verschneidungssparren). |
| `schnittpunkt` | `hg_schnittgerade.md` | Erste eigenständige Schnittpunkt-Funktion im Geometrie-Modul. |
| `kurve` | `hg_streckenzug.md` | Erste Modellierung gekrümmter Geometrie (Bogenträger, gekrümmte Falllinie). |
| `kehlsparren` | `hg_gratsparren.md`, `hg_kehle.md`, `hg_sparren.md` | Erste Walmdach-Modellierung mit Innenecke (Kehle); symmetrisches Gegenstück zum Gratsparren. |
| `schifter` | `hg_gratsparren.md`, `hg_sparren.md` | Erste vollständige Walmdach-Modellierung; verkürzte Sparren mit doppelter Schmiege an Grat-/Kehlsparren. |
| `gebaeude` | `hg_bauwerk.md` | Erste Hochbau-Modellierung mit Schutzfunktion (IFC `IfcBuilding`-Pendant). |
| `standort` | `hg_bauwerk.md` | Erste Georeferenzierung mit Site-Daten (IFC `IfcSite`-Pendant). |
| `dachkoerper` | `hg_polyeder.md` | Erste Modellierung eines Dach-Hüllvolumens als zusammengesetztes Polyeder (Walmdach-Volumen als CSG-Vereinigung dreieckiges Prisma plus zwei rechteckige Pyramiden, Berufsschul-Korpus). |
| `masstoleranz_din18202` | `hg_laengenmass.md`, `hg_lineares_groessenmass.md` | Erste Werkplan-Toleranz-Ausgabe nach DIN 18202 (Toleranzen im Hochbau) bzw. SIA 414 (Maßtoleranzen Bauwesen). |

**(B) Phantom ohne Substanz, ersatzlos gestrichen.** Der Begriff
hat im DACH-Holzbau-Korpus keine eigenständige Verankerung und ist
im verweisenden Eintrag entweder als `abgelehnte_benennungen:`
bereits geführt (redundant) oder als reine Anglizismus-/
Synonym-Variante eines bereits angelegten Begriffs.

| Begriff | Forward-Verweis in (vorher) | Begründung der Streichung |
|---|---|---|
| `polygonzug` | `hg_polygon.md` | Synonym zu `streckenzug`; Abgrenzung muss gegen `streckenzug` selbst formuliert sein, nicht gegen sein Synonym. In `hg_polygon.md` durch `streckenzug` ersetzt. |
| `polylinie` | `hg_polygon.md` | Wie `polygonzug` Synonym von `streckenzug`; in `hg_polygon.md` durch `streckenzug` ersetzt. |
| `pfad` | `hg_streckenzug.md` | In `hg_streckenzug.md` bereits als `abgelehnte_benennungen:` geführt; im DACH-Holzbau-Korpus nicht als eigenständiger Geometriebegriff etabliert (Anglizismus „path"). Aus `abgrenzung_zu:` gestrichen. |
| `hangrichtung` | `hg_falllinie.md` | In `hg_falllinie.md` bereits als `abgelehnte_benennungen:` geführt; im Geomatik-Sprachgebrauch verwendbar, aber im Holzbau-Korpus nicht eigenständig — die Falllinie deckt die Bedeutung ab. Aus `abgrenzung_zu:` gestrichen. |

**(C) Synonym, in `abgelehnte_benennungen:` zu verschieben.** Tritt
ein Forward-Verweis auf, der bei genauer Sichtung ein Synonym oder
eine abzulehnende Benennung eines bereits angelegten Begriffs ist,
gehört er in `abgelehnte_benennungen:` statt in `abgrenzung_zu:`.

**(D) Korpus-Begriff dauerhaft ohne eigenen Eintrag.** Der Begriff
existiert in der Korpus-Sprache (DACH-Holzbau, Bauwesen, CAD/BIM,
IFC, Mathematik) und ist für die Abgrenzung in einem Eintrag
**nützlich**, aber es ist **bewusst nicht geplant**, ihm einen
eigenen Hauptglossar-Eintrag zu geben — typischerweise weil er
in der App nicht modelliert wird oder als externes Begriffs-Pendant
(IFC-Entität, BTLx-Feldname) nur referenziert, nicht eigenständig
geführt wird. Der Forward-Verweis bleibt **dauerhaft** in
`abgrenzung_zu:` stehen; in den betroffenen Einträgen ist die
Nicht-Anlage im `quellenkonflikt:`- oder Erläuterungsblock kurz
zu begründen.

| Begriff | Forward-Verweis in | Begründung Nicht-Anlage |
|---|---|---|
| `bezugssystem` | `hg_koordinatensystem.md` | Mehrdeutig zwischen Geodäsie-/Physik-/Maschinenbau-Lesart; die App entscheidet sich für `koordinatensystem` als Hauptbenennung. |
| `bauteilgeometrie` | `hg_bauteilkoerper.md`, `hg_bauteilflaeche.md` | Code-Sealed-Klasse (`Bauteilgeometrie (Stab \| Flaeche \| Volumen)`); die ontologische Aufgliederung erfolgt im Code, nicht im Glossar. |
| `volumenkoerper` | `hg_bauteilkoerper.md`, `hg_bauteilflaeche.md` | In `hg_polyeder.md` und `hg_bauteilkoerper.md` bereits als `abgelehnte_benennungen:` geführt (zu allgemein in nackter Form); die qualifizierende Form ist Synonym von `bauteilkoerper`. |
| `ifc_shape_representation` | `hg_bauteilkoerper.md`, `hg_bauteilflaeche.md` | Externes IFC-Konstrukt; wird beim IFC-Export als Mapping-Ziel referenziert, nicht als App-Begriff geführt. |
| `auflageflaeche` | `hg_auflager.md` | Geometrische Manifestation des Auflagers (Polygon-Face am Bauteil-Polyeder); im `auflager`-Tupel als Polygon-Komponente bereits getragen, nicht eigenständig geführt. |
| `gps` | `hg_lineares_groessenmass.md` | Akronym „Geometrical Product Specification" — ISO-Rahmenwerk, das durch konkrete Norm-Teile (ISO 14405, ISO 1101, ISO 14638 …) zitiert wird; kein eigener App-Begriff. |
| `toleranzfeld` | `hg_lineares_groessenmass.md` | Tolerierungs-Konzept aus DIN EN ISO 14405-1; die App führt Toleranzen am Längenmaß/linearen Größenmaß selbst, ohne `toleranzfeld` als eigene Entität. |
| `bemassung` | `hg_laengenmass.md` | Prozess-/Tätigkeitsbegriff (das Eintragen von Maßen in eine Zeichnung); im Glossar werden nur die Resultats-Begriffe (`laengenmass`, `lineares_groessenmass`, `winkelmass`) geführt, nicht der Vorgang selbst. |
| `winkelmass` | `hg_laengenmass.md` | Bemaßung eines Winkels; im Holzbau bereits durch `dachneigung`, `hankinson_winkel` und weitere winkel-tragende Begriffe abgedeckt — kein eigener Eintrag. |

Die (D)-Tabelle ist **nicht Trigger-Liste**, sondern dauerhafte
Dokumentation. Sie unterscheidet sich von (A) durch die fehlende
Trigger-Spalte: hier ist die Nicht-Anlage Ziel, nicht Aufschub.

### Pflege

Die obige (A)-Tabelle gilt als verbindliche **Trigger-Liste** für
künftige Etappen: sobald einer der genannten Trigger eintritt
(erstes Tool / erste Domänen-Klasse / erste Visualisierungs-
Operation, die den Begriff fachlich braucht), wird der zugehörige
Glossareintrag angelegt, der Forward-Verweis in `voraussetzungen:`
oder `oberbegriff:` migriert und der Tabelleneintrag gestrichen.
Neu auftauchende Forward-Verweise werden bei der nächsten Sichtung
in die Tabelle aufgenommen.

## 7. Subglossar-Pendant-Pflichtigkeit (`subglossar_pendant:`)

**Orthogonale Achse zur Code-Pendant-Pflichtigkeit** (Sektion 3). Jeder
Hauptglossar-Eintrag trägt das Frontmatter-Feld `subglossar_pendant:`
mit einem von drei Werten:

- **`notwendig`** — ein Subglossar-Pendant (`lerninhalt/subglossar/
  sg_<id>.md`) muss existieren. Der Coverage-Linter (TG-4) bricht den
  Build, wenn die Datei fehlt.
- **`optional`** — ein Subglossar-Pendant darf existieren, der Linter
  erzwingt es nicht. **Begründungspflichtig** (siehe unten).
- **`nein`** — kein Subglossar-Pendant zulässig. Der Linter bricht den
  Build, wenn die Datei existiert. **Begründungspflichtig**.

Das Feld misst, ob die Theorie eines Begriffs für die unteren vier
Stufen **didaktisch aufbereitet** (in ein Subglossar-Pendant gespiegelt)
werden muss — nicht, „ob ein Begriff Theorie hat" (Theorie steigt durch
beide Säulen, siehe `docs/_DOKU_STRUKTUR.md`, Säulen-Modell).

### Normalfall und begründungspflichtige Abweichung

`notwendig` ist der **unmarkierte Normalfall**: im Regelfall verlangt
jeder Begriff eine didaktische Subglossar-Hülle für Schnuppi–Meister;
die Ingenieur-Stufe liest ohnehin direkt aus dem Hauptglossar.
`optional` und `nein` sind **begründungspflichtige Abweichungen**.

Das Feld wird in **jedem** Hauptglossar-Eintrag explizit gesetzt — es
gibt keine stille `begriffstyp`-Default-Ableitung; der TG-4-Linter
behandelt ein fehlendes Feld als Fehler.

### Begründungspflicht für `optional` und `nein`

Jeder Eintrag mit `optional` oder `nein` muss die Wahl begründen —
entweder direkt am Frontmatter-Feld als Kommentar (`# Begründung: …`),
im `quellenkonflikt:`-Block oder im `Implementierungshinweis`-Block
(mit der Begründung prominent erkennbar). Eine stille Abweichung ohne
Begründung ist nicht zulässig. (Der TG-4-Linter erzwingt die Begründung
nicht mechanisch — sie ist Konventionspflicht.)

Typische Begründungsmuster:

- `nein` für `relation`-Begriffe (z. B. `bausystem`): eine Relation
  beschreibt eine Beziehung, keinen greifbaren Gegenstand mit eigener
  didaktischer Hülle.
- `optional`, wenn die didaktische Substanz bei verwandten, selbst
  `notwendig`-Begriffen liegt (z. B. `einheitsvektor` → bei `vektor`;
  `halbraum` → bei `ebene`/`polyeder`).
- `optional` für Bemaßungs-/Tolerierungs-Begriffe (`laengenmass`,
  `lineares_groessenmass`), die in der unteren Stufen-Didaktik nicht
  zentral sind und erst beim künftigen Werkplan-/CNC-Tool greifen.

### Asymmetrie zur Code-Pendant-Pflicht

Die zwei Achsen sind **unabhängig**:

- Ein Begriff kann code-pendant-pflichtig **und** subglossar-pendant-frei
  sein (z. B. `gerichteter_plattenwerkstoff` mit `optional`).
- Ein Begriff kann code-pendant-frei **und** subglossar-pendant-pflichtig
  sein (z. B. `toleranzen` mit `subglossar_pendant: notwendig`).

### Pflege

Beim Anlegen oder Ändern eines Hauptglossar-Eintrags wird
`subglossar_pendant:` im Frontmatter explizit gesetzt — `notwendig` im
Normalfall, sonst `optional`/`nein` mit Begründung. Der Coverage-Linter
(TG-4) prüft Konsistenz mit der `lerninhalt/subglossar/`-Ablage.

## 8. Subglossar-Konvention — Verweis

Die vollständige Subglossar-Konvention (Datei- und Frontmatter-Form,
Body-Gliederung, Inhalts-Verbote, empfohlene Sektionen, SVG-Skizzen,
Stufen-Pattern, Asymmetrie Subglossar ↔ Hauptglossar) steht in
**`lerninhalt/subglossar/SG_KONVENTIONEN.md`**.

### Was HG-seitig gilt

- Das Frontmatter-Feld `subglossar_pendant:` an jedem Hauptglossar-
  Eintrag steuert, ob ein Subglossar-Pendant existieren muss; die
  Werte-Semantik (`notwendig`/`optional`/`nein`) steht in §7.
- Das Subglossar-Pendant trägt den Datei-Namen
  `lerninhalt/subglossar/sg_<id>.md`, wobei `<id>` die `id:` des
  Hauptglossar-Eintrags ist; das Subglossar-Frontmatter referenziert
  den Hauptglossar-Eintrag über `glossar_ref: <id>` und spiegelt den
  `subglossar_pendant:`-Wert.
- Drift zwischen Hauptglossar und Subglossar wird vom TG-4-Linter
  mechanisch sichtbar gemacht.

### Schicht-Trennung

Das Hauptglossar bleibt **parser-strikt und normativ** (mathematische
Definition, Wohldefiniertheit, Quellenkonflikt-Arbitrage, Quellen);
das Subglossar trägt die **didaktische Hülle** für die unteren vier
Stufen. Ingenieur-Stufe wird vom App-Renderer direkt aus dem
Hauptglossar bedient — kein Subglossar-Eintrag für Ingenieur.

Für **alle** Subglossar-internen Regeln (Frontmatter-Felder,
verbotene Section-Header, App-Verantwortungs-Trennung,
Stufen-Pattern) ist `SG_KONVENTIONEN.md` die normative Quelle.

## 9. Cluster-Struktur und Datei-Ablage

Seit 2026-05-14 liegen die Einträge nicht mehr flach unter
`hauptglossar/`, sondern in vier thematischen Cluster-Unterordnern.
Entscheidungsgrundlage: Recherche-Bericht
`docs/recherche/2026-05-14_hg_cluster_struktur.md` (Vorschlag V1,
IFC-naher 4-Schichten-Aufbau) plus NPK-Hybrid-Anker.

### 9.1 Die vier Cluster

| Pfad | Inhalt | Vorbild |
|---|---|---|
| `hauptglossar/00_ressourcen/` | Primitive Geometrie, Mathematik, Bauteil-Geometrie, Toleranzen — alle Begriffe ohne globale UUID, die im Code als reine Werte-Typen erscheinen | IFC Resource Layer |
| `hauptglossar/10_kern/` | Abstrakte UUID-tragende Wurzeln (Element, Bauteil, Bauwerk) und Identifikations-Begriffe (Uuid, Positionsnummer, Produktkennzeichnung) | IFC Core Layer |
| `hauptglossar/20_tragwerk/` | Tragwerks-Aggregate, Statik-Begriffe und Verbindungs-Konzepte | IFC Interoperability / StructuralAnalysis |
| `hauptglossar/30_holzbau/` | Holzbau-Domäne: Bauteilrollen, Werkstoffe, Bearbeitungen, Dach-Anatomie, Dachaufbau-Schichten | IFC Domain Layer |

**Tiefe:** maximal eine Ebene. Wenn `30_holzbau/` auf ~130 Einträge
wächst, ist eine zweite Ebene erlaubt (`30_holzbau/bauteilrolle/`,
`…/dach/`, `…/werkstoff/`, `…/bearbeitung/`). Sub-Cluster-Verfeinerung
ist Folgearbeit, keine sofortige Aktion.

### 9.2 Mapping-Regeln

**Primäre Heimat ist `oberbegriff:`-Vererbungs-Kette.** Wenn die
Vererbungs-Kette mehrere Cluster durchquert, gewinnt der **engste**
Cluster (am stärksten domänen-spezifische). Beispiel: `gratsparren`
erbt von `sparren` (Bauteilrolle) → Cluster `30_holzbau`, nicht
`20_tragwerk`.

**Polyhierarchie-Heuristik** (B.5 im Recherche-Bericht): Wenn ein
Begriff in zwei Cluster passt, primäre Heimat über `oberbegriff:`
fixieren, Querverweis per `abgrenzung_zu:` führen. Bekannte
Spannungs-Fälle: `dachstuhl` (Tragwerk-Aggregat in `20_tragwerk`,
Dach-Bezug im Body), `walm` (Bauteilgruppe in `20_tragwerk`,
Dach-Anatomie im Body).

**ID bleibt unverändert beim Verschieben zwischen Clustern.** Cross-
References (`oberbegriff:`, `voraussetzungen:`, `abgrenzung_zu:`,
Body-`` `id` ``-Refs) verwenden nur `id`, nie Pfade. Eine spätere
Cluster-Korrektur ist daher ein reines `mv` ohne Body-Eingriff.

### 9.3 NPK-Anker (Branchenstandard-Hybrid)

Die Cluster-Struktur ist gegen das Schweizer Branchenwerk
**NPK 335 Holzbauarbeiten** (Stand 2024, konsolidiert aus den
früheren Kapiteln 331/332/333) abgesteckt. Branchenstandard-
Anbindung ist auf Cluster-Ebene **referenziert**, nicht 1:1
geometrisch (die NPK ist kosten-zentriert, das Glossar
begriff-zentriert).

| Cluster | NPK-Pendant (Stand 2024) |
|---|---|
| `00_ressourcen/` | kein NPK-Pendant — App-/Mathematik-intern |
| `10_kern/` | kein NPK-Pendant — IT-/Identifikations-Schicht |
| `20_tragwerk/` | NPK 335 (Tragwerks-Anteile, früher Teil von 331) |
| `30_holzbau/` Bauteilrollen | NPK 335 (Bauteilrollen, früher 331) |
| `30_holzbau/` Werkstoffe | NPK 900 Materialstamm |
| `30_holzbau/` Bearbeitungen | NPK 335 (Pauschalen, kein eigener Code) |
| `30_holzbau/` Dach-Anatomie + Schichten | NPK 363 Dacheindeckung Steildach, NPK 364 Flachdach, NPK 365 Dachfenster/Photovoltaik |

Hintergrund zur 2024-Konsolidierung 331/332/333 → 335: Memory
`reference_richtpreise_holzbau` und Recherche-Bericht §B.7. Bei
Anbindung an Branchenstandard sind die aktuellen Codes (335, nicht
331/332/333) zu verwenden.

### 9.4 Folgearbeit-Trigger: Frontmatter-Feld `npk_code:`

Aktuell **nicht eingeführt**. Folgearbeits-Trigger für künftige
Einführung — Konvention für den Einführungs-Zeitpunkt:

- **Wann:** Erste konkrete Branchenstandard-Anbindung (Export
  Leistungsverzeichnis, Materialliste mit NPK-Codes, Schnittstelle
  zu einem Kalkulations-Tool).
- **Wie:** Optionales Frontmatter-Feld `npk_code:` pro Eintrag,
  Wert ist ein einzelner NPK-Hauptcode (z. B. `"335"`, `"363"`,
  `"900"`) oder leer/fehlend für Begriffe ohne NPK-Pendant
  (`00_ressourcen/`, `10_kern/`).
- **Befüllung:** **Nicht** als 108-Einträge-Backfill, sondern
  organisch eintragsweise bei der jeweils nächsten HG-Welle, die
  einen Eintrag berührt.

### 9.5 Pflege

- Bei neuem Eintrag: Cluster vor dem Anlegen wählen (eine der
  vier Optionen in §9.1) und Datei direkt im Cluster-Ordner anlegen.
- Bei Umklassifizierung (z. B. `walm` von `20_tragwerk` nach
  `30_holzbau` wenn der Bauteilrollen-Charakter überwiegt):
  reines `mv` zwischen Clustern, kein Body-Eingriff. Build-Adapter
  liest rekursiv.
- Bei einer Sub-Cluster-Einführung (z. B. `30_holzbau/dach/`):
  als eigener Etappenschritt mit Welle-Log in
  `STAND_HAUPTGLOSSAR.md` durchführen.

## 10. Quellen-Disziplin: direkt eingesehen vs. via Sekundärquelle

Norm- und Lehrbuch-Verweise im Frontmatter (`quellen_primär:`,
`quellen_sekundär:`) tragen einen **Einsehungs-Status**, der angibt, ob
die zitierte Quelle direkt im Volltext eingesehen wurde, nur in
Vorschau-Form (Inhaltsverzeichnis, kostenlose Auszüge) oder über eine
Sekundärquelle (Pressemitteilung, Merkblatt, Lehrbuch, das die Norm
zitiert).

**Begründung:** Normen-Volltexte sind häufig paywalled (DIN über
Beuth/DINmedia, SIA über SIA-Shop, ISO über ISO Store). Recherche-
Berichte rekonstruieren ihre Aussagen oft aus Sekundärquellen — das
ist fachlich tragfähig, muss aber transparent sein. Ein Verweis auf
„DIN 68800-2 §5" ohne Status suggeriert Volltext-Zugriff; wenn die
zitierten Werte aus einer Lignum-Pressemitteilung übernommen sind,
muss das markiert werden. Ohne diese Trennung entsteht der Eindruck
einer Primärquellen-Verankerung, die nicht besteht.

### 10.1 Marker-Syntax

Quellen-Zeilen tragen optional einen Klammer-Suffix mit dem
Einsehungs-Status. **Ohne Suffix gilt der Default: via Sekundärquelle
(nicht direkt eingesehen).** Der Default reflektiert die paywalled-
Realität — Normen-Volltexte sind selten direkt zugänglich, und die
ehrlichere Voreinstellung ist „aus Sekundärquelle rekonstruiert"
statt „direkt verifiziert".

| Marker | Bedeutung |
|---|---|
| (kein Marker) | via Sekundärquelle (Default — die Sekundärquelle ist in `quellen_sekundär:` zu finden) |
| `[direkt]` | Volltext direkt eingesehen (überschreibt Default) |
| `[einsicht: vorschau-pdf]` | nur kostenlose Vorschau-PDF direkt eingesehen (Inhaltsverzeichnis, Auszug) |
| `[einsicht: snippet]` | nur Snippet direkt eingesehen — Google-Books-Snippet, Buchausschnitt oder WebSearch-Suchergebnis-Snippet, **sofern der zitierte Wortlaut der Quelle im Snippet erschien** (nicht nur ein Norm-Titel oder eine Erwähnung) |
| `[via: <konkrete Quelle>]` | optional: konkrete Sekundärquelle benannt, wenn `quellen_sekundär:` mehrere Belege enthält |

„Direkter Volltext" schließt gekauftes PDF, kostenlos zugängliches
Volltext-PDF (z. B. via WebFetch eines öffentlichen Norm-PDFs),
Bibliothek-Vor-Ort-Einsicht und persönliche Norm-Sammlung ein.

Beispiele:

```yaml
quellen_primär:
  - "DIN 68800-2:2022-02 Abschnitt 5"
  - "SIA 265:2021 §1.1 Fachausdrücke [via: Lignum-Pressemitteilung 2021]"
  - "DIN EN ISO 129-1:2022-02 [einsicht: vorschau-pdf, Inhaltsverz.]"
  - "ISO 704:2009 Abschnitt 7 [direkt]"
```

In diesem Beispiel ist nur ISO 704 direkt eingesehen. DIN 68800-2 und
SIA 265 sind aus Sekundärquellen rekonstruiert; bei SIA wird die
Sekundärquelle explizit benannt, bei DIN ist sie generisch über
`quellen_sekundär:` zu erschließen. DIN EN ISO 129-1 ist nur in
Vorschau-Form eingesehen.

### 10.2 Pflege-Regel

- **Bei Neuanlage** Marker setzen, wenn die Quelle direkt eingesehen
  wurde oder in Vorschau-/Snippet-Form vorlag; ohne Marker gilt der
  Default „via Sekundärquelle" und es muss eine `quellen_sekundär:`-
  Liste vorhanden sein, die den Beleg trägt.
- **Drift entdeckt:** im laufenden R-Schritt fixen (Memory
  `feedback_glossar_drift_sofort`) oder als ABW-Eintrag, wenn
  `ABWEICHUNGEN.md` offen ist.

### 10.3 `quellen_sekundär:` selbst

`quellen_sekundär:`-Einträge (Lehrbücher, Merkblätter, Praxis-
Literatur) tragen **keine Marker**. Die Sektion ist per Definition
Sekundärlit, der Einsehungs-Status dort entscheidet die Quellen-
Beleg-Schärfe nicht. Wer Lehrbuch-Volltext-Zugriff dokumentieren
will, kann das im Quellenkonflikt-Block oder in der Erläuterung
tun, nicht im Frontmatter.

**Geltungsbereich Marker:** Die Marker-Disziplin (`[direkt]`,
`[einsicht: vorschau-pdf]`, `[einsicht: snippet]`, `[via: …]`)
ist **Frontmatter-spezifisch**. Der Prosa-`## Quellen`-Block im
Eintrag-Body (in dem Quellen typischerweise menschen-lesbar mit
Voll-Bibliographie aufgelistet werden) führt **keine Marker** —
weder verpflichtend noch optional. Wer Einsehungs-Status für eine
Prosa-Quelle dokumentieren will, formuliert das prosaisch
(„Volltext eingesehen am …", „Inhaltsverzeichnis-Vorschau …"),
nicht über Klammer-Suffix-Marker.

**Wikipedia und ähnliche Korpus-Quellen** gehören grundsätzlich
in `quellen_sekundär:` (Tier-Mittel-Niedrig nach Recherche-Agent-
Quellenhierarchie). Eine Aufnahme als `quellen_primär:` ist nur
zulässig, wenn das Wikipedia-Lemma die **einzige zugängliche
Definitionsquelle** für einen historischen Begriff ist und kein
Norm- oder Lehrbuch-Pendant existiert — und auch dann ist die
Sekundär-Einordnung der konservative Default.

### 10.4 Bestand-Audit-Methodik

Per §2 ist beim Etablieren dieser Konvention ein vollständiger
Bestand-Audit (alle Einträge) integraler Bestandteil des R-Schritts.
Methodik:

1. Pro Eintrag den zugehörigen Recherche-Bericht in
   `docs/recherche/` rückwärts prüfen: Welche Quelle wurde wie
   zitiert? Methodik-Sektion §A.1 zeigt typischerweise per WebFetch
   geladene URLs — daraus ist Volltext-/Vorschau-/Snippet-Status
   ablesbar.
2. **Direkter Volltext nachweisbar:** `[direkt]`-Marker setzen.
3. **Vorschau-/Snippet-Einsicht nachweisbar:** entsprechenden
   `[einsicht: ...]`-Marker setzen.
4. **Keine direkte Einsicht / unklare Lage:** kein Marker (Default
   „via Sekundärquelle" gilt); sicherstellen, dass `quellen_sekundär:`
   die Aussagen trägt. Wenn nicht, im Audit-Protokoll als
   schwach-belegt vermerken.
5. Audit-Bilanz in `STAND_HAUPTGLOSSAR.md` als eigene Welle
   dokumentieren.

## 11. Stabile Plain-Text-Notation für Mathematik

Die „## Mathematische Definition"-Code-Blöcke jedes Eintrags sind
**Plain-Text**, der von MkDocs Material ohne Math-Renderer (kein
MathJax/KaTeX) ausgegeben wird. Damit gelten **andere**
Stabilitätsregeln als für LaTeX-/MathML-gerenderte Mathematik.

Hintergrund-Recherche: `docs/recherche/2026-05-29_unicode_math_rendering.md`.
Primärquelle: **Unicode Technical Report #25 „Unicode Support for
Mathematics"** Sec. 2.6 — UTR #25 setzt für die Combining-Marks-
Konvention explizit eine „math display facility" voraus. Bei
plain-text-Auslieferung ohne solchen Renderer (unser Fall) liefert
die Combining-Marks-Variante in praktisch allen Programmier-Fonts
inkonsistente Render-Ergebnisse (Akzent rutscht auf nächstes Zeichen
— belegt durch JetBrains-Mono-#100, Cascadia-Code-#330,
VS-Code-#228347, Mozilla-#1500531).

### 11.1 Sechs Regeln

**Regel 1 — Keine Combining Diacritical Marks.** Die Bereiche
U+0300–U+036F (Combining Diacritical Marks) und U+20D0–U+20FF
(Combining Diacritical Marks for Symbols) sind in „## Mathematische
Definition"-Code-Blöcken **verboten**, soweit sie direkt hinter einem
Buchstaben stehen. Konkret verboten:

| Codepoint | Name | Beispiel verboten | Stabiler Ersatz (Regel 2) |
|---|---|---|---|
| U+0302 | COMBINING CIRCUMFLEX ACCENT | `n̂`, `v̂`, `x̂` | `n_hat`, `v_hat`, `x_hat` |
| U+0303 | COMBINING TILDE | `ñ` (math) | `n_tilde` |
| U+0304 | COMBINING MACRON | `n̄`, `x̄` | `n_bar`, `x_bar` |
| U+0305 | COMBINING OVERLINE | `n̅` | `n_bar` |
| U+0307 | COMBINING DOT ABOVE | `ẋ`, `ṅ` | `x_dot`, `n_dot` |
| U+0308 | COMBINING DIAERESIS | `n̈` (math) | `n_ddot` |
| U+20D7 | COMBINING RIGHT ARROW ABOVE | `v⃗` | `v_vec` |
| U+20D6 | COMBINING LEFT ARROW ABOVE | `v⃖` | `v_revvec` |

**Math-Symbole vs. natürlich-sprachlicher Akzent.** Die Regel betrifft
ausschliesslich akzentuierte Math-Symbole (Variablen, Vektoren,
Tensoren) in der „## Mathematische Definition"-Section und in
Math-Code-Blöcken. Präkomponierte Akzent-Buchstaben, die als Math-
Symbole verwendet werden — z. B. `ê` als Einheitsvektor, `ĥ` als
normierte Höhe, `â`, `û`, `ŷ` — fallen ebenfalls unter Regel 2 und
werden zu Suffix-Form (`e_hat`, `h_hat`, `a_hat`, `u_hat`, `y_hat`).
Begründung: visuelle Konsistenz im Glossar. Es soll **eine**
Schreibweise für „Buchstabe mit Hut" geben, unabhängig davon, ob
Unicode zufällig ein präkomponiertes Codepoint anbietet.

Akzentuierte Buchstaben in **natürlich-sprachlichen Wörtern** der
Prosa (Eigennamen, Fremdwörter) bleiben unangetastet — der Akzent
gehört dort zum Wort und ist keine math-symbolische Markierung.

**Regel 2 — Akzent-Suffix-Vokabular.** Akzentuierte Math-Symbole
werden als ASCII-Suffix geschrieben:

| Mathematischer Akzent | Bedeutung | Suffix |
|---|---|---|
| Hut `^` über Buchstabe | Einheitsvektor / normierte Größe | `_hat` |
| Pfeil `→` über Buchstabe | Vektor (ohne Normierung) | `_vec` |
| Balken `‾` über Buchstabe | Mittelwert / Komplement / Querstrich | `_bar` |
| Punkt `˙` über Buchstabe | Zeitableitung | `_dot` |
| Doppelpunkt `¨` über Buchstabe | Zweite Zeitableitung | `_ddot` |
| Tilde `~` über Buchstabe | Approximation / Schätzung | `_tilde` |

Beispiele:

- `n̂` (Normalen-Einheitsvektor) → `n_hat`
- `v⃗` (Verschiebungsvektor) → `v_vec`
- `x̄` (Mittelwert) → `x_bar`
- `ẋ` (Geschwindigkeit) → `x_dot`

Die Suffix-Form ist UTN-#28-Linear-Format-konform (Sargent, MS-Word-
Math-Linear-Modus). Lesbarkeit bleibt hoch, weil das Suffix das
typografische Symbol als ASCII-Pendant nennt.

**Regel 3 — Superscripts und Indizes.** Latin-1-Hochzahlen `¹ ² ³`
(U+00B9, U+00B2, U+00B3) sind erlaubt und empfohlen — sie sind in
praktisch jedem Font stabil. Für Hochzahlen ab `⁴` (U+2074) gilt:

- Kurzer Index in Prosa: `x⁴` ok.
- Längere Terme im Code-Block: lieber `x^4`, `x^(n+1)`, `x^(-1)` (ASCII-
  Caret-Notation, UTN-#28-konform).

Die **Transponierte** wird als `A^T` (ASCII) geschrieben, **nicht**
`Aᵀ` (U+1D40 MODIFIER LETTER CAPITAL T) — Latin-Extended-D-Block hat
schlechtere Font-Coverage als die Latin-1-Superscripts.

Indizes generell als `x_i`, `e_z`, `t_max` (ASCII-Underscore) statt
mit Unicode-Subscript-Glyphen (U+2080+ oder U+1D62+).

**Regel 4 — Mengen-Symbole zurückhaltend.** Die Double-Struck-Großbuchstaben
`ℝ ℕ ℤ ℚ ℂ` (U+211D, U+2115, U+2124, U+211A, U+2102) sind in
Programmier-Fonts oft nicht abgedeckt und fallen auf einen System-
Default zurück — das bricht die Monospace-Spaltenbreite. Wikipedia-MoS-
Mathematics warnt explizit. Empfehlung:

- In **Prosa** (ausserhalb von Code-Blöcken): `ℝ` ok, da Render-Fallback
  visuell harmlos.
- In **Code-Blöcken** der Mathematischen Definition: `R³` statt `ℝ³`,
  `N` statt `ℕ` etc. Wenn die typografische Form aus didaktischen
  Gründen wichtig ist, daneben die ASCII-Form mitgeben.

**Regel 5 — Klammern und Norm-Linien.**

- **Norm-Linie:** `‖x‖` (U+2016 DOUBLE VERTICAL LINE) wird beibehalten;
  Coverage ist breit. ASCII-Alternative `||x||` ist akzeptabel, aber
  nicht erforderlich.
- **Skalarprodukt-Klammern:** `⟨a, b⟩` (U+27E8/U+27E9 MATHEMATICAL
  LEFT/RIGHT ANGLE BRACKET) wird beibehalten — UTR #25 Sec. 2.5
  empfiehlt sie explizit als die math-korrekte Variante. Nicht zu
  verwechseln mit U+2329/U+232A (Legacy-CJK-Form, breit) oder
  U+3008/U+3009 (CJK).
- **Skalar-Punkt:** `·` (U+00B7 MIDDLE DOT, Latin-1) als Skalarprodukt-
  Punkt. **Nicht** `⋅` (U+22C5 DOT OPERATOR) — Latin-1-Erbschaft hat
  bessere Coverage.
- **Runde / eckige Klammern:** ASCII `( )` und `[ ]` ohnehin.

**Regel 6 — Erlaubte Bereiche ohne Sonderregel.**

- Griechische Buchstaben `α β γ δ ε ζ η θ ι κ λ μ ν ξ ο π ρ σ τ υ φ χ ψ ω` und
  Großbuchstaben `Γ Δ Θ Λ Ξ Π Σ Φ Ψ Ω` (U+0370+) — in praktisch jedem
  Font abgedeckt.
- Mathematische Operatoren `∈ ∉ ⊂ ⊆ ⊃ ⊇ ∪ ∩ ∅ ∀ ∃ ∂ ∇ ∑ ∏ ∫ √ ∞ ≤ ≥ ≠ ≈ ≡ ≅ ≪ ≫` (U+2200+) — gut abgedeckt.
- Pfeile `→ ← ↦ ↔ ⇒ ⇐ ⇔` (U+2190+) — gut abgedeckt.
- Bruchstrich `/` (ASCII) oder `÷` (Latin-1, U+00F7) — beide stabil.

### 11.2 Hintergrund

Die Combining-Marks-Form (`n̂` = `n` + U+0302) ist Unicode-konform —
UTR #25 dokumentiert sie als die richtige Codierung für math-akzentuierte
Variablen. Aber UTR #25 Sec. 2.6 sagt wörtlich (Revision 15, 2017):

> „mathematics uses a multitude of combining marks that greatly
> exceeds the predefined composed characters in Unicode. Accordingly,
> it is better to have the math display facility handle all of these
> cases uniformly".

→ Die Combining-Form setzt einen **math display facility** voraus
(LaTeX, MathML, MS Word Math-Mode). MkDocs Material ist keiner: der
Markdown-Plain-Text wird 1:1 an den Browser geliefert; der wiederum
sucht in der Code-Font (JetBrains Mono, Cascadia Code) nach einer
Glyph-Kombination `n` + Combining-Circumflex. Diese Glyph-Kombination
existiert in den meisten Programmier-Fonts nicht, weil sie in keiner
lebenden Sprache vorkommt — der Akzent fällt auf einen Fallback-Font
und wird typischerweise über das **nächste** Zeichen positioniert
(klassisches Combining-Mark-Misalignment).

NFC-Normalisierung repariert das **nicht**: für `n m v x y z` mit
Akzent gibt es kein präkomponiertes Codepoint, NFC liefert die
Sequenz unverändert.

Die Suffix-Konvention (`n_hat`) ist UTN-28-Linear-Format-konform und
hat den Zusatznutzen, dass sie auch in Plain-Text-Mail, ePub-Reader
und Konsole stabil ist — nicht nur in MkDocs.

### 11.3 Verhältnis zu LaTeX

Sollte das Glossar später auf einen Math-Renderer (MathJax/KaTeX)
umgestellt werden, ist die Suffix-Form trivial automatisch in
LaTeX-Notation übersetzbar: `n_hat → \hat{n}`, `v_vec → \vec{v}`,
`x_bar → \bar{x}`, `x_dot → \dot{x}`, `A^T → A^T`. Die Konvention
schliesst eine spätere LaTeX-Migration nicht aus, sondern bereitet sie
strukturell vor.

### 11.4 Bestand-Audit-Methodik

Per §2 ist ein vollständiger Bestand-Audit beim Etablieren dieser
Konvention erforderlich. Vorgehen:

1. **Grep über alle HG- und SG-Einträge** auf die in §11.1 Tabelle
   gelisteten Combining-Marks (U+0302, U+0303, U+0304, U+0305, U+0307,
   U+0308, U+20D6, U+20D7, U+20E1).
2. **Pro Eintrag** die Stellen prüfen: Tatsächlich Math-Variable (→
   Regel 2 anwenden) oder natürliches Wort mit Akzent (→ unverändert
   lassen)?
3. **Suchen-Ersetzen** pro identifizierter Math-Variable.
4. **Visueller Check** nach `sync.sh` und Site-Rebuild: rendert die
   neue Form in MkDocs Material in JetBrains Mono sauber?
5. **Welle-Bilanz** in `STAND_HAUPTGLOSSAR.md`.

Der erste Bestand-Audit zu dieser Konvention wurde am 2026-05-29
durchgeführt; betroffener Hauptkandidat war `n̂` im Geometrie-
Cluster (Falllinie und Normalen-Vektoren). Details in der
zugehörigen `STAND_HAUPTGLOSSAR.md`-Welle.
