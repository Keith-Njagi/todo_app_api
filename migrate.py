from flask import Flask
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

#from models import db
#from app import create_app
from config import *
from resources import api, blueprint
from models import db, ma

app = Flask(__name__)
app.config.from_object(Development)
    
#api.init_app(app)
app.register_blueprint(blueprint)

db.init_app(app)
ma.init_app(app)


migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)


if __name__ == '__main__':
    manager.run()