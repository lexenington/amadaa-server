import datetime
import uuid
import amadaa.database
from amadaa.base import Model

class User(Model):
	def __init__(self, id=None):
		super().__init__()
		self._attribs.update({
			'username': str,
			'password': str,
			'date_created': datetime,
			'last_login': datetime,
			'active': bool
		})
