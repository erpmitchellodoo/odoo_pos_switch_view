{
    'name': 'POS Switch View',
    'version': '18.0.1.0.0',
    'summary': 'Grid and list product layouts with a remembered browser preference',
    'description': '''
POS Switch View for Odoo 18
===========================
Switch between product tiles and full-width product rows directly in the
Point of Sale product screen. Grid and List buttons show the active layout.

Features
--------
* One-click switching between grid and list layouts.
* One product per row in list view, with images when enabled in POS settings.
* Existing product selection, cart quantity badges, search and categories.
* View preference saved per POS configuration in the current browser.
* Responsive layout for desktop and smaller screens.

Requires Odoo 18 Point of Sale and a deployment supporting custom addons.
Browser preferences are not synchronized across devices or cashiers.
No external service, API key or additional Python package is required.

Author and maintainer: Mitchel Admin
Support: erpmitchellodoo@gmail.com
''',
    'category': 'Sales/Point of Sale',
    'author': 'Mitchel Admin',
    'maintainer': 'Mitchel Admin',
    'support': 'erpmitchellodoo@gmail.com',
    'license': 'LGPL-3',
    'images': ['static/description/banner.png'],
    'depends': ['point_of_sale'],
    'assets': {
        'point_of_sale._assets_pos': [
            'odoo_pos_switch_view/static/src/product_screen.js',
            'odoo_pos_switch_view/static/src/product_screen.xml',
            'odoo_pos_switch_view/static/src/product_screen.scss',
        ],
    },
    'installable': True,
    'application': False,
    'auto_install': False,
}
