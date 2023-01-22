# -*- coding: utf-8 -*-
{
    'name': "free_snippets_zg",

    'summary': """
        Free Website Snippets""",

    'description': """
        Free web snippets
    """,

    'author': "My Company",
    'website': "https://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/16.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',
    'license': 'LGPL-3',

    # any module necessary for this one to work correctly
    'depends': ['base','website','web'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    'assets': {
        
        'web.assets_frontend': [
            
            'free_snippets_zg/static/src/css/style.css',
        ],
        
        },
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'images': [
        'static/description/banner.png',
    ]
}
