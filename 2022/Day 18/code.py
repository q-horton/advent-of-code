def parse(lines):
    drops = []
    for line in lines:
        coord = line.strip().split(",")
        drops.append((int(coord[0]), int(coord[1]), int(coord[2])))
    return drops

def isAdjacent(v1, v2):
    x1, y1, z1 = v1
    x2, y2, z2 = v2
    if abs(x1 - x2) == 1 and y1 == y2 and z1 == z2:
        return True
    elif x1 == x2 and abs(y1 - y2) == 1 and z1 == z2:
        return True
    elif x1 == x2 and y1 == y2 and abs(z1 - z2) == 1:
        return True
    else:
        return False

def run(drops):
    overlap = 0
    for i in range(len(drops)):
        for j in range(i):
            if isAdjacent(drops[i], drops[j]):
                overlap += 1
    return 6 * len(drops) - 2 * overlap

def getBounds(drops):
    mins = list(drops[0])
    maxs = list(drops[0])
    for i in drops:
        x,y,z = i
        if x <= mins[0]:
            mins[0] = x - 1
        elif x >= maxs[0]:
            maxs[0] = x + 1
        if y <= mins[1]:
            mins[1] = y - 1
        elif y >= maxs[1]:
            maxs[1] = y + 1
        if z <= mins[2]:
            mins[2] = z - 1
        elif z >= maxs[2]:
            maxs[2] = z + 1
    return [mins, maxs]

def getAdjacent(point, bounds):
    x,y,z = point
    lx,ly,lz = bounds[0]
    ux,uy,uz = bounds[1]
    adjacent = []
    if lx <= x - 1:
        adjacent.append((x-1, y, z))
    if ux >= x + 1:
        adjacent.append((x+1, y, z))
    if ly <= y - 1:
        adjacent.append((x, y-1, z))
    if uy >= y + 1:
        adjacent.append((x, y+1, z))
    if lz <= z - 1:
        adjacent.append((x, y, z-1))
    if uz >= z + 1:
        adjacent.append((x, y, z+1))
    return adjacent

def isInBounds(point, bounds):
    x,y,z = point
    lx,ly,lz = bounds[0]
    ux,uy,uz = bounds[1]
    return lx <= x and x <= ux and ly <= y and y <= uy and lz <= z and z <= uz

def getExternalAir(drops, bounds):
    came_from = {tuple(bounds[0]): None}
    this_round = [[tuple(bounds[0]), None]]
    previous = []
    while len(this_round) > 0:
        this_round = []
        for i in list(came_from.keys()):
            if not i in previous:
                for j in getAdjacent(i, bounds):
                    this_round.append([j,i])
                    previous.append(i)
        for i in this_round:
            if isInBounds(i[0], bounds) and (not i[0] in drops):
                if not i[0] in came_from.keys():
                    came_from[i[0]] = i[1]
    return list(came_from.keys())

def run2(lines):
    drops = parse(lines)
    bounds = getBounds(drops)
    external_air = getExternalAir(drops, bounds)
    internal_air = []
    for x in range(bounds[0][0] + 1, bounds[1][0]):
        for y in range(bounds[0][1] + 1, bounds[1][1]):
            for z in range(bounds[0][2] + 1, bounds[1][2]):
                if (not (x,y,z) in drops) and (not (x,y,z) in external_air):
                    internal_air.append((x,y,z))
    total_area = run(drops)
    hidden_area = run(internal_air)
    return total_area - hidden_area

with open('./input.txt') as f:
    lines = f.readlines()

#print(run(parse(lines)))

print(run2(lines))