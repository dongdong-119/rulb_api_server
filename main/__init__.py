from flask import Flask
from flask_restx import Api
from flask_sqlalchemy import SQLAlchemy

import config

app = Flask(__name__)

api = Api(
    app,
    version='0.1',
    title='RULB REST API GUIDE DOCS',
    description='SCSA AI-WEB PROJECT',
    contact='kodoong119@gmail.com'
)

# config
app.config.from_object(config)

# db/orm
db = SQLAlchemy(app)

with app.app_context():
    db.create_all()

# namespace
from main.views.picture_views import Picture
api.add_namespace(Picture, '/picture')
