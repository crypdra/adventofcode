#!/usr/bin/python

with open("numbers", "r") as f:
   lines = f.readlines()
   for key, number in enumerate(lines):
      for key2 in range(key+1, len(lines)):
         number2 = lines[key2]
         if(int(number) + int(number2) == 2020): print("Two numbers: %s" % (int(number)*(int(number2)))) 
         for key3 in range(key2+1, len(lines)):
            number3 = lines[key3]
            if(int(number) + int(number2) + int(number3) == 2020): print("Three numbers: %s" % (int(number)*(int(number2)*int(number3))))  
        
