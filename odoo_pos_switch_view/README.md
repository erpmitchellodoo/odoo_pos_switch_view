# POS Switch View

Odoo 19 addon adding **Grid** and **List** buttons above the POS products.
List view displays one product per row, retaining product images (when enabled),
cart quantities, category filtering, search, and standard product selection.
The view choice is saved per POS configuration in the current browser.

## Installation

1. Restart Odoo to discover the addon.
2. In developer mode, open Apps and select **Update Apps List**.
3. Remove the default Apps filter, search for **POS Switch View**, and install it.
4. Reload the POS browser tab and use **List** or **Grid** above the products.

The `accounting_kit_19` directory is already in this project's `odoo.conf`
addons path. No configuration file changes are needed.

## Author and support

Author and maintainer: Mitchel Admin.
Support: erpmitchellodoo@gmail.com.
License: LGPL-3 (see `LICENSE`).

The Odoo Apps description, icon, banner and component screenshots are in
`static/description`. See `PUBLISHING.md` for asset dimensions, screenshot
provenance and publishing notes.

## Manual verification

- Switch to List: products appear as full-width rows on desktop and mobile.
- Select a product and verify its cart quantity updates; test a configurable product.
- Search and change category in each view.
- Switch to Grid and confirm the regular product tiles return.
- Reload the POS and confirm the selected view is retained.
- Check List with product images disabled and with a long product name.
