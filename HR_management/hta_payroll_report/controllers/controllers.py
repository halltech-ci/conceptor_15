# -*- coding: utf-8 -*-
# from odoo import http


# class HtaPayrollReport(http.Controller):
#     @http.route('/hta_payroll_report/hta_payroll_report', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/hta_payroll_report/hta_payroll_report/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('hta_payroll_report.listing', {
#             'root': '/hta_payroll_report/hta_payroll_report',
#             'objects': http.request.env['hta_payroll_report.hta_payroll_report'].search([]),
#         })

#     @http.route('/hta_payroll_report/hta_payroll_report/objects/<model("hta_payroll_report.hta_payroll_report"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('hta_payroll_report.object', {
#             'object': obj
#         })
