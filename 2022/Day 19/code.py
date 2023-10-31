import math

def parse(lines):
    blueprints = []
    for line in lines:
        line = line.strip().split()
        blueprint = []
        blueprint.append((int(line[6]), 0, 0, 0))
        blueprint.append((int(line[12]), 0, 0, 0))
        blueprint.append((int(line[18]), int(line[21]), 0, 0))
        blueprint.append((int(line[27]), 0, int(line[30]), 0))
        blueprints.append(blueprint)
    return blueprints

def addVecs(v1, v2):
    res = list(v1)
    for i in range(len(res)):
        res[i] += v2[i]
    return tuple(res)

def subVecs(v1, v2):
    res = list(v1)
    for i in range(len(res)):
        res[i] -= v2[i]
    return tuple(res)

def multVec(v, s):
    res = list(v)
    for i in range(len(res)):
        res[i] *= s
    return tuple(res)

def balAvail(inv, cost):
    for i in range(len(inv)):
        if inv[i] - cost[i] < 0:
            return False
    return True

def blueprintBest(blueprint, inv, bots, time, curr_best):
    if time == 1:
        return addVecs(inv, bots)[-1]
    elif curr_best > inv[-1] + time * (bots[-1] + (time / 2) * min(1, bots[0] / blueprint[-1][0])):
        return addVecs(inv, bots)[-1]
    elif inv[0] < min(blueprint)[0]:
        new_time = max(time - math.ceil((min(blueprint)[0] - inv[0]) / bots[0]), 1)
        new_bal = addVecs(inv, multVec(bots, time - new_time))
        return blueprintBest(blueprint, new_bal, bots, new_time, curr_best)
    else:
        options = []
        for i in range(-1, -len(blueprint) - 1, -1):
            if balAvail(inv, blueprint[i]):
                new_bal = addVecs(subVecs(inv, blueprint[i]), bots)
                new_bots = list(bots)
                new_bots[i] += 1
                options.append(blueprintBest(blueprint, new_bal, tuple(new_bots), time - 1, max(options + [curr_best])))
            else:
                j = -1
                valid = False
                for k in range(len(inv)):
                    if blueprint[i][k] > 0:
                        if bots[k] > 0:
                            if j == -1 and math.ceil((blueprint[i][k] - inv[k]) / bots[k]) > 0:
                                j = k
                                valid = True
                            if math.ceil((blueprint[i][k] - inv[k]) / bots[k]) > math.ceil((blueprint[i][k] - inv[k]) / bots[k]):
                                j = k
                        else:
                            valid = False
                if valid:
                    new_time = time - math.ceil((blueprint[i][j] - inv[j]) / bots[j])
                    if new_time > 0:
                        new_bal = addVecs(inv, multVec(bots, time - new_time))
                        if new_time > 1 and balAvail(new_bal, blueprint[i]):
                            new_new_bal = addVecs(subVecs(new_bal, blueprint[i]), bots)
                            new_bots = list(bots)
                            new_bots[i] += 1
                            options.append(blueprintBest(blueprint, new_new_bal, tuple(new_bots), new_time - 1, max(options + [curr_best])))
                        else:
                            options.append(blueprintBest(blueprint, new_bal, bots, new_time, max(options + [curr_best])))
        options.append(addVecs(inv, multVec(bots, time))[-1])
        return max(options)

def run(lines):
    blueprints = parse(lines)
    sum_ql = 0
    for i in range(len(blueprints)):
        most_geodes = blueprintBest(blueprints[i], (0, 0, 0, 0), (1, 0, 0, 0), 24, 0)
        sum_ql += (i + 1) * (most_geodes)
    return sum_ql

def run2(lines):
    blueprints = parse(lines)
    mult_geodes = 1
    for i in range(3):
        most_geodes = blueprintBest(blueprints[i], (0, 0, 0, 0), (1, 0, 0, 0), 32, 0)
        mult_geodes *= most_geodes
    return mult_geodes

with open('./input.txt') as f:
    lines = f.readlines()

#print(run(lines))

print(run2(lines))