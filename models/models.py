 #-*- coding: utf-8 -*-

from odoo import models, fields, api


class lol_esports(models.Model):
    _name = 'lol_esports.lol_esports'
    _description = 'lol_esports.lol_esports'

    leagueName = fields.Char(size=30, string="Nombre")
    leagueDescription = fields.Char(string="Descripción")
    startDate = fields.Date(string="Fecha comienzo")
    endDate = fields.Date(string="Fecha final")
    leagueLogo = fields.Image(string="")
    numberOfTeams = fields.Integer(string="Nº equipos")
    isMajorLeague = fields.Boolean(string="Es una liga mayor?")
    textField = fields.Text(string="Some text?")
    ligas = fields.One2many('lol_esports.lol_teams', 'equipos', string="Ligas")

class lol_esports_teams(models.Model):
    _name = 'lol_esports.lol_teams'
    _description = 'lol_esports.teams.lol.teams'

    teamName = fields.Char(size=20)
    teamRegion = fields.Char()
    teamLeague = fields.Char()
    teamFoundationYear = fields.Date()
    teamLogo = fields.Image()
    numberOfPlayers = fields.Integer()
    currentChampion = fields.Boolean()
    originCountry = fields.Char()
    equipos = fields.Many2one('lol_esports.lol_esports', string="Equipos")
