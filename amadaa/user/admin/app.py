import cherrypy
from amadaa.base import Controller
from amadaa.user.app import get_all_users, delete_user, User, UserExistsError

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
            try:
                u = User(username=username, password=password)
                u.save()
                self.info('user %s created' % username)
                raise cherrypy.HTTPRedirect('/admin/user')
            except UserExistsError as e:
                self.error(e)
                raise cherrypy.HTTPRedirect('/admin/user/add')

    @cherrypy.expose
    @cherrypy.popargs('id')
    def delete(self, id, confirm=None, *args):
        u = User()
        u.get(id)
        if 'user_to_delete' not in cherrypy.session:
            cherrypy.session['user_to_delete'] = id
            raise cherrypy.HTTPRedirect('/admin/user/delete/{0}'.format(u.id))
        elif confirm == None:
            return self.render_template('user/confirm_delete.html', {'user': u})
        elif confirm == "1":
            delete_user(id)
            cherrypy.session.pop('user_to_delete')
            self.info('User {0} deleted'.format(u.username))
            raise cherrypy.HTTPRedirect('/admin/user')
        else:
            cherrypy.session.pop('user_to_delete')
            self.info("User delete cancelled")
            raise cherrypy.HTTPRedirect('/admin/user')

    @cherrypy.expose
    @cherrypy.popargs('id')
    def view(self, id):
        u = User()
        u.get(id)
        return self.render_template('/user/user_details.html', {'user': u})
