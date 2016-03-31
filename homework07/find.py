#! /usr/bin/env python

# find.py
#Author: Kat Herring
#partial re-implementation of find using python

import sys, os, re

args=''
executable = False
readable = False
writable = False
empty = False

def usage(status=0):
    print '''Usage: find.py directory [options]...

Options:

    -type [f|d]     File is of type f for regular file or d for directory

    -executable     File is executable and directories are searchable to user
    -readable       File readable to user
    -writable       File is writable to user

    -empty          File or directory is empty

    -name  pattern  Base of file name matches shell pattern
    -path  pattern  Path of file matches shell pattern
    -regex pattern  Path of file matches regular expression

    -perm  mode     File's permission bits are exactly mode (octal)
    -newer file     File was modified more recently than file

    -uid   n        File's numeric user ID is n
    -gid   n        File's numeric group ID is n'''.format(os.path.basename(sys.argv[0]))
    sys.exit(status)

if len(sys.argv) < 2:
	usage(1)

args = sys.argv[1:]
for index, arg in enumerate(args):
    if index == 0:
        #check if directory
        print arg
    if arg == '-executable':
        executable = True
    if arg == '-writable':
        writable = True
    if arg == '-readable':
        readable = True
    if arg == '-type':
        try:
            if args[index + 1] == ('f' or 'd'):
                ftype = args[index + 1]
            else: 
                print "Invalid argument: ", args[index + 1]
                ftype = 0
                usage(1)
        except:
            if not 'ftype' in locals():
                print "No option specified."
                usage(1)
    if arg == 'empty'
    
