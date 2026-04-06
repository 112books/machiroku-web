# Guia d'edició de la carta — Machiroku

> Aquesta guia explica com afegir, modificar o desactivar plats i menús del web.
> No cal tocar cap codi. Només cal editar fitxers YAML i fer un deploy.

---

## Índex

1. [Estructura de fitxers](#1-estructura-de-fitxers)
2. [Editar els menús del migdia](#2-editar-els-menús-del-migdia)
3. [Editar la carta nocturna (plats)](#3-editar-la-carta-nocturna-plats)
4. [Afegir fotos als plats](#4-afegir-fotos-als-plats)
5. [Al·lèrgens disponibles](#5-allèrgens-disponibles)
6. [Publicar els canvis](#6-publicar-els-canvis)

---

## 1. Estructura de fitxers

Els continguts de la carta estan a la carpeta `data/`, separats per idioma:

```
data/
  ca/
    menus.yaml      ← Menús del migdia en català
    plats.yaml      ← Carta nocturna en català
    alergics.yaml   ← Llista d'al·lèrgens
  es/
    menus.yaml      ← Menús del migdia en castellà
    plats.yaml      ← Carta nocturna en castellà
  en/
    menus.yaml      ← Menús del migdia en anglès
    plats.yaml      ← Carta nocturna en anglès
```

> **Important:** Quan canviïs un plat o menú, recorda editar els **tres idiomes** (ca, es, en).

---

## 2. Editar els menús del migdia

El fitxer és `data/ca/menus.yaml`. Cada menú té aquesta estructura:

```yaml
- id: "menu-sushi"           # Identificador únic (no canviar)
  nom: "Menú Sushi"          # Nom que apareix al web
  ordre: 1                   # Ordre de visualització (1 = primer)
  actiu: true                # true = visible | false = ocult
  preu: 14.50                # Preu en euros
  foto: ""                   # Deixar buit si no hi ha foto
  descripcio: "El nostre clàssic menú japonès amb varietat de sushi fresc"
  plats:
    - "Sopa miso"
    - "Amanida wakame"
    - "8 peces de sushi variats"
    - "Postre casolà"
    - "Te verd"
  alergics:
    - "peix"
    - "gluten"
    - "soja"
  disponibilitat:
    dies: ["dilluns", "dimarts", "dijous", "divendres"]
    horari: "13:00 - 15:30"
```

### Accions habituals

**Canviar el preu d'un menú:**
```yaml
preu: 15.00   # Era 14.50
```

**Canviar els plats inclosos:**
```yaml
plats:
  - "Sopa miso"
  - "Amanida de temporada"   # Canviat
  - "Nigiri de salmó (6 peces)"   # Canviat
  - "Te verd"
```

**Desactivar un menú temporalment** (no apareix al web però es conserva):
```yaml
actiu: false
```

**Afegir un menú nou:** Copia el bloc d'un menú existent, canvia l'`id` i el contingut, i assigna-li un `ordre` nou.

**Plat del dia** (preu variable): Deixa el preu a `0` i afegeix una nota:
```yaml
preu: 0
nota: "Preu i contingut variable. Preguntar al restaurant."
```

---

## 3. Editar la carta nocturna (plats)

El fitxer és `data/ca/plats.yaml`. Té dues parts: **categories** i **plats**.

### Categories

```yaml
categories:
  - id: "entrants"
    nom: "Entrants"
    ordre: 1       # Ordre en què apareixen al web
```

Les categories disponibles (no les canviïs sense actualitzar els plats):
- `entrants` — Entrants
- `amanides` — Amanides
- `sashimi` — Sashimi
- `nigiri-maki` — Nigiri i Maki
- `calents` — Plats calents
- `postres` — Postres

### Plats

```yaml
plats:
  - id: "goma-wakame"           # Identificador únic (no canviar)
    nom: "Goma Wakame"          # Nom al web
    categoria: "entrants"       # Ha de coincidir amb un id de categories
    ordre: 1                    # Ordre dins la categoria
    actiu: true                 # true = visible | false = ocult
    destacat: false             # true = mostra badge "Destacat"
    preu: 7.50                  # Preu en euros
    foto: ""                    # Deixar buit si no hi ha foto
    descripcio: "Amanida d'algues amb sèsam torrat i vinagreta japonesa"
    alergics:
      - "sesam"
      - "soja"
```

### Accions habituals

**Canviar el preu:**
```yaml
preu: 8.00
```

**Marcar com a destacat** (apareix amb badge):
```yaml
destacat: true
```

**Desactivar un plat** (no apareix al web):
```yaml
actiu: false
```

**Afegir un plat nou:**
```yaml
  - id: "edamame"              # Identificador únic, sense espais ni accents
    nom: "Edamame"
    categoria: "entrants"
    ordre: 3
    actiu: true
    destacat: false
    preu: 5.00
    foto: ""
    descripcio: "Faves de soja al vapor amb sal marina"
    alergics:
      - "soja"
```

**Canviar l'ordre dels plats:** Modifica el número `ordre` (1 = primer, 2 = segon...).

**Moure un plat a una altra categoria:**
```yaml
categoria: "calents"   # Era "entrants"
```

---

## 4. Afegir fotos als plats

Les fotos han d'estar a `static/images/menus/` (per a menús) o `static/images/plats/` (per a la carta).

**Pas a pas:**
1. Prepara la foto en format `.jpg` o `.webp`
   - Mida recomanada: **800×600 px** (proporció 4:3)
   - Pes màxim: **200 KB**
2. Posa el fitxer a `static/images/menus/` o `static/images/plats/`
3. Al YAML, afegeix la ruta:

```yaml
foto: "/images/menus/nom-del-fitxer.jpg"
# o per a plats:
foto: "/images/plats/nom-del-fitxer.jpg"
```

> Si el camp `foto` és buit o la imatge no existeix, la targeta es mostra igualment sense imatge — no dona error.

---

## 5. Al·lèrgens disponibles

Usa exactament aquests identificadors al camp `alergics`:

| Identificador | Al·lèrgen |
|---------------|-----------|
| `gluten` | Gluten (blat, civada...) |
| `crustacis` | Crustacis |
| `ou` | Ou |
| `peix` | Peix |
| `cacauets` | Cacauets |
| `soja` | Soja |
| `lactis` | Lactis |
| `fruits-closca` | Fruits de closca |
| `api` | Api |
| `mostassa` | Mostassa |
| `sesam` | Sèsam |
| `diòxid-sofre` | Diòxid de sofre / Sulfits |
| `llupols` | Llavors de llupol |
| `mol·luscs` | Mol·luscs |

---

## 6. Publicar els canvis

Un cop fets els canvis als fitxers YAML, cal fer un deploy:

```bash
cd ~/Documents/Obsidian/machiroku_hugo
./symc-machiroku.sh deploy
```

Selecciona l'opció **4 → Deploy** al menú.

El deploy fa:
1. Reconstrueix el web amb Hugo
2. Puja els canvis a GitHub
3. GitHub Pages publica el web en 1-2 minuts

> **Recorda:** Editar els tres idiomes (`data/ca/`, `data/es/`, `data/en/`) per mantenir la coherència del web multilingüe.

---

*Generat per LinuxBCN.com — Projecte Machiroku*