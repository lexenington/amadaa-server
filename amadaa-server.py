#! /usr/bin/env python3

import signal
import amadaa.server

signal.signal(signal.SIGTERM, amadaa.server.sighandler)
signal.signal(signal.SIGINT, amadaa.server.sighandler)
amadaa.server.start()
