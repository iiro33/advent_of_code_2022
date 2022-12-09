# advent of code
# anonymous user #1879507

with open('input_day_9.txt') as file:
    lines = file.readlines()
    lines = [line.rstrip() for line in lines]

class PartOfRope:
    def __init__(self, rope_id):
        self.x = 0
        self.y = 0
        self.visits = ["0,0"]
        self.rope_id = rope_id

    def move(self, x, y):
        self.x += x
        self.y += y

    def new_coordinates(self, d, prev):
        if self.rope_id == 0:
            # move only first rope by commands directly
            if d == "U":
                self.move(0, 1)
            elif d == "D":
                self.move(0, -1)
            elif d == "R":
                self.move(1, 0)
            elif d == "L":
                self.move(-1, 0)
        else:
            if self.y == prev.y and abs(self.x - prev.x) > 1:
                if self.x < prev.x:
                    self.move(1, 0)
                else:
                    self.move(-1, 0)
            elif self.x == prev.x and abs(self.y - prev.y) > 1:
                if self.y < prev.y:
                    self.move(0, 1)
                else:
                    self.move(0, -1)
            elif abs(self.x - prev.x) > 1 or abs(self.y - prev.y) > 1:
                self.move(0, int(prev.y > self.y))
                self.move(int(prev.x > self.x), 0)
                self.move(0, -1*int(prev.y < self.y))
                self.move(-1*int(prev.x < self.x), 0)
        self.visits.append(str(self.x) + "," + str(self.y))  # only add visit after all move checks


rope_parts = []
rope_length = 10  # ten for gold solution as well
for rope_creator in range(rope_length):  # create enough rope parts
    rope_parts.append(PartOfRope(rope_creator))

for cmd in lines:
    d, n = cmd.split()
    n = int(n)
    for i in range(n):  # loop commands
        for z in range(len(rope_parts)):  # loop rope_parts for each command
            rope_parts[z].new_coordinates(d, rope_parts[abs(z-1)])

# solution
print("Unique visited coordinates for 2nd part: " + str(len(set(rope_parts[1].visits))))
# gold solution
print("Unique visited coordinates for tail: " + str(len(set(rope_parts[-1].visits))))
