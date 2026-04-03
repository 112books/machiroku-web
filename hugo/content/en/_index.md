---
title: "Home"
---
<section class="hero hero-home">
  <img src="{{ .Site.BaseURL }}logo-gran.svg" alt="Machiroku" class="hero-logo">
  <h1>Authentic Japanese cuisine since 2000</h1>
  <p class="hero-subtitle">{{ i18n "ara_estem" }}: {{ partial "status.html" . }}</p>
</section>

<section class="featured">
  <div class="featured-grid">
    <div class="featured-item">
      <h3>{{ i18n "menu_migdia" }}</h3>
      <p>Monday to Friday. Miso soup, main course and dessert.</p>
    </div>
    <div class="featured-item">
      <h3>{{ i18n "carta_nit" }}</h3>
      <p>Wednesday to Saturday. Sushi, sashimi, nigiri and traditional dishes.</p>
    </div>
  </div>
</section>

<section class="cta-buttons">
  <a href="{{ "/reserves/" | relLangURL }}" class="btn btn-primary">{{ i18n "fer_reserva" }}</a>
  <a href="{{ "/oferta/" | relLangURL }}" class="btn btn-secondary">{{ i18n "veure_menu" }}</a>
</section>
