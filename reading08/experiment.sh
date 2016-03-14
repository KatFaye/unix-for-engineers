#!/bin/sh
# simulates 1000 dice rolls and aggregates output using awk
#Author: Kat Herring

./roll_dice.sh -r 1000 | awk -v OFS="\t" '{ results[$1]++ } END { 
	for(i=1; i<=6; i++)
		print(i, results[i])
}' > results.dat
