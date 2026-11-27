def parse(lines):
    cycles = []
    for i in lines:
        if i[-1] == "\n":
            i = i[:-1]
        if i == "noop":
            cycles.append(0)
        elif i[:4] == "addx":
            cycles.extend([0, int(i[5:])])
    return cycles

def run(lines):
    cycles = parse(lines)
    strengths = []
    X = 1
    for i in range(1, len(cycles) + 1):
        if i % 40 == 20:
            strengths.append(i * X)
        X += cycles[i - 1]
    return sum(strengths)

def display(cycles):
    disp = [[]]
    X = 1
    for i in range(len(cycles)):
        pos = i % 40
        if pos < len(disp[-1]):
            disp.append([])
        if abs(pos - X) <= 1:
            disp[-1].append("#")
        else:
            disp[-1].append(".")
        X += cycles[i]
    return disp

def run2(lines):
    cycles = parse(lines)
    disp = display(cycles)
    output = ""
    for i in disp:
        for j in i:
            output += j
        output += "\n"
    return output[:-1]

with open('./input.txt') as f:
    lines = f.readlines()

#print(run(lines))

print(run2(lines))