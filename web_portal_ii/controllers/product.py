from odoo.http import request, route

from odoo.addons.website.controllers.main import Home


class Product(Home):
    @route(
        "/hola/odoo/v1/products/product/<int:product_id>", auth="public", website=True
    )
    def product(self, product_id, **kwargs):
        result = (
            request.env["product.template"]
            .sudo()
            .search([("id", "=", product_id), ("is_published", "=", True)])
        )

        if result:
            return request.render(
                "web_portal.product_web_portal",
                {
                    "product": result[0],
                },
            )
        else:
            return request.render("web_portal.404", status=404)
