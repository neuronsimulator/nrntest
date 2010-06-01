#!/bin/sh

rm -f tmp1
curl http://senselab.med.yale.edu/modeldb/ModelList.asp?id=1882 | tr -d '\201-\355' > tmp1

sed -n '
	s/.*model=\([0-9]*\).*/\1/p
' < tmp1 > tmp2

for i in `cat tmp2` ; do
	curl "http://senselab.med.yale.edu/modeldb/eavBinDown.asp?o=$i&a=23&mime=application/zip" > modeldb/$i.zip
	echo $i
done

for i in 82894 113435 ; do
	curl "http://senselab.med.yale.edu/modeldb/eavBinDown.asp?o=$i&a=311&mime=application/zip" > modeldb/$i.zip
	echo $i
done

for i in 45539 97747 ; do
rm -r modeldb/$i.zip
done

echo "Done"
