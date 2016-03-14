#!/bin/sh
# simulates a random dice roll using the shuf command
#Author: Kat Herring

SOPT=6
ROPT=10

	while getopts s:r:h opt
	do 
		case $opt in 
			r) ROPT=${OPTARG:-10};;
			s) SOPT=${OPTARG:-6};;
			h|*)  echo  "usage: roll_dice.sh [-r ROLLS -s sides]

    -r ROLLS        Number of rolls of die (default: 10)
    -s SIDES        Number of sides on die (default: 6)"

	exit 0;;
		esac
	done

shift $(($OPTIND -1))

for i in `seq 1 $ROPT`
do
	shuf -i 1-$SOPT -n 1
done
