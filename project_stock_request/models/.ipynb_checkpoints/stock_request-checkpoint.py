# -*- coding: utf-8 -*-

from odoo import models, fields, api, _

REQUEST_STATES = [
    ("draft", "Draft"),
    ("to_approve", "To Approve"),
    ("open", "In progress"),
    ("done", "Done"),
    ('close', 'Closed'),
    ("cancel", "Cancelled"),
]

class StockRequestOrder(models.Model):
    _name = "stock.request"
    _inherit = ["mail.thread", "mail.activity.mixin"]
    _order = "id desc"
    _description = "Manage stock request for project task"
    _check_company_auto = True
    
    
    @api.model
    def _get_default_requested_by(self):
        return self.env["res.users"].browse(self.env.uid)
    
    
    name = fields.Char(string="Request Reference", required=True, tracking=True, default='/', readonly=True)
    company_id = fields.Many2one('res.company', 'Company', default=lambda self: self.env.company, index=True, required=True, readonly=True)
    state = fields.Selection(selection=REQUEST_STATES, string="State", copy=False, default="draft", index=True, readonly=True, tracking=1,)
    date = fields.Datetime(readonly=True, default=fields.Datetime.now, string="Date")
    date_approve = fields.Datetime('Date Approve', readonly=1, index=True, copy=False)
    requested_by = fields.Many2one("res.users", string="Requested by", required=True, copy=False, tracking=True, check_company=True, default=_get_default_requested_by, index=True, readonly=True)
    task_id = fields.Many2one('project.task', string="Project Task", domain ="[('project_id', '=', project_id)]")
    project_id = fields.Many2one('project.project', string="Project",)
    #sale_order = fields.Many2one('sale.order', string="Devis")
    line_ids = fields.One2many('stock.request.line', 'stock_request_id', string="Products")
    partner_id = fields.Many2one('res.partner', related="project_id.partner_id", store=True)