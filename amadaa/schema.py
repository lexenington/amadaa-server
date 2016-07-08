import amadaa.database

conn = amadaa.database.connection()

print("checking if versions table exists")
if not amadaa.database.table_exists('am_schema_version'):
	with conn:
		with conn.cursor() as cur:
			cur.execute("""
			create table am_schema_version(
			schema_version_pk serial,
			module varchar(40) not null,
			version int not null,
			primary key(schema_version_pk),
			unique(module)
			)""")
			
conn.close()

def get_schema_version(module):
	""" Get the current version of a module or None if the module is
	not in the schema versions table. """
	conn = amadaa.database.connection()
	with conn:
		with conn.cursor() as cur:
			cur.execute("""select version from am_schema_version
			where module = %s""", (module))
			ret = cur.fetchone()
	conn.close()
	return ret

def set_schema_version(module, version=1):
	conn = amadaa.database.connection()
	with conn:
		with conn.cursor() as cur:
			if version == 1:
				cur.execute("""insert into am_schema_version(module, version)
				values(%s, %s)""", (module, version))
			else:
				cur.execute("""update am_schema_version set version = %s
				where module = %s""", (version, module))
