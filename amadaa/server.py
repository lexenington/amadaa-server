import sys
import time

this = sys.modules[__name__]
this.running = False

def start():
	this.running = True
	while this.running:
		time.sleep(1)
	stop()
	
def stop():
	pass
	
def sighandler(signum, frame):
	this.running = False
	
