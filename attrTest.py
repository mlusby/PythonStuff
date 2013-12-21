my_list = [5,10,'Dallas','Fresno',3,'Debra',7]

total = 0
for item in my_list:
	if hasattr(item,'bit_length'):
		total = total + item
	if hasattr(item, 'startswith'):
		if getattr(item,"startswith")('D'):
			print "Item: {0}".format(item)
print "Total: {0}".format(total)

	
