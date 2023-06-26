# -*- coding: utf-8 -*-
{
    'name': "Prácticas",

    'summary': """
        Módulo de información de las prácticas del alumnado.""",

    'description': """
        Controla la información de las prácticas FCT de los alumnos.
    """,

    'author': "Iván Martín",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'reports/report_empresa.xml',
        'data/data.xml'
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
