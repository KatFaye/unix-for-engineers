TLDR - valgrind
==========

Overview
--------

[valgrind] - use MEMCHECK and other tools to debug memory errors

	$ valgrind executable-name

Examples
--------

**--leak-check=yes** - detailed memory leak detector
	$ valgrind --leak-check=yes executable-name

**-v** - Gives extra information on program such as warnings or suppressions use

	$ valgrind -v executable-name

Resources
---------

[Manual] - http://man7.org/linux/man-pages/man1/valgrind.1.html
