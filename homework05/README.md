Homework 05
===========

**Activity 01: Caesar.sh**

1. I constructed the source set by simply including 'a-zA-Z', which is all upper and lowercase letters, and using that as the first argument of the tr command to encrypt.

2. To construct the target set, I first created the variable "ALPHA", which was simply the entire alphabet listed twice. I then used that variable to create the "ROTATE" variable, which cut starting from the NOPT (default or non-default Caesar shift) and included the next 25 characters in the set (using the variable END, which was NOPT + SIZE where SIZE is the size of the alphabet - 1). This was then duplicated for uppercase in ROTATEUPPER by converting ALPHA to uppercase before running the cut command. Both variables were included as the second argument in the tr command to make up the target set.

3. I performed the equipped by using cat to get the input piped into the program and then used tr of the source set to the target set to encrypt said input.

**Activity 02: reddit.sh**

1. I filtered the URLs using grep, then removing all irrelevant using a reverse grep, then cutting off extraneous characters using cut.

2. I used a series of if statements to run alternative commands depending on the options selected. If a -r input was read, then the "shuf" command was added to the pipeline; if a -s was read, then "sort" was added to the pipeline. If both were read, then the last input was the value considered.

3. I incorporated everything into one command using "|" in order to pipe the output of one command into the next command until I was done with all modifications and filtering of the data.

**Activity 03: broify.sh**

1. I removed comments using sed to remove any lines containing the comment delimiter.

2. I removed empty lines with sed '/^$/d'

3. I used an if statement to run the appropriate command based on the arguments found using getopts. The value of DOPT was substituted to be the appropriate delimiter based on the input in the command line.


