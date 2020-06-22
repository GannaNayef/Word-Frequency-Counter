from FileManager import *
import matplotlib.pyplot as plt

def plotHistogram(word):

    y = [find(i.root, word) for i in list_of_files]
    bins = [max(y)/10*i for i in range(15)]

    plt.hist(y, bins, histtype='bar', rwidth=0.8)

    plt.xlabel('Word Frequency')
    plt.ylabel('Number of Files')

    plt.show()


def plotPieChart(word):

    x = [i.name for i in list_of_files if find(i.root, word)>0]
    y = [find(i.root, word) for i in list_of_files if find(i.root, word)>0]

    plt.pie(y, labels=x, shadow=1, autopct='%1.1f%%')

    plt.show()
