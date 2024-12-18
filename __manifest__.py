# -*- coding: utf-8 -*-
{
    'name': "owl_custom",

    'summary': "Short (1 phrase/line) summary of the module's purpose",

    'description': """
            this module is practice for Odoo OWL customizations
    """,

    'author': "Huda",
    
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    'assets': {
        'web.assets_backend': [
            'owl_custom\static\src\components\listView\listView.css',
            'owl_custom\static\src\components\listView\listView.xml',
            'owl_custom\static\src\components\listView\listView.js',
        ],
     },
    
}

