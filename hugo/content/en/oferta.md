---
title: "Menu"
slug: "oferta"
---

# Menu

## Reservations

[Book now →](/machiroku-web/en/reserves/)

## Lunch Menu (Monday - Friday)

{{ range where .Site.RegularPages "Section" "menus" }}
{{ if .Params.available }}
- **{{ .Params.title_en | default .Title }}** - {{ .Params.price }} € - {{ .Params.description_en | default .Params.description }}
{{ end }}
{{ end }}

## Dinner Menu (Thursday - Saturday)

{{ $categories := where .Site.RegularPages "Section" "categories" | sortByParam "order" }}

{{ range $categories }}
### {{ .Params.name_en | default .Params.name }}

{{ $dishes := where (where $.Site.RegularPages "Section" "dishes") "Params.category" "==" (.Params.name) }}
{{ range $dishes }}
{{ if .Params.available }}
- **{{ .Params.name_en | default .Params.name }}** {{ if .Params.description_en }}({{ .Params.description_en }}){{ end }} - {{ .Params.price }} €
{{ end }}
{{ end }}

{{ end }}

[Book a table](/machiroku-web/en/reserves/)
