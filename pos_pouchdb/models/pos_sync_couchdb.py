from odoo import models, fields, api, _  
from odoo.exceptions import UserError, ValidationError
import logging
import couchdb


_logger = logging.getLogger(__name__)


class PosSyncCouchDB(models.Model):
    _name = 'pos.sync.couchdb'

    def sync(self):
        couch = couchdb.Server('http://admin:admin123@128.199.175.43:5984')
        db = couch['posorders']
        orders = []
        for row in db.view('_all_docs', include_docs=True, limit=1):
            #_logger.info(row['doc'])
            #orders.append(row['doc'])
            self.env['pos.order'].create_from_ui([{'data':row['doc']}])
        _logger.info(orders)   
            


        
