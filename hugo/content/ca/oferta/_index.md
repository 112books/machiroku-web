---
title: "Oferta gastronòmica"
---

{{ define "main" }}
<section class="page-header">
  <h1>{{ i18n "oferta" }}</h1>
</section>

<section class="offer-section">
  <h2>{{ i18n "menu_migdia" }}</h2>
  <p class="offer-desc">De dilluns a divendres</p>
  
  <div class="menu-list">
    {{ range where site.RegularPages "Type" "menus" }}
      <article class="menu-item">
        <div class="menu-header">
          <h3>{{ .Title }}</h3>
          {{ with .Params.price }}<span class="price">{{ . }}</span>{{ end }}
        </div>
        {{ with .Params.description }}<p class="menu-desc">{{ . }}</p>{{ end }}
        {{ .Content }}
      </article>
    {{ end }}
  </div>
</section>

<section class="offer-section">
  <h2>{{ i18n "carta_nit" }}</h2>
  <p class="offer-desc">Divendres i dissabte</p>
  
  <div class="menu-list">
    {{ range where site.RegularPages "Type" "carta" }}
      <article class="menu-item">
        <div class="menu-header">
          <h3>{{ .Title }}</h3>
          {{ with .Params.price }}<span class="price">{{ . }}</span>{{ end }}
        </div>
        {{ with .Params.description }}<p class="menu-desc">{{ . }}</p>{{ end }}
        {{ .Content }}
      </article>
    {{ end }}
  </div>
</section>
{{ end }}
