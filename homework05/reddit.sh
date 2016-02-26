#!/bin/sh
# reddit.sh
# Displays all the links on a given subreddit
# Author: Kat Herring

NOPT=10
SOPT=0
ROPT=0

while getopts n:rs name
do
	case $name in 
		n) NOPT=${OPTARG:-10};;
		r) ROPT=1 SOPT=0;;
		s) SOPT=1 ROPT=0;;		
		*) echo "Invalid arg" ;;
	esac
done

shift $(($OPTIND -1))

while ([ $1 ]) do
	if [ $SOPT -eq 1 ]
		then 
		curl -s http://www.reddit.com/r/$1/.json | python -m json.tool | grep -ioE "\"url\": \"https://.*\"" | grep -v "i.redditmedia" | cut -c 9- | rev | cut -c 2- | rev | sort | head -$NOPT
	elif [ $ROPT -eq 1 ]
		then
		curl -s http://www.reddit.com/r/$1/.json | python -m json.tool | grep -ioE "\"url\": \"https://.*\"" | grep -v "i.redditmedia" | cut -c 9- | rev | cut -c 2- | rev | shuf | head -$NOPT
	else 
	curl -s http://www.reddit.com/r/$1/.json | python -m json.tool | grep -ioE "\"url\": \"https://.*\"" | grep -v "i.redditmedia" | cut -c 9- | rev | cut -c 2- | rev | head -$NOPT
	fi
shift
done
