# -*- coding: utf-8 -*-
{
    'name': "Rental Barang",
    'summary': "Rental Barang",
    'description': "Learn make module Rental Barang",
    'author': "My Company",
    'website': "https://www.yourcompany.com",
    'category': 'Uncategorized',
    'version': '1.0',
    'depends': ['base', 'product', 'account'],
    'data': [
        'report/rental_barang_report.xml',
        'report/rental_barang_templates.xml',
        'views/rental_cancel_wizard_views.xml',
        'views/rental_report_wizard_views.xml',
        'views/rental_barang_views.xml',
        'views/rental_product_views.xml',
        'views/rental_barang_menu.xml',
        'security/ir.model.access.csv',
      
    ],
    'installable': True,
    'application': True,
}

