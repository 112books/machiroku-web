---
title: "Inici"
hero:
  titol: "Autèntica cuina japonesa des del 2000"
  subtitol: "Menú migdia de dilluns a divendres · Carta nit de dimecres a dissabte"
---

{{ define "main" }}
<section class="hero hero-home">
  <img src="{{ .Site.BaseURL }}logo-gran.svg" alt="Machiroku" class="hero-logo">
  <h1>Autèntica cuina japonesa des del 2000</h1>
  <p class="hero-subtitle">{{ i18n "ara_estem" }}: {{ partial "status.html" . }}</p>
</section>

<section class="featured">
  <div class="featured-grid">
    <div class="featured-item">
      <h3>{{ i18n "menu_migdia" }}</h3>
      <p>De dilluns a divendres. Sopa de miso, plat principal i postres.</p>
    </div>
    <div class="featured-item">
      <h3>{{ i18n "carta_nit" }}</h3>
      <p>De dimecres a dissabte. Sushi, sashimi, nigiri i plats tradicionals.</p>
    </div>
  </div>
</section>

<section class="cta-buttons">
  <a href="{{ .Site.BaseURL }}reserves/" class="btn btn-primary">{{ i18n "fer_reserva" }}</a>
  <a href="{{ .Site.BaseURL }}oferta/" class="btn btn-secondary">{{ i18n "veure_menu" }}</a>
</section>
{{ end }}
