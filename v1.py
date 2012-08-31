import urllib2
import base64
import re

#Just commenting
url = "https://www10.v1host.com/ClickMotive/rest-1.v1/Data/Story?sel=Name,ToDo&where=ToDo='0'"
request_object = urllib2.Request(url)
base64string = base64.encodestring('%s:%s' % ('mlusby','FixThis'))[:-1]
authheader=  "Basic %s" % base64string
request_object.add_header("Authorization", authheader)
try:
	doc = urllib2.urlopen(request_object)
except IOError, e:
	print "Error!"
	if hasattr(e, 'code'):
		print "ErrorCode: %s" % e.code
		if e.code == 401:
			authentication_string = e.headers['www-authenticate']

print "Dumb Stuff"
print doc.read()
print "End Dumb Stuff"
