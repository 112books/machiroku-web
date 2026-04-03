---
title: "Reservas"
---

{{ define "main" }}
<section class="page-header">
  <h1>{{ i18n "reserves" }}</h1>
  <p class="page-desc">Reserva tu mesa para comer o cenar</p>
</section>

<section class="reserves-info">
  <p class="reserves-intro">Para hacer una reserva, puedes llamarnos directamente o enviarnos un WhatsApp. El servicio de noche y fines de semana es recomendable reservar.</p>
  
  <div class="reserve-methods">
    <div class="reserve-method">
      <h3>{{ i18n "tel" }}</h3>
      <a href="tel:{{ site.Data.restaurant.telefon }}" class="btn btn-primary">
        {{ site.Data.restaurant.telefon }}
      </a>
      <p class="reserve-note">De lunes a sábado de 13:00h a 15:30h y de 20:00h a 23:00h</p>
    </div>
    
    <div class="reserve-method">
      <h3>WhatsApp</h3>
      <a href="https://wa.me/{{ site.Data.restaurant.whatsapp | replace "+" "" }}" class="btn">
        WhatsApp
      </a>
      <p class="whatsapp-msg">"Hola, me gustaría reservar para X personas el día X a las Xh."</p>
    </div>
  </div>
</section>
{{ end }}
