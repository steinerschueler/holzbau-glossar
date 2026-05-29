---
id: walm
benennung: Walm
synonyme: []
abgelehnte_benennungen:
  [Walmdach, Walmflaeche, Schopf, Walmdach-Ende, Walmgebinde,
   Walmkonstruktion, Eckabwalmung, Walmsparren-Aggregat,
   "hip", "hip end"]
oberbegriff: bauteilgruppe
begriffstyp: aggregat
voraussetzungen:
  [bauteilgruppe, bauteil, sparren, gratsparren, grat,
   dachflaeche, ebene, strecke, polyeder, uuid,
   lokales_koordinatensystem, weltkoordinatensystem, toleranzen]
abgrenzung_zu:
  [bauteilgruppe, binder, dach, dachflaeche, dachseite, dachform,
   dachausmittlung, sparren, gratsparren, kehlsparren, schifter,
   walmflaeche, krueppelwalm, walmdach, grat, kehle, first,
   traufe, ortgang, fusspfette, firstpfette, verbindung,
   auswechslung]
status: entwurf
subglossar_pendant: notwendig
quellen_primär:
  - "SIA 232/1:2020 'Geneigte Dächer', Schweizerischer Ingenieur- und Architektenverein, Abschnitt 1 (Begriffe und geometrische Grundlagen): Walm und Walmdach als vorausgesetzte geometrische Begriffe; keine geschlossene Aggregat-Definition."
  - "SIA 265:2021 'Holzbau', Schweizerischer Ingenieur- und Architektenverein, Abschnitt 5 (Konstruktive Durchbildung): Walmdach-Konstruktionen als vorausgesetzte Tragwerks-Familie; keine geschlossene Begriffsdefinition des Walms als Aggregat."
  - "DIN EN 1995-1-1:2010-12 (Eurocode 5), Abschnitte 5 (Tragwerksberechnung), 6 (Grenzzustände der Tragfähigkeit) und 10 (Konstruktive Durchbildung): Tragglieder von Walmdächern (Gratsparren, Schifter) vorausgesetzt; keine geschlossene Aggregat-Definition."
  - "DIN 1052:2008-12, Abschnitt 8 und Abschnitt 12 (Konstruktive Anforderungen): Tragglieder geneigter Dächer einschließlich Walmdach-Konstruktionen."
  - "DIN 1356-1:1995-02 'Bauzeichnungen – Teil 1: Arten, Inhalte und Grundregeln der Darstellung', Abschnitt 5 (Darstellung von Dächern): Walm als geometrisches Zeichnungselement des Walmdachs."
  - "DIN 18338:2019-09 'VOB Teil C: Dachdeckungs- und Dachabdichtungsarbeiten', Abschnitt 0 (Begriffe): Walmflaeche als geneigte Dachfläche am giebelseitigen Dachende."
quellen_sekundär:
  - "Lignum (Hrsg.): Holzbautabellen HBT, Lignum, Zürich, aktuelle Auflage, Kap. 'Dachtragwerke' / Walmdach-Konstruktionen."
  - "Lignum (Hrsg.): Lignatec 'Geneigte Dächer in Holzbauweise', Abschnitt 'Walmdach / Grat- und Kehlsparren'."
  - "Mönck, W.; Rug, W.: Holzbau – Bemessung und Konstruktion. 16. Aufl., Beuth Verlag 2015, Kap. 11 'Dachtragwerke', § Walmdach."
  - "Natterer, J.; Herzog, T.; Volz, M.: Holzbau-Atlas. 4. Aufl., Birkhäuser, Basel 2003, Kap. 'Dachtragwerke / Walmdach'."
  - "Krämer, V.: Grundwissen des Zimmerers. Bruderverlag, Köln 2006, Kap. Schiftungen / Walmdach-Austragung."
  - "Koepf, H.; Binding, G.: Bildwörterbuch der Architektur. 4. Aufl., Kröner, Stuttgart 2005, Eintrag 'Walm' und 'Walmdach'."
  - "Gerner, M.: Fachwerk – Instandsetzung, Sanierung, Neubau. DVA, 7. Aufl. 2007, Glossar 'Walmdach'."
  - "Lueger, O.: Lexikon der gesamten Technik, 2. Aufl. 1904, Eintrag 'Walmsparren': 'die zur Walmfläche gehörenden Sparren beziehungsweise Schifter'."
  - "Berufsschul-Lehrmaterial: polybau.ch 'Walmflächen am Walmdach' (Schweiz); zimmerer-treff.com 'Austragung von Schifter und Gratsparren' (Deutschland)."
quellenkonflikt: |
  **Drei Korpus-Lesarten des Wortes „Walm".** Die konsultierten
  Korpus-Quellen verwenden „Walm" nebeneinander in drei
  strukturell unterschiedlichen Bedeutungen, die nirgendwo
  geschlossen voneinander getrennt werden:

  - **Lesart A — Walm als einzelne Dachfläche** (am häufigsten im
    Bauratgeber-Korpus belegt: Wikipedia „Walmdach", DWDS,
    baunetzwissen.de, sanier.de, a-better-place.de). „Walm" ist
    in dieser Lesart die einzelne dreieckige oder trapezförmige
    Dachfläche am giebelseitigen Dachende, die einen Giebel
    ersetzt. Geometrisch Synonym oder Quasi-Synonym zu
    „Walmflaeche".
  - **Lesart B — Walm als konstruktive Einheit / Aggregat**
    (in `hg_bauteilgruppe.md` Sektion „Spezialisierungen" bereits
    aufgenommen; im Korpus implizit über die Bestandteil-
    Aufzählungen von BauNetz Wissen, Wikipedia, polybau.ch
    erschließbar, aber **nie geschlossen formuliert**). „Walm" ist
    die Bauteilgruppe aus zwei Gratsparren, optionalen Schiftern
    und optionalem Mittelsparren in der Walmfläche.
  - **Lesart C — Walm als Dachform / Verkürzung von Walmdach**
    (im Bauträger- und Verkaufs-Korpus gelegentlich: „einen Walm
    machen", „abwalmen"). Im Holzbau-Fachsprachgebrauch unüblich
    und mehrdeutig.

  **App-Wahl: Lesart B.** Dieser Eintrag belegt das Wort „Walm"
  ausschließlich mit Lesart B (Aggregat). Lesart A wird unter
  `walmflaeche` als eigener Folgeeintrag geführt; Lesart C ist
  unter `walmdach` als Folgeeintrag (Dachform) abgedeckt. Beide
  sind in `abgelehnte_benennungen:` aufgenommen — nicht weil die
  Benennungen falsch wären, sondern weil sie im Glossar an einen
  anderen Begriff gebunden sind und die hier festgelegte Lesart B
  nicht treffen. Detail-Befund siehe
  `docs/recherche/2026-05-14_hg_walm.md` §§ 2 und 5.

  **Keine Norm-Definition des Aggregats.** Weder SIA 232/1, SIA
  265, DIN EN 1995-1-1, DIN 1052, DIN 1356 noch DIN 18338 enthalten
  eine geschlossene Aggregat-Definition. Die Norm-Lage ist parallel
  zu `hg_binder.md`, `hg_sparren.md`, `hg_gratsparren.md`,
  `hg_kehlsparren.md`: der Begriff wird vorausgesetzt und nur über
  seine Bestandteile und seine Erscheinung charakterisiert. Die
  hier getroffene Festlegung ist eine **konsolidierende Eigenwahl**
  des Glossars, konsistent mit allen konsultierten Quellen.

  **Eigene Festlegung in diesem Glossar (Lesart B):**

  - **Walm** ist eine **Bauteilgruppe** im Sinne von
    `hg_bauteilgruppe.md`: ein partitives Aggregat aus zwei
    Gratsparren sowie einer (möglicherweise leeren) Menge von
    Schiftern und einem optionalen Mittelsparren in der Walmfläche,
    das einen walmförmig abgeschrägten Dachabschluss eines
    Dachtragwerks an einer Giebelseite bildet und die zugehörige
    Walmfläche als geometrische Hüllkomponente trägt.
  - **Strukturtyp `aggregat`**, **Oberbegriff `bauteilgruppe`**
    (strukturparallel zu `hg_binder.md`): der Walm erfüllt die
    zwei Kern-Merkmale der Bauteilgruppe — exklusive Mitgliedschaft
    (ein Gratsparren des linken Walms ist nicht zugleich
    Bestandteil des rechten Walms eines Vollwalmdachs) und
    kaskadische Lebenszyklus-Bindung (das Entfernen des Walms aus
    dem Modell entfernt seine Bestandteile oder gibt sie
    ausdrücklich an die umgebende Dachfläche zurück).

  **Drei explizite Nicht-Aufnahmen.** Drei nahe liegende, im
  Auftrag erwogene Modellierungs-Entscheidungen werden hier
  **bewusst nicht** getroffen:

  1. **Keine eigene Bauteilrolle „Walmsparren".** Lueger 1904 nutzt
     „Walmsparren" als Sammelbegriff für „Sparren beziehungsweise
     Schifter der Walmfläche"; die heutige Korpus-Verwendung ist
     uneinheitlich (teils für Gratsparren, teils für den
     Mittelsparren in der Walmfläche, teils als Sammelbegriff). In
     `hg_gratsparren.md` und `hg_kehlsparren.md` ist „Walmsparren"
     bereits als `abgelehnte_benennungen:` geführt. Der Walm-
     Eintrag bestätigt diesen Befund: der Mittelsparren in der
     Walmfläche (im symmetrischen Vollwalm mit First genau ein
     Stück) fällt unter die bereits definierte Bauteilrolle
     `sparren` (Falllinien-Kollinearität in der Walmfläche als
     einzelner Trägerebene); die Schifter fallen unter
     `schifter` (Folgearbeit, Trigger-Liste
     `HG_KONVENTIONEN.md` §6). Eine zusätzliche Rolle
     „Walmsparren" ist nicht erforderlich.
  2. **Keine Walm-Fußpfetten als Aggregat-Mitglieder.** Die zwei
     Fußpfetten am Walmende stoßen an einer Walm-Ecke aufeinander,
     und der Gratsparrenfuß sitzt auf diesem Stoß. Aber die
     Fußpfetten verlaufen längs des Hauses und gehören zur
     Hauptdachfläche bzw. zur umlaufenden Trauf-Tragebene; sie
     sind nicht **exklusiv** dem Walm zugeordnet. Die exklusive
     Mitgliedschaft (Bauteilgruppe-Bedingung 1) wäre verletzt. Der
     Walm referenziert die Walm-Trauf-Eckpunkte daher nur als
     geometrische Auflagerorte seiner Gratsparrenfüße (analog zu
     `hg_gratsparren.md`), nicht als Bestandteile des Aggregats.
  3. **Kein eigener Eintrag „Walmlinie".** Die Walmlinie zwischen
     Hauptdachfläche und Walmfläche ist geometrisch eine
     Gratstrecke g_{ij} im Sinne von `hg_grat.md`
     (konvexe Schnittstrecke zweier Trägerebenen); sie hat keine
     eigenständige strukturelle Substanz, die über `grat` hinaus
     ginge. Sie wird im Walm-Eintrag in der Erläuterung benannt,
     erhält aber keinen eigenen Glossareintrag.

  **Synonymie Krüppelwalm = Schopfwalm = Halbwalm = Kurzwalm.**
  Im DACH-Korpus übereinstimmend belegt (Wikipedia „Walmdach";
  sanier.de „Krüppelwalmdach"; dachdecker-spengler.com „Das
  Krüppelwalmdach"; baunetzwissen.de „Krüppelwalmdach"): diese
  vier Benennungen bezeichnen denselben Walm-Subtyp — einen Walm,
  bei dem **nur der obere Teil** der Giebel abgewalmt ist (der
  Walm reicht nicht von Traufe bis First, sondern endet
  oberhalb der Traufe). Regional dominiert „Krüppelwalm"
  (Schweiz/Süddeutschland) bzw. „Schopfwalm" (Norddeutschland);
  „Kurzwalm" ist gleichbedeutend, aber seltener. „Schopf" allein
  (ohne ‑walm) ist österreichischer Regionalbegriff (Wikipedia:
  „Kärntner Schopf(walm)"). Diese Synonymie wird **nicht** auf
  Ebene des hier eingeführten Aggregats geführt, sondern als
  Folge-Entscheidung an den `krueppelwalm`-Eintrag (Forward-
  Verweis A, siehe `abgrenzung_zu:`) verlagert; der vorliegende
  Walm-Eintrag behandelt den Walm als allgemeines Aggregat, der
  `krueppelwalm`-Eintrag wird die Vollwalm/Krüppelwalm/Fußwalm-
  Spezialisierungs-Familie als Folgearbeit modellieren.

  **Englische Anglizismen.** „hip" steht im englischen
  Holzbau-Korpus für den deutschen **Grat**, nicht den Walm;
  „hip end" benennt das Walm-Aggregat. Beide sind hier
  abgelehnte Benennungen, weil sie den deutschen Begriff nicht
  treffen und „hip" zudem in `hg_gratsparren.md` bereits als
  Gratsparren-Anglizismus geführt ist.

  **Schweizer/deutsche Praxis** ist konstruktiv im Wesentlichen
  identisch (Gratsparren + Schifter ± Mittelsparren in beiden
  Ländern); einziger Unterschied ist die Häufigkeit (in
  Deutschland im Wohnungs- und Stadthausbau verbreiteter, in der
  Schweiz vor allem im ländlichen Bauernhausbau).
---

## Prosa-Definition

Ein **Walm** ist eine Bauteilgruppe aus genau zwei Gratsparren,
einer möglicherweise leeren Menge von Schiftern und einem
optionalen Mittelsparren in einer giebelseitig vorgelagerten
Dachfläche (der Walmfläche), deren Bestandteile zusammen den
walmförmig abgeschrägten Dachabschluss eines Dachtragwerks an
einer Giebelseite bilden und deren Gratsparren auf den beiden
Gratstrecken zwischen der Walmfläche und den jeweils anliegenden
Hauptdachflächen liegen.

## Mathematische Definition

Sei

- W das Weltkoordinatensystem (siehe `weltkoordinatensystem`),
- 𝓑 die Menge aller Bauteile im Sinne von `bauteil`,
- 𝓢 ⊂ 𝓑 die Teilmenge der Bauteile, die die Bauteilrolle
  `sparren` tragen,
- 𝓖 ⊂ 𝓢 die Teilmenge mit Bauteilrolle `gratsparren`
  (siehe `hg_gratsparren.md`),
- 𝓓 die Menge der Dachflächen im Sinne von `dachflaeche`,
- 𝓟 die Menge der Ebenen im Sinne von `ebene`,
- 𝒰 der UUID-Raum nach `uuid`,
- 𝒢_huelle die Menge der zulässigen Hüllgeometrie-Repräsentationen
  einer Bauteilgruppe (siehe `bauteilgruppe`).

Dann ist ein **Walm** ein Tupel

```
W := (uuid, gratsparren, schifter, mittelsparren?,
      walmflaeche, hauptdachflaechen,
      lage, huelle, bezeichnung?)
```

mit

- **uuid** ∈ 𝒰: technischer Surrogatschlüssel des Walms (Pflicht,
  persistent, RFC 9562 v7); externe Referenzen auf den Walm gehen
  ausschließlich auf diese UUID (Aggregat-Wurzel im Sinne von
  `bauteilgruppe`).
- **gratsparren** ⊂ 𝓖, |gratsparren| = 2: die genau zwei
  Gratsparren an den beiden Walm-Ecken.
- **schifter** ⊂ 𝓢, |schifter| ≥ 0: die endliche, möglicherweise
  leere Menge der Schifter in der Walmfläche (Bauteilrolle
  `schifter`, Folgearbeit).
- **mittelsparren?** ∈ 𝓢 ∪ {⊥}: optionaler Sparren in der
  Walmfläche entlang ihrer Falllinie (im symmetrischen Vollwalm
  mit First genau ein Stück, in Pyramiden-Walm-Konfigurationen
  ohne First entfällt er, also ⊥). Wenn vorhanden, hat dieses
  Bauteil die gewöhnliche Bauteilrolle `sparren`.
- **walmflaeche** ∈ 𝓓: die geometrische Hüllkomponente — die
  dreieckige oder trapezförmige Dachfläche, die die Bauteile des
  Walms räumlich aufspannt (siehe `walmflaeche`, Folgearbeit).
- **hauptdachflaechen** ⊂ 𝓓, |hauptdachflaechen| = 2: die zwei
  Dachflächen, an die die Walmfläche entlang der beiden Gratlinien
  anschließt (typischerweise die zwei Hauptdachflächen des
  zugehörigen Dachs).
- **lage** ∈ SE(3): die Starrkörpertransformation, die das lokale
  Walm-Koordinatensystem nach W überführt (siehe
  `lokales_koordinatensystem`).
- **huelle** ∈ 𝒢_huelle: die geometrische Hülle des Walms im
  lokalen Koordinatensystem (Polyeder oder Bounding-Volume).
- **bezeichnung?**: optionaler humanlesbarer Name (z. B.
  „Walm Ost").

und den Konsistenzbedingungen

1. **Bauteilgruppen-Konformität**: das Tupel
   (uuid, bestandteile, lage, huelle, bezeichnung?) mit
   bestandteile := gratsparren ∪ schifter ∪ {mittelsparren |
   mittelsparren ≠ ⊥} erfüllt alle Konsistenzbedingungen 1–4 von
   `bauteilgruppe` (exklusive Mitgliedschaft, kaskadische
   Lebenszyklus-Bindung, Hüllen-Inklusion, azyklische
   Verschachtelung). Insbesondere gilt |bestandteile| ≥ 2 wegen
   |gratsparren| = 2.
2. **Gratsparren auf den Walm-Gratlinien**: für jeden der zwei
   Gratsparren g ∈ gratsparren existiert eine **Gratstrecke**
   g_{ij} im Sinne von `hg_grat.md` zwischen walmflaeche und
   einer der zwei Hauptdachflächen aus hauptdachflaechen, sodass
   die Bauteilachse von g auf g_{ij} liegt (im Sinne der
   Gratlinien-Kollinearitäts-Bedingung aus `hg_gratsparren.md`).
   Die beiden Gratstrecken sind verschieden und teilen sich
   höchstens den oberen Endpunkt (Firstendpunkt bzw. Walm-Spitze).
3. **Schifter setzen am Gratsparren an**: für jeden Schifter
   s ∈ schifter existiert genau ein g ∈ gratsparren, an dessen
   Seitenfläche s mit doppelter Schmiege ansetzt (im Sinne der
   Schifter-Definition, Folgearbeit `hg_schifter.md`). Die
   Bauteilachse von s liegt näherungsweise in walmflaeche.
4. **Mittelsparren in der Walmfläche entlang ihrer Falllinie**:
   ist mittelsparren ≠ ⊥, so liegt seine Bauteilachse näherungs-
   weise in walmflaeche und ist mit der Falllinie der Walmfläche
   kollinear (im Sinne der Bauteilrolle `sparren` mit
   walmflaeche als Trägerebene).
5. **Walmflaeche als Hüllen-Bezugsebene**: die geometrische
   Punktmenge ⋃_{b ∈ bestandteile} G_W(b) liegt in einer
   Umgebung von walmflaeche, deren Tiefe durch die Querschnitts-
   höhen der Bestandteile beschränkt ist (Inklusion innerhalb
   eines Toleranzbandes um walmflaeche).
6. **Exklusivität gegenüber benachbarten Walmen**: bei einem
   Vollwalmdach mit zwei Walmen (je einer pro Giebelseite) sind
   die zwei Walm-Aggregate vollständig disjunkt; insbesondere
   gehört jeder Gratsparren zu genau **einem** Walm. Diese
   Bedingung ist eine Spezialisierung der Bauteilgruppen-
   Bedingung 1 (exklusive Mitgliedschaft) und gilt durch sie.

Die **geometrische Punktmenge** des Walms in W ist

```
G_W(W) := lage(G_lokal(huelle)) ⊂ ℝ³
```

(transformierte Hülle); die alternative Repräsentation als
Vereinigung der Bestandteils-Punktmengen
⋃_{b ∈ bestandteile} G_W(b) ist eine abgeleitete Größe und im
Allgemeinen eine echte Teilmenge von G_W(W) (siehe
`bauteilgruppe` Bedingung 3).

## Wohldefiniertheit

- **Existenz**: Für jeden walmförmig abgeschlossenen Dachabschluss
  mit zwei Gratsparren und einer Walmfläche zwischen zwei
  Hauptdachflächen lässt sich ein Walm als Tupel der angegebenen
  Form erfassen. Mindestkonfiguration: |gratsparren| = 2, schifter
  = ∅, mittelsparren = ⊥ (entartete Walm-Spitze ohne First, ohne
  Schifter), walmflaeche und hauptdachflaechen aus dem umgebenden
  Dachtragwerk, lage = id_SE(3), huelle = achsenparalleler
  Hüllquader der zwei Gratsparren-Bounding-Boxen.
- **Eindeutigkeit der Identität**: Bedingung 1 (Bauteilgruppen-
  Konformität) erbt die Aggregat-Wurzel-Auflösung von
  `bauteilgruppe`; die Walm-UUID ist konstruktionsseitig zu
  vergeben und persistent.
- **Eindeutigkeit der Gratsparren-Zuordnung**: durch Bedingung 2
  ist jeder Gratsparren g ∈ gratsparren einer Gratstrecke g_{ij}
  zwischen walmflaeche und einer Hauptdachfläche zugeordnet. Die
  zwei Gratstrecken sind durch die Inzidenz mit walmflaeche und
  je einer Hauptdachfläche eindeutig bestimmt; die zwei
  Gratsparren werden ihnen unsortiert (als Menge) zugeordnet.
- **Trivial wohldefinierte Bestandteils-Menge**: gratsparren,
  schifter und hauptdachflaechen sind als Mengen unsortiert; alle
  Aussagen über den Walm sind invariant unter Permutation der
  Bestandteile innerhalb der jeweiligen Menge.
- **Unabhängigkeit von der Wahl des lokalen Koordinatensystems**:
  für jede zulässige Wahl des lokalen Walm-Koordinatensystems
  liefert die zugehörige Lage-Transformation dieselbe Punktmenge
  G_W(W); semantisch invariant.
- **Konsistenz mit `bauteilgruppe`**: jede Konsistenzbedingung von
  `bauteilgruppe` (exklusive Mitgliedschaft, kaskadische Löschung,
  Hüllen-Inklusion, Azyklizität) gilt für den Walm, weil er
  Subtyp von `bauteilgruppe` ist. Die Walm-spezifischen
  Bedingungen 2–6 treten **additiv** hinzu und schwächen keine
  Bauteilgruppen-Bedingung ab.
- **Konsistenz mit `gratsparren`**: jeder g ∈ gratsparren ist ein
  Gratsparren im Sinne von `hg_gratsparren.md`; insbesondere
  liegt seine Bauteilachse auf einer Gratstrecke zwischen zwei
  Trägerebenen, was hier genau auf eine Walm-Gratlinie zwischen
  walmflaeche und einer Hauptdachfläche fällt.
- **Nicht-Zirkularität**: die Definition verwendet
  `bauteilgruppe`, `bauteil`, `sparren`, `gratsparren`, `grat`,
  `dachflaeche`, `ebene`, `strecke`, `polyeder`, `uuid`,
  `lokales_koordinatensystem`, `weltkoordinatensystem`,
  `toleranzen` — alle bereits definiert. Sie verweist auf
  `walmflaeche` und `schifter` als geometrische bzw. rollenbezogene
  **Bezugsobjekte**, deren Glossareinträge als Folgearbeit
  geführt sind (Forward-Verweise in `abgrenzung_zu:`, nicht in
  `voraussetzungen:`). Die Definition referenziert nicht
  `walmdach` (Dachform-Sicht); der Walm ist Bestandteil eines
  Walmdachs, nicht definitorisch davon abhängig.
- **Eliminierbarkeit**: Jede Verwendung von „Walm" in der App
  lässt sich durch das obige Tupel mit den sechs Konsistenz-
  bedingungen ersetzen.

## Erläuterung (nicht normativ)

Der Walm ist die ontologische Antwort auf den walmförmigen
Dachabschluss: ein Bündel von Stab-Bauteilen, das geometrisch
zur Walmfläche gehört, statisch eigene Auflagerung und Lastpfade
hat und als Modell-Einheit „Walm Ost", „Walm West" identifizierbar
sein muss.

### Geometrische Erscheinung

Beim **Vollwalm** reicht die Walmfläche vom First bis zur
umlaufenden Traufe; sie ist dreieckig (Pyramiden-Walm-Spitze ohne
First) oder trapezförmig (mit First). Die zwei Gratlinien
(Walmlinien) verlaufen geneigt von der Trauf-Ecke zum
Firstendpunkt; die Walmfläche ist daher von zwei Gratstrecken und
einem Trauf-Abschnitt berandet. Beim **Krüppelwalm / Schopfwalm /
Halbwalm / Kurzwalm** (synonyme Benennungen, siehe Quellenkonflikt)
endet die Walmfläche oberhalb der Traufe und gibt unten einen
Restgiebel frei. Beim **Fußwalm** ist es umgekehrt: die Walmfläche
endet unten an der Traufe und oben unter einer noch verbleibenden
Giebel-Spitze. Beim **Niedersachsengiebel** doppel-abgewalmt: die
Walmfläche beginnt oben unter dem First und endet unten über der
Traufkante. Die ersten drei Sub-Formen werden im Folge-Eintrag
`krueppelwalm` zusammengefasst; Fuß- und Niedersachsenwalm sind
seltene Sonderformen.

### Bestandteile in der App-Modellierung

Konstitutiv sind die zwei Gratsparren (Anzahl genau 2 pro Walm).
Variabel sind die Schifter (Anzahl ≥ 0, je nach Walm-Breite und
Sparren-Abstand) und der Mittelsparren (0 oder 1; im
symmetrischen Vollwalm mit First genau 1). Die Walmfläche
(`walmflaeche`) ist **Hüllkomponente** des Aggregats — eine
geometrische Bezugsebene mit polygonaler Berandung —, nicht ein
weiteres Bauteil-Mitglied. Die Walm-Trauf-Eckpunkte und der
Firstendpunkt sind **geometrische Referenzpunkte** des Walms im
umgebenden Dachtragwerk; die Bauteile, die diese Punkte tragen
(Fußpfetten, Firstpfette), gehören längs zum Haus und sind nicht
Bestandteile des Walms.

### Drei-Ebenen-Verhältnis: Walm — Walmfläche — Walmdach

Drei eng verwandte Begriffe, die im Korpus oft vermischt werden,
werden im Glossar strikt getrennt:

```
Walmdach (Dachform-Sicht auf das Dach)
   └── enthält → Walm (Bauteilgruppe, eigene Identität, dieser Eintrag)
                  └── Bestandteile:
                        Gratsparren (2 Stück, Bauteilrolle)
                        Schifter   (≥ 0, Bauteilrolle, Folgearbeit)
                        Mittelsparren (0 oder 1, Bauteilrolle `sparren`)
                  └── Hüllgeometrie:
                        Walmflaeche (Dachflächen-Spezialisierung,
                                     Folgearbeit)
```

- **Walmflaeche** (Folgearbeit `walmflaeche`): die einzelne
  dreieckige oder trapezförmige Dachfläche am giebelseitigen
  Dachende. Spezialisierung von `dachflaeche`. Geometrische
  Hüllkomponente des Walm-Aggregats.
- **Walm** (dieser Eintrag): die Bauteilgruppe aus Gratsparren,
  Schiftern und Mittelsparren, die diese Walmfläche trägt.
- **Walmdach** (Folgearbeit `walmdach`): die Dachform; ein Dach
  ist ein Walmdach, wenn seine Bauteilgruppen-Menge mindestens
  ein Walm-Aggregat enthält. Strukturell eine **Sicht** auf das
  Dach-Aggregat über seine Bauteilrollen und Bauteilgruppen,
  parallel zu Sparrendach/Pfettendach/Binderdach.

### Walm-Anzahl pro Dach

Die Anzahl der Walm-Aggregate pro Dachtragwerk ist eine Folge
der Walm-Variante:

- **Vollwalmdach**: zwei Walme (je einer an Ost- und West-Giebel),
  jeder mit eigener UUID.
- **Halbwalmdach** im Sinne „nur an einer Giebelseite ein Walm,
  am anderen ein Giebel": genau ein Walm. Achtung: in einigen
  Korpus-Quellen wird derselbe Begriff für den Krüppelwalm
  verwendet — siehe `quellenkonflikt:`.
- **Pyramidendach / Zeltdach** (vier Walmflächen ohne First):
  vier Walmflächen, aber nur **ein** Walm-Aggregat als
  geometrisch zusammenhängende Bauteilgruppe um die zentrale
  Spitze; die Modellierung als ein oder vier Walme ist eine
  offene Designfrage und wird beim Folgeeintrag `walmdach`
  entschieden.

### Walmneigung als abgeleitete Größe

Die Walmneigung — die Dachneigung der Walmfläche — ist bei
gleichgeneigtem Vollwalm identisch mit der Neigung der
Hauptdachflächen; bei ungleichgeneigtem Walm weicht sie ab. Sie
ist eine eigenschaftliche Größe der **Walmflaeche** (über
`dachneigung` an `dachflaeche`), nicht des Walm-Aggregats; daher
wird sie hier nicht als eigener Wert geführt, sondern abgeleitet.

### Abgrenzung zu Binder in einem Satz

Ein **Binder** ist eine in einer expliziten Tragebene aufgespannte
Bauteilgruppe, die zwischen Auflagerpunkten eine Spannweite
überbrückt; ein **Walm** ist eine in einer Walmfläche aufgespannte
Bauteilgruppe, deren Gratsparren auf zwei Walm-Gratlinien liegen
und deren statische Funktion der Eckabschluss eines Dachtragwerks
ist. Beide tragen `oberbegriff: bauteilgruppe`, beide tragen
`begriffstyp: aggregat`; sie unterscheiden sich in der
geometrischen Bezugsstruktur (Tragebene vs. Walmfläche +
Gratlinien) und in der konstruktiven Funktion (Spannweiten-
Überbrückung vs. Eckabschluss).

## Beziehungen

- **Oberbegriff**: `bauteilgruppe`. Der Walm erfüllt alle
  Bauteilgruppen-Merkmale (exklusive Mitgliedschaft, kaskadische
  Lebenszyklus-Bindung, eigene Hülle, eigene Identität,
  konstruktive Funktionseinheit) und fügt drei eigene Merkmale
  hinzu: genau zwei Gratsparren als Pflichtbestandteile, eine
  zugeordnete Walmflaeche als Hüllgeometrie-Bezug und zwei
  zugeordnete Hauptdachflächen als geometrischen Anschluss.
- **Bestandteile (partitiv)**:
  - **Gratsparren** (`gratsparren`): genau zwei Stück, an den
    beiden Walm-Ecken.
  - **Schifter** (`schifter`, Folgearbeit): die in der Walmfläche
    liegenden, mit doppelter Schmiege an den Gratsparren
    ansetzenden Sparren (Anzahl variabel, ≥ 0).
  - **Mittelsparren** (`sparren`): optional 0 oder 1 Sparren in
    der Walmfläche entlang ihrer Falllinie.
- **Geometrische Bezugsobjekte (nicht Mitglieder)**:
  - **Walmflaeche** (`walmflaeche`, Folgearbeit): die
    geometrische Hüllkomponente, dreieckige oder trapezförmige
    Dachfläche.
  - **Hauptdachflächen** (`dachflaeche`): zwei benachbarte
    Dachflächen.
  - **Gratstrecken** (`grat`): zwei konvexe Schnittstrecken
    zwischen walmflaeche und je einer Hauptdachfläche.
  - **Walm-Trauf-Eckpunkte und Firstendpunkt**: geometrische
    Referenzpunkte des Walms im umgebenden Dachtragwerk; die
    sie tragenden Bauteile (Fußpfetten, Firstpfette) gehören
    längs zum Haus und sind **nicht** Mitglieder des Walms.
- **Spezialisierungen** (eigene Einträge folgen, trigger-basiert):
  - **Krüppelwalm / Schopfwalm / Halbwalm / Kurzwalm**
    (`krueppelwalm`): Walm, der nur den oberen Teil der Giebel
    abschließt; im Korpus übereinstimmend synonym.
  - **Vollwalm**: Walm vom First bis zur Traufe; ggf. eigener
    Eintrag `vollwalm`, sofern die App ihn vom Default abgrenzt.
  - **Fußwalm**: Walm, der nur den unteren Teil abschließt;
    selten.
  - **Niedersachsengiebel**: doppel-abgewalmt; regionaltypisch.
- **Verwendung**:
  - Bestandteil eines **Daches** (`dach`) — als
    Bauteilgruppe der Walmdach-Variante.
  - Trägt die zugeordnete **Walmflaeche** als Hüllgeometrie-
    Komponente.
- **Abgrenzung**:
  - **Bauteilgruppe** (`bauteilgruppe`): Oberbegriff — siehe oben.
  - **Binder** (`binder`): strukturparalleles Geschwister-Aggregat
    unter `bauteilgruppe`; geometrische Bezugsstruktur und
    konstruktive Funktion verschieden (siehe Erläuterung).
  - **Dach** (`dach`), **Dachform** (`dachform`): das Dach ist
    das umgebende Aggregat; die Dachform (Walmdach) ist eine
    **Sicht** auf das Dach-Aggregat über seine Bauteilgruppen.
    Der Walm ist Bestandteil eines Daches, nicht selbst eines.
  - **Dachflaeche** (`dachflaeche`): die Walmflaeche ist eine
    Spezialisierung von `dachflaeche`; sie ist Hüllkomponente
    des Walms, nicht der Walm selbst.
  - **Dachseite** (`dachseite`): klassifikatorische Sicht auf
    Dachflächen; orthogonal zum Walm-Aggregat.
  - **Dachausmittlung** (`dachausmittlung`, Folgearbeit): das
    geometrische Konstruktionsverfahren, mit dem die Walmflächen
    und Gratlinien aus Grundriss und Dachneigungen ermittelt
    werden; Tätigkeit, nicht Aggregat.
  - **Sparren** (`sparren`): der Mittelsparren in der Walmfläche
    ist ein Sparren in dieser Rolle; der Walm enthält Sparren als
    Bestandteile, ist aber selbst kein Sparren.
  - **Gratsparren** (`gratsparren`): zwei Stück sind konstitutiv
    für den Walm; der Walm ist aber selbst kein Gratsparren.
  - **Kehlsparren** (`kehlsparren`): bei einem Walmdach tritt
    typischerweise keine Kehle auf; Walme und Kehlen sind
    geometrisch komplementär (konvexe vs. konkave Schnittkante).
  - **Schifter** (`schifter`, Forward-Verweis A, Folgearbeit):
    konstitutiver Sub-Typ; siehe Bestandteile.
  - **Walmflaeche** (`walmflaeche`, Forward-Verweis A,
    Folgearbeit): geometrische Hüllkomponente, nicht das Walm-
    Aggregat selbst (Lesart A vs. Lesart B, siehe
    Quellenkonflikt).
  - **Walmdach** (`walmdach`, Forward-Verweis A, Folgearbeit):
    Dachform-Sicht, nicht das Walm-Aggregat (Lesart C vs.
    Lesart B).
  - **Krueppelwalm** (`krueppelwalm`, Forward-Verweis A,
    Folgearbeit): synonyme Walm-Variante (Krüppelwalm =
    Schopfwalm = Halbwalm = Kurzwalm), die nur den oberen Teil
    der Giebel abwalmt.
  - **Grat** (`grat`): geometrische Schnittstrecke; die zwei
    Walmlinien sind Gratstrecken zwischen walmflaeche und den
    Hauptdachflächen. Die Walmlinie hat keinen eigenen
    Glossareintrag (siehe Quellenkonflikt §3).
  - **Kehle** (`kehle`): komplementäres geometrisches Element
    (konkave Schnittstrecke); im Walm-Aggregat nicht enthalten.
  - **First** (`first`): der Firstendpunkt des Walms ist
    geometrischer Referenzpunkt; der First selbst gehört zur
    Hauptdachfläche, nicht zum Walm.
  - **Traufe** (`traufe`): die Walm-Trauf-Abschnitte sind
    Berandungs-Strecken der Walmflaeche; sie gehören zur
    Traufe des umgebenden Daches, nicht exklusiv zum Walm.
  - **Ortgang** (`ortgang`): an einem reinen Walm tritt kein
    Ortgang auf; beim Krüppelwalm gibt es im verbleibenden
    Restgiebel einen Ortgang-Abschnitt, der aber nicht zum
    Walm-Aggregat gehört.
  - **Fusspfette** (`fusspfette`), **Firstpfette** (`firstpfette`):
    geometrische Auflager- und Anschlussreferenzen des Walms;
    die Pfetten verlaufen längs des Hauses und sind nicht
    Bestandteile des Walms (siehe Quellenkonflikt §2 der
    Nicht-Aufnahmen).
  - **Verbindung** (`verbindung`): der Walm enthält Verbindungen
    zwischen seinen Bestandteilen (Gratsparren–Schifter,
    Gratsparren–Fußpfetten-Stoß) und ist selbst keine
    Verbindung.
  - **Auswechslung** (`auswechslung`): Schwester-Spezialisierung
    von `bauteilgruppe` mit anderer Funktion (Lasteinleitung um
    Öffnung); kein Walm.

## Implementierungshinweis

**Im aktuellen Glossarstand wird keine eigene Code-Klasse `Walm`
angelegt.** Die ontologische Vorbereitung lebt zunächst nur im
Glossar; eine Code-Klasse entsteht zusammen mit dem ersten
konkreten Tool, das einen Walm als Bauteilgruppe modelliert
(zugleich Trigger für `schifter`, `walmflaeche` und ggf.
`walmdach`). Der folgende Skizzen-Code ist ausschließlich
orientierender Implementierungshinweis für diesen Zeitpunkt und
folgt der Sealed-Hierarchie unter `Bauteilgruppe` aus
`hg_bauteilgruppe.md`, strukturparallel zur Binder-Skizze in
`hg_binder.md`.

```kotlin
// SKIZZE — nicht jetzt anlegen.
// Glossar: hg_walm.md

package domain.bauteil

import domain.bauteil.Bauteilgruppe
import domain.bauteil.Gratsparren
import domain.bauteil.Sparren
import domain.geometrie.Dachflaeche
import java.util.UUID

/**
 * Walm: Bauteilgruppe aus genau zwei Gratsparren, einer
 * möglicherweise leeren Menge von Schiftern und einem optionalen
 * Mittelsparren in der zugeordneten Walmflaeche; geometrische
 * Hüllkomponente ist die Walmflaeche, die Gratsparren liegen auf
 * den zwei Walm-Gratlinien zwischen Walmflaeche und den zwei
 * anliegenden Hauptdachflächen.
 *
 * Sealed unter Bauteilgruppe; konkrete Sub-Typen (Vollwalm,
 * Krüppelwalm, Fußwalm, Niedersachsengiebel) entstehen trigger-
 * basiert.
 */
sealed class Walm : Bauteilgruppe() {
    abstract val gratsparren: Set<Gratsparren>     // |gratsparren| == 2
    abstract val schifter: Set<Sparren>            // Folgearbeit Schifter-Typ
    abstract val mittelsparren: Sparren?           // 0 oder 1
    abstract val walmflaeche: Dachflaeche          // Folgearbeit Walmflaeche-Typ
    abstract val hauptdachflaechen: Set<Dachflaeche> // |hauptdachflaechen| == 2

    init {
        // 1. gratsparren.size == 2                → sonst Entartet.FalscheGratsparrenAnzahl
        // 2. hauptdachflaechen.size == 2          → sonst Entartet.FalscheHauptdachflaechenAnzahl
        // 3. Gratsparren auf Walm-Gratlinien      → sonst Entartet.GratsparrenAusserhalbWalmGrat
        // 4. Schifter ansetzend an Gratsparren    → sonst Entartet.SchifterOhneGratsparren
        // 5. Mittelsparren in Walmflaeche-Falllinie → sonst Entartet.MittelsparrenAusserhalbWalmflaeche
        // 6. Bauteilachsen in Walmflaeche-Toleranzband → sonst Entartet.AchseAusserhalbWalmflaeche
        // 7. Bauteilgruppen-Bedingungen geerbt    → über sealed-Hierarchie
    }
}
```

- **Einheit**: Längen in mm (Double); Winkel intern in Radiant;
  Lage als SE(3)-Element.
- **Identität**: `uuid` ist Pflicht und persistent (RFC 9562 v7);
  externe Referenzen auf einen Walm gehen ausschließlich auf
  diese UUID. Bestandteile (Gratsparren, Schifter, Mittelsparren)
  werden über ihre jeweiligen UUIDs referenziert (Foreign-Key-
  Regel, Memory `project_bauteil_identifikation`).
- **Invarianten** (in `init` bzw. Fabrikfunktionen prüfen, bei
  Verletzung `Resultat.Fehler` bzw. `Entartet`-Variante; niemals
  Exception werfen):
  1. `gratsparren.size == 2` ⇒ sonst
     `Entartet.FalscheGratsparrenAnzahl`.
  2. `hauptdachflaechen.size == 2` ⇒ sonst
     `Entartet.FalscheHauptdachflaechenAnzahl`.
  3. Für jeden g ∈ gratsparren liegt die Bauteilachse auf einer
     Gratstrecke zwischen walmflaeche und einer Hauptdachfläche
     aus hauptdachflaechen (im Sinne von `hg_gratsparren.md`
     Bedingung 3) ⇒ sonst
     `Entartet.GratsparrenAusserhalbWalmGrat`. Toleranz
     `Toleranzen.LAENGE_EPS` für Achs-Punkt-zu-Strecke-Abstand,
     `Toleranzen.KOLLINEAR_EPS` für die Richtung.
  4. Für jeden s ∈ schifter existiert genau ein g ∈ gratsparren,
     an dessen Seitenfläche s mit doppelter Schmiege ansetzt ⇒
     sonst `Entartet.SchifterOhneGratsparren`. Toleranz
     `Toleranzen.LAENGE_EPS`.
  5. Ist `mittelsparren ≠ null`, so liegt seine Bauteilachse in
     walmflaeche entlang der Falllinie ⇒ sonst
     `Entartet.MittelsparrenAusserhalbWalmflaeche`. Toleranz
     `Toleranzen.LAENGE_EPS` für Ebenen-Inzidenz,
     `Toleranzen.KOLLINEAR_EPS` für Falllinien-Kollinearität.
  6. Für jeden b ∈ bestandteile ist der Abstand der Bauteilachs-
     punkte zu walmflaeche ≤ Querschnittshöhe(b)/2 +
     `Toleranzen.LAENGE_EPS` ⇒ sonst
     `Entartet.AchseAusserhalbWalmflaeche`.
  7. **Exklusive Mitgliedschaft** (geerbt von `bauteilgruppe`):
     kein Bauteil b ∈ bestandteile ist zugleich Bestandteil eines
     anderen Walms oder einer anderen Bauteilgruppe. Prüfung im
     Modell-Container; bei Verletzung
     `Entartet.MehrfachMitgliedschaft`.
- **Edge Cases**:
  - **Pyramidenwalm-Spitze ohne First**: zulässig mit
    walmflaeche dreieckig und mittelsparren = null; bei
    Pyramidendach (vier Walmflächen ohne First) ist die
    Modellierung als ein Walm-Aggregat oder vier Walm-Aggregate
    offene Designfrage (siehe Erläuterung „Walm-Anzahl pro Dach").
  - **Vollwalm symmetrisch mit First**: walmflaeche trapezförmig,
    mittelsparren genau ein Sparren entlang der Falllinie.
  - **Krüppelwalm**: walmflaeche endet oberhalb der Traufe; der
    Walm-Aggregat-Eintrag bleibt strukturell identisch, lediglich
    die Walmflaeche-Berandung ist eingeschränkt. Der konkrete
    Sub-Typ folgt in `krueppelwalm`.
  - **Schmaler Walm ohne Schifter**: |schifter| = 0 zulässig;
    nur die zwei Gratsparren und ggf. der Mittelsparren tragen
    die Walmfläche.
  - **Vollwalmdach mit zwei Walmen**: zwei vollständig disjunkte
    Walm-Aggregate mit je eigener UUID; je ein Walm pro
    Giebelseite.
  - **Bauteil-Wechsel der Walm-Zugehörigkeit** (z. B. ein
    Gratsparren wird beim Umbau einem anderen Walm zugeordnet):
    erfordert koordinierte Modifikation beider Walme über den
    Modell-Container; nicht durch direkten Bauteil-Zugriff.
- **Abgeleitete Eigenschaften** (als Funktionen, keine Felder):
  - `geometrieInWelt(): GeometrieInW` = `lage(huelle)` als
    transformierte Hülle in W (geerbt von `Bauteilgruppe`).
  - `bestandteilsVereinigung(): GeometrieInW` =
    ⋃_{b ∈ bestandteile} G_W(b); im Allgemeinen echte Teilmenge
    der Hülle.
  - `walmlinien(): Pair<Strecke, Strecke>` = die zwei
    Gratstrecken zwischen walmflaeche und den Hauptdachflächen;
    abgeleitet über die Trägerebenen-Schnitte.
  - `walmneigung(): Double` (rad) = `walmflaeche.dachneigung`;
    abgeleitet aus der Walmfläche, nicht eigene Größe.
  - `istKrueppelwalm(): Boolean` = wahr genau dann, wenn die
    Walm-Trauf-Berandung **oberhalb** der umlaufenden Trauf-
    Höhe liegt (Folgearbeit, formale Definition in
    `krueppelwalm`).

## Quellen

**Primär (normativ):**

- SIA 232/1:2020, „Geneigte Dächer", Schweizerischer Ingenieur-
  und Architektenverein, Zürich, Abschnitt 1.
- SIA 265:2021, „Holzbau", Schweizerischer Ingenieur- und
  Architektenverein, Zürich, Abschnitt 5.
- DIN EN 1995-1-1:2010-12, „Eurocode 5: Bemessung und Konstruktion
  von Holzbauten – Teil 1-1: Allgemeines", Abschnitte 5, 6 und 10.
- DIN 1052:2008-12, „Entwurf, Berechnung und Bemessung von
  Holzbauwerken – Allgemeine Bemessungsregeln und
  Bemessungsregeln für den Hochbau", Abschnitte 8 und 12.
- DIN 1356-1:1995-02, „Bauzeichnungen – Teil 1: Arten, Inhalte
  und Grundregeln der Darstellung", Abschnitt 5.
- DIN 18338:2019-09, „VOB Teil C: Dachdeckungs- und
  Dachabdichtungsarbeiten", Abschnitt 0.

**Sekundär:**

- Lignum (Hrsg.): *Holzbautabellen HBT.* Lignum, Zürich,
  aktuelle Auflage.
- Lignum (Hrsg.): *Lignatec „Geneigte Dächer in Holzbauweise".*
- Mönck, W.; Rug, W.: *Holzbau – Bemessung und Konstruktion.*
  16. Aufl., Beuth, Berlin 2015, Kap. 11.
- Natterer, J.; Herzog, T.; Volz, M.: *Holzbau-Atlas.* 4. Aufl.,
  Birkhäuser, Basel 2003.
- Krämer, V.: *Grundwissen des Zimmerers.* Bruderverlag,
  Köln 2006.
- Koepf, H.; Binding, G.: *Bildwörterbuch der Architektur.*
  4. Aufl., Kröner, Stuttgart 2005.
- Gerner, M.: *Fachwerk – Instandsetzung, Sanierung, Neubau.*
  DVA, 7. Aufl. 2007.
- Lueger, O.: *Lexikon der gesamten Technik.* 2. Aufl. 1904,
  Eintrag „Walmsparren" (historisch, als Korpus-Beleg für die
  Begriffsunschärfe).

**Korpus (nicht autoritativ):**

- de.wikipedia.org, Lemma „Walmdach" (abgerufen 2026-05-14).
- de.wikipedia.org, Lemma „Schiftung" (abgerufen 2026-05-14).
- baunetzwissen.de, Eintrag „Krüppelwalmdach".
- sanier.de, Eintrag „Krüppelwalmdach".
- dachdecker-spengler.com, Eintrag „Das Krüppelwalmdach".
- a-better-place.de, Eintrag „Walm".
- polybau.ch, Schweizer Berufsschul-Lehrmittel zu Walmflächen
  (Snippet-Beleg).
- DWDS, Lemma „Walm" (Etymologisches Wörterbuch des Deutschen,
  Snippet-Beleg).
- Recherchebericht `docs/recherche/2026-05-14_hg_walm.md`.

## Folgearbeit (trigger-basiert)

1. **`walmflaeche`** — Spezialisierung von `dachflaeche` mit
   Berandungsbedingung (dreieckig oder trapezförmig, am
   giebelseitigen Dachende). Trigger: erster App-Renderer, der
   Walmflächen von gewöhnlichen Dachflächen unterscheidet, oder
   erste Walmdach-Modellierung (zugleich Trigger für diesen
   Walm-Eintrag selbst).
2. **`schifter`** — bereits in Trigger-Liste
   `HG_KONVENTIONEN.md` §6 (A) geführt; verkürzte Sparren mit
   doppelter Schmiege am Gratsparren. Trigger: erste vollständige
   Walmdach-Modellierung.
3. **`walmdach`** — Spezialisierung von `dach` (Dachform-Sicht);
   ein Dach ist ein Walmdach, wenn seine Bauteilgruppen mindestens
   einen Walm enthalten. Trigger: Dachform-Klassifikation in der
   App („Welche Dachform liegt vor?").
4. **`krueppelwalm`** — Walm-Spezialisierung mit synonymen
   Benennungen Krüppelwalm = Schopfwalm = Halbwalm = Kurzwalm
   (Korpus-Konsens). Trigger: erste Modellierung eines Walmdachs,
   das nicht von der Traufe bis zum First reicht.
5. **`dachausmittlung`** — bereits in Trigger-Liste
   `HG_KONVENTIONEN.md` (Folgearbeit `verschneidung`); das
   zeichnerische oder rechnerische Verfahren zur Ermittlung von
   Walmflächen und Gratlinien aus Grundriss und Dachneigungen.
   Trigger: erstes Tool zur zeichnerischen oder rechnerischen
   Walmdach-Konstruktion.

**R-Schritt-Drift in bestehenden Einträgen** (bei nächstem
R-Schritt nachzuziehen, nicht in diesem Schritt zu ändern):

- **`hg_bauteilgruppe.md` Z. 269–272** sagt im
  Spezialisierungs-Block „Walm (`walm`): walmförmiger Abschluss
  eines Daches als Aggregat aus Gratsparren, Schiftern und
  **Walmsparren**". Die „Walmsparren"-Referenz übernimmt einen
  Lueger-1904-Sammelbegriff, der in `hg_gratsparren.md` und
  `hg_kehlsparren.md` als `abgelehnte_benennungen:` geführt ist;
  die hier festgelegte Komposition ist „Gratsparren, Schifter und
  im symmetrischen Vollwalm einem Mittelsparren in der Walmfläche
  (Bauteilrolle `sparren`)". Die Aufzählungs-Formulierung in
  `hg_bauteilgruppe.md` soll bei nächstem R-Schritt entsprechend
  korrigiert werden.
- **`hg_bauteilgruppe.md` Erläuterungs-Block Walm-Beispiel**
  (Z. 208 ff.) trägt dieselbe Walmsparren-Formulierung und ist
  analog nachzuziehen.
