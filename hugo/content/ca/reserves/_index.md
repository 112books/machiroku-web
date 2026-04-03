---
title: "Reserves"
---

{{ define "main" }}
<section class="page-header">
  <h1>{{ i18n "reserves" }}</h1>
  <p class="page-desc">Reserva la teva taula per a dinar o sopar</p>
</section>

<section class="reserves-info">
  <p class="reserves-intro">Per fer una reserva, pots trukar-nos directament o enviar-nos un WhatsApp. El servei de nit i els caps de setmana és recomanable reservar.</p>
  
  <div class="reserve-methods">
    <div class="reserve-method">
      <h3>{{ i18n "tel" }}</h3>
      <a href="tel:{{ site.Data.restaurant.telefon }}" class="btn btn-primary">
        {{ site.Data.restaurant.telefon }}
      </a>
      <p class="reserve-note">De dilluns a dissabte de 13:00h a 15:30h i de 20:00h a 23:00h</p>
    </div>
    
    <div class="reserve-method">
      <h3>WhatsApp</h3>
      <a href="https://wa.me/{{ site.Data.restaurant.whatsapp | replace "+" "" }}" class="btn">
        WhatsApp
      </a>
      <p class="whatsapp-msg">"Hola, voldria reservar per a X persones el dia X a les Xh."</p>
    </div>
  </div>
  
  <div class="reserve-note-box">
    <p><strong>Important:</strong> Les reserves per a sopar (nit) i dies festius són recomanables. El restaurant té places limitades.</p>
  </div>
</section>
{{ end }}
