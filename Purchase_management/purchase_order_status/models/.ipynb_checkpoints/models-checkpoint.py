# -*- coding: utf-8 -*-

from odoo import api, fields, models
from odoo.tools import float_compare


class PurchaseOrder(models.Model):
    _inherit = "purchase.order"

    reception_status = fields.Selection(
        [
            ("no", "Non reçu"),
            ("partial", "Reçu partiellement"),
            ("received", "Reçu totalement"),
        ],
        compute="_compute_reception_status",
        store=True,
    )
    force_received = fields.Boolean(
        readonly=True,
        states={"done": [("readonly", False)]},
        copy=False,
        help="If true, the reception status will be forced to Fully Received, "
        "even if some lines are not fully received. "
        "To be able to modify this field, you must first lock the order.",
    )

    @api.depends(
        "state", "force_received", "order_line.qty_received", "order_line.product_qty"
    )
    def _compute_reception_status(self):
        prec = self.env["decimal.precision"].precision_get("Product Unit of Measure")
        for order in self:
            status = "no"
            if order.state in ("purchase", "done"):
                if order.force_received:
                    status = "received"
                elif all(
                    [
                        float_compare(
                            line.qty_received, line.product_qty, precision_digits=prec
                        )
                        >= 0
                        for line in order.order_line
                    ]
                ):
                    status = "received"
                elif any(
                    [
                        float_compare(line.qty_received, 0, precision_digits=prec) > 0
                        for line in order.order_line
                    ]
                ):
                    status = "partial"
            order.reception_status = status
            
class PurchaseOrderLine(models.Model):
    _inherit = 'purchase.order.line'
    
    reception_status = fields.Selection(related="order_id.reception_status", store=True)