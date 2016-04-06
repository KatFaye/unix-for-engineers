#! /usr/bin/env python2.7

#rorschach.py
#monitors a series of directories for changes
#Author: Kat Herring

import os, sys, getopt, yaml, glob, re, fnmatch, shlex, time

SECONDS = 2
RULES = ".rorschach.yml"
VERBOSE = False
DIRECTORIES = "."
START_TIME = int(time.time()) #program begins execution


def debug(message, *args):
	#print message formatted with args to sys.stderr
	if VERBOSE:
		print message.format(*args)

def usage(status=0):
    print '''Usage: rorschach.py [-r RULES -t SECONDS] DIRECTORIES...

Options:

    -r RULES    Path to rules file (default is .rorschach.yml)
    -t SECONDS  Time between scans (default is 2 seconds)
    -v          Display verbose debugging output
    -h          Show this help message'''.format(os.path.basename(sys.argv[0]))
    sys.exit(status)

def check_directory(rules):
	#walks specified directory and checks if file matches rule
	
	for rule in rules:
		debug('Checking "{}" directories for "{}"...', DIRECTORIES, rule['pattern'])
		for directory in DIRECTORIES:
			debug('Checking "{}"...', directory)
			for root, dirs, files in os.walk(directory):
				for name in files:
					path = os.path.join(root, name)
					debug('Checking "{}" file...', name)
					check_file(path, rule)

def check_file(path, rule):
	#checks each file to see if matches rules before execution
	debug('Checking "{}" for pattern matches...', path)
	#split back again to check name
	name = path.rsplit('/', 1)
	#check glob
	if fnmatch.fnmatch(name[1], rule['pattern']):
		#check if file modified since program began
		if int(os.path.getmtime(path)) > START_TIME:
			execute_action(path, rule)
		elif int(os.path.getctime(path)) > START_TIME:
			execute_action(path, rule)
	#check regular expression
	elif re.search(rule['pattern'], name[1]):
		if int(os.path.getmtime(path)) > START_TIME:
			execute_action(path, rule)
		elif int(os.path.getctime(path)) > START_TIME:
			execute_action(path, rule)
def execute_action(name, rule):
	try:
		debug('Forking to scan file...')
		child = os.fork()
	except OSError as e:
		print "Unable to fork process."
		sys.exit(1)

	if child == 0:

		debug('Executing "{}"...', rule['action'])
		action = rule['action'].format(path=os.path.abspath(name), name=os.path.basename(name))
		lex = shlex.split(action)
		#expand variables
		os.execvp(lex[0], lex)
	else:
		os.wait()

try:
	opts, args = getopt.getopt(sys.argv[1:], "r:t:vh")

except getopt.GetoptError as err:
	print str(err)
	usage(1)
if len(sys.argv[1:]) < 1:
	print "No directories supplied."
	usage(1)

for o, a in opts:
	if o == '-h':
		usage(1)
	elif o == '-t':
		SECONDS = a
	elif o == '-v':
		VERBOSE = True
	elif o == '-r':
		RULES = a

if len(args) > 0:
	DIRECTORIES = args
#convert yaml to list of dictionaries
try:
	stream = file(RULES, 'r')
	rules = yaml.load(stream)
except:
	print "File does not exist."
	sys.exit(1)

while True:
	time.sleep(SECONDS)
	check_directory(rules)
	#updates time since last program executation
	START_TIME = int(time.time())
