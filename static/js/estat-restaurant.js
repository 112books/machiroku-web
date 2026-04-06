// estat-restaurant.js
// Sistema per calcular si el restaurant està obert/tancat i mostrar proper servei

class EstatRestaurant {
  constructor() {
    this.horaris = null;
    this.excepcions = null;
    this.init();
  }

  async init() {
    // Carregar dades dels fitxers YAML (convertits a JSON per Hugo)
    try {
      await this.carregarDades();
      this.actualitzarEstat();
      // Actualitzar cada minut
      setInterval(() => this.actualitzarEstat(), 60000);
    } catch (error) {
      console.error('Error inicialitzant estat restaurant:', error);
    }
  }

  async carregarDades() {
    // Les dades vindran de variables globals injectades per Hugo
    this.horaris = window.horarisData || {};
    this.excepcions = window.excepcionsData || [];
  }

  getDiaSetmana() {
    const dies = ['diumenge', 'dilluns', 'dimarts', 'dimecres', 'dijous', 'divendres', 'dissabte'];
    return dies[new Date().getDay()];
  }

  getDataActual() {
    const avui = new Date();
    return avui.toISOString().split('T')[0]; // Format: YYYY-MM-DD
  }

  getHoraActual() {
    const ara = new Date();
    return ara.getHours() * 60 + ara.getMinutes(); // Minuts des de mitjanit
  }

  parseHora(horaString) {
    const [hores, minuts] = horaString.split(':').map(Number);
    return hores * 60 + minuts;
  }

  comprovarExcepcio() {
    const dataAvui = this.getDataActual();
    const excepcio = this.excepcions.find(e => e.data === dataAvui && e.actiu);
    
    if (excepcio) {
      if (excepcio.estat === 'tancat') {
        return {
          estat: 'tancat',
          excepcio: true,
          missatge: excepcio.missatge
        };
      }
      
      if (excepcio.estat === 'obert' && excepcio.horari) {
        return {
          estat: 'excepcio',
          servei: excepcio.servei,
          horari: excepcio.horari
        };
      }
    }
    
    return null;
  }

  calcularEstat() {
    // 1. Comprovar excepcions primer
    const excepcio = this.comprovarExcepcio();
    if (excepcio && excepcio.estat === 'tancat') {
      return {
        obert: false,
        servei: null,
        missatge: excepcio.missatge,
        properServei: this.trobarProperServei()
      };
    }

    // 2. Horari base
    const dia = this.getDiaSetmana();
    const horaActual = this.getHoraActual();
    
    let horarisDia = this.horaris && this.horaris.base && this.horaris.base[dia] || [];
    
    // Si hi ha excepció amb horari especial, usar-lo
    if (excepcio && excepcio.estat === 'excepcio') {
      horarisDia = [{
        inici: excepcio.horari.inici,
        fi: excepcio.horari.fi,
        servei: excepcio.servei
      }];
    }

    // Comprovar si estem dins algun horari
    for (const franja of horarisDia) {
      const inici = this.parseHora(franja.inici);
      const fi = this.parseHora(franja.fi);
      
      if (horaActual >= inici && horaActual < fi) {
        return {
          obert: true,
          servei: franja.servei,
          tancaA: franja.fi,
          missatge: null
        };
      }
    }

    // Tancat - buscar proper servei
    return {
      obert: false,
      servei: null,
      missatge: null,
      properServei: this.trobarProperServei()
    };
  }

  trobarProperServei() {
    const diaActual = this.getDiaSetmana();
    const horaActual = this.getHoraActual();
    const dies = ['dilluns', 'dimarts', 'dimecres', 'dijous', 'divendres', 'dissabte', 'diumenge'];
    
    // Buscar avui
    const horarisDiaActual = this.horaris && this.horaris.base && this.horaris.base[diaActual] || [];
    for (const franja of horarisDiaActual) {
      const inici = this.parseHora(franja.inici);
      if (inici > horaActual) {
        return {
          dia: 'avui',
          hora: franja.inici,
          servei: franja.servei
        };
      }
    }

    // Buscar propers dies (màxim 7 dies)
    const indexDiaActual = dies.indexOf(diaActual);
    for (let i = 1; i <= 7; i++) {
      const indexDia = (indexDiaActual + i) % 7;
      const nomDia = dies[indexDia];
      const horarisDia = this.horaris && this.horaris.base && this.horaris.base[nomDia] || [];
      
      if (horarisDia.length > 0) {
        return {
          dia: nomDia,
          hora: horarisDia[0].inici,
          servei: horarisDia[0].servei
        };
      }
    }

    return null;
  }

  actualitzarEstat() {
    const estat = this.calcularEstat();
    this.mostrarEstat(estat);
  }

  mostrarEstat(estat) {
  const container = document.getElementById('estat-restaurant');
  if (!container) return;

  const t = window.i18nEstat || {
    estat_obert:  'Obert',
    estat_tancat: 'Tancat',
    servei_menu:  'Menú del migdia',
    servei_carta: 'Carta de nit',
    msg_obrim_a:  'Obrim a les',
    msg_tornem:   'Tornem',
    horari_fins:  'Fins les',
    avui:         'avui'
  };

  let html = '';

  if (estat.obert) {
    const serveiNom = estat.servei === 'menu' ? t.servei_menu : t.servei_carta;
    html = `
      <div class="estat estat-obert">
        <span class="estat-badge obert">${t.estat_obert}</span>
        <span class="estat-servei">${serveiNom}</span>
        <span class="estat-horari">${t.horari_fins} ${estat.tancaA}</span>
      </div>
    `;
  } else {
    html = `
      <div class="estat estat-tancat">
        <span class="estat-badge tancat">${t.estat_tancat}</span>
    `;

    if (estat.properServei) {
      const serveiNom = estat.properServei.servei === 'menu' ? t.servei_menu : t.servei_carta;
      const diaText = estat.properServei.dia === 'avui'
        ? `${t.msg_obrim_a} ${estat.properServei.hora}`
        : `${t.msg_tornem} ${estat.properServei.dia} ${estat.properServei.hora}`;

      html += `<span class="estat-proper">${diaText} · ${serveiNom}</span>`;
    }

    html += `</div>`;
  }

  container.innerHTML = html;
}

}

// Inicialitzar quan el DOM estigui carregat
if (document.readyState === 'loading') {
  document.addEventListener('DOMContentLoaded', () => {
    new EstatRestaurant();
  });
} else {
  new EstatRestaurant();
}
