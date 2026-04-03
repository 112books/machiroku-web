---
title: "Contact"
---

{{ define "main" }}
<section class="page-header">
  <h1>{{ i18n "contacte" }}</h1>
</section>

<section class="contact-grid">
  <div class="contact-item">
    <h3>{{ i18n "adresa" }}</h3>
    <p>{{ site.Data.restaurant.adreca.en }}</p>
    <a href="{{ site.Data.restaurant.google_maps_url }}" target="_blank" class="link">{{ i18n "obrir_google_maps" }}</a>
  </div>
  
  <div class="contact-item">
    <h3>{{ i18n "tel" }}</h3>
    <p><a href="tel:{{ site.Data.restaurant.telefon }}">{{ site.Data.restaurant.telefon }}</a></p>
  </div>
  
  <div class="contact-item">
    <h3>{{ i18n "email" }}</h3>
    <p><a href="mailto:{{ site.Data.restaurant.email }}">{{ site.Data.restaurant.email }}</a></p>
  </div>
  
  <div class="contact-item">
    <h3>{{ i18n "horaris" }}</h3>
    <p><strong>{{ i18n "menu_migdia" }}:</strong> {{ site.Data.horaris.horaris.menu.obertura }} - {{ site.Data.horaris.horaris.menu.tancament }}</p>
    <p><strong>{{ i18n "carta_nit" }}:</strong> {{ site.Data.horaris.horaris.carta.obertura }} - {{ site.Data.horaris.horaris.carta.tancament }}</p>
  </div>
</section>
{{ end }}
