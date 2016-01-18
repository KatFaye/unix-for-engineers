TLDR - chmod
==========

Overview
--------

[chmod] changes the access permissions on a file

Examples
--------

**-R** - changes files and directories recursively (changes files/directories under one specified as well)

	$ chmod -R myDirectory

**+** adds a permission

**-** removes a permission

**777** - numeric representation of permissions modification (first number user permissions, second group, third other)

	$ chmod 400
		-Only allows user to read file, no one else

Resources
---------

[Intro to Linux] - http://tldp.org/LDP/intro-linux/html/sect_03_05.html