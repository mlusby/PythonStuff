#!/usr/bin/env python

import csv
import random
import sys

if len(sys.argv) < 2:
	print "You should provide a filename!"
	filename = "csvfile.csv"	
else:
	filename = sys.argv[1]

with open(filename,"w") as csvfile:
	writer = csv.writer(csvfile, delimiter=",",quotechar="|", quoting=csv.QUOTE_MINIMAL)
	array = []
	for x in range(5):
		for y in range(5):
			array.append(random.randint(0,100))
		writer.writerow(array)
		array = []

