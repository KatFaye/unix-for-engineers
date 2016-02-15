TLDR - sh.md
==========

1) Variable usage
	To set a variable:
		myVariable="This is how you use a variable"
		To use a variable:
	$myVariable

2) capturing STDOUT
	To save the STDOUT of a given command:
		myCapture=(commandHere)
3) If statement
	Basic use:
		if [ "$1" = "Test comparison" ]
		then
			echo "Do the thing."
		fi
	Note: can also and elif (else if) and else to statement

4) Case statement
	Basic use example:
		case $(uname) in 

		Linux ) echo "Tux"
		;;
		Darwin ) echo "Hexley"
		;;
		FreeBSD | NetBSD | OpenBSD ) echo "Beastie"

		esac
	Note: You can use wildcare variables (*) as a "default" response

5) For loop
	Basic use example:
		for (( i=1; i<=3; i++ ))
		do
		   echo "You're cool x$i!"
		done

6) While loop
	Basic use example:
		while [myConditions]
		do	
			echo All the things
		done

7) Function 
	Works just like you'd expect. Must be declared before use.

	Example: 
		aFunction() {
			echo "This function is amazing."
		}

	Invoked via:
		aFunction

8) Trap
	Execute a command when script receives a signal

	Example:
		trap "echo Your program was terminated." SIGINT SIGTERM SIGKILL

	Can use various signals
