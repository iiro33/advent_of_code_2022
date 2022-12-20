# advent of code
# anonymous user #1879507
# single star solution only

with open('input_day_18.txt') as file:
    lines = file.readlines()
    lines = [eval("["+line.rstrip()+"]") for line in lines]


print(lines)
scores = [-1 for _ in range(len(lines))]

for i in range(len(lines)):
    for z in range(len(lines)):
        if lines[i][0] == lines[z][0] and lines[i][1] == lines[z][1] and abs(lines[i][2] - lines[z][2]) <= 1:
            scores[i] += 1
        elif lines[i][1] == lines[z][1] and lines[i][2] == lines[z][2] and abs(lines[i][0] - lines[z][0]) <= 1:
            scores[i] += 1
        elif lines[i][2] == lines[z][2] and lines[i][0] == lines[z][0] and abs(lines[i][1] - lines[z][1]) <= 1:
            scores[i] += 1

result = 0
for score in scores:
    result += (6 - score)
print(scores)
print(result)
