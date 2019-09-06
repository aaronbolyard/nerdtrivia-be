from nerdtrivia.model.user import User
from nerdtrivia.model import get_database
from sqlalchemy import func
from werkzeug.security import generate_password_hash, check_password_hash

CREATE_USER_RESULT_SUCCESS      = 0
CREATE_USER_RESULT_USER_EXISTS  = 1
CREATE_USER_RESULT_BAD_PASSWORD = 2

def get_user(email):
	return User.query.filter(func.lower(User.email) == func.lower(email)).first()

def does_user_exit(email):
	return not get_user(email) is None

def create_user(email, password):
	if does_user_exit(email):
		return CREATE_USER_RESULT_USER_EXISTS, None

	if not is_valid_password(password):
		return CREATE_USER_RESULT_BAD_PASSWORD, None

	db = get_database()

	password_hash = generate_password_hash(password)
	user = User(email=email, password_hash=password_hash)

	db.session.add(user)
	db.session.commit()

	return CREATE_USER_RESULT_SUCCESS, user

def is_valid_password(password):
	return len(password) >= 8
