# -*- coding: utf-8 -*-

from odoo import models, fields, api, _


class SaleOrder(models.Model):
    _inherit = "sale.order"
    
    date_order = fields.Datetime(readonly=False)
    is_proforma = fields.Boolean('Proformat', default=False)
    description = fields.Text("Description : ")
    signed_user = fields.Many2one("res.users", string="Signed In User", readonly=True, default= lambda self: self.env.uid)
    sale_order_recipient = fields.Char("Destinataire")
    #amount_total_no_tax = fields.Monetary(string='Total HT', store=True, readonly=True, compute='_amount_total_no_tax', tracking=True)
    partner_id = fields.Many2one('res.partner', string='Customer',  required=True, change_default=True, index=True, tracking=1,
        domain="['|', ('company_id', '=', False), ('company_id', '=', company_id)]",)
    