{
    "name": "My Web Portal",
    "summary": "My Web Portal",
    "author": "Jorge Luis,Odoo Community Association (OCA)",
    "website": "https://github.com/joguenco/HolaOdoo",
    "category": "website",
    "version": "18.0.1.0.0",
    "license": "AGPL-3",
    "depends": ["stock", "portal", "website", "product_categ_image"],
    "data": [
        "security/ir.model.access.csv",
        "views/home.xml",
        "views/products_by_category.xml",
        "views/404.xml",
    ],
    "installable": True,
}
