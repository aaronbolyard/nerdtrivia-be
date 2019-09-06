from nerdtrivia.model.db import db

class User(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	# Max email length is 254 characters: see RFC 2821
	email = db.Column(db.String(length=255), nullable=False, unique=True)
	password_hash = db.Column(db.String(length=255), nullable=False)

	def serialize(self):
		return {
			'id': self.id,
			'email': self.email
		}
