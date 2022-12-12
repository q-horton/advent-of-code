def parse(lines):
    start_coords = ()
    end_coords = ()
    height_map = []
    for y in range(len(lines)):
        line = lines[y]
        if line[-1] == "\n":
            line = line[:-1]
        height_map.append([])
        for x in range(len(line)):
            if line[x] == "S":
                start_coords = (x, y)
                height_map[y].append(0)
            elif line[x] == "E":
                end_coords = (x, y)
                height_map[y].append(25)
            else:
                height = ord(line[x]) - ord('a')
                height_map[y].append(height)
    return (height_map, start_coords, end_coords)

def nextTo(x_dim, y_dim, coord):
    next_to = []
    x = coord[0]
    y = coord[1]
    if x > 0:
        next_to.append((x-1, y))
    if y > 0:
        next_to.append((x, y-1))
    if x < x_dim - 1:
        next_to.append((x+1, y))
    if y < y_dim - 1:
        next_to.append((x, y+1))
    return next_to

def isAdjacent(previous, next):
    return abs(previous[0] - next[0]) + abs(previous[1] - next[1]) == 1

def isPredecessor(height_map, previous, next):
    if isAdjacent(previous, next):
        prev_height = height_map[previous[1]][previous[0]]
        next_height = height_map[next[1]][next[0]]
        if next_height <= prev_height + 1:
            return True
    return False
        
def backtrackMap(height_map, end):
    came_from = {end: None}
    this_round = [[end, None]]
    previous = []
    while len(this_round) > 0:
        this_round = []
        for i in list(came_from.keys()):
            if not i in previous:
                for j in nextTo(len(height_map[0]), len(height_map), i):
                    this_round.append([j,i])
                    previous.append(i)
        for i in this_round:
            if isPredecessor(height_map, i[0], i[1]):
                if not i[0] in came_from.keys():
                    came_from[i[0]] = i[1]
    return came_from
            
def run(lines):
    height_map, start, end = parse(lines)
    next_up = backtrackMap(height_map, end)
    path = [start]
    while path[-1] != end:
        path.append(next_up[path[-1]])
    return len(path) - 1

def run2(lines):
    height_map, start, end = parse(lines)
    next_up = backtrackMap(height_map, end)
    lowest = []
    for y in range(len(height_map)):
        for x in range(len(height_map[y])):
            if height_map[y][x] == 0:
                lowest.append((x,y))
    shortest = len(height_map) * len(height_map[0])
    for i in lowest:
        if i in next_up.keys():
            path = [i]
            while path[-1] != end:
                path.append(next_up[path[-1]])
            if len(path) - 1 < shortest:
                shortest = len(path) - 1
    return shortest

with open('./input.txt') as f:
    lines = f.readlines()

#print(run(lines))

print(run2(lines))