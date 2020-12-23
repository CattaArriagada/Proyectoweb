# -*- coding: utf-8 -*-
{
    'name': "Módulo de obra",

    'summary': """
        Licitaciones""",

    'description': """
        Modulo de licitaciones que conlleva la obra
    """,

    'author': "Catalina Arriagada",
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
        'views/view_licitaciones.xml',
        'views/view_presupuesto.xml',
        #'views/view_detalle_presupuesto_materiales.xml',
        'views/view_cliente.xml',
        'views/view_materiales.xml',
        #'views/templates.xml',
    ],
}