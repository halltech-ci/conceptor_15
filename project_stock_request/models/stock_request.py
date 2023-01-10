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
    
    @api.model
    def _get_default_picking_type(self):
        return self.env.ref("project_stock_request.project_stock_picking_type_tm")
    
    @api.model
    def _get_default_src_location(self):
        return self.env.ref("project_stock_request.project_stock_picking_type_tm").default_location_src_id
    
    @api.model
    def _get_default_dest_location(self):
        return self.env.ref("project_stock_request.project_stock_picking_type_tm").default_location_dest_id
    
    
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
    picking_type_id = fields.Many2one('stock.picking.type', default=_get_default_picking_type)
    location_src_id = fields.Many2one('stock.location', default=_get_default_src_location)
    location_dest_id = fields.Many2one('stock.location', default=_get_default_dest_location)
    picking_ids = fields.One2many('stock.picking', 'stock_request_id', string='Transfers')
    picking_count = fields.Integer(string='Picking Orders', compute='_compute_picking_ids', default=0)
    
    
    @api.depends('picking_ids')
    def _compute_picking_ids(self):
        for request in self:
            request.picking_count = len(request.picking_ids)
            
    def action_view_picking(self):
        '''
        This function returns an action that display existing delivery orders
        of given product request ids. It can either be a in a list or in a form
        view, if there is only one delivery order to show.
        '''
        action = self.env.ref('stock.action_picking_tree_all').read()[0]

        pickings = self.mapped('picking_ids')
        if len(pickings) > 1:
            action['domain'] = [('id', 'in', pickings.ids)]
        elif pickings:
            form_view = [(self.env.ref('stock.view_picking_form').id, 'form')]
            if 'views' in action:
                action['views'] = form_view + [(state,view) for state,view in action['views'] if view != 'form']
            else:
                action['views'] = form_view
            action['res_id'] = pickings.id
        # Prepare the context.
        picking_id = pickings.filtered(lambda l: l.picking_type_id.code == 'outgoing')
        if picking_id:
            picking_id = picking_id[0]
        else:
            picking_id = pickings[0]
        action['context'] = dict(self._context, default_picking_type_id=picking_id.picking_type_id.id, default_origin=self.name, default_group_id=picking_id.group_id.id)
        return action
    
    def button_to_approve(self):
        for line in self.line_ids:
            line.action_to_approve()
        return self.write({"state": "to_approve"})
    
    def set_to_draft(self):
        if self.state in ['done', 'close']:
            raise ValidationError(_("Vous ne pouvez pas reinitialiser un OT déja traité"))
        for line in self.line_ids:
            line.set_to_draft()
        self.write({'state': 'draft'})
           
    def button_approve(self):
        for line in self.line_ids:
            line.action_approve()
        self.write({"state": "open", 'date_approve': fields.Datetime.now()})
        return True
    
    def action_confirm(self):
        if not self.button_approve():
            raise ValidationError(_("You must approve this request before"))
        if len(self.picking_ids) > 0:
            raise ValidationError(_("You can not confirm request that is already confirm"))
        #self._create_picking()
        return True
    
    @api.model
    def create(self, vals):
        if vals.get('name', '/') == '/':
            if 'company_id' in  vals:
                vals['name'] = self.env['ir.sequence'].with_context(force_company=vals['company_id']).next_by_code('stock.request') or '/'
            else:
                vals['name'] = self.env['ir.sequence'].next_by_code('stock.request') or '/'
        request = super(StockRequest, self).create(vals)
        return request
    
    def write(self, vals):
        res = super(StockRequest, self).write(vals)
        return res
    
    def unlink(self):
        for request in self:
            if request.state in ('close', 'done'):
                raise UserError(_('Vous ne pouvez pas supprimer un OT déja traité.'))
        return super(StockRequest, self).unlink()
    
    
    