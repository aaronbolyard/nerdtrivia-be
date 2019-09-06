import click
from flask import current_app, g
from flask.cli import with_appcontext

from nerdtrivia.model.db import db, migrate

import nerdtrivia.model.user

def get_database():
	if 'database' not in g:
		g.database = db

	return g.database

def close_database(app):
	pass

def initialize_database():
	database = get_database()
	database.create_all()

def init_app(app):
	db.init_app(app)
	migrate.init_app(app, db)

	app.teardown_appcontext(close_database)
	app.cli.add_command(add_user_command)

@click.command('nt-add-user')
@click.option('--username')
@click.option('--password')
@with_appcontext
def add_user_command(username, password):
	"""
	Adds the specified user.
	"""
	password = generate_password_hash(password)

	db = get_database()
	user = User(username=username, password_hash=password)
	db.session.add(user)
	db.session.commit()

	click.echo("Added user: " + username)
