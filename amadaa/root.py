import cherrypy

class RootController:
	@cherrypy.expose
	def index(self):
		return "This is the root controller"
