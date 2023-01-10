# -*- coding: utf-8 -*-
# from odoo import http


# class PurchaseRequestSale(http.Controller):
#     @http.route('/purchase_request_sale/purchase_request_sale', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/purchase_request_sale/purchase_request_sale/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('purchase_request_sale.listing', {
#             'root': '/purchase_request_sale/purchase_request_sale',
#             'objects': http.request.env['purchase_request_sale.purchase_request_sale'].search([]),
#         })

#     @http.route('/purchase_request_sale/purchase_request_sale/objects/<model("purchase_request_sale.purchase_request_sale"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('purchase_request_sale.object', {
#             'object': obj
#         })
