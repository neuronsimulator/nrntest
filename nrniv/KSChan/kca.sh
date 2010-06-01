#!/bin/sh
# test the import functions
SES=kca.ses

rm temp[0-9].tmp

nrngui $SES << here
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

nrngui temp[0-9].tmp $SES << here
Grapher[0].doplt()
continue_dialog("Continue")
here
