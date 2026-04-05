document.addEventListener('DOMContentLoaded', function() {
  const navToggle = document.querySelector('.nav-toggle');
  const navLinks = document.querySelector('.nav-links');
  
  if (navToggle && navLinks) {
    navToggle.addEventListener('click', function() {
      navLinks.classList.toggle('active');
      navToggle.classList.toggle('active');
      navToggle.setAttribute('aria-expanded', 
        navToggle.getAttribute('aria-expanded') === 'true' ? 'false' : 'true'
      );
    });
  }
  
  // Restaurant status
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
        at: 'a les'
      },
      es: {
        open: 'ABIERTO',
        closed: 'CERRADO',
        lunch: 'Menú',
        dinner: 'Carta',
        nextOpen: 'Abrimos',
        at: 'a las'
      },
      en: {
        open: 'OPEN',
        closed: 'CLOSED',
        lunch: 'Menu',
        dinner: 'Dinner',
        nextOpen: 'We open',
        at: 'at'
      }
    };
    
    const t = labels[lang] || labels.ca;
    let status = '';
    let nextDay = '';
    
    // Day 0 = Sunday, 1 = Monday, etc.
    if (day === 0) {
      status = 'closed';
      nextDay = lang === 'ca' ? 'dimecres' : lang === 'es' ? 'miércoles' : 'wednesday';
    } else if (day === 1 || day === 2) {
      status = 'closed';
      nextDay = lang === 'ca' ? 'dimecres' : lang === 'es' ? 'miércoles' : 'wednesday';
    } else if (day === 3) { // Wednesday
      if (hour >= 13 && hour < 15.5) {
        status = 'open-lunch';
      } else if (hour >= 20 && hour < 23) {
        status = 'open-dinner';
      } else if (hour < 13) {
        status = 'closed';
        nextDay = lang === 'ca' ? 'avui a les 13h' : lang === 'es' ? 'hoy a las 13h' : 'today at 1pm';
      } else {
        status = 'closed';
        nextDay = lang === 'ca' ? 'dissabte' : lang === 'es' ? 'sábado' : 'saturday';
      }
    } else if (day === 4 || day === 5) { // Thursday, Friday
      if (hour >= 13 && hour < 15.5) {
        status = 'open-lunch';
      } else if (hour >= 20 && hour < 23) {
        status = 'open-dinner';
      } else if (hour < 13) {
        status = 'closed';
        nextDay = lang === 'ca' ? 'avui a les 13h' : lang === 'es' ? 'hoy a las 13h' : 'today at 1pm';
      } else {
        status = 'closed';
        nextDay = lang === 'ca' ? 'dissabte' : lang === 'es' ? 'sábado' : 'saturday';
      }
    } else if (day === 6) { // Saturday
      if (hour >= 13 && hour < 15.5) {
        status = 'open-lunch';
      } else if (hour >= 20 && hour < 23) {
        status = 'open-dinner';
      } else if (hour < 13) {
        status = 'closed';
        nextDay = lang === 'ca' ? 'avui a les 13h' : lang === 'es' ? 'hoy a las 13h' : 'today at 1pm';
      } else {
        status = 'closed';
        nextDay = lang === 'ca' ? 'dimecres' : lang === 'es' ? 'miércoles' : 'wednesday';
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
  
  // Smooth scroll
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
