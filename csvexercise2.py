#!/usr/bin/env python

import csv

with open('csvfile.csv','rb') as csvfile:
	csvreader = csv.reader(csvfile, delimiter=",", quotechar="'")
	
	for row in csvreader:
		print ",".join(row)
		total = 0
		for val in row:
			total = total + int(val)
		print "Total: {0}".format(total)
