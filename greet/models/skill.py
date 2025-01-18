from odoo import fields, models


class Skill(models.Model):
    _name = "greet.skill"
    _description = "Skills"

    name = fields.Char()
    active = fields.Boolean(default=True)
