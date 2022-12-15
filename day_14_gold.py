# advent of code
# anonymous user #1879507

# only single star solution

with open('input_day_14.txt') as file:
    lines = file.readlines()
    lines = [[list(map(int, x.split(","))) for x in list(line.rstrip().split(" -> "))] for line in lines]

min_x, max_x, min_y, max_y = 1000, 0, 0, 0
for line in lines:
    for cds in line:
        x, y = cds
        if x < min_x:
            min_x = x
        if x > max_x:
            max_x = x
        if y > max_y:
            max_y = y

sand_start = 500
grid = [["." for _ in range(1000)] for _ in range(max_y - min_y + 1)]

for line in lines:
    prev_x, prev_y = 0, 0
    for i in range(len(line)):
        x, y = line[i]
        grid[y][x] = "#"
        if i > 0:
            new_x = x
            new_y = y
            for _ in range(abs(x - prev_x) - 1):
                if new_x < prev_x:
                    new_x += 1
                else:
                    new_x -= 1
                grid[y][new_x] = "#"
            for _ in range(abs(y - prev_y) - 1):
                if new_y < prev_y:
                    new_y += 1
                else:
                    new_y -= 1
                grid[new_y][x] = "#"
        prev_x = x
        prev_y = y


class Sand:

    def __init__(self, x, y, grid):
        self._x = x
        self._y = y
        self._grid = grid

    def can_move(self):
        try:
            if self._grid[self._y+1][self._x] == ".":
                return True
            if self._grid[self._y+1][self._x-1] == ".":
                return True
            if self._grid[self._y + 1][self._x + 1] == ".":
                return True
        except IndexError:
            return False
        return False

    def move(self):
        if self._grid[self._y + 1][self._x] == ".":
            self._y += 1
        elif self._grid[self._y + 1][self._x - 1] == ".":
            self._x -= 1
            self._y += 1
        elif self._grid[self._y + 1][self._x + 1] == ".":
            self._x += 1
            self._y += 1

    def update_grid(self):
        self._grid[self._y][self._x] = "o"


for _ in range(2):
    line = []
    for i in range(len(grid[0])):
        if _ == 0:
            line.append(".")
        else:
            line.append("#")
    grid.append(line)


sand_dropped = 0
while True:
    sand = Sand(sand_start, 0, grid)
    while sand.can_move():
        sand.move()
    else:
        sand.update_grid()
    grid = sand._grid
    sand_dropped += 1
    if sand._y == 0:
        break

for g in grid:
    print(g)
print(sand_dropped)
