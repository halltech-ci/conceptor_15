# -*- coding: utf-8 -*-

from odoo import models, fields, api


class HrSalaryAdvantage(models.Model):
    _name = "hr.salary.advantage"
    _description = "Manage contract fields"
    
    name = fields.Char()
    #advantage_line = fields.One2many('hr.salary.advantage', 'advantage_id')
    amount = fields.Monetary(string="Amount")
    paid = fields.Boolean()
    contract_id = fields.Many2one('hr.contract')
    currency_id = fields.Many2one(related='contract_id.currency_id')
    
    
class HrContract(models.Model):
    _inherit = "hr.contract"
    
    advantage_ids = fields.One2many('hr.salary.advantage', 'contract_id')
    
    