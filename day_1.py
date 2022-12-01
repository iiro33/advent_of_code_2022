# advent of code
# anonymous user #1879507

with open('input_day_1.txt') as file:
    lines = file.readlines()
    lines = [line.rstrip() for line in lines]

elves = []
calories = []
for line in lines:
    if line == '':
        elves.append(calories)
        calories = []
    else:
        calories.append(int(line))

elves.append(calories)

total_cals = []
for elf in elves:
    total_cals.append(sum(elf))

total_cals = sorted(total_cals,reverse=True)
print(total_cals[0])
print(sum(total_cals[0:3]))