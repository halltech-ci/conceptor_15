# -*- coding: utf-8 -*-

from odoo import models, fields, api


class PurchaseRequest(models.Model):
    _inherit = "purchase.request"
    
    picking_type_id = fields.Many2one(required=False)    


class PurchaseRequestLine(models.Model):
    _inherit = 'purchase.request.line'
    
    product_tmpl_id = fields.Many2one("product.template", related="product_id.product_tmpl_id", store=True)
    attribute_line_ids = fields.One2many("product.template.attribute.line", related="product_tmpl_id.attribute_line_ids")
    specifications = fields.Text(default="")