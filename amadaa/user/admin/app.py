import cherrypy
from amadaa.base import Controller
from amadaa.user.app import get_all_users, delete_user, User

class UserAdminController(Controller):
    @cherrypy.expose
    def index(self):
        tvars = {
            'users': get_all_users()
        }
        return self.render_template('user/user_list.html', tvars)

    @cherrypy.expose
    @cherrypy.popargs('id')
    def edit(self, foo):
        return "The id is %s" % foo

    @cherrypy.expose
    def add(self, username=None, password=None):
        if username == None and password == None:
            return self.render_template('user/edit_user.html')
        else:
            u = User(username=username, password=password)
            u.save()
            self.info('user %s created' % username)
            raise cherrypy.HTTPRedirect('/admin/user')
