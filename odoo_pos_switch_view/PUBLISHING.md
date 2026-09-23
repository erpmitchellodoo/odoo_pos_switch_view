# Odoo Apps listing

## Metadata

- Author and maintainer: Mitchel Admin.
- Support: erpmitchellodoo@gmail.com.
- These details match the existing Customer Site Visits addon in this project.
- License: LGPL-3; full license text is included in `LICENSE`.
- No price or business website has been invented. Set commercial terms separately
  if this is intended to be a paid listing.

## Description assets

All listing assets are local to `static/description`:

| File | Dimensions | Purpose |
| --- | --- | --- |
| `icon.png` | 256 × 256 | Grid/list app icon |
| `banner.png` | 1774 × 887 | High-resolution cover, 2:1 landscape ratio |
| `grid_view.png` | 1120 × 400 | Desktop grid component screenshot |
| `list_view.png` | 1120 × 720 | Desktop list component screenshot |
| `mobile_list_view.png` | 430 × 780 | Narrow-screen list component screenshot |
| `index.html` | Responsive | Features, previews, installation, FAQ and support |

The cover uses a 2:1 thumbnail-friendly composition. The official guidelines
consulted do not prescribe a mandatory pixel size; this is a design choice,
not a claim that Odoo requires these dimensions.

The description inherits the host website's fonts and uses Bootstrap 4 classes
with limited inline color styling. It includes no JavaScript, external fonts,
external stylesheet, iframe or interactive widget. PNG assets use relative paths.
The support link uses `mailto:`.

## Screenshot provenance and checks

The configured local Odoo endpoint was unavailable during preparation. Screenshots
are browser captures of the actual inherited view-switch markup, addon JavaScript,
addon SCSS and Odoo ProductCard template/component with illustrative sample data.
The isolated preview supplies sample POS state and a minimal surrounding page.
It does not represent a live POS session. The index explicitly discloses this.
Sample product imagery comes from Odoo's Point of Sale demo assets.

Checks performed include template inheritance targets, SCSS compilation, OWL
rendering, Grid/List interactions, full-width row geometry, product click/quantity
updates in the preview, preference saving, and horizontal overflow on narrow screens.
These checks do not replace a full installation test on an Odoo 19 database.

Before submission, install and exercise the addon on a staging POS and review the
listing as rendered by the actual Apps Store. Live POS screenshots can replace the
clearly labeled component previews when a running session is available.

## Banner generation

Generated using the built-in image generation tool; no external API key or CLI
fallback was used. Original output was copied into `static/description/banner.png`.
The icon is a deterministic grid/list vector design rendered to PNG in Chrome.

Final banner prompt:

> Create a polished app marketplace cover banner for an Odoo 19 addon called 'POS Switch View'. Landscape 2:1 aspect ratio, ideally exactly 1120 x 560 pixels. Restrained professional SaaS design, white and very pale lavender background, deep plum #714b67 and teal #00898c accents. Left 48 percent: large extremely legible title exactly 'POS Switch View' on two lines; subtitle exactly 'Grid or list. Your choice.'; small understated badge exactly 'Odoo 19'. Right: clean flat vector-style illustration of two overlapping simplified point of sale product panels, one with a 2 by 3 grid of small square cards, the front panel with four horizontal product rows, a subtle bidirectional arrow connecting the modes. These are abstract graphics, not screenshots: no fake interface labels or invented functionality. Generous margins, excellent small-thumbnail readability. No Odoo logo, no company logo, no prices, no photographic imagery, no drop-heavy shadows. Render a finished crisp banner bitmap.

## References

- https://apps.odoo.com/apps/vendor-guidelines
- https://apps.odoo.com/apps/upload

Prepared locally; this work does not publish the module to an Odoo Apps account.
