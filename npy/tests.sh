#!/bin/sh

nrnpy="nrniv -nobanner -python"

py="
	arayerr createdelete execute fixbug hh1 hh
	hocac hoc2py test1 test2 test3
	testeval testext2 testext xpanel testref
"
for i in $py ; do
	echo $i
	$nrnpy $i.py << here
here
done
