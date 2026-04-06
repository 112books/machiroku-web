---
title: "Oferta gastronòmica"
description: "Menús del migdia i carta nocturna del restaurant Machiroku"
---

{{/* Secció de menús del migdia */}}
<section class="oferta-section menus-section">
  <div class="container">
    <div class="section-header">
      <h2>{{ i18n "servei_menu" }}</h2>
      <p class="section-intro">De dilluns a divendres de 13:00 a 15:30h</p>
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
      <p class="section-intro">Divendres i dissabte de 19:00 a 22:00h</p>
      
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

<style>
.container {
  max-width: 1400px;
  margin: 0 auto;
  padding: 0 var(--spacing-md);
}

.oferta-section {
  padding: var(--spacing-xl) 0;
}

.carta-section {
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
  margin-bottom: var(--spacing-md);
}

.cta-reserves {
  margin-top: var(--spacing-lg);
}

.categoria-section {
  margin-bottom: var(--spacing-xl);
}

.categoria-nom {
  font-size: 2rem;
  margin-bottom: var(--spacing-lg);
  padding-bottom: var(--spacing-sm);
  border-bottom: 2px solid var(--color-accent);
  display: inline-block;
}

.alergics-info {
  margin-top: var(--spacing-xl);
  padding: var(--spacing-lg);
  background: white;
  border-radius: 8px;
  text-align: center;
}

.alergics-info h4 {
  font-size: 1.5rem;
  margin-bottom: var(--spacing-sm);
}

.alergics-llegenda {
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  gap: var(--spacing-md);
  margin-top: var(--spacing-md);
}

.alergic-item {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  padding: 0.5rem 1rem;
  background: var(--color-gray-light);
  border-radius: 6px;
  font-size: 0.9rem;
}

.alergic-item .icona {
  font-size: 1.25rem;
}

@media (max-width: 768px) {
  .section-header h2 {
    font-size: 2rem;
  }
  
  .categoria-nom {
    font-size: 1.5rem;
  }
}
</style>