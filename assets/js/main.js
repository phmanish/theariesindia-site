document.addEventListener('DOMContentLoaded', () => {
  const navToggle = document.querySelector('.nav-toggle');
  const navMenu = document.getElementById('nav-menu');
  if (navToggle && navMenu) {
    navToggle.addEventListener('click', () => {
      const expanded = navToggle.getAttribute('aria-expanded') === 'true' || false;
      navToggle.setAttribute('aria-expanded', String(!expanded));
      navMenu.classList.toggle('open');
    });
  }

  const yearSpan = document.getElementById('year');
  if (yearSpan) yearSpan.textContent = String(new Date().getFullYear());
});


