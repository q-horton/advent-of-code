def parse(lines):
    map = []
    for i in lines:
        if i[-1] == "\n":
            i = i[:-1]
        map.append([])
        for j in i:
            map[-1].append(int(j))
    return map

def checkTree(forest_map, coords):
    visible = False
    x = coords[0]
    y = coords[1]
    blockage = False
    for i in range(x):
        if forest_map[i][y] >= forest_map[x][y]:
            blockage = True
            break
    if not blockage:
        visible = True
    blockage = False
    for i in range(x+1, len(forest_map)):
        if forest_map[i][y] >= forest_map[x][y]:
            blockage = True
            break
    if not blockage:
        visible = True
    blockage = False
    for i in range(y):
        if forest_map[x][i] >= forest_map[x][y]:
            blockage = True
            break
    if not blockage:
        visible = True
    blockage = False
    for i in range(y+1, len(forest_map[x])):
        if forest_map[x][i] >= forest_map[x][y]:
            blockage = True
            break
    if not blockage:
        visible = True
    blockage = False
    return visible

def run(lines):
    forest_map = parse(lines)
    visible = 2*len(forest_map) + 2*(len(forest_map[0]) - 2)
    for i in range(1,len(forest_map) - 1):
        for j in range(1, len(forest_map[0]) - 1):
            if checkTree(forest_map, (i, j)):
                visible += 1
    return visible

def viewDists(forest_map, coords):
    view_dist = [0, 0, 0, 0]
    x = coords[0]
    y = coords[1]
    for i in range(x):
        view_dist[0] += 1
        if forest_map[x-i-1][y] >= forest_map[x][y]:
            break
    for i in range(x+1, len(forest_map)):
        view_dist[1] += 1
        if forest_map[i][y] >= forest_map[x][y]:
            break
    for i in range(y):
        view_dist[2] += 1
        if forest_map[x][y-i-1] >= forest_map[x][y]:
            break
    for i in range(y+1, len(forest_map[x])):
        view_dist[3] += 1
        if forest_map[x][i] >= forest_map[x][y]:
            break
    return view_dist

def scenicScore(forest_map, coords):
    view_dist = viewDists(forest_map, coords)
    score = 1
    for i in view_dist:
        score *= i
    return score

def run2(lines):
    forest_map = parse(lines)
    max_scenic = 0
    for i in range(len(forest_map)):
        for j in range(len(forest_map[0])):
            if scenicScore(forest_map, (i,j)) > max_scenic:
                max_scenic = scenicScore(forest_map, (i,j))
    return max_scenic

with open('./input.txt') as f:
    lines = f.readlines()

#print(run(lines))

print(run2(lines))