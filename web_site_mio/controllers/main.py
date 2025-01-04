from odoo.http import request, route

from odoo.addons.website.controllers.main import Home


class Main(Home):
    @route("/", auth="public", website=True)
    def index(self, **kwargs):
        super().index(**kwargs)

        Category = request.env["product.public.category"]
        categories = Category.sudo().search([("is_published", "=", True)])

        return request.render(
            "web_site_mio.home_web_portal",
            {"categories": categories},
        )
