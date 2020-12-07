#!/usr/bin/python

max_row = 127
min_row = 0

max_seat = 7
min_seat = 0

with open("seats", "r") as f:
   max_nr = 0
   nrs = []
   for line in f.readlines():
      max_row = 127
      min_row = 0
      max_seat = 7
      min_seat = 0

      for key, letter in enumerate(line):
         if key <= 6: 
            if letter == "F": 
               max_row = min_row + (max_row-min_row) // 2
            if letter == "B":
               min_row = min_row + (max_row-min_row+1) // 2 
         else:
            if letter == "L":
               max_seat = min_seat + (max_seat-min_seat) // 2
            if letter == "R":
               min_seat = min_seat + (max_seat-min_seat+1) // 2

      row = max_row
      seat = max_seat
      seat_nr = row * 8 + seat
      nrs.append(seat_nr)
      if seat_nr > max_nr: max_nr = seat_nr 
      print("Row: %s, Column: %s" % (row, seat))
   print("Max: %s" % max_nr)

nrs = sorted(nrs)
for key, element in enumerate(nrs):
   if key > 0 and key < len(nrs)-1:
      if element - 2 == nrs[key-1]:
        print("My seat: %s" % (element-1))
