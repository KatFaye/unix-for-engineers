Homework 04
===========

**Activity 01: Bake.sh**

1. a) I set variables to default values using the syntax VARIABLE=${VARIABLE:-"default"}. This used the default value for the variable unless overwritten when calling the script on the command line.

b) I iterated over files matching SUFFIXES by using a for loop. For every file found by the "find *$SUFFIXES", the script attempted to compile the file. 

c) The verbose variable I set to a default value of 0. An if statement within the for loop checked to see if the variable was set to anything other than zero and, if it was, echoed the compilation command.

d) Right after the line containing the command to compile the file, an if statement checked if the compilation had run correctly (a return status of 0). If not, then "exit 1" terminated the program early.

2. bake.sh performs similarly to make, however does not include a "clean" option to remove created executables and does not as written have the capability to link multiple object files together. Make is more flexible as well in that it is easier to only compile specific files within a directory instead of those matching the expected target. Both allow variables to be set, and provide a way of automating compilation, however I will likely continue to use make in the future.


