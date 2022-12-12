# advent of code
# anonymous user #1879507

with open('input_day_12.txt') as file:
    lines = file.readlines()
    lines = [list(line.rstrip()) for line in lines]

class Dot:
    # basic initialization which keeps track of current row, column, distance from start,
    # height and individual visited list
    def __init__(self, row, col, dist, height, visited):
        self.row = row
        self.col = col
        self.dist = dist
        self.height = height
        self.visited = visited


# function which check if the next square is ok to visit
# (not visited before, inside the map and not too high point)
def is_valid(y, x, height, grid, visits):
    if 0 <= x < len(grid[0]) and 0 <= y < len(grid):
        if visits[y][x] == False and grid[y][x] <= height+1:
            return True
    return False


# BFS algorithm https://en.wikipedia.org/wiki/Breadth-first_search
def find_min_steps(queue):
    while len(queue) != 0:
        source = queue.pop(0)  # extract with FIFO logic
        # goal
        if source.row == end[1] and source.col == end[0]:  # end point returns the distance
            return source.dist
    
        # up... takes index ^ above previous on "visual basis".
        # stores visit matrix temporarily because can't use source visits
        if is_valid(source.row-1, source.col, source.height, lines, source.visited):
            temp_visited = source.visited
            temp_visited[source.row-1][source.col] = True
            queue.append(Dot(source.row-1, source.col, source.dist+1, lines[source.row-1][source.col], temp_visited))
        # down
        if is_valid(source.row+1, source.col, source.height, lines, source.visited):
            temp_visited = source.visited
            temp_visited[source.row+1][source.col] = True
            queue.append(Dot(source.row+1, source.col, source.dist+1, lines[source.row+1][source.col], temp_visited))
        # left
        if is_valid(source.row, source.col-1, source.height, lines, source.visited):
            temp_visited = source.visited
            temp_visited[source.row][source.col-1] = True
            queue.append(Dot(source.row, source.col-1, source.dist+1, lines[source.row][source.col-1], temp_visited))
        # right
        if is_valid(source.row, source.col+1, source.height, lines, source.visited):
            temp_visited = source.visited
            temp_visited[source.row][source.col+1] = True
            queue.append(Dot(source.row, source.col+1, source.dist+1, lines[source.row][source.col+1], temp_visited))
    return 999999  # hack to just provide big number => "too long = impossible"


# convert characters to height with ord, and map starting point
for y in range(len(lines)):
    for x in range(len(lines[0])):
        if lines[y][x] == "S":
            start = [x, y]
            lines[y][x] = 1
        elif lines[y][x] == "E":
            end = [x, y]
            lines[y][x] = 26
        else:
            lines[y][x] = ord(lines[y][x]) - 96

start_visited = [[False for _ in range(len(lines[0]))] for _ in range(len(lines))]
start_visited[start[1]][start[0]] = True
beginning = Dot(start[1], start[0], 0, lines[start[1]][start[0]], start_visited)

goal = find_min_steps([beginning])
print("Goal reached: " + str(goal))  # single star solution

goals = []
# brute force repeat same as before, but for each 1 in the heightmap
for y in range(len(lines)):
    for x in range(len(lines[0])):
        if lines[y][x] == 1:
            start_visited = [[False for _ in range(len(lines[0]))] for _ in range(len(lines))]
            start_visited[y][x] = True
            beginning = Dot(y, x, 0, lines[y][x], start_visited)
            goals.append(find_min_steps([beginning]))

print("Goal reached: " + str(min(goals)))  # gold star solution
