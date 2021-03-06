from odoo import models, fields, api
from odoo.exceptions import ValidationError


class Presupuesto(models.Model):
        _name = 'obras.presupuesto'

        name = fields.Char(string='Nombre de presupuesto', required=True)

        fecha = fields.Date('Fecha')
        detalle = fields.Text(string='Observación de presupuesto')
        licitacion_ids = fields.One2many('obras.licitaciones','presupuesto_id', string='Detalle Licitacion')

        #relaciones in
        detalle_presupuesto_material_ids = fields.One2many('obras.detalle_presupuesto','presupuesto_d_id')

class Detalle_presupuesto_materiales(models.Model):

        _name = "obras.detalle_presupuesto"

        name =fields.Char(string='Detalle del presupuesto')
        
        cost = fields.Float(string='Costo',default=0)
        cantidad = fields.Integer(string='Cantidad solicitada', default=1)
        sub_total = fields.Integer(string='Total', compute='_subtotal')

        @api.one
        def _subtotal(self):
               self.sub_total=self.cost*self.cantidad
        
        #relaciones in
        presupuesto_d_id = fields.Many2one('obras.presupuesto')
        materiales_d_id = fields.Many2one('obras.materiales', string='Material')

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
class Material(models.Model):
        _name = 'obras.materiales'

        name = fields.Char(string='Nombre Producto', required=True)
        
        #relacion in
        detalle_presupuesto_material_ids = fields.One2many('obras.detalle_presupuesto','materiales_d_id')
       
        #relacion out
        detalle_orden_id = fields.Many2one('orden_compra.detalle_orden')
        

class Cliente(models.Model):
        _name = 'obras.clientes'
        _rec_name = 'name'

        name = fields.Char(string='Nombre empresa', required=True)
        run_empresa = fields.Char("RUT Empresa", required=True)
        email = fields.Char(string='Correo Electrónico')
        phone = fields.Integer(string='Teléfono')
        giro = fields.Char(String='Giro', required=True)
        
        licitacion_ids = fields.One2many('obras.licitaciones','cliente_id', string='Detalle Licitacion')
        avance_ids = fields.One2many('avance_fisico.cobros', 'avance_id', string='Cobros')

class Licitacione(models.Model):
        _name = 'obras.licitaciones' 

        name = fields.Char(string='Nombre de obra', required=True)
        fechaInicio = fields.Date('Fecha de inicio')
        fechaTermino = fields.Date('Fecha de Termino')
        detalleObra = fields.Text(string='Observación de la obra')
        
        presupuesto_id = fields.Many2one('obras.presupuesto', string='Presupuesto')
        
        cliente_id = fields.Many2one('obras.clientes', string='Cliente')

        avance_ids = fields.One2many('avance_fisico.avance_licitacion','licitacion_avance_id',string='Avance Fisico')
        