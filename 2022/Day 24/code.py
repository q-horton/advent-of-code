def parse(lines):
    mapping = {}
    start, end = None, None
    for y, line in enumerate(lines):
        line = line.strip()
        for x, i in enumerate(line):
            if y == 0 and i == ".":
                start = (x,y)
            elif y == len(lines) - 1 and i == ".":
                end = (x,y)
            if i != ".":
                mapping[(x,y)] = [i]
    return (mapping, start, end)

def getMoves(mapping, coord):
    x,y = coord
    moves = []
    if not (x, y+1) in mapping:
        moves.append((x, y+1))
    if not (x+1, y) in mapping:
        moves.append((x+1, y))
    if not (x-1, y) in mapping:
        moves.append((x-1, y))
    if not (x, y) in mapping:
        moves.append((x, y))
    if not (x, y-1) in mapping:
        moves.append((x, y-1))
    return moves

def moveBliz(mapping, start, end):
    new_mapping = {}
    for (c, b) in mapping.items():
        if "#" in b:
            new_mapping[c] = ["#"]
        else:
            for i in b:
                unmoved = True
                if i == "^":
                    if (c[0], c[1]-1) in mapping:
                        if "#" in mapping[(c[0], c[1]-1)]:
                            if end[0] == c[0]:
                                if not (end[0], end[1]-1) in new_mapping:
                                    new_mapping[(end[0], end[1]-1)] = []
                                new_mapping[(end[0], end[1]-1)].append("^")
                                unmoved = False
                            else:
                                for j in range(c[1],c[1]+len(mapping)):
                                    if (c[0], j) in mapping:
                                        if "#" in mapping[(c[0], j)]:
                                            if not (c[0], j-1) in new_mapping:
                                                new_mapping[(c[0], j-1)] = []
                                            new_mapping[(c[0], j-1)].append("^")
                                            unmoved = False
                                            break
                    if unmoved and c != start:
                        if not (c[0], c[1]-1) in new_mapping:
                            new_mapping[(c[0], c[1]-1)] = []
                        new_mapping[(c[0], c[1]-1)].append("^")
                elif i == "v":
                    if (c[0], c[1]+1) in mapping:
                        if "#" in mapping[(c[0], c[1]+1)]:
                            if start[0] == c[0]:
                                if not (start[0], start[1]+1) in new_mapping:
                                    new_mapping[(start[0], start[1]+1)] = []
                                new_mapping[(start[0], start[1]+1)].append("v")
                                unmoved = False
                            else:
                                for j in range(c[1],c[1]-len(mapping),-1):
                                    if (c[0], j) in mapping:
                                        if "#" in mapping[(c[0], j)]:
                                            if not (c[0], j+1) in new_mapping:
                                                new_mapping[(c[0], j+1)] = []
                                            new_mapping[(c[0], j+1)].append("v")
                                            unmoved = False
                                            break
                    if unmoved and c != end:
                        if not (c[0], c[1]+1) in new_mapping:
                            new_mapping[(c[0], c[1]+1)] = []
                        new_mapping[(c[0], c[1]+1)].append("v")
                elif i == "<":
                    if (c[0]-1, c[1]) in mapping:
                        if "#" in mapping[(c[0]-1, c[1])]:
                            for j in range(c[0],c[0]+len(mapping)):
                                if (j, c[1]) in mapping:
                                    if "#" in mapping[(j, c[1])]:
                                        if not (j-1, c[1]) in new_mapping:
                                            new_mapping[(j-1, c[1])] = []
                                        new_mapping[(j-1, c[1])].append("<")
                                        unmoved = False
                                        break
                    if unmoved:
                        if not (c[0]-1, c[1]) in new_mapping:
                            new_mapping[(c[0]-1, c[1])] = []
                        new_mapping[(c[0]-1, c[1])].append("<")
                elif i == ">":
                    if (c[0]+1, c[1]) in mapping:
                        if "#" in mapping[(c[0]+1, c[1])]:
                            for j in range(c[0],c[0]-len(mapping),-1):
                                if (j, c[1]) in mapping:
                                    if "#" in mapping[(j, c[1])]:
                                        if not (j+1, c[1]) in new_mapping:
                                            new_mapping[(j+1, c[1])] = []
                                        new_mapping[(j+1, c[1])].append(">")
                                        unmoved = False
                                        break
                    if unmoved:
                        if not (c[0]+1, c[1]) in new_mapping:
                            new_mapping[(c[0]+1, c[1])] = []
                        new_mapping[(c[0]+1, c[1])].append(">")
    return new_mapping

def run(lines):
    mapping, start, end = parse(lines)
    paths = [start]
    time = 0
    while True:
        time += 1
        new_paths = []
        mapping = moveBliz(mapping, start, end)
        for i in paths:
            moves = getMoves(mapping, i)
            for j in moves:
                if (not j[1] < start[1]) and (not j[1] > end[1]) and (not j in new_paths) and (not j in mapping):
                    new_paths.append(j)
        paths = new_paths.copy()
        if end in paths:
            return time

def run2(lines):
    mapping, start, end = parse(lines)
    paths = [start]
    time = 0
    while True:
        time += 1
        new_paths = []
        mapping = moveBliz(mapping, start, end)
        for i in paths:
            moves = getMoves(mapping, i)
            for j in moves:
                if (not j[1] < start[1]) and (not j[1] > end[1]) and (not j in new_paths) and (not j in mapping):
                    new_paths.append(j)
        paths = new_paths.copy()
        if end in paths:
            paths = [end]
            break
    while True:
        time += 1
        new_paths = []
        mapping = moveBliz(mapping, start, end)
        for i in paths:
            moves = getMoves(mapping, i)
            for j in moves:
                if (not j[1] < start[1]) and (not j[1] > end[1]) and (not j in new_paths) and (not j in mapping):
                    new_paths.append(j)
        paths = new_paths.copy()
        if start in paths:
            paths = [start]
            break
    while True:
        time += 1
        new_paths = []
        mapping = moveBliz(mapping, start, end)
        for i in paths:
            moves = getMoves(mapping, i)
            for j in moves:
                if (not j[1] < start[1]) and (not j[1] > end[1]) and (not j in new_paths) and (not j in mapping):
                    new_paths.append(j)
        paths = new_paths.copy()
        if end in paths:
            return time

with open('./input.txt') as f:
    lines = f.readlines()

#print(run(lines))

print(run2(lines))