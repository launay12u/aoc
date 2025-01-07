import math
from itertools import product

with open('data.txt') as f:
    lines = f.read().splitlines()
    equations = []
    for line in lines:
        res_, values_ = line.split(":")
        res = int(res_)
        values = list(map(int, values_.strip().split()))
        equations.append((res, values))


def evaluate_expression(numbers, functions):
    result = numbers[0]
    for i in range(1, len(numbers)):
        result = functions[i-1]([result, numbers[i]])
    return result


def find_valid_equations(equations,operations):
    valid_sum = 0

    for test_value, numbers in equations:
        # If there's only one number, no operators, directly check
        if len(numbers) == 1:
            if numbers[0] == test_value:
                valid_sum += test_value
            continue

        function_combinations = product(operations, repeat=len(numbers) - 1)

        for functions in function_combinations:
            if evaluate_expression(numbers, functions) == test_value:
                valid_sum += test_value
                break

    return valid_sum

def combine(vals):
    return int(str(vals[0]) + str(vals[1]))

print(find_valid_equations(equations,[sum, math.prod]))
print(find_valid_equations(equations,[sum, math.prod,combine]))