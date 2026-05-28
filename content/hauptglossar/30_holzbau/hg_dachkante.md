---
id: dachkante
benennung: Dachkante
synonyme: [Dachrandkante, "Begrenzungskante einer Dachfläche"]
abgelehnte_benennungen: [Dachrand, Dachkontur, "roof edge"]
oberbegriff: strecke
begriffstyp: generisch
voraussetzungen: [strecke, dachflaeche, polygon, vektor, toleranzen]
abgrenzung_zu: [traufe, first, ortgang, grat, kehle, pultkante, dachflaeche, polygon]
status: entwurf
theorie_pflichtig: required
quellen_primär:
  - "SIA 232/1:2020 'Geneigte Dächer', Schweizerischer Ingenieur- und Architektenverein, Abschnitt 1 (Begriffe und geometrische Grundlagen): die Begriffe Traufe, First, Ortgang, Grat, Kehle werden als geometrische Begrenzungslinien einer Dachfläche eingeführt."
  - "DIN 1356-1:1995-02 'Bauzeichnungen – Teil 1: Arten, Inhalte und Grundregeln der Darstellung', Abschnitt 5 (Darstellung von Dächern)."
  - "DIN 18338:2019-09 'VOB Teil C: Dachdeckungs- und Dachabdichtungsarbeiten', Abschnitt 0 (Begriffe für Dachflächenränder)."
quellen_sekundär:
  - "Mönck, W.; Rug, W.: Holzbau – Bemessung und Konstruktion. 16. Aufl., Beuth Verlag 2015, Kap. Dachformen."
  - "Gerner, M.: Fachwerk – Instandsetzung, Sanierung, Neubau. DVA, 7. Aufl. 2007, Glossar 'Dach'."
  - "Lignum (Hrsg.): Lignatec 'Geneigte Dächer in Holzbauweise', Lignum, Zürich, aktuelle Auflage."
quellenkonflikt: |
  Keine konsultierte Norm führt einen ausdrücklichen Sammelbegriff
  „Dachkante" als Oberbegriff für Traufe, First, Ortgang, Grat, Kehle
  und Pultkante. SIA 232/1 und DIN 1356 listen die Einzelbegriffe
  parallel auf, ohne sie zu klassifizieren. Eigene Festlegung:
  Dachkante ist der gemeinsame geometrische Oberbegriff für jede
  eindimensionale, gerade oder polygonale Begrenzungslinie einer
  Dachfläche, die entweder im Rand eines Dachflächen-Polygons oder
  als Schnittlinie zweier Dachflächen-Ebenen liegt. Diese Festlegung
  ist konsistent mit allen konsultierten Quellen und vermeidet die
  redundante Wiederholung des partitiven Schemas in jedem
  Spezialeintrag (Traufe, First, Ortgang, …).
---

## Prosa-Definition

Eine **Dachkante** ist eine Strecke oder ein Streckenzug im
dreidimensionalen Raum, die entweder vollständig im Rand des Polygons
einer Dachfläche liegt (Randkante) oder als Schnittmenge der
abgeschlossenen Polygonbereiche zweier benachbarter Dachflächen auf
deren gemeinsamer Schnittgerade verläuft (Schnittkante), und die als
geometrische Begrenzung mindestens einer Dachfläche fungiert.

## Mathematische Definition

Sei

- 𝒟 = { D₁, …, D_m } eine endliche Familie von Dachflächen
  D_i = (E_i, P_i, n_{a,i}) im Sinne von `dachflaeche`,
- F(P_i) ⊂ E_i das von P_i berandete, abgeschlossene Flächenstück
  und ∂F(P_i) sein Rand (geschlossener Polygonzug),
- s ⊂ ℝ³ eine Strecke (im Sinne von `strecke`) oder ein endlicher
  Streckenzug (Vereinigung endlich vieler Strecken mit gemeinsamen
  Endpunkten an den Knickstellen).

Dann heißt s eine **Dachkante** der Familie 𝒟 genau dann, wenn
mindestens eine der folgenden Bedingungen erfüllt ist:

1. **Randkante**: Es existiert ein Index i ∈ {1, …, m} mit
   ```
   s ⊂ ∂F(P_i),
   ```
   d. h. s ist ganz im Rand des Polygons der Dachfläche D_i enthalten.

2. **Schnittkante**: Es existieren Indizes i ≠ j mit
   ```
   s ⊂ F(P_i) ∩ F(P_j) ⊂ E_i ∩ E_j,
   ```
   d. h. s liegt im gemeinsamen abgeschlossenen Polygonbereich beider
   Dachflächen und folglich auf der Schnittgeraden der Trägerebenen.
   Insbesondere gilt s ⊂ ∂F(P_i) ∩ ∂F(P_j).

In beiden Fällen muss s nicht-entartet sein, also positive
Gesamtlänge ℓ(s) > Toleranzen.LAENGE_EPS haben.

## Wohldefiniertheit

- **Existenz**: Jeder Polygonrand ∂F(P_i) ist eine endliche
  Vereinigung nicht-entarteter Strecken (Polygonkanten); jede dieser
  Polygonkanten ist nach Bedingung 1 eine Dachkante. Eine
  Schnittkante existiert genau dann, wenn die Polygone zweier
  Dachflächen einen gemeinsamen Streckenanteil besitzen — bei
  Sattel-, Walm-, Pult- und Mansarddächern ist dies konstruktiv
  garantiert.
- **Eindeutigkeit der Klassifikation**: Eine Strecke kann gleichzeitig
  Randkante (zweier Dachflächen) und Schnittkante sein; das ist genau
  der Regelfall an First, Grat und Kehle. Die Klassifikation in die
  Spezialfälle (Traufe, First, …) erfolgt dann durch zusätzliche
  geometrische Bedingungen (Lage zur Horizontalen, relative Höhe,
  Anschluss an Giebelwand) — siehe die jeweiligen Einträge.
- **Nicht-Zirkularität**: Die Definition stützt sich nur auf die
  bereits definierten Begriffe `strecke`, `dachflaeche`, `polygon`
  und auf elementare Mengentheorie.

## Erläuterung (nicht normativ)

Der Begriff Dachkante fasst alle eindimensionalen Begrenzungslinien
einer Dachfläche zusammen, gleich ob sie am unteren Rand (Traufe), am
oberen Rand (First, Pultkante) oder an einer Seitenflanke (Ortgang,
Grat, Kehle) liegen. Die genaue Benennung der Einzelkante ergibt sich
aus ihrer Lage und Funktion und wird in den Spezialeinträgen
geometrisch präzisiert.

Dachkanten treten in der App an drei Stellen auf:

- als Anschlusslinien für konstruktive Detailbauteile (Traufbohle,
  Firstpfette, Ortbrett, Gratsparren, Kehlsparren),
- als Linien für die Bemaßung in Rissen (Trauflänge, Firstlänge,
  Ortganglänge),
- als Trennlinien beim Stückeln der Dachhaut (Dachüberstand,
  Anschlussdetails).

## Beziehungen

- **Oberbegriff**: `strecke` (im Regelfall) bzw. eine Vereinigung von
  Strecken (Streckenzug). In der Domänen-Schicht wird die geknickte
  Variante als `Streckenzug` modelliert; eine einzelne Strecke ist
  ein Streckenzug der Länge 1.
- **Teilbegriffe (Spezialisierungen)** — alle in Folgeeinträgen
  präzisiert:
  - **Traufe** (`traufe`): untere, näherungsweise horizontale
    Randkante.
  - **First** (`first`): obere Schnittkante zweier nach oben
    zusammenlaufender Dachflächen.
  - **Ortgang** (`ortgang`): seitliche, geneigte Randkante an einer
    Giebelwand.
  - **Grat** (`grat`): geneigte konvexe Schnittkante zweier
    Dachflächen an einem ausspringenden Eck (z. B. Walmdach-Ecke).
  - **Kehle** (`kehle`): geneigte konkave Schnittkante zweier
    Dachflächen an einem einspringenden Eck.
  - **Pultkante** (`pultkante`): obere horizontale Randkante einer
    Pultdachfläche, an der keine zweite Dachfläche anschließt.

Die sechs Spezialisierungen sind als **disjunkte** Klassifikation
angelegt: Eine Dachkante einer korrekt modellierten
Dachflächenfamilie soll genau einer dieser sechs Klassen zugeordnet
werden können. Die disjunkte Trennung erfolgt durch die in den
einzelnen Einträgen formulierten Klassifikations-Bedingungen:
- Schnittkante (First/Grat/Kehle) vs. Randkante
  (Traufe/Ortgang/Pultkante);
- innerhalb der Schnittkanten: horizontal (First) vs. geneigt
  (Grat, Kehle); innerhalb der geneigten Schnittkanten: konvex
  (Grat) vs. konkav (Kehle);
- innerhalb der Randkanten: horizontal mit niedrigster Höhe
  (Traufe), horizontal mit höchster Höhe (Pultkante), entlang der
  Falllinie (Ortgang).
Die sealed-Hierarchie der Implementierung ist im
Implementierungshinweis weiter unten skizziert.
- **Bestandteile (partitiv)**: Anfangs- und Endpunkt der Strecke bzw.
  Stützpunkte des Streckenzugs.
- **Abgrenzung**:
  - **Dachfläche** (`dachflaeche`): zweidimensionales
    Flächenstück; eine Dachkante ist ihre eindimensionale
    Begrenzung.
  - **Polygon** (`polygon`): die geschlossene Kontur ∂F(P_i) als
    Ganzes; eine einzelne Dachkante ist im Allgemeinen ein echter
    Teilstreckenzug eines solchen Polygonrandes.
  - **Bauteilkante** (z. B. Sparrenoberkante): physische Kante eines
    Holzbauteils, die nicht notwendig im Polygonrand einer
    Dachfläche liegt.

## Implementierungshinweis

Datentyp (Domänen-Schicht, Kotlin, Schicht `domain.bauteil`):

```
sealed class Dachkante {
    abstract val polylinie: Streckenzug   // 1..n Strecken, gemeinsame Endpunkte

    data class Randkante(
        override val polylinie: Streckenzug,
        val dachflaeche: Dachflaeche
    ) : Dachkante()

    data class Schnittkante(
        override val polylinie: Streckenzug,
        val dachflaecheA: Dachflaeche,
        val dachflaecheB: Dachflaeche
    ) : Dachkante()

    sealed class Entartet : Dachkante() {
        object Nullkante : Entartet()
        object NichtIdentifizierbar : Entartet()
    }
}
```

- **Einheit**: alle Koordinaten in mm (Double), Längen in mm.
- **Invarianten** (in Factory prüfen, niemals Exception):
  1. ℓ(polylinie) > Toleranzen.LAENGE_EPS — sonst `Entartet.Nullkante`.
  2. Jede Strecke der Polylinie liegt im jeweiligen Polygonrand bzw.
     im Schnitt der beiden Dachflächen-Polygone (geprüft mit
     `LAENGE_EPS`-Toleranz auf den Punkt-Polygon-Abstand).
- **Edge Cases**:
  - **Nullkante**: Strecke der Länge 0 (etwa bei
    zusammenfallenden Eckpunkten zweier benachbarter Dachflächen) →
    `Entartet.Nullkante`.
  - **NichtIdentifizierbar**: Strecke, die weder vollständig im
    Polygonrand einer Dachfläche noch im Schnitt zweier Dachflächen
    liegt; tritt etwa bei numerisch ungenau eingegebenen Modellen
    auf → `Entartet.NichtIdentifizierbar`.
  - **Geknickte Kante** (z. B. polygonaler First eines verzogenen
    Daches): zulässig durch Streckenzug-Modellierung; jede einzelne
    Teilstrecke muss die Lagebedingung erfüllen.
- **Klassifikation in Spezialfälle**: erfolgt in
  `DachkanteOps.kt` durch Prädikate `istTraufe(...)`,
  `istFirst(...)`, `istOrtgang(...)` etc., siehe die Einträge der
  jeweiligen Spezialbegriffe.

## Quellen

**Primär (normativ):**

- SIA 232/1:2020, „Geneigte Dächer", Schweizerischer Ingenieur- und
  Architektenverein, Abschnitt 1.
- DIN 1356-1:1995-02, „Bauzeichnungen – Teil 1: Arten, Inhalte und
  Grundregeln der Darstellung", Abschnitt 5.
- DIN 18338:2019-09, „VOB Teil C: Dachdeckungs- und
  Dachabdichtungsarbeiten", Abschnitt 0.

**Sekundär:**

- Mönck, W.; Rug, W.: *Holzbau – Bemessung und Konstruktion.*
  15. Auflage, Beuth Verlag 2015.
- Gerner, M.: *Fachwerk – Instandsetzung, Sanierung, Neubau.* DVA,
  7. Auflage 2007.
- Lignum (Hrsg.): *Lignatec — Geneigte Dächer in Holzbauweise.*
  Lignum, Zürich, aktuelle Auflage.

**Korpus (nicht autoritativ):**

- Wikipedia, Lemmata „Dach", „Traufe", „Dachfirst", „Ortgang"
  (abgerufen 2026-05-08).
