def parse(lines):
    map = []
    for line in lines:
        row = []
        for i in line.strip():
            if i == '@':
                row.append(1)
            else:
                row.append(0)
        map.append(row)
    return map

def run(inp):
    map = parse(inp)
    new_map = ""
    count = 0
    for y in range(len(map)):
        for x in range(len(map[y])):
            if map[y][x] == 0:
                new_map += "."
                continue
            adj = 0
            for i in range(x - 1, x + 2):
                for j in range(y - 1, y + 2):
                    if (i < 0) or (j < 0) or (i >= len(map[y])) or (j >= len(map)):
                        continue
                    else:
                        adj += map[j][i]
            if adj <= 4:
                new_map += "x"
                count += 1
            else:
                new_map += "@"
        new_map += "\n"
    print(f"{new_map}------\n{count}")

def run2(inp):
    map = parse(inp)
    count = 0
    while True:
        new_map = []
        new_count = 0
        for y in range(len(map)):
            new_map.append([])
            for x in range(len(map[y])):
                if map[y][x] == 0:
                    new_map[-1].append(0)
                    continue
                adj = 0
                for i in range(x - 1, x + 2):
                    for j in range(y - 1, y + 2):
                        if (i < 0) or (j < 0) or (i >= len(map[y])) or (j >= len(map)):
                            continue
                        else:
                            adj += map[j][i]
                if adj <= 4:
                    new_map[-1].append(0)
                    new_count += 1
                else:
                    new_map[-1].append(1)
        if new_count == 0:
            break
        map = new_map
        count += new_count
    print(count)

with open('./input.txt') as f:
    lines = f.readlines()

run2(lines)
