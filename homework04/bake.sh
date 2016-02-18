#!/bin/sh
#compiles code in the current directory

SUFFIXES=${SUFFIXES:-.c}
CC=${CC:-gcc}
CFLAGS=${CFLAGS:-'-std=gnu99 -Wall'}
VERBOSE=${VERBOSE:-0}

for i in $(find *$SUFFIXES); do
	$CC $CFLAGS $i -o $( basename -s $SUFFIXES $i )
	if [ $? != 0 ] 
	then
		echo "Compilation failed for $i. Terminating script..."
		exit 1
	fi
	if [ "$VERBOSE" = "1" ] 
	then
		echo "$CC $CFLAGS $i -o $( basename -s $SUFFIXES $i )"
	fi

done 
