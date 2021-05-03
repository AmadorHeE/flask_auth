from flask.cli import AppGroup

db_cli = AppGroup('db')


@db_cli.command('migrate')
def migrate():
    print('migrate executed')
