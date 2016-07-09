import datetime
import uuid
import amadaa.database
from psycopg2.extras import DictCursor, register_uuid
from amadaa.base import Model

register_uuid()

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

def get(self, id):
		conn = amadaa.database.connection()
		with conn:
			with conn.cursor(cursor_factory=DictCursor) as cur:
				cur.execute("""select * from am_user
				where user_pk = %s""", (id,))
				rec = cur.fetchone()
				self.id = rec['user_pk']
				self.username = rec['username']
				self.password = rec['password']
		conn.close()
