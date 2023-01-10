# -*- coding: utf-8 -*-
# from odoo import http


# class SaleCustomMargin(http.Controller):
#     @http.route('/sale_custom_margin/sale_custom_margin', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/sale_custom_margin/sale_custom_margin/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('sale_custom_margin.listing', {
#             'root': '/sale_custom_margin/sale_custom_margin',
#             'objects': http.request.env['sale_custom_margin.sale_custom_margin'].search([]),
#         })

#     @http.route('/sale_custom_margin/sale_custom_margin/objects/<model("sale_custom_margin.sale_custom_margin"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('sale_custom_margin.object', {
#             'object': obj
#         })
