from odoo import fields, models


class Greet(models.Model):
    _name = "greet.greet"
    _description = "Greetings"

    date = fields.Datetime(default=fields.Datetime.now)
    reason = fields.Char()
    line_ids = fields.One2many("greet.greet.line", "greet_id", "Lines")
