#!/bin/sh
#Uses awk to parse contents of CCL Catalog Server
#Author: Kat Herring

URL=http://catalog.cse.nd.edu:9097/query.text

if [ $1 ]
	then
	URL=$1
fi


MACHINES=`curl -s $URL  | egrep "name" | awk '{ print $2 }' | uniq| wc -l`
CPUS=`curl -s $URL  | egrep "cpu" | awk '{ sum+=$2 } END {print sum}'`
PROLIFIC=`curl -s $URL  | egrep "type" | awk '{ print $2 }' | sort | uniq -c | sort -nr | head -1 | awk '{ print $2 }'`


echo "Total CPUs: $CPUS\nTotal Machines: $MACHINES\nMost Prolific Type: $PROLIFIC"
