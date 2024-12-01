from collections import Counter
left, right = [], []
with open("data.txt", "r") as file:
    for line in file:
        parts = line.strip().split(" ")
        l, r = int(parts[0]), int(parts[-1])
        left.append(l)
        right.append(r)

left.sort()
right.sort()
res = 0
for i,num in enumerate(left):
	res+= abs(num - right[i])
print(res)

count = Counter(right)
sim = 0

for num in left:
    if num in count:
      sim += num * count[num]
print(sim)
