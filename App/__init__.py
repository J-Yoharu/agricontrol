from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
app = Flask(__name__)
app.config.from_object('config')

db = SQLAlchemy(app)
migrate = Migrate(app, db, compare_type = True) 

manager = Manager(app)
manager.add_command('db', MigrateCommand)
db.create_all()
from App.Controllers import routes