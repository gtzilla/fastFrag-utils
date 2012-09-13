#!/bin/sh
python ../converter.py -f input.html > output.json
diff -biw expect1.json output.json || diff -biw expect2.json output.json 
status=$?
test "$status" -eq 0 || echo "Failed!"
test "$status" -eq 0 && echo "Success!"
exit $status
