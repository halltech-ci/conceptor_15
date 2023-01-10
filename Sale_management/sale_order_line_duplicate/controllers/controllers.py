# -*- coding: utf-8 -*-
# from odoo import http


# class SaleOrderLineDuplicate(http.Controller):
#     @http.route('/sale_order_line_duplicate/sale_order_line_duplicate', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/sale_order_line_duplicate/sale_order_line_duplicate/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('sale_order_line_duplicate.listing', {
#             'root': '/sale_order_line_duplicate/sale_order_line_duplicate',
#             'objects': http.request.env['sale_order_line_duplicate.sale_order_line_duplicate'].search([]),
#         })

#     @http.route('/sale_order_line_duplicate/sale_order_line_duplicate/objects/<model("sale_order_line_duplicate.sale_order_line_duplicate"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('sale_order_line_duplicate.object', {
#             'object': obj
#         })
