from odoo import fields, models


class ProductTemplate(models.Model):
    _name = "product.template"
    _inherit = [_name]

    pdf_attachment = fields.Binary("PDF Attachment")
    pdf_attachment_name = fields.Char("PDF File Name")
