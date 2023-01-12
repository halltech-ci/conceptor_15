# -*- coding: utf-8 -*-

from odoo import models, fields, api, _


class PurchaseRequest(models.Model):
    _inherit = "purchase.request"
    
    
    @api.model
    def _get_default_name(self):
        return self.env["ir.sequence"].next_by_code("purchase.request")
    
    
    name = fields.Char(string="Request Reference", required=True, default='/', index=True, readonly=True)
    request_date = fields.Datetime(string="Request date", help="Date when the user initiated the request.", default=fields.Datetime.now, tracking=True, readonly=True)
    

class PurchaseRequestLine(models.Model):
    _inherit = 'purchase.request.line'
    
    product_tmpl_id = fields.Many2one("product.template", related="product_id.product_tmpl_id", store=True)
    attribute_line_ids = fields.One2many("product.template.attribute.line", related="product_tmpl_id.attribute_line_ids")
    specifications = fields.Text(default="")
    
    @api.onchange("product_id")
    def onchange_product_id(self):
        for rec in self:
            if rec.product_id:
                name = rec.product_id.name
                if rec.product_id.code:
                    name = "{} ".format(rec.product_id.product_tmpl_id.name)
                    for no_variant_attribute_value in rec.product_id.product_template_attribute_value_ids:
                        name += "{}".format(no_variant_attribute_value.name + ', ')
                if rec.product_id.description_purchase:
                    name += "\n" + rec.product_id.description_purchase
                rec.product_uom_id = rec.product_id.uom_id.id
                rec.product_qty = 1
                rec.name = name
    
    @api.constrains('product_id', 'product_uom_id')
    def _compare_product_uom(self):
        #for line
        if self.product_id:
            if self.product_id.uom_id.category_id != self.product_uom_id.category_id:
                raise ValidationError("Les unite de mesure de %s ne sont pas dans la meme categorie" % (self.product_id.name))
    
    
    @api.onchange('product_uom_id')
    def _onchange_product_uom(self):
        if self.product_id:
            if self.product_id.uom_id.category_id != self.product_uom_id.category_id:
                raise ValidationError("Les unite de mesure de %s ne sont pas dans la meme categorie" % (self.product_id.name))