def parse(lines):
    splitters = []
    start = ()
    for y in range(len(lines)):
        for x in range(len(lines[y])):
            if lines[y][x] == 'S':
                start = (x, y)
            elif lines[y][x] == '^':
                splitters.append((x, y))
    return [start, splitters, (len(lines[0]), len(lines))]

def run(inp):
    start, splitters, dims = parse(inp)
    split_count = 0
    prev_row = [False] * dims[0]
    prev_row[start[0]] = True
    for y in range(start[1] + 1, dims[1]):
        next_row = [False] * dims[0]
        for x in range(dims[0]):
            if not prev_row[x]:
                continue
            elif (x, y) in splitters:
                split_count += 1
                next_row[x - 1] = True
                next_row[x + 1] = True
            else:
                next_row[x] = True
        prev_row = next_row
    print(split_count)

def run2(inp):
    start, splitters, dims = parse(inp)
    prev_row = [0] * dims[0]
    prev_row[start[0]] = 1
    for y in range(start[1] + 1, dims[1]):
        next_row = [0] * dims[0]
        for x in range(dims[0]):
            if prev_row[x] == 0:
                continue
            elif (x, y) in splitters:
                next_row[x - 1] += prev_row[x]
                next_row[x + 1] += prev_row[x]
            else:
                next_row[x] += prev_row[x]
        prev_row = next_row
    print(sum(next_row))

with open('./input.txt') as f:
    lines = f.readlines()

run2(lines)
