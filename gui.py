from Tkinter import *
import webScraper

webScraper.main()
root = Tk()
root.title("Web Scraper")
listb = Listbox(root)


li = 'Carl Patrick Lindsay Helmut Chris Gwen'.split()

for word in webScraper.getWordDictionary():
    listb.insert(END,word)

listb.delete(0, END)
listb.pack()
root.mainloop()
