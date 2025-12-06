from math import prod
from pathlib import Path

from utils.time_decorator import timer

PATH = Path(__file__).parent / "data.txt"



def parse_file(path: Path) -> tuple[list[str], list[str]]:
    with open(path, "r") as f:
        rows = [
            [int(x) if x.isdigit() else x for x in line.split()]
            for line in f if line.strip()
        ]

    return [( [v for v in col[:-1]], col[-1] ) for col in zip(*rows)]

def combine(vals: list):
    return int("".join(str(v) for v in vals))

def parse_file_right_to_left(path: Path) -> tuple[list[str], list[str]]:
    with open(path, "r") as f:
        rows = [line.rstrip("\n") for line in f if line.strip()]
    current_values = []
    current_operator = None
    problems =[]
    columns = list(zip(*rows))[::-1] # Transpose and reverse
    for column in columns:
        if all(item==' ' for item in column):
            problems.append((current_values, current_operator))
            current_values = []
            current_operator = None
        else:
            operator = column[-1].strip()
            if operator:
                current_operator = operator
            value = combine(column[:-1])
            current_values.append(value)
    if current_values:
        problems.append((current_values,current_operator))
    return problems






@timer
def solve(right_to_left: bool = False) -> int:
    total = 0
    operations = parse_file(PATH) if not right_to_left else parse_file_right_to_left(PATH)
    for values, operator in operations:
        if operator == "+":
            total += sum(values)
        elif operator == "*":
            total += prod(values)
    return total



def main() -> None:
    print("Result 1:")
    print(solve())
    print("Result 2:")
    print(solve(right_to_left=True))

if __name__ == "__main__":
    main()