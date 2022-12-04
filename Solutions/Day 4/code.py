def parse_list(line):
    sections = line.split(",")
    sec1 = sections[0].split("-")
    sec2 = sections[1].split("-")
    return [int(sec1[0]),int(sec1[1]),int(sec2[0]),int(sec2[1])]

def isIncluded(line):
    parsed = parse_list(line)
    if parsed[0] < parsed[2]:
        return parsed[1] >= parsed[3]
    elif parsed[0] == parsed[2]:
        return True
    else:
        return parsed[1] <= parsed[3]

def isOverlap(line):
    parsed = parse_list(line)
    if parsed[0] < parsed[2]:
        return parsed[1] >= parsed[2]
    elif parsed[0] == parsed[2]:
        return True
    else:
        return parsed[3] >= parsed[0]

def run(lines):
    count = 0
    for i in lines:
        if isIncluded(i):
            count += 1
    return count

def run2(lines):
    count = 0
    for i in lines:
        if isOverlap(i):
            count += 1
    return count

with open('./input.txt') as f:
    lines = f.readlines()

#print(run(lines))

print(run2(lines))