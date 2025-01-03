# -*- coding: utf-8 -*-
{
    'name': "web_site_mio",
    "summary": "My Web Portal",
    "author": "Jorge Luis,Odoo Community Association (OCA)",
    "website": "https://github.com/joguenco/HolaOdoo",
    "category": "website",
    "version": "18.0.1.0.0",
    "license": "AGPL-3",
    "depends": ["stock", "portal", "website", "website_sale"],
    'data': [
        # 'security/ir.model.access.csv',
        'views/product_public_category.xml',
        'views/home.xml',
    ],
    "installable": True,
}

