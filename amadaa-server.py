#! /usr/bin/env python3

import os
import signal
import amadaa.server

os.chdir(os.path.dirname(os.path.abspath(__file__)))
signal.signal(signal.SIGTERM, amadaa.server.sighandler)
signal.signal(signal.SIGINT, amadaa.server.sighandler)
amadaa.server.start()
