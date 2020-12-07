#!/usr/bin/python
import re
import numpy as np

with open("map", "r") as f:
   slopes = []
   with open("slopes", "r") as g:
      for line in g.readlines():
         match = re.search("Right (\d), down (\d).", line.strip())
         if match: right, down = match.groups()
         slopes.append({"right": int(right), "down": int(down)})

   matrix = []
   treeC = []
   openC = 0
   for line in f.readlines():
      matrix.append(line.strip())

   for slope in slopes:
      treeCtmp = 0
      for cur in range(1, len(matrix)):
         y = (cur*slope["right"])%len(matrix[0])      
         x = cur*slope["down"]
         if x >=len(matrix): break
#         print("%s %s: %s" % (x, y+1, matrix[x][y]))
         if(matrix[x][y] == "#"): treeCtmp += 1
      treeC.append(treeCtmp)
   treeC = np.array(treeC)
   print(treeC.prod())
