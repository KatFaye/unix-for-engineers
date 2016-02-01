Reading 03
==========

1. less \bin\ls

2. ldd ls

3. strace -e trace=open ls

4. gdb ./hello-debug

5. valgrind --leak-check=yes ./hello-dynamic

6. ./hello-profile
gprof hello-profile > hello-profile.output
