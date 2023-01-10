# -*- coding: utf-8 -*-
# from odoo import http


# class PurchaseOrderAnalytic(http.Controller):
#     @http.route('/purchase_order_analytic/purchase_order_analytic', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/purchase_order_analytic/purchase_order_analytic/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('purchase_order_analytic.listing', {
#             'root': '/purchase_order_analytic/purchase_order_analytic',
#             'objects': http.request.env['purchase_order_analytic.purchase_order_analytic'].search([]),
#         })

#     @http.route('/purchase_order_analytic/purchase_order_analytic/objects/<model("purchase_order_analytic.purchase_order_analytic"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('purchase_order_analytic.object', {
#             'object': obj
#         })
