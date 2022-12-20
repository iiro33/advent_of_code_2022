# advent of code
# anonymous user #1879507
# single star solution only
import collections

with open('input_day_20.txt') as file:
    lines = file.readlines()
    lines = [int(line.strip()) for line in lines]

lines = collections.deque(lines)
tracker = collections.deque([False for _ in range(len(lines))])
list_len = len(lines)

# shift numbers
for _ in range(len(lines)):
    i = tracker.index(False)
    lines.rotate(-i)
    tracker.rotate(-i)
    number = lines.popleft()
    tracker.popleft()
    lines.rotate(-number)
    tracker.rotate(-number)
    lines.insert(0, number)
    tracker.insert(0, True)
    if number < 0:
        number -= (abs(number) // (list_len-1))
    elif number > 0:
        number += (number // (list_len-1))
    lines.rotate(number - (number<0))
    tracker.rotate(number - (number<0))
    # if _ < 10:
    #     print(lines)
    #     print(tracker)

# calculate sum of 1000th, 2000th and 3000th number after 0
index = lines.index(0)
lines.rotate(-1000)
n_1 = lines[index]
lines.rotate(-1000)
n_2 = lines[index]
lines.rotate(-1000)
n_3 = lines[index]

print("%s %s %s" % (n_1, n_2, n_3))
print(str(n_1 + n_2 + n_3))


### start gold star solution
with open('input_day_20.txt') as file:
    lines = file.readlines()
    lines = [int(line.strip())*811589153 for line in lines]

lines = collections.deque(lines)
indexes = collections.deque([x for x in range(len(lines))])
list_len = len(lines)

# shift numbers
for _ in range(10):
    for zzz in range(len(lines)):
        i = indexes.index(zzz)
        lines.rotate(-i)
        indexes.rotate(-i)
        number = lines.popleft()
        i_n = indexes.popleft()
        lines.rotate(-number)
        indexes.rotate(-number)
        lines.insert(0, number)
        indexes.insert(0, i_n)
        if number < 0:
            number -= (abs(number) // (list_len-1))
        elif number > 0:
            number += (number // (list_len-1))
        lines.rotate(number - (number<0))
        indexes.rotate(number - (number<0))

# calculate sum of 1000th, 2000th and 3000th number after 0
index = lines.index(0)
lines.rotate(-1000)
n_1 = lines[index]
lines.rotate(-1000)
n_2 = lines[index]
lines.rotate(-1000)
n_3 = lines[index]

print("%s %s %s" % (n_1, n_2, n_3))
print(str(n_1 + n_2 + n_3))
### end gold star solution