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

ns = api.namespace('sandbox', description='Operations normally done via the Cloudshell portal')


@ns.route('/')
class CategoryCollection(Resource):

    #@api.marshal_list_with()
    @api.expect()
    def get(self):
        """
        # Returns the Catalog.
        ```
        Use URL params for filtering
        name = filter by Lab Name (instead of topology ID)
        category = filter labs by category (i.e. networking, collab, etc)
        availability = filter labs by if they're marked as private or not
        type = filter by Reservation or Always-On
        ```
        """
        json = """
        {
        "stuff" : "this is json stuff"
        }
        """
        return json, 200

    @api.response(201, 'Topology successfully created.')
    @api.expect()
    def post(self):
        """
        Create a new topology.

        Use this method to create a new sandbox lab.

        * Send a JSON object with the lab name in the body.

        ```
        {
          "sandbox_name": "lab name string"
        }
        ```

        """
        return None, 201


@ns.route('/<string:topology_id>')
@api.response(404, 'Category not found.')
class CategoryItem(Resource):

    @api.expect()
    @api.response(200, 'Request sucessfully executed')
    def get(self, game_id):
        """
	    Get the metadata about the contents of a Sandbox Lab.

	    * Lab Name
	    * Resources and their types (ex. CUCM, APIC, etc.)
	    * URL for lab tile image
	    * Type (Always-on vs Reservation
	    * Category
	    * Availability
	    * Etc.
        """

        return None, 200

    @api.response(201, 'Topology successfully deleted.')
    def delete(self, game_id):
        """
        Deletes sandbox lab.
        """


        return None, 201


    @api.response(201, 'Topology successfully updated.')
    def put(self, game_id):
        """
        Update a Sandbox.

        * Name
        * Type
        * Category
        * Availability

        """

        return None, 201

@ns.route('/reservation')
@api.response(404, 'Category not found.')
class CategoryItem(Resource):

    @api.expect()
    @api.response(200, 'Request sucessfully executed')
    def get(self, game_id):
        """
        Returns a list of current reservations.

        Includes:
        * State (Active, Setup, Error, Teardown)
        * Reservation ID
        * Topology ID
        * Reservation Name

        There will be URL params to also include the following data in the response:
        * Lab Owner
        * Scheduled start and end dates
        """

        return None, 200


@ns.route('/reservation/<string:topology_id>')
@api.response(404, 'Category not found.')
class CategoryItem(Resource):
    @api.expect()
    @api.response(202, 'Request sucessfully executed')
    def post(self, game_id):
        """
        Create a new reservation.

               ```
        {
          "duration": 10,
          "start_date": "date string"
          "owner": "username (optional)"
        }
        ```
        """

        return None, 202

@ns.route('/reservation/<string:reservation_id>')
@api.response(404, 'Category not found.')
class CategoryItem(Resource):
    @api.expect()
    @api.response(200, 'Request sucessfully executed')
    def get(self, game_id):
        """
        Returns metadata about a specific reservation.

        Includes:
        * State (Active, Setup, Error, Teardown)
        * Topology ID
        * Type
        * VPN information, if applicable
        * Data about each resource in the topology, including IP, Credentials, Interfaces (HTTP/SSH etc) and more
        * Reservation Scheduled start and end dates
        * Lab Owner
        * TBD

        """

        return None, 200

    @api.expect()
    @api.response(201, 'Reservation sucessfully deleted')
    def delete(self, game_id):
        """
        Delete a reservation.
        """

        return None, 200

    @api.expect()
    @api.response(201, 'Reservation sucessfully updated')
    def put(self, game_id):
        """
        Modify reservation details

         * Start/End dates, extensions by hours or days
         * Update reservation name
         * Update reservation owner

        """


    @ns.route('/reservation/<string:reservation_id>/status')
    @api.response(404, 'Category not found.')
    class CategoryItem(Resource):
        @api.expect()
        @api.response(200, 'Request sucessfully executed')
        def get(self, game_id):
            """
            Returns the state of a specific reservation.

            """

            return None, 200