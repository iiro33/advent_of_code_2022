# advent of code
# anonymous user #1879507
import re

with open('input_day_7.txt') as file:
    lines = file.readlines()
    lines = [line.rstrip() for line in lines]

def modify_path(prev_path, adder):
    if adder == "/":
        return "/"
    elif adder == "..":
        return "/".join(prev_path.split("/")[:-2]) + "/"  # split to elements and rejoin without last
    else:
        return prev_path + adder + "/"

# track current path always
current_path = ""
# store two dictionaries, one holding file sizes in dir path
# and one for storing which filenames have been already added
tree_sizes, tree_names = dict(), dict()

# loop the commands through
# in essence we only have to care about command lines, where
# cd changes current path
# ls will add file sizes for all the numbers
for line in lines:
    if line.startswith("$"):  # command
        active_cmd = line.split()[1]
        if active_cmd == "cd":
            current_path = modify_path(current_path, line.split()[2])
            if current_path not in tree_names.keys():  # first addition to dict as empty folder
                tree_names[current_path] = ["folder"]
                tree_sizes[current_path] = [0]

    if active_cmd == "ls":  # scan for files while in ls and add to dir sizes if file not added yet
        if re.match("^\d", line):  # files start with size
            split_line = line.split()
            size, name = int(split_line[0]), split_line[1]
            if name not in list(tree_names[current_path]):
                tree_names[current_path].append(name)
                tree_sizes[current_path].append(size)


def calculate_folder_sizes(input_dict):
    results = []
    for item in input_dict:
        temp_size = 0
        for k, v in input_dict.items():
            if k.startswith(item):
                temp_size += sum(v)
        results.append(temp_size)
    return results


# loop sizes dictionary and check size sums
limit = 100000
folder_sizes = calculate_folder_sizes(tree_sizes)
print("Folder sizes under 100 000: " + str([x for x in folder_sizes if x <= limit]))
print("Sum of folder sizes under 100 000: " + str(sum([x for x in folder_sizes if x <= limit])))

### gold solution
total_space = 70000000
space_needed = 30000000
current_min = folder_sizes[0]  # root is first in the folders and thus the biggest
for folder in folder_sizes:
    if total_space - folder_sizes[0] + folder >= space_needed and folder < current_min:
        current_min = folder

print("Folder size to be deleted: " + str(current_min))
