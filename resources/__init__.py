from flask import Blueprint
from flask_restplus import Api

from .todos import api as todos

blueprint = Blueprint('api', __name__, url_prefix='/api')
api = Api(blueprint, doc='/documentation', title='Todos API', version='1.0', description='An API to manage tasks')

api.add_namespace(todos, path='/todos')