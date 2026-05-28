---
id: anschnitt
benennung: Anschnitt
synonyme: [Stirnanschnitt, "geneigter Endschnitt", Anschnittschnitt]
abgelehnte_benennungen: [Schrägschnitt, Kappschnitt, "chamfer", "bevel", "miter cut", "end cut", "angle cut", "cut"]
oberbegriff: bearbeitung
begriffstyp: partitiv
voraussetzungen: [bearbeitung, bauteil, bauteilachse, ebene, stirnseite, polyeder, lokales_koordinatensystem, toleranzen]
abgrenzung_zu: [kerve, stirnseite, bearbeitung, senkel, bleischnitt, schmiege, hexenschnitt, versatz, bohrung, zapfen, zapfenloch, fase, querschnitt, bauteilachse]
status: entwurf
theorie_pflichtig: required
quellen_primär:
  - "DIN EN 1995-1-1:2010-12 (Eurocode 5), Abschnitte 5.2 (Berücksichtigung von Querschnittsschwächungen) und 6.5 (Querzug- und Schubnachweise an ausgeklinkten Bauteilen): geneigte Endschnitte am Stab-Bauteil werden bemessungstechnisch als Querschnittsänderung erfasst; eine geschlossene geometrische Definition des Begriffs „Anschnitt“ wird nicht gegeben."
  - "design2machine: 'BTLx interface description', Version 2.1, 16.11.2023, Abschnitt 'List of Processings', Einträge 'JackRafterCut' (Endanschnitt am Sparren mit Parametern Orientation, StartX, StartY, Angle, Inclination, ReferencePlane), 'LongitudinalCut' (längsläufiger Anschnitt mitten am Bauteil), 'DoubleCut' (Doppelanschnitt am selben Endpunkt) und 'TriangleCut' (dreieckiger Endabschnitt): die parametrische Industriestandard-Spezifikation des geneigten Stab-Endschnitts; abstrahiert die Welt-Ausrichtung der Anschnittebene in Inclination-Parameter."
  - "DIN 1052:2008-12, Abschnitt 12 (Konstruktive Anforderungen): Auflagerausbildung geneigter Stäbe mit Stirnschnittausbildung am Sparrenfuß und Sparrenfirstpunkt."
  - "SIA 265:2021 'Holzbau', Schweizerischer Ingenieur- und Architektenverein, Abschnitt 5 (Konstruktive Durchbildung): Stirnausbildung am Stab-Bauteilende; geneigte Schnittflächen sind als Querschnittsänderung in der Bemessung zu berücksichtigen."
quellen_sekundär:
  - "Mönck, W.; Rug, W.: Holzbau – Bemessung und Konstruktion. 16. Aufl., Beuth, Berlin 2015, Kap. 11 'Dachtragwerke', § Sparrenfuß und Stirnausbildung am Sparrenkopf: Verwendung des Begriffs „Anschnitt“ für den geneigten Endschnitt eines Sparrens unter dem Anschnittwinkel α."
  - "Gerner, M.: Fachwerk – Instandsetzung, Sanierung, Neubau. DVA, 7. Aufl. 2007, Glossar 'Senkelschnitt', 'Bleischnitt', 'Schmiege' (Anschnitt-Verwandte; „Anschnitt“ selbst nicht als eigenes Lemma)."
  - "Natterer, J.; Herzog, T.; Volz, M.: Holzbau-Atlas. 4. Aufl., Birkhäuser, Basel 2003, Kap. 'Dachtragwerke', Stirnausbildung."
  - "Lignum (Hrsg.): Holzbautabellen HBT, Lignum, Zürich, aktuelle Auflage, Kap. 'Sparrenanschlüsse' und 'Austragen': Stirnanschnitte am Sparrenfuß und Sparrenfirstpunkt."
  - "Eurotec: Anfängerlehrbuch Teil 3.3 'Holzverbindungen', Kap. Sparren-Pfetten-Anschluss: Verwendung von „Anschnitt“ als Sammelwort für Sparrenfuß-Senkelschnitt und -Bleischnitt."
quellenkonflikt: |
  Es existiert **keine geschlossene normative Begriffsdefinition**
  für „Anschnitt“ in den deutschsprachigen Holzbau-Normen
  (SIA 265, SIA 232/1, DIN EN 1995-1-1, DIN 1052, DIN 68800). Die
  Normen setzen den Begriff voraus, wo er überhaupt vorkommt, und
  beschreiben nur die Bemessungsfolgen einer Stirnausbildung am
  Stab-Ende. Auch die BTLx-2.1-Spezifikation (design2machine)
  kennt kein Lemma „Anschnitt“; das Konzept wird dort über
  mehrere Processing-Klassen abgebildet (siehe „BTLx-Mapping" in
  diesem Block). Die geschlossene Festlegung erfolgt hier
  glossarseitig durch eigene Festlegung, konsistent mit der
  Berufspraxis (Mönck/Rug, Lignum HBT, Eurotec, polybau.ch).
  Methodisches Vorgehen analog zu `hg_senkel.md`,
  `hg_bleischnitt.md` und `hg_kerve.md` (Begriff in Normen
  vorausgesetzt, geschlossene Festlegung über zimmermanns-
  sprachlichen Korpus). Vollständige Quellenlage und
  Falsifizier-Bereitschaft im Recherchebericht
  `docs/recherche/2026-05-14_hg_anschnitt.md`.

  **Drei-Trennung Kerve ↔ Stirnseite ↔ Anschnitt:**

  Die App führt drei separate Konzepte, deren Trennung durch alle
  konsultierten Quellen gestützt wird:

  | Konzept | Eintrag | Typ | Lage am Bauteil | Geometrische Konstitution |
  |---|---|---|---|---|
  | **Kerve** | `hg_kerve.md` | Bearbeitung (`begriffstyp: partitiv`) | innen an der Längsseite, kann nahe Bauteilende liegen | zweiflächige Auskerbung mit Dreiecksquerschnitt (Sohle + Senkel); schwächt den Längsquerschnitt |
  | **Stirnseite** | `hg_stirnseite.md` | Bauteilfläche (`begriffstyp: generisch`) | am Bauteilendpunkt | ebene polygonal berandete Endfläche auf einer Trägerebene; Resultat-Sicht |
  | **Anschnitt** | dieser Eintrag | Bearbeitung (`begriffstyp: partitiv`) | am Bauteilendpunkt | eine Anschnittebene am Endpunkt; erzeugt eine Stirnseite mit α_AS ≠ π/2 |

  Die Trennung ist scharf:

  - Eine **Kerve** ist **nicht** am Stirnende, sondern an der
    Längsseite; sie erzeugt **keine** Stirnseite, sondern
    schwächt den Längsquerschnitt. Eine Kerve nahe dem
    Bauteilende bleibt eine Kerve (zwei Flächen, Sohle + Senkel),
    keine Stirnausbildung.
  - Eine **Stirnseite** ist die geometrische **Endfläche** am
    Bauteilendpunkt — die polygonal berandete Resultat-Fläche,
    unabhängig vom Schnittwinkel α_AS. Stirnseite ist
    **kein** Bearbeitungs-Subtyp, sondern eine Bauteilfläche.
  - Ein **Anschnitt** ist die **Bearbeitung**, die das nicht
    bearbeitete Bauteilende durch eine Anschnittebene am
    Endpunkt zu einer geneigten Stirnseite umformt. Anschnitt
    ist **kein** Lage-Prädikat (wie `senkel`/`bleischnitt`),
    **keine** Endfläche (wie `stirnseite`) und **keine**
    Längsseiten-Auskerbung (wie `kerve`).

  Die Beziehung lässt sich knapp formulieren: ein **Anschnitt
  als Bearbeitung erzeugt eine geneigte Stirnseite als
  Resultat-Fläche**. Die Stirnseite trägt die Geometrie der
  Endfläche; der Anschnitt trägt die Werkzeug-Parametrisierung
  (Anschnittebene, Anschnittwinkel, Anschnittseite). Im
  prismatischen Standardfall α_AS = π/2 gibt es keinen Anschnitt;
  die Stirnseite ist dann rechtwinklig zur Bauteilachse und
  fällt mit dem Querschnitt am Bauteilendpunkt zusammen
  (siehe `hg_stirnseite.md`, prismatischer Standardfall).

  **BTLx-Mapping ist 1:n (nicht 1:1):**

  Der App-Begriff Anschnitt umfasst — analog zur Konvention bei
  `hg_kerve.md` (`BirdsMouth` + `HipValleyRafterNotch` +
  `StepJointNotch`) — **mehrere** BTLx-Processings auf einen
  begrifflich homogenen App-Typ:

  | App-Subtyp Anschnitt-Anwendung | Primäre BTLx-Entsprechung |
  |---|---|
  | Standard-Endanschnitt am Sparren (Trauf-/First-Stirnanschnitt) | `JackRafterCut` |
  | längsläufiger Anschnitt mitten am Bauteil (Folgearbeit `laengsanschnitt`) | `LongitudinalCut` |
  | Doppelanschnitt am selben Endpunkt (Folgearbeit `schmiege` bzw. `hexenschnitt`) | `DoubleCut` |
  | dreieckiger Endabschnitt | `TriangleCut` |

  Die App-Klasse `Anschnitt` modelliert in dieser ersten Stufe
  ausschließlich den **einfachen Endanschnitt** mit **einer**
  Anschnittebene am Bauteilendpunkt (primär `JackRafterCut`).
  Längs- und Doppelanschnitte sind Folgearbeiten mit eigenen
  Glossareinträgen.

  **Eigene Festlegung — Bezug des Anschnittwinkels:**

  Die Recherche dokumentiert mehrere im Korpus verwendete
  Bezüge (Bauteilachse, Welt-Lotachse, Dachneigung,
  Falllinie der Dachfläche). Die App wählt die **Bauteilachse**
  als Definitions-Bezug für den Anschnittwinkel α_AS — konsistent
  mit `hg_stirnseite.md` (4) und mit der BTLx-`Inclination`-
  Konvention. Welt-bezogene Spezialfälle (Senkelschnitt,
  Bleischnitt) sind **abgeleitete Eigenschaften** der
  Anschnittebene über die Prädikate `Ebene.istSenkel` und
  `Ebene.istBleischnitt` (siehe `hg_senkel.md`, `hg_bleischnitt.md`).
  Diese Asymmetrie zwischen Bauteil-lokaler Definition und
  welt-bezogener Klassifikation ist konsistent mit der HG-
  Konvention zu Senkel/Bleischnitt.

  **Wertebereich α_AS — offene Schranken:**

  Der Anschnittwinkel α_AS ist auf das offene Intervall
  (ε_W, π/2 − ε_W) festgelegt:

  - α_AS = π/2 wäre ein rechtwinkliger Endschnitt
    (prismatischer Standardfall); das ist **kein** Anschnitt im
    Sinne dieses Eintrags, sondern das nicht bearbeitete
    Bauteilende.
  - α_AS → 0 wäre eine tangentiale Anschnittebene; die
    resultierende Stirnseite würde entarten (Faser läge in der
    Anschnittebene, kein Materialabtrag mehr).

  Diese Konvention deckt sich mit `hg_stirnseite.md` (4)
  (Anschnittfall mit α_AS ∈ (ε_W, π/2 − ε_W)).

  **Synonym „Stirnanschnitt":**

  Im Korpus (Mönck/Rug Kap. 11, Eurotec) wird „Stirnanschnitt"
  als **Anwendungsbenennung** für den Anschnitt am Bauteilende
  (im Gegensatz zu mittenständigen Längsanschnitten) verwendet.
  Da die App-Klasse `Anschnitt` in dieser ersten Stufe
  ausschließlich Endanschnitte modelliert, ist „Stirnanschnitt"
  ein zulässiges Synonym. Sobald der Folgearbeit-Eintrag
  `laengsanschnitt` angelegt wird, bleibt „Stirnanschnitt"
  Synonym von **Anschnitt am Bauteilende** und damit weiterhin
  der App-Klasse `Anschnitt` zugeordnet.

  **Nicht als Synonym geführt:**

  - **Schmiege** ist **enger** als Anschnitt: sie verlangt eine
    Verschneidung (Schifter an Grat-/Kehlsparren) und trägt
    zusätzliche Bezugsrolle (Anfallfläche an Grat-/Kehlachse).
    Schmiege ist Folgearbeit-Eintrag (`schmiege`), nicht
    Synonym.
  - **Senkelschnitt / Bleischnitt** sind welt-bezogene
    **Spezialfälle** des Anschnitt-Resultats (die
    Anschnittebene ist ein Senkel bzw. Bleischnitt). Sie sind
    eigene Lage-Prädikate über Ebenen, keine Synonyme.
  - **Hexenschnitt** ist ein **Doppelanschnitt** am
    Traufendpunkt von Grat-/Kehlsparren (Folgearbeit-Eintrag
    `hexenschnitt`), keine Synonymie zum einfachen
    Endanschnitt.

  **„Doppelschmiege" nicht aufgenommen:**

  Die Bezeichnung „Doppelschmiege" ist im DACH-Holzbau-Korpus
  nicht als eigenständiges Lemma belegt (siehe Recherche §D.4,
  Tier-Einstufung „unbelegt"). Die geometrische Konstellation
  zweier Schmiegen am selben Bauteilendpunkt wird im Korpus
  unter „Hexenschnitt" geführt; „Doppelschmiege" wird in
  diesem Glossar **nicht** als Synonym oder Lemma aufgenommen.
  Falls eine Korpus-Verankerung später nachgewiesen wird, kann
  ein eigener Eintrag oder ein Synonym ergänzt werden.

  Diese Festlegung ist konsistent mit allen konsultierten
  Quellen.
---

## Prosa-Definition

Ein **Anschnitt** ist eine subtraktive Bearbeitung am Endpunkt eines
Stab-Bauteils, die durch eine einzige Anschnittebene am Bauteil-
Endpunkt vollständig festgelegt ist, deren Normale gegen die
Bauteilachsen-Tangente am Endpunkt einen von π/2 verschiedenen
Anschnittwinkel einschließt, und die als Resultat eine zur
Bauteilachse geneigte Stirnseite des Bauteils erzeugt.

## Mathematische Definition

Sei

- F eine **Bearbeitung** nach `bearbeitung` mit Typ
  τ = Anschnitt ∈ 𝓣,
- B ∈ 𝓑 das zugehörige Stab-Bauteil mit Bauteilachse A(B), die
  Tangentenrichtung d̂(s) ∈ S² an der Stelle s ∈ [0, L], Anfangs-
  punkt p_a := A(B)(0) und Endpunkt p_e := A(B)(L) (siehe
  `bauteilachse`),
- σ ∈ {ANFANG, ENDE} die **Anschnittseite** (analog zu
  `Endposition` in `hg_stirnseite.md`); setze

  ```
  p_σ := { p_a , falls σ = ANFANG;
           p_e , falls σ = ENDE }                                  (1a)
  d̂_σ := { −d̂(0) , falls σ = ANFANG;
            +d̂(L) , falls σ = ENDE }                              (1b)
  ```

  (d̂_σ ist die nach außen gerichtete Tangentenrichtung am
  Anschnittendpunkt),

- E_AS ⊂ ℝ³ die **Anschnittebene**, Ebene nach `ebene` durch p_σ
  mit Einheitsnormaler n̂_AS ∈ S²,
- α_AS := arccos|⟨n̂_AS, d̂_σ⟩| ∈ (ε_W, π/2 − ε_W) der **Anschnitt-
  winkel** mit ε_W := `Toleranzen.WINKEL_EPS`,
- 𝓡 ⊂ ℝ³ ein abgeschlossener, beschränkter „Schnitt-Bereichs-
  Polyeder" am Bauteil-Endpunkt, gross genug, dass er das gesamte
  Material des Bauteils auf der Außenseite der Anschnittebene
  umschließt (Bounding-Box des Bauteilkörpers am Endpunkt p_σ).

Die **Anschnittebene** zerlegt ℝ³ in zwei abgeschlossene Halbräume

```
H_+(E_AS) := { x ∈ ℝ³ | ⟨n̂_AS, x − p_σ⟩ ≥ 0 },                    (2a)
H_−(E_AS) := { x ∈ ℝ³ | ⟨n̂_AS, x − p_σ⟩ ≤ 0 }.                    (2b)
```

Per Konvention zeigt n̂_AS **aus dem Bauteil heraus**:

```
⟨n̂_AS, d̂_σ⟩ > 0.                                                  (3)
```

Damit ist H_+(E_AS) der Halbraum auf der Außenseite des
Bauteilendpunktes (Werkzeug-Halbraum) und H_−(E_AS) der Halbraum
auf der Bauteilseite.

Der **Werkzeugkörper** der Anschnitt-Bearbeitung ist die Begrenzung
des Außenseiten-Halbraums auf den Schnitt-Bereichs-Polyeder 𝓡:

```
K_Anschnitt(p_τ) := H_+(E_AS) ∩ 𝓡 ⊂ ℝ³.                          (4)
```

K_Anschnitt(p_τ) ist ein abgeschlossener, beschränkter Polyeder
im Sinne von `polyeder` (Schnitt zweier konvexer abgeschlossener
beschränkter Mengen ist konvex, abgeschlossen, beschränkt).

Damit ist eine **Anschnitt-Bearbeitung** im Sinne von
`hg_bearbeitung.md` das Tupel

```
F_AS := (uuid, Anschnitt, p_τ = (σ, E_AS), T_F, bezeichnung?),    (5)
```

mit

- **σ** ∈ {ANFANG, ENDE}: Anschnittseite,
- **E_AS**: Anschnittebene durch p_σ mit Einheitsnormaler n̂_AS
  unter Bedingungen (3) und α_AS ∈ (ε_W, π/2 − ε_W),
- **T_F** ∈ SE(3): lokale Platzierung des typeigenen Bezugs-
  Koordinatensystems im Bauteil-Lokal-System (per Konvention
  Identität in SE(3), wenn p_τ direkt im Bauteil-Lokal-System
  parametrisiert ist; siehe Implementierungshinweis).

Die **Wirkung** des Anschnitts auf das Bauteil ist die Boole'sche
Differenz nach `hg_bearbeitung.md` (1):

```
G_B'(F_AS) = G_B^lokal \ T_F( K_Anschnitt(p_τ) ).                 (6)
```

Geometrisch entspricht (6) dem Abschneiden des Bauteilmaterials,
das auf der Außenseite der Anschnittebene liegt.

Das **Resultat** des Anschnitts ist eine geneigte **Stirnseite**
nach `hg_stirnseite.md` an der Anschnittseite σ:

```
S_σ(B; F_AS) := (∂F_S, E_AS, n̂_AS, p_σ)                          (7)
```

mit

- **Trägerebene** der Stirnseite ist die Anschnittebene E_AS,
- **Aussennormale** der Stirnseite ist n̂_AS (kanonisch aus
  Bauteil heraus, siehe (3)),
- **Bezugspunkt** der Stirnseite ist p_σ,
- **Berandung** ∂F_S ist das durch E_AS am bearbeiteten
  Bauteilkörper G_B'(F_AS) entstehende Schnittpolygon.

Es gilt nach Konstruktion

```
|⟨n̂_AS, d̂_σ⟩| = cos(α_AS) < 1 − ε_W,                             (8)
```

also α_AS ≠ π/2; die Stirnseite ist damit **nicht** rechtwinklig
zur Bauteilachse und im Sinne von `hg_stirnseite.md` (4) eine
geneigte (Anschnitt-)Stirnseite.

## Wohldefiniertheit

- **Existenz**: Für jeden Anschnittwinkel α_AS ∈ (ε_W, π/2 − ε_W)
  und jede Anschnittseite σ existiert eine Anschnittebene E_AS
  durch p_σ mit n̂_AS unter (3) und mit dem entsprechenden α_AS.
  Mindestkonfiguration: σ = ENDE, n̂_AS in der durch d̂(L) und
  einer beliebigen zweiten Welt-Richtung aufgespannten Ebene mit
  Winkel α_AS zu d̂(L). Damit existiert F_AS.
- **Eindeutigkeit der Identität**: Wie in `hg_bearbeitung.md`
  über UUID v7 nach RFC 9562.
- **Wohldefiniertheit des Werkzeugkörpers**: Aus E_AS und der
  Vorzeichenkonvention (3) folgt H_+(E_AS) eindeutig. Der
  Schnitt H_+(E_AS) ∩ 𝓡 ist eindeutig, sobald 𝓡 als
  Schnitt-Bereichs-Polyeder festgelegt ist. Die Wahl von 𝓡 wirkt
  sich auf die geometrische Repräsentation des Werkzeugkörpers
  aus, nicht auf die Wirkung (6): zwei verschiedene Wahlen
  𝓡, 𝓡' mit G_B^lokal ⊂ H_−(E_AS) ∪ 𝓡 ∩ 𝓡' liefern dasselbe
  G_B'(F_AS), weil die Differenz nur den Bauteil-internen
  Schnitt H_+(E_AS) ∩ G_B^lokal entfernt. Konkrete App-Konvention:
  𝓡 wird als minimale axenparallele Bounding-Box um G_B^lokal mit
  einem `LAENGE_EPS`-grossen Sicherheitsabstand gewählt; diese
  Wahl ist semantisch invariant.
- **Wohldefiniertheit der Wirkung**: Die Boole'sche Differenz
  (6) ist nach `hg_bearbeitung.md` Wohldefiniertheits-Block
  stets wohldefiniert (abgeschlossene beschränkte Polyeder); das
  Ergebnis ist eine messbare, beschränkte Punktmenge.
- **Wohldefiniertheit der resultierenden Stirnseite**: Die
  Polygonberandung ∂F_S nach (7) ist als Schnitt der
  Anschnittebene E_AS mit dem bearbeiteten Bauteilkörper
  G_B'(F_AS) wohldefiniert; sie ist im Standardfall (konvexer
  Stab-Querschnitt) ein konvexes Polygon im Sinne von
  `hg_polygon.md`. Die Existenz und Eindeutigkeit der
  resultierenden Stirnseite folgt aus `hg_stirnseite.md`
  Wohldefiniertheits-Block, angewandt auf die Trägerebene E_AS.
- **Eindeutigkeit der Anschnittebene gegeben (σ, n̂_AS)**: Aus
  der Wahl der Anschnittseite σ folgt p_σ; aus n̂_AS und (3)
  folgt die Orientierung von E_AS; aus dem Inzidenzpunkt p_σ ∈
  E_AS folgt die Lage der Ebene. Damit ist E_AS eindeutig.
- **Vorzeichen-Invarianz**: Die Hesse-Normalform von E_AS ist
  durch (3) ohne Vorzeichenmehrdeutigkeit festgelegt; in der
  Code-Repräsentation wird die Aussennormale-Konvention durch
  (3) erzwungen.
- **Reihenfolge-Unabhängigkeit bei mehreren Bearbeitungen**:
  Wie in `hg_bearbeitung.md` (kommutative Vereinigung); zwei
  Anschnitte am gleichen Bauteilendpunkt (Doppelanschnitt-
  Sonderfall, Folgearbeit) werden als zwei separate
  Bearbeitungen geführt, ihre Wirkungen kombinieren sich
  reihenfolge-invariant.
- **Konsistenz Werkzeugkörper ↔ Bauteilgeometrie**: Im
  Standardfall ragt K_Anschnitt(p_τ) per Konstruktion (4)
  vollständig in den Außenseiten-Halbraum H_+(E_AS); der
  bauteil-interne Anteil ist H_+(E_AS) ∩ G_B^lokal, was genau
  der zu entfernende Materialteil ist. Die in
  `hg_bearbeitung.md` Edge-Case-Bedingung „Werkzeugkörper
  teilweise außerhalb des Bauteils" ist hier strukturell der
  Standard und keine Verletzung.
- **Plausibilität der Resultats-Stirnseite** (weiche Invariante):
  α_AS-Grenzwerte nahe ε_W oder π/2 − ε_W liefern numerisch
  schwierige Resultate (extrem schmale Anschnittfläche bei
  α_AS → 0 bzw. fast rechtwinkliger Endschnitt bei α_AS →
  π/2). Die App warnt — typisiert in der Bemessungs-/
  Validierungs-Schicht — bei Werten ausserhalb eines
  praxisüblichen Korridors (z. B. α_AS ∈ [π/12, π/2 − π/180]).
  Diese Warnung ist **keine** Definitionsbedingung.
- **Nicht-Zirkularität**: Die Definition stützt sich nur auf
  `bearbeitung`, `bauteil`, `bauteilachse`, `ebene`,
  `stirnseite`, `polyeder`, `lokales_koordinatensystem` und
  `toleranzen`. Sie kommt nicht in ihrer eigenen Definition vor
  und verweist nicht auf konkrete Anschnitt-Folgearbeiten
  (`schmiege`, `hexenschnitt`, `laengsanschnitt`).

## Erläuterung (nicht normativ)

### Was ein Anschnitt ist und was nicht

Der Anschnitt ist die **Bearbeitung**, die am Endpunkt eines
Stab-Bauteils einen geneigten Endschnitt herstellt. Anschnitt ist:

- **kein Lage-Prädikat** wie `senkel` oder `bleischnitt` (die
  beschreiben die Welt-Ausrichtung einer Ebene);
- **keine Endfläche** wie `stirnseite` (die ist die Resultat-
  Fläche am Bauteilendpunkt);
- **keine Längsseiten-Auskerbung** wie `kerve` (die liegt an der
  Längsseite, nicht am Ende);

sondern ein **Bearbeitungs-Subtyp** unter `bearbeitung`,
parallel zu `bohrung`, `versatz`, `zapfenloch`, `schlitz`,
`blatt`, `kamm`, `fase`. Die Resultat-Sicht (die geneigte
Stirnseite) wird über `hg_stirnseite.md` adressiert; der
Anschnitt selbst trägt die Werkzeug-Parametrisierung.

### Typologie der App-Anwendungsfälle

Der App-Begriff Anschnitt deckt im Erstentwurfs-Umfang
einfache End-Anschnitte mit einer Anschnittebene am
Bauteilendpunkt ab. Innerhalb dieses Umfangs treten in der
zimmermannssprachlichen Praxis mehrere Anwendungstypen auf,
deren Klassifikation rein **welt-bezogen** ist (also über die
Prädikate auf der Anschnittebene, nicht über zusätzliche
Anschnitt-Parameter):

- **Senkelschnitt am Sparrenfuß** (oder am Sparrenfirstpunkt):
  die Anschnittebene ist ein `senkel`, also parallel zur
  Welt-Lotachse. Resultat-Stirnseite zeigt vertikal nach unten
  (Sparrenfuß) bzw. firstwärts vertikal (Sparrenfirstpunkt).
  Klassifikation: `E_AS.istSenkel()` liefert `true`.
- **Bleischnitt am Sparrenfuß** (oder am Sparrenfirstpunkt):
  die Anschnittebene ist ein `bleischnitt`, also rechtwinklig
  zur Welt-Lotachse. Resultat-Stirnseite zeigt waagerecht
  (Sparrenfuß-Bleischnitt). Klassifikation:
  `E_AS.istBleischnitt()` liefert `true`.
- **Stirnanschnitt allgemein**: jeder Anschnitt am Bauteilende
  fällt unter diese Anwendungsbenennung (synonym mit Anschnitt
  im Erstentwurfs-Umfang); die Anschnittebene ist weder
  Senkel noch Bleischnitt im scharfen Sinne, sondern eine
  beliebige geneigte Ebene am Endpunkt.

Die folgenden Anwendungsfälle gehen **über** den Erstentwurfs-
Umfang hinaus und sind Folgearbeit-Einträge mit eigenen
Geometriebeschreibungen:

- **Schmiege** (Folgearbeit `schmiege`): Anschnitt-
  Spezialisierung an einer Schifter-Grat- oder
  -Kehl-Verschneidung. Die Anschnittebene trägt eine
  zusätzliche Bezugsrolle (Anfallfläche an Grat-/Kehlachse).
  Drei Sub-Spezialisierungen aus dem Korpus (Lueger 1904,
  Wikipedia/Schiftung):
  - **Fußschmiege** (am Schifter-Fußpunkt),
  - **Lotschmiege / Senkelschmiege** (lotrechte Anfallfläche),
  - **Backenschmiege** (auf der Sparren-Seitenfläche).
- **Hexenschnitt** (Folgearbeit `hexenschnitt`): **Doppelanschnitt**
  am Traufendpunkt eines Grat- oder Kehlsparrens, zur
  fluchtgerechten Verlängerung der Sparren-Traufschnitte über
  den Walmgrat hinaus. Zwei Anschnittebenen am selben Endpunkt;
  modelliert als zwei `Anschnitt`-Instanzen mit derselben
  Anschnittseite, aber unterschiedlichen Anschnittebenen.
- **Längsanschnitt** (Folgearbeit `laengsanschnitt`): Anschnitt
  mitten am Bauteil in Bauteil-Längsrichtung, BTLx
  `LongitudinalCut`. Trigger: erste Sparrenverbreiterung oder
  Längsverjüngung. Vom Endanschnitt durch die Position abweichend.

### Wahl des Anschnittwinkel-Bezugs

In der Berufspraxis tauchen mehrere Bezüge für den
„Anschnittwinkel" auf — Bauteilachse, Welt-Lotachse,
Dachneigung, Falllinie der Dachfläche. Diese App wählt die
**Bauteilachse** als Definitions-Bezug (α_AS = ∢(n̂_AS, d̂_σ)),
konsistent mit der BTLx-`Inclination`-Konvention und mit
`hg_stirnseite.md`. Welt-bezogene Sichten (Senkel-/Bleischnitt-
Eigenschaft, Winkel gegen Dachfläche) sind **abgeleitete
Sichten** über die bestehenden Prädikate und Funktionen, nicht
Bestandteil der Anschnitt-Parametrisierung.

Diese Wahl ist **Bauteil-lokal** und damit invariant gegen
Einbau-Orientierung des Bauteils (Drehung des Sparrens um
seine Bauteilachse ändert α_AS nicht). Die welt-bezogene
Klassifikation (Senkel/Bleischnitt) ändert sich dagegen mit
der Einbau-Orientierung — das ist beabsichtigt und entspricht
der zimmermannssprachlichen Verwendung der drei Begriffe.

### Schiftung als Verfahren, nicht als Bearbeitung

Die in der Wikipedia/Schiftung dokumentierte Notation
„Anschnitt = XO/XU-Paar" (Schnittwinkel an Ober- und
Unterkante des Sparrens, etwa bei einem Schiftsparren am
Walmgrat) ist eine **Konstruktions-Anweisung** zur Bestimmung
der Anschnittwinkel über die Schiftung. Die Schiftung selbst
ist ein **Verfahren**, kein Bearbeitungs-Subtyp; sie gehört in
einen Folgeeintrag `schiftung` oder in das Subglossar
(Lehrlingsstufe). Das geometrische Resultat einer geschifteten
Anschnitt-Bestimmung ist eine `Anschnitt`-Instanz im Sinne
dieses Eintrags.

## Beziehungen

- **Oberbegriff**: `bearbeitung`. Der Anschnitt ist ein
  Bearbeitungs-Subtyp in der sealed-Aufzählung 𝓣 (siehe
  `hg_bearbeitung.md`). Er erbt UUID, lokale Platzierung,
  Bezeichnung, und insbesondere die partitive Komposition
  unter dem Bauteil (kein eigenständiger Lebenszyklus).
- **Spezialisierungen** (Folgearbeit, eigene Glossareinträge):
  - **Schmiege** (`schmiege`, Folgearbeit): Anschnitt-
    Spezialisierung an Schifter-Grat-/Kehl-Verschneidung,
    mit zusätzlicher Bezugsrolle (Anfallfläche an
    Grat-/Kehlachse). Drei Sub-Spezialisierungen aus dem
    Korpus: Fußschmiege, Lotschmiege/Senkelschmiege,
    Backenschmiege. Trigger: erstes Walmdach-Tool mit
    Schiftern.
  - **Hexenschnitt** (`hexenschnitt`, Folgearbeit):
    Doppelanschnitt am Traufendpunkt eines Grat- oder
    Kehlsparrens. Trigger: Walmdach-Tool mit Dachkasten-Detail.
  - **Längsanschnitt** (`laengsanschnitt`, Folgearbeit):
    Anschnitt mitten am Bauteil in Bauteil-Längsrichtung
    (BTLx `LongitudinalCut`). Trigger: erstes Tool mit
    Sparrenverbreiterung oder Längsverjüngung.
  - **Doppelanschnitt allgemein** (Folgearbeit, ggf. Subtyp
    von `schmiege` oder `hexenschnitt`): zwei Anschnittebenen
    am selben Endpunkt (BTLx `DoubleCut`).
- **Bestandteile (partitiv)**:
  - **UUID** (`uuid`, geerbt von `bearbeitung`): technische
    Identität, Pflicht.
  - **Anschnittseite** σ ∈ {ANFANG, ENDE}: Pflicht.
  - **Anschnittebene** E_AS (`ebene`): Pflicht; bestimmt durch
    Inzidenz mit p_σ und Einheitsnormaler n̂_AS unter (3).
  - **Lokale Platzierung** T_F ∈ SE(3) (geerbt von
    `bearbeitung`): Pflicht; in der Standard-Konvention
    Identität in SE(3).
  - **Bezeichnung**: optional.
  - **Abgeleitete Eigenschaften** (Funktionen, keine Felder):
    Anschnittwinkel α_AS = arccos|⟨n̂_AS, d̂_σ⟩|; Lot-Lage der
    Anschnittebene (Senkel/Bleischnitt/geneigt); resultierende
    Stirnseite nach (7).
- **Verwendung**:
  - **Stirnseite** (`stirnseite`): das geometrische Resultat
    eines Anschnitts ist eine geneigte Stirnseite mit
    α_AS ≠ π/2 (siehe `hg_stirnseite.md` (4)). Die Stirnseite
    ist die Resultat-Sicht; der Anschnitt ist die Bearbeitung.
  - **Sparren** (`sparren`), **Gratsparren** (`gratsparren`),
    **Kehlsparren** (`kehlsparren`, Folgearbeit): typische
    Trägerbauteile von Anschnitten (Trauf-, First- und
    Walmgrat-Stirnausbildung).
  - **Bemessung** (EC5 5.2 / SIA 265 4.6): Anschnitt-Stirnseite
    ist eine Querschnittsänderung am Stab-Bauteilende; die
    Bemessungs-Schicht zieht aus α_AS und der resultierenden
    Stirnflächenfläche die Auflagerbedingungen ab.
- **Abgrenzung**:
  - **Kerve** (`kerve`): Bearbeitung an der Längsseite des
    Sparrens, zweiflächig (Sohle + Senkel), Dreiecksquerschnitt;
    schwächt den Längsquerschnitt, erzeugt **keine** Stirnseite.
    Anschnitt liegt am Bauteilende, ist einflächig (eine
    Anschnittebene) und erzeugt eine Stirnseite. Eine Kerve
    nahe dem Bauteilende ist **keine** Anschnitt-Bearbeitung,
    sondern eine Kerve im Sinne von `hg_kerve.md`.
  - **Stirnseite** (`stirnseite`): die geometrische Endfläche
    am Bauteilendpunkt (Bauteilfläche, `begriffstyp:
    generisch`). Eine Stirnseite ist das **Resultat** eines
    Anschnitts, **nicht** der Anschnitt selbst. Der Anschnitt
    ist die Bearbeitung mit eigener UUID, Anschnittseite und
    Anschnittebene; die Stirnseite ist die abgeleitete
    Resultat-Sicht ohne eigene UUID.
  - **Bearbeitung** (`bearbeitung`): Oberbegriff. Der Anschnitt
    ist ein Bearbeitungs-Subtyp neben Kerve, Bohrung, Versatz,
    Zapfenloch, Schlitz, Blatt, Kamm und Fase.
  - **Senkel** (`senkel`): Lage-Prädikat über Ebenen (parallel
    zur Welt-Lotachse). Eine Anschnittebene **kann** ein Senkel
    sein (Senkelschnitt am Sparrenfuß), muss aber nicht. Senkel
    ist eine Klassifikation der Anschnittebene, keine
    Bearbeitung.
  - **Bleischnitt** (`bleischnitt`): Lage-Prädikat über Ebenen
    (rechtwinklig zur Welt-Lotachse). Eine Anschnittebene
    **kann** ein Bleischnitt sein (Bleischnitt am Sparrenfuß),
    muss aber nicht. Bleischnitt ist eine Klassifikation der
    Anschnittebene, keine Bearbeitung.
  - **Schmiege** (`schmiege`, Folgearbeit): Anschnitt-
    Spezialisierung an einer Schifter-Grat-/Kehl-Verschneidung
    mit zusätzlicher Bezugsrolle. Schmiege ist ein engerer
    Begriff als Anschnitt (jede Schmiege ist ein Anschnitt;
    nicht jeder Anschnitt ist eine Schmiege).
  - **Hexenschnitt** (`hexenschnitt`, Folgearbeit):
    Doppelanschnitt am Traufendpunkt von Grat-/Kehlsparren.
    Hexenschnitt ist ein **Verbund** zweier Anschnitt-
    Instanzen, keine einzelne Anschnitt-Bearbeitung im Sinne
    dieses Eintrags.
  - **Versatz** (`versatz`, Folgearbeit): stirnseitige
    Materialwegnahme zur Lastübertragung (Stirnversatz,
    Fersenversatz) am Sparren- oder Strebenfuß, mit
    zusätzlicher Versatztiefe-Geometrie und Lastübertragungs-
    Funktion. Versatz ist **nicht** Anschnitt; ein Versatz
    kann eine Anschnitt-ähnliche Schnittfläche enthalten, ist
    aber eine eigenständige Bearbeitung mit Versatz-Tiefe als
    Zusatzparameter.
  - **Fase** (`fase`, Folgearbeit): kleinflächige Kanten-
    Abschrägung an einer Bauteilkante, keine Endschnittebene.
    Eine Fase ist nicht Anschnitt.
  - **Querschnitt** (`querschnitt`): Schnittfigur an einer
    Stelle s ∈ [0, L] **rechtwinklig** zur Bauteilachse.
    Anschnitt-Stirnseiten sind im Sinne von `hg_querschnitt.md`
    **kein** Querschnitt (siehe `hg_stirnseite.md`,
    Wohldefiniertheits-Block).
  - **Bauteilachse** (`bauteilachse`): Bezugsachse, gegen die
    der Anschnittwinkel α_AS gemessen wird. Anschnitt ist nicht
    die Bauteilachse, sondern eine Bearbeitung am Endpunkt der
    Achse.

## Implementierungshinweis

Datentyp (Domänen-Schicht, Kotlin, Schicht
`domain.bauteil.bearbeitung`):

```kotlin
package domain.bauteil.bearbeitung

import domain.bauteil.flaeche.Endposition
import domain.geometrie.Ebene
import domain.geometrie.LokalePlatzierung
import java.util.UUID

/**
 * Anschnitt: subtraktive Bearbeitung am Bauteilendpunkt durch
 * eine einzige Anschnittebene; erzeugt eine geneigte Stirnseite
 * mit Anschnittwinkel α_AS ∈ (ε_W, π/2 − ε_W).
 *
 * Glossar: hg_anschnitt.md
 *
 * Modelliert im Erstentwurfs-Umfang ausschliesslich den
 * einfachen Endanschnitt (BTLx `JackRafterCut`). Längsanschnitt
 * (`LongitudinalCut`), Doppelanschnitt (`DoubleCut`), Schmiege
 * und Hexenschnitt sind Folgearbeiten mit eigenen
 * Bearbeitungs-Subtypen.
 *
 * Vorzeichenkonvention der Anschnittebenen-Normalen: zeigt aus
 * dem Bauteil heraus, d. h. ⟨n̂_AS, d̂_σ⟩ > 0 mit d̂_σ als
 * nach aussen gerichteter Bauteilachsen-Tangente an der
 * Anschnittseite.
 */
data class Anschnitt(
    override val uuid: UUID,
    val anschnittseite: Endposition,         // ANFANG | ENDE
    val anschnittebene: Ebene,               // E_AS, n̂_AS unter (3)
    override val lokalePlatzierung: LokalePlatzierung,
    override val bezeichnung: String? = null,
) : Bearbeitung
```

- **Einheit**: Punktkoordinaten in mm; Anschnittebene als
  Hesse-Normalform mit Einheits-Normaler.
- **Identität**: `uuid` ist Pflicht und persistent (RFC 9562
  v7, geerbt von `bearbeitung`), unabhängig vom zugeordneten
  Bauteil. Keine Backref auf das Bauteil (partitive Komposition,
  siehe `hg_bearbeitung.md`).
- **Pflicht- und Optionalfelder**:
  - `uuid` — Pflicht, niemals null.
  - `anschnittseite` — Pflicht; `Endposition.ANFANG` oder
    `Endposition.ENDE` (gemeinsame Enum-Konvention mit
    `Stirnseite`, siehe `hg_stirnseite.md` Implementierungs-
    hinweis).
  - `anschnittebene` — Pflicht; Hesse-Normalform mit
    Einheitsnormaler unter Vorzeichenkonvention (3).
  - `lokalePlatzierung` — Pflicht; in der Standard-Konvention
    `LokalePlatzierung.IDENTITAET` (Werkzeug-Bezugssystem
    direkt im Bauteil-Lokal-System).
  - `bezeichnung` — `null` zulässig.
- **Invarianten** (in Companion-Factory
  `Anschnitt.aus(bauteil, anschnittseite, anschnittebene)`,
  `Resultat.Fehler` bei Verletzung; niemals Exception):
  1. `anschnittebene.normaleEinheit()` ist normiert
     (`‖n̂_AS‖² ≈ 1` innerhalb `Toleranzen.NORM_EPS`).
  2. **Inzidenz**: der zugehörige Bauteil-Endpunkt p_σ
     (`p_a` bei ANFANG, `p_e` bei ENDE) liegt auf der
     Anschnittebene (`|⟨n̂_AS, p_σ − stützpunkt⟩| ≤
     Toleranzen.LAENGE_EPS`).
  3. **Aussennormale-Konvention** (3):
     `⟨n̂_AS, d̂_σ⟩ > 0` mit `d̂_σ` als nach aussen
     gerichteter Tangente an der Anschnittseite.
  4. **Anschnittwinkel-Wertebereich**: `α_AS ∈ (ε_W, π/2 −
     ε_W)`. α_AS = π/2 (rechtwinkliger Endschnitt) oder
     α_AS → 0 (tangentialer Anschnitt) sind unzulässig.
     `Resultat.Fehler`-Variante:
     `AnschnittwinkelAusserhalbZulaessigemBereich`.
  5. **Anschnittebene-Bauteil-Inzidenz** (analog
     `hg_bearbeitung.md` Edge Case): die Anschnittebene muss
     den Bauteilkörper am Endpunkt schneiden;
     `Resultat.Fehler`-Variante:
     `AnschnittebeneAusserhalbBauteil`.
- **Konstruktion**: Anschnitt wird über die Companion-Factory
  `Anschnitt.aus(bauteil, anschnittseite, anschnittebene)`
  oder die Convenience-Funktion
  `Bauteil.fuegeAnschnittHinzu(anschnittseite, anschnittebene)`
  erzeugt; nicht über einen freien Konstruktor (die
  Bauteil-Inzidenz-Invarianten verlangen Kenntnis des
  Bauteils).
- **Werkzeugkörper** (abgeleitete Eigenschaft, Geometrie-
  Schicht, Phase 3.2):
  `werkzeugkoerper(): Polyeder` realisiert
  `K_Anschnitt(p_τ) = H_+(E_AS) ∩ 𝓡` mit der App-Konvention
  für 𝓡 (axenparallele Bounding-Box um den Bauteilkörper am
  Endpunkt mit `LAENGE_EPS`-Sicherheitsabstand). Die konkrete
  Polyeder-Repräsentation ist Aufgabe des
  `BearbeitungsAggregator`, siehe `hg_bearbeitung.md`.
- **Resultat-Stirnseite** (abgeleitete Eigenschaft):
  `resultatStirnseite(bauteil: Bauteil): Stirnseite` erzeugt
  die Stirnseite nach (7) — Trägerebene = `anschnittebene`,
  `position = anschnittseite`, `aussennormale =
  anschnittebene.normaleEinheit()`, `bezugspunkt = p_σ`,
  `berandung` = Schnittpolygon der Anschnittebene mit dem
  bearbeiteten Bauteilkörper.
- **BTLx-Export** (Persistenzschicht, Phase 4):
  - **Primäres Mapping**: `JackRafterCut` mit Parametern
    `Orientation` (ANFANG/ENDE), `StartX`/`StartY`
    (Anschnittpunkt auf der Bezugsfläche), `Angle` und
    `Inclination` (aus der Anschnittebenen-Normalen relativ
    zur BTLx-Referenzebene berechnet).
  - **Nicht im Erstentwurfs-Umfang**: `LongitudinalCut`
    (Folgearbeit `laengsanschnitt`), `DoubleCut`
    (Folgearbeit `schmiege` bzw. `hexenschnitt`),
    `TriangleCut` (Sonderfall, ggf. Folgearbeit).
- **IFC-Export** (Persistenzschicht, Phase 4):
  - Anschnitt wird als `IfcOpeningElement` mit eigener
    `GlobalId` (= Bearbeitungs-UUID) angelegt; die Beziehung
    zum Bauteil läuft über `IfcRelVoidsElement` (siehe
    `hg_bearbeitung.md` IFC-Mapping).
- **Edge Cases**:
  - **Anschnitt mit α_AS exakt π/2**: ausgeschlossen
    durch Invariante (4). Wer das Bauteilende rechtwinklig
    geschnitten haben möchte, modelliert **keinen** Anschnitt
    (das ist der prismatische Standardfall, siehe
    `hg_stirnseite.md`).
  - **Mehrere Anschnitte am selben Bauteilendpunkt**
    (Doppelanschnitt-Sonderfall, Folgearbeit
    `hexenschnitt`/`schmiege`): zulässig als zwei separate
    `Anschnitt`-Instanzen mit derselben `anschnittseite`,
    aber unterschiedlichen `anschnittebene`. Die App führt
    sie als unabhängige Bearbeitungen mit eigenen UUIDs; die
    Wirkung kombiniert sich nach `hg_bearbeitung.md` (2).
  - **Anschnitt + Kerve am selben Bauteilende**: zulässig
    und im Korpus üblich (Sparrenfuß mit Klauenkerve und
    Stirnanschnitt unterhalb der Kerve). Beide Bearbeitungen
    sind unabhängig; ihre Wirkungen kombinieren sich
    reihenfolge-invariant.
  - **Anschnitt an einem Bauteil mit Faserrichtung-Modus
    SCHWACH oder KEINE** (z. B. OSB, Spanplatte): zulässig;
    die Anschnitt-Geometrie ist von der Faserrichtung
    unabhängig. Plattenwerkstoffe werden bevorzugt nicht mit
    `Anschnitt` modelliert, sondern als Plattenbauteile mit
    Plattenkante (Folgearbeit, siehe `hg_stirnseite.md`).
  - **Numerisch flacher Anschnitt** (α_AS nahe ε_W): Invariante
    (4) lehnt unzulässige Werte ab; im zulässigen, aber
    praxisuntypischen Korridor (α_AS < π/12) gibt die
    Bemessungs-Schicht eine Warnung aus (weiche Invariante).
- **Bezeichner-Konvention** (CLAUDE.md): Klasse heisst
  `Anschnitt` (deutsch, Glossarbegriff). `Endposition.ANFANG`/
  `Endposition.ENDE` werden mit `Stirnseite` geteilt
  (gemeinsame Konvention).

**Folgearbeit (trigger-basiert):**

- **`schmiege`** (Anschnitt-Spezialisierung an Schifter-Grat-/
  Kehl-Verschneidung mit Anfallflächen-Bezugsrolle; drei
  Sub-Spezialisierungen Fußschmiege, Lotschmiege/
  Senkelschmiege, Backenschmiege). Trigger: erstes
  Walmdach-Tool mit Schiftern (Memory
  `project_grobplan_erstes_tool`, nach D7/D8).
- **`hexenschnitt`** (Doppelanschnitt am Traufendpunkt eines
  Grat- oder Kehlsparrens). Trigger: Walmdach-Tool mit
  Dachkasten-Detail.
- **`laengsanschnitt`** (Anschnitt mitten am Bauteil in
  Bauteil-Längsrichtung, BTLx `LongitudinalCut`). Trigger:
  erstes Tool mit Sparrenverbreiterung oder Längsverjüngung.
- **`schiftung`** (Verfahren zur Bestimmung der
  Anschnittwinkel an Schiftern, Subglossar-Sektion bei
  `anschnitt` für Lehrlingsstufe / Geselle). Trigger:
  TG-4-Subglossar-Anlage zu diesem Eintrag.
- **Cross-Verweis-Einlösung in `hg_senkel.md` und
  `hg_bleischnitt.md`**: deren Folgearbeit-Blöcke nennen
  „Cross-Verweis in `hg_sparren.md` bei Anlage des
  `anschnitt.md`-Eintrags" als Trigger. Trigger ist mit
  Anlage dieses Eintrags eingetreten; die Cross-Verweise
  werden im jeweils nächsten Etappenschritt in
  `hg_sparren.md` nachgezogen.

## Quellen

**Primär (normativ):**

- DIN EN 1995-1-1:2010-12, „Eurocode 5: Bemessung und
  Konstruktion von Holzbauten – Teil 1-1: Allgemeines –
  Allgemeine Regeln und Regeln für den Hochbau", Abschnitte
  5.2 und 6.5.
- design2machine: *BTLx interface description*, Version 2.1,
  16.11.2023, Abschnitt „List of Processings", Einträge
  `JackRafterCut`, `LongitudinalCut`, `DoubleCut`,
  `TriangleCut`.
- DIN 1052:2008-12, „Entwurf, Berechnung und Bemessung von
  Holzbauwerken", Abschnitt 12 (Konstruktive Anforderungen).
- SIA 265:2021, „Holzbau", Schweizerischer Ingenieur- und
  Architektenverein, Zürich, Abschnitt 5 (Konstruktive
  Durchbildung).

**Sekundär:**

- Mönck, W.; Rug, W.: *Holzbau – Bemessung und Konstruktion.*
  16. Auflage, Beuth, Berlin 2015, Kap. 11 „Dachtragwerke".
- Gerner, M.: *Fachwerk – Instandsetzung, Sanierung, Neubau.*
  DVA, 7. Auflage 2007, Glossar.
- Natterer, J.; Herzog, T.; Volz, M.: *Holzbau-Atlas.*
  4. Auflage, Birkhäuser, Basel 2003, Kap. „Dachtragwerke".
- Lignum (Hrsg.): *Holzbautabellen HBT.* Lignum, Zürich,
  aktuelle Auflage, Kap. „Sparrenanschlüsse" und „Austragen".
- Eurotec: *Anfängerlehrbuch Teil 3.3 Holzverbindungen.*

**Korpus (nicht autoritativ):**

- Wikipedia, Lemma „Schiftung" (abgerufen 2026-05-14):
  enthält die XO/XU-Notation für Anschnitt im engeren
  Schiftungs-Kontext.
- Wikipedia, Lemma „Hexenschnitt" (abgerufen 2026-05-14):
  Hexenschnitt als Doppelanschnitt am Trauf-Endpunkt von
  Grat-/Kehlsparren.
- Wikipedia, Lemma „Schmiege" (abgerufen 2026-05-14):
  Schmiege als schräge Anschlussfläche im Holzbau.
- Lueger, *Lexikon der gesamten Technik* (1904), Lemma
  „Schmiegen": drei Schmiege-Arten (Fußschmiege, Lotschmiege,
  Backenschmiege).
- polybau.ch: Unterrichtsmaterial *Sparrenverbindungen*,
  *Hexenschnitt* (Titel-Bestätigung).
- zimmerer-treff.com: *Schräge Sparren, schräge Schifter*,
  *Hexenschnitt*.
- compas_timber-API (Gramazio Kohler Research):
  *BTLx Fabrication Module* (Klassen-Liste).
- Recherchebericht: `docs/recherche/2026-05-14_hg_anschnitt.md`.
