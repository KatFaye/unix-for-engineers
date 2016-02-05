Homework 03
===========

Activity 01
===========

1. a. libgcd.so is larger - bound into program at runtime
b. gcd-static is much larger because the entire libgcd.a library is bound statically into the executable.

2. gcd-static doesn't depend on any: ran ldd gcd-static
gcd-dynamic depends on:
	linux-vdso.so.1 =>  (0x00007ffc29be2000)
	libgcd.so => ./libgcd.so (0x00007efd259a7000)
	libc.so.6 => /lib/x86_64-linux-gnu/libc.so.6 (0x00007efd255ce000)
	/lib64/ld-linux-x86-64.so.2 (0x000055777f68b000)
	(ran ldd gcd-dynamic)

3. Yes, but only because I set my library path to be equal to the home directory to test it. It would not have worked otherwise. Used the command: export LD_LIBRARY_PATH=. to change that environment variable.

4. Static linking has the advantage of being compatible across operating systems and providing a slight speed boost, however its disadvantages include a larger file size and increased maintenance requirements if security vulnerabilities are discovered in the libraries used. Dynamic linking has a disadvantage in that it takes slightly longer since it pulls the library at execution time, however its advantages include being smaller and easier to update and maintain the libraries without requiring all programs using the library to be re-compiled.

I'd in general prefer the dynamic linking to be the default, since it takes up less space and wouldn't require me to check periodically to ensure that the libraries I'm using haven't been updated due to issues found.

Activity 02
===========

1. wget https://www3.nd.edu/~pbui/teaching/cse.20189.sp16/static/tar/is_palindrome.tar.gz
tar -xvzf /home/katricia/Downloads

2. -Wall -g ; These symbols made the executable about 25% larger- when compiled with the -Wall and -g flags, the executable -is_palindrom was 12k; when compiled without these debugging flags, it was only 8.8k.

3. Segmentation fault: I used GDB to diagnose this error, which was caused by the buffer varable not being initialized as an array correctly. I first ran the program in gdb (gdb ./is_palindrome), then backtraced it after the segmentation point and set a breakpoint there. (backtrace; break is_palindrome.c:46). The buffer "array" only contained a single char, so I modified it to be an C-string of size "BUFSIZE".

Memory leak: I used memcheck to diagnose this error (valgrind --leak-check=yes ./is_palindrome). The memory that was allocated with malloc was not being freed- a requirement for dynamically allocated memory, so I added that after the memory was no longer needed (free(sanitized)).

Invalid memory access: *back started comparing at the \0 character instead of at the last character within the string. This was easily fixed by adding a -1 to its initial declaraction. Diagnosed with gdb.

Memory leak: The final error had to do with the usage of malloc and was diagnosed with valgrind --leak-check=yes ./is_palindrome. By replacing malloc with strdup(s), sanitized was instead created as a duplicate string that could then be converted to a string without spaces ending with the appropriate '\0' character, preventing the memory leak. I used GDB to figure out that santized was being returned as "tacocatt" instead of "tacocat" to pinpoint that the \0 was not terminating the string in the right spot.

4. The final memory leak was the hardest, because I didn't really understand how malloc works and how it can cause an automatic memory leak. Even once I figured that out, I also didn't really understand how strdup worked- and after understanding that, I just made a bunch of minor syntax errors in attempting to ensure the string was terminated correctly. This bug could be prevented in the future by always checking that a string is appropriately terminated first, before attempting more complex solutions.

Activity 3
==========

1. Contacting the COURIER

/afs/nd.edu/user15/pbui/pub/bin/COURIER

Output:
 ________________________________________ 
/ Hmm... you sure you put the package in \
\ the right place?                       /
 ---------------------------------------- 
  \
     \
                  _ _
       | __/|  .~    ~.
       /oo `./      .'
      {o__,       {
        / .  . )    
        `-` '-'     }
       .(   _(   )_.'
      '---.~_ _ _|

2. Find package location

strace /afs/nd.edu/user15/pbui/pub/bin/COURIER | grep package

--unhelpful output-
stat("/tmp/kherring.deaddrop", 0x7fff556e1760) = -1 ENOENT (No such file or directory)
--unhelpful output--

3. Create the package in specified location; contact courier again

touch /tmp/kherring.deaddrop
/afs/nd.edu/user15/pbui/pub/bin/COURIER

Output:

 ______________________________________ 
/ Whoa whoa... you can't give everyone \
\ access to the package! Lock it down! /
 -------------------------------------- 
  \
     \
                  _ _
       | __/|  .~    ~.
       /oo `./      .'
      {o__,       {
        / .  . )    
        `-` '-'     }
       .(   _(   )_.'
      '---.~_ _ _|

4. Change file permissions on package; contact courier again

chmod 700 /tmp/kherring.deaddrop
/afs/nd.edu/user15/pbui/pub/bin/COURIER

Output:
_______________________________________ 
/ What are you trying to pull here? The \
\ package is the wrong size!            /
 --------------------------------------- 
  \
     \
                  _ _
       | __/|  .~    ~.
       /oo `./      .'
      {o__,       {
        / .  . )    
        `-` '-'     }
       .(   _(   )_.'
      '---.~_ _ _|

5. Change file to expected size

strace /afs/nd.edu/user15/pbui/pub/bin/COURIER | grep size

Output:
-unhelpful stuff-
clone(child_stack=0, flags=CLONE_PARENT_SETTID|SIGCHLD, parent_tidptr=0x7fff01a41008) = 32609
wait4(32609, \ package is the wrong size!            /
-more unhelpful stuff-

truncate -s 32609 /tmp/kherring.deaddrop
/afs/nd.edu/user15/pbui/pub/bin/COURIER

Output:

 ________________________________________ 
/ Well, everything looks good... I'm not \
| sure what '' means, but I'll pass it   |
\ on.                                    /
 ---------------------------------------- 
  \
     \
                  _ _
       | __/|  .~    ~.
       /oo `./      .'
      {o__,       {
        / .  . )    
        `-` '-'     }
       .(   _(   )_.'
      '---.~_ _ _|


                          
