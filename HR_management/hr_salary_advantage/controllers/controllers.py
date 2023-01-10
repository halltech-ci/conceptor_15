# -*- coding: utf-8 -*-
# from odoo import http


# class HrSalaryAdvantage(http.Controller):
#     @http.route('/hr_salary_advantage/hr_salary_advantage', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/hr_salary_advantage/hr_salary_advantage/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('hr_salary_advantage.listing', {
#             'root': '/hr_salary_advantage/hr_salary_advantage',
#             'objects': http.request.env['hr_salary_advantage.hr_salary_advantage'].search([]),
#         })

#     @http.route('/hr_salary_advantage/hr_salary_advantage/objects/<model("hr_salary_advantage.hr_salary_advantage"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('hr_salary_advantage.object', {
#             'object': obj
#         })
