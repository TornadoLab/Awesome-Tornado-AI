/* Decorative artwork controls. No network calls, timers or stored preferences. */
(() => {
  'use strict';
  const visual = document.querySelector('.hero-visual');
  const toggle = document.getElementById('motion-toggle');
  if (!visual || !toggle) return;
  const reduced = matchMedia('(prefers-reduced-motion: reduce)');
  // null follows the system; an explicit Play is allowed even in reduced-motion mode.
  let userPaused = null;
  let visible = true;

  function update() {
    const requestedPause = userPaused ?? reduced.matches;
    const paused = requestedPause || document.hidden || !visible;
    // One inherited state controls both the inline SVG and the radar sweep.
    visual.style.setProperty('--motion-state', paused ? 'paused' : 'running');
    visual.classList.toggle('motion-paused', paused);
    toggle.setAttribute('aria-pressed', String(requestedPause));
    toggle.textContent = requestedPause ? '▶ Play tornado' : 'Ⅱ Pause tornado';
  }
  toggle.hidden = false;
  toggle.addEventListener('click', () => {
    userPaused = !(userPaused ?? reduced.matches);
    update();
  });
  // A new system preference takes effect immediately; Play can override it again.
  reduced.addEventListener('change', () => { userPaused = null; update(); });
  document.addEventListener('visibilitychange', update);
  if ('IntersectionObserver' in window) {
    new IntersectionObserver(entries => {
      visible = entries[0].isIntersecting;
      update();
    }, {threshold: 0}).observe(visual);
  }
  update();
})();
