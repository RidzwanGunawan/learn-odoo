{
    'name': 'Indonesia PPh 21 Payslip Custom',
    'version': '18.0.1.0.0',
    'category': 'Human Resources',
    'summary': 'Custom Payslip dengan Form PPh 21 Indonesia',
    'description': """
        Modul custom untuk membuat payslip dengan form PPh 21 Indonesia
        Untuk Odoo v18 Community
    """,
    'author': 'Your Name',
    'website': 'https://yourwebsite.com',
    'depends': ['hr', 'l10n_id'],
    'data': [
        'security/ir.model.access.csv',
        'views/hr_payslip_views.xml',
        'views/hr_employee_views.xml',
    ],
    'demo': [],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}