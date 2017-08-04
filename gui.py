import Tkinter
from webScraper import webScraper
from Tkinter import *




class simpleapp_tk(Tkinter.Tk):

    def __init__(self,parent):
        Tkinter.Tk.__init__(self,parent)
        self.parent = parent
        self.initialize()
        self.webScraper = webScraper()

    def initialize(self):
        #Set up the grid and window size
        self.grid()
        self.geometry("800x800")



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
        '''
        listb = Listbox(root)


        for word in webScraper.getWordDictionary():
            tempString = "%"
            listb.insert(END,)

        #Delete the list
        #listb.delete(0, END)
        #listb.pack()
        '''

if __name__ == "__main__":
    #Call the scraper
    #webScraper.main()
    app = simpleapp_tk(None)
    app.title('Web Scraper')
    app.mainloop()
