import sympy

def parse(lines):
    monkeys = {}
    for line in lines:
        line = line.strip().split()
        if len(line) == 4:
            value = line[1:]
        elif len(line) == 2:
            value = int(line[1])
        monkeys[line[0][:-1]] = value
    return monkeys

def evaluate(monkeys):
    while isinstance(monkeys["root"], list):
        for (monkey, job) in monkeys.items():
            if isinstance(job, list):
                if isinstance(monkeys[job[0]], int) and isinstance(monkeys[job[2]], int):
                    monkeys[monkey] = int(eval(str(monkeys[job[0]]) + job[1] + str(monkeys[job[2]])))
    return monkeys

def run(lines):
    monkeys = parse(lines)
    monkey_vals = evaluate(monkeys)
    return monkey_vals["root"]

def evaluate2(monkeys):
    while isinstance(monkeys[monkeys["root"][0]], list) or isinstance(monkeys[monkeys["root"][2]], list):
        for (monkey, job) in monkeys.items():
            if isinstance(job, list) and monkey != "root":
                if not (isinstance(monkeys[job[0]], list) or isinstance(monkeys[job[2]], list)):
                    if isinstance(monkeys[job[0]], sympy.Expr) or isinstance(monkeys[job[2]], sympy.Expr):
                        e1 = "(" + str(monkeys[job[0]]) + ")"
                        e2 = "(" + str(monkeys[job[2]]) + ")"
                        monkeys[monkey] = sympy.sympify(e1 + job[1] + e2)
                    elif isinstance(monkeys[job[0]], int) and isinstance(monkeys[job[2]], int):
                        monkeys[monkey] = int(eval(str(monkeys[job[0]]) + job[1] + str(monkeys[job[2]])))
    return sympy.solve(sympy.Eq(monkeys[monkeys["root"][0]], monkeys[monkeys["root"][2]]))

def run2(lines):
    monkeys = parse(lines)
    monkeys["humn"] = sympy.sympify("x")
    return evaluate2(monkeys)[0]

with open('./input.txt') as f:
    lines = f.readlines()

#print(run(lines))

print(run2(lines))