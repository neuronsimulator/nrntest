#!/bin/sh
# test the import functions

rm temp[0-9].tmp

nrngui hhnaksing.ses << here
run()
strdef fname
objref clist
clist = new List("ChannelBuild")
for i=0, clist.count-1 { clist.object(0).destroy() }
if (clist.count != 0) { continue_dialog("did not destroy all ChannelBuild") quit()}
clist = new List("KSChan")
for i=0, clist.count-1 {
	chanbild(clist.object(i))
}
clist = new List("ChannelBuild")
for i=0, clist.count-1 {
	sprint(fname, "temp%d.tmp", i)
	clist.object(i).kshoc(fname)
}
quit()
here

nrngui temp[0-9].tmp hhnaksing.ses << here
run()
continue_dialog("Continue")
here
