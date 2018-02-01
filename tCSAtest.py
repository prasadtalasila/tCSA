#complete impplementation of t-CSA algorithm from paper
#combine CSA with DCT
#transfer times are included as well. Right now, all stations have the same transfer time.
#Incoming_Connection array actually stores the connections, instead of indices into connections array.
#OMTable incorporated into the CSA

from csalib import *

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
print "sizes (in bytes) of all the arrays"
print "SA = ",sys.getsizeof(SA)

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
#test queries
#result from DCTable
#print "----:Bangalore to Chennai:----"
#tCSA(2141,2143,randint(1,23)*60*60,DCTable,SA,TT,OMTable,CA)

#vijayawada to itarsi
#print "----:Vijayawada to Itarsi:----"
#tCSA(172,135,randint(1,23)*60*60,DCTable,SA,TT,OMTable,CA)

#chennai to vijayawada
#print "----:Chennai to Vijayawada:----"
#tCSA(236,172,randint(1,23)*60*60,DCTable,SA,TT,OMTable,CA)

#madgaon to ratnagiri
#print "----:Madgaon to Ratnagiri:----"
#tCSA(2,38,28000,DCTable,SA,TT,OMTable,CA)
#print "----:Madgaon to Ratnagiri:----"
#CSA(2,38,28000,SA,CA)

#loop for random queries
for _ in range(1):
    src = randint(1,2164)
    dst = randint(1,2164)
    print "----:Itinerary search query: from ", SA[src], "to", SA[dst], "(with tCSA):----"
    print "Travel itinerary:"
    tCSA(src,dst,randint(1,23)*60*60,DCTable,SA,TT,OMTable,CA,3)
    #print "\n----:", SA[src], "to", SA[dst], "(with CSA):----"
    #CSA(src,dst,randint(1,23)*60*60,SA,CA,3)
