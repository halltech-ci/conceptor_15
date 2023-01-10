# -*- coding: utf-8 -*-

from odoo import models, fields, api


class PurchaseRequest(models.Model):
    _inherit = "purchase.request"
    
    sale_order = fields.Many2one('sale.order', string='Sale Order')
    project = fields.Many2one('project.project', related="sale_order.project_id", string="Project", readonly=True, store=True)
    project_code = fields.Char(related='project.code', string="Project Code", readonly=True)
    
    
class PurchaseRequestLine(models.Model):
    _inherit = "purchase.request.line"
    
    project = fields.Many2one('project.project', string="Project", readonly=True, related="request_id.project")
    product_code = fields.Char(related="product_id.default_code", string="Code Article", store=True)
    project_id = fields.Many2one('project.project', compute="_compute_project_id", store=True,)
    
    @api.depends('project')
    def _compute_project_id(self):
        for rec in self:
            if rec.project:
                rec.project_id = rec.project
            else:
                rec.project_id = False
        
    