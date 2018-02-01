#complete impplementation of t-CSA algorithm from paper
#combine CSA with DCT
#transfer times are included as well. Right now, all stations have the same transfer time.
#Incoming_Connection array actually stores the connections, instead of indices into connections array.
#OMTable incorporated into the CSA

from csalib import *
import sys

#set the filenames here
CAFile = "OneDay.txt"
DCTableFile = "DCT_sorted.txt"
OMTableFile = "OMT.txt"
StationsFile = "Stations.txt"


##################################################################
#load all the tables

#Station codes
SA = {}
SABuild(SA,StationsFile)
print sys.getsizeof([])
print sys.getsizeof(SA)

#DCTable build
DCTable = []
DCTableBuild(DCTable,DCTableFile)
print "DCTable = ",sys.getsizeof(DCTable)

#Connection array build
CA = []
CABuild(CA,CAFile)
length = len(CA)
print "CA = ",sys.getsizeof(CA)

#TT (transfer times) build
TT = []
for s in range(len(SA)):
    TT.append(int(600))

#OMTable (other means) table
OMTable = []
OMTableBuild(OMTable,OMTableFile)
omlength = len(OMTable)
print "OMTable = ",sys.getsizeof(OMTable)

##########################################################################
