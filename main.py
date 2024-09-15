import tkinter as tk
import tkinter.font as tkFont
from tkinter import ttk


class ToDoList(tk.Tk):

    def __init__(self,titleOfApp,borderSize):

        #Main setup
        #Set up the window by initializing the title, and dimentions of the window using the borderSize tuple
        super().__init__()
        self.title(titleOfApp)
        self.geometry(f'{borderSize[0]}x{borderSize[1]}')
        self.minsize(borderSize[0],borderSize[1])

        # widgets
        self.main = MainFrame(self)

        #run app
        self.mainloop()

class MainFrame(ttk.Frame):
    #Basically equal to MainFrame = tk.frame(TodoList)
    def __init__(self, parent):
        super().__init__(parent)
        self.place(x=0,y=0)
        self.currentTaskList: int = 1

        self.createWidgets()

    def createWidgets(self):
        self.testFont = tkFont.Font(family="Times", size=16)
        self.checkbutton = tk.Checkbutton(self)
        self.textEntry = tk.Entry(self, font=self.testFont)
        self.addListItemButton = tk.Button(self, text= "+", command=self.addListItem)

        #create grid
        self.rowconfigure((0,1,2,3,4),weight=1)
        self.columnconfigure((0,1,2,3), weight=1)

        #place widgets
        self.checkbutton.grid(row=0,column=0)
        self.textEntry.grid(row=0,column=1, sticky=tk.W+tk.E)
        self.addListItemButton.grid(row=0,column=2,)

    def addListItem(self):
        print(self.currentTaskList)
        for i in range(self.currentTaskList-1,self.currentTaskList):
            self.checkbutton = tk.Checkbutton(self)
            self.checkbutton.grid(row=i+1,column=0)
            self.textEntry = tk.Entry(self, font=self.testFont)
            self.textEntry.grid(row=i+1,column=1, sticky=tk.W+tk.E)
        self.currentTaskList+=1



ToDoList('The jankiest GUI known to man', (400,400))