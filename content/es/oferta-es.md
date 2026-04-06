---
title: "Oferta gastronómica"
description: "Menús del mediodía y carta nocturna del restaurante Machiroku"
---

{{/* Secció de menús del migdia */}}
<section class="oferta-section menus-section">
  <div class="container">
    <div class="section-header">
      <h2>{{ i18n "servei_menu" }}</h2>
      <p class="section-intro">De lunes a viernes de 13:00 a 15:30h</p>
    </div>

    {{/* Grid de menús */}}
    <div class="menus-grid">
      {{ $lang := .Site.Language.Lang }}
      {{ $menusData := index .Site.Data $lang "menus" }}
      {{ $menus := $menusData.menus }}
      
      {{ range sort $menus "ordre" }}
        {{ if .actiu }}
          {{ partial "menu-card.html" . }}
        {{ end }}
      {{ end }}
    </div>
  </div>
</section>

{{/* Secció de carta nocturna */}}
<section class="oferta-section carta-section">
  <div class="container">
    <div class="section-header">
      <h2>{{ i18n "servei_carta" }}</h2>
      <p class="section-intro">Viernes y sábado de 19:00 a 22:00h</p>
      
      <div class="cta-reserves">
        <a href="{{ .Site.BaseURL }}{{ .Site.Language.Lang }}/reserves/" class="btn btn-primary">
          {{ i18n "fer_reserva" }}
        </a>
      </div>
    </div>

    {{/* Mostrar plats per categoria */}}
    {{ $lang := .Site.Language.Lang }}
    {{ $platsData := index .Site.Data $lang "plats" }}
    {{ $categories := $platsData.categories }}
    {{ $plats := $platsData.plats }}

    {{ range sort $categories "ordre" }}
      {{ $categoriaId := .id }}
      {{ $categoriaNom := .nom }}
      
      {{/* Filtrar plats d'aquesta categoria */}}
      {{ $platsCategoria := where $plats "categoria" $categoriaId }}
      {{ $platsActius := where $platsCategoria "actiu" true }}
      
      {{ if $platsActius }}
      <div class="categoria-section">
        <h3 class="categoria-nom">{{ $categoriaNom }}</h3>
        
        <div class="plats-grid">
          {{ range sort $platsActius "ordre" }}
            {{ partial "plat-card.html" . }}
          {{ end }}
        </div>
      </div>
      {{ end }}
    {{ end }}

    {{/* Informació d'al·lèrgens */}}
    <div class="alergics-info">
      <h4>{{ i18n "info_alergics" }}</h4>
      <p>{{ i18n "consultar_alergics" }}</p>
      
      {{/* Llegenda d'al·lèrgens */}}
      <div class="alergics-llegenda">
        {{ $alergicsData := index .Site.Data $lang "alergics" }}
        {{ range $alergicsData.alergics }}
        <span class="alergic-item">
          <span class="icona">{{ .icona }}</span>
          <span class="nom">{{ index .nom $lang }}</span>
        </span>
        {{ end }}
      </div>
    </div>
  </div>
</section>
