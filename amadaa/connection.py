import sys
import socket

this = sys.modules[__name__]
this.state = None
this.observers = []

def check_internet_connection():
    """ Check if we are connected to the Internet and inform observers
    of any change in connectivity. """
    try:
    	socket.setdefaulttimeout(3)
    	socket.socket(socket.AF_INET, socket.SOCK_STREAM).connect(("8.8.8.8", 53))
    	newstate = True
    except:
    	newstate = False
    if not newstate == this.state:
    	for ob in observers:
    		ob(newstate)
    this.state = newstate	
    
def add_observer(ob):
    """ Add an observer.
    :param ob: the function to be called if internet connectivity goes up/down. """
    if callable(ob):
    	this.observers.append(ob)
