#! /usr/bin/env python2.7

#NOTE THAT I USED ECHO_CLIENT as a base
#Also, I was unable to get the range-based find working for this, so I used another script (portScanner.py) to find the open port, and then ran this with the correct IP address and port number...

#Unix Utility: mv. Basic teleportation
#Favorite part: Networks, though you couldn't tell based on how well I did on that portion of the class
#Least favorite part: This test. Mostly because I'm terrible at debugging things in a timely manner. Nothing against your test-writing skills. 

#Author: Kat Herring
#Date : 5/5/16
import getopt
import logging
import os
import socket
import sys

# Constants

ADDRESS  = '127.0.0.1'
LPORT    = 9700
UPORT    = 9799
PORT 	 = 9755
PROGRAM  = os.path.basename(sys.argv[0])
LOGLEVEL = logging.INFO

# Utility Functions

def usage(status=0):
    print '''Usage: timeout.py [-r RANGE] hostname...

Options:

        -r       RANGE  Range of ports to scan. Default 1025-9999 
        -h          Display this help message.'''.format(os.path.basename(sys.argv[0]))
    sys.exit(status)

# TCPClient Class

class TCPClient(object):

    def __init__(self, address=ADDRESS, port=PORT):
        ''' Construct TCPClient object with the specified address and port '''
        self.logger  = logging.getLogger()                              # Grab logging instance
        self.socket  = socket.socket(socket.AF_INET, socket.SOCK_STREAM)# Allocate TCP socket
        self.address = address                                          # Store address to listen on
        self.port    = port                                             # Store port to lisen on

    def handle(self):
        ''' Handle connection '''
        self.logger.debug('Handle')
        raise NotImplementedError

    def run(self):
        ''' Run client by connecting to specified address and port and then
        executing the handle method '''
        try:
            # Connect to server with specified address and port, create file object
            self.socket.connect((self.address, self.port))
            self.stream = self.socket.makefile('w+')
        except socket.error as e:
            self.logger.error('Could not connect to {}:{}: {}'.format(self.address, self.port, e))
            sys.exit(1)

        self.logger.debug('Connected to {}:{}...'.format(self.address, self.port))

        # Run handle method and then the finish method
        try:
            self.handle()
        except Exception as e:
            self.logger.exception('Exception: {}', e)
        finally:
            self.finish()

    def finish(self):
        ''' Finish connection '''
        self.logger.debug('Finish')
        try:
            self.socket.shutdown(socket.SHUT_RDWR)
        except socket.error:
            pass    # Ignore socket errors
        finally:
            self.socket.close()

# EchoClient Class

class EchoClient(TCPClient):
    def handle(self):
        ''' Handle connection by reading data and then writing it back until EOF '''
        self.logger.debug('Handle')

        try:
            data = sys.stdin.readline()
            while data:
                # Send STDIN to Server
                self.stream.write(data)
                self.stream.flush()

                # Read from Server to STDOUT
                data = self.stream.readline()
                sys.stdout.write(data)

                # Read from STDIN
                data = sys.stdin.readline()
        except socket.error:
            pass    # Ignore socket errors

# Main Execution

if __name__ == '__main__':
    # Parse command-line arguments
#parses options; command stored in args
    try:
            opts, args = getopt.getopt(sys.argv[1:], "hr:v")

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
            elif o == "-v":
                    LOGLEVEL = logging.debug
            else:
                    print o
                    usage(1)
    #if len(args) > 0:
            #ADDRESS = args[0]
    #convert host to IP address
    #IP = socket.gethostbyname(HOST)

    if len(args) >= 1:
            ADDRESS = args[0]
    if len(args) >= 2:
            PORT    = int(args[1])

        # Set logging level
    logging.basicConfig(
            level   = LOGLEVEL,
            format  = '[%(asctime)s] %(message)s',
            datefmt = '%Y-%m-%d %H:%M:%S',
        )

        # Lookup host address
    try:
            ADDRESS = socket.gethostbyname(ADDRESS)
    except socket.gaierror as e:
            logging.error('Unable to lookup {}: {}'.format(ADDRESS, e))
            sys.exit(1)

        # Instantiate and run clien
    client = EchoClient(ADDRESS, PORT)
    try:
	    client.run()
    except KeyboardInterrupt:
            sys.exit(0)
