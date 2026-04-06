---
title: "Home"
description: "Authentic Japanese restaurant in the heart of Barcelona. Lunch menu and evening à la carte with seasonal products."
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
      <p class="section-intro">Selection of our most popular dishes</p>
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
        Full {{ i18n "veure_carta" }}
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
