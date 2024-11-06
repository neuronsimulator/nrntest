#!/usr/bin/env bash
# test harness for case when $1.hoc output is to be compared to $1.cmp

set -eu
err=0

# if mod file exists, run nrnivmodl
modfiles="$(find . -maxdepth 1 -name "*.mod")"
if [[ -n "${modfiles}" ]]; then
    if ! nrnivmodl >&/dev/null; then
        echo "nrnivmodl failed"
        exit 1
    fi
fi

# run the tests
for arg in "$@"; do
    # If the $i file contains the .hoc or .cmp extension, remove it
    filename="$(echo "${arg}" | sed -e 's/\.hoc$//' -e 's/\.cmp$//')"
    nrniv -nogui -nobanner "$filename.hoc" >&"$filename.temp"
    if cmp "$filename.cmp" "$filename.temp"; then
        echo "$filename.hoc succeeded ($filename.cmp)"
    elif [[ -e $filename.cmp.c3 ]] && cmp "$filename.cmp.c3" "$filename.temp"; then
        echo "$filename.hoc succeeded ($filename.cmp.c3)"
    elif [[ -e $filename.cmp.ci ]] && cmp "$filename.cmp.ci" "$filename.temp"; then
        echo "$filename.hoc succeeded ($filename.cmp.ci) "
    else
        echo "$filename.hoc failed"
        err=1
    fi
done

exit $err
