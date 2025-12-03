def parse(lines):
    arr = []
    for line in lines:
        arr_line = [int(i) for i in line.strip()]
        arr.append(arr_line)
    return arr

def run(inp):
    banks = parse(inp)
    total = 0
    for bank in banks:
        max = 0
        for i in range(len(bank) - 1):
            for j in range(i + 1, len(bank)):
                if bank[i] * 10 + bank[j] > max:
                    max = bank[i] * 10 + bank[j]
        total += max
    print(total)

def dig_array_to_int(array):
    sum = 0
    for i in range(len(array)):
        sum += array[-(i+1)] * (10 ** i)
    return sum

def run2(inp):
    banks = parse(inp)
    total = 0
    id = 0
    for bank in banks:
        new_bank = []
        index = 0
        sweeping = False
        while True:
            if index == len(bank):
                break
            elif len(bank) - index <= 12 - len(new_bank):
                sweeping = True
            if sweeping:
                new_bank.append(bank[index])
                index += 1
                continue
            start = 0
            if len(bank) - index <= 12:
                start = 12 - (len(bank) - index)
            for i in range(start, len(new_bank)):
                if bank[index] > new_bank[i]:
                    new_bank[i] = bank[index]
                    new_bank = new_bank[:i+1]
                    break
            else:
                if len(new_bank) < 12:
                    new_bank.append(bank[index])
            index += 1
        max_val = dig_array_to_int(new_bank)
        id += 1
        total += max_val
    print(total)

with open('./input.txt') as f:
    lines = f.readlines()

run2(lines)
