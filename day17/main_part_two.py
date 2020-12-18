from copy import deepcopy
class Cube:
    def __init__(self, x,y,z,w):
        self.x = x
        self.y = y
        self.z = z
        self.w = w
        self.active = True

class Grid:
    def __init__(self):
        self.cubes = []
        self.x_min = 0
        self.x_max = 0
        self.y_min = 0
        self.y_max = 0
        self.z_min = 0
        self.z_max = 0
        self.w_min = 0
        self.w_max = 0


    def is_active(self, x,y,z,w):
        for cube in self.cubes:
            if cube.x == x and cube.y == y and cube.z == z and cube.w == w:
                if cube.active:
                    return True
        return False

    def get_cube(self, x, y, z, w):
        for cube in self.cubes:
            if cube.x == x and cube.y == y and cube.z == z and cube.w == w:
                return cube
        return None

    def add_cube(self, x, y, z, w):
        self.cubes.append(Cube(x,y,z,w))
        if x < self.x_min:
            self.x_min = x
        if x > self.x_max:
            self.x_max = x
        if y < self.y_min:
            self.y_min = y
        if y > self.y_max:
            self.y_max = y
        if z > self.z_max:
            self.z_max = z
        if z < self.z_min:
            self.z_min = z
        if w < self.w_min:
            self.w_min = w
        if w > self.w_max:
            self.w_max = w

    def cycle(self):
        current_cubes = deepcopy(self.cubes)
        for w in range(self.w_min -1, self.w_max +2):
            for z in range(self.z_min - 1, self.z_max + 2):
                for y in range(self.y_min - 1, self.y_max + 2):
                    for x in range(self.x_min - 1, self.x_max + 2):
                        neighbors = self.check_cube_neighbors(x,y,z,w, current_cubes)
                        cube = self.get_cube(x,y,z,w)
                        if cube and cube.active and (neighbors == 2 or neighbors == 3):
                            pass
                        elif cube and cube.active:
                            cube.active = False
                        elif cube and not cube.active and neighbors == 3:
                            cube.active = True
                        elif not cube and neighbors == 3:
                            self.add_cube(x,y,z,w)


    def check_cube_neighbors(self, x, y, z, w, cubes):
        neighbor_count = 0
        for cube in cubes:
            if cube.x == x and cube.y == y and cube.z == z and cube.w == w:
                continue
            else:
                if abs(cube.w-w) <= 1 and abs(cube.x-x) <= 1 and abs(cube.y - y) <= 1 and abs(cube.z-z) <= 1 and cube.active:
                    neighbor_count += 1
        return neighbor_count

    def print(self):
        string = ""
        for w in range(self.w_min, self.w_max + 1):
            for z in range(self.z_min, self.z_max + 1):
                string += "z = %s, w = %s\n" % (z, w)
                for y in range(self.y_min, self.y_max + 1):
                    for x in range(self.x_min, self.x_max + 1):
                        cube = self.get_cube(x,y,z,w)
                        if cube and cube.active:
                            string += "#"
                        else:
                            string += "."
                    string += "\n"
        print(string)
    def active_cubes(self):
        count = 0
        for cube in self.cubes:
            if cube.active:
                count += 1
        return count
grid = Grid()
with open("puzzle", "r") as f:
    y = 0
    for line in f.readlines():
        x = 0
        for char in line.strip():
            if char == "#":
                grid.add_cube(x,y,0,0)
            x += 1
        y += 1

grid.print()
for i in range(0,6):
    grid.cycle()
    grid.print()

print(grid.active_cubes())
