import configparser
from .routes.index import index_bp
import os
from flask import Flask
from .extentions import db, migrate, login

root_path = os.getcwd()

config = configparser.RawConfigParser()   
conf_file = os.path.normpath(root_path + '/opendlna/opendlna.conf')
config.read(conf_file)
db_path = os.path.normpath(root_path + "/opendlna/database.db")

print(db_path)

app = Flask(__name__, static_folder='static/')
app.config['SECRET_KEY'] = "3aecf0fa3c22de921cba843775b268f2ca846a94"
app.config['TEMPLATES_AUTO_RELOAD'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{db_path}'
db.init_app(app)
migrate.init_app(app, db)
login.init_app(app)

app.register_blueprint(index_bp)