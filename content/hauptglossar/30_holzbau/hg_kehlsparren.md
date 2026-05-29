---
id: kehlsparren
benennung: Kehlsparren
synonyme: [Kehl-Sparren]
abgelehnte_benennungen:
  [Verschneidungssparren, Walmsparren, Ixe, "valley rafter", "valley"]
oberbegriff: sparren
begriffstyp: bauteilrolle
voraussetzungen:
  [bauteil, bauteilachse, sparren, kehle, dachflaeche, strecke,
   einheitsvektor, ebene, dachneigung, weltkoordinatensystem,
   toleranzen]
abgrenzung_zu:
  [sparren, gratsparren, schifter, kehle, kehlbohle, kehlblech,
   kehlbalken, dachflaeche, dachseite, firstpfette, fusspfette,
   kerve, abkehlung, abgratung, verschneidungssparren, schiftsparren]
status: entwurf
theorie_pflichtig: required
quellen_primär:
  - "SIA 232/1:2020 'Geneigte Dächer', Schweizerischer Ingenieur- und Architektenverein, Abschnitt 1 (Begriffe und geometrische Grundlagen): Kehle als geneigte konkave Schnittkante zweier Dachflächen mit besonderer Bedeutung für die Wasserführung; Kehlsparren als Tragglied entlang der Kehllinie wird vorausgesetzend verwendet."
  - "SIA 265:2021 'Holzbau', Schweizerischer Ingenieur- und Architektenverein, Abschnitt 4 (Bemessung) und Abschnitt 5 (Konstruktive Durchbildung): geneigte stabförmige Tragglieder von Dachtragwerken; Kehlsparren als Sonderform mit konzentrierter Lastabtragung aus zwei Dachflächen-Anteilen und zusätzlicher Wasserführungs- und Schneeansammlungs-Last."
  - "DIN EN 1995-1-1:2010-12 (Eurocode 5), Abschnitt 5 (Tragwerksberechnung) und Abschnitt 6 (Grenzzustände der Tragfähigkeit): biegebeanspruchte Stab-Bauteile in Verschneidungs-Dachkonstruktionen."
  - "DIN 1356-1:1995-02 'Bauzeichnungen – Teil 1: Arten, Inhalte und Grundregeln der Darstellung', Abschnitt 5 (Darstellung von Dächern): Kehlsparren als Zeichnungselement mit eigenem Liniensymbol in der Bauzeichnung von Verschneidungs-Dächern."
  - "DIN 18338:2019-09 'VOB Teil C: Dachdeckungs- und Dachabdichtungsarbeiten', Abschnitt 0 (Begriffe): Kehle als geneigte Schnittlinie zweier nach innen einspringender Dachflächen; das unter der Kehle liegende Tragglied ist Kehlsparren oder Kehlbohle."
  - "DIN 1052:2008-12, Abschnitt 8 und Abschnitt 12 (Konstruktive Anforderungen): Tragglieder geneigter Dächer."
quellen_sekundär:
  - "Lignum (Hrsg.): Holzbautabellen HBT, Lignum, Zürich, aktuelle Auflage, Kap. 'Dachtragwerke' / Verschneidungen."
  - "Lignum (Hrsg.): Lignatec 'Geneigte Dächer in Holzbauweise', Lignum, Zürich, aktuelle Auflage, Abschnitt 'Verschneidungen / Grat- und Kehlsparren'."
  - "Mönck, W.; Rug, W.: Holzbau – Bemessung und Konstruktion. 16. Aufl., Beuth Verlag 2015, Kap. 11 'Dachtragwerke', § Verschneidungen / Walmdach."
  - "Natterer, J.; Herzog, T.; Volz, M.: Holzbau-Atlas. 4. Aufl., Birkhäuser, Basel 2003, Kap. 'Dachtragwerke / Verschneidungen'."
  - "Krämer, V.: Grundwissen des Zimmerers. Bruderverlag, Köln 2006, Kap. Schiftungen / Kehlsparren-Austragung."
  - "Koepf, H.; Binding, G.: Bildwörterbuch der Architektur. 4. Aufl., Kröner, Stuttgart 2005, Eintrag 'Kehlsparren'."
  - "Gerner, M.: Fachwerk – Instandsetzung, Sanierung, Neubau. DVA, 7. Aufl. 2007, Glossar 'Kehlsparren'."
  - "Berufsschul-Lehrmaterial: zimmerer-treff.com 'Austragung von Kehlsparren'; polybau.ch 'Austragung Kehlsparren / rechnerischer Abbund' (Schweiz, paralleler URL-Pfad)."
  - "Bemessungssoftware: Frilo DGK 'Grat- und Kehlsparren'; pbs.de 062J 'Holzbau Grat- und Kehlsparren – EC5'; pcae 4H-GRAT 'Grat- und Kehlsparren'; mb-AEC S120 'Grat- und Kehlsparren'; Harzer-Statik 'Kehlsparren'; Dietrich's 'Dachbauteile / Kehlsparren'."
quellenkonflikt: |
  **Norm-Lage:** Weder SIA 232/1, SIA 265, EN 1995-1-1, DIN 1052,
  DIN 1356 noch DIN 18338 enthalten einen geschlossenen
  Begriffseintrag „Kehlsparren"; der Begriff wird in allen
  konsultierten Normen vorausgesetzt und über seine konstruktive
  Rolle (geneigtes, lastabtragendes Stab-Bauteil entlang der
  Kehllinie zweier zusammentreffender Dachflächen) charakterisiert.
  Die Norm-Lage ist exakt parallel zu „Sparren" (siehe
  `hg_sparren.md`, `quellenkonflikt`) und zu „Gratsparren" (siehe
  `hg_gratsparren.md`, `quellenkonflikt`).

  **Strukturelle Asymmetrie zum Oberbegriff `sparren`:** Der
  Kehlsparren erbt von `sparren` die konstruktive **Rolle**
  (Stab-Bauteil eines Dachtragwerks mit geneigter Bauteilachse als
  lastabtragendes Tragglied), aber **nicht** die zentrale
  geometrische Bedingung 3 aus `hg_sparren.md` (Falllinien-
  Kollinearität in einer einzelnen Dachfläche). Die Bauteilachse
  eines Kehlsparrens liegt nicht in der Trägerebene einer einzelnen
  Dachfläche entlang ihrer Falllinie, sondern auf der
  **Schnittgeraden zweier Trägerebenen** — geometrisch identisch mit
  der Kehllinie im Sinne von `hg_kehle.md`. Diese Asymmetrie ist in
  `hg_sparren.md` Sektion „Wohldefiniertheit / Mehrfachzuordnung"
  bereits explizit antizipiert: „bei Verschneidungs-Sparren
  (Gratsparren, Kehlsparren), die auf zwei Dachflächen liegen, ist
  die Falllinien-Kollinearitätsbedingung nicht zu beiden Dachflächen
  gleichzeitig erfüllbar, weshalb diese Sonderformen eigene
  Begriffsdefinitionen erhalten."

  **Konsequenz:** Bedingung 3 von `hg_sparren.md` wird in der
  hiesigen Definition durch eine analoge **Kehllinien-Kollinearitäts-
  Bedingung** ersetzt (Bed. 3 unten); Bedingung 2 von
  `hg_sparren.md` (Lage in einer einzelnen Trägerebene) entfällt
  zugunsten einer Inzidenz-Bedingung auf eine Kehlstrecke s_{ij} im
  Sinne von `hg_kehle.md`. Die Vorzeichenkonvention (Bed. 4 in
  `hg_sparren.md`, „bergauf, von Traufe zu First") wird mit Bezug
  auf die aufwärts gerichtete Kehllinien-Tangente t_hat (siehe
  `hg_kehle.md`) übernommen. Diese Festlegung ist konsistent mit
  allen konsultierten Quellen.

  **Symmetrie zum Schwester-Begriff `gratsparren`:** Auf der
  **Linien- und Bauteilachsen-Ebene** ist die Definition des
  Kehlsparrens **mathematisch exakt symmetrisch** zur Definition des
  Gratsparrens — die einzige Vorzeichen-Asymmetrie liegt in der
  Konvexitäts-/Konkavitäts-Bedingung der zugeordneten Schnittstrecke:
  Gratsparren verlangt eine **konvexe** Gratstrecke (`hg_grat.md`
  Bed. 3, positives Spatprodukt der äußeren Normalen mit der
  aufwärts gerichteten Tangente), Kehlsparren verlangt eine
  **konkave** Kehlstrecke (`hg_kehle.md` Bed. 2, negatives
  Spatprodukt). Auf der **konstruktiven Ebene** brechen mehrere
  Asymmetrien auf — Wasserführungs- und Schneeansammlungs-Last,
  Abkehlung statt Abgratung der Oberkante, Schifter-Topologie-
  Inversion (Schifter laufen vom First zum Kehlsparren abwärts statt
  von der Fußpfette aufwärts). Diese konstruktiven Asymmetrien sind
  in der Erläuterungs-Sektion ausgeführt; sie sind nicht Bestandteil
  der Definition, prägen aber das Bemessungs- und Bearbeitungs-
  Profil des Bauteils.

  **Hauptmerkmal — geringere Neigung:** Mehrfach belegt (Wikipedia
  „Hexenschnitt"; baubeaver.de „Kehlsparren"; carpentrycompendium.com
  „Valley Rafters"): „Kehlsparren sind länger und flacher als
  normale Sparren." Die mathematische Charakterisierung erfolgt
  unten als abgeleiteter Satz (Reduktions-Formel
  `tan(α_K) = tan(α)·cos(β_plan)`, identisch zur Gratsparren-Formel
  — die Schnittgeraden-Neigung hängt nur von den Ebenenparametern
  ab, nicht von der Konvexität oder Konkavität der Verschneidung);
  sie folgt aus den Primitiven und ist nicht Teil der Definition.

  **Verkantung im Raum:** Mehrfach belegt; bedeutet, dass der
  Kehlsparrenquerschnitt um die Bauteilachse so liegt, dass seine
  Oberseite nicht in einer der beiden anliegenden Trägerebenen
  liegt. Anders als beim Gratsparren steht beim unbearbeiteten
  Kehlsparren-Quader die obere Längskante **über** der geometrischen
  Schnittlinie der beiden Trägerebenen und muss durch
  Bauteilbearbeitung in Übereinstimmung gebracht werden. Die drei
  Standard-Werkstücke der Zimmerei (**Abkehlung** der Oberkante,
  **Absenkung** des ganzen Bauteils, **Anhebung** mit Oberkante in
  der Kehllinie als CAD-Standard) sind Bestandteile der
  Bauteilbearbeitung, nicht der Definition; sie werden als
  Folgearbeit in `hg_abkehlung.md` geführt. Begriffliche
  Eigenständigkeit der Abkehlung gegenüber der Abgratung ist in
  Wikipedia „Kehlsparren" ausdrücklich festgehalten („die Abgratung
  heißt hier Kehlung").

  **Schifter (Schiftsparren) ist nicht synonym:** Schifter setzen
  mit doppelter Schmiege an der Seiten- bzw. Oberfläche des
  Kehlsparrens an. Anders als beim Gratsparren ist die
  Schifter-Topologie **invertiert**: der Kehlschifter beginnt am
  First und endet am Kehlsparren (Wikipedia „Schiftung"), läuft
  also vom First abwärts. Damit ist der Schifter topologisch
  komplementär zum Kehlsparren, kein Synonym.

  **Verschneidungssparren** ist im norddeutsch-BDZ-Sprachgebrauch
  Oberbegriff für Grat- und Kehlsparren; in der Schweiz und
  Süddeutschland selten und mehrdeutig (auch für Schiftsparren
  verwendet — siehe `hg_sparren.md` Spezialisierungen-Block).
  Daher in `abgelehnte_benennungen:` geführt; bei Bedarf späterer
  Sammelbegriff über eigenen Eintrag.

  **„Ixe" — Asymmetrie zum Schwester-Eintrag `hg_kehle.md`:**
  Das regional-schweizerische und süddeutsche Wort „Ixe" wird in
  `hg_kehle.md` als **Synonym zur Kehlkante** geführt (Linie auf
  der Verschneidung zweier Dachflächen). Eine direkte
  bauteilrollen-spezifische Spezialisierung „Ixesparren" /
  „Ix-Sparren" ist im DACH-Holzbau-Korpus nach gezielter
  WebSearch-Sichtung **nicht etabliert** — anders als bei
  „Mauerlatte"/`fusspfette` (siehe HG-§5) existiert für die
  Kehle/Kehlsparren-Achse **keine** spezialisierte Berufssprache-
  Variante des Ixe-Synonyms auf der **Bauteilrollen-Ebene**.
  Die HG-§5-Konvention (Spezialisierungs-Synonyme bei abgelehnter
  Oberbegriffs-Benennung) greift daher nicht, weil sie eine
  berufssprachliche Verankerung **im Spezial-Kontext** voraussetzt;
  „Ixe" ist Kanten-Sprache, nicht Bauteil-Sprache. Konsequenz:
  „Ixe" wird in `synonyme:` des Kehlsparrens **nicht** geführt, in
  `abgelehnte_benennungen:` mit dem Hinweis aufgenommen, dass die
  zulässige Lesart von „Ixe" auf der Kanten-Ebene (`hg_kehle.md`)
  liegt. Diese Asymmetrie zum Schwester-Eintrag ist beabsichtigt
  und dokumentiert.

  **Walmsparren** wird im Korpus uneinheitlich verwendet (teils für
  Gratsparren, teils für Walm-Schifter), für den Kehlsparren ist es
  in keiner konsultierten Quelle belegt; daher abgelehnt.

  **Kehlbalken — Verwechslungsfalle, kein Synonym:** „Kehlbalken"
  ist der **horizontale Querriegel** im Kehlbalkendach (siehe
  `hg_kehlbalken.md`, Forward-Verweis nach HG-§6 Kategorie A) — ein
  vollständig anderer Bauteilbegriff als der Kehlsparren. Die
  Verwechslungsfalle entsteht aus der gemeinsamen Wortwurzel
  „Kehl-". Der Kehlbalken liegt **horizontal** und überspannt zwei
  gegenüberliegende Sparren als Zugband oder Druckriegel; der
  Kehlsparren liegt **geneigt** auf der Kehllinie zweier
  Dachflächen. Beide Begriffe stehen weder in einer
  Spezialisierungs- noch in einer Synonymie-Beziehung. „Kehlbalken"
  wird daher in `abgrenzung_zu:` geführt, nicht in
  `abgelehnte_benennungen:`.

  **Kehlbohle — alternative Konstruktion, kein Synonym:** Statt
  eines Kehlsparrens kann eine **Kehlbohlen-Schiftung** zur
  Ausführung kommen (Wikipedia „Kehlsparren": „Alternativ zum
  Kehlsparren kann auch eine Bohlenschiftung zur Ausführung
  kommen"; zimmerer.de Handbuch Anhang 2). Die Kehlbohle ist eine
  flache Bohle als Unterlage des Kehlblechs ohne tragende Funktion
  für die Schifter; sie ist disjunkt zum Kehlsparren und wird in
  `abgelehnte_benennungen:` geführt, mit dem Vermerk, dass ein
  künftiger eigenständiger Eintrag `hg_kehlbohle.md` als
  Folgearbeit-Trigger absehbar ist.

  **Lignum / SIA Schweiz:** Trotz mehrfacher Recherche keine
  direkten Lignum-Volltextbelege online verifizierbar (Lignum HBT
  und Lignatec nicht volltext-indiziert). Eintrag analog zu
  `hg_sparren.md` und `hg_gratsparren.md` mit Lignum-Quellen-
  Hinweis; die spezifische Begriffsbelegung ist im DACH-Holzbau-
  Korpus als etabliert nachgewiesen, die normative Schweizer
  Quellenstelle ist nicht direkt zitierbar.

  **Forward-Verweise** (HG-§6 Kategorie A): `abkehlung`,
  `schiftsparren`, `kehlbohle`, `kehlblech`, `kehlbalken` —
  Trigger jeweils erste Visualisierung der Kehlsparren-Oberseite
  bzw. erste vollständige Walmdach-/Kehldach-Modellierung bzw.
  erstes Tool zur alternativen Bohlen-Konstruktion. `abgratung` als
  Forward-Verweis in `abgrenzung_zu:` ist redundant zum
  Gratsparren-Eintrag und dient hier nur dem Symmetrie-Vergleich
  Abgratung ↔ Abkehlung.
---

## Prosa-Definition

Ein **Kehlsparren** ist ein Stab-Bauteil eines Dachtragwerks in der
Bauteilrolle eines Sparrens, dessen Bauteilachse auf der Kehllinie
zweier benachbarter Dachflächen liegt — also auf einer geneigten,
konkaven Schnittkante zweier Trägerebenen — und das die Lasten beider
anliegender Dachflächen-Anteile zusammen mit der in der Kehle
konzentriert ablaufenden Wasserführungs- und Schneeansammlungs-Last
entlang seiner Längsachse zwischen einem Trauf-Innen-Eckpunkt am Fuß
und einem Firstend-Punkt am Kopf abträgt.

## Mathematische Definition

Sei

- B ein Bauteil im Sinne von `bauteil` mit Stabgeometrie
  (`geometrie ∈ 𝒢_stab`),
- a(B) = Bauteilachse.Gerade(p_a, p_e) die Bauteilachse von B im
  geraden Fall (siehe `bauteilachse`), mit
  d_hat_K := (p_e − p_a) / ‖p_e − p_a‖ ∈ S² ⊂ ℝ³,
- 𝒟 = {D_1, …, D_m} eine Dachflächenfamilie im Sinne von
  `dachflaeche`,
- D_i = (E_i, P_i, n_{a,i}) und D_j = (E_j, P_j, n_{a,j}) zwei
  verschiedene Dachflächen aus 𝒟 mit i ≠ j,
- s_{ij} ⊂ ℝ³ eine **Kehlstrecke** im Sinne von `hg_kehle.md`,
  also eine Schnittstrecke s_{ij} = F(P_i) ∩ F(P_j), die die
  Kehlen-Bedingungen (1)–(2) aus `hg_kehle.md` erfüllt
  (geneigt, konkav, beide äußeren Normalen in oberer Halbkugel,
  Spatprodukt ⟨n_hat_{a,i} × n_hat_{a,j}, t_hat⟩ < −ε_W),
- t_hat := (b_{ij} − a_{ij}) / ‖b_{ij} − a_{ij}‖ ∈ S² die Tangente
  von s_{ij} mit s_{ij} = [a_{ij}, b_{ij}] und (Vorzeichenkonvention
  aus `hg_kehle.md`) ⟨t_hat, e_z⟩ > 0 (bergauf orientiert),
- e_z := (0, 0, 1)ᵀ die vertikale Achse,
- ε_W := Toleranzen.WINKEL_EPS die Winkeltoleranz,
- ε_K := Toleranzen.KOLLINEAR_EPS die Kollinearitätstoleranz,
- ε_L := Toleranzen.LAENGE_EPS die Längentoleranz.

Dann heißt B ein **Kehlsparren** der Kehlstrecke s_{ij} der
Dachflächenfamilie 𝒟 genau dann, wenn die folgenden Bedingungen
erfüllt sind:

1. **Stabgeometrie**: B besitzt eine gerade Bauteilachse mit
   ‖p_e − p_a‖ > ε_L.

2. **Endpunkt-Inzidenz**: Beide Endpunkte der Bauteilachse liegen
   auf der Kehllinie der Kehlstrecke s_{ij} im Sinne der
   Punkt-Gerade-Inzidenz; konkret existieren Skalare
   s_a, s_e ∈ ℝ mit
   ```
   p_a = a_{ij} + s_a · (b_{ij} − a_{ij}),
   p_e = a_{ij} + s_e · (b_{ij} − a_{ij}),
   ```
   und der zur Kehllinie rechtwinklige Abstand beider Endpunkte
   ist kleiner-gleich ε_L (Lage-Toleranz auf der Schnittgeraden
   der beiden Trägerebenen E_i und E_j).

3. **Kehllinien-Kollinearität** (Ersatz für die
   Falllinien-Kollinearität aus `hg_sparren.md` Bed. 3): Die
   Bauteilachsenrichtung ist kollinear zur Kehllinien-Tangente,
   ```
   ‖d_hat_K × t_hat‖ ≤ ε_K,
   ```
   d. h. der Winkel zwischen d_hat_K und t_hat ist 0 oder π (modulo der
   numerischen Sinus-Toleranz nach §4 HG-Konvention für
   Parallelitäts-Prädikate).

4. **Vorzeichenkonvention** (Kehlsparrenrichtung von Trauf-Innenecke
   zu Firstend-Punkt): Die Bauteilachse ist so gerichtet, dass d_hat_K
   in dieselbe Halbkugel wie t_hat weist, also bergauf:
   ```
   ⟨d_hat_K, t_hat⟩ ≥ +1 − ε_W,
   ```
   äquivalent ⟨d_hat_K, e_z⟩ > 0. p_a ist damit der **Kehlsparrenfuß**
   (am Trauf-Innen-Eckpunkt zweier zusammentreffender Dachflächen),
   p_e der **Kehlsparrenfirstpunkt** (am Firstend-Punkt der
   Kehllinie bzw. am Verschneidungs-Knoten unter dem First).

5. **Zuordnung zu genau einer Kehlstrecke**: B ist Kehlsparren
   einer eindeutig bestimmten Kehlstrecke s_{ij} der Familie 𝒟;
   die Wahl von s_{ij} ist die Zuordnung des Bauteils und nicht
   selbst Bestandteil der Bauteilgeometrie.

Wesentliche abgeleitete Größen:

- **Kehlsparrenlänge**: L_{S,K} := ‖p_e − p_a‖ (in mm), entlang
  der Bauteilachse zwischen Kehlsparrenfuß und
  Kehlsparrenfirstpunkt.

- **Kehlsparrenneigung** (= Kehlneigung der zugeordneten
  Kehlstrecke, siehe `hg_kehle.md`, abgeleitete Operation
  `kehlneigung()`):
  ```
  α_K := arcsin(|⟨t_hat, e_z⟩|) = arcsin(⟨d_hat_K, e_z⟩).
  ```
  Wertebereich α_K ∈ (0, π/2) bei nicht-entarteten Verschneidungs-
  Kehlen.

- **Kehlsparrenfuß** und **Kehlsparrenfirstpunkt** (als Punkte):
  F_{fuß,K} := p_a, F_{first,K} := p_e.

### Abgeleiteter Satz — Reduktions-Formel der Kehlsparrenneigung

Für gleichgeneigte anliegende Dachflächen D_i und D_j mit gemeinsamer
Dachneigung α und einem Plan-Winkel β_plan zwischen der
Grundrissprojektion der Kehllinie und der Trauflinie einer der beiden
Dachflächen gilt

```
tan(α_K) = tan(α) · cos(β_plan).                                  (★)
```

**Herleitung aus den Primitiven:** Die Herleitung ist exakt parallel
zur Gratsparren-Reduktionsformel aus `hg_gratsparren.md`. Sei
π_xy: ℝ³ → ℝ² die Projektion in die Horizontalebene. Die Schnittgerade
s_{ij} ⊂ ℝ³ projiziert auf eine Gerade π_xy(s_{ij}) ⊂ ℝ². Sei e_hat_t :=
(t_hat_x, t_hat_y, 0) / ‖(t_hat_x, t_hat_y)‖ der normierte Grundrissrichtungs-
vektor der Kehllinie und e_hat_fall(E_i) die Falllinie der Dachfläche
D_i (siehe `hg_falllinie.md`). Dann gilt nach Konstruktion

```
cos(β_plan) = |⟨e_hat_t, π_xy(e_hat_fall(E_i)) / ‖π_xy(e_hat_fall(E_i))‖⟩|.
```

Aus der Geneigtheits-Bedingung (`hg_kehle.md` Bed. 1) und der
Tatsache, dass t_hat in beiden Trägerebenen E_i und E_j liegt
(s_{ij} = E_i ∩ E_j), folgt durch Aufspaltung von t_hat in seinen
horizontalen Anteil und e_z-Anteil mit Höhenfunktion z auf E_i

```
⟨t_hat, e_z⟩ / ‖(t_hat_x, t_hat_y)‖ = tan(α) · cos(β_plan)
```

und damit `tan(α_K) = ⟨t_hat, e_z⟩ / ‖(t_hat_x, t_hat_y)‖ = tan(α) ·
cos(β_plan)`. ∎

**Vorzeichen-Unabhängigkeit:** Die Reduktionsformel hängt **nicht**
vom Vorzeichen des Spatprodukts ⟨n_hat_{a,i} × n_hat_{a,j}, t_hat⟩ ab, das die
Konvexität (Gratstrecke, positiv) von der Konkavität (Kehlstrecke,
negativ) trennt. Sie liefert daher dieselbe Reduktion für
Gratsparren und Kehlsparren — die Schnittgeraden-Neigung ist eine
Eigenschaft der beiden Trägerebenen, nicht ihrer
Außenseiten-Orientierung. Diese Identität ist im angelsächsischen
Korpus ausdrücklich festgehalten: „A regular hip rafter and a
regular valley rafter on the same roof typically have the same
slope if both roof planes have the same pitch."

Im symmetrischen Spezialfall (gleichgeneigte Dachflächen mit
horizontalen, rechtwinklig zueinander stehenden Traufen) ist die
Grundrissprojektion der Kehllinie die Winkelhalbierende der beiden
Trauflinien-Polygon-Kanten und damit β_plan = 45°, woraus folgt

```
tan(α_K) = tan(α) / √2.                                          (★★)
```

(★) ist ein **abgeleiteter Satz**, kein Definitionsbestandteil; die
Definition selbst (Bed. 1–5 oben) verwendet ausschließlich die
Primitive Punkt, Vektor, Strecke, Ebene und die bereits definierten
Begriffe `bauteil`, `bauteilachse`, `sparren`, `kehle`, `dachflaeche`.

## Wohldefiniertheit

- **Existenz**: Für jede Verschneidungs-Dachkonstruktion mit nicht-
  entarteten Kehlstrecken existiert in der Standardkonfiguration
  genau ein Kehlsparren pro Kehlstrecke; das ist die übliche
  Verschneidungs-Konstruktion (zwei Kehlsparren bei einem
  T-förmigen Sattel-an-Sattel-Anbau, mehrere bei Gaube-an-
  Hauptdach). Bed. 1–5 sind konstruktiv erfüllbar.

- **Eindeutigkeit der Vorzeichenkonvention**: Aus der
  Geneigtheits-Bedingung der Kehlstrecke (`hg_kehle.md` Bed. 1)
  folgt ⟨t_hat, e_z⟩ > ε_W, also t_hat ≠ −t_hat als Tangentenwahl. Bed. 3
  und 4 zusammen fixieren d_hat_K = +t_hat (modulo ε_K, ε_W). Die
  alternative Orientierung d_hat_K = −t_hat ist durch Bed. 4
  ausgeschlossen.

- **Asymmetrie zum Oberbegriff `sparren` — explizite Auflösung:**
  In `hg_sparren.md` lauten die zentralen geometrischen
  Bedingungen:
  - Bed. 2: beide Endpunkte der Bauteilachse liegen in der
    Trägerebene **einer** zugeordneten Dachfläche;
  - Bed. 3: die Bauteilachsenrichtung ist kollinear zur
    **Falllinie** dieser einen Dachfläche.

  Für den Kehlsparren sind beide Bedingungen strukturell verletzt
  — exakt parallel zum Gratsparren (siehe `hg_gratsparren.md`,
  Wohldefiniertheits-Block):
  - Die Bauteilachse liegt auf der Schnittgeraden **zweier**
    Trägerebenen E_i und E_j; sie liegt also in der gemeinsamen
    Schnittgeraden beider, aber sie verläuft **nicht entlang einer
    Falllinie**, denn die Schnittgerade zweier nicht-paralleler,
    geneigter Ebenen ist nicht die Falllinie einer der beiden
    (außer in entarteten Sonderfällen). Diese strukturelle
    Asymmetrie ist Vorzeichen-unabhängig und betrifft Gratsparren
    und Kehlsparren gleichermaßen.
  - Genau diese Asymmetrie ist in `hg_sparren.md` Sektion
    „Wohldefiniertheit / Mehrfachzuordnung" antizipiert: „bei
    Verschneidungs-Sparren (Gratsparren, Kehlsparren), die auf zwei
    Dachflächen liegen, ist die Falllinien-Kollinearitätsbedingung
    nicht zu beiden Dachflächen gleichzeitig erfüllbar, weshalb
    diese Sonderformen eigene Begriffsdefinitionen erhalten".

  Die hiesige Definition löst die Asymmetrie auf, indem sie:
  - Bed. 2 von `hg_sparren.md` durch eine **Endpunkt-Inzidenz auf
    einer Kehlstrecke s_{ij}** (Bed. 2 hier) ersetzt;
  - Bed. 3 von `hg_sparren.md` durch eine **Kehllinien-Kollinearität
    zur Tangente t_hat** (Bed. 3 hier) ersetzt;
  - Bed. 4 von `hg_sparren.md` als **bergauf-Orientierung relativ
    zu t_hat** statt zu e_hat_fall übernimmt (Bed. 4 hier).

  Die geerbte konstruktive Rolle des Oberbegriffs `sparren`
  (Stab-Bauteil eines Dachtragwerks, geneigt, lastabtragend,
  Bauteilachse bergauf orientiert) bleibt damit unverletzt; nur
  die geometrische Lage-Bedingung wird von der Falllinie einer
  Einzelfläche auf die Kehllinie der Verschneidung umgehängt.

- **Konsistenz mit `hg_kehle.md`**: Aus Bed. 3 und Bed. 4 folgt
  d_hat_K = +t_hat (modulo Toleranzen), wobei t_hat die nach `hg_kehle.md`
  Vorzeichenkonvention bergauf gerichtete Kehllinien-Tangente ist.
  Damit ist der Kehlsparrenfuß stets am unteren Endpunkt a_{ij}
  der Kehlstrecke (Trauf-Innen-Eckpunkt) und der
  Kehlsparrenfirstpunkt stets am oberen Endpunkt b_{ij}
  (Firstend-Punkt der Kehllinie).

- **Konsistenz mit `hg_gratsparren.md` — Vorzeichen-Trennung der
  Bauteilrolle:** Die Vorzeichen-Asymmetrie zwischen Gratsparren
  und Kehlsparren liegt **ausschließlich** in der
  Konvexitäts-/Konkavitäts-Bedingung der zugeordneten
  Schnittstrecke (Spatprodukt der äußeren Normalen mit der
  aufwärts gerichteten Tangente positiv vs. negativ). Diese
  Trennung wird von `hg_grat.md` Bed. 3 (positiv) und
  `hg_kehle.md` Bed. 2 (negativ) getragen, ist disjunkt durch das
  Toleranzband [−ε_W, +ε_W] für entartete Konfigurationen und
  liefert eine **eindeutige Klassifikation** jeder geneigten
  Schnittstrecke s_{ij} einer Dachflächenfamilie als entweder
  Grat- oder Kehlstrecke. Ein Bauteil B ist daher zu jeder
  Schnittstrecke der Familie entweder Gratsparren oder
  Kehlsparren, nie beides.

- **Reduktions-Formel (★) als Konsequenz, nicht als Axiom**: Die
  Formel `tan(α_K) = tan(α)·cos(β_plan)` wurde oben aus den
  Primitiven hergeleitet; sie ist nicht Bestandteil der Definition
  (Bed. 1–5), sondern beweisbar daraus. Damit ist die Definition
  konservativ im Sinne der HG-Konventionen: die mathematische
  Charakterisierung der reduzierten Neigung ist Abkürzung, nicht
  Axiom.

- **Mehrfachzuordnung — gegenseitige Disjunktheit der
  Sparren-Spezialisierungen**: Ein Bauteil B kann nicht
  gleichzeitig
  - Sparren einer einzelnen Dachfläche im Sinne von `hg_sparren.md`
    und Kehlsparren einer Kehlstrecke s_{ij} sein (die
    Falllinien-Kollinearität aus `hg_sparren.md` Bed. 3 ist mit
    der Kehllinien-Kollinearität aus Bed. 3 hier nicht gleichzeitig
    erfüllbar);
  - Gratsparren einer Gratstrecke und Kehlsparren einer Kehlstrecke
    sein (die Konvexitäts- und Konkavitäts-Bedingungen der
    zugeordneten Schnittstrecken aus `hg_grat.md` Bed. 3 und
    `hg_kehle.md` Bed. 2 sind disjunkt durch das Spatprodukt-
    Vorzeichen).

- **Nicht-Zirkularität**: Die Definition stützt sich nur auf
  bereits definierte Begriffe (`bauteil`, `bauteilachse`,
  `sparren`, `kehle`, `dachflaeche`, `strecke`, `einheitsvektor`,
  `ebene`, `dachneigung`, `weltkoordinatensystem`, `toleranzen`).
  Sie kommt nicht in ihrer eigenen Definition vor und verweist
  nicht auf Kehlsparren-Spezialisierungen oder Bearbeitungs-
  Folgegeometrie (Abkehlung, Absenkung, Anhebung).

- **Auflagerung (qualitativ, nicht Bestandteil der Definition)**:
  Ein Kehlsparren wird im Tragwerk typischerweise gestützt durch
  - eine **durchlaufende Fußpfette** der höheren Hauptdachfläche
    plus seitlich anschließende Pfette am Kehlsparrenfuß (am
    Trauf-Innen-Eckpunkt); anders als der Gratsparren liegt der
    Fuß **nicht** an einem Eck-Pfettenstoß zweier endender
    Fußpfetten, sondern an einer durchlaufenden Pfette;
  - einen **Firstpfetten-Knoten** oder einen
    **Verschneidungs-Knoten** unter dem First am
    Kehlsparrenfirstpunkt.

  Die Auflagerung ist Eigenschaft des Tragwerks (siehe
  `hg_tragwerk.md`), nicht des Kehlsparrens selbst. Die
  zugehörigen Bearbeitungen (Kerve am Fuß, Firstanschnitt,
  Backenschnitte, Abkehlung, Hexenschnitt) sind partitive
  Bestandteile des Kehlsparrens, nicht Bestandteile der
  Definition.

## Erläuterung (nicht normativ)

Der Kehlsparren ist das **diagonale Hauptbauteil einer
Verschneidung**: er erscheint überall dort, wo zwei Dachflächen in
einer Innenecke zusammentreffen — typische Fälle sind ein
T-förmiger Sattel-an-Sattel-Anbau (zwei Kehlsparren beidseits an der
Schnittstelle), eine Dachgaube an einem Hauptdach (zwei Kehlsparren
seitlich der Gaube) oder ein Walm-an-Sattel-Übergang
ungleichgeneigter Dächer.

### Geometrische Charakterisierung — die geringere Neigung

Wie der Gratsparren weist auch der Kehlsparren eine **geringere
Neigung gegenüber den anliegenden Sparren** auf, denn die
Reduktionsformel `tan(α_K) = tan(α)·cos(β_plan)` hängt nicht vom
Vorzeichen der Verschneidung ab, sondern nur von den
Ebenenparametern. Im symmetrischen Fall (gleichgeneigte anliegende
Dachflächen, rechtwinklige Trauf-Innenecke) gilt

```
tan(α_K) = tan(α) / √2.
```

Beispiel: bei einer Dachneigung α = 45° hat der Kehlsparren eine
Neigung von α_K = arctan(1/√2) ≈ 35.26° — exakt dieselbe Neigung
wie der Gratsparren desselben Daches. Im allgemeinen Fall
(ungleichgeneigte Dachflächen) gilt `tan(α_K) = tan(α)·cos(β_plan)`.

Die zimmermannssprachliche Praxis-Faustregel „Kehlsparren sind
länger und flacher als normale Sparren" ist die qualitative Lesart
dieser Reduktion.

### Die drei konstruktiven Asymmetrien zum Gratsparren

Auf der **mathematischen Linien-Ebene** sind Gratsparren und
Kehlsparren symmetrische Geschwister — sie unterscheiden sich nur
durch das Vorzeichen des Spatprodukts der äußeren Normalen mit der
aufwärts gerichteten Tangente (`hg_grat.md` Bed. 3 vs.
`hg_kehle.md` Bed. 2). Auf der **konstruktiven Ebene** brechen
jedoch drei substanzielle Asymmetrien auf, die das Bemessungs-
und Bearbeitungs-Profil des Kehlsparrens prägen.

**(1) Wasserführung und Schneeansammlung.** In der Kehle (Innenecke,
Konkavität) fließt das Niederschlagswasser **beider** anliegender
Dachflächen zusammen und konzentriert sich auf die Kehllinie. Der
Kehlsparren trägt daher

- die **gesamte Niederschlagslast** beider anliegender Dachflächen-
  Anteile, konzentriert entlang seiner Längsachse;
- zusätzlich **Schneeansammlungs-Last** durch Sackung des Schnees
  in der Kehlrinne (besonders relevant in der Schweiz und im
  Voralpenraum; einschlägige Bemessungs-Lastfälle nach SIA 261 bzw.
  DIN EN 1991-1-3 „Anhäufung in Kehlen").

Der Gratsparren liegt auf der entgegengesetzt orientierten,
konvexen Außenecke; Wasser fließt vom Grat **abwärts** in die
beiden anliegenden Dachflächen, der Gratsparren trägt keine
konzentrierte Wasser- oder Schneeansammlungs-Last. Diese
Lastfall-Asymmetrie ist die zentrale statisch-konstruktive
Differenz zwischen den beiden Geschwister-Bauteilen und liefert
beim Kehlsparren häufig das maßgebende Bemessungsmoment.

**(2) Abkehlung statt Abgratung.** Da der unbearbeitete
Kehlsparren-Quader mit seiner oberen Längskante **über** der
geometrischen Schnittlinie der beiden Trägerebenen steht (anders
als beim Gratsparren, dessen Querschnitt unbearbeitet **unter** den
beiden Trägerebenen liegt), ist die Standard-Werkstück-Lösung
**inhaltlich gespiegelt**:

- **Abkehlung** (regional auch „Kehlung" — Wikipedia „Kehlsparren":
  „die Abgratung heißt hier Kehlung"): Die obere Längskante wird in
  der Mitte des Kehlsparrens **vertikal weggeschnitten** (V-förmige
  Nut nach unten), so dass die beiden Dachflächen-Trägerebenen bis
  zur Mitte des Kehlsparrens „durchlaufen" können.
- **Absenkung** (englisch *dropping the valley*): Der Kehlsparren
  wird als Ganzes um einen kleinen Betrag vertikal abgesenkt; die
  Schifter setzen mit ihrer Schmiege bündig auf der **Oberkante**
  des Kehlsparrens an. Alternative Lösung mit einfacherem Abbund.
- **Anhebung** mit Oberkante in der Kehllinie (CAD-Standard
  Dietrich's): Der Kehlsparren wird so positioniert, dass seine
  Oberkante exakt auf der geometrischen Kehllinie liegt; die
  Schifter setzen mit Schmiege auf der **Oberseite** des
  Kehlsparrens an. Im Werkstück entspricht dies einer
  unbearbeiteten Oberkante.

Die Abkehlung wird im Glossar als eigener Folge-Begriff
`hg_abkehlung.md` geführt (Folgearbeit, Trigger: erste
Visualisierung der Kehlsparren-Oberseite, gemeinsam mit
`hg_abgratung.md`). Begriffliche Eigenständigkeit gegenüber der
Abgratung ist im Korpus ausdrücklich belegt.

**(3) Schifter-Topologie-Inversion.** Die Schifter am Kehlsparren
setzen mit doppelter Schmiege an, aber ihre **Achsen-Topologie ist
umgekehrt** zur Gratsparren-Situation:

- Am **Gratsparren** laufen die Gratschifter **von der Fußpfette
  (unten) schräg aufwärts zum Gratsparren** und werden von unten
  angesetzt.
- Am **Kehlsparren** laufen die Kehlschifter **von der Firstpfette
  (oben) schräg abwärts zum Kehlsparren** und werden von oben
  angesetzt (Wikipedia „Schiftung": „Der Kehlschifter beginnt am
  First und endet am Kehlsparren").

Die Topologie-Inversion zeigt sich auch in der Anschluss-Variante
**Klauenschifter**: am Gratsparren liegt die Klaue auf der
**Unterkante**, am Kehlsparren auf der **Oberkante**
(Kehlklauenschiftung). Die Schifter-Topologie ist Bestandteil der
Tragwerks-Komposition (siehe `hg_tragwerk.md`), nicht der
Kehlsparren-Definition.

### Verschneidungs-Grundrissprojektion

Bei gleichgeneigten anliegenden Dachflächen mit horizontalen
Traufen bildet die Grundrissprojektion der Kehllinie — analog zur
Gratlinie — die **Winkelhalbierende** der beiden Trauflinien-
Polygon-Kanten (siehe `hg_dachausmittlung.md`, Folgearbeit). Bei
ungleicher Neigung ist die Grundrissprojektion **keine**
Winkelhalbierende mehr, sondern wird über eine
Traufhöhen-Hilfslinien-Konstruktion bestimmt — exakt parallel zum
Gratsparren-Fall.

### Querschnitt und Werkstoff

Kehlsparren werden mit größerem Querschnitt ausgeführt als die
anliegenden Normal-Sparren, weil sie die Lasten beider anliegender
Dachflächen-Anteile plus die Wasser- und Schneeansammlungs-Last
tragen. Statisch ist der Kehlsparren häufig **ungünstiger** als der
vergleichbare Gratsparren (Asymmetrie (1) oben); typische
Querschnitte sind mindestens so groß wie beim Gratsparren des
gleichen Daches, oft eine Sortimentsklasse höher. Die konkrete
Querschnittsfindung ist Gegenstand der Bemessung nach SIA 265 /
EN 1995-1-1 und liegt nicht im Definitionsbereich dieses Glossars.

Sechs unabhängige Bemessungsprogramme (Frilo DGK, pbs.de 062J, pcae
4H-GRAT, mb-AEC S120, Harzer-Statik, Dietrich's) führen Grat- und
Kehlsparren in **einem gemeinsamen Modul** mit gemeinsamer
Geometrie und getrennter Lastfall-Behandlung — die enge Symmetrie
auf der Linien-Ebene und die konstruktive Asymmetrie auf der
Lastfall-Ebene sind im Software-Pendant strukturell präsent.

### Typische Verbindungen und Bearbeitungen am Kehlsparren

- **Kerve am Fuß** auf der Fußpfetten-Trauf-Innenecke
  (Bleischnitt nach `hg_kerve.md`).
- **Firstanschnitt** als oberer Endschnitt am Firstend-Punkt der
  Kehllinie.
- **Backenschnitte / Backenschmiege** an den seitlichen
  Anschluss-Flächen für die Schifter — mit **umgekehrter
  Schmiegen-Richtung** als beim Gratsparren (Schifter von oben).
- **Abkehlung** der Oberkante (Folgearbeit `hg_abkehlung.md`).
- **Hexenschnitt** am Fuß zur beidseitigen planaren Anlage von
  Traufbohle und Stirnbrett — geometrisch gespiegelt zum
  Gratsparren-Hexenschnitt (Innenecke statt Außenecke). Folgearbeit
  `hg_hexenschnitt.md`, gemeinsamer Trigger Grat-/Kehlsparren-
  Bearbeitung; bis dahin Forward-Verweis in `abgrenzung_zu:` nicht
  erzwungen.

Diese Bearbeitungen sind partitive Bestandteile von Kehlsparren-
Bauteilen (siehe `hg_bauteilbearbeitung.md` / `hg_kerve.md` etc.),
**nicht** Bestandteile der Begriffsdefinition.

### Sonderfälle

- **Verschneidung Sattel × Sattel (T-Anbau)**: zwei Kehlsparren
  beidseits des Anbaus; jeder endet am Firstend-Punkt der
  niedrigeren Firstlinie auf der höheren Hauptdachfläche.
- **Verschneidung Dachgaube × Hauptdach**: zwei Kehlsparren von
  den seitlichen Trauf-Innenecken der Gaube aufwärts zum
  Hauptdach.
- **Verschneidung Walm × Sattel ungleich**: Walm-Gratsparren
  trifft Kehlsparren-Endpunkt am kombinierten
  Verschneidungs-Knoten.
- **Verlängerung über den Trauf-Innenecken-Punkt hinaus** (CAD-
  Konstruktions-Detail, Dietrich's): zur Aufnahme einer
  Traufbohle kann der Kehlsparren über den Trauf-Innen-Eckpunkt
  hinausgeführt werden; die Definition bleibt unverändert
  anwendbar.
- **Alternative Konstruktion Kehlbohle**: statt eines Kehlsparrens
  kann eine flache Bohlen-Unterlage (Kehlbohle) eingebaut werden,
  über die die Schifter durchlaufen und an der Kehllinie
  gegeneinander stoßen. Die Kehlbohle ist kein Synonym, sondern
  eine andere Tragwerks-Konstruktion (siehe Folgearbeit
  `hg_kehlbohle.md`).

## Beziehungen

- **Oberbegriff**: `sparren`. Strukturell ist der Kehlsparren eine
  Bauteilrolle, die die konstruktive Sparrenrolle (Stab-Bauteil,
  geneigt, lastabtragend, bergauf orientiert) erbt, aber die
  Falllinien-Kollinearität (`hg_sparren.md` Bed. 3) durch eine
  Kehllinien-Kollinearität ersetzt. Diese Asymmetrie ist in
  `hg_sparren.md` Sektion „Mehrfachzuordnung" explizit
  antizipiert und in `hg_gratsparren.md` parallel ausgeführt.

- **Geschwister-Begriffe** (andere Sparren-Spezialisierungen):
  - `gratsparren`: mathematisch exakt symmetrisches Gegenstück auf
    einer konvexen Gratstrecke statt einer konkaven Kehlstrecke;
    konstruktive Asymmetrien siehe Erläuterungs-Block.
  - `schifter` / `schiftsparren` (Folgearbeit): verkürzte Sparren,
    die am Kehlsparren mit Schmiege ansetzen (topologisch
    komplementär, nicht synonym; Schifter laufen am Kehlsparren
    von oben nach unten — Topologie-Inversion gegenüber dem
    Gratsparren).

- **Bestandteile (partitiv)**:
  - **Bauteilachse** (`bauteilachse.Gerade`, vom Bauteil geerbt)
    mit Kehlsparrenfuß als Anfangs- und Kehlsparrenfirstpunkt als
    Endpunkt;
  - **Querschnitt** (vom Bauteil geerbt; rechteckig, typisch
    mindestens wie Gratsparren des gleichen Daches);
  - **Werkstoff** (vom Bauteil geerbt; Vollholz oder BSH);
  - **Faserrichtung** (Annotation, Default ‖ d_hat_K);
  - **Abkehlung** (partitive Bearbeitung, Folgearbeit
    `hg_abkehlung.md`);
  - **Kerven** am Fuß (siehe `hg_kerve.md`).

- **Verwendung / Beziehung zu anderen Bauteilen**:
  - **Kehle** (`kehle`): geometrische Schnittkante zweier
    Dachflächen, auf der die Bauteilachse des Kehlsparrens liegt;
    das ist die konstitutive Beziehung.
  - **Dachfläche** (`dachflaeche`): der Kehlsparren ist genau zwei
    Dachflächen gleichzeitig zugeordnet (D_i und D_j); seine
    Bauteilachse liegt auf E_i ∩ E_j.
  - **Firstpfette** (`firstpfette`): das obere Auflager des
    Kehlsparrens (Firstend-Punkt der Kehllinie) liegt
    typischerweise an einem Firstpfetten-Knoten der höheren
    Hauptdachfläche.
  - **Fußpfette** (`fusspfette`): das untere Auflager des
    Kehlsparrens liegt am Trauf-Innen-Eckpunkt auf einer
    **durchlaufenden** Fußpfette der höheren Hauptdachfläche
    (Asymmetrie zum Gratsparren, dessen Fuß an einem
    Eck-Pfettenstoß zweier endender Fußpfetten liegt).
  - **Schifter** (`schifter`, Folgearbeit): seitliche Anschluss-
    Sparren, die mit doppelter Schmiege am Kehlsparren ansetzen.
    Anders als am Gratsparren laufen die Schifter am Kehlsparren
    **von oben** (Firstpfette) **abwärts** an.

- **Abgrenzung**:
  - **Sparren** (`sparren`): der allgemeine Sparrenbegriff verlangt
    Falllinien-Kollinearität in einer einzelnen Dachfläche
    (`hg_sparren.md` Bed. 3); der Kehlsparren erfüllt diese
    Bedingung gerade nicht, sondern verlangt stattdessen
    Kehllinien-Kollinearität. Die Asymmetrie ist in
    `hg_sparren.md` Sektion „Mehrfachzuordnung" antizipiert und
    oben im Wohldefiniertheits-Block ausgeführt.
  - **Gratsparren** (`gratsparren`): mathematisch exakt
    symmetrisches Geschwister auf einer **konvexen** Gratstrecke
    (`hg_grat.md` Bed. 3, positives Spatprodukt) statt einer
    konkaven Kehlstrecke (`hg_kehle.md` Bed. 2, negatives
    Spatprodukt). Konstruktiv asymmetrisch in Wasserführung,
    Oberkanten-Bearbeitung (Abgratung vs. Abkehlung) und
    Schifter-Topologie — siehe Erläuterungs-Block.
  - **Schifter** (`schifter`, Folgearbeit): die Schifter setzen am
    Kehlsparren an; sie sind topologisch komplementär, **kein
    Synonym**. „Verschneidungssparren" wird regional mehrdeutig
    sowohl für Kehlsparren als auch für Schiftsparren verwendet
    und ist daher als Hauptbenennung ungeeignet.
  - **Kehle** (`kehle`): die geometrische Kante; der Kehlsparren
    ist das Bauteil entlang dieser Kante. Die Kehle ist eine
    Dachkante (partitive Geometrie der Dachflächenfamilie), der
    Kehlsparren ein Bauteil mit Bauteilachse auf dieser Kante.
  - **Kehlbohle** (Folgearbeit `hg_kehlbohle.md`): alternative
    Konstruktion einer Verschneidung als flache Bohlen-Unterlage
    statt eines tragenden Kehlsparrens; kein Synonym, sondern
    andere Lastabtragungs-Topologie.
  - **Kehlblech** (Folgearbeit `hg_kehlblech.md` / `hg_kehlrinne`):
    wasserführende Blechabdeckung über dem Kehlsparren oder über
    der Kehlbohle; Eindeckungsbauteil, keine Begriffsüberschneidung
    mit dem Kehlsparren.
  - **Kehlbalken** (Folgearbeit `hg_kehlbalken.md`):
    **Verwechslungsfalle**, kein Synonym. Der Kehlbalken ist der
    **horizontale Querriegel** im Kehlbalkendach, der zwei
    gegenüberliegende Sparren als Zugband oder Druckriegel
    überspannt — ein vollständig anderer Bauteilbegriff. Beide
    Begriffe stehen weder in einer Spezialisierungs- noch in einer
    Synonymie-Beziehung; die gemeinsame Wortwurzel „Kehl-" ist
    rein lexikalisch.
  - **Dachfläche** (`dachflaeche`): zweidimensionales geometrisches
    Bauteil; der Kehlsparren liegt nicht in einer einzelnen
    Dachfläche, sondern auf der Schnittgeraden zweier
    Dachflächen.
  - **Dachseite** (`dachseite`): orientierungs-annotierte
    Dachfläche; nicht selbst Träger des Kehlsparrens, sondern
    Sicht auf die Dachfläche.
  - **Firstpfette** (`firstpfette`): horizontaler Längsträger am
    First; der Kehlsparren stößt am Firstend-Punkt typisch an
    einen Firstpfetten-Knoten, ist aber kein Pfettenbauteil.
  - **Fußpfette** (`fusspfette`): horizontaler Längsträger an der
    Traufe; der Kehlsparren stößt am Trauf-Innen-Eckpunkt typisch
    an eine durchlaufende Fußpfette (nicht an einen Eck-Stoß wie
    beim Gratsparren).
  - **Kerve** (`kerve`): partitive Bearbeitung am Kehlsparren-Fuß
    auf der Fußpfetten-Stoßstelle; nicht selbst Sparren.
  - **Abkehlung** (Folgearbeit `hg_abkehlung.md`): partitive
    Bearbeitung der oberen Längskante des Kehlsparrens; nicht
    Bestandteil der Definition. Begrifflich eigenständig
    gegenüber der **Abgratung** (Bearbeitung am Gratsparren) —
    Wikipedia „Kehlsparren": „die Abgratung heißt hier Kehlung".
  - **Verschneidungssparren** (Folgearbeit
    `hg_verschneidungssparren.md`): regional unscharfer
    Oberbegriff für Grat- und Kehlsparren bzw. Schiftsparren; in
    der Schweiz und Süddeutschland selten und mehrdeutig.
  - **Schiftsparren** (`schiftsparren`, Folgearbeit): Synonym zu
    Schifter; siehe oben.

## Implementierungshinweis

Datentyp (Domänen-Schicht, Kotlin, Schicht `domain.bauteil`):

```kotlin
package domain.bauteil

import domain.Toleranzen
import domain.bauteil.Bauteil
import domain.bauteil.Bauteilachse
import domain.bauteil.BauteilId
import domain.bauteil.Kehle
import domain.geometrie.Einheitsvektor
import domain.geometrie.Punkt

/**
 * Kehlsparren als Bauteilrolle: Stab-Bauteil entlang einer
 * Kehlstrecke (geneigte konkave Schnittkante zweier Dachflächen).
 *
 * Glossar: hg_kehlsparren.md
 *
 * Asymmetrie zum Oberbegriff Sparren:
 *   Die Falllinien-Kollinearität aus hg_sparren.md Bed. 3 wird durch
 *   eine Kehllinien-Kollinearität ersetzt; statt einer einzelnen
 *   Dachfläche ist eine Kehlstrecke s_{ij} zugeordnet (Lage auf der
 *   Schnittgeraden zweier Trägerebenen).
 *
 * Symmetrie zum Schwester-Begriff Gratsparren:
 *   Auf der Linien-Ebene mathematisch exakt symmetrisch — Unterschied
 *   ausschließlich im Vorzeichen des Spatprodukts der äußeren
 *   Normalen mit der aufwärts gerichteten Tangente
 *   (positiv → Grat, negativ → Kehle). Auf der Konstruktions-Ebene
 *   asymmetrisch in Wasserführung (Kehlsparren trägt konzentrierte
 *   Niederschlags- und Schneeansammlungs-Last), Oberkanten-
 *   Bearbeitung (Abkehlung statt Abgratung) und Schifter-Topologie
 *   (Schifter von oben statt von unten).
 *
 * Vorzeichenkonvention (normativ):
 *   p_a = Kehlsparrenfuß       (am Trauf-Innen-Eckpunkt)
 *   p_e = Kehlsparrenfirstpunkt (am Firstend-Punkt der Kehllinie)
 *   d_hat_K zeigt bergauf (⟨d_hat_K, e_z⟩ > 0), kollinear zur
 *   aufwärts gerichteten Kehllinien-Tangente t_hat.
 */
data class Kehlsparren(
    val bauteil: Bauteil,
    val kehle: Kehle,                // zugeordnete Kehlstrecke (Regulaer-Variante)
) {
    init {
        require(bauteil.geometrie is Bauteilgeometrie.Stab) {
            "Kehlsparren erfordert Stabgeometrie"
        }
        // Lage- und Kehllinien-Bedingungen werden in der Factory
        // kehlsparrenAusBauteil(...) geprüft und liefern bei Verletzung
        // ein Resultat.Fehler mit KehlsparrenEntartet-Variante (siehe unten).
    }

    val kehlsparrenfuss: Punkt        get() = achse().anfang
    val kehlsparrenfirstpunkt: Punkt  get() = achse().ende
    val laenge: Double                get() = achse().laenge          // mm
    val kehlsparrenneigung: Double                                     // rad
        get() = kehle.kehlneigung()

    private fun achse(): Bauteilachse.Gerade =
        (bauteil.geometrie as Bauteilgeometrie.Stab).achse as Bauteilachse.Gerade
}

sealed class KehlsparrenEntartet {
    object NichtAufKehllinie         : KehlsparrenEntartet()
    object NichtKollinearZurTangente : KehlsparrenEntartet()
    object FalscheRichtung           : KehlsparrenEntartet()   // d_hat_K zeigt bergab
    object Nullachse                 : KehlsparrenEntartet()
    object EntarteteKehlstrecke      : KehlsparrenEntartet()
}
```

- **Einheit**: Längen in mm (Double), Winkel intern in Radiant.
- **Identität**: `BauteilId` aus dem zugrunde liegenden Bauteil.
- **Invarianten** (in der Factory `kehlsparrenAusBauteil(...)` prüfen,
  bei Verletzung `Resultat.Fehler` mit der jeweiligen
  `KehlsparrenEntartet`-Variante; niemals Exception):
  1. Stabgeometrie und Bauteilachse vom Typ `Bauteilachse.Gerade`.
  2. Achsenlänge > Toleranzen.LAENGE_EPS — sonst `Nullachse`.
  3. Zugeordnete Kehlstrecke `kehle` ist `Kehle.Regulaer` mit
     wohldefinierten Endpunkten — sonst `EntarteteKehlstrecke`.
  4. p_a und p_e liegen auf der Kehllinien-Geraden bis ε_L —
     sonst `NichtAufKehllinie`.
  5. ‖d_hat_K × t_hat‖ ≤ Toleranzen.KOLLINEAR_EPS — sonst
     `NichtKollinearZurTangente`.
     (§4 HG-Konvention: Kollinearitäts-Test über das normierte
     Kreuzprodukt mit `KOLLINEAR_EPS`, **nicht** über
     `WINKEL_EPS`.)
  6. ⟨d_hat_K, t_hat⟩ ≥ +1 − Toleranzen.WINKEL_EPS — sonst
     `FalscheRichtung` (Konsumenten können durch Achsen-Umkehr
     automatisch korrigieren).
- **Edge Cases**:
  - **Verschneidung Sattel × Sattel (T-Anbau)**: Kehlsparren endet
    am Firstend-Punkt der niedrigeren Firstlinie auf der höheren
    Hauptdachfläche; die Definition bleibt anwendbar.
  - **Verschneidung Dachgaube × Hauptdach**: zwei Kehlsparren
    seitlich der Gaube; jeder erfüllt die Definition gegen seine
    eigene Kehlstrecke.
  - **Ungleichgeneigte Verschneidung**: Reduktions-Formel (★)
    bleibt gültig mit β_plan ≠ 45°; die Definition unverändert
    anwendbar.
  - **Kehlsparren mit Verbearbeitung (Abkehlung, Absenkung,
    Anhebung)**: die Bauteilachse bleibt die geometrische
    Schwerlinie; die Bearbeitungen sind separate Geometrie-
    Modifikationen am Bauteil und nicht Bestandteil der
    Kehlsparren-Definition.
  - **Verlängerung über den Trauf-Innen-Eckpunkt hinaus**:
    p_a liegt auf einer Verlängerung der Kehllinien-Geraden
    jenseits von a_{ij}; die Definition bleibt anwendbar, sofern
    p_a auf der Geraden durch s_{ij} liegt (Bed. 2 testet
    Inzidenz auf der **Gerade** durch die Kehlstrecke, nicht
    Enthaltensein in der Strecke selbst).
  - **Sehr kleine Verschneidungsflächen / kurze Kehlstrecke**:
    bei ‖s_{ij}‖ → ε_L wird die Kehlstrecke entartet; in diesem
    Fall liefert die Factory `EntarteteKehlstrecke`.
- **Abgeleitete Eigenschaften** (als Funktionen):
  - `kehlsparrenneigung(): Double` — = Kehlneigung der
    zugeordneten Kehlstrecke, in Radiant. Es gilt
    `tan(α_K) = tan(α) · cos(β_plan)` mit α =
    `min(D_i.dachneigung(), D_j.dachneigung())` bzw. allgemein
    der dachflächen-spezifischen Falllinien-Neigung
    (Reduktions-Formel als Konsequenz, nicht als Code-
    Berechnungs-Identität).
  - `dachflaechenPaar(): Pair<Dachflaeche, Dachflaeche>` —
    die beiden zugeordneten Dachflächen (D_i, D_j).
  - `planWinkel(d: Dachflaeche): Double` — Grundrissprojektions-
    Winkel β_plan zwischen Kehllinie und Trauflinie der
    Dachfläche `d`; Bemessungs-Hilfsfunktion.
- **Bezeichner-Konvention** (CLAUDE.md): Klasse heißt `Kehlsparren`
  (deutsch, Glossarbegriff); zugeordnete Kehlstrecke ist
  `Kehle.Regulaer`.

## Quellen

**Primär (normativ):**

- SIA 232/1:2020, „Geneigte Dächer", Schweizerischer Ingenieur- und
  Architektenverein, Zürich, Abschnitt 1.
- SIA 265:2021, „Holzbau", Schweizerischer Ingenieur- und
  Architektenverein, Zürich, Abschnitt 4 und 5.
- DIN EN 1995-1-1:2010-12, „Eurocode 5: Bemessung und Konstruktion
  von Holzbauten – Teil 1-1: Allgemeines", Abschnitt 5 und 6.
- DIN 1356-1:1995-02, „Bauzeichnungen – Teil 1: Arten, Inhalte und
  Grundregeln der Darstellung", Abschnitt 5.
- DIN 18338:2019-09, „VOB Teil C: Dachdeckungs- und
  Dachabdichtungsarbeiten", Abschnitt 0.
- DIN 1052:2008-12, „Entwurf, Berechnung und Bemessung von
  Holzbauwerken", Abschnitt 8 und 12.

**Sekundär:**

- Lignum (Hrsg.): *Holzbautabellen HBT.* Lignum, Zürich, aktuelle
  Auflage.
- Lignum (Hrsg.): *Lignatec — Geneigte Dächer in Holzbauweise.*
  Lignum, Zürich, aktuelle Auflage.
- Mönck, W.; Rug, W.: *Holzbau – Bemessung und Konstruktion.*
  16. Auflage, Beuth Verlag, Berlin 2015.
- Natterer, J.; Herzog, T.; Volz, M.: *Holzbau-Atlas.* 4. Auflage,
  Birkhäuser, Basel 2003.
- Krämer, V.: *Grundwissen des Zimmerers.* Bruderverlag, Köln 2006.
- Koepf, H.; Binding, G.: *Bildwörterbuch der Architektur.*
  4. Auflage, Kröner, Stuttgart 2005, Eintrag „Kehlsparren".
- Gerner, M.: *Fachwerk – Instandsetzung, Sanierung, Neubau.*
  DVA, 7. Auflage 2007.

**Korpus (nicht autoritativ):**

- Wikipedia, Lemmata „Kehlsparren", „Schifter", „Schiftung",
  „Hexenschnitt", „Walmdach", „Dachausmittlung" (abgerufen
  2026-05-14).
- zimmerer-treff.com: „Austragung von Kehlsparren";
  „Rechnerischer Abbund Kehlsparren".
- polybau.ch (Schweiz): „Austragung Kehlsparren / rechnerischer
  Abbund" (paralleler URL-Pfad zu zimmerer-treff.com).
- Greifswalder Zimmerer: „Rechnerischer Abbund Kehlsparren".
- Bund Deutscher Zimmermeister, Handbuch „Anleitung Kehl-/
  Gratsparrengrafik" und „Kehlbohlengrafik" (zimmerer.de).
- zimmererzentrum.de DigiBAU „Austragung Kehlsparren gleiche
  Dachneigung mit Hexenschnitt".
- zimmerin.de „Dachausmittlung".
- Zimmerer-Bayern Gesellenprüfung 2019 (Kehlsparren als
  Prüfungsthema).
- baubeaver.de: „Kehlsparren".
- dachdecker.com: „Kehlsparren".
- Bemessungssoftware: Frilo DGK „Grat- und Kehlsparren"; pbs.de
  062J „Holzbau Grat- und Kehlsparren – EC5"; pcae 4H-GRAT
  „Grat- und Kehlsparren"; mb-AEC S120 „Grat- und Kehlsparren";
  Harzer-Statik „Kehlsparren"; Dietrich's „Dachbauteile /
  Kehlsparren" und Support-Blog „Verlängerung eines Kehlsparrens
  über den Kehltraufpunkt hinaus".
- Angelsächsische Valley-Rafter-Literatur: carpentrycompendium.com
  „Valley Rafters" („The top of the unbacked valley rafter rises
  slightly above the geometric intersection and must be cut off.");
  prebuiltml.com; yourownarchitect.com; roofobservations.com;
  sbebuilders.blogspot.com (für die Reduktions-Formel und
  „backing angle for valley" / „dropping the valley" als
  konstruktive Pendants zu Abkehlung und Absenkung).

**Nicht verifizierbar (negativer Befund):**

- Lignum HBT (aktuelle Auflage), spezifische Begriffsbelegung
  „Kehlsparren"; online nicht volltext-indiziert.
- Lignatec „Geneigte Dächer in Holzbauweise", spezifische
  Begriffsbelegung „Kehlsparren"; online nicht volltext-indiziert.
- SIA 261:2020 Lastfall „Schneeanhäufung in Kehlen" — Existenz
  vermutet, spezifische Stelle nicht direkt zitiert.
- Direkte Volltextstellen Mönck/Rug, Natterer Holzbau-Atlas,
  Blass/Sandhaas, Gerner, Krämer für „Kehlsparren" — nur über
  Inhaltsverzeichnis bestätigt.
- Koepf/Binding-Eintragstext „Kehlsparren": Pendant zum (wörtlich
  zitierten) Gratsparren-Eintrag vermutet, nicht direkt zitierbar.
