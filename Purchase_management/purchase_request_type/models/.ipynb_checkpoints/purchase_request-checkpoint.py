# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import UserError, ValidationError
from datetime import date, datetime, timedelta

class PurchaseRequest(models.Model):
    _inherit= 'purchase.request'
    _inherit = ["mail.thread", "mail.activity.mixin"]
    
    
    @api.model
    def _default_date_required(self):
        req_date = date.today() + timedelta(days=7)
        return req_date
    
    
    purchase_type = fields.Selection(selection_add=[('project', 'Matières/Consommables'), ('travaux', 'Travaux'), ('transport', 'Transport'), ('subcontract', 'Sous Traitance'), ('stock', 'Appro'),('service', 'Prestation de service')], string="Type Achat")
    is_project_approver = fields.Boolean(compute='_compute_is_project_approver')
    is_expense = fields.Boolean('is_expense', default=False)
    picking_type_id = fields.Many2one(required=False)
    is_for_project = fields.Boolean(string="Imputer au projet", default=True)
    requested_by = fields.Many2one('res.users', string="Demandeur DA", readonly=True)
    date_required = fields.Date(string="Request Date", default=lambda self:self._default_date_required(), tracing=True)
    date_approve = fields.Date(string="Date Approve", tracking=True)
    
    
    def _compute_is_project_approver(self):
        for req in self:
            user = self.env.user
            if user.has_group('project.group_project_manager'):
                req.is_project_approver = True
            else:
                req.is_project_approver = False
                
    def button_approved(self):
        self.to_approve_check()
        if self.project and not self.is_project_approver:
            raise UserError(
                    _("Vous n'êtes pas autorisé à valider cette DA")
                )
        return self.write({"state": "approved", "date_approve": date.today()})
    
    def to_approve_check(self):
        user = self.env.user
        if not user.has_group('purchase_request_type.group_purchase_request_approver'):
            raise UserError(
                    _("Vous n'êtes pas autorisé à valider cette DA")
                )
            
class PurchaseRequestLine(models.Model):
    _inherit = 'purchase.request.line'
    
    
    purchase_type = fields.Selection(related='request_id.purchase_type', store=True)
    
    
    