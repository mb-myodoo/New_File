from odoo import api, fields, models


class SaleOrder(models.Model):
    _inherit = "sale.order"
    
    new_field = fields.Char(string='Product')