# -*- coding: utf-8 -*-

from odoo import models, fields, api


class ResPartnerInherit(models.Model):
    _inherit = 'res.partner'

    tags_id = fields.Many2many(comodel_name="res.partner.category", relation="tags_table", column1="tags1",
                               column2="tags2", string="Tags", )


class AccountMoveInherit(models.Model):
    _inherit = 'account.move'

    tags_id = fields.Many2one(comodel_name="res.partner.category", string="Tag", required=False)
    tag_sale_ids = fields.Many2many('crm.tag', string='Tags')
    cost = fields.Float(string="Cost", required=False)
    net_profit = fields.Float(string="Net Profit", required=False)
    commission_amount = fields.Float(string="Commission Amount", required=False)
    commission_pre = fields.Float(string="Commission %", required=False)
    branch_id = fields.Many2one('stock.warehouse', 'Branch')

    def commission(self):
        for rec in self:
            sales = self.env['sale.order'].sudo().search([('name', '=', rec.invoice_origin)], limit=1)
            rec.branch_id = sales.warehouse_id.id
            rec.tag_sale_ids = sales.tag_ids.ids
            tag = rec.assigned_doctor.tags_id.filtered(lambda p: "ST:" in p.name and "BR:" not in p.name and rec.tag_sale_ids[0].name + ";" in p.name)
            if not tag and rec.tag_sale_ids:
                tag = rec.assigned_doctor.tags_id.filtered(
                    lambda p: rec.branch_id.code in p.name and rec.tag_sale_ids[0].name + ";" in p.name)
            rec.tags_id = tag[0].id if tag else False
            rec.commission_pre = int(rec.tags_id.name[-3:-1]) if rec.tags_id else False
            journal_line = rec.line_ids.filtered(
                lambda p: p.account_id.user_type_id.id == self.env.ref("account.data_account_type_direct_costs").id)
            rec.cost = journal_line[0].debit if journal_line else False
            rec.net_profit = rec.amount_untaxed_signed - rec.cost
            rec.commission_amount = rec.commission_pre * rec.net_profit / 100

    def action_post(self):
        res = super(AccountMoveInherit, self).action_post()
        for rec in self:
            rec.commission()
        return res
