TLDR - host
==========

Overview
--------

[host] - converts names to IP addresses and vice-versa

	$ host 216.58.216.238

Examples
--------

**-R** - sets number of UDP retries for lookup (how many times it tries the conversion)

	$ host -R 5 google.com

**-w** - specifies how long a replied will be waited for in seconds (can effectively wait forever)

	$ host -w 5 google.com

Resources
---------

[Manual] - http://linux.die.net/man/1/host
