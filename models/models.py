# -*- coding: utf-8 -*-

from odoo import models, fields, api


class libros(models.Model):
    _name = 'libreria.libros'
    _description = 'libros'

    name = fields.Char('ID', required=True)
    titulo = fields.Char(String ='titulo', required = True)
    autor = fields.Char(String ='autor', required = True)
    editorial = fields.Many2one('libreria.leditoriales', String = 'editorial', required = True)
    vendido = fields.One2many('libreria.lvendidos', 'idLibro', String='vendido')
    fecha_lanzamiento = fields.Date(String = 'fecha lanzamiento', required = True)

class lvendidos (models.Model):
    _name = 'libreria.lvendidos'
    _description = 'libros vendidos'

    name = fields.Char ('ID', required = True)
    idLibro = fields.Many2one('libreria.libros', String='idLibro')
    unidades = fields.Integer (String = 'unidades', required = True)
    total = fields.Float(String = 'total', compute = '_get_total')

    @api.depends('unidades')
    def _get_total (self):
       for preciototal in self:
           preciototal.total = preciototal.unidades * 15

class leditoriales  (models.Model):
    _name = 'libreria.leditoriales'
    _description = 'editoriales'

    name = fields.Char ('ID', required = True)
    nombre = fields.Char(String = 'Nombre', required = True)
    fundador = fields.Char (String = 'Fundador', required = True)
    libros = fields.One2many('libreria.libros', 'editorial', String = 'libros')