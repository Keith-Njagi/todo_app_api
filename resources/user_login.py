from flask_restplus import Namespace, Resource, fields
from werkzeug.exceptions import BadRequest
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import jwt_required, create_access_token, get_jwt_identity

from datetime import datetime

from models.user_model import User, UserSchema


api = Namespace('login', description='Log in user')

user_schema = UserSchema()
users_schema = UserSchema(many=True)

user_model = api.model('User', {
    'username': fields.String(required=True, description='The username'),
    'password': fields.String(required=True, description='The user\'s password')

})

@api.route('')
class LogIn(Resource):
    @api.doc('login_user', responses={ 200: 'OK', 201:'Created', 400: 'Invalid Argument', 404: 'Not Found', 500: 'Mapping Key Error' })    
    @api.expect(user_model)
    def post(self):
        '''Log in user'''
        try:
            data = api.payload
            user = User.query.filter_by(username=data['username']).first()
            name = data['username']
            if user:
                if check_password_hash(user.password, data['password']):
                    access_token = create_access_token(identity=user.id, expires_delta=False)#,  expires_delta=expires)
                    
                    current_user = user.username#user_schema.dump(data)
                    return {'status':'User logged in', 'user':current_user, 'access_token': access_token}, 200
        except KeyError as e:
            api.abort(500, e.__doc__, status = "Could not perform this action", statusCode = "500")
        except Exception as e:
            api.abort(400, e.__doc__, status = "Could not perform this action", statusCode = "400")