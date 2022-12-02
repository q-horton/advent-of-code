def parse_line(line):
    values = line.split()
    them = 0
    you = 0
    if values[0] == 'A':
        them = 1
    elif values[0] == 'B':
        them = 2
    elif values[0] == 'C':
        them = 3
    
    if values[1] == 'X':
        you = 1
    elif values[1] == 'Y':
        you = 2
    elif values[1] == 'Z':
        you = 3
    
    return (them, you)

def evaluate1(line):
    input = parse_line(line)
    output = input[1]
    if input[1] == 1 and input[0] == 3:
        output += 6
    elif input[1] == 2 and input[0] == 1:
        output += 6
    elif input[1] == 3 and input[0] == 2:
        output += 6
    elif input[1] == input[0]:
        output += 3
    
    return output

def evaluate2(line):
    input = parse_line(line)
    you = 0
    them = input[0]
    win_points = 0
    if input[1] == 1:
        you = (them - 1) % 3
        if you == 0:
            you = 3
    elif input[1] == 2:
        you = them
        win_points = 3
    elif input[1] == 3:
        you = (them + 1) % 3
        if you == 0:
            you = 3
        win_points = 6
    return you + win_points

def evaluations1(lines):
    results = []
    for i in lines:
        results.append(evaluate1(i))
    return results

def run(lines):
    return sum(evaluations1(lines))

def evaluations2(lines):
    results = []
    for i in lines:
        results.append(evaluate2(i))
    return results

def run2(lines):
    return sum(evaluations2(lines))

with open('./input.txt') as f:
    lines = f.readlines()

print(run2(lines))