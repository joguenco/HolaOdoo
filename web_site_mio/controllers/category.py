from odoo.http import request, route

from odoo.addons.portal.controllers.portal import pager as portal_pager
from odoo.addons.website.controllers.main import Home


class Category(Home):
    @route(
        [
            "/hola/odoo/v1/products/category/<model(product.public.category):category>",
            "/hola/odoo/v1/products/category/<model(product.public.category):category>/page/<int:page>",
        ],
        auth="public",
        website=True,
    )
    def products_category(self, category, page=1, search=None, **kwargs):

        domain = [
            ("public_categ_ids", "in", category.id),
            ("is_published", "=", True),
        ]

        if search:
            domain.append(("name", "ilike", search))

        products = request.env["product.template"].sudo().search(domain)

        if not products:
            return request.render("http_routing.404", status=404)

        total = len(products)

        slug = request.env["ir.http"]._slug
        step = 3
        pager = portal_pager(
            url=f"/hola/odoo/v1/products/category/{slug(category)}",
            url_args={"search": search},
            total=total,
            page=page,
            step=step,  # Number of items per page
        )

        # Select the range of products to display
        products = products[(page - 1) * step : page * step]

        return request.render(
            "web_site_mio.products_by_category_mio",
            {
                "products": products,
                "category": category,
                "pager": pager,
                "total": total,
                "search": search,
            },
        )
