---
title: "Menu"
---

{{ define "main" }}
<section class="page-header">
  <h1>{{ i18n "oferta" }}</h1>
  <p class="page-desc">Lunch menu and dinner à la carte</p>
</section>

<section class="offer-section">
  <h2>Menu Monday - Friday</h2>
  
  <div class="menu-list">
    <article class="menu-item">
      <div class="menu-header">
        <h3>Sushi Menu</h3>
        <span class="price">16,00 €</span>
      </div>
      <p class="menu-desc">5 nigiri + 4 maki, Wafu sarada, Miso Soup</p>
    </article>
    
    <article class="menu-item">
      <div class="menu-header">
        <h3>Salmon Don Menu</h3>
        <span class="price">16,00 €</span>
      </div>
      <p class="menu-desc">Salmon Don (sashimi on rice), Kobachi, Miso Soup</p>
    </article>
    
    <article class="menu-item">
      <div class="menu-header">
        <h3>Tendon Menu</h3>
        <span class="price">16,00 €</span>
      </div>
      <p class="menu-desc">Rice with shrimp and vegetable tempura, Sashimi moriawase, Miso Soup</p>
    </article>
    
    <article class="menu-item">
      <div class="menu-header">
        <h3>Unaju Menu</h3>
        <span class="price">17,50 €</span>
      </div>
      <p class="menu-desc">Rice with grilled eel in sauce, Sashimi moriawase, Miso Soup</p>
    </article>
  </div>
</section>

<section class="offer-section">
  <h2>Starters</h2>
  <div class="menu-list">
    <article class="menu-item">
      <div class="menu-header">
        <h3>Goma Wakame</h3>
        <span class="price">5,00 €</span>
      </div>
      <p class="menu-desc">Wakame seaweed salad with sesame</p>
    </article>
    
    <article class="menu-item">
      <div class="menu-header">
        <h3>Yakitori</h3>
        <span class="price">5,50 €</span>
      </div>
      <p class="menu-desc">chicken skewers</p>
    </article>
    
    <article class="menu-item">
      <div class="menu-header">
        <h3>Gyoza</h3>
        <span class="price">5,50 €</span>
      </div>
      <p class="menu-desc">4 pork dumplings</p>
    </article>
  </div>
</section>

<section class="cta-buttons">
  <a href="{{ "/reserves/" | relLangURL }}" class="btn btn-primary">{{ i18n "fer_reserva" }}</a>
</section>
{{ end }}
