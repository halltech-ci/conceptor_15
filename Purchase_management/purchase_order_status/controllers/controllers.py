# -*- coding: utf-8 -*-
# from odoo import http


# class PurchaseOrderStatus(http.Controller):
#     @http.route('/purchase_order_status/purchase_order_status', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/purchase_order_status/purchase_order_status/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('purchase_order_status.listing', {
#             'root': '/purchase_order_status/purchase_order_status',
#             'objects': http.request.env['purchase_order_status.purchase_order_status'].search([]),
#         })

#     @http.route('/purchase_order_status/purchase_order_status/objects/<model("purchase_order_status.purchase_order_status"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('purchase_order_status.object', {
#             'object': obj
#         })
