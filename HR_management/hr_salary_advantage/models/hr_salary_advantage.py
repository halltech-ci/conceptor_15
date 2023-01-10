# -*- coding: utf-8 -*-

from odoo import models, fields, api


class HrSalaryAdvantage(models.Model):
    _name = "hr.salary.advantage"
    _description = "Manage contract fields"
    
    name = fields.Char()
    code = fields.Char(related="advantage_line.code")
    amount = fields.Monetary(string="Amount")
    is_paid = fields.Boolean(default=True)
    contract_id = fields.Many2one('hr.contract')
    currency_id = fields.Many2one(related='contract_id.currency_id')
    advantage_line = fields.Many2one('hr.salary.advantage.line', string="Advantage line")
    
    
class HrContract(models.Model):
    _inherit = "hr.contract"
    
    advantage_ids = fields.One2many('hr.salary.advantage', 'contract_id')
    
    def get_advantages_fields(self, code):
        res = self.advantage_ids.filtered(lambda l : l.code == code).amount
        return res
    
    