#!/usr/bin/python2

import sys
from network_utils import *

def _print_usage(errorMsg=""):
    if errorMsg:
        print errorMsg

    print "Run in server mode: netmsg.py <portnum>"
    print "Run in client mode: netmsg.py <server> <portnum>"

def _print_port_instuctions():
    print "ERROR: Port number should be between 1024 and 65535\n"

def _get_args():
    """Gets the arguments passed from the command line.

    Gets all of the the

    Returns:
        A two element tuple containing the provided command line arguments in
        the format: (server, port). If any of the arguments were not provided
        they will be None.
    """
    numArgs = len(sys.argv)

    if numArgs == 2:
        return None, sys.argv[1]
    elif numArgs == 3:
        return sys.argv[1], sys.argv[2]
    else:
        return None, None

def _run_server(port):
    socket, error = get_udp_socket(port)

    if (socket):
        print "IP Address: ".join(str(socket.getsockname()[0]))

def _run_client(server, port):
    pass

print "=========================================="
print "Network Messaging Tool:"
print "Sends messages over the network via UDP."
print "==========================================\n"

# read the arguments and run server or client version
server, port = _get_args()
port = parse_and_validate_port(port)

if not port:
    _print_port_instuctions()
    _print_usage()
    sys.exit(1)

if server:
    # a server was specified, run in client mode
    _run_client(server, port)

elif port:
    # no server was specified, run in server mode
    _run_server(port)

else:
    _print_usage()
    sys.exit(1)