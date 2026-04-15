# Machiroku — Guia d'operació del web

Web corporativa del restaurant japonès Machiroku (Barcelona).
Construït amb Hugo, allotjat a GitHub Pages.

---

## Adreces del web

| | URL |
|---|---|
| **Producció** | https://machiroku.com/ |
| **Staging** (proves) | https://112books.github.io/machiroku-web/ca/inici/ |
| **Estadístiques** | https://machiroku.com/admin/ |
| **Codi font** | https://github.com/112books/machiroku-web |

---

## Estadístiques de visites

Accedeix al panell d'estadístiques a `/admin/`:

- **URL**: https://machiroku.com/admin/
- **Contrasenya**: `machiroku`

El panell mostra:
- Visites per dia, setmana i mes (gràfic)
- Idiomes i seccions més visitades
- Navegadors, sistemes operatius i tipus de dispositiu

Les dades s'actualitzen automàticament cada hora.

---

## Publicar canvis al web

Des del terminal, a la carpeta del projecte:

```bash
./symc-machiroku.sh
```

Selecciona l'opció **5 → Deploy**.

El deploy fa:
1. Reconstrueix el web amb Hugo
2. Puja els canvis a GitHub
3. GitHub Pages publica el web en 1-2 minuts

> Sempre usa l'opció 5 (Deploy) per publicar. L'opció 4 (Push) només puja el codi sense reconstruir el web.

---

## Avisos temporals

Els avisos (tancaments, promocions, esdeveniments especials) es gestionen a `data/avisos.yaml`.

Apareixen com a **banner** (barra a dalt de la pàgina) o **popup** (modal) i s'activen i desactiven automàticament per dates.

### Estructura d'un avís

```yaml
- id: "tancat-setmana-santa"     # Identificador únic (no repetir)
  actiu: true                    # true = actiu | false = ignorat
  des_de: "2026-04-01"           # Data d'inici (YYYY-MM-DD)
  fins_a: "2026-04-06"           # Data de fi (YYYY-MM-DD)
  prioritat: "alta"              # alta (vermell) | mitjana (groc) | baixa (verd)
  tipus: "banner"                # banner (barra) | popup (modal)
  titol:
    ca: "Tancats per Setmana Santa"
    es: "Cerrados por Semana Santa"
    en: "Closed for Easter"
  text:
    ca: "Tornem el dimarts 7 d'abril."
    es: "Volvemos el martes 7 de abril."
    en: "We reopen on Tuesday 7 April."
  cta:
    ca: ""                       # Text del botó (opcional)
    es: ""
    en: ""
  link: ""                       # URL del botó (opcional)
```

### Com crear un avís nou

1. Obre `data/avisos.yaml`
2. Afegeix un bloc nou (copia el d'un existent i canvia el contingut)
3. Assigna un `id` únic
4. Posa `actiu: true`
5. Defineix les dates `des_de` i `fins_a`
6. Escriu el títol i text en els tres idiomes
7. Fes un deploy (opció 5)

Quan arribi la data `fins_a`, l'avís desapareix sol. No cal desactivar-lo manualment.

---

## Menús del migdia

Els menús del migdia es gestionen als fitxers:

```
data/ca/menus.yaml    ← Català
data/es/menus.yaml    ← Castellà
data/en/menus.yaml    ← Anglès
```

> Quan canviïs un menú, recorda editar els tres idiomes.

### Estructura d'un menú

```yaml
- id: "menu-sushi"
  nom: "Menú Sushi"
  ordre: 1                       # Ordre de visualització (1 = primer)
  actiu: true                    # true = visible | false = ocult
  preu: 14.50
  foto: ""                       # Deixar buit fins tenir foto
  descripcio: "El nostre clàssic menú japonès..."
  plats:
    - "Sopa miso"
    - "8 peces de sushi variats"
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

**Canviar el preu:**
```yaml
preu: 15.00
```

**Canviar els plats inclosos:**
```yaml
plats:
  - "Sopa miso"
  - "Amanida de temporada"
  - "Nigiri de salmó (6 peces)"
```

**Desactivar un menú temporalment** (no apareix al web, es conserva):
```yaml
actiu: false
```

**Afegir un menú nou:** Copia el bloc d'un menú existent, canvia l'`id` i el contingut.

---

## Carta nocturna (plats)

La carta es gestiona als fitxers:

```
data/ca/plats.yaml    ← Català
data/es/plats.yaml    ← Castellà
data/en/plats.yaml    ← Anglès
```

### Categories disponibles

| id | Nom |
|----|-----|
| `entrants` | Entrants |
| `amanides` | Amanides |
| `carn` | Carn |
| `arros` | Arròs |
| `sashimi` | Sashimi |
| `nigiri` | Nigiri Sushi |
| `maki` | Maki Sushi |

### Estructura d'un plat

```yaml
- id: "goma-wakame"              # Identificador únic (sense espais ni accents)
  nom: "Goma Wakame"
  categoria: "entrants"          # Ha de coincidir amb un id de categories
  ordre: 1                       # Ordre dins la categoria (1 = primer)
  actiu: true                    # true = visible | false = ocult
  destacat: false                # true = mostra badge "Destacat"
  preu: 7.50
  foto: ""                       # Deixar buit fins tenir foto
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

**Marcar com a destacat:**
```yaml
destacat: true
```

**Desactivar un plat:**
```yaml
actiu: false
```

**Afegir un plat nou:** Copia el bloc d'un plat existent i canvia l'`id` i el contingut. L'`id` ha de ser únic, sense espais ni accents (usa guions: `nigiri-salmo`).

---

## Al·lèrgens

Usa exactament aquests identificadors al camp `alergics` de plats i menús:

| Identificador | Al·lèrgen |
|---------------|-----------|
| `gluten` | Gluten (blat, civada...) |
| `crustacis` | Crustacis |
| `ou` | Ou |
| `peix` | Peix |
| `cacauets` | Cacauets |
| `soja` | Soja |
| `lactis` | Lactis |
| `fruits-secs` | Fruits de closca |
| `api` | Api |
| `mostassa` | Mostassa |
| `sesam` | Sèsam |
| `sulfits` | Sulfits |
| `mol·luscos` | Mol·luscos |
| `altramossos` | Altramossos |

Les icones apareixen automàticament al web. Si l'identificador no coincideix exactament, la icona no es mostra.

---

## Fotos de plats i menús

Les fotos han d'estar a:
- `static/images/plats/` — per a la carta nocturna
- `static/images/menus/` — per als menús del migdia

**Especificacions:**
- Format: `.jpg` o `.webp`
- Mida recomanada: **800×600 px** (proporció 4:3)
- Pes màxim: **200 KB**

**Com afegir una foto:**
1. Posa el fitxer a `static/images/plats/` o `static/images/menus/`
2. Al YAML del plat o menú, afegeix la ruta:

```yaml
foto: "/images/plats/nom-del-fitxer.jpg"
```

Si la foto no existeix, la targeta es mostra igualment sense imatge.

---

## Horaris del restaurant

Els horaris es gestionen a `data/horaris.yaml`. Canviant aquest fitxer s'actualitzen els horaris a tot el web (header, footer i pàgina de contacte).

---

## Informació del restaurant

Telèfon, email, adreça, xarxes socials i Google Maps: `data/restaurant.yaml`.

---

## Estructura tècnica (referència)

Per a canvis de codi o consultes tècniques, consulta `CLAUDE.md`.

---

*Web desenvolupada per [LinuxBCN.com](https://linuxbcn.com)*
