from odoo.http import request, route

from odoo.addons.portal.controllers.portal import pager as portal_pager
from odoo.addons.website.controllers.main import Home


class Main(Home):
    @route("/", auth="public", website=True)
    def index(self, **kwargs):
        super().index(**kwargs)

        Category = request.env["product.category"]
        categories = Category.sudo().search([])

        res = request.render(
            "web_portal.home_web_portal",
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
            "web_portal.products_category_web_portal_v1",
            {
                "products": products,
                "category_name": category_name,
            },
        )

    @route(
        [
            "/hola/odoo/v2/products/category/<model(product.category):category>",
            "/hola/odoo/v2/products/category/<model(product.category):category>/page/<int:page>",
        ],
        auth="public",
        website=True,
    )
    def products_category_v2(self, category, page=1, **kwargs):
        products = (
            request.env["product.template"]
            .sudo()
            .search([("categ_id", "=", category.id)])
        )

        total = len(products)
        slug = request.env["ir.http"]._slug
        step = 6
        pager = portal_pager(
            url=f"/hola/odoo/v2/products/category/{slug(category)}",
            total=total,
            page=page,
            step=step,
        )

        products = products[(page - 1) * step : page * step]

        return request.render(
            "web_portal.products_category_web_portal_v2",
            {
                "products": products,
                "category": category,
                "pager": pager,
            },
        )

    @route(
        [
            "/hola/odoo/v3/products/category/<model(product.category):category>",
            "/hola/odoo/v3/products/category/<model(product.category):category>/page/<int:page>",
        ],
        auth="public",
        website=True,
    )
    def products_category_v3(self, category, page=1, search=None, **kwargs):
        domain = [("categ_id", "=", category.id)]

        if search:
            domain.append(("name", "ilike", search))

        products = request.env["product.template"].sudo().search(domain)

        total = len(products)
        slug = request.env["ir.http"]._slug
        step = 6
        pager = portal_pager(
            url=f"/hola/odoo/v3/products/category/{slug(category)}",
            url_args={"search": search},
            total=total,
            page=page,
            step=step,
        )

        products = products[(page - 1) * step : page * step]

        return request.render(
            "web_portal.products_category_web_portal_v3",
            {
                "products": products,
                "category": category,
                "pager": pager,
                "search": search,
                "total": total,
            },
        )
