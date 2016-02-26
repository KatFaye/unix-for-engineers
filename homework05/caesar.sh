#!/bin/sh
# casesar.sh: Implements Caesar cipher on inputted text.
#Author: Kat Herring

NOPT=13 #default Caesar shift
ALPHA=abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz
SIZE=25 #num char in alphabet - 1

if [ "$1" = "-h" ]
	then 
	echo "usage: caesar.sh [rotation]

This program will read from stdin and rotate (shift right) the text by
the specified rotation.  If none is specified, then the default value is 13."

	exit 0

elif [ $1 ]
	then 
	if [ "$1" -eq "$1" ]
 		then NOPT=$1
	fi
fi

NOPT=$(( NOPT + 1 ))
if [ "$NOPT" -gt "26" ]
	then 
		NOPT=$(( NOPT % 26 ))
fi
END=$(( NOPT + SIZE ))

ROTATE=$(echo $ALPHA | cut -c $NOPT-$END)
ROTATEUPPER=$(echo $ALPHA | tr 'a-z' 'A-Z' | cut -c $NOPT-$END)

cat | tr 'a-zA-Z' $ROTATE$ROTATEUPPER
