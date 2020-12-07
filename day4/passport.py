#!/usr/bin/python

import re
with open("passports", "r") as f:
   data = f.read()
   lines = data.split("\n\n")
   valid = 0
   for read in lines:
      line = read + "\n"
      byr = re.search("byr:([1][9][2-9][0-9]|200[0-2])\s",line)
      iyr = re.search("iyr:(201[0-9]|2020)\s",line)
      eyr = re.search("eyr:(202[0-9]|2030)\s",line)
      hgt = re.search("hgt:(1([5-8][0-9]|[9][0-3])cm|((59)|[6][0-9]|[7][0-6])in)\s",line)
      hcl = re.search("hcl:#[0-9a-f]{6}\s",line)
      ecl = re.search("ecl:(amb|blu|brn|gry|grn|hzl|oth){1}(\s)",line)
      pid = re.search("pid:[0-9]{9}(\s)",line)


      if byr and iyr and eyr and hgt and hcl and ecl and pid:
         valid += 1

   print("%s passports valid" % valid)
