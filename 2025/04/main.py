from pathlib import Path
from dataclasses import dataclass

from utils.time_decorator import timer

PATH = Path(__file__).parent / "data.txt"



def parse_file(path: Path) -> list[str]:
    locations = []
    with path.open() as file:
        for line in file:
            locations.append(parse_line(line.strip()))
    return locations


def parse_line(line: str) -> str:
    return [char for char in line]


def is_accessible(x,y,lines) -> bool:
    adjacent_paper = 0
    adjacent_locations = [
        (x-1, y-1),
        (x-1, y),
        (x-1, y+1),
        (x, y-1),
        (x, y+1),
        (x+1, y-1),
        (x+1, y),
        (x+1, y+1)
    ]
    for location in adjacent_locations:
        if (
            0 <= location[0] < len(lines) and
            0 <= location[1] < len(lines[0]) and
            lines[location[0]][location[1]] == "@"
        ):
            adjacent_paper += 1
    return adjacent_paper < 4

@timer
def solve(should_retry: bool = False) -> int:
    total = 0
    lines = parse_file(PATH)
    first_pass = True
    loop_retry = should_retry

    while first_pass or loop_retry:
        first_pass = False
        loop_retry = False
        new_lines = [row.copy() for row in lines]
        for i, line in enumerate(lines):
            for j, char in enumerate(line):
                if char == "@":
                    if is_accessible(i, j, lines):
                        new_lines[i][j] = "."
                        loop_retry = should_retry
                        total += 1
        lines = new_lines

    return total



def main() -> None:
    print("Result 1:")
    print(solve())
    print("Result 2:")
    print(solve(True))

if __name__ == "__main__":
    main()