from nerdtrivia import create_app
from nerdtrivia.model.db import db as _db

@pytest.fixture(scope='session')
def app():
	app = create_app({ 'SQLALCHEMY_DATABASE_URI': 'sqlite:///:memory:'})

	return app

@pytest.fixture(scope='session')
def db(app):
	_db.app = app
	_db.create_all()

@pytest.fixture(scope='function')
def session(db):
	connection = db.engine.connect()
	transaction = connection.begin()

	options = dict(bind=connection, binds={})
	session = db.create_scoped_session(options=options)

	db.session = session

	def teardown():
		transaction.rollback()
		connection.close()
		session.remove()

	request.addfinalizer(teardown)
	return session
