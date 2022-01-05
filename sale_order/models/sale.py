# -*- coding: utf-8 -*-
##############################################################################
#
# Copyright 2019 EquickERP
#
##############################################################################

from odoo import models, fields, api, _
from odoo.exceptions import UserError
from odoo.exceptions import ValidationError




class sale_order(models.Model):
    _inherit = 'sale.order'

    assigned_doctor = fields.Many2one('res.partner',string="Assigned Doctor",required=True)


    