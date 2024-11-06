#!/usr/bin/env bash
set -eu

CURRENT_DIR="$(cd -- "$(dirname -- "$0")" &>/dev/null && pwd)"
sh "$CURRENT_DIR/testutil/clean"
neurondemo -c 'quit()'

have_nrnpython=yes
have_nrnmpi=yes
have_coreneuron=no
if nrniv -nobanner -nogui -c 'nrnversion(6)' | grep "NRN_ENABLE_PYTHON=OFF" >/dev/null; then
    have_nrnpython=no
    echo "Python is disabled: NRN_ENABLE_PYTHON=OFF"
fi
if nrniv -nobanner -nogui -c 'nrnversion(6)' | grep "NRN_ENABLE_MPI=OFF" >/dev/null; then
    have_nrnmpi=no
    echo "MPI is disabled: NRN_ENABLE_MPI=OFF"
fi
if nrniv -nobanner -nogui -c 'nrnversion(6)' | grep -i -E "NRN_ENABLE_CORENEURON=(ON|TRUE|YES|Y|1)" >/dev/null; then
    have_coreneuron=yes
    echo "CORENEURON is enabled: NRN_ENABLE_CORENEURON=ON"
fi
export have_nrnpython
export have_nrnmpi
export have_coreneuron

#list in "scripts", the scripts to run tests in subdirectories.
#list in "compare", the folders to execute comparison tests
#  for all the *.cmp files in those folders
#

scripts=(
    "${CURRENT_DIR}/fast/Readme" "${CURRENT_DIR}/nrniv/Parallel/recv/test.sh"
)

if [[ "$have_nrnpython" = yes ]] && [[ "$have_nrnmpi" = yes ]]; then
    scripts="${CURRENT_DIR}/nrniv/Parallel/dotests.sh $scripts"
fi

compare=(
    "ivoc/Random" "ivoc/Pointer" "ivoc/Vector" "ivoc/Matrix"
    "nrniv" "nrniv/NetCon" "nrniv/SaveState"
    "nmodl" "nmodl/FOR_NETCONS" "nmodl/functiontable" "nmodl/LONGDIFUS"
    "nmodl/order" "nmodl/WATCH"
    "nmodl/CONDUCTANCE"
)

cmpprog="$CURRENT_DIR/testutil/cmpdatfile"

failed_runs=()
failed_comparisons=()

runscript() {
    working_dir=$(dirname "$1")
    script=$(basename "$1")
    echo "Running test $1"
    cd "${working_dir}"
    if ! bash "${script}"; then
        failed_runs+=("$1")
    fi
    cd -
}

runcompare() {
    working_dir=$1
    echo "Running cmpdatfile in $1"
    cd "${working_dir}"
    if ! bash "${cmpprog}" ./*.cmp; then
        failed_comparisons+=("$1")
    fi
    cd -
}

for i in ${scripts[@]}; do
    runscript "$i"
done

for i in ${compare[@]}; do
    runcompare "$CURRENT_DIR/$i"
done

if [[ ${#failed_runs[@]} -gt 0 ]]; then
    echo "Failed runs: ${failed_runs[@]}"
fi
if [[ ${#failed_comparisons[@]} -gt 0 ]]; then
    echo "Failed comparisons: ${failed_comparisons[@]}"
fi

if [[ ${#failed_runs[@]} -ne 0 || ${#failed_comparisons[@]} -ne 0 ]]; then
    echo "There were failures in either failed_runs or failed_comparisons, see above."
    exit 1
else
    echo "All checks passed."
    exit 0
fi
