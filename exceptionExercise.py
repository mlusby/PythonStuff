#!usr/bin/env python

my_list = [1, 2, 3, 5]
my_dict = {"Fruit": "Apple", "car": "Suburban"}

try:
    #print my_list[6]
    print my_dict["Friend"]
except (IndexError, KeyError) as e:
    print "This is an {0} Error!".format(e.Message)
