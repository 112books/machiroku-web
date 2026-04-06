---
title: "Reserves"
description: "Reserva taula al restaurant Machiroku. Telèfon i WhatsApp disponibles."
---

<section class="reserves-section">
  <div class="container">
    <div class="reserves-header">
      <h1>{{ i18n "fer_reserva" }}</h1>
      <p class="reserves-intro">{{ .Site.Data.restaurant.reserves.nota.ca }}</p>
    </div>

    {{/* Mètodes de reserva */}}
    <div class="reserves-metodes">
      {{ $restaurant := .Site.Data.restaurant }}
      
      {{/* Telèfon */}}
      {{ if $restaurant.reserves.sistemes.telefon }}
      <div class="reserva-card reserva-telefon">
        <div class="reserva-icona">📞</div>
        <h3>{{ i18n "telefon" }}</h3>
        <p class="reserva-descripcio">La manera més ràpida i directa</p>
        
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
        <p class="reserva-descripcio">Envia'ns un missatge</p>
        
        {{ $missatge := replace (replace (replace $restaurant.reserves.missatge_whatsapp.ca "{persones}" "X") "{data}" "DD/MM/YYYY") "{hora}" "HH:MM" }}
        {{ $whatsappUrl := printf "https://wa.me/%s?text=%s" (replace $restaurant.whatsapp "+" "") (querify "text" $missatge | replaceRE "text=" "") }}
        
        <a href="{{ $whatsappUrl }}" target="_blank" rel="noopener" class="btn btn-primary btn-large">
          Obrir WhatsApp
        </a>
        
        <p class="reserva-numero">{{ $restaurant.whatsapp }}</p>
      </div>
      {{ end }}
    </div>

    {{/* Informació addicional */}}
    <div class="reserves-info">
      <div class="info-card">
        <h3>🕐 Horari de reserves</h3>
        <div class="info-content">
          {{ $horaris := .Site.Data.horaris.base }}
          
          <div class="info-item">
            <strong>{{ i18n "servei_menu" }}</strong>
            <p>No cal reserva prèvia</p>
            <p class="info-detail">Dl, Dt, Dj, Dv: 13:00 - 15:30</p>
          </div>
          
          <div class="info-item">
            <strong>{{ i18n "servei_carta" }}</strong>
            <p>{{ i18n "reserves_recomanades" }}</p>
            <p class="info-detail">Dv, Ds: 19:00 - 22:00</p>
          </div>
        </div>
      </div>

      <div class="info-card">
        <h3>ℹ️ Informació important</h3>
        <div class="info-content">
          <ul class="info-llista">
            <li>Les reserves es confirmen per ordre d'arribada</li>
            <li>Taules per a grups de més de 6 persones, contactar directament</li>
            <li>Si no pots assistir, agrairem que ens ho comuniquis</li>
            <li>Màxim 2 hores de taula per grup</li>
          </ul>
        </div>
      </div>

      <div class="info-card">
        <h3>📍 Com arribar</h3>
        <div class="info-content">
          {{ $lang := .Site.Language.Lang }}
          <p><strong>{{ index $restaurant.adreca.complet $lang }}</strong></p>
          
          <div class="transport-info">
            <p><strong>Metro:</strong> L4 (Jaume I) - 3 min caminant</p>
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
      <p>Tens alguna pregunta o petició especial?</p>
      <a href="{{ .Site.BaseURL }}{{ .Site.Language.Lang }}/contacte/" class="btn btn-outline">
        {{ i18n "contacte" }}
      </a>
    </div>
  </div>
</section>

<style>
.reserves-section {
  padding: var(--spacing-xl) var(--spacing-md);
  background: var(--color-gray-light);
  min-height: 70vh;
}

.reserves-header {
  text-align: center;
  margin-bottom: var(--spacing-xl);
}

.reserves-header h1 {
  font-size: 3rem;
  margin-bottom: var(--spacing-sm);
}

.reserves-intro {
  font-size: 1.125rem;
  color: var(--color-gray-dark);
  max-width: 600px;
  margin: 0 auto;
}

/* Mètodes de reserva */
.reserves-metodes {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
  gap: var(--spacing-lg);
  margin-bottom: var(--spacing-xl);
  max-width: 900px;
  margin-left: auto;
  margin-right: auto;
}

.reserva-card {
  background: white;
  padding: var(--spacing-xl);
  border-radius: 12px;
  text-align: center;
  box-shadow: var(--shadow-md);
  transition: transform var(--transition-normal);
}

.reserva-card:hover {
  transform: translateY(-4px);
  box-shadow: var(--shadow-lg);
}

.reserva-icona {
  font-size: 4rem;
  margin-bottom: var(--spacing-md);
}

.reserva-card h3 {
  font-size: 1.75rem;
  margin-bottom: var(--spacing-sm);
}

.reserva-descripcio {
  color: var(--color-gray-dark);
  margin-bottom: var(--spacing-lg);
}

.reserva-numero {
  margin-top: var(--spacing-md);
  font-size: 1.25rem;
  font-weight: 600;
  color: var(--color-gray-dark);
}

/* Informació addicional */
.reserves-info {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
  gap: var(--spacing-lg);
  margin-bottom: var(--spacing-xl);
}

.info-card {
  background: white;
  padding: var(--spacing-lg);
  border-radius: 8px;
  box-shadow: var(--shadow-sm);
}

.info-card h3 {
  font-size: 1.5rem;
  margin-bottom: var(--spacing-md);
  color: var(--color-black);
}

.info-content {
  font-size: 1rem;
  line-height: 1.6;
}

.info-item {
  margin-bottom: var(--spacing-md);
}

.info-item:last-child {
  margin-bottom: 0;
}

.info-item strong {
  display: block;
  font-size: 1.125rem;
  margin-bottom: 0.25rem;
  color: var(--color-accent);
}

.info-detail {
  font-size: 0.9rem;
  color: var(--color-gray-dark);
  margin-top: 0.25rem;
}

.info-llista {
  list-style: none;
  padding: 0;
}

.info-llista li {
  padding: 0.5rem 0;
  padding-left: 1.5rem;
  position: relative;
}

.info-llista li:before {
  content: "✓";
  position: absolute;
  left: 0;
  color: var(--color-accent);
  font-weight: bold;
}

.transport-info {
  margin: var(--spacing-md) 0;
  padding: var(--spacing-md);
  background: var(--color-gray-light);
  border-radius: 6px;
}

.transport-info p {
  margin-bottom: 0.5rem;
}

.transport-info p:last-child {
  margin-bottom: 0;
}

/* CTA final */
.reserves-cta {
  text-align: center;
  padding: var(--spacing-xl);
  background: white;
  border-radius: 12px;
  box-shadow: var(--shadow-sm);
}

.reserves-cta p {
  font-size: 1.25rem;
  margin-bottom: var(--spacing-md);
}

/* Responsive */
@media (max-width: 768px) {
  .reserves-header h1 {
    font-size: 2rem;
  }
  
  .reserves-metodes {
    grid-template-columns: 1fr;
  }
  
  .reserves-info {
    grid-template-columns: 1fr;
  }
}
</style>
