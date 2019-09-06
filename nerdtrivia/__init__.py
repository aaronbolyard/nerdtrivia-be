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

	if not test_config is None:
		app.config.from_mapping(test_config)

	import nerdtrivia.model as model
	model.init_app(app)

	import nerdtrivia.views.api.v1.user
	from nerdtrivia.views.api.main import init_app as init_api
	init_api(app)

	return app
