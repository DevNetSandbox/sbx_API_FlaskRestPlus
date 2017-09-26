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

ns = api.namespace('metrics', description='Usage metrics in the DevNet Sandbox')


@ns.route('/')
class CategoryCollection(Resource):

    #@api.marshal_list_with()
    @api.expect()
    def get(self):
        """
        Returns a custom snapshot of Sandbox metrics, tbd.
        """

        return None, 200



@ns.route('/reservations')
@api.response(404, 'Category not found.')
class CategoryItem(Resource):

    @api.expect()
    @api.response(200, 'Request sucessfully executed')
    def get(self, game_id):
        """
        returns metrics about the global sum of metrics

         Includes:
        * All time number of reservations
        * All time sum of reservation hours
        * YTD number of reservations
        * YTD sum of reservation hours
        * Number of reservations by month
        * Sum of reservations hours by month
        """

        return None, 200




@ns.route('/reservations/<string:topology_id>')
@api.response(404, 'Category not found.')
class CategoryItem(Resource):

    @api.expect()
    @api.response(200, 'Request sucessfully executed')
    def get(self, game_id):
        """
        Returns metrics about a given sandbox

         Includes:
        * All time number of reservations
        * All time sum of reservation hours
        * YTD number of reservations
        * YTD sum of reservation hours
        * Number of reservations by month
        * Sum of reservations hours by month
        """

        return None, 200

    @ns.route('/users')
    @api.response(404, 'Category not found.')
    class CategoryItem(Resource):
        @api.expect()
        @api.response(200, 'Request sucessfully executed')
        def get(self, game_id):
            """
            returns metrics about end users

             Includes:
            * All time number of end users
            * YTD number of end users
            * Number of reservations by month
            * Sum of reservations hours by month
            """

            return None, 200


@ns.route('/users/<string:username>')
@api.response(404, 'Category not found.')
class CategoryItem(Resource):
    @api.expect()
    @api.response(200, 'Request sucessfully executed')
    def get(self, game_id):
        """
        returns metrics about given username

         Includes:
        * All time number of reservations
        * YTD number of reservations
        * Top 5 reserved labs
        * user info
        """

        return None, 200
