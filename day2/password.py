#!/usr/bin/python
import re
import sys

with open("passwords", "r") as f:
   valid = 0
   valid_2nd = 0
   for line in f.readlines():
      match = re.search('(\d+)-(\d+) (\w): (\w+)', line)
      if not match: sys.exit(0)
      minC, maxC, letter, password = match.groups()
      if(password.count(letter) >= int(minC) and password.count(letter) <= int(maxC)):
         valid += 1
      if((password[int(minC)-1] == letter) ^ (password[int(maxC)-1] == letter)):
         valid_2nd += 1
   print(valid)
   print(valid_2nd)
