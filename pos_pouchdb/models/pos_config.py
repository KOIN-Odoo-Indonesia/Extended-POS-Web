# -*- coding: utf-8 -*-
from odoo import api, fields, models, _
import logging
from odoo.exceptions import UserError
import json


class PosConfig(models.Model):
    _inherit = 'pos.config'
    
    iface_pouchdb = fields.Boolean(
        string='Use Pouchdb',
    )
    
    iface_couchdb = fields.Boolean(
        string='Use CouchDB'
    )
    
    couchdb_url = fields.Char(
        string='CouchDB Server',
        size=200,
        help='Format http://username:password@ip_address:port/dbname'
    )