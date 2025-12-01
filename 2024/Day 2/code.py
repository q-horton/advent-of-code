def parse(lines):
    result = []
    for line in lines:
        var = [int(i) for i in line.split()]
        result.append(var)
    return result

def run(inp):
    reports = parse(inp)
    num_safe = 0
    for rep in reports:
        diff = rep[0] - rep[1]
        if diff == 0:
            continue
        dir = diff / abs(diff)
        safe = True
        for i in range(len(rep) - 1):
            diff = rep[i] - rep[i + 1]
            if not (1 <= abs(diff) <= 3):
                safe = False
                break
            if diff / abs(diff) != dir:
                safe = False
                break
        if safe:
            num_safe += 1
    print(num_safe)

def check_safe(rep):
    diff = rep[0] - rep[1]
    if diff == 0:
        return False
    dir = diff / abs(diff)
    for i in range(len(rep) - 1):
        diff = rep[i] - rep[i + 1]
        if not (1 <= abs(diff) <= 3):
            return False
        if diff / abs(diff) != dir:
            return False
    return True

def run2(inp):
    reports = parse(inp)
    num_safe = 0
    for rep in reports:
        if check_safe(rep):
            num_safe += 1
        else:
            for i in range(len(rep)):
                if check_safe(rep[:i] + rep[i + 1:]):
                    num_safe += 1
                    break
    print(num_safe)

with open('./input.txt') as f:
    lines = f.readlines()

run2(lines)
