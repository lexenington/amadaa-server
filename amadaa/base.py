import os
import uuid
import cherrypy
from jinja2 import Environment, FileSystemLoader

class Controller:
    def __init__(self):
        self.view_dir = os.path.join(os.getcwd(), 'views')

    def info(self, message):
        self._message('info', message)

    def warning(self, message):
        self._message('warning', message)

    def error(self, message):
        self._message('error', message)

    def _message(self, type, message):
        if not 'messages' in cherrypy.session:
            cherrypy.session['messages'] = []
        cherrypy.session['messages'].append((type, message))

    def render_template(self, tpl, template_vars={}):
        env = Environment(loader = FileSystemLoader(self.view_dir))
        t = env.get_template(tpl)
        try:
            template_vars['messages'] = cherrypy.session['messages']
        except:
            template_vars['messages'] = []
        cherrypy.session['messages'] = []
        return t.render(template_vars)

class Model:
    def __init__(self, id=None):
        self._attribs = { 'id': uuid.UUID }
        self.id = id

    def __getattr__(self, key):
        if key[0] == '_' or key in self._attribs:
         # XXX: don't really know why I need this here, but at times
         # I get stupid errors if I leave it out.
         try:
             return super.__getattr__(self, key)
         except:
             # TODO: appropriate exception class
             raise Exception("get: no such key")
         else:
             # TODO: appropriate exception class
             raise Exception("get: no such key")

    def __setattr__(self, key, value):
        if key[0] == '_':
         super.__setattr__(self, key, value)
        elif key in self._attribs:
            if value == None or isinstance(value, self._attribs[key]):
                super.__setattr__(self, key, value)
            else:
                # TODO: appropriate exception class
                raise Exception("set: incorrect value type")
        else:
            # TODO: appropriate exception class
            raise Exception("set: no such attribute")

    def save(self):
        if self.id == None:
            self._insert()
        else:
            self._update()

    def _insert(self):
        pass

    def _update(self):
        pass

class RootController:
    @cherrypy.expose
    def index(self):
        user = cherrypy.session.get('user')
        if user:
            raise cherrypy.HTTPRedirect("/dashboard")
        else:
            raise cherrypy.HTTPRedirect("/auth/login")
