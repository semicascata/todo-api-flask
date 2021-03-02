from marshmallow import Schema, fields, validate
from sqlalchemy import ForeignKey, Enum
from . import db
import datetime
import enum

class Status(enum.Enum):
  OPEN = "open"
  DONE = "done"


class TodoModel(db.Model):

  __tablename__ = 'todo'

  id = db.Column(db.Integer, primary_key=True)
  description = db.Column(db.Text)
  status = db.Column(Enum(Status), default="OPEN")
  created_at = db.Column(db.DateTime, default=datetime.datetime.now)

  # fk_userid = db.Column(db.Integer, ForeignKey('user.id'), nullable=False)

  def save(self):
    db.session.add(self)
    db.session.commit()

  def update(self, data):
    for key, item in data.items():
      setattr(self, key, item)  
    db.session.commit()

  def delete(self):
    db.session.delete(self)
    db.session.commit()

  @staticmethod
  def get_all():
    return TodoModel.query.all()

  @staticmethod
  def get_one(id):
    return TodoModel.query.get(id)

class TodoSchema(Schema):
  id = fields.Int(dump_only=True)
  description = fields.Str(required=True)
  status = fields.Str(validate=validate.OneOf(['OPEN', 'DONE']))
  created_at = fields.DateTime(dump_only=True)

  # fk_userid = fields.Int(required=True)