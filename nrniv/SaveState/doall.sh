(
nrngui hocevent.hoc <<here
quit()
here

sh sync.sh << here
quit()
here

for i in vecplay*.hoc ; do
	nrngui $i <<here
	quit()
here
done

~/papers/localstep/tccx/i686/special tccxtst.hoc - << here
	firstlaunch()
	quit()
here
~/papers/localstep/tccx/i686/special tccxtst.hoc - << here
	secondlaunch()
	quit()
here

) > out.dat 2>&1

if cmp standard.dat out.dat ; then
	echo "standard.dat is the same as out.dat"
else
	diff standard.dat out.dat
	echo "standard.dat differs from out.dat"
fi
