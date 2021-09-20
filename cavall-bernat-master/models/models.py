# -*- coding: utf-8 -*-

from odoo import models, fields, api

#Definim les diferents classes de la nostra base de dades postgreSQL
class comanda(models.Model):
    _name = 'cavall_bernat.comanda'
    _description = 'Permet definir les caracteristiques de comanda'
    _order = 'id_comanda'

    id_comanda = fields.Integer(string='ID', required=True)
    preu = fields.Float('Preu', (6,2), default=0.00)
    data = fields.Date('Data de comanda', required = True, default = fields.date.today())
    estat_comanda = fields.Selection(string='Estat de la comanda', selection=[('r','Revisió'),('c','Confirmada'),('f','Finalitzada'),('m','Cancelada')], default='r')
    ingredient_ids = fields.One2many('cavall_bernat.ingredient', 'comanda_id', string='Ingredients')

    #restricions
    _sql_constraints=[('id_comanda_uniq', 'unique(id_comanda)', 'Aquesta ID ja existeix')]

class ingredient(models.Model):
    _name = 'cavall_bernat.ingredient'
    _description = 'Permet definir las caracteristiques de ingredient'
    _order = 'nom'

    id_ingredient = fields.Integer(string='ID', required=True)
    nom = fields.Char('Nom', required=True)
    familia = fields.Char('Familia', required=True)
    mesura = fields.Char('Mesura', required=True, size=20)
    preuing = fields.Float('Preu', (5,2), default=0.00)
    comanda_id = fields.Many2one('cavall_bernat.comanda', string='Comanda')
    proveidor_id = fields.Many2one('cavall_bernat.proveidor', string='Proveidor')

    #restricions
    _sql_constraints=[('id_ingredient_uniq', 'unique(id_ingredient)', 'Aquesta ID ja existeix'),
    ('nom_uniq', 'unique(nom)', 'Ingredient amb el mateix nom ja creat')]

class proveidor(models.Model):
    _name = 'cavall_bernat.proveidor'
    _description = 'Permet definir les caracteristiques dels proveidors'
    _order = 'nom_proveidor'

    id_proveidor = fields.Integer(string='ID', required=True)
    nom_proveidor = fields.Char('Nom', required=True)
    telefon = fields.Integer(string='Numero de telefon', required=True, size=9)
    ingredient_ids = fields.One2many('cavall_bernat.ingredient', 'proveidor_id', string='Ingredients')

    #restricions
    _sql_constraints=[('id_proveidor_uniq', 'unique(id_proveidor)', 'Aquesta ID ja existeix'),
    ('telefon_uniq', 'unique(telefon)', 'Aquest numero de telefon es utilitzat per un altre proveidor')]

class professor(models.Model):
    _name = 'cavall_bernat.professor'
    _description = 'Permet definir les caracteristiques dels professors'
    _order = 'nif'

    nif = fields.Char('NIF', required=True, size=9)
    nom_professor = fields.Char('Nom', required=True)
    email = fields.Char('Email', required=True)

    #restricions
    _sql_constraints=[('nif_uniq', 'UNIQUE(nif)', 'Aquests NIF ja existeix'), ('email_uniq', 'unique(email)', 'Aquest Mail ja esta utilitzat')]

