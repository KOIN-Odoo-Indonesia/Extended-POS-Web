# -*- coding: utf-8 -*-
from odoo import api, fields, models, _
import logging
from odoo.exceptions import UserError
import json


class PosConfig(models.Model):
    _inherit = 'pos.config'
    
    is_pouchdb = fields.Boolean(
        string='Use Pouchdb',
    )
    
    couchdb_url = fields.Char(
        string='CouchDB Server',
    )
    
    
    
    