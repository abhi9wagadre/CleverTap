import calendar
import csv
import datetime
import time
from os import listdir
from os.path import isfile, join

dataFiles = []
dataFileIdentifier = "_eventsUsageSummary"

onlyfiles = [f for f in listdir(".") if isfile(join(".", f))]
for file in onlyfiles:
	if file.__contains__(dataFileIdentifier) and file.endswith(".csv"):
		dataFiles.append(file)

fout=open("out.csv","a")

 
for csvfile in dataFiles:
 	print csvfile
	f = open(csvfile)
	#f.next() # skip the header
	for line in f:
		fout.write(line)
	f.close() # not really needed
fout.close()