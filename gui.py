import Tkinter
import webScraper
from Tkinter import *




class simpleapp_tk(Tkinter.Tk):

    def __init__(self,parent):
        Tkinter.Tk.__init__(self,parent)
        self.parent = parent
        self.initialize()

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
