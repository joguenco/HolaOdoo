from odoo import fields, models, api
from odoo.exceptions import ValidationError


class Friend(models.Model):
    _name = 'greet.friend'
    _description = 'Friend'
    _inherits = {'res.partner': 'partner_id'}

    nickname = fields.Char()
    partner_id = fields.Many2one(
        'res.partner', 
        delegate=True, 
        ondelete='cascade', 
        required=True
    )

    @api.constrains('nickname', 'name')
    def _check_nickname(self):
        for friend in self:
            if not friend.nickname.isalpha():
                raise ValidationError('Nickname must be alphabetic')

            if not friend.name.isalpha():
                raise ValidationError('Name must be alphabetic')
