#Import the url library
import urllib2
#Import the regex matching pattern
import re
#HTML parser
from HTMLParser import HTMLParser
import operator


#The regex pattern that matches words, pre compiled for later use
pattern = re.compile(r'([a-zA-Z]+)')
#Needed for reference by the HTML parser
#Not the most elegant but will do
scrap = None

# Override of handler methods for the parser
class MyHTMLParser(HTMLParser):

    #We are only concerned with text data so every other tag is ignored
    def handle_data(self, data):
        #Find all of the words matching the regex in the data
        results = re.findall(pattern,data)
        #If the return list is not empty start adding them to the dictionary
        #Through the custom method
        if results:
            scrap.addWordsFromLine(results)

class webScraper():
    def __init__(self):
        # used for referencey by the html parser
        global scrap
        scrap = self
        #Stores the words as keys and their occurence counter as the value
        self.wordDictionary = dict({})
        #Stores letters for now, the values will be updated to determine the
        # most occuring letter
        self.alphabetDictionary  = dict({})
         #Stores the current longest word
        self.longestWord = ""
        #Stores the current most occuring letter
        self.mostCommonLetter = "";

    # Resets the values to empty so that you can run the scraper again
    def reset(self):
        self.longestWord = ""
        self.mostCommonLetter = ""
        self.alphabetDictionary = dict({})
        self.wordDictionary = dict ({})


    #Checks whether the words are already in dictionary
    # If true it updates to the counter to the new value
    # If false it adds the word with a initial count of 1
    def addWordsFromLine(self, words):
        #Iterate through the words as they come in as a array
        #from the regex
        for word in words:
            #If the word is already in there update its occurence counter
            if word in self.wordDictionary:
                self.wordDictionary[word] += 1
                #self.wordDictionary.get(word) and self.wordDictionary.update({word: self.wordDictionary[word]+1})
            #Otherwise add the word and initialize with a value of 1
            else:
                self.wordDictionary[word] = 1
                #Check whether the word is longer than the current longest on
                if len(word) > len(self.longestWord):
                    self.longestWord = word
            self.countLetters(word)

    #Counts the letters in each word and adds them to corresponding keys in a dictionary
    def countLetters(self, word):
        #Makes sure the characters are uniform
        word = word.lower()
        for char in word:
            #Adds to the key value count if it is already in the dictionary
            if char in self.alphabetDictionary:
                self.alphabetDictionary[char] += 1
            #Adds the new key to the dictionary with inital value of 1
            else:
                self.alphabetDictionary[char] = 1

    def findCommonLetter(self):
        self.mostCommonLetter = max(self.alphabetDictionary.iteritems(), key=operator.itemgetter(1))[0]

    #Prints the output of the self.wordDictionary in a pretty format
    def prettyPrint(self):
        print "             *Welcome to the web scraper* "
        print "\n*---------------------------------------------*"
        print "| Word                           |  WordCount |"
        print "*---------------------------------------------*"
        #Iterate through each word and print the key and value
        for word in self.wordDictionary.items():
            print "|%20s            |     %5d  |" % (word)
        print "*---------------------------------------------*"
        print "| Most common letter: %5s   | Count: %5d  |" % (self.mostCommonLetter, self.alphabetDictionary[self.mostCommonLetter])
        print "*---------------------------------------------*"
        print "| Longest Word: %20s          |" % (self.longestWord)
        print "*---------------------------------------------*"


    #Run Method
    def runParser(self, link):
        # Instantiate the parser and feed it some HTML
        parser = MyHTMLParser()

        #Copy the data from the website specified
        data = urllib2.urlopen(link)
        #The code is usually split into lines so we send it on line by line to the parser
        for line in data:
            results = parser.feed(line)
        #Find the common Letter in all the data
        self.findCommonLetter()
        #self.prettyPrint()

    #Getters
    def getCommonLetter(self):
        return self.mostCommonLetter, self.alphabetDictionary[self.mostCommonLetter]

    def getLongestWord(self):
        return self.longestWord, len(self.longestWord)

    def getWordDictionary(self):
        return self.wordDictionary

    def getWordCount(self, word):
        return self.wordDictionary[word]


    #Main Method
    def main(self):
        #Run the parser
        self.runParser("http://testing-ground.scraping.pro/blocks")

        # Test scraping websites
        #"http://webscraper.io/test-sites/e-commerce/allinone/computers")
        #"http://testing-ground.scraping.pro/blocks")

        #Call on the print method
        self.prettyPrint()

#scraper = webScraper()
#scraper.main()
