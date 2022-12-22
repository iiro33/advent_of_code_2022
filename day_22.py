# advent of code
# anonymous user #1879507
# single star solution only
import re

with open('input_day_22.txt') as file:
    lines = file.readlines()
    lines = [line.strip("\n") for line in lines]

class Adventurer:

    def __init__(self, x, y, g):
        self._x = x
        self._y = y
        self._direction = 0
        self._grid = g

    def turn(self, d):
        if d == "R":
            self._direction += 1
        elif d == "L":
            self._direction -= 1

        if self._direction > 3:
            self._direction = 0
        elif self._direction < 0:
            self._direction = 3

    def move(self):
        next_cell_x, next_cell_y = self.get_next_valid_cell(self._x, self._y)
        next_cell = self._grid[next_cell_y][next_cell_x]
        if next_cell == ".":
            self._x = next_cell_x
            self._y = next_cell_y

    def get_next_valid_cell(self, x, y):
        if self._direction == 0:  # right
            x += 1
        elif self._direction == 1:
            y += 1
        elif self._direction == 2:
            x -= 1
        elif self._direction == 3:
            y -= 1

        if x < 0:
            x = len(grid[y]) - 1
        if y < 0:
            y = len(grid) - 1
        if y >= len(grid):
            y = 0
        if x >= len(grid[y]):
            x = 0

        while self._grid[y][x] == " ":  # have to loop around
            x, y = self.get_next_valid_cell(x, y)

        return [x, y]

    def find_password(self):
        return 1000*(self._y + 1) + 4*(self._x+1) + self._direction


# parse grid
grid = [list(x) for x in lines[:-2]]
max_l = 0
for row in grid:
    if len(row) > max_l:
        max_l = len(row)
for i in range(len(grid)):
    while len(grid[i]) < max_l:
        grid[i].append(' ')

# parse commands
commands = lines[len(lines)-1]
commands = re.split("([A-Z])", commands)  # keep separators

# starting point
for i in range(len(grid[0])):
    if grid[0][i] == ".":
        starting_point = [i, 0]
        break

# ACTION!
adventurer = Adventurer(starting_point[0], starting_point[1], grid)
for cmd in commands:
    if re.match("\d+", cmd) is None:  # it's a turn command
        adventurer.turn(cmd)
    else:  # it's a move command
        for _ in range(int(cmd)):
            adventurer.move()

# for row in grid:
#     print(row)
# print(commands)
print("Final password is: " + str(adventurer.find_password()))
