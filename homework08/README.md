Homework 08
===========

#timeout.py

1. The child process executes the inputted 
command using os.execvp() unless it receives 
an alarm signal. It is created with os.fork() 
and an exception is thrown if it cannot be 
created. The parent process sets up an alarm 
using signal.signal() and signal.alarm() that 
goes off after a given number of seconds, and 
then tries to wait until the child was 
finished using os.wait() An exception is 
thrown if the alarm is signalled, and the 
child process is killed with os.kill() and 
OSError is raised. 

2. The timeout mechanism uses signal.signal(), 
which takes an input of SIGALRM and handler. 
This is then set to go off after the number of 
seconds stored in SECONDS passes using signal.
alarm(). handler is a function that handles 
the signal with the alarm goes off. Within the 
handler function, the os.kill() function is 
used to end the child process with SIGTERM 
before raising a timeout notification within 
the parent process. If the alarm is not 
raised, it is disabled by setting signal.alarm(
0).

3. The test script runs through the various 
usage options and scenarios, returning 1 and 
displaying an error message if the expected 
results do not occur. This is done using if 
statements and for loops. If no errors occur, 
then the script displays a success message.

4. Although the script returns 0 the majority 
of the time, it occasionally returns a non-
zero value. I experiment with this by running 
the command "for i in `seq 1 300`; do ./timeout
.py -t 2 sleep 2 | echo $? ; done". It is not 
reasonable to except completely consistent 
results. Since the two processes are running 
simultaneously, if the parent happens to send 
the signal milliseconds before the child 
process finishes, the results may be skewed.

#rorschach.py

1. I scanned the file system using os.walk() on each 
inputted directory then iterated over all of the files 
within the path.

2. I loaded the rules by opening the file they were stored 
in using file(), and returning an error if the file did not 
exist/could not be opened. This was then fed into yaml.load()
, which returns a rules list. From there, a while loop was 
entered that continues until the user quits the program. 
check_directory() splits the rules and iterates over each 
directory then each file to check if the pattern stored in 
rule['pattern'] matched the file's name

3. I detected changes to the file using os.path.getmtime() 
to check if each file had been modified since the last scan. 
os.path.getctime() was used to check if the file had been 
created since the last scan.

4. Each action was executed by forking using os.fork() 
before using os.execvp() to execute the command stored in 
rule['action']. The variables path and name were expanded 
within the child process.

5. Busy-waiting occurs due to the fact that the program 
continually runs a check, then pauses the specified time, 
then runs again. This causes a extra delay in program 
execution, and would especially be a noticable problem when 
scanning large directories, since if a program is modified 
while the directory is being scanned, the change would not 
be caught. This could possibly be improved if the start-time 
for the next check was updated at the beginning of the scan, 
while the current scan uses the previous value of start_time.
Cache invalidation could occur if you delete a directory 
while attempting to scan it; I'm not sure how you could 
alleviate this issue.