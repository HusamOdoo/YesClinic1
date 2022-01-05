# -*- coding: utf-8 -*-
##############################################################################
#
# Copyright 2019 EquickERP
#
##############################################################################

{
    'name': "Sale_order",
    'version': '14.0.1.0',
    'category': 'Sales',
    'author': 'Fatima Ismail',
  
    'description': """
      
    """,
    'depends': ['sale_management', 'sale_stock','stock'],
    
    'website': "",
    'data': [
        'views/sale_order.xml',
        'views/invoice_view_reports.xml',
        'views/invoice_view.xml',
        
    ],
    'installable': True,
    'auto_install': False,
    'application': False,
}

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
