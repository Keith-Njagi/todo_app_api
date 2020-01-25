from flask_restplus import Namespace, Resource, fields
from werkzeug.exceptions import BadRequest
from werkzeug.security import generate_password_hash, check_password_hash

from datetime import datetime

from models.user_model import User, UserSchema


api = Namespace('change_password', description='Change user password')

user_schema = UserSchema()
users_schema = UserSchema(many=True)

user_model = api.model('User', {
    'username': fields.String(required=True, description='The username'),
    'password': fields.String(required=True, description='The user\'s password')
})
@api.route('')
class ChangePassword(Resource):
    @api.doc('edit_user', responses={ 200: 'OK', 201:'Created', 400: 'Invalid Argument', 404: 'Not Found', 500: 'Mapping Key Error' })
    @api.expect(user_model)
    def put(self, id):
        '''Edit user item in database'''
        try:
            data = api.payload
            
            id=id
            password = data['password']
            hashed_password = generate_password_hash(password, method='sha256')
            updated = datetime.utcnow()
            User.update_password(id=id, password=hashed_password, updated=updated)
            user = user_schema.dump(data)
            return {'status':'Password has been updated', 'user':user}, 201
        except KeyError as e:
            api.abort(500, e.__doc__, status = "Could not perform this action", statusCode = "500")
        except Exception as e:
            api.abort(400, e.__doc__, status = "Could not perform this action", statusCode = "400")