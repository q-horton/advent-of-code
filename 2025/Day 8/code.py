def parse(lines):
    result = []
    for line in lines:
        result.append(tuple([int(i) for i in line.strip().split(',')]))
    return result

def get_distances(coords):
    dists = []
    for i in range(len(coords)):
        a = coords[i]
        for j in range(i + 1, len(coords)):
            b = coords[j]
            dist = ((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2 + (a[2] - b[2]) ** 2) ** 0.5
            dists.append((dist, i, j))
    dists.sort()
    return dists

def run(inp):
    coords = parse(inp)
    dists = get_distances(coords)
    circuits = []
    for i in range(1000):
        index = -1
        for j in range(len(circuits)):
            if dists[i][1] in circuits[j] or dists[i][2] in circuits[j]:
                if index >= 0:
                    circuits[index].update(circuits[j])
                    circuits.pop(j)
                    break
                else:
                    index = j
        else:
            if index >= 0:
                circuits[index].update({dists[i][1], dists[i][2]})
            else:
                circuits.append({dists[i][1], dists[i][2]})
    sizes = []
    for i in circuits:
        sizes.append(len(i))
    sizes += [1] * (len(coords) - sum(sizes))
    sizes.sort()
    result = 1
    for i in range(3):
        result *= sizes[-(i+1)]
    print(result)

def run2(inp):
    coords = parse(inp)
    dists = get_distances(coords)
    circuits = []
    i = 0
    while True:
        index = -1
        for j in range(len(circuits)):
            if dists[i][1] in circuits[j] or dists[i][2] in circuits[j]:
                if index >= 0:
                    circuits[index].update(circuits[j])
                    circuits.pop(j)
                    break
                else:
                    index = j
        else:
            if index >= 0:
                circuits[index].update({dists[i][1], dists[i][2]})
            else:
                circuits.append({dists[i][1], dists[i][2]})
        if len(circuits) == 1 and len(circuits[0]) == len(coords):
            break
        i += 1
    x1 = coords[dists[i][1]][0]
    x2 = coords[dists[i][2]][0]
    print(x1 * x2)

with open('./input.txt') as f:
    lines = f.readlines()

run2(lines)
