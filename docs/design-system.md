# Covan Labs — Visual Design System

Canonical design source supplied by the owner on 20 October 2026. This document governs **theme 2** and the default website. Theme 1 deliberately preserves the previous design. Record any deviation, its reason and scope in [design-decisions.md](design-decisions.md).

## 1. Brand overview

- Brand: **Covan Labs**; Chinese name: **高凡**.
- Independent software product studio / developer lab. Parent brand and developer website for apps, developer tools, SaaS, AI products, utilities, experiments and future software projects.
- Technical, calm, precise, modern, premium, independent, trustworthy, product-focused, experimental without chaos, developer-oriented without hacker stereotypes.
- Positioning: “A small but highly capable software lab building useful digital products.” A company capable of building reliable products for many years.
- Avoid the appearance of an AI consultancy, agency, Web3/crypto startup, gaming studio, enterprise consultancy, cybersecurity hacker brand, generic SaaS landing page or neon sci-fi company.

## 2. Core visual direction

**Deep Navy + Cool Silver + Aqua**. Approximately 75% dark navy / neutral surfaces, 20% white / silver typography, 5% aqua accent. Aqua must never dominate the interface.

## 3. Color system

| Role | Value |
| --- | --- |
| Primary background | `#08111F` |
| Secondary background / alternate sections | `#101C2C` |
| Tertiary background / elevated surface | `#172436` |
| Primary text | `#F4F7FA` |
| Secondary text | `#9EADBD` |
| Muted text | `#6F8092` |
| Disabled text | `#516172` |
| Primary accent | `#39C6C8` |
| Accent hover | `#70E1E3` |
| Accent dark | `#15999C` |
| Accent soft | `rgba(57,198,200,0.12)` |
| Subtle border | `#1B2B3D` |
| Default border | `#27394D` |
| Strong border | `#385168` |
| Success | `#56C596` |
| Warning | `#E6B85C` |
| Error | `#E76F73` |
| Info | `#5BA9E6` |

Avoid pure black backgrounds and pure white body text. Backgrounds retain a blue undertone. Use aqua for primary CTAs, links, active navigation, small logo accents, important metrics, selected states, focus rings and tiny highlights; never large surfaces. Semantic colors are muted functional signals, never brand colors. Prefer subtle borders over heavy shadows.

## 4. Light mode

Dark is canonical; light is optional and secondary.

| Role | Value |
| --- | --- |
| Background | `#F6F8FB` |
| Secondary background | `#EDF2F6` |
| Surface | `#FFFFFF` |
| Primary text | `#101A26` |
| Secondary text | `#647485` |
| Muted text | `#82909E` |
| Border | `#DCE4EC` |
| Accent | `#15999C` |
| Accent hover | `#117E81` |

## 5. Typography

Primary font: **Inter**. Fallback: `Inter, ui-sans-serif, system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif`. Neutral, technical and readable without overpowering product brands. Optional **Manrope** for very large hero headings only. Maximum two font families. No futuristic sci-fi fonts.

## 6. Typography scale

| Desktop style | Size / line height / weight |
| --- | --- |
| Display XL | 72px / 76px / 600 |
| Display L | 56px / 62px / 600 |
| H1 | 44px / 52px / 600 |
| H2 | 36px / 44px / 600 |
| H3 | 28px / 36px / 600 |
| H4 | 22px / 30px / 600 |
| Body large | 18px / 30px / 400 |
| Body | 16px / 26px / 400 |
| Body small | 14px / 22px / 400 |
| Caption | 12px / 18px / 500 |

Mobile: hero 42px / 48px; H1 36px / 42px; H2 30px / 38px; H3 24px / 32px; body 16px / 25px. Avoid oversized SaaS typography occupying the whole screen.

## 7. Spacing

8px base system with 4px half-step. Values: 4, 8, 12, 16, 24, 32, 48, 64, 80, 96, 128px. Section spacing: desktop 96–128px; tablet 72–96px; mobile 56–72px. Maximum page width 1200px; text-heavy blocks 720px.

## 8. Border radius

Controls 6px; buttons 8px; cards 12px; large panels 16px. No bubbly 24px+ aesthetics. Pills only for tags, status labels and small filters.

## 9. Shadows

Rely on borders and surface contrast. Optional shadow: `0 8px 32px rgba(0,0,0,0.20)`. Rare accent glow: `0 0 40px rgba(57,198,200,0.10)`. No exaggerated floating shadows or large neon glow.

## 10. Layout

Spacious, structured, calm and intentional. Strong grid, breathing room, thoughtful asymmetry, real product screenshots, minimal decoration. No floating clutter, excessive gradients, busy graphics, random glassmorphism, blobs or large gradient orbs.

## 11. Navigation

Left: Covan Labs logo. Right: Products, About, Updates, Contact; optionally GitHub. CTA only if meaningful, e.g. Explore Products. Transparent or minimally elevated. Optional scrolled background `rgba(8,17,31,0.86)` and `backdrop-filter: blur(16px)`; use blur sparingly.

## 12. Hero

Recommended: “Building useful software, one product at a time.” Supporting copy: “Independent software lab creating apps, developer tools, AI products and experiments.” CTAs: Explore Products; About Covan Labs.

Alternatives: “Software products built with care.” / “Tools, apps and experiments from Covan Labs.” Avoid “Revolutionizing”, “Next-generation”, “Disrupting”, “AI-powered everything”, “Building the future”, “Web3 revolution”.

## 13. Hero visual style

Background `#08111F`. Optional faint technical grids, subtle geometric construction lines, tiny nodes, thin paths, modular geometry, minimal aqua glow, slow gradient noise. Opacity generally below 10%. No AI brains, robot heads, blockchain hexagons, crypto coins, code rain, Matrix text, glass spheres, giant neon gradients or purple AI backgrounds.

## 14. Product cards

Products are independent identities; Covan Labs is their parent. Structure: app icon, product name, short useful description, category/platform, Learn More link. Example: JWT Loupe — selection-first JWT inspector with local JWKS validation — Developer Tool.

Background `#101C2C`; border `1px solid #27394D`; radius 12px. Hover slightly brightens border and lifts at most 2–3px. No exaggerated animation.

## 15. Product colors

Keep the parent brand neutral. Product accents may vary: developer tool blue/cyan; AI teal/blue; productivity jade/green; finance muted gold/teal; game purple/warmer tones. Do not recolor Covan Labs to match a product.

## 16. Buttons

Primary aqua `#39C6C8`, navy `#08111F` text, 8px radius; hover `#70E1E3`. Secondary transparent, `#F4F7FA` text, `1px solid #385168`; hover `rgba(255,255,255,0.04)`. Normal height 40–44px, hero 48px; apply the accessibility minimum of 44px to all interactive buttons. No giant pills.

## 17. Icons

Simple geometric line icons, 1.5–2px strokes, rounded joins, minimal geometry. Lucide, Phosphor or Heroicons are suitable references. Do not mix icon styles or use cartoons.

## 18. Illustrations

Prefer real product screenshots, app icons, abstract technical diagrams and minimal generated assets. No stock photography; avoid people unless a product requires them. Generated illustrations: dark technical background, subtle depth, clean minimal geometry, no embedded text unless requested, no AI/blockchain clichés.

## 19. Image generation direction

“Minimal premium software-lab visual language. Deep navy background, cool silver geometric forms, restrained aqua highlights, subtle dimensional lighting, clean technical precision, high negative space, editorial product-design quality.”

Avoid cyberpunk, neon purple, glowing hacker aesthetics, excessive gradients, sci-fi clutter, generic AI brains, robots, crypto coins, circuit-board clichés, stock photography, binary code and illegible text.

## Current logo identity status

**Polish B — Confluence C is the final approved master.** Freeze the selected silhouette and confluence. Production requirements: [brand-production.md](brand-production.md). Use the master for prominent placements and a separately derived Micro C for small UI. Canonical production assets live in `public/brand/`; `/brand/` documents their use. Historical exploration remains archived; it is not an alternative identity.

## 20. Logo direction

Explore multiple simple concepts. Must function as navbar logo, favicon, social avatar, publisher identity, GitHub avatar and legal/company branding on dark and light backgrounds. No reliance on tiny details.

## 21. Logo personality

Abstract engineering, building, experimentation, precision, systems, modularity and forward movement. No literal flask, atom, robot, brain, monitor, code brackets / `</>`, blockchain cube or cryptocurrency mark.

## 22. Logo structure

A compact geometric symbol plus wordmark. Explore:

1. **Modular C**: 2–4 geometric components suggesting systems fitting together; not a copyright symbol.
2. **C + V**: subtle monogram, potentially a negative-space V; still works as an abstract mark.
3. **Forward module**: layers, connections and iteration using three aligned modules, one offset element and one aqua accent.

## 23. Geometry

45° angles, circular arcs, square/modular geometry, consistent weight, strong negative space. No complex thin lines, blobs, handwriting, detailed mascots, shields or crests. Recognizable silhouette at **24 × 24px**.

## 24. Logo colors

Dark-background primary mark: cool white `#F4F7FA`; accent `#39C6C8` occupies at most 10–25% of symbol. Never entirely cyan. Wordmark: Covan `#F4F7FA`, Labs `#9EADBD`. Provide full-white and full-black/dark-navy monochrome alternatives.

## 25. Wordmark

“Covan Labs” for marketing; uppercase “COVAN LABS” allowed in compact lockup. Geometric clean sans serif, medium weight, slightly increased spacing. Inter SemiBold, Manrope SemiBold, Geist or restrained Sora are starting points. No sci-fi typography.

## 26. Lockups

Horizontal `[MARK] Covan Labs` for navigation; stacked mark over `COVAN LABS` for brand/social uses; mark-only for favicons, avatars and small UI.

## 27. Required exports

SVG is the preferred source. PNG exports must have transparent backgrounds.

```text
/logo/covan-logo-horizontal-dark.svg
/logo/covan-logo-horizontal-light.svg
/logo/covan-logo-stacked-dark.svg
/logo/covan-logo-stacked-light.svg
/logo/covan-mark-dark.svg
/logo/covan-mark-light.svg
/logo/covan-mark-512.png
/logo/covan-mark-256.png
/logo/covan-mark-128.png
/logo/covan-mark-64.png
/logo/favicon-32.png
/logo/favicon-16.png
```

## 28. Optional logo image-generation prompt

“Create a minimal geometric brand mark for a software product studio named ‘Covan Labs’. The company builds independent apps, developer tools, AI products, SaaS products and software experiments. Create an abstract symbol based subtly on the letter C, optionally incorporating a hidden V through negative space. The symbol should communicate modular software systems, precision, engineering and forward movement. Premium modern software-company identity. Simple geometric construction, strong negative space, balanced proportions, recognizable at 24px. Primary colors: cool white #F4F7FA and restrained aqua #39C6C8 on deep navy #08111F. Flat vector-style logo, no 3D, no shadows, no gradients, no text inside the symbol, no mockup.” Generate distinct concepts.

## 29. Logo exclusions

No flask, atom, robot, AI brain, circuit board, blockchain cube, cryptocurrency icon, code brackets, `</>`, rocket, lightning bolt, shield, mascot, generic infinity symbol, neon glow, purple gradient, 3D logo, metallic mockup, perspective distortion, fake wall signage, text-heavy logo or illegible typography. It must be a reusable vector identity, not a mockup.

## 30. Selection criteria

Reject concepts that fail at 24px, resemble major tech brands too closely, rely on gradients, contain excessive detail, look like crypto/Web3 or AI clichés, use literal lab symbols, fail in monochrome, lack silhouette, or feel trendy instead of durable. Prefer the simplest viable concept.

## 31. App icons vs publisher logo

Do not force app icons into the Covan system. Products retain their icons, accents and illustration styles. Publisher attribution stays consistent, e.g. “JWT Loupe — by Covan Labs”. The master logo stays neutral.

## 32. Background motifs

Optional modular grid: thin lines, nodes, rounded squares and connected modules. Aqua line `rgba(57,198,200,0.08)`; secondary line `rgba(244,247,250,0.04)`. Only in hero, footer or product showcase, never across the entire site.

## 33. Gradients

Only subtle, e.g. `radial-gradient(circle at 70% 25%, rgba(57,198,200,0.10), transparent 40%)`. No purple → blue → pink. Gradients are not the core identity.

## 34. Motion

150–250ms transitions, subtle card lift, slight underline motion, slow grid drift or gentle opacity reveal. Optional hero loops 6–15 seconds. No bouncing, exaggerated parallax, spinning objects, particle clutter or cursor-following blobs. Respect `prefers-reduced-motion`.

## 35. Screenshots

Use real extension/app/product interfaces where available. Never synthesize fake UI in place of real screenshots. Restrained frame: `#101C2C` background, `1px solid #27394D` border, 12px radius, 8px padding. Screenshots optional; do not invent interfaces to fill space.

## 36. Homepage structure

Navbar; hero/value proposition/CTA; 3–6 selected products; What We Build (Apps, Developer Tools, AI Products, Experiments); About; Principles (Useful, Reliable, Simple, Privacy-aware); optional Updates / Latest Work; footer.

## 37. Copy tone

Short and confident. “We build useful software products.” “Small tools. Serious engineering.” “Apps, developer tools and experiments from Covan Labs.” “Built with care. Designed to last.” Never generic agency copy about leveraging cutting-edge technology or revolutionizing digital experiences.

## 38. About tone

Product studio, not freelance portfolio. Preferred: “Covan Labs is an independent software lab building apps, developer tools and digital products. We focus on solving practical problems with simple interfaces and reliable engineering.” Founder may appear separately; company identity remains independent. Avoid “Hi, I’m Evan, a developer available for freelance projects.”

## 39. Chinese identity

English is the primary digital brand. 高凡 mainly in company/legal information, localization, About and footer. Do not force bilingual wording into all lockups. Optional localized lockup may put 高凡 below Covan Labs, visually secondary.

## 40. Accessibility

WCAG AA text contrast, visible keyboard focus, no color-only information, minimum 44 × 44px button targets, semantic HTML, meaningful image alternatives and reduced motion. Small aqua text on white is prohibited unless contrast is sufficient.

## 41. Responsive behavior

Mobile first. Guideline breakpoints: 640, 768, 1024, 1280px. Mobile navbar collapses; cards stack; retain whitespace and readable type; no horizontal page scrolling. Only genuinely necessary product screenshots may scroll horizontally.

## 42. Central tokens

Keep palette, radii and widths in `:root`; no random component colors. Canonical roles: `--bg-primary`, `--bg-secondary`, `--surface`, `--text-primary`, `--text-secondary`, `--text-muted`, `--accent`, `--accent-hover`, `--accent-dark`, `--border-subtle`, `--border-default`, `--border-strong`, `--radius-sm` (6px), `--radius-md` (8px), `--radius-lg` (12px), `--radius-xl` (16px), `--content-width` (1200px), `--text-width` (720px). Use the values above.

## 43. Component consistency

Reuse or extend Button, Card, Badge, SectionHeading, ProductCard, Logo, Navbar, Footer and ScreenshotFrame. Avoid unjustified one-off components.

## 44. Completion checklist

- Recognizably Covan Labs, navy dominant, restrained aqua, no AI/Web3 clichés.
- Whitespace, clear hierarchy, consistent cards.
- Maximum two typefaces, deliberate weights, readable body text.
- Logo works at 24px and in monochrome; SVG and transparent PNG; no cliché marks.
- No stock developer photos, fake UI or off-palette generated imagery.
- Subtle hover, visible focus and reduced motion.

## 45. Final creative rule

When uncertain: **simpler, calmer, more technical, more timeless**. Impress through precision, restraint, hierarchy, typography, product quality and consistency, not decoration.

Desired impression: “This is a small software lab run by people who care deeply about engineering and product quality.” Not another trendy AI startup landing page.
