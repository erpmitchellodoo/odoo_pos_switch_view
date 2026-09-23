/** @odoo-module **/

import { useState } from "@odoo/owl";
import { browser } from "@web/core/browser/browser";
import { patch } from "@web/core/utils/patch";
import { ProductScreen } from "@point_of_sale/app/screens/product_screen/product_screen";

patch(ProductScreen.prototype, {
    setup() {
        super.setup(...arguments);
        this.productViewStorageKey = `odoo_pos_switch_view.${this.pos.config.id}`;
        let mode = this.pos.switchProductViewMode || "grid";
        try {
            const savedMode = browser.localStorage.getItem(this.productViewStorageKey);
            if (savedMode === "grid" || savedMode === "list") {
                mode = savedMode;
            }
        } catch {
            // The switch remains usable when browser storage is unavailable.
        }
        this.productViewState = useState({ mode });
    },

    setProductViewMode(mode) {
        if (mode !== "grid" && mode !== "list") {
            return;
        }
        this.productViewState.mode = mode;
        this.pos.switchProductViewMode = mode;
        try {
            browser.localStorage.setItem(this.productViewStorageKey, mode);
        } catch {
            // Keep the choice in the POS store for this session.
        }
    },
});
