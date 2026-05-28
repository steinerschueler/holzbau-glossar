---
id: stirnseite
benennung: Stirnseite
synonyme: [Hirnholz, Hirnseite, Stirnholz, Kopfholz, Hirnschnittfläche]
abgelehnte_benennungen: [Stirnfläche, "end grain", "endgrain", "end face", "end cut", Stirn]
oberbegriff: bauteilflaeche
begriffstyp: generisch
voraussetzungen: [bauteilflaeche, polygon, ebene, bauteil, bauteilachse, faserrichtung, toleranzen]
abgrenzung_zu: [querschnitt, laengsseite, polygon, ebene, anschnitt, bauteilachse, faserrichtung]
status: entwurf
theorie_pflichtig: required
quellen_primär:
  - "DIN 4074-1:2012-06, 'Sortierung von Holz nach der Tragfähigkeit – Teil 1: Nadelschnittholz', Abschnitt 5 (Sortiermerkmale): Markröhre und Jahresringe sind an der Stirnseite (Hirnseite) zu beurteilen."
  - "DIN 68800-2:2022-02, 'Holzschutz – Teil 2: Vorbeugende bauliche Maßnahmen im Hochbau', Abschnitt 5: Hirnholz / Stirnholz als Schwachstelle für Bewitterung; Hirnholzschutz an exponierten Stirnseiten."
  - "DIN EN 1995-1-1:2010-12 (Eurocode 5), Abschnitt 8.5 (Verbindungen mit stiftförmigen Verbindungsmitteln): Hirnholz-Anschluss als Sonderfall mit reduzierter Tragfähigkeit."
  - "DIN EN 350:2016-12, 'Dauerhaftigkeit von Holz und Holzprodukten', Hirnholz-Bewitterung als Bewertungskriterium."
quellen_sekundär:
  - "Mönck, W.; Rug, W.: Holzbau – Bemessung und Konstruktion. 16. Aufl., Beuth, Berlin 2015, Kap. 2 'Holz als Werkstoff' und Kap. 7 'Verbindungen': Hirnholzanschlüsse."
  - "Natterer, J.; Herzog, T.; Volz, M.: Holzbau-Atlas. 4. Aufl., Birkhäuser, Basel 2003, Kap. 'Werkstoff Holz'."
  - "Gerner, M.: Fachwerk – Instandsetzung, Sanierung, Neubau. DVA, 7. Aufl. 2007, Glossar 'Hirnholz'."
  - "Lignum (Hrsg.): Holzbautabellen HBT, Lignum, Zürich, aktuelle Auflage, Kap. 'Werkstoff Holz' und 'Holzschutz'."
quellenkonflikt: |
  Die konsultierten Holzbau-Normen (DIN 4074-1, DIN 68800-2,
  DIN EN 1995-1-1, DIN EN 350) verwenden „Hirnholz" und „Hirnseite"
  als gegebene Begriffe; eine geschlossene geometrische Definition
  fehlt. Die fachsprachliche Verwendung ist im DACH-Raum jedoch
  einheitlich: Hirnholz/Hirnseite/Stirnholz/Stirnseite/Kopfholz
  bezeichnen die quer zur Faserrichtung geschnittene Schnittfläche
  eines Holzbauteils, an der die Jahresringe als Kreise oder
  Kreissegmente sichtbar sind.

  Synonym-Befund (Sekundärquellen, fachsprachlicher Korpus):

  - **Hirnholz**: dominant in DE-Holzfachsprache (Mönck/Rug,
    Natterer, Gerner, DIN 4074-1, DIN 68800-2). Bezeichnet das
    Material an der Schnittfläche, oft synonym mit der Schnittfläche
    selbst.
  - **Hirnseite**: Schnittflächen-Bezeichnung; in der CH-Praxis
    geläufig.
  - **Stirnholz**: gleichbedeutend mit Hirnholz; in DE und CH
    verbreitet.
  - **Stirnseite**: bezeichnet im Holzbau primär die Schnittfläche
    selbst (geometrische Lesart) und ist der Hauptbegriff dieser
    App. Wird auch in der allgemeinen Bautechnik („Stirnseite eines
    Bauteils") für die schmale Endfläche eines länglichen Bauteils
    verwendet, was geometrisch meist mit der Hirnseite zusammenfällt.
  - **Kopfholz**: Synonym in einigen DE-Quellen
    (Holzhandel-Glossare, Wikipedia „Hirnholz"); im Holzbau weniger
    geläufig als Hirnholz/Stirnholz.

  Eigene Festlegung in diesem Glossar:

  - **Stirnseite** ist der Hauptbegriff dieses Eintrags. Begründung:
    geometrische Lesart („Seite" als Fläche) ist im Tooling-Kontext
    der App eindeutiger als „Hirnholz" (das primär das Material
    bezeichnet); zugleich bleibt der Begriff anschlussfähig an die
    breite zimmermannsmäßige Verwendung.
  - **Hirnholz**, **Hirnseite**, **Stirnholz**, **Kopfholz** werden
    als gleichberechtigte Synonyme geführt; die App-Anzeige bevorzugt
    „Stirnseite" (geometrisch) bzw. „Hirnholz" (materialbezogen,
    Holzschutz/Bemessung).
  - **Stirnseite ist eine Bauteilfläche**: konkret die ebene
    Schnittfläche an einem Bauteilende, die rechtwinklig zur
    Bauteilachse (im prismatischen Standardfall) bzw. unter dem
    Anschnittwinkel (siehe `bearbeitung`-Subtyp `anschnitt`,
    Folgearbeit) zur Bauteilachse liegt. Die Faserrichtung tritt
    an der Stirnseite **aus** dem Bauteil aus.
  - **Oberbegriff ist Polygon (Berandungs-Lesart), nicht
    Querschnitt**: `hg_querschnitt.md` setzt voraus, dass die
    Querschnittsebene **rechtwinklig zur Bauteilachse** liegt; bei
    einer Anschnitt-Stirnseite (Bearbeitungs-Subtyp `anschnitt`,
    geneigter Endschnitt) ist diese Bedingung verletzt. Die
    Stirnseite ist daher kein Querschnitt im Sinne von
    `hg_querschnitt.md`, sondern geometrisch eine polygonal berandete
    Punktmenge auf einer ausgezeichneten Trägerebene am
    Bauteilende. Sie wird unter `oberbegriff: polygon` in der
    Berandungs-Lesart (siehe `hg_polygon.md`, Abschnitt „Zwei
    zulässige Lesarten") geführt und trägt zusätzlich Bauteilrolle
    und Aussennormalen-Konvention. Eine Stirnseite ist genau dann
    zugleich ein Querschnitt im Sinne von `hg_querschnitt.md`, wenn
    ihre Trägerebenen-Normale parallel zur Bauteilachsen-Tangente
    am Endpunkt liegt (Anschnittwinkel α_AS = π/2, prismatischer
    Standardfall); bei α_AS ≠ π/2 trifft das nicht zu.
  - Bei einem **Anschnitt** (geneigter Endschnitt) bleibt die
    entstehende geneigte Endfläche begrifflich eine Stirnseite des
    Bauteils, weil die Faser auch dann (mit grösserer
    Schnittwinkel-Komponente) durch die Fläche austritt; sie ist
    geometrisch ein Sonderfall der Stirnseite, kein eigener
    Begriff. Der zugehörige Bearbeitungs-Subtyp `anschnitt`
    (Folgearbeit, siehe `hg_bearbeitung.md`) beschreibt den Vorgang;
    das Resultat ist eine Stirnseite mit Schnittwinkel ≠ π/2.
  - Stirnseite ist nur für **Stabbauteile** definiert. Für
    Plattenbauteile gilt der Begriff „Plattenkante", siehe
    Folgearbeit.

  Diese Festlegung ist konsistent mit allen konsultierten Quellen.
---

## Prosa-Definition

Eine **Stirnseite** ist die ebene, polygonal berandete Endfläche
eines Stabbauteils, an der die Bauteilachse das Bauteil verlässt
und an der die Faserrichtung im Holz aus der Schnittfläche austritt.

## Mathematische Definition

Sei

- B ein **Stabbauteil** im Sinne von `bauteil` mit Stabgeometrie
  (`geometrie ∈ 𝒢_stab`),
- A(B) = Bauteilachse(B) die Bauteilachse mit Anfangspunkt p_a und
  Endpunkt p_e (siehe `bauteilachse`), Tangentenrichtung
  d̂(s) ∈ S² an der Stelle s ∈ [0, L],
- E_S eine **Trägerebene** im Sinne von `ebene` durch den
  jeweiligen Bauteilendpunkt mit Einheitsnormaler n̂_S ∈ S²,
- ∂F_S ⊂ E_S ein **Polygon in Berandungs-Lesart** (siehe
  `hg_polygon.md`, Abschnitt „Zwei zulässige Lesarten"), das die
  Bauteilberandung an dem jeweiligen Bauteilende bildet,
- ε_W := Toleranzen.WINKEL_EPS.

**Stirnseite am Bauteilanfang** (s = 0):

```
S_a(B) := (∂F_S^{(a)}, E_S^{(a)}, n̂_S^{(a)}, p_a)                   (1)
          mit ∂F_S^{(a)} = Bauteilberandung von B in E_S^{(a)}
          am Bauteilanfang p_a.
```

**Stirnseite am Bauteilende** (s = L):

```
S_e(B) := (∂F_S^{(e)}, E_S^{(e)}, n̂_S^{(e)}, p_e)                   (2)
          mit ∂F_S^{(e)} = Bauteilberandung von B in E_S^{(e)}
          am Bauteilende p_e.
```

Im **prismatischen Standardfall** (rechtwinkliger Endschnitt) gilt
für die Trägerebenen-Normale n̂_S der Stirnseiten-Ebene

```
|⟨n̂_S^{(a)}, d̂(0)⟩| ≥ 1 − ε_W,                                      (3)
|⟨n̂_S^{(e)}, d̂(L)⟩| ≥ 1 − ε_W.                                      (3')
```

In diesem Fall liegt die Stirnseiten-Ebene rechtwinklig zur
Bauteilachse, und die Stirnseite ist zugleich ein **Querschnitt**
im Sinne von `hg_querschnitt.md` am Bauteilende; der
Flächenschwerpunkt der berandeten Punktmenge fällt mit p_a bzw.
p_e zusammen, und ∂F_S stimmt mit der Polygonberandung des
Querschnitts QS(0) bzw. QS(L) überein. Diese Identität ist im
prismatischen Standardfall der Anker, an dem die Stirnseite mit
der App-Querschnitts-Hierarchie verbunden wird.

Im Fall eines **Anschnitts** (Bearbeitungs-Subtyp `anschnitt`,
Folgearbeit) am Bauteilende ist die Stirnseite eine ebene
polygonal berandete Punktmenge in einer Anschnittebene E_AS, deren
Normale n̂_AS einen Winkel α_AS ∈ (ε_W, π/2 − ε_W) mit d̂(L)
einschließt:

```
|⟨n̂_AS, d̂(L)⟩| = cos(α_AS) < 1 − ε_W.                              (4)
```

Die Stirnseite bleibt eine ebene polygonal berandete Punktmenge
auf einer ausgezeichneten Trägerebene am Bauteilende, ist aber
**nicht mehr rechtwinklig zur Bauteilachse** und damit kein
Querschnitt im Sinne von `hg_querschnitt.md`. Sie bleibt eine
Stirnseite im Sinne dieses Eintrags, weil die geometrischen
Konstitutionsbedingungen (ebene Endfläche auf einer Trägerebene
am Bauteilendpunkt mit Bauteilberandung und Aussennormalen-
Konvention) erfüllt sind. Der zugehörige Begriff `anschnitt`
(Folgearbeit) ist ein Bearbeitungs-Subtyp nach `bearbeitung`,
dessen Resultat eine modifizierte Stirnseite ist.

**Faserrichtungs-Bedingung** (zur Abgrenzung von der Längsseite,
siehe `laengsseite`): Sei f̂ ∈ S² die Faserrichtung des Bauteils
(siehe `faserrichtung`, Modus HART). Dann gilt für eine Stirnseite
mit Trägerebenen-Normaler n̂_S

```
|⟨n̂_S, f̂⟩| > sin(α_grenz),                                         (5)
```

mit einem Anschnittwinkel-Grenzwert α_grenz typisch zwischen 0 und
π/4. Die Bedingung (5) drückt aus, dass die Faserrichtung **mit
einer wesentlichen Komponente quer zur Stirnseiten-Ebene** verläuft,
also die Faser durch die Stirnseite austritt — im Gegensatz zur
Längsseite, an der die Faser in der Trägerebene liegt. Der konkrete
Grenzwinkel α_grenz ist nicht im Glossar fixiert und in der App
nicht aktiv geprüft; (5) charakterisiert den Begriff, ist aber
keine Validierungsregel.

## Wohldefiniertheit

- **Existenz**: Für jedes Stabbauteil mit Stabgeometrie und
  positiver Bauteillänge ist die Bauteilberandung an jedem
  Bauteilendpunkt durch die Bauteilkonstruktion festgelegt (im
  prismatischen Standardfall identisch mit der Polygonberandung des
  Querschnitts QS(0) bzw. QS(L); im Anschnittfall verlängert auf
  die Anschnittebene). Damit existieren ∂F_S^{(a)} und ∂F_S^{(e)}
  konstruktiv, und beide Stirnseiten S_a(B), S_e(B) sind durch
  (1) und (2) festgelegt.
- **Eindeutigkeit**: Bei festgelegtem Bauteil B mitsamt allfälliger
  Anschnitt-Bearbeitung sind die Bauteilberandungs-Polygone an
  beiden Bauteilenden eindeutig bestimmt; folglich auch S_a(B) und
  S_e(B) eindeutig durch (1) und (2).
- **Anzahl der Stirnseiten**: Jedes prismatische Stabbauteil hat
  **genau zwei** Stirnseiten (eine an jedem Bauteilende). Im Fall
  eines Bauteils mit gekrümmter Bauteilachse (Folgearbeit) gilt
  dieselbe Aussage; die Stirnseiten liegen an den Endpunkten der
  gekrümmten Achse.
- **Wohldefiniertheit der Trägerebene**: Die Trägerebene E_S der
  Stirnseite ist im prismatischen Standardfall identisch mit der
  Querschnittsebene am Bauteilendpunkt (siehe `querschnitt`,
  rechtwinklig zur Bauteilachse), in diesem Fall festgelegt durch
  den Bauteilendpunkt und die Tangentenrichtung der Bauteilachse.
  Im Anschnittfall ist E_S durch den Bauteilendpunkt und die
  Anschnitt-Normale n̂_AS festgelegt; sie wird bei der Anschnitt-
  Bearbeitung konstruktiv erzeugt (siehe `bearbeitung`-Subtyp
  `anschnitt`, Folgearbeit). In beiden Fällen ist die Trägerebene
  eindeutig (modulo Vorzeichen, vgl. `ebene` Wohldefiniertheits-
  Abschnitt). Die kanonische Vorzeichenwahl ist „äußere Normale",
  also n̂_S^{(a)} := −d̂(0) (Anfangs-Stirnseite, prismatisch) bzw.
  n̂_S^{(e)} := +d̂(L) (End-Stirnseite, prismatisch); im
  Anschnittfall zeigt n̂_AS analog aus dem Bauteil heraus.
- **Anschnitt als Sonderfall**: Bei einem Anschnitt (Bearbeitung
  am Bauteilende) bleibt das Bauteilende eine ebene Schnittfläche;
  der Anschnitt ändert nur den Schnittwinkel α_AS und damit die
  Trägerebenen-Normale, aber nicht die Eigenschaft, eine
  Stirnseite zu sein. Die Modellierung des Anschnitts ist eine
  Bearbeitung im Sinne von `bearbeitung` (Folgearbeit-Subtyp);
  die resultierende Endfläche ist die Stirnseite des bearbeiteten
  Bauteils.
- **Faserrichtungs-Bedingung (5) ist nicht-konstitutiv**: Die
  Bedingung (5) charakterisiert den Stirnseiten-Begriff
  semantisch, ist aber nicht Teil der Validierungsbedingungen.
  Sie kann verletzt sein bei Bauteilen mit nicht-axialer
  Faserrichtung (Drehwuchs, schräggesägt; siehe `faserrichtung`-
  Modi); die geometrische Stirnseite bleibt davon unberührt.
- **Nicht-Zirkularität**: Die Definition stützt sich auf
  `polygon` (in Berandungs-Lesart), `ebene`, `bauteil`,
  `bauteilachse`, `faserrichtung` und `toleranzen` und nimmt nicht
  auf sich selbst Bezug. Der Bezug auf `querschnitt` ist
  nicht-konstitutiv: er erläutert nur den prismatischen
  Standardfall, in dem Stirnseite und Querschnitt am Bauteilende
  zusammenfallen.

## Erläuterung (nicht normativ)

### Bedeutung im Holzbau

Die Stirnseite ist diejenige Bauteilfläche, an der das **Hirnholz**
sichtbar ist: die Jahresringe treten als Kreise oder Kreissegmente
zu Tage, die Faserrichtung verläuft rechtwinklig (oder schräg) zur
Fläche. Diese Geometrie hat zwei wesentliche Konsequenzen:

1. **Holzschutz** (DIN 68800-2): Hirnholz nimmt durch Kapillar-
   wirkung wesentlich mehr Wasser auf als die Längsseiten. Stirn-
   seiten an exponierten Bauteilen (Sparrenüberstand, Dachvorsprung,
   Pfettenkopf am Giebel) sind besonders durch Bewitterung gefährdet
   und benötigen aktiven Hirnholzschutz (Lasur, Hirnholzkappe,
   konstruktiver Wetterschutz).
2. **Verbindungstragfähigkeit** (DIN EN 1995-1-1, Abschnitt 8.5):
   Hirnholz-Anschlüsse von Verbindungsmitteln (Schrauben in
   Hirnholz, Stabdübel parallel zur Faser) tragen wesentlich
   weniger als Anschlüsse rechtwinklig zur Faser. Die Stirnseite
   ist daher konstruktiv möglichst nicht für Lasteinleitungen zu
   verwenden.

### Zwei Stirnseiten pro Stabbauteil

Jeder Sparren, jede Pfette, jede Stütze hat **genau zwei**
Stirnseiten — eine am Bauteilanfang p_a, eine am Bauteilende p_e.
Im Sparren-Tool sind das die **Sparrenfuß-Stirnseite** (am
traufseitigen Ende) und die **Sparrenfirstpunkt-Stirnseite** (am
firstseitigen Ende; zur Vermeidung der Korpus-Mehrdeutigkeit von
„Sparrenkopf" siehe quellenkonflikt-Hinweis in `hg_sparren.md`). In dieser App werden
beide Stirnseiten bei Bedarf konstruktiv aus dem zugehörigen
Querschnitt am jeweiligen Bauteilende abgeleitet.

### Synonym-Verwendung in der App-Anzeige

| Kontext                                | Bevorzugter Begriff |
|----------------------------------------|---------------------|
| Geometrie / 3D-Visualisierung          | Stirnseite          |
| Werkstoff / Holzschutz                 | Hirnholz            |
| Bemessung Verbindungstragfähigkeit     | Hirnholz-Anschluss  |
| Werkplan-Beschriftung                  | Stirnseite          |

Die App führt eine konsistente Übersetzung zwischen diesen
Synonymen über die Synonyme-Liste des Glossareintrags.

### Stirnseite vs. Längsseite (Übersicht)

Ein Stabbauteil mit Rechteckquerschnitt hat insgesamt sechs
ebene Aussenflächen:

- **2 Stirnseiten** (Bauteilanfang, Bauteilende), Faser tritt
  durch die Fläche aus,
- **4 Längsseiten** (Oberseite, Unterseite, beide Schmalseiten),
  Faser liegt in der Fläche.

Stirnseite und Längsseite sind die beiden disjunkten Bauteilflächen-
Kategorien; sie werden in dieser App als getrennte Glossar-Begriffe
geführt (siehe `laengsseite`).

### Anschnitt am Bauteilende

Wird ein Bauteilende **angeschnitten** (geneigt geschnitten,
Bearbeitungs-Subtyp `anschnitt` als Folgearbeit), entsteht eine
geneigte Stirnseite. Beispiele:

- Sparren-Firstanschnitt (Stirnanschnitt zweier sich am First
  treffender Sparren),
- Sparrenfuß-Anschnitt zur traufseitigen Sichtflächen-Verlängerung,
- Pfetten-Stoßanschnitt am Giebelüberstand.

Geometrisch bleibt die geneigte Endfläche eine Stirnseite des
Bauteils; der Schnittwinkel α_AS ≠ π/2 wird als Anschnitt-Parameter
geführt.

## Beziehungen

- **Oberbegriff**: `polygon` (in Berandungs-Lesart, siehe
  `hg_polygon.md`, Abschnitt „Zwei zulässige Lesarten"). Die
  Stirnseite ist ein ebenes Polygon auf einer ausgezeichneten
  Trägerebene am Bauteilende, das die Bauteilberandung an dieser
  Stelle bildet, zusammen mit Bauteilrolle (Endfläche eines Stab-
  Bauteils) und Aussennormalen-Konvention. Im prismatischen
  Standardfall (rechtwinkliger Endschnitt) ist die Stirnseite
  zusätzlich ein **Querschnitt** im Sinne von `hg_querschnitt.md`
  am Bauteilende; bei einer Anschnitt-Stirnseite (α_AS ≠ π/2)
  ist diese zusätzliche Identität nicht gegeben (siehe
  `quellenkonflikt`-Block und Wohldefiniertheits-Abschnitt). Die
  Beziehung zum Querschnitt wird daher nicht als Oberbegriffs-
  Linie geführt, sondern als bedingte Identität im
  Standardfall.
- **Spezialisierungen** (Folgearbeit):
  - **Anschnitt-Stirnseite**: Stirnseite mit Anschnittwinkel
    α_AS ≠ π/2; entsteht durch Bearbeitung `anschnitt` (siehe
    `hg_bearbeitung.md`, Folgearbeit).
  - **Plattenkante** (`plattenkante`, Folgearbeit): die Stirn-
    Entsprechung bei Plattenbauteilen; eigener Begriff, weil die
    Stab-Bauteil-Definition für Platten nicht unmittelbar
    übertragbar ist.
- **Bestandteile (partitiv)**:
  - **Trägerebene** E (geerbt von `querschnitt`).
  - **Polygonberandung** ∂QS am Bauteilende (geerbt von
    `querschnitt`, konkret `polygon`).
  - **Aussennormalen-Vektor** n̂_S (per Konvention aus dem Bauteil
    heraus zeigend).
  - **Bauteil-Endpunkt-Position**: p_a (Anfangsstirnseite) bzw. p_e
    (Endstirnseite).
- **Verwendung**:
  - **Holzschutz** (`dachhaut`, Folgearbeit `hirnholzschutz`):
    Hirnholz-Bewitterungsschutz an exponierten Stirnseiten.
  - **Verbindungen** (`verbindungsmittel`): Hirnholz-Anschluss als
    Bemessungs-Sonderfall.
  - **Werkplan-Beschriftung**: Stirnseiten-Markierung mit
    Schnittwinkel und Bauteil-Referenz.
  - **3D-Visualisierung**: Stirnseiten erhalten typisch eine
    eigene Texturierung (Hirnholz-Maserung), die sich von den
    Längsseiten (Längsmaserung) unterscheidet.
- **Abgrenzung**:
  - **Querschnitt** (`querschnitt`): Schnittfigur eines Stab-
    Bauteils mit einer Ebene **rechtwinklig zur Bauteilachse** an
    einer beliebigen Stelle s ∈ [0, L]. Eine Stirnseite ist genau
    dann ein Querschnitt im Sinne von `hg_querschnitt.md`, wenn ihre
    Trägerebenen-Normale parallel zur Bauteilachsen-Tangente am
    Endpunkt liegt (prismatischer Standardfall, α_AS = π/2). Bei
    einer Anschnitt-Stirnseite (α_AS ≠ π/2) ist die Trägerebene
    der Stirnseite nicht rechtwinklig zur Bauteilachse, und die
    Stirnseite ist kein Querschnitt im Sinne von `hg_querschnitt.md`.
  - **Bauteilfläche** (`bauteilflaeche`, Folgearbeit): die
    Stirnseite und die Längsseite sind die beiden disjunkten
    Bauteilflächen-Kategorien an einem Stabbauteil; sie sind
    derzeit als getrennte Glossareinträge direkt unter `polygon`
    (Berandungs-Lesart) geführt, ohne gemeinsamen Sammel-
    Oberbegriff. Ein expliziter Begriff `bauteilflaeche` als
    Sammelkategorie ist Folgearbeit (Trigger: erste Domänen-
    Klasse oder Visualisierungs-Operation, die Stirn- und
    Längsseite einheitlich adressieren muss). Siehe auch
    `hg_laengsseite.md`, Folgearbeit-Block.
  - **Längsseite** (`laengsseite`): die zur Bauteilachse parallele
    Bauteilfläche (Oberseite, Unterseite, Schmalseite). Faser
    liegt in der Längsseiten-Trägerebene; bei der Stirnseite
    tritt die Faser aus der Trägerebene aus. Die beiden Begriffe
    sind disjunkt.
  - **Polygon** (`polygon`): die Stirnseite hat eine polygonale
    Berandung, ist aber selbst nicht das Polygon; sie trägt
    zusätzlich die Bauteil-Bezugsrolle (Endfläche eines Stab-
    Bauteils) und die Aussennormalen-Konvention.
  - **Ebene** (`ebene`): die Trägerebene einer Stirnseite ist eine
    Ebene; die Stirnseite selbst ist eine **beschränkte** Teilmenge
    dieser Ebene mit Bauteilrolle.
  - **Anschnitt** (`anschnitt`, Folgearbeit als Bearbeitungs-
    Subtyp): Bearbeitung, die einen geneigten Schnitt am
    Bauteilende herstellt. Die Stirnseite ist das geometrische
    Resultat dieser Bearbeitung; der Anschnitt ist die Bearbeitung
    selbst.
  - **Bauteilachse** (`bauteilachse`): die Stirnseiten liegen an
    den Endpunkten der Bauteilachse; sie sind aber nicht die
    Achse selbst.
  - **Faserrichtung** (`faserrichtung`): an der Stirnseite tritt
    die Faser durch die Fläche aus; an der Längsseite liegt die
    Faser in der Fläche. Die Faserrichtung ist Annotation des
    Bauteils, die Stirnseite eine Bauteilfläche.

## Implementierungshinweis

Datentyp (Domänen-Schicht, Kotlin, Schicht
`domain.bauteil.flaeche`):

```kotlin
package domain.bauteil.flaeche

import domain.geometrie.Ebene
import domain.geometrie.KonvexesPolygon
import domain.geometrie.Punkt
import domain.geometrie.Vektor

/**
 * Stirnseite: Endfläche eines Stab-Bauteils, an der die Faser
 * durch die Schnittfläche austritt.
 *
 * Glossar: hg_stirnseite.md
 *
 * Im prismatischen Standardfall rechtwinklig zur Bauteilachse
 * (und damit zugleich Querschnitt im Sinne von hg_querschnitt.md);
 * im Anschnittfall mit Schnittwinkel α_AS ∈ (0, π/2) gegen die
 * Bauteilachse — dann polygonal berandete Endfläche, aber kein
 * Querschnitt.
 *
 * Trägerpolygon ∂F_S in Berandungs-Lesart (siehe hg_polygon.md);
 * Aussennormale n̂_S zeigt per Konvention aus dem Bauteil heraus.
 */
data class Stirnseite(
    val berandung: KonvexesPolygon,   // ∂F_S in Berandungs-Lesart
    val position: Endposition,        // ANFANG | ENDE
    val aussennormale: Vektor,        // n̂_S, ‖aussennormale‖ ≈ 1
    val bezugspunkt: Punkt,           // p_a bzw. p_e
)

/** An welchem Ende des Bauteils die Stirnseite liegt. */
enum class Endposition {
    ANFANG,   // s = 0, n̂_S := −d̂(0)
    ENDE,     // s = L, n̂_S := +d̂(L)
}
```

- **Einheit**: Punktkoordinaten in mm; Vektor dimensionslos
  (Einheitsvektor); Querschnitt nach `querschnitt`.
- **Identität**: keine eigene UUID. Die Stirnseite ist eine
  abgeleitete Sicht auf das Bauteil-Ende; sie wird konstruktiv
  aus dem Bauteil bezogen, nicht persistiert.
- **Pflicht- und Optionalfelder**:
  - `berandung` — Pflicht; Bauteilberandungs-Polygon ∂F_S in
    Berandungs-Lesart (siehe `hg_polygon.md`, Abschnitt „Zwei
    zulässige Lesarten"). Im prismatischen Standardfall identisch
    mit der Polygonberandung des Querschnitts am Bauteilende; im
    Anschnittfall die durch die Anschnittebene erzeugte
    Polygonberandung.
  - `position` — Pflicht; ANFANG oder ENDE.
  - `aussennormale` — Pflicht; per Konvention aus dem Bauteil heraus.
  - `bezugspunkt` — Pflicht; Bauteil-Endpunkt p_a bzw. p_e.
- **Invarianten** (in Companion-Factory `Stirnseite.aus(bauteil,
  position)`, `Resultat.Fehler` bei Verletzung; keine Exception):
  1. `aussennormale` ist normiert (‖aussennormale‖ ≈ 1 innerhalb
     `Toleranzen.NORM_EPS`).
  2. Im prismatischen Standardfall: `aussennormale` ist parallel
     zur Bauteilachsen-Tangente am Endpunkt (Anschnittwinkel
     α_AS = π/2).
  3. Im Anschnittfall: 0 < α_AS < π/2 (Anschnitt-Bearbeitung als
     Vorbedingung).
- **Konstruktion**: Die Stirnseite wird **abgeleitet** aus dem
  Bauteil und der gewählten Endposition; sie wird **nicht** als
  unabhängiges Objekt konstruiert. Die Domänen-Schicht stellt
  Faktor-Funktionen `Bauteil.stirnseiteAm(position)` bereit,
  die das jeweilige `Stirnseite`-Objekt aus dem Bauteilkontext
  zusammensetzen.
- **IFC-Mapping** (Persistenzschicht, Phase 4):
  - Stirnseite wird nicht als eigene IFC-Entität geführt; sie
    ist eine Sicht auf die `IfcExtrudedAreaSolid`-Endfläche des
    Bauteils.
- **Edge Cases**:
  - **Stirnseite an einem Bauteil mit Anschnitt** (Anschnittwinkel
    α_AS < π/2): die Stirnseite hat eine grössere Fläche als der
    Bauteilquerschnitt rechtwinklig zur Achse; das Verhältnis ist
    `1 / sin(α_AS)`.
  - **Stirnseite an einem Bauteil mit Faserrichtung-Modus
    SCHWACH oder KEINE** (z. B. OSB, Spanplatte, siehe
    Memory `project_faserrichtung_modi`): Bedingung (5) ist für
    diese Modi nicht sinnvoll; die geometrische Stirnseite bleibt
    aber definiert. Plattenwerkstoffe werden bevorzugt mit dem
    Begriff `plattenkante` (Folgearbeit) modelliert.
  - **Doppelter Anschnitt am selben Bauteilende** (Schiftsparren-
    Doppelschnitt): zwei Anschnitte führen zu zwei Schnittflächen
    am selben Endpunkt; jede ist eine eigene Stirnseite des
    bearbeiteten Bauteils. Die App führt sie als getrennte
    `Stirnseite`-Instanzen mit derselben `position`, aber
    unterschiedlichen `aussennormale`.
- **Bezeichner-Konvention** (CLAUDE.md): Klasse heißt `Stirnseite`
  (deutsch, Glossarbegriff). `Endposition.ANFANG` / `Endposition.ENDE`
  sind technische Konstanten ohne eigenen Glossarbezug.

**Folgearbeit (trigger-basiert):**

- **Bauteilfläche** (`bauteilflaeche`-Eintrag, Folgearbeit):
  Sammelkategorie für Stirnseite und Längsseite als die beiden
  disjunkten ebenen Aussenflächen-Klassen eines Stabbauteils.
  Stirnseite und Längsseite sind derzeit symmetrisch direkt unter
  `polygon` in Berandungs-Lesart aufgehängt; ein gemeinsamer
  Sammel-Oberbegriff existiert nicht. Trigger: erste Domänen-Klasse
  oder Visualisierungs-Operation, die Stirn- und Längsseite
  einheitlich als „Bauteilfläche" adressieren muss (z. B.
  Sammel-Iteration über alle Aussenflächen eines Bauteils,
  einheitliche Aussennormalen-Behandlung im Renderer).
- **Hirnholzschutz** (`hirnholzschutz`-Eintrag, Folgearbeit):
  konstruktive und chemische Schutzmassnahmen an exponierten
  Stirnseiten nach DIN 68800-2. Trigger: erste Bemessung mit
  Bewitterungs-Beurteilung.
- **Anschnitt** (`anschnitt`-Eintrag, Folgearbeit als Bearbeitungs-
  Subtyp; siehe `hg_bearbeitung.md`): Bearbeitung am Bauteilende mit
  Schnittwinkel ≠ π/2. Trigger: erstes Tool, das angeschnittene
  Bauteilenden modelliert.
- **Plattenkante** (`plattenkante`-Eintrag, Folgearbeit): Stirn-
  Entsprechung bei Plattenbauteilen, mit von der Stirnseite
  abweichender Definition (Faserrichtung-Modus-Spezifika nach
  `hg_faserrichtungs_modus.md`). Trigger: erstes Plattenbauteil mit
  expliziter Kantenmodellierung.

## Quellen

**Primär (normativ):**

- DIN 4074-1:2012-06, „Sortierung von Holz nach der Tragfähigkeit
  – Teil 1: Nadelschnittholz", DIN Deutsches Institut für Normung,
  Berlin.
- DIN 68800-2:2022-02, „Holzschutz – Teil 2: Vorbeugende bauliche
  Maßnahmen im Hochbau", DIN Deutsches Institut für Normung,
  Berlin.
- DIN EN 1995-1-1:2010-12, „Eurocode 5: Bemessung und Konstruktion
  von Holzbauten – Teil 1-1: Allgemeines – Allgemeine Regeln und
  Regeln für den Hochbau".
- DIN EN 350:2016-12, „Dauerhaftigkeit von Holz und Holzprodukten".

**Sekundär:**

- Mönck, W.; Rug, W.: *Holzbau – Bemessung und Konstruktion.*
  16. Auflage, Beuth, Berlin 2015.
- Natterer, J.; Herzog, T.; Volz, M.: *Holzbau-Atlas.* 4. Auflage,
  Birkhäuser, Basel 2003.
- Gerner, M.: *Fachwerk – Instandsetzung, Sanierung, Neubau.*
  DVA, 7. Auflage 2007.
- Lignum (Hrsg.): *Holzbautabellen HBT.* Lignum, Zürich, aktuelle
  Auflage.

**Korpus (nicht autoritativ):**

- Wikipedia, Lemma „Hirnholz" (abgerufen 2026-05-09).
- holzhandel-deutschland.de, Glossar „Hirnholz" (abgerufen
  2026-05-09).
- baumundborke.com, Lexikon „Hirnholz / Stirnholz" (abgerufen
  2026-05-09).
- leyendecker.de, Holz-Glossar „Hirnholz" (abgerufen 2026-05-09).
