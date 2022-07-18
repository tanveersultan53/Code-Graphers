from flask import Flask
from src.config import app_config
from src.models import db
from src.models import user,job
from src import api_test as test_blueprint
from src import api_sultan as sultan_blueprint
from src import  api_job as job_blueprint
from flasgger import Swagger
from dotenv import load_dotenv
load_dotenv()

SWAGGER_TEMPLATE = {"securityDefinitions": {"x-access-tokens": {"type": "apiKey", "name": "x-access-tokens", "in": "header"}}}
def create_app(app_env):
    app = Flask(__name__)
    swagger = Swagger(app, template=SWAGGER_TEMPLATE)
    app.config['JSON_SORT_KEYS'] = False
    app.config.from_object(app_config[app_env])

    db.init_app(app)

    app.register_blueprint(test_blueprint,url_prefix='/api')
    app.register_blueprint(job_blueprint,url_prefix='/api')

    @app.route('/')
    def index():
        return "Welcome to Flask API"

    return app
