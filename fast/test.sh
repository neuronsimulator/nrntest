#!/usr/bin/env bash

# A series of fast tests that can be run to verify NEURON functionality.
# Each test, if successful, should print nothing and set the value
# of b to 1.
# e.g
# 	nrniv -nobanner t1.hoc -c '{printf("%d\n", b)}'
#
# When this Readme is executed by the shell, it runs all the t*.hoc and
# indicates the tests that fail or print anything or has b != 1.  Tests that
# need more than one file should still have the same prefix but use
# different extensions, e.g.  t1.mod or t1.2.mod etc.  The t*.hoc file
# should have a comment at the beginning explaining what is being tested.
# Note that it is fair for any test to "load_file" any other test.

nrnivmodl

err=0
for script in t*.hoc; do
    a="$(nrniv -nobanner -nogui "${script}" -c 'if (name_declared("b")==5){execute("printf(\\\"%d\\\n\\\", b)")}else{printf(\"%d\n\", bb)}' 2>&1)"
    echo "${script} stdout: ${a}"
    if test "$a" = "2"; then
        echo "${script} invalid test"
        err=1
        continue
    fi
    if test "$a" != "1"; then
        echo "${script} failed"
        err=1
        continue
    fi
    echo "${script} succeeded"
done
exit $err
