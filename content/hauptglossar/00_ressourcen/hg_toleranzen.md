---
id: toleranzen
benennung: Toleranzen (numerische Klassifikationsschwellen)
synonyme: ["Epsilon-Schwellen", "Klassifikationstoleranzen", "numerische Toleranzen"]
abgelehnte_benennungen: [Genauigkeit, Messunsicherheit, Fertigungstoleranz, "tolerance", "epsilon"]
oberbegriff: null
begriffstyp: hilfsbegriff
voraussetzungen: [punkt, vektor, strecke, ebene, polygon]
abgrenzung_zu: [messunsicherheit, fertigungstoleranz, masstoleranz_din18202, masstoleranz_sia414]
status: entwurf
theorie_pflichtig: required
quellen_primär:
  - "IEEE Std 754-2019, 'IEEE Standard for Floating-Point Arithmetic', insbesondere § 3 (Formats) und § 4 (Attributes and Rounding)."
  - "ISO/IEC/IEEE 60559:2020, 'Information technology — Microprocessor Systems — Floating-point arithmetic', technisch identisch mit IEEE 754-2019."
quellen_sekundär:
  - "Higham, N. J.: Accuracy and Stability of Numerical Algorithms. 2. Aufl., SIAM, Philadelphia 2002, Kap. 1 (Principles of Finite Precision Computation), Kap. 2 (Floating Point)."
  - "Goldberg, D.: 'What Every Computer Scientist Should Know About Floating-Point Arithmetic'. ACM Computing Surveys 23(1), 1991, S. 5–48."
  - "Knuth, D. E.: The Art of Computer Programming, Vol. 2: Seminumerical Algorithms. 3. Aufl., Addison-Wesley 1997, § 4.2.2 'Accuracy of Floating Point Arithmetic'."
  - "Shewchuk, J. R.: 'Robust Adaptive Floating-Point Geometric Predicates'. Proc. 12th ACM Symp. Computational Geometry, 1996, S. 141–150."
quellenkonflikt: |
  Es gibt keine normative Quelle des Holzbaus (DIN 1052, DIN EN 1995-1-1,
  SIA 265, DIN 18202, SIA 414), die numerische Klassifikationsschwellen
  für geometrische Vergleiche im Sinne dieses Eintrags festlegt. Die
  genannten Bauwerksnormen behandeln ausschließlich handwerkliche Maß-
  und Fertigungstoleranzen (z. B. ±1 mm bis ±5 mm) und sind hier nicht
  einschlägig — siehe Abschnitt „Abgrenzung". Eigene Festlegung: die in
  diesem Eintrag definierten Toleranzen sind reine numerische Schwellen
  zur Klassifikation entartet vs. regulär in der Domänen-Schicht; ihre
  Größenordnungen sind aus IEEE 754-Eigenschaften und der typischen
  Größenordnung der modellierten Bauteile (≤ 10⁴ mm) hergeleitet, nicht
  aus einer Bauwerksnorm. Diese Festlegung ist konfliktfrei mit allen
  konsultierten Quellen.
---

## Prosa-Definition

Eine **Toleranz** im Sinne dieses Glossars ist ein nicht-negativer reeller
Schwellwert ε ≥ 0, mit dem ein numerischer Gleichheits-, Null- oder
Lagevergleich zwischen geometrischen Größen so durchgeführt wird, dass
zwei Werte als gleich, ein Wert als null oder eine Lagebeziehung als
erfüllt gilt, sobald die zugehörige reellwertige Abweichung den Wert ε
nicht überschreitet, und die ausschließlich der Klassifikation
entartet vs. regulär in der Domänen-Schicht dient.

## Mathematische Definition

Sei

- 𝕄 ⊂ ℝ die Menge der in IEEE 754 binary64 darstellbaren reellen Zahlen,
- d : X × X → ℝ_{≥0} eine Abweichungsfunktion auf einer geometrischen
  Größenmenge X (z. B. Längenabweichung, Winkelabweichung,
  Flächeninhalt, sin des eingeschlossenen Winkels),
- ε ∈ 𝕄 mit ε ≥ 0 ein fester Schwellwert.

Dann heißen zwei Größen a, b ∈ X **bezüglich der Toleranz ε gleich**
genau dann, wenn

```
gleich_ε(a, b) :⇔ d(a, b) ≤ ε.
```

Eine Toleranz ist die Festlegung des Paares (d, ε). Im vorliegenden
Glossar werden fünf solche Paare normativ benannt:

| Bezeichner       | Abweichung d                                          | Einheit | empfohlener Default |
|------------------|-------------------------------------------------------|---------|---------------------|
| `LAENGE_EPS`     | d(a, b) = |a − b|, a, b Längen oder Koordinaten       | mm      | 1·10⁻³ mm           |
| `WINKEL_EPS`     | d(α, β) = |α − β|, α, β Winkel                        | rad     | 1·10⁻⁹ rad          |
| `NORM_EPS`       | d(v, 0) = | ‖v‖² − s |, mit s ∈ {0, 1} (Null- bzw.    |         |                     |
|                  | Einheitsvektor-Test)                                  | mm² bzw. dimensionslos | 1·10⁻¹² |
| `FLAECHE_EPS`    | d(F, 0) = |F|, F Flächeninhalt                        | mm²     | 1·10⁻⁶ mm²          |
| `KOLLINEAR_EPS`  | d(u, v) = ‖u_hat × v_hat‖ = |sin∠(u, v)|, u_hat, v_hat normiert     | dimensionslos | 1·10⁻⁹       |

Die konkreten Zahlenwerte sind **empfohlene Default-Werte** dieses
Eintrags; die kanonische Quelle der im Code verwendeten Werte ist die
Kotlin-Klasse `domain.Toleranzen`. Eine Implementierung darf abweichen,
muss die Abweichung aber im Code-Kommentar dieser Klasse mit Verweis
auf einen Glossarbegriff begründen.

## Wohldefiniertheit

- Eindeutigkeit der Klassifikation: Für festes (d, ε) und feste a, b ist
  d(a, b) ≤ ε eine Aussage über reelle Zahlen und damit eindeutig.
  Numerische Auswertung in IEEE 754 binary64 kann am Rand der Toleranz
  nicht-deterministisch ausfallen; die Toleranz ist deshalb so zu wählen,
  dass der erwartete Rundungsfehler von d in fließenden Größenordnungen
  von Bauteilkoordinaten (≤ 10⁴ mm) deutlich kleiner ist als ε (siehe
  Begründungen je Toleranz).
- Symmetrie: Alle oben genannten d sind symmetrisch
  (d(a, b) = d(b, a)). Die Relation gleich_ε ist reflexiv und symmetrisch,
  jedoch im Allgemeinen **nicht transitiv**; sie ist also keine
  Äquivalenzrelation, sondern eine Toleranzrelation im Sinne von Poston.
  Diese fehlende Transitivität ist im Implementierungshinweis zu
  beachten (kein naives Clustering durch wiederholten Gleichheitstest).
- Nicht-Zirkularität: Die Definition verwendet ausschließlich reelle
  Zahlen, die Primitive Punkt, Vektor, Strecke, Ebene, Polygon (mit
  ihren Längen-, Winkel-, Flächen- und Normfunktionen) und das
  IEEE-754-Modell der Gleitkommazahl.

## Erläuterung (nicht normativ)

Toleranzen in diesem Eintrag sind ein **numerisches Werkzeug**, kein
fachlicher Holzbau-Begriff. Sie beantworten Fragen wie „liegt dieser
Punkt in dieser Ebene?", „sind diese drei Punkte kollinear?", „ist dieser
Vektor ein Einheitsvektor?". Ohne Toleranzen könnten diese Fragen in
Gleitkomma-Arithmetik nie mit ja beantwortet werden, da exakte
Gleichheit auf 𝕄 ein Maß-Null-Ereignis ist.

Die Wahl der Größenordnung balanciert zwei Forderungen:

1. **Größer als der Rundungsfehler**, sonst werden gleiche Werte fälschlich
   als ungleich klassifiziert (Falsch-Negativ, „Phantom-Entartung").
2. **Kleiner als die kleinste fachlich relevante Abweichung**, sonst
   werden tatsächlich verschiedene geometrische Konfigurationen
   fälschlich identifiziert (Falsch-Positiv, „Kollaps").

Für Holzbau-Geometrie bei Koordinaten in mm und Bauteilgrößen bis
ca. 10⁴ mm liegt das Maschinenepsilon der relativen Rundung bei rund
2,2·10⁻¹⁶, der absolute Rundungsfehler einer Koordinate bei rund
2·10⁻¹² mm. Eine handwerkliche Holzbautoleranz beträgt nach SIA 414
bzw. DIN 18202 typischerweise ±1 mm bis ±5 mm. Zwischen diesen beiden
Schranken liegen rund elf Zehnerpotenzen Spielraum; die hier gewählten
Defaults siedeln in der unteren Hälfte dieses Korridors, also weit
oberhalb des Rundungsfehlers und weit unterhalb jeder fachlichen
Abweichung.

## Toleranz-Arten im Einzelnen

> **Anwendungs-Zuordnung**: Welche Toleranz-Konstante bei welcher
> Art von Prädikat zu verwenden ist (Längen-, Winkel-, Lot-,
> Kollinearitäts-, Flächen-Test), steht zentral in
> `_KONVENTIONEN.md` Sektion 4 („Toleranz-Konstanten und ihre
> Anwendung"). Insbesondere gilt: alle Lot- und Lage-Prädikate
> (Senkel-, Bleischnitt-, Pfetten-Horizontalitäts-, Falllinien-
> Kollinearitäts-Test) verwenden `KOLLINEAR_EPS` (Sinus-Test über
> normiertes Kreuzprodukt); explizite Winkel-Vergleiche
> (`acos`/`atan2`-Resultat gegen Soll-Winkel) verwenden
> `WINKEL_EPS`. Die folgenden Unterabschnitte beschreiben die
> Konstanten selbst (Bedeutung, Default, Begründung) und führen
> typische Verwendungsbeispiele auf, ohne die Anwendungs-Regel
> hier zu duplizieren. Bei Konflikt zwischen einem konkreten
> Eintrag (auch diesem) und der Tabelle in `_KONVENTIONEN.md`
> Sektion 4 wird der konkrete Eintrag korrigiert.

### Längen-Toleranz `LAENGE_EPS`

- **Bedeutung**: Maximale absolute Abweichung in mm, unterhalb derer
  zwei Längen, Abstände oder einzelne Koordinatenkomponenten als gleich
  gelten.
- **Empfohlener Default**: `LAENGE_EPS = 1·10⁻³` mm = 1 µm.
- **Begründung**: Liegt rund 10⁹ mal über dem absoluten Rundungsfehler
  bei mm-Koordinaten in binary64 und rund 10³ mal unter der feinsten
  handwerklichen Holzbau-Maßtoleranz (±1 mm nach SIA 414, Toleranzklasse
  „fein"). Damit ist LAENGE_EPS für jeden konstruktiven Vergleich
  numerisch sicher und fachlich unsichtbar.
- **Verwendung**:
  - `Punkt.gleich(q, eps = LAENGE_EPS)`: ‖p − q‖ ≤ eps.
  - `Punkt.istInEbene(E)`: |⟨n, p − p₀⟩| ≤ LAENGE_EPS bei normiertem n.
  - `Strecke.istEntartet`: Länge ≤ LAENGE_EPS ⇒ `Entartet.PunktStrecke`.
  - `Polygon`: aufeinanderfolgende Eckpunkte mit Abstand ≤ LAENGE_EPS
    werden als doppelter Eckpunkt klassifiziert ⇒
    `Entartet.DoppelterEckpunkt`.

### Winkel-Toleranz `WINKEL_EPS`

- **Bedeutung**: Maximale absolute Abweichung in Radiant, unterhalb derer
  zwei Winkel oder ein Winkel zu einem ausgezeichneten Wert (0, π/2, π)
  als gleich gelten.
- **Empfohlener Default**: `WINKEL_EPS = 1·10⁻⁹` rad
  (≈ 5,73·10⁻⁸ Grad).
- **Begründung**: Liegt mehrere Größenordnungen über dem akkumulierten
  Rundungsfehler weniger trigonometrischer Auswertungen
  (`acos`, `atan2`) bei normierten Argumenten und gleichzeitig weit
  unter jeder im Holzbau praktisch unterscheidbaren Winkelabweichung
  (typische Anrissgenauigkeit ≈ 0,1° = 1,7·10⁻³ rad).
- **Verwendung**:
  - Test auf Rechtwinkligkeit, Parallelität bei explizit berechneten
    Winkeln statt über Skalarprodukt.
  - Klassifikation Flach- vs. Geneigtdach am Rand
    (Dachneigung α: Flachdach genau dann, wenn α ≤ WINKEL_EPS).
  - Toleranz auf die Bedingung n_a · e_z ≥ −WINKEL_EPS in
    `Dachflaeche.init` (kleine numerische Unterschreitung wird als
    0 toleriert, siehe `dachflaeche`).

### Norm-Toleranz `NORM_EPS`

- **Bedeutung**: Schwelle für das Quadrat der Vektorlänge ‖v‖² beim
  Test, ob ein Vektor der Nullvektor ist, bzw. für | ‖v‖² − 1 | beim
  Test auf Einheitsvektor.
- **Empfohlener Default**: `NORM_EPS = 1·10⁻¹²` (dimensionslos für
  Einheitsvektor-Test; mm² für Nullvektor-Test, da ‖v‖² in mm² gemessen
  wird).
- **Begründung**: Auf normierten Vektoren entspricht ‖v‖² < 1·10⁻¹²
  einer Vektorlänge < 1·10⁻⁶, also weit unterhalb jeder geometrisch
  relevanten Größe. Die Verwendung des Quadrats vermeidet eine
  Quadratwurzel im heißen Pfad und ist numerisch günstiger.
- **Verwendung**:
  - `Vektor.istNull`: ‖v‖² ≤ NORM_EPS ⇒ `Entartet.Nullvektor`.
  - `Vektor.istEinheit`: | ‖v‖² − 1 | ≤ NORM_EPS.
  - Eingangsprüfung von Normalenvektoren in `Ebene` und
    `Dachflaeche` (siehe Implementierungshinweise dort).

### Flächen-Toleranz `FLAECHE_EPS`

- **Bedeutung**: Maximale absolute Abweichung eines Flächeninhalts in
  mm² vom Wert null, unterhalb derer ein Polygon als entartet
  (degeneriertes Flächenstück) gilt.
- **Empfohlener Default**: `FLAECHE_EPS = 1·10⁻⁶` mm².
- **Begründung**: Konsistent zu LAENGE_EPS als Quadrat: ein Polygon mit
  charakteristischer Kantenlänge LAENGE_EPS hat Flächeninhalt der
  Größenordnung LAENGE_EPS² = 10⁻⁶ mm². Damit klassifiziert
  FLAECHE_EPS genau jene Polygone als entartet, deren Eckpunkte
  innerhalb der Längen-Toleranz kollabieren.
- **Verwendung**:
  - `Polygon.istEntartet`: |Flächeninhalt| ≤ FLAECHE_EPS ⇒
    `Entartet.NullFlaeche`.
  - Bedingung in `Dachflaeche.init`:
    Flächeninhalt(F(P)) > FLAECHE_EPS (siehe `dachflaeche`).

### Kollinearitäts-Toleranz `KOLLINEAR_EPS`

- **Bedeutung**: Schwelle für ‖u_hat × v_hat‖ = |sin∠(u_hat, v_hat)| zwischen zwei
  normierten Vektoren u_hat, v_hat beim Test auf Kollinearität (parallel oder
  antiparallel).
- **Empfohlener Default**: `KOLLINEAR_EPS = 1·10⁻⁹` (dimensionslos).
- **Begründung**: Konsistent zu WINKEL_EPS, da für kleine Winkel α gilt
  sin α ≈ α; ein Sinuswert ≤ 10⁻⁹ entspricht einem Winkel ≤ 10⁻⁹ rad.
  Der Sinus-Test über das Kreuzprodukt ist numerisch stabiler als der
  Cosinus-Test über das Skalarprodukt, weil cos in der Nähe von ±1
  schlecht konditioniert ist (Auslöschung), während sin in der Nähe
  von 0 gut konditioniert ist.
- **Verwendung**:
  - Drei Punkte p, q, r kollinear genau dann, wenn
    ‖(q − p)/‖q − p‖ × (r − p)/‖r − p‖‖ ≤ KOLLINEAR_EPS.
  - Zwei Geraden parallel genau dann, wenn ihre Richtungsvektoren
    den Kollinearitätstest erfüllen.
  - Drei Eckpunkte eines Polygons kollinear ⇒ überzähliger Eckpunkt
    (`Entartet.KollinearerEckpunkt`).

## Bearbeitungs-Plausibilitäts-Konstanten

Neben den fünf numerischen Klassifikations-Schwellen führt die App
unter demselben Modul `domain.Toleranzen` eine zweite Gruppe von
Konstanten: **Plausibilitäts-Faustregeln** für die Bearbeitungs-
Subtypen `kerve`, `versatz`, `zapfen` und `zapfenloch`. Sie haben
einen kategorisch anderen Status als die EPS-Konstanten und sind
deshalb in einer eigenen Sektion verortet.

### Abgrenzung weiche Constraints vs. harte Invarianten

| Eigenschaft | EPS-Konstanten | Plausibilitäts-Konstanten |
|---|---|---|
| Rolle im Validierungs-Verhalten | Bestandteil **harter Invarianten** (`Resultat.Fehler(*Ungueltig.*)`) | Auslöser **weicher Warnungen** (`Warnung.*`) |
| Wirkung bei Verletzung | Modellierung wird abgelehnt | Modellierung wird zugelassen, Warnung angezeigt |
| Quellen-Charakter | numerisch hergeleitet aus IEEE 754 + Bauteil-Größenordnung | berufssprachliche Faustregel oder normative Bemessungs-Faustregel (NCI NA.12, DIN 1052 §15, DACH-Praxis) |
| Überschreibbarkeit | konstant; Abweichung verlangt Code-Kommentar mit Begründung | projekt-, norm- oder regional konfigurierbar (z. B. SIA-CH vs. DIN-DE, Nadelholz vs. Laubholz) |
| Test-Form | Längen-, Winkel-, Flächen-, Norm-, Kollinearitäts-Vergleich | dimensionslose Bruchteile (`Double`) oder dimensionierte Mindest-Maße (mm) |

Eine Plausibilitäts-Konstante ist **kein** numerischer Schwellwert
einer geometrischen Klassifikations-Aussage, sondern eine
**fachliche Faustregel**, deren Verletzung in der Bemessungs-
Schicht eine Warnung produziert. Die Validierung blockiert die
Modellierung in keinem Fall — nur die harten Invarianten der
jeweiligen Bearbeitung tun das (siehe `hg_kerve.md`, `hg_versatz.md`,
`hg_zapfen.md`, `hg_zapfenloch.md`, Block „Wohldefiniertheit").

### Inventar

Die folgenden elf Konstanten sind zentral in `domain.Toleranzen`
geführt; ihre Bedeutung steht im jeweils zuständigen Bearbeitungs-
Eintrag, hier wird der **Wert**, die **normative Stütze** und die
**Klassifikation** verbucht.

| Konstante | Default | Einheit | Bauteil-/Bearbeitungs-Kontext | Normative Stütze | Klassifikation |
|---|---|---|---|---|---|
| `KERVTIEFE_FAUSTREGEL_DRITTEL` | `1.0/3.0` | dimensionslos (Bruchteil von h_B) | `kerve` — Kervtiefe t ≤ ⅓ der Sparrenhöhe h_B | DACH-Berufssprache („⅓-Faustregel"); EC 5 § 6.5 Schubnachweis als Bemessungs-Anker; IRC R802.7.1 lokale Lesart ¼; konservative Klauen-Lesart ⅙ | weich (Warnung `KerveZuTief`) |
| `VERSATZ_TIEFE_FLACH_VIERTEL` | `1.0/4.0` | dimensionslos (Bruchteil von h_B) | `versatz` — Versatztiefe t_i ≤ ¼·h_B bei flachem Strebenanschluss α ≤ 50° | DIN EN 1995-1-1/NA:2013-08 NCI NA.12 (Sekundärquellen-belegt; Volltext-Verifikation ausstehend, siehe `hg_versatz.md` Quellenkonflikt 1) | weich (Warnung `VersatzZuTief`) |
| `VERSATZ_TIEFE_STEIL_SECHSTEL` | `1.0/6.0` | dimensionslos (Bruchteil von h_B) | `versatz` — Versatztiefe t_i ≤ ⅙·h_B bei steilem Strebenanschluss α ≥ 60°; zwischen 50° und 60° lineare Interpolation | DIN EN 1995-1-1/NA:2013-08 NCI NA.12 (s. o.) | weich (Warnung `VersatzZuTief`) |
| `VERSATZ_VORHOLZ_FAKTOR` | `8.0` | dimensionslos (Faktor an t_v) | `versatz` — Vorholzlänge l_v ≥ Faktor · maßgebende Versatztiefe t_v | DIN EN 1995-1-1/NA:2013-08 NCI NA.12; EC 5 § 6.5 Schubnachweis am Vorholz | weich (Warnung `VersatzVorholzZuKurz`) |
| `VERSATZ_VORHOLZ_MINDESTLAENGE_MM` | `200.0` | mm | `versatz` — Vorholzlänge l_v ≥ 200 mm (untere Schranke neben dem Faktor-Kriterium) | DIN EN 1995-1-1/NA:2013-08 NCI NA.12 | weich (Warnung `VersatzVorholzZuKurz`) |
| `VERSATZ_KAMM_MINDESTHOEHE_MM` | `10.0` | mm | `versatz` (Subtyp `DOPPELT`) — Tiefendifferenz t_F − t_S ≥ 10 mm an der Versatzkamm-Sohle (Ferse mind. 1 cm tiefer als Stirn) | Holzbau-Taschenbuch Kap. 20; DACH-Praxisregel (Abscher-Schutz der Kamm-Sohle) | weich (Warnung `VersatzKammSohleZuFlach`) |
| `ZAPFENBREITE_FAUSTREGEL_DRITTEL` | `1.0/3.0` | dimensionslos (Bruchteil von b_B) | `zapfen` — Zapfenbreite w_Z ≈ ⅓ der Bauteildicke des stärkeren Holzes | DIN 1052:2008-12 § 15 (Sekundärquellen-belegt); DACH-Berufssprache | weich (Warnung `ZapfenbreiteAtypisch`) |
| `ZAPFENLOCH_RESTHOLZ_SEITLICH_MIN` | `30.0` | mm | `zapfenloch` — Mindest-Restholz seitlich des Loch-Rechtecks (auf jeder Seite in u-Richtung und v-Richtung der Bezugsfläche) | DIN 1052:2008-12 § 15 (norm-implizit über Schubnachweis); DACH-Praxisregel | weich (Warnung `ZapfenlochZuNahAmRand`) |
| `ZAPFENLOCH_RESTHOLZ_UNTEN_MIN` | gleich Lochtiefe t (d. h. d_F(B) ≥ 2·t) | mm | `zapfenloch` — Mindest-Restholz unter dem Loch in Richtung der Flächen-Normalen | EC 5 § 6.1.5 Querdruck + § 6.5 Schubnachweis am verbleibenden Holz (norm-implizit) | weich (Warnung `ZapfenlochZuTief`) |
| `ZAPFENLUFT_MIN` | `5.0` | mm | `zapfenloch` (im Verbindungs-Kontext) — Lochtiefe minus Zapfenlänge ≥ 5 mm (untere Schranke der Zapfenluft) | Wikipedia-Lemma „Zapfenverbindung" als belegter Konsens; DIN 1052 § 15 norm-implizit (Schwund/Quellung) | weich (Warnung `ZapfenluftAusserhalb`) |
| `ZAPFENLUFT_MAX` | `10.0` | mm | `zapfenloch` (im Verbindungs-Kontext) — Lochtiefe minus Zapfenlänge ≤ 10 mm (obere Schranke der Zapfenluft) | Wikipedia-Lemma „Zapfenverbindung"; DACH-Berufssprache-Konsens | weich (Warnung `ZapfenluftAusserhalb`) |

### Status der Konstanten

Alle elf Plausibilitäts-Konstanten teilen drei Eigenschaften:

1. **Kein Bestandteil einer Bearbeitungs-Definition.** Die Geometrie
   der Kerve, des Versatzes, des Zapfens und des Zapfenlochs ist
   ohne diese Konstanten **vollständig wohldefiniert** (siehe die
   jeweiligen Wohldefiniertheits-Blöcke). Die Plausibilitäts-
   Konstanten sind ein Bemessungs- und Praxis-Filter, der über die
   Geometrie hinausgeht.
2. **Quellen-Lage indirekt.** Die normativen Stützen NCI NA.12,
   DIN 1052 § 15 und SIA 265 Anhang A sind in den Sandbox-
   Recherchen nicht volltext-zugänglich; die Werte folgen dem
   Sekundärquellen-Konsens (Mönck/Rug, Holzbau-Taschenbuch,
   baunetzwissen.de) und sind in den jeweiligen Einträgen unter
   `quellenkonflikt:` dokumentiert. Eine Volltext-Verifikation gegen
   den NA-/DIN-1052-/SIA-265-Wortlaut ist Folgearbeit (siehe
   Recherche-Berichte `docs/recherche/2026-05-14_hg_versatz.md` und
   `docs/recherche/2026-05-14_hg_zapfen.md`).
3. **Konfigurierbarkeit.** Eine projekt-, norm- oder
   regionalspezifische Überschreibung der Defaults ist
   ausdrücklich vorgesehen — z. B. Kervtiefe `1.0/4.0` für IRC-
   konforme Projekte, `1.0/6.0` für die konservative Klauen-Lesart;
   Zapfenluft eng `[5.0, 7.0]` bei trockenem Brettschichtholz, weit
   `[8.0, 12.0]` bei frischem Vollholz. Der Mechanismus dieser
   Überschreibung (Konfigurationsobjekt, Profil, Projekt-Default)
   ist Folgearbeit der Bemessungs-Schicht.

## Beziehungen

- **Oberbegriff**: keiner. Toleranzen sind ein numerisches
  Hilfskonzept der Domänen-Schicht und stehen quer zu den
  geometrischen Primitiven.
- **Teilbegriffe (extensional)**: die fünf oben definierten
  Toleranzen LAENGE_EPS, WINKEL_EPS, NORM_EPS, FLAECHE_EPS,
  KOLLINEAR_EPS. Die Liste ist nicht abgeschlossen; weitere
  Toleranzen (z. B. eine Volumen-Toleranz) werden bei Bedarf in
  diesem Eintrag ergänzt.
- **Abgrenzung**:
  - **Maßtoleranz im Holzbau (DIN 18202, SIA 414)**: handwerkliche
    Grenzabweichungen zwischen Soll- und Ist-Maß eines gefertigten
    Bauteils, typischerweise ±1 mm bis ±5 mm. Diese Toleranzen sind
    fachliche Eigenschaften der Ausführung, nicht numerische Schwellen
    eines Vergleichs. Sie sind in der App separat als Bauteilattribut
    zu führen (eigene Glossareinträge `masstoleranz_din18202`,
    `masstoleranz_sia414`).
  - **Messunsicherheit (JCGM 100, GUM)**: statistische Streuung eines
    Messwerts um den wahren Wert. Bezieht sich auf reale Messung,
    nicht auf rechnerische Klassifikation.
  - **Fertigungstoleranz**: Synonym zu Maßtoleranz im
    fertigungstechnischen Kontext, nicht synonym zur Toleranz dieses
    Eintrags.
  - **Maschinenepsilon (`Double.ulp`, ≈ 2,22·10⁻¹⁶)**: untere
    Schranke der relativen Rundung in IEEE 754 binary64.
    Maschinenepsilon ist eine **Eigenschaft der Arithmetik**, nicht
    eine Toleranz im Sinne dieses Eintrags. Toleranzen werden so
    gewählt, dass sie viele Größenordnungen über dem
    Maschinenepsilon liegen, sind aber kein Vielfaches davon.

## Implementierungshinweis

Datentyp und Werte (Domänen-Schicht, Kotlin, Schicht
`domain.Toleranzen`):

```
package domain

/**
 * Numerische Klassifikationsschwellen für geometrische Vergleiche.
 * Glossar: hg_toleranzen.md
 *
 * Diese Werte sind die kanonische Quelle der Implementierung.
 * Abweichungen vom Default des Glossars sind hier zu begründen.
 */
object Toleranzen {
    /** Längen-Toleranz, mm. Glossar: toleranzen#laenge_eps */
    const val LAENGE_EPS: Double = 1.0e-3

    /** Winkel-Toleranz, rad. Glossar: toleranzen#winkel_eps */
    const val WINKEL_EPS: Double = 1.0e-9

    /** Norm-Toleranz für ‖v‖² bzw. |‖v‖² − 1|. Glossar: toleranzen#norm_eps */
    const val NORM_EPS: Double = 1.0e-12

    /** Flächen-Toleranz, mm². Glossar: toleranzen#flaeche_eps */
    const val FLAECHE_EPS: Double = 1.0e-6

    /** Kollinearitäts-Toleranz für ‖u_hat × v_hat‖, dimensionslos.
     *  Glossar: toleranzen#kollinear_eps */
    const val KOLLINEAR_EPS: Double = 1.0e-9

    // ----- Bearbeitungs-Plausibilitäts-Konstanten -----
    // Weiche Faustregeln, kein Validierungsfehler bei Verletzung.
    // Glossar: toleranzen, Sektion „Bearbeitungs-Plausibilitäts-
    // Konstanten".

    /** Kervtiefe ≤ ⅓ der Sparrenhöhe.
     *  Glossar: hg_kerve.md (Plausibilität). */
    const val KERVTIEFE_FAUSTREGEL_DRITTEL: Double = 1.0 / 3.0

    /** Versatztiefe ≤ ¼ der Bauteilhöhe bei flachem
     *  Strebenanschluss α ≤ 50° (NCI NA.12).
     *  Glossar: hg_versatz.md. */
    const val VERSATZ_TIEFE_FLACH_VIERTEL: Double = 1.0 / 4.0

    /** Versatztiefe ≤ ⅙ der Bauteilhöhe bei steilem
     *  Strebenanschluss α ≥ 60° (NCI NA.12).
     *  Glossar: hg_versatz.md. */
    const val VERSATZ_TIEFE_STEIL_SECHSTEL: Double = 1.0 / 6.0

    /** Vorholz-Faktor: l_v ≥ Faktor · t_v (NCI NA.12).
     *  Glossar: hg_versatz.md. */
    const val VERSATZ_VORHOLZ_FAKTOR: Double = 8.0

    /** Mindest-Vorholzlänge in mm (NCI NA.12).
     *  Glossar: hg_versatz.md. */
    const val VERSATZ_VORHOLZ_MINDESTLAENGE_MM: Double = 200.0

    /** Doppelter Versatz: Mindest-Tiefendifferenz t_F − t_S in mm.
     *  Glossar: hg_versatz.md. */
    const val VERSATZ_KAMM_MINDESTHOEHE_MM: Double = 10.0

    /** Zapfenbreite ≈ ⅓ der Bauteildicke (DIN 1052 §15).
     *  Glossar: hg_zapfen.md. */
    const val ZAPFENBREITE_FAUSTREGEL_DRITTEL: Double = 1.0 / 3.0

    /** Mindest-Restholz seitlich des Zapfenlochs in mm.
     *  Glossar: hg_zapfenloch.md. */
    const val ZAPFENLOCH_RESTHOLZ_SEITLICH_MIN: Double = 30.0

    /** Mindest-Zapfenluft (Lochtiefe − Zapfenlänge) in mm.
     *  Glossar: hg_zapfenloch.md. */
    const val ZAPFENLUFT_MIN: Double = 5.0

    /** Maximal-Zapfenluft (Lochtiefe − Zapfenlänge) in mm.
     *  Glossar: hg_zapfenloch.md. */
    const val ZAPFENLUFT_MAX: Double = 10.0

    // ZAPFENLOCH_RESTHOLZ_UNTEN_MIN ist kein Skalar, sondern eine
    // bauteilabhängige Regel d_F(B) ≥ 2·t; sie wird in der
    // Bemessungs-Schicht als Funktion realisiert, nicht als
    // konstanter Wert hier.
}
```

- **Einheit**: je Toleranz unterschiedlich, siehe Tabelle und
  Unterabschnitte. Niemals Einheiten mischen. Für die
  Bearbeitungs-Plausibilitäts-Konstanten gilt: dimensionslose
  Bruchteile (`*_DRITTEL`, `*_VIERTEL`, `*_SECHSTEL`,
  `*_FAKTOR`) sind reine `Double`-Werte; Mindest-Maße tragen das
  Suffix `_MM` und sind in Millimetern angegeben.
- **Invarianten** (EPS-Konstanten):
  1. Alle Werte sind endlich, nicht-negativ und kleiner als 1.
  2. LAENGE_EPS² ≤ FLAECHE_EPS (Konsistenz Längen-↔Flächen-Toleranz).
  3. WINKEL_EPS und KOLLINEAR_EPS liegen in derselben Größenordnung
     (sin α ≈ α für kleine α).
  4. NORM_EPS ≤ LAENGE_EPS² (Norm-Quadrat-Test ist mindestens so
     scharf wie der Längen-Test auf den Nullvektor).
- **Invarianten** (Plausibilitäts-Konstanten):
  1. Alle Bruchteil-Werte (`*_DRITTEL`, `*_VIERTEL`,
     `*_SECHSTEL`) liegen im offenen Intervall (0, 1).
  2. `VERSATZ_TIEFE_STEIL_SECHSTEL < VERSATZ_TIEFE_FLACH_VIERTEL`
     (steilere Strebe → schärfere Tiefen-Schranke).
  3. `ZAPFENLUFT_MIN < ZAPFENLUFT_MAX` (nicht-leeres
     Plausibilitäts-Intervall).
  4. Alle Mindest-Maße (`*_MM`) sind strikt positiv und größer
     als `LAENGE_EPS` (sonst würde die Faustregel mit der
     numerischen Toleranz kollidieren).
  5. `VERSATZ_VORHOLZ_FAKTOR > 1` (Vorholzlänge mindestens
     größer als die Versatztiefe selbst).
- **Verwendungsregel**: Funktionen, die einen Toleranzvergleich
  durchführen, akzeptieren den Schwellwert als optionalen Parameter
  mit dem entsprechenden `Toleranzen.*`-Default. Direkte
  Float-Gleichheit (`==`, `!=`) auf Längen, Winkel oder
  Flächeninhalten ist verboten. Plausibilitäts-Konstanten
  werden in der Bemessungs-Schicht (nicht in der Geometrie-
  Schicht) angewandt und produzieren `Warnung.*`-Werte, niemals
  `Resultat.Fehler`.
- **Edge Cases**:
  - **Nicht-Transitivität**: Aus
    `gleich_ε(a, b)` und `gleich_ε(b, c)` folgt **nicht**
    `gleich_ε(a, c)`. Insbesondere darf nicht durch wiederholten
    Gleichheitstest ein Cluster aufgebaut werden; für
    Punktverschmelzung ist ein expliziter Cluster-Algorithmus mit
    fester Bezugswahl zu verwenden.
  - **Skalierung**: Werden Modelle nicht in mm, sondern in einer
    anderen Längeneinheit verwendet, sind LAENGE_EPS und
    FLAECHE_EPS entsprechend zu skalieren. Eine globale Umstellung
    der Längeneinheit ist im aktuellen Domänenmodell **nicht**
    vorgesehen (CLAUDE.md: Längen in mm).
  - **Sehr große Bauteile**: Bei Koordinaten ≫ 10⁴ mm wächst der
    absolute Rundungsfehler einer Koordinate proportional. Falls
    künftig Modelle ≫ 10⁶ mm zugelassen werden, sind die Defaults
    neu zu prüfen und in diesem Eintrag zu aktualisieren.
  - **Plausibilitäts-Konstante an einem fachfremden Bauteil**:
    Eine Versatz-Tiefen-Faustregel auf einen Plattenwerkstoff
    angewandt liefert formal einen Wert, ist aber fachlich
    sinnfrei. Die Anwendung der Plausibilitäts-Konstanten auf
    Bauteile mit Faserrichtungs-Modus `STRUKTURIERT`, `SCHWACH`
    oder `KEINE` erzeugt eine eigene Warnung (siehe
    `hg_versatz.md` Edge Cases) und blockiert nicht.
  - **Plausibilitäts-Konstante außerhalb der Norm-Geltung**:
    Die NCI-NA.12-Konstanten sind für den DACH-Raum kalibriert.
    Bei einem Projekt unter anderem Normwerk (z. B. IRC in
    Nordamerika) wird die Konstante über das Konfigurationsobjekt
    der Bemessungs-Schicht überschrieben (Folgearbeit); der
    Default-Wert dieses Eintrags bleibt unverändert.

## Quellen

**Primär (normativ):**

- IEEE Std 754-2019, „IEEE Standard for Floating-Point Arithmetic".
- ISO/IEC/IEEE 60559:2020, „Information technology — Microprocessor
  Systems — Floating-point arithmetic".

**Sekundär:**

- Higham, N. J.: *Accuracy and Stability of Numerical Algorithms.*
  2. Auflage, SIAM, Philadelphia 2002.
- Goldberg, D.: „What Every Computer Scientist Should Know About
  Floating-Point Arithmetic". *ACM Computing Surveys* 23(1), 1991,
  S. 5–48.
- Knuth, D. E.: *The Art of Computer Programming, Vol. 2:
  Seminumerical Algorithms.* 3. Auflage, Addison-Wesley 1997.
- Shewchuk, J. R.: „Robust Adaptive Floating-Point Geometric
  Predicates". *Proc. 12th ACM Symp. Computational Geometry*, 1996.

**Nur in der Abgrenzung referenziert (nicht als Definitionsquelle):**

- DIN 18202:2019-07, „Toleranzen im Hochbau – Bauwerke".
- SIA 414:2024, „Maßtoleranzen im Bauwesen", Schweizerischer
  Ingenieur- und Architektenverein.
- JCGM 100:2008, „Evaluation of measurement data — Guide to the
  expression of uncertainty in measurement (GUM)".

**Quellen der Bearbeitungs-Plausibilitäts-Konstanten (verweisend
auf die zuständigen Bearbeitungs-Einträge):**

- DIN EN 1995-1-1/NA:2013-08, „Nationaler Anhang Deutschland zum
  Eurocode 5", NCI NA.12 „Zimmermannsmäßige Verbindungen"
  (Stützung der `VERSATZ_*`-Konstanten; Volltext-Verifikation
  ausstehend, siehe `hg_versatz.md` Quellenkonflikt).
- DIN 1052:2008-12 (zurückgezogen), Abschnitt 15
  „Zimmermannsmäßige Verbindungen" (Stützung der
  `ZAPFENBREITE_FAUSTREGEL_DRITTEL`- und `ZAPFENLOCH_*`-
  Konstanten; Sekundärquellen-belegt).
- SIA 265:2021, „Holzbau", Anhang A (Schweizer Pendant für die
  zimmermannsmäßigen Faustregeln; Volltext-Verifikation
  ausstehend).
- DIN EN 1995-1-1:2010-12 (Eurocode 5), Abschnitt 6.1.5
  (Querdruck) und Abschnitt 6.5 (Schubnachweis) als Bemessungs-
  Anker hinter den `ZAPFENLOCH_RESTHOLZ_*`- und `VERSATZ_VORHOLZ_*`-
  Konstanten.
- Mönck, W.; Rug, W.: *Holzbau – Bemessung und Konstruktion.*
  16. Auflage, Beuth, Berlin 2015, Kap. 7 (Sekundärquelle für die
  ⅓-Faustregeln von Kervtiefe und Zapfenbreite).
- Peter, M.; Scheer, C. (Hrsg.): *Holzbau-Taschenbuch.*
  Wiley-VCH, Berlin 2015, Kap. 19/20 (Sekundärquelle für die
  Versatzkamm-Mindesthöhe von 10 mm).
- Wikipedia, Lemma „Zapfenverbindung" (abgerufen 2026-05-14):
  Belegter Konsens für Zapfenluft 5–10 mm.

**Korpus (nicht autoritativ):**

- Wikipedia, Lemmata „Maschinenepsilon" und „Toleranz (Technik)"
  (abgerufen 2026-05-07).
