from flask_restplus import Namespace, Resource, fields
from werkzeug.exceptions import BadRequest
from werkzeug.security import generate_password_hash, check_password_hash

from datetime import datetime

from models.user_model import User, UserSchema


api = Namespace('users', description='Users\' Operations')

user_schema = UserSchema()
users_schema = UserSchema(many=True)

user_model = api.model('User', {
    'username': fields.String(required=True, description='The username'),
    'password': fields.String(required=True, description='The user\'s password')
})

@api.route('/')
class UserList(Resource):
    @api.doc('list_users', responses={ 200: 'OK', 400: 'Invalid Argument', 404: 'Not Found', 500: 'Mapping Key Error' })    
    def get(self):
        '''List all users'''
        try:
            my_users = User.fetch_all() 
            users = users_schema.dump(my_users)
            return {'status':'Matches retrieved', 'users':users}, 200
        except KeyError as e:
            api.abort(500, e.__doc__, status = "Could not perform this action", statusCode = "500")
        except Exception as e:
            api.abort(400, e.__doc__, status = "Could perform this action", statusCode = "400")
    

@api.route('/<int:id>')
@api.param('id', 'The user item identifier')
class UserItem(Resource):
    @api.doc('get_user', responses={ 200: 'OK', 400: 'Invalid Argument', 404: 'Not Found', 500: 'Mapping Key Error' })
    def get(self, id):
        '''Get user item from database'''
        try:
            my_user = User.fetch_by_id(id)
            user = user_schema.dump(my_user)
            if len(user) == 0:
                e = BadRequest('User item does not exist')
                e.data = {'status':'404'}
                raise e
            return {'status':'Match retrieved', 'user':user}, 200
        except KeyError as e:
            api.abort(500, e.__doc__, status = "Could not retrieve information", statusCode = "500")
        except Exception as e:
            api.abort(404, e.__doc__, status = "User item does not exist", statusCode = "404")

    @api.doc('edit_user', responses={ 200: 'OK', 201:'Created', 400: 'Invalid Argument', 404: 'Not Found', 500: 'Mapping Key Error' })
    @api.expect(user_model)
    def put(self, id):
        '''Edit user item in database'''
        try:
            data = api.payload
            
            id=id
            username = data['username']
            updated = datetime.utcnow()
            User.update_user(id=id, username=username, updated=updated)
            user = user_schema.dump(data)
            return {'status':'User item has been updated', 'user':user}, 201
        except KeyError as e:
            api.abort(500, e.__doc__, status = "Could not perform this action", statusCode = "500")
        except Exception as e:
            api.abort(400, e.__doc__, status = "Could not perform this action", statusCode = "400")

    @api.doc('delete_user', responses={ 200: 'OK', 201:'Created', 400: 'Invalid Argument', 404: 'Not Found', 500: 'Mapping Key Error' })
    def delete(self, id):
        '''Delete user item from database'''
        try:
            my_user = User.fetch_by_id(id)
            user = user_schema.dump(my_user)
            if len(user) == 0:
                e = BadRequest('User item does not exist')
                e.data = {'status':'404'}
                raise e
            User.delete_by_id(id)
            return {'status':'User item has been deleted'}
        except KeyError as e:
            api.abort(500, e.__doc__, status = "Could not perform this action", statusCode = "500")
        except Exception as e:
            api.abort(400, e.__doc__, status = "Could perform this action", statusCode = "400")
