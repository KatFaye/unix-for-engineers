
#! python

# uniq.py
# $ ./uniq.py -h
#usage: uniq.py [-c] files ...

#-c      prefix lines by the 
# number of occurrence   

import sys, getopt, os

PREFIX = False
# Usage function

def usage(status=0):
    print '''usage: uniq.py [-c] files ...

-c      prefix lines by the number of occurrences'''.format(os.path.basename(sys.argv[0]))
    sys.exit(status)

# Parse command line options

try:
    opts, args = getopt.getopt(sys.argv[1:], "hc")
except getopt.GetoptError as e:
    print e
    usage(1)

for o, a in opts:
    if o == '-c':
        PREFIX = True
    else:
        usage(1)

if len(args) == 0:
    args.append('-')

for path in args:
	if path == '-':
		stream = sys.stdin
	else:
		stream = open(path)

	uniq_dict = dict()
	for line in stream:
		line = line.rstrip()
		uniq_dict[line] = uniq_dict.get(line,0) + 1

	for key,value in uniq_dict.iteritems(): 
		if PREFIX:
			print '%i ' % value,
		print key