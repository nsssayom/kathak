from flask import Flask
# this below line should be app.config, putting only config doesn't work
from app.config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db, compare_type = True)

from app import  models, bot,globals