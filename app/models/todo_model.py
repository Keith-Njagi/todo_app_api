from . import db, ma
#from models.user_model import User
from .user_model import User

from marshmallow import Schema, fields

from datetime import datetime


class Todo(db.Model):
    __tablename__ = 'todos'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    description = db.Column(db.String, nullable=False)
    created = db.Column(db.TIMESTAMP, server_default=db.func.current_timestamp(), nullable=False)
    updated = db.Column(db.DateTime, nullable=False, default=datetime.utcnow(), onupdate=datetime.utcnow())
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False) 
    user = db.relationship('User', backref=db.backref("todos", single_parent=True, lazy='joined'))#, primaryjoin='and_(User.id == Todo.user_id)')

    def __init__(self, title, description):
        self.title = title
        self.description = description

    def insert_record(self):
        db.session.add(self)
        db.session.commit()
        return self

    @classmethod
    def fetch_all(cls):
        return cls.query.order_by(cls.id.desc()).all()

    @classmethod
    def fetch_by_user(cls, user_id):
        return cls.query.filter_by(user_id=user_id).all()

    @classmethod
    def fetch_by_id(cls, id):
        return cls.query.filter_by(id=id).first()
    
    @classmethod #TODO: read on keyword functions & default functions
    def update_todo(cls, id, title=None, description=None, updated=None): #update
        record = cls.fetch_by_id(id)
        if title:
            record.title = title
        if description:
            record.description = description
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

class TodoSchema(ma.ModelSchema):
    class Meta:
        # fields = ('id','title','description','created','updated')
        model = Todo