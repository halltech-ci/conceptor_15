# -*- coding: utf-8 -*-

from odoo import models, fields, api, _


class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'
    
    def duplicate_line(self):
        max_seq = max(line.sequence for line in self.order_id.order_line)
        seq = self.sequence
        self.copy({'order_id': self.order_id.id, 'sequence': seq + 1})