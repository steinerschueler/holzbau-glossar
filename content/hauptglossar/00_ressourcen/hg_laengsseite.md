---
id: laengsseite
benennung: Längsseite
synonyme: ["Längsfläche", "Bauteillängsseite", "Mantelfläche (eines Stab-Bauteils)"]
abgelehnte_benennungen: ["Seitenfläche", "Längsseite des Brettes", "side face", "lateral face", "long side"]
oberbegriff: bauteilflaeche
begriffstyp: generisch
voraussetzungen: [bauteilflaeche, polygon, ebene, bauteil, bauteilachse, faserrichtung, querschnitt, toleranzen]
abgrenzung_zu: [polygon, ebene, stirnseite, bauteilachse, faserrichtung, querschnitt]
status: entwurf
theorie_pflichtig: required
quellen_primär:
  - "DIN 4074-1:2012-06, 'Sortierung von Holz nach der Tragfähigkeit – Teil 1: Nadelschnittholz', Abschnitt 5 (Sortiermerkmale): Sortierung an den Längsseiten (Brettseiten) durch visuelle Inspektion der Längsmaserung; an den Schmal- und Breitseiten."
  - "DIN EN 14081-1:2019-10, 'Holzbauwerke – Nach Festigkeit sortiertes Bauholz mit rechteckigem Querschnitt – Teil 1', Bezugnahme auf Schmal- und Breitseite eines rechteckigen Querschnitts."
  - "DIN EN 1995-1-1:2010-12 (Eurocode 5), Abschnitt 6 und 8 (Bemessung): Lasteinleitung in Bauteile rechtwinklig oder parallel zur Faser an den Längsseiten."
  - "DIN ISO 80000-2:2022-08, Abschnitt 2 (Geometrie): Polygon (siehe `hg_polygon.md`); eine Längsseite ist ein Polygon mit Bauteilrolle."
quellen_sekundär:
  - "Mönck, W.; Rug, W.: Holzbau – Bemessung und Konstruktion. 16. Aufl., Beuth, Berlin 2015, Kap. 2 'Holz als Werkstoff' und Kap. 4 'Stabbauteile'."
  - "Natterer, J.; Herzog, T.; Volz, M.: Holzbau-Atlas. 4. Aufl., Birkhäuser, Basel 2003, Kap. 'Werkstoff Holz' und 'Bauteile'."
  - "Gerner, M.: Fachwerk – Instandsetzung, Sanierung, Neubau. DVA, 7. Aufl. 2007, Glossar 'Brett — Schmalseite — Breitseite'."
  - "Lignum (Hrsg.): Holzbautabellen HBT, Lignum, Zürich, aktuelle Auflage, Kap. 'Bauteile und Querschnitte'."
quellenkonflikt: |
  Die konsultierten Holzbau-Normen (DIN 4074-1, DIN EN 14081-1,
  DIN EN 1995-1-1) verwenden „Schmalseite" und „Breitseite" eines
  rechteckigen Bauholz-Querschnitts als gegebene Begriffe, ohne
  einen geometrisch geschlossenen Oberbegriff „Längsseite"
  einzuführen. Die Sekundärliteratur (Mönck/Rug, Natterer/Herzog,
  Gerner) verwendet „Längsseite" oder „Brettseite" weitgehend
  synonym für die zur Bauteilachse parallelen Aussenflächen eines
  Stab-Bauteils.

  Eric hat die folgende Festlegung getroffen (in der vorigen
  Klärungsrunde bestätigt):

  - **Kein Sammelbegriff `bauteilflaeche`**: Stirnseite und
    Längsseite werden als getrennte Glossarbegriffe direkt unter
    `polygon` (in Berandungs-Lesart, siehe `hg_polygon.md`, Abschnitt
    „Zwei zulässige Lesarten") geführt. Ein abstrakter Sammel-
    Oberbegriff `bauteilflaeche` ist nicht eingeführt; er ist als
    Folgearbeit-Trigger im Block „Folgearbeit" benannt (Trigger:
    erste Domänen-Klasse oder Visualisierungs-Operation, die
    Stirn- und Längsseite einheitlich adressieren muss).

  Eigene Festlegung in diesem Glossar:

  - **Längsseite** ist eine ebene, polygonal berandete
    Aussenfläche eines Stabbauteils, deren Trägerebene **parallel
    zur Bauteilachse** liegt und in der die Faserrichtung **in
    der Trägerebene** verläuft (im Standardfall axialer
    Faserrichtung).
  - **Schmalseite** und **Breitseite** sind Spezialisierungen der
    Längsseite für Bauteile mit rechteckigem Querschnitt
    (`rechteck_querschnitt`); sie werden in einem eigenen
    Folge-Eintrag definiert (Trigger: erstes Tool, das die
    Schmal-/Breit-Unterscheidung benötigt, etwa für
    Faserneigungs-Sortierung). Im vorliegenden Eintrag werden
    sie als Spezialisierungen referenziert, aber nicht als
    eigene Begriffe ausgeführt.
  - **Längsseite ist nur für Stabbauteile definiert**.
    Plattenbauteile haben Plattenflächen (Oberseite, Unterseite)
    und Plattenkanten (siehe Folgearbeit `plattenkante`); diese
    sind eigene Begriffe.
  - Längsseite und Stirnseite sind disjunkte Bauteilflächen-
    Kategorien (siehe `hg_stirnseite.md`, Erläuterung); ein Stab-
    Bauteil mit Rechteckquerschnitt hat genau zwei Stirnseiten
    und vier Längsseiten.

  Diese Festlegung ist konsistent mit allen konsultierten Quellen.
---

## Prosa-Definition

Eine **Längsseite** ist eine ebene, polygonal berandete Aussenfläche
eines Stabbauteils, deren Trägerebene parallel zur Bauteilachse liegt
und in deren Trägerebene die Faserrichtung des Bauteils im Standardfall
axialer Faserrichtung verläuft.

## Mathematische Definition

Sei

- B ein **Stabbauteil** im Sinne von `bauteil` mit Stabgeometrie
  (`geometrie ∈ 𝒢_stab`),
- A(B) = Bauteilachse(B) die Bauteilachse mit Tangentenrichtung
  d̂(s) ∈ S² an der Stelle s ∈ [0, L] (siehe `bauteilachse`),
- ∂G_B^lokal die Oberfläche des Bauteilkörpers im Bauteil-Lokal-
  System,
- F ⊂ ∂G_B^lokal eine ebene polygonal berandete Teilfläche der
  Bauteiloberfläche mit Trägerebene E_F und Trägerebenen-Normaler
  n̂_F ∈ S²,
- ε_W := Toleranzen.WINKEL_EPS.

Die Teilfläche F heißt eine **Längsseite** von B genau dann, wenn
gilt:

1. **Bauteilachsen-Parallelität der Trägerebene**: Die
   Bauteilachsen-Tangente d̂(s) liegt in der Trägerebene E_F:
   ```
   |⟨n̂_F, d̂(s)⟩| ≤ ε_W   für alle s ∈ [0, L].                     (1)
   ```
   Im prismatischen Fall (konstantes d̂(s) = d̂) reduziert sich (1)
   auf die einzelne Bedingung |⟨n̂_F, d̂⟩| ≤ ε_W.

2. **Aussenflächen-Eigenschaft**: F ist eine zusammenhängende ebene
   Teilfläche der Bauteiloberfläche ∂G_B^lokal mit nicht-leerem
   Inneren (positives Flächenmass).

3. **Polygonale Berandung**: ∂F ist eine Polygonkurve in E_F (siehe
   `polygon`).

4. **Aussennormalen-Konvention**: n̂_F zeigt aus dem Bauteil heraus.

**Faserrichtungs-Bedingung** (zur Abgrenzung von der Stirnseite,
siehe `stirnseite`): Sei f̂ ∈ S² die Faserrichtung des Bauteils
(siehe `faserrichtung`, Modus HART). Im Standardfall axialer
Faserrichtung (f̂ ∥ d̂) gilt

```
|⟨n̂_F, f̂⟩| ≤ ε_W,                                                  (2)
```

d. h. die Faserrichtung **liegt in der Trägerebene** der Längsseite —
im Gegensatz zur Stirnseite, an der die Faserrichtung mit einer
wesentlichen Komponente quer zur Trägerebene verläuft.

## Wohldefiniertheit

- **Existenz**: Für jedes Stabbauteil mit Rechteckquerschnitt
  existieren konstruktiv vier Längsseiten (Oberseite, Unterseite,
  zwei Schmalseiten); ihre Trägerebenen sind durch die
  Bauteilachse und die Querschnittsorientierung eindeutig
  bestimmt.
- **Eindeutigkeit**: Bei festgelegtem prismatischen Bauteilkörper
  und Querschnitt sind die Längsseiten als ebene Teilflächen der
  Bauteiloberfläche eindeutig bestimmt; sie entsprechen den
  Querschnitts-Kantenrichtungen, gesweept entlang der
  Bauteilachse.
- **Anzahl bei Standard-Querschnitten**:
  - **Rechteckquerschnitt**: vier Längsseiten (zwei Breitseiten
    + zwei Schmalseiten).
  - **Rundquerschnitt**: eine zylindrische Mantelfläche, die nicht
    eben ist und damit **keine Längsseite** im Sinne dieses
    Glossars ist (sondern eine Mantelfläche; siehe Folgearbeit
    `mantelflaeche` für rotationssymmetrische Stab-Bauteile).
  - **I-, T-, L-Profil-Querschnitt**: mehrere Längsseiten gemäß
    der Anzahl ebener Aussen-Teilflächen des Profils.
  - **Beliebig polygonaler Querschnitt mit k Eckpunkten**: k
    Längsseiten, je eine pro Polygonkante.
- **Disjunktheit von Längsseite und Stirnseite**: Aus (1)
  folgt |⟨n̂_F, d̂⟩| ≤ ε_W, während für die Stirnseite per
  `stirnseite` Gleichung (3) bzw. (4) |⟨n̂_S, d̂⟩| ≥ cos(α_AS) >
  ε_W gilt (für jeden zulässigen Anschnittwinkel α_AS < π/2 −
  ε_W). Die beiden Bedingungen sind unvereinbar; eine ebene
  Teilfläche der Bauteiloberfläche ist entweder Längsseite oder
  Stirnseite, nicht beides.
- **Wohldefiniertheit der Trägerebene**: Die Trägerebene jeder
  Längsseite ist eine Ebene im Sinne von `ebene`; sie wird durch
  einen beliebigen Eckpunkt der Längsseiten-Polygonberandung und
  die Aussennormale n̂_F repräsentiert (Hesse-Normalform).
- **Wohldefiniertheit der Aussennormale**: Da F Aussenfläche des
  Bauteilkörpers ist, gibt es eine eindeutige aus dem Bauteil heraus
  zeigende Normalenrichtung; die andere Wahl (in das Bauteil hinein)
  ist durch Bedingung 4 ausgeschlossen.
- **Faserrichtungs-Bedingung (2) ist nicht-konstitutiv**: Bedingung
  (2) charakterisiert den Längsseiten-Begriff für Bauteile mit
  axialer Faserrichtung; bei Drehwuchs, Schrägsägung oder
  Faserrichtungs-Modi STRUKTURIERT/SCHWACH/KEINE
  (Memory `project_faserrichtung_modi`) kann sie verletzt sein,
  ohne dass die geometrische Längsseiten-Eigenschaft betroffen ist.
  Sie ist semantisch erläuternd, nicht validierend.
- **Nicht-Zirkularität**: Die Definition stützt sich auf
  `polygon`, `ebene`, `bauteil`, `bauteilachse`, `faserrichtung`,
  `querschnitt`, `toleranzen` und nimmt nicht auf sich selbst
  Bezug.

## Erläuterung (nicht normativ)

### Bedeutung im Holzbau

Die Längsseite ist diejenige Bauteilfläche, an der das **Längsholz**
sichtbar ist: die Faserrichtung läuft in der Fläche, die
Längsmaserung ist sichtbar, die Jahresringe erscheinen je nach
Schnittlage als Streifen (Riftschnitt), Flammen (Sehnenschnitt)
oder Kombinationen. Längsseiten sind die **dominanten Flächen** für
Lasteinleitung und Auflagerung im Holzbau:

1. **Auflagerung**: Sparren liegen mit der Unterseite (einer
   Längsseite) auf der Pfette auf; die Pfette wiederum liegt mit
   ihrer Unterseite (auch eine Längsseite) auf der Wand auf. Die
   Druckkraft wirkt rechtwinklig zur Faser (Holz ist quer zur
   Faser etwa um den Faktor 10 weicher als längs zur Faser; siehe
   EC5 Abschnitt 6).
2. **Verbindungen**: Schrauben und Stabdübel werden bevorzugt
   durch Längsseiten geführt (Lasteinleitung rechtwinklig zur
   Faser hat höhere Tragfähigkeit als längs zur Faser, siehe
   `stirnseite` und EC5 8.5).
3. **Sichtoberflächen**: bei sichtbar bleibenden Bauteilen
   (Dachuntersicht, Fachwerk, Sichtholzdecke) sind die Längsseiten
   die ästhetisch dominanten Flächen.

### Spezialisierungen Schmalseite und Breitseite

Bei einem Stabbauteil mit **rechteckigem Querschnitt** (Standardfall
im Holzbau, siehe `rechteck_querschnitt`) werden die vier
Längsseiten konventionell unterschieden:

- **Breitseite** (auch: Brettseite): die beiden Längsseiten
  parallel zur Querschnitt-Längsachse (Querschnittshöhe). Bei
  einem Sparren 80/200 sind die Breitseiten 200 mm hoch.
  Standardmässig die Sicht- und Auflagerseiten (Sparren-Oberseite
  trägt die Lattung; Sparren-Unterseite ist Untersicht;
  Pfetten-Oberseite trägt die Sparren).
- **Schmalseite**: die beiden Längsseiten parallel zur
  Querschnitt-Querachse (Querschnittsbreite). Bei einem Sparren
  80/200 sind die Schmalseiten 80 mm breit. Konstruktiv treten
  Schmalseiten auf bei seitlichen Sparrenschalungen, bei der
  Stossfuge zweier nebeneinanderliegender Sparren oder bei der
  Schmalseiten-Besichtigung für die Sortierung nach DIN 4074-1.

Schmalseite und Breitseite werden als **eigene Folge-Einträge**
geführt (Trigger: erstes Tool oder Bemessungs-Schritt mit
expliziter Schmal-/Breit-Unterscheidung — z. B. Faserneigungs-
Sortierung, Visualisierung der Sicht-Untersicht).

### Längsseite vs. Stirnseite

| Eigenschaft                | Längsseite                         | Stirnseite                          |
|----------------------------|------------------------------------|-------------------------------------|
| Trägerebene zur Bauteilachse | parallel                          | rechtwinklig (im Standardfall)      |
| Faserrichtung               | in der Trägerebene                | quer zur Trägerebene (Faser tritt aus) |
| Anzahl bei Rechteck-Stab    | 4 (Oberseite, Unterseite, 2 Schmalseiten) | 2 (Anfang, Ende)             |
| Lasteinleitung              | rechtwinklig zur Faser (hoch tragfähig) | parallel zur Faser (gering tragfähig) |
| Bewitterungs-Anfälligkeit   | gering                            | hoch (Hirnholz)                     |
| Sichtfläche im Werkplan     | dominante Sichtfläche             | begleitende Sichtkante              |

### Abgrenzung zu Mantelflächen rotationssymmetrischer Stäbe

Die zylindrische Mantelfläche einer **Rundholzstütze** ist nicht
eben und damit **keine Längsseite** im Sinne dieses Glossars. Sie
wird in einem Folge-Eintrag `mantelflaeche` (Folgearbeit, Trigger:
erstes Bauteil mit Rundquerschnitt) als eigener Begriff geführt;
die Begriffe Längsseite und Mantelfläche sind disjunkt.

## Beziehungen

- **Oberbegriff**: `polygon` (in Berandungs-Lesart, siehe
  `hg_polygon.md`, Abschnitt „Zwei zulässige Lesarten"). Die
  Längsseite ist ein ebenes Polygon auf der Bauteiloberfläche mit
  zusätzlicher Bauteilrolle (Aussenfläche eines Stab-Bauteils,
  Trägerebene parallel zur Bauteilachse) und Aussennormalen-
  Konvention. Die Stirnseite (`stirnseite`) ist symmetrisch dazu
  unter demselben Oberbegriff `polygon` in Berandungs-Lesart
  geführt.
- **Spezialisierungen** (Folgearbeit):
  - **Schmalseite** (`schmalseite`, Folgearbeit): Längsseite eines
    Bauteils mit rechteckigem Querschnitt parallel zur
    Querschnitts-Querachse (Querschnittsbreite). Trigger: erstes
    Tool mit expliziter Schmal-/Breit-Unterscheidung.
  - **Breitseite** (`breitseite`, Folgearbeit): Längsseite eines
    Bauteils mit rechteckigem Querschnitt parallel zur
    Querschnitts-Längsachse (Querschnittshöhe). Trigger:
    siehe Schmalseite.
- **Bestandteile (partitiv)** (geerbt von `polygon`):
  - **Polygonberandung** ∂F (geerbt von `polygon`).
  - **Trägerebene** E_F (geerbt von `polygon`).
  - **Aussennormalen-Vektor** n̂_F (per Konvention aus dem Bauteil
    heraus zeigend).
  - **Längsausdehnung** entlang der Bauteilachse: ‖p_e − p_a‖
    (= Bauteillänge L im prismatischen Fall).
- **Verwendung**:
  - **Auflagerung**: Längsseite trägt Druckkräfte rechtwinklig zur
    Faser ein.
  - **Verbindungen** (`verbindungsmittel`): Schrauben, Stabdübel,
    Bolzen werden bevorzugt durch Längsseiten geführt.
  - **Bearbeitungen** (`bearbeitung`): Kerven, Versätze, Schlitze,
    Bohrungen liegen typisch an einer Längsseite.
  - **Faserneigungs-Sortierung** (DIN 4074-1): die Sortier-
    Inspektion erfolgt an Schmal- und Breitseite.
  - **3D-Visualisierung**: Längsseiten erhalten typisch eine
    Längsmaserungs-Texturierung, die sich von der Hirnholz-
    Texturierung der Stirnseiten unterscheidet.
- **Abgrenzung**:
  - **Polygon** (`polygon`): allgemeines geometrisches Primitiv
    ohne Bauteilrolle. Die Längsseite ist ein Polygon mit
    zugewiesener Bauteilrolle und Aussennormalen-Konvention.
  - **Ebene** (`ebene`): die Trägerebene einer Längsseite ist eine
    Ebene; die Längsseite ist eine **beschränkte** Teilmenge mit
    polygonaler Berandung und Bauteilrolle.
  - **Stirnseite** (`stirnseite`): zur Bauteilachse rechtwinklige
    Endfläche; Faser tritt durch die Trägerebene aus. Längsseite
    und Stirnseite sind disjunkte Bauteilflächen-Kategorien
    (siehe Wohldefiniertheits-Abschnitt).
  - **Bauteilachse** (`bauteilachse`): die Bauteilachse liegt in
    der Trägerebene jeder Längsseite (im prismatischen Fall sogar
    auf gleicher Höhe wie die Längsseite, parallel verschoben um
    die halbe Querschnittsdimension); sie ist aber nicht selbst
    die Längsseite.
  - **Faserrichtung** (`faserrichtung`): bei axialer Faserrichtung
    liegt die Faser in der Trägerebene jeder Längsseite (Bedingung
    (2)); bei Drehwuchs oder Plattenwerkstoff-Modi gilt das nicht
    universell. Die Faserrichtung ist Bauteil-Annotation, die
    Längsseite eine Bauteilfläche.
  - **Querschnitt** (`querschnitt`): die Längsseiten eines
    prismatischen Bauteils sind die Spuren der Querschnittskanten
    entlang der Bauteilachse (Sweep des Querschnitts). Die
    Längsseite hat den Querschnitt als implizite Erzeugende, ist
    aber nicht selbst der Querschnitt.
  - **Bauteilfläche** (`bauteilflaeche`, Folgearbeit): Längsseite
    und Stirnseite sind die beiden disjunkten Bauteilflächen-
    Kategorien an einem Stabbauteil. Beide sind symmetrisch unter
    `polygon` (Berandungs-Lesart) geführt, ohne gemeinsamen
    Sammel-Oberbegriff. Ein expliziter Begriff `bauteilflaeche`
    als Sammelkategorie ist Folgearbeit (siehe Folgearbeit-Block).

## Implementierungshinweis

Datentyp (Domänen-Schicht, Kotlin, Schicht
`domain.bauteil.flaeche`):

```kotlin
package domain.bauteil.flaeche

import domain.bauteil.querschnitt.QuerschnittsKantenIndex
import domain.geometrie.Ebene
import domain.geometrie.KonvexesPolygon
import domain.geometrie.Vektor

/**
 * Längsseite: Aussenfläche eines Stab-Bauteils mit Trägerebene
 * parallel zur Bauteilachse.
 *
 * Glossar: hg_laengsseite.md
 *
 * Aussennormale n̂_F zeigt per Konvention aus dem Bauteil heraus.
 *
 * Beim Rechteckquerschnitt sind vier Längsseiten konstruierbar;
 * sie werden über den Querschnitts-Kantenindex (Schmal-/Breitseite,
 * Folgearbeit) identifiziert.
 */
data class Laengsseite(
    val polygon: KonvexesPolygon,           // ∂F mit Trägerebene
    val aussennormale: Vektor,               // n̂_F, ‖aussennormale‖ ≈ 1
    val querschnittsKante: QuerschnittsKantenIndex,  // Index der Querschnitts-
                                                      // erzeugendenkante; Folgearbeit
)
```

- **Einheit**: Polygonkoordinaten in mm; Vektor dimensionslos
  (Einheitsvektor).
- **Identität**: keine eigene UUID. Die Längsseite ist eine
  abgeleitete Sicht auf die Bauteiloberfläche; sie wird konstruktiv
  aus dem Bauteil bezogen, nicht persistiert.
- **Pflicht- und Optionalfelder**:
  - `polygon` — Pflicht; ebenes Polygon der Längsseiten-Berandung.
  - `aussennormale` — Pflicht; per Konvention aus dem Bauteil heraus.
  - `querschnittsKante` — Pflicht; Index der erzeugenden
    Querschnittskante. Der Datentyp `QuerschnittsKantenIndex` ist
    Folgearbeit (Trigger: erste Visualisierung mit
    Schmal-/Breitseiten-Unterscheidung).
- **Invarianten** (in Companion-Factory `Laengsseite.aus(bauteil,
  querschnittsKante)`, `Resultat.Fehler` bei Verletzung; keine
  Exception):
  1. `aussennormale` ist normiert (‖aussennormale‖ ≈ 1 innerhalb
     `Toleranzen.NORM_EPS`).
  2. Die Trägerebene des Polygons enthält die Bauteilachsen-Tangente:
     |⟨aussennormale, d̂⟩| ≤ Toleranzen.WINKEL_EPS (Bedingung (1)).
  3. Die `querschnittsKante` ist konsistent mit dem Querschnitt
     des Bauteils (Index liegt in [0, k−1] für einen Querschnitt
     mit k Kanten).
- **Konstruktion**: Die Längsseite wird **abgeleitet** aus dem
  Bauteil und dem Querschnitts-Kantenindex; sie wird **nicht** als
  unabhängiges Objekt konstruiert. Die Domänen-Schicht stellt
  Faktor-Funktionen `Bauteil.laengsseiten()` und
  `Bauteil.laengsseiteAn(kantenIndex)` bereit.
- **IFC-Mapping** (Persistenzschicht, Phase 4):
  - Längsseite wird nicht als eigene IFC-Entität geführt; sie ist
    eine Sicht auf die Mantelfläche des
    `IfcExtrudedAreaSolid`-Sweep-Körpers.
- **Edge Cases**:
  - **Längsseite an einem Bauteil mit Rundquerschnitt**: die
    Mantelfläche ist nicht eben; in diesem Glossar nicht als
    Längsseite geführt. Stattdessen Folgearbeit `mantelflaeche`
    für rotationssymmetrische Stab-Bauteile.
  - **Längsseite an einem Bauteil mit Drehwuchs/Schrägsägung**:
    die Faserrichtungs-Bedingung (2) kann verletzt sein; die
    geometrische Längsseite bleibt definiert.
  - **Bauteil mit Faserrichtungs-Modus SCHWACH oder KEINE** (z. B.
    OSB, Spanplatte): Bedingung (2) nicht sinnvoll; die App
    bevorzugt für Plattenwerkstoffe ohnehin den Begriff
    `plattenflaeche` (Folgearbeit).
  - **Längsseite mit Bearbeitung** (Kerve, Versatz, Schlitz):
    die Polygonberandung der Längsseite wird durch die Bearbeitung
    modifiziert; die App führt entweder die ungeschwächte
    Längsseite mit zusätzlicher Bearbeitungsliste oder die
    bearbeitete Längsseite mit komplexerer Polygonberandung. Die
    Wahl ist Implementierungssache der Geometrie-Schicht
    (Folgearbeit Phase 3.2).
- **Bezeichner-Konvention** (CLAUDE.md): Klasse heißt `Laengsseite`
  (deutsch, Glossarbegriff; ASCII-Schreibweise wegen
  Kotlin-Identifier-Konvention).

**Folgearbeit (trigger-basiert):**

- **Bauteilfläche** (`bauteilflaeche`-Eintrag, Folgearbeit):
  Sammelkategorie für Stirnseite und Längsseite als die beiden
  disjunkten ebenen Aussenflächen-Klassen eines Stabbauteils.
  Die Symmetrie der beiden Begriffe unter `polygon`
  (Berandungs-Lesart) reicht derzeit ohne expliziten
  Sammel-Oberbegriff. Trigger: erste Domänen-Klasse oder
  Visualisierungs-Operation, die Stirn- und Längsseite einheitlich
  als „Bauteilfläche" adressieren muss (z. B. Sammel-Iteration
  über alle Aussenflächen eines Bauteils, einheitliche
  Aussennormalen-Behandlung im Renderer).
- **Schmalseite** (`schmalseite`-Eintrag und -Klasse):
  Längsseite eines Bauteils mit rechteckigem Querschnitt parallel
  zur Querschnittsbreite. Trigger: erstes Tool mit Schmal-/Breit-
  Unterscheidung (Faserneigungs-Sortierung, Sicht-Untersicht-
  Markierung).
- **Breitseite** (`breitseite`-Eintrag und -Klasse): siehe
  Schmalseite.
- **Mantelfläche** (`mantelflaeche`-Eintrag): nicht-ebene Mantel-
  fläche rotationssymmetrischer Stab-Bauteile (Rundholzstütze).
  Trigger: erstes Bauteil mit Rundquerschnitt.
- **Plattenfläche** (`plattenflaeche`-Eintrag): Stirn-Entsprechung
  bei Plattenbauteilen (Oberseite, Unterseite einer Platte). Trigger:
  erstes Plattenbauteil mit expliziter Flächenmodellierung.
- **Querschnitts-Kantenindex**
  (`QuerschnittsKantenIndex`-Datentyp): Indizierung der Längsseiten
  über die Querschnittskanten. Trigger: erste Visualisierung mit
  Schmal-/Breitseiten-Unterscheidung.

## Quellen

**Primär (normativ):**

- DIN 4074-1:2012-06, „Sortierung von Holz nach der Tragfähigkeit
  – Teil 1: Nadelschnittholz", DIN Deutsches Institut für Normung,
  Berlin.
- DIN EN 14081-1:2019-10, „Holzbauwerke – Nach Festigkeit
  sortiertes Bauholz mit rechteckigem Querschnitt – Teil 1".
- DIN EN 1995-1-1:2010-12, „Eurocode 5: Bemessung und Konstruktion
  von Holzbauten – Teil 1-1".
- DIN ISO 80000-2:2022-08, „Größen und Einheiten – Teil 2:
  Mathematik", Abschnitt 2.

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

- Holzbau Deutschland, Merkblatt „Begriffe und Klassifizierungen
  für den Holzbau" (abgerufen 2026-05-09).
- Wikipedia, Lemma „Schnittholz" (abgerufen 2026-05-09).
