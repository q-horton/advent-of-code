def parse(lines):
    rates = {}
    connections = {}
    for line in lines:
        words = line.strip().split()
        valve = words[1]
        rate = int(words[4][5:-1])
        connected = words[9:]
        for i in range(len(connected)):
            if connected[i][-1] == ",":
                connected[i] = connected[i][:-1]
        rates[valve] = rate
        connections[valve] = connected
    return (rates, connections)

def getProdValves(rates):
    valves = []
    for i in rates:
        if rates[i] > 0:
            valves.append(i)
    return valves

def getDist(connections, searched, p2):
    while True:
        newest_depth = []
        for i in searched[-1]:
            if p2 in connections[i]:
                return len(searched)
            else:
                newest_depth.extend(connections[i])
        searched.append(newest_depth)

def productivePaths(rates, connections):
    prod_paths = {}
    prod_valves = getProdValves(rates)
    for valve in rates:
        prod_paths[valve] = []
        for i in prod_valves:
            dist = getDist(connections, [[valve]], i)
            prod_paths[valve].append((i, dist + 1, rates[i]))
    return prod_paths

def getNextPath(prod_paths, curr_path, time_left, curr_total_pressure):
    if time_left <= 1:
        return (curr_total_pressure, curr_path)
    options = []
    for i in prod_paths[curr_path[-1]]:
        valve, time, pressure_rate = i
        if (not valve in curr_path) and (time_left - time > 0):
            options.append(getNextPath(prod_paths, curr_path + [valve], time_left - time, curr_total_pressure + pressure_rate * (time_left - time)))
        else:
            options.append((curr_total_pressure, curr_path))
    return max(options)

def run(lines):
    rates, connections = parse(lines)
    prod_paths = productivePaths(rates, connections)
    if rates["AA"] > 0:
        p1 = getNextPath(prod_paths, ["AA"], 29, rates["AA"]*29)
        p2 = getNextPath(prod_paths, ["AA"], 30, 0)
        score, _ = max(p1, p2)
    else:
        score, _ = getNextPath(prod_paths, ["AA"], 30, 0)
    return score

def getNextPaths(prod_paths, curr_paths, time_left, curr_total_pressure):
    if time_left[0] <= 1 and time_left[1] <= 1:
        return (curr_total_pressure, curr_paths)
    options = []
    path1, path2 = curr_paths
    time1, time2 = time_left
    if time1 >= time2:
        for i in prod_paths[path1[-1]]:
            valve, time, pressure_rate = i
            if (not valve in path1) and (not valve in path2) and (time1 - time > 0):
                options.append(getNextPaths(prod_paths, (path1 + [valve], path2), (time1 - time, time2), curr_total_pressure + pressure_rate * (time1 - time)))
            else:
                options.append((curr_total_pressure, curr_paths))
    else:
        for i in prod_paths[path2[-1]]:
            valve, time, pressure_rate = i
            if (not valve in path1) and (not valve in path2) and (time2 - time > 0):
                options.append(getNextPaths(prod_paths, (path1, path2 + [valve]), (time1, time2 - time), curr_total_pressure + pressure_rate * (time2 - time)))
            else:
                options.append((curr_total_pressure, curr_paths))
    return max(options)

def run2(lines):
    rates, connections = parse(lines)
    prod_paths = productivePaths(rates, connections)
    if rates["AA"] > 0:
        p1 = getNextPaths(prod_paths, [["AA"],["AA"]], [26,25], rates["AA"]*25)
        p2 = getNextPaths(prod_paths, [["AA"],["AA"]], [26,26], 0)
        score, path = max(p1, p2)
    else:
        score, path = getNextPaths(prod_paths, [["AA"],["AA"]], [26,26], 0)
    return score

with open('./input.txt') as f:
    lines = f.readlines()

#print(run(lines))

print(run2(lines))