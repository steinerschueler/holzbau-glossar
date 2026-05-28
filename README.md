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
- **Inhalts-Quelle:** Markdown-Dateien aus dem Repo `zimmermann_app`
  (`hauptglossar/<cluster>/hg_*.md` und `theorie/subglossar/sg_*.md`),
  per sparse-checkout in der GitHub Action eingelesen. Sync ist
  unidirektional — gepflegt wird nur im Quell-Repo.
- **Drei Formate pro Eintrag:** HTML, Markdown (`.md`), Plain-Text (`.txt`)
  für Direkt-Zitieren.
- **Hosting:** GitHub Pages mit Custom Domain.
