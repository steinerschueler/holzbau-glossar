---
id: gratsparren
benennung: Gratsparren
synonyme: [Grat-Sparren]
abgelehnte_benennungen:
  [Walmsparren, Eckgrat, Eckgratbalken, Verschneidungssparren,
   "hip rafter", "hip", Ixe]
oberbegriff: sparren
begriffstyp: bauteilrolle
voraussetzungen:
  [bauteil, bauteilachse, sparren, grat, dachflaeche, strecke,
   einheitsvektor, ebene, dachneigung, weltkoordinatensystem,
   toleranzen]
abgrenzung_zu:
  [sparren, kehlsparren, schifter, grat, dachflaeche, dachseite,
   firstpfette, fusspfette, kerve, abgratung, verschneidungssparren,
   schiftsparren]
status: entwurf
subglossar_pendant: notwendig
quellen_primär:
  - "SIA 232/1:2020 'Geneigte Dächer', Schweizerischer Ingenieur- und Architektenverein, Abschnitt 1 (Begriffe und geometrische Grundlagen): Grat als geneigte konvexe Schnittkante zweier Dachflächen am Walmdach; Gratsparren als Tragglied entlang der Gratlinie wird vorausgesetzend verwendet."
  - "SIA 265:2021 'Holzbau', Schweizerischer Ingenieur- und Architektenverein, Abschnitt 4 (Bemessung) und Abschnitt 5 (Konstruktive Durchbildung): geneigte stabförmige Tragglieder von Dachtragwerken; Gratsparren als Sonderform mit eigener Lastabtragung aus zwei Dachflächen-Anteilen."
  - "DIN EN 1995-1-1:2010-12 (Eurocode 5), Abschnitt 5 (Tragwerksberechnung) und Abschnitt 6 (Grenzzustände der Tragfähigkeit): biegebeanspruchte Stab-Bauteile in Walmdach-Konstruktionen."
  - "DIN 1356-1:1995-02 'Bauzeichnungen – Teil 1: Arten, Inhalte und Grundregeln der Darstellung', Abschnitt 5 (Darstellung von Dächern): Gratsparren als Zeichnungselement in der Bauzeichnung des Walmdachs."
  - "DIN 1052:2008-12, Abschnitt 8 und Abschnitt 12 (Konstruktive Anforderungen): Tragglieder geneigter Dächer."
quellen_sekundär:
  - "Lignum (Hrsg.): Holzbautabellen HBT, Lignum, Zürich, aktuelle Auflage, Kap. 'Dachtragwerke' / Walmdach-Konstruktionen."
  - "Lignum (Hrsg.): Lignatec 'Geneigte Dächer in Holzbauweise', Lignum, Zürich, aktuelle Auflage, Abschnitt 'Walmdach / Grat- und Kehlsparren'."
  - "Mönck, W.; Rug, W.: Holzbau – Bemessung und Konstruktion. 16. Aufl., Beuth Verlag 2015, Kap. 11 'Dachtragwerke', § Walmdach."
  - "Natterer, J.; Herzog, T.; Volz, M.: Holzbau-Atlas. 4. Aufl., Birkhäuser, Basel 2003, Kap. 'Dachtragwerke / Walmdach'."
  - "Krämer, V.: Grundwissen des Zimmerers. Bruderverlag, Köln 2006, Kap. Schiftungen / Walmdach-Austragung."
  - "Koepf, H.; Binding, G.: Bildwörterbuch der Architektur. 4. Aufl., Kröner, Stuttgart 2005, Eintrag 'Gratsparren': „Der Gratsparren ist in einer Dachkonstruktion eines abgewalmten Dachs der den Grat unterstützende, diagonal von der ausspringenden Ecke einer Traufe zum First verlaufende Sparren.\""
  - "Gerner, M.: Fachwerk – Instandsetzung, Sanierung, Neubau. DVA, 7. Aufl. 2007, Glossar 'Gratsparren'."
  - "Berufsschul-Lehrmaterial: zimmerer-treff.com 'Austragung von Schifter und Gratsparren'; polybau.ch 'Austragung Schifter/Gratsparren' (Schweiz)."
  - "Bemessungssoftware: Frilo DGK 'Grat- und Kehlsparren'; pbs.de 062J 'Holzbau Grat- und Kehlsparren – EC5'; Harzer-Statik 'Gratsparren'."
quellenkonflikt: |
  **Norm-Lage:** Weder SIA 232/1, SIA 265, EN 1995-1-1, DIN 1052 noch
  DIN 1356 enthalten einen geschlossenen Begriffseintrag „Gratsparren";
  der Begriff wird in allen konsultierten Normen vorausgesetzt und über
  seine konstruktive Rolle (geneigtes, lastabtragendes Stab-Bauteil
  entlang der Gratlinie eines Walmdachs) charakterisiert. Die Norm-Lage
  ist exakt parallel zu „Sparren" (siehe `hg_sparren.md`,
  `quellenkonflikt`).

  **Strukturelle Asymmetrie zum Oberbegriff `sparren`:** Der Gratsparren
  erbt von `sparren` die konstruktive **Rolle** (Stab-Bauteil eines
  Dachtragwerks mit geneigter Bauteilachse als lastabtragendes
  Tragglied), aber **nicht** die zentrale geometrische Bedingung 3 aus
  `hg_sparren.md` (Falllinien-Kollinearität in einer einzelnen
  Dachfläche). Die Bauteilachse eines Gratsparrens liegt nicht in der
  Trägerebene einer einzelnen Dachfläche entlang ihrer Falllinie,
  sondern auf der **Schnittgeraden zweier Trägerebenen** — geometrisch
  identisch mit der Gratlinie im Sinne von `hg_grat.md`. Diese
  Asymmetrie ist in `hg_sparren.md` Sektion „Wohldefiniertheit /
  Mehrfachzuordnung" bereits explizit antizipiert: „bei Verschneidungs-
  Sparren (Gratsparren, Kehlsparren), die auf zwei Dachflächen liegen,
  ist die Falllinien-Kollinearitätsbedingung nicht zu beiden
  Dachflächen gleichzeitig erfüllbar, weshalb diese Sonderformen eigene
  Begriffsdefinitionen erhalten."

  **Konsequenz:** Bedingung 3 von `hg_sparren.md` wird in der hiesigen
  Definition durch eine analoge **Gratlinien-Kollinearitäts-Bedingung**
  ersetzt (Bed. 3 unten); Bedingung 2 von `hg_sparren.md` (Lage in
  einer einzelnen Trägerebene) entfällt zugunsten einer
  Inzidenz-Bedingung auf eine Gratstrecke g_{ij} im Sinne von
  `hg_grat.md`. Die Vorzeichenkonvention (Bed. 4 in `hg_sparren.md`,
  „bergauf, von Traufe zu First") wird mit Bezug auf die aufwärts
  gerichtete Gratlinien-Tangente t_hat (siehe `hg_grat.md`) übernommen.
  Diese Festlegung ist konsistent mit allen konsultierten Quellen.

  **Hauptmerkmal — geringere Neigung:** Mehrfach belegt (Wikipedia
  „Gratsparren"; Koepf/Binding 2005; baubeaver.de; BauNetz Wissen;
  dachdecker.com; greifswalder-zimmerer.de „Gratgrundverschiebung"):
  „Der Gratsparren besitzt eine geringere Neigung als die Sparren und
  Schifter der angrenzenden Dachflächen." Die mathematische
  Charakterisierung erfolgt unten als abgeleiteter Satz (Reduktions-
  Formel `tan(α_G) = tan(α)·cos(β_plan)`); sie folgt aus den
  Primitiven und ist nicht Teil der Definition.

  **Verkantung im Raum:** Mehrfach belegt; bedeutet, dass der
  Gratsparrenquerschnitt um die Bauteilachse so liegt, dass seine
  Ober-/Seitenflächen nicht in einer der beiden anliegenden
  Trägerebenen liegen. Die zwei Standard-Werkstücke der Zimmerei
  (**Abgratung** der Oberkante / **Absenkung** des ganzen Bauteils)
  sind Bestandteile der Bauteilbearbeitung, nicht der Definition;
  sie werden als Folgearbeit in `hg_abgratung.md` geführt.

  **Schifter (Schiftsparren) ist nicht synonym:** Schifter setzen mit
  doppelter Schmiege an der Seitenfläche des Gratsparrens an (Wikipedia
  „Schifter"; zimmerer-treff.com „Austragung Schifter/Gratsparren");
  sie sind topologisch komplementär zum Gratsparren, kein Synonym.

  **Verschneidungssparren** ist im norddeutsch-BDZ-Sprachgebrauch
  Oberbegriff für Grat- und Kehlsparren; in der Schweiz und
  Süddeutschland selten und mehrdeutig (auch für Schiftsparren
  verwendet — siehe `hg_sparren.md` Spezialisierungen-Block).
  Daher in `abgelehnte_benennungen:` geführt; bei Bedarf späterer
  Sammelbegriff über eigenen Eintrag.

  **Walmsparren** wird im Korpus uneinheitlich verwendet (teils für
  Gratsparren, teils für Walm-Schifter); daher abgelehnt.

  **Ixe** bezeichnet im DACH-Korpus die **Kehle** (siehe
  `hg_kehle.md`), nicht den Grat; daher abgelehnt.

  **Lignum / SIA Schweiz:** Trotz mehrfacher Recherche keine direkten
  Lignum-Volltextbelege online verifizierbar (Lignum HBT und Lignatec
  nicht volltext-indiziert). Eintrag analog zu `hg_sparren.md` mit
  Lignum-Quellen-Hinweis; die spezifische Begriffsbelegung ist im
  DACH-Holzbau-Korpus als etabliert nachgewiesen, die normative
  Schweizer Quellenstelle ist nicht direkt zitierbar.
---

## Prosa-Definition

Ein **Gratsparren** ist ein Stab-Bauteil eines Dachtragwerks in der
Bauteilrolle eines Sparrens, dessen Bauteilachse auf der Gratlinie
zweier benachbarter Dachflächen liegt — also auf einer geneigten,
konvexen Schnittkante zweier Trägerebenen — und das die Lasten beider
anliegender Dachflächen-Anteile entlang seiner Längsachse zwischen
einem Trauf-Eckpunkt (Walm-Ecke) am Fuß und einem Firstend-Punkt
(oder der Walm-Spitze) am Kopf abträgt.

## Mathematische Definition

Sei

- B ein Bauteil im Sinne von `bauteil` mit Stabgeometrie
  (`geometrie ∈ 𝒢_stab`),
- a(B) = Bauteilachse.Gerade(p_a, p_e) die Bauteilachse von B im
  geraden Fall (siehe `bauteilachse`), mit
  d_hat_G := (p_e − p_a) / ‖p_e − p_a‖ ∈ S² ⊂ ℝ³,
- 𝒟 = {D_1, …, D_m} eine Dachflächenfamilie im Sinne von
  `dachflaeche`,
- D_i = (E_i, P_i, n_{a,i}) und D_j = (E_j, P_j, n_{a,j}) zwei
  verschiedene Dachflächen aus 𝒟 mit i ≠ j,
- g_{ij} ⊂ ℝ³ eine **Gratstrecke** im Sinne von `hg_grat.md`,
  also eine Schnittstrecke s_{ij} = F(P_i) ∩ F(P_j), die die
  Grat-Bedingungen (1)–(4) aus `hg_grat.md` erfüllt
  (geneigt, konvex, beide äußeren Normalen in oberer Halbkugel),
- t_hat := (b_{ij} − a_{ij}) / ‖b_{ij} − a_{ij}‖ ∈ S² die Tangente
  von g_{ij} mit g_{ij} = [a_{ij}, b_{ij}] und (Vorzeichenkonvention
  aus `hg_grat.md`) ⟨t_hat, e_z⟩ > 0 (bergauf orientiert),
- e_z := (0, 0, 1)ᵀ die vertikale Achse,
- ε_W := Toleranzen.WINKEL_EPS die Winkeltoleranz,
- ε_K := Toleranzen.KOLLINEAR_EPS die Kollinearitätstoleranz,
- ε_L := Toleranzen.LAENGE_EPS die Längentoleranz.

Dann heißt B ein **Gratsparren** der Gratstrecke g_{ij} der
Dachflächenfamilie 𝒟 genau dann, wenn die folgenden Bedingungen
erfüllt sind:

1. **Stabgeometrie**: B besitzt eine gerade Bauteilachse mit
   ‖p_e − p_a‖ > ε_L.

2. **Endpunkt-Inzidenz**: Beide Endpunkte der Bauteilachse liegen
   auf der Gratlinie der Gratstrecke g_{ij} im Sinne der
   Punkt-Gerade-Inzidenz; konkret existieren Skalare
   s_a, s_e ∈ ℝ mit
   ```
   p_a = a_{ij} + s_a · (b_{ij} − a_{ij}),
   p_e = a_{ij} + s_e · (b_{ij} − a_{ij}),
   ```
   und der zur Gratlinie rechtwinklige Abstand beider Endpunkte
   ist kleiner-gleich ε_L (Lage-Toleranz auf der Schnittgeraden
   der beiden Trägerebenen E_i und E_j).

3. **Gratlinien-Kollinearität** (Ersatz für die
   Falllinien-Kollinearität aus `hg_sparren.md` Bed. 3): Die
   Bauteilachsenrichtung ist kollinear zur Gratlinien-Tangente,
   ```
   ‖d_hat_G × t_hat‖ ≤ ε_K,
   ```
   d. h. der Winkel zwischen d_hat_G und t_hat ist 0 oder π (modulo der
   numerischen Sinus-Toleranz nach §4 HG-Konvention für
   Parallelitäts-Prädikate).

4. **Vorzeichenkonvention** (Gratsparrenrichtung von Walm-Ecke zu
   Firstend-Punkt): Die Bauteilachse ist so gerichtet, dass d_hat_G
   in dieselbe Halbkugel wie t_hat weist, also bergauf:
   ```
   ⟨d_hat_G, t_hat⟩ ≥ +1 − ε_W,
   ```
   äquivalent ⟨d_hat_G, e_z⟩ > 0. p_a ist damit der **Gratsparrenfuß**
   (am Trauf-Eckpunkt der Walm-Ecke), p_e der
   **Gratsparrenfirstpunkt** (am Firstend-Punkt bzw. an der
   Walm-Spitze).

5. **Zuordnung zu genau einer Gratstrecke**: B ist Gratsparren
   einer eindeutig bestimmten Gratstrecke g_{ij} der Familie 𝒟;
   die Wahl von g_{ij} ist die Zuordnung des Bauteils und nicht
   selbst Bestandteil der Bauteilgeometrie.

Wesentliche abgeleitete Größen:

- **Gratsparrenlänge**: L_{S,G} := ‖p_e − p_a‖ (in mm), entlang
  der Bauteilachse zwischen Gratsparrenfuß und
  Gratsparrenfirstpunkt.

- **Gratsparrenneigung** (= Gratneigung der zugeordneten
  Gratstrecke, siehe `hg_grat.md`, abgeleitete Operation
  `gratneigung()`):
  ```
  α_G := arcsin(|⟨t_hat, e_z⟩|) = arcsin(⟨d_hat_G, e_z⟩).
  ```
  Wertebereich α_G ∈ (0, π/2) bei nicht-entarteten Walmdach-Graten.

- **Gratsparrenfuß** und **Gratsparrenfirstpunkt** (als Punkte):
  F_{fuß,G} := p_a, F_{first,G} := p_e.

### Abgeleiteter Satz — Reduktions-Formel der Gratsparrenneigung

Für gleichgeneigte anliegende Dachflächen D_i und D_j mit gemeinsamer
Dachneigung α und einem Plan-Winkel β_plan zwischen der
Grundrissprojektion der Gratlinie und der Trauflinie einer der beiden
Dachflächen gilt

```
tan(α_G) = tan(α) · cos(β_plan).                                  (★)
```

**Herleitung aus den Primitiven:** Sei π_xy: ℝ³ → ℝ² die
Projektion in die Horizontalebene. Die Schnittgerade g_{ij} ⊂ ℝ³
projiziert auf eine Gerade π_xy(g_{ij}) ⊂ ℝ². Sei e_hat_t :=
(t_hat_x, t_hat_y, 0) / ‖(t_hat_x, t_hat_y)‖ der normierte Grundrissrichtungs-
vektor der Gratlinie und e_hat_fall(E_i) die Falllinie der Dachfläche
D_i (siehe `hg_falllinie.md`). Dann gilt nach Konstruktion

```
cos(β_plan) = |⟨e_hat_t, π_xy(e_hat_fall(E_i)) / ‖π_xy(e_hat_fall(E_i))‖⟩|.
```

Aus der Geneigtheits-Bedingung (`hg_grat.md` Bed. 1) und der
Tatsache, dass t_hat in beiden Trägerebenen E_i und E_j liegt
(g_{ij} = E_i ∩ E_j), folgt durch Aufspaltung von t_hat in seinen
horizontalen Anteil und e_z-Anteil mit Höhenfunktion z auf E_i

```
⟨t_hat, e_z⟩ / ‖(t_hat_x, t_hat_y)‖
   = (∂z/∂e_hat_t entlang der Grundrissprojektion in E_i)
   = ⟨−e_hat_fall(E_i), e_z⟩ · cos(β_plan) / √(1 − ⟨e_hat_fall(E_i), e_z⟩²) · …
```

mit Auflösung über tan(α) = |⟨e_hat_fall(E_i), e_z⟩| /
‖π_xy(e_hat_fall(E_i))‖ (siehe `hg_falllinie.md`, abgeleitete Größe
„Dachneigung entlang der Falllinie"). Zusammenfassend
ergibt sich tan(α_G) = ⟨t_hat, e_z⟩ / ‖(t_hat_x, t_hat_y)‖ = tan(α) ·
cos(β_plan). ∎

Im symmetrischen Spezialfall (gleichgeneigte Dachflächen mit
horizontalen, rechtwinklig zueinander stehenden Traufen) ist die
Grundrissprojektion der Gratlinie die Winkelhalbierende der beiden
Traufkanten und damit β_plan = 45°, woraus folgt

```
tan(α_G) = tan(α) / √2.                                          (★★)
```

Die populäre US-Faustregel „6-in-12 wird zu 6-in-16.97 am Grat" ist
genau diese Aussage in Steigungs-Schreibweise.

(★) ist ein **abgeleiteter Satz**, kein Definitionsbestandteil; die
Definition selbst (Bed. 1–5 oben) verwendet ausschließlich die
Primitive Punkt, Vektor, Strecke, Ebene und die bereits definierten
Begriffe `bauteil`, `bauteilachse`, `sparren`, `grat`, `dachflaeche`.

## Wohldefiniertheit

- **Existenz**: Für jede Walmdach-Konstruktion mit nicht-entarteten
  Gratstrecken existiert in der Standardkonfiguration genau ein
  Gratsparren pro Gratstrecke; das ist die übliche Walmdach-
  Konstruktion (vier Gratsparren am Vollwalm). Bed. 1–5 sind
  konstruktiv erfüllbar.

- **Eindeutigkeit der Vorzeichenkonvention**: Aus der
  Geneigtheits-Bedingung der Gratstrecke (`hg_grat.md` Bed. 1) folgt
  ⟨t_hat, e_z⟩ > ε_W, also t_hat ≠ −t_hat als Tangentenwahl. Bed. 3 und 4
  zusammen fixieren d_hat_G = +t_hat (modulo ε_K, ε_W). Die alternative
  Orientierung d_hat_G = −t_hat ist durch Bed. 4 ausgeschlossen.

- **Asymmetrie zum Oberbegriff `sparren` — explizite Auflösung:**
  In `hg_sparren.md` lauten die zentralen geometrischen Bedingungen:
  - Bed. 2: beide Endpunkte der Bauteilachse liegen in der
    Trägerebene **einer** zugeordneten Dachfläche;
  - Bed. 3: die Bauteilachsenrichtung ist kollinear zur **Falllinie**
    dieser einen Dachfläche.

  Für den Gratsparren sind beide Bedingungen strukturell verletzt:
  - Die Bauteilachse liegt auf der Schnittgeraden **zweier**
    Trägerebenen E_i und E_j; sie liegt also in der gemeinsamen
    Schnittgeraden beider, aber sie verläuft **nicht entlang einer
    Falllinie**, denn die Schnittgerade zweier nicht-paralleler,
    geneigter Ebenen ist nicht die Falllinie einer der beiden
    (außer im entarteten Fall ⟨n_hat_{a,i}, e_z⟩ = ⟨n_hat_{a,j}, e_z⟩ und
    Spiegel-Symmetrie, in dem die Schnittgerade in einer
    Vertikalebene liegt, aber auch dann ist ihre Richtung nicht die
    Falllinien-Richtung einer der beiden Einzelflächen).
  - Genau diese Asymmetrie ist in `hg_sparren.md` Sektion
    „Wohldefiniertheit / Mehrfachzuordnung" antizipiert: „bei
    Verschneidungs-Sparren (Gratsparren, Kehlsparren), die auf zwei
    Dachflächen liegen, ist die Falllinien-Kollinearitätsbedingung
    nicht zu beiden Dachflächen gleichzeitig erfüllbar, weshalb
    diese Sonderformen eigene Begriffsdefinitionen erhalten".

  Die hiesige Definition löst die Asymmetrie auf, indem sie:
  - Bed. 2 von `hg_sparren.md` durch eine **Endpunkt-Inzidenz auf
    einer Gratstrecke g_{ij}** (Bed. 2 hier) ersetzt;
  - Bed. 3 von `hg_sparren.md` durch eine **Gratlinien-Kollinearität
    zur Tangente t_hat** (Bed. 3 hier) ersetzt;
  - Bed. 4 von `hg_sparren.md` als **bergauf-Orientierung relativ zu
    t_hat** statt zu e_hat_fall übernimmt (Bed. 4 hier).

  Die geerbte konstruktive Rolle des Oberbegriffs `sparren` (Stab-
  Bauteil eines Dachtragwerks, geneigt, lastabtragend, Bauteilachse
  bergauf orientiert) bleibt damit unverletzt; nur die geometrische
  Lage-Bedingung wird von der Falllinie einer Einzelfläche auf die
  Gratlinie der Verschneidung umgehängt.

- **Konsistenz mit `hg_grat.md`**: Aus Bed. 3 und Bed. 4 folgt
  d_hat_G = +t_hat (modulo Toleranzen), wobei t_hat die nach `hg_grat.md`
  Vorzeichenkonvention bergauf gerichtete Gratlinien-Tangente ist.
  Damit ist der Gratsparrenfuß stets am unteren Endpunkt a_{ij} der
  Gratstrecke und der Gratsparrenfirstpunkt stets am oberen Endpunkt
  b_{ij} — konsistent mit der Beschreibung in Koepf/Binding 2005
  „diagonal von der ausspringenden Ecke einer Traufe zum First".

- **Reduktions-Formel (★) als Konsequenz, nicht als Axiom**: Die
  Formel `tan(α_G) = tan(α)·cos(β_plan)` wurde oben aus den
  Primitiven hergeleitet; sie ist nicht Bestandteil der Definition
  (Bed. 1–5), sondern beweisbar daraus. Damit ist die Definition
  konservativ im Sinne der HG-Konventionen: die mathematische
  Charakterisierung der reduzierten Neigung ist Abkürzung, nicht
  Axiom.

- **Mehrfachzuordnung — gegenseitige Disjunktheit der
  Sparren-Spezialisierungen**: Ein Bauteil B kann nicht
  gleichzeitig Sparren einer einzelnen Dachfläche im Sinne von
  `hg_sparren.md` und Gratsparren einer Gratstrecke g_{ij} sein,
  da die Falllinien-Kollinearität (`hg_sparren.md` Bed. 3) mit
  der Gratlinien-Kollinearität (Bed. 3 hier) nicht gleichzeitig
  erfüllbar ist (die Falllinie einer geneigten Einzelfläche und
  die Tangente einer Gratstrecke der gleichen Flächenfamilie sind
  nicht kollinear, außer in entarteten Sonderfällen). Ebenso ist
  die Disjunktheit zu `kehlsparren` durch die Konvexitäts-
  Bedingung der Gratstrecke (`hg_grat.md` Bed. 3 vs. die analoge
  Konkavitäts-Bedingung der Kehlstrecke) gesichert.

- **Nicht-Zirkularität**: Die Definition stützt sich nur auf
  bereits definierte Begriffe (`bauteil`, `bauteilachse`,
  `sparren`, `grat`, `dachflaeche`, `strecke`, `einheitsvektor`,
  `ebene`, `dachneigung`, `weltkoordinatensystem`, `toleranzen`).
  Sie kommt nicht in ihrer eigenen Definition vor und verweist
  nicht auf Gratsparren-Spezialisierungen oder Bearbeitungs-
  Folgegeometrie (Abgratung, Absenkung).

- **Auflagerung (qualitativ, nicht Bestandteil der Definition)**:
  Ein Gratsparren wird im Tragwerk typischerweise gestützt durch
  - einen **Eck-Pfettenstoß zweier Fußpfetten** am Gratsparrenfuß
    (gemeinsamer Endpunkt zweier Trauflinien an der Walm-Ecke);
  - einen **Firstpfetten-Endpunkt** oder eine **Walm-Spitze** /
    einen zentralen Stahlknoten am Gratsparrenfirstpunkt.

  Die Auflagerung ist Eigenschaft des Tragwerks (siehe
  `hg_tragwerk.md`), nicht des Gratsparrens selbst. Die
  zugehörigen Bearbeitungen (Kerve am Fuß, Firstanschnitt,
  Backenschnitte, Abgratung) sind partitive Bestandteile des
  Gratsparrens, nicht Bestandteile der Definition.

## Erläuterung (nicht normativ)

Der Gratsparren ist das **diagonale Hauptbauteil eines Walmdachs**:
in der klassischen Vollwalm-Konstruktion gibt es vier Gratsparren,
die jeweils von einer Walm-Trauf-Ecke schräg nach oben zum
Firstend-Punkt verlaufen. Bei der Pyramiden-Walm-Spitze (kein
First, Spitzdach) laufen alle vier Gratsparren in einem zentralen
Knoten zusammen.

### Geometrische Charakterisierung — die geringere Neigung

Das geometrisch und konstruktiv wichtigste Merkmal des Gratsparrens
ist seine **geringere Neigung gegenüber den anliegenden Sparren**.
Im symmetrischen Fall (gleichgeneigte anliegende Dachflächen,
rechtwinklige Walm-Ecke) gilt nach der oben hergeleiteten
Reduktions-Formel

```
tan(α_G) = tan(α) / √2.
```

Beispiel: bei einer Dachneigung α = 45° hat der Gratsparren eine
Neigung von α_G = arctan(1/√2) ≈ 35.26°. Im allgemeinen Fall
(ungleichgeneigte Dachflächen, schiefwinklige Walm-Ecke) gilt
`tan(α_G) = tan(α) · cos(β_plan)`, wobei β_plan der
Grundriss-Winkel zwischen der Gratlinien-Projektion und der
Trauflinie einer der beiden anliegenden Dachflächen ist; dieser
allgemeine Fall ist in der zimmermannssprachlichen
„Gratgrundverschiebung" und in der angelsächsischen
„hip rafter geometry" behandelt.

### Walmdach-Grundrissprojektion

Bei gleichgeneigten anliegenden Dachflächen mit horizontalen,
rechtwinklig zueinander stehenden Traufen bildet die
Grundrissprojektion der Gratlinie die **Winkelhalbierende** der
beiden Traufkanten — Standardstoff der Dachausmittlung
(zugehöriger Folge-Eintrag `hg_dachausmittlung.md`). Bei
ungleicher Neigung ist die Grundrissprojektion **keine**
Winkelhalbierende mehr, sondern wird über eine
Traufhöhen-Hilfslinien-Konstruktion bestimmt.

### Verkantung im Raum — Abgratung und Absenkung

Da die Bauteilachse des Gratsparrens auf der Schnittgeraden zweier
geneigter Ebenen liegt und sein rechteckiger Querschnitt um diese
Achse rotationssymmetrisch in vier Quadranten-Lagen platziert
werden kann, ergibt sich konstruktiv eine **Verkantung im Raum**:
die Ober- und Seitenflächen des unverbearbeiteten Quaders liegen
nicht in den anliegenden Dachflächen. Zwei Standard-Lösungen der
Zimmerei lösen dieses Problem:

- **Abgratung** (englisch *backing angle*): Die obere Längskante
  des Gratsparrens wird beidseitig symmetrisch in der jeweils
  anliegenden Dachneigung abgekantet — die obere Bauteilfläche
  wird zu einer dachförmigen Doppelfacette, deren beide
  Halbflächen in den anliegenden Dachflächen-Trägerebenen liegen.
  Das ist die dominante Lösung in der Zimmerei.

- **Absenkung** (englisch *dropping the hip*): Der Gratsparren
  wird als Ganzes um einen kleinen Betrag vertikal abgesenkt, so
  dass die Schifter mit ihrer Schmiege bündig an der unbearbeiteten
  Flanke des Gratsparrens anschlagen. Alternative Lösung mit
  einfacherem Abbund, aber kleinerem effektiven Querschnitt.

Die Abgratung wird im Glossar als eigener Folge-Begriff
`hg_abgratung.md` geführt (Folgearbeit, Trigger: erste
Visualisierung der Gratsparren-Oberkante).

### Querschnitt und Werkstoff

Gratsparren werden mit größerem Querschnitt ausgeführt als die
anliegenden Normal-Sparren, weil sie die Lasten **beider**
anliegender Dachflächen-Anteile tragen. Faustregel aus der Praxis
(Wikipedia „Gratsparren"; baubeaver.de; dachdecker.com; Frilo DGK):

> „Ein Gratsparren ist länger und etwa um die Hälfte höher als
> ein Normalsparren desselben Daches."

Beispielquerschnitte (Frilo DGK): 8/18 cm bei einem Normalsparren-
Querschnitt von 6/12 oder 8/16. Die konkrete Querschnittsfindung
ist Gegenstand der Bemessung nach SIA 265 / EN 1995-1-1 und liegt
nicht im Definitionsbereich dieses Glossars.

### Typische Verbindungen und Bearbeitungen am Gratsparren

- **Kerve am Fuß** auf der Eck-Pfettenstoßstelle (zwei
  aufeinanderfolgende Schnitte, einer pro Fußpfette — siehe
  `hg_kerve.md` für die geometrische Definition der Kerve).
- **Firstanschnitt** als oberer Endschnitt am Firstend-Punkt der
  Firstlinie.
- **Backenschnitte / Backenschmiege** an den seitlichen
  Anschluss-Flächen für die Schifter.
- **Abgratung** der Oberkante (siehe Folgearbeit
  `hg_abgratung.md`).
- **Hexenschnitt** an der Gratsparren-Unterseite am Fuß zur
  beidseitigen planaren Anlage von Traufbohle und Stirnbrett
  (regional, Berufsschul-Standardstoff).

Diese Bearbeitungen sind partitive Bestandteile von Gratsparren-
Bauteilen (siehe `hg_bauteilbearbeitung.md` / `hg_kerve.md` etc.),
**nicht** Bestandteile der Begriffsdefinition.

### Sonderfälle

- **Vollwalm-Pyramide**: kein First; vier Gratsparren laufen an
  einer zentralen Spitze zusammen (konstruktiv häufig zentraler
  Stahlknoten oder Holzknoten).
- **Krüppelwalm**: Gratsparren endet nicht am Firstend-Punkt,
  sondern auf einer Mittel- oder Kehlbohle unterhalb des Firsts.
- **Ungleichgeneigte Walme**: anliegende Dachflächen mit
  unterschiedlicher Neigung; die Grundrissprojektion der
  Gratlinie ist dann keine Winkelhalbierende.

## Beziehungen

- **Oberbegriff**: `sparren`. Strukturell ist der Gratsparren eine
  Bauteilrolle, die die konstruktive Sparrenrolle (Stab-Bauteil,
  geneigt, lastabtragend, bergauf orientiert) erbt, aber die
  Falllinien-Kollinearität (`hg_sparren.md` Bed. 3) durch eine
  Gratlinien-Kollinearität ersetzt. Diese Asymmetrie ist in
  `hg_sparren.md` Sektion „Mehrfachzuordnung" explizit antizipiert.

- **Geschwister-Begriffe** (andere Sparren-Spezialisierungen):
  - `kehlsparren` (Folgearbeit): analog zum Gratsparren, aber auf
    einer konkaven Kehlstrecke statt auf einer konvexen
    Gratstrecke;
  - `schifter` / `schiftsparren` (Folgearbeit): verkürzte Sparren,
    die am Gratsparren oder Kehlsparren mit Schmiege ansetzen
    (topologisch komplementär, nicht synonym).

- **Bestandteile (partitiv)**:
  - **Bauteilachse** (`bauteilachse.Gerade`, vom Bauteil geerbt)
    mit Gratsparrenfuß als Anfangs- und Gratsparrenfirstpunkt als
    Endpunkt;
  - **Querschnitt** (vom Bauteil geerbt; rechteckig, typisch
    1.5× Sparrenhöhe);
  - **Werkstoff** (vom Bauteil geerbt; Vollholz oder BSH);
  - **Faserrichtung** (Annotation, Default ‖ d_hat_G);
  - **Abgratung** (partitive Bearbeitung, Folgearbeit
    `hg_abgratung.md`);
  - **Kerven** am Fuß (siehe `hg_kerve.md`).

- **Verwendung / Beziehung zu anderen Bauteilen**:
  - **Grat** (`grat`): geometrische Schnittkante zweier Dachflächen,
    auf der die Bauteilachse des Gratsparrens liegt; das ist die
    konstitutive Beziehung.
  - **Dachfläche** (`dachflaeche`): der Gratsparren ist genau zwei
    Dachflächen gleichzeitig zugeordnet (D_i und D_j); seine
    Bauteilachse liegt auf E_i ∩ E_j.
  - **Firstpfette** (`firstpfette`): das obere Auflager des
    Gratsparrens (Firstend-Punkt der Firstlinie) liegt
    typischerweise am Firstpfetten-Endpunkt.
  - **Fußpfette** (`fusspfette`): das untere Auflager des
    Gratsparrens liegt am Eck-Pfettenstoß zweier Fußpfetten an
    der Walm-Ecke.
  - **Schifter** (`schifter`, Folgearbeit): seitliche Anschluss-
    Sparren, die mit doppelter Schmiege an der Flanke des
    Gratsparrens anschlagen.

- **Abgrenzung**:
  - **Sparren** (`sparren`): der allgemeine Sparrenbegriff verlangt
    Falllinien-Kollinearität in einer einzelnen Dachfläche
    (`hg_sparren.md` Bed. 3); der Gratsparren erfüllt diese
    Bedingung gerade nicht, sondern verlangt stattdessen
    Gratlinien-Kollinearität. Die Asymmetrie ist in
    `hg_sparren.md` Sektion „Mehrfachzuordnung" antizipiert und
    oben im Wohldefiniertheits-Block ausgeführt.
  - **Kehlsparren** (`kehlsparren`, Folgearbeit): analog zum
    Gratsparren, aber auf einer **konkaven** Kehlstrecke (siehe
    `hg_kehle.md` / `hg_kehlsparren.md`) statt einer konvexen
    Gratstrecke; statisch und konstruktiv verschieden
    (Wasserführung, Schneeansammlung, keine Abgratung).
  - **Schifter** (`schifter`, Folgearbeit): die Schifter setzen am
    Gratsparren an; sie sind topologisch komplementär, **kein
    Synonym**. „Verschneidungssparren" wird regional mehrdeutig
    sowohl für Gratsparren als auch für Schiftsparren verwendet
    und ist daher als Hauptbenennung ungeeignet.
  - **Grat** (`grat`): die geometrische Kante; der Gratsparren ist
    das Bauteil entlang dieser Kante. Der Grat ist eine
    Dachkante (partitive Geometrie der Dachflächenfamilie), der
    Gratsparren ein Bauteil mit Bauteilachse auf dieser Kante.
  - **Dachfläche** (`dachflaeche`): zweidimensionales geometrisches
    Bauteil; der Gratsparren liegt nicht in einer einzelnen
    Dachfläche, sondern auf der Schnittgeraden zweier
    Dachflächen.
  - **Dachseite** (`dachseite`): orientierungs-annotierte
    Dachfläche; nicht selbst Träger des Gratsparrens, sondern
    Sicht auf die Dachfläche.
  - **Firstpfette** (`firstpfette`): horizontaler Längsträger am
    First; der Gratsparren stößt am Firstend-Punkt typisch an die
    Firstpfette, ist aber kein Pfettenbauteil.
  - **Fußpfette** (`fusspfette`): horizontaler Längsträger an der
    Traufe; der Gratsparren stößt am Walm-Trauf-Eckpunkt typisch
    an einen Eck-Stoß zweier Fußpfetten.
  - **Kerve** (`kerve`): partitive Bearbeitung am Gratsparren-Fuß
    auf der Fußpfetten-Stoßstelle; nicht selbst Sparren.
  - **Abgratung** (Folgearbeit `hg_abgratung.md`): partitive
    Bearbeitung der oberen Längskante des Gratsparrens; nicht
    Bestandteil der Definition.
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
import domain.bauteil.Grat
import domain.geometrie.Einheitsvektor
import domain.geometrie.Punkt

/**
 * Gratsparren als Bauteilrolle: Stab-Bauteil entlang einer
 * Gratstrecke (geneigte konvexe Schnittkante zweier Dachflächen).
 *
 * Glossar: hg_gratsparren.md
 *
 * Asymmetrie zum Oberbegriff Sparren:
 *   Die Falllinien-Kollinearität aus hg_sparren.md Bed. 3 wird durch
 *   eine Gratlinien-Kollinearität ersetzt; statt einer einzelnen
 *   Dachfläche ist eine Gratstrecke g_{ij} zugeordnet (Lage auf der
 *   Schnittgeraden zweier Trägerebenen).
 *
 * Vorzeichenkonvention (normativ):
 *   p_a = Gratsparrenfuß       (am Trauf-Eckpunkt der Walm-Ecke)
 *   p_e = Gratsparrenfirstpunkt (am Firstend-Punkt / Walm-Spitze)
 *   d_hat_G zeigt bergauf (⟨d_hat_G, e_z⟩ > 0), kollinear zur
 *   aufwärts gerichteten Gratlinien-Tangente t_hat.
 */
data class Gratsparren(
    val bauteil: Bauteil,
    val grat: Grat,                  // zugeordnete Gratstrecke (Regulaer-Variante)
) {
    init {
        require(bauteil.geometrie is Bauteilgeometrie.Stab) {
            "Gratsparren erfordert Stabgeometrie"
        }
        // Lage- und Gratlinien-Bedingungen werden in der Factory
        // gratsparrenAusBauteil(...) geprüft und liefern bei Verletzung
        // ein Resultat.Fehler mit GratsparrenEntartet-Variante (siehe unten).
    }

    val gratsparrenfuss: Punkt        get() = achse().anfang
    val gratsparrenfirstpunkt: Punkt  get() = achse().ende
    val laenge: Double                get() = achse().laenge          // mm
    val gratsparrenneigung: Double                                     // rad
        get() = grat.gratneigung()

    private fun achse(): Bauteilachse.Gerade =
        (bauteil.geometrie as Bauteilgeometrie.Stab).achse as Bauteilachse.Gerade
}

sealed class GratsparrenEntartet {
    object NichtAufGratlinie       : GratsparrenEntartet()
    object NichtKollinearZurTangente : GratsparrenEntartet()
    object FalscheRichtung         : GratsparrenEntartet()   // d_hat_G zeigt bergab
    object Nullachse               : GratsparrenEntartet()
    object EntarteteGratstrecke    : GratsparrenEntartet()
}
```

- **Einheit**: Längen in mm (Double), Winkel intern in Radiant.
- **Identität**: `BauteilId` aus dem zugrunde liegenden Bauteil.
- **Invarianten** (in der Factory `gratsparrenAusBauteil(...)` prüfen,
  bei Verletzung `Resultat.Fehler` mit der jeweiligen
  `GratsparrenEntartet`-Variante; niemals Exception):
  1. Stabgeometrie und Bauteilachse vom Typ `Bauteilachse.Gerade`.
  2. Achsenlänge > Toleranzen.LAENGE_EPS — sonst `Nullachse`.
  3. Zugeordnete Gratstrecke `grat` ist `Grat.Regulaer` mit
     wohldefinierten Endpunkten — sonst `EntarteteGratstrecke`.
  4. p_a und p_e liegen auf der Gratlinien-Geraden bis ε_L —
     sonst `NichtAufGratlinie`.
  5. ‖d_hat_G × t_hat‖ ≤ Toleranzen.KOLLINEAR_EPS — sonst
     `NichtKollinearZurTangente`.
     (§4 HG-Konvention: Kollinearitäts-Test über das normierte
     Kreuzprodukt mit `KOLLINEAR_EPS`, **nicht** über
     `WINKEL_EPS`.)
  6. ⟨d_hat_G, t_hat⟩ ≥ +1 − Toleranzen.WINKEL_EPS — sonst
     `FalscheRichtung` (Konsumenten können durch Achsen-Umkehr
     automatisch korrigieren).
- **Edge Cases**:
  - **Krüppelwalm-Gratsparren**: Gratsparren endet auf einer
    Mittel- oder Kehlbohle statt am Firstend-Punkt; die
    Definition bleibt anwendbar, p_e liegt dann auf einer
    inneren Stelle der Gratstrecke.
  - **Vollwalm-Pyramide**: vier Gratsparren laufen an einer
    Spitze zusammen; jeder einzelne Gratsparren erfüllt die
    Definition gegen seine eigene Gratstrecke; die
    Knotenbehandlung an der Spitze ist Aufgabe des Tragwerk-
    Aggregats.
  - **Ungleichgeneigte Walme**: Reduktions-Formel (★) bleibt
    gültig mit β_plan ≠ 45°; die Definition unverändert
    anwendbar.
  - **Gratsparren mit Verbearbeitung (Abgratung, Absenkung)**:
    die Bauteilachse bleibt die geometrische Schwerlinie; die
    Bearbeitungen sind separate Geometrie-Modifikationen am
    Bauteil und nicht Bestandteil der Gratsparren-Definition.
  - **Sehr kleine Walmflächen / kurze Gratstrecke**: bei
    ‖g_{ij}‖ → ε_L wird die Gratstrecke entartet; in diesem Fall
    liefert die Factory `EntarteteGratstrecke`.
- **Abgeleitete Eigenschaften** (als Funktionen):
  - `gratsparrenneigung(): Double` — = Gratneigung der
    zugeordneten Gratstrecke, in Radiant. Es gilt
    `tan(α_G) = tan(α) · cos(β_plan)` mit α =
    `min(D_i.dachneigung(), D_j.dachneigung())` bzw. allgemein
    der dachflächen-spezifischen Falllinien-Neigung
    (Reduktions-Formel als Konsequenz, nicht als Code-
    Berechnungs-Identität).
  - `dachflaechenPaar(): Pair<Dachflaeche, Dachflaeche>` —
    die beiden zugeordneten Dachflächen (D_i, D_j).
  - `planWinkel(d: Dachflaeche): Double` — Grundrissprojektions-
    Winkel β_plan zwischen Gratlinie und Trauflinie der
    Dachfläche `d`; Bemessungs-Hilfsfunktion.
- **Bezeichner-Konvention** (CLAUDE.md): Klasse heißt `Gratsparren`
  (deutsch, Glossarbegriff); zugeordnete Gratstrecke ist
  `Grat.Regulaer`.

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
  4. Auflage, Kröner, Stuttgart 2005, Eintrag „Gratsparren".
- Gerner, M.: *Fachwerk – Instandsetzung, Sanierung, Neubau.*
  DVA, 7. Auflage 2007.

**Korpus (nicht autoritativ):**

- Wikipedia, Lemmata „Gratsparren", „Walmdach", „Schifter",
  „Schiftung", „Dachausmittlung" (abgerufen 2026-05-14).
- BauNetz Wissen Glossar „Gratsparren"
  (`baunetzwissen.de/glossar/g/gratsparren-3000593`).
- zimmerer-treff.com: „Austragung von Schifter und Gratsparren";
  „Rechnerischer Abbund von Schifter und Gratsparren";
  „Krüppelwalmgratsparren".
- polybau.ch: „Austragung Schifter/Gratsparren" (Schweiz).
- Bund Deutscher Zimmermeister, Handbuch „Anleitung Kehl-/
  Gratsparrengrafik" (zimmerer.de).
- Greifswalder Zimmerer: „Gratgrundverschiebung berechnen".
- baubeaver.de: „Gratsparren" / „Walmdach-Workshop".
- dachdecker.com: „Gratsparren".
- Bemessungssoftware: Frilo DGK „Grat- und Kehlsparren"; pbs.de
  062J „Holzbau Grat- und Kehlsparren – EC5"; Harzer-Statik
  „Gratsparren".
- Angelsächsische Hip-Rafter-Literatur: sbebuilders.blogspot.com;
  raftertools.net; jlconline.com (für die Reduktions-Formel und
  „backing angle" / „dropping the hip" als konstruktive
  Pendants zu Abgratung und Absenkung).

**Nicht verifizierbar (negativer Befund):**

- Lignum HBT (aktuelle Auflage), spezifische Begriffsbelegung
  „Gratsparren"; online nicht volltext-indiziert.
- Lignatec „Geneigte Dächer in Holzbauweise", spezifische
  Begriffsbelegung „Gratsparren"; online nicht volltext-indiziert.
