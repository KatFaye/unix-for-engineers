TLDR - zip
==========

Overview
--------

[zip] - package and compress files

	$ zip archive fileToCompress

Examples
--------

**-** - write zip to standard ouput
	$ zip -r - . | progToPipeTo

**-d** - remove entries from a zip archive

	$ zip -d archive archive/doNotWant 

Resources
---------

[Manual] - http://linux.die.net/man/1/zip
