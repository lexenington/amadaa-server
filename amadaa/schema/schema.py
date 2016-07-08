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
