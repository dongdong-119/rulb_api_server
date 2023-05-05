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
    contact_email='kodong119@gmail.com'
)

# config
app.config.from_object(config)


# db/orm
db = SQLAlchemy(app)


import main.models
with app.app_context():
    db.create_all()

# namespace
from main.controller.picture_controller import Picture
from main.controller.contact_controller import Contact

api.add_namespace(Picture, '/picture')
api.add_namespace(Contact, '/contact')