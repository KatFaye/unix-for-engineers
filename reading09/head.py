#! python

# head.py

import sys, getopt, os

NUM = 10
count = 0

# Usage function

def usage(status=0):
    print '''usage: head.py [-n NUM] files ...

    -n NUM  print the first NUM lines instead of the first 10'''.format(os.path.basename(sys.argv[0]))
    sys.exit(status)

# Parse command line options

try:
    opts, args = getopt.getopt(sys.argv[1:], "hn:")
except getopt.GetoptError as e:
    print e
    usage(1)

for o, a in opts:
    if o == '-n':
        NUM = a

    else:
        usage(1)

if len(args) == 0:
    args.append('-')

for path in args:
	if path == '-':
		stream = sys.stdin
	else:
		stream = open(path)

	for line in stream:
		line = line.rstrip()
		count = count + 1
		if count <= int(NUM):
			print line

