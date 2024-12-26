from odoo.http import request, route

from odoo.addons.website.controllers.main import Home


class Category(Home):
    @route(
        "/hola/odoo/v2/products/category/<model(product.category):category>",
        auth="public",
        website=True,
    )
    def products_category(self, category, **kwargs):
        category_name = f"Products of {category.name}"

        products = (
            request.env["product.template"]
            .sudo()
            .search([("categ_id", "=", category.id)])
        )

        return request.render(
            "web_portal_ii.products_category_web_portal",
            {
                "products": products,
                "category_name": category_name,
            },
        )
