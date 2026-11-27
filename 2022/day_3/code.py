def getPriority(line):
    mid = int(len(line) / 2)
    compartmentOne = line[:mid]
    compartmentTwo = line[mid:]
    duplicate = ""
    for i in compartmentOne:
        if i in compartmentTwo:
            duplicate = i
            break
    value = 0
    if duplicate.isupper():
        value = ord(duplicate) - 64 + 26
    elif duplicate.islower():
        value = ord(duplicate) - 96
    return value

def getPriority2(line1, line2, line3):
    badge = ""
    for i in line1:
        if (i in line2) and (i in line3):
            badge = i
            break
    value = 0
    if badge.isupper():
        value = ord(badge) - 64 + 26
    elif badge.islower():
        value = ord(badge) - 96
    return value

def run(lines):
    sum = 0
    for i in lines:
        sum += getPriority(i)
    return sum

def run2(lines):
    sum = 0
    for i in range(int(len(lines)/3)):
        sum += getPriority2(lines[3*i],lines[3*i+1],lines[3*i+2])
    return sum

with open('./input.txt') as f:
    lines = f.readlines()

print(run2(lines))