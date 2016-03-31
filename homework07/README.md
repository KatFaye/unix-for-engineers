Homework 07
===========

1. I parsed command line options using a for 
loop that ran through the values in sys.argv.
 If an '=' sign was found, I split the 
 argument in half, with the first part being 
 the option and the second part being the 
 argument (eg. seek would be stored in o, and 
 N in a). Another if statement checked for the 
 various argumet options, and returned an 
 error if an invalid argument was found.

2. I opened the input and output files using os
.open. The input file was opened in read-only 
mode, and the output file was opened in write-
only mode or created if needed.

3. Seek and skip were set to default values of 
zero. If options were entered, then the values 
of seek and skip were changed to the inputted 
block numbers within the initial if statement 
reading in arguments. Once the for loop 
reading in arguments finished, the values of 
seek and skip were multiplied by the value 
stored in bs. That number was then inputted as 
the second argument of lseek paired with 
either the input file (for skip) or the output 
file (for seek).

4. By default, count was set to the highest 
value possible- equivalent to saying "read as 
much of the file as you can." IF and OF were 
set to 0 and 1 respectively to read from stdin 
and stdout, then overwritten with the inputted 
file arguments if entered. While the current 
number of blocks read was less than the value 
of count, os.read and os.write was used to 
copy the amount of bytes stored in bs from 
read to write. If an empty string was 
encountered, the while loop terminated since 
the entire file had been read.

