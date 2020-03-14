from flask_restx import Namespace, Resource, fields
from werkzeug.exceptions import BadRequest
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import jwt_required, create_access_token,get_jwt_identity

from datetime import datetime

from models.user_model import User, UserSchema


api = Namespace('signup', description='Register user')

user_schema = UserSchema()
users_schema = UserSchema(many=True)

user_model = api.model('User', {
    'username': fields.String(required=True, description='The username'),
    'password': fields.String(required=True, description='The user\'s password')

})

@api.route('')
class SignUp(Resource):
    @api.doc('register_user', responses={ 200: 'OK', 201:'Created', 400: 'Invalid Argument', 404: 'Not Found', 500: 'Mapping Key Error' })    
    @api.expect(user_model)
    def post(self):
        '''Register user'''
        try:
            data = api.payload
            username = data['username']
            hashed_password = generate_password_hash(data['password'], method='sha256')
            new_user = User(username=username, password=hashed_password)
            new_user.insert_record()
            user = user_schema.dump(data)
            this_user = User.fetch_by_user(username)

            access_token = create_access_token(identity=this_user.id, expires_delta=False)
            return {'status':'User added','access token': access_token, 'user':user}, 201
        except KeyError as e:
            api.abort(500, e.__doc__, status = "Could not perform this action", statusCode = "500")
        except Exception as e:
            api.abort(400, e.__doc__, status = "Could not perform this action", statusCode = "400")