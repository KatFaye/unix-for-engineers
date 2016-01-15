TLDR - git
==========

Overview
--------

[Git] is a distributed version control system.

Examples
--------

- **Clone** a remote *repository*:

        $ git clone git@bitbucket.org:CSE-20189-SP16/assignments.git

- **Remote** shows your configured remote servers

		$ git remote

	Add the -v flag to get the URL that goes with each shortname found

- **Pull** - generally, fetches data from cloned server and attempts to merge data

	$ git pull

- **Push** - 'push' your updates out to the remote server. Can specify remote and branch names

	$ git push (remote name) (branch name)

- **Config** - used to create aliases for both default and custom commands

	$ git config --global alias.up commit

		- This would set "up" as an alias for "commit"
Resources
---------

- [Pro Git](https://git-scm.com/book/en/v2)

[git]: https://git-scm.com/
