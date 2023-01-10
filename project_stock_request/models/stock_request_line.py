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

class StockRequestLine(models.Model):
    _name = "stock.request.line"
    _description = "Manage stock request line"
    _inherit = ["mail.thread", "mail.activity.mixin"]
    
    
    name = fields.Char(string="Description")
    request_state = fields.Selection(selection=REQUEST_STATES, string='Status', readonly=True, copy=False, default='draft', required=True, help='Expense Report State',)
    stock_request_id = fields.Many2one('stock.request', string="Product Request")
    product_id = fields.Many2one("product.product", string="Product", domain=[("purchase_ok", "=", True)], tracking=True,)
    product_uom_id = fields.Many2one("uom.uom", string="Product Unit of Measure", tracking=True, related='product_id.uom_id')
    requested_by = fields.Many2one("res.users", related="stock_request_id.requested_by", string="Requested by", store=True,)
    initial_qty = fields.Float('Initial Qty', digits="Product Unit of Measure")#Quantity in sale order
    product_uom_qty = fields.Float('Product Qty', digits="Product Unit of Measure")#Quantity as for workorder
    qty_done = fields.Float('Qty Done', digits="Product Unit of Measure", compute='_compute_qty_done',)#Quantity give by stock
    #product_request_allocation_ids = fields.One2many("product.request.allocation", "product_request_line_id", string="Product Request Allocation",)
    qty_in_progress = fields.Float(string="Qty In Progress", digits="Product Unit of Measure", readonly=True, store=True,
        help="Quantity in progress. Qty left", default=0)
    #analytic_account_id = fields.Many2one(comodel_name="account.analytic.account", string="Analytic Account", track_visibility="onchange",)
    #product_request_allocation_ids = fields.One2many("product.request.allocation", "product_request_line_id", string="Product Request Allocation",)
    task_id = fields.Many2one('project.task', string='Project Task', required=True, ondelete='cascade')
    project_id = fields.Many2one('project.project', related="stock_request_id.project_id")
    #manage product_requestpicking
    #move_ids = fields.One2many('stock.move', 'product_line_id', string='Reservation', readonly=True, ondelete='set null', copy=False)
    
    def action_to_approve(self):
        self.request_state = "to_approve"
    
    def action_approve(self):
        self.request_state = "open"
    
    def action_done(self):
        self.request_state = "done"
    
    def set_to_draft(self):
        self.request_state = 'draft'
        
    def action_close(self):
        self.request_state = 'close'
    
    