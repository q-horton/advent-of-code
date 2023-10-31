def parse(lines):
    monkeys = []
    info = {}
    for line in lines:
        if line[-1] == "\n":
            line = line[:-1]
        if line[2:17] == "Starting items:":
            items = line[18:].split(", ")
            nums = []
            for i in items:
                nums.append(int(i))
            info["items"] = nums
        elif line[2:12] == "Operation:":
            info["op"] = line[19:]
        elif line[2:7] == "Test:":
            info["test"] = int(line[21:])
        elif line[4:12] == "If true:":
            info["true"] = int(line[29:])
        elif line[4:13] == "If false:":
            info["false"] = int(line[30:])
            info["inspect"] = 0
            monkeys.append(info)
        elif line == "":
            info = {}
    return monkeys

def inspect(monkeys, me):
    old = monkeys[me]["items"].pop(0)
    new = int(eval(monkeys[me]["op"]))
    new = new // 3
    if new % monkeys[me]["test"] == 0:
        monkeys[monkeys[me]["true"]]["items"].extend([new])
    else:
        monkeys[monkeys[me]["false"]]["items"].extend([new])
    monkeys[me]["inspect"] += 1

def inspectAll(monkeys, me):
    total_items = len(monkeys[me]["items"])
    for i in range(total_items):
        inspect(monkeys, me)

def run(lines):
    monkeys = parse(lines)
    for i in range(20):
        for monkey in range(len(monkeys)):
            inspectAll(monkeys, monkey)
    inspects = []
    for monkey in monkeys:
        inspects.append(monkey["inspect"])
    inspects.sort()
    return inspects[-1] * inspects[-2]

def inspect2(monkeys, me, mod):
    old = monkeys[me]["items"].pop(0)
    new = int(eval(monkeys[me]["op"])) % mod
    if new % monkeys[me]["test"] == 0:
        monkeys[monkeys[me]["true"]]["items"].extend([new])
    else:
        monkeys[monkeys[me]["false"]]["items"].extend([new])
    monkeys[me]["inspect"] += 1

def inspectAll2(monkeys, me, mod):
    total_items = len(monkeys[me]["items"])
    for i in range(total_items):
        inspect2(monkeys, me, mod)

def run2(lines):
    monkeys = parse(lines)
    mod = 1
    for monkey in monkeys:
        mod *= monkey["test"]
    for i in range(10000):
        for monkey in range(len(monkeys)):
            inspectAll2(monkeys, monkey, mod)
    inspects = []
    for monkey in monkeys:
        inspects.append(monkey["inspect"])
    inspects.sort()
    return inspects[-1] * inspects[-2]

with open('./input.txt') as f:
    lines = f.readlines()

#print(run(lines))

print(run2(lines))