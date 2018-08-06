from app import app
from app.models import Todo
from flask_script import Manager

manager = Manager(app)

@manager.command
def save():
    tode = Todo(cotent="study flask")
    tode.save()


if __name__ == '__main__':
    app.run(host='0.0.0.0')