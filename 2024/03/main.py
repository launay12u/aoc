import re
with open("data.txt", "r") as file:
    memory = file.read()

total = 0
mul_regex = r"mul\((\d{1,3}),(\d{1,3})\)"
matches = re.findall(mul_regex, memory)
for match in matches:
    x,y = match
    total += int(x) * int(y)
print(total)

control_regex = r"(do\(\)|don't\(\))"
matches = re.findall(f"{mul_regex}|{control_regex}", memory)
total = 0
enable=True
for match in matches:
    if match[2] == "do()":
        enable=True
    elif match[2] == "don't()":
        enable=False
    elif match[2] == "" and enable:
        total += int(match[0]) * int(match[1])
print(total)