# -*- coding: utf-8 -*-

from odoo import fields, models, api, _
from odoo.exceptions import ValidationError, UserError
from datetime import datetime
from datetime import date, timedelta
import odoo.addons.decimal_precision as dp




class AccountMove(models.Model):
    _inherit = "account.move"
    
    
    
    
    
    assigned_doctor = fields.Many2one('res.partner',string="Assigned Doctor",readonly=True)
    warehouse_id = fields.Many2one('stock.warehouse',string="warehouse",readonly=True)
    
    
#class AccountMoveLine(models.Model):
   # _inherit = "account.move.line"
    
    
   # x_category_on_invoiceline = fields.Many2one(related='sale_line_ids.xcategory_on_saleorderline')

    
    
    
#class AccountMoveLine(models.Model):
   # _inherit='account.move.line'
   # internal_ref=fields.Char(string='Internal 
               #reference product',store=True)




