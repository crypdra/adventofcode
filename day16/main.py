import re
import numpy as np

with open("puzzle", "r") as f:
    lines = f.readlines()
    key = 0
    valid_numbers = {}
    for key, line in enumerate(lines):
        match_fields = re.findall("(\d+)-(\d+)", line)
        if match_fields:
            classname = re.search("(\w+ *\w+): ", line)
            classname = classname.groups()[0]
            if not classname in valid_numbers:
                valid_numbers[classname] = []
            for field_range in match_fields:
                for number in range(int(field_range[0]), int(field_range[1])+1):
                    valid_numbers[classname].append(number)
        if "your ticket" in line:
            break
        if "nearby" in line:
            break
    key += 1
    my_ticket = [int(item) for item in lines[key].strip().split(",")]
    key += 3

    invalid = []
    pos_position = {}
    neg_position = {}
    pos_to_pop = []
    tickets = []
    for key2 in range(key, len(lines)):
        ticket_fields = [int(field) for field in lines[key2].strip().split(",")]
        tickets.append(ticket_fields)
        for pos, field in enumerate(ticket_fields):
            found = False
            for classname in valid_numbers:
                if field in valid_numbers[classname]:
                    found = True
            if not found:
                pos_to_pop.append(len(tickets)-1)
                invalid.append(field)
                
    for pop in sorted(pos_to_pop, reverse=True):
        tickets.pop(pop)

    for key2 in range(0, len(tickets)):
        ticket_fields = tickets[key2]
        for pos, field in enumerate(ticket_fields):
            found = False
            for classname in valid_numbers:
                if field in valid_numbers[classname]:
                    if not pos in pos_position:
                        pos_position[pos] = []
                    if classname not in pos_position[pos] and (pos not in neg_position or classname not in neg_position[pos]):
                        pos_position[pos].append(classname)
                    found = True
                else:
                    if pos in pos_position and classname in pos_position[pos]:
                        pos_position[pos].remove(classname)
                    if not pos in neg_position:
                        neg_position[pos] = []
                    neg_position[pos].append(classname)
            if not found:
                pos_to_pop.append(len(tickets)-1)
                invalid.append(field)
    positions = {}
    while(True):
        items = np.array([len(item[1]) for item in pos_position.items()])

        mask = (items[:] > 0)
        if len(items[mask][:]) == 0:
            break
        argmin = np.argmin(items[mask][:])
        argmin = np.arange(items.shape[0])[mask][argmin]
        positions[argmin] = pos_position[argmin][0]
        remove = pos_position[argmin][0]
        for key in pos_position:
            if remove in pos_position[key]:
                pos_position[key].remove(remove)
    product = np.prod([my_ticket[position] for position in positions if "departure" in positions[position]])
    #for position in positions:
    #    if("departure" in positions[position]):
    #        product *= my_ticket[position]

    print("Part One: %s" % np.array(invalid).sum())
    print("Part Two: %s" % product)