import logging
import json
import rethinkdb as r
import calendar
import time



from flask import request, jsonify
from flask_restplus import Resource
from api.blog.business import db_host, db_port
#from api.blog.serializers import category
from api.restplus import api
#from database.models import Category

log = logging.getLogger(__name__)

ns = api.namespace('events', description='Run events in the Sandbox')


@ns.route('/')
class CategoryCollection(Resource):

    #@api.marshal_list_with()
    @api.expect()
    def get(self):
        """
        Returns the 'Events Catalog'.

        Will and more endpoints for events at a later date...
        """

        return None, 201



