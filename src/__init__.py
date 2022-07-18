from flask import Flask, Blueprint

app = Flask(__name__)

api_sultan = Blueprint('sultan', __name__)
api_test = Blueprint('test', __name__)
api_job = Blueprint('job',__name__)

@api_test.route('/')
def index():
    return "I am at Test"


from . import controllers
