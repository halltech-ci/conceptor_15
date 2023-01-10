# -*- coding: utf-8 -*-

from odoo import models, fields, api


class HrSalaryAdvantageLine(models.Model):
    _name = "hr.salary.advantage.line"
    _description = "Salary advantage line"
    
    
    name = fields.Char()
    code = fields.Char(required=True)
    
    _sql_constraints = [
        ('code_uniq', 'unique (code)', 'Ce code est déja utilisé !')
    ]    