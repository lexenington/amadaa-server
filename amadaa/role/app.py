import uuid
import amadaa.database
from psycopg2.extras import DictCursor, register_uuid
from amadaa.base import Model

class Role(Model):
	def __init__(self):
		super().__init__()
		self._attribs.update({
			'rolename': str,
			'parent': uuid.UUID
		})
		self.rolename = None
		self.parent = None
		
	def get(self, id):
		conn = amadaa.database.connection()
		with conn:
			with conn.cursor(cursor_factory=DictCursor) as cur:
				cur.execute("""select * from am_role
				where role_pk = %s""", (id,))
				rec = cur.fetchone()
				self.id = rec['role_pk']
				self.rolename = rec['rolename']
				self.parent = rec['parent']
		conn.close()
		
	def get_by_rolename(self, rolename):
		conn = amadaa.database.connection()
		with conn:
			with conn.cursor(cursor_factory=DictCursor) as cur:
				cur.execute("""select * from am_role
				where rolename = %s""", (rolename,))
				rec = cur.fetchone()
				self.id = rec['role_pk']
				self.rolename = rec['rolename']
				self.parent = rec['parent']
		conn.close()
		
	def _insert(self):
		conn = amadaa.database.connection()
		with conn:
			with conn.cursor() as cur:
				self.id = uuid.uuid4()
				cur.execute("""insert into am_role(role_pk, rolename, parent)
				values(%s, %s, %s)""", (self.id, self.rolename, self.parent))
		conn.close()
		
	def _update(self):
		conn = amadaa.database.connection()
		with conn:
			with conn.cursor() as cur:
				cur.execute("""update am_role set rolename = %s, parent = %s
				where role_pk = %s""", (self.rolename, self.parent, self.id))
		conn.close()
