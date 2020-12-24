# -*- coding: utf-8 -*-
{
    'name': "Modulo Orden Compra",

    'summary': """
        Orden compra, Detalle orden, Proveedores""",

    'description': """
        Modulo de orden compra que realiza la gestion de una orden, conlleva a los proveedor donde se podra
        agregar, crear, ademas de integrar materiales desde el modulo de obras que contiene mas de 1000 materiales.
    """,

    'author': "Alvaro Caceres Leiva",
    'website': "http://www.ContructoraLaCallecita.com",

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
        'views/view_orden_compra.xml',
        #'views/view_detalle_orden.xml',
        'views/view_proveedores.xml',
    ],
}