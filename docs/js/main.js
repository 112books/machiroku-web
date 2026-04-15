document.addEventListener('DOMContentLoaded', function() {
  const navToggle = document.querySelector('.nav-toggle');
  const headerNav = document.querySelector('.header-nav');

if (navToggle && headerNav) {
  navToggle.addEventListener('click', function() {
    const expanded = navToggle.getAttribute('aria-expanded') === 'true';
    headerNav.classList.toggle('active');
    navToggle.classList.toggle('active');
    navToggle.setAttribute('aria-expanded', expanded ? 'false' : 'true');
    navToggle.setAttribute('aria-label', expanded ? 'Obrir menú de navegació' : 'Tancar menú de navegació');
  });
}
  
  const statusEl = document.getElementById('restaurant-status');
  if (statusEl) {
    const now = new Date();
    const day = now.getDay();
    const hour = now.getHours();
    const lang = document.documentElement.lang || 'ca';
    
    const labels = {
      ca: {
        open: 'OBERT',
        closed: 'TANCAT',
        lunch: 'Menú',
        dinner: 'Carta',
        nextOpen: 'Obirim',
        at: 'a les',
        days: ['diumenge', 'dilluns', 'dimarts', 'dimecres', 'dijous', 'divendres', 'dissabte']
      },
      es: {
        open: 'ABIERTO',
        closed: 'CERRADO',
        lunch: 'Menú',
        dinner: 'Carta',
        nextOpen: 'Abrimos',
        at: 'a las',
        days: ['domingo', 'lunes', 'martes', 'miércoles', 'jueves', 'viernes', 'sábado']
      },
      en: {
        open: 'OPEN',
        closed: 'CLOSED',
        lunch: 'Menu',
        dinner: 'Dinner',
        nextOpen: 'We open',
        at: 'at',
        days: ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday']
      }
    };
    
    const t = labels[lang] || labels.ca;
    let status = '';
    let nextService = '';
    
    if (day === 0 || day === 1 || day === 2) {
      status = 'closed';
      nextService = t.days[3] + ' ' + t.lunch.toLowerCase();
    } else if (day === 3 || day === 4 || day === 5 || day === 6) {
      if (hour >= 13 && hour < 15.5) {
        status = 'open-lunch';
      } else if (hour >= 20 && hour < 23) {
        status = 'open-dinner';
      } else if (hour < 13) {
        status = 'closed';
        nextService = t.lunch;
      } else {
        status = 'closed';
        if (day === 6) {
          nextService = t.days[3] + ' ' + t.lunch.toLowerCase();
        } else {
          nextService = day === 3 ? t.lunch : 'dissabte ' + t.lunch.toLowerCase();
        }
      }
    }
    
    if (status === 'open-lunch') {
      statusEl.innerHTML = `<span class="status status--open">${t.open}: ${t.lunch}</span>`;
    } else if (status === 'open-dinner') {
      statusEl.innerHTML = `<span class="status status--open">${t.open}: ${t.dinner}</span>`;
    } else {
      statusEl.innerHTML = `<span class="status status--closed">${t.closed}</span>`;
    }
  }
  
  document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function(e) {
      const href = this.getAttribute('href');
      if (href !== '#') {
        e.preventDefault();
        const target = document.querySelector(href);
        if (target) {
          target.scrollIntoView({ behavior: 'smooth' });
        }
      }
    });
  });
});
