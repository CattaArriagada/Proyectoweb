# -*- coding: utf-8 -*-
{
    'name': "Módulo de obra",

    'summary': """
        Licitaciones""",

    'description': """
        Modulo de licitaciones que conlleva la obra
    """,

    'author': "Catalina Arriagada",
    'website': "http://www.LaCallecita.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Insurance',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}