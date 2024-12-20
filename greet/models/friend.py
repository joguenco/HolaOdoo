import re

from odoo import _, api, fields, models
from odoo.exceptions import ValidationError


class Friend(models.Model):
    _name = "greet.friend"
    _description = "Friend"
    _inherits = {"res.partner": "partner_id"}

    partner_id = fields.Many2one(
        "res.partner", delegate=True, ondelete="cascade", required=True
    )

    @api.constrains("name")
    def _check_name(self):
        for friend in self:
            if not friend.name.isalpha():
                raise ValidationError(
                    _(
                        "Name must be alphabetic. "
                        "Must not contain spaces or special characters or numbers."
                    )
                )

    @api.constrains("email")
    def _check_email(self):
        for friend in self:
            if friend.email and not self._is_valid_email(friend.email):
                raise ValidationError(_("Invalid email address."))

    def _is_valid_email(self, email):
        email_regex = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
        return re.match(email_regex, email) is not None
