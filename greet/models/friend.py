from odoo import _, api, fields, models
from odoo.exceptions import ValidationError


class Friend(models.Model):
    _name = "greet.friend"
    _description = "Friend"
    _inherits = {"res.partner": "partner_id"}

    nickname = fields.Char(required=True)
    partner_id = fields.Many2one(
        "res.partner", delegate=True, ondelete="cascade", required=True
    )

    @api.constrains("nickname", "name")
    def _check_nickname(self):
        for friend in self:
            if friend.nickname:
                if not friend.nickname.isalpha():
                    raise ValidationError(_("Nickname must be alphabetic"))

            if not friend.name.isalpha():
                raise ValidationError(_("Name must be alphabetic"))
