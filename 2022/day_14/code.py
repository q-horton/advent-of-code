def parse(lines):
    rocks = {}
    lowest = 0
    for line in lines:
        end_points = line.strip().split(" -> ")
        for i in range(len(end_points)):
            end_points[i] = eval("(" + end_points[i] + ")")
            if end_points[i][1] > lowest:
                lowest = end_points[i][1]
        for i in range(len(end_points)-1):
            if end_points[i][0] == end_points[i+1][0]:
                if end_points[i][1] > end_points[i+1][1]:
                    for j in range(end_points[i+1][1]+1, end_points[i][1]+1):
                        rocks[(end_points[i][0], j)] = "#"
                else:
                    for j in range(end_points[i][1], end_points[i+1][1]):
                        rocks[(end_points[i][0], j)] = "#"
            elif end_points[i][1] == end_points[i+1][1]:
                if end_points[i][0] > end_points[i+1][0]:
                    for j in range(end_points[i+1][0]+1, end_points[i][0]+1):
                        rocks[(j, end_points[i][1])] = "#"
                else:
                    for j in range(end_points[i][0], end_points[i+1][0]):
                        rocks[(j, end_points[i][1])] = "#"
        rocks[end_points[-1]] = "#"
    rocks[(500, 0)] = "+"
    return (rocks, (500, 0), lowest)

def newSand(mapping, start, lowest):
    x, y = start
    while True:
        if y == lowest:
            return False
        else:
            if not (x,y+1) in mapping:
                y += 1
            elif not (x-1,y+1) in mapping:
                x -= 1
                y += 1
            elif not (x+1,y+1) in mapping:
                x += 1
                y += 1
            else:
                mapping[(x,y)] = "o"
                return True

def run(lines):
    mapping, start, lowest = parse(lines)
    more_sand = True
    total_sand = 0
    while more_sand:
        more_sand = newSand(mapping, start, lowest)
        if more_sand:
            total_sand += 1
    return total_sand

def newSand2(mapping, start, lowest):
    x, y = start
    while True:
        if y+1 == lowest:
            mapping[(x,y)] = "o"
            return True
        elif not (x,y+1) in mapping:
            y += 1
        elif not (x-1,y+1) in mapping:
            x -= 1
            y += 1
        elif not (x+1,y+1) in mapping:
            x += 1
            y += 1
        else:
            mapping[(x,y)] = "o"
            return (x,y) != start

def run2(lines):
    mapping, start, lowest = parse(lines)
    more_sand = True
    total_sand = 0
    while more_sand:
        more_sand = newSand2(mapping, start, lowest + 2)
        total_sand += 1
    return total_sand

with open('./input.txt') as f:
    lines = f.readlines()

#print(run(lines))

print(run2(lines))