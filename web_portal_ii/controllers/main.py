from odoo.http import request, route

from odoo.addons.website.controllers.main import Home


class Main(Home):
    @route("/", auth="public", website=True)
    def index(self, **kwargs):
        super().index(**kwargs)

        Category = request.env["product.category"]
        categories = Category.sudo().search([])

        res = request.render(
            "web_portal_ii.home_web_portal",
            {"categories": categories},
        )

        return res
