# advent of code
# anonymous user #1879507

with open('input_day_4.txt') as file:
    lines = file.readlines()
    lines = [line.rstrip() for line in lines]


n_fully_overlaps = 0
n_partly_overlaps = 0

for line in lines:
    elf_1, elf_2 = line.split(",")
    x_1, x_2 = map(int, elf_1.split("-"))
    y_1, y_2 = map(int, elf_2.split("-"))
    if (x_1 >= y_1 and x_2 <= y_2) or (y_1 >= x_1 and y_2 <= x_2):
        n_fully_overlaps += 1
    if x_2 < y_1 or y_2 < x_1:
        # no overlap, go to next
        continue
    else:
        n_partly_overlaps += 1

print(lines)
print(n_fully_overlaps)
print(n_partly_overlaps)
