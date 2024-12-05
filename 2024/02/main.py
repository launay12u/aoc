from typing import List

reports: List[List[int]] = []
with open("data.txt", "r") as file:
    for line in file:
        reports.append([int(item) for item in line.strip().split(" ")])

def is_safe(levels: List[int], tolerance: bool = False) -> bool:
    direction = 1 if levels[0] < levels[1] else -1
    for x in range(1, len(levels)):
        differ = (levels[x] - levels[x - 1])
        if abs(differ) in {1, 2, 3} or differ * direction < 0:
            if not tolerance:
                return False
            for i in range(len(levels)):
                levels_copy = levels[:i] + levels[i + 1:]
                if is_safe(levels_copy):
                    return True
            return False
    return True

count_safe_report: int = sum(1 for levels in reports if is_safe(levels))
print(count_safe_report)

count_safe_report_with_tolerance: int = sum(1 for levels in reports if is_safe(levels, tolerance=True))
print(count_safe_report_with_tolerance)
