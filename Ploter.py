import os
import numpy
import math
import json
import random
import matplotlib.pyplot as plt

path = "./" #Folder's path

def main():
    fileList = FileFilter()
    data = JsonReader(fileList)
    Ploter(data)
    return

# Filter out .json files
def FileFilter():
    files = os.listdir(path) #Get all files under this folder
    fileList = []

    for f in files:
        if not os.path.isdir(f) and os.path.splitext(f)[1] == ".json":
            fileList.append(f)

    if fileList == []:
        raise Exception("No Json file in this folder.")
    else:
        return fileList

# Store all of data in an array
def JsonReader(fileList):
    dataList = []
    for f in fileList:
        with open(path + f, 'r') as jfile:
            data = json.load(jfile)
            dataList.append(data)
    return dataList
    
# Plot and show
def Ploter(data):
    for d in data:
        label = d.pop()
        xaxis = numpy.linspace(0, len(d), len(d))
        plt.plot(xaxis, d, marker = '.', label = label)
    plt.legend()
    plt.ylabel("Surface area")
    plt.xlabel("Time")
    plt.savefig('./figure.png', dpi = 1080)
    return

main()