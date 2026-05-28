---
id: dampfbremse
benennung: Dampfbremse
synonyme: [Dampfbremsfolie, "diffusionshemmende Schicht", Klimamembran]
abgelehnte_benennungen: [Dampfsperre, Luftdichtheitsebene, Luftdichtungsbahn, Tauwassersperre, "PE-Folie", "vapour barrier", "vapour retarder", "air barrier"]
oberbegriff: schicht
begriffstyp: generisch
voraussetzungen: [schicht, dachaufbau, waermedaemmung, toleranzen]
abgrenzung_zu: [schicht, dachaufbau, waermedaemmung, unterdach, eindeckung, dachabdichtung, dampfsperre, luftdichtheitsebene]
status: entwurf
theorie_pflichtig: required
quellen_primär:
  - "DIN 4108-3:2018-10 'Wärmeschutz und Energie-Einsparung in Gebäuden – Teil 3: Klimabedingter Feuchteschutz – Anforderungen, Berechnungs- und Bemessungsverfahren', Abschnitt 'Klassifizierung von Schichten nach dem Wasserdampfdiffusionswiderstand' (sd-Wert-Klassen diffusionsoffen / diffusionshemmend / diffusionsdicht)."
  - "DIN EN ISO 12572:2025-03 'Wärme- und feuchtetechnisches Verhalten von Baustoffen und Bauprodukten — Bestimmung der Wasserdampfdurchlässigkeit — Cup-Verfahren', Abschnitt 3 (Begriffe sd-Wert, µ-Wert)."
  - "DIN EN 13984:2013-05 'Abdichtungsbahnen — Kunststoff- und Elastomer-Dampfsperrbahnen — Definitionen und Eigenschaften', Begriffsabschnitt (Produktnorm für Bahnen)."
  - "SIA 180:2014 'Wärmeschutz, Feuchteschutz und Raumklima in Gebäuden', Schweizerischer Ingenieur- und Architektenverein, Abschnitt 'Feuchteschutz' (Dampfbremse als Funktionsschicht; Doppelfunktion mit Luftdichtheitsebene zulässig)."
  - "DIN 4108-7:2011-01 (Neuausgabe 2026-04) 'Wärmeschutz und Energie-Einsparung in Gebäuden – Teil 7: Luftdichtheit von Gebäuden', Abschnitt 'Luftdichtheitsebene' (zur Abgrenzung gegen die Diffusionsschicht zitiert)."
quellen_sekundär:
  - "Wegleitung zur Norm SIA 180, Gebäudehülle Schweiz / SIA 4001:2022."
  - "Lignum (Hrsg.): Lignatec 'Geneigte Dächer in Holzbauweise', Lignum, Zürich, aktuelle Auflage, Kap. 'Feuchteschutz'."
  - "Informationsdienst Holz: 'Tauwasserschutz im Holzbau', DE-Branchenträger."
  - "Mönck, W.; Rug, W.: Holzbau – Bemessung und Konstruktion, 16. Aufl., Beuth Verlag 2015, Kap. 'Feuchteschutz und Dampfdiffusion'."
  - "Fraunhofer-IBP: Anwendungshinweise zu DIN EN 15026 (hygrothermische Simulation, WUFI)."
  - "pro clima Technische Information: INTELLO/INTELLO PLUS, DB+ — feuchtevariabler sd-Wert-Bereich."
  - "SIGA.swiss: Produktdaten Majrex 200 — Hygrobrid-Membran mit richtungsabhängigem sd-Wert."
  - "Recherchebericht docs/recherche/2026-05-14_hg_dampfbremse.md."
quellenkonflikt: |
  **(1) sd-Wert-Schwelle 100 m falsifiziert.** Die ursprüngliche
  Auftrags-Hypothese verortete die Trenngrenze zwischen Dampfbremse
  und Dampfsperre bei **sd = 100 m**. Diese Schwelle ist in keiner
  konsultierten Norm- oder Lehrbuchquelle als definitorische
  Begriffsgrenze belegt. Die in DIN 4108-3:2018-10 verankerte
  Klassifikation trennt **diffusionsoffen** (sd < 0,5 m),
  **diffusionshemmend** (0,5 m ≤ sd ≤ 1500 m) und **diffusionsdicht**
  (sd > 1500 m); die Grenze liegt bei **sd = 1500 m**, nicht bei
  100 m. Die 100-m-Linie ist eine **Praxis-/Produktkonvention** für
  PE-Folie (Standard-PE-Folie ca. 0,2 mm Dicke ≈ sd 100 m;
  Produktname „SD100"), keine normative Definitionsschwelle. Im
  Glossareintrag wird die DIN-4108-3-Grenze 1500 m verwendet; die
  100-m-Linie ist nur in der Erläuterung als PE-Folie-Praxis-Schwelle
  vermerkt. Recherche-Bericht:
  `docs/recherche/2026-05-14_hg_dampfbremse.md`, Abschnitt C.

  **(2) „Dampfsperre veraltet" — Hersteller-Konsens, nicht Norm.**
  Die Auftrags-Aussage „Dampfsperre veralteter Begriff, durch
  Dampfbremse ersetzt" trifft die Sprache der Hersteller (SIGA,
  pro clima, Isover) im modernen Holzbau, ist aber **nicht
  normativ** belegt. DIN 4108-3 führt die Klasse „diffusionsdicht"
  (sd > 1500 m) weiter; DIN EN 13984 trägt den Begriff
  „Dampfsperrbahnen" im deutschen Titel. „Dampfsperre" ist im
  Glossar daher **kein abgelehnter Synonym-Eintrag** der Dampfbremse,
  sondern eine **eigene Klasse** (sd > 1500 m) — geführt als
  Forward-Verweis Kategorie A (`hg_dampfsperre.md`, Trigger: erste
  Schwimmbad-/Industriedach-Modellierung mit Aluminium- oder
  Bitumenbahn). Die Migration aus `abgelehnte_benennungen` in einen
  eigenen Eintrag ist beim Anlegen von `hg_dampfsperre.md`
  nachzuziehen.

  **(3) Luftdichtheitsebene funktional getrennt.** Nach
  DIN 4108-7 ist die **Luftdichtheitsebene** eine eigenständige
  Funktionsschicht (Schutz vor konvektivem Feuchteeintrag durch
  Druckdifferenzen), normativ getrennt von der **Dampfbremse**
  als Diffusionsschicht (Schutz vor Diffusion durch
  Dampfdruckgefälle). In der Holzbau-Praxis werden beide
  Funktionen häufig **auf derselben Bahn** realisiert (raumseitige
  Bahn mit verklebten Stössen erfüllt beides). SIA 180:2014
  erlaubt diese Doppelnutzung ausdrücklich. Die definitorische
  Trennung bleibt aber bestehen: eine lose verlegte Dampfbremse
  ohne Stoss-Verklebung ist Dampfbremse, aber nicht Luftdichtheits-
  ebene; eine Holzwerkstoffplatte als luftdichte Schicht ist
  Luftdichtheitsebene, aber nur dann Dampfbremse, wenn ihr sd-Wert
  im diffusionshemmenden Bereich liegt. Im Glossar wird
  `luftdichtheitsebene` als Forward-Verweis Kategorie A geführt
  (Trigger: erste Bauphysik-Vollmodellierung mit Blower-Door-
  Schnittstelle); die Dampfbremse ist hier strikt als
  **Diffusionsschicht** definiert.

  **(4) Wahl des `oberbegriff: schicht`.** Der Oberbegriff `schicht`
  (`hg_schicht.md`) ist im selben R-Schritt entstanden und sammelt
  alle Funktionsschichten des Dachaufbaus. Die Dampfbremse ist eine
  Spezialisierung von `schicht` mit fixierter Funktionsklasse
  (`SchichtFunktion.DAMPFBREMSE`). Code-Realisierung folgt der
  Komposition-Strategie (`Dampfbremse.schicht: Schicht`), nicht
  der Vererbung — siehe `hg_schicht.md` Quellenkonflikt-Punkt 5.

  **(5) Wahl des `begriffstyp: generisch`.** Die Dampfbremse trägt
  interne Struktur (Bahn-Material + Schichtdicke + sd-Wert-Funktion
  + Nahtsystem) und eine sealed-Hierarchie nach Funktionsweise:
  **Konventionell** (konstanter sd-Wert; PE-Folie, Aluminium-frei
  bis 1500 m), **Feuchteadaptiv** (sd-Wert als monotone Funktion
  der mittleren relativen Feuchte φ̄; INTELLO 0,25–25 m, DB+
  0,4–4 m, Vario KM 0,3–5 m), **Hygrobrid** (sd-Wert zusätzlich
  richtungsabhängig je Seite der Bahn; SIGA Majrex 0,8–35 m). Sie
  ist nicht Lebenszyklus-gekoppelt an den Dachaufbau (eine
  Dampfbremse kann erneuert werden, ohne dass der Aufbau
  vollständig entfernt wird); damit nicht `partitiv`. Die Bahn
  besteht im Geltungsbereich nicht aus eigenständigen Trägerbegriffen
  mit eigener Identität; damit nicht `aggregat`. Sie ist geometrisches
  Objekt (Schicht mit positiver Dicke), kein Wert; damit nicht
  `merkmal`.

  **(6) Tauwassernachweis nicht in die Definition aufgenommen.**
  Glaser-Verfahren (DIN 4108-3, stationär) vs. hygrothermische
  Simulation (DIN EN 15026, instationär, WUFI/Delphin) sind
  Methoden der bauphysikalischen Beurteilung, nicht
  Merkmale des Begriffs `Dampfbremse`. Die Wahl der Nachweis-
  methode ist Anwendung, nicht definitorischer Bestandteil; sie
  ist im Eintrag bewusst weggelassen.

  **(7) Norm-Volltext-Lücke.** Die Wortlauten der DIN-4108-3-
  Klassen „diffusionsoffen / -hemmend / -dicht" und die genaue
  Schwellen 0,5 m und 1500 m sind über mehrere konsistente
  Sekundärquellen (BauNetz Wissen, energie-experten.org, ifb.info,
  Wissen-Wiki, DIN-NABau-Auslegungen) belegt; der DIN-4108-3-
  Volltext wurde nicht im Original eingesehen (Paywall). SIA 180
  ebenfalls nur sekundär (Holzbau-Schweiz-Magazin, SIGA, Isover).
  Die Klassen-Bezeichnungen sind aufgrund der breiten Konvergenz
  der Sekundärquellen als gesichert anzunehmen; eine
  Volltext-Verifikation erfolgt bei nächster Gelegenheit.

  **(8) „Klimamembran" als Synonym nur der feuchteadaptiven
  Variante.** Der Begriff „Klimamembran" wird im DACH-Korpus
  uneinheitlich gebraucht (bausep, Isover: Sammelbegriff; pro clima
  vermeidet; Isover-Markenname „Vario KM"). Er ist nicht
  normativ verankert. Im Glossar wird er als Synonym der
  **gesamten** Dampfbremse geführt (nach Auftrag), mit dem Hinweis
  in der Erläuterung, dass die berufssprachliche Bindung an die
  feuchteadaptive Variante stärker ist.

  **(9) Lokales Norm-Enum `DampfbremsenNorm`.** Die Norm-Aufzählung in
  der parametrischen Klassifikation
  `klassifiziereNachSdWert(sd, norm)` heisst lokal `DampfbremsenNorm`,
  nicht generisch `Norm`. Damit kollidiert sie nicht mit den lokalen
  Enums `UnterdachNorm` (`hg_unterdach.md`), `AbdichtungsNorm`
  (`hg_dachabdichtung.md`) und `WaermedaemmungsNorm`
  (`hg_waermedaemmung.md`). `DIN_4108_3` ist namensgleich auch in
  `UnterdachNorm` und `WaermedaemmungsNorm` enthalten, weil diese
  Feuchteschutz-Norm in mehreren Bauphysik-Modellierungen
  referenziert wird. **Folgearbeit-Trigger:** sobald mindestens zwei
  Bauphysik-Module dieselbe Norm funktional referenzieren (im
  aktuellen Bestand bereits gegeben: DIN 4108-3 in Dampfbremsen-,
  Unterdach- *und* Wärmedämmungs-Kontext), wird ein zentraler
  Eintrag `hg_norm.md` angelegt und `DampfbremsenNorm` durch eine
  Filter-Sicht auf das gemeinsame Norm-Enum ersetzt; bis dahin
  bleibt die lokale Form mit eindeutigem Klassennamen, und die
  wertgleichen Enum-Konstanten in verschiedenen lokalen Enums
  werden bei der Migration zu einem gemeinsamen Wert
  deduppliziert.
---

## Prosa-Definition

Eine **Dampfbremse** ist eine raumseitige diffusionshemmende
Funktionsschicht des wärmegedämmten Bauteils, deren wasserdampf-
diffusionsäquivalente Luftschichtdicke (sd-Wert) im Bereich
0,5 m ≤ sd ≤ 1500 m nach DIN 4108-3 liegt und die in dieser
Lage den Wasserdampf-Diffusionsstrom von innen nach aussen so
weit reduziert, dass das Ausfallen von Tauwasser in der
Wärmedämmung und an angrenzenden Holzbauteilen begrenzt bleibt.

## Mathematische Definition

Sei

- A = (𝒟, 𝒮, H) ein **Dachaufbau** im Sinne von `dachaufbau` mit
  Dachflächen-Familie 𝒟 = { D₁, …, D_m }, geordneter Schichtfolge
  𝒮 = (S₁, …, S_k) von innen nach aussen, und Dachhaut H,
- F := ⋃_{i=1..m} F(P_i) ⊂ ℝ³ der Trägerbereich der Dachflächen,
- ein Index j* ∈ { 1, …, k } so gewählt, dass die Schicht S_{j*}
  die Funktionsklasse `SchichtFunktion.DAMPFBREMSE` trägt,
- d_{j*} ∈ ℝ_{>0} (in mm) die Dicke von S_{j*},
- φ̄ ∈ [0, 1] die mittlere relative Feuchte im Querschnitt der
  Bahn (dimensionslos),
- σ ∈ { **innen**, **aussen** } die Seite der Bahn,
- s_d : [0, 1] × { innen, aussen } → ℝ_{>0} die sd-Wert-Funktion
  der Bahn, Einheit m,
- s_min, s_max ∈ ℝ_{>0} mit s_min ≤ s_max die zertifizierten
  Schranken der Bahn nach DIN EN 13984.

Dann ist eine **Dampfbremse** das Quintupel

```
B := (𝒟, S_{j*}, s_d, s_min, s_max)
```

mit den Konsistenzbedingungen

1. **Lage im Dachaufbau:** j* > 1 und j* ≤ k − 1; die
   Dampfbremse liegt **raumseitig** der Wärmedämmung im Aufbau
   und ist nicht die äusserste Schicht.
2. **Funktionsklasse:** `S_{j*}.funktion = DAMPFBREMSE`.
3. **Positive Dicke:** d_{j*} > Toleranzen.LAENGE_EPS.
4. **Diffusionshemmende Schranken (DIN 4108-3):**
   0,5 m ≤ s_min ≤ s_max ≤ 1500 m.
5. **Wertebereichs-Konsistenz:** für alle (φ̄, σ)
   gilt s_min ≤ s_d(φ̄, σ) ≤ s_max.
6. **Träger-Konsistenz:** S_{j*} ist über F definiert (gleiche
   Träger-Dachflächen wie A).

Die **sd-Wert-Funktion** s_d beschreibt das Diffusionsverhalten
der Bahn. Die folgenden drei Spezialformen klassifizieren die
sealed-Hierarchie:

- **Konventionell:** s_d ist konstant in φ̄ und in σ, also
  s_d(φ̄, σ) ≡ s_konst mit s_min = s_max = s_konst.
- **Feuchteadaptiv:** s_d ist unabhängig von σ (richtungs-
  symmetrisch), aber monoton antiton in φ̄: für φ̄₁ ≤ φ̄₂ gilt
  s_d(φ̄₁) ≥ s_d(φ̄₂). Die physikalische Lesart: bei niedriger
  Feuchte (Winter, raumseitig) ist sd hoch (Diffusion gehemmt);
  bei hoher Feuchte (Sommer, Rücktrocknung) ist sd niedrig
  (Diffusion erlaubt).
- **Hygrobrid:** s_d hängt sowohl von φ̄ als auch von σ ab und
  ist im Allgemeinen weder symmetrisch in σ noch in φ̄ monoton
  in derselben Richtung. Charakterisierend ist eine asymmetrische
  Bedingung der Form s_d(φ̄, innen) ≠ s_d(φ̄, aussen) für mindestens
  ein φ̄ ∈ [0, 1].

Die **wasserdampf-diffusionsäquivalente Luftschichtdicke** in der
zugrunde liegenden Materialdefinition ist

```
s_d = µ · d
```

mit µ ∈ ℝ_{>0} (Wasserdampf-Diffusions-Widerstandszahl,
dimensionslos, DIN EN ISO 12572) und d ∈ ℝ_{>0} (Schichtdicke
in m). Bei feuchteadaptiven und Hygrobrid-Bahnen ist µ selbst
eine Funktion µ(φ̄, σ); s_d = µ(φ̄, σ) · d folgt punktweise.

**Bemerkung — Bindung an konkrete Bahn-Produkte.** Die
definitorische Schicht legt keine konkreten Produktklassen
(INTELLO, DB+, Majrex, Vario KM, PE-Folie) im Begriff fest;
diese sind als Spezialisierungen der drei Funktionsweisen
einzuordnen, mit produktspezifischen Schranken (s_min, s_max).

## Wohldefiniertheit

- **Existenz.** Für jeden Dachaufbau A mit einer Schicht der
  Funktionsklasse DAMPFBREMSE, einer Bahn mit zertifizierten
  Schranken (s_min, s_max) ⊂ [0,5 m, 1500 m] und einer
  Funktion s_d, die die Schrankenbedingung punktweise erfüllt,
  ist B wohldefiniert.
- **Eindeutigkeit der Funktion s_d.** s_d ist als Eingabe
  Teil des Tupels; eine in φ̄ und σ konstante Funktion existiert
  immer (Konventionell). Für feuchteadaptive Bahnen ist die
  Antitonie eine Anforderung an die Eingabefunktion, kein
  Bestandteil der Existenz-Behauptung: ist die Eingabefunktion
  nicht antiton, fällt der Subtyp `Feuchteadaptiv` weg und das
  Tupel ist als `Konventionell` oder `Hygrobrid` zu konstruieren.
- **Klassen-Disjunktheit.** Die drei Subtypen sind durch die
  Form der Funktion eindeutig diskriminiert:
  s_d-konstant ⇒ Konventionell;
  s_d antiton in φ̄, symmetrisch in σ ⇒ Feuchteadaptiv;
  s_d asymmetrisch in σ ⇒ Hygrobrid.
  Grenzfälle (annähernd konstante Bahn, die als Konventionell
  oder schwach feuchteadaptiv eingeordnet werden könnte) werden
  über eine Toleranz auf den Variations-Schwerpunkt der Funktion
  in der Validierung diskriminiert; diese Diskriminierung ist
  konstruktive Modellierungsentscheidung, nicht Eindeutigkeits-
  problem der Definition.
- **Eindeutigkeit der Dampfbremsen-Schicht im Aufbau.** Die
  Definition lässt offen, ob ein Dachaufbau **eine** oder
  **mehrere** Schichten der Funktionsklasse DAMPFBREMSE enthalten
  darf. Im üblichen Aufbau ist j* eindeutig; bei doppelter
  Diffusionssicherung (Sonderfall Sanierung) zerfällt B in
  mehrere Dampfbremsen-Instanzen, je Schicht eine.
- **Konsistenz mit `dachaufbau`.** Die Dampfbremse ist eine
  Schicht S_{j*} **im** Dachaufbau; sie ist kein eigenständiges
  Aggregat ausserhalb des Aufbaus und teilt mit ihm den
  Trägerbereich F.
- **Konsistenz mit `dachhaut` und `unterdach`.** Die Dampfbremse
  liegt **raumseitig** der Wärmedämmung und damit weit unterhalb
  der Dachhaut H und des Unterdachs S_{j_unterdach} (mit
  j_unterdach > j*). Eine konstruktive Überschneidung ist
  ausgeschlossen.
- **Grenzfall sd = 1500 m.** Der Wert sd = 1500 m liegt am
  Rand der diffusionshemmenden Klasse nach DIN 4108-3. Die
  Toleranz auf die obere Schranke wird konventionell als
  scharf gewertet: s_max ≤ 1500 m (inkl.); sd > 1500 m fällt
  in die Klasse `dampfsperre` (Forward-Verweis A) und wird
  hier ausdrücklich nicht erfasst.
- **Nicht-Zirkularität.** Die Definition verwendet die Primitive
  Punkt, Strecke, Polygon, die reellen Zahlen, monotone
  Funktionen sowie die bereits definierten Begriffe `dachaufbau`,
  `dachflaeche`, `waermedaemmung`, `toleranzen`. Die abgegrenzten
  Begriffe `eindeckung`, `dachabdichtung`, `unterdach`,
  `dampfsperre`, `luftdichtheitsebene` treten nur erläuternd auf,
  nicht definitorisch.

## Erläuterung (nicht normativ)

Die Dampfbremse ist im DACH-Holzbau die **raumseitige
Funktionsschicht des wärmegedämmten Daches**, die den Eintrag
von Wasserdampf aus dem Innenraum in die Wärmedämmung durch
**Diffusion** reduziert. Sie ist nach DIN 4108-3 über die
sd-Wert-Klassifikation eingegrenzt:

| Klasse                 | sd-Wert          | Bezeichnung               |
|---|---|---|
| diffusionsoffen        | sd < 0,5 m       | nicht Dampfbremse         |
| **diffusionshemmend**  | 0,5 m ≤ sd ≤ 1500 m | **Dampfbremse**       |
| diffusionsdicht        | sd > 1500 m      | `dampfsperre` (Forward A) |

Die im Auftrag angedeutete Schwelle „sd = 100 m" zwischen
Dampfbremse und Dampfsperre ist **keine normative Grenze**,
sondern eine **Praxis-Konvention**: klassische PE-Folie
(d ≈ 0,2 mm, µ ≈ 500 000) erreicht sd ≈ 100 m und wird im
Volksmund häufig als „Dampfsperre" bezeichnet, weil sie für
übliche Wohnbau-Anwendungen ausreichend dampfdicht ist. Norm-
seitig bleibt eine PE-Folie SD100 eine Dampfbremse (0,5 ≤ 100 ≤
1500).

### Funktionsweise der drei Subtypen

Die App führt drei Subtypen als sealed-Klassen:

| Subtyp           | s_d-Funktion             | Beispiel-Produkte                 | typischer Bereich |
|---|---|---|---|
| **Konventionell** | konstant in φ̄ und σ      | PE-Folie SD100, Aluminium-frei    | 2 m bis 1500 m    |
| **Feuchteadaptiv** | antiton in φ̄, symmetrisch in σ | pro clima INTELLO/INTELLO PLUS, pro clima DB+, Isover Vario KM Duplex UV | 0,25 m bis 25 m   |
| **Hygrobrid**     | asymmetrisch in σ         | SIGA Majrex 200                   | 0,8 m bis 35 m    |

- **Konventionelle Dampfbremse:** konstanter sd-Wert. Wirkt im
  Winter (Diffusion vom warmen Innenraum nach aussen) wie im
  Sommer (umgekehrtes Gefälle bei aufgeheiztem Dach). Begrenzt
  Rücktrocknung nach innen.
- **Feuchteadaptive Dampfbremse (Klimamembran):** der sd-Wert
  sinkt mit steigender mittlerer Umgebungsfeuchte im Querschnitt
  der Bahn. Im Winter (trockene Raumluft, niedriges φ̄ im
  Querschnitt) ist sd hoch; im Sommer (feuchte Konstruktion bei
  Rücktrocknung, hohes φ̄) ist sd niedrig. Die Bahn erlaubt die
  Rücktrocknung der Konstruktion nach innen, ohne im Winter die
  Diffusionshemmung aufzugeben. Der Begriff „Klimamembran" ist
  ein Branchen-Begriff für diese Variante; er ist im DACH-Korpus
  uneinheitlich gebraucht und im Glossar als Synonym geführt,
  ohne normative Bindung.
- **Hygrobrid-Dampfbremse:** der sd-Wert hängt zusätzlich von
  der **Seite** der Bahn ab (innen vs. aussen). Bei SIGA Majrex
  200 ist sd_innen (raumseitig) deutlich höher als sd_aussen
  (dämmungsseitig), so dass die Bahn Feuchte stärker aus der
  Dämmung in den Raum ablässt als umgekehrt. Strukturell ist
  Hygrobrid eine eigenständige Funktionsklasse, nicht eine
  Sub-Sub-Variante der Feuchteadaptiven, weil die Asymmetrie
  in σ ein qualitativ neues Merkmal ist.

### Luftdichtheit vs. Diffusion

Die Dampfbremse ist die **Diffusionsschicht**; die
**Luftdichtheitsebene** (DIN 4108-7, SIA 180) ist eine
**funktional getrennte Schicht**, die den konvektiven Lufttausch
durch Stoss- und Anschlussfugen verhindert. Die beiden Schichten
werden in der Holzbau-Praxis **häufig auf derselben Bahn**
realisiert (raumseitige Dampfbremse mit verklebten Stössen
erfüllt zugleich die Luftdichtheits-Anforderung); SIA 180
erlaubt diese Doppelnutzung ausdrücklich. Funktional bleibt die
Trennung streng:

- Eine lose verlegte Dampfbremse ohne Stoss-Verklebung ist
  diffusionshemmend, aber nicht luftdicht — heute Ausführungs-
  Mangel.
- Eine Holzwerkstoffplatte (z. B. OSB-Schalung) kann als
  Luftdichtheitsebene fungieren und (bei sd 1–4 m je nach
  Dicke und Hersteller) zugleich Dampfbremse sein; sie wird
  dann nach DIN 4108-3 mit ihrem realen sd-Wert als Bahn
  modelliert.

Quantitativ ist der konvektive Feuchteeintrag durch
Undichtheiten typischerweise **10- bis 1000-mal grösser** als
der diffusive Eintrag bei intakter Dampfbremse; die
Luftdichtheit ist deshalb in der Praxis die dominante
Schutzgrösse, auch wenn die Dampfbremse die normative
Aufmerksamkeit auf den Diffusionsstrom lenkt.

### Tauwassernachweis (Anwendung, nicht Begriff)

Die bauphysikalische Bewertung eines Aufbaus mit Dampfbremse
erfolgt nach DIN 4108-3 **stationär (Glaser-Verfahren)** oder
nach DIN EN 15026 **instationär (hygrothermische Simulation,
WUFI, Delphin)**. Das Glaser-Verfahren ist auf Aufbauten mit
**konstantem sd-Wert** beschränkt und kann feuchteadaptive
Bahnen nicht modellieren; für solche Bahnen sowie für alle
Aufbauten mit Schlagregen- oder Sonneneinstrahlungs-Lastfall
ist die hygrothermische Simulation Stand der Technik. Die Wahl
der Nachweismethode ist **Anwendung**, nicht Begriffsmerkmal
der Dampfbremse; sie ist im Eintrag nicht definitorisch verankert.

### IFC-Pendant

Im IFC-Schema wird die Dampfbremse als **`IfcMaterialLayer`** in
einem `IfcMaterialLayerSet` der Dachkonstruktion realisiert.
Es gibt im Standard **kein eigenständiges `Pset_VapourBarrier`**;
der sd-Wert wird über `Pset_MaterialCommon.VaporPermeability`
(bzw. die µ-Zahl mit Layer-Dicke) abgelegt, die Funktionsrolle
über `IfcMaterialLayer.Category = "VapourBarrier"` oder
`"VapourControlLayer"`. BTLx (cadwork, hsbcad) führt
„Dampfbremse" als explizite Funktionsklasse in der Material-
Bibliothek.

## Beziehungen

- **Oberbegriff:** derzeit `null`. Künftig **`schicht`**, sobald
  der Schicht-Begriff als Hauptglossar-Eintrag angelegt ist
  (parallel zum vorliegenden Eintrag in Vorbereitung; analog zur
  Pendant-Situation bei `dachaufbau`, `dachhaut`, `unterdach`,
  `eindeckung`).
- **Bestandteil von:** Eine Dampfbremse ist eine Schicht S_{j*}
  eines `dachaufbau`. Sie ist Bestandteil des Aufbaus, nicht
  selbst eigenständiges Aggregat.
- **Spezialisierungen (sealed-Hierarchie nach Funktionsweise
  der sd-Wert-Funktion):**
  - **Konventionelle Dampfbremse** — konstanter sd-Wert.
  - **Feuchteadaptive Dampfbremse** — antitone Abhängigkeit
    von der mittleren relativen Feuchte φ̄, symmetrisch in der
    Seite σ.
  - **Hygrobrid-Dampfbremse** — zusätzlich asymmetrisch in σ.
- **Verwendung:**
  - Funktions-Schicht im `dachaufbau`
    (`SchichtFunktion.DAMPFBREMSE`).
  - Raumseitig der `waermedaemmung`.
- **Abgrenzung:**
  - **`schicht`:** der Oberbegriff aller Schichten des Dachaufbaus;
    die Dampfbremse ist eine Spezialisierung von `schicht` mit
    fixierter Funktionsklasse.
  - **`dachaufbau`:** das Aggregat **aller** Schichten oberhalb
    des Tragwerks; die Dampfbremse ist **eine** Schicht darin.
  - **`waermedaemmung`:** die wärmedämmende Schicht **aussen** der
    Dampfbremse. Die Dampfbremse schützt sie vor diffundierendem
    Wasserdampf aus dem Innenraum; das verhindert den Tauwasser-
    Ausfall innerhalb der Wärmedämmung am kalten Ende (Glaser).
    Die Dampfbremse ist nicht selbst Wärmedämmung.
  - **`unterdach`:** die zweite wasserführende Ebene **aussen**
    der Wärmedämmung. Liegt zwischen Wärmedämmung und Eindeckung,
    nicht zwischen Innenraum und Wärmedämmung. Funktional und
    geometrisch von der Dampfbremse getrennt.
  - **`eindeckung`:** die äusserste Schicht des Dachaufbaus.
    Die Dampfbremse ist die raumseitige Sicherungsschicht und
    liegt strikt **unter** der Eindeckung in der Schichtfolge.
  - **`dachabdichtung`:** die wasserdichte äusserste Schicht eines
    Flachdachs. Liegt aussen, nicht raumseitig; funktional disjunkt
    von der Dampfbremse.
  - **`dampfsperre`** (Forward-Verweis A, Sub-Variante mit
    sd > 1500 m): die strikt diffusionsdichte Schicht
    (Aluminium-Verbundbahn, Bitumen-Schweissbahn, dicke PE-
    Folie über 1500 m). Eigenständige Klasse nach DIN 4108-3;
    typische Anwendung in Schwimmbad-, Sauna-, Industrie- und
    Beton-Dachaufbauten. Im normalen Holzbau-Wohndach durch
    feuchteadaptive Dampfbremsen funktional überholt (Hersteller-
    Konsens), normativ aber weiter geführt — siehe
    `quellenkonflikt:` (2).
  - **`luftdichtheitsebene`** (Forward-Verweis A, funktional
    getrennte Schicht nach DIN 4108-7): die Schicht, die den
    konvektiven Lufttausch durch Druckdifferenzen verhindert.
    In der Holzbau-Praxis häufig auf derselben Bahn wie die
    Dampfbremse realisiert; bauphysikalisch und definitorisch
    aber getrennt — siehe `quellenkonflikt:` (3).

## Implementierungshinweis

Datentyp (Domänen-Schicht, Kotlin, Schicht `domain.bauteil`):

```
package domain.bauteil

import domain.Toleranzen

/**
 * Dampfbremse als raumseitige diffusionshemmende Schicht
 * des Dachaufbaus. Glossar: hg_dampfbremse.md
 *
 * Sealed-Hierarchie nach Form der sd-Wert-Funktion:
 *   Konventionell  — sd konstant in (φ̄, σ).
 *   Feuchteadaptiv — sd antiton in φ̄, symmetrisch in σ.
 *   Hygrobrid      — sd asymmetrisch in σ.
 */
sealed class Dampfbremse {
    abstract val dachflaechen: List<Dachflaeche>
    abstract val schicht: Schicht          // mit funktion = DAMPFBREMSE
    abstract val sdMin: Double             // m, untere Schranke (>= 0.5)
    abstract val sdMax: Double             // m, obere Schranke (<= 1500.0)

    /** Punktwert der sd-Wert-Funktion in der gegebenen
     *  mittleren relativen Feuchte phi (∈ [0,1]) und auf der
     *  gegebenen Seite. */
    abstract fun sdWert(phi: Double, seite: Seite): Double  // m

    enum class Seite { INNEN, AUSSEN }

    data class Konventionell(
        override val dachflaechen: List<Dachflaeche>,
        override val schicht: Schicht,
        val sdKonst: Double                // m, im Bereich [0.5, 1500.0]
    ) : Dampfbremse() {
        override val sdMin: Double get() = sdKonst
        override val sdMax: Double get() = sdKonst
        override fun sdWert(phi: Double, seite: Seite): Double = sdKonst
    }

    data class Feuchteadaptiv(
        override val dachflaechen: List<Dachflaeche>,
        override val schicht: Schicht,
        override val sdMin: Double,
        override val sdMax: Double,
        // Antitone Funktion phi -> sd(phi); im Code als
        // monotone Tabelle oder Closure realisiert.
        val sdKurve: (Double) -> Double
    ) : Dampfbremse() {
        override fun sdWert(phi: Double, seite: Seite): Double = sdKurve(phi)
    }

    data class Hygrobrid(
        override val dachflaechen: List<Dachflaeche>,
        override val schicht: Schicht,
        override val sdMin: Double,
        override val sdMax: Double,
        val sdKurveInnen: (Double) -> Double,
        val sdKurveAussen: (Double) -> Double
    ) : Dampfbremse() {
        override fun sdWert(phi: Double, seite: Seite): Double = when (seite) {
            Seite.INNEN  -> sdKurveInnen(phi)
            Seite.AUSSEN -> sdKurveAussen(phi)
        }
    }
}

// DIN-4108-3-Klassifikation eines sd-Werts als parametrische
// Funktion (analog klassifiziereNachStauwasser an
// hg_unterdach.md). Hier — und nur hier — sind die
// Schwellenwerte materialisiert.
enum class DiffusionsKlasse { OFFEN, HEMMEND, DICHT }

// Lokale Norm-Aufzählung für Dampfbremsen-Klassifikation. Eindeutiger
// Klassenname analog zu UnterdachNorm (hg_unterdach.md),
// AbdichtungsNorm (hg_dachabdichtung.md) und WaermedaemmungsNorm
// (hg_waermedaemmung.md), um Kollisionen zu vermeiden.
// Folgearbeit-Trigger: sobald mehrere Bauphysik-Module dieselbe
// Norm referenzieren (DIN 4108-3 ist auch in UnterdachNorm und
// WaermedaemmungsNorm geführt), wird ein zentraler hg_norm.md
// angelegt und die lokalen Enums migriert.
enum class DampfbremsenNorm { DIN_4108_3, SIA_180, OENORM_B_8110_2 }

fun klassifiziereNachSdWert(sd: Double, norm: DampfbremsenNorm): DiffusionsKlasse =
    when (norm) {
        DampfbremsenNorm.DIN_4108_3 -> when {
            sd <  0.5    -> DiffusionsKlasse.OFFEN
            sd <= 1500.0 -> DiffusionsKlasse.HEMMEND
            else         -> DiffusionsKlasse.DICHT
        }
        else -> error("DampfbremsenNorm $norm: sd-Schwellen noch nicht hinterlegt.")
    }
```

- **Einheit:** sd-Wert in **Metern** (Double); Schichtdicke der
  Bahn in mm (über `Schicht.dicke` geerbt). Die zwei Einheiten
  sind in der Bauphysik kanonisch (sd in m, Schichtdicke in mm)
  und werden nicht miteinander vermischt.
- **Mittlere relative Feuchte φ̄** als Eingabe der sd-Wert-
  Funktion ist dimensionslos in [0, 1].
- **Trennung Definition ↔ Norm-Schwellen.** Die definitorische
  Bedingung an die Bahn ist
  0,5 m ≤ s_min ≤ s_max ≤ 1500 m. Die konkrete Klassifikation
  eines beliebigen sd-Werts (offen / hemmend / dicht) ist in der
  parametrischen Funktion `klassifiziereNachSdWert(sd, norm)`
  pro Norm materialisiert — analog zur Auslagerung
  normabhängiger Stauwasser-Schwellen in
  `klassifiziereNachStauwasser(h, norm)` an `hg_unterdach.md`.
- **Invarianten** (in `init` jedes Subtyps prüfen, bei Verletzung
  `Resultat.Fehler` bzw. `Entartet`-Variante zurückgeben, niemals
  Exception werfen):
  1. `dachflaechen.isNotEmpty()` ⇒ sonst `Entartet.LeerTraeger`.
  2. `schicht.funktion == SchichtFunktion.DAMPFBREMSE` ⇒ sonst
     `Entartet.FalscheSchichtFunktion`.
  3. `schicht.dicke > Toleranzen.LAENGE_EPS` ⇒ sonst
     `Entartet.NullDickeSchicht`.
  4. `sdMin >= 0.5 - Toleranzen.LAENGE_EPS / 1000.0` (untere
     diffusionshemmende Schranke der DIN 4108-3, sd in m;
     Toleranz auf Mikrometer-Skalenwert) ⇒ sonst
     `Entartet.DiffusionsoffeneBahn`.
  5. `sdMax <= 1500.0 + Toleranzen.LAENGE_EPS / 1000.0` (obere
     Schranke gegen Dampfsperre; sd > 1500 m gehört zu
     `dampfsperre`) ⇒ sonst `Entartet.Diffusionsdicht`.
  6. `sdMin <= sdMax` ⇒ sonst `Entartet.SchrankenVerdreht`.
  7. **Subtyp-spezifisch:**
     - `Konventionell`: `sdMin == sdMax == sdKonst` ⇒ sonst
       `Entartet.NichtKonstant`.
     - `Feuchteadaptiv`: `sdKurve` ist antiton im Sinne von
       φ̄₁ ≤ φ̄₂ ⇒ sdKurve(φ̄₁) ≥ sdKurve(φ̄₂). Wird über eine
       Stichprobe in [0, 1] geprüft (z. B. 11 Stützstellen
       0,0; 0,1; …; 1,0); Verletzung ⇒ `Entartet.NichtAntiton`.
     - `Hygrobrid`: `sdKurveInnen(phi) ≠ sdKurveAussen(phi)` für
       mindestens ein φ̄ ∈ [0, 1]. Verletzung ⇒
       `Entartet.NichtAsymmetrisch` (in diesem Fall wäre der
       korrekte Subtyp `Feuchteadaptiv` oder `Konventionell`).
- **Edge Cases:**
  - **Diffusionsoffene Bahn (sd < 0,5 m, z. B. Unterdachbahn,
    Fassadenbahn):** **keine Dampfbremse**; gehört zur
    diffusionsoffenen Klasse. Wird durch Bedingung 4 abgewiesen
    (`Entartet.DiffusionsoffeneBahn`).
  - **Diffusionsdichte Bahn (sd > 1500 m, z. B. Aluminium-
    Verbundbahn, Bitumen-Schweissbahn):** **keine Dampfbremse**;
    gehört in die Klasse `dampfsperre` (Forward-Verweis A).
    Wird durch Bedingung 5 abgewiesen (`Entartet.Diffusionsdicht`).
  - **Grenzfall sd = 0,5 m oder sd = 1500 m:** beide Werte sind
    inkl. zulässig (DIN 4108-3 fasst die Schranke jeweils
    schliessend, im Glossar wird die Toleranz auf Mikrometer-
    Skala zugelassen, um Floating-Point-Rauschen zu absorbieren).
  - **PE-Folie SD100:** sd ≈ 100 m konstant, Subtyp
    `Konventionell` mit `sdKonst = 100.0`. Im Volksmund oft
    „Dampfsperre" genannt, normativ aber Dampfbremse — siehe
    Erläuterung.
  - **Holzwerkstoffplatte (OSB, Vollholzschalung)** als Schicht
    mit diffusionshemmender Wirkung: kann als `Konventionell`
    mit produkt-spezifischem `sdKonst` (typ. 1–4 m bei 15 mm
    OSB) modelliert werden, wenn ihre `SchichtFunktion`
    DAMPFBREMSE ist; alternativ als `LUFTDICHTHEITSEBENE` oder
    `SCHALUNG` mit dampfhemmender Nebenwirkung — die Wahl der
    Funktionsklasse ist konstruktive Entscheidung.
  - **Sanierungs-Doppelbelegung:** ein Aufbau mit doppelter
    Diffusionssicherung (Bestands-Dampfbremse + neue raumseitige
    Schicht) wird als zwei DAMPFBREMSE-Schichten im selben
    Aufbau modelliert; jede ist eine eigenständige Dampfbremsen-
    Instanz.
  - **Flachdach:** ein Flachdach hat im Regelfall eine
    `dachabdichtung` als alleinige wasserführende Ebene aussen
    und kann zusätzlich eine raumseitige Dampfbremse oder
    Dampfsperre tragen (Warmdach mit Dampfsperre unter der
    Wärmedämmung). Die Dampfbremse ist im Flachdach-Aufbau
    bauphysikalisch zulässig.
- **Abgeleitete Eigenschaften** (als Funktionen, keine Felder):
  - `klasse(norm: DampfbremsenNorm): DiffusionsKlasse` — bei einer
    Dampfbremse stets `HEMMEND`; bei Bahnen, die fälschlich als
    Dampfbremse konstruiert werden, deckt die parametrische
    Klassifikationsfunktion die Inkonsistenz auf.
  - `sdMittelwert(): Double` — arithmetischer Mittelwert der
    sd-Wert-Funktion über [0, 1] (für Feuchteadaptiv und
    Hygrobrid); bei Konventionell trivial `sdKonst`.
  - `istFeuchteadaptiv(): Boolean` — true, wenn der Subtyp
    `Feuchteadaptiv` oder `Hygrobrid` ist.
- **IFC-Mapping** (am API-Rand des IFC-Exporters, nicht im
  Datentyp selbst): `IfcMaterialLayer` mit
  `Category = "VapourBarrier"` (oder `"VapourControlLayer"`);
  sd-Wert über `Pset_MaterialCommon.VaporPermeability` bzw.
  µ-Zahl mit `LayerThickness`. Kein eigenständiges
  `Pset_VapourBarrier` im IFC-Standard 4.3.

## Quellen

**Primär (normativ):**

- DIN 4108-3:2018-10, „Wärmeschutz und Energie-Einsparung in
  Gebäuden – Teil 3: Klimabedingter Feuchteschutz —
  Anforderungen, Berechnungs- und Bemessungsverfahren", Beuth
  Verlag, Berlin.
- DIN 4108-7:2011-01 (Neuausgabe 2026-04), „Wärmeschutz und
  Energie-Einsparung in Gebäuden – Teil 7: Luftdichtheit von
  Gebäuden", Beuth Verlag.
- DIN EN ISO 12572:2025-03, „Wärme- und feuchtetechnisches
  Verhalten von Baustoffen und Bauprodukten — Bestimmung der
  Wasserdampfdurchlässigkeit — Cup-Verfahren".
- DIN EN 13984:2013-05, „Abdichtungsbahnen — Kunststoff- und
  Elastomer-Dampfsperrbahnen — Definitionen und Eigenschaften".
- DIN EN ISO 9972:2018-12, „Wärmetechnisches Verhalten von
  Gebäuden — Bestimmung der Luftdurchlässigkeit von Gebäuden —
  Differenzdruckverfahren" (Abgrenzung Luftdichtheitsebene).
- DIN EN 15026:2007-07, „Wärme- und feuchtetechnisches Verhalten
  von Bauteilen und Bauelementen — Bewertung der Feuchteübertragung
  durch numerische Simulation" (Hintergrund hygrothermische
  Simulation; nicht im Begriff verankert).
- SIA 180:2014, „Wärmeschutz, Feuchteschutz und Raumklima in
  Gebäuden", Schweizerischer Ingenieur- und Architektenverein,
  Zürich.

**Sekundär:**

- Lignum (Hrsg.): *Lignatec — Geneigte Dächer in Holzbauweise.*
  Lignum, Zürich, aktuelle Auflage.
- Mönck, W.; Rug, W.: *Holzbau – Bemessung und Konstruktion.*
  16. Auflage, Beuth Verlag 2015.
- SIA 4001:2022, Wegleitung zur Norm SIA 180.
- Informationsdienst Holz: *Tauwasserschutz im Holzbau.*
- Fraunhofer-Institut für Bauphysik IBP: Anwendungshinweise zu
  DIN EN 15026 (WUFI).
- pro clima Technische Information: INTELLO / INTELLO PLUS,
  DB+ — Produkt-Datenblätter feuchtevariabler sd-Wert.
- SIGA.swiss: Produktdaten Majrex 200 — Hygrobrid-Membran mit
  richtungsabhängigem sd-Wert.
- Isover / Saint-Gobain: Vario KM Duplex UV — Klimamembran.
- ZVDH-Fachregel für Dachdeckungen, Stand 2024.

**Korpus (nicht autoritativ):**

- Recherchebericht
  `docs/recherche/2026-05-14_hg_dampfbremse.md`.
- BauNetz Wissen: „Stoffeigenschaften und Wasserdampfdiffusions-
  widerstand"; „Dampfbremse, Dampfsperre, Luftdichtheit".
- energie-experten.org: „sd-Wert".
- ifb.info: „Neuauflage Teil 3 der DIN 4108".
- DIN-NABau: „Auslegungen zu DIN 4108-3".
- Wikipedia, Lemmata „Dampfbremse", „sd-Wert", „Klimamembran"
  (abgerufen 2026-05-14).
