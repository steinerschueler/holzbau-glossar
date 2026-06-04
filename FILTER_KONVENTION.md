# Filter-Konvention: Transfer Zimmermannsapp → holzbau-glossar

Diese Konvention regelt, **was beim Übernehmen der Hauptglossar-Einträge
aus der Zimmermannsapp (ZMA) in die öffentliche Webseite holzbau-glossar
(HBG) entfernt wird** und wie. Sie ist die Referenz für `hg_public_filter.py`
(läuft in `sync.sh`) und für das Markieren in der ZMA-Quelle.

## Grundsatz

- **ZMA (`zimmermann_app/hauptglossar/`) ist Single Source of Truth.** Dort
  steht der vollständige Eintrag inklusive App-Implementierung und
  Autoren-Prozess-Notizen — das gehört dort hin.
- **HBG (`content/hauptglossar/`) ist der öffentliche Spiegel.** Er speist
  Website, JSON-API (`/api/v1/`) und den **Zenodo-DOI-Tarball** (`content/**`
  liegt im Archiv — daher muss `content/` selbst sauber sein, nicht erst der
  gebaute HTML-Output).
- **Nur die HG-Einträge** (`hg_*.md`) werden gefiltert. **Nicht** gefiltert:
  `HG_KONVENTIONEN.md`, die Subglossar-Dateien, das API-Frontmatter-Schema.
- **Der Filter läuft idempotent** in `sync.sh` nach dem `rsync` (sonst
  stellt `rsync --delete` die Vollfassung wieder her).

Leitfrage beim Markieren: *Braucht jemand, der das HBG als Glossar, als
DOI-Zitat oder über die API nutzt, diesen Satz?* App-Klassen, Kotlin,
Wellen-Prozess, Verifikations-Trigger, die Autoren-Person → **nein**.
Definitionen, Quellen, Normbezüge, Quellen-Transparenz, Begriffs-Provenienz
→ **ja, bleibt**.

## A — Automatische Regeln (kein Marker nötig)

Diese Transformationen führt `hg_public_filter.py` ohne Zutun durch:

1. **Sektions-Schnitt.** Die Sektionen `## Implementierungshinweis` und
   `## Folgearbeit (trigger-basiert)` werden samt Inhalt entfernt (bis zur
   nächsten `## `-Sektion). Dort sitzt praktisch der gesamte Kotlin-Code und
   die internen Projekt-TODOs. Die normativen Definitionen stehen in
   `## Prosa-Definition`, `## Mathematische Definition`, `## Wohldefiniertheit`
   — die bleiben.
2. **Autoren-Anonymisierung.** `Eric` → `Anweiser`, `Erics` → `Anweisers`.
   Die Person tritt öffentlich nur als Rolle „Anweiser" auf.
3. **Memory-Referenzen.** `(Memory `…`)` und `; Memory `…`` werden entfernt.
4. **Tote Sektions-Zeiger.** Klammer-/Zusatz-Zeiger auf die gestrichene
   Implementierungshinweis-Sektion — `(siehe Implementierungshinweis)`,
   `; siehe Implementierungshinweis.`, `… und Implementierungshinweis)` —
   werden entfernt.
5. **Interne Recherche-Bericht-Zitate neutralisieren.** Selbstzitate auf
   `docs/recherche/<…>.md` (mit oder ohne Backticks) sind öffentlich tote
   Links. Der Pfad wird durch das Zitat-Token `[intern]` ersetzt — die
   Satz-Grammatik bleibt erhalten, der Hinweis „es gibt einen internen
   Bericht" bleibt, der tote Pfad verschwindet.

## B — Manueller Marker für chirurgische Stellen

Alles, was **satz-eingebettet** ist und sich nicht durch eine sichere
allgemeine Regel fassen lässt, wird **in der ZMA-Quelle markiert**:

```text
<!--hbg:intern-->…interner Text…<!--/hbg:intern-->
```

- **HTML-Kommentar-Klammer** — in jedem Markdown-Renderer unsichtbar, vom
  ZMA-Codegen ignoriert (er liest nur `id:`/`benennung:` aus dem Frontmatter).
  Bricht also den ZMA-Build nicht und stört die ZMA-Eigenanzeige nicht.
- **Inline oder über mehrere Zeilen/Absätze** einsetzbar.
- **Auch im Frontmatter-Block-Skalar** (`quellenkonflikt: |`, `erlaeuterung: |` …)
  einsetzbar — der Filter strippt den Marker auf dem **ganzen Dokument**, nicht
  nur im Body. Das ist wichtig, weil viele Prozess-Notizen (z. B. die
  nummerierten „(N) SIA-265-Verifikations-Trigger"/„BauNetz-Block-Signal"-
  Punkte) im `quellenkonflikt:`-Skalar stehen und über die API (`frontmatter.
  quellenkonflikt`) publiziert werden. Marker innerhalb des Skalars so setzen,
  dass die Einrückung gültig bleibt.
- Der Filter entfernt den Marker **samt eingeschlossenem Text** restlos; im
  HBG-`content/` (und damit in API + DOI) bleibt nichts davon übrig.

### Chirurgisch markieren — Transparenz behalten, Prozess entfernen

Der Schlüssel: den Marker **nur um den Prozess-Teil** legen, die Satz-Substanz
(z. B. Quellen-Transparenz) außerhalb lassen. Punktuation so setzen, dass nach
dem Entfernen ein sauberer Satz steht.

**Beispiel — SIA-Verifikations-Trigger (Transparenz bleibt):**

```text
Der Norm-Volltext ist **nicht direkt eingesehen** (SIA-Shop-Paywall)<!--hbg:intern-->;
Block-Signal, analog Welle 8/9/10. Verifikations-Trigger bei
Anweiser-Volltext-Zugriff<!--/hbg:intern-->.
```

Nach dem Filter: „Der Norm-Volltext ist **nicht direkt eingesehen**
(SIA-Shop-Paywall)." — die Paywall-Transparenz bleibt, der Wellen-/Zugriffs-
Prozess ist weg.

**Beispiel — eingebetteter Sektions-Verweis (ganzer Satz intern):**

```text
<!--hbg:intern-->Diese fehlende Transitivität ist im Implementierungshinweis zu behandeln.<!--/hbg:intern-->
```

**Beispiel — nur eine Klammer (z. B. „Hauptinstanz"-Verifikation):**

```text
…Pfosten/Ständer-Trennung (Bauatlas Appenzellerland<!--hbg:intern-->, Hauptinstanz-WebFetch-verifiziert<!--/hbg:intern-->)…
```

### Was typischerweise markiert wird

- **Autoren-/KI-Prozess:** „Hauptinstanz", „Anweiser-Volltext-Zugriff",
  „Verifikations-Trigger bei …", „… hat entschieden, den Eintrag anzulegen".
- **Recherche-Werkzeug-Notizen:** „BauNetz Block-Signal (HTTP 403)",
  „Bot-Detektion", „aus WebSearch-Snippets rekonstruiert" (sofern nicht als
  reine Quellen-Transparenz gewünscht), interne `[via: …]`/`[einsicht: …]`-Marker.
- **Wellen-/Auftrags-Prozess:** „analog Welle 9/10", „Vorgriff bis Welle 12",
  „im Auftrag 2026-…". *(Achtung: bloße Begriffs-Provenienz wie
  „`stuhlsaeule` (Welle 13)" ist Inhalt und bleibt — nur den Prozess-Bezug
  markieren.)*
- **Verweise auf gestrichene Sektionen,** die satz-eingebettet sind und von
  Regel A.4 nicht erfasst werden.

### Was nicht markiert wird (bleibt öffentlich)

- Prosa-/Mathematische Definition, Wohldefiniertheit, Erläuterung, Beziehungen.
- Quellen und Quellen-Transparenz („nicht direkt eingesehen / Paywall",
  „snippet-basiert" — der *Befund* ist Transparenz; nur der *Prozess* drumherum
  wird markiert).
- Begriffs-Provenienz (Wellen-Nummer als Datierung eines Begriffs).
- Frontmatter (`id`, `benennung`, `synonyme`, `quellen_*`, …).

## Ablauf

```bash
./sync.sh /pfad/zu/zimmermann_app   # rsync + hg_public_filter.py
git -C <hbg> diff content/          # prüfen, was sich öffentlich ändert
```

**Vor einem Zenodo-Release** den `git diff content/` durchsehen — das Archiv
ist permanent. Releases zieht nur Eric/der Anweiser, nie automatisch.

## Pflege

- Filter-Logik: `hg_public_filter.py` (HBG).
- Marker-Konvention spiegeln: ZMA-`hauptglossar/HG_KONVENTIONEN.md` trägt
  einen Kurzverweis auf diese Datei, damit beim Verfassen neuer HG-Einträge
  direkt korrekt markiert wird.
