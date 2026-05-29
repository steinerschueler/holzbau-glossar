---
id: lotebene
benennung: Lotebene
synonyme: ["Senkelebene durch die Bauteilachse", "Vertikalebene des Bauteils", "lotrechte Ebene durch die Bauteilachse"]
abgelehnte_benennungen: ["vertikale Schnittebene", "Lotebene zur Bauteilachse", "vertical plane", "plumb plane", "Senkelebene"]
oberbegriff: senkel
begriffstyp: merkmal
voraussetzungen: [senkel, ebene, bauteilachse, weltkoordinatensystem, einheitsvektor, toleranzen]
abgrenzung_zu: [senkel, bleischnitt, ebene, bauteilachse, bezugsebene, dachflaeche, weltkoordinatensystem]
status: entwurf
subglossar_pendant: optional
quellen_primär:
  - "Wikipedia, Lemma 'Lot (Mathematik)' (de.wikipedia.org/wiki/Lot_(Mathematik), abgerufen 2026-05-14): 'Eine Ebene, die senkrecht zu einer Geraden steht, heißt Lotebene.' — mathematische Lesart, hier abgelehnt, siehe quellenkonflikt-Block. [einsicht: snippet]"
  - "Wikipedia, Lemma 'Lotrichtung' (de.wikipedia.org/wiki/Lotrichtung, abgerufen 2026-05-14): 'Die örtliche Richtung der Schwerebeschleunigung.' — geodätische Verankerung des Lot-Begriffs. [einsicht: snippet]"
  - "Wikipedia, Lemma 'Vertikalkreis' (de.wikipedia.org/wiki/Vertikalkreis, abgerufen 2026-05-14): 'Großkreis der Himmelskugel, der durch Zenit und Nadir geht; die zugehörige Ebene ist eine Vertikalebene' — geodätisch-astronomisches Wortfeld für die hier gewählte Lesart (Ebene, die das Lot enthält). [einsicht: snippet]"
quellen_sekundär:
  - "Hartmann, E.: Darstellende Geometrie für Bauingenieure, Skript, TU Darmstadt (www2.mathematik.tu-darmstadt.de/~ehartmann/darg15.pdf, Volltext nicht eingesehen): Lotebene als Standard-Konstruktion der darstellenden Geometrie (mathematische Lesart)."
  - "Henke, K.: Darstellende Geometrie, Skript, Lehrstuhl für Holzbau und Baukonstruktion TU München (Volltext nicht eingesehen): Lotebene/Hilfsebene im Kontext orthogonale Parallelprojektion."
  - "LEIFIphysik, Brockhaus 'Horizont': Vertikalebene / lotrechte Ebene als Ebene, die das Lot enthält (geodätisch-astronomischer Sprachgebrauch)."
  - "docs/recherche/2026-05-14_hg_lotebene.md — interner Recherche-Bericht zur Begriffslage, Negativbefund Holzbau-Korpus, Abgrenzung der drei Bedeutungssphären (Mathematik / Geodäsie / Holzbau)."
quellenkonflikt: |
  Der Begriff „Lotebene" trägt **zwei nicht deckungsgleiche
  etablierte Bedeutungen** im deutschsprachigen Fachgebrauch, und
  beide Bedeutungen sind keine geschlossene Norm-Definition aus
  einer Holzbau-Norm — der Holzbau-Korpus selbst kennt den
  Begriff nicht eigenständig:

  1. **Mathematische Lesart** (Schul- und Hochschul-Mathematik,
     darstellende Geometrie; Wikipedia „Lot (Mathematik)",
     Hartmann TUD, Henke TUM): die Lotebene zu einer Geraden g
     durch einen Punkt P ist die Ebene mit Stützpunkt P, deren
     Normalenvektor der Richtungsvektor von g ist; sie steht
     rechtwinklig zu g. Der Wortteil „Lot" verweist hier auf
     „Lotgerade" / „Lotfußpunkt", **nicht** auf die Schwerkraft.
     Eine Welt-Vertikalität ist in dieser Lesart nicht eingebaut.

  2. **Geodätisch-astronomische Lesart** (Wikipedia „Lotrichtung",
     „Vertikalkreis", „Meridianebene"; LEIFIphysik;
     Brockhaus „Horizont"): eine **Vertikalebene** ist eine Ebene,
     die das **Lot** enthält (welt-vertikale Schwerkraft-Richtung).
     Der einschlägige stehende Begriff in diesem Wortfeld ist
     „Vertikalebene" (allgemein) bzw. „Meridianebene" (spezialisiert).
     Der Wortlaut „Lotebene" tritt in den durchsuchten geodätischen
     Quellen **nicht** unmittelbar auf — das Wortfeld besetzt
     „Vertikalebene" oder die Umschreibung „lotrechte Ebene".

  Im **DACH-Holzbau-Korpus** (SIA 265, DIN EN 1995-1-1, DIN 1052,
  Holzbau-Atlas, Mönck/Rug, Berufsfach-Foren) ist „Lotebene"
  **nicht als eigenständiger Fachbegriff belegt**; die
  Berufssprache verwendet `senkel`/`bleischnitt` für die Lot-
  Lage-Klassifikation einer Ebene und „Lotschnitt"/„Lotschiftung"
  als verfahrensbezogene Begriffe. Der vorliegende Eintrag ist
  daher eine **eigene Glossar-Wortbildung** im Anschluss an die
  geodätische Lesart, nicht eine Übernahme aus einer Holzbau-
  Norm.

  **Eigene Festlegung dieses Glossars** (geodätische Lesart, mit
  Achsen-Inzidenz-Bedingung): Eine **Lotebene** eines Stabbauteils
  B ist eine Ebene, die zugleich
  - ein **Senkel** ist (welt-vertikal, im Sinne von `hg_senkel.md`
    Gl. (1) — Ebenen-Normale rechtwinklig zur Welt-Lotachse), und
  - die **Bauteilachse** A_B enthält (im Sinne von
    `hg_bauteilachse.md`).

  Damit ist die Lotebene ein **Senkel mit zusätzlicher Inzidenz-
  Bedingung** und somit konsistent mit der bestehenden
  `senkel`/`bleischnitt`-Architektur als Prädikat über Ebenen.
  Sie ist `begriffstyp: merkmal` wie ihre Geschwister.

  **Wesentlicher Konflikt mit der mathematischen Lesart bei
  geneigter Bauteilachse**: Die beiden Lesarten fallen nur dann
  zusammen, wenn die Bauteilachse welt-horizontal ist; bei einem
  geneigten Sparren divergieren sie. Die **mathematische Lotebene
  zur Sparrenachse** (Normale = Sparrenachsen-Richtung) ist eine
  vom Bauteil determinierte schiefe Ebene — sie steht rechtwinklig
  zur Sparrenachse, ist aber weder Senkel noch Bleischnitt. Die in
  diesem Eintrag definierte **geodätische Lotebene** ist dagegen
  ein Senkel, der die Sparrenachse enthält — sie ist welt-vertikal,
  aber im allgemeinen **nicht** rechtwinklig zur Sparrenachse.

  Die Wahl der geodätischen Lesart ist begründet durch:
  - **Konsistenz mit `senkel`/`bleischnitt`**: beide bestehenden
    Lot-Lage-Begriffe sind welt-bezogen (gegen die Welt-Lotachse
    e_hat_z^welt formuliert); die Lotebene fügt sich in dieses Schema
    als Spezialisierung des Senkels ein.
  - **Anschluss an die Schweizer Berufssprache**: der Wortteil
    „Lot" steht im DACH-Holzbau-Korpus immer für den welt-vertikalen
    Schwerkraft-Bezug (Lot, Lotwaage, Lotmaß, Lotschnitt,
    Lotschiftung) — nie für die mathematische Lotgerade.
  - **App-interne Verwendung**: in `hg_kerve.md` L287–L288 wird die
    Lotebene bereits als „welt-vertikale Ebene, die die Bauteilachse
    enthält" eingeführt; der vorliegende Eintrag verankert diesen
    bestehenden Wortgebrauch normativ.

  Die mathematische Lesart wird im Glossar **abgelehnt** (siehe
  `abgelehnte_benennungen:` „Lotebene zur Bauteilachse"); wo die
  zur Bauteilachse **rechtwinklige** Ebene gemeint ist, wird im
  Glossar der Begriff `bezugsebene` oder eine ausdrückliche
  Umschreibung („Ebene rechtwinklig zur Bauteilachse durch …")
  verwendet.

  Detailrecherche und Quellenlage: siehe
  `docs/recherche/2026-05-14_hg_lotebene.md`.
---

## Prosa-Definition

Eine **Lotebene** eines Stabbauteils ist ein Senkel, der die
Bauteilachse enthält — also die welt-vertikale Ebene durch die
Bauteil-Längsachse.

## Mathematische Definition

Sei

- W das Welt-Koordinatensystem (siehe `weltkoordinatensystem`)
  mit Einheitsvektoren e_hat_x^welt, e_hat_y^welt, e_hat_z^welt, wobei
  e_hat_z^welt vertikal nach oben zeigt und die **Welt-Lotachsen-
  Richtung** trägt,
- B ein Stabbauteil im Sinne von `bauteil` mit
  `geometrie ∈ 𝒢_stab` und einer geraden, prismatischen
  Bauteilachse,
- A_B = [p_a, p_e] ⊂ ℝ³ die **Bauteilachse** von B im Sinne von
  `bauteilachse`, repräsentiert durch Anfangspunkt p_a,
  Endpunkt p_e und Richtungs-Einheitsvektor
  d_hat_B := (p_e − p_a) / ‖p_e − p_a‖ ∈ S²,
- O_B ∈ A_B ein beliebiger Punkt der Bauteilachse (z. B.
  p_a oder der Bauteil-Ursprung der lokalen Platzierung),
- E ⊂ ℝ³ eine Ebene im Sinne von `ebene`, repräsentiert in
  Hesse-Normalform durch das Paar (n_hat, d) ∈ S² × ℝ,
- ε_K := `Toleranzen.KOLLINEAR_EPS` die einschlägige
  dimensionslose Toleranzkonstante für Skalarprodukt-basierte
  Lage-Tests (siehe `toleranzen`),
- ε_L := `Toleranzen.LAENGE_EPS` die Längen-Toleranzkonstante
  für die Achsen-Inzidenz-Prüfung.

**Voraussetzung (nicht-vertikale Bauteilachse):**

```
| ⟨ d_hat_B, e_hat_z^welt ⟩ |  ≤  1 − ε_K.                                (V)
```

Bedingung (V) sichert, dass die Bauteilachse **nicht** parallel
zur Welt-Lotachse ist; siehe Wohldefiniertheit unten zum Sonderfall
welt-vertikaler Bauteilachse.

Dann gilt **`E ist Lotebene von B`** genau dann, wenn beide
Bedingungen erfüllt sind:

```
(L1)  E ist Senkel:        | ⟨ n_hat, e_hat_z^welt ⟩ |  ≤  ε_K.
(L2)  A_B ⊂ E:             dist(p_a, E)  ≤  ε_L  ∧  dist(p_e, E)  ≤  ε_L.
```

Dabei bezeichnet `dist(q, E) := |⟨n_hat, q⟩ − d|` den vorzeichenlosen
Punkt-Ebenen-Abstand (siehe `ebene`).

**Konstruktive Form** (Punkt-Normale-Repräsentation): Unter der
Voraussetzung (V) ist die **Lotebene** Π_⊥(B) eindeutig festgelegt
durch

```
Π_⊥(B)  :=  { O_B  +  s · e_hat_z^welt  +  t · d_hat_B  |  s, t ∈ ℝ }    (1)
```

mit Stützpunkt O_B ∈ A_B und aufspannenden Richtungen e_hat_z^welt
und d_hat_B. Äquivalente Hesse-Repräsentation: Normaleneinheitsvektor

```
n_hat_Π  :=  (e_hat_z^welt × d_hat_B) / ‖e_hat_z^welt × d_hat_B‖                    (2)
```

und Stützabstand d_Π := ⟨n_hat_Π, O_B⟩, also

```
Π_⊥(B)  =  { q ∈ ℝ³ |  ⟨n_hat_Π, q⟩  =  d_Π }.                        (3)
```

Der Nenner ‖e_hat_z^welt × d_hat_B‖ = sin∠(e_hat_z^welt, d_hat_B) ist unter
(V) bis auf höchstens ε_K von null verschieden, sodass n_hat_Π
wohldefiniert ist.

## Wohldefiniertheit

- **Existenz und Eindeutigkeit unter (V)**: Sind d_hat_B und
  e_hat_z^welt linear unabhängig (Bedingung (V)), so spannen sie
  einen zweidimensionalen Unterraum von ℝ³ auf. Die affine Ebene
  durch O_B mit diesem Richtungsraum ist eindeutig; sie enthält
  A_B (weil d_hat_B im Richtungsraum liegt) und ist ein Senkel (weil
  e_hat_z^welt im Richtungsraum liegt, also rechtwinklig zur Normale
  n_hat_Π = e_hat_z^welt × d_hat_B steht). Umgekehrt: jede Ebene, die A_B
  enthält und Senkel ist, muss e_hat_z^welt als Tangentialrichtung
  enthalten (Senkel-Bedingung) und d_hat_B (Achsen-Inzidenz) — damit
  ist sie gleich (1).

- **Unabhängigkeit vom Stützpunkt O_B**: Die Konstruktion (1)
  hängt scheinbar vom gewählten Punkt O_B ∈ A_B ab. Tatsächlich
  ist jedes O_B' ∈ A_B von der Form O_B' = O_B + λ · d_hat_B für
  ein λ ∈ ℝ; die Ebene durch O_B' mit denselben Richtungen
  e_hat_z^welt und d_hat_B ist dieselbe Punktmenge (die Translation
  bleibt im Richtungsraum). Die Definition ist damit von der
  Wahl von O_B unabhängig.

- **Vorzeichen-Invarianz der Normale**: n_hat_Π in (2) ist nur bis
  auf Vorzeichen festgelegt (Wahl der Reihenfolge im Kreuzprodukt
  oder Wahl der Orientierung von d_hat_B). Beide Vorzeichen liefern
  dieselbe Ebene Π_⊥(B); die Senkel-Bedingung (L1) ist eine
  Betragsbedingung und damit vorzeichen-invariant (siehe
  `hg_senkel.md` Wohldefiniertheit).

- **Sonderfall welt-vertikale Bauteilachse (Singularität)**:
  Ist Bedingung (V) verletzt — also d_hat_B parallel oder
  antiparallel zu e_hat_z^welt (typisch für eine welt-vertikale
  Stütze) —, dann ist e_hat_z^welt × d_hat_B = 0 und die Konstruktion
  (2) bricht zusammen. Geometrisch: in diesem Fall ist **jede**
  Ebene, die A_B enthält, automatisch ein Senkel (weil die Achse
  selbst parallel zur Lotachse verläuft); die Lotebene-Bedingungen
  (L1) und (L2) sind dann von einer ganzen einparametrigen Schar
  von Ebenen erfüllt, und Π_⊥(B) ist **nicht eindeutig
  festgelegt**. Die Lotebene ist in diesem Fall **undefiniert**;
  Anwendungs-Code muss diese Singularität explizit behandeln
  (siehe Implementierungshinweis).

- **Existenz im Toleranz-Grenzbereich**: Wird (V) gerade noch
  erfüllt (|⟨d_hat_B, e_hat_z^welt⟩| nahe an 1 − ε_K), so ist n_hat_Π
  zwar wohldefiniert, aber die numerische Konditionierung des
  Kreuzprodukts wird schlecht. Praktisch betroffen sind nur
  Bauteile mit Einbau-Neigung sehr nahe 90° gegen die
  Horizontale (steiler als ca. arccos(ε_K)). Für den
  App-Default ε_K = 10⁻⁹ entspricht das einer Neigungs-
  Reststrecke unterhalb 5,73·10⁻⁸ Grad und liegt damit weit
  jenseits jeder praktischen Holzbau-Geometrie.

- **Konsistenz mit (L1) ∧ (L2)**: Die konstruktive Form (1)
  und die Prädikat-Form (L1) ∧ (L2) beschreiben unter
  Voraussetzung (V) dieselbe Ebene. Beweis: (1) erfüllt (L1)
  (weil n_hat_Π rechtwinklig zu e_hat_z^welt steht, siehe (2)) und
  (L2) (weil p_a = O_B + λ_a · d_hat_B mit λ_a ∈ ℝ in (1) liegt,
  analog p_e). Umgekehrt: jede Ebene, die (L1) und (L2)
  erfüllt, enthält d_hat_B (über (L2)) und e_hat_z^welt als
  Tangentialrichtung (über (L1)) — damit ist sie durch O_B
  und das Richtungspaar (d_hat_B, e_hat_z^welt) eindeutig festgelegt
  und gleich (1).

- **Nicht-Zirkularität**: Die Definition stützt sich nur auf
  bereits definierte Begriffe (`senkel`, `ebene`, `bauteilachse`,
  `weltkoordinatensystem`, `einheitsvektor`, `toleranzen`). Sie
  kommt nicht in ihrer eigenen Definition vor und verweist
  nicht auf `bleischnitt` als Voraussetzung, sondern nur in der
  Abgrenzung.

## Erläuterung (nicht normativ)

### Hinweis zur Theorie-Pflicht

`subglossar_pendant: optional` (Abweichung vom Normalfall `notwendig`,
`HG_KONVENTIONEN.md` §7) ist hier **bewusst** gewählt: die Lotebene ist
eine konstruierte Hilfsebene ohne eigenständigen Stufen-Inhalt für die
Lehrlings-Stufen; der bedeutungstragende didaktische Stoff liegt bei
den Geschwistern `senkel` und `bleischnitt` (beide `notwendig`), von
denen die Lotebene strukturell als Ebenen-Klassifikation abgeleitet
ist.

### Etymologie und Wortgebrauch

Der Wortteil „Lot" verweist im DACH-Holzbau-Korpus durchgängig
auf das klassische Zimmermanns-Werkzeug (Bleigewicht an einer
Schnur, das per Schwerkraft die welt-vertikale Richtung
markiert). Die Lotebene ist die Ebene, **die das Lot enthält**
— sie schneidet eine ideal aufgehängte Lotschnur durchgehend
(nicht in einem einzelnen Punkt). Eine Lotebene durch ein
geneigtes Stabbauteil enthält darüber hinaus die Bauteilachse
und bildet damit die natürliche Bezugs-Vertikalebene zur
Beschreibung von Bauteil-Schnittflächen, die welt-bezogene
Ausrichtung tragen.

Der Begriff ist im Holzbau-Korpus **nicht als stehender
Fachbegriff belegt** (Recherche-Bericht
`docs/recherche/2026-05-14_hg_lotebene.md`); er wird in diesem
Glossar in Analogie zu `senkel` und `bleischnitt` eingeführt
und ist konsistent mit dem geodätisch-astronomischen
Sprachgebrauch (Wikipedia „Lotrichtung", „Vertikalkreis"). Die
abgelehnten Synonyme „vertikale Schnittebene" und „vertical
plane" sind unspezifisch (keine Achsen-Bindung); „Vertikalebene"
ist im geodätischen Sprachgebrauch ohne Achsen-Bindung etabliert
und wird daher hier nicht als Hauptbenennung gewählt, kann aber
in der Erläuterung verwendet werden.

### Verwendung im Holzbau

Lotebenen treten als geometrischer Bezug an mehreren Stellen auf:

- **Kerv-Geometrie eines Sparrens** (siehe `hg_kerve.md`,
  Gleichungen (0)–(4)): die Lotebene Π_⊥(B) ist die Bezugsebene
  für die Definition der Kerv-Eckpunkte C, P, A und der welt-
  aligned Hilfsrichtungen e_hat_h (welt-horizontal in der Lotebene)
  und e_hat_v = e_hat_z^welt (welt-vertikal). Die welt-Ausrichtung der
  Schnittflächen (Sohlenebene als Bleischnitt, Senkelebene als
  Senkel) wird relativ zur Lotebene formuliert.
- **Werkplan-Aufriss eines Stabbauteils**: der traditionelle
  Aufriss eines geneigten Sparrens wird auf die Lotebene des
  Sparrens projiziert; die im Aufriss sichtbare Bauteilkontur
  ist die Schnittlinie der Bauteilhülle mit der Lotebene.
- **Falllinien-Konstruktion** an einer Dachfläche: die Falllinie
  durch einen Punkt der Dachfläche liegt in der Lotebene durch
  diesen Punkt und die Dachflächen-Normale (in Analogie zur
  Bauteilachsen-Konstruktion hier, siehe `hg_falllinie.md`).

### Beziehung zu Senkel und Bleischnitt

Die drei Lot-bezogenen Ebenen-Klassen des Glossars stehen in
folgender struktureller Beziehung:

| Begriff | Bedingung an die Ebene |
|---|---|
| `senkel` | Normalenvektor rechtwinklig zur Welt-Lotachse: \|⟨n_hat, e_hat_z^welt⟩\| ≤ ε_K |
| `bleischnitt` | Normalenvektor parallel zur Welt-Lotachse: \|⟨n_hat, e_hat_z^welt⟩\| ≥ 1 − ε_K |
| `lotebene` eines Bauteils B | ist Senkel **und** enthält die Bauteilachse A_B |

Jede Lotebene ist also ein Senkel; nicht jeder Senkel ist eine
Lotebene (der Senkel sagt nichts über die enthaltene Bauteilachse).
Lotebene und Bleischnitt sind unter Voraussetzung (V) disjunkt
(eine Ebene kann nicht gleichzeitig Senkel und Bleischnitt sein,
siehe `hg_senkel.md` Wohldefiniertheit).

### Abgrenzung zur mathematischen Lotebene

Der Begriff „Lotebene" ist im **Schul- und Hochschul-Mathematik-
Kanon** abweichend besetzt: dort bezeichnet er die Ebene
**rechtwinklig zu einer Geraden** (Normalenvektor = Richtungsvektor
der Geraden). Bei geneigter Bauteilachse fallen die beiden Lesarten
auseinander:

- **Mathematische Lotebene zur Sparrenachse** (nicht im Glossar
  geführt): Normale parallel zu d_hat_B, also rechtwinklig zur Sparrenachse —
  eine vom Sparren determinierte schiefe Ebene; weder Senkel
  noch Bleischnitt.
- **Lotebene im Sinne dieses Eintrags** (geodätisch): Senkel
  durch die Sparrenachse — welt-vertikal, aber im allgemeinen
  nicht rechtwinklig zur Sparrenachse.

Die beiden fallen genau dann zusammen, wenn die Bauteilachse
welt-horizontal ist (d_hat_B rechtwinklig zu e_hat_z^welt). Siehe
quellenkonflikt-Block.

### Toleranz in der Praxis

Die Singularitätsbedingung (V) ist mit `KOLLINEAR_EPS = 10⁻⁹`
extrem scharf und filtert nur exakt-vertikale Bauteilachsen.
Praktisch entscheidet die Anwendungs-Schicht, wie streng die
Vertikalitäts-Klassifikation eines Bauteils erfolgt — eine
Stütze mit Einbau-Neigung 0,01° gegen die Vertikale ist nach
(V) zwar formal nicht singulär, ihr Lotebene-Konstruktor ist
aber numerisch schlecht konditioniert. Die App führt für
Stützen-artige Bauteile keine Lotebene; sie ist für
Stabbauteile mit deutlich geneigter Achse (Sparren) gedacht.

## Beziehungen

- **Oberbegriff**: `senkel`. Eine Lotebene ist ein Senkel mit
  zusätzlicher Inzidenz-Bedingung gegen die Bauteilachse.
- **Spezialisierungen**: keine eigenständigen Glossar-
  Spezialisierungen. Konkrete Anwendungen (Kerv-Bezugsebene,
  Sparren-Aufrissebene) sind keine eigenen Begriffe, sondern
  Verwendungen.
- **Bestandteile**:
  - **Trägerebene** (geerbt von `senkel` und letztlich `ebene`):
    die Punktmenge im Welt-Koordinatensystem.
  - **Bauteilachsen-Inzidenz** (zusätzlich gegenüber `senkel`):
    die enthaltene Bauteilachse A_B als Identifikations-Anker.
- **Verwendung**:
  - **Kerv-Geometrie** in `hg_kerve.md`: Π_⊥(B) als Bezugsebene
    für die Kerv-Eckpunkte und die welt-aligned Hilfsrichtungen
    e_hat_h, e_hat_v.
  - **Werkplan-Aufriss** eines Sparrens (Folgearbeit).
  - **Falllinien-Konstruktion** an Dachflächen (Folgearbeit).
- **Abgrenzung**:
  - **Senkel** (`senkel`): Oberbegriff. Jede Lotebene ist ein
    Senkel, aber nicht jeder Senkel ist eine Lotebene — der
    Senkel-Begriff trägt keine Achsen-Inzidenz-Bedingung.
  - **Bleischnitt** (`bleischnitt`): geometrisch komplementäre
    Lot-Lage-Klasse (Ebene rechtwinklig zur Welt-Lotachse).
    Eine Lotebene ist unter Voraussetzung (V) niemals ein
    Bleischnitt.
  - **Ebene** (`ebene`): allgemeines geometrisches Primitiv
    ohne Lot- oder Achsen-Bezug. Lotebene ist eine
    Spezialisierung mit zwei Lage-Bedingungen.
  - **Bauteilachse** (`bauteilachse`): die Trägerachse der
    Inzidenz-Bedingung. Die Bauteilachse ist eine eindimensionale
    Punktmenge in ℝ³, die Lotebene eine zweidimensionale; die
    Lotebene enthält die Bauteilachse als Untermenge.
  - **Bezugsebene** (`bezugsebene`): tool-eigene Höhenreferenz
    mit zusätzlicher Bezugsrolle. Eine Bezugsebene im Standardfall
    ist ein Bleischnitt (horizontal), eine Lotebene ist es nicht;
    die beiden Begriffe sind orthogonale Spezialisierungen.
  - **Dachfläche** (`dachflaeche`): geneigte Berandungsfläche.
    Eine Dachfläche ist im Regelfall weder Senkel noch
    Lotebene; nur im Grenzfall Dachneigung = 90° wäre sie ein
    Senkel (aber im allgemeinen keine Lotebene eines bestimmten
    Sparrens).
  - **Welt-Koordinatensystem** (`weltkoordinatensystem`): legt
    die Welt-Lotachse e_hat_z^welt fest, gegen die die Senkel-
    Bedingung (L1) formuliert ist. Ohne Welt-Koordinatensystem
    ist die Lotebene nicht definiert.

## Implementierungshinweis

**Kein eigener Code-Typ.** Lotebene wird in der Domänen-Schicht
als **Konstruktor-Funktion** auf einem Stabbauteil realisiert,
die eine `Ebene` zurückliefert (analog zur `senkel`/`bleischnitt`-
Prädikat-Form, aber mit Konstruktor-Charakter wegen der
Achsen-Inzidenz-Bedingung). Die Funktion ist ein Resultat-Typ,
weil sie bei welt-vertikaler Bauteilachse undefiniert ist:

```kotlin
package domain.geometrie

import domain.Toleranzen
import domain.bauteil.Bauteil
import kotlin.math.abs

/**
 * Lotebene eines Stabbauteils: die welt-vertikale Ebene, die
 * die Bauteilachse enthält.
 *
 * Konstruktion (siehe hg_lotebene.md Gl. (1)–(3)):
 *
 *   n_hat_Π = (e_hat_z^welt × d_hat_B) / ‖e_hat_z^welt × d_hat_B‖,
 *   d_Π = ⟨n_hat_Π, O_B⟩.
 *
 * Singularität: Bei welt-vertikaler Bauteilachse
 * (|⟨d_hat_B, e_hat_z^welt⟩| > 1 − KOLLINEAR_EPS) ist die Lotebene
 * **nicht eindeutig** — der Konstruktor liefert dann
 * `Lotebene.AchseVertikal`.
 *
 * Glossar: hg_lotebene.md (Spezialisierung von hg_senkel.md
 * mit zusätzlicher Bauteilachsen-Inzidenz).
 */
sealed class LotebeneResultat {
    data class Ebene(val ebene: domain.geometrie.Ebene) : LotebeneResultat()
    data object AchseVertikal : LotebeneResultat()
}

fun Bauteil.lotebene(
    eps: Double = Toleranzen.KOLLINEAR_EPS
): LotebeneResultat {
    val d = this.achse.richtungEinheit()        // d_hat_B
    val ez = WeltKoordinatensystem.eZ            // e_hat_z^welt
    val cos = abs(d.skalar(ez))                  // |⟨d_hat_B, e_hat_z^welt⟩|
    if (cos > 1.0 - eps) return LotebeneResultat.AchseVertikal
    val n = ez.kreuz(d).normiert()               // n_hat_Π
    val o = this.achse.anfangspunkt()            // O_B
    return LotebeneResultat.Ebene(
        domain.geometrie.Ebene.ausPunktUndNormale(o, n)
    )
}
```

- **Einheit**: keine direkte Einheit; die Lotebene ist eine Ebene
  im Welt-Koordinatensystem (Längeneinheit der Stützabstände in
  mm, geerbt von `ebene`).
- **Identität**: keine eigene Identität; die Lotebene wird aus
  dem Bauteil abgeleitet und trägt keine eigene UUID. Mehrfache
  Aufrufe von `bauteil.lotebene()` liefern dieselbe Ebene (modulo
  Vorzeichen der Normale).
- **Toleranz**: `KOLLINEAR_EPS` für die Singularitätsbedingung
  (V). Die Inzidenz-Prüfung (L2) verwendet `LAENGE_EPS` für die
  Endpunkt-Abstände — relevant, wenn eine vorgegebene Ebene als
  Lotebene-Kandidat klassifiziert werden soll (Prädikatlesart,
  hier nicht primär implementiert).
- **Edge Cases**:
  - **Welt-vertikale Stütze** (Stützen-artiges Bauteil mit
    d_hat_B = ±e_hat_z^welt): Konstruktor liefert
    `LotebeneResultat.AchseVertikal`; aufrufender Code muss den
    Fall behandeln (z. B. Lotebene durch zusätzliche
    Konvention festlegen oder Geometrie-Pfad abbrechen).
  - **Bauteil mit gekrümmter Achse**: nicht im Scope des
    Konstruktors; die Lotebene ist für Stabbauteile mit gerader
    Achse definiert. Für gekrümmte Achsen müsste die Lotebene
    punktweise (pro Achsen-Parameter s) konstruiert werden;
    Folgearbeit-Trigger.
  - **Numerische Konditionierung nahe der Singularität**: bei
    |⟨d_hat_B, e_hat_z^welt⟩| nahe 1 − ε_K wird das Kreuzprodukt
    kurz und n_hat_Π ungenau; in der Praxis irrelevant, weil
    diese Konfiguration weit jenseits realer Sparren-Neigungen
    liegt.

**Folgearbeit (trigger-basiert):**

- **`vertikalebene`** als allgemeinerer Geschwister-Begriff
  (Senkel **ohne** Achsen-Inzidenz, im Sprachgebrauch der
  Geodäsie/Astronomie): nicht im aktuellen Tool-Bedarf;
  Trigger: erstes Tool, das eine welt-vertikale Ebene ohne
  Bauteilachsen-Bindung als eigenständiges Objekt benötigt.
  Bis dahin reicht `senkel` als Oberbegriff.
- **Vereinheitlichung mit `hg_sparren.md` L182**: dort wird
  „Vertikalebene" einmal informell verwendet; bei nächster
  substanzieller `hg_sparren.md`-Überarbeitung in „Lotebene"
  angleichen oder explizit als Synonym führen.
- **Lotebene für gekrümmte Bauteilachsen**: punktweise
  Konstruktion entlang der natürlichen Achsen-Parametrisierung.
  Trigger: erstes Tool mit gekrümmten Bauteilen (BSH-Bögen,
  gekrümmte Brettschichtholz-Träger).
- **`falllinie`-Cross-Verweis**: die Falllinie einer Dachfläche
  durch einen Punkt liegt in einer Lotebene durch diesen Punkt
  und die Dachflächen-Normale; Strukturparallele zur
  Bauteilachsen-Konstruktion hier. Trigger: bei nächster
  substanzieller `hg_falllinie.md`-Überarbeitung.

## Quellen

**Primär (normativ und konzeptuell):**

- Wikipedia, Lemma „Lot (Mathematik)"
  (de.wikipedia.org/wiki/Lot_(Mathematik), abgerufen 2026-05-14):
  mathematische Lesart, hier abgelehnt.
- Wikipedia, Lemma „Lotrichtung"
  (de.wikipedia.org/wiki/Lotrichtung, abgerufen 2026-05-14):
  geodätische Verankerung des Lot-Begriffs.
- Wikipedia, Lemma „Vertikalkreis"
  (de.wikipedia.org/wiki/Vertikalkreis, abgerufen 2026-05-14):
  geodätisch-astronomisches Wortfeld der hier gewählten Lesart.

**Sekundär:**

- Hartmann, E.: *Darstellende Geometrie für Bauingenieure.*
  Skript, TU Darmstadt
  (www2.mathematik.tu-darmstadt.de/~ehartmann/darg15.pdf,
  Volltext nicht eingesehen): Lotebene als Standard-Konstruktion
  der darstellenden Geometrie (mathematische Lesart).
- Henke, K.: *Darstellende Geometrie.* Skript, Lehrstuhl für
  Holzbau und Baukonstruktion TU München (Volltext nicht
  eingesehen): Lotebene/Hilfsebene im Kontext orthogonale
  Parallelprojektion.
- LEIFIphysik; Brockhaus, Lemma „Horizont": Vertikalebene /
  lotrechte Ebene als Ebene, die das Lot enthält.

**Recherche-Bericht (intern):**

- `docs/recherche/2026-05-14_hg_lotebene.md` — Belegfreiheit
  im DACH-Holzbau-Korpus, drei Bedeutungssphären (Mathematik /
  Geodäsie / Holzbau), Lesart-Optionen, Negativbefunde
  (SIA 265, DIN EN 1995-1-1, DIN 1052, Holzbau-Atlas,
  Mönck/Rug, baubeaver.de).

**Korpus (nicht autoritativ, intern):**

- `hauptglossar/hg_kerve.md` (L287–L288, L357 ff.) — bestehende
  App-interne Verwendung der Lotebene als „welt-vertikale Ebene,
  die die Bauteilachse enthält"; dieser Eintrag verankert den
  bestehenden Wortgebrauch normativ.
- `hauptglossar/hg_senkel.md`, `hauptglossar/hg_bleischnitt.md` —
  Geschwister-Begriffe zum Lot-Lage-Schema; Lotebene als
  Spezialisierung des Senkels.
