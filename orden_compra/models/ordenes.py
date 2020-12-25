# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError

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

class Detalle_Orden_Material(models.Model):
        _name = 'orden_compra.detalle_orden'

        name = fields.Char(string='Detalle orden')

        cost = fields.Float(string='Costo', default=0)
        cantidad = fields.Integer(string='Cantidad solicitada', default =1)
        sub_total = fields.Integer(string='Total', compute='_subtotal')

        #relaciones out
        materiales_o_id = fields.Many2one('obras.materiales', string='Material')
        #relaciones in
        orden_c_id =fields.Many2one('orden_compra.orden_compras')

        @api.one
        def _subtotal(self):
               self.sub_total=self.cost*self.cantidad

        #Validaciones
        @api.onchange('cost')
        @api.depends('cost')
        def validar_cost(self):
                if self.cost < 0:
                        raise ValidationError("No puedes ingresar un costo negativo")

        @api.onchange('cantidad')
        @api.depends('cantidad')
        def validar_cantidad(self):
                if self.cantidad < 1:
                        raise ValidationError("No puedes ingresar una cantidad negativa o un cero como cantidad")

class Proveedores(models.Model):
        _name = 'orden_compra.proveedores'

        name = fields.Char(string='Codigo del Proveedor', required=True)

        nombre = fields.Char(string='Nombre del proveedor')
        rut = fields.Char(string='RUT')
        telefono = fields.Integer('Numero de telefono')
        correo = fields.Char(string='Correo Electronico')

        ordenes_ids = fields.Many2one('orden_compra.orden_compras', string='Numero de orden')
        cobro_ids = fields.Many2many('avance_fisico.avance_licitacion', string='Lista Licitacion')