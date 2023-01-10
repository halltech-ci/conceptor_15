# -*- coding: utf-8 -*-
# from odoo import http


# class HtaCustomEmployee(http.Controller):
#     @http.route('/hta_custom_employee/hta_custom_employee', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/hta_custom_employee/hta_custom_employee/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('hta_custom_employee.listing', {
#             'root': '/hta_custom_employee/hta_custom_employee',
#             'objects': http.request.env['hta_custom_employee.hta_custom_employee'].search([]),
#         })

#     @http.route('/hta_custom_employee/hta_custom_employee/objects/<model("hta_custom_employee.hta_custom_employee"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('hta_custom_employee.object', {
#             'object': obj
#         })
