# CLAUDE.md — Machiroku Web

Guia per a Claude Code quan treballa en aquest repositori.
Última revisió: 2026-11-19

---

## Visió del projecte

Web corporativa del restaurant japonès Machiroku (Barcelona).
Objectius: informar (oferta, horaris, ubicació), activar reserves, permetre autonomia d'edició al client sense tocar codi.

- **Repo**: https://github.com/112books/machiroku-web
- **Staging**: https://112books.github.io/machiroku-web/ca/inici/
- **Producció**: https://machiroku.com/
- **Hugo**: v0.168 (extended)
- **Stack**: Hugo + GitHub Pages + GoatCounter

### Documentació

- `README.md` — guia d'operació (menús, plats, avisos, horaris)
- `CLAUDE.md` — referència tècnica (aquest fitxer)
- `SEO-INDEXACIO.md` — SEO, redireccions, sitemaps i Search Console
- `ANALYTICS.md` — estadístiques i dashboard

---

## Comandes habituals

```bash
# Servidor local
./symc-machiroku.sh server        # environment: development → localhost:1313
hugo server --environment development

# Deploy a GitHub Pages
./symc-machiroku.sh deploy        # opció 5 — environment: production
hugo --environment production --destination docs

# Regenerar redireccions de URLs antigues (només si canvies data/redirects.yaml)
python3 scripts/generate-redirects.py
```

**Important**: Sempre `deploy` (opció 5) per publicar. `push` (opció 4) no reconstrueix `docs/`.
Si canvies `data/redirects.yaml`, executa abans `python3 scripts/generate-redirects.py`: genera les pàgines de redirecció a `static/` que després es copien a `docs/`.

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
│   ├── redirects.yaml          # Mapa d'URLs antigues → noves (genera static/)
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
│       ├── schema.html         # JSON-LD schema.org Restaurant (des de data/)
│       ├── menu-schema.html    # JSON-LD schema.org Menu (carta + preus)
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
│   │   ├── background-flors-top.webp     # Flors (cantonada superior dreta)
│   │   └── background-flors-bottom.webp  # Flors (cantonada inferior esquerra)
│   ├── logos/
│   │   └── Machiroku-logo-gran-vectoritzat.svg
│   └── admin/
│       ├── index.html          # Dashboard estadístiques (protegit amb password)
│       └── analytics.json      # Actualitzat per GitHub Action cada hora
├── scripts/
│   ├── build-analytics-json.py # Consolida raw JSON de GoatCounter
│   ├── process-analytics.py   # Genera analytics.json final (hits_by_day inclòs)
│   └── generate-redirects.py  # Genera static/<url-antiga>/index.html des de data/redirects.yaml
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

### SEO — indexació i redireccions

Google Search Console pot reportar quatre motius perquè una pàgina no s'indexi:

| Motiu | Què és | Acció |
|-------|--------|-------|
| **Pàgina amb redirecció** | `/index.html`, `/ca/`, `/es/`, `/en/` redirigeixen a `/{lang}/inici/` (GitHub Pages no fa 301) | Intencionat — no cal tocar res |
| **Exclòs per `noindex`** | Només `/admin/` i `/404.html` | Intencionat |
| **No s'ha trobat (404)** | URLs antigues (WordPress 2020, builds intermedis) | Afegir a `data/redirects.yaml` + `python3 scripts/generate-redirects.py` |
| **Rastrejada: sense indexar** | Pàgines primes o poc úniques | Millorar títol/descripció/contingut; no és un error tècnic |

- Les redireccions de URLs antigues viuen a `data/redirects.yaml` (font única) i es materialitzen a `static/<url-antiga>/index.html` amb canonical + `meta refresh` + JS.
- **No usar `aliases:` al frontmatter**: en un lloc multiidioma Hugo prefixa l'alias amb l'idioma (`/contacto/` → `/ca/contacto/`) i no serveix per a URLs antigues a l'arrel.
- HTTPS forçat a GitHub Pages activat: `http://` fa 301 → `https://`.
- `<lastmod>` als sitemaps: `enableGitInfo = true` agafa la data dels commits de cada `.md`. **Les pàgines que es renderitzen des de `data/`** (`oferta`, `reserves`, `contacte`) porten `lastmod:` manual al frontmatter: **actualitza'l quan canviïs preus, menús o horaris** a `data/*.yaml`.

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
- Dashboard: `/admin/` — contrasenya gestionada per l'equip (**no es publica en aquest repositori públic**; demana-la si cal)
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

Fonts: **Oswald** (cos, variable 300–900) i **Kaushan Script** (eslògan), **auto-allotjades** a `static/fonts/` (sense Google Fonts), amb `preload` i `font-display: swap`.
Fons ornamental: color paper `#f8f7ef` + flors fixades a les cantonades (`background-flors-top/bottom.webp`) com a `background-image` del `body` (amb `background-attachment: fixed`). Així el fons omple tot l'ample i les flors **sempre** es veuen (abans `cover` les retallava en pantalles amples).

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

## Horaris — patró de visualització

Els horaris es mostren en **tres llocs** sempre llegint de `data/horaris.yaml`:

| Lloc | Template | Estil |
|------|----------|-------|
| Footer | `layouts/_default/baseof.html` | Fons fosc — colors blancs |
| Reserves | `layouts/_default/reserves.html` | Fons clar — overrides `.reserva-card .footer-*` |
| Contacte | `layouts/_default/contacte.html` | Taula dia per dia (diferent) |

### Format footer/reserves (dos blocs Dinar/Sopar)

Classes CSS: `.footer-horaris-grid`, `.fdb`, `.fdb--menu` (vermell), `.fdb--carta` (daurat), `.fdb--off` (gris).
Lògica: sessions amb `inici < "16:00"` → dinar; `inici >= "16:00"` → sopar.
Excepcions d'hora (ex: Dijous tanca 22:30) es mostren automàticament si `fi != "23:00"`.

**Per canviar els horaris**: editar només `data/horaris.yaml` — es reflecteix als tres llocs automàticament.

---

## IDs d'al·lèrgens vàlids

`gluten`, `crustacis`, `ou`, `peix`, `cacauets`, `soja`, `lactis`, `fruits-secs`, `api`, `mostassa`, `sesam`, `sulfits`, `mol·luscos`, `altramossos`

Han de coincidir exactament entre `data/[lang]/plats.yaml` i `data/[lang]/alergics.yaml`.

---

## Migració Hugo 0.168

- Config: `languageCode` → `locale`, `languageName` → `label`
- Dades: `.Site.Data` → `hugo.Data`
- Idiomes: `.Site.Languages` → `.AllTranslations` (selector d'idioma i hreflang)
- JSON-LD: dins `<script>` cal `{{ $d | jsonify | safeJS }}` (Go escapa el JSON com a string)
- Build net: sense warnings de deprecació amb Hugo 0.168

---

## Pendents

### Prioritat baixa

- [x] SEO: meta description personalitzada per pàgina
- [ ] Accessibilitat WCAG 2.1 AA: contrast verificat, alt text, nav teclat
- [ ] humans.txt a `static/`

### Pendent de client

- [ ] Fotos de plats (`static/images/plats/`) i menús (`static/images/menus/`) — JPG/WebP, 800×600px, màx 200KB
- [ ] WhatsApp real (mòbil) → `data/restaurant.yaml` camp `whatsapp:`
- [ ] Verificar preus i plats de la carta

### Producció

- [x] DNS: CNAME a Dinahosting → `112books.github.io`
- [x] Activar HTTPS a GitHub Pages (`https_enforced` = true; http → 301 https)
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
| 2026-11-19 | SEO/indexació (Search Console): eliminades 10 pàgines primes residuals (`categories`, `dishes`, `menus` a ca/es) que sortien com a `noindex`; 61 redireccions per a URLs antigues (WordPress 2020 + builds intermedis + seccions eliminades) via `data/redirects.yaml` i `scripts/generate-redirects.py`; títols millorats (`inici` i `sobre-nosaltres` als 3 idiomes); HTTPS forçat a GitHub Pages (`http` → 301 `https`) |
| 2026-11-17 | Hugo 0.168 (locale/label, hugo.Data, .AllTranslations, jsonify+safeJS); preus actualitzats (Tofu Salad 6,80; Gyu Tataki 8,50; Unaju 15,80; Maguro to Salmon 18,00; Salmó 16,50; nigiri 5 kan 10,90 / 7 kan 17,00 / moriawase 17,00; tots els makis +1€); SEO/IA: Schema Restaurant i Menu generats des de dades, hreflang per traduccions, og:locale, llms.txt, robots per a IA, favicon = logo, h1 a inici i legals; eliminació de 8 pàgines duplicades i 25 orfes amb localhost; admin: contrast de llegendes i contrasenya gestionada fora del repo |
| 2026-09-19 | Dashboard `/admin/`: KPI **Mitjana diària** (visites/dia sobre dies amb dades); bloc **Dies de la setmana més visitats** al final de pàgina amb resum natural; vinculat al període temporal (7/30/90/365 dies) del gràfic; visualització en **gràfic donut** (Chart.js) amb diferents colors per dia |
| 2026-04-18 | Fix analytics: `process-analytics.py` reescrit (parsing GoatCounter correcte, camp `daily` no `count`, detecció idioma URLs producció); eliminar `config.yml` Netlify CMS amb credencials exposades; favicon admin; footer horaris → dos blocs Dinar/Sopar amb badges de dies (dinàmic des de YAML); mateixa lògica a Reserves amb overrides fons clar; fix foto distorsionada `sobre-nosaltres`; `servei_carta` → "A la Carta (menú no disponible)" / "À la carte" |
| 2026-04-15 | Dashboard estadístiques `/admin/` amb Chart.js, contrasenya simple, dades per dia/setmana/mes; fix GitHub Action per actualitzar `docs/`; unificació CLAUDE.md |
| 2026-04-07 | SEO complet (seo.html, schema.html, og:image, hreflang); CSS reorganitzat 16 seccions; icones transport SVG; i18n ES/EN fix |
| 2026-04-06 | Projecte inicial: Hugo multiidioma ca/es/en, 3 entorns, layouts propis, carta completa, al·lèrgens, avisos temporals, GoatCounter, footer, header |


---

## Control horari

Skill actiu: `gestor-hores` — registra automàticament el temps de treball per sessió.

- Logs a `.taques/machiroku_hugo/YYYY-MM-DD.md` (creat automàticament)
- Comandes: `/time-log [tasca] [hores]`, `/time-report [periode]`, `/time-config [hores] [tarifa]`
- No modificar manualment els fitxers `.taques/` — són append-only
