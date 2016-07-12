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
		self.username = None
		self.password = None
		self.date_created = None
		self.last_login = None
		self.active = None

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

	def get_by_username(self, username):
		conn = amadaa.database.connection()
		with conn:
			with conn.cursor(cursor_factory=DictCursor) as cur:
				cur.execute("""select * from am_user
				where username = %s""", (username,))
				rec = cur.fetchone()
				self.id = rec['user_pk']
				self.username = rec['username']
				self.password = rec['password']
				self.active = rec['active']
		conn.close()

	def _insert(self):
		conn = amadaa.database.connection()
		with conn:
			with conn.cursor() as cur:
				self.id = uuid.uuid4()
				cur.execute("""insert into am_user(user_pk, username, password, active)
				values(%s, %s, %s, %s)""", (self.id, self.username, self.password, self.active))
		conn.close()

	def _update(self):
		conn = amadaa.database.connection()
		with conn:
			with conn.cursor() as cur:
				cur.execute("""update am_user set username = %s, password = %s, active = %s
				where user_pk = %s""", (self.username, self.password, self.active, self.id))
		conn.close()

class UserDirectory:
	def __init__(self):
		pass
		
	def id_exists(self, uid):
		conn = amadaa.database.connection()
		with conn:
			with conn.cursor() as cur:
				cur.execute("select * from am_user where user_pk = %s", (uid,))
				rec = cur.fetchone()
				if rec:
					ret = True
				else:
					ret = False
		conn.close()
		return ret
	
	def username_exists(self, username):
		conn = amadaa.database.connection()
		with conn:
			with conn.cursor() as cur:
				cur.execute("select * from am_user where username = %s", (username,))
				rec = cur.fetchone()
				if rec:
					ret = True
				else:
					ret = False
		conn.close()
		return ret
