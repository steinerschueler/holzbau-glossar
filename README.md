# holzbau-glossar

Quell-Repo für [holzbau-glossar.ch](https://holzbau-glossar.ch/) — eine
öffentliche, frei zugängliche Web-Publikation des im Schwester-Repo
`zimmermann_app` gepflegten Holzbau-Glossars (Hauptglossar + Subglossar).

Inhalte stehen unter [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/deed.de).

## Lokal bauen

```bash
python3 -m venv .venv
.venv/bin/pip install -r requirements.txt
.venv/bin/mkdocs serve
```

Site läuft dann unter <http://localhost:8000>.

## Architektur

- **Static-Site-Generator:** MkDocs Material.
- **Inhalts-Quelle:** Markdown-Dateien aus dem privaten lokalen
  `zimmermann_app`-Projekt (`hauptglossar/<cluster>/hg_*.md` und
  `theorie/subglossar/sg_*.md`). Quelle bleibt strikt lokal — nur die
  publikationsfähigen Markdown-Einträge wandern via `sync.sh` in
  `content/` und werden mit diesem Repo gepusht.
- **Sync-Workflow** (manuell, vor jedem inhaltlichen Update):
  ```bash
  ./sync.sh                          # Default-Pfad: ../zimmermann_app
  git add content/
  git commit -m "sync: Welle 14 (Beispiel)"
  git push
  ```
  Die GitHub Action baut die Site bei jedem Push auf `main`.
- **Drei Formate pro Eintrag:** HTML, Markdown (`.md`), Plain-Text (`.txt`)
  für Direkt-Zitieren (Welle 3).
- **Hosting:** GitHub Pages mit Custom Domain `holzbau-glossar.ch`.
