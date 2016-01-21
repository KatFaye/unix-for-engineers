Homework 01
===========

Exercise 01: Paths
===========

1. Absolute path: cd /afs/nd.edu/user14/csesoft

2. Relative path: cd ../../user14/csesoft

3. cd ~csesoft

4. ln -s ~csesoft ~/csesoft

Exercise 02: Copying, Moving, Removing
============

1. cp -r /usr/share/pixmaps ~/images

2. Yes, they are displayed in red font and highlighted in gray

3. mv ~/images ~/pixmap
To time: time mv ~/images ~/pixmap

3. mv ~/pixmap /tmp/kherring-pixmaps
To time: time mv ~/pixmap /tmp/kherring-pixmaps
Operation is slower because moving from the home directory to a higher directory before creating a new directory to store data in (kherring-pixmaps)

4. rm /tmp/kherring-pixmaps -r
To time: time rm/tmp/kherring-pixmaps -r
Operation is much quicker.

Exercise 03: Files and Directories
=============

1. ls -l -h

2. ls -l -t

3. find cctools -type f | wc -l

4. find -name 'weaver' -executable 
	Was found

5. du cctools/x86_64 -ah | sort -hr | head -n 2
 a) cctools/x86/redhat5 is the largest at 77MB (Excluding directory itself)

6. find cctools/x86_64/redhat5 -type f | wc -l
768 files

7. find cctools/x86_64 -type f -print0 | xargs -0 du | sort -n | tail -1 cut -f2 | xargs du -sh
 a) Largest file is cctools/x86_64/redhat5/bin/parrot_run_hdfs at 18MB

8. find cctools/x86_64 -type f -mtime +30 | wc -l
1937 (no files have been modified in past 30 days)

Exercise 04: Unix Permissions
=============

1. Owner and group can read, only owner can write, all (owner, group, other) can execute

2. a) chmod 711 data.txt 
	All can execute, only user can r/w
b) chmod 770 data.txt
	Only you and group members can r/w/x
c) chmod 444 data.txt
	All can read
d) chmod 000 data.txt

3. Can still be removed if you have delete permissions in parent sub-directory

Exercise 05: AFS Permissions
==============

1. Home: nd_campus/authuser (l)
admin/kherring (rlidwka)

Private: nd_campus/authuser (none)
admin/kherring (rlidwka)

Public: nd_campus (rlk)
admin/kherring (rlidwka)

On the home directory, nd_campus or authuser can only look up the directories/files.
On the private directory, nd_campus or authuser have no access permissions
On the public directory, nd_campus and authuser can read files, look them up, or set read/write locks

2. Unix permissions are rwx for both owner, group, and others. However, touch was unsuccessful because common is a read-only file system: non-administrators only have read or lookup (list) permissions with ACL

3. fs setacl -dir ~ -acl pbui rl

Exercise 06: Masks
==============

1. They are no. world1.txt has rw permisions for owner/group/others.
world2.txt has rw permissions for user but only r permissions for group/others. world3.txt has rw permissions for user but only write permissions for group/others.

They are different because umask sets default file permissions for future newly created files. It can be useful if you know the general default permissions you want to have for files you're creating (such as accessible only to yourself). By setting the umask default, you don't have to chmod every file.



