Reading 06
==========

1. echo "All your base are belong to us" | tr [a-z] [A-Z]

2. cat /etc/passwd | awk -F: '/root/ {print $7}'

3. echo "monkeys love bananas" | sed -e 's/monkeys/gorillaz/g'

4. cat /etc/passwd | sed -e 's/\/bin\/bash/\/usr\/bin\/python/g' -e 's/\/bin\/csh/\/usr\/bin\/python/g' -e 's/\/bin\/tcsh/\/usr\/bin\/python/g' | grep python


5. echo "     monkeys love bananas" | sed -e 's/^[ \t]*//'

6. cat /etc/passwd | grep -E ':4.*7:' | grep -v -E ':4:|:7:'

7. tail -f [log path]

8. grep -F -x -f file1 file2
