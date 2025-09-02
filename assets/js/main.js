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

  // Reveal on scroll
  const revealEls = Array.from(document.querySelectorAll('.reveal'));
  const onScroll = () => {
    const trigger = window.innerHeight * 0.9;
    revealEls.forEach(el => {
      const rect = el.getBoundingClientRect();
      if (rect.top < trigger) el.classList.add('visible');
    });
  };
  window.addEventListener('scroll', onScroll, { passive: true });
  onScroll();
});


