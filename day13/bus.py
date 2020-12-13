from math import ceil

with open("notes", "r") as f:
    earliest = int(f.readline().strip())
    busses = f.readline().strip().split(",")
    bus_min = float("inf")
    bus_leave = float("inf")
    for key, bus in enumerate(busses):
        if(bus == "x"):
            continue
        bus = int(bus)
        leave = ceil(earliest/bus)*bus
        if(leave < bus_leave):
            bus_leave = leave
            bus_min = key
    wait = bus_leave - earliest
    print(wait*int(busses[bus_min]))

    timestamp = 0
    iteration = 0
    step = int(busses[0])
    while(True):
        timestamp = iteration + step
        iteration = timestamp
        works = True
        for key, bus in enumerate(busses):
            if(bus == "x"):
                timestamp += 1
                continue 
            bus = int(bus)
            if(timestamp%bus == 0):
                timestamp += 1
                if not step % bus == 0:
                    step *= bus
                continue
            else:
                works = False
                break
        if works:
            print(iteration)
            break
        else:
            print(iteration)
            