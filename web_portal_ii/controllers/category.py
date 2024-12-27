from odoo.http import request, route

from odoo.addons.portal.controllers.portal import pager as portal_pager
from odoo.addons.website.controllers.main import Home


class Category(Home):
    @route(
        [
            "/hola/odoo/v2/products/category/<model(product.category):category>/search",
            "/hola/odoo/v2/products/category/<model(product.category):category>",
            "/hola/odoo/v2/products/category/<model(product.category):category>/page/<int:page>",
        ],
        auth="public",
        website=True,
    )
    def products_category(self, category, page=1, search="", **kwargs):
        domain = [
            ("categ_id", "=", category.id),
            ("categ_id.is_published", "=", True),
            ("is_published", "=", True),
        ]

        products = request.env["product.template"].sudo().search(domain)

        if not products:
            return request.render("web_portal_ii.404", status=404)

        total = len(products)

        slug = request.env["ir.http"]._slug
        step = 6
        pager = portal_pager(
            url=f"/hola/odoo/v2/products/category/{slug(category)}",
            total=total,
            page=page,
            step=step,  # Number of items per page
        )

        products = products[(page - 1) * step : page * step]

        return request.render(
            "web_portal_ii.products_category_web_portal",
            {
                "products": products,
                "category": category,
                "pager": pager,
                "total": total,
            },
        )
