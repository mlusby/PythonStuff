class Dog(object):
	breed = "Pit Mix"
	coat = "Brindle"
	
	def speak(self):
		print "I'm a {0} {1}".format(self.coat,self.breed)

