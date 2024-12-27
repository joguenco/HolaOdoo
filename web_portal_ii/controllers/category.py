from odoo.http import request
from odoo import fields
from odoo import http

from odoo.addons.portal.controllers.portal import CustomerPortal

class Category(CustomerPortal):
    @http.route(
        [
            "/hola/odoo/v2/products/category/<model(product.category):category>",
            "/hola/odoo/v2/products/category/<model(product.category):category>/page/<int:page>",
        ],
        auth="public",
        website=True,
    )
    def products_category(self, category, page=1, **kwargs):
        category_name = f"Products of {category.name}"

        domain = [
            ("categ_id", "=", category.id),
            ("categ_id.is_published", "=", True),
            ("is_published", "=", True),
        ]

        products = request.env["product.template"].sudo().search(domain)
        total = request.env["product.template"].sudo().search_count(domain)

        pager = request.website.pager(
            url='/hola/odoo/v2/products/category/<model(product.category):category>',
            total=total,
            page=page,
            step=5,  # Number of items per page
        )

        print(f"pager: {pager}")


        if not products:
            return request.render("web_portal_ii.404", status=404)

        return request.render(
            "web_portal_ii.products_category_web_portal",
            {
                "products": products,
                "category_name": category_name,
            },
        )
