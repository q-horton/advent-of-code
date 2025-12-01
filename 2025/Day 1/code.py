def parse(lines):
    instructions = []
    for line in lines:
        if line[0] == 'L':
            instructions.append(-1 * int(line[1:]))
        else:
            instructions.append(int(line[1:]))
    return instructions

def run(inp):
    instr = parse(inp)
    count = 0
    curr_state = 50
    for i in instr:
        curr_state = (curr_state + i) % 100
        if curr_state == 0:
            count += 1
    print(count)

def run2(inp):
    instr = parse(inp)
    count = 0
    curr_state = 50
    for i in instr:
        count += abs(i) // 100
        rem = int((abs(i) - (abs(i) // 100) * 100) * i / abs(i))
        if (rem < 0) and (curr_state == 0):
            curr_state = 100
        if (rem != 0) and not (0 < curr_state + rem < 100):
            count += 1
#        print(f"Orig: {curr_state} \tInstr: {i} \tNext: {(curr_state + rem) % 100} \tCount: {count}")
        curr_state = (curr_state + rem) % 100
    print(count)

with open('./input.txt') as f:
    lines = f.readlines()

run2(lines)
