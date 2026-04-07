Aquí tens el _CLAUDE.md actualitzat:

_CLAUDE.md — Projecte Machiroku.com
Última actualització: 2026-04-07
Estat del projecte: En desenvolupament actiu
Stack: Hugo + GitHub Pages + GoatCounter

🎯 VISIÓ DEL PROJECTE
Web corporativa per al restaurant japonès Machiroku (Barcelona), amb tres objectius clars:

Informar → oferta gastronòmica, horaris, ubicació
Activar → reserves immediates (telèfon/WhatsApp)
Autonomia → client edita continguts clau sense tocar codi


🏗️ ARQUITECTURA TÈCNICA
Entorns
EntornComandamentURLLocalhugo server (sense flags)http://localhost:1313/machiroku-web/Staging./symc-machiroku.sh deployhttps://112books.github.io/machiroku-web/Producció(pendent)https://machiroku.com/
Regles Hugo

hugo server SENSE --baseURL — Hugo agafa el baseURL del hugo.toml i l'adapta a localhost
Si es passa --baseURL /machiroku-web/ sense protocol, Hugo genera URL malformada
El hugo.toml no té baseURL — es defineix per entorn a config/

Configuració multiidioma

defaultContentLanguage = "ca" → català és l'idioma per defecte
defaultContentLanguageInSubdir = true → obligatori per prefixos /ca/ /es/ /en/
Sense aquesta línia, el català va a l'arrel i les URLs dels menús no funcionen (404)

Warnings Hugo v0.159

.Site.Languages deprecated des de v0.156.0 → pendent de solució oficial Hugo
.Site.Data deprecated des de v0.156.0 → ✅ substituït per hugo.Data a tots els templates

Patrons Hugo aprovats (après a la pràctica)

Llegir dades globals: (hugo.Data).horaris.base
Llegir dades per idioma: (index (hugo.Data) $lang).alergics.alergics
Passar context a partials: {{ partial "menu-card.html" (dict "menu" . "lang" $.Site.Language.Lang) }}
Fitxers i18n: han de ser ca.yaml, es.yaml, en.yaml (sense prefix i18n-)
Traduccions al JS: injectar via Hugo al partial com window.i18nEstat = { ... }

Stack principal

Generador: Hugo v0.159 (extended)
Hosting: GitHub Pages (publica des de /docs a main)
Analytics: GoatCounter (machiroku.goatcounter.com)
Repositori: https://github.com/112books/machiroku-web
Web staging: https://112books.github.io/machiroku-web/ca/inici/

Directori local
/Users/joan/Documents/Obsidian/machiroku_hugo
Estructura del projecte
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
│   │   └── sobre-nosaltres.html
│   └── partials/
│       ├── avisos.html         # Banners/popups temporals
│       ├── estat-restaurant.html  # Injecta horaris + i18n com a JSON per JS
│       ├── menu-card.html      # Card de menú del migdia
│       └── plat-card.html      # Card de plat de la carta
├── static/
│   ├── css/
│   │   ├── main.css            # CSS reorganitzat (16 seccions, 1 bloc responsive)
│   │   └── estat-restaurant.css
│   ├── js/
│   │   ├── main.js             # Toggle nav mòbil + scroll suau
│   │   └── estat-restaurant.js # Sense optional chaining (?.) per compatibilitat
│   ├── images/
│   │   ├── machiroku-web-background.svg
│   │   ├── machiroku-acercade-01.jpeg.webp
│   │   └── machiroku-acercade-02.jpeg.webp
│   ├── logos/
│   │   ├── Machiroku-logo-gran-vectoritzat.svg
│   │   └── logo.svg
│   └── admin/
│       ├── index.html
│       └── analytics.json
├── scripts/
│   ├── build-analytics-json.py
│   └── process-analytics.py
├── .github/
│   └── workflows/
│       └── fetch-analytics.yml
├── i18n/
│   ├── ca.yaml         # ✅ nom correcte
│   ├── es.yaml         # ✅ renombrat (era i18n-es.yaml)
│   └── en.yaml         # ✅ renombrat (era i18n-en.yaml)
├── hugo.toml
└── symc-machiroku.sh

🚀 FLUX DE TREBALL
bashcd /Users/joan/Documents/Obsidian/machiroku_hugo

# Servidor local
hugo server

# Publicar a GitHub Pages (staging)
./symc-machiroku.sh
# → Opció 4 (Deploy)

# Només guardar codi (sense build)
# → Opció 3 (Push)
Regla important: Sempre usar opció 4 (deploy) per publicar. L'opció 3 (push) no reconstrueix el docs/.

🌍 SISTEMA MULTIIDIOMA

Català (principal, /ca/) — i18n/ca.yaml
Castellà (/es/) — i18n/es.yaml
Anglès (/en/) — i18n/en.yaml

Claus i18n rellevants afegides (2026-04-07)
yamlhorari_fins: "Fins les"   # / "Hasta las" / "Until"
avui: "avui"              # / "hoy" / "today"
telefon: "Telèfon"        # / "Teléfono" / "Phone"
Layouts per pàgina
Els fitxers .md de contingut han de tenir layout: al frontmatter:
yaml---
title: "Oferta gastronòmica"
layout: "oferta"
---
Dades per idioma

data/ca/, data/es/, data/en/ — menus, plats, alergics
Al·lèrgens: llegits dinàmicament per idioma amb (index (hugo.Data) $lang).alergics.alergics


🍱 SISTEMA DE CONTINGUTS
Menús del migdia (data/ca/menus.yaml)
yamlmenus:
  - id: "menu-sushi"
    nom: "Menú Sushi"
    ordre: 1
    actiu: true
    preu: 16.00
    foto: ""
    descripcio: "..."
    plats:
      - "Sushi moriawase (5 nigiri i 4 maki)"
    alergics:
      - "peix"
    disponibilitat:
      horari: "13:00 - 15:30"
Carta nocturna (data/ca/plats.yaml)
Categories: entrants, amanides, carn, arros, sashimi, nigiri, maki
yamlplats:
  - id: "edamame"
    nom: "Edamame"
    categoria: "entrants"
    ordre: 1
    actiu: true
    destacat: false
    preu: 3.80
    foto: ""
    descripcio: "Mongetes verdes bullides amb sal"
    alergics:
      - "soja"
Al·lèrgens
IDs vàlids (han de coincidir EXACTAMENT):
gluten, crustacis, ou, peix, cacauets, soja, lactis, fruits-secs, api, mostassa, sesam, sulfits, mol·luscos, altramossos
Les icones es mostren automàticament als partials llegint data/[lang]/alergics.yaml.

⚠️ SISTEMA D'AVISOS TEMPORALS (data/avisos.yaml)
yamlavisos:
  - id: "tancat-setmana-santa"
    actiu: true
    des_de: "2026-04-01"
    fins_a: "2026-04-06"
    prioritat: "alta"
    tipus: "banner"
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

📊 SISTEMA D'ANALYTICS

GoatCounter: machiroku.goatcounter.com
Dashboard: https://112books.github.io/machiroku-web/admin/
Token: GOATCOUNTER_TOKEN a GitHub Secrets
GitHub Action: actualitza analytics.json cada hora


🎨 DISSENY
Paleta corporativa

--color-accent: #8b1a1a — Vermell corporatiu
--color-accent-dark: #5a0f0f
--color-black: #1a1a1a
--header-overlay: rgba(30, 5, 5, 0.98)
--bg-overlay: rgba(26, 26, 26, 0.55)

Tipografia

Principal: Oswald
Eslogan: Kaushan Script

Fons

machiroku-web-background.svg (2064×2912px — format retrat)
background-size: auto 100vh desktop / cover mòbil

CSS (static/css/main.css) — 16 seccions
01. Variables globals
02. Reset & base
03. Tipografia
04. Botons
05. Header
06. Navegació
07. Estat restaurant
08. Avisos temporals
09. Main content
10. Hero – Inici
11. Footer
12. Pàgina Oferta
13. Pàgina Reserves
14. Pàgina Contacte
15. Pàgina Sobre nosaltres
16. Responsive (UN SOL BLOC — tablet 769-1024px + mòbil ≤768px)
Icones transport (Contacte → Com arribar)
SVG Lucide amb stroke="currentColor" — color controlat per .arribar-icona { color: var(--color-accent) }

Metro: train-front-tunnel
Tren: tram-front
Bus: bus
Bici: bike
Aeroport: plane
Port: ship
Pàrquing: square-parking


📄 PÀGINES I ESTAT
PàginaURLLayoutEstatInici/ca/inici/single.html✅Oferta/ca/oferta/oferta.html✅Reserves/ca/reserves/reserves.html✅Sobre nosaltres/ca/sobre-nosaltres/sobre-nosaltres.html✅Contacte/ca/contacte/contacte.html✅Admin/admin/HTML estàtic✅

📝 PENDENTS
Prioritat baixa (poliment)

 SEO: meta tags per pàgina (description, og:image, og:title)
 SEO: sitemap verificat
 SEO: robots.txt
 SEO: structured data (schema.org Restaurant)
 Accessibilitat WCAG 2.1 AA: contrast de colors verificat
 Accessibilitat: alt text a totes les imatges
 Accessibilitat: navegació per teclat completa
 humans.txt a static/humans.txt
 og:type "website" a pàgines d'inici (frontmatter + seo.html)

Pendent de client

 Fotos de plats (static/images/plats/) i menús (static/images/menus/) — JPG/WebP, 800×600px, màx 200KB
 Número de WhatsApp real (mòbil) → data/restaurant.yaml camp whatsapp:
 Verificar preus i plats de la carta (importats del web original)

Producció

 Connectar domini machiroku.com → GitHub Pages

 DNS a Dinahosting (CNAME → 112books.github.io)
 Activar HTTPS a GitHub Pages


 Verificar config/production/hugo.toml (baseURL = "https://machiroku.com/")
 Eliminar Google Analytics del web antic
 Primer deploy de producció (do_publish al symc-machiroku.sh)


✅ HISTORIAL DE CANVIS
2026-04-06

Script symc-machiroku.sh amb deploy automatitzat
Configuració multiidioma (ca/es/en) amb 3 entorns
GitHub Pages funcionant amb baseURL correcte
Layouts propis: oferta, reserves, contacte, sobre-nosaltres
Carta completa amb menús i plats reals
Sistema d'al·lèrgens multiidioma (estructura correcta)
Sistema d'avisos temporals (banner/popup per dates)
Footer i header polits
Eslogan en Kaushan Script (dues línies)
Dashboard /admin (analytics + manual d'edició)
GoatCounter integrat

2026-04-07

✅ Footer horaris: corregit amb hugo.Data + lògica de dies
✅ Al·lèrgens a cards: corregit amb (index (hugo.Data) $lang) + dict al partial
✅ Avís d'estat traduït ES/EN: i18n injectat via Hugo + fix classe JS + eliminat ?.
✅ Icones transport SVG Lucide (currentColor) a pàgina Contacte
✅ Responsive mòbil/tablet complet i unificat
✅ CSS reorganitzat: 16 seccions, 1 bloc responsive, focus-visible, prefixos webkit
✅ Fitxers i18n renombrats: es.yaml, en.yaml (eren i18n-es.yaml, i18n-en.yaml)
✅ CTA "Fer una reserva" reposicionat a oferta


### 2026-04-07 (tarda)

- ✅ SEO: partial `seo.html` amb title, description, canonical, hreflang, og:*, twitter:*
- ✅ SEO: partial `schema.html` amb JSON-LD schema.org Restaurant
- ✅ SEO: `robots.txt` a `static/`
- ✅ SEO: `og:image` — `og-machiroku.jpg` (1200×630px) amb logo oficial
- ✅ SEO: hreflang ca/es/en/x-default validat
- ✅ SEO: Schema.org validat a Google Rich Results (Empresa local + Organització)
- ✅ SEO: og:image validat al Facebook Sharing Debugger
- ✅ Fix: `.nojekyll` a `static/` — desactiva Jekyll a GitHub Pages
- ✅ Fix: `.File nil` a `seo.html` — protegit per pàgines virtuals (list pages)
- ✅ Frontmatter: `description`, `og_image`, `schema: true` a inici.md (ca/es/en)


🔑 ACCESOS

GitHub repo: https://github.com/112books/machiroku-web
GoatCounter: machiroku.goatcounter.com (compte: webmaster@linuxbcn.com)
GitHub Secret: GOATCOUNTER_TOKEN
Email restaurant: machiroku@machiroku.com → redirecció Gmail


🔄 COM REPRENDRE LA SESSIÓ AMB CLAUDE

Comparteix aquest fitxer _CLAUDE.md
Afegeix l'estat actual: ./symc-machiroku.sh → Opció 1 (Status)
Descriu el problema o tasca concreta
Adjunta el fitxer afectat si és un bug


Font única de veritat del projecte Machiroku.
Actualitzar amb cada decisió important.
Generat per LinuxBCN.com — Claude Sonnet