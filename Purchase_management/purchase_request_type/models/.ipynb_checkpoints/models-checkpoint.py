# -*- coding: utf-8 -*-

from odoo import models, fields, api


class PurchaseRequest(models.Model):
    _inherit= 'purchase.request'
    
    
    purchase_type = fields.Selection(selection=[('project', 'Matières/Consommables'), ('travaux', 'Travaux'), ('transport', 'Transport'), ('subcontract', 'Sous Traitance'), ('stock', 'Appro'),], string="Type Achat")
    is_project_approver = fields.Boolean(compute='_compute_is_project_approver')
    is_expense = fields.Boolean('is_expense', default=False)
    picking_type_id = fields.Many2one(required=False)
    is_for_project = fields.Boolean(string="Imputer au projet", default=True)
    requested_by = fields.Many2one('res.users', string="Demandeur DA", readonly=True)
    date_required = fields.Date(string="Request Date", track_visibility="onchange", default=lambda self:self._default_date_required())
    date_approve = fields.Date(string="Date Approve")
    
    
    def _compute_is_project_approver(self):
        for req in self:
            user = self.env.user
            if user.has_group('project.group_project_manager'):
                req.is_project_approver = True
            else:
                req.is_project_approver = False
    
    