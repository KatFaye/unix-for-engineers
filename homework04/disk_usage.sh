#!/bin/sh
#given a directory, lists 'n' largest files 

NOPT=10
AOPT=''

while getopts n:a name
do
	case $name in 
		n) NOPT=${OPTARG:-10};;
		a) AOPT=-a;;
		*) echo "Invalid arg" ;;
	esac
done

shift $(($OPTIND -1))

if [ $# = 0 ]; then
	echo "usage: disk_usage.sh [-a -n N] directory..."

else 
	while ([ $1 ]) do
		if [ -d $1 ]; then
			du $1 -h $AOPT  2>/dev/null | sort -hr | head -$NOPT
			shift	
		else
			echo "Error: '$1' usage: Must be a directory"
			shift
		fi
	done
fi

