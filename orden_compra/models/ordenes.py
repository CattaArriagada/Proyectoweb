# -*- coding: utf-8 -*-

from odoo import models, fields, api

class OrdenDeCompra(models.Model):
        _name = 'orden_compra.orden_compras'

        name = fields.Char(string='N° Orden')
       
        licitacion_id = fields.Many2one('obras.licitaciones', string='Obra')
        monto_total = fields.Integer(string='Monto total')
        observacion = fields.Text(string='Observacion')

        #relaciones in
        proveedor_ids = fields.Many2one('orden_compra.proveedores',string='Proveedor asocido')
        #relaciones out

        detalle_orden_ids=fields.One2many('orden_compra.detalle_orden','orden_c_id')