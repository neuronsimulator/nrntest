#!/usr/bin/python
# find all the NEURON model object ids (accession numbers) and download their zip files
# into a modeldb folder

# first a download file function found on the web:
import os
import urllib2
from urllib2 import urlopen, URLError, HTTPError, Request

def dlfile(url,filename):
    # Open the url
    try:
        f = urlopen(url)
        print "downloading " + url
        
        # Open our local file for writing
        with open(filename, "wb") as local_file:
            local_file.write(f.read())
        
    #handle errors
    except HTTPError, e:
        print "HTTP Error:", e.code, url
    except URLError, e:
        print "URL Error:", e.reason, url
  
# get a fresh copy of the web page listing the NEURON models in ModelDB
#

req = Request('http://senselab.med.yale.edu/modeldb/ModelList.asp?id=1882')
response=urllib2.urlopen(req)
html=response.read()

# store the ObjectID's (Accession numbers) for the NEURON models in ModelDB
#

modeleq = html.split("model=")
objectids=[]
for tmp in modeleq[1:]:
  tmplist=tmp.split("'")
  objectids.append(tmplist[0])
print("We have found "+str(len(objectids))+" NEURON model objectids")

# download the archives for these model objectids
#
for objid in objectids:
  dlfile('http://senselab.med.yale.edu/modeldb/eavBinDown.asp?o='+objid+'&a=23&mime=application/zip',
    "modeldb/"+objid+".zip")

# get the ones which are "alternate version" models
# one is the Traub (orig. Fortran), another Golomb (orig. XPP)

for objid in ['82894', '113435']:
  dlfile('http://senselab.med.yale.edu/modeldb/eavBinDown.asp?o='+objid+'&a=311&mime=application/zip',
    "modeldb/"+objid+".zip")

# delete the original Traub fortran and Golomb XPP which were downloaded inappropriately 
for i in ['45539', '97747']:
  os.remove("modeldb/"+i+".zip")


print("Done")
