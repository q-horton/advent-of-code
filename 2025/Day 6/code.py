def parse(lines):
    result = []
    for i in lines[-1].strip().split(' '):
        if i == '':
            continue
        result.append((i, []))
    for line in lines[:-1]:
        vals = line.strip().split(' ')
        offset = 0
        for i in range(len(result)):
            while vals[i + offset] == '':
                offset += 1
            result[i][1].append(int(vals[i + offset]))
    return result

def calc(data):
    total = 0
    for eqn in data:
        if eqn[0] == '+':
            result = 0
            for i in eqn[1]:
                result += i
        elif eqn[0] == '*':
            result = 1
            for i in eqn[1]:
                result *= i
        total += result
    return total

def run(inp):
    data = parse(inp)
    total = calc(data)
    print(total)

def parse2(lines):
    result = []
    max_line_len = 0
    lines = [(line[:-1] if line[-1] == '\n' else line) for line in lines]
    for i in lines:
        if len(i) > max_line_len:
            max_line_len = len(i)
    temp = []
    for i in range(max_line_len, -1, -1):
        temp.append("")
        for j in range(len(lines) - 1):
            if len(lines[j]) <= i:
                temp[-1] += ' '
            else:
                temp[-1] += lines[j][i]
        if len(lines[-1]) > i and lines[-1][i] != ' ':
            if temp[0] == ' '*len(lines[:-1]):
                temp = temp[1:]
            result.append((lines[-1][i], [int(j) for j in temp]))
            i -= 1
            temp = []
    return result

def run2(inp):
    data = parse2(inp)
    total = calc(data)
    print(total)

with open('./input.txt') as f:
    lines = f.readlines()

run2(lines)
