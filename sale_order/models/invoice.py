# -*- coding: utf-8 -*-

from odoo import fields, models, api, _
from odoo.exceptions import ValidationError, UserError
from datetime import datetime
from datetime import date, timedelta
import odoo.addons.decimal_precision as dp




class AccountMove(models.Model):
    _inherit = "account.move"

    assigned_doctor = fields.Many2one('res.partner',required=True,string="Assigned Doctor")
    warehouse_id = fields.Many2one('stock.warehouse',required=True,string="Branch")



