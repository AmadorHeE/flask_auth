from api.scripts.db import db_cli


def init_scripts(app):
    app.cli.add_command(db_cli)
