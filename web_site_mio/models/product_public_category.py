from odoo import fields, models


class ProductPublicCategory(models.Model):
    _name = 'product.public.category'
    _inherit = [_name]

    is_published = fields.Boolean(
        string="Published",
        default=True,
    )
