def run(lines):
    line = lines[0]
    prev = []
    marker = 0
    for i in range(len(line)):
        if len(prev) < 4:
            prev.append(line[i])
        else:
            dup = False
            for j in prev:
                if prev.count(j) > 1:
                    dup = True
                    prev.append(line[i])
                    prev.pop(0)
                    break
            if not dup:
                marker = i
                break
    return marker

def run2(lines):
    line = lines[0]
    prev = []
    marker = 0
    for i in range(len(line)):
        if len(prev) < 14:
            prev.append(line[i])
        else:
            dup = False
            for j in prev:
                if prev.count(j) > 1:
                    dup = True
                    prev.append(line[i])
                    prev.pop(0)
                    break
            if not dup:
                marker = i
                break
    return marker

with open('./input.txt') as f:
    lines = f.readlines()

#print(run(lines))

print(run2(lines))