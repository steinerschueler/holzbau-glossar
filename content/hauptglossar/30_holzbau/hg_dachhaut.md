---
id: dachhaut
benennung: Dachhaut
synonyme: []
abgelehnte_benennungen: [Dachdeckung, Dacheindeckung, Dachfläche, Dachschräge, Dachaufbau, "roof skin", "roof covering"]
oberbegriff: null
begriffstyp: generisch
voraussetzungen: [dachflaeche, polygon, ebene, toleranzen]
abgrenzung_zu: [dachflaeche, dach, dachaufbau, eindeckung, dachabdichtung, unterdach]
status: entwurf
subglossar_pendant: notwendig
quellen_primär:
  - "Musterbauordnung (MBO) 2002, zuletzt geändert 2016, § 32 'Dächer' (Bezugnahme auf Dachhaut als wettertrennende äußere Schicht)."
  - "SIA 232/1:2020 'Geneigte Dächer', Schweizerischer Ingenieur- und Architektenverein, Abschnitt 1 (Begriffe) und Abschnitt 2 (Anforderungen an die Dachhaut als wetterabführende Außenschicht)."
  - "SIA 271:2007 'Abdichtungen von Hochbauten', Abschnitt 1 (Begriffe) — für Flachdach-Abdichtung als Dachhaut-Variante."
  - "DIN 18531-1:2017-07 'Abdichtung von Dächern sowie von Balkonen, Loggien und Laubengängen – Teil 1', Abschnitt 3 (Begriffe)."
  - "DIN 18338:2019-09 'VOB Teil C: Dachdeckungs- und Dachabdichtungsarbeiten', Abschnitt 0 (Hinweise zum Leistungsbereich)."
quellen_sekundär:
  - "Lignum (Hrsg.): Lignatec 'Geneigte Dächer in Holzbauweise', Lignum, Zürich, aktuelle Auflage."
  - "Mönck, W.; Rug, W.: Holzbau – Bemessung und Konstruktion. 16. Aufl., Beuth Verlag 2015."
  - "Gerner, M.: Fachwerk. DVA, 7. Aufl. 2007."
  - "Wikipedia, Lemma 'Dachhaut' (abgerufen 2026-05-08) — Korpusbeleg für die enge Lesart."
quellenkonflikt: |
  Im Sprachgebrauch existieren zwei Lesarten:
  (a) **eng**: Dachhaut = nur die äußerste, wetter­trennende Schicht
      (Eindeckung bei geneigten Dächern, Abdichtung bei Flachdächern).
  (b) **weit**: Dachhaut = der gesamte Schichtaufbau über dem Tragwerk.
  Die enge Lesart (a) ist normativ besser belegt (MBO, Landes­bau­ordnungen,
  DIN 18531, SIA 232/1) und entspricht der Auffassung der Dachdecker,
  die die Dachhaut sogar als rein geometrische, fiktive Hüllfläche über
  den höchsten Punkten der Eindeckung verstehen — also nicht als
  materielles Bauteil. Die weite Lesart (b) wird in diesem Glossar unter
  dem eigenständigen Begriff `dachaufbau` geführt; damit ist die
  Polysemie aufgelöst.

  **Festlegung dieses Glossars**: Dachhaut ist die geometrisch
  modellierte **äußere Hüllfläche** des Daches — eine fiktive Fläche,
  die sich über die höchsten Punkte der Eindeckung bzw. der
  Abdichtung spannt. Sie ist kein materielles Bauteil, sondern ein
  abgeleitetes geometrisches Objekt. Diese Festlegung ist konsistent
  mit MBO, DIN 18531, SIA 232/1 und mit dem Dachdecker-Sprachgebrauch.
  Die Synonyme `Dachdeckung` und `Dacheindeckung` werden für die
  geneigte-Dach-Lesart akzeptiert; bei Flachdächern wird häufiger von
  `Dachabdichtung` gesprochen — diese wird als verwandter, hier nicht
  selbständig definierter Begriff in `abgrenzung_zu` geführt.

  **Wahl des `begriffstyp`**: `merkmal` statt früher `aggregat`. Die
  Dachhaut ist nach dieser Definition kein Bauteil-Aggregat aus
  Schichten, sondern eine geometrische Größe (Hüllfläche) eines
  Daches. Ein Oberbegriff `hueltflaeche` / `flaeche` ist im Glossar
  noch nicht definiert; bis zu dessen Einführung wird
  `oberbegriff: null` gesetzt.
---

## Prosa-Definition

Eine **Dachhaut** ist die fiktive, geometrisch glatte Hüllfläche, die
sich von außen über die höchsten Punkte der äußersten wetter­trennenden
Schicht eines Daches spannt — bei geneigten Dächern über die
Eindeckung (Ziegel, Schindeln, Blech), bei Flachdächern über die
Abdichtung (Bitumenbahn, Dichtungsfolie, Flüssigkunststoff).

## Mathematische Definition

Sei

- 𝒟 = { D₁, …, D_m } mit m ≥ 1 eine endliche, nicht-leere Familie
  von Dachflächen D_i = (E_i, P_i, n_{a,i}) im Sinne von
  `dachflaeche`,
- F := ⋃_{i=1..m} F(P_i) ⊂ ℝ³ die geometrische
  Vereinigungsfläche der Dachflächen (Trägerbereich),
- M ⊂ ℝ³ eine endliche, nicht-leere Punktwolke der **Eindeckungs-
  bzw. Abdichtungs-Oberseite**: für jedes Eindeckungs- bzw.
  Abdichtungselement (Ziegel, Schindel, Blechtafel, Bahn, Folie)
  enthält M die Menge seiner äußeren Oberflächenpunkte; M ist
  kompakt und liegt vollständig im Halbraum
  ⋃_{i=1..m} { x ∈ ℝ³ | ⟨n_{a,i}, x − p_{0,i}⟩ ≥ 0 }.

Für jeden Punkt q ∈ F(P_i) sei

```
ρ_i(q) := sup { t ∈ ℝ | ∃ x ∈ M : x = q + t · n_{a,i}, t ≥ 0 }
```

der **Höhenabtrag** der Eindeckungspunktwolke entlang der äußeren
Normalen der zugehörigen Dachfläche, mit der Konvention
sup ∅ := 0. Ist q ∈ F(P_i) ∩ F(P_j) auf einer gemeinsamen
Randstrecke zweier Dachflächen, so wird ρ als Maximum über die
zuständigen Indizes genommen.

Dann ist die **Dachhaut** des Daches die Bildmenge

```
H := { q + ρ(q) · n_{a(q)} | q ∈ F }   ⊂ ℝ³,
```

wobei n_{a(q)} die äußere Normale der für q lokal zuständigen
Dachfläche bezeichnet.

Äquivalent (parametrisch über jede Dachfläche):

```
H_i := { q + ρ_i(q) · n_{a,i} | q ∈ F(P_i) },
H   := ⋃_{i=1..m} H_i.
```

Die Funktion h_i : F(P_i) → ℝ, q ↦ ρ_i(q), heißt
**Höhenfunktion** der Dachhaut über der Dachfläche D_i; sie liefert
in der Praxis stückweise glatte, im Bereich von wenigen
Zentimetern variierende Werte (Profilhöhe der Eindeckung).

## Wohldefiniertheit

- **Existenz**: Für jede nicht-leere, kompakte, oberhalb der
  Dachflächen liegende Punktwolke M ist ρ_i als Supremum einer
  beschränkten, abgeschlossenen Menge wohldefiniert und endlich;
  das Supremum wird angenommen, also ist ρ_i eine Funktion
  F(P_i) → ℝ_{≥0}.
- **Eindeutigkeit**: H hängt deterministisch von 𝒟 und M ab. Die
  Wahl der Vorzeichen ist durch die äußere Normale n_{a,i} jeder
  Dachfläche festgelegt (siehe `dachflaeche`).
- **Verhalten an gemeinsamen Rändern (First, Grat, Kehle)**: Auf
  gemeinsamen Randstrecken zweier Dachflächen wird ρ als
  Maximum über die anliegenden Dachflächen genommen. Damit ist H
  auch dort wohldefiniert, allerdings im Allgemeinen knickbehaftet
  — was der baulichen Realität entspricht (Firstziegel,
  Gratabdeckung).
- **Grenzfall leerer Eindeckung** (M = ∅, etwa Rohbau): ρ ≡ 0,
  H = F. Die Dachhaut fällt mit der Dachfläche zusammen. Dieser
  Grenzfall ist explizit zugelassen und sinnvoll (z. B. zur
  Visualisierung des unbedeckten Tragwerks-Resultats).
- **Konsistenz mit `dachflaeche`**: Die Dachfläche bleibt
  zweidimensional, dickenlos; die Dachhaut liegt parallel-versetzt
  bzw. mit Profilrelief über der Dachfläche. Die Dachhaut ist
  niemals identisch mit der Dachfläche, außer im Grenzfall ρ ≡ 0.
- **Nicht-Zirkularität**: Die Definition verwendet die Primitive
  Punkt, Vektor, Halbgerade, Supremum sowie die bereits definierten
  Begriffe `dachflaeche`, `polygon`, `ebene`. Sie verweist auf
  `eindeckung` und `dachabdichtung` nur erläuternd, nicht definitorisch
  — die Punktwolke M wird unabhängig von der Materialklassifikation
  spezifiziert.

## Erläuterung (nicht normativ)

Die Dachhaut ist nach dieser Festlegung **kein materielles Bauteil**,
sondern eine **fiktive Fläche**, die das Dach geometrisch nach außen
abschließt. Die Dachdecker-Tradition erfasst die Dachhaut genau so:
als die Fläche, die man berührt, wenn man auf das fertige Dach faßt
— über die Pfannenkämme der Ziegel, über die obersten Falze der
Blechdeckung, über die Oberkante der Bitumenbahn.

Diese Modellierung hat drei Konsequenzen:

1. **Dachhaut ist geometrisch, nicht materiell.** Welche Schichten
   konkret unter ihr liegen, regelt der `dachaufbau`. Die Dachhaut
   selbst ist eine Hüllfläche.
2. **Dachhaut ist abgeleitet, nicht primitiv.** Sie wird aus der
   Dachflächengeometrie und der Eindeckungs-Punktwolke berechnet —
   nicht direkt eingegeben.
3. **Dachhaut ist eindeutig.** Zu einem gegebenen Dach mit
   gegebener Eindeckung gibt es genau eine Dachhaut.

Bei geneigten Dächern entsteht durch das Profil der Eindeckung
(Ziegelprofil, Blechfalz, Wellenstruktur) eine sichtbare
Reliefstruktur in H, die aber im Modell oft glättend approximiert
wird (mittlere Hüllfläche im Abstand der mittleren Profilhöhe von
der Dachfläche). Bei Flachdächern ist H typischerweise sehr nahe
an einer parallelen Verschiebung der Dachfläche um die
Abdichtungsdicke nach außen.

Die Synonyme `Dachdeckung` und `Dacheindeckung` sind für geneigte
Dächer gebräuchlich. Bei Flachdächern wird die wettertrennende
Schicht meist `Abdichtung` oder `Dachabdichtung` genannt; die
Dachhaut als Hüllfläche existiert in beiden Fällen, das darunter
liegende Material wechselt.

## Beziehungen

- **Oberbegriff**: derzeit `null`. Künftig `hueltflaeche` bzw.
  `flaeche` (geometrisches Hüllobjekt, oberer Verband im Sinne der
  Computational Geometry). Eintrag wird angelegt, sobald weitere
  Hüllflächen-Begriffe (Wandhülle, Geländehülle) hinzukommen.
- **Verwendung**:
  - Geometrisches Außen-Merkmal eines `dach`.
  - Außenschicht-Repräsentant des `dachaufbau` (die Dachhaut ist
    die obere Hüllfläche der äußersten Schicht des Dachaufbaus).
- **Abgrenzung**:
  - **Dachfläche** (`dachflaeche`): rein geometrische,
    zweidimensionale Bezugsebene, dickenlos. Die Dachhaut liegt
    **über** der Dachfläche im Halbraum der äußeren Normalen, im
    allgemeinen mit Abstand > 0. Bei leerer Eindeckung fallen
    beide zusammen.
  - **Dach** (`dach`): das Bauteil-Aggregat aus Tragwerk,
    Dachflächen und Dachaufbau. Die Dachhaut ist eine abgeleitete
    geometrische Größe des Daches, kein eigenständiges Bauteil.
  - **Dachaufbau** (`dachaufbau`): die materielle Schichtfolge
    zwischen Tragwerk und Dachhaut (Dampfbremse, Dämmung,
    Unterdach, Konterlattung, Traglattung, Eindeckung). Im
    Sprachgebrauch oft fälschlich „Dachhaut" genannt — siehe
    Quellenkonflikt. In diesem Glossar streng getrennt: Dachhaut
    ist Geometrie, Dachaufbau ist Materialfolge.
  - **Eindeckung** (`eindeckung`, bereits angelegt): die
    äußerste **materielle** Schicht eines geneigten Daches
    (Ziegel, Schindeln, Blech). Die Dachhaut ist die Hüllfläche
    **über** der Eindeckung; Dachhaut und Eindeckung sind nicht
    identisch, aber die Hüllfläche wird aus der Eindeckungs-
    Oberseitenpunktwolke konstruiert.
  - **Dachabdichtung** (eigener Eintrag folgt, falls relevant):
    die wassertragende Schicht eines Flachdaches (Bitumenbahn,
    Folie, Flüssigkunststoff). Bei Flachdächern wird die Dachhaut
    aus der Abdichtungs-Oberseitenpunktwolke konstruiert.
    Begrifflich abzugrenzen, weil bei Flachdächern „Dachhaut" und
    „Abdichtung" im Alltagssprachgebrauch oft vertauscht werden.
  - **Unterdach** (`unterdach`, bereits angelegt): die
    zweite, unter der Eindeckung liegende wasserführende Ebene.
    Nicht Bestandteil der Dachhaut, sondern des Dachaufbaus.

## Implementierungshinweis

Datentyp (Domänen-Schicht, Kotlin, Schicht `domain.bauteil`):

```
data class Dachhaut(
    val dachflaechen: List<Dachflaeche>,         // 𝒟, Trägerbereich F = ⋃ F(P_i)
    val hoehenfunktion: (Punkt, Int) -> Double  // ρ_i(q) für i = Index der Dachfläche
) {
    init {
        // 1. dachflaechen.isNotEmpty()                  → sonst Entartet.LeerTraeger
        // 2. hoehenfunktion liefert Werte ≥ 0           → ansonsten Entartet.NegativeHoehe
    }

    fun punktAuf(q: Punkt, i: Int): Punkt =
        q + dachflaechen[i].aeussereNormale * hoehenfunktion(q, i)

    fun mittlereDicke(): Double = /* numerische Integration über F(P_i) */
}
```

- **Einheit**: Längen und Höhenfunktionswerte in mm (Double).
- **Repräsentation**: Die Dachhaut wird selten direkt eingegeben.
  Sie wird typischerweise aus dem `dachaufbau` und der konkreten
  Eindeckung abgeleitet — entweder analytisch (für Flachdächer
  mit konstanter Abdichtungsdicke ρ ≡ const) oder numerisch (für
  Profilziegel als obere Hüllfläche der Pfannenkämme).
- **Invarianten** (in `init` prüfen, bei Verletzung
  `Resultat.Fehler` oder `Entartet`-Variante zurückgeben, niemals
  Exception werfen):
  1. `dachflaechen.isNotEmpty()` ⇒ sonst `Entartet.LeerTraeger`.
  2. `hoehenfunktion` liefert für jedes (q, i) einen Wert
     ≥ −Toleranzen.LAENGE_EPS ⇒ sonst `Entartet.NegativeHoehe`.
  3. `hoehenfunktion` ist beschränkt durch eine plausible
     Maximalhöhe (z. B. < 200 mm für übliche Eindeckungen);
     Verletzung als Warnung, nicht als harter Fehler.
- **Edge Cases**:
  - **Rohbau ohne Eindeckung**: ρ ≡ 0, Dachhaut = Dachfläche.
    Zulässig.
  - **Flachdach mit homogener Folienabdichtung**: ρ = const,
    Dachhaut ist parallele Verschiebung der Dachfläche.
  - **Profilziegel** (z. B. Doppelmuldenfalzziegel): ρ schwankt
    periodisch über der Fläche; in der App typischerweise als
    mittlere Hüllfläche dargestellt.
  - **Knicke an First/Grat**: Dachhaut ist nicht glatt, sondern
    knickbehaftet; entspricht der Realität (Firstabdeckung).
- **Abgeleitete Eigenschaften** (als Funktionen, keine Felder):
  - `mittlereDicke(): Double` (mm) = mittlerer Wert von ρ über F.
  - `gesamtflaeche(): Double` (mm²) = Flächeninhalt von H,
    leicht größer als der Flächeninhalt von F (Schrägstellung
    durch ρ-Variation).
  - `liegtAussen(p: Punkt, eps): Boolean` = Test, ob Punkt p in
    der nach außen weisenden Halbraumseite von H liegt.

## Quellen

**Primär (normativ):**

- Musterbauordnung (MBO) 2002, zuletzt geändert 2016, § 32.
- SIA 232/1:2020, „Geneigte Dächer", Schweizerischer Ingenieur-
  und Architektenverein, Abschnitt 1 und 2.
- SIA 271:2007, „Abdichtungen von Hochbauten", Schweizerischer
  Ingenieur- und Architektenverein, Abschnitt 1.
- DIN 18531-1:2017-07, „Abdichtung von Dächern sowie von Balkonen,
  Loggien und Laubengängen – Teil 1", Abschnitt 3.
- DIN 18338:2019-09, „VOB Teil C: Dachdeckungs- und
  Dachabdichtungsarbeiten", Abschnitt 0.

**Sekundär:**

- Lignum (Hrsg.): *Lignatec — Geneigte Dächer in Holzbauweise.*
  Lignum, Zürich, aktuelle Auflage.
- Mönck, W.; Rug, W.: *Holzbau – Bemessung und Konstruktion.*
  15. Auflage, Beuth Verlag 2015.
- Gerner, M.: *Fachwerk – Instandsetzung, Sanierung, Neubau.*
  DVA, 7. Auflage 2007.

**Korpus (nicht autoritativ):**

- Wikipedia, Lemma „Dachhaut" (abgerufen 2026-05-08).
