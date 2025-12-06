from pathlib import Path
from dataclasses import dataclass

from utils.time_decorator import timer

PATH = Path(__file__).parent / "data.txt"



def parse_file(path: Path) -> tuple[list[str], list[str]]:

    fresh = []
    values = []

    with open(path, "r") as f:
        lines = [line.strip() for line in f]

    # Split on blank line
    blank_index = lines.index("")

    range_lines = lines[:blank_index]
    value_lines = lines[blank_index + 1:]

    # Parse ranges
    for line in range_lines:
        start, end = line.split("-")
        fresh.append((int(start), int(end)))

    # Parse individual values
    for line in value_lines:
        values.append(int(line))

    return fresh, values




@timer
def solve(list: bool) -> int:
    total = 0
    fresh, values = parse_file(PATH)
    ranges = sorted(fresh, key=lambda x: x[0])

    merged = []
    cur_start, cur_end = ranges[0]

    for start, end in ranges[1:]:
        if start <= cur_end + 1:
            cur_end = max(cur_end, end)
        else:
            merged.append((cur_start, cur_end))
            cur_start, cur_end = start, end

    merged.append((cur_start, cur_end))

    if list:
        values_sorted = sorted(values)
        i = 0
        for value in values_sorted:
            while i < len(merged) and merged[i][1] < value:
                i += 1
            if i < len(merged) and merged[i][0] <= value <= merged[i][1]:
                total += 1
    else:
        total = sum(end - start + 1 for start, end in merged)
    return total



def main() -> None:
    print("Result 1:")
    print(solve(True))
    print("Result 2:")
    print(solve(False))

if __name__ == "__main__":
    main()