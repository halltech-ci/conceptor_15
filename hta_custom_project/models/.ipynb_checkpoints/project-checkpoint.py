# -*- coding: utf-8 -*-

from odoo import models, fields, api, _


class Project(models.Model):
    _inherit = "project.project"
    
    code = fields.Char(string="Project Code", required=True, default="/", readonly=True)
    project_description = fields.Char(string='Description')

    _sql_constraints = [
        ("project_unique_code", "UNIQUE (code)", _("The code must be unique!"))
    ]
    
    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            if vals.get("code", "/") == "/":
                vals["code"] = self.env["ir.sequence"].next_by_code("project.code") or '/'
        return super().create(vals_list)
    
    """
    @api.model
    def create(self, vals):
        # Prevent double project creation
        #project = super(Project, self).create(vals)
        if vals.get('code', '/') == '/':
            self = self.with_context(mail_create_nosubscribe=True)
            vals['code'] = self.env['ir.sequence'].next_by_code('project.code') or '/'
            project = super(Project, self).create(vals)
            if not vals.get('subtask_project_id'):
                project.subtask_project_id = project.id
            if project.privacy_visibility == 'portal' and project.partner_id:
                project.message_subscribe(project.partner_id.ids)
        project = super(Project, self).create(vals)
        return project
    """
    def copy(self, default=None):
        self.ensure_one()
        if default is None:
            default = {}
        default["code"] = self.env["ir.sequence"].next_by_code("project.code")
        return super().copy(default)
    
    def name_get(self):
        result = super().name_get()
        new_result = []

        for project in result:
            rec = self.browse(project[0])
            name = "{}-{}".format(rec.code, project[1])
            new_result.append((rec.id, name))
        return new_result
