---
id: ferse
benennung: Ferse
synonyme: [Brust]
abgelehnte_benennungen: ["heel cut", "heel", "Ferserl", "plumb cut"]
oberbegriff: versatz
begriffstyp: merkmal
voraussetzungen: [versatz, bauteilachse, lotebene, toleranzen]
abgrenzung_zu: [versatz, stirnseite, kerve, senkel, bleischnitt, anschnitt, stirn]
status: entwurf
subglossar_pendant: notwendig  # Begründung: die Term-Überladung Ferse↔Ferserl↔heel cut ist eine lernrelevante Verwechslung (didaktischer Kern); siehe Implementierungshinweis.
quellen_primär:
  - "DIN EN 1995-1-1/NA:2013-08, Nationaler Anhang Deutschland zum Eurocode 5, NCI NA.12 'Zimmermannsmäßige Verbindungen': regelt den Versatz (Versatztiefe, Vorholzlänge, Anschnittwinkel) ohne eigene Typologie; die Lage-Bezeichnung 'Ferse' tritt nur gebunden im Fersenversatz auf. Paywall (DIN-Media); über Sekundärbeschreibungen und `hg_versatz.md` belegt, Volltext nicht eingesehen [via: hg_versatz.md / NCI NA.12-Sekundärbeschreibung]."
quellen_sekundär:
  - "Colling, F.: Holzbau – Grundlagen, Bemessungshilfen. Springer Vieweg, Wiesbaden, §8.5 'Versätze', Bild 8.15 'Fersen-/Rückversatz': die Druckfläche des Fersenversatzes steht rechtwinklig zur Strebe (δ_F = β − π/2); maßgebliche Benennungs-Autorität für die ⊥-Strebe-Geometrie als Fersenversatz (s. `hg_versatz.md` Konflikt 6). Print/Paywall, über `hg_versatz.md`-Quellenapparat geführt [via: hg_versatz.md]."
  - "Berner Fachhochschule (BFH) / Stiftung Denkmalpflege: 'Historische Holzverbindungen – Untersuchung des Trag- und Lastverformungsverhaltens', Leitfaden 2016, §2.1–2.5 (S. 17–20): benennt 'Stirn-, Brust- und Fersenversatz'; der ursprüngliche Versatz leitet Druck 'durch einen rechtwinkligen Schnitt an der Stirnseite' ein (rechtwinklig = ⊥ Strebe, nicht lotrecht). PDF frei, über lokalen PDF-Lesepfad eingesehen [direkt]."
  - "Thesaurus Traditioneller Holzbau (TTH), RWTH Aachen: führt 'Ferse' nicht als eigenständiges Lemma; nur 'Fersenversatz' (Begriff-ID 757) als leerer Stub unter Oberbegriff 'Holzverbindung'. Negativ-Befund zur Eigenständigkeit. `thesaurus-traditioneller-holzbau.net`, abgerufen 2026-06-03 [direkt]."
  - "DWDS / Pfeifer, Etymologisches Wörterbuch des Deutschen, 'Ferse': ahd. *fersna* (um 800), germ. *fersnō / *fersni-, Grundbedeutung 'Hacke, hinterer Teil des Fußes/Strumpfes/Schuhs'. Belegt die anatomische Metapher (hinterer Teil), nicht die Bauteil-Bedeutung; nur für Erläuterung/SG-Apparat, nicht normative Definition (QUELLEN.md §5). `dwds.de/wb/etymwb/Ferse`, abgerufen 2026-06-03 [direkt]."
quellenkonflikt: |
  **Konflikt A — `begriffstyp: merkmal` ↔ `oberbegriff: versatz` (§3-Spannung):**

  Die §3-Tabelle führt `merkmal` als „Wert/Annotation an einem
  Trägerbegriff" und nennt als Differenzierungs-Hilfe ausdrücklich nur
  die Spezialisierung eines `generisch`-Oberbegriffs (Beispiel
  `bauteilkoerper` unter `polyeder`). Der hier gewählte Oberbegriff
  `versatz` ist dagegen `partitiv`. Das ist eine Spannung zur
  unmittelbaren Lesart der Tabelle.

  **Eigene Festlegung (konsistent mit §3):** Die Asymmetrie zwischen
  `oberbegriff:` (fachliche Spezialisierungs-Linie) und `begriffstyp:`
  (strukturelle Rolle) ist nach §3 ausdrücklich „zulässig und
  beabsichtigt". Die Ferse ist strukturell ein **Wert ohne eigene
  Identität und ohne eigene Subtyp-Hierarchie** — die Lage-Achse, auf
  der `Versatz.art = FERSE` einen Wert annimmt. Sie ist damit `merkmal`,
  nicht `partitiv`: ein eigener partitiver Bestandteil „Ferse" mit
  eigener UUID existiert im Modell **nicht**; die Druckflächen-Geometrie
  lebt am `versatz` (`art = FERSE`, δ_F = β − π/2), nicht an einem
  separaten Träger. Der Oberbegriff `versatz` drückt nur aus, **wo** die
  Ferse fachlich beheimatet ist (sie tritt im Korpus ausschließlich
  gebunden im „Fersenversatz" auf — TTH kennt kein freistehendes Lemma
  „Ferse"), nicht, dass die Ferse strukturell ein Versatz-Bestandteil
  mit Lebenszyklus wäre. Diese Festlegung ist parallel zur §3-Erlaubnis
  „`merkmal` als Spezialisierung eines `generisch`-Oberbegriffs",
  konservativ auf einen `partitiv`-Oberbegriff übertragen: in beiden
  Fällen trägt die Spezialisierung weder `GlobalId` noch sealed-
  Hierarchie. Code-Pendant-frei (§3-Pendant-Tabelle: `merkmal` = nein),
  weil `VersatzArt.FERSE` bereits im `Versatz`-Code lebt.

  **Konflikt B — „Ferse = senkrechter Schnitt" (importierter EN-Fehlschluss):**

  Im englischen Birdsmouth-Kontext ist `heel cut` = `plumb cut` der
  **lotrechte** Schnitt (Wikipedia *Birdsmouth joint*). Wer „heel"
  mechanisch mit „Ferse" übersetzt und den Birdsmouth-Kontext mitnimmt,
  landet beim Fehlschluss „Ferse = senkrechter Schnitt". Dieser ist für
  den **Fersenversatz falsch**: dessen Druckfläche steht **rechtwinklig
  zur Strebe** (δ_F = β − π/2), also **geneigt**, nicht lotrecht (Colling
  §8.5; `hg_versatz.md` harte Invariante: δ = π/2 wäre der entartete
  Grenzfall, ausgeschlossen). Der lotrechte Schnitt am Fuß eines
  geneigten Holzes heißt im DACH-Korpus **Senkel** (`hg_senkel.md`),
  **nie** „Ferse". `heel cut`/`plumb cut` sind deshalb als
  `abgelehnte_benennungen:` geführt; sie sind das engl. Pendant zu
  **Senkel** (in der Kerve), nicht zur Ferse (im Versatz).

  **Konflikt C — „Brust(versatz)" als Synonym vs. eigener Typ:**

  „Brust"/„Brustversatz" ist im HG bereits zugunsten Colling als
  **Synonym** der ⊥-Strebe-Fersenversatz-Geometrie arbitriert
  (`hg_versatz.md` Konflikt 6). Die BFH-Lesart (S. 17), die „Brust-"
  **neben** „Fersenversatz" als dritten einfachen Versatz führt, und die
  baubeaver-Lesart (Web) sind nachrangig (QUELLEN.md §2: Lehrbuch >
  Berufsbildung > Web). Diese Linie wird hier **nicht neu aufgerollt**,
  sondern referenziert; „Brust" steht als Synonym der Ferse.

  **Konflikt D — „Ferserl" (österr./Wiener) = ganze Kerve, lexikografisch
  nicht belegt:**

  „Ferserl" ist im österr./Wiener Holzbau-Fach-Korpus (Eurotec,
  deutscher-bauzeiger, zimmerer-treff) Synonym für die **ganze Kerve**,
  nicht für eine Versatz-Lage. Es ist **kein** Synonym der Ferse und in
  `hg_kerve.md` `synonyme:` bereits geführt. Lexikografisch ist
  „Ferserl=Kerve" **nicht** erfasst — das DWDS kennt „Ferserl" nur als
  österr. Fußball-Ausdruck (Hackentrick), nicht als Holzbau-Begriff.
  „Ferserl" ist deshalb hier `abgelehnte_benennungen:` (falscher Freund,
  führt im CH-Holzbau nicht weiter), nicht `synonyme:`.
---

## Prosa-Definition

Die **Ferse** ist die zur Druckstab-Innenseite weisende hintere Lage am
Fuß eines geneigten Druckstabs, an der der **Fersenversatz** (`versatz`
mit `art = FERSE`) seine zur Strebe rechtwinklige Druckfläche und seinen
tiefsten Einschnitt führt.

## Mathematische Definition

Die Ferse ist eine **Lage-Position**, kein eigener geometrischer
Körper; ihre Geometrie ist die des Fersen-Ausschnitts in `hg_versatz.md`
(`art = FERSE`) und wird hier **nicht dupliziert**, sondern als Position
am Strebenfuß bestimmt.

Sei

- B der **geneigte Druckstab** (Strebe, Kopfband oder Sparren) mit
  Bauteilachse, deren Richtung in der Lotebene Π_⊥(B) den
  Strebenanschlusswinkel β ∈ (π/2, π) gegen die Trägerbauteil-Achse
  einschließt (siehe `bauteilachse`, `versatz`),
- T das liegende **Trägerbauteil** (Schwelle, Rähm, Bundbalken,
  Fußpfette) mit Oberseite auf der Lokal-Höhe z = h_B,
- v := V mit p_Versatz = (x_0, FERSE, β, ⊥, ⊥, t_F, ⊥, l_v) ein
  **Fersenversatz** nach `versatz` (Tupel (2) dort), mit Versatztiefe
  t_F > 0 und dem **Aufsetzpunkt** Q := (x_0, 0, h_B) ∈ ℝ³ — dem
  Schnittpunkt der Druckstab-Achse mit der Trägerbauteil-Oberseite,
- A_F := Q der **Fersen-Aufsetzpunkt** des einfachen Fersenversatzes und
  Δ_Versatz(FERSE) ⊂ Π_⊥(B) der Fersen-Anschnittquerschnitt nach
  `versatz` (V-Dreieck conv{A_F, C_F, B_F}, Druckfläche rechtwinklig zur
  Strebe δ_F = β − π/2, Sohle parallel zur Strebe σ = π − β).

Dann ist die **Ferse** von v die ausgezeichnete Lage

```
Ferse(v)  :=  ( A_F, ê_innen )                                       (1)
```

mit

- dem **Aufsetz-/Bezugspunkt** A_F = Q am Strebenfuß und
- der **Innenrichtung** ê_innen — der in Π_⊥(B) liegende Einheitsvektor
  in der Trägerbauteil-Oberseite (z = h_B), der vom Strebenfuß **firstwärts
  zur Druckstab-Innenseite** zeigt (entgegen der talseitigen Stirn). Damit
  liegt der **tiefste Punkt** der Fersen-Druckfläche auf der von A_F in
  Richtung ê_innen abgetragenen Seite (Versatztiefe t_F, gemessen lotrecht
  zur Strebe in den Träger hinein).

Die Ferse ist mithin die **Position** ⟨Aufsetzpunkt, Innenrichtung⟩,
gegen die der Fersen-Ausschnitt aus `versatz` orientiert ist; die
Druckflächen-, Sohlen- und Werkzeugkörper-Geometrie selbst trägt
`hg_versatz.md`, nicht dieser Eintrag.

## Wohldefiniertheit

- **Existenz/Eindeutigkeit von A_F.** A_F = Q ist der Schnittpunkt der
  Druckstab-Achse mit der Trägerbauteil-Oberseite z = h_B; für jeden
  geneigten Druckstab (β ∈ (π/2, π), nicht parallel zur Oberseite) ist
  dieser Schnittpunkt eindeutig (siehe `versatz`, Parameter x_0). Beim
  doppelten Versatz (`art = DOPPELT`) verschiebt sich der Fersen-
  Aufsetzpunkt auf den Gipfel der Stirn-Sohle (`hg_versatz.md`); für den
  reinen Fersenversatz (`art = FERSE`), den dieser Eintrag bezeichnet,
  gilt A_F = Q ohne Verschiebung.

- **Eindeutigkeit von ê_innen.** In der Lotebene Π_⊥(B) und in der
  Trägerbauteil-Oberseite (z = h_B) gibt es genau zwei zur
  Trägerbauteil-Achse parallele Einheitsrichtungen; ê_innen ist die
  firstwärtige (zur Druckstab-Innenseite, entgegen der Stirn). Die
  Auszeichnung ist durch die Lage des Druckstabs eindeutig: die Stirn
  liegt talseitig (über das Trägerbauteil ragend), die Ferse firstseitig.
  Da β ≠ π/2 (geneigter Druckstab), sind Stirn- und Innenrichtung
  verschieden, also ê_innen eindeutig bestimmt.

- **Unabhängigkeit von der Versatzart.** Die Ferse als **Lage** (1) ist
  bereits durch den geneigten Druckstab und das Trägerbauteil bestimmt
  und existiert auch dort, wo keine Schnittfläche an ihr sitzt (am
  Stirnversatz ist die Ferse nur die hintere Auslauf-Ecke, ohne eigene
  Druckfläche). Die **Druckfläche an der Ferse** entsteht erst bei
  `art ∈ {FERSE, DOPPELT}` und ist Gegenstand von `hg_versatz.md`. Dieser
  Eintrag bezeichnet die Lage; die Geometrie ist konservativ dorthin
  delegiert und wird nicht hier festgelegt — damit ist (1) frei von der
  Versatz-Geometrie eliminierbar.

- **Grenzfälle.** Für β → π/2 (Druckstab nähert sich der Lotrechten zum
  Träger) fallen Stirn- und Innenrichtung gegen die Lotebene zusammen;
  die Lage-Auszeichnung wird singulär — das ist der von `versatz`
  ausgeschlossene entartete Fall (kein Versatz mehr). Für β → π
  (Druckstab fast parallel zum Träger) ist die Ferse weit firstwärts,
  geometrisch wohldefiniert, aber konstruktiv ungebräuchlich.

## Erläuterung (nicht normativ)

### Die Ferse als hintere Lage am Strebenfuß

Der Fuß eines geneigten Druckstabs hat — in der anatomischen
Körper-Metapher (vom menschlichen Fuß übertragen) — zwei ausgezeichnete
Lagen: **vorn/talseitig die Stirn** (die über das Trägerbauteil ragende
Spitze, an der die Stirnfläche sitzt) und **hinten/innen die Ferse** (die
zurückliegende, firstwärtige Ecke). Belegt ist im DACH-Holzbau-Korpus
allein dieses Paar **Stirn ↔ Ferse** als Lage-Achse am Versatz; das
darüber hinaus oft vermutete reiche anatomische Wortfeld (Zehe, Backe,
Wange, Spiegel, Rücken als Ferse-Gegenstücke) ist **nicht** quellenbelegt
und wird hier bewusst nicht eingeführt. Die Etymologie (ahd. *fersna*
„Hacke, hinterer Teil des Fußes/Strumpfes/Schuhs", DWDS/Pfeifer) motiviert
die Metapher, trägt aber keine normative Definitionsaussage.

### Disambiguierung — „Ferse" ist über Verbindungstypen hinweg überladen

Der eigentliche Gebrauchswert dieses Eintrags liegt im sauberen Trennen
der mehreren Bedeutungen, die im Praxis-Korpus an „Ferse"/„heel" hängen.
Sie sitzen in **disjunkten Bearbeitungstypen**:

| Begriff | Gehört zu | Geometrie | Verweis |
|---|---|---|---|
| **Ferse / Fersenversatz** | `versatz` (`art = FERSE`) | Druckfläche **rechtwinklig zur Strebe**, δ_F = β − π/2 — **geneigt**, **kein** Lotschnitt | `hg_versatz.md` |
| **„Brust(versatz)"** | `versatz` (`art = FERSE`) | **Synonym** der Ferse (HG-arbitriert, Konflikt 6) | `hg_versatz.md` |
| **engl. „heel cut" / „plumb cut"** | `kerve` (Birdsmouth) | der **lotrechte** Schnitt = **Senkel** (welt-vertikal) — heißt im DACH **nie** „Ferse" | `hg_senkel.md`, `hg_kerve.md` |
| **„Ferserl"** (österr./Wiener) | `kerve` | die **ganze Kerve** (Fach-Synonym, lexikografisch nicht belegt) | `hg_kerve.md` |

Die drei Kern-Verwechslungen, die dieser Eintrag ausräumt:

1. **„Ferse = senkrechter Schnitt" ist falsch** (Konflikt B). Das ist ein
   importierter englischer Fehlschluss: `heel cut`/`plumb cut` ist im
   Birdsmouth-Kontext der lotrechte Schnitt, der im Deutschen **Senkel**
   heißt und zur **Kerve** gehört — nicht zum Versatz. Die Fersenversatz-
   Druckfläche ist **geneigt** (⊥ Strebe), nie lotrecht.

2. **„Ferserl" ist nicht die Ferse** (Konflikt D). Das österr./Wiener
   „Ferserl" meint die **ganze Kerve**, nicht eine Versatz-Lage; es ist
   in `hg_kerve.md` als Kerve-Synonym geführt, hier als falscher Freund
   abgelehnt. Im CH-Holzbau nicht einschlägig.

3. **„Brust" ist die Ferse** (Konflikt C), kein eigener dritter Versatz —
   bereits in `hg_versatz.md` arbitriert.

### Vorholz und Ausstiegskante

Beim Fersenversatz liegt die tragende Druckfläche zur Ferse hin nach
hinten/innen verschoben; die **Vorholzlänge** l_v (Scher-Trag-Länge im
Träger) wird am Fersenversatz an der **Fersen-Ausstiegskante** gemessen
(`hg_versatz.md`, Parameter l_v). Die Ferse benennt dabei die hintere
Ecke; ob dort eine Schnittfläche sitzt (Fersenversatz, doppelter Versatz)
oder nur eine Auslauf-Ecke (Stirnversatz), hängt vom Verbindungstyp ab.

## Beziehungen

- **Oberbegriff** (`versatz`): Die Ferse lebt im Fach-Korpus nur gebunden
  im „Fersenversatz"; `versatz` ist ihre fachliche Heimat. Die Asymmetrie
  `merkmal` (struktureller Wert) ↔ `oberbegriff: versatz` (partitiv) ist
  in Konflikt A begründet.
- **Gegenstück** (`stirn`, Forward-Verweis): Die **Stirn** ist die vordere/
  talseitige Lage am selben Strebenfuß; Stirn ↔ Ferse ist das einzige
  korpus-belegte Lage-Paar am Versatz. „Stirn" hat keinen eigenen HG-
  Eintrag (im Versatz als Lage geführt, `hg_versatz.md`); der Forward-
  Verweis bezeichnet die Lage, nicht die Bauteilfläche.
- **Abgrenzung**:
  - **Versatz** (`versatz`): trägt die **Geometrie** des Fersen-
    Ausschnitts (δ_F = β − π/2, Sohle ∥ Strebe, V-Werkzeugkörper); die
    Ferse ist die **Lage**, an der diese Geometrie sitzt — keine eigene
    geometrische Substanz.
  - **Stirnseite** (`stirnseite`): eine **Bauteilfläche** (Hirnholz,
    `generisch`) mit Trägerebene, Berandung und Außennormale. Die Ferse
    ist **keine** solche Fläche, sondern eine Lage innerhalb einer
    Bearbeitung. Die Stirnseite-Analogie zur Ferse ist widerlegt (kein
    Beleg für eine eigenständige „Fersenfläche").
  - **Kerve** (`kerve`): andere Bearbeitung (Auflager-Einschnitt am
    Sparren auf der Pfette). Das österr. „Ferserl" meint die ganze Kerve,
    nicht die Ferse; der lotrechte Kerv-Schnitt heißt Senkel.
  - **Senkel** (`senkel`): der **lotrechte** Schnitt am Fuß eines
    geneigten Holzes (welt-vertikal). Das engl. `heel cut`/`plumb cut`
    ist Senkel, **nicht** Ferse — die Quelle der „Ferse=senkrecht"-
    Verwechslung (Konflikt B).
  - **Bleischnitt** (`bleischnitt`): der **waagerechte** Schnitt
    (welt-horizontal); engl. `seat cut`. Weder Ferse noch Senkel.
  - **Anschnitt** (`anschnitt`): allgemeine schräge Endausbildung;
    die Fersen-Druckfläche ist ein spezieller Anschnitt am Versatz, die
    Ferse selbst aber eine Lage, kein Anschnitt.

## Implementierungshinweis

**Kein eigenes Code-Pendant erforderlich** (`begriffstyp: merkmal` ist
nach §3 pendant-frei). Die Ferse ist im Code bereits als Wert der
Konfigurations-Achse `VersatzArt.FERSE` am `Versatz` vorhanden
(`hg_versatz.md`); ein eigener `@GlossarBegriff(GlossarTerm.FERSE)`-Typ
wird **nicht** angelegt. Der Fersen-Aufsetzpunkt A_F und die Innenrichtung
ê_innen sind aus dem `Versatz`-Parametertupel (x_0, β, art) ableitbar
(abgeleitete Eigenschaft am `Versatz`, kein eigener Konstruktor).

- **Datentyp**: keiner eigenständig; Lage am `Versatz` (Enum-Wert
  `art = FERSE` plus die ableitbaren A_F, ê_innen).
- **Einheit**: A_F in mm (Bauteil-Lokalkoordinaten), ê_innen
  dimensionsloser Einheitsvektor in Π_⊥(B).
- **Toleranzen**: für die Geometrie an der Ferse gelten die Versatz-
  Toleranzen (`hg_versatz.md`); die Richtungs-Auszeichnung ê_innen ist
  über Π_⊥(B) und die Trägerbauteil-Achse bestimmt (Parallelitäts-
  Tests via `KOLLINEAR_EPS`, falls eine Klassifikations-Hilfsfunktion
  eingeführt wird).
- **Edge Cases**:
  - **Stirnversatz** (`art = STIRN`): die Ferse existiert als Lage
    (hintere Auslauf-Ecke), trägt aber **keine** Druckfläche; eine
    naive Abfrage einer „Fersen-Druckfläche" am Stirnversatz ist
    undefiniert und muss `art` prüfen.
  - **Doppelter Versatz** (`art = DOPPELT`): A_F sitzt nicht bei Q,
    sondern am Gipfel der Stirn-Sohle (`hg_versatz.md`); die Lage-
    Auszeichnung verschiebt sich entsprechend.
  - **EN-Importfalle**: ein BTLx/COMPAS-Import, der `heel cut` (engl.,
    Birdsmouth) mechanisch nach „Ferse" übersetzt, ordnet die Geometrie
    falsch zu (lotrechter Kerv-Senkel statt geneigte Versatz-Druckfläche)
    — beim EN↔DE-Mapping `heel cut` → `senkel`/`kerve`, **nicht** → Ferse.

**Begründung `subglossar_pendant: notwendig`.** Die Term-Überladung
(Ferse-Druckfläche ‖ Ferserl=Kerve ‖ heel cut=Senkel) ist eine
**lernrelevante Verwechslung**: gerade der importierte EN-Fehlschluss
„Ferse=senkrecht" und das österr. „Ferserl" sind typische Stolpersteine,
deren Auflösung didaktischen Wert hat. Damit ist die didaktische
Subglossar-Hülle (Schnuppi–Meister) gerechtfertigt — keine Abweichung vom
`notwendig`-Normalfall.

## Quellen

**Primär (normativ, gebunden):**

- DIN EN 1995-1-1/NA:2013-08, NCI NA.12 „Zimmermannsmäßige Verbindungen"
  (Versatz ohne Typologie; „Ferse" nur gebunden im Fersenversatz).
  Paywall (DIN-Media); über `hg_versatz.md` und Sekundärbeschreibungen
  geführt [via: hg_versatz.md].

**Sekundär:**

- Colling, F.: *Holzbau – Grundlagen, Bemessungshilfen.* Springer Vieweg,
  §8.5, Bild 8.15 „Fersen-/Rückversatz" (Druckfläche ⊥ Strebe,
  δ_F = β − π/2). Benennungs-Autorität der ⊥-Strebe-Geometrie als
  Fersenversatz. Print/Paywall [via: hg_versatz.md].
- Berner Fachhochschule / Stiftung Denkmalpflege: *Historische
  Holzverbindungen – Untersuchung des Trag- und Lastverformungsverhaltens.*
  Leitfaden 2016, §2.1–2.5 (S. 17–20): „Stirn-, Brust- und Fersenversatz";
  „rechtwinkliger Schnitt an der Stirnseite" (= ⊥ Strebe). PDF frei,
  lokaler PDF-Lesepfad [direkt].
- Thesaurus Traditioneller Holzbau (TTH), RWTH Aachen: „Ferse" kein
  eigenes Lemma; nur „Fersenversatz" (ID 757, leerer Stub).
  `thesaurus-traditioneller-holzbau.net`, abgerufen 2026-06-03 [direkt].

**Etymologie (nur Erläuterung/SG-Apparat, QUELLEN.md §5):**

- DWDS / Pfeifer, *Etymologisches Wörterbuch des Deutschen*, „Ferse"
  (ahd. *fersna*, germ. *fersnō*; „Hacke, hinterer Teil des Fußes/
  Strumpfes/Schuhs"). `dwds.de/wb/etymwb/Ferse`, abgerufen 2026-06-03
  [direkt].
- DWDS, „Ferserl": nur österr. Fußball-Ausdruck (Hackentrick); die
  Holzbau-Bedeutung „Ferserl = Kerve" ist lexikografisch **nicht**
  erfasst (Fach-Korpus-Sprache). `dwds.de/wb/Ferserl`, abgerufen
  2026-06-03 [direkt].

**Korpus (nicht autoritativ, Synonym-/Cross-Kontext-Sammlung):**

- Eurotec Anfängerlehrbuch Teil 3.3, deutscher-bauzeiger.de,
  zimmerer-treff.com: „Ferserl" als Kerve-Synonym (österr./Wiener;
  über `hg_kerve.md` geführt).
- Wikipedia *Birdsmouth joint* (heel cut = plumb cut = lotrecht =
  Senkel; nicht Ferse). `en.wikipedia.org/wiki/Birdsmouth_joint`,
  abgerufen 2026-06-03.
