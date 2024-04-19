from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import os
from subprocess import call
import sys
import csv

def about():
    messagebox.showinfo('About', 'SBS System\nVersion 1.1\n\nCreated by: Lipani Technologies LLC\n\nContact: 1-570-815-3774\n\nEmail: brandon@technologies.com\n\nWebsite: https://lipanitech.com')

  
root = Tk() 
root.geometry("700x450") 
root.title("PYWriter") 
#root.minsize(height=250, width=350) 
#root.maxsize(height=250, width=350) 
  
  
# adding scrollbar 
scrollbar = Scrollbar(root) 
  
# packing scrollbar 
scrollbar.pack(side=RIGHT, 
               fill=Y) 
  
  
text_info = Text(root, 
                 yscrollcommand=scrollbar.set) 
text_info.pack(fill=BOTH)
  
# configuring the scrollbar 
scrollbar.config(command=text_info.yview) 

#Toolbar
toolbar = Frame(root)
insertBut = Button(toolbar, text='Insert Image', command='').pack(side=LEFT, padx=2, pady=2)
insertBut = Button(toolbar, text='Insert Table', command='').pack(side=LEFT, padx=2, pady=2)
insertBut = Button(toolbar, text='Insert Chart', command='').pack(side=LEFT, padx=2, pady=2)
printBut = Button(toolbar, text='Print', command='').pack(side=LEFT, padx=2, pady=2)
toolbar.pack(side=TOP, fill=X)

#status Bar
status = Label(root, text='Preparing to do nothing...', bd=1, relief=SUNKEN, anchor=W)
status.pack(side=BOTTOM, fill=X)

#menu Bar
menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Open", command='')
filemenu.add_command(label="Save", command='')
filemenu.add_command(label="Save As", command='')
filemenu.add_separator()
filemenu.add_command(label="Exit", command=quit)
menubar.add_cascade(label="File", menu=filemenu)

exportsmenu = Menu(menubar, tearoff=0)
exportsmenu.add_command(label="Undo", command='')
exportsmenu.add_command(label="Copy", command='')
exportsmenu.add_command(label="Paste", command='')
exportsmenu.add_command(label="Delete", command='')
exportsmenu.add_separator()
exportsmenu.add_command(label="Print", command='')
exportsmenu.add_command(label="Save As PDF", command='')
exportsmenu.add_command(label="Find", command='')
menubar.add_cascade(label="Edit", menu=exportsmenu)

helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="About...", command=about)
menubar.add_cascade(label="Help", menu=helpmenu)

#root.title('PyWriter')
#root.geometry('700x450')

#write table to csv

#start program
root.config(menu=menubar)
root.mainloop()

#https://www.youtube.com/watch?v=D24Vx3_IM8U&t=116s
