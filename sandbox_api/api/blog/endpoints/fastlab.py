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

ns = api.namespace('fastlab', description='Get an active Sandbox in 10 seconds or less, for LL integration')


@ns.route('/')
class CategoryCollection(Resource):

    #@api.marshal_list_with()
    @api.expect()
    def get(self):
        """
        Returns the fastlabs available.
        """

        return None, 200



@ns.route('/<string:fastlab_name>')
@api.response(404, 'Category not found.')
class CategoryItem(Resource):

    @api.expect()
    @api.response(200, 'Request sucessfully executed')
    def get(self, game_id):
        """
        Returns metadata about the given FastLab Envionment

        Equivalent  to EnvInfo in the old model. Includes:
        * Number of lab and their state (Ready, InUse, Baselining, Off etc.)
        * Which users are associated to each instace
        """

        return None, 200


    @api.response(200, 'Category successfully deleted.')
    def post(self, game_id):
        """
        Request a fastlab

        Must specify
        * User
        * TTL

        """

        return None, 201



@ns.route('/<string:fastlab_name>/<string:fastlab_user>')
@api.response(404, 'Category not found.')
class CategoryItem(Resource):
    @api.expect()
    @api.response(200, 'Request sucessfully executed')
    def get(self, game_id):
        """
        Returns metadata about the fastlab given a specific user

        Includes
        * VPN info
        * Resoruces, IP, access methods, and crednials
        * VPNless URLs
        * TTL
        * More TBD
        """

        return None, 200

    @api.expect()
    @api.response(201, 'Request sucessfully executed')
    def delete(self, game_id):
        """
        Terminates the FastLab associated with  a given user
        """

        return None, 201

    @api.expect()
    @api.response(201, 'Request sucessfully executed')
    def put(self, game_id):
        """
        Modify the FastLab associated with  a given user

        Modify the TTL of the fastlab.
        """

        return None, 201

@ns.route('/<string:fastlab_name>/pool')
@api.response(404, 'Category not found.')
class CategoryItem(Resource):
    @api.expect()
    @api.response(200, 'Request sucessfully executed')
    def get(self, game_id):
        """
        Returns the ready pool size of a FastLab

        """

        return None, 200


@ns.route('/<string:fastlab_name>/pool/<string:pool_size>')
@api.response(404, 'Category not found.')
class CategoryItem(Resource):

    @api.expect()
    @api.response(201, 'Request sucessfully executed')
    def put(self, game_id):
        """
        Modify the ready pool size

        """

        return None, 201