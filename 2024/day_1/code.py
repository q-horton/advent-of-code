def parse(lines):
    left = []
    right = []
    for line in lines:
        vals = line.split()
        left += [int(vals[0])]
        right += [int(vals[1])]
    return (left, right)

def run(inp):
    left, right = parse(inp)
    left.sort()
    right.sort()
    total = 0
    for i in range(len(left)):
        total += abs(left[i] - right[i])
    print(total)

def run2(inp):
    left, right = parse(inp)
    max_left = max(left)
    lookup = {}
    for i in range(max_left + 1):
        for j in right:
            if i == j:
                if i in lookup:
                    lookup[i] += 1
                else:
                    lookup[i] = 1
    similarity = 0
    for i in left:
        if i in lookup:
            similarity += i * lookup[i]
    print(similarity)

with open('./input.txt') as f:
    lines = f.readlines()

run2(lines)
