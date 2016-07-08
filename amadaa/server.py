import sys
import os
import time
import schedule
import cherrypy
import logging
import amadaa.connection
import amadaa.node
from amadaa.root import RootController
from amadaa.auth import AuthController
from amadaa.dashboard.app import DashboardController

this = sys.modules[__name__]
this.running = False
this.logger = logging.getLogger(__name__)
this.logger.setLevel(logging.INFO)
ch = logging.StreamHandler()
formatter = logging.Formatter('%(asctime)-15s : %(name)-15s : %(levelname)-6s : %(message)s')
ch.setFormatter(formatter)
this.logger.addHandler(ch)

def start():
	this.running = True
	this.logger.info('amadaa server starting')
	amadaa.connection.add_observer(amadaa.node.connection_change)
	schedule.every(1).minutes.do(amadaa.connection.check_internet_connection)
	cherrypy.config.update({
		'tools.sessions.on': True,
		'tools.sessions.storage_type': 'ram'
	})
	cherrypy.tree.mount(RootController(), "/", {
		'/static': {
			'tools.staticdir.on': True,
			'tools.staticdir.dir': os.path.join(os.getcwd(), 'static')
		}
	})
	cherrypy.tree.mount(AuthController(), "/auth")
	cherrypy.tree.mount(DashboardController(), "/dashboard")
	cherrypy.engine.start()
	this.logger.info('amadaa server started')
	while this.running:
		schedule.run_pending()
		time.sleep(1)
	stop()
	
def stop():
	this.logger.info('amadaa server shutting down')
	cherrypy.engine.exit()
	this.logger.info('amadaa server shutdown complete')
	
def sighandler(signum, frame):
	this.running = False
	
