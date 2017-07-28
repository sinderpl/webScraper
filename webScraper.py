#Import the url library
import urllib2
#Import the regex matching pattern
import re
#HTML parser
from HTMLParser import HTMLParser


#Stores the words as keys and their occurence counter as the value
wordDictionary = dict({})
#Stores letters for now, the values will be updated to determine the
# most occuring letter
aplhabetDictionary = dict({"a" : 0 , "b" : 0, "c": 0 ,"d" : 0, "e" : 0, "f" : 0, "g" : 0,
"h" : 0, "i" : 0 , "j" : 0, "k" : 0, "l" : 0 , "m" : 0, "n" : 0, "o" : 0, "p": 0,
"q": 0, "r" : 0, "s" : 0, "t" : 0, "u" : 0, "v": 0, "w" : 0, "x" : 0,
 "y" : 0, "z" : 0})
 #Stores the current longest word
longestWord = ""
#Stores the current most occuring letter
commonLetter = "";
#The regex pattern that matches words, pre compiled for later use
pattern = re.compile(r'([a-zA-Z]+)')


#Checks whether the words are already in dictionary
# If true it updates to the counter to the new value
# If false it adds the word with a initial count of 1
def addWordsFromLine( words):
    #Iterate through the words as they come in as a array
    #from the regex
    for word in words:
        #If the word is already in there update its occurence counter
        if word in wordDictionary:
            wordDictionary[word] += 1
            #wordDictionary.get(word) and wordDictionary.update({word: wordDictionary[word]+1})
        #Otherwise add the word and initialize with a value of 1
        else:
            wordDictionary[word] = 1

#Prints the output of the wordDictionary in a pretty format
def printDictionaryWords(dictionary):
    print "*---------------------------------------------*"
    print "| Word                           |  WordCount |"
    print "*---------------------------------------------*"
    #Iterate through each word and print the key and value
    for word in dictionary.items():
        print "|%20s            |     %5d  |" % word
    print "*---------------------------------------------*"

# Override of handler methods for the parser
class MyHTMLParser(HTMLParser):

    #We are only concerned with text data so every other tag is ignored
    def handle_data(self, data):
        #Find all of the words matching the regex in the data
        f = re.findall(pattern,data)
        #If the return list is not empty start adding them to the dictionary
        #Through the custom method
        if f:
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

#Call on the print method
printDictionaryWords(wordDictionary)
