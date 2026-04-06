---
title: "Inici"
description: "Restaurant japonès autèntic al cor de Barcelona. Menú del migdia i carta nocturna amb producte de temporada."
type: "home"
---

{{/* Hero Section */}}
<section class="hero">
  <div class="hero-content">
    <div class="hero-logo">
      <img src="{{ .Site.BaseURL }}logos/Machiroku-logo-gran-vectoritzat.svg" alt="Machiroku">
    </div>
    
    <h1 class="hero-slogan">{{ .Site.Language.Params.slogan }}</h1>
    
    {{/* Estat del restaurant */}}
    <div class="hero-estat">
      {{ partial "estat-restaurant.html" . }}
    </div>
    
    {{/* CTAs principals */}}
    <div class="hero-ctas">
      <a href="{{ .Site.BaseURL }}{{ .Site.Language.Lang }}/reserves/" class="btn btn-primary btn-large">
        {{ i18n "fer_reserva" }}
      </a>
      <a href="{{ .Site.BaseURL }}{{ .Site.Language.Lang }}/oferta/" class="btn btn-outline btn-large">
        {{ i18n "veure_carta" }}
      </a>
    </div>
  </div>
  
  {{/* Imatge de fons */}}
  <div class="hero-bg">
    <img src="{{ .Site.BaseURL }}images/machiroku-web-background.svg" alt="" aria-hidden="true">
  </div>
</section>

{{/* Plats destacats */}}
<section class="home-section destacats-section">
  <div class="container">
    <div class="section-header">
      <h2>{{ i18n "plats_principals" }}</h2>
      <p class="section-intro">Selecció dels nostres plats més populars</p>
    </div>

    <div class="plats-grid">
      {{ $lang := .Site.Language.Lang }}
      {{ $platsData := index .Site.Data $lang "plats" }}
      {{ $platsDestacats := where $platsData.plats "destacat" true }}
      {{ $platsActius := where $platsDestacats "actiu" true }}
      
      {{ range first 6 $platsActius }}
        {{ partial "plat-card.html" . }}
      {{ end }}
    </div>

    <div class="section-cta">
      <a href="{{ .Site.BaseURL }}{{ .Site.Language.Lang }}/oferta/" class="btn btn-primary">
        {{ i18n "veure_carta" }} completa
      </a>
    </div>
  </div>
</section>

{{/* Horaris i Reserves */}}
<section class="home-section horaris-section">
  <div class="container">
    <div class="horaris-grid">
      {{/* Bloc esquerra: Horaris */}}
      <div class="horaris-bloc">
        <h3>{{ i18n "horaris" }}</h3>
        
        {{ $horaris := .Site.Data.horaris.base }}
        
        <div class="horaris-llista">
          {{/* Menú migdia */}}
          {{ $dilluns := index $horaris "dilluns" }}
          {{ if $dilluns }}
          <div class="horari-item">
            <div class="horari-dia">
              <strong>{{ i18n "dilluns" }}, {{ i18n "dimarts" }}, {{ i18n "dijous" }}, {{ i18n "divendres" }}</strong>
            </div>
            <div class="horari-hores">
              {{ (index $dilluns 0).inici }} - {{ (index $dilluns 0).fi }}
            </div>
            <div class="horari-servei">{{ i18n "servei_menu" }}</div>
          </div>
          {{ end }}
          
          {{/* Carta nit */}}
          {{ $divendres := index $horaris "divendres" }}
          {{ if gt (len $divendres) 1 }}
          <div class="horari-item">
            <div class="horari-dia">
              <strong>{{ i18n "divendres" }}, {{ i18n "dissabte" }}</strong>
            </div>
            <div class="horari-hores">
              {{ (index $divendres 1).inici }} - {{ (index $divendres 1).fi }}
            </div>
            <div class="horari-servei">{{ i18n "servei_carta" }}</div>
          </div>
          {{ end }}
          
          {{/* Dies tancats */}}
          <div class="horari-item horari-tancat">
            <div class="horari-dia">
              <strong>{{ i18n "dimecres" }}, {{ i18n "diumenge" }}</strong>
            </div>
            <div class="horari-hores">{{ i18n "estat_tancat" }}</div>
          </div>
        </div>
      </div>

      {{/* Bloc dreta: Contacte ràpid */}}
      <div class="contacte-bloc">
        <h3>{{ i18n "contacte" }}</h3>
        
        {{ $restaurant := .Site.Data.restaurant }}
        
        <div class="contacte-llista">
          <div class="contacte-item">
            <span class="contacte-icona">📍</span>
            <div class="contacte-info">
              <strong>{{ i18n "on_som" }}</strong>
              <p>{{ index $restaurant.adreca.complet $lang }}</p>
            </div>
          </div>
          
          <div class="contacte-item">
            <span class="contacte-icona">📞</span>
            <div class="contacte-info">
              <strong>{{ i18n "telefon" }}</strong>
              <p>
                <a href="tel:{{ $restaurant.telefon }}">{{ $restaurant.telefon }}</a>
              </p>
            </div>
          </div>
          
          <div class="contacte-item">
            <span class="contacte-icona">✉️</span>
            <div class="contacte-info">
              <strong>Email</strong>
              <p>
                <a href="mailto:{{ $restaurant.email }}">{{ $restaurant.email }}</a>
              </p>
            </div>
          </div>
        </div>

        <div class="contacte-cta">
          <a href="{{ .Site.BaseURL }}{{ .Site.Language.Lang }}/reserves/" class="btn btn-primary btn-block">
            {{ i18n "fer_reserva" }}
          </a>
        </div>
      </div>
    </div>
  </div>
</section>

<style>
/* Hero Section */
.hero {
  position: relative;
  min-height: 70vh;
  display: flex;
  align-items: center;
  justify-content: center;
  overflow: hidden;
  background: linear-gradient(135deg, #1a1a1a 0%, #2d2d2d 100%);
}

.hero-bg {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  opacity: 0.1;
  z-index: 1;
}

.hero-bg img {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.hero-content {
  position: relative;
  z-index: 2;
  text-align: center;
  padding: var(--spacing-xl) var(--spacing-md);
  max-width: 900px;
  margin: 0 auto;
}

.hero-logo {
  margin-bottom: var(--spacing-lg);
}

.hero-logo img {
  max-width: 300px;
  height: auto;
  filter: brightness(0) invert(1);
}

.hero-slogan {
  color: white;
  font-size: 2.5rem;
  font-weight: 300;
  letter-spacing: 0.05em;
  margin-bottom: var(--spacing-lg);
  line-height: 1.3;
  text-transform: none;
}

.hero-estat {
  margin-bottom: var(--spacing-xl);
}

.hero-estat .estat-restaurant-container {
  padding: 0;
}

.hero-ctas {
  display: flex;
  gap: var(--spacing-md);
  justify-content: center;
  flex-wrap: wrap;
}

.btn-large {
  padding: 1rem 2.5rem;
  font-size: 1.125rem;
}

.btn-outline {
  background: transparent;
  border: 2px solid white;
  color: white;
}

.btn-outline:hover {
  background: white;
  color: var(--color-black);
}

/* Sections */
.home-section {
  padding: var(--spacing-xl) 0;
}

.destacats-section {
  background: white;
}

.horaris-section {
  background: var(--color-gray-light);
}

.section-header {
  text-align: center;
  margin-bottom: var(--spacing-xl);
}

.section-header h2 {
  font-size: 2.5rem;
  margin-bottom: var(--spacing-sm);
}

.section-intro {
  font-size: 1.125rem;
  color: var(--color-gray-dark);
}

.section-cta {
  text-align: center;
  margin-top: var(--spacing-xl);
}

/* Horaris i Contacte */
.horaris-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(350px, 1fr));
  gap: var(--spacing-xl);
  max-width: 1200px;
  margin: 0 auto;
}

.horaris-bloc,
.contacte-bloc {
  background: white;
  padding: var(--spacing-xl);
  border-radius: 12px;
  box-shadow: var(--shadow-sm);
}

.horaris-bloc h3,
.contacte-bloc h3 {
  font-size: 1.75rem;
  margin-bottom: var(--spacing-lg);
  color: var(--color-black);
}

.horaris-llista,
.contacte-llista {
  display: flex;
  flex-direction: column;
  gap: var(--spacing-md);
}

.horari-item {
  padding: var(--spacing-md);
  border-left: 3px solid var(--color-accent);
  background: var(--color-gray-light);
  border-radius: 0 6px 6px 0;
}

.horari-item.horari-tancat {
  border-left-color: var(--color-gray-mid);
  opacity: 0.7;
}

.horari-dia {
  font-size: 1rem;
  margin-bottom: 0.25rem;
}

.horari-hores {
  font-size: 1.25rem;
  font-weight: 600;
  color: var(--color-accent);
  margin-bottom: 0.25rem;
}

.horari-servei {
  font-size: 0.9rem;
  color: var(--color-gray-dark);
  text-transform: uppercase;
  letter-spacing: 0.05em;
}

.contacte-item {
  display: flex;
  gap: var(--spacing-md);
  align-items: flex-start;
}

.contacte-icona {
  font-size: 2rem;
  flex-shrink: 0;
}

.contacte-info strong {
  display: block;
  margin-bottom: 0.25rem;
  font-size: 0.9rem;
  text-transform: uppercase;
  letter-spacing: 0.05em;
  color: var(--color-gray-dark);
}

.contacte-info p {
  margin: 0;
  font-size: 1rem;
}

.contacte-info a {
  color: var(--color-black);
  font-weight: 500;
}

.contacte-info a:hover {
  color: var(--color-accent);
}

.contacte-cta {
  margin-top: var(--spacing-lg);
}

.btn-block {
  display: block;
  width: 100%;
}

/* Responsive */
@media (max-width: 768px) {
  .hero {
    min-height: 60vh;
  }
  
  .hero-slogan {
    font-size: 1.75rem;
  }
  
  .hero-logo img {
    max-width: 200px;
  }
  
  .hero-ctas {
    flex-direction: column;
  }
  
  .btn-large {
    width: 100%;
  }
  
  .horaris-grid {
    grid-template-columns: 1fr;
  }
}
</style>
