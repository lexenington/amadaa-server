import uuid
import psycopg2.extras
import amadaa.database
from amadaa.schema import set_schema_version

conn = amadaa.database.connection()

if not amadaa.database.table_exists('am_user'):
	with conn:
		with conn.cursor() as cur:
			cur.execute("""
			create table am_user(
			user_pk uuid,
			username varchar(30),
			password varchar(40),
			date_created timestamp,
			last_login timestamp,
			active bool, 
			primary key(user_pk),
			unique(username)
			)""")
	set_schema_version(__package__, 1)
	
# XXX: temporary
try:
	with conn:
		with conn.cursor() as cur:
			psycopg2.extras.register_uuid()
			cur.execute("""insert into am_user(user_pk, username, password, active)
			values(%s, %s, %s, %s)""", (uuid.uuid4(), 'lorenzo', 'foo', True))
except Exception as e:
	print(e)
	
conn.close()




