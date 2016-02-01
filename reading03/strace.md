TLDR - strace
==========

Overview
--------

[strace] - trace system calls/signals

	$ strace command

Examples
--------

**-f** - trace child processes as they are created by currently traced processes
	$ strace -f command

**-e trace=open** - Display only open system calls of given command

	$ strace -e trace=open command

Resources
---------

[Manual] - http://man7.org/linux/man-pages/man1/strace.1.html
