from odoo.http import request, route

from odoo.addons.website.controllers.main import Home


class Product(Home):
    @route(
        "/hola/odoo/v1/products/product/<model(product.template):product>",
        auth="public",
        website=True,
    )
    def product(self, product, **kwargs):
        if product.is_published:
            return request.render(
                "web_site_mio.product_web_portal",
                {
                    "product": product,
                },
            )
        else:
            return request.render("http_routing.404", status=404)
