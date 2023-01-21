# -*- coding: utf-8 -*-
# from odoo import http


# class PurchaseRequestLine(http.Controller):
#     @http.route('/purchase_request_line/purchase_request_line', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/purchase_request_line/purchase_request_line/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('purchase_request_line.listing', {
#             'root': '/purchase_request_line/purchase_request_line',
#             'objects': http.request.env['purchase_request_line.purchase_request_line'].search([]),
#         })

#     @http.route('/purchase_request_line/purchase_request_line/objects/<model("purchase_request_line.purchase_request_line"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('purchase_request_line.object', {
#             'object': obj
#         })
