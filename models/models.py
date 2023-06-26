# -*- coding: utf-8 -*-
from odoo import models, fields, api

class alumno(models.Model):
    _name = 'practicas.alumno'
    
    name = fields.Char(string="Nombre", required=True)
    apellidos = fields.Char(string="Apellidos", required=True)
    fechaNacimiento = fields.Date(string="Fecha de nacimiento", required=True)
    cicloFormativo = fields.Selection([('0','DAM'),('1','DAW'),('2','ASIR')], string="Ciclo formativo", required=True)
    notaMedia = fields.Float(string="Nota media")
    notaMediaTexto = fields.Char(string="Nota media (texto)", compute="_notaMediaTexto", store=True)
    empresa= fields.Many2one("practicas.empresa", string="Empresa", ondelete="cascade")

    @api.depends('notaMedia')
    def _notaMediaTexto(self): 
        for r in self:
            if r.notaMedia < 5.0:
                r.notaMediaTexto = "Suspenso"
            elif r.notaMedia < 7.0:
                r.notaMediaTexto = "Aprobado"
            elif r.notaMedia < 9.0:
                r.notaMediaTexto = "Notable"
            else:
                r.notaMediaTexto = "Sobresaliente"
            
class empresa(models.Model):
    _name="practicas.empresa"
    
    name = fields.Char(string="Nombre", required=True)
    direccion = fields.Text(string="Dirección")
    listaAlumnos = fields.One2many("practicas.alumno", "empresa", string="Alumnos")

