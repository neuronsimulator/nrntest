#!/bin/sh
# test the import functions

nrngui mh1.hoc << here
run()
load_file("chanbild.hoc")
chanbild(KSChan[0])
ChannelBuild[0].kshoc("temp.tmp")
quit()
here

nrngui temp.tmp mh.ses << here
run()
continue_dialog("Continue")
here
