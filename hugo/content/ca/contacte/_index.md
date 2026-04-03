---
title: "Contacte"
---

{{ define "main" }}
<section class="page-header">
  <h1>{{ i18n "contacte" }}</h1>
</section>

<section class="contact-grid">
  <div class="contact-item">
    <h3>{{ i18n "adresa" }}</h3>
    <p>{{ site.Data.restaurant.adreca.ca }}</p>
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

<section class="map">
  <iframe 
    src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d2983.538860095403!2d2.1730995!3d41.3828935!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x12a4a2f5c5c5c5c5%3A0x5c5c5c5c5c5c5c5c!2sMachiroku!5e0!3m2!1sca!2ses!4v1234567890" 
    width="100%" 
    height="400" 
    style="border:0;" 
    allowfullscreen="" 
    loading="lazy">
  </iframe>
</section>
{{ end }}
