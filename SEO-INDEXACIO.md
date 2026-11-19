# SEO i indexació — Referència tècnica

Com està muntat el SEO del web, com funcionen les redireccions i què cal fer a
Google Search Console quan apareixen incidències d'indexació.

Última revisió: 2026-11-19

---

## Estat de partida (Search Console, 19 nov. 2026)

Search Console va reportar quatre motius d'exclusió:

| Motiu | Pàgines | Causa real | Resolució |
|-------|---------|------------|-----------|
| Pàgina amb redirecció | 9 | `/index.html`, `/ca/`, `/es/`, `/en/` redirigeixen a `/{lang}/inici/` (GitHub Pages no fa 301) | **Intencionat** |
| Exclòs per `noindex` | 4 | Pàgines primes residuals de taxonomies (`categories`, `dishes`, `menus`) | **Eliminades** (ara redirigeixen) |
| No s'ha trobat (404) | 3 | URLs de l'antic WordPress 2020 i de builds intermedis | **61 redireccions** |
| Rastrejada: sense indexar | 3 | Pàgines primes / poc úniques | Títols millorats + sol·licitud d'indexació |

**Resultat:** només queden amb `noindex` `/admin/` i `/404.html` (intencionat).

---

## Mapa del lloc

- **Sitemap índex**: `/sitemap.xml` → referencia els 3 sitemaps d'idioma
- **Sitemaps d'idioma**: `/ca/sitemap.xml`, `/es/sitemap.xml`, `/en/sitemap.xml`
- **Total**: 24 URLs (8 per idioma)
- Cada `<url>` porta `<lastmod>` i els `<xhtml:link rel="alternate" hreflang>`
- Les redireccions de URLs antigues **no** entren al sitemap (són fitxers estàtics)
- `robots.txt` bloqueja `/admin/` i permet explícitament els bots d'IA (GPTBot, ClaudeBot, etc.)

---

## Head SEO (`layouts/partials/seo.html`)

Cada pàgina genera:

- `<title>` = `{Títol} | Machiroku`
- `<meta name="description">` (frontmatter `description` o descripció de l'idioma)
- `<link rel="canonical">` → sempre l'URL propi
- `hreflang` per a cada traducció real + `x-default` (versió catalana)
- Open Graph + Twitter Card
- JSON-LD: `Restaurant` (a inici) i `Menu` (a oferta, 8 seccions / 46 plats)
- `noindex` només per a seccions de taxonomia (regla defensiva; avui no n'hi ha)

---

## Redireccions d'URLs antigues

GitHub Pages **no permet 301 reals**. Per això cada URL antiga és un fitxer
estàtic amb `canonical` + `meta refresh` + JS.

### Font única: `data/redirects.yaml`

```yaml
redirects:
  - from: /contacto/          # URL antiga (comença i acaba amb /)
    to: /ca/contacte/         # pàgina nova
```

### Generació: `scripts/generate-redirects.py`

```bash
python3 scripts/generate-redirects.py
```

- Escriu `static/<url-antiga>/index.html` per a cada entrada
- Els fitxers generats porten el marcador `<!-- generated-redirect -->`
- A cada execució esborra i reescriu **només** els fitxers amb aquest marcador
- **Es nega a sobreescriure** un `index.html` que no sigui seu (seguretat)
- S'executa **abans** del build; el deploy els copia a `docs/`

### Com afegir una redirecció

1. Afegeix l'entrada a `data/redirects.yaml`
2. `python3 scripts/generate-redirects.py`
3. Deploy (`./symc-machiroku.sh` → opció 5)

### Important

- **No** usar `aliases:` al frontmatter: en un lloc multiidioma Hugo prefixa
  l'alias amb l'idioma (`/contacto/` → `/ca/contacto/`) i no serveix per a URLs
  antigues a l'arrel.
- Un sitemap **no** ha de contenir redireccions: no les hi afegim mai.

---

## `<lastmod>` als sitemaps

- `enableGitInfo = true` a `hugo.toml` → la data surt del commit de cada `.md`
- `[frontmatter] lastmod = ["lastmod", ":git", "date", "publishDate"]` dona
  prioritat al valor manual
- La taula `[frontmatter]` ha d'anar **al final** del `hugo.toml`; si va al
  mig, s'empassa les claus següents (per exemple `canonifyURLs`) i trenca els
  enllaços absoluts.

### Regla de manteniment

Les pàgines `oferta`, `reserves` i `contacte` es renderitzen des de `data/`,
així que porten `lastmod:` manual al frontmatter:

> **Quan canviïs preus, menús o horaris a `data/*.yaml`, actualitza el camp
> `lastmod` de les pàgines afectades (als 3 idiomes).**

---

## HTTPS

- `https_enforced = true` a GitHub Pages (activat per API)
- `http://` fa **301 → `https://`**
- Certificat: `machiroku.com` + `www.machiroku.com`
- `static/CNAME` conté `machiroku.com` perquè el build no perdi el domini

---

## Guia d'actuació a Search Console

### 1. Sitemaps

`Indexació → Sitemaps` → només ha de constar `https://machiroku.com/sitemap.xml`.
Esborra qualsevol entrada `http://` (no es pot llegir).

### 2. Indexació de pàgines

| Motiu | Acció |
|-------|-------|
| **Pàgina amb redirecció** | No validar. És intencionat. |
| **Exclòs per `noindex`** | Validar només si no hauria de ser `noindex`. |
| **No s'ha trobat (404)** | Afegir a `data/redirects.yaml` + generar + deploy. Després validar. |
| **Rastrejada / Detectada: sense indexar** | `Inspecció d'URL` → `Provar URL en directe` → `Sol·licitar indexació`. |

### 3. Inspecció d'URL

- **"Provar URL en directe"** comprova la versió actual (200, indexable). **No**
  indica si ja és a l'índex.
- L'estat d'indexació és el text de dalt: **"L'URL és a Google"** o
  **"L'URL no és a Google"**.
- `Sol·licitar indexació` té quota diària (~10-12 per propietat).

### 4. Terminis orientatius

| Fet | Temps |
|-----|-------|
| Recrawl després de sol·licitar | 1–3 dies |
| Validació d'un grup de correcció | 3 dies – 2 setmanes |
| Baixada dels 404 | dies (quan Google recrawleja) |

---

## Diagnòstic ràpid

```bash
# Capçaleres d'una pàgina
curl -sI https://machiroku.com/ca/oferta/

# Canonical / noindex / title
curl -s https://machiroku.com/ca/oferta/ | grep -E '<title>|canonical|name="robots"'

# Sitemap i lastmod
curl -s https://machiroku.com/ca/sitemap.xml | grep -E '<loc>|<lastmod>'

# Redirecció antiga
curl -s https://machiroku.com/contacto/ | grep -E 'canonical|refresh'

# HTTP -> HTTPS
curl -s -o /dev/null -w '%{http_code} -> %{redirect_url}\n' http://machiroku.com/
```

---

## Registre de canvis

| Data | Canvi |
|------|-------|
| 2026-11-19 | Eliminades 10 pàgines primes (`categories`/`dishes`/`menus`); 61 redireccions; títols d'inici i sobre-nosaltres millorats; HTTPS forçat; `lastmod` als sitemaps; `static/CNAME` |
