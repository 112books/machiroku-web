# Analytics — Referència tècnica

Sistema d'estadístiques basat en GoatCounter + GitHub Actions + dashboard estàtic.

---

## Arquitectura

```
GoatCounter API (machiroku.goatcounter.com)
    ↓  GitHub Action (cada hora)
scripts/build-analytics-json.py   → /tmp/raw_all.json
scripts/process-analytics.py      → static/admin/analytics.json
                                   → docs/admin/analytics.json
    ↓  servit estàticament
static/admin/index.html (dashboard protegit amb contrasenya)
```

---

## Fitxers clau

| Fitxer | Funció |
|--------|--------|
| `.github/workflows/fetch-analytics.yml` | Workflow horari: fetch → processa → commit |
| `scripts/build-analytics-json.py` | Consolida 5 respostes API → `/tmp/raw_all.json` |
| `scripts/process-analytics.py` | Transforma raw → `analytics.json` normalitzat |
| `static/admin/index.html` | Dashboard (Chart.js, login per SHA-256) |
| `static/admin/analytics.json` | Dades servides al dashboard |
| `docs/admin/analytics.json` | Còpia per GitHub Pages (sincronitzada al deploy) |

---

## Workflow (`fetch-analytics.yml`)

### Pas 1 — Fetch GoatCounter

Crida 5 endpoints de l'API v0:

```
/api/v0/stats/hits?start=START&end=END&limit=100
/api/v0/stats/browsers?start=START&end=END&limit=10
/api/v0/stats/systems?start=START&end=END&limit=10
/api/v0/stats/sizes?start=START&end=END&limit=10
/api/v0/stats/locations?start=START&end=END&limit=10
```

- `START` = 365 dies enrere, `END` = avui
- La funció `fetch_json` valida que la resposta sigui JSON; si no, escriu `null`
- `|| true` al curl evita que `set -e` mati el script per errors SSL/xarxa

### Pas 2 — `build-analytics-json.py`

Llegeix els 5 fitxers `/tmp/*.json` i els consolida a `/tmp/raw_all.json`.

Logging de depuració (surt a GitHub Actions → logs del pas):
- Si un fitxer és buit o null → `WARN: /tmp/X.json buit o null`
- Per cada endpoint amb dades → `DEBUG /tmp/X.json → key[0] keys: [...]`

### Pas 3 — `process-analytics.py`

Transforma `raw_all.json` → `analytics.json` amb estructura normalitzada.

**Funció `norm_items`** — extreu counts de browsers/systems/sizes/locations:
- GoatCounter API v0: `GET /stats/{page}` → `{"stats": [{id, name, count}]}`
- El camp principal és `item.count` (directe a l'item, no dins `stats[]`)
- Fallback: `stats[].daily` / `stats[].count` / `item.total` per compatibilitat

### Pas 4 — Commit

```bash
cp static/admin/analytics.json docs/admin/analytics.json
git add static/admin/analytics.json docs/admin/analytics.json
git diff --staged --quiet || git commit -m "chore: actualitzar analytics [skip ci]"
git pull --rebase && git push
```

---

## Estructura de `analytics.json`

```json
{
  "generated": "2026-04-18T18:11:31Z",
  "period": { "start": "2025-04-18", "end": "2026-04-18" },
  "total": 244,
  "hits_by_day": [{ "date": "2026-04-06", "count": 38 }],
  "by_lang":    { "ca": 188, "en": 31, "es": 25 },
  "by_section": { "inici": 101, "oferta": 51 },
  "browsers":   [{ "name": "Chrome", "id": "Chrome", "count": 150 }],
  "systems":    [{ "name": "Android", "id": "Android", "count": 90 }],
  "sizes":      [{ "name": "phone", "id": "phone", "count": 120 }],
  "locations":  [{ "name": "Spain", "id": "ES", "count": 200 }]
}
```

**IDs de mides vàlids** (per als icones del dashboard):
`phone`, `tablet`, `desktop`, `desktophd`, `larger`

---

## Configuració

| Variable | Valor |
|----------|-------|
| `GOATCOUNTER_TOKEN` | GitHub Secret (Settings → Secrets) |
| `GC_ACCOUNT` | `machiroku` (al workflow, línia `GC_ACCOUNT: machiroku`) |
| Contrasenya dashboard | SHA-256 de "machiroku" → `PW_HASH` a `index.html` |

**Canviar contrasenya:**
```bash
echo -n "nova_contrasenya" | sha256sum
# → actualitzar PW_HASH a static/admin/index.html
```

---

## Errors habituals

### Exit code 35 (SSL connect error)
**Causa:** curl no pot connectar amb `machiroku.goatcounter.com` per TLS.
**Fix aplicat:** `result=$(curl ...) || true` al workflow — el script continua i l'API retorna dades parcials.
**Símptoma residual:** Si tots els curls fallen, `analytics.json` queda buit (0 visites, arrays buits).

### Dispositius/navegadors buits (`browsers: []`, `sizes: []`)
**Causa probable:** GoatCounter retorna una estructura de `count` diferent de la que espera `norm_items`.
**Com diagnosticar:** Mirar els logs del pas "Fetch analytics data" a GitHub Actions → buscar línies `DEBUG /tmp/browsers.json`.
**Fix aplicat:** `norm_items` ara prova `stats[].daily`, `stats[].count`, `item.total` i `item.count`.

### El workflow corre al repo equivocat
**Causa:** El fitxer `.github/workflows/fetch-analytics.yml` existeix a un altre repo.
**Fix:** Eliminar el workflow del repo incorrecte.

---

## Adaptar a un altre web

1. Crear compte GoatCounter a `nom.goatcounter.com`
2. Generar API token a GoatCounter → Settings → API
3. Afegir secret `GOATCOUNTER_TOKEN` al repo GitHub
4. Al workflow: canviar `GC_ACCOUNT: machiroku` → `GC_ACCOUNT: nom`
5. Copiar `static/admin/` i `scripts/` al nou projecte
6. Actualitzar `PW_HASH` a `index.html` amb la nova contrasenya
7. Actualitzar el link "← Tornar al web" a `index.html`
8. Actualitzar `SECTION_NAMES` a `process-analytics.py` amb les seccions del nou web
