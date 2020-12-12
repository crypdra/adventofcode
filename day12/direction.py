import re



def change_direction(direction, degree, current):
    current = current + direction * degree
    return int(current % 360)

def change_waypoint_direction(direction, degree, waypoint):
    new_waypoint = {0: 1, 90: 10, 180: 0, 270: 0}
    for key in waypoint.keys():
        new_waypoint[(key+direction*degree)%360] = waypoint[key]
    return new_waypoint
    
with open("directions", "r") as f:
    lines = f.readlines()
    current_direction = 90
    directions = {0: 0, 90: 0, 180: 0, 270: 0}
    direction_mapping = {"N": 0, "E": 90, "S": 180, "W": 270}
    for line in lines:
        match = re.search("(\w)(\d+)", line)
        if match:
            instruction, value = match.groups()
            value = int(value)
            if instruction == "R":
                current_direction = change_direction(1,value,current_direction)
            elif instruction == "L":
                current_direction = change_direction(-1,value,current_direction)
            elif instruction == "F":
                directions[current_direction] += value
            else:
                directions[direction_mapping[instruction]] += value

    print(abs(directions[0]-directions[180])+abs(directions[90]-directions[270]))
    ship_position = {0: 0, 90: 0, 180: 0, 270: 0}
    direction_mapping = {"N": 0, "E": 90, "S": 180, "W": 270}
    waypoint = {0: 1, 90: 10, 180: 0, 270: 0}

    for line in lines:
        match = re.search("(\w)(\d+)", line)
        if match:
            instruction, value = match.groups()
            value = int(value)
            if instruction == "R":
                waypoint = change_waypoint_direction(1,value,waypoint)
            elif instruction == "L":
                waypoint = change_waypoint_direction(-1,value,waypoint)
            elif instruction == "F":
                ship_position[0] += value * waypoint[0]
                ship_position[90] += value * waypoint[90]
                ship_position[180] += value * waypoint[180]
                ship_position[270] += value * waypoint[270]
            else:
                waypoint[direction_mapping[instruction]] += value
        print(waypoint)
    print(abs(ship_position[0]-ship_position[180])+abs(ship_position[90]-ship_position[270]))



