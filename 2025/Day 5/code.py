def parse(lines):
    fresh_indices = []
    avail_indices = []
    ranges = True
    for line in lines:
        if line == "\n":
            ranges = False
            continue
        if ranges:
            fresh_indices.append(tuple([int(i) for i in line.strip().split('-')]))
        else:
            avail_indices.append(int(line.strip()))
    return (fresh_indices, avail_indices)

def run(inp):
    fresh, avail = parse(inp)
    count = 0
    for i in avail:
        for j in fresh:
            if j[0] <= i <= j[1]:
                count += 1
                break
    print(count)

def run2(inp):
    fresh, _ = parse(inp)
    overlaps = [[(fresh[i][0], fresh[i][1], (i,)) for i in range(len(fresh))]]
    fresh = [(fresh[i][0], fresh[i][1], i) for i in range(len(fresh))]
    depth = 0
    while True:
        print(f"Completed {depth} layers of overlaps.",
              f"Now {len(overlaps[-1])} items in latest layer.")
        overlaps.append([])
        checked = []
        for i in range(len(overlaps[-2])):
            for j in range(len(fresh)):
                if set(overlaps[-2][i][2] + (fresh[j][2],)) in checked:
                    continue
                else:
                    checked.append(set(overlaps[-2][i][2] + (fresh[j][2],)))
                if fresh[j][2] in overlaps[-2][i][2]:
                    continue
                if overlaps[-2][i][1] < fresh[j][0]:
                    continue
                elif overlaps[-2][i][0] > fresh[j][1]:
                    continue
                elif overlaps[-2][i][0] <= fresh[j][0] and \
                        fresh[j][1] <= overlaps[-2][i][1]:
                    overlaps[-1].append((fresh[j][0], fresh[j][1],
                                         overlaps[-2][i][2] + (fresh[j][2],)))
                elif fresh[j][0] <= overlaps[-2][i][0] and \
                        overlaps[-2][i][1] <= fresh[j][1]:
                    overlaps[-1].append((overlaps[-2][i][0],
                                         overlaps[-2][i][1],
                                         overlaps[-2][i][2] + (fresh[j][2],)))
                elif overlaps[-2][i][0] <= fresh[j][0] and \
                        overlaps[-2][i][1] <= fresh[j][1]:
                    overlaps[-1].append((fresh[j][0], overlaps[-2][i][1],
                                         overlaps[-2][i][2] + (fresh[j][2],)))
                elif fresh[j][0] <= overlaps[-2][i][0] and \
                        fresh[j][1] <= overlaps[-2][i][1]:
                    overlaps[-1].append((overlaps[-2][i][0], fresh[j][1],
                                         overlaps[-2][i][2] + (fresh[j][2],)))
        depth += 1
        if len(overlaps[-1]) == 0:
            break
    count = 0
    sign = 1
    for i in overlaps:
        for j in i:
            count += sign * (j[1] - (j[0] - 1))
        sign *= -1
    print(count)

with open('./input.txt') as f:
    lines = f.readlines()

run2(lines)
