from flask import Flask
from flask_restful import Api

api = Api()


def create_app(environment='local'):
    app = Flask(__name__)
    from api.config import app_config
    app.config.from_object(app_config[environment])
    api.init_app(app)

    from api.models import db
    db.init_app(app)

    from api.scripts import init_scripts
    init_scripts(app)

    return app
