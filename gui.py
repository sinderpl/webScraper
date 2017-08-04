import Tkinter
from webScraper import webScraper
from Tkinter import *
import ttk

class simpleapp_tk(Tkinter.Tk):

    def __init__(self,parent):
        Tkinter.Tk.__init__(self,parent)
        self.parent = parent
        self.initialize()
        self.webScraper = webScraper()


    def initialize(self):
        #Set up the grid and window size
        self.grid()
        self.geometry("650x500")

        #Set up the link entry area
        self.labelAdress = Label(self,text = "Please enter the link you wish to scrape: ")
        self.labelAdress.grid()
        self.labelAdress.grid(column=0,row=0,sticky='EW')
        self.linkVariable = Tkinter.StringVar()
        self.linkVariable.set(u"http://testing-ground.scraping.pro")
        self.linkEntry = Tkinter.Entry(self,textvariable=self.linkVariable)
        self.linkEntry.grid(column=0,row=1,sticky='EW')

        #Set up the button
        self.scrapeButton = Tkinter.Button(self,text="Scrape the web",
                                command=self.scrapeButtonClick)
        self.scrapeButton.grid(column=1, row=1)



    def scrapeButtonClick(self):
        self.webScraper.runParser(self.linkEntry.get())


        #Show the most common letter count
        commonLetterStr = "The most common letter is: %s with a count of: %d" % (self.webScraper.getCommonLetter())
        self.commonLetterLabel = Label(self, text = commonLetterStr)
        self.commonLetterLabel.grid(column=0,row=2,sticky='EW')

        #Show the longest word
        longestWordStr = "The longest word is: %s with a letter count of: %d" %(self.webScraper.getLongestWord())
        self.longestWordLabel = Label(self,  text = longestWordStr)
        self.longestWordLabel.grid(column=0, row=3, sticky="EW")

        #Show the words and their occurence countLetters
        #self.listBoxWords = Listbox(self, height= 30, width = 50)
        #for word in self.webScraper.getWordDictionary():
        #    tempString = "  %s       %15d" %(self.webScraper.getWordCount(word))
        #    self.listBoxWords.insert(0,tempString)
        #self.listBoxWords.grid(column=0, row=4, sticky="SW")
        tree = ttk.Treeview()
        tree["columns"] = ("one")
        tree.column("one", width = 20)
        tree.heading("one", text="Word Occurence: ")
        for word in self.webScraper.getWordDictionary():
            tree.insert("", 0,text=word,  values=(self.webScraper.getWordCount(word)))
            #tempString = "  %s       %15d" %(self.webScraper.getWordCount(word))
            #self.listBoxWords.insert(0,tempString)
        tree.grid(column=0, row=4, sticky="EW")
        #Reset the scraper data for the next possible search
        self.webScraper.reset()

if __name__ == "__main__":
    app = simpleapp_tk(None)
    app.title('Web Scraper')
    app.mainloop()
