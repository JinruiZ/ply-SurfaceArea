import os
import numpy
import math
import json
from plyfile import PlyData

# Set the path to store data file.
dataStorePath = "./"

# Set file's name to store data
dataFileName = "test"

def main():
    path = "./" #Folder's path
    files = os.listdir(path) #Get all files under this folder
    plyList = []
    surfaceArea = []

    for f in files:
        if not os.path.isdir(f) and os.path.splitext(f)[1] == ".ply":
            plyList.append(f)

    plyList.sort(key = lambda x: int(x[:-4]) )

    if plyList == []:
        raise Exception("No PLY file in this folder.")
    else:
        #Calculate surface area and store it in array
        for ply in plyList:
            surfaceArea.append(plyReader(ply))

        # Restore the file name for plot
        surfaceArea.append(dataFileName)
        with open(dataStorePath + dataFileName + ".json", "w") as writeFile:
             json.dump(surfaceArea, writeFile)
             print("Data has been stored.")
    return 

def plyReader(ply_filename):
    data = PlyData.read(ply_filename)
    total_area = 0

    if 'face' in data:
        faces = data['face']
        verteices = data['vertex']
        for f in faces['vertex_indices']:
            tri = Triangel(verteices[f[0]], verteices[f[1]], verteices[f[2]])
            total_area += tri.area
    return total_area

class Triangel():
     def __init__(self, vertex_a, vertex_b, vertex_c):
         self.va = vertex_a
         self.vb = vertex_b
         self.vc = vertex_c
         self.sa = 0
         self.sb = 0
         self.sc = 0
         self.area = 0
         self.SideClaculator()
         self.AreaCalculator()

     def SideClaculator(self):
         def LengthCal(a, b):
             length = math.sqrt(pow((a[0] - b[0]), 2) + pow((a[1] - b[1]), 2) + pow((a[2] - b[2]), 2))
             return length

         self.sa = LengthCal(self.vb, self.vc)
         self.sb = LengthCal(self.va, self.vc)
         self.sc = LengthCal(self.va, self.vb)

     def AreaCalculator(self):
         if self.sa + self.sb <= self.sc or self.sb + self.sc <= self.sa or self.sa + self.sc <= self.sb:
             print(self.va, self.vb, self.vc)
             raise Exception("Triangel can not be made up.")
         else:
             p = 0.5 * (self.sa + self.sb + self.sc)
             self.area = math.sqrt(p * (p - self.sa) * (p - self.sb) * (p - self.sc))

main()