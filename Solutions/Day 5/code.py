def parse(lines):
    instr = False
    stacks = []
    instructions = []
    for i in lines:
        if i[-1] == "\n":
            i = i[:-1]
        if instr:
            instruction = i.split()
            instructions.append((int(instruction[1]),int(instruction[3]),int(instruction[5])))
        elif not i:
            instr = True
        else:
            load = [i[j:j+3] for j in range(0, len(i), 4)]
            if stacks == []:
                for j in range(len(load)):
                    stacks.append([])
            for j in range(len(load)):
                stacks[j].append(load[j])
    cleaned = cleanStacks(stacks)
    return (instructions, cleaned)

def cleanStacks(stacks):
    new_stacks = []
    for i in stacks:
        i.pop()
        i.reverse()
        length = len(i)
        for j in range(1,length):
            if i[-1] == "   ":
                i.pop()
        new_stacks.append(i)
    return new_stacks
    

def run(lines):
    (instr, stacks) = parse(lines)
    for i in instr:
        for j in range(i[0]):
            move = stacks[i[1]-1].pop()
            stacks[i[2]-1].append(move)
    result = ""
    for i in stacks:
        result += i.pop()[1]
    return result

def run2(lines):
    (instr, stacks) = parse(lines)
    for i in instr:
        stacks[i[2]-1].extend(stacks[i[1]-1][-i[0]:])
        for j in range(i[0]):
            stacks[i[1]-1].pop()
    result = ""
    for i in stacks:
        result += i.pop()[1]
    return result

with open('./input.txt') as f:
    lines = f.readlines()

#print(run(lines))

print(run2(lines))