from flask_restful import Api

rest = Api()

def init_app(app):
	rest.init_app(app)
