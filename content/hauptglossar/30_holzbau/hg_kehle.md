---
id: kehle
benennung: Kehle
kurz: "Eine Kehle ist die geneigte, nach innen springende Dachkante, in der zwei Dachflächen wie eine Rinne zusammenlaufen und in der sich das Regenwasser beider Flächen sammelt."
synonyme: [Kehlkante, Kehllinie, Ixe]
abgelehnte_benennungen: [Kehlblech, Kehlbohle, Kehlsparren, "valley", "valley line"]
oberbegriff: dachkante
begriffstyp: partitiv
voraussetzungen: [strecke, dachflaeche, polygon, ebene, vektor, toleranzen, dachkante]
abgrenzung_zu: [traufe, first, ortgang, grat, pultkante, kehlblech, kehlbohle, kehlsparren]
status: entwurf
subglossar_pendant: notwendig
quellen_primär:
  - "SIA 232/1:2020 'Geneigte Dächer', Schweizerischer Ingenieur- und Architektenverein, Abschnitt 1 (Begriffe): Kehle als geneigte, einspringende Schnittkante zweier Dachflächen mit besonderer Bedeutung für die Wasserführung."
  - "DIN 1356-1:1995-02 'Bauzeichnungen – Teil 1', Abschnitt 5 (Darstellung von Dächern): Kehle als geneigte Dachkante an einer einspringenden Ecke zweier zusammentreffender Dachflächen."
  - "DIN 18338:2019-09 'VOB Teil C: ATV Dachdeckungsarbeiten' (Titel seit 2019 ohne Abdichtungs-Teil, dieser in DIN 18336; die ATV führt keine Begriffs-Sektion — Abschnitt 0 sind Hinweise für das Aufstellen der Leistungsbeschreibung, die Dachkanten-Begriffe werden vorausgesetzt und nach Längenmaß abgerechnet), vorausgesetzte Lesart: Kehle als geneigte Schnittlinie zweier nach innen einspringender Dachflächen, in der das Niederschlagswasser konzentriert abläuft."
quellen_sekundär:
  - "Bläsi, W.; Ferdinand, S.: Tabellenbuch Zimmerer. 9. Aufl., Bildungsverlag EINS (Westermann Gruppe), Köln 2021, ISBN 978-3-427-02144-5, Kap. 3.9.9 'Dachteile und ihre Begriffe', S. 173: Positionstafel am axonometrischen Dachmodell führt die Kehle an zwei Positionen (⑩, ⑪) als eigene Dachteil-Kante, neben ① First, ⑥/⑬ Grat und ⑦/⑧ Traufe. Einer von nur zwei Fundorten im Werk, an denen die Kehle als Linie (und nicht als Kehlsparren) benannt ist — Berufsschul-Kanon der Dachanatomie."
  - "Bläsi, W.; Ferdinand, S.: Tabellenbuch Zimmerer. 9. Aufl., Bildungsverlag EINS (Westermann Gruppe), Köln 2021, ISBN 978-3-427-02144-5, Kap. 8 'Vergabe- und Vertragsordnung für Bauleistungen (VOB)', S. 271, Block 'Dachdeckungs- und Dachabdichtungsarbeiten nach VOB, DIN 18338': Abrechnung nach Längenmaß (m) 'getrennt nach Bauart und Maßen für: Deckungen oder Abdichtungen von Firsten, Graten, Kehlen, Ortgängen und dgl.' — gegenüber Abrechnung nach Flächenmaß (m²) für 'Dachdeckungen, Dachabdichtungen …'. Die Aufmaß-Systematik weist die Kehle (wie First, Grat, Ortgang) als linienhaftes, nicht flächenhaftes Dachteil aus und stützt damit die Führung als Dachkante. Ausführungsseitig ferner: 'Kehlen sind als unterlegte Drei-Pfannen-Kehlen herzustellen' bzw. 'als untergelegte Metallkehlen'."
  - "Mönck, W.; Rug, W.: Holzbau – Bemessung und Konstruktion. 16. Aufl., Beuth Verlag 2015, Kap. Dachformen (Verschneidungen, Gauben)."
  - "Gerner, M.: Fachwerk – Instandsetzung, Sanierung, Neubau. DVA, 7. Aufl. 2007, Glossar 'Kehle'."
  - "Lignum (Hrsg.): Lignatec 'Geneigte Dächer in Holzbauweise', Lignum, Zürich, aktuelle Auflage."
quellenkonflikt: |
  Im Sprachgebrauch existieren mehrere Lesarten von „Kehle":
  (a) **geometrisch**: Kehle = Kehlkante, also die geneigte konkave
      Schnittkante zweier Dachflächen.
  (b) **Bauteil Eindeckung**: Kehlblech / Kehlrinne = die in der Kehle
      eingelegte wasserführende Blechabdeckung.
  (c) **Bauteil Tragwerk**: Kehlsparren / Kehlbohle = der unter der
      Kehlkante verlaufende Tragwerksbalken.
  Normativ ist (a) belegt (SIA 232/1, DIN 1356, DIN 18338).
  **Festlegung dieses Glossars**: Kehle bezeichnet hier ausschließlich
  die geometrische **Kehlkante** im Sinne (a). Die Bauteile
  **Kehlblech**, **Kehlbohle**, **Kehlsparren** werden in
  `abgrenzung_zu` ausdrücklich abgegrenzt.

  Regionale Synonyme: „Ixe" ist im süddeutschen und schweizerischen
  Sprachraum für die Kehlkante geläufig; es wird hier als Synonym
  geführt, jedoch nicht als Hauptbenennung verwendet.

  Abgrenzung zu **First** und **Grat**: First, Grat und Kehle sind
  alle Schnittkanten zweier Dachflächen. Der First ist näherungsweise
  horizontal; Grat und Kehle sind geneigt. Grat und Kehle wiederum
  unterscheiden sich durch die Konvexität der Geometrie:
  - **Grat**: konvex/ausspringend (Außenecke).
  - **Kehle**: konkav/einspringend (Innenecke).
  Die mathematische Schärfung der qualitativen Begriffe „ausspringend"
  / „einspringend" über die **Querlage der Flächenstücke** (Bedingung
  (2), wie in `hg_grat.md` mit umgekehrtem Vorzeichen) ist eigene
  Festlegung; sie ist konsistent mit allen
  konsultierten Quellen, die nur die qualitativen Begriffe verwenden.

  Klassifikation: Eine Kante einer Dachflächenfamilie soll genau einer
  der sechs Klassen (Traufe, First, Ortgang, Grat, Kehle, Pultkante)
  zugeordnet werden — siehe `hg_dachkante.md`. Kehle ist disjunkt zu
  First (durch Neigungsbedingung) und disjunkt zu Grat (durch
  Konkavitätsbedingung mit umgekehrtem Vorzeichen).

  Bestätigung und Negativ-Befund im Tabellenbuch Zimmerer
  (Bläsi/Ferdinand, 9. Aufl. 2021; Volltext-Scan liegt Anweiser vor,
  direkt eingesehen 2026-08-14, OCR-Sweep über alle 333 Seiten):
  Das Berufsschul-Standardwerk kennt die Kehle als Dachteil-Kante
  nur an **zwei** Stellen — in der Positionstafel „Dachteile und
  ihre Begriffe" (S. 173, Positionen ⑩ und ⑪) und in der
  VOB-Aufmaß-Systematik nach DIN 18338 (S. 271, „Firsten, Graten,
  Kehlen, Ortgängen" unter Abrechnung nach Längenmaß). In den
  gesamten Abbund- und Dachausmittlungs-Kapiteln (Kap. 1.13,
  S. 24–33; Kap. 10.16/10.20, S. 305–324) wird die Kehle
  **ausschließlich über das Bauteil `kehlsparren`** angesprochen
  („Länge des Kehlsparrens k", Legenden S. 25/32; „Verlauf der
  Grat- und Kehlsparren", S. 307; „First, Grat, Kehlsparren im
  Grundriss", S. 305) — die geometrische Kehllinie selbst trägt
  dort keinen eigenen Namen.

  Zwei Folgerungen: (1) Der Negativ-Befund verschärft die im
  Quellenkonflikt beschriebene Praxis-Drift (c) — im
  Praktiker-Korpus verdrängt das Bauteil den Kantenbegriff
  weitgehend, was die Aufnahme von „Kehlsparren" in
  `abgelehnte_benennungen:` rechtfertigt. (2) Das Werk stützt keine
  der regionalen Synonym-Varianten: weder „Kehllinie" noch
  „Kehlkante" noch „Ixe" erscheinen im OCR-Volltext
  (OCR-basierter Negativ-Befund, Sweep 2026-08-14; die
  OCR-Zuverlässigkeit ist bei Fließtext hoch, bei
  Bildbeschriftungen eingeschränkt). Das bestätigt „Kehle" als
  Hauptbenennung, entwertet aber die anderweitig belegten
  Synonyme nicht.
---

## Prosa-Definition

Eine **Kehle** ist eine Dachkante, die als Schnittkante zweier
benachbarter Dachflächen auf der Schnittgerade ihrer Trägerebenen
liegt, gegenüber der Horizontalen geneigt verläuft (also nicht
näherungsweise horizontal ist) und an einer einspringenden Innenecke
des Daches die beiden anliegenden Dachflächen so zusammenführt, dass
ihre äußeren Normalen in einen **gemeinsamen oberen Halbraum**
weisen (konkave Konfiguration), wodurch in der Kehle das von beiden
Dachflächen abfließende Niederschlagswasser zusammenläuft.

## Mathematische Definition

Sei

- D_i = (E_i, P_i, n_{a,i}) und D_j = (E_j, P_j, n_{a,j}) zwei
  verschiedene Dachflächen im Sinne von `dachflaeche` mit i ≠ j,
- E_i und E_j nicht parallel, also E_i ∩ E_j eine Gerade
  g_{ij} ⊂ ℝ³ (Schnittgerade der Trägerebenen),
- F(P_i) ⊂ E_i und F(P_j) ⊂ E_j die berandeten abgeschlossenen
  Flächenstücke,
- s_{ij}:= F(P_i) ∩ F(P_j) die gemeinsame Schnittstrecke (vgl.
  `first`),
- e_z = (0, 0, 1)ᵀ die vertikale Achse,
- ε_W:= Toleranzen.WINKEL_EPS die Winkeltoleranz,
- ε_L:= Toleranzen.LAENGE_EPS die Längentoleranz.

Sei ℓ(s_{ij}) > ε_L und t_hat der Einheits-Tangentenvektor von s_{ij},
mit der Konvention ⟨t_hat, e_z⟩ > 0 (Tangente nach oben orientiert; vgl.
`grat`).

Eine Schnittstrecke s_{ij} heißt **geneigt**, wenn

```text
|⟨t_hat, e_z⟩| > ε_W                                            (1)
```

(d. h. t_hat ist nicht näherungsweise horizontal — diese Bedingung grenzt
Kehle und Grat gemeinsam vom First ab).

Zur Schärfung von **konvex/konkav** genügen die beiden äußeren Normalen
allein **nicht**: Ein Grat und eine Kehle können dasselbe Normalenpaar
besitzen und unterscheiden sich nur darin, auf welcher Seite der Kante
das jeweilige Flächenstück liegt (Gegenbeispiel in der Erläuterung zu
`hg_grat.md`). Die Konkavität wird darum über die **Lage der
Flächenstücke relativ zur Kante** bestimmt — wie in `hg_grat.md`, mit
umgekehrtem Vorzeichen. Sei

```text
w:= (t_hat × e_z) / ‖t_hat × e_z‖   ∈ S²
```

die zur Kantentangente orthogonale **horizontale** Querachse
(wohldefiniert, solange die Kante nicht lotrecht ist, also
‖t_hat × e_z‖ > ε_L). Sei c_i ein innerer Punkt (Flächenschwerpunkt)
von F(P_i) und m ∈ s_{ij} ein Kantenpunkt; die **signierte Querlage**
des Flächenstücks D_i ist τ_i:= ⟨c_i − m, w⟩ (mit τ_i · τ_j < 0).
Eine geneigte Schnittstrecke s_{ij} heißt **konkav** (einspringend,
Kehle), wenn sich **beide** äußeren Normalen horizontal zur
**Gegenseite** ihres eigenen Flächenstücks neigen:

```text
⟨ n_hat_{a,i}, w ⟩ · sign(τ_i) < −ε_W   und
⟨ n_hat_{a,j}, w ⟩ · sign(τ_j) < −ε_W.                                 (2)
```

Anschaulich: Jede äußere Normale „kippt" horizontal **entgegen** der
Erstreckungsrichtung ihres eigenen Flächenstücks, weist also nach innen,
zur Kehle hin (Innenecke). Beim **Grat** ist das Vorzeichen umgekehrt
(⟨n_hat_{a,i}, w⟩ · sign(τ_i) > ε_W, nach außen). Die Bedingung (2) ist
**pro Flächenstück** formuliert und damit unmittelbar unabhängig von der
Reihenfolge der beiden Dachflächen; eine reine Normalen-Bedingung
⟨n_hat_{a,i} × n_hat_{a,j}, t_hat⟩ kann Grat und Kehle nicht trennen.

Eine Schnittstrecke s_{ij} heißt **Kehle** der Dachflächenfamilie 𝒟
genau dann, wenn

1. ℓ(s_{ij}) > ε_L (nicht-entartet),
2. s_{ij} ist **geneigt** im Sinne von (1),
3. s_{ij} ist **konkav** im Sinne von (2),
4. beide äußeren Normalen weisen in die obere Halbkugel:
   ⟨n_hat_{a,i}, e_z⟩ > 0 und ⟨n_hat_{a,j}, e_z⟩ > 0 (Ausschluss
   senkrechter Wände).

Die Vereinigung aller so identifizierten Schnittstrecken bildet,
falls sie über gemeinsame Eckpunkte zusammenhängt, die **Kehllinie**
als Streckenzug; im Regelfall (Verschneidung Hauptdach × Gaube,
Verschneidung zweier Sattel­dächer mit T-Grundriss) besteht sie aus
einer oder zwei Strecken pro einspringender Ecke.

## Wohldefiniertheit

- **Existenz der Tangente**: Wegen ℓ(s_{ij}) > ε_L ist t_hat
  wohldefiniert. Die Konvention ⟨t_hat, e_z⟩ > 0 ist wegen (1) erfüllbar
  und legt die Orientierung eindeutig fest.
- **Unabhängigkeit von der Indexreihenfolge**: Bedingung (2) ist pro
  Flächenstück formuliert (je eine Ungleichung für i und für j); ein
  Vertauschen i ↔ j benennt nur die beiden Ungleichungen um.
- **Unabhängigkeit von der Punktwahl**: t_hat ist auf der ganzen
  Strecke konstant; die Bedingungen (1) und (2) sind punktunabhängig.
- **Disjunktheit zu First**: First verlangt |⟨t_hat, e_z⟩| ≤ ε_W;
  Kehle verlangt |⟨t_hat, e_z⟩| > ε_W.
- **Disjunktheit zu Grat**: Grat verlangt ⟨n_hat_{a,i}, w⟩ · sign(τ_i)
  > +ε_W (konvex, nach außen), Kehle verlangt < −ε_W (konkav, nach
  innen). Dazwischen liegt das Toleranzband [−ε_W, +ε_W], das als
  Entartung klassifiziert wird (`Entartet.NichtIdentifizierbar`); eine
  **gemischte** Kante (ein Flächenstück nach außen, das andere nach
  innen geneigt) erfüllt weder Grat noch Kehle.
- **Konsistenz mit `dachkante`**: Eine Kehle ist nach Konstruktion
  eine Schnittkante zweier Dachflächen, also eine Dachkante (Fall
  „Schnittkante").
- **Nicht-Zirkularität**: Die Definition stützt sich nur auf
  `strecke`, `dachflaeche`, `polygon`, `ebene`, `vektor`,
  `toleranzen` und den Oberbegriff `dachkante`.

## Erläuterung (nicht normativ)

Die Kehle ist die geneigte „Innenkante" zweier Dachflächen an einem
einspringenden Eck. Sie tritt typischerweise dort auf, wo zwei
Dachvolumina sich verschneiden — etwa beim T-förmigen Anbau eines
Satteldachs an ein anderes Satteldach, oder bei der Verschneidung
einer Satteldachgaube mit einer Hauptdachfläche. An solchen Stellen
fließt das Wasser beider Dachflächen in der Kehlinie zusammen; sie
ist daher konstruktiv besonders relevant.

Konstruktiv liegt in der Kehle üblicherweise ein **Kehlblech**
(metallene Kehlrinne, von der Eindeckung überdeckt) oder eine
**Kehlbohle** (Holzbohle als Unterkonstruktion); unter der Kehlinie
verläuft im Tragwerk häufig ein **Kehlsparren**. Diese Bauteile sind
nicht Bestandteil der geometrischen Kehlkante.

Warum die Normalen allein nicht genügen: Ein Grat (Λ, beide Flächen
fallen von der Kante weg) und eine Kehle (V, beide steigen weg) besitzen
**dasselbe Paar äußerer Normalen** und unterscheiden sich nur in der
Querlage der Flächenstücke (Gegenbeispiel und Begründung in der
Erläuterung zu `hg_grat.md`). An der **Kehle** zeigt jede äußere Normale
horizontal zur **Gegenseite** ihres eigenen Flächenstücks — zur Kehlinie
hin; die Geometrie öffnet sich nach oben wie eine Rinne, in der das
Wasser zusammenläuft. Beim Grat zeigt jede Normale nach außen, die
Geometrie öffnet sich nach unten. Die Winkelhalbierende der Normalen
taugt zur Unterscheidung nicht: bei symmetrischer Neigung weist sie an
Grat und Kehle gleichermaßen senkrecht nach oben.

Regional ist die Bezeichnung „Ixe" (auch „Ix") in der Schweiz und
Süddeutschland für die Kehlinie geläufig und insbesondere bei der
Aufrissdarstellung des Dachs gebräuchlich.

## Beziehungen

- **Oberbegriff**: `dachkante`, Spezialfall „Schnittkante" mit
  zusätzlichen Lagebedingungen (geneigt, konkav, beide Normalen mit
  positiver z-Komponente).
- **Geschwister-Begriffe** (andere Spezialisierungen von
  `dachkante`): `traufe`, `first`, `ortgang`, `grat`, `pultkante`.
- **Bestandteile (partitiv)**: Anfangspunkt und Endpunkt der
  Kehllinien-Strecke; im Regelfall ist der untere Endpunkt zugleich
  Eckpunkt zweier Trauflinien (Trauf-Innenecke) und der obere
  Endpunkt zugleich Eckpunkt einer Firstlinie oder eines Grats.
- **Abgrenzung**:
    - **First** (`first`): horizontale Schnittkante zweier nach oben
    zusammenlaufender Dachflächen. Kehle ist im Gegensatz dazu
    geneigt (Bedingung (1)).
    - **Grat** (`grat`): geneigte konvexe Schnittkante. Kehle ist
    konkav; Vorzeichen in (2) umgekehrt zum Grat.
    - **Ortgang** (`ortgang`): geneigte Randkante einer einzelnen
    Dachfläche entlang ihrer Falllinie. Kehle ist Schnittkante
    zweier Dachflächen.
    - **Traufe** (`traufe`): horizontale, untere Randkante.
    - **Pultkante** (`pultkante`): obere Randkante einer einzelnen
    Pultdachfläche.
    - **Kehlblech / Kehlrinne**: Eindeckungs-Bauteil zur
    Wasserführung in der Kehle; nicht die Kante selbst. Hier nicht
    definiert.
    - **Kehlbohle**: Holz-Bauteil als Unterlage des Kehlblechs;
    Bauteil, nicht Kante. Hier nicht definiert.
    - **Kehlsparren** (`kehlsparren`, bereits angelegt):
    Tragwerksbalken unter der Kehlkante; Bauteil, nicht Kante.

## Quellen

**Primär (normativ):**

- SIA 232/1:2020, „Geneigte Dächer", Schweizerischer Ingenieur- und
  Architektenverein, Abschnitt 1.
- DIN 1356-1:1995-02, „Bauzeichnungen – Teil 1: Arten, Inhalte und
  Grundregeln der Darstellung", Abschnitt 5.
- DIN 18338:2019-09, „VOB Teil C: ATV Dachdeckungsarbeiten"
  (Titel seit 2019 ohne Abdichtungs-Teil, dieser in DIN 18336),
  Abschnitt 0 (Hinweise für das Aufstellen der Leistungsbeschreibung).

**Sekundär:**

- Bläsi, W.; Ferdinand, S.: *Tabellenbuch Zimmerer.* 9. Auflage,
  Bildungsverlag EINS (Westermann Gruppe), Köln 2021,
  ISBN 978-3-427-02144-5. Kap. 3.9.9 „Dachteile und ihre Begriffe"
  (S. 173, Positionen ⑩/⑪ Kehle) und Kap. 8, S. 271
  („Dachdeckungs- und Dachabdichtungsarbeiten nach VOB,
  DIN 18338": Kehlen unter Abrechnung nach Längenmaß). Zugleich
  Negativ-Befund für die Abbund- und Dachausmittlungs-Kapitel
  (S. 24–33, 305–324), die die Kehle nur über den Kehlsparren
  ansprechen — siehe `quellenkonflikt:`. Volltext-Scan liegt Anweiser
  vor; direkt eingesehen 2026-08-14 (seitenweise am Scan-PNG
  verifiziert).
- Mönck, W.; Rug, W.: *Holzbau – Bemessung und Konstruktion.*
  15. Auflage, Beuth Verlag 2015.
- Gerner, M.: *Fachwerk – Instandsetzung, Sanierung, Neubau.* DVA,
  7. Auflage 2007.
- Lignum (Hrsg.): *Lignatec — Geneigte Dächer in Holzbauweise.*
  Lignum, Zürich, aktuelle Auflage.

**Korpus (nicht autoritativ):**

- Wikipedia, Lemma „Dachkehle" (abgerufen 2026-05-08).
