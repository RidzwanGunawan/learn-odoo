{
    'name': 'Rental Management',
    'version': '1.0',
    'summary': 'Manage rental orders and schedules',
    'description': """
        Comprehensive rental management system similar to Odoo Enterprise
        with rental orders, scheduling, and product management.
    """,
    'author': 'Your Name',
    'website': 'https://yourwebsite.com',
    'category': 'Sales/Rental',
    'depends': ['sale_management', 'stock', 'account'],
    'data': [
        'security/rental_security.xml',
        'security/ir.model.access.csv',
        'data/rental_data.xml',
        'views/rental_menu.xml',
        'views/rental_product_views.xml',
        'views/rental_order_views.xml',
        'views/rental_schedule_views.xml',
        'wizard/rental_wizard.xml',
    ],
    'demo': ['demo/rental_demo.xml'],
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}