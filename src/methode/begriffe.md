---
title: Begriffe und Schema
description: Begriffstypen, Pflichtfelder, Abgrenzungs-Logik.
---

# Begriffe und Schema

## Begriffstypen

Jeder Eintrag trägt genau einen von acht Begriffstyp-Werten. Die
Wahl ordnet den Eintrag einer strukturellen Rolle im Begriffssystem
zu, die orthogonal zur fachlichen Spezialisierungs-Linie
(Oberbegriff) ist.

| Wert | Bedeutung |
|---|---|
| `primitiv` | Unzerlegbares Konzept ohne weitere innere Struktur (Tupel von Skalaren, keine eigenen Subtypen). Beispiele: Punkt, Vektor, Gerade. |
| `generisch` | Eigenständiges Konzept mit interner Struktur, ggf. mit Subtypen, aber ohne Komposition aus mehreren Trägerbegriffen. Beispiele: Ebene, Polygon, Werkstoff. |
| `aggregat` | Komposition mehrerer eigenständiger Begriffe mit eigener Identität (UUID); trägt Konsistenzbedingungen über der Komposition. Beispiele: Verbindung, Tragwerk, Dach. |
| `partitiv` | Strenger Bestandteil eines Trägerbegriffs ohne eigenständige Existenz; Lebenszyklus an den Träger gekoppelt. Beispiele: Bearbeitung, Lage, Lagenstruktur. |
| `relation` | Beziehung zwischen Trägerbegriffen ohne eigene partitive Komposition. Beispiel: Bausystem als Mitgliedschafts-Sicht. |
| `bauteilrolle` | Konstruktiv definierter Bauteil-Subtyp mit rollenspezifischen geometrischen Constraints. Beispiele: Sparren, Pfette, Fusspfette. |
| `merkmal` | Eigenschaft oder Annotation an einem Trägerbegriff — ein **Wert**, kein **Objekt**. Beispiele: Faserrichtung, Dachneigung. |
| `hilfsbegriff` | Infrastrukturelle Festlegung der Geometrie-Schicht selbst, von vielen Begriffen vorausgesetzt. Beispiele: Toleranzen, Weltkoordinatensystem. |

Die Trennlinien sind im Hauptglossar präzisiert; bei Konflikt
zwischen einem Eintrag und der Begriffstyp-Tabelle wird der Eintrag
korrigiert, nicht die Tabelle.

## Pflichtfelder pro Eintrag

Jeder Hauptglossar-Eintrag trägt ein streng definiertes
YAML-Frontmatter. Die Pflichtfelder sind die Mindest-Belegmenge,
die ein Eintrag erfüllen muss, bevor er publiziert wird:

| Feld | Pflicht | Funktion |
|---|---|---|
| `id` | ✓ | Eindeutige Kennung, in Cross-Links verwendet (`bauteilachse`, `kerve`). |
| `benennung` | ✓ | Menschenlesbare Hauptform — die Form, die im Glossar als Titel und in Tabellen erscheint. |
| `synonyme` | empfohlen | Gleichwertige Alternativ-Benennungen (gefunden in Norm-Quellen oder regional). Werden im JSON-LD `alternateName` ausgespielt. |
| `abgelehnte_benennungen` | empfohlen | Verwechselbare oder falsch verwendete Benennungen, die das Glossar bewusst NICHT verwendet — mit Begründung im Fließtext. |
| `oberbegriff` | ✓ | ID eines anderen HG-Eintrags, der den Oberbegriff stellt. |
| `begriffstyp` | ✓ | Einer der acht oben gelisteten Werte. |
| `voraussetzungen` | ✓ | IDs anderer Einträge, die zum Verständnis nötig sind. Müssen existieren (kein Forward-Verweis). |
| `abgrenzung_zu` | ✓ | IDs von Geschwister-/Nachbarbegriffen, gegen die abgegrenzt wird. Forward-Verweise zulässig. |
| `status` | ✓ | `entwurf` / `in_revision` / `final`. |
| `subglossar_pendant` | ✓ | `notwendig` / `optional` / `nein` — steuert die Pflicht zum Subglossar-Pendant. |
| `quellen_primär` | empfohlen | Normen, Lehrbücher, anerkannte Standards (Tier *Hoch* / *Mittel-Hoch*). |
| `quellen_sekundär` | empfohlen | Wikipedia, Hersteller-Doku, Fach-Foren (Tier *Mittel* und niedriger). |
| `quellenkonflikt` | optional | Prosa-Block, wenn primär- oder sekundärseitige Quellen sich widersprechen. Konflikt wird explizit gemacht und entschieden. |

Felder dürfen nicht still gelassen werden. Wenn `synonyme` leer ist,
steht es als `synonyme: []` da — die explizite Aussage ist Teil der
Pflege-Disziplin.

## Abgrenzung gegen Geschwister-Begriffe

Jeder Eintrag dokumentiert seine Abgrenzung zu fachlich benachbarten
Begriffen explizit. Die Felder `abgrenzung_zu:`,
`abgelehnte_benennungen:` und der Quellenkonflikt-Block bilden
zusammen ein engmaschiges Trenn-Geflecht, das Begriffsdrift in der
Praxis sichtbar macht und gegen den korrekten Eintrag leitet.

Forward-Verweise — Abgrenzungen gegen Begriffe, die noch keinen
eigenen Eintrag haben — sind im `abgrenzung_zu:`-Feld zulässig, in
`voraussetzungen:` nicht. Begründung: Abgrenzungen benötigen den
abzugrenzenden Begriff nicht definitorisch, sondern nur als
Ankerwort; Voraussetzungen dagegen tragen die zirkelfreie
Aufbaureihenfolge des Glossars und müssen auf existierende Einträge
zeigen.
