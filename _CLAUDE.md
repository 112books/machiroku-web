CLAUDE.md — Projecte Machiroku.com
Última actualització: 2026-04-05
Estat del projecte: En desenvolupament actiu
Stack: Hugo + GitHub Pages + Decap CMS

🎯 VISIÓ DEL PROJECTE
Web corporativa per al restaurant japonès Machiroku (Barcelona), amb tres objectius clars:

Informar → oferta gastronòmica, horaris, ubicació
Activar → reserves immediates (telèfon/WhatsApp)
Autonomia → client edita continguts clau sense tocar codi


🏗️ ARQUITECTURA TÈCNICA
Stack principal

Generador: Hugo (web estàtica)
Hosting: GitHub Pages
CMS: Decap CMS (edició visual des de mòbil)
Repositori: https://github.com/112books/machiroku-web
Web provisional: https://112books.github.io/machiroku-web/ca/inici/

Directori local
/Users/joan/Documents/Obsidian/machiroku_hugo
Estructura del projecte
machiroku_hugo/
├── content/
│   ├── ca/          # Contingut en català (idioma principal)
│   ├── es/          # Contingut en castellà
│   └── en/          # Contingut en anglès
├── data/
│   ├── horaris.yaml           # Horaris base del restaurant
│   ├── excepcions.yaml        # Dies especials/tancaments
│   ├── avisos.yaml            # Avisos programats
│   ├── menu-migdia.yaml       # Menús del migdia
│   └── carta-nit.yaml         # Carta nocturna
├── layouts/
│   ├── _default/
│   └── partials/
├── static/
│   ├── css/
│   ├── js/
│   ├── images/
│   └── admin/       # Decap CMS
├── i18n/
│   ├── ca.yaml
│   ├── es.yaml
│   └── en.yaml
└── config.yaml

🌍 SISTEMA MULTIIDIOMA
Idiomes actius

Català (principal, /ca/)
Castellà (/es/)
Anglès (/en/)

Regles

Mateixa estructura per tots els idiomes
Contingut separat per llengua a /content/{lang}/
Traduccions de textos globals a /i18n/{lang}.yaml
CMS compatible amb edició multilingüe


🧠 SISTEMA CENTRAL: ESTAT DEL RESTAURANT
Aquest és el cor funcional del projecte.
Estats possibles

MENÚ MIGDIA → Dl-Dv 13:00-15:30
CARTA NIT → Dv-Ds 19:00-22:00
TANCAT

Lògica de decisió (prioritat descendent)

Excepcions → Dies especials definits manualment
Horari base → Franges regulars setmanals
Estat per defecte → TANCAT

Fonts de dades
data/horaris.yaml (horari base)
yamlhoraris:
  migdia:
    dies: ["dl","dt","dc","dj","dv"]
    obertura: "13:00"
    tancament: "15:30"
  nit:
    dies: ["dv","ds"]
    obertura: "19:00"
    tancament: "22:00"
data/excepcions.yaml (dies especials)
yamlexcepcions:
  - data: "2026-01-01"
    estat: "tancat"
    missatge: "Tancat per Cap d'Any"
  - data: "2026-08-15"
    estat: "obert"
    horari:
      obertura: "19:00"
      tancament: "23:00"
data/avisos.yaml (avisos programats)
yamlavisos:
  - des_de: "2025-12-25"
    fins_a: "2026-01-01"
    missatge: "Recordeu que l'1 de gener estarem tancats"

📄 ESTRUCTURA DEL WEB
HOME (/ca/inici/)

Hero visual amb CTA
Estat actual (Obert/Tancat + franja activa)
Avisos destacats
Plats del dia (si escau)
Horaris resumits
Destacats (targetes cap a seccions clau)
Contacte ràpid (telèfon click-to-call)

OFERTA GASTRONÒMICA (/ca/oferta/)
Migdia

Menú Sushi
Menú Tendon
Menú Salmon Don
Menú Unaju
Plat del dia (variable)

Nit (Dv-Ds)

Carta completa
Producte elaborat
CTA → Reserves

RESERVES (/ca/reserves/)

Canal principal: Telèfon
Alternativa: WhatsApp (missatge predefinit)
Explicació senzilla del procés
Horaris específics de reserves

Missatge WhatsApp:

"Hola, voldria reservar per X persones el dia X a les X."

ACERCA DE (/ca/acerca-de/)

Història del restaurant
Masahiro Tottori (xef)
Sachie (gestió)
Filosofia gastronòmica

CONTACTE (/ca/contacte/)

Direcció + Google Maps embed
Telèfon (click-to-call)
Email (machiroku@machiroku.com → Gmail)
Horaris separats per franja:

Menú Migdia: Dl-Dv 13:00-15:30
Carta Nit: Dv-Ds 19:00-22:00




⚙️ DECAP CMS
Objectiu
Permetre al client editar des de mòbil sense tocar codi:

Excepcions d'horari
Avisos programats
Textos bàsics del web
Menús i plats

Col·leccions editables

excepcions → Dies especials
avisos → Comunicacions temporals
menu-migdia → Plats del migdia
carta-nit → Plats nocturns
textos → Continguts globals

Regla crítica
El CMS MAI modifica l'estructura tècnica del sistema
(només edita continguts via fitxers YAML/Markdown)

🎨 DISSENY I UX
Concepte: MA (間) — Espai entre les coses

Minimalisme real (no decoració buida)
Jerarquia clara
Espais amplis
Tipografia protagonista

Paleta cromàtica

Blanc (fons principal)
Negre (text, accents)
Vermell subtil (CTA, destacats)

Animacions (MOLT subtils)
Permès:

Fades suaus (entrada de blocs)
Hover lleu en botons
Transicions de secció

PROHIBIT:

Efectes agressius
Animacions llargues
Distraccions visuals


♿ ACCESSIBILITAT (obligatori)

Estructura HTML semàntica
Navegació per teclat funcional
Contrast AA mínim (WCAG 2.1)
Focus visible
Jerarquia de headings correcta (h1 → h6)
alt descriptiu en totes les imatges


⚡ RENDIMENT
Objectius

Lighthouse: 95+ en totes les mètriques
Càrrega: instantània (<1s)
JS mínim (només imprescindible)
Imatges optimitzades (WebP, lazy loading)


📲 SISTEMA DE RESERVES
Actual

Telèfon com a canal principal

Evolució futura (opcions)

Bàsic → Telèfon + click-to-call
Intermedi → WhatsApp link amb missatge predefinit
Avançat → Formulari + notificacions

Regla: No complicar abans d'hora.

🌐 GOOGLE REVIEWS
Integració recomanada

Embed simple (widget oficial)
Enllaç directe al perfil de Google

Evitar: APIs complexes o scraping.

🚧 FASES DEL PROJECTE
Fase 1 — Base tècnica (2-3 dies)

 Estructura Hugo configurada
 Sistema multiidioma actiu
 Pàgines base creades

Fase 2 — Sistema funcional (3-4 dies)

 Motor d'estat (menú/carta/tancat)
 Horaris base operatius
 Sistema d'excepcions
 Avisos programats

Fase 3 — CMS (2 dies)

 Decap CMS configurat
 Col·leccions editables
 Autenticació GitHub

Fase 4 — Disseny UX/UI (4-6 dies)

 Wireframes finals
 Estil visual aplicat
 Animacions subtils
 Poliment visual

Fase 5 — Contingut (2-3 dies)

 Textos definitius
 Imatges optimitzades
 Traduccions completes

Fase 6 — Deploy (1 dia)

 GitHub Pages configurat
 Domini connectat (si escau)
 Certificat SSL actiu

Fase 7 — QA (1-2 dies)

 SEO revisat
 Performance > 95
 Accessibilitat validada
 Proves multiidioma
 Proves en mòbil


🧠 PUNTS CRÍTICS

El sistema d'horaris és la peça més delicada
→ Provar exhaustivament la lògica de decisió
El CMS no ha d'infectar la lògica del sistema
→ Només edita dades, mai codi
Multiidioma s'ha de decidir des del dia 1
→ Estructura de carpetes i rutes
El disseny no ha de comprometre la velocitat
→ Sempre prioritzar rendiment


📧 CORREU ELECTRÒNIC
Configuració actual

Domini: machiroku@machiroku.com
Redirecció: Gmail personal
Proveïdor: Dinahosting (?)

Opcions futures

Mantenir redirecció simple
Configurar SMTP per enviar com @machiroku.com


🚀 ESTAT ACTUAL I PRÒXIM PAS
Estat

Repositori creat: ✅
Web provisional activa: ✅
Fase actual: Base tècnica

Pròxim pas immediat
Dissenyar la HOME com a estructura (wireframe)
Definir:

Blocs exactes de contingut
Ordre visual i jerarquia
Què veu l'usuari en 3 segons
Com es mostra l'estat del restaurant


📝 NOTES TÈCNIQUES

Hugo version: (especificar després de hugo version)
Node.js version: (si cal per Decap CMS)
Comandaments clau:

bash  hugo server -D          # Servidor local
  hugo                    # Build production
  git push origin main    # Deploy a GitHub Pages

Aquest document és la font única de veritat per al projecte Machiroku.
Actualitzar-lo amb cada decisió important.