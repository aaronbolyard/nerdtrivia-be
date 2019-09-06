from nerdtrivia.controller.user import (
	create_user, get_user,

	CREATE_USER_RESULT_SUCCESS,
	CREATE_USER_RESULT_USER_EXISTS,
	CREATE_USER_RESULT_BAD_PASSWORD
)
from werkzeug.security import check_password_hash

from nerdtrivia.model.user import User

def test_should_create_user(app, session):
	result, user = create_user('jsmit@example.com', 'password1234@')

	assert result == CREATE_USER_RESULT_SUCCESS
	assert user.email == 'jsmit@example.com'
	assert check_password_hash(user.password_hash, 'password1234@')
	assert not get_user('jsmit@example.com') is None

def test_should_not_create_dupe_users(app, session):
	result1, user1 = create_user('jsmit@example.com', 'password1234@')
	result2, user2 = create_user('jsmit@example.com', 'password1234@')

	assert result1 == CREATE_USER_RESULT_SUCCESS
	assert result2 == CREATE_USER_RESULT_USER_EXISTS
	assert not user1 is None
	assert user2 is None

def test_should_not_create_user_with_weak_password(app, session):
	result, user = create_user('jsmit@example.com', 'weak')

	assert result == CREATE_USER_RESULT_BAD_PASSWORD
	assert user is None
