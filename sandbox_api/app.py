import logging.config


from flask import Flask, Blueprint, redirect
import settings
from api.blog.endpoints.sandbox import ns as api_sandbox
from api.blog.endpoints.fastlab import ns as api_fastlab
from api.blog.endpoints.metrics import ns as api_metrics
from api.blog.endpoints.event import ns as api_events
#from api.blog.endpoints.score import ns as api_score
#from api.blog.endpoints.players import ns as api_players
from api.restplus import api
from database import db

# from api.blog.business import db_host, db_port

app = Flask(__name__)
#logging.config.fileConfig('logging.conf')
#log = logging.getLogger(__name__)

@app.route('/newGame')
def new_game():
    return app.send_static_file('newGame.html')

@app.route('/score')
def score():
    return app.send_static_file('score.html')

@app.route('/mgmt')
def roll():
    return redirect('http://www.piilossa.com/')

def configure_app(flask_app):
    #flask_app.config['SERVER_NAME'] = settings.FLASK_SERVER_NAME
    flask_app.config['SQLALCHEMY_DATABASE_URI'] = settings.SQLALCHEMY_DATABASE_URI
    flask_app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = settings.SQLALCHEMY_TRACK_MODIFICATIONS
    flask_app.config['SWAGGER_UI_DOC_EXPANSION'] = settings.RESTPLUS_SWAGGER_UI_DOC_EXPANSION
    flask_app.config['RESTPLUS_VALIDATE'] = settings.RESTPLUS_VALIDATE
    flask_app.config['RESTPLUS_MASK_SWAGGER'] = settings.RESTPLUS_MASK_SWAGGER
    flask_app.config['ERROR_404_HELP'] = settings.RESTPLUS_ERROR_404_HELP


def initialize_app(flask_app):
    configure_app(flask_app)

    blueprint = Blueprint('api', __name__, url_prefix='/api')
    api.init_app(blueprint)
    api.add_namespace(api_sandbox)
    api.add_namespace(api_fastlab)
    api.add_namespace(api_metrics)
    api.add_namespace(api_events)
    #api.add_namespace(api_players)
    flask_app.register_blueprint(blueprint)

    db.init_app(flask_app)


def main():
    initialize_app(app)
    #log.info('>>>>> Starting development server at http://{}/api/ <<<<<'.format(app.config['SERVER_NAME']))
    app.run(host="0.0.0.0", debug=True)

if __name__ == "__main__":
    main()
