---
id: balkenlage
benennung: Balkenlage
kurz: "Eine Balkenlage ist das tragende Gerippe einer Holzdecke aus mehreren waagrechten Balken, die parallel nebeneinander liegen und oben genau auf einer Höhe abschließen, damit der Fußboden eben aufliegt, samt den Querhölzern, die an einer Öffnung für Treppe oder Kamin die unterbrochenen Balken abfangen."
synonyme: [Tramlage, "floor frame"]
abgelehnte_benennungen: [Holzbalkendecke, Balkendecke, Tramdecke, Gebälk, Deckentragwerk]
oberbegriff: bauteilgruppe
begriffstyp: aggregat
voraussetzungen:
  [bauteilgruppe, deckenbalken, wechsel, bauteil, bauteilachse,
   ebene, bezugsebene, einheitsvektor, weltkoordinatensystem,
   lokales_koordinatensystem, polyeder, uuid, toleranzen]
abgrenzung_zu:
  [bauteilgruppe, deckenbalken, wechsel, stichbalken, auswechslung,
   randbalken, unterzug, kehlbalken, kehlbalkenlage, holzbalkendecke,
   tragwerk, deckentragwerk, bausystem, wand, einbinder, stockschwelle,
   lage]
status: entwurf
subglossar_pendant: notwendig
quellen_primär:
  - "ISO 16739-1:2024 'Industry Foundation Classes (IFC) for data sharing in the construction and facility management industries — Part 1: Data schema' (IFC 4.3), `IfcElementAssemblyTypeEnum.BEAM_GRID`: 'Interconnected beams, located in one (typically horizontal) plane.' — Abbildungsziel der Balkenlage als `IfcElementAssembly` (Aggregation über `IfcRelAggregates`, siehe `hg_bauteilgruppe.md`); dazu für die Glieder `IfcBeamTypeEnum.JOIST`: 'A beam used to support a floor or ceiling.' Wortlaut im buildingSMART-Quelltext auf GitHub (Repository IFC4.3.x-development, Branch master) am 2026-11-14 bestätigt; die HTML-Fassung auf standards.buildingsmart.org stand hinter einer Bot-Prüfung und wurde nicht geöffnet. [direkt]"
  - "DIN 18334 (VOB Teil C, Zimmer- und Holzbauarbeiten), Abrechnung: „Auswechselungen z.B. Kamine, Treppen, Dachflächenfenster, Dachausstiegen“ nach Anzahl (Stück). Stützt nur die Folgearbeit Auswechslung als zählbare, verschachtelte Bauteilgruppe, nicht die Definition der Balkenlage. [via: Bläsi/Ferdinand, Tabellenbuch Zimmerer, 9. Aufl. 2021, S. 270]"
quellen_sekundär:
  - "Volmer, L.; Zimmermann, W. H. (Hrsg.): Glossary of Prehistoric and Historic Timber Buildings / Glossar zum prähistorischen und historischen Holzbau. Studien zur Landschafts- und Siedlungsgeschichte im südlichen Nordseegebiet 3, NIhK / Verlag Marie Leidorf, Rahden 2012, ISBN 978-3-86757-333-7. Nr. 2.6.2 „Balkenlage“ (S. 207): „Konstruktives → Gebinde (2.3.11) aus horizontal verlegte [sic] Balken, die in einer Ebene in bestimmten Abständen verlegt sind. Bei einer regelmäßigen Balkenlage liegen die Balken parallel meist in Querrichtung, beim verschossenen Gebälk liegen sie in verschiedenen Teilen des Gebäudes in wechselnden Richtungen. […] Die Hölzer können unterschiedliche Maße (Stärken und Längen) besitzen“; deutsche Zeile „> Kehlbalkenlage“ und „~ Gebälk (imprecise / ungenau)“, englisch „floor frame“, „joisting“. Dazu Nr. 2.6.3 „verschossenes Gebälk“ (S. 207), 2.6.13 „Balkendecke“, 2.6.21 „Unterzug“ (S. 216), 2.6.22 „Überzug“, 2.6.25 „Stichbalken“ (S. 218), 2.6.33 „Wechsel“ (S. 221); Bedeutungszeichen S. 44."
  - "Hölder-Pichler-Tempsky (HPT): Fachkunde Zimmerer 2, Kap. 1 „Holzdecken“, Leseprobe lp.hpt.at/LP_22256.pdf, Buch-S. 5: „Wird eine Deckenkonstruktion in Holz ausgeführt, so spricht man von einer Tram- oder Balkenlage.“ Arten nach der Lage im Gebäude: „1.1 Kehlbalkenlagen […] 1.2 Dachbalkenlagen […] 1.3 Geschoßbalkenlagen“. S. 6: „Der Tramabstand soll je nach Belastung und Spannweite im Bereich zwischen 50 cm bis maximal 90 cm liegen.“ S. 7, Bild „Benennung der einzelnen Teile einer Tramdecke“: Tram, Stichbalken, Wechsel, Füllholz, Ortbalken, „Tramabstand 60 - 100cm“. Autoren, Auflage und ISBN stehen nicht in der Leseprobe."
  - "Saint-Gobain Rigips: Technik aktuell Nr. 02/12 „Innendämmung bei Holzbalkendecken“, 31.05.2012, S. 3: „Eine Balkenlage bezeichnet dabei die Gesamtheit aller tragenden und in einer Ebene liegenden Holzbalken.“ und „Als Holzbalkendecke wird eine, in einer horizontalen Ebene liegende, Balkenlage bezeichnet“; S. 4: „Die Balkenabstände liegen zwischen 0,40 m und 1,30 m.“"
  - "Bläsi, W.; Ferdinand, S.: Tabellenbuch Zimmerer. 9. Aufl., Bildungsverlag EINS, Köln 2021, ISBN 978-3-427-02144-5, S. 131 (Teilung der Balkenlage: Σe = l − 2·2 cm − b; n_F = Σe / e_max aufgerundet; n_Balken = n_F + 1; e_vorh = Σe / n_F), S. 159 (Holzbalkendecke als Deckenart, Skizze einer Einschubdecke mit Boden, Einschub und Schlackenbeton), S. 161 (Fachwerk-Legende „⑪ Deckenbalken“), S. 270 (DIN 18334, Auswechselungen nach Stück)."
  - "Degiuli, F.: „Auswechselungen in Holzbalkendecken“, mb-news 3/2019, S. 32–36 (mb AEC Software), S. 32: „Auswechselungen werden im Holzbau gebraucht, um Öffnungen in Balkenlagen realisieren zu können.“ und „Der Wechsel ist rechtwinklig zur Balkenlage angeordnet und ist an den nächsten durchlaufenden Balken (Wechselbalken) befestigt.“"
  - "Kolb, J.; Kolb, H.; Müller, A.: Holzbau mit System. Tragkonstruktion und Schichtaufbau der Bauteile. 4. Aufl., Birkhäuser, Basel 2024, hg. mit Lignum – Holzwirtschaft Schweiz, ISBN 978-3-0356-2644-5, S. 41 („Balkenlage“, „Balkenlage mit flächiger Tragschicht“ als Deckensysteme), S. 113, 116, 117, 121 (Deckenscheibe, Lastverteilung auf die aussteifenden Wände), S. 121 (Scheiben „müssen umlaufend mit einem Randbalken ausgebildet werden. Parallel zur Spannrichtung wirken diese als Randgurte, rechtwinklig zur Spannrichtung als Auflagerbalken.“), S. 160 („Abstand der Balken: 500 bis 700 Millimeter, in der Regel 625 Millimeter“), S. 295 („Sparrendach mit Kehlbalken, Balkenlage und Aufschiebling“), S. 311 („Balkenlage C24/GL24 ohne Verbindung mit der oberen Beplankung“), S. 413 („Rohdecken 1 Balkenlage …“)."
  - "Colling, F.: Holzbau — Grundlagen und Bemessung nach EC 5. 7. Aufl., Springer Vieweg, Wiesbaden 2021, ISBN 978-3-658-34446-7, S. 78: Holzbalkendecke aus Deckenbalken und Schalung, „aber ‚den einzelnen Deckenbalken‘ gibt es meistens gar nicht“ (Querverteilung über die Schalung)."
  - "Esselborn, K. (Hrsg.): Lehrbuch des Hochbaues, Bd. 1, Leipzig 1908, Kap. III „Holzkonstruktionen“ von K. Stief, S. 194: Achsmaß der Balkenlage, „ungefähre Entfernung von Mitte zu Mitte von 0,60 bis 0,75 m“; S. 194–195, Abb. 102–110: Wechsel mit Brustzapfen, Oberkante bündig (aus den Abbildungen gelesen). Digitalisat UB Paderborn, urn:nbn:de:hbz:466:1-50294."
  - "Colling, F.; Kessel, M. H.; Sieder, M.; Janßen, P.: „Bemessung von aussteifenden Deckentafeln“, holzbau technik 9/2019: Abstand der Deckenbalken 0,625 m bzw. 0,833 m (Raster der Plattenbreiten); „durchgehende Kopfrippe der Traufwand“."
  - "Wikipedia, Lemma „Holzbalkendecke“ (de.wikipedia.org/wiki/Holzbalkendecke), abgerufen 2026-11-14: „eine Geschossdecke mit tragenden Elementen aus Holz in Form von gesägten oder behauenen (Decken-)Balken, die Balkenlage“."
  - "DWDS, Lemma „Gebälk“ (eWDG 1967), abgerufen 2026-11-14: „sämtliche Balken eines Bauwerkes, besonders des Dachstuhles“."
  - "Recherche-Bericht: [intern] (§B, §D, §F, §G.3, §H, §I.2)."
quellenkonflikt: |
  Elf Punkte. Grundlage ist Anweisers Entscheid vom 14.11.2026 für
  Weg A aus dem Recherche-Bericht §I.2.

  **(1) Norm-Lücke, IFC als einziger normativer Anker.** Keine
  zugängliche Norm definiert „Balkenlage" (Recherche §B.1).
  DIN EN 1995-1-1 und DIN 1052 sind nicht im Volltext geprüft
  (Verlag). Colling bemisst Deckenbalken nach EC 5, ohne Balkenlage
  oder Deckenbalken zu definieren; eine Normdefinition ist daher
  unwahrscheinlich, aber nicht ausgeschlossen (negativer Befund,
  nicht gesichert). SIA 265 ist nicht geprüft. Normativ greifbar ist
  nur ISO 16739-1 mit `BEAM_GRID` („Interconnected beams, located in
  one (typically horizontal) plane."), fast wörtlich gleich Volmer
  2.6.2. IFC sagt „typically horizontal", dieser Eintrag verlangt die
  waagrechte Ebene (Bedingung 2). Das ist eine Verengung: Eine
  geneigte Lage paralleler Stäbe liegt in einer Dachfläche und ist
  im Glossar eine Lage von Sparren (`sparren`), keine Balkenlage.
  Die Definition stützt sich damit auf Volmer (wissenschaftliches
  Glossar), HPT, Rigips und IFC. Ihr gemeinsamer Kern: waagrechte
  Balken in einer Ebene, in Abständen verlegt.

  **(2) Balkenlage oder Holzbalkendecke.** Zwei gleichrangige
  Lesarten (Recherche §D.3). HPT S. 5 („Deckenkonstruktion in Holz
  … Tram- oder Balkenlage") und Rigips S. 3 („Als Holzbalkendecke
  wird eine, in einer horizontalen Ebene liegende, Balkenlage
  bezeichnet") setzen beide Wörter gleich. Wikipedia, Volmer 2.6.13
  („Balkendecke"), Tabellenbuch S. 159 und Colling S. 78 führen die
  Decke als Bauteil mit allen Schichten und die Balkenlage als ihren
  tragenden Teil. Kolb stützt die zweite Lesart für die Schweiz:
  S. 311 „Balkenlage … ohne Verbindung mit der oberen Beplankung",
  S. 413 „Rohdecken 1 Balkenlage …" (nur Textausschnitte).
  Entscheid Anweiser: Holzbalkendecke ⊃ Balkenlage. „Holzbalkendecke",
  „Balkendecke" und „Tramdecke" bezeichnen das Bauteil mit allen
  Schichten und stehen in `abgelehnte_benennungen:`;
  `holzbalkendecke` steht zugleich in `abgrenzung_zu:` (Folgearbeit,
  Schichtaufbau analog `dachaufbau`).

  **(3) Kehlbalkenlage: der Eintrag ist enger als der
  Sprachgebrauch.** Volmer führt „> Kehlbalkenlage" unter der
  Balkenlage, also mit eingeschränktem Bedeutungsumfang (Zeichen „>"
  nach S. 44). HPT S. 5 zählt die Kehlbalkenlagen als Art 1.1 der
  Balkenlagen. In Weg A sind nur Deckenbalken und Wechsel Glieder.
  Kehlbalken tragen die Rolle Kehlbalken (`hg_kehlbalken.md`, am
  Sparrenpaar angeschlossen) und gehören nicht dazu. Eine
  Kehlbalkenlage ist nach diesem Eintrag also **keine** Balkenlage.
  Das weicht von Volmer und HPT ab und bleibt offen. Ihre Aufnahme
  als Unterbegriff `kehlbalkenlage` ist Folgearbeit. Weil ein
  Unterbegriff keine Glieder haben kann, die der Oberbegriff
  ausschließt, muss diese Folgearbeit Bedingung 1 um die Rolle
  Kehlbalken erweitern. Das Gleiche gilt für die Dachbalkenlage
  (HPT 1.2), falls ihre Balken als Zugglied des Sparrendachs später
  die Rolle `bundbalken` erhalten (Recherche §H Nr. 4 und 5);
  solange sie Deckenbalken sind, ist sie eine Balkenlage im Sinne
  dieses Eintrags. Die Geschoßbalkenlage (HPT 1.3) ist der Regelfall.
  Kolb S. 295 nennt „Kehlbalken, Balkenlage" nebeneinander; ob Kolb
  die Kehlbalken zur Balkenlage zählt, geht aus dem Textausschnitt
  nicht hervor.

  **(4) Regelmäßige Balkenlage und verschossenes Gebälk.** Nach
  Volmer liegen die Balken nur in der **regelmäßigen** Balkenlage
  parallel. Das verschossene Gebälk (2.6.3) mit wechselnden
  Richtungen und die diagonal oder radial verlegte Zerrbalkenlage
  sind dort ebenfalls Balkenlagen. Bedingung 3 ist nach Anweisers
  Entscheid hart und verengt den Begriff auf die regelmäßige
  Balkenlage. Ein verschossenes Gebälk wird als mehrere
  Balkenlagen mit derselben Bezugsebene modelliert; nichts im
  Eintrag verbietet zwei Balkenlagen dieselbe Höhe z_L. Vorläufig
  gilt das auch für Stichbalken einer Vorkragung, die quer zu den
  Hauptbalken liegen (Volmer 2.6.25, Bedeutung 1). Eine Gruppe, die
  solche Balkenlagen zusammenfasst, ist Folgearbeit.

  **(5) Benennungen.** „Balkenlage" ist in Deutschland (Volmer,
  Tabellenbuch S. 131, mb-news, Rigips, Esselborn), Österreich (HPT,
  neben „Tramlage") und der Schweiz (Kolb S. 41, 295, 311, 413)
  gleich belegt. Ein eigenes Schweizer Synonym ist nicht gefunden.
  „Tramlage" (Österreich) nach HPT S. 5. „floor frame" nach Volmer
  2.6.2; Volmers zweites englisches Wort „joisting" ist nicht
  übernommen (Anweisers Entscheid nennt nur „floor frame"). Abgelehnt:
  „Gebälk", weil Volmer es als ungenau markiert („~ Gebälk
  (imprecise / ungenau)") und DWDS es für „sämtliche Balken eines
  Bauwerkes, besonders des Dachstuhles" führt; „Deckentragwerk",
  weil `hg_tragwerk.md` darunter eine künftige Spezialisierung des
  Tragwerks versteht, also eine nicht exklusive Sicht
  (`bausystem`). Die Klammer „(Balkenlage, BSP-Decke,
  Holz-Beton-Verbunddecke)" dort nennt Beispiele, keine
  Typgleichheit. Eine Balkenlage kann zugleich Bauteilgruppe und
  Teil eines Deckentragwerks sein (`hg_bausystem.md`, Edge Case
  „Mitgliedschaft … in einer Bauteilgruppe und in einem Bausystem
  gleichzeitig"). Daher steht `deckentragwerk` nach
  HG_KONVENTIONEN §5a zugleich in `abgrenzung_zu:`. Homonym: „Lage"
  ist in `hg_lage.md` die Brett- oder Furnierlage im Mehrlagenholz;
  eine Balkenlage ist keine Lage in diesem Sinn. Das Feld für die
  Starrkörper-Platzierung heißt hier deshalb `platzierung` (in
  `hg_bauteilgruppe.md`: `lage`).

  **(6) Exklusive Mitgliedschaft und Auswechslung (Recherche
  §D.8).** Heute sind die Wechsel direkte Glieder der Balkenlage.
  `hg_bauteilgruppe.md` plant die Auswechslung als eigene
  Bauteilgruppe; DIN 18334 rechnet sie nach Stück ab. Konfliktfrei
  mit der exklusiven Mitgliedschaft (Bedingung 1 von
  `bauteilgruppe`) ist nur diese Verschachtelung: Die Auswechslung
  ist eine Bauteilgruppe innerhalb der Balkenlage und enthält nur
  Wechsel und Stichbalken. Der durchlaufende Nachbarbalken (bei
  mb-news „Wechselbalken"; in der Schweiz heißt so der Wechsel
  selbst, siehe `hg_wechsel.md`) bleibt direktes Glied der
  Balkenlage. Sonst
  gehörte ein Nachbarbalken zwischen zwei Öffnungen zu zwei
  Auswechslungen. mb-news rechnet ihn statisch zur Auswechselung;
  das ist eine Tragwerkssicht (`bausystem`), keine
  Gruppenmitgliedschaft. **Folgearbeit `auswechslung`, Trigger:
  erste Öffnung (Treppe, Kamin) im Simulator.** Mit ihr beziehen
  sich die Bedingungen 2 bis 4 sowie Z1 und Z2 auf die Glieder
  einschließlich der Glieder verschachtelter Auswechslungen.

  **(7) Unterzug.** Volmer 2.6.21: „Tragendes Holz, das eine
  Balkenlage unterstützt und so deren Spannweite verringert.
  Verläuft immer unterhalb der eigentlichen Balkenlage". Der
  Unterzug ist Auflager der Deckenbalken, kein Glied; dasselbe gilt
  für den Überzug (2.6.22) und den Streichbalken in Volmers Sinn
  als Auflager (2.6.19). Ausgeschlossen sind sie durch die Rolle
  (Bedingung 1) und, weil ihre Oberkante nicht auf z_L liegt, auch
  geometrisch (Bedingung 2b). **Folgearbeit `unterzug` (steht im
  Folgewellen-Plan), Trigger: erste Balkenlage mit
  Zwischenauflager.**

  **(8) Lesart der Bedingungen aus Recherche §D.7.** Anweisers
  Entscheid: Punkte 1 bis 4 hart, Punkt 5 weich. Beim Formalisieren
  sind drei Stellen präzisiert, Bestätigung durch Anweiser offen:
  (a) Punkt 1 „mindestens zwei Glieder" ist hier „mindestens zwei
  Deckenbalken". Volmer spricht von Balken „in bestimmten
  Abständen", Rigips von der „Gesamtheit aller … Holzbalken", und
  ein Achsabstand (Punkt 5) braucht zwei Balken. Eine Gruppe nur
  aus Wechseln oder aus einem Balken und einem Wechsel ist keine
  Balkenlage. (b) Punkt 2 „Die Oberkanten aller Glieder liegen …
  in E_L" ist gelesen als: Bauteilachse waagrecht (2a) und höchster
  Punkt auf der Höhe z_L (2b). Für einen geraden Stab heißt „die
  Oberkante liegt in einer waagrechten Ebene" genau das. Belege:
  Volmer („horizontal verlegte Balken"), Esselborn (Wechsel mit
  Brustzapfen, Oberkante bündig, aus den Abbildungen gelesen,
  Recherche §E.6). Für Wechsel in
  einer Decke folgt 2a aus der Lage der Oberseite (`wechsel`,
  Satz 2 (i)) und bleibt hier als eigene Vorprüfung stehen; im Dach
  folgt die waagrechte Achse des Wechsels nur dann aus der
  Geometrie, wenn die Sparren in der Falllinie liegen (`wechsel`,
  Satz 2 (ii); Recherche §E.6 Punkt 3). (c) Punkt 3 hatte die Form |⟨a_i, a_j⟩| ≥ 1 − ε_W. Hier
  ist er nach HG_KONVENTIONEN §4 als Kreuzprodukt-Test mit
  `KOLLINEAR_EPS` geschrieben (Parallelitäts-Prädikat), Punkt 4 und
  2a als Lage-Prädikate ebenfalls mit `KOLLINEAR_EPS` (Vorbild
  `hg_wand.md`, `hg_stockschwelle.md`). Beide Konstanten haben
  denselben Standardwert.

  **(9) Randbalken und Deckenscheibe (Entscheid Anweiser
  2026-11-14).** Die Deckenscheibe ist die Decke in ihrer Wirkung
  als waagrechte Scheibe, die Horizontallasten auf die aussteifenden
  Wände verteilt (Kolb S. 113, 116, 117, 121). Kolb S. 121: Scheiben
  „müssen umlaufend mit einem Randbalken ausgebildet werden.
  Parallel zur Spannrichtung wirken diese als Randgurte, rechtwinklig
  zur Spannrichtung als Auflagerbalken." „Randbalken" ist also ein
  Wort der Scheiben-Statik und meint den ganzen umlaufenden Rand.
  Festlegung: Längs der Spannrichtung ist der Randbalken (Randgurt)
  ein Deckenbalken in der Lage RAND (`deckenbalken`), also Glied der
  Balkenlage; er liegt parallel zu den übrigen Deckenbalken und
  erfüllt Bedingung 3. Quer zur Spannrichtung ist er Auflagerbalken:
  kein Deckenbalken (Entscheid Anweiser) und kein Wechsel (Recherche
  §C.3; `wechsel`, Bedingung 4), nach Bedingung 1 also kein Glied
  der Balkenlage, und Bedingung 3 betrifft ihn nicht. Für ihn folgt
  der eigene Eintrag `randbalken`; ob er dann Glied wird (Erweiterung
  von Bedingung 1 wie bei der Kehlbalkenlage, Punkt 3), entscheidet
  jener Eintrag. „Kopfrippe" (Colling u. a. 2019, „durchgehende
  Kopfrippe der Traufwand") steht nur als Hinweis: ein einziger,
  nicht nachgeprüfter Fundort, Anweiser kennt das Wort nicht.

  **(10) Zuordnung der Glieder zu ihren Rollen (Kohärenzprüfung
  2026-11-14).** Der Entwurf von `hg_deckenbalken.md` verlangte als
  Bedingung, dass ein Deckenbalken Glied genau einer Balkenlage ist
  und dort nicht als Wechsel geführt wird; dieser Eintrag bestimmt
  seine Glieder über die Rolle Deckenbalken. Das war ein Zirkel.
  Festlegung: Die Gliedschaft ist keine Bedingung der Rolle, sondern
  die Zuordnungsprüfung Z1 bis Z3 dieses Eintrags, so wie `wechsel`
  seine Stablage nicht selbst bestimmt. Z1 und Z2 halten fest, dass
  die Oberkantenebene E der Deckenbalken, die Bezugsebene E_L und die
  Ebene E_Λ der Stablage, in der die Wechsel liegen, dieselbe Ebene
  sind: E = E_L = E_Λ. Z3 übernimmt die frühere Bedingung des
  Deckenbalkens. Bestätigung durch Anweiser offen.

  **(11) Einsicht.** IFC: Quelltext auf GitHub, siehe
  `quellen_primär:`. Volmer: frei verfügbares PDF; Nr. 2.6.2 ist
  wörtlich an der Quelle bestätigt, die übrigen
  Nummern sind im Volltext gelesen. HPT:
  Leseprobe im Volltext, S. 6 wörtlich
  bestätigt, S. 5 und 7 gelesen. mb-news: Volltext;
  der Satz zum Wechsel am durchlaufenden Balken ist bestätigt. Rigips, Esselborn, Colling u. a. 2019,
  Wikipedia, DWDS: Volltext gelesen. Tabellenbuch
  S. 131, 159, 161, 270: Seitenbild des lokalen Scans; S. 159 ist
  aus der Skizze gelesen. Colling S. 78: nur OCR-Text. Kolb: nur
  Textausschnitte der Suche im Buch bei Google Books, Kontext der
  Ausschnitte nicht geprüft.
---

## Prosa-Definition

Eine **Balkenlage** ist eine Bauteilgruppe aus mindestens zwei
zueinander parallelen Deckenbalken und einer möglicherweise leeren
Menge von Wechseln, die rechtwinklig zu den Deckenbalken liegen und
an ihnen anschließen, wobei die Bauteilachsen aller Glieder
waagrecht verlaufen und ihre Oberkanten, also die jeweils höchsten
Punkte der Bauteile, in einer gemeinsamen waagrechten Bezugsebene
liegen.

## Mathematische Definition

Sei

- e_z:= (0, 0, 1) der lotrecht nach oben zeigende Einheitsvektor
  des Weltkoordinatensystems (siehe `weltkoordinatensystem`,
  `einheitsvektor`),
- 𝓑 die Menge aller Bauteile im Sinne von `bauteil` und
  G_W(b) ⊂ ℝ³ die Punktmenge des Bauteils b im
  Weltkoordinatensystem (der Index W steht wie in `bauteilgruppe`
  nur für „Welt“),
- 𝓑_DB, 𝓑_WE ⊂ 𝓑 die Bauteile mit der Bauteilrolle `deckenbalken`
  bzw. `wechsel`,
- für b ∈ 𝓑 a(b) = (p_a(b), p_e(b)) die Bauteilachse und
  d_hat_b:= (p_e(b) − p_a(b)) / ‖p_e(b) − p_a(b)‖ ihr
  Richtungs-Einheitsvektor (siehe `bauteilachse`),
- 𝒰 der UUID-Raum nach `uuid` und 𝒢_huelle die Menge der
  zulässigen Hüllgeometrien einer Bauteilgruppe (siehe
  `bauteilgruppe`, `polyeder`),
- ε_K:= Toleranzen.KOLLINEAR_EPS, ε_L:= Toleranzen.LAENGE_EPS.

Für jedes Bauteil b ∈ 𝓑 ist die **Oberkantenhöhe** die abgeleitete
Größe

```
z_OK(b):= max { ⟨e_z, p⟩ | p ∈ G_W(b) }        (in mm)          (1)
```

Dann ist eine **Balkenlage** ein Tupel

```
L:= (uuid, deckenbalken, wechsel, z_L, platzierung, huelle,
      funktion?, bezeichnung?)
```

mit

- **uuid** ∈ 𝒰: technischer Surrogatschlüssel der Balkenlage
  (Pflicht, persistent, RFC 9562 v7); externe Referenzen gehen auf
  diese UUID (Aggregat-Wurzel nach `bauteilgruppe`).
- **deckenbalken** ⊂ 𝓑_DB, |deckenbalken| ≥ 2: die Deckenbalken
  der Balkenlage, einschließlich verkürzter Balken an Wechseln.
- **wechsel** ⊂ 𝓑_WE, |wechsel| ≥ 0: die Wechsel der Balkenlage.
  Muss die Balkenlage genannt werden, heißen die beiden Gliedmengen
  deckenbalken(L) und wechsel(L) (so in `deckenbalken`).
- **z_L** ∈ ℝ: die Höhe der Bezugsebene in mm. Die **Bezugsebene**
  der Balkenlage ist
  ```
  E_L:= { x ∈ R³ | ⟨e_z, x⟩ = z_L }                              (2)
  ```
  in Hesse-Normalform (e_z, z_L) nach `ebene`. Sie hat die Form von
  `bezugsebene` Gleichung (1); ihr Kontext ist die Balkenlage, nicht
  ein Tool.
- **platzierung** ∈ SE(3): die Starrkörpertransformation, die das
  lokale Koordinatensystem der Balkenlage ins Weltkoordinatensystem
  überführt (Feld `lage` von `bauteilgruppe`, siehe
  `lokales_koordinatensystem`).
- **huelle** ∈ 𝒢_huelle: die Hülle der Balkenlage im lokalen
  Koordinatensystem.
- **funktion?**: optionale Klassifikation; die Wertemenge ist offen.
- **bezeichnung?**: optionaler Name, etwa „Balkenlage über EG".

und den Konsistenzbedingungen 1 bis 4 und der Zuordnungsprüfung Z1
bis Z3 (hart):

1. **Bauteilgruppen-Konformität und Rollen.** Mit
   ```
   bestandteile:= deckenbalken ∪ wechsel
   ```
   erfüllt das Tupel (uuid, bestandteile, platzierung, huelle,
   funktion?, bezeichnung?) die Bedingungen 1 bis 4 von
   `bauteilgruppe` (exklusive Mitgliedschaft, Lebenszyklus-Bindung,
   Hüllen-Inklusion, azyklische Verschachtelung). Glieder mit einer
   anderen Bauteilrolle sind nicht zulässig. Aus
   |deckenbalken| ≥ 2 folgt |bestandteile| ≥ 2.

2. **Gemeinsame waagrechte Bezugsebene.** Für alle
   b ∈ bestandteile gilt
   ```
   (2a)  |⟨d_hat_b, e_z⟩| ≤ ε_K          (Bauteilachse waagrecht)
   (2b)  |z_OK(b) − z_L| ≤ ε_L           (Oberkante in E_L)
   ```

3. **Regelmäßige Balkenlage.** Alle Deckenbalken sind parallel:
   ```
   ‖d_hat_b × d_hat_c‖ ≤ ε_K     für alle b, c ∈ deckenbalken
   ```

4. **Wechsel rechtwinklig zu den Deckenbalken.**
   ```
   |⟨d_hat_q, d_hat_b⟩| ≤ ε_K    für alle q ∈ wechsel, b ∈ deckenbalken
   ```

**Zuordnungsprüfung** (hart; Verträglichkeit der Glieder mit ihren
Rollen). Sie macht ausdrücklich, was „Glied mit der Rolle
Deckenbalken bzw. Wechsel" in dieser Balkenlage heißt, und bindet
die Ebene, auf die sich `deckenbalken` und `wechsel` beziehen, an
die Bezugsebene:

- **Z1. Deckenbalken in der Bezugsebene.** Jedes b ∈ deckenbalken
  erfüllt die Bedingungen 1 bis 3 von `deckenbalken` bezüglich der
  Oberkantenebene E:= E_L.
- **Z2. Wechsel in der Stablage der Deckenbalken.** Für ein
  b_0 ∈ deckenbalken sei
  ```
  Λ_L:= (S_Λ, a_hat_Λ, E_Λ):= (deckenbalken, d_hat_b0, E_L)     (3)
  ```
  die **Stablage der Balkenlage** im Sinne von `wechsel`. Jedes
  q ∈ wechsel ist ein Wechsel in der Stablage Λ_L (`wechsel`,
  Bedingungen 1 bis 4).
- **Z3. Gliedschaft, modellweit.** Jedes Bauteil des Modells mit
  der Bauteilrolle Deckenbalken ist Glied genau einer Balkenlage.
  „Höchstens eine" folgt aus der exklusiven Mitgliedschaft
  (Bedingung 1), „mindestens eine" prüft der Modell-Container.
  Zugleich in deckenbalken und in wechsel kann ein Bauteil nicht
  stehen, weil es genau eine Bauteilrolle trägt.

**Gleichsetzung der Ebenen.** Nach Z1 und Z2 gilt

```
E = E_L = E_Λ                                                     (4)
```

Die Oberkantenebene jedes Deckenbalkens (`deckenbalken`,
Bedingung 3), die Bezugsebene der Balkenlage und die Ebene der
Stablage, in der die Wechsel liegen (`wechsel`, Bedingung 3), sind
eine einzige Ebene.

Weiche Bedingung (Warnung, kein Fehler):

5. **Achsabstand.** Jedes b ∈ deckenbalken wird nach der weichen
   Regel 6 von `deckenbalken` geprüft: Achsabstand zum nächsten
   parallelen Deckenbalken dieser Balkenlage, Warnung über
   `DECKENBALKEN_ACHSABSTAND_MAX_MM`. Definition des Achsabstands und
   Wert stehen nur dort (Tabelle „Werte" in `deckenbalken`); die
   Balkenlage führt keine eigenen und sammelt nur die Warnungen ihrer
   Deckenbalken.

Die **geometrische Punktmenge** der Balkenlage im
Weltkoordinatensystem ist wie bei `bauteilgruppe` die transformierte
Hülle G_W(L):= platzierung(G_lokal(huelle)) ⊂ ℝ³.

## Wohldefiniertheit

- **Existenz**: Zwei parallele Deckenbalken mit waagrechter Achse
  und gleicher Oberkantenhöhe z_L, wechsel = ∅, Hülle als
  achsenparalleler Hüllquader der beiden Bauteile, platzierung =
  Identität: Die Bedingungen 1 bis 4 und Z1 sind erfüllt, wenn beide
  Deckenbalken ihre Rollenbedingungen bezüglich E_L erfüllen; Z2 ist
  leer erfüllt; Z3 gilt, wenn das Modell keine weiteren Deckenbalken
  enthält. Bedingung 5 hat genau einen Achsabstand oder keinen
  (siehe Edge Cases).
- **Oberkantenhöhe (1)**: G_W(b) ist als Punktmenge eines
  Bauteilkörpers beschränkt und abgeschlossen (siehe `polyeder`),
  ⟨e_z, ·⟩ ist stetig, also existiert das Maximum. z_OK(b) wird im
  Weltkoordinatensystem berechnet und hängt daher nicht vom lokalen
  Koordinatensystem des
  Bauteils ab. Für einen waagrechten Stab mit aufrecht stehendem
  Rechteckquerschnitt gilt z_OK(b) = z_B + h_B / 2; das ist die
  Oberkante, die `hg_stockschwelle.md` für die Stockschwelle
  verwendet. Abtragende Bearbeitungen an der Oberseite (etwa der
  Kamm für eine verkämmte Stockschwelle) ändern z_OK nicht, solange
  ein Teil der Oberseite stehen bleibt.
- **Unabhängigkeit von der Achsorientierung**: Die Bedingungen 2a,
  3 und 4 verwenden nur |⟨·,·⟩| und ‖· × ·‖. Sie sind invariant
  unter d_hat_b → −d_hat_b, also unabhängig von der Wahl von p_a und
  p_e (Vorzeichenkonvention von `bauteilachse`).
- **Bezugsebene bis auf Toleranz eindeutig**: z_L ist ein Feld. Wenn
  zwei Höhen z_L und z_L' Bedingung 2b für dieselben Glieder
  erfüllen, gilt |z_L − z_L'| ≤ 2·ε_L. Die Glieder legen die
  Bezugsebene also bis auf Toleranz fest; das Feld bestimmt den
  Vertreter. Wird z_L aus den Gliedern bestimmt, empfiehlt sich
  z_L:= max { z_OK(b) | b ∈ bestandteile }; das ist unabhängig von
  der Reihenfolge der Glieder.
- **Stablage (3) wohldefiniert**: Λ_L ist eine Stablage im Sinne
  von `wechsel`. deckenbalken hat mindestens zwei Stäbe mit gerader
  Achse; nach Bedingung 3 gilt ‖d_hat_b × a_hat_Λ‖ ≤ ε_K für alle
  b ∈ deckenbalken; E_L hat die nach oben zeigende Normale e_z mit
  ⟨e_z, e_z⟩ = 1 > ε_K und enthält die Stabrichtung bis auf ε_K
  (2a); jeder Deckenbalken hat nach Z1 eine Längsseite mit Normale
  e_z in E_L, also eine Oberseite in E_Λ; und kein Wechsel liegt in
  S_Λ (Z3). Die Wahl von b_0 ändert a_hat_Λ wegen Bedingung 3 nur in
  der Toleranzordnung ε_K, und `wechsel` verwendet a_hat_Λ nur über
  |⟨·,·⟩| und ‖· × ·‖, also auch nicht über sein Vorzeichen.
- **Gleichsetzung (4)**: E = E_L ist Z1, E_Λ = E_L ist Z2. Für die
  Deckenbalken folgt 2b aus Z1: Nach `deckenbalken` Bedingung 3
  liegt kein Punkt über z_L + ε_L, und die Eckpunkte der Oberseite
  liegen nicht tiefer als z_L − ε_L. Für die Wechsel bleibt 2b eine
  eigene Forderung, weil `wechsel` nur die Lage der Oberseite
  verlangt. Im Modell übergibt die Balkenlage E_L als Ebene an beide
  Rollen; die Gleichheit gilt dann exakt.
- **Konsistenz mit `bauteilgruppe`**: Bedingung 1 übernimmt alle
  Bedingungen des Oberbegriffs, die Bedingungen 2 bis 5 und Z1 bis
  Z3 kommen hinzu und schwächen keine ab.
- **Konsistenz mit den Bauteilrollen**: Jedes Glied erfüllt die
  Bedingungen seiner Rolle (`deckenbalken`, `wechsel`), und zwar
  bezüglich der Ebene und der Stablage dieser Balkenlage (Z1, Z2).
  Bedingung 2a fällt für Deckenbalken mit deren Bedingung 1
  zusammen, für Wechsel folgt sie aus Z2 (`wechsel`, Satz 2 (i));
  Bedingung 4 folgt aus Z2 (`wechsel`, Bedingung 2). Die Doppelung
  ist unschädlich; 2a und 4 bleiben Vorprüfungen ohne Auflager-Daten.
  Dass ein waagrechter Stab Deckenbalken und nicht Wechsel ist,
  entscheidet nicht `deckenbalken`, sondern seine Einbindung hier:
  Deckenbalken liegen parallel (Bedingung 3), Wechsel rechtwinklig
  dazu und an ihnen gelagert (Bedingung 4, Z2).
- **Nicht-Zirkularität**: Die Definition stützt sich auf
  `bauteilgruppe`, `deckenbalken`, `wechsel`, `bauteil`,
  `bauteilachse`, `ebene`, `bezugsebene`, `einheitsvektor`,
  `weltkoordinatensystem`, `lokales_koordinatensystem`, `polyeder`,
  `uuid` und `toleranzen`. Sie verweist nicht auf sich selbst.
  `deckenbalken` und `wechsel` setzen die Balkenlage nicht voraus;
  sie nennen sie nur in `abgrenzung_zu:`. Die Gliedschaft eines
  Deckenbalkens ist deshalb hier geprüft (Z3), nicht dort
  (Quellenkonflikt, Punkt 10). Das ist dasselbe Muster wie bei
  `wand` und ihren Bauteilrollen.
- **Eliminierbarkeit**: Jede Verwendung von „Balkenlage" lässt sich
  durch das Tupel mit den Bedingungen 1 bis 4, Z1 und Z2 ersetzen;
  Z3 ist eine Bedingung an das Modell, nicht an das Tupel.
- **Konsistenz Prosa ↔ Formal**: „mindestens zwei zueinander
  parallele Deckenbalken" steht in den Feldern und in Bedingung 3,
  „Wechsel, die rechtwinklig zu den Deckenbalken liegen und an ihnen
  anschließen" in Bedingung 4 und Z2, „Bauteilachsen waagrecht" in
  2a, „Oberkanten in einer gemeinsamen waagrechten Bezugsebene" in
  (1), (2), 2b und Z1. Bauteilgruppe ist Bedingung 1.
- **Grenzfälle**: Eine geneigte Lage paralleler Stäbe verletzt 2a
  und ist keine Balkenlage. Zwei Balkenlagen in parallelen Ebenen
  (übereinander liegende Geschosse) sind getrennte Gruppen. Zwei
  Balkenlagen in derselben Ebene sind zulässig (verschossenes
  Gebälk, Quellenkonflikt Punkt 4). Kein Bauteil gehört zu beiden.

## Erläuterung (nicht normativ)

Die Balkenlage ist das tragende Gerippe einer Holzdecke: eine Schar
paralleler Deckenbalken, auf deren Oberkanten der Fußboden liegt,
dazu die Wechsel, die die Balken an Öffnungen abfangen. Nach der
Lage im Gebäude unterscheidet HPT Kehlbalkenlage, Dachbalkenlage
und Geschoßbalkenlage, nach der Spannrichtung Volmer Längs- und
Querbalkenlagen.

### Warum die Oberkante

Die Bezugsebene geht durch die Oberkanten, nicht durch die Achsen.
Die Hölzer einer Balkenlage dürfen nach Volmer „unterschiedliche
Maße (Stärken und Längen)" haben, etwa ein stärkerer Nachbarbalken
am Wechsel (mb-news). Bündig sind sie oben, weil dort Schalung und
Fußboden aufliegen. Die Unterkanten dürfen verspringen.

### Geschossfuge

Im Stockwerkbau liegt die Balkenlage zwischen den Wänden zweier
Geschosse:

```
Einbinder (UG) → Balkenlage → Stockschwelle (OG)
```

Die Bezugsebene E_L ist die „Oberkanten-Ebene der Balkenlage", auf
der `hg_stockschwelle.md` die Stockschwelle auflagert (dort E_⊥,
Bedingung 5). Die Deckenbalken liegen auf dem Einbinder der unteren
Wand (`hg_einbinder.md`), auf Mauerwerk, auf einem Unterzug oder, als
verkürzte Balken, auf einem Wechsel.

### Was zur Balkenlage gehört und was nicht

| Holz | Glied? | Begründung |
|---|---|---|
| Deckenbalken | ja | Rolle `deckenbalken` |
| Stichbalken an einer Öffnung | ja, als Deckenbalken | Volmer 2.6.25 (2): „Balken einer Balkenlage, der aufgrund einer Deckenöffnung kürzer ist" |
| Nachbarbalken am Wechsel | ja, als Deckenbalken | bleibt direktes Glied (Quellenkonflikt Punkt 6) |
| Randbalken längs der Spannrichtung (Randgurt) | ja, als Deckenbalken | Lage RAND in `deckenbalken`; Kolb S. 121 (Quellenkonflikt Punkt 9) |
| Wechsel | ja | Rolle `wechsel` |
| Randbalken quer zur Spannrichtung (Auflagerbalken) | nein | weder Deckenbalken noch Wechsel; eigener Eintrag `randbalken` folgt (Quellenkonflikt Punkt 9) |
| Kehlbalken | nein | eigene Rolle (Quellenkonflikt Punkt 3) |
| Unterzug, Überzug | nein | Auflager unter bzw. Holz über der Balkenlage (Volmer 2.6.21, 2.6.22) |
| Streichbalken als Auflager auf Konsolen | nein | Volmer 2.6.19 |
| Füllholz zwischen Wechsel und Kamin | nein | keine zulässige Rolle; ob Bestandteil oder Zubehör, lassen die Quellen offen (HPT S. 7–8) |
| Schalung, Fußboden, Einschub | nein | Schichten der Holzbalkendecke |

### Achsabstand und Teilung

Definition, belegte Spannen und Warnschwelle des Achsabstands stehen
in `deckenbalken` (weiche Regel 6, Quellenkonflikt Punkt 9, Tabelle
„Werte"): Mitte zu Mitte gemessen, Warnung erst über 900 mm, 625 mm
und 500 bis 700 mm im Holzrahmenbau (Kolb S. 160) nur als übliche
Werte.

Das Tabellenbuch (S. 131) gibt das Verfahren zur Teilung der
Balkenlage: Σe = l − 2 · 2 cm − b, also Raumlänge l abzüglich des
Wandabstands je Seite und der Balkenbreite b; die Zahl der Felder
ist Σe / e_max, aufgerundet, die Zahl der Balken eins mehr, und der
tatsächliche Abstand ist Σe geteilt durch die Zahl der Felder. Der
Wandabstand von 2 cm entspricht der Konstante
`STREICHBALKEN_WANDABSTAND_MIN_MM` in der Tabelle „Werte" von
`deckenbalken`; der Wert ist vorläufig und offen, Anweiser kennt keinen
Praxiswert (HPT S. 7 verlangt mehr als 3 cm).

### Balkenlage und Holzbalkendecke

Die Holzbalkendecke ist das ganze Bauteil mit Balkenlage, Schalung,
Füllung und Fußboden. Die Balkenlage ist nur ihr tragender Teil aus
Stäben. Das Datenmodell trennt beide wie Dachstuhl und Dachaufbau:
Die Balkenlage ist eine Bauteilgruppe, die Schichten der Decke
gehören in eine eigene Schicht-Familie (`hg_schicht.md`,
Folgearbeit `holzbalkendecke`).

## Beziehungen

- **Oberbegriff**: `bauteilgruppe`. Die Balkenlage hat alle
  Merkmale einer Bauteilgruppe (eigene Identität, eigene Hülle,
  exklusive Mitgliedschaft, Lebenszyklus-Bindung, konstruktive
  Funktionseinheit) und dazu die gemeinsame waagrechte Bezugsebene,
  parallele Deckenbalken und rechtwinklige Wechsel.
- **Bestandteile (partitiv)**:
  - **Deckenbalken** (`deckenbalken`, mindestens 2), einschließlich
    Stichbalken und Nachbarbalken an Wechseln.
  - **Wechsel** (`wechsel`, 0 oder mehr).
- **Geometrisches Bezugsobjekt (kein Glied)**: die Bezugsebene E_L
  (`ebene`, `bezugsebene`).
- **Verwendung**:
  - Auflagerebene der Stockschwelle (`stockschwelle`).
  - Tragender Teil einer Holzbalkendecke (Folgearbeit
    `holzbalkendecke`).
  - Möglicher Teil eines Tragwerks bzw. künftigen Deckentragwerks
    als nicht exklusive Sicht (`tragwerk`, `bausystem`).
- **Spezialisierungen** (Folgearbeit): `kehlbalkenlage`
  (Quellenkonflikt Punkt 3).
- **Verschachtelte Gruppen** (Folgearbeit): `auswechslung`
  (Quellenkonflikt Punkt 6).
- **Abgrenzung**:
  - **Bauteilgruppe** (`bauteilgruppe`): Oberbegriff.
  - **Deckenbalken** (`deckenbalken`), **Wechsel** (`wechsel`):
    Bauteilrollen der Glieder, nicht die Balkenlage selbst.
  - **Stichbalken** (`stichbalken`, Folgearbeit): verkürzter
    Deckenbalken; in Bedeutung 1 (Vorkragung) quer zu den
    Hauptbalken (Quellenkonflikt Punkt 4).
  - **Auswechslung** (`auswechslung`, Folgearbeit): Bauteilgruppe
    aus Wechseln und Stichbalken innerhalb der Balkenlage.
  - **Randbalken** (`randbalken`, Folgearbeit): umlaufender Rand
    der Deckenscheibe (Kolb S. 121). Längs der Spannrichtung ein
    Deckenbalken in Lage RAND und damit Glied; quer dazu
    Auflagerbalken, kein Glied (Quellenkonflikt Punkt 9).
  - **Unterzug** (`unterzug`, Folgearbeit): Auflager unter der
    Balkenlage, kein Glied.
  - **Kehlbalken** (`kehlbalken`), **Kehlbalkenlage**
    (`kehlbalkenlage`, Folgearbeit): eigene Rolle, Kehlbalkenlage
    nach diesem Eintrag keine Balkenlage.
  - **Holzbalkendecke** (`holzbalkendecke`, Folgearbeit): das
    Bauteil mit allen Schichten.
  - **Tragwerk** (`tragwerk`), **Deckentragwerk**
    (`deckentragwerk`, Folgearbeit in `hg_tragwerk.md`), **Bausystem**
    (`bausystem`): nicht exklusive Sichten; eine Balkenlage kann
    zugleich darin Mitglied sein.
  - **Wand** (`wand`): Geschwister-Bauteilgruppe mit lotrechter
    Wandebene.
  - **Einbinder** (`einbinder`): oberes Wandholz, Auflager der
    Deckenbalken, kein Glied.
  - **Stockschwelle** (`stockschwelle`): unteres Wandholz des
    oberen Geschosses, liegt auf E_L, kein Glied.
  - **Lage** (`lage`): Brett- oder Furnierlage im Mehrlagenholz,
    Homonym.

## Quellen

**Primär (normativ):**

- ISO 16739-1:2024, „Industry Foundation Classes (IFC) for data
  sharing in the construction and facility management industries —
  Part 1: Data schema" (IFC 4.3), `IfcElementAssemblyTypeEnum`
  (`BEAM_GRID`) und `IfcBeamTypeEnum` (`JOIST`). Wortlaut im
  buildingSMART-Quelltext auf GitHub (IFC4.3.x-development, Branch
  master) am 2026-11-14 eingesehen.
- DIN 18334 (VOB Teil C), Zimmer- und Holzbauarbeiten, Abrechnung
  der Auswechselungen nach Stück; zitiert nach Bläsi/Ferdinand,
  *Tabellenbuch Zimmerer*, 2021, S. 270.

**Sekundär:**

- Volmer, L.; Zimmermann, W. H. (Hrsg.): *Glossary of Prehistoric
  and Historic Timber Buildings / Glossar zum prähistorischen und
  historischen Holzbau.* NIhK / Verlag Marie Leidorf, Rahden 2012,
  Kap. 2.6 (S. 206–222), S. 44. Frei verfügbares PDF, im Volltext
  gelesen.
- Hölder-Pichler-Tempsky (HPT): *Fachkunde Zimmerer 2*, Kap. 1
  „Holzdecken", Leseprobe (Buch-S. 5–13), im Volltext gelesen.
- Saint-Gobain Rigips: *Technik aktuell* 02/12, „Innendämmung bei
  Holzbalkendecken", 2012, S. 3–4.
- Bläsi, W.; Ferdinand, S.: *Tabellenbuch Zimmerer.* 9. Auflage,
  Bildungsverlag EINS, Köln 2021, S. 131, 159, 161, 270 (lokaler
  Scan).
- Degiuli, F.: „Auswechselungen in Holzbalkendecken", *mb-news*
  3/2019, S. 32–36.
- Kolb, J.; Kolb, H.; Müller, A.: *Holzbau mit System.* 4. Auflage,
  Birkhäuser, Basel 2024, mit Lignum, S. 41, 113, 116, 117, 121, 160,
  295, 311, 413. Nur
  Textausschnitte der Suche im Buch bei Google Books, 2026-11-14.
- Colling, F.: *Holzbau — Grundlagen und Bemessung nach EC 5.*
  7. Auflage, Springer Vieweg, Wiesbaden 2021, S. 78 (OCR-Text).
- Esselborn, K. (Hrsg.): *Lehrbuch des Hochbaues*, Bd. 1, Leipzig
  1908, Kap. III von K. Stief, S. 194.
- Colling, F.; Kessel, M. H.; Sieder, M.; Janßen, P.: „Bemessung von
  aussteifenden Deckentafeln", *holzbau technik* 9/2019.
- Recherche-Bericht [intern].

**Korpus (nicht autoritativ):**

- Wikipedia, Lemma „Holzbalkendecke" (abgerufen 2026-11-14).
- DWDS, Lemma „Gebälk" (eWDG 1967, abgerufen 2026-11-14).
