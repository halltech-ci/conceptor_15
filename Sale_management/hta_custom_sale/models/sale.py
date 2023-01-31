# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from num2words import num2words
from odoo.addons import decimal_precision as dp
from odoo.exceptions import UserError, ValidationError


class SaleOrder(models.Model):
    _inherit = "sale.order"
    
    def _num_to_words(self, num):
        def _num2words(number, lang):
            try:
                return num2words(number, lang=lang).title()
            except NotImplementedError:
                return num2words(number, lang='en').title()
        if num2words is None:
            logging.getLogger(__name__).warning("The library 'num2words' is missing, cannot render textual amounts.")
            return ""
        lang_code = self.env.context.get('lang') or self.env.user.lang
        lang = self.env['res.lang'].with_context(active_test=False).search([('code', '=', lang_code)])
        num_to_word = _num2words(num, lang=lang.iso_code)
        return num_to_word
    
    name = fields.Char(readonly=True,)
    amount_tax = fields.Monetary(string='Total TTC')
    date_order = fields.Datetime(readonly=False)
    is_proforma = fields.Boolean('Proformat', default=False)
    description = fields.Text("Description : ")
    signed_user = fields.Many2one("res.users", string="Signed In User", readonly=True, default= lambda self: self.env.uid)
    sale_order_recipient = fields.Char("Destinataire")
    amount_to_word = fields.Char(string="Montant en lettre:", compute='_compute_amount_to_word')
    #amount_total_no_tax = fields.Monetary(string='Total HT', store=True, readonly=True, compute='_amount_total_no_tax', tracking=True)
    partner_id = fields.Many2one('res.partner', string='Customer',  required=True, change_default=True, index=True, tracking=1,
        domain="['|', ('company_id', '=', False), ('company_id', '=', company_id)]",)
    
    
    def _compute_amount_to_word(self):
        for rec in self:
            rec.amount_to_word = str(self._num_to_words(rec.amount_total)).upper()
    
    