import sys
import time
import schedule
import cherrypy
import amadaa.connection
import amadaa.node
from amadaa.root.controller import RootController

this = sys.modules[__name__]
this.running = False

def start():
	this.running = True
	amadaa.connection.add_observer(amadaa.node.connection_change)
	schedule.every(1).minutes.do(amadaa.connection.check_internet_connection)
	cherrypy.tree.mount(RootController(), "/")
	cherrypy.engine.start()
	while this.running:
		schedule.run_pending()
		time.sleep(1)
	stop()
	
def stop():
	cherrypy.engine.exit()
	
def sighandler(signum, frame):
	this.running = False
	
