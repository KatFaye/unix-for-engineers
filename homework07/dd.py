#! /usr/bin/env python

# dd.py
#Author: Kat Herring
#partial re-implementation of dd using python

import sys, os, re

IF=0
OF=1
bs=512
count=sys.maxint
seek=0
skip=0
ret = 0
x=0

def usage(status=0):
    print '''Usage: dd.py options...

Options:

      if=FILE     Read from FILE instead of stdin
      of=FILE     Write to FILE instead of stdout

      count=N     Copy only N input blocks
      bs=BYTES    Read and write up to BYTES bytes at a time

      seek=N      Skip N obs-sized blocks at start of output
      skip=N      Skip N ibs-sized blocks at start of input'''.format(os.path.basename(sys.argv[0]))
    sys.exit(status)

for arg in sys.argv[1:]:
	arg = re.sub('[^A-Za-z0-9=./]+', '', arg)
	if '=' in arg:
		o, a = arg.split('=')
		if o == 'if':
			IF = a
		elif o == 'of':
			OF = a
		elif o == 'count':
			count = int(a)
		elif o == 'bs':
			bs = int(a)
		elif o == 'seek':
			seek = int(a)
		elif o == 'skip':
			skip = int(a)
		else:
			print "Invalid argument."
			usage(1)
	else:
		print "Invalid argument."
		usage(1)

skip = int(skip) * int(bs)
seek = int(seek) * int(bs)
 
if IF != 0:
	IF = os.open(IF, os.O_RDONLY)
	os.lseek(IF, skip, 0)
if OF != 1:
	OF = os.open(OF, os.O_WRONLY|os.O_CREAT)
	os.lseek(OF, seek, 0)
i = 0
while int(i) < int(count):
	copy = os.read(IF, bs)
	if copy == "":
		break
	os.write(OF, copy)
	i += 1

os.close(IF)
os.close(OF)
