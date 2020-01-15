from flask import Flask, Blueprint

from config import *


def create_app(config_class):
    app = Flask(__name__)
    app.config.from_object(config_class)

    from resources import api, blueprint
    from models import db, ma
    
    #api.init_app(app)
    app.register_blueprint(blueprint, url_prefix='/api')
    
    db.init_app(app)
    ma.init_app(app)
    
    return app


if __name__ == '__main__':
    app = create_app('config.Production')
    app.run(debug=True, port=5055)