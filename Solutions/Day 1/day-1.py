def process(items):
    elves = [0]
    for i in items:
        if i[:-1]:
            elves[-1] += int(i[:-1])
        else:
            elves.append(0)
    return elves

def run(inp):
    print(max(process(inp)))

def run2(inp):
    processed = process(inp)
    top = max(processed)
    processed.remove(top)
    second = max(processed)
    processed.remove(second)
    third = max(processed)
    print(top + second + third)

with open('input.txt') as f:
    lines = f.readlines()

run2(lines)
