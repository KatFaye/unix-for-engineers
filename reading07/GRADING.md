Reading 07 - Grading
====================

**Score**: 3.25 / 4

Deductions
----------

-0.25	Doesn't use associative array to count machines and types:
-0.5 	test_catalog_summary.sh fails

Comments
--------

catalog_summary.sh:
The \n did not convert to end line characters, so the output printed on one line and the test failed. Also, you should use associative arrays to get the information like this:
  /name/      {
                    if ($2 in machines == 0) {
                        machines[$2] += 1
                        total_machines += 1
                    }
                }

