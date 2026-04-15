# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project overview

Corporate website for Machiroku, a Japanese restaurant in Barcelona. Built with Hugo, hosted on GitHub Pages, with GoatCounter analytics.

- **Repo**: https://github.com/112books/machiroku-web
- **Staging**: https://112books.github.io/machiroku-web/ca/inici/
- **Production**: https://machiroku.com/ (pending DNS setup)
- **Hugo version**: v0.159 (extended)

## Common commands

```bash
# Local dev server
./symc-machiroku.sh server        # opció 2 — environment: development → localhost:1313
# o directament:
hugo server --environment development

# Build and deploy to GitHub Pages (production → machiroku.com)
./symc-machiroku.sh deploy        # opció 5 — environment: production
# o directament:
hugo --environment production --destination docs
```

**Important**: Sempre usar `deploy` (opció 5) per publicar a GitHub Pages — `push` (opció 4) no reconstrueix `docs/`.

### Entorns Hugo
| Entorn | Config | URL |
|--------|--------|-----|
| `development` | `config/development/hugo.toml` | `http://localhost:1313/` |
| `staging` | `config/staging/hugo.toml` | `https://112books.github.io/machiroku-web/` |
| `production` | `config/production/hugo.toml` | `https://machiroku.com/` |

## Architecture

### Multi-environment config
- `hugo.toml` (root) — shared config, no `baseURL`
- `config/staging/hugo.toml` — `baseURL = "https://112books.github.io/machiroku-web/"`
- `config/production/hugo.toml` — `baseURL = "https://machiroku.com/"`

### Multilingual (ca/es/en)
- `defaultContentLanguage = "ca"` — Catalan is primary
- `defaultContentLanguageInSubdir = true` — required for `/ca/`, `/es/`, `/en/` prefixes; without it, Catalan routes to root and nav URLs 404
- i18n files: `i18n/ca.yaml`, `i18n/es.yaml`, `i18n/en.yaml` (no `i18n-` prefix)

### Data access patterns
```
# Global data
(hugo.Data).horaris.base

# Language-scoped data
(index (hugo.Data) $lang).alergics.alergics

# Pass context to partials
{{ partial "menu-card.html" (dict "menu" . "lang" $.Site.Language.Lang) }}

# JS i18n: inject via Hugo partial
window.i18nEstat = { ... }
```

### Partial rules (from notes/hugo-rules.md)
- Logic partials return a `dict` — never HTML
- Render partials output HTML — never return data
- Don't chain partials without type control
- Don't use `template.HTML` in control flow
- Don't use `index()` on HTML strings
- Restaurant state contract: `status` (string: `open | closed | menu`), `reason` (string)

### Content data structure
- `data/restaurant.yaml` — phone, email, maps, social
- `data/horaris.yaml` — opening hours (single source of truth for footer and contacte)
- `data/avisos.yaml` — temporary banners/popups with date ranges
- `data/ca/`, `data/es/`, `data/en/` — `menus.yaml`, `plats.yaml`, `alergics.yaml`

### Page layouts
Content `.md` files must declare `layout:` in frontmatter:
```yaml
layout: "oferta"   # oferta | reserves | contacte | sobre-nosaltres
```

### CSS structure (static/css/main.css)
16 sections in order: Variables → Reset → Tipografia → Botons → Header → Navegació → Estat restaurant → Avisos → Main content → Hero → Footer → Oferta → Reserves → Contacte → Sobre nosaltres → **Responsive (single block at bottom: tablet 769–1024px + mobile ≤768px)**

### Analytics
- GoatCounter at `machiroku.goatcounter.com`
- GitHub Action updates `static/admin/analytics.json` **i** `docs/admin/analytics.json` hourly via `GOATCOUNTER_TOKEN` secret
- Dashboard d'estadístiques: `/admin/` — protegit amb contrasenya **`machiroku`**
  - Staging: `https://112books.github.io/machiroku-web/admin/`
  - Producció: `https://machiroku.com/admin/`
- Per canviar la contrasenya: `echo -n "nova" | sha256sum` i actualitzar `PW_HASH` a `static/admin/index.html`
- Mostra: visites per dia/setmana/mes, idiomes, seccions, navegadors, SO, dispositius

## Known Hugo v0.159 warnings
- `.Site.Languages` deprecated since v0.156.0 — pending official Hugo solution
- `.Site.Data` deprecated since v0.156.0 — replaced everywhere with `hugo.Data`

## Design tokens
```css
--color-accent: #8b1a1a
--color-accent-dark: #5a0f0f
--color-black: #1a1a1a
--header-overlay: rgba(30, 5, 5, 0.98)
--bg-overlay: rgba(26, 26, 26, 0.55)
```
Fonts: **Oswald** (body), **Kaushan Script** (slogan). Background SVG: `machiroku-web-background.svg` (2064×2912px portrait), `background-size: auto 100vh` on desktop, `cover` on mobile.

## Valid allergen IDs
`gluten`, `crustacis`, `ou`, `peix`, `cacauets`, `soja`, `lactis`, `fruits-secs`, `api`, `mostassa`, `sesam`, `sulfits`, `mol·luscos`, `altramossos`

These must match exactly between `data/[lang]/plats.yaml` and `data/[lang]/alergics.yaml`.
