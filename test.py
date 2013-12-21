#!/usr/bin/env python

def mult(*args, **kwargs):
	if not "verbose" in kwargs:
		kwargs["verbose"] = False
	total = 1
	list_of_ints = []
	for num in args:
		total = total * num
		list_of_ints.append(str(num))
	if kwargs["verbose"]:
		print " x ".join(list_of_ints)
	return total

print mult(4,5,5,verbose=True)