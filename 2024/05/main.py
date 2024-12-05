with open("data.txt", "r") as file:
    lines = file.read().splitlines()
    rules = [tuple(map(int, line.split('|'))) for line in lines[:lines.index('')]]
    updates = [list(map(int, line.split(','))) for line in lines[lines.index('') + 1:]]


def is_update_valid(update, rules):
    for i in range(len(update)):
        for j in range(i + 1, len(update)):
            if (update[j], update[i]) in rules:
                return False
    return True

def find_rules(update,rules):
    applying_rules = []
    for x, y in rules:
        if x in update and y in update:
            applying_rules.append((x, y))
    return applying_rules
def re_order(update, rules):
    applying_rules = find_rules(update, rules)
    if is_update_valid(update, applying_rules):
        return update
    else :
        for page in update:
            for pair in applying_rules:
                if page == pair[1] and update.index(pair[0]) > update.index(pair[1]):
                    new_update = update.copy()
                    new_update.remove(pair[0])
                    new_update.insert(update.index(pair[1]), pair[0])
                    res = re_order(new_update, applying_rules)
                    if res:
                        return res



result_p1 = 0
result_p2 = 0

for update in updates:
    if is_update_valid(update, rules):
        result_p1 += update[len(update) // 2]
    else:
        ordered = re_order(update, rules)
        result_p2 += ordered[len(ordered) // 2]

print(result_p1)
print(result_p2)
