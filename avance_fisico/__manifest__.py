# -*- coding: utf-8 -*-
{
    'name': "Modulo de Avance Fisico",

    'summary': """
        Avances y cobros
        """,

    'description': """
        Modulo que presenta un avance fisico de una obra, con sus cobros incluidos
    """,

    'author': "Victor Venegas Galaz",
    'website': "http://www.ConstructoraLaCallecita.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Insurance',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/view_avance_licitacion.xml',
        'views/view_cobros.xml',
    ],
}