{
    'name': 'Rental Management',
    'version': '1.0',
    'summary': 'Manage rental orders, products, pricing and schedules',
    'description': """
        Comprehensive rental management system for Odoo Community
        Features include rental contracts, rental products, time-based pricing,
        rental scheduling, and automated price calculation.
    """,
    'author': 'Your Name',
    'website': 'https://yourwebsite.com',
    'category': 'Services/Rental',
    'depends': ['base', 'product', 'stock'],
    'data': [
        'security/rental_security.xml',
        'security/ir.model.access.csv',
        'data/rental_data.xml',
        'views/product_template_views.xml',
        'views/rental_product_views.xml',
        'views/rental_pricing_views.xml',
        'views/rental_order_views.xml',
        'views/rental_order_line_views.xml',
        'views/rental_schedule_views.xml',
        'views/menus.xml',
    ],
    'demo': ['demo/rental_demo.xml'],
    'assets': {
        'web.assets_backend': [
            'rental_management/static/src/js/rental_schedule.js',
            'rental_management/static/src/xml/rental_schedule_views.xml',
        ],
    },
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}