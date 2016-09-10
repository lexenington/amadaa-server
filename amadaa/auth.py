import os
import cherrypy
import bcrypt
from amadaa.base import Controller
import amadaa.database
from amadaa.user.app import open_user_session, close_user_session

def authenticate(username, password):
    conn = amadaa.database.connection()
    with conn:
        with conn.cursor() as cur:
            cur.execute("""select user_pk, password from am_user
            where username = %s and active='t' and deleted='f'""", (username,))
            user = cur.fetchone()
            if user == None:
                return None
            hashed_pw = user[1]

            if bcrypt.checkpw(password, hashed_pw):
                uid = user[0]
            else:
                uid = None
    conn.close()
    return uid

def login_required(f):
    def decorate(*args, **kwargs):
        if cherrypy.session.get('user'):
            return f(*args, **kwargs)
        else:
            raise cherrypy.HTTPRedirect('/auth/login')
    return decorate
    
class AuthController(Controller):
    @cherrypy.expose
    def login(self, username=None, password=None):
        if username == None and password == None:
            tvars = {}
            if 'auth_message' in cherrypy.session:
                tvars['auth_message'] = cherrypy.session.pop('auth_message')
            return self.render_template('auth/login.html', tvars)
        else:
            uid = authenticate(username, password)
            if uid == None:
                cherrypy.session['auth_message'] = 'Authentication failed'
                raise cherrypy.HTTPRedirect('/auth/login')
            else:
                cherrypy.session['user'] = uid
                open_user_session(uid)
                raise cherrypy.HTTPRedirect('/')

    @cherrypy.expose
    def logout(self):
        uid = cherrypy.session.pop('user')
        close_user_session()
        raise cherrypy.HTTPRedirect('/')
