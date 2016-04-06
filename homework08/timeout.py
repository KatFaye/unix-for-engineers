#! /usr/bin/env python2.7

#timeout.py
#Author: Kat Herring
# executes command then waits for it to complete 
# terminates if not finished in time
import os, sys, time, getopt, signal, re

verbose = False
SECONDS = 10

def debug(message, *args):
	#print message formatted with args to sys.stderr
	if verbose:
		print message.format(*args)


def handler(signum, frame):
	os.kill(child, signal.SIGTERM)
	debug('Alarm Triggered after "{}" seconds!', SECONDS)
	raise OSError("Process has timed out.")

def usage(status=0):
    print '''Usage: timeout.py [-t SECONDS] command...

Options:

      -t SECONDS  Timeout duration before killing command (default is 10)
      -v          Display verbose debugging output.'''.format(os.path.basename(sys.argv[0]))
    sys.exit(status)
#parses options; command stored in args
try:
	opts, args = getopt.getopt(sys.argv[1:], "ht:v")

except getopt.GetoptError as err:
	print str(err)
	usage(1)
if len(sys.argv[1:]) < 1:
	print "No argument supplied."
	usage(1)

for o, a in opts:
	if o == "-v":
		verbose = True
	elif o == "-h":
		usage(1)
	elif o == "-t":
		SECONDS = int(a)
	else:
		print o

debug('Executing "{}" for at most {} seconds...', args[0], SECONDS)

try:
	debug('Forking...')
	child = os.fork()
except OSError as e:
	print "Unable to fork process."
	sys.exit(1)
if child == 0:
	#signal.alarm(SECONDS)
	debug('Execing...')
	os.execvp(args[0], args)
else: 
	debug('Enabling Alarm...')
	signal.signal(signal.SIGALRM, handler)
	signal.alarm(SECONDS)
	try:
		debug('Waiting...')
		exit = os.wait()
	except OSError:
		debug('Killing PID "{}"', child)
		os.kill(child, signal.SIGTERM)
		exit = os.wait()
	debug('Disabling alarm...')		
	signal.alarm(0)
	debug('Process "{}" terminated with exit status "{}"', exit[0], exit[1])

sys.exit(exit[1])