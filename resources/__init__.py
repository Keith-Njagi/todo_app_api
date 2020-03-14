from flask import Blueprint
from flask_restx import Api


from .todos import api as todos
from .users import api as users
from .user_signup import api as register_user
from .user_login import api as login_user
from .user_change_password import api as change_password

authorizations = {
    'apikey': {
        'type': 'apiKey',
        'in': 'header',
        'name': 'Authorization',#'X-API-KEY',
        'description':'Please input Access token'
    }
}

blueprint = Blueprint('api', __name__, url_prefix='/api')
api = Api(blueprint, doc='/documentation', title='Todos API', version='1.0', description='An API to manage tasks', authorizations=authorizations, security='apikey')

api.add_namespace(todos)
api.add_namespace(users)
api.add_namespace(register_user)
api.add_namespace(login_user)
api.add_namespace(change_password)
