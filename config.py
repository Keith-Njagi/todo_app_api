import os 

class Config(object):
    basedir = os.path.abspath(os.path.dirname(__file__))
    SQLALCHEMY_ECHO = False
    ENVIRONMENT = 'Development'
    
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:kitgiana@localhost/todo_app'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = 'su93r-su93r-s3cr3t-qu1t3-h@r6-t0-h@ck-k1tg1@n@l1k3chr1st96040001'

class Development(Config):
    basedir = os.path.abspath(os.path.dirname(__file__))
    SQLALCHEMY_ECHO = False
    ENVIRONMENT = 'Development'
    
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:kitgiana@localhost/todo_app'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = 'su93r-su93r-s3cr3t-qu1t3-h@r6-t0-h@ck-k1tg1@n@l1k3chr1st96040001'

class Testing (Config):
    basedir = os.path.abspath(os.path.dirname(__file__))
    SQLALCHEMY_ECHO = False
    ENVIRONMENT = 'Development'
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:kitgiana@localhost/todo_app'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = 'su93r-su93r-s3cr3t-qu1t3-h@r6-t0-h@ck-k1tg1@n@l1k3chr1st96040001'

class Production(Config):
    basedir = os.path.abspath(os.path.dirname(__file__))
    SQLALCHEMY_ECHO = False
    ENVIRONMENT = 'Development'
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:kitgiana@localhost/todo_app'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = 'su93r-su93r-s3cr3t-qu1t3-h@r6-t0-h@ck-k1tg1@n@l1k3chr1st96040001'
