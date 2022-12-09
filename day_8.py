# advent of code
# anonymous user #1879507

with open('input_day_8.txt') as file:
    lines = file.readlines()
    lines = [list(map(int, line.rstrip())) for line in lines]

visible_trees = len(lines)*2 + len(lines[0])*2 - 4  # outside trees as start
mapped_trees = []

def check_trees(x, y, matrix):
    left, right, top, down = True, True, True, True
    scenic = []
    shorter_trees = 0
    for ind in range(x-1, -1, -1):  # left, loop in reverse
        shorter_trees += 1  # closest tree is always visible
        if not matrix[x][y] > matrix[ind][y]:
            left = False
            break  # exit loop when all visible trees are counted
    scenic.append(shorter_trees)
    shorter_trees = 0
    for ind in range(x+1, len(matrix[0])):  # right
        shorter_trees += 1
        if not matrix[x][y] > matrix[ind][y]:
            right = False
            break
    scenic.append(shorter_trees)
    shorter_trees = 0
    for ind in range(y-1, -1, -1):  # top, loop in reverse
        shorter_trees += 1
        if not matrix[x][y] > matrix[x][ind]:
            top = False
            break
    scenic.append(shorter_trees)
    shorter_trees = 0
    for ind in range(y+1, len(matrix)):  # down
        shorter_trees += 1
        if not matrix[x][y] > matrix[x][ind]:
            down = False
            break
    scenic.append(shorter_trees)
    return [any([left, right, top, down]), scenic[0]*scenic[1]*scenic[2]*scenic[3]]


scenic_points = []
for i in range(1, len(lines[0])-1):
    for z in range(1, len(lines)-1):  # for each tree inside outer tree range
        visible, points = check_trees(i, z, lines)  # true if visible from any direction, trees visible
        scenic_points.append(points)
        if visible:
            mapped_trees.append(str(i) + "," + str(z))

print("Trees visible: " + str(visible_trees + len(set(mapped_trees))))
print("Max scenic points: " + str(max(scenic_points)))
