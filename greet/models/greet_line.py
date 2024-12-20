from odoo import models, fields


class GreetLine(models.Model):
    _name = 'greet.greet.line'
    _description = 'Greetings lines'

    greet_id = fields.Many2one(
        comodel_name='greet.greet',
        ondelete='cascade'
    )
    partner_id = fields.Many2one(
        'res.partner',
        'Partner',
        required=True
    )
    quantity = fields.Integer(default=1)

    _sql_constraints = [
        ('quantity_check', 'CHECK(quantity > 0)', 'Quantity must be greater than 0'),
    ]