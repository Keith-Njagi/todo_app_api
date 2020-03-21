import os 

class Config(object):
    basedir = os.path.abspath(os.path.dirname(__file__))
    SQLALCHEMY_ECHO = False
    ENVIRONMENT = 'Development'
    JWT_SECRET_KEY = '38hyt)h'
    PROPAGATE_EXCEPTIONS = True
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:kitgiana@localhost/todo_app'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = 'su93r-su93r-s3cr3t-qu1t3-h@r6-t0-h@ck-k1tg1@n@l1k3chr1st96040001'

class Development(Config):
    basedir = os.path.abspath(os.path.dirname(__file__))
    SQLALCHEMY_ECHO = False
    ENVIRONMENT = 'Development'
    JWT_SECRET_KEY = '38hyt)h'
    PROPAGATE_EXCEPTIONS = True
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:kitgiana@localhost/todo_app'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = 'su93r-su93r-s3cr3t-qu1t3-h@r6-t0-h@ck-k1tg1@n@l1k3chr1st96040001'

class Testing (Config):
    basedir = os.path.abspath(os.path.dirname(__file__))
    SQLALCHEMY_ECHO = False
    ENVIRONMENT = 'Production'
    JWT_SECRET_KEY = '38hyt)h'
    PROPAGATE_EXCEPTIONS = True
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = 'postgres://vfqexyxzulxyfm:0b8befb8b2e862387252fb08c00bdf09af90f099e2ae273ce84fda40d71a699a@ec2-54-197-239-115.compute-1.amazonaws.com:5432/db3csiff14brv8'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = 'su93r-su93r-s3cr3t-qu1t3-h@r6-t0-h@ck-k1tg1@n@l1k3chr1st96040001'

class Production(Config):
    basedir = os.path.abspath(os.path.dirname(__file__))
    SQLALCHEMY_ECHO = False
    ENVIRONMENT = 'Production'
    JWT_SECRET_KEY = '38hyt)h'
    PROPAGATE_EXCEPTIONS = True
    DEBUG = False
    SQLALCHEMY_ENGINE_OPTIONS = {'pool_recycle': 280, 'pool_timeout': 100, 'pool_pre_ping': True}
    SQLALCHEMY_DATABASE_URI = 'postgresql://keithnjagi:k1tg1@n@@172.17.0.1/mytodo'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = 'su93r-su93r-s3cr3t-qu1t3-h@r6-t0-h@ck-k1tg1@n@l1k3chr1st96040001'
