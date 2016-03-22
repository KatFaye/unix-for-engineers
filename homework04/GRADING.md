Homework 04 - Grading
=====================

**Score**: 14.5 / 15

Deductions
----------
Deductions are specified under their respective section
 if there are none written, no points were lost

Activity 01: Bake (5 Points)
-.5:this was not passing the test for me 
I think the biggest thing missing is the looping through the sources in the suffix. 
It looks like you got most of the concepts for the problem so I am only taking of .5
Here is one way to do it:
for suffix in ${SUFFIXES}; do 
	for src in *${suffix}; do         
		tgt=$(basename ${src} ${suffix})
		[ "$VERBOSE" -gt 0 ] && echo ${CC} ${CFLAGS} -o ${tgt} ${src}         
		${CC} ${CFLAGS} -o ${tgt} ${src} || exit 1     
	done 
done

Activity 02: Disk Usage (5 Points)
Activity 03: Taunt (5 Points)
Messages very on point! + I like the cat
It looks like the "exit" is working, but know that you can also do:

trap 'drop' HUP 
trap 'taunt' INT TERM QUIT

where drop(){..} andt taunt(){..} are functions defined in the file

Comments
--------
