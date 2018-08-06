from app import db
import datetime
from flask_mongoengine.wtf import model_form

class Todo(db.Document):
    content = db.StringField(required=True,max_length=20)
    time = db.DateTimeField(default = datetime.datetime.now())
    status = db.IntField(dafault = 0)

TodoForm = model_form(Todo)
