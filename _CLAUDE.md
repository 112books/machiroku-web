# _CLAUDE.md — Projecte Machiroku.com
**Última actualització:** 2026-04-06  
**Estat del projecte:** En desenvolupament actiu  
**Stack:** Hugo + GitHub Pages + GoatCounter

---

## 🎯 VISIÓ DEL PROJECTE

Web corporativa per al restaurant japonès Machiroku (Barcelona), amb tres objectius clars:

- **Informar** → oferta gastronòmica, horaris, ubicació
- **Activar** → reserves immediates (telèfon/WhatsApp)
- **Autonomia** → client edita continguts clau sense tocar codi

---

## 🏗️ ARQUITECTURA TÈCNICA

### Entorns
| Entorn | Comandament | URL |
|--------|-------------|-----|
| Local | `hugo server` (sense flags) | `http://localhost:1313/machiroku-web/` |
| Staging | `./symc-machiroku.sh deploy` | `https://112books.github.io/machiroku-web/` |
| Producció | (pendent) | `https://machiroku.com/` |

### Regles Hugo
- `hugo server` **SENSE** `--baseURL` — Hugo agafa el baseURL del `hugo.toml` i l'adapta a localhost
- Si es passa `--baseURL /machiroku-web/` sense protocol, Hugo genera URL malformada
- El `hugo.toml` **no té** `baseURL` — es defineix per entorn a `config/`

### Configuració multiidioma
- `defaultContentLanguage = "ca"` → català és l'idioma per defecte
- `defaultContentLanguageInSubdir = true` → obligatori per prefixos `/ca/` `/es/` `/en/`
- Sense aquesta línia, el català va a l'arrel i les URLs dels menús no funcionen (404)

### Warnings Hugo v0.159
- `.Site.Languages` deprecated des de v0.156.0 → substituir als templates
- `.Site.Data` deprecated des de v0.156.0 → usar `hugo.Data`

### Stack principal
- **Generador:** Hugo v0.159 (extended)
- **Hosting:** GitHub Pages (publica des de `/docs` a `main`)
- **Analytics:** GoatCounter (`machiroku.goatcounter.com`)
- **Repositori:** `https://github.com/112books/machiroku-web`
- **Web staging:** `https://112books.github.io/machiroku-web/ca/inici/`

### Directori local
```
/Users/joan/Documents/Obsidian/machiroku_hugo
```

### Estructura del projecte
```
machiroku_hugo/
├── config/
│   ├── _default/       # (buit — configuració base al hugo.toml arrel)
│   ├── staging/
│   │   └── hugo.toml   # baseURL = "https://112books.github.io/machiroku-web/"
│   └── production/
│       └── hugo.toml   # baseURL = "https://machiroku.com/"
├── content/
│   ├── ca/             # Català (idioma principal)
│   ├── es/             # Castellà
│   └── en/             # Anglès
├── data/
│   ├── restaurant.yaml # Dades del restaurant (tel, email, maps, xarxes)
│   ├── horaris.yaml    # Horaris base (font única — s'usa a footer i contacte)
│   ├── avisos.yaml     # Avisos temporals (banner/popup)
│   ├── ca/
│   │   ├── menus.yaml  # Menús del migdia en català
│   │   ├── plats.yaml  # Carta nocturna en català
│   │   └── alergics.yaml
│   ├── es/             # Ídem en castellà
│   └── en/             # Ídem en anglès
├── layouts/
│   ├── _default/
│   │   ├── baseof.html         # Template base (header + footer + cookies + avisos)
│   │   ├── home.html           # Redirect a /ca/inici/
│   │   ├── single.html         # {{ .Content }} genèric
│   │   ├── oferta.html         # Layout pàgina oferta (layout: "oferta")
│   │   ├── reserves.html       # Layout pàgina reserves (layout: "reserves")
│   │   ├── contacte.html       # Layout pàgina contacte (layout: "contacte")
│   │   └── sobre-nosaltres.html # Layout sobre nosaltres (layout: "sobre-nosaltres")
│   └── partials/
│       ├── avisos.html         # Banners/popups temporals
│       ├── estat-restaurant.html
│       ├── menu-card.html      # Card de menú del migdia
│       └── plat-card.html      # Card de plat de la carta
├── static/
│   ├── css/
│   │   ├── main.css            # CSS principal (15+ seccions numerades)
│   │   └── estat-restaurant.css
│   ├── js/
│   │   ├── main.js             # Toggle nav mòbil + scroll suau
│   │   └── estat-restaurant.js
│   ├── images/
│   │   ├── machiroku-web-background.svg  # Fons (2064×2912px, retrat)
│   │   ├── machiroku-acercade-01.jpeg.webp  # Foto entrada restaurant
│   │   └── machiroku-acercade-02.jpeg.webp  # Foto Sachie i Masahiro Tottori
│   ├── logos/
│   │   ├── Machiroku-logo-gran-vectoritzat.svg  # Header
│   │   └── logo.svg            # Kanji (hero + footer)
│   └── admin/
│       ├── index.html          # Dashboard admin (analytics + manual)
│       └── analytics.json      # Dades GoatCounter (actualitzat pel GitHub Action)
├── scripts/
│   ├── build-analytics-json.py # Agrupa respostes API GoatCounter
│   └── process-analytics.py   # Processa i genera analytics.json
├── .github/
│   └── workflows/
│       └── fetch-analytics.yml # GitHub Action: actualitza analytics cada hora
├── i18n/
│   ├── ca.yaml
│   ├── i18n-es.yaml
│   └── i18n-en.yaml
├── hugo.toml               # Configuració principal (sense baseURL)
└── symc-machiroku.sh       # Script de deploy (opcions: status/pull/push/deploy)
```

---

## 🚀 FLUX DE TREBALL

```bash
cd /Users/joan/Documents/Obsidian/machiroku_hugo

# Servidor local
hugo server

# Publicar a GitHub Pages (staging)
./symc-machiroku.sh deploy
# → Opció 4

# Només guardar codi (sense build)
./symc-machiroku.sh push
# → Opció 3
```

**Regla important:** Sempre usar opció **4 (deploy)** per publicar. L'opció 3 (push) no reconstrueix el `docs/`.

---

## 🌍 SISTEMA MULTIIDIOMA

- **Català** (principal, `/ca/`) — `i18n/ca.yaml`
- **Castellà** (`/es/`) — `i18n/i18n-es.yaml`
- **Anglès** (`/en/`) — `i18n/i18n-en.yaml`

### Layouts per pàgina
Els fitxers `.md` de contingut han de tenir `layout:` al frontmatter:
```yaml
---
title: "Oferta gastronòmica"
layout: "oferta"
---
```
Layouts disponibles: `oferta`, `reserves`, `contacte`, `sobre-nosaltres`

### Dades per idioma
Els fitxers `data/ca/`, `data/es/`, `data/en/` contenen versions idiomàtiques de:
- `menus.yaml` — menús del migdia
- `plats.yaml` — carta nocturna amb categories
- `alergics.yaml` — al·lèrgens (font única a `ca/`, llegit sempre des de `$.Site.Data.ca`)

---

## 🍱 SISTEMA DE CONTINGUTS

### Menús del migdia (`data/ca/menus.yaml`)
```yaml
menus:
  - id: "menu-sushi"
    nom: "Menú Sushi"
    ordre: 1
    actiu: true        # false = ocult però conservat
    preu: 16.00
    foto: ""           # /images/menus/nom.jpg quan existeixi
    descripcio: "..."
    plats:
      - "Sushi moriawase (5 nigiri i 4 maki)"
    alergics:
      - "peix"         # ids del alergics.yaml
    disponibilitat:
      horari: "13:00 - 15:30"
```

### Carta nocturna (`data/ca/plats.yaml`)
Categories disponibles: `entrants`, `amanides`, `carn`, `arros`, `sashimi`, `nigiri`, `maki`

```yaml
plats:
  - id: "edamame"
    nom: "Edamame"
    categoria: "entrants"  # ha de coincidir amb id de categories
    ordre: 1
    actiu: true
    destacat: false        # true = badge "Destacat"
    preu: 3.80
    foto: ""
    descripcio: "Mongetes verdes bullides amb sal"
    alergics:
      - "soja"
```

### Al·lèrgens
IDs vàlids (han de coincidir EXACTAMENT):
`gluten`, `crustacis`, `ou`, `peix`, `cacauets`, `soja`, `lactis`, `fruits-secs`, `api`, `mostassa`, `sesam`, `sulfits`, `mol·luscos`, `altramossos`

Les icones es mostren automàticament als partials llegint `data/ca/alergics.yaml`.

---

## ⚠️ SISTEMA D'AVISOS TEMPORALS (`data/avisos.yaml`)

```yaml
avisos:
  - id: "tancat-setmana-santa"
    actiu: true              # false = ignorat
    des_de: "2026-04-01"    # YYYY-MM-DD
    fins_a: "2026-04-06"
    prioritat: "alta"       # alta (vermell) | mitjana (groc) | baixa (verd)
    tipus: "banner"         # banner (barra) | popup (modal)
    titol:
      ca: "Tancats per Setmana Santa"
      es: "Cerrados por Semana Santa"
      en: "Closed for Easter"
    text:
      ca: "Tornem el dimarts 7 d'abril."
      es: "..."
      en: "..."
    cta:
      ca: ""
    link: ""
```

Quan passen les dates, l'avís desapareix sol sense tocar res.

---

## 📊 SISTEMA D'ANALYTICS

- **GoatCounter:** `machiroku.goatcounter.com`
- **Tracking:** script al `baseof.html` línia 63
- **Dashboard:** `https://112books.github.io/machiroku-web/admin/`
- **Token:** guardat a GitHub Secrets com `GOATCOUNTER_TOKEN`
- **GitHub Action:** `.github/workflows/fetch-analytics.yml` — s'executa cada hora
- **JSON de dades:** `static/admin/analytics.json`

El dashboard inclou:
- Estadístiques per idioma, secció, navegador, dispositiu, ubicació
- Manual d'edició integrat (pestanya "📖 Manual d'edició")

---

## 🎨 DISSENY

### Paleta corporativa
- `--color-accent: #8b1a1a` — Vermell corporatiu
- `--color-accent-dark: #5a0f0f`
- `--color-black: #1a1a1a`
- `--header-overlay: rgba(30, 5, 5, 0.98)` — Negre vermellós fosc (header + footer)
- `--bg-overlay: rgba(26, 26, 26, 0.55)` — Overlay sobre el fons

### Tipografia
- **Principal:** Oswald (navegació, títols, botons)
- **Eslogan:** Kaushan Script (cursiva, aire de signatura)

### Fons
- SVG `machiroku-web-background.svg` (2064×2912px — format retrat)
- `background-size: auto 100vh` a desktop (mostra les fulles dalt i baix)
- `background-size: cover` a mòbil

### CSS (`static/css/main.css`) — 15+ seccions
1. Variables globals
2. Reset
3. Tipografia base
4. Botons (`border-radius: 6px`)
5. Header
6. Navegació
7. Estat restaurant
8. Main content
9. Hero – Pàgina d'inici
10. Footer – Grid principal
11. Footer – Horaris
12. Footer – Ubicació i xarxes
13. Footer – Reserves i Reviews
14. Footer – Fila inferior
15. Responsive
16. Pàgina d'oferta
17. Pàgina de reserves
18. Pàgina sobre nosaltres
19. Avisos temporals
20. Pàgina de contacte

---

## 📄 PÀGINES I ESTAT

| Pàgina | URL | Layout | Estat |
|--------|-----|---------|-------|
| Inici | `/ca/inici/` | `single.html` + contingut MD | ✅ Funciona |
| Oferta | `/ca/oferta/` | `oferta.html` | ✅ Funciona |
| Reserves | `/ca/reserves/` | `reserves.html` | ✅ Funciona |
| Sobre nosaltres | `/ca/sobre-nosaltres/` | `sobre-nosaltres.html` | ✅ Funciona |
| Contacte | `/ca/contacte/` | `contacte.html` | ✅ Funciona |
| Admin | `/admin/` | HTML estàtic | ✅ Funciona |

---

## 📝 PENDENTS

### Prioritat alta
- [ ] Horaris al **footer** no surten bé (funcionen a Contacte però no al footer)
- [ ] Al·lèrgens no visibles als menús ni a la carta (partials usen `$.Site.Data.ca`)
- [ ] **Header mòbil:** logo més petit + selector idioma en una línia
- [ ] **Avís d'estat** (header) — falta traduir a ES i EN
- [ ] **Oferta gastronòmica** — verificar que al·lèrgens surten a les cards

### Prioritat mitjana
- [ ] Pàgina Contacte / Com arribar — icones noves + 1 columna a mòbil
- [ ] SEO (meta tags, sitemap, robots.txt)
- [ ] Accessibilitat (WCAG 2.1 AA)
- [ ] `humans.txt`

### Pendent de client
- [ ] Fotos de plats (`static/images/plats/` i `static/images/menus/`)
- [ ] Número de WhatsApp real (mòbil, no fix) — el número destí no es veu a la pàgina
- [ ] Connexió domini `machiroku.com` → GitHub Pages (quan el web estigui llest)

### Producció (quan es connecti el domini)
- [ ] Activar `config/production/hugo.toml` (`baseURL = "https://machiroku.com/"`)
- [ ] Configurar DNS a Dinahosting
- [ ] Activar `do_publish` al `symc-machiroku.sh` (rsync SSH)

---

## 🔑 ACCESOS I TOKENS

- **GitHub repo:** `https://github.com/112books/machiroku-web`
- **GitHub token actiu:** "Machiroku deploy token" (repo + workflow)
- **GoatCounter:** `machiroku.goatcounter.com` (compte: webmaster@linuxbcn.com)
- **GitHub Secret:** `GOATCOUNTER_TOKEN` (token API de GoatCounter)
- **Email restaurant:** `machiroku@machiroku.com` → redirecció Gmail

---

## 🔄 COM REGENERAR LA SESSIÓ AMB CLAUDE

Per reprendre el treball en una nova sessió, comparteix aquest fitxer i afegeix:

1. **L'estat actual** — `./symc-machiroku.sh status` (opció 1)
2. **El problema o tasca concreta** que vols resoldre
3. **El fitxer afectat** si és un bug concret (ex: `cat static/css/main.css | grep -A5 ".footer-schedule"`)

Claude té accés al browser via l'extensió de Chrome per veure el web en directe.

---

*Aquest document és la font única de veritat per al projecte Machiroku.*  
*Actualitzar-lo amb cada decisió important.*  
*Generat per LinuxBCN.com — Claude Sonnet*