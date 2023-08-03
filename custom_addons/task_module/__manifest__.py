# -*- coding: utf-8 -*-
{
    'name': "Task Module Ariosg",

    'summary': """
        Odoo 15 Development Tutorials""",

    'description': """
       Test module
    """,

    'author': 'Armando Rios Gallego',
    'company': 'Nose',
    'website': 'https://www.google.com',

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Productivity',
    'version': '1.0.0.0.0',
    'license': 'AGPL-3',

    # any module necessary for this one to work correctly
    'images': ['static/description/banner.gif'],
    'installable': True,
    'auto_install': False,
    'data':[
        'views/menu.xml',
        'views/task.xml',
    ],
    # always loaded
    #'data': [
    #    'data/slide_channel_data.xml',
    #    'data/slide_channel_data_v13.xml',
    #    'data/slide_channel_data_v15.xml',
    #    'security/security.xml',
    #    'security/ir.model.access.csv',
    #    'views/views.xml',
    #    'views/templates.xml',
    #    'views/openacademy.xml',
    #    'views/partner.xml',
    #    'views/session_board.xml',
    #    'reports.xml',
    #],
    # only loaded in demonstration mode
    #'demo': [
    #    'demo/demo.xml',
    #],
}