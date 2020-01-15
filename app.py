from flask import Flask, Blueprint

from config import *

app = Flask(__name__)

def create_app(config_class):
    
    app.config.from_object(config_class)

    from resources import api, blueprint
    from models import db, ma
    
    #api.init_app(app)
    app.register_blueprint(blueprint)
    
    db.init_app(app)
    ma.init_app(app)
    
    return app


if __name__ == '__main__':
    app = create_app('config.Production')
    #app.run(debug=True, port=5055)
    app.run()