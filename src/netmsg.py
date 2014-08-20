#!/usr/bin/python2

import sys
import network_utils

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
    pass

def _run_client(server, port):
    pass

print "=========================================="
print "Network Messaging Tool:"
print "Sends messages over the network via UDP."
print "==========================================\n"

# read the arguments and run server or client version
server, port = _parse_args()

if server:
    # a server was specified, run in client mode
    port = network_utils.parse_and_validate_port(port)
    if not port:
        _print_port_instuctions()
        _print_usage()
        sys.exit(1)
    
    _run_client(server, port)

elif port:
    # no server was specified, run in server mode
    port = network_utils.parse_and_validate_port(port)
    if not port:
        _print_port_instuctions()
        _print_usage()
        sys.exit(1)
    
    _run_server(port)

else: 
    _print_usage()
    sys.exit(1)