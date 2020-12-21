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
       
class Detalle_presupuesto_materiales(models.Model):

        _name = "obras.detalle_presupuesto"

        name =fields.Char(string='Detalle del presupuesto')
        
        cost = fields.Float(string='Costo')
        cantidad = fields.Integer(string='Cantidad solicitada')
        sub_total = fields.Integer(string='Total', compute='_subtotal')

        @api.one
        def _subtotal(self):
               self.sub_total=self.cost*self.cantidad
        
        #relaciones in
        presupuesto_d_id = fields.Many2one('obras.presupuesto')
        materiales_d_id = fields.Many2one('obras.materiales', string='Material')

class Material(models.Model):
        _name = 'obras.materiales'

        name = fields.Char(string='Nombre Producto', required=True)
        #codigo = fields.Integer(string='Codigo', required=True)
        
        #relacion in
        detalle_presupuesto_material_ids = fields.One2many('obras.detalle_presupuesto','materiales_d_id')
        #relacion out
        detalle_orden_ids = fields.One2many('orden_compra.detalle_orden','materiales_o_id')
        #estamos tocando
        #cobros_id = fields.Many2one('avance_fisico.cobros', string='cobro')
        #costo 

# LISTO
#otro intento
class Cliente(models.Model):
        _name = 'obras.clientes'
        _rec_name = 'name'

        name = fields.Char(string='Nombre empresa', required=True)
        run_empresa = fields.Char("RUT Empresa", required=True)
        email = fields.Char(string='Correo Electronico')
        phone = fields.Integer(string='Telefono')
        giro = fields.Char(String='Giro', required=True)
        
        #licitacion_ids = fields.One2many('obras.licitaciones','cliente_id', string='Detalle Licitacion')
        #avance_ids = fields.Many2one('avance_fisico.cobros', string='Avance Fisico')

class Licitacione(models.Model):
        _name = 'obras.licitaciones' 

        name = fields.Char(string='Nombre Obra', required=True)
        fechaInicio = fields.Date('Fecha de inicio')
        fechaTermino = fields.Date('Fecha de Termino')
        detalleObra = fields.Text(string='Observación de la obra')
        
        #presupuesto_id = fields.Many2one('obras.presupuesto', string='Presupuesto')
        
        #cliente_id = fields.Many2one('obras.clientes', string='Cliente')

        #avance_ids = fields.One2many('avance_fisico.avance_licitacion','licitacion_avance_id',string='Avance Fisico')
        #orden_compra_ids = fields.One2many('orden_compra.orden_compras', 'licitacion_id', string='N Orden')