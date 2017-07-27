#Import the url library
import urllib2
#Import the regex matching pattern
import re
#HTML parser
from HTMLParser import HTMLParser





# create a subclass and override the handler methods
class MyHTMLParser(HTMLParser):
    def handle_data(self, data):
        print "Encountered some data  :", data

# instantiate the parser and fed it some HTML
parser = MyHTMLParser()
data = urllib2.urlopen("http://testing-ground.scraping.pro/blocks")


for line in data:
    parser.feed(line)
   #print line+"\n ----------------------"
