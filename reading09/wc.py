#! python

# wc.py

import sys, getopt, os

CHAR = False
LINE = False
WORD = False
lcount = 0
ccount = 0
wcount = 0
# Usage function

def usage(status=0):
    print '''usage: wc.py [-c -l -w] files ...

    -c      print the byte/character counts
    -l      print the newline counts
    -w      print the word counts'''.format(os.path.basename(sys.argv[0]))
    sys.exit(status)

# Parse command line options

try:
    opts, args = getopt.getopt(sys.argv[1:], "clw")
except getopt.GetoptError as e:
    print e
    usage(1)

if len(sys.argv) < 3:
    print "Must provide flag."
    usage(1)

for o, a in opts:
    if o == '-c':
        CHAR = True
    elif o == '-l':
        LINE = True
    elif o == '-w':
        WORDS = True
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
        line.rstrip()
        lcount += 1
        ccount += len(line)
        wcount += len(line.split())

if LINE:
    print lcount
elif CHAR:
    print ccount
else: 
    print wcount
