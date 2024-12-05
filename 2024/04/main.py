with open("data.txt", "r") as file:
    words: str = file.read()

data = words.split()


def get_diagonals(grid):
    rows = len(grid)
    cols = len(grid[0])

    left_diagonals = {}
    right_diagonals = {}

    for r in range(rows):
        for c in range(cols):
            key_main = r - c
            if key_main not in left_diagonals:
                left_diagonals[key_main] = ""
            left_diagonals[key_main] += grid[r][c]

            key_anti = r + c
            if key_anti not in right_diagonals:
                right_diagonals[key_anti] = ""
            right_diagonals[key_anti] += grid[r][c]

    combined_diagonals = list(left_diagonals.values()) + list(right_diagonals.values())
    return combined_diagonals


all_data = data.copy()
transpose = [''.join(row) for row in zip(*data)]

all_data.extend(get_diagonals(data))
all_data.extend(transpose)

print(sum(line.count("XMAS") + line.count("SAMX") for line in all_data))


def count_x_mas(grid):
    count = 0
    for r in range(1, len(grid) - 1):
        for c in range(1, len(grid[0]) - 1):
            missing = {"M", "S"}
            if data[r][c] == "A":
                if ({data[r - 1][c - 1], data[r + 1][c + 1]} == missing
                and {data[r - 1][c + 1], data[r + 1][c - 1]} == missing):
                    count += 1
    return count

print(count_x_mas(data))
