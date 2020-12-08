#!/usr/bin/python

import re

def check_code(data):
   read_lines = [0] * len(data)
   pointer = 0
   acc = 0
   last_pointer = 0
   while(True):
      if pointer >= len(data):
         return True, acc
      elif read_lines[pointer] > 0:
         return False, acc
      else:
         read_lines[pointer] += 1
      last_pointer = pointer
      match = re.search("(nop|acc|jmp) ([+|-])(\d+)", data[pointer])
      if(match): instruction, sign, argument = match.groups()
      if instruction == "acc":
         acc = acc + int(argument) if sign == "+" else acc - int(argument)
         pointer += 1
      elif instruction == "jmp":
         pointer = pointer + int(argument) if sign == "+" else pointer - int(argument)
      elif instruction == "nop":
         pointer += 1

with open("code", "r") as f:
   ### PART ONE
   data = f.readlines()
   _, acc = check_code(data) 
   print(acc) 

   ### PART TWO
   for key, line in enumerate(data):
      orig_line = line
      match = re.search("(nop|acc|jmp) ([+|-])(\d+)", line)
      if(match): instruction, sign, argument = match.groups() 
      if instruction == "jmp": data[key] = line.replace("jmp", "nop")
      elif instruction == "nop": data[key] = line.replace("nop", "jmp") 
      succ, acc = check_code(data) 
      if succ: print(acc)
      data[key] = orig_line

