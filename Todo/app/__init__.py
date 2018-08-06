from flask import Flask
from flask_mongoengine import MongoEngine

# 定义连接Mongodb的数据库连接

app = Flask(__name__)
app.config.from_object('config')

db = MongoEngine(app)

from app import views,models
