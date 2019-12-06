# -*- coding: utf-8 -*-
{
    'name' : 'altinkaya Invoice',
    'version' : '12.0',
    'category': 'General',
    'depends' : ['base', 'sale', 'stock', 'sale_stock', 'delivery','partner_fax'],
    'author' : 'OnurUgur,Codequarters,Acespritech Solutions Pvt. Ltd.',
    'description': """
        * Provides Invoice Address
        * Provides Delivery Address
        * History of Invoices and Picking
        * Delivery Method
        * Add Button In delivery order for reference to Sale order.
    """,
    'website': 'http://www.codequarters.com',
    'data': [
             'views/account_views.xml',
             'wizard/partner_reconcile_close_view.xml',
            ],
    'demo': [],
    'installable': True,
    'auto_install': False,
}

