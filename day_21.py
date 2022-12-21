# advent of code
# anonymous user #1879507
import sympy

with open('input_day_21.txt') as file:
    lines = file.readlines()
    lines = [line.strip() for line in lines]

calcs = {}
for line in lines:
    l, r = line.split(": ")
    calcs[l] = r

def make_formula(input_dict, param):
    right = input_dict[param]
    if len(right) > 4:
        right_list = right.split(" ")
        doer_1 = make_formula(input_dict, right_list[0])
        operation = right_list[1]
        doer_2 = make_formula(input_dict, right_list[2])
    else:
        return "(" + right + ")"

    return "(%s %s %s)" % (doer_1, operation, doer_2)


def make_formula_gold(input_dict, param):
    right = input_dict[param]
    if param == "root":
        right = right.replace("+", "==").replace("-", "==").replace("/", "==").replace("*", "==")

    if len(right) > 4:
        right_list = right.split(" ")
        doer_1 = make_formula_gold(input_dict, right_list[0])
        operation = right_list[1]
        doer_2 = make_formula_gold(input_dict, right_list[2])
    elif param == "humn":
        return "(x)"
    else:
        return "(" + right + ")"

    return "(%s %s %s)" % (doer_1, operation, doer_2)


calculation = make_formula(calcs, "root")
print("Single star evaluation:")
print(calculation)
print(int(eval(calculation)))
print("")

calculation_gold = make_formula_gold(calcs, "root")
print("Gold star evaluation:")
print(calculation_gold)
x = sympy.symbols("x")
a = sympy.simplify(calculation_gold.split(" == ")[0][1:])
b = sympy.simplify(calculation_gold.split(" == ")[1][:-1])
print("left: " + str(a))
print("right: " + str(b))
print(sympy.solve(a - b))
