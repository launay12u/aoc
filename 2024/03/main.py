import re
from typing import List, Tuple

with open("data.txt", "r") as file:
    memory: str = file.read()

mul_regex: str = r"mul\((\d{1,3}),(\d{1,3})\)"
control_regex: str = r"(do\(\)|don't\(\))"


def compute_mul(matches: List[Tuple[str, str, str]],verify_control: bool = False) -> int:
    enable: bool = True
    total: int = 0
    for match in matches:
        x, y, control = match
        if verify_control:
            if control == "do()":
                enable = True
            elif control == "don't()":
                enable = False
        if x and y:
            if enable:
                total += int(x) * int(y)

    return total


matches: List[Tuple[str, str, str]] = re.findall(f"{mul_regex}|{control_regex}", memory)

total_part_1: int = compute_mul(matches)
total_part_2: int = compute_mul(matches, verify_control=True)

print(total_part_1)
print(total_part_2)
