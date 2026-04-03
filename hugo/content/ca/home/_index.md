---
title: "Inici"
hero:
  titol: "Autèntica cuina japonesa"
  subtitol: "Menú migdia de dilluns a divendres · Carta nit divendres i dissabte"
---

{{ define "main" }}
<section class="hero">
  <h1>{{ .Title }}</h1>
  <p class="hero-subtitle">{{ i18n "ara_estem" }}: {{ partial "status.html" . }}</p>
</section>

<section class="cta-buttons">
  <a href="{{ "/reserves" | relLangURL }}" class="btn btn-primary">{{ i18n "fer_reserva" }}</a>
  <a href="{{ "/oferta" | relLangURL }}" class="btn btn-secondary">{{ i18n "oferta" }}</a>
</section>
{{ end }}
