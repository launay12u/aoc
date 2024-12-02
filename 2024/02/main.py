reports = []
with open("data.txt", "r") as file:
    for line in file:
        reports.append([int(item) for item in line.strip().split(" ")])


def is_safe(levels) -> bool:
    direction = 1 if levels[0] < levels[1] else -1
    for x in range(1,len(levels)):
        differ = (levels[x] - levels[x-1])
        if abs(differ) > 3 or differ == 0 or differ * direction < 0:
            return False
    return True
def is_safe_tolerance(levels) -> bool:
    if is_safe(levels):
        return True

    for i in range(len(levels)):
        levels_copy = levels[:i] + levels[i + 1:]
        if is_safe(levels_copy):
            return True

count_safe = 0
for levels in reports:
 if is_safe(levels):
     count_safe += 1
print(count_safe)

count_safe = 0
for levels in reports:
 if is_safe_tolerance(levels):
     count_safe += 1
print(count_safe)

