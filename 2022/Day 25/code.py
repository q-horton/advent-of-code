import math

def snafuConv(num):
    val = 0
    order = len(num) - 1
    for i in range(len(num)):
        if num[i] == "2":
            val += 2 * (5 ** (order - i))
        elif num[i] == "1":
            val += 5 ** (order - i)
        elif num[i] == "-":
            val -= 5 ** (order - i)
        elif num[i] == "=":
            val -= 2 * (5 ** (order - i))
    return val

def decConv(num):
    if num == -2:
        return "="
    elif num == -1:
        return "-"
    elif num == 0:
        return "0"
    elif num == 1:
        return "1"
    elif num == 2:
        return "2"
    else:
        snafu = ""
        sym_val = math.floor(math.log(2*abs(num), 5))
        curr = round(num / (5 ** sym_val))
        if curr == -2:
            snafu += "="
        elif curr == -1:
            snafu += "-"
        elif curr == 1:
            snafu += "1"
        elif curr == 2:
            snafu += "2"
        lower = decConv(num - curr * (5 ** sym_val))
        return snafu + "0" * (sym_val - len(lower)) + lower

def run(lines):
    vals = []
    for line in lines:
        line = line.strip()
        vals.append(snafuConv(line))
    return decConv(sum(vals))

with open('./input.txt') as f:
    lines = f.readlines()

print(run(lines))