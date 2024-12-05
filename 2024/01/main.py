from collections import Counter
from typing import List

left: List[int] = []
right: List[int] = []

with open("data.txt", "r") as file:
    for line in file:
        parts = line.strip().split(" ")
        left.append(int(parts[0]))
        right.append(int(parts[-1]))

left.sort()
right.sort()

res: int = sum(abs(l - r) for l, r in zip(left, right))
print(res)

count: Counter = Counter(right)
sim: int = sum(count[num] * num for num in left)
print(sim)