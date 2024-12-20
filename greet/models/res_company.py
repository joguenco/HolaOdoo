from odoo import models, api

class ResCompany(models.Model):
    _inherit = 'res.company'


    def action_greet_me_ii(self):
        return {
            'type': 'ir.actions.act_window',
            'name': 'My Company',
            'view_mode': 'form',
            'view_id': self.env.ref('greet.view_me_form').id,
            'res_model': 'res.company',
            'res_id': self.env.company.id,
            'target': 'current',
            'context': {'create': False, 'delete': False, 'edit': False},
        }

