# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class sale_custom_margin(models.Model):
#     _name = 'sale_custom_margin.sale_custom_margin'
#     _description = 'sale_custom_margin.sale_custom_margin'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
