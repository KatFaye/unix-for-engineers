#!/bin/bash
# Prints Hello for each cmd argument passed to script 

while [ "$1" != "" ]; do 
echo Hello $1
shift
done
