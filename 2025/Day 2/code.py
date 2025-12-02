def parse(lines):
    ranges = []
    for line in lines:
        x = line.strip().split(',')
        if x[-1] == '':
            x = x[:-1]
        for i in x:
            y = i.split('-')
            ranges.append(tuple([int(j) for j in y]))
    return ranges

def run(inp):
    ranges = parse(inp)
    count = 0
    for i in ranges:
        for j in range(i[0], i[1] + 1):
            string = str(j)
            if string[:len(string)//2] == string[len(string)//2:]:
                count += j
    print(count)

def run2(inp):
    ranges = parse(inp)
    count = 0
    for i in ranges:
        for j in range(i[0], i[1] + 1):
            string = str(j)
            for k in range(1, len(string)//2 + 1):
                if (len(string)/k - len(string)//k) > 0:
                    continue
                passed = False
                for x in range(len(string)//k - 1):
                    if string[x*k:(x+1)*k] != string[(x+1)*k:(x+2)*k]:
                        break
                else:
                    passed = True
                if passed:
                    count += j
                    break
    print(count)

with open('./input.txt') as f:
    lines = f.readlines()

run2(lines)
