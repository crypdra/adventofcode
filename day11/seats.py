from copy import deepcopy

def is_empty_seat(layout, row, seat):

    adjacent_seats = [{"x": -1, "y": 0},{"x": -1, "y": -1},{"x": -1, "y": 1},{"x": 1, "y": -1},{"x": 1, "y": 0},{"x": 1, "y": 1},{"x": 0, "y": -1},{"x": 0, "y": 1},]
    seats_taken = 0
    for adjacent_seat in adjacent_seats:
        seat_y = row + adjacent_seat["y"]
        seat_x = seat + adjacent_seat["x"]
        while(seat_y >= 0 and seat_y < len(layout) and seat_x >= 0 and seat_x < len(layout[seat_y]) and layout[seat_y][seat_x] == "."):
            seat_y = seat_y + adjacent_seat["y"]
            seat_x = seat_x + adjacent_seat["x"]
        if(seat_y < 0 or seat_y >= len(layout) or seat_x < 0 or seat_x >= len(layout[seat_y])):
            seat_y = seat_y - adjacent_seat["y"]
            seat_x = seat_x - adjacent_seat["x"]
        if(seat_x == seat and seat_y == row):
            continue

        if(layout[seat_y][seat_x] == "#"):
            seats_taken += 1
    #print("Row: %s, Seat: %s, Taken: %s" % (row, seat, seats_taken))
    return seats_taken
def print_layout(layout):
    for line in layout:
        print(str(line))
def count_occupied_seats(layout):
    occupied = 0
    for row in layout:
        for seat in row:
            if(seat == "#"):
                occupied+=1
    print(occupied)
with open("layout", "r") as f:
    layout = [list(line.strip()) for line in f.readlines()]
    print_layout(layout)
    seats_changed = 1
    while(seats_changed != 0):
        layout_copy = deepcopy(layout)
        print("----")
        seats_changed = 0
        for rownr, row in enumerate(layout_copy):
            for seatnr, seat in enumerate(row):
                if layout_copy[rownr][seatnr] != "." and is_empty_seat(layout_copy, rownr, seatnr) >= 5:
                    if layout[rownr][seatnr] != "L": 
                        seats_changed += 1
                        layout[rownr][seatnr] = "L"
                elif layout_copy[rownr][seatnr] != "." and is_empty_seat(layout_copy, rownr, seatnr) == 0:
                    if layout[rownr][seatnr] != "#": 
                        seats_changed += 1
                        layout[rownr][seatnr] = "#"
                    
        print_layout(layout)
        count_occupied_seats(layout)