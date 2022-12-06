# advent of code
# anonymous user #1879507

with open('input_day_6.txt') as file:
    lines = file.readlines()
    lines = [line.rstrip() for line in lines]

def check_unique(input_list):
    if len(input_list) == len(set(input_list)):
        return True
    else:
        return False


line = lines[0]
i_marker, i_message = 4, 14
cache_marker, cache_message = list(line[0:i_marker]), list(line[0:i_message])

for char in line:
    if check_unique(cache_marker):
        pass
    else:
        cache_marker.pop(0)
        cache_marker.append(line[i_marker])
        i_marker += 1
    if check_unique(cache_message):
        break
    else:
        cache_message.pop(0)
        cache_message.append(line[i_message])
        i_message += 1


print(line)
print(str(i_marker) + ". character is the marker.")
print(str(i_message) + ". character is the message starter.")
