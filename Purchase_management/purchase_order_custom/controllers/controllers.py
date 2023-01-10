# -*- coding: utf-8 -*-
# from odoo import http


# class PurchaseOrderCustom(http.Controller):
#     @http.route('/purchase_order_custom/purchase_order_custom', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/purchase_order_custom/purchase_order_custom/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('purchase_order_custom.listing', {
#             'root': '/purchase_order_custom/purchase_order_custom',
#             'objects': http.request.env['purchase_order_custom.purchase_order_custom'].search([]),
#         })

#     @http.route('/purchase_order_custom/purchase_order_custom/objects/<model("purchase_order_custom.purchase_order_custom"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('purchase_order_custom.object', {
#             'object': obj
#         })
