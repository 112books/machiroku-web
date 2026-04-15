# CLAUDE.md — Machiroku Web

Guia per a Claude Code quan treballa en aquest repositori.
Última revisió: 2026-04-15

---

## Visió del projecte

Web corporativa del restaurant japonès Machiroku (Barcelona).
Objectius: informar (oferta, horaris, ubicació), activar reserves, permetre autonomia d'edició al client sense tocar codi.

- **Repo**: https://github.com/112books/machiroku-web
- **Staging**: https://112books.github.io/machiroku-web/ca/inici/
- **Producció**: https://machiroku.com/
- **Hugo**: v0.159 (extended)
- **Stack**: Hugo + GitHub Pages + GoatCounter

---

## Comandes habituals

```bash
# Servidor local
./symc-machiroku.sh server        # environment: development → localhost:1313
hugo server --environment development

# Deploy a GitHub Pages
./symc-machiroku.sh deploy        # opció 5 — environment: production
hugo --environment production --destination docs
```

**Important**: Sempre `deploy` (opció 5) per publicar. `push` (opció 4) no reconstrueix `docs/`.

### Entorns Hugo

| Entorn        | Config                        | URL                                         |
|---------------|-------------------------------|---------------------------------------------|
| `development` | `config/development/hugo.toml`| `http://localhost:1313/`                    |
| `staging`     | `config/staging/hugo.toml`    | `https://112books.github.io/machiroku-web/` |
| `production`  | `config/production/hugo.toml` | `https://machiroku.com/`                    |

El `hugo.toml` arrel no té `baseURL` — es defineix per entorn a `config/`.

---

## Arquitectura

### Estructura del projecte

```
machiroku_hugo/
├── config/
│   ├── staging/hugo.toml       # baseURL = "https://112books.github.io/machiroku-web/"
│   └── production/hugo.toml    # baseURL = "https://machiroku.com/"
├── content/
│   ├── ca/                     # Català (idioma principal)
│   ├── es/                     # Castellà
│   └── en/                     # Anglès
├── data/
│   ├── restaurant.yaml         # Tel, email, maps, xarxes socials
│   ├── horaris.yaml            # Horaris (font única — footer + contacte)
│   ├── avisos.yaml             # Avisos temporals (banner/popup)
│   ├── ca/
│   │   ├── menus.yaml          # Menús del migdia en català
│   │   ├── plats.yaml          # Carta nocturna en català
│   │   └── alergics.yaml
│   ├── es/                     # Ídem en castellà
│   └── en/                     # Ídem en anglès
├── layouts/
│   ├── _default/
│   │   ├── baseof.html         # Template base (header + footer + cookies + avisos)
│   │   ├── home.html           # Redirect a /ca/inici/
│   │   ├── oferta.html         # layout: "oferta"
│   │   ├── reserves.html       # layout: "reserves"
│   │   ├── contacte.html       # layout: "contacte"
│   │   └── sobre-nosaltres.html
│   └── partials/
│       ├── seo.html            # title, description, canonical, hreflang, og:*, twitter:*
│       ├── schema.html         # JSON-LD schema.org Restaurant
│       ├── avisos.html         # Banners/popups temporals
│       ├── estat-restaurant.html  # Injecta horaris + i18n com a JSON per JS
│       ├── menu-card.html      # Card de menú del migdia
│       └── plat-card.html      # Card de plat de la carta
├── static/
│   ├── css/main.css            # 16 seccions (veure baix)
│   ├── js/
│   │   ├── main.js             # Toggle nav mòbil + scroll suau
│   │   └── estat-restaurant.js # Sense optional chaining (?.) per compatibilitat
│   ├── images/
│   │   └── machiroku-web-background.svg  # 2064×2912px retrat
│   ├── logos/
│   │   └── Machiroku-logo-gran-vectoritzat.svg
│   └── admin/
│       ├── index.html          # Dashboard estadístiques (protegit amb password)
│       └── analytics.json      # Actualitzat per GitHub Action cada hora
├── scripts/
│   ├── build-analytics-json.py # Consolida raw JSON de GoatCounter
│   └── process-analytics.py   # Genera analytics.json final (hits_by_day inclòs)
├── .github/workflows/
│   └── fetch-analytics.yml     # Actualitza analytics.json cada hora
├── i18n/
│   ├── ca.yaml
│   ├── es.yaml
│   └── en.yaml
├── hugo.toml
├── symc-machiroku.sh
└── CLAUDE.md
```

### Multiidioma (ca/es/en)

- `defaultContentLanguage = "ca"` — català és l'idioma per defecte
- `defaultContentLanguageInSubdir = true` — obligatori per prefixos `/ca/` `/es/` `/en/`; sense aquesta línia el català va a l'arrel i les URLs dels menús donen 404
- Fitxers i18n: `ca.yaml`, `es.yaml`, `en.yaml` (sense prefix `i18n-`)

### Patrons d'accés a dades

```
# Dades globals
(hugo.Data).horaris.base

# Dades per idioma
(index (hugo.Data) $lang).alergics.alergics

# Passar context a partials
{{ partial "menu-card.html" (dict "menu" . "lang" $.Site.Language.Lang) }}

# Traduccions al JS: injectar via Hugo al partial
window.i18nEstat = { ... }
```

### Regles de partials

- Partials de lògica retornen un `dict` — mai HTML
- Partials de renderització emeten HTML — mai retornen dades
- No encadenar partials sense control de tipus
- No usar `template.HTML` en control de flux
- No usar `index()` sobre strings HTML
- Contracte estat restaurant: `status` (string: `open | closed | menu`), `reason` (string)

### Layouts de pàgina

Els fitxers `.md` de contingut han de declarar `layout:` al frontmatter:

```yaml
layout: "oferta"   # oferta | reserves | contacte | sobre-nosaltres
```

---

## Analytics i panell d'administració

- GoatCounter: `machiroku.goatcounter.com`
- GitHub Action actualitza `static/admin/analytics.json` **i** `docs/admin/analytics.json` cada hora via secret `GOATCOUNTER_TOKEN`
- Dashboard: `/admin/` — contrasenya: **`machiroku`**
  - Staging: `https://112books.github.io/machiroku-web/admin/`
  - Producció: `https://machiroku.com/admin/`
- Per canviar la contrasenya: `echo -n "nova" | sha256sum` → actualitzar `PW_HASH` a `static/admin/index.html`
- Mostra: visites per dia/setmana/mes (Chart.js), idiomes, seccions, navegadors, SO, dispositius

---

## Disseny

### Tokens CSS

```css
--color-accent:      #8b1a1a
--color-accent-dark: #5a0f0f
--color-black:       #1a1a1a
--header-overlay:    rgba(30, 5, 5, 0.98)
--bg-overlay:        rgba(26, 26, 26, 0.55)
```

Fonts: **Oswald** (cos), **Kaushan Script** (eslogan).
Fons: `machiroku-web-background.svg` (2064×2912px retrat) — `background-size: auto 100vh` desktop, `cover` mòbil.

### CSS — 16 seccions (`static/css/main.css`)

```
01 Variables globals    09 Main content
02 Reset & base         10 Hero – Inici
03 Tipografia           11 Footer
04 Botons               12 Oferta
05 Header               13 Reserves
06 Navegació            14 Contacte
07 Estat restaurant     15 Sobre nosaltres
08 Avisos temporals     16 Responsive (1 bloc: tablet 769–1024px + mòbil ≤768px)
```

---

## IDs d'al·lèrgens vàlids

`gluten`, `crustacis`, `ou`, `peix`, `cacauets`, `soja`, `lactis`, `fruits-secs`, `api`, `mostassa`, `sesam`, `sulfits`, `mol·luscos`, `altramossos`

Han de coincidir exactament entre `data/[lang]/plats.yaml` i `data/[lang]/alergics.yaml`.

---

## Warnings Hugo v0.159 coneguts

- `.Site.Languages` deprecated des de v0.156.0 — pendent de solució oficial Hugo
- `.Site.Data` deprecated des de v0.156.0 — substituït per `hugo.Data` a tots els templates

---

## Pendents

### Prioritat baixa

- [ ] SEO: meta description personalitzada per pàgina
- [ ] Accessibilitat WCAG 2.1 AA: contrast verificat, alt text, nav teclat
- [ ] humans.txt a `static/`

### Pendent de client

- [ ] Fotos de plats (`static/images/plats/`) i menús (`static/images/menus/`) — JPG/WebP, 800×600px, màx 200KB
- [ ] WhatsApp real (mòbil) → `data/restaurant.yaml` camp `whatsapp:`
- [ ] Verificar preus i plats de la carta

### Producció

- [ ] DNS: CNAME a Dinahosting → `112books.github.io`
- [ ] Activar HTTPS a GitHub Pages
- [ ] Eliminar Google Analytics del web antic

---

## Accesos

- **GitHub repo**: https://github.com/112books/machiroku-web
- **GoatCounter**: machiroku.goatcounter.com (compte: webmaster@linuxbcn.com)
- **GitHub Secret**: `GOATCOUNTER_TOKEN`
- **Email restaurant**: machiroku@machiroku.com → redirecció Gmail

---

## Com reprendre la sessió amb Claude

1. Obre el projecte: `cd /Users/joan/Documents/Obsidian/machiroku_hugo`
2. Comprova l'estat: `./symc-machiroku.sh` → opció 1 (Status)
3. Comparteix aquest `CLAUDE.md` amb Claude Code
4. Descriu la tasca concreta

---

## Historial de canvis rellevants

| Data       | Canvis |
|------------|--------|
| 2026-04-15 | Dashboard estadístiques `/admin/` amb Chart.js, contrasenya simple, dades per dia/setmana/mes; fix GitHub Action per actualitzar `docs/`; unificació CLAUDE.md |
| 2026-04-07 | SEO complet (seo.html, schema.html, og:image, hreflang); CSS reorganitzat 16 seccions; icones transport SVG; i18n ES/EN fix |
| 2026-04-06 | Projecte inicial: Hugo multiidioma ca/es/en, 3 entorns, layouts propis, carta completa, al·lèrgens, avisos temporals, GoatCounter, footer, header |
