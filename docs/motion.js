/* Decorative artwork controls. No network calls, timers or stored preferences. */
(() => {
  'use strict';
  const visual = document.querySelector('.hero-visual');
  const toggle = document.getElementById('motion-toggle');
  if (!visual || !toggle) return;
  const reduced = matchMedia('(prefers-reduced-motion: reduce)');
  let userPaused = false;
  let visible = true;

  function update() {
    const paused = userPaused || reduced.matches || document.hidden || !visible;
    visual.classList.toggle('motion-paused', paused);
    toggle.disabled = reduced.matches;
    toggle.setAttribute('aria-pressed', String(userPaused || reduced.matches));
    toggle.textContent = reduced.matches ? 'Motion reduced' : userPaused ? 'Play animation' : 'Pause animation';
  }
  toggle.hidden = false;
  toggle.addEventListener('click', () => { userPaused = !userPaused; update(); });
  reduced.addEventListener('change', update);
  document.addEventListener('visibilitychange', update);
  if ('IntersectionObserver' in window) {
    new IntersectionObserver(entries => {
      visible = entries[0].isIntersecting;
      update();
    }, {threshold: 0}).observe(visual);
  }
  update();
})();
