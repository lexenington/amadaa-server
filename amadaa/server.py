import sys
import time
import schedule

this = sys.modules[__name__]
this.running = False

def start():
	this.running = True
	while this.running:
		schedule.run_pending()
		time.sleep(1)
	stop()
	
def stop():
	pass
	
def sighandler(signum, frame):
	this.running = False
	
