import cherrypy
from amadaa.base import Controller
from amadaa.auth import login_required

class DashboardController(Controller):
    @cherrypy.expose
    @login_required
    def index(self):
        return self.render_template('dashboard/dashboard.html')
