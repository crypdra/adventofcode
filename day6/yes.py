with open("answers", "r") as f:
   data = f.read()
   groups = data.split("\n\n")
   yes_sum = 0
   yes_sum_excl = 0
   for group in groups:
      yes_arr = []
      yes_excl_arr = []
      for person in group.strip().split("\n"):
         yes_arr_person = []
         for answer in person.strip():
            if answer not in yes_arr:
               yes_arr.append(answer)
            yes_arr_person.append(answer)
         yes_excl_arr.append(yes_arr_person)
      intersection = yes_excl_arr[0]
      for person in yes_excl_arr:
         intersection = list(set(intersection).intersection(person)) 
      yes_sum += len(yes_arr)
      yes_sum_excl += len(intersection) 
   print("Sum per group: %s" % yes_sum)
   print("Intersection per group: %s" % yes_sum_excl)
