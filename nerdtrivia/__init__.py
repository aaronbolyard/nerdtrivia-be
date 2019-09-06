import os

from flask import Flask

def create_app(test_config=None):
	app = Flask(__name__, instance_relative_config=True)
	app.config.from_mapping(
		SQLALCHEMY_TRACK_MODIFICATIONS=False,
		SQLALCHEMY_COMMIT_ON_TEARDOWN=True,
		SECRET_KEY=os.environ.get('NT_FLASK_SECRET_KEY', None),
		SQLALCHEMY_DATABASE_URI=os.environ.get('NT_SQLALCHEMY_DATABASE_URI', None),
	)

	import nerdtrivia.model as model
	model.init_app(app)

	return app
