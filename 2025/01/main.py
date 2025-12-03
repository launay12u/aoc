from pathlib import Path
from dataclasses import dataclass
from enum import Enum

from utils.time_decorator import timer

PATH = Path(__file__).parent / "data.txt"

# Use constants instead of magic numbers
DIAL_SIZE = 100
START_POSITION = 50


class Direction(Enum):
    LEFT = 'L'
    RIGHT = 'R'


@dataclass
class Instruction:
    direction: Direction
    steps: int


def parse_file(path: Path) -> list[Instruction]:
    with path.open() as file:
        return [parse_line(line) for line in file]


def parse_line(line: str) -> Instruction:
    return Instruction(
        direction=Direction(line[0]),
        steps=int(line[1:].strip())
    )


def rotate_dial(current: int, instruction: Instruction) -> int:
    delta = instruction.steps if instruction.direction == Direction.RIGHT else -instruction.steps
    return (current + delta) % DIAL_SIZE


def count_zero_crossings(current: int, instruction: Instruction) -> tuple[int, int]:
    if instruction.direction == Direction.RIGHT:
        zeros = (current + instruction.steps) // DIAL_SIZE
    else:
        # If current is 0, prevent counting the same zero twice (already counted last time when stop on zero)
        zeros = 0 if current != 0 else -1 
        zeros += (instruction.steps + DIAL_SIZE - current) // DIAL_SIZE
    
    return rotate_dial(current, instruction), zeros

@timer
def solve(count_all_crossings: bool = False) -> int:
    current = START_POSITION
    total_zeros = 0
    
    for instruction in parse_file(PATH):
        if count_all_crossings:
            current, zeros = count_zero_crossings(current, instruction)
            total_zeros += zeros
        else:
            current = rotate_dial(current, instruction)
            if current == 0:
                total_zeros += 1
    
    return total_zeros


def main() -> None:
    print("Result 1:")
    print(solve(count_all_crossings=False))
    print("Result 2:")
    print(solve(count_all_crossings=True))

if __name__ == "__main__":
    main()