def parse(lines):
    pairs = [[]]
    for line in lines:
        if line[-1] == "\n":
            line = line[:-1]
        if line == "":
            pairs.append([])
        else:
            pairs[-1].append(eval(line))
    return pairs

def compare(left, right):
    if isinstance(left, int) and isinstance(right, int):
        return (left != right, left < right)
    elif isinstance(left, list) and isinstance(right, list):
        for i in range(min(len(left), len(right))):
            comparable, comparison = compare(left[i], right[i])
            if comparable:
                return (True, comparison)
        return (len(left) != len(right), len(left) < len(right))
    elif isinstance(left, int) and isinstance(right, list):
        return compare([left], right)
    elif isinstance(left, list) and isinstance(right, int):
        return compare(left, [right])
    else:
        return (False, False)

def run(lines):
    pairs = parse(lines)
    sum_correct = 0
    for i in range(len(pairs)):
        pair = pairs[i]
        _, comparison = compare(pair[0], pair[1])
        if comparison:
            sum_correct += i + 1
    return sum_correct

def run2(lines):
    pairs = parse(lines)
    all_packets = [[[2]], [[6]]]
    for i in pairs:
        all_packets.append(i[0])
        all_packets.append(i[1])
    indices = [1, 1]
    for i in all_packets:
        if compare(i, [[2]])[1]:
            indices[0] += 1
        if compare(i, [[6]])[1]:
            indices[1] += 1
    return indices[0] * indices[1]

with open('./input.txt') as f:
    lines = f.readlines()

#print(run(lines))

print(run2(lines))