#Import the required Libraries
import numbers
from tkinter import *
from tkinter import ttk
import os
import json
import tkinter.messagebox

#Create an instance of Tkinter frame
win= Tk()

#Set the geometry of Tkinter frame
win.geometry("750x500")

userPath = ""

if os.stat("SlippiPath.txt") != 0:
    with open("SlippiPath.txt") as slipPath:
        userPath = slipPath.readline()


if userPath == "":
    labelU = Label(win, text="Enter User Path:", font=("Courier 15 bold"))
    labelU.pack()

    entryU = Entry(win, width= 40)
    entryU.focus_set()
    entryU.pack()

    if os.stat("SlippiPath.txt") != 0:
        userPath = entryU.get()

        with open("SlippiPath.txt", "a") as slipPath:   
            slipPath.write(entryU.get())
    else:
        tkinter.messagebox.showinfo("Incorrect File",  "Your chosen file path does not exist.")


def makeDo(list):
    newDict = {
        "uid" : list[2],
        "displayName" : list[6],
        "playKey" : list[10],
        "connectCode" : list[14],
        "latestVersion" : list[18]
    }
    json_object = json.dumps(newDict, indent = 5)

    with open(userPath, "w") as outfile:
        outfile.write(json_object)

    print(list)

if os.stat("SlippiStuff.txt") != 0:
    with open("SlippiStuff.txt") as slipFile:
        for line in slipFile:
            lSplit = line.split("+")
            eList = lSplit[1][2:len(lSplit[1]) - 1].split('"')
            e = Button(win, text=lSplit[0], font=("Courier 15 bold"), command=lambda j=eList: makeDo(j))
            e.pack(side = BOTTOM, pady=10)

def make_button():

    eList = entryD.get()[2:len(lSplit[1]) - 1].split('"')
    e = Button(win, text=entryN.get(), font=("Courier 15 bold"), command=lambda j=eList: makeDo(j))
    e.pack(side = BOTTOM, pady=10)

    with open("SlippiStuff.txt", "a") as slipPut:   
        slipPut.write(entryN.get() + "+" + entryD.get())

    

#Initialize a Label to display the User Input
labelN = Label(win, text="Name", font=("Courier 15 bold"))
labelN.pack()

entryN = Entry(win, width= 40)
entryN.focus_set()
entryN.pack()

labelD = Label(win, text="Data", font=("Courier 15 bold"))
labelD.pack()

#Create an Entry widget to accept User Input
entryD = Entry(win, width= 40)
entryD.focus_set()
entryD.pack()

#Create a Button to validate Entry Widget
ttk.Button(win, text= "Create New Account",width= 20, command=lambda : make_button()).pack(pady=5)

win.mainloop()