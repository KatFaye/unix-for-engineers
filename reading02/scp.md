TLDR - scp
==========

Overview
--------

[scp] - secure way to copy remote files

	$ scp kherring@remote-server:myFile.txt localDirectoryName

Examples
--------

**-r** - recursively copy whole directory (also follows symlinks)

	$ scp -r kherring@remote-server:myFile.txt localDirectoryName

**-q** - disable progress meter and warning messages

	$ scp -q kherring@remote-server:myFile.txt localDirectoryName

Resources
---------

[Manual] - http://man7.org/linux/man-pages/man1/scp.1.html
