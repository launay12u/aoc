from pathlib import Path
from dataclasses import dataclass

from utils.time_decorator import timer

PATH = Path(__file__).parent / "data.txt"

@dataclass
class Bank:
    bateries: list[str]


def parse_file(path: Path) -> list[Bank]:
    banks = []
    with path.open() as file:
        for line in file:
            banks.append(parse_line(line.strip()))
    return banks


def parse_line(line: str) -> Bank:
    parsed_bank = []
    for char in line:
        parsed_bank.append(char)
    return Bank(parsed_bank)

def get_max_joltage(bank: Bank,action=12) -> int:
    batteries = bank.bateries
    n = len(batteries)
    result = []
    start = 0

    for remaining in range(action, 0, -1):
        end = n - remaining + 1
        max_digit = max(batteries[start:end])
        idx = batteries.index(max_digit, start, end)
        result.append(max_digit)
        start = idx + 1

    return int("".join(result))

@timer
def solve(action=12) -> int:
    sum = 0
    for banks in parse_file(PATH):
        sum += get_max_joltage(banks,action)
    return sum


def main() -> None:
    print("Result 1:")
    print(solve(2))
    print("Result 2:")
    print(solve(12))

if __name__ == "__main__":
    main()