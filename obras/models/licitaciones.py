from odoo import models, fields, api


class Presupuesto(models.Model):
        _name = 'obras.presupuesto'

        name = fields.Char(string='Obra', required=True)

        fecha = fields.Date('Fecha')
        detalle = fields.Text(string='Detalle de presupuesto')
        #licitacion_ids = fields.One2many('obras.licitaciones','presupuesto_id', string='Detalle Licitacion')

        #relaciones in
        #detalle_presupuesto_material_ids = fields.One2many('obras.detalle_presupuesto','presupuesto_d_id')
        #orden_ids = fields.Many2many('orden_compra.orden_compras', string="Orden de compra")
       