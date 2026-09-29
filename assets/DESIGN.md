# Visual system

**Concept: a research observatory, not a disaster-alert dashboard.**

Ink (`#08151b`), pale paper (`#edf5ed`), radar mint (`#70dec5`), signal lime (`#c6f78e`) and muted amber (`#edc186`). Editorial typography, thin radar rings, compact technical labels and generous whitespace. No fake live indicators, weather tracks, benchmark scores or star counts.

`banner.svg`, `docs/storm.svg` and the favicon are original programmatic vector artwork. The funnel consists of tapered elliptical streamlines, not a measured field or simulation. No third-party photography, assets, font files, analytics or hotlinked images are required. Brand artwork uses the code license; paper copyrights remain with their owners.

Both SVG artworks contain decorative rotating flow segments, slow funnel sway and drifting dust. Their base paths remain visible when animation is unsupported. The site inlines the canonical `docs/storm.svg` through `templates/index.html`; regenerate with `tools/build.py` after artwork changes. `motion.js` supplies a pause/play control and pauses the artwork when the document is hidden or the illustration leaves the viewport. All motion respects `prefers-reduced-motion`. The SVG banner can animate in image contexts that allow embedded CSS; GitHub/image proxies may render a static fallback. Do not apply EF-scale colors to evidence quality or reading difficulty.
