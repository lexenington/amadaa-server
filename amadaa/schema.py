import amadaa.database

def setup():
	conn = amadaa.database.connection()
	print("checking if versions table exists")
	if not amadaa.database.table_exists('am_schema_version'):
		with conn:
			with conn.cursor() as cur:
				cur.execute("""
				create table am_schema_version(
				schema_version_pk serial,
				app varchar(40) not null,
				version int not null,
				primary key(schema_version_pk),
				unique(app)
				)""")
	conn.close()

def get_schema_version(app):
	""" Get the current version of a app or None if the app is
	not in the schema versions table. """
	conn = amadaa.database.connection()
	with conn:
		with conn.cursor() as cur:
			cur.execute("""select version from am_schema_version
			where app = %s""", (app,))
			ver = cur.fetchone()
	conn.close()
	return ver

def set_schema_version(app, version=1):
	conn = amadaa.database.connection()
	with conn:
		with conn.cursor() as cur:
			if version == 1:
				cur.execute("""insert into am_schema_version(app, version)
				values(%s, %s)""", (app, version))
			else:
				cur.execute("""update am_schema_version set version = %s
				where app = %s""", (version, app))
				
	
