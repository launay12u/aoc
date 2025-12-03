from pathlib import Path
from dataclasses import dataclass

from utils.time_decorator import timer

PATH = Path(__file__).parent / "data.txt"

# Use constants instead of magic numbers
DIAL_SIZE = 100
START_POSITION = 50


@dataclass
class Range:
    first: int
    last: int

def is_invalid(id: str, split: int) -> bool:
    if len(id) % split != 0:
        return False
    
    if split == 1:
        return len(set(id)) == 1
    
    part_size = len(id) // split
    first_part = id[:part_size]
    for i in range(1, split):
        next_part = id[i * part_size:(i + 1) * part_size]
        if next_part != first_part:
            return False
    
    return True


def parse_file(path: Path) -> list[Range]:
    ranges = []
    with path.open() as file:
        for line in file:
            ranges.extend(parse_line(line.strip().split(",")))
    return ranges


def parse_line(id_ranges: list[str]) -> list[Range]:
    parsed_ranges = []
    for range_str in id_ranges:
        first, last = range_str.strip().split("-")
        parsed_ranges.append(Range(int(first), int(last)))
    return parsed_ranges

def sum_invalid_ids(id_range: Range, only_twice: bool) -> int:
    sum = 0
    for id in range(id_range.first, id_range.last+1):
        if only_twice:
            if is_invalid(str(id),2):
                sum += id
        else:
            for split in range(1, (len(str(id)) // 2)+1):
                if is_invalid(str(id),split):
                    sum += id
                    break
    return sum

@timer
def solve(only_twice: bool) -> int:
    sum = 0
    for range in parse_file(PATH):
        sum += sum_invalid_ids(range, only_twice)
    return sum


def main() -> None:
    print("Result 1:")
    print(solve(True))
    print("Result 2:")
    print(solve(False))

if __name__ == "__main__":
    main()