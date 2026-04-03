---
title: "Reservas"
---

{{ define "main" }}
<section class="page-header">
  <h1>{{ i18n "reserves" }}</h1>
</section>

<section class="reserves-info">
  <p class="reserves-intro">Las reservas solo están disponibles para el servicio de noche y días festivos.</p>
  
  <div class="reserve-methods">
    <div class="reserve-method">
      <h3>{{ i18n "tel" }}</h3>
      <a href="tel:{{ site.Data.restaurant.telefon }}" class="btn btn-primary">
        {{ site.Data.restaurant.telefon }}
      </a>
    </div>
    
    <div class="reserve-method">
      <h3>WhatsApp</h3>
      <a href="https://wa.me/{{ site.Data.restaurant.whatsapp | replace "+" "" }}" class="btn btn-secondary">
        WhatsApp
      </a>
      <p class="whatsapp-msg">"Hola, quisiera reservar para X personas el día X a las X."</p>
    </div>
  </div>
</section>
{{ end }}
