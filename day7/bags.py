#!/usr/bin/python

class Color:
   colors = {}

   def __init__(self, name, childList):
      self.children = []
      self.children_count = []
      self.name = name
      for child in childList.keys():
         self.addChild(child, childList[child])
   def addChild(self, child, count):
      if(child not in self.colors):
         self.colors[child] = Color(child, {})
      self.children.append(self.colors[child])
      self.children_count.append(count)
   def isGold(self):
      return True if self.name == "shiny gold" else False
   def childIsGold(self):
      for child in self.children:
         if(child.isGold()): 
            return True
         else:
            if child.childIsGold(): return True
      return False 
   def bagCount(self):
      count = 0
      for key, child in enumerate(self.children):
         childCount = int(self.children_count[key])
         count += childCount * (1+child.bagCount())
      return count

with open("rules", "r") as f:
   for line in f.readlines():
      parent = line.split(" bags")[0]
      childrenList = line.split("contain")[1].strip().split(",")
      children = {}
      if "contain no other bags" in line:
         continue
      for child in childrenList:
         childCandidate = child.strip().split(" ")
         children[childCandidate[1] + " " + childCandidate[2]] = childCandidate[0] 
      if parent in Color.colors:
          for child in children.keys():
             Color.colors[parent].addChild(child, children[child])
      else:
          Color.colors[parent] = Color(parent, children)

count = 0
for color in Color.colors.keys():
   hasGold = Color.colors[color].childIsGold()
   if hasGold: count += 1
print("%s bags contain shiny gold bag" % count)
print("Shiny gold bags contain %s bags" % Color.colors["shiny gold"].bagCount())
