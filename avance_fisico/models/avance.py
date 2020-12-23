from odoo import models, fields, api

class AvanceLicitacion(models.Model):
        _name = 'avance_fisico.avance_licitacion'

        name = fields.Char(string='Nombre del avance')
       
        
        fecha_avance = fields.Date('Fecha del Avance')
        detalle_avance = fields.Text(string='Detalle del Avance')
        observacion = fields.Text(string='Observacion')
        
        #relaciones in
        cobro_ids = fields.One2many('avance_fisico.cobros', 'name',string='Cobro del avance')

        #relaciones out
        licitacion_avance_id = fields.Many2one('obras.licitaciones', string='Obra')

class Cobros(models.Model):
    _name = 'avance_fisico.cobros'

    name = fields.Char(string='Cobro', required=True)

    fecha_cobro = fields.Date('Fecha cobro')
    detalle_cobro = fields.Text('Detalle del Cobro')
    costo = fields.Integer(string='Costo')

    #relaciones out
    #avance_id = fields.Many2one('avance_fisico.avance_licitacion')

    #relaciones in
    cliente_ids = fields.Many2one('obras.clientes', string='Cliente Asociado')

