#!/usr/bin/env python

import sys
import time
import urllib2
from wsgiref.simple_server import make_server, demo_app

def forever():
    httpd = make_server('', 8000, demo_app)
    print "Serving HTTP (fovever) on port 8000..."
    # Respond to requests until process is killed
    httpd.serve_forever()

def once():
    httpd = make_server('', 8000, demo_app)
    print "Serving HTTP (once) on port 8000..."
    # Alternative: serve one request, then exit
    httpd.handle_request()

def ping():
    while True:
        print time.time()
        try:
            print urllib2.urlopen('http://localhost:8000',timeout=.5).read().split('\n')[0]
            sys.stdout.flush()
        except urllib2.URLError, exc:
            print exc

        time.sleep(2)

if __name__ == "__main__":
    import sys
    action = sys.argv[1]
    actions = dict(ping=ping,once=once,forever=forever)
    if action not in actions:
        sys.exit('choose one of %s' % ('|'.join(actions)),)
    actions[action]()
