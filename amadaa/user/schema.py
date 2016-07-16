import uuid
import psycopg2.extras
import amadaa.database
from amadaa.schema import set_schema_version, has_schema_version
from amadaa.user.app import Role, User, rolename_exists, username_exists

conn = amadaa.database.connection()
if not has_schema_version(__package__):
	if not amadaa.database.table_exists('am_role'):
		with conn:
			with conn.cursor() as cur:
				cur.execute("""create table am_role(
				role_pk uuid,
				rolename varchar(40) not null,
				parent_fk uuid references am_role,
				primary key(role_pk),
				unique(rolename))""")
			
	if not amadaa.database.table_exists('am_user'):
		with conn:
			with conn.cursor() as cur:
				cur.execute("""
				create table am_user(
				user_pk uuid,
				username varchar(30),
				password varchar(40),
				date_created timestamp,
				active bool not null default 't',
				hidden bool not null default 'f',
				deletable bool not null default 't',
				deleted bool not null default 'f',
				primary key(user_pk),
				unique(username)
				)""")

	if not amadaa.database.table_exists('am_user_role'):
		with conn:
			with conn.cursor() as cur:
				cur.execute("""create table am_user_role(
					user_role_pk uuid,
					user_fk uuid,
					role_fk uuid,
					primary key(user_role_pk),
					unique(user_fk, role_fk)
				)""")

	set_schema_version(__package__, 1)

for rn in ('fruit', 'administrators'):
	if not rolename_exists(rn):
		r = Role(rolename=rn)
		r.save()
	
if not username_exists('amadaa'):
	u = User(username='amadaa', password='changeme', hidden=True, deletable=False)
	u.save()

conn.close()



