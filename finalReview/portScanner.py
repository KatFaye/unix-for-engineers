#! /usr/bin/env python2.7

#test port scanner for oracle assignment
#Author: Kat Herring
# Date 5/3/16

#!/usr/bin/env python
import socket, getopt, subprocess, sys

HOST = 'localhost'
LBOUND = 1025
UBOUND = 9999

def usage(status=0):
    print '''Usage: timeout.py [-r RANGE] hostname...

Options:

	-r	 RANGE	Range of ports to scan. Default 1025-9999 
	-h          Display this help message.'''.format(os.path.basename(sys.argv[0]))
    sys.exit(status)
#parses options; command stored in args
try:
	opts, args = getopt.getopt(sys.argv[1:], "hr:")

except getopt.GetoptError as err:
	print str(err)
	usage(1)
# specify ports

for o, a in opts:
	if o == "-r":
		a = a.split('-')
		#print a
		LBOUND = int(a[0])
		UBOUND = int(a[1])
	elif o == "-h":
		usage(1)
	else:
		print o

if len(args) > 0:
	HOST = args[0]
#convert host to IP address
IP = socket.gethostbyname(HOST)
print IP

try:
    for port in range(LBOUND,UBOUND):  
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	   
	result = sock.connect_ex((IP, port))
        if result == 0:
            print "Port {}: 	 Open".format(port)
	sock.settimeout(2.0)
        sock.close()

except socket.gaierror:
    print 'Hostname could not be resolved. Exiting'
    sys.exit()

except socket.error:
    print "Couldn't connect to server"
    sys.exit()

except socket.timeout:
	print "Error: Timed out during scan"
	sys.exit()
