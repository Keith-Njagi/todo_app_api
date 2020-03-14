from . import db, ma
#from models.todo_model import Todo

from marshmallow import Schema, fields

from datetime import datetime

class User( db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, nullable=False)
    password = db.Column(db.String, nullable=False)
    created = db.Column(db.TIMESTAMP, server_default=db.func.current_timestamp(), nullable=False)
    updated = db.Column(db.DateTime, nullable=False, default=datetime.utcnow(), onupdate=datetime.utcnow())

    def __init__(self, username, password):
        self.username = username
        self.password =password

    def insert_record(self):
        db.session.add(self)
        db.session.commit()
        return self

    @classmethod
    def fetch_all(cls):
        return cls.query.order_by(cls.id.desc()).all()

    @classmethod
    def fetch_by_id(cls, id):
        return cls.query.filter_by(id=id).first()

    @classmethod
    def fetch_by_user(cls, username):
        return cls.query.filter_by(username=username).first()
    
    @classmethod #TODO: read on keyword functions & default functions
    def update_user(cls, id, username=None, password=None, updated=None): #update
        record = cls.fetch_by_id(id)
        
        if username:
            record.username = username
        if updated:
            record.updated = updated

        db.session.commit()
        return True

    @classmethod #TODO: read on keyword functions & default functions
    def update_password(cls, id, password=None, updated=None): #update
        record = cls.fetch_by_id(id)
        if password:
            record.password = password
        if updated:
            record.updated = updated

        db.session.commit()
        return True

    @classmethod
    def delete_by_id(cls, id):
        record = cls.query.filter_by(id=id)
        record.delete()
        db.session.commit()
        return True

class UserSchema(ma.ModelSchema):
    class Meta:
        fields = ('id','username','created','updated')
        #model = User