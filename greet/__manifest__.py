{
    "name": "Greetings",
    "summary": "Greetings in different languages",
    "author": "Jorge Luis,Odoo Community Association (OCA)",
    "website": "https://github.com/joguenco/HolaOdoo",
    "category": "Learning/Learning",
    "version": "18.0.1.0.0",
    "license": "AGPL-3",
    "depends": ["base", "web"],
    "data": [
        "security/ir.model.access.csv",
        "views/greet_dashboard.xml",
        "views/greet_greet.xml",
        "views/res_country.xml",
        "views/greet_friend.xml",
        "views/greet_report.xml",
        "views/greet_menu.xml",
    ],
    "demo": [
        "demo/friend.xml",
    ],
    "installable": True,
    "application": True,
    "assets": {
        "web.assets_backend": [
            "greet/static/src/components/**/*.js",
            "greet/static/src/components/**/*.xml",
        ],
    },
}
