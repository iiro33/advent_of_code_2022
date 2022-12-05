# advent of code
# anonymous user #1879507
import re, copy

with open('input_day_5.txt') as file:
    lines = file.readlines()
    lines = [line.rstrip("\n").ljust(35, " ") for line in lines]  # have to ljust cause reading failed

status, commands = [], []
for line in lines:
    if "[" in line:
        i = 0
        line_codes = []
        while i <= len(line):
            line_codes.append(line[i:i+3])
            i += 4  # lines are three characters long and have one space in between fields
        status.append(line_codes)
    elif "move" in line:
        commands.append([int(s) for s in re.findall("\d+", line)])


# transpose the matrix to have nested lists as separate stacks
status = [list(reversed(i)) for i in zip(*status)]
# remove empties from end of stacks
status = [[item for item in state if bool(re.search("\w", item))] for state in status]
print("Status in the beginning:")
[print(item) for item in status]
gold_status = copy.deepcopy(status)

for cmd in commands:
    f_ind, t_ind = cmd[1] - 1, cmd[2] - 1
    for i in range(cmd[0]):
        status[t_ind].append(status[f_ind][-1])  # add top of stack to other stack
        status[f_ind].pop()  # remove from top of stack

    ### start gold level solution
    cutoff = len(gold_status[f_ind]) - cmd[0]  # where to break the lists
    to_add = gold_status[f_ind][cutoff:]
    for crate in to_add:  # add one by one to avoid nested lists
        gold_status[t_ind].append(crate)
    gold_status[f_ind] = gold_status[f_ind][:cutoff]
    ### end gold level solution


print("\nCommands: " + str(commands) + "\n")
print("Status in the end:")
[print(item) for item in status]
print("\nGold Status in the end:")
[print(gold_item) for gold_item in gold_status]
