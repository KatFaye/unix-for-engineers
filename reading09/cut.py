#! python

# cut.py

import sys, getopt, os

DELIM = '\t'
FIELDS = -1

# Usage function

def usage(status=0):
    print '''usage: wc.py [-d DELIM -f] files ...

    -d DELIM  use DELIM instead of TAB for field delimiter
    -f FIELDS select only these FIELDS'''.format(os.path.basename(sys.argv[0]))
    sys.exit(status)

# Parse command line options

try:
    opts, args = getopt.getopt(sys.argv[1:], "d:f:")
except getopt.GetoptError as e:
    print e
    usage(1)

for o, a in opts:
    if o == '-f':
        FIELDS = a
    elif o == '-d':
        DELIM = a
    else:
        usage(1)

if FIELDS == -1:
    print "Must provide a field."
    usage(1)

if len(args) == 0:
    args.append('-')

for path in args:
	if path == '-':
		stream = sys.stdin
	else:
		stream = open(path)

for line in stream:
    line.rstrip()
    for field in FIELDS:
        if len(field) < len(line.split(DELIM)):
            line = line.split(DELIM)[int(field)-1]
    print line