#!/bin/sh
# broify.sh
# "bro-ifies" script- removes comments and whitespace
# Author: Kat Herring

DOPT='#'
WOPT=0
while getopts d:Wh name
do
	case $name in 
		d) DOPT=$OPTARG;;
		W) WOPT=1;;	
		h) echo "usage: broify.sh

  -d DELIM    Use this as the comment delimiter.
  -W          Don not strip empty lines.";;	
		*) echo "Invalid arg" ;;
	esac
done

if [ $WOPT -eq 0 ];
        then
        cat | sed "s|$DOPT.*$||" | sed 's|[ \t]*$||'| sed '/^$/d'
else
       cat | sed "s|$DOPT.*$||" | sed 's|[ \t]*$||'
fi 
