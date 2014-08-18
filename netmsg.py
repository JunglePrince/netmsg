#!/usr/bin/python2

import sys

def _print_usage():
    print "Run in server mode: netmsg.py <portnum>"
    print "Run in client mode: netmsg.py <server> <portnum>"

def _run_server(port):
    pass

def _run_client(server, port):
    pass

print "Network Messaging Tool: Sends messages over the network via UDP."

# read args and run server or client version
numArgs = len(sys.argv)

if numArgs < 2 or numArgs > 3:
    print_usage()
    sys.exit(1)

if len(sys.argv) == 2:
    port = sys.argv[1]
    run_server(port)
elif len(sys.argv) == 3:
    server = sys.argv[1]
    port = sys.argv[2]
    run_client(server, port)
