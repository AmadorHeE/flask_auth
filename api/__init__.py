from flask import Flask
from api.extensions import migrate, ma
from api.resources import users_v1_bp


def create_app(environment='local'):
    app = Flask(__name__)
    from api.config import app_config
    app.config.from_object(app_config[environment])

    from api.db import db
    db.init_app(app)
    migrate.init_app(app, db)

    ma.init_app(app)

    app.register_blueprint(users_v1_bp)

    return app
