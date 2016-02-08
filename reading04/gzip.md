TLDR - gzip
==========

Overview
--------

[gzip] - compress/decompress files 

	$ gzip sourceFile

Examples
--------

**-r** - recursively zip entire directory (generally, should archive first instead)
	$ gzip -r myDirectory

**-[1-9]** - optimization flags; -1 fastest but least thorough

	$ gzip -9 sourceFile

Resources
---------

[Manual] - http://linux.die.net/man/1/gzip
