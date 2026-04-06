---
title: "Reservations"
description: "Book a table at Machiroku restaurant. Phone and WhatsApp available."
---

<section class="reserves-section">
  <div class="container">
    <div class="reserves-header">
      <h1>{{ i18n "fer_reserva" }}</h1>
      <p class="reserves-intro">{{ .Site.Data.restaurant.reserves.nota.en }}</p>
    </div>

    {{/* Mètodes de reserva */}}
    <div class="reserves-metodes">
      {{ $restaurant := .Site.Data.restaurant }}
      
      {{/* Telèfon */}}
      {{ if $restaurant.reserves.sistemes.telefon }}
      <div class="reserva-card reserva-telefon">
        <div class="reserva-icona">📞</div>
        <h3>{{ i18n "telefon" }}</h3>
        <p class="reserva-descripcio">The fastest and most direct way</p>
        
        <a href="tel:{{ $restaurant.telefon }}" class="btn btn-primary btn-large">
          {{ i18n "trucar_ara" }}
        </a>
        
        <p class="reserva-numero">{{ $restaurant.telefon }}</p>
      </div>
      {{ end }}

      {{/* WhatsApp */}}
      {{ if $restaurant.reserves.sistemes.whatsapp }}
      <div class="reserva-card reserva-whatsapp">
        <div class="reserva-icona">💬</div>
        <h3>WhatsApp</h3>
        <p class="reserva-descripcio">Send us a message</p>
        
        {{ $missatge := replace (replace (replace $restaurant.reserves.missatge_whatsapp.en "{people}" "X") "{date}" "DD/MM/YYYY") "{time}" "HH:MM" }}
        {{ $whatsappUrl := printf "https://wa.me/%s?text=%s" (replace $restaurant.whatsapp "+" "") (querify "text" $missatge | replaceRE "text=" "") }}
        
        <a href="{{ $whatsappUrl }}" target="_blank" rel="noopener" class="btn btn-primary btn-large">
          Open WhatsApp
        </a>
        
        <p class="reserva-numero">{{ $restaurant.whatsapp }}</p>
      </div>
      {{ end }}
    </div>

    {{/* Informació addicional */}}
    <div class="reserves-info">
      <div class="info-card">
        <h3>🕐 Reservation hours</h3>
        <div class="info-content">
          {{ $horaris := .Site.Data.horaris.base }}
          
          <div class="info-item">
            <strong>{{ i18n "servei_menu" }}</strong>
            <p>No prior reservation needed</p>
            <p class="info-detail">Mon, Tue, Thu, Fri: 1:00 PM - 3:30 PM</p>
          </div>
          
          <div class="info-item">
            <strong>{{ i18n "servei_carta" }}</strong>
            <p>{{ i18n "reserves_recomanades" }}</p>
            <p class="info-detail">Fri, Sat: 7:00 PM - 10:00 PM</p>
          </div>
        </div>
      </div>

      <div class="info-card">
        <h3>ℹ️ Important information</h3>
        <div class="info-content">
          <ul class="info-llista">
            <li>Reservations are confirmed on a first-come, first-served basis</li>
            <li>For groups of more than 6 people, please contact us directly</li>
            <li>If you cannot attend, we appreciate if you let us know</li>
            <li>Maximum 2 hours per table per group</li>
          </ul>
        </div>
      </div>

      <div class="info-card">
        <h3>📍 How to get here</h3>
        <div class="info-content">
          {{ $lang := .Site.Language.Lang }}
          <p><strong>{{ index $restaurant.adreca.complet $lang }}</strong></p>
          
          <div class="transport-info">
            <p><strong>Metro:</strong> L4 (Jaume I) - 3 min walk</p>
            <p><strong>Bus:</strong> 45, 120, V15, V17</p>
          </div>
          
          <a href="{{ $restaurant.google_maps.url }}" target="_blank" rel="noopener" class="btn btn-outline">
            {{ i18n "veure_mapa" }}
          </a>
        </div>
      </div>
    </div>

    {{/* CTA final */}}
    <div class="reserves-cta">
      <p>Do you have any questions or special requests?</p>
      <a href="{{ .Site.BaseURL }}{{ .Site.Language.Lang }}/contacte/" class="btn btn-outline">
        {{ i18n "contacte" }}
      </a>
    </div>
  </div>
</section>
