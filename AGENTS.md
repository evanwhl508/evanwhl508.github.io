# Covan Labs website

- The owner's canonical visual source is `docs/design-system.md`. It governs theme 2 and the default site. Document any deviation and its reason in `docs/design-decisions.md` before implementing it.
- Preserve theme 1's existing design, snapshots in `site/theme1/`, CSS in `assets/site.css`, and original brand assets. New styling belongs to `assets/theme2.css` and new branding to `logo/`.
- Theme selection is exclusively by path: `/` defaults to theme 2; `/theme1/` and `/theme2/` are explicit alternatives. The local server port is arbitrary. Keep studio navigation inside the chosen prefix.
- Edit `site/theme2/home.html`, `site/pages/`, and `scripts/build-site.py` for content/shell changes. Run `python3 scripts/build-site.py` to regenerate all route variants, then `python3 scripts/check-site.py`.
- Use the centralized design tokens and existing component classes. Keep product icons and independent product domains intact.
- Verify responsive layout, keyboard navigation, reduced motion and contrast for meaningful UI changes. Keep browser QA output under `output/playwright/`.
- The repo contains static GitHub Pages output; no production DNS, mail routing or account verification changes are implied by editing it.
