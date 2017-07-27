#Import the url library
import urllib2
#Import the regex matching pattern
import re

data = urllib2.urlopen("http://testing-ground.scraping.pro/")
for line in data:
    print line+"\n ----------------------"
