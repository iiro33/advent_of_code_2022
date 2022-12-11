# advent of code
# anonymous user #1879507
import re

with open('input_day_11.txt') as file:
    lines = file.readlines()
    lines = [line.rstrip() for line in lines]

class Monkey:
    monkey_test_divisor = 1

    def __init__(self, monkey_id, items, operation, test, throw_true, throw_false):
        self._monkey_id = int(monkey_id)
        self._items = [int(x) for x in items]
        self._operation = operation
        self._test = int(test)
        self._throw_list = [throw_false, throw_true]
        self._inspects = 0
        Monkey.monkey_test_divisor *= self._test  # all monkey divisors combined, for part 2 => 9699690

    def add_item(self, item_to_receive):
        self._items.append(item_to_receive)

    def inspect_all_items(self, worry_level):
        _throw_items_to = []
        _items_to_throw = []
        for _i in range(len(self._items)):
            old = self._items[_i]  # for operation evaluation
            self._items[_i] = eval(self._operation)
            if worry_level:  # only needed for single star
                self._items[_i] = self._items[_i] // 3
            self._inspects += 1
            if not(self._items[_i] % self._test):  # is divisible by the monkey, decides who to send the item to
                _throw_items_to.append(self._throw_list[1])
            else:
                _throw_items_to.append(self._throw_list[0])
            if self._items[_i] > Monkey.monkey_test_divisor:  # if the item is divisible by ALL monkey divisors
                self._items[_i] = self._items[_i] % Monkey.monkey_test_divisor

            _items_to_throw.append(self._items[_i])

        self._items = []
        return [_items_to_throw, _throw_items_to]


monkeys = []
i = 0
while True:  # parse all input lines and add to monkey list
    monkey_id = re.findall("\d+", lines[i])
    items = re.findall("\d+", lines[i+1])
    operation = re.findall("= (.*)$", lines[i+2])
    test = re.findall("\d+", lines[i+3])
    throw_true = re.findall("\d+", lines[i+4])
    throw_false = re.findall("\d+", lines[i+5])
    parsed_input = [monkey_id, items, operation, test, throw_true, throw_false]
    monkeys.append(Monkey(monkey_id[0], items, operation[0], test[0], int(throw_true[0]), int(throw_false[0])))
    i += 7
    if i >= len(lines):
        break

worrying = False
for round_n in range(10000):  # 20 for single star solution and worrying = True
    for monkey in monkeys:
        to_throw, monkey_to_receive = monkey.inspect_all_items(worry_level=worrying)
        for i in range(len(monkey_to_receive)):
            monkeys[monkey_to_receive[i]].add_item(to_throw[i])
    if (round_n+1) % 1000 == 0:
        print("End of round " + str(round_n+1))

inspects_list = []
for monkey in monkeys:
    inspects_list.append(monkey._inspects)
print(inspects_list)
inspects_list = sorted(inspects_list, reverse=True)
print("Solution: " + str(inspects_list[0]*inspects_list[1]))
