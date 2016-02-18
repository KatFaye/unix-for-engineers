Homework 04
===========

**Activity 01: Bake.sh**

1. a) I set variables to default values using the syntax VARIABLE=${VARIABLE:-"default"}. This used the default value for the variable unless overwritten when calling the script on the command line.

b) I iterated over files matching SUFFIXES by using a for loop. For every file found by the "find *$SUFFIXES", the script attempted to compile the file. 

c) The verbose variable I set to a default value of 0. An if statement within the for loop checked to see if the variable was set to anything other than zero and, if it was, echoed the compilation command.

d) Right after the line containing the command to compile the file, an if statement checked if the compilation had run correctly (a return status of 0). If not, then "exit 1" terminated the program early.

2. bake.sh performs similarly to make, however does not include a "clean" option to remove created executables and does not as written have the capability to link multiple object files together. Make is more flexible as well in that it is easier to only compile specific files within a directory instead of those matching the expected target. Both allow variables to be set, and provide a way of automating compilation, however I will likely continue to use make in the future.

**Activity 02: disk_usage.sh**

1. a) I parsed command line arguments using the "getopts" utility first. This went through the arguments until it had checked them all, returning a error message if an invalid argument was entered. After all flags have been parsed (if there are any), the remaining argument should be the directory to check, which is then shifted in order to be accessed with '$1'.

b) The script checks if the number of command line arguments is equal to zero using the '$#' variable. If it is, then message is returned displaying appropiate usage of the script.

c) Directory arguments were processed within a while loop that continued until all directory arguments had be processed. For each expected directory argument, a test was done to ensure that the argument was in fact a directory and returned an error if it was not. shift was then used to shift the positional parameter by one so the next directory would be processed as '$1'.

d) The command line argument for the -n flag was stored in the variable 'NOPT' using the 'OPTARG' variable with getopts. If no value was provided but the -n flag was included, it default to 'n'. This was then incorporated into the flags for the head command by accessing the variable.

2. The hardest part of the script was testing if no arguments had been entered, since my initial method of checking for that without the use of $# failed "test_disk_usage.sh". The longest part of the code was simply checking for valid inputs before performing the needed commands for display. This was not surprising, since error checking needs to be thorough in order to account for all possible outcomes.
