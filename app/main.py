from flask import Flask, Blueprint
from flask_cors import CORS
from flask import Flask, jsonify, request
from flask_jwt_extended import JWTManager

from config import *
from resources import api, blueprint
from models import db, ma



app = Flask(__name__)
app.config.from_object(Production)
#cors = CORS(app, resources={r"/api/*": {"origins": "*"}})
CORS(app)
jwt = JWTManager(app)
#api.init_app(app)
app.register_blueprint(blueprint)

db.init_app(app)
ma.init_app(app)

@app.before_first_request
def create_tables():
    db.create_all()


#def create_app(config_class):
    #app = Flask(__name__)
    #app.config.from_object(config_class)

    #from resources import api, blueprint
    #from models import db, ma
    
    ##api.init_app(app)
    #app.register_blueprint(blueprint)
    
    #db.init_app(app)
    #ma.init_app(app)
    
    #@app.before_first_request
    #def create_tables():
        #db.create_all()

    #return app




if __name__ == '__main__':
    #app = create_app('config.Production')
    app.run(debug=True, host='0.0.0.0', port=5055)
    #app.run()