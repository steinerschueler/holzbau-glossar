---
title: Sprachregeln
description: Senkrecht / rechtwinklig / orthogonal — warum die Trennung wichtig ist.
---

# Sprachregeln

Im Glossar wird **„rechtwinklig"** oder **„im rechten Winkel zu"**
verwendet, wenn ein 90°-Winkel zwischen zwei geometrischen Objekten
gemeint ist (relationale Bedeutung). **„Senkrecht"** ist
ausschliesslich für **„lotrecht"** reserviert — in Fallrichtung
eines losgelassenen Gegenstands. **„Orthogonal"** ist Synonym zu
„rechtwinklig", wenn der mathematische Kontext es nahelegt.

Begründung: „Senkrecht" hat im Deutschen zwei nicht zur Deckung zu
bringende Bedeutungen — relational und absolut. Im Holzbau-Kontext,
in dem zugleich vom Welt-Koordinatensystem und von Bauteil-
Lokalsystemen die Rede ist, führt diese Mehrdeutigkeit zu
vermeidbarer Unklarheit.

Die zimmermannssprachlichen Realisierungen der absoluten
Lot-Bezogenheit — **Senkel** (parallel zur Lotachse) und
**Bleischnitt** (rechtwinklig zur Lotachse) — sind als eigene
Glossarbegriffe geführt und ersetzen die mehrdeutigen Wortlauten
„vertikaler Schnitt" / „horizontaler Schnitt".

## Tabelle der typischen Fälle

| Aussage | Bedeutung | Empfohlener Wortlaut |
|---|---|---|
| Faserrichtung im 90°-Winkel zur Last | relational | „rechtwinklig zur Faser" |
| Plattendicken-Achse im 90°-Winkel zur Plattenebene | relational | „rechtwinklig zur Plattenebene" |
| Wand steht in Schwerkraftrichtung | absolut | „die Wand steht senkrecht" |
| Stütze ist lotrecht ausgerichtet | absolut | „die Stütze steht senkrecht" |
| Schnittfläche parallel zur Lotachse | absolut (zimmermannssprachlich) | „Senkel" / „Senkelschnitt" |
| Schnittfläche rechtwinklig zur Lotachse | absolut (zimmermannssprachlich) | „Bleischnitt" / „Blei" |
| Vektor `n_hat` mit `n_hat · t_hat = 0` | mathematisch-relational | „n_hat steht orthogonal zu t_hat" |

## Weitere Konvention: Math-Notation

Mathematische Variablen in Code-Blöcken folgen einer ASCII-Suffix-
Konvention statt Unicode-Combining-Akzenten. Statt `n̂`, `v⃗`, `x̄`
wird `n_hat`, `v_vec`, `x_bar` geschrieben. Hintergrund: Render-
Stabilität in jeder Schriftart und in jedem Plain-Text-Konsumenten
(Mail, ePub, Konsole). Details siehe Sektion 11 in der
[HG-Konventionen-Volltext-Datei](hg-konventionen.md).
