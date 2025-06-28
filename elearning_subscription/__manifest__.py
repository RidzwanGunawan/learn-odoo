{
    'name': 'E-Learning Subscription',
    'summary': 'Manajemen materi dan langganan e-learning',
    'category': 'Education',
    'version': '1.0',
    'author': 'Nama Kamu',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/menu_views.xml',
        'views/course_views.xml',
        'views/material_views.xml',
        'views/category_views.xml',
        'views/subscription_views.xml',
    ],
    'installable': True,
    'application': True,  # <<< penting!
    'assets': {},
}
