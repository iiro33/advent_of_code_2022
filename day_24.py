# advent of code
# anonymous user #1879507
from copy import deepcopy

with open('input_day_24.txt') as file:
    lines = file.readlines()
    lines = [list(line.strip()) for line in lines]

class Blizzard:
    def __init__(self, x, y, d, max_x, max_y):
        self._x = x
        self._y = y
        self._direction = d
        self._max_x = max_x
        self._max_y = max_y

    def get_x(self):
        return self._x

    def get_y(self):
        return self._y

    def move(self):
        if self._direction == ">":  # right
            self._x += 1  # move right
            if self._x == self._max_x:  # hitting a wall
                self._x = 1  # return to left side wall
        elif self._direction == "<":  # left
            self._x -= 1
            if self._x == 0:
                self._x = self._max_x - 1
        elif self._direction == "^":  # up
            self._y -= 1
            if self._y == 0:
                self._y = self._max_y - 1
        elif self._direction == "v":  # down
            self._y += 1
            if self._y == self._max_y:
                self._y = 1


class Adventurer:

    def __init__(self, x, y, minutes):
        self._x = x
        self._y = y
        self._minutes = minutes

    def get_x(self):
        return self._x

    def get_y(self):
        return self._y

    def get_minutes(self):
        return self._minutes



def find_path(start, end, og_grid, stars):
    # create blizzards which move
    blizzards = []
    successes = 0
    grid = deepcopy(og_grid)
    og_end = deepcopy(end)
    og_start = deepcopy(start)
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            if grid[y][x] != "." and grid[y][x] != "#":
                blizzards.append(Blizzard(x, y, grid[y][x], len(grid[y]) - 1, len(grid) - 1))

    queue = [[Adventurer(start[0], start[1], 0)]]
    iterations = 0
    while True:
        iterations += 1
        visited = []
        # create grid for checking
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                grid[row][col] = "."
        for blizzard in blizzards:  # move the blizzard before adventurer takes a move
            blizzard.move()
            grid[blizzard.get_y()][blizzard.get_x()] = "B"
        for _ in range(len(queue)):
            source_queue = queue.pop(0)
            new_queue = []
            for path in source_queue:
                path_x, path_y, path_minutes = path.get_x(), path.get_y(), path.get_minutes()
                if path_x > 1 and [path_x-1, path_y] not in visited and path_y != len(grid)-1:  # moving left
                    new_queue.append(Adventurer(path_x-1, path_y, path_minutes+1))
                    visited.append([path_x-1, path_y])
                # moving right, excluding end row:
                if path_x <= len(grid[0])-3 and path_y != 0 and [path_x+1, path_y] not in visited:
                    new_queue.append(Adventurer(path_x+1, path_y, path_minutes + 1))
                    visited.append([path_x + 1, path_y])
                if (path_y > 1 or (path_y == 1 and path_x == 1)) and [path_x, path_y - 1] not in visited:  # moving up
                    new_queue.append(Adventurer(path_x, path_y-1, path_minutes + 1))
                    visited.append([path_x, path_y - 1])
                # moving down, allowing on goal column as well:
                if (path_y <= len(grid)-3 or (path_x == og_end[0] and path_y  == len(grid)-2)) and [path_x, path_y + 1] not in visited:
                    new_queue.append(Adventurer(path_x, path_y+1, path_minutes + 1))
                    visited.append([path_x, path_y + 1])
                if [path_x, path_y] not in visited:
                    new_queue.append(Adventurer(path_x, path_y, path_minutes + 1))  # waiter
                    visited.append([path_x, path_y])
            for i in range(len(new_queue)-1, -1, -1):
                if new_queue[i].get_x() == end[0] and new_queue[i].get_y() == end[1]:  # we found the goal
                    successes += 1
                    if stars == 1:
                        print("Found the exit in " + str(new_queue[i].get_minutes()) + " minutes!")
                        return True
                    if stars == 2 and successes == 1:  # let's flip the goal and continue
                        end = og_start
                        print("First success, next goal: " + str(end))
                        print(new_queue[i].get_minutes())
                        new_queue = [new_queue[i]]
                        break
                    elif stars == 2 and successes == 2:
                        end = og_end
                        print("Second success, next goal: " + str(end))
                        print(new_queue[i].get_minutes())
                        new_queue = [new_queue[i]]
                        break
                    else:
                        print("Found the exit in " + str(new_queue[i].get_minutes()) + " minutes!")
                        return True
                if grid[new_queue[i].get_y()][new_queue[i].get_x()] == "B":
                    # adventurer ended up in a snowstorm, and we remove it
                    del new_queue[i]

        queue.append(new_queue)
        if iterations % 50 == 0:
            print(str(iterations) + " - queue len: " + str(len(queue)) + " - new_queue len: " + str(len(new_queue)))

start_point = [1, 0]
end_point = [len(lines[0])-2, len(lines)-1]
find_path(start_point, end_point, lines, 1)  ## single star solution

find_path(start_point, end_point, lines, 2)  # gold star solution
