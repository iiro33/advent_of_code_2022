# advent of code
# anonymous user #1879507

with open('input_day_3.txt') as file:
    lines = file.readlines()
    lines = [line.rstrip() for line in lines]


def get_points(char):
    if char.isupper():
        return ord(char) - 38
    else:
        return ord(char) - 96


def calc_priorities(p1, p2):
    string_prio = 0
    added_list = []
    for char in p1:
        if char in p2 and char not in added_list:
            added_list.append(char)
            string_prio += get_points(char)
    return string_prio


def calc_gold_priorities(elf_group):
    for char in elf_group[0]:
        if char in elf_group[1] and char in elf_group[2]:
            return get_points(char)


priorities, gold_priorities = 0, 0
for line in lines:
    midpoint = int(len(line)/2)
    p1, p2 = line[:midpoint], line[midpoint:]
    priorities += calc_priorities(p1, p2)

i = 0
while i <= len(lines)-3:
    gold_priorities += calc_gold_priorities(lines[i:i+3])
    i += 3

print(priorities)
print(gold_priorities)
