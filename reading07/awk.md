TLDR - awk
==========

Overview
--------

[awk] - pattern scanning and processing language

	$ '/search_pattern/ { action_to_take_on_matches; another_action; }' file_to_parse

Examples
--------

**$n** - Print Specific Fields
	$ { print $2, $1 }

**-F** - update user's cached credentials; does not run a command

	$ awk -F  ":"

**BEGIN** - executed before actual AWK script

	$ awk 'BEGIN{awk initializing code}{actual AWK code}' filename.txt

**END** - executed after all AWK code processed

	$ awk 'END{print "Finished processing code!"} test.txt

**pattern matching** - Pattern matching with AWK

	$ awk '/pattern/' myFile.txt

**NR** - number of current record

	$ awk '{ print NR, $0 }'

**NF** - last field

	$ awk '{ print $NF }'

**array** - set the value of an awk array

	$ awk '{ array[subscript] = value }'
Resources
---------

[Manual] - http://linux.die.net/man/1/awk
