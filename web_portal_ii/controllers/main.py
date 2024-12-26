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

    @route(
        "/hola/odoo/v1/products/category/<int:category_id>", auth="public", website=True
    )
    def products_category_v1(self, category_id, **kwargs):
        result = (
            request.env["product.category"]
            .sudo()
            .search_read([("id", "=", category_id)], ["name"], limit=1)
        )

        if result:
            category_name = f"Products of {result[0]["name"]}"

            Product = request.env["product.template"]
            products = Product.sudo().search([("categ_id", "=", category_id)])
        else:
            return request.render("web_portal.404", status=404)

        return request.render(
            "web_portal_ii.products_category_web_portal",
            {
                "products": products,
                "category_name": category_name,
            },
        )

    @route(
        "/hola/odoo/v2/products/category/<model(product.category):category>",
        auth="public",
        website=True,
    )
    def products_category_v2(self, category, **kwargs):
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
