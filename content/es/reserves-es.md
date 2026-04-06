---
title: "Reservas"
description: "Reserva mesa en el restaurante Machiroku. Teléfono y WhatsApp disponibles."
---

<section class="reserves-section">
  <div class="container">
    <div class="reserves-header">
      <h1>{{ i18n "fer_reserva" }}</h1>
      <p class="reserves-intro">{{ .Site.Data.restaurant.reserves.nota.es }}</p>
    </div>

    {{/* Mètodes de reserva */}}
    <div class="reserves-metodes">
      {{ $restaurant := .Site.Data.restaurant }}
      
      {{/* Telèfon */}}
      {{ if $restaurant.reserves.sistemes.telefon }}
      <div class="reserva-card reserva-telefon">
        <div class="reserva-icona">📞</div>
        <h3>{{ i18n "telefon" }}</h3>
        <p class="reserva-descripcio">La manera más rápida y directa</p>
        
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
        <p class="reserva-descripcio">Envíanos un mensaje</p>
        
        {{ $missatge := replace (replace (replace $restaurant.reserves.missatge_whatsapp.es "{personas}" "X") "{fecha}" "DD/MM/YYYY") "{hora}" "HH:MM" }}
        {{ $whatsappUrl := printf "https://wa.me/%s?text=%s" (replace $restaurant.whatsapp "+" "") (querify "text" $missatge | replaceRE "text=" "") }}
        
        <a href="{{ $whatsappUrl }}" target="_blank" rel="noopener" class="btn btn-primary btn-large">
          Abrir WhatsApp
        </a>
        
        <p class="reserva-numero">{{ $restaurant.whatsapp }}</p>
      </div>
      {{ end }}
    </div>

    {{/* Informació addicional */}}
    <div class="reserves-info">
      <div class="info-card">
        <h3>🕐 Horario de reservas</h3>
        <div class="info-content">
          {{ $horaris := .Site.Data.horaris.base }}
          
          <div class="info-item">
            <strong>{{ i18n "servei_menu" }}</strong>
            <p>No es necesaria reserva previa</p>
            <p class="info-detail">Lu, Ma, Ju, Vi: 13:00 - 15:30</p>
          </div>
          
          <div class="info-item">
            <strong>{{ i18n "servei_carta" }}</strong>
            <p>{{ i18n "reserves_recomanades" }}</p>
            <p class="info-detail">Vi, Sá: 19:00 - 22:00</p>
          </div>
        </div>
      </div>

      <div class="info-card">
        <h3>ℹ️ Información importante</h3>
        <div class="info-content">
          <ul class="info-llista">
            <li>Las reservas se confirman por orden de llegada</li>
            <li>Mesas para grupos de más de 6 personas, contactar directamente</li>
            <li>Si no puedes asistir, agradeceremos que nos lo comuniques</li>
            <li>Máximo 2 horas de mesa por grupo</li>
          </ul>
        </div>
      </div>

      <div class="info-card">
        <h3>📍 Cómo llegar</h3>
        <div class="info-content">
          {{ $lang := .Site.Language.Lang }}
          <p><strong>{{ index $restaurant.adreca.complet $lang }}</strong></p>
          
          <div class="transport-info">
            <p><strong>Metro:</strong> L4 (Jaume I) - 3 min caminando</p>
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
      <p>¿Tienes alguna pregunta o petición especial?</p>
      <a href="{{ .Site.BaseURL }}{{ .Site.Language.Lang }}/contacte/" class="btn btn-outline">
        {{ i18n "contacte" }}
      </a>
    </div>
  </div>
</section>
