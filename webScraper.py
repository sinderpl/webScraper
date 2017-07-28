#Import the url library
import urllib2
#Import the regex matching pattern
import re
#HTML parser
from HTMLParser import HTMLParser

import glob


wordDictionary = dict({})
aplhabetDictionary = dict({"a" : 0 , "b" : 0, "c": 0 ,"d" : 0, "e" : 0, "f" : 0, "g" : 0,
"h" : 0, "i" : 0 , "j" : 0, "k" : 0, "l" : 0 , "m" : 0, "n" : 0, "o" : 0, "p": 0,
"q": 0, "r" : 0, "s" : 0, "t" : 0, "u" : 0, "v": 0, "w" : 0, "x" : 0,
 "y" : 0, "z" : 0})
longestWord = ""
commonLetter = "";

pattern = re.compile(r'([a-zA-Z]+)')

def addWordsFromLine( words):
    for word in words:
        if word in wordDictionary:
            wordDictionary[word] += 1
            #my_dict.get('corse') and my_dict.update({'corse': 'my definition'})
        else:
            wordDictionary[word] = 1
            #wordDictionary

# create a subclass and override the handler methods
class MyHTMLParser(HTMLParser):

    def handle_data(self, data):
        #F
        f = re.findall(pattern,data)
        if f:
            #print "New data: ", f
            addWordsFromLine(f)




# instantiate the parser and fed it some HTML
parser = MyHTMLParser()
data = urllib2.urlopen("http://testing-ground.scraping.pro/blocks")
#"http://webscraper.io/test-sites/e-commerce/allinone/computers")
#https://facebook.com")
#"http://testing-ground.scraping.pro/blocks")


for line in data:
    parser.feed(line)
   #print line+"\n ----------------------"

print "*---------------------------------------------*"
print "| Word                           |  WordCount |"
print "*---------------------------------------------*"
for word in wordDictionary.items():
    print "|%20s            |     %5d  |" % word
print "*---------------------------------------------*"
