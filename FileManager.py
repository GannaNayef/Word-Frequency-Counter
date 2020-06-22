import glob
import os
import operator
from typing import Any

from Trie import *
import ctypes


class File:

    def __init__(self, name, root, wordCnt, mostRepeatedWord):
        self.name = name
        self.root = root
        self.wordCnt = wordCnt
        self.mostRepeatedWord = mostRepeatedWord



list_of_files = []

neglectedWords = open('neglectedWords.txt', 'r', encoding="utf8").read().split()

def loadFiles():
    count = 0
    for filePath in glob.glob('Files\\*.txt'):
        addFile(filePath, filePath[6:-4])
        count += 1
    return count
def wordCount():
    count = 0
    for i in list_of_files:
        count += i.wordCnt
    return count

def searchCount(word):
    count = 0
    for i in list_of_files:
        count += find(i.root, word)
    return count
def searchMed(word):
    arr = []
    for i in list_of_files:
        arr.append(find(i.root, word))
    arr.sort()
    if len(arr) % 2 != 0:
        return arr[len(arr)/2]
    else:
        return (arr[int(len(arr)/2)]+arr[(int(len(arr)/2))+1])/2
def searchMod(word):
    arr = {}
    for i in list_of_files:
        if(find(i.root, word) in arr):
            arr[find(i.root, word)] += 1
        else:
            arr[find(i.root, word)] = 1
    return max(arr.items(), key=operator.itemgetter(1))[0]
def addFile(filePath, fileName):

    if ~fileName.find(' '):
        ctypes.windll.user32.MessageBoxW(0, "File name can't contain white spaces", "Error", 1)
        return
    if os.path.isfile(filePath):
        if fileName != filePath[6:-4]:
            os.system('copy ' + filePath + ' Files\\' + fileName + '.txt')
        cnt = mxRepetition = 0
        mostReapetedWord = ''
        newRoot = Root()
        ff = open(filePath, 'r', encoding="utf8")
        for word in ff.read().split():
            temp = insert(newRoot, word)
            if temp > mxRepetition and word.lower() not in neglectedWords and len(word) > 2:
                mxRepetition = temp
                mostReapetedWord = word
            cnt += 1
        ff.close()
        list_of_files.append(File(fileName, newRoot, cnt, mostReapetedWord))
    else:
        ctypes.windll.user32.MessageBoxW(0, "File not found\nPlease make sure you enter the full path of the file", "Error", 1)


def deleteFile(fileName):

    for i in list_of_files:
        if i.name == fileName:
            del list_of_files[list_of_files.index(i)]
            os.system('del Files\\' + fileName + '.txt')
            ctypes.windll.user32.MessageBoxW(0, "Done\n", "", 1)
            return
    ctypes.windll.user32.MessageBoxW(0, "File not found\n", "Error", 1)
