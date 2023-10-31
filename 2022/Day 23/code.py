def parse(lines):
    mapping = []
    for (y, line) in enumerate(lines):
        line = line.strip()
        for (x, i) in enumerate(line):
            if i == "#":
                mapping.append((x,y))
    return mapping

def getOpen(mapping, coord):
    x, y = coord
    open_spaces = []
    if (x-1, y-1) in mapping:
        open_spaces.append("NW")
    if (x, y-1) in mapping:
        open_spaces.append("N")
    if (x+1, y-1) in mapping:
        open_spaces.append("NE")
    if (x-1, y) in mapping:
        open_spaces.append("W")
    if (x+1, y) in mapping:
        open_spaces.append("E")
    if (x-1, y+1) in mapping:
        open_spaces.append("SW")
    if (x, y+1) in mapping:
        open_spaces.append("S")
    if (x+1, y+1) in mapping:
        open_spaces.append("SE")
    return open_spaces

def roundOne(mapping, round):
    checks = [(["N", "NE", "NW"], (0, -1)), (["S", "SE", "SW"], (0, 1)), (["W", "NW", "SW"], (-1, 0)), (["E", "NE", "SE"], (1, 0))]
    new_pos = {}
    for i in mapping:
        open_adj = getOpen(mapping, i)
        x, y = i
        if len(open_adj) == 0:
            new_pos[(x, y)] = (x, y)
        elif not (checks[round % 4][0][0] in open_adj or checks[round % 4][0][1] in open_adj or checks[round % 4][0][2] in open_adj):
            new_pos[(x, y)] = (x + checks[round % 4][1][0], y + checks[round % 4][1][1])
        elif not (checks[(round + 1) % 4][0][0] in open_adj or checks[(round + 1) % 4][0][1] in open_adj or checks[(round + 1) % 4][0][2] in open_adj):
            new_pos[(x, y)] = (x + checks[(round + 1) % 4][1][0], y + checks[(round + 1) % 4][1][1])
        elif not (checks[(round + 2) % 4][0][0] in open_adj or checks[(round + 2) % 4][0][1] in open_adj or checks[(round + 2) % 4][0][2] in open_adj):
            new_pos[(x, y)] = (x + checks[(round + 2) % 4][1][0], y + checks[(round + 2) % 4][1][1])
        elif not (checks[(round + 3) % 4][0][0] in open_adj or checks[(round + 3) % 4][0][1] in open_adj or checks[(round + 3) % 4][0][2] in open_adj):
            new_pos[(x, y)] = (x + checks[(round + 3) % 4][1][0], y + checks[(round + 3) % 4][1][1])
        else:
            new_pos[(x, y)] = (x, y)
    return new_pos

def run(lines):
    mapping = parse(lines)
    for round in range(10):
        new_mapping = []
        prop_map = roundOne(mapping, round)
        for (a,b) in prop_map.items():
            if list(prop_map.values()).count(b) > 1:
                new_mapping.append(a)
            else:
                new_mapping.append(b)
        mapping = new_mapping.copy()
    bounds = [list(mapping[0]), list(mapping[0])]
    for i in mapping:
        x,y = i
        if x < bounds[0][0]:
            bounds[0][0] = x
        elif x > bounds[1][0]:
            bounds[1][0] = x
        if y < bounds[0][1]:
            bounds[0][1] = y
        elif y > bounds[1][1]:
            bounds[1][1] = y
    total_area = (bounds[1][0] - bounds[0][0] + 1) * (bounds[1][1] - bounds[0][1] + 1)
    return total_area - len(mapping)

def run2(lines):
    mapping = parse(lines)
    round = 0
    while True:
        new_mapping = []
        prop_map = roundOne(mapping, round)
        for (a,b) in prop_map.items():
            if list(prop_map.values()).count(b) > 1:
                new_mapping.append(a)
            else:
                new_mapping.append(b)
        if mapping == new_mapping:
            break
        mapping = new_mapping.copy()
        round += 1
    return round + 1

with open('./input.txt') as f:
    lines = f.readlines()

#print(run(lines))

print(run2(lines))