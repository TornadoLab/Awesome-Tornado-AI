# Visual system

**Concept: a research observatory, not a disaster-alert dashboard.**

Ink (`#08151b`), pale paper (`#edf5ed`), radar mint (`#70dec5`), signal lime (`#c6f78e`) and muted amber (`#edc186`). Editorial typography, thin radar rings, compact technical labels and generous whitespace. No fake live indicators, weather tracks, benchmark scores or star counts.

`banner.svg`, `docs/storm.svg` and the favicon are original programmatic vector artwork. The funnel consists of tapered elliptical streamlines, not a measured field or simulation. No third-party photography, assets, font files, analytics or hotlinked images are required. Brand artwork uses the code license; paper copyrights remain with their owners.

Both SVG artworks contain decorative rotating flow segments, slow funnel sway and drifting dust. Their base paths remain visible when animation is unsupported. The site inlines the canonical `docs/storm.svg` through `templates/index.html`; regenerate with `tools/build.py` after artwork changes. `motion.js` supplies a pause/play control and pauses the artwork when the document is hidden or the illustration leaves the viewport. The inherited `--motion-state` controls the SVG and radar together. Reduced-motion visitors start with paused artwork and can explicitly choose **Play tornado**; the control must remain enabled. Changing the system preference resets that temporary choice. Without JavaScript, the SVG's CSS still respects reduced motion. The SVG banner can animate in image contexts that allow embedded CSS; GitHub/image proxies may render a static fallback. Do not apply EF-scale colors to evidence quality or reading difficulty.

The interface uses a shared `rem` type scale in `docs/style.css`: 13–14 px metadata, 16 px summaries and controls, 18–20 px introductory prose and 22 px paper titles at the browser's default font size. Narrow screens reflow controls and cards instead of shrinking reading text. The optional browser checks compare actual tornado pixels with the radar hidden, verify pause/play with reduced motion, and check reading sizes and overflow from 320 to 1440 px.
