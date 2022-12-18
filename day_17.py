# advent of code
# anonymous user #1879507
# single star solution only

with open('input_day_17.txt') as file:
    line = file.readlines()[0]


class Shape:

    def __init__(self, shape):
        self._shape = shape
        self._cells = self.create_cells()

    def create_cells(self):
        if self._shape == 0:
            return [Cell(2, 0), Cell(3, 0), Cell(4, 0), Cell(5, 0)]
        elif self._shape == 1:
            return [Cell(3, 0), Cell(2, 1), Cell(3, 1), Cell(4, 1), Cell(3, 2)]
        elif self._shape == 2:
            return [Cell(4, 0), Cell(4, 1), Cell(2, 2), Cell(3, 2), Cell(4, 2)]
        elif self._shape == 3:
            return [Cell(2, 0), Cell(2, 1), Cell(2, 2), Cell(2, 3)]
        elif self._shape == 4:
            return [Cell(2, 0), Cell(3, 0), Cell(2, 1), Cell(3, 1)]
        elif self._shape == 5:
            return [Cell(0, 4), Cell(1, 4), Cell(2, 4), Cell(3, 4), Cell(4, 4), Cell(5, 4), Cell(6, 4)]

    def push_shape(self, d):
        for cell in self._cells:
            if d == "right":
                cell.add_x(1)
            elif d == "left":
                cell.add_x(-1)

    def can_push(self, g, d):
        for cell in self._cells:
            if d == "right":
                if cell.get_x() == 6:  # wall
                    return False
                elif g[cell.get_y()][cell.get_x()+1] == "#":  # other shape
                    return False
            elif d == "left":
                if cell.get_x() == 0:  # wall
                    return False
                elif g[cell.get_y()][cell.get_x()-1] == "#":  # other shape
                    return False
        return True

    def fall(self):
        for cell in self._cells:
            cell.add_y(1)

    def can_fall(self, g):
        for cell in self._cells:
            if g[cell.get_y()+1][cell.get_x()] == "#":
                return False
        return True

    def get_min_y(self):
        y_number = []
        for cell in self._cells:
            y_number.append(cell.get_y())
        return min(y_number)

    def clean_grid(self, g):
        for cell in self._cells:
            g[cell.get_y()][cell.get_x()]  = "."
        return g

    def update_grid(self, g):
        for cell in self._cells:
            g[cell.get_y()][cell.get_x()]  = "#"
        return g

    def maintenance(self, n):
        for cell in self._cells:
            cell.add_y(n)


class Cell:

    def __init__(self, x, y):
        self._x = x
        self._y = y

    def get_x(self):
        return self._x

    def get_y(self):
        return self._y

    def add_y(self, n):
        self._y += n

    def add_x(self, n):
        self._x += n


def shift_n(next_shape, baseline):
    n = 3 - baseline
    if next_shape == 0:
        n += 1
    elif next_shape == 1 or next_shape == 2:
        n += 3
    elif next_shape == 3:
        n += 4
    elif next_shape == 4:
        n += 2
    return n


# create starting grid
grid, shapes = [], []
for i in range(5):
    grid.append([".", ".", ".", ".", ".", ".", "."])
floor = Shape(5)
grid = floor.update_grid(grid)

# loop enough times (2022)
cmd = 0
for i in range(2022):
    shape_id = i % 5  # 0-4, floor is 5
    shape = Shape(shape_id)
    #print("Shape: " + str(shape_id))
    # loop until hits ground
    while True:
        #print("Cmd: " + str(cmd) + " - " + str(line[cmd]))
        if line[cmd] == ">":
            if shape.can_push(grid, "right"):
                shape.push_shape("right")
        elif line[cmd] == "<":
            if shape.can_push(grid, "left"):
                shape.push_shape("left")

        # get next command
        cmd += 1
        if cmd >= len(line):
            cmd = 0

        if not shape.can_fall(grid):
            break
        shape.fall()

    shapes.append(shape)
    # add rows to grid
    min_y = 100  # just as a blocker
    for s in shapes:
        shape_min_y = s.get_min_y()
        if shape_min_y < min_y:
            min_y = shape_min_y
    shifts = shift_n((shape_id+1)%5, min_y)
    if shifts > 0:
        for shift in range(shifts):
            for s in shapes:
                s.maintenance(1)
            grid.insert(0, [".", ".", ".", ".", ".", ".", "."])
    elif shifts < 0:
        for shift in range(abs(shifts)):
            for s in shapes:
                s.maintenance(-1)
            grid.pop(0)

    # draw to grid only after shape has stopped and everything else done
    grid = shape.update_grid(grid)

print(len(grid) - min_y - shifts - 1)  # length of rocks
