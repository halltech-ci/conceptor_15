# -*- coding: utf-8 -*-

from odoo import models, fields, api


class HrEmployee(models.Model):
    _inherit = "hr.employee"
    
    hiring_date = fields.Date(string='Hiring Start Date', related="contract_id.date_start")
    seniority = fields.Integer(string="Seniority", store=True, compute='_compute_seniority')
    hiring_end = fields.Date(string='End Hiring Date', related="contract_id.date_end")
    nbre_part = fields.Float(string="Nombre de Part", default=1)
    
    
    @api.depends('hiring_date')
    def _compute_seniority(self):
        today = fields.Date.today()
        today_date = fields.Date.from_string(today)
        for rec in self:
            if rec.contract_id:
                if rec.hiring_end and rec.hiring_date:
                    rec.seniority = int((fields.Date.from_string(rec.hiring_end) - fields.Date.from_string(rec.hiring_date)).days)/366
                if rec.hiring_date:
                    age = today_date - fields.Date.from_string(rec.hiring_date)
                    rec.seniority = int(age.days/366)
                else:
                    rec.seniority = 0
            else:
                rec.seniority = 0