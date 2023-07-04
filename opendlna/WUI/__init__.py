import configparser
from .routes.index import index_bp
import os
from flask import Flask
from .extentions import db, migrate, login

root_path = os.getcwd()

config = configparser.RawConfigParser()   
conf_file = os.path.normpath(root_path + '/opendlna/opendlna.conf')
config.read(conf_file)
db_path = os.path.normpath(root_path + "/opendlna/db/database.db")

print(db_path)

app = Flask(__name__, static_folder='static/')
app.config['SECRET_KEY'] = "3aecf0fa3c22de921cba843775b268f2ca846a94"
app.config['TEMPLATES_AUTO_RELOAD'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

if config.get("opendlna", "use_local_database"):
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///database.db'
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql://{config.get("postgres", "user")}:{config.get("postgres", "password")}@{config.get("postgres", "url")}:{config.get("postgres", "port")}/{config.get("postgres", "db")}' 
db.init_app(app)
migrate.init_app(app, db)
login.init_app(app)

app.register_blueprint(index_bp)