#!/bin/sh
# Uses awk to implement own version of head filter
#Author: Kat Herring

NOPT=10

	while getopts n:h opt
	do 
		case $opt in 
			n) NOPT=${OPTARG:-10};;
			h)  echo  "usage: head.sh

      -n N    Display the first N lines"

	exit 0;;
			*) echo "Invalid argument." ;;
		esac
	done

shift $(($OPTIND -1))

NPLUS=$(( NOPT + 1 )) #adds one to number of options for awk command

cat | awk -v N="$NPLUS" 'NR < N'

