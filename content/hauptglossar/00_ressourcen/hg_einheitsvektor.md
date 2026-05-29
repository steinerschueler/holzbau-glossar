---
id: einheitsvektor
benennung: Einheitsvektor
synonyme: ["Normierter Vektor", "Vektor mit Norm 1", "Einheitsrichtungsvektor"]
abgelehnte_benennungen: [Richtung, Richtungsvektor, Normalvektor, "unit vector", "direction"]
oberbegriff: vektor
begriffstyp: primitiv
voraussetzungen: [vektor, toleranzen]
abgrenzung_zu: [vektor, faserrichtung, gerade]
status: entwurf
subglossar_pendant: optional  # Überschreibung primitiv-Default required → optional: normierte Sonderform des Vektors (Norm = 1), mathematische Feinheit ohne Praxisbegriff; didaktische Substanz liegt bei vektor und faserrichtung (HG_KONVENTIONEN §7).
quellen_primär:
  - "DIN ISO 80000-2:2022-08, Abschnitt 2 (Geometrie und Vektoren), Symbol 2-7.6 'Einheitsvektor'."
  - "ISO 80000-2:2019, Abschnitt 2 'Vektoren und Tensoren', Eintrag zum normierten Vektor."
quellen_sekundär:
  - "Bronstein, I. N. et al.: Taschenbuch der Mathematik. Kap. 3.5.1.5 'Einheitsvektor', Kap. 4.1.2 'Norm und normierte Vektoren'."
  - "Fischer, G.: Lineare Algebra. 19. Aufl., Springer Spektrum 2020, Kap. 0.3 'Skalarprodukt und Norm'."
  - "Bär, C.: Elementare Differentialgeometrie. de Gruyter 2010, Kap. 1.1 (Sphäre S² als Menge der Einheitsvektoren)."
quellenkonflikt: |
  Keine Holzbau-Norm definiert den Einheitsvektor; DIN ISO 80000-2 führt
  ihn als Vektor mit Norm 1 ein, gibt jedoch keine numerische Schwelle
  für die Norm-Bedingung an. Eigene Festlegung: ein Einheitsvektor ist
  ein Vektor v ∈ ℝ³ mit | ‖v‖² − 1 | ≤ NORM_EPS (siehe `toleranzen`).
  Die exakte Bedingung ‖v‖ = 1 ist die mathematische Idealform; die
  Toleranz-Bedingung ist die in der Domänen-Schicht prüfbare Variante.
  Diese Festlegung ist konsistent mit ISO 80000-2 und der zitierten
  Lehrbuchliteratur.
---

## Prosa-Definition

Ein **Einheitsvektor** ist ein Vektor des dreidimensionalen reellen
Vektorraumes ℝ³, dessen euklidische Norm gleich 1 ist und der dadurch
eine reine Richtung ohne metrischen Längenanteil repräsentiert.

## Mathematische Definition

Sei

- v ∈ ℝ³ ein Vektor (siehe `vektor`),
- ‖v‖ := √(v_x² + v_y² + v_z²) seine euklidische Norm,
- NORM_EPS ∈ ℝ_{>0} die Norm-Toleranz aus `toleranzen`.

Dann heißt v **Einheitsvektor** genau dann, wenn

```
‖v‖ = 1     (mathematische Idealform)
```

bzw. in der Domänen-Schicht prüfbar

```
| ‖v‖² − 1 | ≤ NORM_EPS     (numerische Form).
```

Die Menge aller (idealen) Einheitsvektoren ist die **Einheitssphäre**

```
S² := { v ∈ ℝ³ | ‖v‖ = 1 } ⊂ ℝ³.
```

**Konstruktion durch Normierung**: Für einen Vektor v ∈ ℝ³ mit
‖v‖² > NORM_EPS ist

```
v_hat := v / ‖v‖ ∈ S²
```

der zu v gehörige Einheitsvektor; v_hat ist genau dann definiert, wenn v
nicht der Nullvektor ist (siehe Wohldefiniertheit).

## Wohldefiniertheit

- **Existenz von v_hat**: Für jeden Vektor v ∈ ℝ³ \ {0} ist ‖v‖ > 0, also
  ist v_hat = v / ‖v‖ wohldefiniert. Es gilt ‖v_hat‖ = ‖v‖ / ‖v‖ = 1, somit
  v_hat ∈ S².
- **Eindeutigkeit von v_hat**: v_hat ist eindeutig bestimmt durch v, da die
  Division durch eine eindeutige positive reelle Zahl eine Bijektion
  ist.
- **Vorzeichen-Mehrdeutigkeit der Richtung**: Ein nicht ausgerichteter
  geometrischer Begriff der „Richtung" (z. B. die Richtung einer
  Geraden) wird durch zwei antipodale Einheitsvektoren {v_hat, −v_hat}
  repräsentiert. Der Einheitsvektor selbst ist orientiert; die Wahl
  des Vorzeichens ist Teil seiner Identität.
- **Numerische Wohldefiniertheit der Konstruktion**: Die Bedingung
  ‖v‖² > NORM_EPS sichert, dass die Division v / ‖v‖ in IEEE 754
  binary64 ohne katastrophale Auslöschung ausgewertet werden kann
  (siehe `toleranzen#norm_eps`).
- **Nicht-Zirkularität**: Die Definition verwendet ausschließlich
  `vektor` und `toleranzen`; sie kommt nicht in ihrer eigenen
  Definition vor.

## Erläuterung (nicht normativ)

Ein Einheitsvektor ist die mathematische Form einer **reinen
Richtung**: er hat keine Länge im fachlichen Sinn (er ist
dimensionslos), sondern beschreibt nur, **wohin** ein
geometrisches Objekt zeigt. In der Holzkonstruktion treten
Einheitsvektoren typisch in folgenden Rollen auf:

- **Normalenvektor** einer Ebene oder eines Halbraumes
  (Hesse-Normalform: ‖n_hat‖ = 1, siehe `ebene`, `halbraum`).
- **Normalenvektor** einer Dachfläche (siehe `dachflaeche`).
- **Faserrichtung** eines Bauteils, also die lokale Hauptachse der
  Holzfaser (siehe `faserrichtung`).
- **Achsenrichtung** einer Geraden oder Halbgeraden in normierter
  Form.
- **Basisvektoren** des Welt-Koordinatensystems
  (e_x, e_y, e_z ∈ S²).

Die zentrale konzeptionelle Trennung zum allgemeinen Vektor ist:
ein **Vektor** kann sowohl Längen- als auch Richtungsinformation
tragen (z. B. die Differenz zweier Punkte in mm); ein
**Einheitsvektor** trägt **nur** Richtungsinformation und ist
dimensionslos. In der Domänen-Schicht ist diese Trennung
typkonsistent durch Konvention sichergestellt: Funktionen, die
einen Einheitsvektor erwarten, prüfen die Norm-Bedingung am
Eingang.

## Beziehungen

- **Oberbegriff**: `vektor`. Ein Einheitsvektor ist ein Vektor mit
  dem Zusatzmerkmal ‖v‖ = 1.
- **Teilbegriffe (Spezialisierungen / Rollen)**:
  - **Faserrichtung** (`faserrichtung`): Einheitsvektor in der
    semantischen Rolle „lokale Hauptachse der Holzfaser eines
    Bauteils".
  - **Normalenvektor** einer Ebene (`ebene.normale`): Einheitsvektor
    in der Rolle „rechtwinklig zu einer Ebene".
  - **Normalenvektor** eines Halbraumes (`halbraum.normale`):
    Einheitsvektor in der Rolle „auswärts gerichtete Normale auf
    der Begrenzungsebene".
  - **Achsenrichtung** einer Geraden (`gerade.richtung` in
    normierter Form): Einheitsvektor in der Rolle „Richtung einer
    Geraden", bis auf das Vorzeichen.
- **Abgrenzung**:
  - **`vektor`** (allgemein): kann beliebige Norm haben, insbesondere
    auch Längeninformation (z. B. ein Verschiebungsvektor in mm).
    Ein Einheitsvektor verzichtet auf Längeninformation und trägt
    ausschließlich Richtung.
  - **„Richtung"** als eigener Begriff wird in diesem Glossar
    bewusst **nicht** eingeführt: in der App ist die kanonische
    Repräsentation einer Richtung ein Einheitsvektor; der Begriff
    „Richtung" tritt nur im Erläuterungstext auf. Eine ungerichtete
    Richtung (Linie ohne Orientierung) wird durch das antipodale
    Paar {v_hat, −v_hat} ⊂ S² repräsentiert.
  - **Nullvektor** (siehe `vektor`): ‖v‖ = 0 ist der einzige Vektor,
    aus dem **kein** Einheitsvektor durch Normierung gewonnen werden
    kann. Versuche der Normierung des Nullvektors liefern die
    Entartet-Variante `EntartetGeometrie.Nullrichtung`.
  - **`faserrichtung`**: ein Einheitsvektor in einer holzbau-
    spezifischen semantischen Rolle. Strukturell identisch zu einem
    allgemeinen Einheitsvektor, aber zusätzlich annotiert mit der
    Bedeutung „Materialachse".

## Implementierungshinweis

Datentyp (Domänen-Schicht, Kotlin, Schicht `domain.geometrie`):

```
package domain.geometrie

/**
 * Einheitsvektor: Vektor mit ‖v‖ = 1 ± NORM_EPS.
 * Glossar: hg_einheitsvektor.md
 *
 * Wrapper-Typ um Vektor, der die Einheitsnorm zur Konstruktionszeit
 * prüft. Die Domänen-Schicht verwendet Einheitsvektor überall dort,
 * wo eine reine Richtung erwartet wird (Normalenvektoren, Faser-
 * richtung, Geraden-Richtung in normierter Form).
 */
public class Einheitsvektor private constructor(public val vektor: Vektor) {

    // Properties: dx, dy, dz, normQuadrat, norm — delegiert an `vektor`.
    // Operatoren: unaryMinus, dot, cross, get.
    // Methoden: istGleich, istParallelZu, istAntiparallelZu, istOrthogonalZu.

    public companion object {
        /** Kanonische Achsen, rechnerisch normiert; ueber `bildeUngeprueft`. */
        public val EX: Einheitsvektor = bildeUngeprueft(Vektor.EX)
        public val EY: Einheitsvektor = bildeUngeprueft(Vektor.EY)
        public val EZ: Einheitsvektor = bildeUngeprueft(Vektor.EZ)

        /**
         * Erzeugt einen Einheitsvektor durch Normierung von [v]. Wirft niemals.
         * Liefert
         *  - `Resultat.Erfolg(v / ‖v‖)`, wenn `v` finit und `‖v‖² > eps`,
         *  - `Resultat.Fehler(EntartetGeometrie.NichtFinit)`, wenn eine
         *    Komponente NaN oder ±∞ ist,
         *  - `Resultat.Fehler(EntartetGeometrie.Nullrichtung)`, wenn
         *    `‖v‖² ≤ eps`.
         */
        public fun bilde(
            v: Vektor,
            eps: Double = Toleranzen.NORM_EPS,
        ): Resultat<Einheitsvektor, EntartetGeometrie> {
            if (!v.istFinit()) return Resultat.Fehler(EntartetGeometrie.NichtFinit)
            if (v.normQuadrat <= eps) return Resultat.Fehler(EntartetGeometrie.Nullrichtung)
            return Resultat.Erfolg(Einheitsvektor(v * (1.0 / v.norm)))
        }

        /**
         * Erzeugt einen Einheitsvektor **ohne** Norm-Pruefung. Aufrufer
         * garantiert `‖normalisierter‖ ≈ 1`. Vorgesehen fuer Operationen, die
         * rechnerisch einen Einheitsvektor liefern (Vorzeichenumkehr,
         * Achsenkonstanten).
         */
        internal fun bildeUngeprueft(normalisierter: Vektor): Einheitsvektor =
            Einheitsvektor(normalisierter)
    }
}
```

- **Einheit**: dimensionslos. Ein Einheitsvektor trägt **nie**
  Längeninformation in mm.
- **Invariante**: | (v.dx² + v.dy² + v.dz²) − 1 | ≤ Toleranzen.NORM_EPS.
  Die Invariante wird in der Companion-Factory `bilde(...)` zur
  Konstruktionszeit geprüft; ein bereits konstruierter
  `Einheitsvektor` darf von Klienten als invariant angenommen werden.
- **Edge Cases**:
  - **Nullvektor** (‖v‖² ≤ NORM_EPS): `Einheitsvektor.bilde(...)`
    liefert `EntartetGeometrie.Nullrichtung`. Der Aufrufer
    entscheidet über die fachliche Reaktion (Fehlermeldung im UI,
    Defaultachse usw.).
  - **NaN/±∞ in einer Komponente**: durch `bilde(...)` abgefangen
    (Prüfung `!v.istFinit()` erfolgt **vor** dem Norm-Test); das
    Ergebnis ist `EntartetGeometrie.NichtFinit`.
  - **Sehr kleine, aber nicht-null Vektoren** (NORM_EPS < ‖v‖² ≪ 1):
    werden numerisch sicher normiert, bleiben aber fachlich
    fragwürdig (z. B. fast-paralleler Sparrenanschnitt). Die
    fachliche Plausibilität ist Aufgabe des Aufrufers, nicht des
    Konstruktors.
  - **Antipodale Mehrdeutigkeit**: v_hat und −v_hat sind beides gültige
    Einheitsvektoren. Wo nur die ungerichtete Richtung relevant ist
    (z. B. Geraden-Richtung), ist die Vorzeichenwahl konventionell
    festzulegen (siehe Glossareintrag des verwendenden Begriffs).
- **Verwendungsregel**: Funktionen, die eine Richtung erwarten
  (Normalenvektor, Faserrichtung, Achse), nehmen `Einheitsvektor` als
  Parametertyp, **nicht** `Vektor`. Dadurch wird die
  Norm-Invariante typsicher kommuniziert und am API-Rand erzwungen.

## Quellen

**Primär (normativ):**

- DIN ISO 80000-2:2022-08, „Größen und Einheiten – Teil 2: Mathematik".
- ISO 80000-2:2019.

**Sekundär:**

- Bronstein, I. N.; Semendjajew, K. A.; Musiol, G.; Mühlig, H.:
  *Taschenbuch der Mathematik.*
- Fischer, G.: *Lineare Algebra.* 19. Aufl., Springer Spektrum 2020.
- Bär, C.: *Elementare Differentialgeometrie.* 2. Aufl., de Gruyter 2010.

**Korpus (nicht autoritativ):**

- Wikipedia, Lemma „Einheitsvektor" (abgerufen 2026-05-08).
