#Import the url library
import urllib2
#Import the regex matching pattern
import re
#HTML parser
from HTMLParser import HTMLParser
import operator

#Stores the words as keys and their occurence counter as the value
wordDictionary = dict({})
#Stores letters for now, the values will be updated to determine the
# most occuring letter
alphabetDictionary = dict({"a" : 0 , "b" : 0, "c": 0 ,"d" : 0, "e" : 0, "f" : 0, "g" : 0,
"h" : 0, "i" : 0 , "j" : 0, "k" : 0, "l" : 0 , "m" : 0, "n" : 0, "o" : 0, "p": 0,
"q": 0, "r" : 0, "s" : 0, "t" : 0, "u" : 0, "v": 0, "w" : 0, "x" : 0,
 "y" : 0, "z" : 0})
 #Stores the current longest word
longestWord = ""
#Stores the current most occuring letter
mostCommonLetter = "";
#The regex pattern that matches words, pre compiled for later use
pattern = re.compile(r'([a-zA-Z]+)')


#Checks whether the words are already in dictionary
# If true it updates to the counter to the new value
# If false it adds the word with a initial count of 1
def addWordsFromLine(words):
    global longestWord
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
            #Check whether the word is longer than the current longest on
            if len(word) > len(longestWord):
                longestWord = word
        countLetters(word)

#Counts the letters in each word and adds them to corresponding ones
def countLetters(word):
    #TODO Could be updated to add chars to the dictionary as you go along
    word = word.lower()
    for char in word:
        alphabetDictionary[char] += 1

def findCommonLetter(dictionary):
    global mostCommonLetter
    mostCommonLetter = max(dictionary.iteritems(), key=operator.itemgetter(1))[0]
    print mostCommonLetter

#Prints the output of the wordDictionary in a pretty format
def prettyPrint(dictionary):
    print "\n*---------------------------------------------*"
    print "| Word                           |  WordCount |"
    print "*---------------------------------------------*"
    #Iterate through each word and print the key and value
    for word in dictionary.items():
        print "|%20s            |     %5d  |" % (word)
    print "*---------------------------------------------*"
    print "| Most common letter: %5s   | Count: %5d  |" % (mostCommonLetter, alphabetDictionary[mostCommonLetter])
    print "*---------------------------------------------*"
    print "| Longest Word: %20s          |" % (longestWord)
    print "*---------------------------------------------*"




# Override of handler methods for the parser
class MyHTMLParser(HTMLParser):

    #We are only concerned with text data so every other tag is ignored
    def handle_data(self, data):
        #Find all of the words matching the regex in the data
        results = re.findall(pattern,data)
        #If the return list is not empty start adding them to the dictionary
        #Through the custom method
        if results:
            addWordsFromLine(results)

#Run Method
def runParser():
    # Instantiate the parser and feed it some HTML
    parser = MyHTMLParser()

    #Copy the data from the website specified
    data = urllib2.urlopen("http://testing-ground.scraping.pro/blocks")

    # Test scraping websites
    #"http://webscraper.io/test-sites/e-commerce/allinone/computers")
    #"http://testing-ground.scraping.pro/blocks")

    for line in data:
        parser.feed(line)

#Main Method
def main():

    print "             *Welcome to the web scraper* "

    #Run the parser
    runParser()

    #Find the common Letter
    findCommonLetter(alphabetDictionary)

    #Call on the print method
    prettyPrint(wordDictionary)

if __name__ == "__main__": main()
