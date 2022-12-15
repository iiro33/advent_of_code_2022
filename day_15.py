# advent of code
# anonymous user #1879507
import re

with open('input_day_15.txt') as file:
    lines = file.readlines()

class Sensor:

    def __init__(self, x, y, beacon_min):
        self._x = x
        self._y = y
        self._beacon_min = beacon_min


def calc_manhattan(point1, point2):
    return abs(point1[0]-point2[0]) + abs(point1[1]-point2[1])

sensors, beacons = [], []
for line in lines:
    sx, sy, bx, by = list(map(int, re.findall("-?\d+", line)))
    sensors.append(Sensor(sx, sy, calc_manhattan([sx, sy], [bx, by])))

### start single star solution
y = 2000000
not_beacon = 0
for x in range(-2000000, 7000000):
    cant_be = 0
    for sensor in sensors:
        if calc_manhattan([x,y], [sensor._x, sensor._y]) <= sensor._beacon_min:
            cant_be += 1
    if cant_be > 0:
        not_beacon += 1

print(str(not_beacon - 1))  # one beacon on the row
### end single star solution

### start gold star solution
points_to_check = []
for s in sensors:
    # the distress beacon has to be on the "bottom left edge" of some sensors range
    p1 = [s._x, s._y + s._beacon_min]
    p2 = [s._x - s._beacon_min, s._y]
    for i in range(1, p1[1]-p2[1]):
        z = [p1[0]-(i-1), p1[1]+(2-i)]
        if 0 <= z[0] <= 4000000 and 0 <= z[1] <= 4000000:  # check that within limits
            points_to_check.append(z)

# check mapped points
for item in points_to_check:
    cant_be = 0
    for s in sensors:  # loop all sensors to check the points
        if calc_manhattan(item, [s._x, s._y]) <= s._beacon_min:  # if any sensor is closer than the point it can't be
            cant_be += 1
            break
    if cant_be == 0:
        if 0 <= item[0] <= 4000000 and 0 <= item[1] <= 4000000:  # found the one and only correct point
            print(item)
            print(str(item[0]*4000000 + item[1]))  # tuning frequency
            break

### end gold star solution
