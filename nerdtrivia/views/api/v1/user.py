from flask import request
from flask_restful import Resource

from nerdtrivia.controller.user import (
	create_user,

	CREATE_USER_RESULT_SUCCESS,
	CREATE_USER_RESULT_USER_EXISTS,
	CREATE_USER_RESULT_BAD_PASSWORD
)

class User(Resource):
	def put(self):
		json = request.get_json()

		email = json.get('email', None)
		password = json.get('password', None)

		result, user = create_user(email, password)

		if result == CREATE_USER_RESULT_SUCCESS:
			return { 'status': 'CREATE_USER_RESULT_SUCCESS' }, 201
		else:
			if result == CREATE_USER_RESULT_BAD_PASSWORD:
				return { 'status': 'CREATE_USER_RESULT_BAD_PASSWORD' }, 400
			elif result == CREATE_USER_RESULT_USER_EXISTS:
				return { 'status': 'CREATE_USER_RESULT_USER_EXISTS' }, 400


from nerdtrivia.views.api.main import rest
rest.add_resource(User, '/api/v1/user')
