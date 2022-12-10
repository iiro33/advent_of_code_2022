# advent of code
# anonymous user #1879507

with open('input_day_10.txt') as file:
    lines = file.readlines()
    lines = [line.rstrip() for line in lines]

def modify_cycle(i):
    if i >= 200:
        return i - 200
    elif i >= 160:
        return i - 160
    elif i >= 120:
        return i - 120
    elif i >= 80:
        return i - 80
    elif i >= 40:
        return i - 40
    else:
        return i


signal_strength = 1
que = [0, 0]
signal_strength_list = []

for line in lines:  # create cycle additions list
    if line == "noop":
        que.append(0)
    else:
        que.append(int(line.split()[1]))
        que.append(0)  # after addition we have to skip one iteration in the results

for item in que:  # add signal strengths by cycle
    signal_strength += item
    #print("Added " + str(item))
    signal_strength_list.append(signal_strength)
    #print("Signal srength now " + str(signal_strength))

result_value = 0  # for single star solution
cycle_ids = [19, 59, 99, 139, 179, 219]  # for single star solution
drawing = ""
for cycle in range(len(signal_strength_list)):
    if cycle in cycle_ids:
        result_value += (signal_strength_list[cycle] * (cycle+1))  # single star solution
    new_cycle = modify_cycle(cycle)  # if cycle >= 40 switch to draw the next row
    # check the sprite which is three pixels long
    if signal_strength_list[cycle] <= (new_cycle + 1) <= (signal_strength_list[cycle] + 2):
        drawing += "#"
    else:
        drawing += "."

print("Sum of signal strengths with multiplier : " + str(result_value))
print("CRT Image:")
print(drawing[0:40])
print(drawing[40:80])
print(drawing[80:120])
print(drawing[120:160])
print(drawing[160:200])
print(drawing[200:240])
