---
title: "Contacto"
---

{{ define "main" }}
<section class="page-header">
  <h1>{{ i18n "contacte" }}</h1>
</section>

<section class="contact-section">
  <div class="contact-grid">
    <div class="contact-item">
      <h3>{{ i18n "ubicacio" }}</h3>
      <p>Calle Magdalenas, 23</p>
      <p>08003 Barcelona</p>
      <a href="https://maps.google.com/?q=Machiroku+Barcelona" target="_blank" class="btn">{{ i18n "obrir_google_maps" }}</a>
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
      <p><strong>{{ i18n "menu_migdia" }}:</strong> Lunes - Viernes: 13:00h - 15:30h</p>
      <p><strong>{{ i18n "carta_nit" }}:</strong> Jueves - Sábado: 20:00h - 23:00h</p>
    </div>
  </div>
</section>
{{ end }}
