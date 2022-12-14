# advent of code
# anonymous user #1879507

# only single star solution

with open('input_day_13.txt') as file:
    lines = file.readlines()


def as_list(val):
    return val if type(val) == list else [val]


def compare_lists(l1, l2):
    print(l1)
    print(l2)
    if len(l1) == 0 and len(l2) != 0:  # checks whether first list is empty and second IS NOT
        return True
    for z in range(len(l2)):
        try:  # catches if trying to go too far on first list...
            e1, e2 = l1[z], l2[z]
            temp_result = None
            if type(e1) == int and type(e2) == int:
                if e1 < e2:
                    return True
                elif e1 > e2:
                    return False
            else:
                temp_result = compare_lists(as_list(e1), as_list(e2))

            if temp_result is None:  # values match
                continue
            else:
                return temp_result

        except IndexError:  # ... and returns True as first list is shorter and no differing int so far
            return True
    if len(l1) > len(l2):
        return False
    elif len(l1) < len(l2):
        return True


i, result, counter = 0, 0, 1
while i < len(lines):
    line_1 = eval(lines[i].strip())
    line_2 = eval(lines[i + 1].strip())
    if compare_lists(line_1, line_2):
        result += counter
    else:
        print("Not in order")
        print(line_1)
        print(line_2)
    print("Current result: " + str(result))
    print("")
    i += 3
    counter += 1
