# -*- coding: utf-8 -*-

from odoo import models, fields, api


class PurchaseRequestLine(models.Model):
    _inherit = 'purchase.request.line'
    
    ordered_qty = fields.Float(compute='_compute_qty_ordered', help="Effective qty buy")
    ordered_price_total = fields.Float(compute='_compute_qty_ordered')
    qty_receive = fields.Float(compute='_compute_qty_receive', help="Effective qty receive")
    
    @api.depends('purchase_lines')
    def _compute_qty_receive(self):
        for rec in self:
            rec.qty_receive = 0
            for line in rec.purchase_lines.filtered(lambda x:x.state in ['done', 'purchase']):
                if rec.product_uom_id and line.product_uom != rec.product_uom_id:
                    rec.qty_receive += line.product_uom._compute_quantity(line.qty_received, rec.product_uom_id)
                else:
                    rec.qty_receive += line.qty_received
                
    
    def _compute_qty_ordered(self):
        for rec in self:
            rec.ordered_qty = 0.0
            rec.ordered_price_total = 0
            for line in rec.purchase_lines.filtered(lambda x: x.state in ["done", "purchase"]):
                if rec.product_uom_id and line.product_uom != rec.product_uom_id:
                    rec.ordered_qty += line.product_uom._compute_quantity(
                        line.product_qty, rec.product_uom_id
                    )
                    rec.ordered_price_total += line.price_subtotal
                else:
                    rec.ordered_qty += line.product_qty
                    rec.ordered_price_total += line.price_subtotal
    
    
    