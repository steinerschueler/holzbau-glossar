---
id: schwelle
benennung: Schwelle
synonyme: [Grundschwelle, Schwellholz, Schwellenholz, Schwellbalken, Grundbalken]
abgelehnte_benennungen: [Mauerschwelle, Sohlbank, Fußschwelle, Saumschwelle, Stockschwelle, Setzschwelle, Vorschwelle, Balkenschwelle, Richtschwelle, Schwellpfette, "sill plate", "sole plate", "mudsill", "bottom plate", "ground plate", "ground sill", groundsel]
oberbegriff: bauteil
begriffstyp: bauteilrolle
voraussetzungen: [bauteil, bauteilachse, querschnitt, bezugsebene, weltkoordinatensystem, einheitsvektor, punkt, toleranzen]
abgrenzung_zu: [raehm, fusspfette, pfette, pfosten, staender, riegel, strebe, kopfband, fussband, knagge, fundament, bauteil, stockschwelle, tuerschwelle, bahnschwelle, sohlbank_fenster]
status: entwurf
subglossar_pendant: notwendig
quellen_primär:
  - "DIN 68800-2:2022-02 'Holzschutz – Teil 2: Vorbeugende bauliche Maßnahmen im Hochbau', Abschnitt 5 (Anforderungen an den Wandfuß), insb. Mindestabstand Unterkante Schwelle ↔ OK Gelände (Regelmaß 30 cm; Abminderungen auf 15 cm bzw. 5 cm bei Kiesbett bzw. Abdichtung nach DIN 18533)."
  - "DIN EN 1995-1-1:2010-12 (Eurocode 5), Abschnitt 5 und 9 (Tragwerksberechnung, Holztafelbau): Schwelle als unterer Anschluss einer Wandtafel."
  - "DIN 1052:2008-12, Abschnitt 8 und 12, Schwelle / Grundschwelle als Wandbauteil."
  - "DIN 18533-1:2017-07 'Abdichtung von erdberührten Bauteilen', referenziert in DIN 68800-2 §5 für die 5-cm-Abminderung."
  - "EN 335:2013 / DIN 68800-1:2011-10, Gebrauchsklassen-Einordnung (GK 2 / GK 3.1 / GK 3.2) als Instanz-Eigenschaft am konkreten Schwellen-Einbau."
quellen_sekundär:
  - "Lignum (Hrsg.): Lignatec 35/2023 'Holzschutz im Bauwesen', Empa/Lignum, Zürich 2023, Abschnitt Wandfuß / Spritzwasserzone."
  - "Mönck, W.; Rug, W.: Holzbau – Bemessung und Konstruktion. 16. Aufl., Beuth, Berlin 2015, Kap. 'Wandkonstruktionen' und 'Holzrahmenbau'."
  - "Gerner, M.: Fachwerk – Instandsetzung, Sanierung, Neubau. DVA, 7. Aufl. 2007, Glossar 'Schwelle', 'Grundschwelle', 'Stockschwelle'."
  - "Natterer, J.; Herzog, T.; Volz, M.: Holzbau-Atlas. 4. Aufl., Birkhäuser, Basel 2003, Kap. 'Wandsysteme'."
  - "Informationsdienst Holz: Reihe 5 Teil 2 Folge 2 'Holzschutz – Bauliche Maßnahmen', Wandfuß-Details."
  - "Holzfaser-Verband: Merkblatt 'Anschlüsse und Fugen – Details für Holzmassivbau'."
quellenkonflikt: |
  Drei Punkte sind in der Recherche
  (`docs/recherche/2026-05-14_hg_schwelle.md`) nicht
  widerspruchsfrei und werden hier ausdrücklich aufgelöst.

  **(1) Familien-Begriff vs. Grundschwellen-Lesart.** Im
  DACH-Fachwerk-Vokabular ist „Schwelle" Familien-Begriff über
  Geschoss-Subtypen (Grundschwelle, Stockschwelle / Saumschwelle /
  Fußschwelle / Setzschwelle / Vorschwelle / Balkenschwelle). Im
  modernen Holzrahmen- und Tafelbau wird „Schwelle" hingegen
  primär für den **untersten** horizontalen Längsträger einer
  Wandtafel verwendet, der direkt auf Bodenplatte/Sockel oder auf
  der Decke des darunterliegenden Geschosses sitzt; diese Lesart
  fällt im Fachwerk-Vokabular mit „Grundschwelle" bzw. mit
  „Stockschwelle" (im Obergeschoss) zusammen.

  Eigene Festlegung: Dieser Eintrag definiert die **Grundschwellen-
  Lesart** als Default-Lesart von „Schwelle" — der unterste
  horizontale Längsträger einer Wand auf einem mineralischen
  Auflager (Fundament, Sockel, Bodenplatte). „Grundschwelle" ist
  enges Synonym. Die Geschoss-Subtypen Stockschwelle / Saumschwelle /
  Fußschwelle / Setzschwelle / Vorschwelle / Balkenschwelle, die
  die obergeschossige bzw. deckenbezogene Lage betreffen, sind
  in `abgelehnte_benennungen:` als **nicht** mit diesem Eintrag
  zusammenfallend geführt; ein eigener `hg_stockschwelle.md`
  folgt bei Mehrgeschoss-Bedarf (siehe Forward-Verweise).

  Die Spezialisierungs-Synonym-Regel (HG_KONVENTIONEN §5) wirkt
  bei späterer Anlage von `hg_grundschwelle.md` ausdrücklich
  **nicht**, weil „Grundschwelle" hier bereits Synonym der
  Wurzel-Lesart ist und kein Spezial-Eintrag mit getrennter
  Lesart entsteht.

  **(2) Englische Pendants — als Synonyme statt als abgelehnte
  Benennungen.** `hg_fusspfette.md` führt englische Pendants
  (`wall plate`, `eaves purlin`) in `abgelehnte_benennungen:`.
  Dieser Eintrag weicht davon ab und führt `sill plate`,
  `sole plate`, `mudsill`, `bottom plate` als Synonyme
  (Eric-Linie, Auftrag 2026-05-14). Begründung: Die englischen
  Begriffe sind im internationalen Holzrahmenbau-Diskurs (CLT-
  Engineering, IRC, CSA O86) als Pendants etabliert und werden
  in Schweizer Ingenieurbüros mit internationalen Auftraggebern
  aktiv verwendet. Die US-Praxis-Disambiguation (`sill plate` /
  `mudsill` auf Fundament; `sole plate` / `bottom plate` auf
  Decke/Unterboden) ist in der Erläuterung als „Andere
  Bedeutungen / Englisch"-Block dokumentiert.

  `ground plate`, `ground sill` und `groundsel` sind als
  historische englische Varianten in `abgelehnte_benennungen:`
  geführt; sie sind im modernen Diskurs nicht etabliert.

  **(3) DIN 68800-2-Maße aus Sekundärreferaten.** Die konkreten
  Maße 30 cm / 15 cm / 5 cm sowie die Sektions-Verortung in
  DIN 68800-2:2022-02 §5.2.1.3 stammen aus konsistenten
  Sekundär-Referaten (bba-online, Holzfaser-Verband,
  Informationsdienst Holz); der Norm-Volltext wurde nicht
  unmittelbar eingesehen. Die Maße sind in der Erläuterung als
  Sekundär-Referat gekennzeichnet, nicht als unmittelbare
  Norm-Wiedergabe.

  **(4) `Sohlbank` als abgelehnte Benennung.** „Sohlbank" ist
  im traditionellen Schweizer Strick-/Blockbau zwar Synonym zu
  „Grundschwelle", kollidiert aber mit der **Fenster-Sohlbank**
  (unteres Querholz am Fensterstock) als einschlägigem Homonym
  in der modernen Bauweise. Eigene Festlegung: `Sohlbank` wird
  in `abgelehnte_benennungen:` aufgenommen und nicht als
  Synonym geführt; im Werkplan- und App-Vokabular bleibt
  „Sohlbank" für das Fenster-Bauteil reserviert
  (Forward-Verweis `sohlbank_fenster` in `abgrenzung_zu:`,
  Klasse D — keine eigene HG-Anlage geplant).

  **(5) Türschwelle / Bodenschwelle / Bahnschwelle als Homonyme,
  nicht als abgelehnte Benennungen.** „Türschwelle" und
  „Bodenschwelle" bezeichnen heute ein **Tür-Bauteil** (unteres
  Querholz/-profil am Türrahmen), nicht eine Variante der
  Wand-Schwelle. „Bahnschwelle" ist Eisenbahn-Bauteil. Beide
  sind **homonyme Begriffe in anderer Bauteildomäne** und
  stehen ausdrücklich in `abgrenzung_zu:` (Forward-Verweise),
  nicht in `abgelehnte_benennungen:`. Behandlung im
  Erläuterungs-Block „Andere Bedeutungen".
---

## Prosa-Definition

Eine **Schwelle** ist eine Bauteilrolle in einer Wand, deren
Bauteilachse horizontal entlang der Wandflucht am untersten
Wand-Niveau verläuft, die unmittelbar auf dem mineralischen
Auflager (Fundament, Sockel, Bodenplatte) der Wand aufliegt und
die die vertikalen Lasten der auf ihr stehenden Pfosten oder
Ständer in das Auflager einleitet sowie als erste Holzschicht
über dem mineralischen Untergrund die konstruktive Trennung
zwischen feuchteführendem Auflager und trockenem Wandholz
herstellt.

## Mathematische Definition

Sei

- B ein Bauteil im Sinne von `bauteil` mit Bauteilachse
  a(B) = (p_a, p_e) ∈ ℝ³ × ℝ³ und Richtungs-Einheitsvektor
  d_hat_B := (p_e − p_a) / ‖p_e − p_a‖,
- e_hat_z := (0, 0, 1) die Welt-z-Achse nach `weltkoordinatensystem`,
- E_⊥ eine horizontale Bezugsebene im Sinne von `bezugsebene` mit
  Normalen-Einheitsvektor e_hat_z (die Oberkante des Auflagers, im
  Folgenden „Auflagerebene" genannt) und Höhe z_E := z-Koordinate
  jedes Punktes in E_⊥,
- z_B := (p_a.z + p_e.z) / 2 die mittlere Höhe der Bauteilachse,
- h_B die Querschnittshöhe von B nach `querschnitt`,
- ε_K := Toleranzen.KOLLINEAR_EPS, ε_L := Toleranzen.LAENGE_EPS,
- δ_z := h_B / 2 + ε_L die konstruktive Höhentoleranz für die
  Auflagernähe.

Dann heißt B eine **Schwelle** bezüglich E_⊥ genau dann, wenn die
folgenden Bedingungen alle erfüllt sind:

1. **Horizontalität der Bauteilachse**:
   ```
   |d_hat_B · e_hat_z| ≤ ε_K.
   ```
   Sinus-Test gegen e_z-Parallelität (Skalarprodukt-Form, drei
   von vier Welle-8-Einträgen einheitlich): die Bauteilachse liegt
   rechtwinklig zur Welt-z-Achse, also horizontal. Nach
   `HG_KONVENTIONEN.md` Sektion 4 ist `KOLLINEAR_EPS` die
   einschlägige Toleranz für Lot- und Lage-Prädikate.

2. **Auflagernähe**: Die Bauteilachse liegt innerhalb δ_z
   oberhalb der Auflagerebene,
   ```
   0 ≤ z_B − z_E ≤ δ_z + h_B / 2.
   ```
   In Worten: die Unterkante des Schwellen-Querschnitts liegt
   höchstens ε_L oberhalb (oder genau in) der Auflagerebene; die
   Schwelle sitzt unmittelbar auf E_⊥.

3. **Unterste Wand-Längslage**: Es existiert in derselben
   Wand-Längsachse a_W (Geradenfortsetzung von a(B) in der
   Wand-Ebene) kein weiteres horizontales Bauteil B′ ≠ B mit
   d_hat_{B′} kollinear zu d_hat_B und z_{B′} < z_B − ε_L. In Worten:
   die Schwelle ist das **unterste** horizontale Längsbauteil
   entlang der Wandlinie.

4. **Pfosten-Auflagerbedingung**: Mindestens ein Bauteil
   P im Tragwerks-Kontext (`pfosten` oder `ständer`) mit
   lotrechter Bauteilachse a(P), d_hat_P kollinear zu e_hat_z bis auf
   ε_K, hat seinen unteren Endpunkt p_a(P) innerhalb ε_L oberhalb
   der Schwellen-Bauteilachse, projektive Lage zwischen p_a und
   p_e. Schwellen ohne aufgesetzte Pfosten sind im Tragwerks-
   Sinne nicht definiert; die Bedingung wird im Tragwerks-Kontext
   geprüft, nicht im Einzel-Bauteil-Kontext.

Wesentliche abgeleitete Größen:

- **Schwellen-Oberkante (lokale Bezugskote)**:
  z_OK(B) := z_B + h_B / 2; übliche Werkplan-Bezugskote für
  Wandhöhen und Pfosten-Längen.
- **Vertikalabstand zur Auflagerebene**:
  Δz := z_B − h_B / 2 − z_E ≥ 0 (Unterkante über Auflager;
  meist Dicke der Trennlage / Sperrlage, typisch 1–3 mm).
- **Abstand zur OK Gelände** (Holzschutz-Größe nach
  DIN 68800-2): z_B − h_B / 2 − z_OKG, vorzeichenbehaftet,
  zu prüfen gegen 30 cm / 15 cm / 5 cm je nach
  Zusatzmaßnahmen; siehe Erläuterung.

## Wohldefiniertheit

- **Existenz**: In jeder Holzwand mit definierter Wand-Längsachse
  und mineralischem Auflager existiert eine Schwelle als
  unterster Längsträger; die Bedingungen 1–3 sind konstruktiv
  erfüllbar. Bedingung 4 wird im Tragwerks-Kontext geprüft.
- **Eindeutigkeit**: Bedingung 3 stellt sicher, dass nur das
  unterste horizontale Längsbauteil entlang der Wandachse als
  Schwelle qualifiziert. Bei Doppel-Schwellen (zwei
  übereinanderliegende Bretter als Schwellen-Paket im Holztafelbau)
  qualifiziert das untere als Schwelle im Sinne dieses Eintrags;
  das obere ist ein konstruktives Doppel und wird als separates
  Bauteil mit Rolle Schwelle oder als Bestandteil der Schwellen-
  Konstruktion modelliert (Implementierungs-Entscheidung).
- **Konsistenz mit `hg_bauteil.md`**: Alle Bedingungen aus
  `bauteil` (eindeutige Identität, Geometrie, Werkstoff, Lage in
  W) sind erfüllt; die Bauteilrolle „Schwelle" ergänzt die
  Lage-Constraints 1–4.
- **Geschoss-Unabhängigkeit**: Die Definition macht keine Aussage
  über das Geschoss. Eine Schwelle im Erdgeschoss auf Fundament/
  Sockel und eine Schwelle im Obergeschoss auf der darunterliegenden
  Decke (im Fachwerk-Vokabular: Grundschwelle vs. Stockschwelle)
  unterscheiden sich nur durch die Wahl der Auflagerebene E_⊥.
  Die Default-Lesart dieses Eintrags ist die Grundschwelle (E_⊥ =
  Oberkante Sockel/Bodenplatte); für die obergeschossige Lesart
  folgt ein eigener Eintrag `hg_stockschwelle.md` bei
  Mehrgeschoss-Bedarf.
- **Schwellen-Lesart ohne Bezugsebene**: Eine isolierte
  Schwelle ohne zugeordnete Auflagerebene ist im Sinne dieser
  Definition nicht qualifiziert; die Auflagernähe (Bedingung 2)
  setzt E_⊥ voraus. Im Modell wird E_⊥ aus dem Bauwerks-Kontext
  (Sockel-Oberkante, Decken-Oberkante) abgeleitet.
- **Nicht-Zirkularität**: Die Definition stützt sich nur auf
  bereits definierte Begriffe (`bauteil`, `bauteilachse`,
  `querschnitt`, `bezugsebene`, `weltkoordinatensystem`,
  `einheitsvektor`, `punkt`, `toleranzen`). Der Begriff
  `pfosten` aus Bedingung 4 ist Forward-Verweis und wird im
  Tragwerks-Kontext geprüft, nicht zur Definition der Schwelle
  selbst benötigt.

## Erläuterung (nicht normativ)

Die Schwelle ist im Holzbau die **erste Holzschicht über dem
mineralischen Untergrund** und zugleich die **konstruktive
Anschlussfuge zwischen Bauwerks-Sockel und Wand**. Sie erfüllt
drei Funktionen gleichzeitig:

- **statisch**: nimmt die Vertikallasten der Pfosten / Ständer
  auf und leitet sie kontinuierlich entlang der Wandlinie in das
  Fundament ein; verteilt Punktlasten zu einer Streckenlast und
  reduziert dadurch die Auflagerpressung auf das mineralische
  Auflager;
- **konstruktiv**: bildet die gerade, horizontale Anschluss-
  Linie, an der die Pfosten / Ständer aufstehen und gegen die
  die Riegel und Streben angeschlossen werden;
- **bauphysikalisch / holzschutz-konstruktiv**: stellt zusammen
  mit der Sperrlage die kapillare Trennung zwischen Sockel und
  Wandholz her und definiert die Höhenkote, oberhalb derer das
  Wandholz dauerhaft trocken bleiben soll.

### Wand-oben-Pendant: Rähm

Geometrisch und konstruktiv ist die Schwelle symmetrisch zum
**Rähm** (`raehm`): das Rähm schließt die Wand
oben ab, die Schwelle unten. Beide Bauteile haben üblicherweise
denselben Querschnitt und denselben Werkstoff; sie unterscheiden
sich nur durch Lage (oben/unten) und Funktion (Lasteinleitung in
Decke/Dach vs. Lasteinleitung in Sockel/Fundament). Ein Bauteil
kann **nicht gleichzeitig** Schwelle und Rähm sein, sondern ist
durch seine Wand-Vertikallage genau einer der beiden Rollen
zugeordnet.

### Holzschutz nach DIN 68800-2:2022-02

Die Schwelle ist das holzschutz-konstruktiv kritischste
Wandbauteil, weil sie der Spritzwasserzone am nächsten liegt.
Aus DIN 68800-2:2022-02 (Sektion §5.2.1.3, nach
Sekundär-Referaten — Norm-Volltext nicht direkt eingesehen)
folgen drei Regelmaße für den Mindestabstand der Schwellen-
Unterkante zur Oberkante Gelände:

| Maß | Anforderung |
|---|---|
| **≥ 30 cm** | Regelmaß ohne weitere Maßnahmen. |
| **≥ 15 cm** | Abminderung zulässig bei umlaufendem Kiesbett (Korn 16/32 mm, Bett-Breite ≥ 15 cm, Bett-Außenkante ≥ 30 cm zur Schwellen-Außenkante) **oder** wasserableitende Oberfläche mit ≥ 2 % Gefälle. |
| **≥ 5 cm**  | Abminderung zulässig nur bei zusätzlicher Abdichtung nach DIN 18533. |

Die Gebrauchsklasse (GK 2, GK 3.1, GK 3.2 nach EN 335 / DIN
68800-1) der konkreten Schwellen-Einbausituation hängt von der
konstruktiven Einbettung (Bewitterung, Trocknungsbedingungen,
Vordach) ab und ist eine **Instanz-Eigenschaft** des konkreten
Schwellen-Einbaus, **keine Typ-Eigenschaft der Bauteilrolle**.
Im Modell wird die GK als Annotation am konkreten Schwellen-
Bauteil geführt, nicht als Eigenschaft der Schwellen-Klasse.

### Sperrlage / Trennlage zwischen Schwelle und mineralischem Auflager

Zwischen Schwelle und mineralischem Auflager (Mauerwerk,
Stahlbeton-Sockel, Bodenplatte) ist eine horizontale Trenn- bzw.
Sperrlage erforderlich (Bitumenbahn oder dampfdiffusionsoffene
Spezial-Folie). Funktionen: kapillare Trennung gegen aufsteigende
Feuchte; Spritzwasserschutz an der seitlichen Schwellen-Flanke.
Verankerungen (Schwellenanker, Schwerlastdübel, Klebeanker)
durchdringen die Sperrlage; die Durchdringungen sind konstruktiv
abzudichten.

### Schweizer Praxis

In der Schweiz wird im Holzrahmen- und Holztafelbau **„Grundschwelle"**
für die Wand-Unterkante auf Bodenplatte/Sockel üblicher verwendet als
das alleinstehende „Schwelle"; im traditionellen Strick-/Blockbau ist
historisch „Sohlbank" oder „Schwellbalken" belegt — „Sohlbank"
kollidiert aber mit dem Fenster-Bauteil (siehe Quellenkonflikt (4))
und wird in diesem Glossar nicht als Synonym geführt. „Mauerschwelle"
ist in der CH-Praxis praktisch nicht etabliert und nur als
abgelehnte Benennung geführt. Die maßgebliche Schweizer Holzschutz-
Publikation ist **Lignatec 35/2023 „Holzschutz im Bauwesen"**
(Empa/Lignum); die 30-cm-Spritzwasserzone wird dort deckungsgleich
mit DIN 68800-2 angegeben, mit SIA-265-Verweis statt DIN.

### Andere Bedeutungen (Homonyme in anderen Domänen)

„Schwelle" ist außerhalb des Holzbau-Wand-Kontexts in weiteren
Bauteil- und Sach-Domänen einschlägig. Diese Bedeutungen sind
**keine** Varianten der hier definierten Wand-Schwelle und
gehören in eigene Begriffsfelder:

- **Türschwelle / Bodenschwelle** (Forward-Verweis `tuerschwelle`
  in `abgrenzung_zu:`): das untere Querholz oder Profil eines
  Türrahmens. Funktionen: Abdichtung gegen Wasser und Zugluft,
  Schallschutz, Bodenbelags-Übergang, Barrierefreiheit. Tür-
  Bauteil, nicht Wand-Bauteil; die etymologische Verbindung zur
  Fachwerk-Schwelle („Schwelle, über die man hinwegsteigt") ist
  heute nicht mehr begriffstragend.
- **Bahnschwelle** (Forward-Verweis `bahnschwelle` in
  `abgrenzung_zu:`, Klasse D — keine eigene HG-Anlage geplant):
  Querbalken aus Holz, Stahlbeton oder Stahl im Eisenbahn-
  Oberbau, der die Schienen quer zur Fahrtrichtung trägt und
  Lasten in den Schotterkörper verteilt. Außerhalb der
  Holzbau-Domäne.
- **Englisch: `sill plate` / `mudsill` vs. `sole plate` /
  `bottom plate`**. Die US-Praxis trennt schärfer als das Deutsche:
  - `sill plate` / `mudsill`: unterste Schwelle direkt auf dem
    Fundament (entspricht der hier definierten Schwellen-Lesart,
    Grundschwelle).
  - `sole plate` / `bottom plate`: unterste Schwelle einer
    Wandtafel auf einer Decke (im Mehrgeschoss-Holztafelbau auf
    der Geschossdecke; entspricht der Stockschwelle).
  Im DACH-Vokabular fallen beide unter „Schwelle"; die Unterscheidung
  wird über die Auflagerebene E_⊥ (Fundament vs. Decke) modelliert,
  nicht über die Bezeichnung. Daher sind alle vier englischen
  Begriffe in diesem Eintrag als Synonyme der Schwellen-Rolle
  geführt; in der App-Anzeige ist „Schwelle" bevorzugt.

### Schwellwert und weitere Bedeutungen

„Schwelle" im mathematisch-physikalischen Sinne (Schwellwert,
englisch `threshold`) und in der Wahrnehmungspsychologie
(Reizschwelle) sind außerhalb der Holzbau-Domäne; sie werden
nicht weiter behandelt.

## Beziehungen

- **Oberbegriff**: `bauteil`. Die Schwelle ist eine Bauteilrolle
  mit Lagebedingungen entlang einer Wand am untersten Niveau.
- **Bestandteile (partitiv)**: geerbt von `bauteil` (Bauteilachse,
  Querschnitt, Werkstoff, Faserrichtung); Faserrichtung axial
  entlang der Bauteilachse (Vollholz, BSH, ggf. LVL).
- **Verwendung / Beziehung zu anderen Bauteilen**:
  - **Pfosten / Ständer** (`pfosten`, Forward-Verweis): stehen
    auf der Schwelle und übertragen ihre Vertikallasten in die
    Schwelle. Die Schwelle ist deren unteres Auflager.
  - **Rähm** (`raehm`): geometrisches und
    konstruktives Pendant der Schwelle am Wand-Oberen-Niveau.
    Schwelle und Rähm schließen zusammen die Wand vertikal ab.
  - **Riegel** (zwischen zwei Pfosten in der Wandfläche, nicht
    durchlaufend): durch die Schwelle und ggf. Riegelreihen
    gehalten.
  - **Fundament / Sockel / Bodenplatte** (`fundament`,
    Forward-Verweis): mineralisches Auflager der Schwelle;
    durch die Sperrlage von der Schwelle getrennt und durch
    Schwellenanker mit ihr kraftschlüssig verbunden.
  - **Decke** (im Mehrgeschoss): bildet das Auflager für die
    Stockschwelle des darüberliegenden Geschosses.
- **Abgrenzung**:
  - **Rähm** (`raehm`): Welle-8-Geschwister;
    Wand-oben-Pendant. Geometrisch ähnlich (horizontaler
    Längsträger derselben Wandfluchten), aber an der Wand-
    Oberkante statt -Unterkante; trägt das Geschoss/Dach über
    sich, nicht das Wandgerippe selbst. Funktionen-Wechsel
    Schwelle ↔ Rähm ist nicht möglich am selben Bauteil; die
    Wand-Vertikallage entscheidet eindeutig.
  - **Fußpfette** (`fusspfette`): Dach-Bauteil unten im
    Dachtragwerk, parallel zur Traufe, trägt die Sparrenfüße.
    Trotz formaler Ähnlichkeit (horizontaler Stab auf einer
    Auflagerung) gehört die Fußpfette zum Dachtragwerk, nicht
    zur Wand. Im Tafelbau kann das oberste Rähm zugleich als
    Fußpfette wirken, aber die Schwelle hat **kein** Pendant am
    Dach: die Dach-Unterkante ist Fußpfette und Sparrenfuß,
    nicht „Schwelle".
  - **Pfette** (`pfette`): Pfetten gehören grundsätzlich zum
    Dachtragwerk und liegen parallel zu Dachkanten; Schwellen
    gehören zum Wandtragwerk und liegen parallel zu Wand-
    Achsen. Die regional und historisch belegte „Schwellpfette"
    (siehe `hg_fusspfette.md`) ist eine **Fußpfette** mit
    Schwellen-artiger Auflagerung, **nicht** eine Schwelle mit
    Pfetten-Funktion; die Bezeichnung steht trotz des
    Bestandteils „Schwelle" für eine Pfette.
  - **Pfosten** (`pfosten`, Forward-Verweis): lotrechtes Wand-
    Bauteil; steht **auf** der Schwelle. Pfosten und Schwelle
    sind komplementär (vertikal vs. horizontal an derselben
    Wand-Unterkante), nicht alternativ.
  - **Fundament** (`fundament`, Forward-Verweis):
    mineralisches Bauteil unterhalb der Schwelle; die Schwelle
    ist das **Holz**-Bauteil unmittelbar über dem Fundament.
    Schwelle und Fundament sind durch die Sperrlage räumlich
    getrennt; die kraftschlüssige Verbindung erfolgt über
    Schwellenanker.
  - **Bauteil** (`bauteil`): Schwelle ist Bauteilrolle, also
    ein konstruktiv spezialisierter Bauteil-Subtyp; die
    allgemeinen Bauteil-Eigenschaften (Identität, Geometrie,
    Werkstoff, Lage in W) bleiben erhalten.
  - **Stockschwelle** (`stockschwelle`, Forward-Verweis): im
    Fachwerk-Vokabular die unterste Schwelle eines
    Obergeschosses, auf der Decke des Untergeschosses; bei
    Mehrgeschoss-Bedarf eigener HG-Eintrag, geometrisch
    Spezialisierung dieses Eintrags mit anderer
    Auflagerebene E_⊥.
  - **Türschwelle** (`tuerschwelle`, Forward-Verweis):
    homonymes Tür-Bauteil, nicht Variante der Wand-Schwelle.
  - **Bahnschwelle** (`bahnschwelle`, Forward-Verweis,
    Klasse D — keine eigene HG-Anlage geplant): homonymes
    Eisenbahn-Bauteil, außerhalb der Holzbau-Domäne.
  - **Sohlbank** am Fenster (`sohlbank_fenster`, Forward-Verweis,
    Klasse D — keine eigene HG-Anlage geplant): unteres
    Querholz/-profil am Fensterstock; im Schweizer
    Strick-/Blockbau historisch zugleich Synonym zur
    Grundschwelle, in der modernen Bauweise ausschließlich
    Fenster-Bauteil.

## Implementierungshinweis

Datentyp (Domänen-Schicht, Kotlin, Schicht `domain.bauteil`):

```kotlin
package domain.bauteil

import domain.Toleranzen
import domain.bauteil.Bauteil
import domain.geometrie.Bezugsebene

/** Auflagerart der Schwelle; relevant für die Holzschutz-Bewertung. */
enum class SchwelleAuflager {
    BODENPLATTE_STAHLBETON,        // Stahlbeton-Bodenplatte direkt
    SOCKEL_MAUERWERK,              // gemauerter Sockel auf Fundament
    SOCKEL_STAHLBETON,             // Stahlbeton-Sockel
    GESCHOSSDECKE_HOLZ,            // im Mehrgeschoss-Holztafelbau (Stockschwellen-Konfiguration)
    GESCHOSSDECKE_STAHLBETON,      // Mehrgeschoss mit Stahlbeton-Decke
    UNBEKANNT
}

/** Gebrauchsklasse nach EN 335 / DIN 68800-1, Instanz-Eigenschaft. */
enum class Gebrauchsklasse {
    GK_0, GK_1, GK_2, GK_3_1, GK_3_2, GK_4, GK_5,
    UNBEKANNT
}

/**
 * Schwelle: unterster horizontaler Längsträger einer Wand,
 * unmittelbar auf einer Auflagerebene (Fundament, Sockel,
 * Bodenplatte, oder Geschossdecke).
 *
 * Glossar: hg_schwelle.md
 *
 * Synonyme: Grundschwelle (enges Synonym, CH und Fachwerk),
 * Schwellholz, Schwellbalken, Grundbalken; englisch sill plate /
 * sole plate / mudsill / bottom plate (US-Praxis-Disambiguation
 * im Erläuterungsblock).
 */
data class Schwelle(
    override val bauteil: Bauteil,
    val auflagerebene: Bezugsebene,
    val auflager: SchwelleAuflager = SchwelleAuflager.UNBEKANNT,
    val gebrauchsklasse: Gebrauchsklasse = Gebrauchsklasse.UNBEKANNT,
    val abstandZuOKGelaende: Double? = null            // mm, vorzeichenbehaftet, optional
) : Bauteil.Schwelle() {

    init {
        // 1. Horizontalität (Bedingung 1 aus hg_schwelle.md):
        //    |d_hat_B · e_hat_z| ≤ Toleranzen.KOLLINEAR_EPS — sonst
        //    Resultat.Fehler(SchwelleEntartet.NichtHorizontal).
        //    Sinus-Test; siehe HG_KONVENTIONEN.md Sektion 4.
        // 2. Auflagernähe (Bedingung 2): Unterkante des
        //    Schwellen-Querschnitts ≤ Toleranzen.LAENGE_EPS
        //    oberhalb der Auflagerebene — sonst
        //    SchwelleEntartet.NichtAufAuflager.
        // 3. Unterste Wand-Längslage (Bedingung 3) und
        // 4. Pfosten-Auflager (Bedingung 4) werden im
        //    Tragwerks-Kontext geprüft.
    }

    /**
     * Schwellen-Oberkante als lokale Bezugskote für Wandhöhen
     * und Pfosten-Längen.
     */
    fun oberkante(): Double =
        bauteil.bauteilachse.mittlereHoehe() + bauteil.querschnitt.hoehe / 2.0

    /**
     * Prüfung der DIN-68800-2-Mindestabstände zur OK Gelände.
     * Liefert true, wenn der Abstand für die gegebene
     * Zusatzmaßnahme zulässig ist.
     */
    fun erfuelltMindestabstand(
        zusatz: HolzschutzZusatzmassnahme
    ): Boolean? {
        val abstand = abstandZuOKGelaende ?: return null
        return when (zusatz) {
            HolzschutzZusatzmassnahme.KEINE        -> abstand >= 300.0
            HolzschutzZusatzmassnahme.KIESBETT     -> abstand >= 150.0
            HolzschutzZusatzmassnahme.ABDICHTUNG_18533 -> abstand >=  50.0
        }
    }

    /**
     * Anzeigename: bevorzugt „Schwelle"; bei Auflagerung auf
     * Geschossdecke darf zusätzlich „(Stockschwelle)" annotiert
     * werden, sobald hg_stockschwelle.md existiert.
     */
    fun anzeigeName(): String = "Schwelle"
}

enum class HolzschutzZusatzmassnahme {
    KEINE,
    KIESBETT,                  // 16/32 mm, ≥ 15 cm Breite, ≥ 30 cm Abstand
    ABDICHTUNG_18533           // Bauwerksabdichtung nach DIN 18533
}

sealed class SchwelleEntartet {
    object NichtHorizontal      : SchwelleEntartet()
    object NichtAufAuflager     : SchwelleEntartet()
    object NichtUnterstesLaengsbauteil : SchwelleEntartet()
    object KeinPfostenAufgesetzt: SchwelleEntartet()
}
```

- **Einheit**: Längen in mm; Winkel intern in Radiant.
- **Identität**: `BauteilId` aus dem zugrunde liegenden Bauteil.
- **Invarianten** (zusätzlich zu denen von `Bauteil`):
  1. Horizontalität der Bauteilachse — sonst `NichtHorizontal`.
  2. Auflagernähe zu einer horizontalen Auflagerebene — sonst
     `NichtAufAuflager`.
  3. Unterstes Längsbauteil entlang der Wandlinie — sonst
     `NichtUnterstesLaengsbauteil` (Tragwerks-Cross-Cutting).
  4. Mindestens ein aufgesetzter Pfosten / Ständer — sonst
     `KeinPfostenAufgesetzt` (Tragwerks-Cross-Cutting).
- **Edge Cases**:
  - **Doppel-Schwelle** (zwei übereinanderliegende Bretter im
    Holztafelbau): das untere Bauteil qualifiziert; das obere
    wird als separates Bauteil mit eigener Rolle oder als
    Schwellen-Paket-Komponente modelliert.
  - **Eckverbindung zweier Schwellen verschiedener Wände**: je
    Wandlinie eine Schwelle; die Eckverbindung (Blattung, Zapfen,
    Stoss) ist eigene Bearbeitung an beiden Schwellen.
  - **Schwelle in Wandöffnung** (Türstock): die Schwelle ist in
    der Wandöffnung unterbrochen; die Türschwelle des Türrahmens
    ist eigenes Bauteil und nicht Bestandteil der Wand-Schwelle.
  - **Eingelassene Schwelle**: bei sehr geringer Aufbauhöhe
    sitzt die Schwelle in einer Aussparung des Sockels;
    Bedingung 2 mit δ_z um die Einlasstiefe erweitern.
  - **Stockschwelle** (Mehrgeschoss): Auflagerebene E_⊥ ist die
    Geschossdecke statt Sockel/Bodenplatte; geometrisch
    qualifiziert nach denselben Bedingungen 1–4.
- **Abgeleitete Eigenschaften**:
  - `getrageneStaenderIn(t: Tragwerk): List<Pfosten>` — Pfosten
    in `t`, deren unterer Endpunkt auf der Schwellen-Bauteilachse
    innerhalb Toleranzen liegt.
  - `holzschutzNachweis(): NachweisErgebnis` — Auswertung
    `abstandZuOKGelaende` gegen DIN-68800-2-Maße in Kombination
    mit `HolzschutzZusatzmassnahme`.
  - `gebrauchsklasseAusEinbau(): Gebrauchsklasse` — Ableitung
    der GK aus konstruktiver Einbettung (Bewitterung, Vordach,
    Trocknung).

## Quellen

**Primär (normativ):**

- DIN 68800-2:2022-02, „Holzschutz – Teil 2: Vorbeugende
  bauliche Maßnahmen im Hochbau".
- DIN EN 1995-1-1:2010-12, „Eurocode 5".
- DIN 1052:2008-12.
- DIN 18533-1:2017-07, „Abdichtung von erdberührten Bauteilen".
- EN 335:2013 / DIN 68800-1:2011-10, „Gebrauchsklassen".

**Sekundär:**

- Lignum (Hrsg.): *Lignatec 35/2023 – Holzschutz im Bauwesen.*
  Empa/Lignum, Zürich 2023.
- Mönck, W.; Rug, W.: *Holzbau – Bemessung und Konstruktion.*
  16. Auflage, Beuth, Berlin 2015.
- Gerner, M.: *Fachwerk – Instandsetzung, Sanierung, Neubau.*
  DVA, 7. Auflage 2007.
- Natterer, J.; Herzog, T.; Volz, M.: *Holzbau-Atlas.* 4. Auflage,
  Birkhäuser, Basel 2003.
- Informationsdienst Holz: *Reihe 5 Teil 2 Folge 2 – Holzschutz
  – Bauliche Maßnahmen.*
- Holzfaser-Verband: *Merkblatt Anschlüsse und Fugen – Details
  für Holzmassivbau.*

**Korpus (nicht autoritativ):**

- Wikipedia, Lemmata „Fachwerkschwelle", „Rähm", „Sill plate",
  „Gebrauchsklasse (Holzschutz)" (abgerufen 2026-05-14).
- Baukobox, „Schwelle, Schwellenholz" (abgerufen 2026-05-14).
- BILP, FH Finnholz Lexikon, Bohnholzbau Lexikon (abgerufen
  2026-05-14).
- Recherche-Bericht: `docs/recherche/2026-05-14_hg_schwelle.md`.
