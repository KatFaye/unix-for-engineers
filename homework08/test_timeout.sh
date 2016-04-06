#!/bin/sh
#test_timeout.sh
#verify the correctness of timeout.py

#verify executable

FILE='./timeout.py'

if (! [ -x "$FILE" ] )
then
	echo "Test failed - not an executable."
	exit 1

fi

#verify python2.7 in she-bang
if (! grep -q 'python2.7' $FILE ) then
	echo "Test failed - incorrect she-bang."
	exit 1
fi

#verify reasonable STDERR print with -h flag

./timeout.py -h | grep -ie "usage" 

if [ $? != 0 ]
then
	echo "Test failed - help statement"
	exit 1
fi

#verify that timeout.py exits with success when n = 1-4
for i in $(seq 1 4); do
	$FILE -t 5 sleep $i

	if  [ $? != 0 ]
	then
		echo "Test failed - unsuccessful exit."
		exit 1
	fi
done

for i in `seq 2 5`
do
	$FILE -t 1 sleep $i
	if [ $? = 0 ]
	then
		echo "Test failed - did not kill process."
		exit 1
	fi
done

#verify reasonable debugging messages

./timeout.py -v -t 5 sleep 1 | grep -ie "Forking" -ie "exit" -ie "alarm"

if [ $? != 0 ]
then
	echo "Test failed - verbose flag."
	exit 1
fi

echo "$FILE test successful!"