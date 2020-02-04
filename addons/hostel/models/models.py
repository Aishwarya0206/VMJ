# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class hostel(models.Model):
#     _name = 'hostel.hostel'
#     _description = 'hostel.hostel'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
from odoo import models, fields, api

class Course(models.Model):
    _name = 'hostel.name'
    _description = "Girls Hostel"

    name = fields.Char(string="Title", required=True)
    description = fields.Text()
