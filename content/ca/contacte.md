---
title: "Contacte"
description: "Contacta amb el restaurant Machiroku. Adreça, telèfon, email i horaris."
---

<section class="contacte-section">
  <div class="container">
    <div class="contacte-header">
      <h1>{{ i18n "contacte" }}</h1>
      <p class="contacte-intro">Vine a veure'ns o posa't en contacte amb nosaltres</p>
    </div>

    {{/* Grid principal */}}
    <div class="contacte-grid">
      {{/* Informació de contacte */}}
      <div class="contacte-info-bloc">
        {{ $restaurant := .Site.Data.restaurant }}
        {{ $lang := .Site.Language.Lang }}

        {{/* Adreça */}}
        <div class="contacte-item-gran">
          <div class="contacte-icona-gran">📍</div>
          <h3>{{ i18n "on_som" }}</h3>
          <p class="contacte-adreca">{{ index $restaurant.adreca.complet $lang }}</p>
          <a href="{{ $restaurant.google_maps.url }}" target="_blank" rel="noopener" class="btn btn-outline">
            {{ i18n "veure_mapa" }}
          </a>
        </div>

        {{/* Telèfon */}}
        <div class="contacte-item-gran">
          <div class="contacte-icona-gran">📞</div>
          <h3>{{ i18n "telefon" }}</h3>
          <p class="contacte-dada">
            <a href="tel:{{ $restaurant.telefon }}" class="contacte-link">
              {{ $restaurant.telefon }}
            </a>
          </p>
          <a href="tel:{{ $restaurant.telefon }}" class="btn btn-primary">
            {{ i18n "trucar_ara" }}
          </a>
        </div>

        {{/* Email */}}
        <div class="contacte-item-gran">
          <div class="contacte-icona-gran">✉️</div>
          <h3>Email</h3>
          <p class="contacte-dada">
            <a href="mailto:{{ $restaurant.email }}" class="contacte-link">
              {{ $restaurant.email }}
            </a>
          </p>
        </div>

        {{/* Xarxes socials */}}
        <div class="contacte-item-gran">
          <div class="contacte-icona-gran">🌐</div>
          <h3>{{ i18n "segueix_nos" }}</h3>
          <div class="contacte-social">
            {{ if $restaurant.xarxes.instagram.actiu }}
            <a href="{{ $restaurant.xarxes.instagram.url }}" target="_blank" rel="noopener" class="social-link">
              <svg width="24" height="24" viewBox="0 0 24 24" fill="currentColor"><path d="M7.8 2h8.4C19.4 2 22 4.6 22 7.8v8.4a5.8 5.8 0 0 1-5.8 5.8H7.8C4.6 22 2 19.4 2 16.2V7.8A5.8 5.8 0 0 1 7.8 2m-.2 2A3.6 3.6 0 0 0 4 7.8v8.4C4 18.39 5.61 20 7.8 20h8.4a3.6 3.6 0 0 0 3.6-3.6V7.8C20 5.61 18.39 4 16.2 4H7.8m9.65 1.5a1.25 1.25 0 0 1 1.25 1.25A1.25 1.25 0 0 1 17.25 8 1.25 1.25 0 0 1 16 6.75a1.25 1.25 0 0 1 1.25-1.25M12 7a5 5 0 0 1 5 5 5 5 0 0 1-5 5 5 5 0 0 1-5-5 5 5 0 0 1 5-5m0 2a3 3 0 0 0-3 3 3 3 0 0 0 3 3 3 3 0 0 0 3-3 3 3 0 0 0-3-3z"/></svg>
              Instagram
            </a>
            {{ end }}
            {{ if $restaurant.xarxes.facebook.actiu }}
            <a href="{{ $restaurant.xarxes.facebook.url }}" target="_blank" rel="noopener" class="social-link">
              <svg width="24" height="24" viewBox="0 0 24 24" fill="currentColor"><path d="M22 12c0-5.52-4.48-10-10-10S2 6.48 2 12c0 4.84 3.44 8.87 8 9.8V15H8v-3h2V9.5C10 7.57 11.57 6 13.5 6H16v3h-2c-.55 0-1 .45-1 1v2h3v3h-3v6.95c5.05-.5 9-4.76 9-9.95z"/></svg>
              Facebook
            </a>
            {{ end }}
          </div>
        </div>
      </div>

      {{/* Horaris */}}
      <div class="contacte-horaris-bloc">
        <h3>{{ i18n "horaris" }}</h3>
        
        {{ $horaris := .Site.Data.horaris.base }}
        
        <div class="horaris-taula">
          {{/* Dilluns */}}
          {{ $dilluns := index $horaris "dilluns" }}
          <div class="horari-fila">
            <div class="horari-dia">{{ i18n "dilluns" }}</div>
            <div class="horari-detall">
              {{ if $dilluns }}
              {{ range $dilluns }}
              <div class="horari-franja">
                <span class="horari-hores">{{ .inici }} - {{ .fi }}</span>
                <span class="horari-servei">{{ if eq .servei "menu" }}{{ i18n "servei_menu" }}{{ else }}{{ i18n "servei_carta" }}{{ end }}</span>
              </div>
              {{ end }}
              {{ else }}
              <span class="horari-tancat">{{ i18n "estat_tancat" }}</span>
              {{ end }}
            </div>
          </div>

          {{/* Dimarts */}}
          {{ $dimarts := index $horaris "dimarts" }}
          <div class="horari-fila">
            <div class="horari-dia">{{ i18n "dimarts" }}</div>
            <div class="horari-detall">
              {{ if $dimarts }}
              {{ range $dimarts }}
              <div class="horari-franja">
                <span class="horari-hores">{{ .inici }} - {{ .fi }}</span>
                <span class="horari-servei">{{ if eq .servei "menu" }}{{ i18n "servei_menu" }}{{ else }}{{ i18n "servei_carta" }}{{ end }}</span>
              </div>
              {{ end }}
              {{ else }}
              <span class="horari-tancat">{{ i18n "estat_tancat" }}</span>
              {{ end }}
            </div>
          </div>

          {{/* Dimecres */}}
          {{ $dimecres := index $horaris "dimecres" }}
          <div class="horari-fila">
            <div class="horari-dia">{{ i18n "dimecres" }}</div>
            <div class="horari-detall">
              {{ if $dimecres }}
              {{ range $dimecres }}
              <div class="horari-franja">
                <span class="horari-hores">{{ .inici }} - {{ .fi }}</span>
                <span class="horari-servei">{{ if eq .servei "menu" }}{{ i18n "servei_menu" }}{{ else }}{{ i18n "servei_carta" }}{{ end }}</span>
              </div>
              {{ end }}
              {{ else }}
              <span class="horari-tancat">{{ i18n "estat_tancat" }}</span>
              {{ end }}
            </div>
          </div>

          {{/* Dijous */}}
          {{ $dijous := index $horaris "dijous" }}
          <div class="horari-fila">
            <div class="horari-dia">{{ i18n "dijous" }}</div>
            <div class="horari-detall">
              {{ if $dijous }}
              {{ range $dijous }}
              <div class="horari-franja">
                <span class="horari-hores">{{ .inici }} - {{ .fi }}</span>
                <span class="horari-servei">{{ if eq .servei "menu" }}{{ i18n "servei_menu" }}{{ else }}{{ i18n "servei_carta" }}{{ end }}</span>
              </div>
              {{ end }}
              {{ else }}
              <span class="horari-tancat">{{ i18n "estat_tancat" }}</span>
              {{ end }}
            </div>
          </div>

          {{/* Divendres */}}
          {{ $divendres := index $horaris "divendres" }}
          <div class="horari-fila">
            <div class="horari-dia">{{ i18n "divendres" }}</div>
            <div class="horari-detall">
              {{ if $divendres }}
              {{ range $divendres }}
              <div class="horari-franja">
                <span class="horari-hores">{{ .inici }} - {{ .fi }}</span>
                <span class="horari-servei">{{ if eq .servei "menu" }}{{ i18n "servei_menu" }}{{ else }}{{ i18n "servei_carta" }}{{ end }}</span>
              </div>
              {{ end }}
              {{ else }}
              <span class="horari-tancat">{{ i18n "estat_tancat" }}</span>
              {{ end }}
            </div>
          </div>

          {{/* Dissabte */}}
          {{ $dissabte := index $horaris "dissabte" }}
          <div class="horari-fila">
            <div class="horari-dia">{{ i18n "dissabte" }}</div>
            <div class="horari-detall">
              {{ if $dissabte }}
              {{ range $dissabte }}
              <div class="horari-franja">
                <span class="horari-hores">{{ .inici }} - {{ .fi }}</span>
                <span class="horari-servei">{{ if eq .servei "menu" }}{{ i18n "servei_menu" }}{{ else }}{{ i18n "servei_carta" }}{{ end }}</span>
              </div>
              {{ end }}
              {{ else }}
              <span class="horari-tancat">{{ i18n "estat_tancat" }}</span>
              {{ end }}
            </div>
          </div>

          {{/* Diumenge */}}
          {{ $diumenge := index $horaris "diumenge" }}
          <div class="horari-fila">
            <div class="horari-dia">{{ i18n "diumenge" }}</div>
            <div class="horari-detall">
              {{ if $diumenge }}
              {{ range $diumenge }}
              <div class="horari-franja">
                <span class="horari-hores">{{ .inici }} - {{ .fi }}</span>
                <span class="horari-servei">{{ if eq .servei "menu" }}{{ i18n "servei_menu" }}{{ else }}{{ i18n "servei_carta" }}{{ end }}</span>
              </div>
              {{ end }}
              {{ else }}
              <span class="horari-tancat">{{ i18n "estat_tancat" }}</span>
              {{ end }}
            </div>
          </div>
        </div>
      </div>
    </div>

    {{/* Mapa de Google */}}
    <div class="contacte-mapa">
      <h3>{{ i18n "com_arribar" }}</h3>
      <div class="mapa-container">
        <iframe 
          src="{{ $restaurant.google_maps.embed }}"
          width="100%" 
          height="450" 
          style="border:0;" 
          allowfullscreen="" 
          loading="lazy" 
          referrerpolicy="no-referrer-when-downgrade">
        </iframe>
      </div>
      
      <div class="transport-info">
        <div class="transport-item">
          <strong>🚇 Metro:</strong> L4 (Jaume I) - 3 min caminant
        </div>
        <div class="transport-item">
          <strong>🚌 Bus:</strong> 45, 120, V15, V17
        </div>
        <div class="transport-item">
          <strong>🅿️ Pàrquing:</strong> BSM Moll de la Fusta (5 min caminant)
        </div>
      </div>
    </div>
  </div>
</section>

<style>
.contacte-section {
  padding: var(--spacing-xl) var(--spacing-md);
  background: var(--color-gray-light);
}

.contacte-header {
  text-align: center;
  margin-bottom: var(--spacing-xl);
}

.contacte-header h1 {
  font-size: 3rem;
  margin-bottom: var(--spacing-sm);
}

.contacte-intro {
  font-size: 1.125rem;
  color: var(--color-gray-dark);
}

.contacte-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: var(--spacing-xl);
  margin-bottom: var(--spacing-xl);
}

.contacte-info-bloc,
.contacte-horaris-bloc {
  background: white;
  padding: var(--spacing-xl);
  border-radius: 12px;
  box-shadow: var(--shadow-sm);
}

.contacte-item-gran {
  margin-bottom: var(--spacing-xl);
  padding-bottom: var(--spacing-xl);
  border-bottom: 1px solid var(--color-border);
}

.contacte-item-gran:last-child {
  border-bottom: none;
  margin-bottom: 0;
  padding-bottom: 0;
}

.contacte-icona-gran {
  font-size: 3rem;
  margin-bottom: var(--spacing-md);
}

.contacte-item-gran h3 {
  font-size: 1.5rem;
  margin-bottom: var(--spacing-sm);
}

.contacte-adreca,
.contacte-dada {
  font-size: 1.125rem;
  margin-bottom: var(--spacing-md);
  line-height: 1.5;
}

.contacte-link {
  color: var(--color-black);
  font-weight: 600;
  transition: color var(--transition-fast);
}

.contacte-link:hover {
  color: var(--color-accent);
}

.contacte-social {
  display: flex;
  flex-direction: column;
  gap: var(--spacing-sm);
}

.social-link {
  display: flex;
  align-items: center;
  gap: var(--spacing-sm);
  padding: var(--spacing-sm) var(--spacing-md);
  background: var(--color-gray-light);
  border-radius: 6px;
  color: var(--color-black);
  transition: all var(--transition-fast);
}

.social-link:hover {
  background: var(--color-accent);
  color: white;
}

/* Horaris */
.contacte-horaris-bloc h3 {
  font-size: 1.75rem;
  margin-bottom: var(--spacing-lg);
}

.horaris-taula {
  display: flex;
  flex-direction: column;
  gap: var(--spacing-sm);
}

.horari-fila {
  display: grid;
  grid-template-columns: 120px 1fr;
  gap: var(--spacing-md);
  padding: var(--spacing-sm) 0;
  border-bottom: 1px solid var(--color-border);
}

.horari-fila:last-child {
  border-bottom: none;
}

.horari-dia {
  font-weight: 600;
  color: var(--color-gray-dark);
}

.horari-detall {
  display: flex;
  flex-direction: column;
  gap: 0.25rem;
}

.horari-franja {
  display: flex;
  flex-direction: column;
}

.horari-hores {
  font-weight: 600;
  color: var(--color-black);
}

.horari-servei {
  font-size: 0.875rem;
  color: var(--color-accent);
}

.horari-tancat {
  color: var(--color-gray-mid);
  font-style: italic;
}

/* Mapa */
.contacte-mapa {
  background: white;
  padding: var(--spacing-xl);
  border-radius: 12px;
  box-shadow: var(--shadow-sm);
}

.contacte-mapa h3 {
  font-size: 1.75rem;
  margin-bottom: var(--spacing-lg);
}

.mapa-container {
  border-radius: 8px;
  overflow: hidden;
  margin-bottom: var(--spacing-lg);
}

.transport-info {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
  gap: var(--spacing-md);
}

.transport-item {
  padding: var(--spacing-md);
  background: var(--color-gray-light);
  border-radius: 6px;
}

/* Responsive */
@media (max-width: 1024px) {
  .contacte-grid {
    grid-template-columns: 1fr;
  }
  
  .horari-fila {
    grid-template-columns: 100px 1fr;
  }
}

@media (max-width: 768px) {
  .contacte-header h1 {
    font-size: 2rem;
  }
  
  .transport-info {
    grid-template-columns: 1fr;
  }
}
</style>
