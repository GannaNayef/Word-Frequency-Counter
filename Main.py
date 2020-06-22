from tkinter import *
from DataVisualization import *
from FileManager import *

root = Tk()
root.title("Word Frequancy Counter")

root.geometry('400x400')

nFiles = loadFiles()


def searchFrame():
    frame1.pack_forget()
    frame2 = Frame(root)
    frame2.pack()
    nLabel = Label(frame2, text="Word : ")
    nLabel.pack(side=LEFT)
    wordText = Text(frame2, height=1, width=10)
    wordText.pack()
    pieButton = Button(frame2, height=1, width=12, text="Show Pie Chart", command=lambda: plotPieChart(wordText.get("1.0", "end-1c")))
    pieButton.pack()
    histoButton = Button(frame2, height=1, width=12, text="Show Histogram", command=lambda: plotHistogram(wordText.get("1.0", "end-1c")))
    histoButton.pack()
    meanButton = Button(frame2, height=1, width=10, text="Show Mean", command=lambda: ctypes.windll.user32.MessageBoxW(0, str(float(searchCount(wordText.get("1.0", "end-1c"))) / float(nFiles)), "Mean", 1))
    meanButton.pack()
    medButton = Button(frame2, height=1, width=10, text="Show Median", command=lambda: ctypes.windll.user32.MessageBoxW(0, str(searchMed(wordText.get("1.0", "end-1c"))), "Median", 1))
    medButton.pack()
    modButton = Button(frame2, height=1, width=10, text="Show Mod", command=lambda: ctypes.windll.user32.MessageBoxW(0, str(searchMod(wordText.get("1.0", "end-1c"))),"Mod", 1))
    modButton.pack()
    backButton1 = Button(frame2, height=1, width=10, text="Back", command=lambda: backToTheMain(frame2))
    backButton1.pack(side=BOTTOM)


def addFrame():
    frame1.pack_forget()
    frame2 = Frame(root)
    frame2.pack()
    pathLabel = Label(frame2, text="File Path : ")
    pathLabel.pack()
    pathText = Text(frame2, height=1, width=10)
    pathText.pack()
    fNameLabel = Label(frame2, text="File Name : ")
    fNameLabel.pack()
    fNameText = Text(frame2, height=1, width=10)
    fNameText.pack()
    addButton = Button(frame2, height=1, width=10, text="Add", command=lambda: addFile(pathText.get("1.0", "end-1c"), fNameText.get("1.0","end-1c")))
    addButton.pack()
    backButton2 = Button(frame2, height=1, width=10, text="Back", command=lambda: backToTheMain(frame2))
    backButton2.pack(side=BOTTOM)
    nFiles += 1

def remFrame():
    frame1.pack_forget()
    frame2 = Frame(root)
    frame2.pack()
    remLabel = Label(frame2, text="File Name")
    remLabel.pack()
    remText = Text(frame2, height=1, width=10)
    remText.pack()
    remButton = Button(frame2, height=1, width=10, text="Delete", command=lambda: deleteFile(remText.get("1.0", "end-1c")))
    remButton.pack()
    backButton3 = Button(frame2, height=1, width=10, text="Back", command=lambda: backToTheMain(frame2))
    backButton3.pack(side=BOTTOM)
    nFiles -= 1

def backToTheMain(frame):
    frame.destroy()
    frame1.pack()


frame1 = Frame(root)
frame1.pack()
searchButton = Button(frame1, height=1, width=10, text="Search", command=lambda: searchFrame())
searchButton.pack()
addButton = Button(frame1, height=1, width=10, text="Add File", command=lambda : addFrame())
addButton.pack()
remButton = Button(frame1, height=1, width=10, text="Remove File", command=lambda : remFrame())
remButton.pack()
root.mainloop()
