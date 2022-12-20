def parse(lines):
    message = []
    for line in lines:
        message.append(int(line.strip()))
    return message

def rearrange(message, count):
    indices = [i for i in range(len(message))]
    for _ in range(count):
        for i in range(len(indices)):
            old_index = indices[i]
            move = message[i] % (len(message) - 1)
            if move == 0:
                continue
            elif indices[i] + move >= len(message):
                new_index = (indices[i] + move + 1) % len(message)
            elif indices[i] + move <= 0:
                new_index = (indices[i] + move - 1) % len(message)
            else:
                new_index = indices[i] + move
            if old_index > new_index:
                for j in range(len(indices)):
                    if indices[j] >= new_index and indices[j] < old_index:
                        indices[j] += 1
            elif old_index < new_index:
                for j in range(len(indices)):
                    if indices[j] <= new_index and indices[j] > old_index:
                        indices[j] -= 1
            indices[i] = new_index
    new_message = [None] * len(message)
    for i in range(len(indices)):
        new_message[indices[i]] = message[i]
    return new_message

def run(lines):
    message = parse(lines)
    decoded_msg = rearrange(message, 1)
    grove_coords = []
    zero_in = decoded_msg.index(0)
    for i in (1000, 2000, 3000):
        grove_coords.append(decoded_msg[(zero_in + i) % len(decoded_msg)])
    return sum(grove_coords)

def run2(lines):
    message = parse(lines)
    key = 811589153
    for i in range(len(message)):
        message[i] *= key
    decoded_msg = rearrange(message, 10)
    grove_coords = []
    zero_in = decoded_msg.index(0)
    for i in (1000, 2000, 3000):
        grove_coords.append(decoded_msg[(zero_in + i) % len(decoded_msg)])
    return sum(grove_coords)

with open('./input.txt') as f:
    lines = f.readlines()

#print(run(lines))

print(run2(lines))