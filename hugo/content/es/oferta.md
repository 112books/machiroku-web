---
title: "Oferta gastronómica"
slug: "oferta"
---

# Oferta gastronómica

## Reservas

[Reservar ahora →](/machiroku-web/es/reserves/)

## Menú del día (Lunes - Viernes)

{{ range where .Site.RegularPages "Section" "menus" }}
{{ if .Params.available }}
- **{{ .Params.title_es | default .Title }}** - {{ .Params.price }} € - {{ .Params.description_es | default .Params.description }}
{{ end }}
{{ end }}

## Carta de noche (Jueves - Sábado)

{{ $categories := where .Site.RegularPages "Section" "categories" | sortByParam "order" }}

{{ range $categories }}
### {{ .Params.name_es | default .Params.name }}

{{ $dishes := where (where $.Site.RegularPages "Section" "dishes") "Params.category" "==" (.Params.name) }}
{{ range $dishes }}
{{ if .Params.available }}
- **{{ .Params.name_es | default .Params.name }}** {{ if .Params.description_es }}({{ .Params.description_es }}){{ end }} - {{ .Params.price }} €
{{ end }}
{{ end }}

{{ end }}

[Reservar una mesa](/machiroku-web/es/reserves/)
