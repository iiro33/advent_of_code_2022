# advent of code
# anonymous user #1879507

with open('input_day_23.txt') as file:
    lines = file.readlines()
    lines = [list(line.strip()) for line in lines]

class Elf:

    def __init__(self, x, y):
        self._x = x
        self._y = y
        self._suggestion = ""
        self._suggestion_x = None
        self._suggestion_y = None
        self._position = [x, y]

    def get_x(self):
        return self._x

    def get_y(self):
        return self._y

    def suggest(self, all_positions, queue) -> "returns True if need to move and new location":
        self._suggestion_x = self._x
        self._suggestion_y = self._y
        # do I need to move?
        if [self._x - 1, self._y - 1] not in all_positions:
            if [self._x, self._y - 1] not in all_positions:
                if [self._x + 1, self._y - 1] not in all_positions:
                    if [self._x - 1, self._y] not in all_positions:
                        if [self._x + 1, self._y] not in all_positions:
                            if [self._x - 1, self._y + 1] not in all_positions:
                                if [self._x, self._y + 1] not in all_positions:
                                    if [self._x + 1, self._y + 1] not in all_positions:
                                        self._suggestion = str(self._suggestion_x) + "," + str(self._suggestion_y)
                                        return [False, self._suggestion]

        # check movement
        for q in queue:
            if q == "n":
                if [self._x - 1, self._y - 1] not in all_positions:
                    if [self._x, self._y - 1] not in all_positions:
                        if [self._x + 1, self._y - 1] not in all_positions:
                            self._suggestion_x = self._x
                            self._suggestion_y = self._y - 1
                            break
            elif q == "s":
                if [self._x - 1, self._y + 1] not in all_positions:
                    if [self._x, self._y + 1] not in all_positions:
                        if [self._x + 1, self._y + 1] not in all_positions:
                            self._suggestion_x = self._x
                            self._suggestion_y = self._y + 1
                            break
            elif q == "w":
                if [self._x - 1, self._y - 1] not in all_positions:
                    if [self._x - 1, self._y] not in all_positions:
                        if [self._x - 1, self._y + 1] not in all_positions:
                            self._suggestion_x = self._x - 1
                            self._suggestion_y = self._y
                            break
            elif q == "e":
                if [self._x + 1, self._y - 1] not in all_positions:
                    if [self._x + 1, self._y] not in all_positions:
                        if [self._x + 1, self._y + 1] not in all_positions:
                            self._suggestion_x = self._x + 1
                            self._suggestion_y = self._y
                            break

        self._suggestion = str(self._suggestion_x) + "," + str(self._suggestion_y)
        return [True, self._suggestion]

    def move(self, all_suggestions):
        if self._suggestion in all_suggestions:
            if all_suggestions[self._suggestion] == 1:
                self._x = self._suggestion_x
                self._y = self._suggestion_y
                self._position = [self._x, self._y]

    def get_position(self):
        return self._position


elves, current_positions = [], []
# get initial positions
for y in range(len(lines)):
    for x in range(len(lines[0])):
        if lines[y][x] == "#":
            elf = Elf(x, y)
            elves.append(elf)
            current_positions.append(elf.get_position())

# main loop
command_queue = ["n", "s", "w", "e"]
for i in range(10000):
    suggestions = {}
    for elf in elves:
        s = elf.suggest(current_positions, command_queue)
        if s[0]:
            if s[1] in suggestions:
                suggestions[s[1]] += 1
            else:
                suggestions[s[1]] = 1
    current_positions = []
    min_x, max_x, min_y, max_y = 9999, -9999, 9999, -9999
    for elf in elves:
        elf.move(suggestions)
        current_positions.append(elf.get_position())
        if i < 10:  # only needed for single star solution
            elf_x = elf.get_x()
            elf_y = elf.get_y()
            if elf_x < min_x:
                min_x = elf_x
            if elf_x > max_x:
                max_x = elf_x
            if elf_y < min_y:
                min_y = elf_y
            if elf_y > max_y:
                max_y = elf_y
    queue_manager = command_queue.pop(0)  # shift the command queue, which is same for all elves
    command_queue.append(queue_manager)
    if i == 9:  # single star solution
        result = (max_x - min_x + 1) * (max_y - min_y + 1) - len(elves)
        print("Empty spaces in grid after ten rounds: " + str(result))
    if len(suggestions) == 0:  # gold star solution
        print("No need to move after " + str(i + 1) + " rounds")
        break
    if (i + 1) % 10 == 0:
        print("Ending round " + str(i + 1))


#print(lines)
#print(current_positions)
