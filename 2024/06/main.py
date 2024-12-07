with open('data.txt') as f:
    lines = f.read().splitlines()


def init(lines):
    start = ()
    obstacles =[]
    for i in range(len(lines)):
        for j in range(len(lines[0])):
            if lines[i][j] == "^":
                start =(i, j)
            elif lines[i][j] == "#":
                obstacles.append((i,j))
    return start, obstacles

def on_map(x, y, height, width):
    return 0 <= x < height and 0 <= y < width


def turn(dir):
    return (dir + 1) % 4


def step(pos, dx, dy):
    return (pos[0] + dx, pos[1] + dy)


def walk(lines,added_obstacle=None):
    height = len(lines)
    width = len(lines[0])
    visited = set()
    start, obstacles = init(lines)
    if added_obstacle:
        obstacles.append(added_obstacle)
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    dir = 0
    pos = start
    while on_map(pos[0], pos[1], height, width):
        visited.add((pos,dir))
        dx, dy = directions[dir]

        if (pos[0] + dx, pos[1] + dy) in obstacles:
            dir = turn(dir)
            dx, dy = directions[dir]
        if ((pos[0] + dx, pos[1] + dy),dir) in visited:
            raise Exception('Loop found')
        pos = step(pos, dx, dy)

    return visited


def check_loop(pos, dir, obstacle, lines,obstacles):
    height = len(lines)
    width = len(lines[0])
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    check_states = set()

    while on_map(pos[0], pos[1], height, width):
        check_states.add((pos, dir))
        dx, dy = directions[dir]

        # Turn if needed (avoid obstacles and current obstacle)
        if (pos[0] + dx, pos[1] + dy) in obstacles or (pos[0] + dx, pos[1] + dy) == obstacle:
            dir = turn(dir)
            dx, dy = directions[dir]

        if ((pos[0] + dx, pos[1] + dy), dir) in check_states:
            # Found loop
            return True

        # Step forward
        pos = step(pos, dx, dy)

    return False


def get_good_obstacles(visited):
    visited = walk(lines)
    good_obstacle = set()
    start,_ = init(lines)
    for new_obstacle in visited:
        try :
            walk(lines, new_obstacle[0])
        except:
            good_obstacle.add(new_obstacle[0])

    return good_obstacle

visited = walk(lines)
count_unique_visited = len(set([x[0] for x in visited]))
print(count_unique_visited)
good_obstacle = get_good_obstacles(visited)
count_good_obstacle = len(good_obstacle)
print(count_good_obstacle)
