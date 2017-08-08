#!/bin/bash

# point_mod_files.zip contain all the mod files in ModelDB as of July 2017
# that are POINT_PROCESS with NET_RECEIVE blocks. This extracts into
# modeldb with one subfolder (the accession number) per model.
# This script copies all the mod files into a single "modfiles" folder
# appending the accession number to the filename and to the POINT_PROCESS
# name so that they do not conflict when a single nrnmech.dll is made.
# Files that have INCLUDE are removed from modfiles as are a few files
# that do not compile. e.g. mod files that use EXTERNAL.

mods=`find modeldb -name \*.mod`

if false ; then
  rm -f temp
  for i in $mods ; do
    nocmodl $i >>temp 2>&1
  done
fi

# copy all the mod files to modfiles with unique names and POINT_PROCESS
# names derived from the existing basename and the accession number

rm -f -r modfiles
mkdir modfiles
for i in $mods ; do
  n=`echo $i | sed -n 's,modeldb/\([0-9]*\)/.*,\1,p'`
  base=`basename $i .mod`
  echo ${base}_${n}
  sed "
    s/\(POINT_PROCESS[ \t]*[a-zA-Z][a-zA-Z0-9_]*\)/\1_${n}/
  " $i > modfiles/${base}_${n}.mod
done

# Some mod files INCLUDE a missing file
for i in modfiles/*.mod ; do
  if grep INCLUDE $i ; then
    echo "$i has an INCLUDE statement. Removing"
    rm $i
  fi
done

#notes:
#ampa_147867 has parameter discontinuity not managed by NET_RECEIVE so cvode...

#Some mod files have compilation problems due to EXTERNAL.
#  ampa_116769 nmda_116769
#  izhi2007_194897 declares STATE but has no equations for them

files="
  izhi2007_194897
  ampa_116769 nmda_116769
  "

if true ; then
for i in $files ; do
  echo "$i does not compile. Removing but should be fixed"
  rm modfiles/$i.mod
done
fi

rm -r -f x86_64
#nrnivmodl modfiles
