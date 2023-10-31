def parse(lines):
    is_map = True
    start_square = None
    map = []
    pathway = []
    width = 0
    for y, line in enumerate(lines):
        if line[-1] == "\n":
            line = line[:-1]
        if is_map:
            if len(line) > width:
                width = len(line)
            if line == "":
                is_map = False
                continue
            map.append([])
            for x, i in enumerate(line):
                if start_square == None and i == ".":
                    start_square = (x,y)
                map[-1].append(i)
        else:
            start_num = 0
            current_dir = None
            for i in range(len(line)):
                if line[i].isalpha():
                    pathway.append((current_dir, int(line[start_num:i])))
                    current_dir = line[i]
                    if i < len(line) - 1:
                        start_num = i + 1
                if i == len(line) - 1:
                    if line[i].isalpha():
                        pathway.append((current_dir, 0))
                    else:
                        pathway.append((current_dir, int(line[start_num:])))
    for i in range(len(map)):
        if len(map[i]) < width:
            map[i].extend([" "] * (width - len(map[i])))
    return (start_square, map, pathway)

def dir_to_vec(dir):
    if dir == 0:
        return (1, 0)
    elif dir == 1:
        return (0, 1)
    elif dir == 2:
        return (-1, 0)
    elif dir == 3:
        return (0, -1)

def addVecs(v1, v2):
    return (v1[0] + v2[0], v1[1] + v2[1])

def turn(facing, turn):
    if turn == "R":
        return (facing + 1) % 4
    elif turn == "L":
        return (facing - 1) % 4
    elif turn == None:
        return facing

def navigate(start, map, path):
    current = [start[0], start[1], 0]
    move_vec = (0, 0)
    for move in path:
        current[2] = turn(current[2], move[0])
        move_vec = dir_to_vec(current[2])
        for i in range(move[1]):
            nx, ny = addVecs(current[:2], move_vec)
            if nx < 0 or nx >= len(map[current[1]]) or ny < 0 or ny >= len(map) or map[ny][nx] == " ":
                if move_vec == (1, 0):
                    for j in range(len(map[ny])):
                        if map[ny][j] != " ":
                            nx = j
                            break
                elif move_vec == (-1, 0):
                    for j in range(1, len(map[ny]) + 1):
                        if map[ny][-j] != " ":
                            nx = len(map[ny]) - j
                            break
                elif move_vec == (0, 1):
                    for j in range(len(map)):
                        if map[j][nx] != " ":
                            ny = j
                            break
                elif move_vec == (0, -1):
                    for j in range(1, len(map) + 1):
                        if map[-j][nx] != " ":
                            ny = len(map) - j
                            break
            if map[ny][nx] == ".":
                current[0], current[1] = nx, ny
            elif map[ny][nx] == "#":
                break
    return current

def run(lines):
    start, map, path = parse(lines)
    a = navigate(start, map, path)
    row = a[1] + 1
    column = a[0] + 1
    facing = a[2]
    return 1000 * row + 4 * column + facing

def edge(nx, ny, dir):
    if ny == -1 and dir == 3:
        if nx // 50 == 1:
            x = 0
            y = nx + 100
            f = 0
        elif nx // 50 == 2:
            x = nx - 100
            y = 199
            f = 3
    elif ny == 50 and dir == 1:
        x = 99
        y = nx - 50
        f = 2
    elif ny == 99 and dir == 3:
        x = 50
        y = nx + 50
        f = 0
    elif ny == 150 and dir == 1:
        x = 49
        y = nx + 100
        f = 2
    elif ny == 200 and dir == 1:
        x = nx + 100
        y = 0
        f = 1
    elif nx == -1 and dir == 2:
        if ny // 50 == 2:
            x = 50
            y = 49 - (ny - 100)
            f = 0
        elif ny // 50 == 3:
            x = ny - 100
            y = 0
            f = 1
    elif nx == 49 and dir == 2:
        if ny // 50 == 0:
            x = 0
            y = (49 - ny) + 100
            f = 0
        elif ny // 50 == 1:
            x = ny - 50
            y = 100
            f = 1
    elif nx == 50 and dir == 0:
        x = ny - 100
        y = 149
        f = 3
    elif nx == 100 and dir == 0:
        if ny // 50 == 1:
            x = ny + 50
            y = 49
            f = 3
        elif ny // 50 == 2:
            x = 149
            y = 49 - (ny - 100)
            f = 2
    elif nx == 150 and dir == 0:
        x = 99
        y = (49 - ny) + 100
        f = 2
    return (x, y, f)

def navigate2(start, map, path):
    current = [start[0], start[1], 0]
    for move in path:
        current[2] = turn(current[2], move[0])
        for _ in range(move[1]):
            nx, ny = addVecs(current[:2], dir_to_vec(current[2]))
            nd = current[2]
            if nx < 0 or nx >= len(map[current[1]]) or ny < 0 or ny >= len(map) or map[ny][nx] == " ":
                nx, ny, nd = edge(nx, ny, nd)
            if map[ny][nx] == ".":
                current = [nx, ny, nd]
            elif map[ny][nx] == "#":
                break
    return current

def run2(lines):
    start, map, path = parse(lines)
    a = navigate2(start, map, path)
    row = a[1] + 1
    column = a[0] + 1
    facing = a[2]
    return 1000 * row + 4 * column + facing

with open('./input.txt') as f:
    lines = f.readlines()

#print(run(lines))

print(run2(lines))