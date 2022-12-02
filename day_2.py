# advent of code
# anonymous user #1879507

with open('input_day_2.txt') as file:
    lines = file.readlines()
    value_map = {"A": "1", "B": "2", "C": "3", "X": "1", "Y": "2", "Z": "3"}
    new_lines = []
    for line in lines:
        for k, v in value_map.items():
            line = line.replace(k, v)
        new_lines.append(line.rstrip().split())
    new_lines = [[int(x)for x in line] for line in new_lines]


def get_result_points(rps):
    if rps[1] == rps[0]:  # draw
        points = 3
    elif rps[1] - rps[0] == 1 or (rps[1] == 1 and rps[0] == 3):  # win
        points = 6
    else:  # loss
        points = 0
    return points + rps[1]


def get_result_gold(rps):
    if rps[1] == 2:  # draw
        points = 3 + rps[0]
    elif rps[1] == 1:  # loss
        if rps[0] == 1:  # if rock then scissors : 3
            points = 3
        else:  # else take one lower
            points = rps[0] - 1
    else:  # win
        points = 6
        if rps[0] == 3:
            points += 1
        else:
            points += rps[0] + 1
    return points


result = 0
result_gold = 0
for rps in new_lines:
    result += get_result_points(rps)
    result_gold += get_result_gold(rps)

print(result)
print(result_gold)
