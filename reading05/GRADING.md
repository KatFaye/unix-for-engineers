Reading 05 - Grading
====================

**Score**: 3.5 / 4

Deductions
----------
-.5: your implementation of resolve_links.sh does not work correctly. 
One of the correct solutions was:
#!/bin/sh

for path in $@; do
    for file_path in $path/*; do
        if [ -L "$file_path" ]; then
            echo $file_path links to $(readlink -f $file_path)
        fi
    done
done


Comments
--------
