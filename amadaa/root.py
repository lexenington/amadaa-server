import cherrypy

class RootController:
	@cherrypy.expose
	def index(self):
		user = cherrypy.session.get('user')
		if user:
			raise cherrypy.HTTPRedirect("/dashboard")
		else:
			raise cherrypy.HTTPRedirect("/auth/login")
