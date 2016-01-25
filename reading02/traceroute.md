TLDR - traceroute
==========

Overview
--------

[traceroute] displays path packets take to network host

	$ traceroute 216.58.216.238

Examples
--------

**-6** - force ipv6 tracerouting over ipv4

	$ traceroute -6 ipaddr

**--back** - prints number of backwards hops (if it's different)

	$ traceroute --back ipaddr

Resources
---------

[Manual] - http://man7.org/linux/man-pages/man8/traceroute.8.html
