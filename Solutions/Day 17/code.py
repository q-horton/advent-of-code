rocks = [
    [["#", "#", "#", "#"]],
    [["", "#", ""], ["#", "#", "#"], ["", "#", ""]],
    [["#", "#", "#"], ["", "", "#"], ["", "", "#"]],
    [["#"], ["#"], ["#"], ["#"]],
    [["#", "#"], ["#", "#"]]
]

def parse(lines):
    gusts = []
    for line in lines:
        line = line.strip()
        for move in line:
            if move == "<":
                gusts.append(-1)
            elif move == ">":
                gusts.append(1)
    return gusts

def checkVacant(cave_map, rock, coord):
    for y in range(len(rock)):
        for x in range(len(rock[y])):
            if len(cave_map) > y + coord[1]:
                if cave_map[y + coord[1]][x + coord[0]] != "" and rock[y][x] != "":
                    return False
    return True

def run(lines):
    gusts = parse(lines)
    cave_map = []
    current_gust = 0
    for rock_count in range(2022):
        coord = [2, len(cave_map) + 3]
        rock = rocks[rock_count % len(rocks)]
        while True:
            if coord[0] + gusts[current_gust] >= 0 and coord[0] + len(rock[0]) + gusts[current_gust] <= 7:
                if checkVacant(cave_map, rock, (coord[0] + gusts[current_gust], coord[1])):
                    coord[0] += gusts[current_gust]
            current_gust = (current_gust + 1) % len(gusts)
            if coord[1] > 0 and checkVacant(cave_map, rock, (coord[0], coord[1] - 1)):
                coord[1] -= 1
            else:
                break
        if len(cave_map) < coord[1] + len(rock):
            for i in range(coord[1] + len(rock) - len(cave_map)):
                cave_map.append([""] * 7)
        for y in range(len(rock)):
            for x in range(len(rock[y])):
                if rock[y][x] != "":
                    cave_map[coord[1] + y][coord[0] + x] = rock[y][x]
    return len(cave_map)

def checkCycle(cave_map, min_length):
    for a in range(min_length,len(cave_map) // 2):
        if cave_map[-a:] == cave_map[-2*a:-a]:
            return (True, len(cave_map), cave_map[-a:])
    return (False, 0, [])

def run2(lines, total, min_length, start_checking):
    gusts = parse(lines)
    cave_map = []
    current_gust = 0
    cycle_found = False
    cycle_start = 0
    cycle_period = [0, 0]
    cycle = []
    cycle_heights = []
    for rock_count in range(total):
        coord = [2, len(cave_map) + 3]
        rock = rocks[rock_count % len(rocks)]
        while True:
            if coord[0] + gusts[current_gust] >= 0 and coord[0] + len(rock[0]) + gusts[current_gust] <= 7:
                if checkVacant(cave_map, rock, (coord[0] + gusts[current_gust], coord[1])):
                    coord[0] += gusts[current_gust]
            current_gust = (current_gust + 1) % len(gusts)
            if coord[1] > 0 and checkVacant(cave_map, rock, (coord[0], coord[1] - 1)):
                coord[1] -= 1
            else:
                break
        if len(cave_map) < coord[1] + len(rock):
            for i in range(coord[1] + len(rock) - len(cave_map)):
                cave_map.append([""] * 7)
        for y in range(len(rock)):
            for x in range(len(rock[y])):
                if rock[y][x] != "":
                    cave_map[coord[1] + y][coord[0] + x] = rock[y][x]
        if not cycle_found and rock_count > start_checking:
            check_cycle = checkCycle(cave_map, min_length)
            if check_cycle[0]:
                cycle_found, cycle_start, cycle = check_cycle
                cycle_period[0] = rock_count
        elif cycle_found:
            if cave_map[-len(cycle):] == cycle:
                cycle_period[1] = rock_count
                break
            elif len(cave_map) - cycle_start > len(cycle):
                cycle_found = False
            else:
                cycle_heights.append(len(cave_map[cycle_start:]) - 1)
    r = (total - cycle_period[0]) % (cycle_period[1] - cycle_period[0])
    num_cycles = (total - cycle_period[0]) // (cycle_period[1] - cycle_period[0])
    return len(cycle) * num_cycles + cycle_start + cycle_heights[r - 1]

with open('./input.txt') as f:
    lines = f.readlines()

#print(run(lines))

print(run2(lines, 1000000000000, 100, 10000))