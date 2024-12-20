from odoo import fields, models


class Greet(models.Model):
    _name = "greet.greet"
    _description = "Greetings"

    description = fields.Char()
    date = fields.Datetime(default=fields.Datetime.now)
    partner_id = fields.Many2one("res.partner", "Partner", required=True)
    line_ids = fields.One2many("greet.greet.line", "greet_id", "Lines")
