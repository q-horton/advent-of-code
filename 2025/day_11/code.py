def parse(lines):
    sys_map = {}
    for line in lines:
        breakdown = line.strip().split(':')
        outputs = [i for i in breakdown[1].strip().split()]
        sys_map[breakdown[0].strip()] = outputs
    return sys_map

def paths_from_node(sys_map, node, cache):
    if node == "out":
        return 1, cache
    if node in cache:
        return cache[node], cache
    count = 0
    for next_node in sys_map[node]:
        num_paths, cache = paths_from_node(sys_map, next_node, cache)
        count += num_paths
    cache[node] = count
    return count, cache

def run(inp):
    data = parse(inp)
    cache = {}
    num_paths, cache = paths_from_node(data, "you", cache)
    print(num_paths)

def paths_from_node2(sys_map, node, cache):
    if node == "out":
        return ((1, 0), cache)
    if node in cache:
        return (cache[node], cache)
    new_status = 0
    if node == "fft":
        new_status |= 1
    elif node == "dac":
        new_status |= 2
    count = 0
    max_status = 0
    for next_node in sys_map[node]:
        response, cache = paths_from_node2(sys_map, next_node, cache)
        num_paths, sub_status = response
        if sub_status > max_status:
            max_status = sub_status
            count = num_paths
        elif sub_status == max_status:
            count += num_paths
    status = max_status | new_status
    cache[node] = (count, status)
    return ((count, status), cache)

def run2(inp):
    data = parse(inp)
    cache = {}
    response, cache = paths_from_node2(data, "svr", cache)
    num_paths, status = response
    print(num_paths)

with open('./input.txt') as f:
    lines = f.readlines()

run2(lines)
