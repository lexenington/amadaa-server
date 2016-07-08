import amadaa.database

def authenticate(username, password):
	conn = amadaa.database.connection()
	with conn:
		with conn.cursor() as cur:
			cur.execute("""select user_pk from am_user
			where username = %s and password = %s""", (username, password))
			uid = cur.fetchone()
	conn.close()
	return uid

def login_required(f):
	def decorate(*args, **kwargs):
		if cherrypy.session.get('user'):
			return f(*args, **kwargs)
		else:
			raise cherrypy.HTTPRedirect('/auth/login')
	return decorate
