#!/usr/bin/env python


listoflists = []
firstList = [1,2,3,4]
secondList = [5,6,7,8]
thirdList = [9,10,11,12]

listoflists.append(firstList)
listoflists.append(secondList)
listoflists.append(thirdList)

f = open("output.csv", "w")

for list in listoflists:
	f.write(",".join(str(x) for x in list))
	f.write("\n")

f.close()

