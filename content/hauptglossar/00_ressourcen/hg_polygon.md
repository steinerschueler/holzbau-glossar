---
id: polygon
benennung: Polygon
kurz: "Ein Polygon ist eine ebene Fläche, die von lauter geraden Strecken zu einem geschlossenen Vieleck umrandet wird — wie ein Dreieck, ein Rechteck oder jedes andere Vieleck."
synonyme: [Vieleck, "ebenes Polygon", "einfaches Polygon"]
abgelehnte_benennungen: [Mehreck, Polyzug, "polygon"]
oberbegriff: null
begriffstyp: generisch
voraussetzungen: [punkt, strecke, ebene]
abgrenzung_zu: [streckenzug, dachflaeche, polyeder, stirnseite, laengsseite]
status: entwurf
subglossar_pendant: notwendig
quellen_primär:
  - "DIN ISO 80000-2:2022-08, Abschnitt 2 (Geometrie), Bezeichnungen für Vielecke."
  - "ISO 19107:2019 'Geographic information – Spatial schema', Abschnitt 6.4 'GM_Polygon' (geometrische Definition eines einfachen ebenen Polygons mit Innenbereich)."
quellen_sekundär:
  - "Bronstein, I. N. et al.: Taschenbuch der Mathematik. Kap. 3.1.5 'Vielecke' und Kap. 3.5 'Polygone im Raum'."
  - "de Berg, M.; Cheong, O.; van Kreveld, M.; Overmars, M.: Computational Geometry – Algorithms and Applications. 3. Aufl., Springer 2008, Kap. 3 'Polygon Triangulation' (Definition einfacher Polygone, Jordan-Kurvensatz für stückweise lineare Kurven)."
  - "Preparata, F. P.; Shamos, M. I.: Computational Geometry – An Introduction. Springer 1985, Kap. 1.3."
quellenkonflikt: |
  Holzbau-Normen verwenden „Vieleck" oder „polygonal begrenzt" ohne
  axiomatische Definition. ISO 19107 (GIS) liefert eine präzise
  Definition für GM_Polygon, allerdings im Kontext geographischer
  Daten. Eigene Festlegung: ein Polygon ist ein endlicher, einfach
  geschlossener, ebener Streckenzug mit k ≥ 3 Eckpunkten in
  allgemeiner Lage; das berandete Flächenstück gehört zur Definition
  dazu (Pendant zu GM_Polygon und zur Definition in de Berg et al.).
  Diese Festlegung ist konsistent mit allen konsultierten Quellen
  und mit der bereits verwendeten Definition in `hg_dachflaeche.md`.
---

## Prosa-Definition

Ein **Polygon** ist ein endlicher, in einer gemeinsamen Ebene
liegender, einfach geschlossener Streckenzug mit k ≥ 3 paarweise
verschiedenen Eckpunkten, dessen Kanten (außer an gemeinsamen
Endpunkten) einander nicht schneiden, zusammen mit dem von ihm
nach dem Jordan-Kurvensatz eindeutig berandeten, beschränkten
Flächenstück seines Inneren.

## Mathematische Definition

Sei

- E ⊂ ℝ³ eine Ebene (im Sinne des Eintrags `ebene`),
- (v₁, v₂, …, v_k) eine Tupel von Eckpunkten v_i ∈ E mit k ≥ 3.

Definiere die **Kanten** zyklisch als Strecken

```
e_i:= [v_i, v_{i+1}]   für  i = 1, …, k,   v_{k+1}:= v_1.
```

Das Tupel (v₁, …, v_k) heißt ein **Polygon** in E genau dann, wenn
folgende Bedingungen gelten:

1. **Koplanarität**: Alle v_i liegen in derselben Ebene E.
2. **Mindesteckenzahl**: k ≥ 3.
3. **Nicht-Degeneration der Eckpunkte**:
   v_i ≠ v_{i+1} für alle i (keine Nullkanten).
4. **Nicht-Kollinearität in der Folge**: Für alle i sind
   v_{i−1}, v_i, v_{i+1} nicht kollinear (keine „überflüssigen"
   Eckpunkte). *(Diese Bedingung ist optional und kann durch
   einen Vorverarbeitungsschritt zur Normalisierung erzwungen
   werden.)*
5. **Einfachheit (Jordan-Bedingung)**: Für alle i, j mit
   i ≠ j und {i+1, j+1} ∩ {i, j} = ∅ gilt
   e_i ∩ e_j = ∅. Nicht benachbarte Kanten schneiden sich nicht;
   benachbarte Kanten teilen genau ihren gemeinsamen Eckpunkt.

Aus Bedingungen 1–3 und 5 folgt, dass die Vereinigung der Kanten
∂P:= e₁ ∪ … ∪ e_k eine einfache geschlossene stückweise lineare
Kurve in E ist. Nach dem **Jordan-Kurvensatz** zerlegt ∂P die
Ebene E in genau zwei zusammenhängende Komponenten, von denen
genau eine beschränkt ist; diese beschränkte Komponente, vereinigt
mit ihrem Rand, sei

```
F(P):= { x ∈ E | x liegt im beschränkten Bereich von E ∖ ∂P } ∪ ∂P.
```

Das **Polygon** ist dann das Paar P = ((v₁, …, v_k), F(P)) bzw.
in implementierungsnaher Form das Tupel (v₁, …, v_k) zusammen mit
der Ebene E; F(P) ist eine abgeleitete Größe.

Wesentliche abgeleitete Größen:

- **Trägerebene**: E.
- **Eckenzahl**: k ∈ ℕ_{≥3}.
- **Kantenmenge**: { e₁, …, e_k }.
- **Umfang**: U(P):= Σ_{i=1}^{k} ‖v_{i+1} − v_i‖ (in mm).
- **Flächeninhalt** (für Polygon mit Einheitsnormale n_hat der
  Trägerebene): A(P):= ½ · |⟨n_hat, Σ_{i=1}^{k} v_i × v_{i+1}⟩|
  (in mm²; verallgemeinert die 2D-Schuhbänder-/Gauß-Trapezformel
  auf eine in ℝ³ liegende Ebene).
- **Orientierung**: Das Vorzeichen von ⟨n_hat, Σ v_i × v_{i+1}⟩
  unterscheidet positive (gegen den Uhrzeigersinn von n_hat aus
  betrachtet) und negative Orientierung der Eckenfolge.

## Wohldefiniertheit

- **Existenz von F(P)**: Aus Bedingungen 1, 2, 3 und 5 folgt, dass
  ∂P eine einfache geschlossene Jordan-Kurve in E ist; der
  Jordan-Kurvensatz garantiert die Existenz und Eindeutigkeit
  einer beschränkten Komponente.
- **Repräsentantenwahl**: Zyklische Verschiebung der Eckenfolge
  (v₁, …, v_k) → (v₂, …, v_k, v₁) liefert dieselbe Kantenmenge
  und damit dasselbe Polygon. Die Domänen-Schicht definiert die
  Identität von Polygonen daher modulo zyklischer Verschiebung
  (und optional modulo Umkehrung, wenn Orientierung irrelevant ist).
- **Unabhängigkeit des Flächeninhalts vom Stützpunkt**: Die
  Schuhbänderformel in 3D verwendet das Kreuzprodukt v_i × v_{i+1}.
  Eine Translation aller v_i um denselben Vektor t liefert
  Σ (v_i + t) × (v_{i+1} + t) = Σ v_i × v_{i+1} + t × Σ v_{i+1} +
  Σ v_i × t + k · (t × t). Wegen Σ v_{i+1} = Σ v_i und
  t × t = 0 reduziert sich der Korrekturterm auf
  t × Σ v_i + Σ v_i × t = t × Σ v_i − t × Σ v_i = 0. Der Wert ist
  also translations-invariant; insbesondere kann ohne Beschränkung
  der Allgemeinheit ein Eckpunkt als Ursprung gewählt werden.
- **Vorzeichenwahl der Normalen**: Die Formel hängt linear von n_hat
  ab; (n_hat, −n_hat) ändert das Vorzeichen. Die Betragsbildung |·|
  liefert einen wohldefinierten unsignierten Flächeninhalt.
- **Nicht-Zirkularität**: Definition stützt sich auf Punkt, Strecke,
  Ebene, reellwertige Operationen und den Jordan-Kurvensatz für
  stückweise lineare Kurven (klassisches Resultat, beweisbar
  ohne Bezug auf Polygon).

## Erläuterung (nicht normativ)

Polygone treten im Holzbau überall dort auf, wo eine
ebene Außen- oder Schnittfläche eines Bauteils oder einer
Konstruktion beschrieben werden soll: Umriss einer Dachfläche,
Querschnitt eines Sparrens, Grundriss einer Wand, Polygonalisierung
einer Holzplatte.

Drei verbreitete Spezialfälle:

- **Dreieck** (k = 3): einfachstes Polygon; immer eben und einfach.
- **Konvexes Polygon**: jede Kante teilt die Ebene in zwei
  Halbebenen, und alle anderen Eckpunkte liegen in derselben
  Halbebene. Für Tragwerksgeometrien selten zwingend, aber
  numerisch günstig.
- **Rechteck**: konvexes Polygon mit vier rechten Innenwinkeln.

Im **Dachgrundriss-Polygon** hat die Eckform eine direkte
konstruktive Konsequenz: eine **ausspringende (konvexe) Ecke**
erzeugt bei der Dachausmittlung einen **Grat** zwischen den
angrenzenden Dachflächen; eine **einspringende (konkave) Ecke**
erzeugt eine **Kehle**. Bei einem L-förmigen Grundriss liegt an
der einspringenden Innenecke eine Kehllinie, an jeder
ausspringenden Außenecke ein Grat. Die konvex/konkav-Unterscheidung
am Polygon ist damit nicht bloß numerisch günstig, sondern trägt im
Holzbau eine unmittelbare Bauteil-Bedeutung (Grat- oder
Kehlsparren als Schnittlinie der Dachflächen über der jeweiligen
Ecke).

In der Domänen-Schicht ist das Polygon ein **abgeschlossenes**
Flächenstück (Rand gehört dazu); offene Polygone werden nicht
unterstützt.

In der **Vermessungs-/Geodäsie-Schicht** lebt das Polygon-Vokabular
eigenständig: **Polygonzug** (Spur einer Wegfolge aus
Geradenstücken, offen oder als „Ringpolygon" geschlossen) und
**Polygonpunkt** (vermessener Eckpunkt) sind dort die primären
Begriffe. Am Bauplatz tritt das **Schnurgerüst** als geschlossener
Polygonzug auf, dessen Eckpunkte als Polygonpunkte abgesteckt
werden. Diese geodätische Verwendung ist mit der hier festgelegten
mathematischen Polygon-Definition konsistent, das berufssprachliche
Vokabular am Bauplatz ist aber unterschiedlich gewachsen und kann
zwischen Mathematik- und Vermessungs-Sprache zu Stolpersteinen
führen (Abgrenzung zum Streckenzug-Eintrag, siehe §Beziehungen).

### Zwei zulässige Lesarten: Punktmenge und Berandung

Der oben definierte Polygon-Begriff trägt zwei zulässige Lesarten
desselben Konzepts, die sich nur in der zugewiesenen
Substanz-Schicht unterscheiden — nicht in der zugrundeliegenden
Information:

- **Punktmengen-Lesart (primär):** Das Polygon ist das berandete,
  beschränkte, abgeschlossene Flächenstück F(P) ⊂ E zusammen mit
  seiner Eckenfolge. Dies ist die in der mathematischen Definition
  oben festgelegte Standardauffassung; sie ist die für
  flächeninhaltsbezogene Operationen (Schwerpunkt, Flächeninhalt,
  Punkt-in-Polygon-Test) und für die Domänen-Klasse
  `KonvexesPolygon` maßgebliche Lesart.
- **Berandungs-Lesart (zulässig, kontext-gebunden):** Das Polygon
  ist die geschlossene polygonale Randkurve ∂P = e₁ ∪ … ∪ e_k in E
  zusammen mit ihrer Eckenfolge. Diese Lesart ist insbesondere für
  die Modellierung von **Bauteilflächen** als Randpolygon auf einer
  Trägerebene relevant (siehe `stirnseite`, `laengsseite`), in der
  die Bauteilfläche durch ihren Linienzug auf einer ausgezeichneten
  Trägerebene beschrieben wird und das Flächenstück nur als
  abgeleitete Größe geführt wird.

Beide Lesarten tragen **dieselbe Information**: aus der Eckenfolge
(v₁, …, v_k) und der Trägerebene E ergibt sich der Linienzug ∂P
deterministisch durch zyklisches Verbinden der Eckpunkte, und aus
dem Linienzug folgt durch den Jordan-Kurvensatz eindeutig das
beschränkte Flächenstück F(P). Die Wahl zwischen Punktmengen- und
Berandungs-Lesart ist **Kontext-Frage**, keine Strukturfrage des
Begriffs: in Operationen über Flächeninhalt und Lage von Punkten
liegt die Punktmengen-Lesart nahe; in der Bauteilflächen-
Modellierung mit Trägerebene und Aussennormalen-Konvention liegt
die Berandungs-Lesart näher. Die Implementierung führt beide
Lesarten über denselben Datentyp (`KonvexesPolygon` mit
Eckenfolge in einer Trägerebene); die zusätzliche semantische
Schicht (Bauteilrolle, Aussennormalen-Konvention) trägt der
verwendende Begriff.

## Beziehungen

- **Oberbegriff**: einfach geschlossener stückweise linearer
  ebener Streckenzug mit innerem Flächenstück (formal). Im
  Glossar Primitiv.
- **Teilbegriffe (Spezialisierungen)**:
  - **Dreieck** (k = 3).
  - **Viereck**, **Rechteck**, **Trapez** (k = 4 mit Zusatz-
    bedingungen).
  - **Konvexes Polygon**.
  - Anwendungs-Spezialisierungen: **Umriss einer Dachfläche**,
    **Querschnittspolygon eines Bauteils**.
- **Bestandteile (partitiv)**:
  - Eckpunkte v_i, Kanten e_i, Innenfläche F(P) ∖ ∂P, Rand ∂P.
- **Abgrenzung**:
  - **Streckenzug** (siehe `streckenzug`; Synonyme: Polygonzug,
    Polylinie): stückweise lineare Kurve, die nicht notwendig
    geschlossen und nicht notwendig einfach ist. Ein Polygon ist
    ein geschlossener, einfacher Streckenzug *mitsamt* dem
    berandeten Flächenstück. In der **Vermessungs-/Geodäsie-
    Schicht** wird „Polygonzug" als eigenständiger Begriff
    geführt (Schnurgerüst am Bauplatz als geschlossener
    Polygonzug, Polygonpunkte als vermessene Eckpunkte); diese
    geodätische Lesart ist mit der mathematischen Polygon-
    Definition konsistent, das Vokabular am Bauplatz jedoch
    unterschiedlich gewachsen (siehe §Erläuterung).
  - **Strecke**: einzelne Kante; kein Polygon.
  - **Dachfläche**: ein Polygon in einer Ebene mit zusätzlicher
    Orientierung und Rolle als Außenfläche eines Daches; das
    Polygon ist die geometrische Substanz, die Dachfläche eine
    rollenbezogene Spezialisierung.
  - **Polyeder**: dreidimensionaler Körper, dessen Oberfläche aus
    Polygonen zusammengesetzt ist; ein Polygon ist zweidimensional.
  - **Stirnseite** (`stirnseite`) und **Längsseite** (`laengsseite`):
    Bauteilflächen, die geometrisch über die Berandungs-Lesart des
    Polygons modelliert werden (Randpolygon auf einer Trägerebene
    mit Bauteilrolle und Aussennormalen-Konvention). Das Polygon
    trägt die geometrische Substanz; die Bauteilfläche fügt die
    Bauteilrolle und die Aussennormalen-Konvention hinzu.
  - **Selbstüberschneidende Vielecke** (z. B. Pentagramm):
    werden in diesem Glossar **nicht** als Polygon zugelassen.
    Die `KonvexesPolygon`-Implementierung schließt sie für die
    im Holzbau auftretenden Eckreihenfolgen über die lokale
    Konvexitäts-Invariante aus. Mit der Folgearbeit
    `EinfachesPolygon` werden Selbstschnitte global als
    `Entartet.Selbstschnitt` zurückgewiesen — diese Variante ist
    heute noch nicht im `EntartetGeometrie`-Sealed-Interface
    vorhanden.

## Quellen

**Primär (normativ):**

- DIN ISO 80000-2:2022-08, „Größen und Einheiten – Teil 2: Mathematik",
  Abschnitt 2.
- ISO 19107:2019, „Geographic information – Spatial schema",
  Abschnitt 6.4 (GM_Polygon).

**Sekundär:**

- Bronstein, I. N.; Semendjajew, K. A.; Musiol, G.; Mühlig, H.:
  *Taschenbuch der Mathematik.* Kap. 3.1.5 und 3.5.
- de Berg, M.; Cheong, O.; van Kreveld, M.; Overmars, M.:
  *Computational Geometry – Algorithms and Applications.*
  3. Aufl., Springer 2008.
- Preparata, F. P.; Shamos, M. I.: *Computational Geometry – An
  Introduction.* Springer 1985.

**Korpus (nicht autoritativ):**

- Wikipedia, Lemma „Polygon" (abgerufen 2026-05-07).
