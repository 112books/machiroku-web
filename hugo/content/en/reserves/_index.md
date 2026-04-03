---
title: "Reservations"
---

{{ define "main" }}
<section class="page-header">
  <h1>{{ i18n "reserves" }}</h1>
  <p class="page-desc">Book your table for lunch or dinner</p>
</section>

<section class="reserves-info">
  <p class="reserves-intro">To make a reservation, you can call us directly or send us a WhatsApp. Dinner service and weekends are recommended to book.</p>
  
  <div class="reserve-methods">
    <div class="reserve-method">
      <h3>{{ i18n "tel" }}</h3>
      <a href="tel:{{ site.Data.restaurant.telefon }}" class="btn btn-primary">
        {{ site.Data.restaurant.telefon }}
      </a>
      <p class="reserve-note">Monday - Saturday: 13:00h - 15:30h & 20:00h - 23:00h</p>
    </div>
    
    <div class="reserve-method">
      <h3>WhatsApp</h3>
      <a href="https://wa.me/{{ site.Data.restaurant.whatsapp | replace "+" "" }}" class="btn">
        WhatsApp
      </a>
      <p class="whatsapp-msg">"Hello, I would like to book for X people on X at Xh."</p>
    </div>
  </div>
</section>
{{ end }}
