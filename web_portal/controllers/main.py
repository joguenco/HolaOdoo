from odoo.http import request, route
from odoo.addons.website.controllers.main import Home


class Main(Home):
    @route("/", auth="public", website=True)
    def index(self, **kwargs):
        super().index(**kwargs)

        res = request.render(
            "web_portal.home_web_portal",
            {},
        )

        return res
