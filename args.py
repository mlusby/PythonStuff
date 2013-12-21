#!/usr/bin/env python
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-v","--verbose",action="count")
parser.add_argument("x")
parser.add_argument("y")

args = parser.parse_args()

if args.verbose > 0:
	if args.verbose == 3:
		print "It's TOTALLY VERBOSE!"
	elif args.verbose == 2:
		print "It's getting more verbose in here..."
	else:
		print "It's Verbose!"
print "X is {0}".format(args.x)
print "Y is {0}".format(args.y)

